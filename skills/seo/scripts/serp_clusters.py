#!/usr/bin/env python3
"""serp_clusters.py: SERP overlap keyword clusters and consolidation candidates (Python 3.10+, standard library only).

Two keywords belong on the same page when Google ranks the same URLs for both. This script
reads a SERP export (top 10 organic URLs per keyword), links keywords whose top 10 sets share
at least T normalized URLs, and groups them into clusters (connected components, computed for
each threshold so you can see how sensitive the result is). With a Search Console export it
also finds clusters where two or more of your own pages get impressions and drafts a
consolidation proposal. It reads files only: no network, nothing is changed.

Usage:
  python3 serp_clusters.py --serp serps.csv
  python3 serp_clusters.py --serp serps.csv --gsc gsc.csv --site www.example.com
  python3 serp_clusters.py --serp serps.csv --gsc gsc.csv --thresholds 3,4,5 --primary 4 \
      --json --out clusters.json

Inputs:
  --serp CSV (required)  columns: keyword, url, position; optional volume. One row per ranking
                         URL. Only organic positions 1 to 10 count. URLs are normalized before
                         comparing: lowercase scheme and host, "www." removed, fragment removed,
                         trailing slash removed, utm_* and gclid/fbclid parameters dropped.
  --gsc CSV (optional)   Search Console export with query, page, clicks, impressions. Common
                         header variants are accepted ("Top queries", "Landing page", any
                         case). An optional conversions column outranks clicks when choosing
                         the URL to keep. Numbers may use a comma as thousands separator.
  --site DOMAIN          your domain, to recognise your own URLs in the SERP file. Without it
                         and with --gsc, your host is inferred from the Search Console pages.
  --thresholds LIST      overlap thresholds to compare, default 3,4,5.
  --primary N            threshold used for the detailed report, default 4.
  --json                 print a JSON document instead of text.
  --out FILE             write the report to FILE instead of stdout.

Intent check: for each keyword in a cluster the top 3 URLs are classified by path as guide
(/blog/, /guide, /how-to, /what-is, /learn, /news, /article), commercial (/product, /products/,
/shop, /collections/, /category, /pricing, /buy, /p/) or other (also used when a path matches
both). When guides and commercial each make up at least 30 percent of those top 3 URLs the
cluster is flagged MIXED INTENT and no merge is proposed.

Exit codes: 0 the check ran (proposals are not failures), 2 it could not run (missing file,
missing required column, empty or unreadable input, bad arguments). The last printed line
always starts "This check cannot cover:". In --json mode that line goes to stderr so that
stdout stays valid JSON.
"""
import argparse
import csv
import io
import json
import math
import sys
from collections import Counter, defaultdict
from urllib import parse

VERSION = "1.0"
MAX_POSITION = 10
THIN_SERP_URLS = 5
MIXED_SHARE_PERCENT = 30
TOP_URLS_FOR_INTENT = 3
GUIDE_MARKERS = ("/blog/", "/guide", "/how-to", "/what-is", "/learn", "/news", "/article")
COMMERCIAL_MARKERS = ("/product", "/products/", "/shop", "/collections/", "/category", "/pricing", "/buy", "/p/")
DROP_PARAMS = ("gclid", "fbclid")
NO_GSC_LINE = "no Search Console data: clusters show what one page should target; consolidation needs GSC"
CANNOT_COVER = ("This check cannot cover: SERP volatility, personalization and location, whether pages truly "
                "serve the same need, backlinks and conversion value outside the files, and AI Overview features.")
APPROVAL_LINE = ("Proposal only, nothing has been changed. Content merges and 301 redirects need explicit human "
                 "approval (gate G3) and site-engineer release QA before anything goes live.")

SERP_ALIASES = {
    "keyword": ("keyword", "keywords", "query", "search term", "search query"),
    "url": ("url", "result url", "ranking url", "organic url"),
    "position": ("position", "rank", "pos", "organic position", "ranking position"),
    "volume": ("volume", "search volume", "monthly volume", "msv"),
}
GSC_ALIASES = {
    "query": ("query", "queries", "top queries", "top query", "search query", "search queries"),
    "page": ("page", "pages", "top pages", "landing page", "landing pages", "url"),
    "clicks": ("clicks", "click"),
    "impressions": ("impressions", "impression"),
    "conversions": ("conversions", "conversion", "key events", "goal completions"),
}


