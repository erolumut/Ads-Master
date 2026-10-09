#!/usr/bin/env python3
"""Check a filled LAUNCH-READINESS.md: no launch while a Blocker is unproved.

Reads the checklist table (columns #, Item, Severity, How to prove it, Status,
Evidence, Checked on) and fails when:
  - a Blocker is FAIL or OPEN
  - any PASS has no evidence, or evidence that is only a word like "done" or "ok"
  - any NA has no reason in Evidence
  - a status is not PASS, FAIL, OPEN or NA
  - a PASS older than --max-age days (default 30) before the check date
Warn rows that are not PASS are listed as follow ups, not failures.

  python3 launch_check.py docs/LAUNCH-READINESS.md
  python3 launch_check.py docs/LAUNCH-READINESS.md --max-age 14 --today 2026-10-09

Exit codes: 0 ready (a human still decides GO), 1 not ready, 2 could not run.
Standard library only.
"""
from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

CANNOT_COVER = ("This gate cannot cover: whether the evidence is true (a reviewer or verifier re-checks it), "
                "items missing from the list, and anything that changed after the Checked on date.")
EMPTY_EVIDENCE = re.compile(r"^(done|ok|okay|yes|fine|checked|looks (good|fine)|n/?a|-|tbd|todo)?\.?$", re.I)


def rows(text: str):
    header = None
    for no, line in enumerate(text.splitlines(), 1):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = [c.lower() for c in cells]
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        yield no, dict(zip(header, cells))


def col(row, name):
    for k, v in row.items():
        if k.startswith(name):
            return v
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", nargs="?", default="docs/LAUNCH-READINESS.md")
    ap.add_argument("--max-age", type=int, default=30)
    ap.add_argument("--today")
    a = ap.parse_args()
    p = Path(a.path)
    if not p.is_file():
        print(f"could not run: {p} not found (copy templates/LAUNCH-READINESS.md first)")
        print(CANNOT_COVER)
        return 2
    data = [(n, r) for n, r in rows(p.read_text(encoding="utf-8")) if col(r, "item")]
    if not data or "severity" not in "".join(data[0][1].keys()):
        print("could not run: no checklist table with Item, Severity and Status columns")
        print(CANNOT_COVER)
        return 2
    today = datetime.date.fromisoformat(a.today) if a.today else datetime.date.today()
    fails, follow = [], []
    counts = {"PASS": 0, "FAIL": 0, "OPEN": 0, "NA": 0}
    for no, r in data:
        item, sev = col(r, "item"), col(r, "severity").lower()
        status, ev, when = col(r, "status").upper(), col(r, "evidence"), col(r, "checked")
        tag = f"line {no} #{col(r, '#')} {item[:60]}"
        if status not in counts:
            fails.append(f"{tag}: status '{status}' is not PASS, FAIL, OPEN or NA")
            continue
        counts[status] += 1
        if status == "PASS":
            if EMPTY_EVIDENCE.match(ev):
                fails.append(f"{tag}: PASS without evidence another person can re-check")
            try:
                d = datetime.date.fromisoformat(when)
                if (today - d).days > a.max_age:
                    fails.append(f"{tag}: evidence from {when} is older than {a.max_age} days; re-check")
            except ValueError:
                fails.append(f"{tag}: Checked on must be YYYY-MM-DD for a PASS")
        elif status == "NA":
            if EMPTY_EVIDENCE.match(ev):
                fails.append(f"{tag}: NA needs a reason in Evidence")
        elif sev.startswith("blocker"):
            fails.append(f"{tag}: Blocker is {status}")
        else:
            follow.append(f"{tag}: Warn is {status}; name an owner and a date")
    print(f"{len(data)} items: {counts['PASS']} PASS, {counts['NA']} NA, {counts['OPEN']} OPEN, {counts['FAIL']} FAIL")
    for f in fails:
        print("FAIL", f)
    for w in follow:
        print("WARN", w)
    print("Verdict: " + ("NOT READY" if fails else "READY for a human GO decision"))
    print(CANNOT_COVER)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
