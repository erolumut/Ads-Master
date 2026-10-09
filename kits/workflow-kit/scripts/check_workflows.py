#!/usr/bin/env python3
"""GitHub Actions workflow lint (Workflow Kit, review-gates skill).

Line checks (standard library, always run):
  error  duplicate keys in one mapping (YAML parsers silently keep the last one)
  error  ${{ github.event.* }}, ${{ github.head_ref }} or ${{ inputs.* }} interpolated inside run:
         (script injection; pass the value through env: and quote "$VAR" instead)
  error  success(), failure(), always() or cancelled() used outside an if: condition
  warn   third party uses: not pinned to a 40 character commit SHA

Structure checks (need PyYAML; reported as "could not run" without it):
  error  no `on` trigger, no jobs or an empty jobs map
  error  no permissions: block at the workflow level and none on some job

  python3 check_workflows.py                     every file in .github/workflows
  python3 check_workflows.py a.yml b.yml         these files
  python3 check_workflows.py --strict            warnings fail too

Exit codes: 0 pass, 1 fail, 2 could not run (no files found, unreadable file, or structure
checks skipped because PyYAML is missing while no error was found).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CANNOT_COVER = ("This gate cannot cover: whether the workflow logic is right, secrets scope and "
                "environment protection rules, actions' own behavior, reusable workflows it calls, and "
                "anything in the repository settings.")
KEY = re.compile(r"^(\s*)(-\s+)?([A-Za-z0-9_.\-]+|\"[^\"]+\"|'[^']+')\s*:(\s|$)(.*)$")
BLOCK_SCALAR = re.compile(r"^[|>][+-]?\d*\s*(#.*)?$")
INJECTION = re.compile(r"\$\{\{\s*(github\.event\.[^}]*|github\.head_ref[^}]*|inputs\.[^}]*)\}\}")
STATUS_FN = re.compile(r"\b(success|failure|always|cancelled)\(\s*\)")
USES = re.compile(r"^\s*(-\s+)?uses:\s*['\"]?([^'\"\s#]+)")
FIRST_PARTY = ("actions/", "github/")
SHA = re.compile(r"^[0-9a-f]{40}$")


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def line_checks(name: str, text: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    lines = text.splitlines()
    scopes: dict[int, dict[str, int]] = {}
    block_owner: tuple[str, int] | None = None  # (key, indent) of an open block scalar
    for no, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        ind = indent_of(line)
        if block_owner and ind > block_owner[1]:
            key, _ = block_owner
            if key == "run":
                for m in INJECTION.finditer(line):
                    errors.append(f"{name}:{no}: {m.group(0)} inside run: (injection); pass it via env:")
            if key != "if" and STATUS_FN.search(line):
                errors.append(f"{name}:{no}: status function outside if: ({STATUS_FN.search(line).group(0)})")
            continue
        block_owner = None
        m = KEY.match(line)
        if not m:
            if STATUS_FN.search(line):
                errors.append(f"{name}:{no}: status function outside if: ({STATUS_FN.search(line).group(0)})")
            continue
        dash, key, value = m.group(2), m.group(3).strip("\"'"), m.group(5).strip()
        key_ind = ind + (len(dash) if dash else 0)
        for d in [k for k in scopes if k > key_ind or (dash and k >= key_ind)]:
            del scopes[d]
        seen = scopes.setdefault(key_ind, {})
        if key in seen:
            errors.append(f"{name}:{no}: duplicate key '{key}' (first at line {seen[key]})")
        else:
            seen[key] = no
        if BLOCK_SCALAR.match(value):
            block_owner = (key, key_ind)
            continue
        if key == "run":
            for mm in INJECTION.finditer(value):
                errors.append(f"{name}:{no}: {mm.group(0)} inside run: (injection); pass it via env:")
        if key != "if" and STATUS_FN.search(value):
            errors.append(f"{name}:{no}: status function outside if: ({STATUS_FN.search(value).group(0)})")
        um = USES.match(line)
        if um:
            ref = um.group(2)
            if ref.startswith(("./", "docker://")) or ref.startswith(FIRST_PARTY):
                continue
            if "@" not in ref or not SHA.match(ref.rsplit("@", 1)[1]):
                warnings.append(f"{name}:{no}: third party action not pinned to a commit SHA: {ref}")
    return errors, warnings


def structure_checks(name: str, text: str, yaml) -> list[str]:
    errors: list[str] = []
    try:
        doc = yaml.safe_load(text)
    except Exception as exc:  # noqa: BLE001 (any parser error is a finding)
        return [f"{name}: YAML does not parse: {str(exc).splitlines()[0]}"]
    if not isinstance(doc, dict):
        return [f"{name}: top level is not a mapping"]
    if "on" not in doc and True not in doc:  # PyYAML reads a bare `on` key as True
        errors.append(f"{name}: no `on` trigger")
    jobs = doc.get("jobs")
    if not isinstance(jobs, dict) or not jobs:
        errors.append(f"{name}: jobs missing or empty")
        jobs = {}
    if "permissions" not in doc:
        missing = [j for j, body in jobs.items() if not isinstance(body, dict) or "permissions" not in body]
        if missing or not jobs:
            errors.append(f"{name}: no workflow level permissions: block (jobs without one: {', '.join(missing) or 'all'})")
    return errors


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="*", help="workflow files (default: .github/workflows/*.yml|yaml)")
    ap.add_argument("--root", default=".", help="repo root (default: current directory)")
    ap.add_argument("--strict", action="store_true", help="warnings fail too")
    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    files = [Path(f) if Path(f).is_absolute() else root / f for f in args.files] or sorted(
        list((root / ".github/workflows").glob("*.yml")) + list((root / ".github/workflows").glob("*.yaml")))
    if not files:
        print("COULD NOT RUN: no workflow files found")
        print(CANNOT_COVER)
        return 2
    try:
        import yaml  # optional
    except ImportError:
        yaml = None

    errors: list[str] = []
    warnings: list[str] = []
    unreadable: list[str] = []
    for f in files:
        name = f.relative_to(root).as_posix() if f.is_relative_to(root) else str(f)
        try:
            text = f.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            unreadable.append(f"{name}: {exc}")
            continue
        e, w = line_checks(name, text)
        errors += e
        warnings += w
        if yaml is not None:
            errors += structure_checks(name, text, yaml)

    for w in warnings:
        print(f"warn  {w}")
    for e in errors:
        print(f"error {e}")
    for u in unreadable:
        print(f"could not run: {u}")
    skipped = "PyYAML missing: on, jobs and permissions checks could not run (pip install pyyaml)" if yaml is None else ""
    if skipped:
        print(f"could not run: {skipped}")
    failed = bool(errors) or (args.strict and bool(warnings))
    if failed:
        verdict, code = "FAIL", 1
    elif unreadable or skipped:
        verdict, code = "COULD NOT RUN", 2
    else:
        verdict, code = "OK", 0
    print(f"{verdict}: {len(files)} file(s), {len(errors)} error(s), {len(warnings)} warning(s)")
    print(CANNOT_COVER)
    return code


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 (an unexpected crash is "could not run", never "fail")
        print(f"COULD NOT RUN: unexpected error: {exc!r}")
        print(CANNOT_COVER)
        sys.exit(2)
