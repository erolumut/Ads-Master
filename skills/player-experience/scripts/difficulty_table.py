#!/usr/bin/env python3
"""difficulty_table.py: build a per level difficulty table from an attempt event log.

Standard library only. It reads facts and prints a table plus flags. It never
recommends level parameters: difficulty belongs to the game's own repo. The table can
feed the level_rating input of a pxe policy once a human has reviewed it.

Input CSV (header row, one row per attempt)
  required: player_id, level (integer), result (win, fail or quit)
  optional: attempts_before (attempts this player made on the level before this one),
            duration_ms (read and checked, not used in this version),
            ts (epoch seconds or ISO 8601; with no ts column the file order is the time order)

Per level
  attempts            every event on the level (a quit counts as an attempt that did not pass)
  players             distinct players with at least one event on the level
  pass rate           wins / attempts
  first try pass      wins on a player's first attempt / first attempts. A first attempt is
                      attempts_before == 0 when that cell is filled, otherwise the player's
                      first event on the level in time order
  median attempts     median over players who passed of the attempts up to and including
                      their first win (attempts_before + 1 when that cell is filled)
  quit at level rate  players whose last event overall is on this level and is a fail or a
                      quit, divided by players who reached it
  elo                 level rating from replaying every attempt in time order. Players start at
                      1500, levels start at 1500. Expected player win chance is
                      1 / (1 + 10 ** (gap / 400)), where gap is the level rating minus the player rating. A win scores 1 for the player,
                      a fail or quit scores 0. The player moves by K 24 times (score minus
                      expected), the level moves by K 8 times (expected minus score). Only
                      differences between levels carry meaning, and levels with few attempts
                      stay near 1500.

Labels (practitioner defaults; record the values used)
  insufficient data   attempts below --min-attempts (default 30)
  super hard          pass rate below --super-hard (default 0.25)
  hard                pass rate below --hard (default 0.45)
  ok                  everything else

Flags (judged only on levels with enough attempts)
  spike      pass rate at least 0.15 below both neighbouring levels (both with enough attempts)
  wall       quit at level rate at least 2 times the median of all judged levels, and at least 0.05
  sawtooth   a summary, not a flag: share of hard levels and the spacing between them

Usage
  python3 -I difficulty_table.py events.csv
  python3 -I difficulty_table.py events.csv --min-attempts 50 --hard 0.5 --json --out table.json

With --json, stdout is one JSON document (the cannot cover sentence is under "cannotCover" and is
also written to stderr as the last line). --out writes the same text to a file.

Exit codes: 0 the table was written (flags are not failures), 2 could not run.
"""
from __future__ import annotations

import argparse
import csv
import json
import statistics
import sys
from datetime import datetime, timezone

CANNOT_COVER = ("This check cannot cover: whether the measured difficulty matches how the level feels, the mix "
                "of cohorts behind the numbers, level changes during the window, and bots or shared accounts.")

REQUIRED = ("player_id", "level", "result")
RESULTS = ("win", "fail", "quit")
START_RATING = 1500.0
K_PLAYER = 24.0
K_LEVEL = 8.0
SPIKE_GAP = 0.15
WALL_RATIO = 2.0
WALL_FLOOR = 0.05
EPS = 1e-9


class CannotRun(Exception):
    """Input problem that makes the table untrustworthy."""


def parse_ts(value: str, line: int) -> float:
    try:
        return float(value)
    except ValueError:
        pass
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        raise CannotRun(f"line {line}: ts is neither a number nor an ISO 8601 time ({value!r})")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.timestamp()


def parse_int(value: str, col: str, line: int, minimum: int = 0) -> int:
    try:
        x = float(value)
    except ValueError:
        raise CannotRun(f"line {line}: column {col} is not a number ({value!r})")
    if x != int(x) or x < minimum:
        raise CannotRun(f"line {line}: column {col} must be a whole number of {minimum} or more ({value!r})")
    return int(x)


def load(path: str) -> list[dict]:
    try:
        fh = open(path, encoding="utf-8-sig", newline="")
    except OSError as exc:
        raise CannotRun(f"cannot read {path}: {exc.strerror}")
    with fh:
        reader = csv.DictReader(fh)
        header = [h.strip().lower() for h in (reader.fieldnames or [])]
        if not header:
            raise CannotRun("the file has no header row")
        missing = [c for c in REQUIRED if c not in header]
        if missing:
            raise CannotRun(f"missing column {', '.join(missing)}")
        has_ts = "ts" in header
        events: list[dict] = []
        for line, raw in enumerate(reader, 2):
            row = {(k or "").strip().lower(): (v or "").strip() for k, v in raw.items() if k}
            if not any(row.values()):
                continue
            player = row.get("player_id", "")
            if not player:
                raise CannotRun(f"line {line}: player_id is empty")
            result = row.get("result", "").lower()
            if result not in RESULTS:
                raise CannotRun(f"line {line}: result must be win, fail or quit ({row.get('result')!r})")
            before = row.get("attempts_before", "")
            duration = row.get("duration_ms", "")
            if duration:
                parse_int(duration, "duration_ms", line)
            events.append({
                "idx": len(events),
                "player": player,
                "level": parse_int(row.get("level", ""), "level", line),
                "result": result,
                "before": parse_int(before, "attempts_before", line) if before else None,
                "ts": (parse_ts(row["ts"], line) if row.get("ts") else _missing_ts(line)) if has_ts else 0.0,
            })
    if not events:
        raise CannotRun("the file has no data rows")
    return events


