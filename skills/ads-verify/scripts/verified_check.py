#!/usr/bin/env python3
"""Check ads-master/VERIFIED.md: every row complete, valid and not expired.

A verified fact is only as good as its record. This fails on rows with no
evidence, no level, an unknown level, missing or malformed dates, an expiry
before the verification date, or an expiry in the past. Rows expiring within
--soon days (default 14) are listed as warnings so the monthly verification
pass can renew them before a decision leans on a stale fact.

Usage:
  python3 verified_check.py [ads-master/VERIFIED.md] [--soon 14] [--today YYYY-MM-DD]

Exit codes: 0 pass, 1 fail, 2 could not run. Standard library only.
"""
import argparse
import datetime
import os
import re
import sys

LEVEL = re.compile(r"\bL([1-4])\b")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def rows(path):
    header, out = None, []
    with open(path, encoding="utf-8") as fh:
        for no, line in enumerate(fh, 1):
            if not line.lstrip().startswith("|"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if header is None:
                header = [c.lower() for c in cells]
                continue
            if all(set(c) <= set("-: ") for c in cells):
                continue
            if not any(cells):
                continue
            out.append((no, dict(zip(header, cells))))
    return header, out


def col(row, name):
    for k, v in row.items():
        if k.startswith(name):
            return v
    return ""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", nargs="?", default=os.path.join("ads-master", "VERIFIED.md"))
    ap.add_argument("--soon", type=int, default=14)
    ap.add_argument("--today")
    a = ap.parse_args()
    if not os.path.isfile(a.path):
        print(f"could not run: {a.path} not found (run /ads-setup first)")
        return 2
    header, data = rows(a.path)
    if not header or "claim" not in header[0]:
        print("could not run: no VERIFIED table with a Claim column found")
        return 2
    today = a.today or datetime.date.today().isoformat()
    soon = (datetime.date.fromisoformat(today) + datetime.timedelta(days=a.soon)).isoformat()
    fails, warns = [], []
    for no, r in data:
        claim = col(r, "claim") or "(no claim text)"
        tag = f"line {no} '{claim[:60]}'"
        level, evidence = col(r, "level"), col(r, "evidence")
        verified, expires = col(r, "verified"), col(r, "expires")
        if not col(r, "claim"):
            fails.append(f"{tag}: claim text missing")
        if not LEVEL.search(level):
            fails.append(f"{tag}: level must be L1, L2, L3 or L4 (found '{level}')")
        if not evidence:
            fails.append(f"{tag}: evidence missing (link, export name or test id)")
        if not DATE.match(verified):
            fails.append(f"{tag}: verified date missing or not YYYY-MM-DD")
        if not DATE.match(expires):
            fails.append(f"{tag}: expiry missing or not YYYY-MM-DD (every fact expires)")
        elif DATE.match(verified) and expires < verified:
            fails.append(f"{tag}: expires before it was verified")
        elif expires < today:
            fails.append(f"{tag}: expired {expires}; re-verify before any decision uses it")
        elif expires <= soon:
            warns.append(f"{tag}: expires {expires}")
        if LEVEL.search(level) and LEVEL.search(level).group(1) == "3":
            warns.append(f"{tag}: L3 is enough for planning, not for money, price, live or public claim decisions")
    print(f"{len(data)} verified rows checked against {today}")
    for f in fails:
        print("FAIL", f)
    for w in warns:
        print("WARN", w)
    print("This gate cannot cover: whether the evidence actually says what the row claims "
          "(that is the verifier's job), and claims used in decisions without a row here.")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
