#!/usr/bin/env python3
"""variant_matrix.py: plan a video variant batch (hook x body x CTA x deliverables) with valid names.

Standard library only. Reads a JSON spec, writes a CSV production plan and an append-ready CSV for
ads-master/creative-library/registry.csv, and prints a summary (test cells, files, estimated cost).

Names follow the creative-strategy ad name grammar:
  {launch}_{concept}_{angle}_{persona}_{aware}_{fmt}_{hook}_{creator}_{len}_{ratio}_{ver}[_{flags}]
  File stem = ad name without the launch date.
  Body variants use the ver token (v1, v2). CTA or end card variants, language and AI use go into
  flags joined with hyphens: cta2, Ltr (L + ISO 639-1 code), aiG, aiV, aiP (synthetic performer on screen).

Strategies (one variable family per test, the rest held constant):
  hooks-first   vary hooks; body = bodies[0], cta = ctas[0]           (default for new concepts)
  bodies-first  vary bodies; hook = hooks[0] (the winner), cta = ctas[0]
  ctas-first    vary CTAs or end cards; hook = hooks[0], body = bodies[0]
  full          every combination (warns above --max-files)
Ratios, lengths and languages are deliverables of the same test cell, not extra test cells.

Example spec (JSON):
{
  "launch": "20261015", "concept": "C021", "angle": "hcause", "persona": "runner", "aware": "prob",
  "fmt": "ugc", "creator": "cr07",
  "hooks": ["H01", "H02", "H03", "H04"], "bodies": ["v1", "v2"], "ctas": ["cta1", "cta2"],
  "lengths": ["15s", "30s"], "ratios": ["916", "45"], "languages": ["en"],
  "flags": ["aiV"], "strategy": "hooks-first", "cost_per_file": 0.0, "production_mode": "footage"
}

Usage:
  python3 variant_matrix.py spec.json --out plan.csv --registry-out registry_rows.csv
  python3 variant_matrix.py spec.json --strategy full --max-files 80
  python3 variant_matrix.py --validate "20261015_C021_hcause_runner_prob_ugc_H03_cr07_30s_916_v2_aiV"
"""
import argparse
import csv
import itertools
import json
import re
import sys

AD_RE = re.compile(
    r"^(\d{8})_(C\d{3})_([a-z]+)_([a-z0-9]+)_(unaw|prob|sol|prod|most)_"
    r"(ugc|cre|fdr|demo|test|uvt|list|ps|stat|car|meme|pod|str|gs|ai|cat)_"
    r"(H\d{2}|na)_(cr\d{2}|na)_(\d+s|na)_(916|45|11|169|na)_(v\d+)(_[a-zA-Z0-9-]+)?$"
)
PLACEMENTS = {
    "916": "Meta Reels and Stories, TikTok, YouTube Shorts, LinkedIn mobile vertical",
    "45": "Meta Feed (FB, IG), LinkedIn feed, Demand Gen",
    "11": "Meta Feed, LinkedIn, Demand Gen, carousel cards",
    "169": "YouTube in-stream, Demand Gen, LinkedIn desktop, CTV",
}
REGISTRY_COLUMNS = [
    "creative_id", "ad_name", "concept_id", "hook_id", "body_ver", "cta_id", "format", "length",
    "ratio", "language", "flags", "test_cell", "production_mode", "ai_disclosure", "claims_ids",
    "music_license", "talent_release_ids", "file_path", "status", "created", "owner", "source_brief",
    "learnings",
]


def err(msg):
    sys.exit("error: " + msg)


def check_token(name, value, pattern):
    if not re.fullmatch(pattern, value):
        err(f"token {name}='{value}' does not match {pattern}")


def disclosure_for(flags):
    if "aiP" in flags:
        return "onscreen-synthetic-performer"
    if "aiG" in flags or "aiV" in flags:
        return "platform-label-check"
    return "none"


