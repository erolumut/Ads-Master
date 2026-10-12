#!/usr/bin/env python3
"""Check App Store and Google Play metadata drafts before anyone pastes them into a console.

Input: a JSON file with one entry per store and locale.

  [{"store": "apple", "locale": "en-US",
    "name": "Acme: Habit Tracker", "subtitle": "Daily goals and streaks",
    "keywords": "routine,planner,reminder,streak,goals",
    "promotional_text": "...", "description": "...",
    "captions": ["Build habits that stick", "See your streaks", "Reminders that adapt"],
    "target_terms": ["habit tracker", "daily planner", "goal reminder"]},
   {"store": "google", "locale": "en-US",
    "title": "Acme: Habit Tracker", "short_description": "...", "full_description": "...",
    "target_terms": ["habit tracker"]}]

Checks (FAIL blocks, WARN advises):
  Apple: field limits (name, subtitle, keyword field, promotional text,
    description); keyword field in bytes as well as characters; spaces after
    commas and duplicate keywords (wasted space); keywords already in name or
    subtitle (wasted, Apple combines fields); competitor names; target term
    coverage across name, subtitle and keyword field; the description is NOT a
    search field on the App Store, so it is written for people and AI readers.
  Google Play: field limits; performance, rank, price and promo terms the
    metadata policy restricts in the title (warned in the short description) (free, #1, best, top, sale and similar, emoji, all
    caps); keyword repetition in the full description (spam risk); target term
    coverage in title, short and full description.
  Both: up to N captions (first three matter most), caption length, empty fields.

Limits live in LIMITS below with their source labels; re-verify them in the
Freshness Protocol and update this table, not the logic.

Usage:
  python3 -I aso_metadata_check.py drafts.json [--competitors competitors.txt]

Exit codes: 0 pass (warnings allowed), 1 at least one FAIL, 2 could not run.
Standard library only. Claims still go through compliance (claims_check.py).
"""
import argparse
import json
import re
import sys
import unicodedata
from collections import Counter

# Field limits. Labels say how sure we are; the Freshness Protocol re-checks them.
LIMITS = {
    "apple": {"name": 30, "subtitle": 30, "keywords": 100, "promotional_text": 170, "description": 4000},
    "google": {"title": 30, "short_description": 80, "full_description": 4000},
}
LIMIT_LABEL = "[Official: App Store Connect Help and Play Console Help field limits; re-verify each quarter]"
PLAY_RESTRICTED = re.compile(
    r"(?<!\w)(free|#\s?1|no\.?\s?1|number one|best|top|sale|discount|cheap(est)?|new|hot|million downloads|"
    r"app of the year|editor'?s choice)(?!\w)", re.I)
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
STOP = {"app", "apps", "the", "and", "for", "a", "an", "of", "with", "free", "best"}


def words(s):
    return [w for w in re.findall(r"[\w']+", (s or "").lower()) if w]


def length(s):
    return len(unicodedata.normalize("NFC", s or ""))


def check_apple(e, competitors, out):
    for f, lim in LIMITS["apple"].items():
        v = e.get(f, "")
        if f == "keywords":
            if len(v.encode("utf-8")) > lim:
                out.append(("WARN" if length(v) <= lim else "FAIL",
                            f"keywords: {length(v)} characters, {len(v.encode('utf-8'))} bytes; limit {lim} "
                            "(App Store Connect may count bytes for non Latin scripts; verify in the console)"))
        elif length(v) > lim:
            out.append(("FAIL", f"{f}: {length(v)} characters, limit {lim}"))
    for f in ("name", "keywords"):
        if not e.get(f):
            out.append(("FAIL", f"{f}: empty"))
    kw = e.get("keywords", "")
    if re.search(r",\s", kw):
        out.append(("WARN", "keywords: spaces after commas waste characters"))
    items = [k.strip().lower() for k in kw.split(",") if k.strip()]
    dup = [k for k, n in Counter(items).items() if n > 1]
    if dup:
        out.append(("WARN", f"keywords: duplicates {dup}"))
    title_words = set(words(e.get("name")) + words(e.get("subtitle")))
    wasted = sorted({w for k in items for w in words(k)} & title_words)
    if wasted:
        out.append(("WARN", f"keywords: already in name or subtitle, usually wasted: {wasted}"))
    stops = sorted({w for k in items for w in words(k)} & STOP)
    if stops:
        out.append(("WARN", f"keywords: low value words {stops}"))
    indexed = title_words | {w for k in items for w in words(k)}
    for t in e.get("target_terms", []):
        tw = words(t)
        if not tw:
            continue
        if all(w in indexed for w in tw):
            strong = t.lower() in (e.get("name", "") + " " + e.get("subtitle", "")).lower()
            out.append(("OK", f"term '{t}': covered{' (exact phrase in name or subtitle)' if strong else ' (combined across fields)'}"))
        else:
            missing = [w for w in tw if w not in indexed]
            out.append(("WARN", f"term '{t}': not coverable, missing {missing} in name, subtitle and keyword field"))
    text = " ".join(str(e.get(f, "")) for f in ("name", "subtitle", "keywords")).lower()
    hits = [c for c in competitors if c and re.search(r"(?<!\w)" + re.escape(c.lower()) + r"(?!\w)", text)]
    if hits:
        out.append(("FAIL", f"competitor names in indexed fields {hits} (App Review and trademark risk)"))