def _missing_ts(line: int) -> float:
    raise CannotRun(f"line {line}: ts is empty (fill every ts or drop the column)")


def pct(x: float | None) -> str:
    return "-" if x is None else f"{x:.2f}"


def compute(events: list[dict], args: argparse.Namespace) -> dict:
    ordered = sorted(events, key=lambda e: (e["ts"], e["idx"]))
    player_r: dict[str, float] = {}
    level_r: dict[int, float] = {}
    stats: dict[int, dict] = {}
    seen: dict[tuple[str, int], int] = {}
    passed: set[tuple[str, int]] = set()
    last: dict[str, dict] = {}

    for e in ordered:
        lv, p = e["level"], e["player"]
        s = stats.setdefault(lv, {"attempts": 0, "wins": 0, "players": set(), "first": 0, "first_wins": 0,
                                  "to_pass": []})
        key = (p, lv)
        seen[key] = seen.get(key, 0) + 1
        win = e["result"] == "win"
        s["attempts"] += 1
        s["wins"] += 1 if win else 0
        s["players"].add(p)
        is_first = (e["before"] == 0) if e["before"] is not None else (seen[key] == 1)
        if is_first:
            s["first"] += 1
            s["first_wins"] += 1 if win else 0
        if win and key not in passed:
            passed.add(key)
            s["to_pass"].append(e["before"] + 1 if e["before"] is not None else seen[key])
        rp = player_r.get(p, START_RATING)
        rl = level_r.get(lv, START_RATING)
        expected = 1.0 / (1.0 + 10 ** ((rl - rp) / 400.0))
        score = 1.0 if win else 0.0
        player_r[p] = rp + K_PLAYER * (score - expected)
        level_r[lv] = rl + K_LEVEL * (expected - score)
        last[p] = e

    stoppers: dict[int, int] = {}
    for e in last.values():
        if e["result"] in ("fail", "quit"):
            stoppers[e["level"]] = stoppers.get(e["level"], 0) + 1

    rows = []
    for lv in sorted(stats):
        s = stats[lv]
        players = len(s["players"])
        rate = s["wins"] / s["attempts"]
        enough = s["attempts"] >= args.min_attempts
        if not enough:
            label = "insufficient data"
        elif rate < args.super_hard:
            label = "super hard"
        elif rate < args.hard:
            label = "hard"
        else:
            label = "ok"
        rows.append({
            "level": lv,
            "attempts": s["attempts"],
            "players": players,
            "wins": s["wins"],
            "pass_rate": round(rate, 4),
            "first_try_pass_rate": round(s["first_wins"] / s["first"], 4) if s["first"] else None,
            "median_attempts_to_pass": statistics.median(s["to_pass"]) if s["to_pass"] else None,
            "quit_at_level_rate": round(stoppers.get(lv, 0) / players, 4),
            "elo": round(level_r[lv], 1),
            "label": label,
            "flags": [],
        })

    judged = [r for r in rows if r["label"] != "insufficient data"]
    flags: list[dict] = []
    for i, r in enumerate(rows):
        if r["label"] == "insufficient data" or i == 0 or i == len(rows) - 1:
            continue
        before, after = rows[i - 1], rows[i + 1]
        if before["label"] == "insufficient data" or after["label"] == "insufficient data":
            continue
        gap = min(before["pass_rate"], after["pass_rate"]) - r["pass_rate"]
        if r["pass_rate"] <= before["pass_rate"] - SPIKE_GAP + EPS and r["pass_rate"] <= after["pass_rate"] - SPIKE_GAP + EPS:
            r["flags"].append("spike")
            flags.append({"level": r["level"], "flag": "spike",
                          "detail": f"pass rate {r['pass_rate']:.2f} against {before['pass_rate']:.2f} on level "
                                    f"{before['level']} and {after['pass_rate']:.2f} on level {after['level']} "
                                    f"(gap {gap:.2f} to the nearer neighbour)"})

    median_quit = statistics.median(r["quit_at_level_rate"] for r in judged) if judged else None
    if median_quit is not None:
        threshold = max(WALL_RATIO * median_quit, WALL_FLOOR)
        for r in judged:
            if r["quit_at_level_rate"] >= threshold - EPS:
                r["flags"].append("wall")
                flags.append({"level": r["level"], "flag": "wall",
                              "detail": f"quit at level rate {r['quit_at_level_rate']:.2f} against a median of "
                                        f"{median_quit:.2f} (threshold {threshold:.2f})"})
    flags.sort(key=lambda f: (f["level"], f["flag"]))

    hard_levels = [r["level"] for r in judged if r["label"] in ("hard", "super hard")]
    spacing = [b - a for a, b in zip(hard_levels, hard_levels[1:])]
    sawtooth = {
        "judged_levels": len(judged),
        "hard_levels": hard_levels,
        "hard_share": round(len(hard_levels) / len(judged), 4) if judged else None,
        "spacing": spacing,
        "median_spacing": statistics.median(spacing) if spacing else None,
    }
    return {
        "settings": {"min_attempts": args.min_attempts, "hard": args.hard, "super_hard": args.super_hard,
                     "spike_gap": SPIKE_GAP, "wall_ratio": WALL_RATIO, "wall_floor": WALL_FLOOR,
                     "elo_start": START_RATING, "elo_k_player": K_PLAYER, "elo_k_level": K_LEVEL},
        "events": len(events),
        "players": len(player_r),
        "levels": rows,
        "flags": flags,
        "median_quit_at_level_rate": median_quit,
        "sawtooth": sawtooth,
        "cannotCover": CANNOT_COVER,
    }