def build(spec, strategy, max_files):
    req = ["launch", "concept", "angle", "persona", "aware", "fmt", "hooks", "bodies", "ctas", "lengths", "ratios"]
    for k in req:
        if k not in spec or spec[k] in ("", []):
            err(f"spec is missing '{k}'")
    check_token("launch", spec["launch"], r"\d{8}")
    check_token("concept", spec["concept"], r"C\d{3}")
    check_token("angle", spec["angle"], r"[a-z]+")
    check_token("persona", spec["persona"], r"[a-z0-9]+")
    creator = spec.get("creator", "na")
    check_token("creator", creator, r"cr\d{2}|na")
    for h in spec["hooks"]:
        check_token("hook", h, r"H\d{2}|na")
    for b in spec["bodies"]:
        check_token("body (ver)", b, r"v\d+")
    for c in spec["ctas"]:
        check_token("cta", c, r"cta\d+")
    for ln in spec["lengths"]:
        check_token("length", ln, r"\d+s|na")
    for r in spec["ratios"]:
        check_token("ratio", r, r"916|45|11|169")
    langs = spec.get("languages", ["en"])
    for lg in langs:
        check_token("language", lg, r"[a-z]{2}")
    base_flags = spec.get("flags", [])
    for f in base_flags:
        check_token("flag", f, r"[a-zA-Z0-9]+")

    hooks, bodies, ctas = spec["hooks"], spec["bodies"], spec["ctas"]
    if strategy == "hooks-first":
        cells = [(h, bodies[0], ctas[0]) for h in hooks]
    elif strategy == "bodies-first":
        cells = [(hooks[0], b, ctas[0]) for b in bodies]
    elif strategy == "ctas-first":
        cells = [(hooks[0], bodies[0], c) for c in ctas]
    elif strategy == "full":
        cells = list(itertools.product(hooks, bodies, ctas))
    else:
        err(f"unknown strategy {strategy}")

    rows = []
    for idx, (h, b, c) in enumerate(cells, 1):
        cell_id = f"{spec['concept']}-T{idx:02d}"
        for ln, r, lg in itertools.product(spec["lengths"], spec["ratios"], langs):
            flags = list(base_flags)
            if c != "cta1":
                flags.append(c)
            if lg != spec.get("primary_language", "en"):
                flags.append("L" + lg)
            flag_tok = ("_" + "-".join(flags)) if flags else ""
            stem = (f"{spec['concept']}_{spec['angle']}_{spec['persona']}_{spec['aware']}_{spec['fmt']}_"
                    f"{h}_{creator}_{ln}_{r}_{b}{flag_tok}")
            ad_name = f"{spec['launch']}_{stem}"
            if not AD_RE.match(ad_name):
                err(f"generated name does not parse: {ad_name}")
            rows.append({
                "test_cell": cell_id, "ad_name": ad_name, "file_name": stem + ".mp4", "hook": h, "body": b,
                "cta": c, "length": ln, "ratio": r, "language": lg, "flags": "-".join(flags),
                "placement_hint": PLACEMENTS[r], "status": "planned",
            })
    if len(rows) > max_files:
        print(f"WARNING: {len(rows)} files exceeds --max-files {max_files}. Cut ratios, lengths or "
              f"languages, or test one variable family at a time.", file=sys.stderr)
    return cells, rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", nargs="?", help="JSON spec file")
    ap.add_argument("--strategy", help="override spec strategy")
    ap.add_argument("--out", help="production plan CSV")
    ap.add_argument("--registry-out", help="append-ready rows for creative-library/registry.csv")
    ap.add_argument("--max-files", type=int, default=60)
    ap.add_argument("--owner", default="video-studio")
    ap.add_argument("--created", default="", help="YYYY-MM-DD for registry rows")
    ap.add_argument("--validate", help="validate one ad name and exit")
    args = ap.parse_args()

    if args.validate:
        ok = bool(AD_RE.match(args.validate))
        print(("VALID   " if ok else "INVALID ") + args.validate)
        sys.exit(0 if ok else 1)
    if not args.spec:
        ap.error("spec is required unless --validate is used")
    with open(args.spec, encoding="utf-8") as fh:
        spec = json.load(fh)
    strategy = args.strategy or spec.get("strategy", "hooks-first")
    cells, rows = build(spec, strategy, args.max_files)

    if args.out:
        with open(args.out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    if args.registry_out:
        with open(args.registry_out, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=REGISTRY_COLUMNS)
            w.writeheader()
            for r in rows:
                w.writerow({
                    "creative_id": r["file_name"][:-4], "ad_name": r["ad_name"], "concept_id": spec["concept"],
                    "hook_id": r["hook"], "body_ver": r["body"], "cta_id": r["cta"], "format": spec["fmt"],
                    "length": r["length"], "ratio": r["ratio"], "language": r["language"], "flags": r["flags"],
                    "test_cell": r["test_cell"], "production_mode": spec.get("production_mode", ""),
                    "ai_disclosure": disclosure_for(r["flags"].split("-")), "claims_ids": spec.get("claims_ids", ""),
                    "music_license": spec.get("music_license", ""), "talent_release_ids": spec.get("talent_release_ids", ""),
                    "file_path": "", "status": "planned", "created": args.created, "owner": args.owner,
                    "source_brief": spec.get("source_brief", ""), "learnings": "",
                })
    cost = spec.get("cost_per_file", 0) * len(rows)
    print(f"strategy: {strategy}")
    print(f"test cells: {len(cells)} (each cell is one ad concept variant the channel agent tests)")
    print(f"files: {len(rows)} (cells x lengths x ratios x languages)")
    if cost:
        print(f"estimated production cost: {cost:.2f} (cost_per_file x files; add rerolls)")
    for c_idx, (h, b, c) in enumerate(cells, 1):
        print(f"  {spec['concept']}-T{c_idx:02d}: hook {h} | body {b} | {c}")
    if not args.out:
        for r in rows[:12]:
            print("  " + r["ad_name"])
        if len(rows) > 12:
            print(f"  ... {len(rows) - 12} more (use --out)")


if __name__ == "__main__":
    main()
