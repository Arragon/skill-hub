#!/usr/bin/env python3
"""Generate only the marked README skill table from catalog.json."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

START = '<!-- skill-table:start -->'
END = '<!-- skill-table:end -->'


def render(entries):
    local = sum(e['kind'] == 'local' for e in entries)
    pending = sum(e['status'] == 'reference-only' for e in entries)
    upstream = len(entries) - local - pending
    lines = [f'共 **{len(entries)}** 个条目：**{local}** 个本地技能、**{upstream}** 个外部引用、**{pending}** 个仅供参考条目。', '',
             '点击调用名称可查看技能正文或来源项目。外部引用需要读取登记的上游版本；仅供参考条目暂不能通过本库加载执行。实际执行还取决于当前 Agent 的工具和授权。', '']
    groups = {}
    for e in entries:
        if e['kind'] == 'local':
            group = '本地通用技能'
        elif e['id'].startswith('superpowers:'):
            group = '开发流程 · Superpowers'
        elif e['id'].startswith('vercel:'):
            group = '应用开发与部署 · Vercel'
        elif e['id'].startswith('supabase:'):
            group = '数据库 · Supabase'
        elif e['id'].startswith('google-drive:'):
            group = '办公协作 · Google Drive'
        elif e['id'].startswith('notion:'):
            group = '知识与项目管理 · Notion'
        elif e['id'] == 'alibabacloud-workbench-cli':
            group = '云资源管理 · Alibaba Cloud'
        else:
            group = '产品体验、前端与动效'
        groups.setdefault(group, []).append(e)
    order = ['本地通用技能', '产品体验、前端与动效', '开发流程 · Superpowers',
             '应用开发与部署 · Vercel', '数据库 · Supabase', '办公协作 · Google Drive',
             '知识与项目管理 · Notion', '云资源管理 · Alibaba Cloud']
    for group in order:
        records = groups.get(group, [])
        if not records:
            continue
        lines.extend([f'### {group}（{len(records)}）', '', '| 调用名称 | 简单介绍 | 状态 |', '| --- | --- | --- |'])
        for e in sorted(records, key=lambda x: x['id']):
            if e['kind'] == 'local':
                url, status = e['entry'], '本地技能'
            elif e['status'] == 'reference-only':
                url, status = e['project'], '仅供参考'
            else:
                url = f"{e['project']}/blob/{e['ref']}/{e['entry']}"
                status = '外部引用'
            desc = e['description'].replace('|', '&#124;').replace('\n', ' ')
            lines.append(f"| [${e['id']}]({url}) | {desc} | {status} |")
        lines.append('')
    return '\n'.join(lines)


def update_readme(text, table):
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) > text.index(END):
        raise ValueError('README must have one ordered skill-table marker pair')
    before, rest = text.split(START, 1)
    _, after = rest.split(END, 1)
    return before + START + '\n' + table.rstrip() + '\n' + END + after


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true', help='refresh the marked README table')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    entries = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))['skills']
    path = root / 'README.md'
    original = path.read_text(encoding='utf-8')
    updated = update_readme(original, render(entries))
    if args.write:
        path.write_text(updated, encoding='utf-8')
        print('README skill table refreshed')
    elif updated != original:
        print('README skill table is stale; run: python3 scripts/readme_catalog.py --write')
        raise SystemExit(1)
    else:
        print('README skill table is current')
