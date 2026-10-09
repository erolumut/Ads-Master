#!/usr/bin/env python3
"""Regenerate the auto sections of docs/HOW_TO_USE.md from the repo itself.

Sources: agents/*.md and skills/*/SKILL.md frontmatter, docs/packs.json and
kits/*/.claude-plugin/plugin.json. Hand written text outside the AUTO markers
is never touched, so the document stays a living one: add an agent, run this
script, and the catalog, the packs and the kits update themselves.

Usage:
  python3 scripts/build_docs.py          # rewrite the auto sections
  python3 scripts/build_docs.py --check  # exit 1 if the doc is out of date
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOC = os.path.join(ROOT, "docs", "HOW_TO_USE.md")


def frontmatter(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---\n"):
        return {}
    block = text[4:text.find("\n---", 4)]
    data, key = {}, None
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            data[key] = val
        elif key and line.startswith("  ") and not line.strip().startswith("-"):
            data[key] = (data[key] + " " + line.strip()).strip()
    desc = data.get("description", "").strip("\"'>| ")
    data["description"] = desc
    return data


def first_sentence(text, limit=190):
    text = re.sub(r"\s+", " ", text)
    m = re.match(r"(.+?[.!?])(\s|$)", text)
    out = m.group(1) if m else text
    return out if len(out) <= limit else out[:limit].rsplit(" ", 1)[0] + "..."


def load_packs():
    with open(os.path.join(ROOT, "docs", "packs.json"), encoding="utf-8") as fh:
        packs = json.load(fh)
    packs.pop("_comment", None)
    return packs


def agents():
    out = []
    for name in sorted(os.listdir(os.path.join(ROOT, "agents"))):
        if name.endswith(".md"):
            fm = frontmatter(os.path.join(ROOT, "agents", name))
            out.append((name[:-3], fm.get("model", "inherit"), fm.get("description", "")))
    return out


def skills():
    out = []
    base = os.path.join(ROOT, "skills")
    for slug in sorted(os.listdir(base)):
        p = os.path.join(base, slug, "SKILL.md")
        if os.path.isfile(p):
            out.append((slug, frontmatter(p).get("description", "")))
    return out


def kits():
    out = []
    base = os.path.join(ROOT, "kits")
    if not os.path.isdir(base):
        return out
    for slug in sorted(os.listdir(base)):
        p = os.path.join(base, slug, ".claude-plugin", "plugin.json")
        if os.path.isfile(p):
            with open(p, encoding="utf-8") as fh:
                meta = json.load(fh)
            n_agents = len([f for f in os.listdir(os.path.join(base, slug, "agents")) if f.endswith(".md")]) \
                if os.path.isdir(os.path.join(base, slug, "agents")) else 0
            n_skills = len([d for d in os.listdir(os.path.join(base, slug, "skills"))]) \
                if os.path.isdir(os.path.join(base, slug, "skills")) else 0
            out.append((meta.get("name", slug), meta.get("version", ""), meta.get("description", ""),
                        n_agents, n_skills, f"kits/{slug}"))
    return out


def section_agents(packs):
    member = {}
    for pname, p in packs.items():
        if pname == "full":
            continue
        for a in p.get("agents", []):
            member.setdefault(a, []).append(pname)
    rows = ["| Agent | What it does | Packs | Model |", "|-------|--------------|-------|-------|"]
    for slug, model, desc in agents():
        rows.append(f"| `{slug}` | {first_sentence(desc)} | {', '.join(member.get(slug, ['full']))} | {model} |")
    return "\n".join(rows)


def section_skills():
    rows = ["| Skill | Use it for |", "|-------|-----------|"]
    for slug, desc in skills():
        rows.append(f"| `{slug}` | {first_sentence(desc)} |")
    return "\n".join(rows)


def section_packs(packs):
    rows = ["| Pack | For | Agents added on top of core | Install |", "|------|-----|------------------------------|---------|"]
    for pname, p in packs.items():
        ag = "all agents" if p.get("agents") == ["*"] else ", ".join(f"`{a}`" for a in p.get("agents", []))
        cmd = "always" if pname == "core" else f"`install.sh <project> --pack {pname}`"
        rows.append(f"| {p.get('label', pname)} | {p.get('for', '')} | {ag} | {cmd} |")
    return "\n".join(rows)


def section_kits():
    found = kits()
    if not found:
        return "_No kits yet._"
    rows = ["| Kit | Version | What it is | Agents | Skills | Path |", "|-----|---------|-----------|-------:|-------:|------|"]
    for name, ver, desc, na, ns, path in found:
        rows.append(f"| `{name}` | {ver} | {first_sentence(desc, 220)} | {na} | {ns} | `{path}` |")
    return "\n".join(rows)


def render(text):
    packs = load_packs()
    blocks = {"agents": section_agents(packs), "skills": section_skills(),
              "packs": section_packs(packs), "kits": section_kits()}
    for key, body in blocks.items():
        pat = re.compile(rf"(<!-- AUTO:{key}:start -->\n)(?:.*?\n)?(<!-- AUTO:{key}:end -->)", re.S)
        if not pat.search(text):
            raise SystemExit(f"marker AUTO:{key} missing in docs/HOW_TO_USE.md")
        text = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(2), text)
    return text


def main():
    with open(DOC, encoding="utf-8") as fh:
        current = fh.read()
    new = render(current)
    if "--check" in sys.argv:
        if new != current:
            print("docs/HOW_TO_USE.md is out of date: run python3 scripts/build_docs.py")
            return 1
        print("docs/HOW_TO_USE.md is up to date")
        return 0
    with open(DOC, "w", encoding="utf-8") as fh:
        fh.write(new)
    print("docs/HOW_TO_USE.md regenerated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
