#!/usr/bin/env python3
"""Validate the UI/UX Design Suite package using only the Python standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML frontmatter")
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def check_skill(path: Path, expected_name: str) -> list[str]:
    errors: list[str] = []
    try:
        fm = parse_frontmatter(path)
    except Exception as exc:
        return [f"{path}: {exc}"]
    if fm.get("name") != expected_name:
        errors.append(f"{path}: name={fm.get('name')!r}, expected {expected_name!r}")
    desc = fm.get("description", "")
    if not desc:
        errors.append(f"{path}: missing description")
    if len(desc) > 1400:
        errors.append(f"{path}: description too long ({len(desc)} chars)")
    if path.read_text(encoding="utf-8").count("\n") > 500:
        errors.append(f"{path}: SKILL.md exceeds 500 lines")
    return errors


def main() -> int:
    errors: list[str] = []
    errors += check_skill(ROOT / "SKILL.md", ROOT.name)

    manifest_path = ROOT / "manifest.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"manifest.json: {exc}")
        manifest = {"subskills": []}

    for name in manifest.get("subskills", []):
        path = ROOT / "subskills" / name / "SKILL.md"
        if not path.exists():
            errors.append(f"missing subskill: {path}")
            continue
        errors += check_skill(path, name)

    for name in manifest.get("internal_fallback_playbooks", []):
        if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9-]+", name):
            errors.append(f"invalid fallback name: {name!r}")
            continue
        path = ROOT / "references" / f"fallback-{name}.md"
        if not path.is_file():
            errors.append(f"missing fallback: {path}")

    # Check literal local file references written in backticks.
    skill_files = [ROOT / "SKILL.md"] + list((ROOT / "subskills").glob("*/SKILL.md"))
    ref_pattern = re.compile(r"`((?:(?:\.\./)+)?(?:subskills|references)/[^`]+\.(?:md|json))`")
    for skill in skill_files:
        text = skill.read_text(encoding="utf-8")
        for ref in ref_pattern.findall(text):
            if "*" in ref:
                if not any(ROOT.glob(ref)):
                    errors.append(f"{skill}: unmatched reference pattern {ref}")
                continue
            if ref.startswith("../"):
                candidate = (skill.parent / ref).resolve()
            else:
                candidate = (ROOT / ref).resolve()
            if not candidate.exists():
                errors.append(f"{skill}: broken reference {ref}")

    required_refs = [
        "references/UI-Design-manual.md",
        "references/capability-routing.md",
        "references/external-skill-adapters.md",
        "references/workflow-zero-to-one.md",
        "references/workflow-redesign.md",
        "references/workflow-small-change.md",
        "references/artifacts-and-gates.md",
        "references/component-regression.md",
        "references/quality-bar.md",
        "references/reference-research.md",
    ]
    for rel in required_refs:
        if not (ROOT / rel).exists():
            errors.append(f"missing required reference: {rel}")

    if errors:
        print("VALIDATION FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print("VALIDATION PASSED")
    print(f"root: {ROOT}")
    print(f"subskills: {len(manifest.get('subskills', []))}")
    print(f"internal fallbacks: {len(manifest.get('internal_fallback_playbooks', []))}")
    print(f"references: {len(list((ROOT / 'references').glob('*')))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
