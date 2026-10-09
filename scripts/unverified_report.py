#!/usr/bin/env python3
"""List every [Unverified] and [Contested] claim in the playbooks and research.

The output is the verification queue: what still needs a live account check,
an official source or a test before it should drive spend.

Usage:
  python3 scripts/unverified_report.py                 # summary per package
  python3 scripts/unverified_report.py --slug meta-ads # full queue for one package
  python3 scripts/unverified_report.py --out queue.md  # write the full queue to a file
  python3 scripts/unverified_report.py --json          # machine readable
"""
import argparse
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABEL = re.compile(r"\[(Unverified|Contested)[^\]]*\]", re.I)


def scan():
    items = []
    for base in ("skills", "research"):
        top = os.path.join(ROOT, base)
        for dirpath, _, files in os.walk(top):
            for name in sorted(files):
                if not name.endswith(".md") or "/template" in dirpath:
                    continue
                path = os.path.join(dirpath, name)
                rel = os.path.relpath(path, ROOT)
                parts = rel.split(os.sep)
                slug = parts[1] if base == "skills" else name[:-3]
                with open(path, encoding="utf-8") as fh:
                    for no, line in enumerate(fh, 1):
                        for m in LABEL.finditer(line):
                            text = re.sub(r"\s+", " ", line.strip().strip("|").strip())
                            items.append({"slug": slug, "file": rel, "line": no,
                                          "label": m.group(1).capitalize(),
                                          "text": text[:240]})
    return items


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--slug")
    ap.add_argument("--out")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    items = scan()
    if args.slug:
        items = [i for i in items if i["slug"] == args.slug]
    if args.json:
        print(json.dumps(items, indent=2, ensure_ascii=False))
        return 0
    by_slug = {}
    for i in items:
        by_slug.setdefault(i["slug"], []).append(i)
    lines = ["# Verification queue", "",
             f"{len(items)} labeled claims across {len(by_slug)} packages. "
             "Clear them with the `ads-verify` skill (evidence ladder: live account, official source, "
             "two independent dated sources, controlled test).", "",
             "| Package | Unverified | Contested |", "|---------|-----------:|----------:|"]
    for slug in sorted(by_slug, key=lambda s: -len(by_slug[s])):
        u = sum(1 for i in by_slug[slug] if i["label"] == "Unverified")
        c = sum(1 for i in by_slug[slug] if i["label"] == "Contested")
        lines.append(f"| {slug} | {u} | {c} |")
    if args.slug or args.out:
        for slug in sorted(by_slug):
            lines += ["", f"## {slug}", ""]
            for i in by_slug[slug]:
                lines.append(f"- [{i['label']}] `{i['file']}:{i['line']}` {i['text']}")
    text = "\n".join(lines) + "\n"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"wrote {args.out} ({len(items)} items)")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