class InputError(Exception):
    """The check could not run (exit code 2)."""


# ---------------------------------------------------------------- normalization
def clean_keyword(text):
    return " ".join(text.lower().split())


def normalize_url(url):
    """Lowercase scheme and host, drop www., fragment, trailing slash, utm_* and gclid/fbclid parameters."""
    raw = url.strip()
    if raw.startswith("/") and not raw.startswith("//"):
        raise ValueError("relative URL")
    if "://" not in raw:
        raw = "https://" + raw.lstrip("/")
    p = parse.urlsplit(raw)
    scheme = (p.scheme or "https").lower()
    host = (p.hostname or "").lower()
    if not host:
        raise ValueError("no host")
    if host.startswith("www."):
        host = host[4:]
    port = p.port
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        host = "%s:%d" % (host, port)
    path = p.path.rstrip("/")
    kept = []
    for part in p.query.split("&"):
        if not part:
            continue
        key = parse.unquote_plus(part.split("=", 1)[0]).lower()
        if key.startswith("utm_") or key in DROP_PARAMS:
            continue
        kept.append(part)
    return "%s://%s%s%s" % (scheme, host, path, ("?" + "&".join(kept)) if kept else "")


def url_host(normalized):
    return parse.urlsplit(normalized).netloc


def host_from_site(site):
    s = site.strip().lower()
    if "://" not in s:
        s = "//" + s
    host = parse.urlsplit(s).hostname or ""
    if host.startswith("www."):
        host = host[4:]
    if not host:
        raise InputError("--site %r is not a domain" % site)
    return host


def classify_path(url):
    """Return guide, commercial or other from the URL path (other also when both marker sets match)."""
    path = parse.urlsplit(url).path.lower() + "/"
    guide = any(m in path for m in GUIDE_MARKERS)
    commercial = any(m in path for m in COMMERCIAL_MARKERS)
    if guide and not commercial:
        return "guide"
    if commercial and not guide:
        return "commercial"
    return "other"


# ---------------------------------------------------------------- CSV reading
def canon_header(text):
    return " ".join(text.replace("\ufeff", "").replace("_", " ").lower().split())


def parse_number(text, what, label, line):
    t = text.strip().replace(",", "").replace(" ", "")
    if t == "":
        return None
    try:
        v = float(t)
    except ValueError:
        raise InputError("%s file line %d: %s %r is not a number" % (label, line, what, text.strip()))
    if not math.isfinite(v) or v < 0:
        raise InputError("%s file line %d: %s %r is not a usable number" % (label, line, what, text.strip()))
    return int(v) if v == int(v) else v


def read_table(path, aliases, required, label):
    """Return (rows, present fields). Each row is (line number, {field: stripped text})."""
    try:
        with open(path, encoding="utf-8-sig", newline="") as fh:
            text = fh.read()
    except FileNotFoundError:
        raise InputError("%s file not found: %s" % (label, path))
    except UnicodeDecodeError:
        raise InputError("%s file is not UTF-8 text: %s" % (label, path))
    except OSError as e:
        raise InputError("cannot read %s file %s: %s" % (label, path, e.strerror or e))
    if not text.strip():
        raise InputError("%s file is empty: %s" % (label, path))
    first = text.splitlines()[0]
    delimiter = max(",;\t", key=lambda d: first.count(d))
    reader = csv.reader(io.StringIO(text), delimiter=delimiter)
    try:
        header = next(reader)
    except (StopIteration, csv.Error):
        raise InputError("%s file is empty: %s" % (label, path))
    index = {}
    for i, name in enumerate(header):
        c = canon_header(name)
        for field, names in aliases.items():
            if c in names and field not in index:
                index[field] = i
    missing = [f for f in required if f not in index]
    if missing:
        raise InputError("%s file is missing required column(s): %s (found: %s). Accepted names: %s" % (
            label, ", ".join(missing), ", ".join(h.strip() for h in header) or "none",
            "; ".join("%s = %s" % (f, "/".join(aliases[f])) for f in missing)))
    rows = []
    try:
        for row in reader:
            if not any(cell.strip() for cell in row):
                continue
            rec = {f: (row[i].strip() if i < len(row) else "") for f, i in index.items()}
            rows.append((reader.line_num, rec))
    except csv.Error as e:
        raise InputError("%s file is not valid CSV: %s" % (label, e))
    if not rows:
        raise InputError("%s file has a header but no data rows: %s" % (label, path))
    return rows, set(index)


