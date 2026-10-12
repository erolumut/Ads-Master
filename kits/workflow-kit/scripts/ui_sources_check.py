#!/usr/bin/env python3
"""Check UI sources against the project's UI-SOURCES.md ledger and policy.

Reads docs/UI-SOURCES.md (copied from templates/UI-SOURCES.md) and every
package.json under the root (node_modules, .git and build folders skipped), then
fails when:
  - a banned package (Banned table) is a dependency
  - a UI dependency (built in patterns plus the Watch table) has no ledger row
  - a ledger row has no licence, an "unknown" licence, or no Reviewed on date
  - a review is older than --max-age days (default 365)
  - a copied row has no Origin URL, or a Used in path that does not exist
Warnings (exit 0): ledger packages no longer installed, copyleft or source
available licences that need a decision record, copied files without an
origin comment.

  python3 ui_sources_check.py
  python3 ui_sources_check.py docs/UI-SOURCES.md --root . --max-age 180 --today 2026-10-12

Exit codes: 0 pass, 1 fail, 2 could not run. Standard library only.
"""
from __future__ import annotations

import argparse
import datetime
import fnmatch
import json
import re
import sys
from pathlib import Path

CANNOT_COVER = ("This gate cannot cover: code copied without a ledger row, whether a licence named in the "
                "ledger is the real one, accessibility and design fit of a source (a reviewer checks those), "
                "and dependencies outside package.json (CDN script tags, Liquid assets, vendored files).")
SKIP_DIRS = {"node_modules", ".git", ".next", "dist", "build", "out", ".turbo", ".vercel", "coverage", ".data"}
UI_PATTERNS = [
    "@radix-ui/*", "radix-ui", "@base-ui/*", "@base-ui-components/*", "react-aria*", "@react-aria/*",
    "@ark-ui/*", "@headlessui/*", "@mui/*", "@mantine/*", "@chakra-ui/*", "antd", "@shopify/polaris*",
    "motion", "framer-motion", "gsap", "@gsap/*", "@react-spring/*", "lottie*", "@lottiefiles/*", "@rive-app/*",
    "auto-animate", "@formkit/auto-animate", "react-transition-group",
    "recharts", "chart.js", "react-chartjs-2", "echarts", "echarts-for-react", "@visx/*", "d3", "d3-*",
    "uplot", "@observablehq/plot", "@nivo/*", "victory*", "@tremor/*", "@unovis/*", "liveline",
    "lucide*", "@heroicons/*", "@phosphor-icons/*", "@tabler/icons*", "react-icons", "@fortawesome/*",
    "@iconify/*", "@remixicon/*",
    "sonner", "vaul", "cmdk", "input-otp", "@number-flow/*", "embla-carousel*", "swiper", "keen-slider",
    "@dnd-kit/*", "react-day-picker", "react-virtuoso", "@tanstack/react-table", "@tanstack/react-virtual",
    "class-variance-authority", "tailwind-variants", "tailwind-merge", "tw-animate-css", "tailwindcss-animate",
    "@tailwindcss/typography", "@tailwindcss/forms", "react-leaflet", "leaflet", "react-map-gl", "mapbox-gl",
    "maplibre-gl", "three", "@react-three/*", "howler", "@silk-hq/*", "react-modal-sheet", "next-themes",
]
REVIEW_LICENCES = re.compile(r"\b(a?gpl|lgpl|sspl|busl|bsl|fsl|elastic|commons clause|proprietary|paid|commercial|cc-by-nc)", re.I)
UNKNOWN = re.compile(r"^(|unknown|\?|tbd|todo|n/?a|-|none)$", re.I)


def tables(text: str) -> dict[str, list[dict[str, str]]]:
    """Map each '## Heading' to the rows of the first table under it."""
    out: dict[str, list[dict[str, str]]] = {}
    section, header = "", None
    for line in text.splitlines():
        if line.startswith("## "):
            section, header = line[3:].strip().lower(), None
            continue
        if not line.lstrip().startswith("|"):
            if header is not None and line.strip():
                header = None
            continue
        cells = [c.strip().strip("`").strip() for c in line.strip().strip("|").split("|")]
        if header is None:
            header = [c.lower() for c in cells]
            out.setdefault(section, [])
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        row = dict(zip(header, cells))
        if any(v and not v.startswith("<") for v in row.values()):
            out[section].append(row)
    return out


def col(row: dict[str, str], name: str) -> str:
    for k, v in row.items():
        if k.startswith(name):
            return v
    return ""


def find(sections: dict[str, list[dict[str, str]]], word: str) -> list[dict[str, str]]:
    for name, rows in sections.items():
        if word in name:
            return rows
    return []


