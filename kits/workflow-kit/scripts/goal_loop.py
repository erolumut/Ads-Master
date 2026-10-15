#!/usr/bin/env python3
"""Keep a long, metric driven agent run honest: baseline, noise, verdicts, a log and a chart.

The helper never runs the project's commands itself, except through `measure`.
All state lives in one folder (default .progress): goal.json, log.csv, chart.html.

  python3 goal_loop.py init --goal-name "Home LCP" --unit ms --direction lower --target 2000
  python3 goal_loop.py measure --cmd "node scripts/bench.js" --runs 5 --baseline
  python3 goal_loop.py measure --cmd "node scripts/bench.js" --runs 3 --label "lazy load hero"
  python3 goal_loop.py record --label "manual trace" --values 2100,2050,2080 --note "Chrome trace"
  python3 goal_loop.py chart
  python3 goal_loop.py status

Subcommands:
  init     write goal.json and an empty log.csv (exit 2 if goal.json exists, unless --force)
  measure  run --cmd N times (shell, 1800 s limit each); the last non empty stdout line of each
           run must be a number, optionally followed by a unit word such as ms or %
  record   same decision logic, with the values given by hand (also accepts --baseline)
  chart    write chart.html (one page, inline SVG, no network, light and dark, phone width)
  status   print the summary as text

Decision (measure and record, not baseline): best so far is the baseline median or the best kept
median. A result is better only when it beats best by at least max(min_gain_pct, noise_pct)
percent in the goal's direction. Verdicts: KEEP (commit after the project's gate passes),
REVERT, GOAL MET (median reaches the target and is at least as good as best).
A baseline needs at least 5 runs; it also records noise_pct = (max minus min) / median x 100.

Exit codes: 0 KEEP, GOAL MET or any other success, 1 REVERT, 2 could not run,
3 stop the loop (turn budget used, or max_flat reverts in a row; logged first).
A GOAL MET result always exits 0, even on the last turn.
Standard library only, Python 3.10+.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import html
import json
import math
import re
import statistics
import subprocess
import sys
from pathlib import Path

CANNOT_COVER = ("This check cannot cover: whether the measure reflects real users, damage the project's "
                "own gate does not test, and the cost of the run (time, money and compute).")
HEADER = ["ts", "turn", "label", "run_values", "median", "best_so_far", "kept", "note"]
KEPT_KINDS = {"keep", "met", "baseline"}
TIMEOUT_S = 1800
NUMBER_LINE = re.compile(r"^\s*([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)\s*[A-Za-z%/]*\s*$")


class Fail(Exception):
    """Could not run: message goes to stderr, exit code 2."""


class Parser(argparse.ArgumentParser):
    def format_help(self) -> str:
        return super().format_help().rstrip("\n") + "\n\n" + CANNOT_COVER + "\n"

    def error(self, message: str) -> None:
        self.print_usage(sys.stderr)
        print(f"{self.prog}: error: {message}", file=sys.stderr)
        print(CANNOT_COVER, file=sys.stderr)
        raise SystemExit(2)


# ---------------------------------------------------------------- helpers

def fmt(x: float) -> str:
    if x == int(x) and abs(x) < 1e15:
        return str(int(x))
    return f"{x:.12f}".rstrip("0").rstrip(".") if abs(x) < 1e15 else f"{x:.6g}"


def pct(x: float) -> str:
    return fmt(round(x, 2))


def paths(d: str) -> tuple[Path, Path, Path]:
    base = Path(d)
    return base / "goal.json", base / "log.csv", base / "chart.html"


def load_goal(d: str) -> dict:
    gp = paths(d)[0]
    if not gp.is_file():
        raise Fail(f"{gp} not found (run init first)")
    try:
        goal = json.loads(gp.read_text(encoding="utf-8"))
        for key in ("goal_name", "unit", "direction", "target", "min_gain_pct", "max_turns", "max_flat"):
            goal[key]
    except (ValueError, KeyError, TypeError) as exc:
        raise Fail(f"{gp} is not a valid goal file ({exc})")
    return goal


def save_goal(d: str, goal: dict) -> None:
    paths(d)[0].write_text(json.dumps(goal, indent=2) + "\n", encoding="utf-8")


def load_log(d: str) -> list[dict]:
    lp = paths(d)[1]
    if not lp.is_file():
        return []
    with lp.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def append_log(d: str, row: dict) -> None:
    lp = paths(d)[1]
    new = not lp.is_file()
    with lp.open("a", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=HEADER)
        if new:
            w.writeheader()
        w.writerow(row)


def better(direction: str, a: float, b: float) -> bool:
    """True when a is strictly better than b."""
    return a < b if direction == "lower" else a > b


def gain_pct(direction: str, m: float, best: float) -> float:
    delta = (best - m) if direction == "lower" else (m - best)
    if best == 0:
        return math.inf if delta > 0 else (-math.inf if delta < 0 else 0.0)
    return delta / abs(best) * 100


def meets(direction: str, m: float, target: float) -> bool:
    return m <= target if direction == "lower" else m >= target


def best_so_far(goal: dict, rows: list[dict]) -> float | None:
    cands = [float(r["median"]) for r in rows if r["kept"] in ("keep", "met")]
    if goal.get("baseline_median") is not None:
        cands.append(float(goal["baseline_median"]))
    if not cands:
        return None
    return min(cands) if goal["direction"] == "lower" else max(cands)


def summary(goal: dict, rows: list[dict]) -> dict:
    best = best_so_far(goal, rows)
    turns = sum(1 for r in rows if r["kept"] != "baseline")
    gap = pgap = None
    if best is not None:
        raw = (best - goal["target"]) if goal["direction"] == "lower" else (goal["target"] - best)
        gap = max(raw, 0.0)
        pgap = (gap / abs(best) * 100) if best != 0 else (0.0 if gap == 0 else math.inf)
    return {"goal": goal, "best": best, "gap": gap, "gap_pct": pgap, "turns": turns,
            "noise": goal.get("noise_pct"), "baseline": goal.get("baseline_median")}


def summary_lines(s: dict) -> list[str]:
    g = s["goal"]
    u = g["unit"]
    word = "at most" if g["direction"] == "lower" else "at least"
    best = "none yet" if s["best"] is None else f"{fmt(s['best'])} {u}"
    if s["gap"] is None:
        gap = "unknown until a baseline exists"
    elif s["gap"] == 0:
        gap = "0 (target reached)"
    else:
        gap = f"{fmt(s['gap'])} {u} ({pct(s['gap_pct'])} percent of best)"
    noise = "not measured (run a baseline)" if s["noise"] is None else f"{pct(s['noise'])} percent"
    base = "none" if s["baseline"] is None else f"{fmt(s['baseline'])} {u}"
    return [
        f"Goal: {g['goal_name']}, {g['direction']} is better, target {word} {fmt(g['target'])} {u}",
        f"Baseline: {base}",
        f"Best so far: {best}",
        f"Gap left: {gap}",
        f"Turns used: {s['turns']} of {g['max_turns']}",
        f"Noise: {noise}",
        f"Minimum gain to keep: {pct(max(g['min_gain_pct'], s['noise'] or 0))} percent",
    ]


# ---------------------------------------------------------------- numbers

def parse_value(line: str) -> float | None:
    m = NUMBER_LINE.match(line)
    if not m:
        return None
    v = float(m.group(1))
    return v if math.isfinite(v) else None


def run_command(cmd: str, runs: int) -> list[float]:
    values: list[float] = []
    for i in range(1, runs + 1):
        try:
            p = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding="utf-8",
                               errors="replace", timeout=TIMEOUT_S)
        except subprocess.TimeoutExpired:
            raise Fail(f"run {i} of {runs} timed out after {TIMEOUT_S} s")
        tail = "\n".join(p.stderr.strip().splitlines()[-10:])
        if p.returncode != 0:
            raise Fail(f"run {i} of {runs} exited with {p.returncode}\nstderr tail:\n{tail}")
        lines = [ln for ln in p.stdout.splitlines() if ln.strip()]
        v = parse_value(lines[-1]) if lines else None
        if v is None:
            last = lines[-1][:120] if lines else "(no output)"
            raise Fail(f"run {i} of {runs}: last non empty line is not a number: {last}\nstderr tail:\n{tail}")
        values.append(v)
    return values


def parse_values(text: str) -> list[float]:
    out = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            v = float(part)
        except ValueError:
            raise Fail(f"'{part}' in --values is not a number")
        if not math.isfinite(v):
            raise Fail(f"'{part}' in --values is not a finite number")
        out.append(v)
    if not out:
        raise Fail("--values needs at least one number, for example 1.2,1.3,1.1")
    return out


# ---------------------------------------------------------------- commands

def cmd_init(a: argparse.Namespace) -> int:
    gp, lp, _ = paths(a.dir)
    if gp.exists() and not a.force:
        raise Fail(f"{gp} already exists (use --force to replace it)")
    if a.min_gain_pct < 0 or a.max_turns < 1 or a.max_flat < 1 or not math.isfinite(a.target):
        raise Fail("--min-gain-pct must be 0 or more, --max-turns and --max-flat 1 or more, --target a number")
    Path(a.dir).mkdir(parents=True, exist_ok=True)
    goal = {"goal_name": a.goal_name, "unit": a.unit, "direction": a.direction, "target": a.target,
            "min_gain_pct": a.min_gain_pct, "max_turns": a.max_turns, "max_flat": a.max_flat,
            "baseline_median": None, "noise_pct": None}
    save_goal(a.dir, goal)
    with lp.open("w", newline="", encoding="utf-8") as fh:
        csv.writer(fh).writerow(HEADER)
    print(f"Wrote {gp} and {lp}")
    print(f"Next: measure the baseline with at least 5 runs (measure --baseline).")
    return 0


def decide(a: argparse.Namespace, values: list[float], baseline: bool) -> int:
    goal = load_goal(a.dir)
    rows = load_log(a.dir)
    u = goal["unit"]
    med = statistics.median(values)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    label = a.label or ("baseline" if baseline else "")
    print("Runs: " + ", ".join(fmt(v) for v in values) + f" {u}")
    print(f"Median: {fmt(med)} {u}")

    row = {"ts": now, "run_values": ";".join(fmt(v) for v in values), "label": label,
           "median": fmt(med), "note": a.note or ""}
    if baseline:
        if len(values) < 5:
            raise Fail("a baseline needs at least 5 runs to measure noise")
        spread = max(values) - min(values)
        if med == 0 and spread != 0:
            raise Fail("median is 0 but the runs differ, noise_pct cannot be computed")
        noise = 0.0 if spread == 0 else spread / abs(med) * 100
        goal["baseline_median"], goal["noise_pct"] = med, round(noise, 4)
        save_goal(a.dir, goal)
        append_log(a.dir, {**row, "turn": 0, "best_so_far": fmt(med), "kept": "baseline"})
        print(f"BASELINE recorded: median {fmt(med)} {u}, noise {pct(noise)} percent "
              f"(a change must gain at least {pct(max(goal['min_gain_pct'], noise))} percent to count)")
        verdict_code = 0
    else:
        best = best_so_far(goal, rows)
        if best is None:
            raise Fail("no baseline yet (run measure --baseline --runs 5 first)")
        d = goal["direction"]
        need = max(goal["min_gain_pct"], goal.get("noise_pct") or 0)
        g = gain_pct(d, med, best)
        if meets(d, med, goal["target"]) and not better(d, best, med):
            kind, new_best, verdict_code = "met", med, 0
            print(f"GOAL MET: median {fmt(med)} {u} reaches the target {fmt(goal['target'])} {u} "
                  f"(best before {fmt(best)} {u}). Commit after the project's gate passes.")
        elif g >= need:
            kind, new_best, verdict_code = "keep", med, 0
            print(f"KEEP: median {fmt(med)} {u} beats best {fmt(best)} {u} by {pct(g)} percent "
                  f"(needed {pct(need)}). Commit after the project's gate passes.")
        else:
            kind, new_best, verdict_code = "revert", best, 1
            print(f"REVERT: median {fmt(med)} {u} against best {fmt(best)} {u} is a gain of {pct(g)} percent "
                  f"(needed {pct(need)}). Undo the change.")
        turn = sum(1 for r in rows if r["kept"] != "baseline") + 1
        append_log(a.dir, {**row, "turn": turn, "best_so_far": fmt(new_best), "kept": kind})
        rows = load_log(a.dir)
        if kind != "met":
            recent = [r["kept"] for r in rows if r["kept"] != "baseline"][-goal["max_flat"]:]
            if turn >= goal["max_turns"]:
                print("STOP: turn budget used")
                verdict_code = 3
            elif len(recent) >= goal["max_flat"] and all(k == "revert" for k in recent):
                print(f"STOP: no gain in {goal['max_flat']} tries")
                verdict_code = 3
    try:
        write_chart(a.dir)
        print(f"Chart: {paths(a.dir)[2]}")
    except OSError as exc:
        raise Fail(f"result logged, but the chart could not be written ({exc})")
    return verdict_code


def cmd_measure(a: argparse.Namespace) -> int:
    runs = a.runs if a.runs is not None else (5 if a.baseline else 3)
    if runs < 1:
        raise Fail("--runs must be 1 or more")
    if a.baseline and runs < 5:
        raise Fail("a baseline needs at least 5 runs to measure noise (use --runs 5 or more)")
    load_goal(a.dir)
    return decide(a, run_command(a.cmd, runs), a.baseline)


def cmd_record(a: argparse.Namespace) -> int:
    values = parse_values(a.values)
    return decide(a, values, a.baseline)


def cmd_status(a: argparse.Namespace) -> int:
    goal = load_goal(a.dir)
    for line in summary_lines(summary(goal, load_log(a.dir))):
        print(line)
    print(f"Log rows: {len(load_log(a.dir))}")
    return 0


# ---------------------------------------------------------------- chart

CSS = """
:root{--bg:#fbf8f2;--fg:#231f1a;--mute:#6f675c;--line:#2a63d8;--goal:#1d8a4a;--base:#8a6d1d;--bad:#b3392f;--card:#f0ebe1;--grid:#d9d2c4}
@media (prefers-color-scheme:dark){:root{--bg:#171512;--fg:#f0ebe1;--mute:#a79f91;--line:#7aa5ff;--goal:#58c985;--base:#d6b45a;--bad:#ef7f74;--card:#26221d;--grid:#3a352d}}
*{box-sizing:border-box}
body{margin:0;padding:16px;background:var(--bg);color:var(--fg);font:16px/1.4 system-ui,sans-serif}
main{max-width:720px;margin:0 auto}
h1{font-size:1.15rem;margin:0 0 12px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:8px;margin:0 0 16px}
.stat{background:var(--card);border-radius:8px;padding:8px 10px}
.stat b{display:block;font-size:.75rem;font-weight:600;color:var(--mute)}
.stat span{font-size:1.05rem}
svg{display:block;width:100%;height:auto}
svg text{fill:var(--mute);font-size:10px}
.axis{stroke:var(--grid);stroke-width:1}
.series{fill:none;stroke:var(--line);stroke-width:2}
.dot-kept{fill:var(--line);stroke:var(--line);stroke-width:2}
.dot-revert{fill:var(--bg);stroke:var(--bad);stroke-width:2}
.goal{stroke:var(--goal);stroke-width:1.5;stroke-dasharray:6 4}
.base{stroke:var(--base);stroke-width:1.5;stroke-dasharray:2 3}
.goal-t{fill:var(--goal)!important}
.base-t{fill:var(--base)!important}
.legend{font-size:.8rem;color:var(--mute);margin:6px 0 16px}
table{width:100%;border-collapse:collapse;font-size:.8rem}
th,td{text-align:left;padding:4px 6px;border-bottom:1px solid var(--grid);overflow-wrap:anywhere}
.wrap{overflow-x:auto}
"""


def build_svg(goal: dict, rows: list[dict]) -> str:
    w, h, ml, mr, mt, mb = 360, 220, 44, 10, 14, 24
    meds = [float(r["median"]) for r in rows]
    marks = [goal["target"]] + ([goal["baseline_median"]] if goal.get("baseline_median") is not None else [])
    vals = meds + marks
    lo, hi = min(vals), max(vals)
    if hi == lo:
        hi, lo = hi + 1, lo - 1
    pad = (hi - lo) * 0.08
    lo, hi = lo - pad, hi + pad

    def y(v: float) -> float:
        return mt + (hi - v) / (hi - lo) * (h - mt - mb)

    n = len(rows)

    def x(i: int) -> float:
        return ml + ((w - ml - mr) / 2 if n <= 1 else i * (w - ml - mr) / (n - 1))

    out = [f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="Median per measurement against the goal">']
    for v in (lo + pad, hi - pad):
        out.append(f'<line class="axis" x1="{ml}" x2="{w - mr}" y1="{y(v):.1f}" y2="{y(v):.1f}"/>')
        out.append(f'<text x="{ml - 4}" y="{y(v) + 3:.1f}" text-anchor="end">{html.escape(fmt(round(v, 4)))}</text>')
    out.append(f'<line class="goal" x1="{ml}" x2="{w - mr}" y1="{y(goal["target"]):.1f}" y2="{y(goal["target"]):.1f}"/>')
    out.append(f'<text class="goal-t" x="{ml + 2}" y="{y(goal["target"]) - 3:.1f}">goal {html.escape(fmt(goal["target"]))}</text>')
    if goal.get("baseline_median") is not None:
        yb = y(goal["baseline_median"])
        out.append(f'<line class="base" x1="{ml}" x2="{w - mr}" y1="{yb:.1f}" y2="{yb:.1f}"/>')
        out.append(f'<text class="base-t" x="{w - mr - 2}" y="{yb + 11:.1f}" text-anchor="end">'
                   f'baseline {html.escape(fmt(goal["baseline_median"]))}</text>')
    if n:
        pts = " ".join(f"{x(i):.1f},{y(m):.1f}" for i, m in enumerate(meds))
        out.append(f'<polyline class="series" points="{pts}"/>')
        for i, r in enumerate(rows):
            cls = "dot-kept" if r["kept"] in KEPT_KINDS else "dot-revert"
            out.append(f'<circle class="{cls}" cx="{x(i):.1f}" cy="{y(meds[i]):.1f}" r="4">'
                       f'<title>{html.escape(r["label"])}: {html.escape(r["median"])} ({html.escape(r["kept"])})</title></circle>')
        out.append(f'<text x="{x(0):.1f}" y="{h - 8}" text-anchor="middle">1</text>')
        if n > 1:
            out.append(f'<text x="{x(n - 1):.1f}" y="{h - 8}" text-anchor="middle">{n}</text>')
    else:
        out.append(f'<text x="{w / 2}" y="{h / 2}" text-anchor="middle">No measurements yet</text>')
    out.append("</svg>")
    return "\n".join(out)


def write_chart(d: str) -> Path:
    goal = load_goal(d)
    rows = load_log(d)
    s = summary(goal, rows)
    u = goal["unit"]
    word = "at most" if goal["direction"] == "lower" else "at least"
    best = "none yet" if s["best"] is None else f"{fmt(s['best'])} {u}"
    if s["gap"] is None:
        gap = "unknown"
    elif s["gap"] == 0:
        gap = "0, target reached"
    else:
        gap = f"{fmt(s['gap'])} {u} ({pct(s['gap_pct'])}%)"
    noise = "not measured" if s["noise"] is None else f"{pct(s['noise'])}%"
    cards = [("Goal", f"{goal['goal_name']}: {word} {fmt(goal['target'])} {u}"),
             ("Best so far", best), ("Gap left", gap),
             ("Turns used", f"{s['turns']} of {goal['max_turns']}"), ("Noise", noise)]
    stats = "".join(f'<div class="stat"><b>{html.escape(k)}</b><span>{html.escape(v)}</span></div>' for k, v in cards)
    trs = "".join(
        "<tr>" + "".join(f"<td>{html.escape(r[c])}</td>" for c in ("turn", "label", "median", "kept", "note")) + "</tr>"
        for r in rows)
    data = json.dumps({"goal": goal, "rows": rows}).replace("</", "<\\/")
    page = (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<meta name="color-scheme" content="light dark">\n'
        f"<title>{html.escape(goal['goal_name'])}: progress</title>\n<style>{CSS}</style>\n</head>\n<body>\n<main>\n"
        f"<h1>{html.escape(goal['goal_name'])}</h1>\n<div class=\"stats\">{stats}</div>\n"
        f"{build_svg(goal, rows)}\n"
        '<p class="legend">Line: median per row. Filled dot: kept or baseline. Hollow dot: reverted. '
        "Green dashed: goal. Gold dotted: baseline.</p>\n"
        '<div class="wrap"><table><thead><tr><th>Turn</th><th>Label</th><th>Median</th><th>Result</th><th>Note</th></tr></thead>'
        f"<tbody>{trs}</tbody></table></div>\n</main>\n"
        f'<script type="application/json" id="data">{data}</script>\n</body>\n</html>\n')
    cp = paths(d)[2]
    cp.write_text(page, encoding="utf-8")
    return cp


def cmd_chart(a: argparse.Namespace) -> int:
    try:
        print(f"Wrote {write_chart(a.dir)}")
    except OSError as exc:
        raise Fail(f"could not write the chart ({exc})")
    return 0


# ---------------------------------------------------------------- main

def build_parser() -> argparse.ArgumentParser:
    ap = Parser(prog="goal_loop.py", description=__doc__.splitlines()[0],
                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=None)
    sub = ap.add_subparsers(dest="command", required=True)

    def add(name: str, fn, help_text: str) -> argparse.ArgumentParser:
        p = sub.add_parser(name, help=help_text, description=help_text)
        p.add_argument("--dir", default=".progress", help="state folder (default .progress)")
        p.set_defaults(fn=fn)
        return p

    p = add("init", cmd_init, "write goal.json and an empty log.csv")
    p.add_argument("--goal-name", required=True)
    p.add_argument("--unit", required=True)
    p.add_argument("--direction", required=True, choices=["lower", "higher"])
    p.add_argument("--target", required=True, type=float)
    p.add_argument("--min-gain-pct", type=float, default=5.0)
    p.add_argument("--max-turns", type=int, default=50)
    p.add_argument("--max-flat", type=int, default=10)
    p.add_argument("--force", action="store_true", help="replace an existing goal.json")

    p = add("measure", cmd_measure, "run a command N times and decide")
    p.add_argument("--cmd", required=True, help="shell command; last non empty stdout line is the number")
    p.add_argument("--runs", type=int, help="runs (default 3, or 5 with --baseline)")
    p.add_argument("--label", default="")
    p.add_argument("--note", default="")
    p.add_argument("--baseline", action="store_true", help="record baseline and noise (5 runs or more)")

    p = add("record", cmd_record, "decide from values given by hand")
    p.add_argument("--label", required=True)
    p.add_argument("--values", required=True, help="comma separated numbers, for example 1.2,1.3,1.1")
    p.add_argument("--note", default="")
    p.add_argument("--baseline", action="store_true", help="record baseline and noise (5 values or more)")

    add("chart", cmd_chart, "write chart.html")
    add("status", cmd_status, "print the summary as text")
    return ap


def main(argv: list[str] | None = None) -> int:
    a = build_parser().parse_args(argv)
    try:
        code = a.fn(a)
    except Fail as exc:
        print(f"could not run: {exc}", file=sys.stderr)
        print(CANNOT_COVER, file=sys.stderr)
        return 2
    print(CANNOT_COVER)
    return code


if __name__ == "__main__":
    sys.exit(main())
