#!/usr/bin/env python3
"""Local gate: run every check against a clean clone of HEAD (Workflow Kit, review-gates skill).

Why a clean clone: uncommitted files, local caches and a half staged tree make
"works on my machine" passes. The gate clones the committed HEAD into a temp
folder, installs, runs each step, and reports PASS, FAIL or COULD NOT RUN per
step. A step that could not run is never reported as ok.

Config (workflow-kit.json at the repo root):
  "gate": {
    "install": "npm ci",                         optional
    "steps": [{"name": "lint", "run": "npm run lint"}, ...],
    "ledger": "gate/cleared.txt",                 optional, see --record
    "ci": ".github/workflows/ci.yml",             optional, see --parity
    "timeout": 1800                               seconds per step
  }
Without gate.steps the four project.checks commands are used; placeholders
(<...>) are skipped and reported as COULD NOT RUN.

  python3 gate.py                  run the gate on HEAD
  python3 gate.py --record         on a full pass, append "<sha> <utc> <host python>" to the ledger,
                                   so a deploy can ship only cleared commits
  python3 gate.py --parity         also fail when the CI workflow runs a command the gate lacks
  python3 gate.py --list           print the steps and exit
  python3 gate.py --root PATH      repository root (default: git toplevel of the cwd)

Exit codes: 0 pass, 1 fail, 2 could not run (no config, not a git repo, or a step could not run).
"""
from __future__ import annotations

import argparse
import datetime
import json
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CANNOT_COVER = ("This gate cannot cover: production data and traffic, third party services, secrets only "
                "CI has, platforms other than this machine, and anything not listed as a step.")
PLACEHOLDER = re.compile(r"<[^>]+>")


def git(args, cwd):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def load_steps(cfg):
    gate = cfg.get("gate") or {}
    steps = [s for s in gate.get("steps", []) if isinstance(s, dict) and s.get("run")]
    if not steps:
        checks = (cfg.get("project") or {}).get("checks") or {}
        steps = [{"name": k, "run": v} for k, v in checks.items() if isinstance(v, str) and v]
    return gate, steps


def ci_commands(path: Path):
    """Commands from run: lines (single line and block scalars) of one workflow file."""
    cmds, block_indent = [], None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if block_indent is not None:
            if line.strip() and (len(line) - len(line.lstrip())) > block_indent:
                cmds.append(line.strip())
                continue
            block_indent = None
        m = re.match(r"^(\s*)(-\s+)?run:\s*(.*)$", line)
        if m:
            rest = m.group(3).strip()
            if rest in ("|", ">", "|-", ">-", "|+", ">+"):
                block_indent = len(m.group(1)) + (len(m.group(2) or ""))
            elif rest:
                cmds.append(rest.strip("'\""))
    return [c for c in cmds if c and not c.startswith("#") and not c.startswith("echo ")]


def norm(cmd):
    return re.sub(r"\s+", " ", cmd.strip())


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root")
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--parity", action="store_true")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    start = Path(a.root or ".").resolve()
    top = git(["rev-parse", "--show-toplevel"], start)
    if top.returncode != 0:
        print("could not run: not inside a git repository")
        print(CANNOT_COVER)
        return 2
    root = Path(top.stdout.strip())
    cfg_path = root / "workflow-kit.json"
    try:
        cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"could not run: cannot read {cfg_path} ({exc})")
        print(CANNOT_COVER)
        return 2
    gate, steps = load_steps(cfg)
    if not steps:
        print("could not run: no gate.steps and no project.checks in workflow-kit.json")
        print(CANNOT_COVER)
        return 2
    if a.list:
        for s in steps:
            print(f"{s.get('name', '?')}: {s['run']}")
        return 0

    results, parity_missing = [], []
    if a.parity:
        ci = root / gate.get("ci", ".github/workflows/ci.yml")
        if not ci.is_file():
            results.append(("parity", "COULD NOT RUN", f"{ci.relative_to(root)} not found"))
        else:
            mine = {norm(s["run"]) for s in steps} | ({norm(gate["install"])} if gate.get("install") else set())
            parity_missing = [c for c in ci_commands(ci) if norm(c) not in mine]
            results.append(("parity", "FAIL" if parity_missing else "PASS",
                            "CI runs commands the gate lacks: " + "; ".join(parity_missing[:5])
                            if parity_missing else "every CI command is a gate step"))

    sha = git(["rev-parse", "HEAD"], root).stdout.strip()
    timeout = int(gate.get("timeout", 1800))
    tmp = Path(tempfile.mkdtemp(prefix="gate-"))
    clone = tmp / "repo"
    try:
        c = git(["clone", "-q", "--local", "--no-checkout", str(root), str(clone)], root)
        if c.returncode != 0 or git(["checkout", "-q", sha], clone).returncode != 0:
            print(f"could not run: clean clone failed ({c.stderr.strip()[:200]})")
            print(CANNOT_COVER)
            return 2
        todo = ([{"name": "install", "run": gate["install"]}] if gate.get("install") else []) + steps
        for s in todo:
            name, cmd = s.get("name", "step"), s["run"]
            if PLACEHOLDER.search(cmd):
                results.append((name, "COULD NOT RUN", "placeholder command; set it in workflow-kit.json"))
                continue
            try:
                p = subprocess.run(cmd, shell=True, cwd=clone, capture_output=True, text=True, timeout=timeout)
            except subprocess.TimeoutExpired:
                results.append((name, "FAIL", f"timed out after {timeout} s"))
                continue
            tail = (p.stdout + p.stderr).strip().splitlines()[-1:] or [""]
            if p.returncode == 127:
                results.append((name, "COULD NOT RUN", f"command not found: {tail[0][:160]}"))
            elif p.returncode == 0:
                results.append((name, "PASS", ""))
            else:
                results.append((name, "FAIL", f"exit {p.returncode}: {tail[0][:160]}"))
            if name == "install" and p.returncode != 0:
                break
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"# Gate on {sha[:12]} (clean clone)\n")
    for name, status, note in results:
        print(f"- {status:<13} {name}" + (f": {note}" if note else ""))
    failed = any(s == "FAIL" for _, s, _ in results)
    blocked = any(s == "COULD NOT RUN" for _, s, _ in results)
    if not failed and not blocked and a.record:
        ledger = root / gate.get("ledger", "gate/cleared.txt")
        ledger.parent.mkdir(parents=True, exist_ok=True)
        stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        with ledger.open("a", encoding="utf-8") as fh:
            fh.write(f"{sha} {stamp} python{platform.python_version()}\n")
        print(f"\ncleared: {sha[:12]} recorded in {ledger.relative_to(root)}")
    print("\n" + CANNOT_COVER)
    return 1 if failed else 2 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
