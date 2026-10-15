#!/usr/bin/env python3
"""level_flags.py: flag difficulty and content signals in a level (or day) funnel.

Standard library only. Reads a CSV with one row per level or day, exported by the
measurement agent (its level dashboard or the churn by level table of game_kpis.py),
compares each level with its neighbors and prints flags for the game repo. It never
recommends level parameters: difficulty belongs to the game's own repo.

Definitions (summaries; ads-master/METRICS.md wins):
  completion rate          players_completed / players_reached
  attempts per completion  attempts / players_completed
  churn rate               churned / players_reached, where churned = players whose last
                           level was this one and who were inactive 7 or more days
  quit rate                quits / attempts
  continue rate            continues / attempts

Input columns (header row)
  required: level (or the column named by --key, for example day), players_reached
            (alias: reached), churned (alias: churned_here)
  optional: players_completed, attempts, quits, continues

Flags (thresholds are practitioner defaults; record the values used)
  churn_spike          high    churn >= churn-ratio x neighborhood median and >= churn-gap above it
  frontier_wall        medium  the churn condition inside the frontier band (last --frontier levels)
  quit_spike           medium  quit rate >= quit-ratio x median and >= quit-gap above it
  attempts_spike       low     attempts per completion >= attempts-ratio x median (medium with churn or quit)
  continue_pressure    medium  continue rate >= continue-ratio x median (hand to game-monetization)
  funnel_inconsistent  error   completed > reached, churned > reached, or reached(N+1) > completed(N) by 2%
  low_sample           info    players_reached below --min-reached

Usage
  python3 -I level_flags.py level_funnel.csv --frontier 10
  python3 -I level_flags.py daily_funnel.csv --key day --frontier 0 --min-reached 500 --json flags.json

Exit codes: 0 no churn_spike and no data error, 1 a churn_spike or a data error, 2 could not run.
"""
from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys

CANNOT_COVER = ("This check cannot cover: why a level loses players (bug, unclear goal, difficulty, a release or "
                "an outage), whether the export is complete or uses mature cohorts, segment differences you did "
                "not split (payers, markets, app versions, UA sources), and whether a hard level is hard by design; "
                "every flag is a question for the game repo, never a parameter change.")

ALIASES = {"players_reached": ("players_reached", "reached"), "churned": ("churned", "churned_here")}
OPTIONAL = ("players_completed", "attempts", "quits", "continues")
SEVERITY_ORDER = {"error": 0, "high": 1, "medium": 2, "low": 3, "info": 4}


class CannotRun(Exception):
    """Input problem that makes every flag untrustworthy."""


def to_number(value: str, col: str, line: int) -> float:
    try:
        x = float(value)
    except (TypeError, ValueError):
        raise CannotRun(f"line {line}: column {col} is not a number ({value!r})")
    if x < 0:
        raise CannotRun(f"line {line}: column {col} is negative")
    return x


def load(path: str, key: str) -> list[dict]:
    try:
        fh = open(path, encoding="utf-8", newline="")
    except OSError as exc:
        raise CannotRun(f"cannot read {path}: {exc.strerror}")
    with fh:
        reader = csv.DictReader(fh)
        header = [h.strip() for h in (reader.fieldnames or [])]
        if not header:
            raise CannotRun("the CSV has no header row")
        cols = {}
        if key not in header:
            raise CannotRun(f"missing key column '{key}'")
        for name, options in ALIASES.items():
            found = next((o for o in options if o in header), None)
            if not found:
                raise CannotRun(f"missing column {name} (or {options[1]})")
            cols[name] = found
        for name in OPTIONAL:
            if name in header:
                cols[name] = name
        rows, seen = [], set()
        for line, raw in enumerate(reader, 2):
            raw = {k.strip(): (v or "").strip() for k, v in raw.items() if k}
            if not any(raw.values()):
                continue
            try:
                k = int(raw[key])
            except ValueError:
                raise CannotRun(f"line {line}: {key} must be an integer index ({raw[key]!r})")
            if k in seen:
                raise CannotRun(f"line {line}: duplicate {key} {k}")
            seen.add(k)
            row = {"key": k, "line": line}
            for name, col in cols.items():
                if raw.get(col, "") == "":
                    row[name] = None
                else:
                    row[name] = to_number(raw[col], col, line)
            if row["players_reached"] is None or row["churned"] is None:
                raise CannotRun(f"line {line}: players_reached and churned are required on every row")
            rows.append(row)
    if not rows:
        raise CannotRun("the CSV has no data rows")
    rows.sort(key=lambda r: r["key"])
    return rows


def ratio(num, den):
    if num is None or den is None or den <= 0:
        return None
    return num / den


