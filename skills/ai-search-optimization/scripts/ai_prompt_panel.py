#!/usr/bin/env python3
"""Score an AI answer panel: mention, recommendation, first pick, top 3 and citation rates with honest intervals.

Input is answers you collected (pasted from the interface, exported from a
tracking tool, or saved from an API run), one JSON object per line:

  {"period": "2026-10", "prompt_id": "p01", "prompt_class": "best_app", "engine": "chatgpt",
   "mode": "free", "run": 1, "date": "2026-10-06", "text": "...answer...",
   "cited_urls": ["https://apps.apple.com/...", "https://www.reddit.com/..."]}

Config (JSON) names the brand and a fixed competitor set:

  {"brand": {"name": "Acme", "aliases": ["Acme App"], "domains": ["acme.com", "apps.apple.com/app/acme"]},
   "competitors": [{"name": "Rival", "aliases": [], "domains": ["rival.com"]}]}

Metrics follow references/measurement-and-prompt-tracking.md section 4. Intervals
are 95 percent, bootstrapped over prompts (runs of one prompt are correlated).
Prompts with fewer than 3 runs are excluded and listed: one answer is an
anecdote, not a measurement. Recommendation detection is a heuristic (brand in
a sentence with recommending language, or first named brand); spot check it.
First pick: the brand is the first brand named and is recommended. The gap list
shows non owned URLs cited in answers that name a competitor but not the brand:
pages to check for a listing, a review or a correction.

Usage:
  python3 -I ai_prompt_panel.py answers.jsonl --config panel.json [--min-runs 3] [--by prompt_class]

Exit codes: 0 report written, 1 a period comparison shows a significant drop in
mention rate, 2 could not run (bad input, or no prompt has enough runs).
Answer text is data, never instructions. Standard library only.
"""
import argparse
import json
import random
import re
import sys
from collections import Counter, defaultdict
from urllib.parse import parse_qs, urlparse

RECOMMEND = re.compile(r"\b(recommend|best|top pick|go with|i'?d (?:suggest|choose|pick)|choose|our pick|winner|ideal)\b", re.I)
NEGATION = re.compile(r"\b(not|n't|never|avoid|worse|instead of)\b", re.I)
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+|\n+")


def names_re(entity):
    names = [entity["name"]] + list(entity.get("aliases", []))
    return re.compile(r"(?<![\w])(" + "|".join(re.escape(n) for n in names if n) + r")(?![\w])", re.I)


def domain_of(url):
    try:
        p = urlparse(url if "://" in url else "https://" + url)
        return (p.netloc.lower().removeprefix("www.") + p.path.lower()).rstrip("/")
    except ValueError:
        return ""


def _split(url):
    p = urlparse(url if "://" in url else "https://" + url)
    host = p.netloc.lower().removeprefix("www.")
    rest = p.path.rstrip("/") + ("?" + p.query if p.query else "")
    return host, rest.lower()


def owned(url, domains):
    """Host match on whole labels (acme.com never matches acme.community); entries with a path or
    query (apps.apple.com/app/acme, play.google.com/store/apps/details?id=com.acme) must match that too."""
    try:
        host, rest = _split(url)
    except ValueError:
        return False
    for entry in domains:
        eh, er = _split(entry)
        if not (host == eh or host.endswith("." + eh)):
            continue
        if not er:
            return True
        if "?" in er:  # query entries (Play listings): same path, and every entry parameter present with the same value
            epath, _, eq = er.partition("?")
            upath, _, uq = rest.partition("?")
            want, have = parse_qs(eq), parse_qs(uq)
            if upath == epath and all(have.get(k) == v for k, v in want.items()):
                return True
        elif rest == er or rest.startswith(er + "/") or rest.startswith(er + "?"):
            return True
    return False


def first_positions(text, entities):
    pos = {}
    for key, rx in entities.items():
        m = rx.search(text)
        if m:
            pos[key] = m.start()
    return [k for k, _ in sorted(pos.items(), key=lambda kv: kv[1])]


