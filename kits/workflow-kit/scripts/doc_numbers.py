#!/usr/bin/env python3
"""Decision and rule numbers are given when the work ships (Workflow Kit, decision-log skill).

While working, write ADR-NEW<n> and R-NEW<n> placeholders (n = 1, 2, 3 ...). Right before the
push that reaches the main branch (after fetching and integrating it), run --assign: each
placeholder becomes the highest existing number + 1, + 2 ... in placeholder order, in every
scanned file that names it.

Without --assign this is the check. It fails on: two entries with one ADR number, two index rows
with one number, an entry without an index row or a row without an entry, two rule definitions
with one number, and (with --no-placeholders) any placeholder at all.

  python3 doc_numbers.py --check                    check (default)
  python3 doc_numbers.py --check --no-placeholders  also refuse placeholders (pre-push, CI)
  python3 doc_numbers.py --assign                   show what would be numbered (dry run)
  python3 doc_numbers.py --assign --apply --yes     number the placeholders (writes files)

Exit codes: 0 pass, 1 fail, 2 could not run (no decision file found, bad config).

Config (workflow-kit.json at the project root, all optional):
  decisions.files      files holding ADR entries and the index   (default: DECISIONS.md)
  decisions.ruleFiles  files holding rule definitions            (default: none)
  decisions.scan       globs scanned for placeholders            (default: **/*.md)
  decisions.exclude    globs never scanned

Prose that explains the syntax writes a literal <n>, which this tool does not match.
Standard library only.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path

PLACEHOLDER = re.compile(r"(?<![A-Za-z0-9])(ADR|R)-NEW(\d+)(?![0-9])")
ADR_NUMBER = re.compile(r"(?<![A-Za-z0-9-])ADR-(\d{1,6})(?![0-9])")
RULE_NUMBER = re.compile(r"(?<![A-Za-z0-9-])R(\d{1,6})(?![0-9])")
ADR_HEADING = re.compile(r"^## ADR-(\d{1,6}|NEW\d+)(?![0-9])", re.M)
RULE_DEF = re.compile(r"^\s*[-*]\s+\*\*R(\d{1,6}|-NEW\d+)(?![0-9])", re.M)
INDEX_HEADING = re.compile(r"^## Index\s*$", re.M)
INDEX_ROW = re.compile(r"^\|\s*(?:ADR-)?(\d{1,6}|NEW\d+)\s*\|", re.M)

CANNOT_COVER = ("This gate cannot cover: numbers taken on the remote after your last fetch, entries "
                "outside the configured files, and whether a decision is right.")

DEFAULT_EXCLUDE = [
    ".git/**", "node_modules/**", "dist/**", "build/**", ".next/**", ".venv/**", "venv/**",
    "coverage/**", "**/scripts/tests/**", "**/workflow-kit/**",
]


def load_config(root: Path) -> dict:
    path = root / "workflow-kit.json"
    if not path.is_file():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8")).get("decisions", {}) or {}
    except (OSError, ValueError) as exc:
        print(f"warning: cannot read {path}: {exc}", file=sys.stderr)
        return {}


def matches(rel: str, patterns: list[str]) -> bool:
    for pat in patterns:
        if fnmatch.fnmatch(rel, pat):
            return True
        if pat.startswith("**/") and fnmatch.fnmatch(rel, pat[3:]):
            return True
    return False


def scan_files(root: Path, scan: list[str], exclude: list[str]) -> list[Path]:
    found: set[Path] = set()
    for pat in scan:
        for p in root.glob(pat):
            if not p.is_file():
                continue
            rel = p.relative_to(root).as_posix()
            if matches(rel, exclude):
                continue
            found.add(p)
    return sorted(found)


def read(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def index_section(text: str) -> str:
    m = INDEX_HEADING.search(text)
    if not m:
        return ""
    rest = text[m.end():]
    end = re.search(r"^## ", rest, re.M)
    return rest if end is None else rest[: end.start()]


def duplicates(keys: list[str]) -> list[str]:
    seen: set[str] = set()
    twice: list[str] = []
    for k in keys:
        if k in seen and k not in twice:
            twice.append(k)
        seen.add(k)
    return twice


def norm(key: str) -> str:
    """'012' and '12' are the same number; placeholders stay as they are."""
    return key if key.startswith("NEW") or key.startswith("-NEW") else str(int(key))


def existing_max(texts: list[str], pattern: re.Pattern) -> tuple[int, int]:
    """Highest number and the widest zero padded width seen (padding only counts with a leading 0)."""
    top, width = 0, 0
    for t in texts:
        for m in pattern.finditer(t):
            digits = m.group(1)
            top = max(top, int(digits))
            if digits.startswith("0") and len(digits) > 1:
                width = max(width, len(digits))
    return top, width


def check(root: Path, cfg: dict, files: list[Path], no_placeholders: bool) -> int:
    errors: list[str] = []
    decision_files = cfg.get("files", ["DECISIONS.md"])
    if not any((root / n).is_file() for n in decision_files):
        print(f"COULD NOT RUN: no decision file found ({', '.join(decision_files)}); set decisions.files in workflow-kit.json")
        print(CANNOT_COVER)
        return 2
    for name in cfg.get("files", ["DECISIONS.md"]):
        p = root / name
        if not p.is_file():
            continue
        text = read(p)
        heads = [norm(k) for k in ADR_HEADING.findall(text)]
        rows = [norm(k) for k in INDEX_ROW.findall(index_section(text))]
        for d in duplicates(heads):
            errors.append(f"{name}: two entries with ADR-{d}")
        for d in duplicates(rows):
            errors.append(f"{name}: two index rows with {d}")
        if rows or INDEX_HEADING.search(text):
            for k in sorted(set(heads) - set(rows)):
                errors.append(f"{name}: entry ADR-{k} has no index row")
            for k in sorted(set(rows) - set(heads)):
                errors.append(f"{name}: index row {k} has no entry")
    for name in cfg.get("ruleFiles", []):
        p = root / name
        if not p.is_file():
            continue
        defs = [norm(k) for k in RULE_DEF.findall(read(p))]
        for d in duplicates(defs):
            errors.append(f"{name}: two rule definitions with R{d}")
    placeholders: list[str] = []
    for p in files:
        for i, line in enumerate(read(p).splitlines(), 1):
            for m in PLACEHOLDER.finditer(line):
                placeholders.append(f"{p.relative_to(root).as_posix()}:{i}: {m.group(0)}")
    for e in errors:
        print(f"error: {e}")
    if placeholders:
        label = "error" if no_placeholders else "info"
        for ph in placeholders:
            print(f"{label}: placeholder {ph}")
    if errors or (no_placeholders and placeholders):
        print(f"FAIL: {len(errors)} numbering error(s), {len(placeholders)} placeholder(s)")
        print(CANNOT_COVER)
        return 1
    print(f"OK: no numbering errors; {len(placeholders)} placeholder(s) waiting for --assign")
    print(CANNOT_COVER)
    return 0


def assign(root: Path, cfg: dict, files: list[Path], apply: bool) -> int:
    dry_run = not apply
    texts = {p: read(p) for p in files}
    order: dict[str, list[int]] = {"ADR": [], "R": []}
    for t in texts.values():
        for m in PLACEHOLDER.finditer(t):
            n = int(m.group(2))
            if n not in order[m.group(1)]:
                order[m.group(1)].append(n)
    if not order["ADR"] and not order["R"]:
        print("OK: no placeholders to assign")
        print(CANNOT_COVER)
        return 0
    if order["ADR"] and not any((root / f).is_file() for f in cfg.get("files", ["DECISIONS.md"])):
        print("COULD NOT RUN: no decision file to read the highest ADR number from; set decisions.files")
        print(CANNOT_COVER)
        return 2

    adr_sources = [read(root / f) for f in cfg.get("files", ["DECISIONS.md"]) if (root / f).is_file()]
    rule_sources = [read(root / f) for f in cfg.get("ruleFiles", []) if (root / f).is_file()]
    adr_top, adr_width = existing_max(adr_sources, ADR_NUMBER)
    rule_top, rule_width = existing_max(rule_sources, RULE_NUMBER)
    adr_width = adr_width or 3

    mapping: dict[tuple[str, int], str] = {}
    for i, n in enumerate(sorted(order["ADR"]), 1):
        mapping[("ADR", n)] = f"ADR-{str(adr_top + i).zfill(adr_width)}"
    for i, n in enumerate(sorted(order["R"]), 1):
        mapping[("R", n)] = f"R{str(rule_top + i).zfill(rule_width)}" if rule_width else f"R{rule_top + i}"

    for (kind, n), new in sorted(mapping.items()):
        print(f"{kind}-NEW{n} -> {new}")

    def repl(m: re.Match) -> str:
        return mapping[(m.group(1), int(m.group(2)))]

    changed = 0
    for p, t in texts.items():
        new_text = PLACEHOLDER.sub(repl, t)
        if new_text != t:
            changed += 1
            if not dry_run:
                p.write_text(new_text, encoding="utf-8")
            print(f"{'would update' if dry_run else 'updated'} {p.relative_to(root).as_posix()}")
    print(f"OK: {len(mapping)} placeholder(s) in {changed} file(s){' (dry run; add --apply --yes to write)' if dry_run else ''}")
    print(CANNOT_COVER)
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="check numbering (default)")
    mode.add_argument("--assign", action="store_true", help="replace placeholders with the next free numbers")
    ap.add_argument("--no-placeholders", action="store_true", help="with --check: any placeholder fails")
    ap.add_argument("--apply", action="store_true", help="with --assign: write the files (needs --yes)")
    ap.add_argument("--yes", action="store_true", help="confirm --apply")
    ap.add_argument("--root", default=".", help="project root (default: current directory)")
    ap.add_argument("paths", nargs="*", help="files to scan instead of decisions.scan")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    cfg = load_config(root)
    if args.paths:
        files = sorted({(root / p).resolve() for p in args.paths if (root / p).is_file()})
    else:
        exclude = DEFAULT_EXCLUDE + list(cfg.get("exclude", []))
        files = scan_files(root, cfg.get("scan", ["**/*.md"]), exclude)
    if args.apply and not args.yes:
        print("COULD NOT RUN: --apply rewrites files; repeat with --apply --yes")
        return 2
    if args.assign:
        return assign(root, cfg, files, args.apply and args.yes)
    return check(root, cfg, files, args.no_placeholders)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 (an unexpected crash is "could not run", never "fail")
        print(f"COULD NOT RUN: unexpected error: {exc!r}")
        print(CANNOT_COVER)
        sys.exit(2)
