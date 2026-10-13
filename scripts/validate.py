#!/usr/bin/env python3
"""Validate registry and local packages; never execute skills or access the network."""
from __future__ import annotations

import json
import re
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlparse
from readme_catalog import render, update_readme


def safe_path(value):
    return (isinstance(value, str) and bool(value) and '\\' not in value
            and not PurePosixPath(value).is_absolute()
            and all(p not in ('..', '.') for p in value.split('/')))


def validate(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    try:
        data = json.loads((root / 'catalog.json').read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return [f'catalog read failed: {exc}']
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        return ['unsupported catalog schema_version']
    if not isinstance(data.get('skills'), list):
        return ['skills must be a list']
    ids, local_entries = set(), set()
    for e in data['skills']:
        if not isinstance(e, dict):
            errors.append('skill record must be an object')
            continue
        name = e.get('id')
        if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*(?::[a-z0-9]+(?:-[a-z0-9]+)*)?', name):
            errors.append(f'invalid id: {name!r}')
            continue
        if name in ids:
            errors.append(f'duplicate id: {name}')
        ids.add(name)
        for field in ('description', 'provenance', 'license'):
            if not isinstance(e.get(field), str) or not e[field].strip():
                errors.append(f'{name}: missing {field}')
        if not isinstance(e.get('requires'), list) or not all(isinstance(x, str) and x for x in e['requires']):
            errors.append(f'{name}: invalid requires')
        if e.get('kind') not in ('local', 'external'):
            errors.append(f'{name}: invalid kind')
            continue
        if e.get('status') not in ('active', 'reference-only'):
            errors.append(f'{name}: invalid status')
            continue
        if e['kind'] == 'external':
            url = e.get('project', '')
            if not isinstance(url, str) or not url.startswith('https://'):
                errors.append(f'{name}: invalid project')
            if e['status'] == 'reference-only':
                if not e.get('reason'):
                    errors.append(f'{name}: missing reason')
                continue
            if not isinstance(url, str) or not re.fullmatch(r'https://github.com/[\w.-]+/[\w.-]+', url):
                errors.append(f'{name}: active project must identify a GitHub repository')
            if not isinstance(e.get('ref'), str) or not re.fullmatch('[0-9a-f]{40}', e['ref']):
                errors.append(f'{name}: invalid ref')
            if not isinstance(e.get('entry_sha256'), str) or not re.fullmatch('[0-9a-f]{64}', e['entry_sha256']):
                errors.append(f'{name}: invalid entry_sha256')
            for field in ('upstream_name', 'verified', 'verification'):
                if not isinstance(e.get(field), str) or not e[field]:
                    errors.append(f'{name}: missing {field}')
        entry = e.get('entry')
        if not safe_path(entry) or not entry.endswith('/SKILL.md'):
            errors.append(f'{name}: unsafe entry')
            continue
        if e['kind'] == 'local':
            if e['status'] != 'active' or entry != f'skills/{name}/SKILL.md':
                errors.append(f'{name}: local layout/status mismatch')
            local_entries.add(entry)
            p = root / entry
            if not p.is_file():
                errors.append(f'{name}: missing entry')
                continue
            text = p.read_text(encoding='utf-8')
            fm = re.match(r'\A---\n(.*?)\n---(?:\n|$)', text, re.S)
            if not fm:
                errors.append(f'{name}: missing frontmatter')
                continue
            match = re.search(r'^name:\s*([^\n]+)', fm[1], re.M)
            if not match or match[1].strip().strip('\'\"') != name:
                errors.append(f'{name}: name mismatch')
            if not re.search(r'^description:\s*\S', fm[1], re.M):
                errors.append(f'{name}: missing frontmatter description')

    for p in (root / 'skills').rglob('*'):
        rel = p.relative_to(root)
        if p.is_symlink():
            errors.append(f'{rel}: symlink is not portable')
            continue
        if 'agents' in rel.parts or p.name in ('.codex', '.claude'):
            errors.append(f'{rel}: platform metadata')
        if p.name == 'SKILL.md' and str(rel) not in local_entries:
            errors.append(f'{rel}: unregistered skill')
        if p.name == 'manifest.json' and p.is_file():
            try:
                manifest = json.loads(p.read_text(encoding='utf-8'))
                fallbacks = manifest.get('internal_fallback_playbooks', [])
                if not isinstance(fallbacks, list):
                    raise ValueError('fallback list required')
                for child in fallbacks:
                    if not isinstance(child, str) or not re.fullmatch('[a-z0-9-]+', child):
                        errors.append(f'{rel}: invalid fallback')
                    elif not (p.parent / 'references' / f'fallback-{child}.md').is_file():
                        errors.append(f'{rel}: missing fallback {child}')
            except (ValueError, AttributeError) as exc:
                errors.append(f'{rel}: invalid manifest: {exc}')

    # Inspect actual Markdown links outside fenced examples, plus literal package refs.
    for p in root.rglob('*.md'):
        if '.git' in p.relative_to(root).parts or p.is_symlink():
            continue
        text = p.read_text(encoding='utf-8')
        prose = re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', text)
        refs = re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', prose)
        for ref in refs:
            ref = ref.strip().strip('<>')
            if urlparse(ref).scheme or ref.startswith('#'):
                continue
            path = unquote(ref.split('#')[0])
            if not path:
                continue
            target = (p.parent / path).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f'{p.relative_to(root)}: broken link {ref}')
        if p.name == 'SKILL.md':
            for ref in re.findall(r'`((?:references|scripts|assets)/[^`]+)`', prose):
                if any(c in ref for c in '*<>') or ref.endswith('/'):
                    continue
                if not (p.parent / ref).exists():
                    errors.append(f'{p.relative_to(root)}: broken package reference {ref}')
    readme = root / 'README.md'
    if not errors and readme.is_file():
        text = readme.read_text(encoding='utf-8')
        try:
            if update_readme(text, render(data['skills'])) != text:
                errors.append('README skill table is stale; run: python3 scripts/readme_catalog.py --write')
        except ValueError as exc:
            errors.append(str(exc))
    return sorted(set(errors))


if __name__ == '__main__':
    problems = validate(Path(__file__).resolve().parents[1])
    for problem in problems:
        print(f'ERROR: {problem}')
    print(f'Validation {"FAILED" if problems else "PASSED"}: {len(problems)} error(s)')
    raise SystemExit(bool(problems))
