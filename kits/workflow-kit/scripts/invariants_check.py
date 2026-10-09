#!/usr/bin/env python3
"""Project invariants on staged files (Workflow Kit, review-gates skill).

Rules live in invariants.json (project root, or --config). Each rule:
  id                 short id shown in every violation, for example "INV-UTM"
  description        one line
  paths              trigger globs (brace expansion and ** supported)
  exclude            globs exempt from the rule (optional)
  must_contain       regexes that must each match somewhere in a triggered file (optional)
  must_not_contain   regexes that must not match anywhere in a triggered file (optional)
  message            what to do instead (optional)

Modes:
  python3 invariants_check.py                  check staged files (git index content)
  python3 invariants_check.py --files a b      check these working tree files
  python3 invariants_check.py --hook           PreToolUse hook: reads the tool call JSON on stdin,
                                               acts only on `git commit`, and returns a deny
                                               decision naming the rule id and file

Exit codes: 0 pass, 1 violations, 2 could not run. In --hook mode the decision is printed as
JSON and the exit code is 0 (a could-not-run state denies the commit with the reason, so a
broken gate is never silently skipped). Standard library only.
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import re
import subprocess
import sys
from pathlib import Path

CANNOT_COVER = ("This gate cannot cover: rules nobody wrote, meaning that needs judgment, files outside "
                "the trigger globs, and anything committed with --no-verify or outside Claude Code.")
COMMIT = re.compile(r"(^|[;&|(]\s*|\s)git(\s+-C\s+\S+)?(\s+-c\s+\S+)*\s+commit\b")


class CouldNotRun(Exception):
    pass


def expand_braces(pattern: str) -> list[str]:
    m = re.search(r"\{([^{}]*)\}", pattern)
    if not m:
        return [pattern]
    out: list[str] = []
    for alt in m.group(1).split(","):
        out.extend(expand_braces(pattern[: m.start()] + alt + pattern[m.end():]))
    return out


def glob_match(path: str, patterns: list[str]) -> bool:
    for pat in patterns:
        for p in expand_braces(pat):
            variants = {p, p.replace("**/", "")} if "**/" in p else {p}
            if any(fnmatch.fnmatch(path, v) for v in variants):
                return True
    return False


def load_rules(path: Path) -> list[dict]:
    if not path.is_file():
        raise CouldNotRun(f"config not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise CouldNotRun(f"cannot parse {path}: {exc}") from exc
    rules = data.get("rules")
    if not isinstance(rules, list):
        raise CouldNotRun(f"{path}: 'rules' must be a list")
    for r in rules:
        if not r.get("id") or not r.get("paths"):
            raise CouldNotRun(f"{path}: every rule needs 'id' and 'paths' ({r!r:.80})")
        for key in ("must_contain", "must_not_contain"):
            for rx in r.get(key, []):
                try:
                    re.compile(rx)
                except re.error as exc:
                    raise CouldNotRun(f"{path}: rule {r['id']}: bad regex {rx!r}: {exc}") from exc
    return rules


def git(root: Path, *args: str) -> subprocess.CompletedProcess:
    try:
        return subprocess.run(["git", "-C", str(root), *args], capture_output=True, timeout=30)
    except (OSError, subprocess.SubprocessError) as exc:
        raise CouldNotRun(f"git failed: {exc}") from exc


def staged(root: Path) -> dict[str, str]:
    out = git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR")
    if out.returncode != 0:
        raise CouldNotRun(f"not a git repository or git error: {out.stderr.decode(errors='replace').strip()}")
    files: dict[str, str] = {}
    for name in [l for l in out.stdout.decode(errors="replace").splitlines() if l.strip()]:
        show = git(root, "show", f":{name}")
        if show.returncode != 0:
            raise CouldNotRun(f"cannot read staged content of {name}")
        if b"\0" in show.stdout[:8000]:
            continue  # binary file: text rules do not apply
        files[name] = show.stdout.decode("utf-8", errors="replace")
    return files


def working(root: Path, names: list[str]) -> dict[str, str]:
    files: dict[str, str] = {}
    for n in names:
        p = (root / n)
        if not p.is_file():
            raise CouldNotRun(f"file not found: {n}")
        rel = p.resolve().relative_to(root).as_posix() if p.resolve().is_relative_to(root) else n
        files[rel] = p.read_text(encoding="utf-8", errors="replace")
    return files


def violations(rules: list[dict], files: dict[str, str]) -> list[str]:
    found: list[str] = []
    for r in rules:
        for name, text in files.items():
            if not glob_match(name, r["paths"]) or glob_match(name, r.get("exclude", [])):
                continue
            hint = f" ({r['message']})" if r.get("message") else ""
            for rx in r.get("must_not_contain", []):
                m = re.search(rx, text, re.M)
                if m:
                    line = text.count("\n", 0, m.start()) + 1
                    found.append(f"{r['id']}: {name}:{line} contains /{rx}/{hint}")
            for rx in r.get("must_contain", []):
                if not re.search(rx, text, re.M):
                    found.append(f"{r['id']}: {name} lacks /{rx}/{hint}")
    return found


def deny(reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="repo root (default: current directory)")
    ap.add_argument("--config", help="rules file (default: <root>/invariants.json)")
    ap.add_argument("--files", nargs="+", help="check these working tree files instead of the index")
    ap.add_argument("--hook", action="store_true", help="run as a PreToolUse hook (stdin JSON)")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()

    if args.hook:
        try:
            payload = json.load(sys.stdin)
        except ValueError:
            return 0  # not a tool call we understand; let the normal flow decide
        command = ((payload.get("tool_input") or {}).get("command") or "")
        if payload.get("tool_name") not in (None, "Bash") or not COMMIT.search(command):
            return 0
        if payload.get("cwd"):
            root = Path(payload["cwd"]).resolve()

    config = Path(args.config) if args.config else root / "invariants.json"
    try:
        rules = load_rules(config if config.is_absolute() else root / config)
        files = working(root, args.files) if args.files else staged(root)
    except CouldNotRun as exc:
        if args.hook:
            deny(f"invariants check could not run: {exc}. Fix the config or ask the human.")
            return 0
        print(f"COULD NOT RUN: {exc}")
        print(CANNOT_COVER)
        return 2

    found = violations(rules, files)
    if args.hook:
        if found:
            deny("Invariant violation, commit blocked: " + "; ".join(found))
        return 0
    for v in found:
        print(f"error {v}")
    print(f"{'FAIL' if found else 'OK'}: {len(found)} violation(s) in {len(files)} file(s), {len(rules)} rule(s)")
    print(CANNOT_COVER)
    return 1 if found else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 (an unexpected crash is "could not run", never "fail")
        print(f"COULD NOT RUN: unexpected error: {exc!r}")
        print(CANNOT_COVER)
        sys.exit(2)