def compute(rows: list[dict], args) -> dict:
    flags = []
    for r in rows:
        r["churn_rate"] = ratio(r["churned"], r["players_reached"])
        r["completion_rate"] = ratio(r.get("players_completed"), r["players_reached"])
        r["attempts_per_completion"] = ratio(r.get("attempts"), r.get("players_completed"))
        r["quit_rate"] = ratio(r.get("quits"), r.get("attempts"))
        r["continue_rate"] = ratio(r.get("continues"), r.get("attempts"))
        r["sampled"] = r["players_reached"] >= args.min_reached

    def flag(r, kind, severity, detail):
        flags.append({"key": r["key"], "flag": kind, "severity": severity, "detail": detail,
                      "players_reached": int(r["players_reached"])})

    # Data consistency first.
    bad = set()
    for i, r in enumerate(rows):
        done = r.get("players_completed")
        if done is not None and done > r["players_reached"]:
            flag(r, "funnel_inconsistent", "error", "players_completed is above players_reached")
            bad.add(r["key"])
        if r["churned"] > r["players_reached"]:
            flag(r, "funnel_inconsistent", "error", "churned is above players_reached")
            bad.add(r["key"])
        if i + 1 < len(rows) and done is not None and rows[i + 1]["key"] == r["key"] + 1:
            nxt = rows[i + 1]["players_reached"]
            if nxt > done * 1.02 and nxt - done >= 1:
                flag(rows[i + 1], "funnel_inconsistent", "error",
                     f"{int(nxt)} players reached it but only {int(done)} completed the previous one")
                bad.add(rows[i + 1]["key"])

    max_key = rows[-1]["key"]
    frontier_from = max_key - args.frontier + 1 if args.frontier > 0 else None

    def neighborhood(i: int, metric: str):
        vals = []
        for j in range(max(0, i - args.window), min(len(rows), i + args.window + 1)):
            if j == i:
                continue
            o = rows[j]
            if abs(o["key"] - rows[i]["key"]) > args.window or not o["sampled"] or o["key"] in bad:
                continue
            if o.get(metric) is not None:
                vals.append(o[metric])
        return statistics.median(vals) if len(vals) >= 3 else None

    for i, r in enumerate(rows):
        if r["key"] in bad:
            continue
        if not r["sampled"]:
            flag(r, "low_sample", "info", f"{int(r['players_reached'])} players reached it "
                                          f"(minimum {args.min_reached})")
            continue
        in_frontier = frontier_from is not None and r["key"] >= frontier_from
        churn_hit = quit_hit = False
        med = neighborhood(i, "churn_rate")
        if med is not None and r["churn_rate"] is not None:
            if r["churn_rate"] >= args.churn_ratio * med and r["churn_rate"] - med >= args.churn_gap:
                churn_hit = True
                detail = f"churn {r['churn_rate']:.1%} vs neighborhood median {med:.1%}"
                if in_frontier:
                    flag(r, "frontier_wall", "medium", detail + "; inside the frontier band: check content runway")
                else:
                    flag(r, "churn_spike", "high", detail)
        med = neighborhood(i, "quit_rate")
        if med is not None and r["quit_rate"] is not None:
            if r["quit_rate"] >= args.quit_ratio * med and r["quit_rate"] - med >= args.quit_gap:
                quit_hit = True
                flag(r, "quit_spike", "medium", f"quit rate {r['quit_rate']:.1%} vs median {med:.1%}")
        med = neighborhood(i, "attempts_per_completion")
        if med is not None and r["attempts_per_completion"] is not None:
            if r["attempts_per_completion"] >= args.attempts_ratio * med:
                sev = "medium" if (churn_hit or quit_hit) else "low"
                flag(r, "attempts_spike", sev, f"{r['attempts_per_completion']:.2f} attempts per completion "
                                               f"vs median {med:.2f}")
        med = neighborhood(i, "continue_rate")
        if med is not None and r["continue_rate"] is not None and med > 0:
            if r["continue_rate"] >= args.continue_ratio * med:
                flag(r, "continue_pressure", "medium", f"continue rate {r['continue_rate']:.1%} vs median "
                                                       f"{med:.1%}; hand to game-monetization with the game repo")

    flags.sort(key=lambda f: (SEVERITY_ORDER[f["severity"]], f["key"], f["flag"]))
    settings = {k: getattr(args, k) for k in ("key", "window", "min_reached", "churn_ratio", "churn_gap",
                                              "quit_ratio", "quit_gap", "attempts_ratio", "continue_ratio",
                                              "frontier")}
    return {"settings": settings, "rows": len(rows), "max_key": max_key,
            "frontier_from": frontier_from, "flags": flags}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Flag difficulty and content signals in a level or day funnel.")
    ap.add_argument("funnel", help="CSV export with one row per level or day")
    ap.add_argument("--key", default="level", help="index column (default level; use day for daily games)")
    ap.add_argument("--window", type=int, default=5, help="neighbors on each side (default 5)")
    ap.add_argument("--min-reached", type=int, default=200, help="minimum players reached to judge (default 200)")
    ap.add_argument("--churn-ratio", type=float, default=2.0)
    ap.add_argument("--churn-gap", type=float, default=0.01, help="absolute gap as a fraction (default 0.01)")
    ap.add_argument("--quit-ratio", type=float, default=2.0)
    ap.add_argument("--quit-gap", type=float, default=0.02)
    ap.add_argument("--attempts-ratio", type=float, default=2.0)
    ap.add_argument("--continue-ratio", type=float, default=2.0)
    ap.add_argument("--frontier", type=int, default=10, help="last N levels treated as the frontier (0 for none)")
    ap.add_argument("--json", help="write settings and flags as JSON to this path")
    args = ap.parse_args(argv)
    try:
        if args.window < 1 or args.min_reached < 1 or args.frontier < 0:
            raise CannotRun("--window and --min-reached must be 1 or more; --frontier 0 or more")
        rows = load(args.funnel, args.key)
    except CannotRun as exc:
        print(f"ERROR {exc}")
        print(CANNOT_COVER)
        return 2
    res = compute(rows, args)
    print(f"{res['rows']} rows by {args.key}, last {args.key} {res['max_key']}"
          + (f", frontier from {res['frontier_from']}" if res["frontier_from"] is not None else ""))
    if not res["flags"]:
        print("No flags.")
    for f in res["flags"]:
        print(f"{f['severity'].upper():7} {args.key} {f['key']}: {f['flag']} ({f['detail']}; "
              f"reached {f['players_reached']})")
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=2)
    print(CANNOT_COVER)
    hit = any(f["flag"] == "churn_spike" or f["severity"] == "error" for f in res["flags"])
    return 1 if hit else 0


if __name__ == "__main__":
    sys.exit(main())