def package_files(root: Path) -> list[Path]:
    found = []
    for p in root.rglob("package.json"):
        rel = p.relative_to(root).parts
        if any(part in SKIP_DIRS for part in rel) or len(rel) > 5:
            continue
        found.append(p)
    return sorted(found)


def deps_of(files: list[Path]) -> dict[str, list[str]]:
    deps: dict[str, list[str]] = {}
    for f in files:
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for key in ("dependencies", "devDependencies", "peerDependencies", "optionalDependencies"):
            for name in (data.get(key) or {}):
                deps.setdefault(name, []).append(str(f))
    return deps


def matches(name: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(name, p) for p in patterns)


def names_in(cell: str) -> list[str]:
    return [n.strip().strip("`") for n in re.split(r"[,;]| and ", cell) if n.strip()]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("path", nargs="?", default="docs/UI-SOURCES.md")
    ap.add_argument("--root", default=".")
    ap.add_argument("--max-age", type=int, default=365)
    ap.add_argument("--today")
    a = ap.parse_args(argv)
    root, ledger_path = Path(a.root), Path(a.path)
    if not ledger_path.is_file():
        print(f"could not run: {ledger_path} not found (copy templates/UI-SOURCES.md first)")
        print(CANNOT_COVER)
        return 2
    sections = tables(ledger_path.read_text(encoding="utf-8"))
    ledger = [r for r in find(sections, "ledger") if col(r, "source")]
    if "ledger" not in " ".join(sections):
        print("could not run: no '## Ledger' table with Source, Kind, Licence and Reviewed on columns")
        print(CANNOT_COVER)
        return 2
    files = package_files(root)
    if not files:
        print(f"could not run: no package.json under {root} (for a project without npm, keep the ledger "
              "and review it by hand; this script only reads package.json)")
        print(CANNOT_COVER)
        return 2
    today = datetime.date.fromisoformat(a.today) if a.today else datetime.date.today()
    deps = deps_of(files)
    banned = [n for r in find(sections, "banned") for n in names_in(col(r, "package") or col(r, "source"))]
    watch = UI_PATTERNS + [n for r in find(sections, "watch") for n in names_in(col(r, "pattern") or col(r, "package"))]
    listed: set[str] = set()
    for r in ledger:
        listed.update(names_in(col(r, "source")))
    fails, warns = [], []

    for name, where in sorted(deps.items()):
        if banned and matches(name, banned):
            fails.append(f"banned package {name} is a dependency in {', '.join(where)}")
        elif matches(name, watch) and name not in listed:
            fails.append(f"UI dependency {name} ({', '.join(where)}) has no ledger row")

    for r in ledger:
        src, kind = col(r, "source"), col(r, "kind").lower()
        lic, when, origin, used = col(r, "licence") or col(r, "license"), col(r, "reviewed"), col(r, "origin"), col(r, "used")
        tag = f"ledger row '{src}'"
        if UNKNOWN.match(lic):
            fails.append(f"{tag}: licence missing or unknown; find the LICENSE file or do not use it")
        elif REVIEW_LICENCES.search(lic):
            warns.append(f"{tag}: licence '{lic}' needs a decision record (terms, seats, redistribution)")
        try:
            d = datetime.date.fromisoformat(when)
            if (today - d).days > a.max_age:
                fails.append(f"{tag}: reviewed {when}, older than {a.max_age} days; re-run the vetting checklist")
        except ValueError:
            fails.append(f"{tag}: Reviewed on must be YYYY-MM-DD")
        if kind.startswith("package") and not any(n in deps for n in names_in(src)):
            warns.append(f"{tag}: not in any package.json; remove the row or note why it stays")
        if kind.startswith("cop"):
            if not origin.startswith("http"):
                fails.append(f"{tag}: copied code needs an Origin URL")
            for path in names_in(used):
                f = root / path
                if not f.exists():
                    fails.append(f"{tag}: Used in path {path} does not exist")
                elif f.is_file() and origin.startswith("http"):
                    try:
                        if origin not in f.read_text(encoding="utf-8", errors="ignore"):
                            warns.append(f"{tag}: {path} has no origin comment with {origin}")
                    except OSError:
                        pass

    print(f"{len(files)} package.json files, {len(deps)} dependencies, {len(ledger)} ledger rows, "
          f"{len(banned)} banned entries")
    for f in fails:
        print("FAIL", f)
    for w in warns:
        print("WARN", w)
    print("Verdict: " + ("FAIL" if fails else "PASS"))
    print(CANNOT_COVER)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
