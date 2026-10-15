#!/usr/bin/env python3
"""liveops_calendar_check.py: check a LIVEOPS_CALENDAR against store limits and liveops rules.

Standard library only. Reads the Markdown template in
skills/game-liveops/references/liveops-calendar-and-store-events.md section 9 (tables
"Calendar" and, optionally, "Store event metadata") or a CSV with the Calendar columns.

Store limits used (verify with the Freshness protocol before relying on them):
  Apple In-App Events [Official, read 2026-10-12]: up to 31 days; promoted up to 14 days
  before the start; up to 10 published and 15 approved at a time; event name 30, short
  description 50, long description 120 characters; no specific prices in metadata.
  Google Play promotional content [Reported, 2026-10, search summaries]: submit no earlier
  than 60 days and at least 4 days before the start.

Usage
  python3 -I liveops_calendar_check.py ads-master/LIVEOPS_CALENDAR.md
  python3 -I liveops_calendar_check.py calendar.csv --today 2026-10-15 --json out.json

Exit codes: 0 no FAIL (warnings allowed), 1 at least one FAIL, 2 could not run.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import re
import sys

CANNOT_COVER = ("This check cannot cover: whether an event is a good idea or fair in play, whether copy is "
                "truthful or compliant (compliance decides), whether media meet Apple's visual guidance, whether "
                "the deep link opens the right screen, whether Play's live console rules still match the reported "
                "ones, the exact moment Apple counts an event as approved, and anything not written in the calendar.")

REQUIRED = ["ID", "Name", "Format", "Scale", "Start", "End", "Store", "Status"]
OPTIONAL = ["Audience", "Ranked board", "Badge", "Promo start", "Submit by", "Deep link", "Reminders",
            "Offer ref", "Holdout", "KPI", "Owner"]
FORMATS = {"milestone", "collection", "race", "cohort_leaderboard", "team_chest", "in_team_leaderboard",
           "community_goal", "challenge", "theme_week", "tournament", "premiere", "season", "league_season",
           "content_drop", "offer", "community", "holiday", "freeze"}
COMPETITIVE = {"race", "cohort_leaderboard", "in_team_leaderboard", "tournament", "league_season"}
UNMEASURED = {"content_drop", "offer", "community", "holiday", "freeze"}
SCALES = {"burst", "short", "week", "season", "annual", "none"}
STACKED_SCALES = {"burst", "short", "week", "season"}
STORES = {"none", "apple", "play", "both"}
STATUSES = {"idea", "planned", "approved", "submitted", "live", "done", "cancelled"}
INACTIVE = {"cancelled", "done"}
BADGES = {"challenge", "competition", "live event", "major update", "new season", "premiere", "special event"}
PURPOSES = {"all users", "new users", "active users", "lapsed users"}
PRIORITIES = {"normal", "high"}
EMPTY = {"", "none", "n/a", "na", "-"}

APPLE_MAX_DAYS = 31
APPLE_PROMO_DAYS = 14
APPLE_MAX_PUBLISHED = 10
APPLE_MAX_APPROVED = 15
APPLE_LIMITS = {"Event name": 30, "Short description": 50, "Long description": 120}
PLAY_EARLIEST_DAYS = 60
PLAY_LATEST_DAYS = 4

PRICE_SYMBOL_RE = re.compile(r"([$\u20ac\u00a3\u20ba\u00a5\u20b9]\s?\d)|(\d\s?[$\u20ac\u00a3\u20ba\u00a5\u20b9])|"
                             r"(\d+\s?%\s?off\b)", re.IGNORECASE)
PRICE_CODE_RE = re.compile(r"(\b(USD|EUR|GBP|TRY|TL|JPY|INR)\s?\d)|(\d\s?(USD|EUR|GBP|TRY|TL|JPY|INR)\b)")
CLAIM_RE = re.compile(r"(\bthe best\b(?!\s+(counts?|scores?|tries|try|results?|attempts?)\b)|#\s?1\b|"
                      r"\bnumber one\b|\bno\.\s?1\b|\bbest (game|app|puzzle)s?\b)", re.IGNORECASE)
EXTRA_WORDS_RE = re.compile(r"\bgame event\b", re.IGNORECASE)
CAPS_RE = re.compile(r"\b[A-Z]{4,}\b")
PRESSURE_RE = re.compile(r"(last chance|hurry|ends soon|don'?t miss|before it'?s too late|now or never|act now|"
                         r"only today|streak (is )?at risk|will expire|lose your)", re.IGNORECASE)


class CannotRun(Exception):
    """Input problem that makes the whole check meaningless."""


def norm(value: str | None) -> str:
    return (value or "").strip()


def is_empty(value: str | None) -> bool:
    return norm(value).lower() in EMPTY


def parse_when(value: str, is_end: bool) -> dt.datetime:
    """Date only: start at 00:00, end at the end of that day. Date and time: exact."""
    v = norm(value).replace("T", " ")
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"):
        try:
            return dt.datetime.strptime(v, fmt)
        except ValueError:
            pass
    day = dt.datetime.strptime(v, "%Y-%m-%d")
    return day + dt.timedelta(days=1) if is_end else day


def split_row(line: str) -> list[str]:
    cells = line.strip().strip("|").split("|")
    return [c.strip() for c in cells]


def markdown_tables(text: str) -> list[tuple[list[str], list[list[str]]]]:
    """Return (header, rows) for every pipe table outside fenced code blocks."""
    tables, header, rows, in_fence = [], None, [], False

    def close():
        nonlocal header, rows
        if header:
            tables.append((header, rows))
        header, rows = None, []

    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            close()
            in_fence = not in_fence
            i += 1
            continue
        if not in_fence and line.strip().startswith("|"):
            if header is None:
                nxt = lines[i + 1] if i + 1 < len(lines) else ""
                if re.match(r"^\s*\|?\s*:?-{3,}", nxt):
                    header = split_row(line)
                    i += 2
                    continue
            else:
                rows.append(split_row(line))
                i += 1
                continue
        close()
        i += 1
    close()
    return tables


def load(path: str) -> tuple[list[dict], list[dict]]:
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError as exc:
        raise CannotRun(f"cannot read {path}: {exc.strerror}")
    if path.lower().endswith(".csv"):
        reader = csv.DictReader(text.splitlines())
        if not reader.fieldnames:
            raise CannotRun("CSV has no header row")
        cal = [{k.strip(): norm(v) for k, v in r.items() if k} for r in reader]
        header = [h.strip() for h in reader.fieldnames]
        meta: list[dict] = []
    else:
        cal, meta, header = [], [], None
        for head, rows in markdown_tables(text):
            if "ID" in head and "Start" in head and "End" in head and header is None:
                header = head
                cal = [dict(zip(head, r + [""] * (len(head) - len(r)))) for r in rows]
            elif "ID" in head and "Event name" in head:
                meta = [dict(zip(head, r + [""] * (len(head) - len(r)))) for r in rows]
        if header is None:
            raise CannotRun("no Calendar table found (a pipe table with ID, Start and End columns)")
    missing = [c for c in REQUIRED if c not in header]
    if missing:
        raise CannotRun(f"Calendar table misses required columns: {', '.join(missing)}")
    cal = [r for r in cal if any(norm(v) for v in r.values())]
    return cal, meta


def stores_of(row: dict) -> set[str]:
    s = norm(row.get("Store")).lower()
    return {"apple", "play"} if s == "both" else ({s} if s in ("apple", "play") else set())


def check(cal: list[dict], meta: list[dict], today: dt.date | None) -> dict:
    fails, warns, infos = [], [], []
    seen: set[str] = set()
    parsed = []
    for idx, row in enumerate(cal, 1):
        rid = norm(row.get("ID")) or f"row {idx}"
        tag = rid
        if rid in seen:
            fails.append(f"{tag}: duplicate ID")
        seen.add(rid)
        fmt = norm(row.get("Format")).lower()
        scale = norm(row.get("Scale")).lower()
        store = norm(row.get("Store")).lower()
        status = norm(row.get("Status")).lower()
        if fmt not in FORMATS:
            warns.append(f"{tag}: unknown Format '{row.get('Format')}' (see the template's field values)")
        if scale not in SCALES:
            warns.append(f"{tag}: unknown Scale '{row.get('Scale')}'")
        if store not in STORES:
            fails.append(f"{tag}: Store must be none, apple, play or both (got '{row.get('Store')}')")
        if status not in STATUSES:
            warns.append(f"{tag}: unknown Status '{row.get('Status')}'")
        try:
            start = parse_when(row.get("Start", ""), False)
            end = parse_when(row.get("End", ""), True)
        except ValueError:
            fails.append(f"{tag}: Start and End must be YYYY-MM-DD or YYYY-MM-DD HH:MM")
            continue
        if end <= start:
            fails.append(f"{tag}: End is not after Start")
            continue
        rec = {"id": rid, "row": row, "format": fmt, "scale": scale, "store": store, "status": status,
               "start": start, "end": end, "promo": None, "submit": None}
        for col, key in (("Promo start", "promo"), ("Submit by", "submit")):
            if not is_empty(row.get(col)):
                try:
                    rec[key] = parse_when(row.get(col, ""), False)
                except ValueError:
                    fails.append(f"{tag}: {col} must be YYYY-MM-DD or YYYY-MM-DD HH:MM")
        parsed.append(rec)
        active = status not in INACTIVE
        st = stores_of(row)

        if "apple" in st:
            badge = norm(row.get("Badge")).lower()
            if badge not in BADGES:
                fails.append(f"{tag}: Apple event needs a Badge (Challenge, Competition, Live Event, Major Update, "
                             f"New Season, Premiere, Special Event); got '{row.get('Badge', '')}'")
            if is_empty(row.get("Deep link")):
                fails.append(f"{tag}: Apple event needs a deep link (Guideline 2.3.13)")
            days = (end - start).total_seconds() / 86400
            if days > APPLE_MAX_DAYS:
                fails.append(f"{tag}: Apple event lasts {days:g} days; the maximum is {APPLE_MAX_DAYS}")
            promo = rec["promo"] or start
            if promo > start:
                fails.append(f"{tag}: Promo start is after Start")
            if (start - promo).total_seconds() / 86400 > APPLE_PROMO_DAYS:
                fails.append(f"{tag}: Promo start is more than {APPLE_PROMO_DAYS} days before Start")
            if rec["submit"] is None:
                warns.append(f"{tag}: Apple event has no Submit by date")
            elif rec["submit"] > promo:
                fails.append(f"{tag}: Submit by is after the promotion start; approval cannot land in time")
            if fmt == "offer":
                warns.append(f"{tag}: Apple lists price promotions without new content as poor in-app event "
                             f"candidates")
        if "play" in st:
            if rec["submit"] is None:
                warns.append(f"{tag}: Play promotional content has no Submit by date")
            else:
                lead = (start - rec["submit"]).total_seconds() / 86400
                if lead < PLAY_LATEST_DAYS:
                    warns.append(f"{tag}: Play submission {lead:g} days before Start; submit at least "
                                 f"{PLAY_LATEST_DAYS} days ahead (approval can take up to 4 days) [Reported]")
                if lead > PLAY_EARLIEST_DAYS:
                    warns.append(f"{tag}: Play submission {lead:g} days before Start; the earliest is "
                                 f"{PLAY_EARLIEST_DAYS} days [Reported]")
            if is_empty(row.get("Deep link")):
                warns.append(f"{tag}: Play promotional content without a deep link")
        if fmt in COMPETITIVE and is_empty(row.get("Ranked board")):
            warns.append(f"{tag}: competitive format '{fmt}' must declare its ranked board and scope "
                         f"(group or everyone) so the monetization policy can protect it")
        if fmt == "offer" and "game-monetization" not in norm(row.get("Owner")).lower():
            warns.append(f"{tag}: offer rows are owned by game-monetization")
        if active and fmt not in ("holiday", "freeze") and not norm(row.get("KPI")):
            warns.append(f"{tag}: no KPI")
        if active and not norm(row.get("Owner")):
            warns.append(f"{tag}: no Owner")
        if PRESSURE_RE.search(norm(row.get("Name"))):
            warns.append(f"{tag}: pressure wording in Name; route to compliance (never for minors)")
        if today and active and st and rec["submit"] and status in ("idea", "planned") \
                and rec["submit"].date() < today:
            fails.append(f"{tag}: Submit by {rec['submit'].date()} has passed and the status is still {status}")
        if today and status in ("idea", "planned", "approved", "submitted") and start.date() < today:
            warns.append(f"{tag}: Start {start.date()} has passed but the status is {status}")
        if today and active and rec["submit"] and today <= rec["submit"].date() <= today + dt.timedelta(days=7):
            infos.append(f"{tag}: store submission due {rec['submit'].date()}")

    live = [r for r in parsed if r["status"] not in INACTIVE]

    # One event per scale.
    for i, a in enumerate(live):
        if a["scale"] not in STACKED_SCALES or a["format"] in ("holiday", "freeze"):
            continue
        for b in live[i + 1:]:
            if b["scale"] == a["scale"] and b["format"] not in ("holiday", "freeze") \
                    and a["start"] < b["end"] and b["start"] < a["end"]:
                warns.append(f"{a['id']} and {b['id']}: two '{a['scale']}' events overlap; one event per scale "
                             f"unless their audiences are disjoint")

    # Freeze windows.
    freezes = [r for r in live if r["format"] == "freeze"]
    for r in live:
        if r["format"] == "freeze":
            continue
        for f in freezes:
            if f["start"] <= r["start"] < f["end"]:
                warns.append(f"{r['id']}: starts inside freeze window {f['id']}")

    # Holdout coverage per measured format.
    measured = {r["format"] for r in live if r["format"] in FORMATS and r["format"] not in UNMEASURED}
    for fmt in sorted(measured):
        if not any(r["format"] == fmt and not is_empty(r["row"].get("Holdout")) for r in live):
            warns.append(f"format '{fmt}': no row has a holdout; read each format against a holdout at least once")

    # Apple concurrency.
    apple = [r for r in live if "apple" in stores_of(r["row"])]
    if apple:
        def day_span(a_from: dt.datetime, a_to: dt.datetime):
            d = a_from.date()
            last = (a_to - dt.timedelta(seconds=1)).date()
            while d <= last:
                yield d
                d += dt.timedelta(days=1)

        published: dict[dt.date, list[str]] = {}
        approved: dict[dt.date, list[str]] = {}
        high: dict[dt.date, list[str]] = {}
        meta_by_id = {norm(m.get("ID")): m for m in meta}
        for r in apple:
            promo = r["promo"] or r["start"]
            for d in day_span(promo, r["end"]):
                published.setdefault(d, []).append(r["id"])
                if norm(meta_by_id.get(r["id"], {}).get("Priority")).lower() == "high" and d >= r["start"].date():
                    high.setdefault(d, []).append(r["id"])
            for d in day_span(r["submit"] or promo, r["end"]):
                approved.setdefault(d, []).append(r["id"])
        over = sorted(d for d, ids in published.items() if len(ids) > APPLE_MAX_PUBLISHED)
        if over:
            fails.append(f"Apple: more than {APPLE_MAX_PUBLISHED} events published at once on {over[0]} "
                         f"({len(published[over[0]])}: {', '.join(published[over[0]])})")
        over = sorted(d for d, ids in approved.items() if len(ids) > APPLE_MAX_APPROVED)
        if over:
            warns.append(f"Apple: more than {APPLE_MAX_APPROVED} events approved at once around {over[0]} "
                         f"(approximated from Submit by)")
        over = sorted(d for d, ids in high.items() if len(ids) > 1)
        if over:
            warns.append(f"Apple: more than one high priority event live on {over[0]} ({', '.join(high[over[0]])})")
        for r in apple:
            if r["id"] not in meta_by_id:
                warns.append(f"{r['id']}: Apple event has no row in Store event metadata yet")

    # Store event metadata.
    ids = {r["id"] for r in parsed}
    for m in meta:
        mid = norm(m.get("ID"))
        tag = f"{mid} metadata"
        if mid and mid not in ids:
            warns.append(f"{tag}: no Calendar row with this ID")
        texts = []
        for col, limit in APPLE_LIMITS.items():
            value = norm(m.get(col))
            texts.append(value)
            if len(value) > limit:
                fails.append(f"{tag}: {col} has {len(value)} characters; the limit is {limit}")
        for value in texts:
            if PRICE_SYMBOL_RE.search(value) or PRICE_CODE_RE.search(value):
                fails.append(f"{tag}: specific pricing in event metadata leads to rejection ('{value}')")
            if CLAIM_RE.search(value):
                warns.append(f"{tag}: avoid unverifiable claims such as 'best' or '#1' ('{value}')")
            if EXTRA_WORDS_RE.search(value):
                warns.append(f"{tag}: avoid extra words such as 'game event' ('{value}')")
            if CAPS_RE.search(value):
                warns.append(f"{tag}: avoid all capital words ('{value}')")
            if "!!" in value:
                warns.append(f"{tag}: avoid repeated exclamation marks ('{value}')")
            if PRESSURE_RE.search(value):
                warns.append(f"{tag}: pressure wording; route to compliance, never for minors ('{value}')")
        purpose = norm(m.get("Purpose")).lower()
        if purpose and purpose not in PURPOSES:
            warns.append(f"{tag}: Purpose should be all users, new users, active users or lapsed users")
        priority = norm(m.get("Priority")).lower()
        if priority and priority not in PRIORITIES:
            warns.append(f"{tag}: Priority should be normal or high")

    return {"fails": fails, "warnings": warns, "info": infos, "rows": len(cal), "metadata_rows": len(meta)}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Check a LIVEOPS_CALENDAR against store limits and liveops rules.")
    ap.add_argument("calendar", help="LIVEOPS_CALENDAR.md (template tables) or a CSV with the Calendar columns")
    ap.add_argument("--today", help="YYYY-MM-DD: also check deadlines against this date")
    ap.add_argument("--json", help="write the result as JSON to this path")
    args = ap.parse_args(argv)
    try:
        today = dt.datetime.strptime(args.today, "%Y-%m-%d").date() if args.today else None
    except ValueError:
        print("ERROR --today must be YYYY-MM-DD")
        print(CANNOT_COVER)
        return 2
    try:
        cal, meta = load(args.calendar)
    except CannotRun as exc:
        print(f"ERROR {exc}")
        print(CANNOT_COVER)
        return 2
    if not cal:
        print("ERROR the Calendar table has no rows")
        print(CANNOT_COVER)
        return 2
    res = check(cal, meta, today)
    for line in res["fails"]:
        print(f"FAIL {line}")
    for line in res["warnings"]:
        print(f"WARN {line}")
    for line in res["info"]:
        print(f"INFO {line}")
    print(f"\n{res['rows']} calendar rows, {res['metadata_rows']} metadata rows, "
          f"{len(res['fails'])} FAIL, {len(res['warnings'])} WARN")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=2)
    print(CANNOT_COVER)
    return 1 if res["fails"] else 0


if __name__ == "__main__":
    sys.exit(main())
