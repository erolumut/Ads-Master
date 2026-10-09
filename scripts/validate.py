#!/usr/bin/env python3
"""Validate the Ads Master repo against docs/AUTHORING_SPEC.md.

Checks:
  - every agent has valid frontmatter (name matches file, description, skills list)
  - every skill referenced by an agent exists, every skill has SKILL.md with name and description
  - SKILL.md stays under 500 lines and every relative link resolves
  - every domain agent has a research dossier and the required reference files
  - style: no em dash or en dash, no banned words
Exit code 1 when any error is found.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UTILITY_SKILLS = {"ads-setup", "ads-review", "ads-verify"}
REQUIRED_REFS = {"audit-checklist.md", "sources.md"}
BANNED = re.compile(
    r"\b(excel\w*|robust\w*|honed|spearhead\w*|prospect\w*|resonat\w*|thriv\w*)\b",
    re.IGNORECASE,
)
DASHES = re.compile("[—–]")
LINK = re.compile(r"\]\(([^)#\s]+\.md)(?:#[^)]*)?\)")
SKIP_DIRS = {".git", "node_modules"}

errors, warnings = [], []


try:
    import yaml  # optional: stricter frontmatter check when PyYAML is installed
except ImportError:
    yaml = None


def yaml_error(path):
    """Return an error string when the frontmatter is not valid YAML."""
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---\n") or text.find("\n---", 4) == -1:
        return None
    block = text[4:text.find("\n---", 4)]
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError as exc:
            return str(exc).splitlines()[0]
        return None if isinstance(data, dict) else "frontmatter is not a mapping"
    for line in block.splitlines():
        m = re.match(r"^(name|description):\s*(.*)$", line)
        if m and not m.group(2).startswith(("'", '"')) and ": " in m.group(2):
            return f"unquoted ': ' inside {m.group(1)} breaks YAML"
    return None


def frontmatter(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    block = text[4:end]
    data, key = {}, None
    for line in block.splitlines():
        if re.match(r"^\s+-\s+", line) and key:
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(line.split("-", 1)[1].strip())
            continue
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            data[key] = val if val else []
    return data, text[end + 4:]


def rel(path):
    return os.path.relpath(path, ROOT)


agents_dir = os.path.join(ROOT, "agents")
skills_dir = os.path.join(ROOT, "skills")
research_dir = os.path.join(ROOT, "research")

agent_slugs = sorted(f[:-3] for f in os.listdir(agents_dir) if f.endswith(".md")) if os.path.isdir(agents_dir) else []
skill_slugs = sorted(d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))) if os.path.isdir(skills_dir) else []

for slug in agent_slugs:
    path = os.path.join(agents_dir, slug + ".md")
    err = yaml_error(path)
    if err:
        errors.append(f"{rel(path)}: invalid YAML frontmatter ({err})")
    fm, _ = frontmatter(path)
    if fm is None:
        errors.append(f"{rel(path)}: missing frontmatter")
        continue
    if fm.get("name") != slug:
        errors.append(f"{rel(path)}: name '{fm.get('name')}' does not match file name")
    if not fm.get("description"):
        errors.append(f"{rel(path)}: missing description")
    skills = fm.get("skills") or []
    if isinstance(skills, str):
        errors.append(f"{rel(path)}: skills must be a YAML list")
        skills = [s.strip() for s in skills.split(",")]
    for s in skills:
        if s not in skill_slugs:
            errors.append(f"{rel(path)}: preloaded skill '{s}' not found in skills/")
    if "Agent" not in str(fm.get("disallowedTools", "")):
        errors.append(f"{rel(path)}: add 'disallowedTools: Agent' (main session is the only conductor)")
    if "tools" in fm:
        warnings.append(f"{rel(path)}: has a tools field (spec says inherit all tools)")
    if not os.path.isfile(os.path.join(research_dir, slug + ".md")):
        errors.append(f"research/{slug}.md missing for agent {slug}")

for slug in skill_slugs:
    path = os.path.join(skills_dir, slug, "SKILL.md")
    if not os.path.isfile(path):
        errors.append(f"skills/{slug}: SKILL.md missing")
        continue
    err = yaml_error(path)
    if err:
        errors.append(f"{rel(path)}: invalid YAML frontmatter ({err})")
    fm, body = frontmatter(path)
    if fm is None or not fm.get("description"):
        errors.append(f"{rel(path)}: missing frontmatter description")
    elif fm.get("name") and fm.get("name") != slug:
        errors.append(f"{rel(path)}: name '{fm.get('name')}' does not match folder")
    if fm and len(str(fm.get("description", ""))) > 1024:
        errors.append(f"{rel(path)}: description longer than 1024 characters")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()
    if len(lines) > 500:
        errors.append(f"{rel(path)}: {len(lines)} lines (limit 500)")
    for target in LINK.findall("\n".join(lines)):
        if target.startswith("http"):
            continue
        if not os.path.isfile(os.path.normpath(os.path.join(skills_dir, slug, target))):
            errors.append(f"{rel(path)}: broken link {target}")
    if slug not in UTILITY_SKILLS:
        refs_dir = os.path.join(skills_dir, slug, "references")
        refs = set(os.listdir(refs_dir)) if os.path.isdir(refs_dir) else set()
        for req in REQUIRED_REFS - refs:
            errors.append(f"skills/{slug}/references/{req} missing")
        linked = {os.path.basename(t) for t in LINK.findall("\n".join(lines))}
        for ref in sorted(refs - linked):
            warnings.append(f"skills/{slug}/references/{ref} is not linked from SKILL.md")

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
    for name in filenames:
        if not name.endswith(".md"):
            continue
        path = os.path.join(dirpath, name)
        with open(path, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                if DASHES.search(line):
                    errors.append(f"{rel(path)}:{i}: em or en dash")
                # Citation lines (with a URL) may quote third party titles verbatim.
                # The style spec itself names the banned words.
                if "http" in line or "Banned words" in line:
                    continue
                m = BANNED.search(line)
                if m:
                    errors.append(f"{rel(path)}:{i}: banned word '{m.group(0)}'")

# Packs: every agent belongs to at least one pack, every pack member exists.
packs_path = os.path.join(ROOT, "docs", "packs.json")
if os.path.isfile(packs_path):
    import json
    with open(packs_path, encoding="utf-8") as fh:
        packs = {k: v for k, v in json.load(fh).items() if not k.startswith("_")}
    covered = set()
    for pname, pack in packs.items():
        for member in pack.get("agents", []) + pack.get("skills", []):
            if member == "*":
                continue
            covered.add(member)
            if member not in agent_slugs and member not in skill_slugs:
                errors.append(f"docs/packs.json: pack '{pname}' lists unknown '{member}'")
    for slug in agent_slugs:
        if slug not in covered:
            errors.append(f"docs/packs.json: agent '{slug}' is in no pack")

# The living guide must be regenerated whenever agents, skills, packs or kits change.
link_dev = os.path.join(ROOT, "scripts", "link_dev.py")
if os.path.isfile(link_dev):
    import subprocess
    res = subprocess.run([sys.executable, link_dev, "--check"], capture_output=True, text=True)
    if res.returncode != 0:
        errors.append(res.stdout.strip() or "dev links out of date: run python3 scripts/link_dev.py")

build_docs = os.path.join(ROOT, "scripts", "build_docs.py")
if os.path.isfile(build_docs) and os.path.isfile(os.path.join(ROOT, "docs", "HOW_TO_USE.md")):
    import subprocess
    res = subprocess.run([sys.executable, build_docs, "--check"], capture_output=True, text=True)
    if res.returncode != 0:
        errors.append("docs/HOW_TO_USE.md is out of date: run python3 scripts/build_docs.py")

for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(f"\n{len(agent_slugs)} agents, {len(skill_slugs)} skills, {len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