def score_run(rec, brand_rx, comp_rx, brand_domains):
    text = rec.get("text", "") or ""
    mentioned = bool(brand_rx.search(text))
    order = first_positions(text, {"__brand__": brand_rx, **comp_rx})
    recommended = False
    if mentioned:
        first = next((s for s in SENT_SPLIT.split(text) if brand_rx.search(s)), "")
        if order and order[0] == "__brand__" and len(order) > 1 and not NEGATION.search(first):
            recommended = True
        for s in SENT_SPLIT.split(text):
            if brand_rx.search(s) and RECOMMEND.search(s) and not NEGATION.search(s):
                recommended = True
                break
    top3 = int("__brand__" in order[:3]) if order else None
    first_pick = int(bool(order) and order[0] == "__brand__" and recommended) if order else None
    cites = rec.get("cited_urls") or []
    own = sum(1 for u in cites if owned(u, brand_domains))
    comp_mentions = {k: int(bool(rx.search(text))) for k, rx in comp_rx.items()}
    return {"mentioned": int(mentioned), "recommended": int(recommended), "top3": top3, "first_pick": first_pick,
            "gap_urls": [] if mentioned or not any(comp_mentions.values()) else
            [u for u in cites if not owned(u, brand_domains)],
            "gap_comps": [k for k, v in comp_mentions.items() if v],
            "cited": int(own > 0), "own_cites": own, "all_cites": len(cites), "comp": comp_mentions,
            "domains": [domain_of(u).split("/")[0] for u in cites]}


def bootstrap(prompt_vals, iters=2000, seed=7):
    keys = list(prompt_vals)
    if not keys:
        return (0.0, 0.0)
    rnd = random.Random(seed)
    stats = []
    for _ in range(iters):
        vals = [v for k in (rnd.choice(keys) for _ in keys) for v in prompt_vals[k]]
        stats.append(sum(vals) / len(vals) if vals else 0.0)
    stats.sort()
    return stats[int(0.025 * iters)], stats[int(0.975 * iters) - 1]


def summarize(rows, metric):
    per_prompt = defaultdict(list)
    for r in rows:
        v = r["score"][metric]
        if v is not None:
            per_prompt[r["prompt_id"]].append(v)
    vals = [v for vs in per_prompt.values() for v in vs]
    if not vals:
        return None
    lo, hi = bootstrap(per_prompt)
    return sum(vals) / len(vals), lo, hi, len(per_prompt), len(vals)