def render_text(res: dict) -> str:
    head = f"{'level':>5} {'attempts':>8} {'players':>7} {'pass':>5} {'first':>5} {'medAtt':>6} {'quit@':>5} {'elo':>7}  label"
    out = [f"{res['events']} events, {res['players']} players, {len(res['levels'])} levels", head]
    for r in res["levels"]:
        med = r["median_attempts_to_pass"]
        flags = f"  [{', '.join(r['flags'])}]" if r["flags"] else ""
        out.append(f"{r['level']:>5} {r['attempts']:>8} {r['players']:>7} {pct(r['pass_rate']):>5} "
                   f"{pct(r['first_try_pass_rate']):>5} {('-' if med is None else f'{med:g}'):>6} "
                   f"{pct(r['quit_at_level_rate']):>5} {r['elo']:>7.1f}  {r['label']}{flags}")
    if not res["flags"]:
        out.append("No flags.")
    for f in res["flags"]:
        out.append(f"FLAG {f['flag']} level {f['level']}: {f['detail']}")
    saw = res["sawtooth"]
    if saw["hard_share"] is None:
        out.append("Sawtooth: no level has enough attempts to judge.")
    else:
        spacing = ", ".join(str(s) for s in saw["spacing"]) or "none"
        out.append(f"Sawtooth: {len(saw['hard_levels'])} of {saw['judged_levels']} judged levels are hard "
                   f"({saw['hard_share']:.0%}); hard levels {saw['hard_levels'] or 'none'}; spacing between them {spacing}")
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Build a per level difficulty table from an attempt event log.")
    ap.add_argument("events", help="CSV with player_id, level, result and optional attempts_before, duration_ms, ts")
    ap.add_argument("--min-attempts", type=int, default=30, help="attempts needed to judge a level (default 30)")
    ap.add_argument("--hard", type=float, default=0.45, help="pass rate below this is hard (default 0.45)")
    ap.add_argument("--super-hard", type=float, default=0.25, help="pass rate below this is super hard (default 0.25)")
    ap.add_argument("--json", action="store_true", help="print the table as one JSON document")
    ap.add_argument("--out", help="also write the printed output to this file")
    args = ap.parse_args(argv)
    try:
        if args.min_attempts < 1:
            raise CannotRun("--min-attempts must be 1 or more")
        if not (0 < args.super_hard <= args.hard <= 1):
            raise CannotRun("--super-hard and --hard must satisfy 0 < super-hard <= hard <= 1")
        res = compute(load(args.events), args)
    except CannotRun as exc:
        print(f"ERROR {exc}")
        print(CANNOT_COVER)
        return 2
    body = json.dumps(res, indent=2) if args.json else render_text(res) + "\n" + CANNOT_COVER
    print(body)
    if args.json:
        print(CANNOT_COVER, file=sys.stderr)
    if args.out:
        try:
            with open(args.out, "w", encoding="utf-8") as fh:
                fh.write(body + "\n")
        except OSError as exc:
            print(f"ERROR cannot write {args.out}: {exc.strerror}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
