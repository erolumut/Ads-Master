#!/usr/bin/env python3
"""Instruction budget check (Workflow Kit, instructions-budget skill).

Checks:
  1. CLAUDE.md line budget (instructions.maxLines, default 200). Block HTML comments are
     stripped before the model sees the file, so they do not count.
  2. Every referenced path exists: backtick spans and @imports that look like a path
     (contain "/" or end in a known extension). Spans with *, <, >, spaces or :// are skipped,
     as are paths listed in instructions.ignorePaths.
  3. Every .claude/rules/*.md has valid frontmatter; each `paths` glob is relative, has balanced
     braces and brackets, and (warning) matches at least one file.

  python3 check_instructions.py            errors exit 1, warnings print
  python3 check_instructions.py --strict   warnings exit 1 too

Exit codes: 0 pass, 1 fail, 2 could not run (no CLAUDE.md and no rules to check).

Config (workflow-kit.json at the project root, all optional):
  instructions.claudeMd    default CLAUDE.md
  instructions.maxLines    default 200
  instructions.rulesDir    default .claude/rules
  instructions.ignorePaths paths or globs never reported as missing
Standard library only.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import sys
from pathlib import Path

CANNOT_COVER = ("This gate cannot cover: whether the instructions are right or followed, rules in "
                "~/.claude or managed policy, and the combined size of every file loaded at startup.")
EXTENSIONS = (
    ".md", ".json", ".yml", ".yaml", ".toml", ".py", ".ts", ".tsx", ".js", ".mjs", ".cjs",
    ".jsx", ".sh", ".sql", ".css", ".html", ".txt", ".env", ".lock", ".cfg", ".ini",
)
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".next", ".venv", "venv", "coverage", "__pycache__"}
COMMENT = re.compile(r"<!--.*?-->", re.S)
COMMENT_BLOCK = re.compile(r"^[ \t]*<!--.*?-->[ \t]*(?:\n|$)", re.S | re.M)
CODE_FENCE = re.compile(r"^```.*?^```", re.S | re.M)
BACKTICK = re.compile(r"`([^`\n]+)`")
IMPORT = re.compile(r"(?<![\w`])@([A-Za-z0-9_./~-][^\s`]*)")


def load_config(root: Path) -> dict:
    p = root / "workflow-kit.json"
    if not p.is_file():
        return {}
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("instructions", {}) or {}
    except (OSError, ValueError) as exc:
        print(f"warning: cannot read {p}: {exc}", file=sys.stderr)
        return {}


def effective_lines(text: str) -> int:
    stripped = COMMENT.sub("", COMMENT_BLOCK.sub("", text))
    return len(stripped.rstrip("\n").splitlines()) if stripped.strip() else 0


def looks_like_path(s: str) -> bool:
    if any(c in s for c in "*<>{}$ ") or "://" in s or s.startswith("-"):
        return False
    if s.startswith(("~", "/")):
        return False  # home or absolute paths are machine specific
    s = s.rstrip(".,;:")
    return "/" in s or s.lower().endswith(EXTENSIONS)


def referenced_paths(text: str) -> list[tuple[int, str]]:
    body = COMMENT.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    body = CODE_FENCE.sub(lambda m: "\n" * m.group(0).count("\n"), body)
    refs: list[tuple[int, str]] = []
    for i, line in enumerate(body.splitlines(), 1):
        for m in BACKTICK.finditer(line):
            span = m.group(1).strip()
            if span.startswith("@"):
                span = span[1:]
            if looks_like_path(span):
                refs.append((i, span.rstrip(".,;:")))
        for m in IMPORT.finditer(BACKTICK.sub("", line)):
            span = m.group(1).rstrip(".,;:)")
            if looks_like_path(span) or span.upper().endswith(".MD"):
                refs.append((i, span))
    return refs


def ignored(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatch(path, p) or path == p for p in patterns)


def parse_frontmatter(text: str) -> tuple[dict | None, str | None]:
    """Minimal YAML subset: `key: value`, `key:` + `- item` lists, comma strings."""
    if not text.startswith("---"):
        return {}, None
    lines = text.splitlines()
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, "frontmatter opened with --- but never closed"
    data: dict = {}
    key = None
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.lstrip().startswith("- ") and key:
            if not isinstance(data.get(key), list):
                return None, f"list item under '{key}' which already has a scalar value"
            data[key].append(raw.lstrip()[2:].strip().strip("\"'"))
            continue
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if not m:
            return None, f"cannot parse frontmatter line: {raw!r}"
        key, value = m.group(1), m.group(2).strip()
        if value == "":
            data[key] = []
        elif value.startswith("[") and value.endswith("]"):
            data[key] = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
        else:
            data[key] = value.strip("\"'")
    return data, None


def expand_braces(pattern: str) -> list[str]:
    m = re.search(r"\{([^{}]*)\}", pattern)
    if not m:
        return [pattern]
    out: list[str] = []
    for alt in m.group(1).split(","):
        out.extend(expand_braces(pattern[: m.start()] + alt + pattern[m.end():]))
    return out


def glob_error(pattern: str) -> str | None:
    if not pattern:
        return "empty pattern"
    if pattern.startswith("/") or re.match(r"^[A-Za-z]:\\", pattern):
        return "absolute path; rule globs are relative to the project root"
    if pattern.startswith("./"):
        return "leading ./ ; write the path relative to the project root without it"
    depth = 0
    for ch in pattern:
        depth += ch == "{"
        depth -= ch == "}"
        if depth < 0:
            return "unbalanced braces"
    if depth:
        return "unbalanced braces"
    i = 0
    while i < len(pattern):
        if pattern[i] == "\\":
            i += 2
            continue
        if pattern[i] == "[":
            close = pattern.find("]", i + 2 if i + 1 < len(pattern) and pattern[i + 1] in "!^" else i + 1)
            if close == -1:
                return "unbalanced [ ; escape a literal bracket as \\["
            i = close
        i += 1
    return None


def all_files(root: Path) -> list[str]:
    files: list[str] = []
    for p in root.rglob("*"):
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts):
            continue
        if p.is_file():
            files.append(p.relative_to(root).as_posix())
    return files


def glob_matches(pattern: str, files: list[str]) -> bool:
    for pat in expand_braces(pattern):
        variants = {pat}
        if "**/" in pat:
            variants.add(pat.replace("**/", ""))
        for f in files:
            if any(fnmatch.fnmatch(f, v) for v in variants):
                return True
    return False


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="project root (default: current directory)")
    ap.add_argument("--strict", action="store_true", help="warnings fail too")
    ap.add_argument("--max-lines", type=int, help="override instructions.maxLines")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    cfg = load_config(root)
    claude_md = root / cfg.get("claudeMd", "CLAUDE.md")
    max_lines = args.max_lines or int(cfg.get("maxLines", 200))
    rules_dir = root / cfg.get("rulesDir", ".claude/rules")
    ignore = list(cfg.get("ignorePaths", [])) + ["PARALLEL-SESSIONS.md"]  # the ledger is git-ignored
    errors: list[str] = []
    warnings: list[str] = []

    sources: list[Path] = []
    if claude_md.is_file():
        text = claude_md.read_text(encoding="utf-8")
        n = effective_lines(text)
        raw = len(text.splitlines())
        msg = f"{claude_md.name}: {n} effective lines ({raw} raw), budget {max_lines}"
        if n > max_lines:
            errors.append(msg + " (over budget)")
        print(("over" if n > max_lines else "ok  ") + f"  {msg}")
        sources.append(claude_md)
    rule_files = sorted(rules_dir.glob("**/*.md")) if rules_dir.is_dir() else []
    if not claude_md.is_file():
        if not rule_files:
            print(f"COULD NOT RUN: {claude_md.relative_to(root).as_posix()} and {rules_dir.relative_to(root).as_posix()} not found")
            print(CANNOT_COVER)
            return 2
        warnings.append(f"{claude_md.relative_to(root).as_posix()} not found")
    sources.extend(rule_files)

    for src in sources:
        text = src.read_text(encoding="utf-8")
        for line_no, ref in referenced_paths(text):
            if ignored(ref, ignore):
                continue
            candidates = [root / ref, src.parent / ref]
            if not any(c.exists() for c in candidates):
                errors.append(f"{src.relative_to(root).as_posix()}:{line_no}: referenced path not found: {ref}")

    files = all_files(root) if rule_files else []
    unconditional = 0
    for rf in rule_files:
        rel = rf.relative_to(root).as_posix()
        text = rf.read_text(encoding="utf-8")
        data, err = parse_frontmatter(text)
        if err:
            errors.append(f"{rel}: {err}")
            continue
        paths = data.get("paths") if data else None
        if paths is None:
            unconditional += effective_lines(text)
            print(f"info  {rel}: no paths, loads every session")
            continue
        if isinstance(paths, str):
            paths = [p.strip() for p in paths.split(",") if p.strip()]
        if not paths:
            errors.append(f"{rel}: paths is empty")
            continue
        for pat in paths:
            gerr = glob_error(pat)
            if gerr:
                errors.append(f"{rel}: glob {pat!r}: {gerr}")
            elif not glob_matches(pat, files):
                warnings.append(f"{rel}: glob {pat!r} matches no file")
    if unconditional:
        print(f"info  unconditional rule lines: {unconditional} (these load with CLAUDE.md)")

    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"error {e}")
    failed = bool(errors) or (args.strict and bool(warnings))
    print(f"{'FAIL' if failed else 'OK'}: {len(errors)} error(s), {len(warnings)} warning(s)")
    print(CANNOT_COVER)
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 (an unexpected crash is "could not run", never "fail")
        print(f"COULD NOT RUN: unexpected error: {exc!r}")
        print(CANNOT_COVER)
        sys.exit(2)