def check_google(e, out):
    for f, lim in LIMITS["google"].items():
        if length(e.get(f, "")) > lim:
            out.append(("FAIL", f"{f}: {length(e.get(f, ''))} characters, limit {lim}"))
        if not e.get(f):
            out.append(("FAIL", f"{f}: empty"))
    for f in ("title", "short_description"):
        v = e.get(f, "")
        m = PLAY_RESTRICTED.findall(v)
        level = "FAIL" if f == "title" else "WARN"  # the metadata policy names title, icon and developer name
        if m:
            out.append((level, f"{f}: performance, rank, price or promo terms {sorted({x[0].lower() for x in m})} "
                               "(Play metadata policy for the title; risky elsewhere)"))
        if EMOJI.search(v):
            out.append((level, f"{f}: emoji (metadata policy for the title; reported since 2021)"))
        if re.search(r"\b[A-Z]{4,}\b", v) and v.upper() != v:
            out.append(("WARN", f"{f}: all caps word (policy risk unless it is a brand name)"))
    full = words(e.get("full_description"))
    if full:
        top = [(w, n) for w, n in Counter(w for w in full if w not in STOP and len(w) > 3).most_common(5)]
        for w, n in top:
            if n / len(full) > 0.03 and n >= 6:
                out.append(("WARN", f"full_description: '{w}' is {n / len(full):.1%} of words; repetition reads as spam"))
    hay = {f: (e.get(f) or "").lower() for f in ("title", "short_description", "full_description")}
    for t in e.get("target_terms", []):
        where = [f for f, v in hay.items() if t.lower() in v]
        out.append(("OK" if where else "WARN", f"term '{t}': {'in ' + ', '.join(where) if where else 'not present'}"))


def check_captions(e, out):
    caps = e.get("captions") or []
    if not caps:
        return
    if len(caps) < 3:
        out.append(("WARN", f"captions: {len(caps)} provided; the first three screenshots carry most of the decision"))
    for i, c in enumerate(caps[:10], 1):
        if length(c) > 50:
            out.append(("WARN", f"caption {i}: {length(c)} characters; long captions are unreadable in search results"))
    dup = [c for c, n in Counter(c.strip().lower() for c in caps).items() if n > 1]
    if dup:
        out.append(("WARN", f"captions: duplicates {dup}"))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("drafts")
    ap.add_argument("--competitors", help="text file, one competitor or brand name per line")
    a = ap.parse_args()
    try:
        entries = json.load(open(a.drafts, encoding="utf-8"))
        entries = entries if isinstance(entries, list) else [entries]
        comps = [l.strip() for l in open(a.competitors, encoding="utf-8")] if a.competitors else []
    except (OSError, ValueError) as exc:
        print(f"could not run: {exc}")
        return 2
    failed = False
    for e in entries:
        store = (e.get("store") or "").lower()
        out = []
        if store == "apple":
            check_apple(e, comps, out)
        elif store == "google":
            check_google(e, out)
        else:
            print(f"could not run: entry store must be 'apple' or 'google' (got '{store}')")
            return 2
        check_captions(e, out)
        print(f"\n## {store} {e.get('locale', '?')}")
        for level, msg in out:
            print(f"{level:<4} {msg}")
        failed |= any(level == "FAIL" for level, _ in out)
    print(f"\nLimits: {LIMIT_LABEL}")
    print("This gate cannot cover: how each store actually ranks the terms, search volume and difficulty "
          "(use the term map and rank reads), screenshot design, and claims (run compliance).")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