def load_serp(path):
    rows, present = read_table(path, SERP_ALIASES, ("keyword", "url", "position"), "SERP")
    positions = defaultdict(dict)  # keyword -> normalized url -> best position
    volume = {}
    used = ignored = 0
    for line, rec in rows:
        kw = clean_keyword(rec["keyword"])
        if not kw:
            raise InputError("SERP file line %d: keyword is empty" % line)
        if not rec["url"]:
            raise InputError("SERP file line %d: url is empty" % line)
        pos = parse_number(rec["position"], "position", "SERP", line)
        if pos is None:
            raise InputError("SERP file line %d: position is empty" % line)
        vol = parse_number(rec.get("volume", ""), "volume", "SERP", line) if "volume" in present else None
        if pos < 1 or pos > MAX_POSITION:
            ignored += 1
            continue
        try:
            url = normalize_url(rec["url"])
        except ValueError as e:
            raise InputError("SERP file line %d: bad url %r (%s)" % (line, rec["url"], e))
        used += 1
        if vol is not None:
            volume[kw] = max(volume.get(kw, 0), vol)
        current = positions[kw].get(url)
        if current is None or pos < current:
            positions[kw][url] = pos
    if not positions:
        raise InputError("SERP file has no organic rows in positions 1 to %d: %s" % (MAX_POSITION, path))
    return {"positions": dict(positions), "volume": volume, "rows_used": used, "rows_ignored": ignored}


def load_gsc(path, our_host):
    rows, present = read_table(path, GSC_ALIASES, ("query", "page", "clicks", "impressions"), "Search Console")
    parsed = []
    for line, rec in rows:
        q = clean_keyword(rec["query"])
        if not q:
            raise InputError("Search Console file line %d: query is empty" % line)
        if not rec["page"]:
            raise InputError("Search Console file line %d: page is empty" % line)
        clicks = parse_number(rec["clicks"], "clicks", "Search Console", line) or 0
        impressions = parse_number(rec["impressions"], "impressions", "Search Console", line) or 0
        conversions = (parse_number(rec.get("conversions", ""), "conversions", "Search Console", line) or 0
                       if "conversions" in present else 0)
        parsed.append((line, q, rec["page"], clicks, impressions, conversions))
    host, source = our_host, "from --site" if our_host else None
    if host is None:
        counts = Counter()
        for _, _, page, _, _, _ in parsed:
            if not page.startswith("/"):
                try:
                    counts[url_host(normalize_url(page))] += 1
                except ValueError:
                    pass
        if counts:
            host = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
            source = "inferred from Search Console pages"
    data = defaultdict(lambda: defaultdict(lambda: [0, 0, 0]))  # query -> page -> [clicks, impressions, conversions]
    for line, q, page, clicks, impressions, conversions in parsed:
        if page.startswith("/"):
            if host is None:
                raise InputError("Search Console file line %d: page %r is a path and no host is known; pass --site" % (line, page))
            page = "https://" + host + page
        try:
            url = normalize_url(page)
        except ValueError as e:
            raise InputError("Search Console file line %d: bad page %r (%s)" % (line, page, e))
        cell = data[q][url]
        cell[0] += clicks
        cell[1] += impressions
        cell[2] += conversions
    return {"data": data, "rows": len(parsed), "has_conversions": "conversions" in present,
            "host": host, "host_source": source}


# ---------------------------------------------------------------- clustering
def overlap_pairs(positions):
    by_url = defaultdict(list)
    for kw, urls in positions.items():
        for u in urls:
            by_url[u].append(kw)
    pairs = Counter()
    for kws in by_url.values():
        kws.sort()
        for i in range(len(kws)):
            for j in range(i + 1, len(kws)):
                pairs[(kws[i], kws[j])] += 1
    return pairs


