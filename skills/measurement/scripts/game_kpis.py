#!/usr/bin/env python3
"""game_kpis.py: core game KPIs from a raw event export (Python 3 standard library only).

Computes, with the definitions in skills/measurement/references/game-kpis.md:
  - DAU (on the as-of day), WAU (7 days), MAU (30 days), stickiness (average DAU over 30 days / MAU)
  - classic D1, D7 and D30 retention by install cohort; install = first activity day in the
    chosen timezone; a cohort is reported for day N only when day N is complete (mature);
    pooled rates are ratios of sums with a Wilson 95% interval
  - ARPDAU split into IAP and ads, payer conversion and ARPPU over a window (default 7 days),
    plus a daily table
  - churn by last level: players inactive for --churn-days whose last level was N / players
    who reached N
  - optional retention gates (PASS, FAIL or CANNOT JUDGE when the pooled cohort is smaller
    than --min-cohort)

Input CSV (one row per event)
  required: user_id, ts (ISO 8601 with an offset; a trailing Z is accepted), event
  optional: revenue      decimal in major units of ONE currency, signed: write purchase_refunded
                         value as a negative number; if the events store integer minor units
                         (catalog prices do), divide in the export query
            revenue_type iap | ad (required when revenue is not zero)
            level        integer in progression order (labels like "w2-l3" disable churn by level)
            currency     ISO 4217; more than one value stops the run
            transaction_id  IAP rows sharing (transaction_id, sign) are counted once
            game         filter rows with --game when one product holds many games

Usage
  python3 game_kpis.py events.csv --timezone Europe/Istanbul --as-of 2026-10-10
  python3 game_kpis.py events.csv --as-of 2026-10-10 --min-cohort 1000 --gates gates.json --json out.json

gates.json: {"d1": 0.30, "d7": 0.10, "d30": 0.03} (fractions, not percent)

Activity: every event is activity except --non-activity-events (default: server side
purchase_refunded, entitlement_granted, entitlement_revoked), because a server notification does
not prove the player opened the game.

Exit codes: 0 report (and every gate PASS), 1 a gate FAILED, 2 could not run or a gate could not
be judged (pooled cohort under --min-cohort). A FAIL outranks a CANNOT JUDGE.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import math
import re
import sys
from collections import defaultdict
from decimal import Decimal, InvalidOperation

CANNOT_COVER = ("This check cannot cover: whether the export holds every event (SDK loss, consent, ad blockers, "
                "offline queues), whether revenue is gross or net of store fees and tax (it reports what the "
                "file holds), ad revenue that mediation estimates before payout, installs that never sent an "
                "event, players whose history started before the export (they look like installs on the first "
                "day; use --cohorts-from), and cause: a gate PASS says the curve met a threshold, not why.")
DEFAULT_NON_ACTIVITY = "purchase_refunded,entitlement_granted,entitlement_revoked"
RETENTION_DAYS = (1, 7, 30)
Z95 = 1.96
OFFSET_RE = re.compile(r"^([+-])(\d{2}):(\d{2})$")


class CannotRun(Exception):
    """Input problem that makes every number untrustworthy."""


def parse_tz(name: str) -> dt.tzinfo:
    if name.upper() in ("UTC", "Z", "+00:00"):
        return dt.timezone.utc
    m = OFFSET_RE.match(name)
    if m:
        sign = 1 if m.group(1) == "+" else -1
        return dt.timezone(sign * dt.timedelta(hours=int(m.group(2)), minutes=int(m.group(3))))
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo(name)
    except Exception as exc:  # ZoneInfoNotFoundError, ValueError, missing tzdata
        raise CannotRun(f"unknown timezone {name!r} ({exc.__class__.__name__}); use an IANA name or +HH:MM")


def parse_date(value: str, what: str) -> dt.date:
    try:
        return dt.date.fromisoformat(value.strip())
    except ValueError:
        raise CannotRun(f"{what}: {value!r} is not a date (YYYY-MM-DD)")


def parse_ts(value: str, line: int) -> tuple[dt.datetime, bool]:
    s = (value or "").strip()
    if s.endswith(("Z", "z")):
        s = s[:-1] + "+00:00"
    try:
        t = dt.datetime.fromisoformat(s)
    except ValueError:
        raise CannotRun(f"line {line}: ts {value!r} is not ISO 8601")
    naive = t.tzinfo is None
    if naive:
        t = t.replace(tzinfo=dt.timezone.utc)
    return t, naive


def rnd(x, places: int = 6):
    if x is None:
        return None
    return round(float(x), places)


def wilson(k: int, n: int) -> list[float] | None:
    if n <= 0:
        return None
    p = k / n
    z2 = Z95 * Z95
    denom = 1 + z2 / n
    centre = (p + z2 / (2 * n)) / denom
    half = Z95 * math.sqrt(p * (1 - p) / n + z2 / (4 * n * n)) / denom
    return [round(max(0.0, centre - half), 4), round(min(1.0, centre + half), 4)]


def load(path: str, tz: dt.tzinfo, game: str | None, non_activity: set[str]) -> dict:
    try:
        fh = open(path, newline="", encoding="utf-8-sig")
    except OSError as exc:
        raise CannotRun(f"cannot open {path}: {exc}")
    with fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise CannotRun(f"{path} has no header")
        fields = [f.strip().lower() for f in reader.fieldnames]
        reader.fieldnames = fields
        missing = [c for c in ("user_id", "ts", "event") if c not in fields]
        if missing:
            raise CannotRun(f"missing required column(s): {', '.join(missing)}")
        if game is not None and "game" not in fields:
            raise CannotRun("--game given but the file has no game column")
        rows = []
        for line, row in enumerate(reader, start=2):
            if game is not None and (row.get("game") or "").strip() != game:
                continue
            user = (row.get("user_id") or "").strip()
            event = (row.get("event") or "").strip()
            if not user or not event:
                raise CannotRun(f"line {line}: empty user_id or event")
            t, naive = parse_ts(row.get("ts", ""), line)
            raw_rev = (row.get("revenue") or "").strip()
            try:
                revenue = Decimal(raw_rev) if raw_rev else Decimal(0)
            except InvalidOperation:
                raise CannotRun(f"line {line}: revenue {raw_rev!r} is not a number")
            rtype = (row.get("revenue_type") or "").strip().lower()
            if revenue != 0 and rtype not in ("iap", "ad"):
                raise CannotRun(f"line {line}: revenue {raw_rev} needs revenue_type iap or ad, got {rtype!r}")
            raw_level = (row.get("level") or "").strip()
            rows.append({
                "line": line, "user": user, "event": event, "utc": t.astimezone(dt.timezone.utc),
                "date": t.astimezone(tz).date(), "naive": naive, "revenue": revenue, "rtype": rtype,
                "level": raw_level, "currency": (row.get("currency") or "").strip().upper(),
                "txn": (row.get("transaction_id") or "").strip(),
                "activity": event not in non_activity,
            })
    if not rows:
        raise CannotRun("no event rows (after the --game filter)" if game else "no event rows")
    currencies = {r["currency"] for r in rows if r["currency"] and r["revenue"] != 0}
    if len(currencies) > 1:
        raise CannotRun(f"revenue in more than one currency ({', '.join(sorted(currencies))}); convert to one first")
    return {"rows": rows, "currency": currencies.pop() if currencies else None}


def compute(data: dict, as_of: dt.date | None, window: int, churn_days: int, min_cohort: int,
            cohorts_from: dt.date | None) -> dict:
    rows = data["rows"]
    max_date = max(r["date"] for r in rows)
    as_of_source = "argument"
    if as_of is None:
        as_of = max_date - dt.timedelta(days=1)
        as_of_source = "default: the day before the latest event date, which is usually partial"
    kept = [r for r in rows if r["date"] <= as_of]
    after = len(rows) - len(kept)

    activity: dict[str, set] = defaultdict(set)
    by_date: dict[dt.date, set] = defaultdict(set)
    level_events: dict[str, list] = defaultdict(list)
    bad_levels = 0
    for r in kept:
        if not r["activity"]:
            continue
        activity[r["user"]].add(r["date"])
        by_date[r["date"]].add(r["user"])
        if r["level"]:
            try:
                level_events[r["user"]].append((r["utc"], r["line"], int(r["level"])))
            except ValueError:
                bad_levels += 1
    if not activity:
        raise CannotRun(f"no activity on or before as-of {as_of}")

    # Revenue: IAP rows deduplicated on (transaction_id, sign).
    seen_txn: set = set()
    dup = 0
    rev_day: dict[dt.date, dict] = defaultdict(lambda: defaultdict(Decimal))   # date -> (user, type) -> amount
    for r in kept:
        if r["revenue"] == 0:
            continue
        if r["rtype"] == "iap" and r["txn"]:
            key = (r["txn"], r["revenue"] > 0)
            if key in seen_txn:
                dup += 1
                continue
            seen_txn.add(key)
        rev_day[r["date"]][(r["user"], r["rtype"])] += r["revenue"]

    def days_back(n: int) -> list[dt.date]:
        return [as_of - dt.timedelta(days=i) for i in range(n - 1, -1, -1)]

    # Activity
    days30 = days_back(30)
    mau_users = set().union(*(by_date.get(d, set()) for d in days30))
    wau_users = set().union(*(by_date.get(d, set()) for d in days_back(7)))
    dau = len(by_date.get(as_of, set()))
    avg_dau = sum(len(by_date.get(d, set())) for d in days30) / 30
    act = {"dau": dau, "wau": len(wau_users), "mau": len(mau_users), "avg_dau_30d": rnd(avg_dau),
           "stickiness": rnd(avg_dau / len(mau_users)) if mau_users else None}

    # Retention (classic, calendar days in the chosen timezone)
    install = {u: min(ds) for u, ds in activity.items()}
    installs_per_day: dict[dt.date, int] = defaultdict(int)
    for d in install.values():
        installs_per_day[d] += 1
    cohorts: dict[dt.date, list] = defaultdict(list)
    for u, d in install.items():
        if cohorts_from is None or d >= cohorts_from:
            cohorts[d].append(u)
    cohort_rows = []
    pooled = {n: {"cohorts": 0, "cohort_users": 0, "retained": 0} for n in RETENTION_DAYS}
    for d in sorted(cohorts):
        users = cohorts[d]
        row = {"install_date": d.isoformat(), "size": len(users)}
        for n in RETENTION_DAYS:
            target = d + dt.timedelta(days=n)
            if target > as_of:
                row[f"d{n}"] = None
                continue
            kept_n = sum(1 for u in users if target in activity[u])
            row[f"d{n}"] = {"retained": kept_n, "rate": rnd(kept_n / len(users))}
            pooled[n]["cohorts"] += 1
            pooled[n]["cohort_users"] += len(users)
            pooled[n]["retained"] += kept_n
        cohort_rows.append(row)
    pooled_out = {}
    for n in RETENTION_DAYS:
        p = pooled[n]
        if p["cohort_users"] == 0:
            pooled_out[f"d{n}"] = None
            continue
        pooled_out[f"d{n}"] = {
            "cohorts": p["cohorts"], "cohort_users": p["cohort_users"], "retained": p["retained"],
            "rate": rnd(p["retained"] / p["cohort_users"]), "ci95": wilson(p["retained"], p["cohort_users"]),
            "below_min_cohort": p["cohort_users"] < min_cohort,
        }

    # Monetization window
    wdays = days_back(window)
    day_rows = []
    window_users: set = set()
    tot_iap = tot_ad = Decimal(0)
    dau_days = 0
    user_iap: dict[str, Decimal] = defaultdict(Decimal)
    for d in wdays:
        users = by_date.get(d, set())
        window_users |= users
        day_rev = rev_day.get(d, {})
        iap = sum((v for (u, t), v in day_rev.items() if t == "iap"), Decimal(0))
        ad = sum((v for (u, t), v in day_rev.items() if t == "ad"), Decimal(0))
        payers = sum(1 for u in users if day_rev.get((u, "iap"), Decimal(0)) > 0)
        n = len(users)
        day_rows.append({
            "date": d.isoformat(), "dau": n,
            "new_users": installs_per_day.get(d, 0),
            "iap_revenue": rnd(iap), "ad_revenue": rnd(ad),
            "arpdau_iap": rnd(iap / n) if n else None, "arpdau_ad": rnd(ad / n) if n else None,
            "arpdau": rnd((iap + ad) / n) if n else None,
            "payers": payers, "payer_share": rnd(payers / n) if n else None,
        })
        tot_iap += iap
        tot_ad += ad
        dau_days += n
        for (u, t), v in day_rev.items():
            if t == "iap":
                user_iap[u] += v
    payer_set = {u for u, v in user_iap.items() if v > 0}
    payers_active = payer_set & window_users
    payer_revenue = sum((user_iap[u] for u in payer_set), Decimal(0))
    total = tot_iap + tot_ad
    totals = {
        "dau_days": dau_days, "active_users": len(window_users),
        "iap_revenue": rnd(tot_iap), "ad_revenue": rnd(tot_ad), "revenue": rnd(total),
        "arpdau_iap": rnd(tot_iap / dau_days) if dau_days else None,
        "arpdau_ad": rnd(tot_ad / dau_days) if dau_days else None,
        "arpdau": rnd(total / dau_days) if dau_days else None,
        "ad_share": rnd(tot_ad / total) if total else None,
        "payers": len(payer_set), "payers_inactive": len(payer_set - window_users),
        "payer_conversion": rnd(len(payers_active) / len(window_users)) if window_users else None,
        "arppu": rnd(payer_revenue / len(payer_set)) if payer_set else None,
    }
    money = {"window_days": window, "window": [wdays[0].isoformat(), wdays[-1].isoformat()],
             "days": day_rows, "totals": totals}

    # Churn by last level
    if bad_levels:
        churn = {"computed": False, "reason": f"{bad_levels} activity rows have non integer levels; map labels to an index"}
    elif not level_events:
        churn = {"computed": False, "reason": "no level column or no level values"}
    else:
        last_active = {u: max(ds) for u, ds in activity.items()}
        max_level, last_level = {}, {}
        for u, evs in level_events.items():
            evs.sort(key=lambda e: (e[0], e[1]))
            max_level[u] = max(e[2] for e in evs)
            last_level[u] = evs[-1][2]
        churned = {u for u in level_events if (as_of - last_active[u]).days >= churn_days}
        lo, hi = min(min(e[2] for e in evs) for evs in level_events.values()), max(max_level.values())
        lrows = []
        for lv in range(lo, hi + 1):
            reached = sum(1 for u in max_level if max_level[u] >= lv)
            here = sum(1 for u in churned if last_level[u] == lv)
            lrows.append({"level": lv, "reached": reached, "churned_here": here,
                          "rate": rnd(here / reached) if reached else None})
        churn = {"computed": True, "inactive_days": churn_days, "users_with_levels": len(level_events),
                 "churned_users": len(churned), "rows": lrows}

    return {
        "as_of": as_of.isoformat(), "as_of_source": as_of_source, "min_cohort": min_cohort,
        "input": {"rows": len(rows), "rows_after_as_of": after,
                  "non_activity_rows": sum(1 for r in kept if not r["activity"]),
                  "duplicate_iap_rows": dup, "naive_timestamps": sum(1 for r in rows if r["naive"]),
                  "users": len(activity), "currency": data["currency"],
                  "cohorts_from": cohorts_from.isoformat() if cohorts_from else None},
        "activity": act,
        "retention": {"cohorts": cohort_rows, "pooled": pooled_out},
        "monetization": money,
        "churn_by_level": churn,
    }


def judge(result: dict, gates: dict) -> tuple[list, str, int]:
    out = []
    for key in sorted(gates, key=lambda k: int(k[1:])):
        threshold = gates[key]
        p = result["retention"]["pooled"].get(key)
        if p is None:
            out.append({"metric": key, "threshold": threshold, "rate": None, "cohort_users": 0,
                        "status": "CANNOT JUDGE", "reason": "no mature cohort", "threshold_inside_ci95": None})
            continue
        lo, hi = p["ci95"]
        inside = lo <= threshold <= hi
        if p["cohort_users"] < result["min_cohort"]:
            status, reason = "CANNOT JUDGE", f"{p['cohort_users']} users in mature cohorts, under --min-cohort {result['min_cohort']}"
        elif p["rate"] >= threshold:
            status, reason = "PASS", "rate at or above threshold"
        else:
            status, reason = "FAIL", "rate under threshold"
        out.append({"metric": key, "threshold": threshold, "rate": p["rate"], "cohort_users": p["cohort_users"],
                    "status": status, "reason": reason, "threshold_inside_ci95": inside})
    statuses = {g["status"] for g in out}
    if "FAIL" in statuses:
        return out, "FAIL", 1
    if "CANNOT JUDGE" in statuses:
        return out, "CANNOT JUDGE", 2
    return out, "PASS", 0


def load_gates(path: str) -> dict:
    try:
        with open(path, encoding="utf-8") as fh:
            raw = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        raise CannotRun(f"cannot read gates file {path}: {exc}")
    if not isinstance(raw, dict) or not raw:
        raise CannotRun("gates file must be a JSON object such as {\"d1\": 0.3, \"d7\": 0.1}")
    gates = {}
    for k, v in raw.items():
        key = str(k).strip().lower()
        if key not in {f"d{n}" for n in RETENTION_DAYS}:
            raise CannotRun(f"gate {k!r}: only d1, d7 and d30 are supported")
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not 0 < v <= 1:
            raise CannotRun(f"gate {k!r}: threshold must be a fraction between 0 and 1 (0.35 means 35%), got {v!r}")
        gates[key] = float(v)
    return gates


def pct(x) -> str:
    return "n/a" if x is None else f"{x * 100:.1f}%"


def money(x) -> str:
    """Up to 4 decimals (ARPDAU is often a few cents), at least 2."""
    if x is None:
        return "n/a"
    s = f"{x:,.4f}"
    while s.endswith("0") and len(s.split(".")[1]) > 2:
        s = s[:-1]
    return s


def markdown(res: dict, tz_name: str, gates_out: list | None, verdict: str, path: str) -> str:
    L = [f"# Game KPI report: {path}", "",
         f"As of {res['as_of']} ({res['as_of_source']}), timezone {tz_name}, calendar days, classic retention. "
         f"Currency: {res['input']['currency'] or 'not stated'}. Revenue is reported as the file holds it (state gross or net).", ""]
    i = res["input"]
    L.append(f"Input: {i['rows']} rows; active users: {i['users']}; rows after as-of (ignored): {i['rows_after_as_of']}; "
             f"server side rows not counted as activity: {i['non_activity_rows']}; duplicate IAP rows dropped: {i['duplicate_iap_rows']}.")
    if i["naive_timestamps"]:
        L.append(f"WARNING: {i['naive_timestamps']} timestamps had no offset and were read as UTC.")
    if i["cohorts_from"]:
        L.append(f"Cohorts from {i['cohorts_from']}.")
    a = res["activity"]
    L += ["", "## Activity", "", "| DAU (as-of day) | WAU (7 days) | MAU (30 days) | Average DAU (30 days) | Stickiness |",
          "|---:|---:|---:|---:|---:|",
          f"| {a['dau']} | {a['wau']} | {a['mau']} | {a['avg_dau_30d']} | {pct(a['stickiness'])} |"]
    L += ["", "## Retention by install cohort (classic; blank = not mature)", "", "| Install date | Size | D1 | D7 | D30 |",
          "|---|---:|---:|---:|---:|"]
    for c in res["retention"]["cohorts"]:
        cells = ["" if c[f"d{n}"] is None else f"{c[f'd{n}']['retained']} ({pct(c[f'd{n}']['rate'])})" for n in RETENTION_DAYS]
        L.append(f"| {c['install_date']} | {c['size']} | " + " | ".join(cells) + " |")
    L += ["", "Pooled over mature cohorts (sum retained / sum cohort users, never an average of rates):", "",
          "| Metric | Cohorts | Users | Retained | Rate | 95% interval | Under --min-cohort |", "|---|---:|---:|---:|---:|---|---|"]
    for n in RETENTION_DAYS:
        p = res["retention"]["pooled"][f"d{n}"]
        if p is None:
            L.append(f"| D{n} | 0 | 0 | 0 | n/a | n/a | yes |")
        else:
            L.append(f"| D{n} | {p['cohorts']} | {p['cohort_users']} | {p['retained']} | {pct(p['rate'])} | "
                     f"{pct(p['ci95'][0])} to {pct(p['ci95'][1])} | {'yes' if p['below_min_cohort'] else 'no'} |")
    m = res["monetization"]
    L += ["", f"## Monetization, {m['window'][0]} to {m['window'][1]}", "",
          "| Date | DAU | New | IAP | Ads | ARPDAU IAP | ARPDAU ads | ARPDAU | Payers | Payer share |",
          "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for d in m["days"]:
        L.append(f"| {d['date']} | {d['dau']} | {d['new_users']} | {money(d['iap_revenue'])} | {money(d['ad_revenue'])} | "
                 f"{money(d['arpdau_iap'])} | {money(d['arpdau_ad'])} | {money(d['arpdau'])} | {d['payers']} | {pct(d['payer_share'])} |")
    t = m["totals"]
    L += ["", f"Window: ARPDAU {money(t['arpdau'])} (IAP {money(t['arpdau_iap'])}, ads {money(t['arpdau_ad'])}, "
          f"ad share {pct(t['ad_share'])}) over {t['dau_days']} DAU days; payer conversion {pct(t['payer_conversion'])} "
          f"({t['payers'] - t['payers_inactive']} paying of {t['active_users']} active users); ARPPU {money(t['arppu'])}."]
    if any(d["iap_revenue"] < 0 for d in m["days"]):
        L.append("Note: refunds land on the day the store reports them, so a day can show negative IAP revenue.")
    if t["payers_inactive"]:
        L.append(f"Note: {t['payers_inactive']} payer(s) had IAP revenue but no activity in the window (renewals or web purchases).")
    ch = res["churn_by_level"]
    L += ["", "## Churn by last level"]
    if not ch["computed"]:
        L.append(f"Not computed: {ch['reason']}.")
    else:
        L += [f"Players inactive {ch['inactive_days']} or more days, by the level of their last level event "
              f"({ch['churned_users']} churned of {ch['users_with_levels']} with level data).", "",
              "| Level | Reached | Churned here | Rate |", "|---:|---:|---:|---:|"]
        for r in ch["rows"]:
            L.append(f"| {r['level']} | {r['reached']} | {r['churned_here']} | {pct(r['rate'])} |")
    if gates_out is not None:
        L += ["", f"## Gates: {verdict}", "", "| Gate | Threshold | Rate | Users | Status | Threshold inside 95% interval | Reason |",
              "|---|---:|---:|---:|---|---|---|"]
        for g in gates_out:
            inside = "n/a" if g["threshold_inside_ci95"] is None else ("yes, fragile" if g["threshold_inside_ci95"] else "no")
            L.append(f"| {g['metric'].upper()} | {pct(g['threshold'])} | {pct(g['rate'])} | {g['cohort_users']} | "
                     f"{g['status']} | {inside} | {g['reason']} |")
    L += ["", CANNOT_COVER]
    return "\n".join(L) + "\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Core game KPIs from an event export.")
    ap.add_argument("events", help="CSV with user_id, ts, event (+ revenue, revenue_type, level, currency, transaction_id, game)")
    ap.add_argument("--timezone", default="UTC", help="IANA name or +HH:MM; defines day boundaries (default UTC)")
    ap.add_argument("--as-of", help="last complete day to include (default: day before the latest event date)")
    ap.add_argument("--min-cohort", type=int, default=1000, help="smallest pooled cohort a gate may judge (default 1000)")
    ap.add_argument("--gates", help="JSON file with retention thresholds, e.g. {\"d1\": 0.3, \"d7\": 0.1}")
    ap.add_argument("--window", type=int, default=7, help="days in the monetization window (default 7)")
    ap.add_argument("--churn-days", type=int, default=7, help="inactive days that count as churned (default 7)")
    ap.add_argument("--cohorts-from", help="ignore install cohorts before this date (use when the export starts after launch)")
    ap.add_argument("--game", help="keep only rows whose game column equals this id")
    ap.add_argument("--non-activity-events", default=DEFAULT_NON_ACTIVITY,
                    help="comma list of events that never make a player active (default: %(default)s)")
    ap.add_argument("--json", help="write the results as JSON to this path")
    ap.add_argument("--out", help="write the Markdown report to this path instead of stdout")
    args = ap.parse_args(argv)
    try:
        if args.min_cohort < 1 or args.window < 1 or args.churn_days < 1:
            raise CannotRun("--min-cohort, --window and --churn-days must be 1 or more")
        tz = parse_tz(args.timezone)
        as_of = parse_date(args.as_of, "--as-of") if args.as_of else None
        cohorts_from = parse_date(args.cohorts_from, "--cohorts-from") if args.cohorts_from else None
        gates = load_gates(args.gates) if args.gates else None
        non_activity = {e.strip() for e in args.non_activity_events.split(",") if e.strip()}
        data = load(args.events, tz, args.game, non_activity)
        result = compute(data, as_of, args.window, args.churn_days, args.min_cohort, cohorts_from)
    except CannotRun as exc:
        print(f"COULD NOT RUN: {exc}")
        print(CANNOT_COVER)
        return 2
    result["timezone"] = args.timezone
    gates_out, verdict, code = (None, "REPORT", 0)
    if gates:
        gates_out, verdict, code = judge(result, gates)
    result["gates"] = gates_out
    result["verdict"] = verdict
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=2, sort_keys=True)
            fh.write("\n")
    report = markdown(result, args.timezone, gates_out, verdict, args.events)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report)
        print(f"Report written to {args.out}. Verdict: {verdict}.")
        print(CANNOT_COVER)
    else:
        sys.stdout.write(report)
    return code


if __name__ == "__main__":
    sys.exit(main())
