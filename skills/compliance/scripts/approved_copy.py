#!/usr/bin/env python3
"""Lock approved customer facing copy so it cannot change unnoticed.

After compliance approves a line or block, its exact text is recorded with a
hash in ads-master/brand/approved-copy.json. Anywhere that copy is reused
(outputs, emails, landing page source, feed text) it is wrapped in markers:

  <!-- approved:hero-claim-protein -->20 g protein per bar<!-- /approved -->

`check` then fails when the wrapped text differs from what was approved, when
the ID is unknown, or when the approval has expired. Whitespace differences
are ignored; anything else (a number, a word, a unit) is a change.

Usage:
  approved_copy.py add --id hero-claim-protein --text "20 g protein per bar" \\
      --by "Jane (compliance)" --expires 2027-04-01 [--registry PATH]
  approved_copy.py check PATH [PATH ...] [--registry PATH]
  approved_copy.py verify [--registry PATH]    # registry integrity only

Exit codes: 0 pass, 1 fail, 2 could not run. Standard library only.
Recording an approval is the human's decision; this script only writes down
what was approved and checks it later.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import sys

DEFAULT_REGISTRY = os.path.join("ads-master", "brand", "approved-copy.json")
MARK = re.compile(r"<!--\s*approved:([A-Za-z0-9_.-]+)\s*-->(.*?)<!--\s*/approved\s*-->", re.S)
TEXT_EXT = (".md", ".txt", ".html", ".htm", ".liquid", ".json", ".csv", ".tsv", ".xml",
            ".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".php", ".mjml", ".yaml", ".yml")


def norm(text):
    return re.sub(r"\s+", " ", text).strip()


def digest(text):
    return hashlib.sha256(norm(text).encode("utf-8")).hexdigest()


def load(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return data.get("entries", {}) if isinstance(data, dict) else {}


def save(path, entries):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"_comment": "Approved customer facing copy. Edit only through approved_copy.py add, after a "
                               "compliance approval. Text is matched with whitespace normalized.",
                   "entries": entries}, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


def expired(entry, today):
    exp = entry.get("expires")
    return bool(exp) and exp < today


def files_under(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
        elif os.path.isdir(p):
            for dirpath, dirs, files in os.walk(p):
                dirs[:] = [d for d in dirs if d not in {".git", "node_modules", ".next", "dist", "build"}]
                for f in files:
                    if f.endswith(TEXT_EXT):
                        yield os.path.join(dirpath, f)


def cmd_add(a):
    entries = load(a.registry) if os.path.isfile(a.registry) else {}
    if a.id in entries and not a.replace:
        print(f"FAIL: id '{a.id}' exists; pass --replace to record a new approval for it")
        return 1
    entries[a.id] = {"text": norm(a.text), "sha256": digest(a.text), "approved_by": a.by,
                     "approved_on": datetime.date.today().isoformat(), "expires": a.expires or "",
                     "channels": a.channels or "", "claim_ref": a.claim_ref or ""}
    save(a.registry, entries)
    print(f"recorded approval '{a.id}' in {a.registry}")
    return 0


def cmd_verify(entries, today):
    problems = []
    for cid, e in entries.items():
        if e.get("sha256") != digest(e.get("text", "")):
            problems.append(f"{cid}: registry text and hash disagree (edited by hand?)")
        if not e.get("approved_by"):
            problems.append(f"{cid}: no approver recorded")
        if expired(e, today):
            problems.append(f"{cid}: approval expired {e['expires']}")
    return problems


def cmd_check(entries, paths, today):
    problems, used, scanned = [], 0, 0
    for path in files_under(paths):
        scanned += 1
        try:
            text = open(path, encoding="utf-8", errors="ignore").read()
        except OSError:
            continue
        for m in MARK.finditer(text):
            used += 1
            cid, body = m.group(1), m.group(2)
            line = text.count("\n", 0, m.start()) + 1
            e = entries.get(cid)
            if not e:
                problems.append(f"{path}:{line}: unknown approval id '{cid}'")
            elif digest(body) != e.get("sha256"):
                problems.append(f"{path}:{line}: '{cid}' changed after approval: "
                                f"approved \"{e.get('text', '')[:80]}\", found \"{norm(body)[:80]}\"")
            elif expired(e, today):
                problems.append(f"{path}:{line}: '{cid}' approval expired {e['expires']}")
    return problems, used, scanned


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd")
    p_add = sub.add_parser("add")
    p_add.add_argument("--id", required=True)
    p_add.add_argument("--text", required=True)
    p_add.add_argument("--by", required=True, help="who approved it (name and role)")
    p_add.add_argument("--expires", help="YYYY-MM-DD, usually the evidence expiry in CLAIMS.md")
    p_add.add_argument("--channels")
    p_add.add_argument("--claim-ref", help="row in brand/CLAIMS.md this copy relies on")
    p_add.add_argument("--replace", action="store_true")
    p_check = sub.add_parser("check")
    p_check.add_argument("paths", nargs="+")
    sub.add_parser("verify")
    for p in (p_add, p_check, sub.choices["verify"]):
        p.add_argument("--registry", default=DEFAULT_REGISTRY)
    a = ap.parse_args()
    if not a.cmd:
        ap.print_help()
        return 2
    if a.cmd == "add":
        return cmd_add(a)
    if not os.path.isfile(a.registry):
        print(f"could not run: registry {a.registry} not found (record approvals with `add` first)")
        return 2
    try:
        entries = load(a.registry)
    except ValueError as exc:
        print(f"could not run: registry is not valid JSON ({exc})")
        return 2
    today = datetime.date.today().isoformat()
    problems = cmd_verify(entries, today)
    if a.cmd == "check":
        found, used, scanned = cmd_check(entries, a.paths, today)
        problems += found
        print(f"scanned {scanned} files, {used} approved blocks, {len(entries)} approvals on record")
    for p in problems:
        print("FAIL", p)
    print("This gate cannot cover: copy that was never wrapped in approved markers, images and video with "
          "burned in text, and claims rewritten in new words (those go to compliance review).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
