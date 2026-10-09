#!/usr/bin/env python3
"""Find secrets in the working tree and, with --history, in every commit ever made.

Removing a key from the latest commit does not remove it from git: anyone with
the repo history still has it. So a key found in history must be rotated
(revoked and replaced in the provider console), not just deleted.

Findings are masked (first 4 and last 2 characters) so this script never
prints a usable secret.

  python3 secret_scan.py                  tracked files in the working tree
  python3 secret_scan.py --history        plus every blob in every commit (all refs)
  python3 secret_scan.py --root PATH      repository root (default: git toplevel of the cwd)
  python3 secret_scan.py --allow FILE     file of regexes for known false positives (one per line)

Exit codes: 0 no findings, 1 findings, 2 could not run (not a git repository).
Standard library only. Pattern list is a starting point, not a guarantee.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

CANNOT_COVER = ("This gate cannot cover: secrets in other repositories, CI logs, chat or tickets, build "
                "artifacts and deployed bundles not in git, and key formats not in the pattern list.")

PATTERNS = [
    ("Anthropic key", r"(?<![A-Za-z0-9_\-])sk-ant-[A-Za-z0-9_\-]{20,}"),
    ("OpenAI style key", r"(?<![A-Za-z0-9_\-])sk-(?:proj-)?[A-Za-z0-9_\-]{32,}"),
    ("Stripe live key", r"(?:sk|rk)_live_[0-9a-zA-Z]{20,}"),
    ("AWS access key id", r"AKIA[0-9A-Z]{16}"),
    ("Google API key", r"AIza[0-9A-Za-z_\-]{35}"),
    ("Google OAuth token", r"ya29\.[0-9A-Za-z_\-]{30,}"),
    ("GitHub token", r"gh[pousr]_[A-Za-z0-9]{36,}"),
    ("Slack token", r"xox[baprs]-[0-9A-Za-z\-]{10,}"),
    ("Meta access token", r"EAA[A-Za-z0-9]{40,}"),
    ("Shopify token", r"shp(?:at|ca|pa|ss)_[a-fA-F0-9]{32}"),
    ("Supabase service role JWT", r"eyJhbGciOi[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{40,}\.[A-Za-z0-9_\-]{20,}"),
    ("Private key block", r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |)PRIVATE KEY-----"),
    ("Generic assignment", r"(?i)(?:api[_-]?key|secret|password|token)\s*[:=]\s*['\"](?=[A-Za-z_\-/+=]*\d)[A-Za-z0-9_\-/+=]{20,}['\"]"),
]
COMPILED = [(n, re.compile(p)) for n, p in PATTERNS]
SKIP_SUFFIX = (".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".woff", ".woff2", ".ttf", ".zip",
               ".gz", ".mp4", ".mov", ".lock")
SAFE_FILES = re.compile(r"(^|/)\.env\.(example|sample|template)$")


def git(args, cwd, binary=False):
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=not binary)


def mask(s: str) -> str:
    return s[:4] + "*" * max(len(s) - 6, 3) + s[-2:] if len(s) > 8 else "***"


def scan_text(text: str, allow):
    for name, rx in COMPILED:
        for m in rx.finditer(text):
            hit = m.group(0)
            if any(a.search(hit) for a in allow):
                continue
            yield name, hit


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root")
    ap.add_argument("--history", action="store_true")
    ap.add_argument("--allow")
    a = ap.parse_args()
    top = git(["rev-parse", "--show-toplevel"], Path(a.root or ".").resolve())
    if top.returncode != 0:
        print("could not run: not inside a git repository")
        print(CANNOT_COVER)
        return 2
    root = Path(top.stdout.strip())
    allow = []
    if a.allow:
        try:
            allow = [re.compile(l.strip()) for l in Path(a.allow).read_text().splitlines() if l.strip()]
        except (OSError, re.error) as exc:
            print(f"could not run: bad allow file ({exc})")
            return 2

    findings = {}  # (kind, masked) -> set of locations
    files = git(["ls-files", "-z"], root).stdout.split("\0")
    for f in filter(None, files):
        if f.endswith(SKIP_SUFFIX) or SAFE_FILES.search(f):
            continue
        p = root / f
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for kind, hit in scan_text(text, allow):
            findings.setdefault((kind, mask(hit)), set()).add(f"working tree: {f}")

    if a.history:
        objs = git(["rev-list", "--all", "--objects"], root).stdout.splitlines()
        seen = set()
        for line in objs:
            parts = line.split(" ", 1)
            if len(parts) != 2 or parts[0] in seen:
                continue
            sha, path = parts
            seen.add(sha)
            if path.endswith(SKIP_SUFFIX) or SAFE_FILES.search(path):
                continue
            if git(["cat-file", "-t", sha], root).stdout.strip() != "blob":
                continue
            blob = git(["cat-file", "-p", sha], root, binary=True).stdout
            if b"\0" in blob[:4096]:
                continue
            for kind, hit in scan_text(blob.decode("utf-8", "ignore"), allow):
                key = (kind, mask(hit))
                first = git(["log", "--all", "--format=%h %ad", "--date=short", "-1", "--find-object=" + sha],
                            root).stdout.strip()
                findings.setdefault(key, set()).add(f"history: {path} ({first or 'commit unknown'})")

    for (kind, masked), where in sorted(findings.items()):
        in_history = any(w.startswith("history") for w in where)
        print(f"FAIL {kind} {masked}")
        for w in sorted(where):
            print(f"     {w}")
        if in_history:
            print("     action: rotate this key in the provider console (revoke, replace, update env); "
                  "deleting it from git does not remove it from history")
    print(f"{len(findings)} distinct secret(s) found" + (" (working tree and history)" if a.history else
                                                          " (working tree only; add --history before launch)"))
    print(CANNOT_COVER)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