def components(keywords, pairs, threshold):
    parent = {k: k for k in keywords}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for (a, b), n in pairs.items():
        if n >= threshold:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[max(ra, rb)] = min(ra, rb)
    groups = defaultdict(list)
    for k in keywords:
        groups[find(k)].append(k)
    return list(groups.values())


def pick_stats(stats):
    """Sort key for the keep URL: conversions, clicks, impressions, best SERP position, then URL."""
    pos = stats["best_serp_position"]
    return (-stats["conversions"], -stats["clicks"], -stats["impressions"], MAX_POSITION + 1 if pos is None else pos, stats["url"])


def keep_reason(ordered):
    if len(ordered) < 2:
        return ""
    a, b = ordered[0], ordered[1]
    if a["conversions"] != b["conversions"]:
        return "most conversions"
    if a["clicks"] != b["clicks"]:
        return "most clicks"
    if a["impressions"] != b["impressions"]:
        return "most impressions"
    if a["best_serp_position"] != b["best_serp_position"]:
        return "best SERP position"
    return "alphabetical tie break, no metric separates the pages"


def analyze_cluster(members, serp, our_host, query_impressions):
    volume, positions = serp["volume"], serp["positions"]

    def order(kw):
        return (-(volume.get(kw) or 0), -query_impressions.get(kw, 0), kw)

    members = sorted(members, key=order)
    counts = {"guide": 0, "commercial": 0, "other": 0}
    for kw in members:
        top = sorted(positions[kw].items(), key=lambda kv: (kv[1], kv[0]))[:TOP_URLS_FOR_INTENT]
        for url, _ in top:
            counts[classify_path(url)] += 1
    total = sum(counts.values())
    mixed = (total > 0 and counts["guide"] * 100 >= MIXED_SHARE_PERCENT * total
             and counts["commercial"] * 100 >= MIXED_SHARE_PERCENT * total)
    best = {}  # url -> (position, keyword) across the cluster
    for kw in members:
        for url, pos in positions[kw].items():
            if url not in best or (pos, kw) < best[url]:
                best[url] = (pos, kw)
    ours = []
    if our_host:
        ours = sorted(({"url": u, "best_position": p, "keyword": k} for u, (p, k) in best.items() if url_host(u) == our_host),
                      key=lambda d: (d["best_position"], d["url"]))
    return {
        "head": members[0],
        "keywords": [{"keyword": kw, "volume": volume.get(kw), "serp_urls": len(positions[kw])} for kw in members],
        "mixed_intent": mixed,
        "intent_counts": counts,
        "our_ranking_urls": ours,
        "_best": best,
        "_members": members,
    }


def consolidation(cluster, gsc):
    """Proposal for one cluster from Search Console data."""
    queries = set(cluster["_members"])
    pages = {}
    for q in queries:
        for page, (clicks, impressions, conversions) in gsc["data"].get(q, {}).items():
            if impressions <= 0:
                continue
            st = pages.setdefault(page, {"url": page, "clicks": 0, "impressions": 0, "conversions": 0, "queries": {}})
            st["clicks"] += clicks
            st["impressions"] += impressions
            st["conversions"] += conversions
            st["queries"][q] = st["queries"].get(q, 0) + clicks
    for st in pages.values():
        pos = [cluster["_best"][st["url"]][0]] if st["url"] in cluster["_best"] else []
        st["best_serp_position"] = min(pos) if pos else None
    ordered = sorted(pages.values(), key=pick_stats)
    out_pages = [{"url": s["url"], "clicks": s["clicks"], "impressions": s["impressions"],
                  "conversions": s["conversions"] if gsc["has_conversions"] else None,
                  "best_serp_position": s["best_serp_position"]} for s in ordered]
    res = {"pages": out_pages, "keep_url": None, "keep_reason": "", "candidates": []}
    if not ordered:
        res["status"] = "no_pages"
    elif len(ordered) == 1:
        res["status"] = "single_page"
    elif cluster["mixed_intent"]:
        res["status"] = "review_mixed_intent"
    else:
        res["status"] = "merge_candidates"
        keep = ordered[0]
        res["keep_url"] = keep["url"]
        res["keep_reason"] = keep_reason(ordered)
        for cand in ordered[1:]:
            warns = []
            for q in sorted(cand["queries"]):
                theirs, mine = cand["queries"][q], keep["queries"].get(q, 0)
                if theirs > mine:
                    warns.append("WARN candidate has more clicks than the keep URL for the query \"%s\" (%s vs %s): "
                                 "it may play a different role, review before merging" % (q, theirs, mine))
            res["candidates"].append({
                "url": cand["url"],
                "action": "candidate to merge into %s, then 301 after site-engineer release QA" % keep["url"],
                "warnings": warns,
            })
    return res