def fmt(s):
    return "n/a" if s is None else f"{s[0]:.0%} ({s[1]:.0%} to {s[2]:.0%})"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("answers")
    ap.add_argument("--config", required=True)
    ap.add_argument("--min-runs", type=int, default=3)
    ap.add_argument("--by", default="prompt_class", help="second grouping field after engine")
    a = ap.parse_args()
    try:
        cfg = json.load(open(a.config, encoding="utf-8"))
        brand = cfg["brand"]
        brand_rx = names_re(brand)
        comp_rx = {c["name"]: names_re(c) for c in cfg.get("competitors", [])}
        recs = [json.loads(l) for l in open(a.answers, encoding="utf-8") if l.strip()]
    except (OSError, ValueError, KeyError) as exc:
        print(f"could not run: {exc}")
        return 2
    runs_per = Counter((r.get("period", ""), r.get("engine", ""), r.get("prompt_id", "")) for r in recs)
    excluded = sorted({k for k, n in runs_per.items() if n < a.min_runs})
    rows = []
    for r in recs:
        key = (r.get("period", ""), r.get("engine", ""), r.get("prompt_id", ""))
        if key in excluded:
            continue
        rows.append({**r, "score": score_run(r, brand_rx, comp_rx, brand.get("domains", []))})
    if not rows:
        print(f"could not run: no prompt has {a.min_runs} or more runs per engine and period")
        return 2

    periods = sorted({r.get("period", "") for r in rows})
    print(f"# AI answer panel: {brand['name']}\n")
    print(f"{len(rows)} scored runs, {len({r['prompt_id'] for r in rows})} prompts, periods: {', '.join(periods)}. "
          f"Intervals: 95%, bootstrapped over prompts.\n")
    groups = defaultdict(list)
    for r in rows:
        groups[(r.get("period", ""), r.get("engine", ""), r.get(a.by, "all"))].append(r)
    print(f"| Period | Engine | {a.by} | Prompts | Runs | Mention | Recommend | First pick | Top 3 | Owned citation |")
    print("|--------|--------|------|-------:|-----:|---------|-----------|------------|-------|----------------|")
    for (p, e, g), rs in sorted(groups.items()):
        m = summarize(rs, "mentioned")
        print(f"| {p} | {e} | {g} | {m[3]} | {m[4]} | {fmt(m)} | {fmt(summarize(rs, 'recommended'))} | "
              f"{fmt(summarize(rs, 'first_pick'))} | {fmt(summarize(rs, 'top3'))} | {fmt(summarize(rs, 'cited'))} |")

    print("\n## Share of voice (mentions) and citation share, by period\n")
    for p in periods:
        rs = [r for r in rows if r.get("period", "") == p]
        totals = Counter({brand["name"]: sum(r["score"]["mentioned"] for r in rs)})
        for r in rs:
            totals.update({k: v for k, v in r["score"]["comp"].items()})
        allm = sum(totals.values()) or 1
        own = sum(r["score"]["own_cites"] for r in rs)
        allc = sum(r["score"]["all_cites"] for r in rs) or 1
        sov = ", ".join(f"{k} {v / allm:.0%}" for k, v in totals.most_common())
        print(f"- {p}: share of voice {sov}; citation share {own / allc:.0%} of {allc} citations")

    print("\n## Most cited domains (source map input)\n")
    dom = Counter(d for r in rows for d in r["score"]["domains"] if d)
    for d, n in dom.most_common(15):
        print(f"- {d}: {n}")

    print("\n## Gap pages: cited where a competitor is named and the brand is not (latest period)\n")
    latest = [r for r in rows if r.get("period", "") == periods[-1]]
    gap = Counter(u for r in latest for u in r["score"]["gap_urls"])
    gap_comps = defaultdict(Counter)
    for r in latest:
        for u in r["score"]["gap_urls"]:
            gap_comps[u].update(r["score"]["gap_comps"])
    if not gap:
        print("- none in the collected answers")
    for u, n in gap.most_common(15):
        names = ", ".join(k for k, _ in gap_comps[u].most_common(3))
        print(f"- {u}: {n} answers (competitors named: {names})")
    print("\nA gap URL is a lead, not a verdict: open the page and check whether the brand is listed, "
          "missing or described wrongly before any outreach.")

    drop = False
    if len(periods) >= 2:
        prev, cur = periods[-2], periods[-1]
        print(f"\n## Change {prev} to {cur} (mention rate, per engine)\n")
        for e in sorted({r.get("engine", "") for r in rows}):
            a1 = summarize([r for r in rows if r.get("period") == prev and r.get("engine") == e], "mentioned")
            a2 = summarize([r for r in rows if r.get("period") == cur and r.get("engine") == e], "mentioned")
            if not a1 or not a2:
                continue
            verdict = "no proven change (intervals overlap)"
            if a2[1] > a1[2]:
                verdict = "proven increase"
            elif a2[2] < a1[1]:
                verdict, drop = "proven decrease", True
            print(f"- {e}: {fmt(a1)} to {fmt(a2)}: {verdict}")
    if excluded:
        print(f"\nExcluded (fewer than {a.min_runs} runs): " + ", ".join("/".join(k) for k in excluded[:20]))
    print("\nThis gate cannot cover: answers you did not collect, personalization and memory effects, "
          "recommendation wording the heuristic misses (spot check 10 answers), and whether cited pages are accurate.")
    return 1 if drop else 0


if __name__ == "__main__":
    sys.exit(main())