def analyze(serp_path, gsc_path=None, site=None, thresholds=(3, 4, 5), primary=4):
    serp = load_serp(serp_path)
    our_host = host_from_site(site) if site else None
    gsc = load_gsc(gsc_path, our_host) if gsc_path else None
    host_source = "from --site" if our_host else None
    if gsc and not our_host:
        our_host, host_source = gsc["host"], gsc["host_source"]
    thresholds = sorted(set(thresholds) | {primary})
    positions = serp["positions"]
    keywords = sorted(positions)
    pairs = overlap_pairs(positions)

    warnings = []
    for kw in keywords:
        if len(positions[kw]) < THIN_SERP_URLS:
            warnings.append("WARN thin SERP: \"%s\" has %d URL(s) in positions 1 to %d (fewer than %d); its overlap with other keywords "
                            "is capped at %d, check the SERP export"
                            % (kw, len(positions[kw]), MAX_POSITION, THIN_SERP_URLS, len(positions[kw])))
    if our_host is None:
        warnings.append("WARN our host unknown: pass --site (or --gsc) to recognise your own URLs in the SERP file")
    elif not any(url_host(u) == our_host for urls in positions.values() for u in urls):
        warnings.append("WARN no URL in the SERP file is on %s: check --site" % our_host)

    sensitivity = []
    for t in thresholds:
        comps = components(keywords, pairs, t)
        sensitivity.append({"threshold": t, "clusters": len(comps), "singletons": sum(1 for c in comps if len(c) == 1)})

    query_impr = {}
    if gsc:
        for q, pages in gsc["data"].items():
            query_impr[q] = sum(v[1] for v in pages.values())
    clusters = [analyze_cluster(c, serp, our_host, query_impr) for c in components(keywords, pairs, primary)]
    clusters.sort(key=lambda c: (-len(c["_members"]), c["head"]))
    for i, c in enumerate(clusters, 1):
        c["id"] = i
        if gsc:
            c["consolidation"] = consolidation(c, gsc)
        else:
            c["consolidation"] = {"status": "not_assessed", "pages": [], "keep_url": None, "keep_reason": "", "candidates": []}

    page_clusters = defaultdict(set)
    for c in clusters:
        for p in c["consolidation"]["pages"]:
            page_clusters[p["url"]].add(c["id"])
    merges, reviews = [], []
    for c in clusters:
        cons = c["consolidation"]
        for cand in cons["candidates"]:
            others = sorted(page_clusters[cand["url"]].difference({c["id"]}))
            if others:
                cand["warnings"].append("WARN this page also gets impressions in cluster(s) %s: check them before any 301"
                                        % ", ".join(str(o) for o in others))
            merges.append({"cluster": c["id"], "keep_url": cons["keep_url"], "merge_url": cand["url"],
                           "step": "merge useful content into the keep URL, then 301 the merged URL to it after site-engineer release QA",
                           "warnings": list(cand["warnings"])})
        if cons["status"] == "review_mixed_intent":
            reviews.append({"cluster": c["id"], "reason": "review: mixed intent",
                            "pages": [p["url"] for p in cons["pages"]]})

    gsc_summary = None
    if gsc:
        gsc_summary = {"rows": gsc["rows"], "has_conversions": gsc["has_conversions"],
                       "queries_outside_serp_file": sum(1 for q in gsc["data"] if q not in positions)}
    for c in clusters:
        del c["_best"], c["_members"]
    return {
        "tool": "serp_clusters.py",
        "version": VERSION,
        "inputs": {
            "keywords": len(keywords),
            "serp_rows_used": serp["rows_used"],
            "serp_rows_ignored_outside_top10": serp["rows_ignored"],
            "thresholds": thresholds,
            "primary_threshold": primary,
            "our_host": our_host,
            "our_host_source": host_source,
            "gsc": gsc_summary,
        },
        "warnings": warnings,
        "sensitivity": sensitivity,
        "clusters": clusters,
        "note": None if gsc else NO_GSC_LINE,
        "draft_change_request": {
            "applied": False,
            "approval": APPROVAL_LINE,
            "merges": merges,
            "reviews": reviews,
        },
        "cannot_cover": CANNOT_COVER,
    }


# ---------------------------------------------------------------- output
def render_text(res):
    inp = res["inputs"]
    lines = ["serp_clusters.py %s: keyword clusters from SERP overlap" % res["version"]]
    host = ("%s (%s)" % (inp["our_host"], inp["our_host_source"])) if inp["our_host"] else "not identified"
    lines.append("Keywords: %d. SERP rows used: %d, ignored outside positions 1 to %d: %d. Our host: %s."
                 % (inp["keywords"], inp["serp_rows_used"], MAX_POSITION, inp["serp_rows_ignored_outside_top10"], host))
    if inp["gsc"]:
        g = inp["gsc"]
        lines.append("Search Console: %d rows, conversions column %s, %d queries not in the SERP file (ignored)."
                     % (g["rows"], "present" if g["has_conversions"] else "absent", g["queries_outside_serp_file"]))
    else:
        lines.append("Search Console: not provided.")
    lines.append("")
    for w in res["warnings"]:
        lines.append(w)
    if res["warnings"]:
        lines.append("")
    lines.append("Sensitivity (two keywords link when their top 10 share at least T URLs)")
    lines.append("%-12s %-9s %s" % ("threshold", "clusters", "singletons"))
    for s in res["sensitivity"]:
        label = "%d%s" % (s["threshold"], " (primary)" if s["threshold"] == inp["primary_threshold"] else "")
        lines.append("%-12s %-9d %d" % (label, s["clusters"], s["singletons"]))
    lines.append("")
    lines.append("Clusters at threshold %d (primary)" % inp["primary_threshold"])
    if res["note"]:
        lines.append(res["note"])
    for c in res["clusters"]:
        cons = c["consolidation"]
        lines.append("")
        lines.append("Cluster %d: head \"%s\", %d keyword(s)" % (c["id"], c["head"], len(c["keywords"])))
        lines.append("  Keywords: " + ", ".join(
            "%s (%s)" % (k["keyword"], k["volume"] if k["volume"] is not None else "no volume") for k in c["keywords"]))
        ic = c["intent_counts"]
        counts = "guide %d, commercial %d, other %d" % (ic["guide"], ic["commercial"], ic["other"])
        if c["mixed_intent"]:
            lines.append("  Intent: MIXED INTENT: likely needs two pages, do not merge (top 3 URLs of each keyword: %s)" % counts)
        else:
            lines.append("  Intent: not mixed (top 3 URLs of each keyword: %s)" % counts)
        if c["our_ranking_urls"]:
            lines.append("  Our ranking URLs in the SERP file:")
            for u in c["our_ranking_urls"]:
                lines.append("    %s (best position %s, \"%s\")" % (u["url"], u["best_position"], u["keyword"]))
        else:
            lines.append("  Our ranking URLs in the SERP file: none")
        if cons["pages"]:
            lines.append("  Our pages with impressions in Search Console:")
            for p in cons["pages"]:
                conv = ", conversions %s" % p["conversions"] if p["conversions"] is not None else ""
                pos = ("best SERP position %s" % p["best_serp_position"]
                       if p["best_serp_position"] is not None else "not in the SERP file")
                lines.append("    %s (clicks %s, impressions %s%s, %s)"
                             % (p["url"], p["clicks"], p["impressions"], conv, pos))
        status = cons["status"]
        if status == "not_assessed":
            lines.append("  Proposal: not assessed, no Search Console data")
        elif status == "no_pages":
            lines.append("  Proposal: none, no page of ours has impressions for this cluster")
        elif status == "single_page":
            lines.append("  Proposal: none, one page of ours serves this cluster")
        elif status == "review_mixed_intent":
            lines.append("  Proposal: review: mixed intent. Several of our pages get impressions, but guides and commercial "
                         "pages both rank, so no merge is proposed")
        else:
            lines.append("  Proposal: keep %s (%s)" % (cons["keep_url"], cons["keep_reason"]))
            for cand in cons["candidates"]:
                lines.append("    %s: %s" % (cand["url"], cand["action"]))
                for w in cand["warnings"]:
                    lines.append("    " + w)
    lines.append("")
    dcr = res["draft_change_request"]
    lines.append("Draft change request (not applied)")
    lines.append(dcr["approval"])
    if res["note"]:
        lines.append("No merges proposed. Without Search Console data there is nothing to compare.")
    elif dcr["merges"]:
        lines.append("Proposed merges and redirects:")
        for i, m in enumerate(dcr["merges"], 1):
            lines.append("  %d. Cluster %d: merge %s into %s, then 301 %s to %s" % (
                i, m["cluster"], m["merge_url"], m["keep_url"], m["merge_url"], m["keep_url"]))
            for w in m["warnings"]:
                lines.append("     " + w)
    else:
        lines.append("No merges proposed.")
    if dcr["reviews"]:
        lines.append("To review before any merge:")
        for r in dcr["reviews"]:
            lines.append("  Cluster %d: %s. Pages: %s" % (r["cluster"], r["reason"], ", ".join(r["pages"])))
    lines.append("")
    lines.append(res["cannot_cover"])
    return "\n".join(lines) + "\n"


class Parser(argparse.ArgumentParser):
    def error(self, message):
        self.print_usage(sys.stderr)
        sys.stderr.write("%s: error: %s\n%s\n" % (self.prog, message, CANNOT_COVER))
        sys.exit(2)


def parse_thresholds(text):
    out = []
    for part in text.split(","):
        part = part.strip()
        if not part.isdigit() or not 1 <= int(part) <= MAX_POSITION:
            raise InputError("--thresholds must be whole numbers from 1 to %d separated by commas, got %r" % (MAX_POSITION, text))
        out.append(int(part))
    return out


def main(argv=None):
    ap = Parser(description="Cluster keywords by SERP overlap and draft consolidation proposals (stdlib only).")
    ap.add_argument("--serp", required=True, help="SERP CSV: keyword, url, position, optional volume")
    ap.add_argument("--gsc", help="Search Console CSV: query, page, clicks, impressions, optional conversions")
    ap.add_argument("--site", help="Your domain, to recognise your own URLs in the SERP file")
    ap.add_argument("--thresholds", default="3,4,5", help="Overlap thresholds to compare (default 3,4,5)")
    ap.add_argument("--primary", type=int, default=4, help="Threshold for the detailed report (default 4)")
    ap.add_argument("--json", action="store_true", help="Print JSON instead of text")
    ap.add_argument("--out", help="Write the report to this file instead of stdout")
    args = ap.parse_args(argv)
    try:
        thresholds = parse_thresholds(args.thresholds)
        if not 1 <= args.primary <= MAX_POSITION:
            raise InputError("--primary must be from 1 to %d" % MAX_POSITION)
        res = analyze(args.serp, args.gsc, args.site, thresholds, args.primary)
        body = json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False) + "\n" if args.json else render_text(res)
        if args.out:
            try:
                with open(args.out, "w", encoding="utf-8") as fh:
                    fh.write(body)
            except OSError as e:
                raise InputError("cannot write %s: %s" % (args.out, e.strerror or e))
    except InputError as e:
        sys.stderr.write("serp_clusters.py: %s\n%s\n" % (e, CANNOT_COVER))
        return 2
    if args.out:
        sys.stdout.write("Wrote report to %s\n" % args.out)
        sys.stdout.write(CANNOT_COVER + "\n")
    elif args.json:
        sys.stdout.write(body)
        sys.stderr.write(CANNOT_COVER + "\n")
    else:
        sys.stdout.write(body)
    return 0


if __name__ == "__main__":
    sys.exit(main())
