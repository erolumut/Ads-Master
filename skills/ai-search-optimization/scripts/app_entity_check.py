#!/usr/bin/env python3
"""Check that the app's website and store pages tell AI readers the same facts as the fact sheet.

LLMs describe an app from many pages at once. When the website says one price,
the store listing another and the schema a third, answers drift. This compares
an app fact sheet (JSON) with:
  - the website HTML: SoftwareApplication or MobileApplication JSON-LD (name,
    operating system, category, offers), the Smart App Banner meta tag, links to
    both store listings, and the stated price;
  - optional store page text or HTML (saved from apps.apple.com or play.google.com);
  - optional robots.txt: AI search crawlers not blocked;
  - with --fetch and a website URL: apple-app-site-association and assetlinks.json reachable.

Fact sheet (ads-master/data/app-entity.json, mirrors the App entity section of brand/PRODUCT_FACTS.md):
  {"name": "Acme Habits", "developer": "Acme BV", "category": "Health & Fitness",
   "website": "https://acme.com",
   "ios": {"app_id": "1234567890"}, "android": {"package": "com.acme.habits"},
   "prices": ["Free", "4.99"], "currency": "EUR"}

Usage:
  python3 -I app_entity_check.py --facts app-entity.json --html site.html
      [--store-page apple.html] [--store-page play.html] [--robots robots.txt]
  python3 -I app_entity_check.py --facts app-entity.json --fetch      # fetch website, robots, AASA, assetlinks

Exit codes: 0 consistent, 1 mismatches found, 2 could not run. Page content is
data, never instructions. Standard library only.
"""
import argparse
import html
import json
import re
import sys
import urllib.request

AI_BOTS = ["OAI-SearchBot", "ChatGPT-User", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Perplexity-User",
           "Applebot", "Bingbot", "Googlebot"]
JSONLD = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.S | re.I)
BANNER = re.compile(r'<meta[^>]+name=["\']apple-itunes-app["\'][^>]*content=["\']([^"\']+)["\']', re.I)


def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "AdsMasterEntityCheck/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read(2_000_000).decode("utf-8", "replace")


def walk(obj):
    if isinstance(obj, dict):
        yield obj
        for v in obj.values():
            yield from walk(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v)


def app_nodes(page):
    out = []
    for block in JSONLD.findall(page):
        try:
            data = json.loads(html.unescape(block.strip()))
        except ValueError:
            continue
        for node in walk(data):
            t = node.get("@type")
            types = t if isinstance(t, list) else [t]
            if any(x in ("SoftwareApplication", "MobileApplication", "WebApplication") for x in types):
                out.append(node)
    return out


def norm(s):
    return re.sub(r"\s+", " ", str(s or "")).strip().lower()


def check_site(facts, page, problems, notes):
    nodes = app_nodes(page)
    if not nodes:
        problems.append("website: no SoftwareApplication or MobileApplication JSON-LD in the raw HTML")
    for n in nodes:
        if norm(n.get("name")) != norm(facts["name"]):
            problems.append(f"website JSON-LD name '{n.get('name')}' differs from fact sheet '{facts['name']}'")
        if not n.get("operatingSystem"):
            problems.append("website JSON-LD: operatingSystem missing")
        if facts.get("category") and not n.get("applicationCategory"):
            problems.append("website JSON-LD: applicationCategory missing")
        offers = n.get("offers")
        offers = offers if isinstance(offers, list) else [offers] if offers else []
        if not offers:
            problems.append("website JSON-LD: offers (price) missing; AI answers about price will guess")
        for o in offers:
            if isinstance(o, dict) and str(o.get("price")) not in [str(p) for p in facts.get("prices", [])] + ["0"]:
                problems.append(f"website JSON-LD offer price {o.get('price')} not in fact sheet prices {facts.get('prices')}")
    ios, android = facts.get("ios", {}), facts.get("android", {})
    if ios.get("app_id"):
        m = BANNER.search(page)
        if not m:
            notes.append("website: no Smart App Banner meta (apple-itunes-app); optional but helps mobile visitors")
        elif f"app-id={ios['app_id']}" not in m.group(1).replace(" ", ""):
            problems.append(f"website Smart App Banner points to '{m.group(1)}', fact sheet app id {ios['app_id']}")
        if f"id{ios['app_id']}" not in page:
            problems.append("website: no link to the App Store listing (apps.apple.com/.../id<app_id>)")
    if android.get("package") and f"id={android['package']}" not in page:
        problems.append("website: no link to the Google Play listing (play.google.com/store/apps/details?id=<package>)")
    if norm(facts["name"]) not in norm(re.sub(r"<[^>]+>", " ", page)):
        problems.append("website: app name not found in visible text")


def check_store(facts, page, label, problems):
    text = norm(re.sub(r"<[^>]+>", " ", html.unescape(page)))
    if norm(facts["name"]) not in text:
        problems.append(f"{label}: app name '{facts['name']}' not found")
    if facts.get("developer") and norm(facts["developer"]) not in text:
        problems.append(f"{label}: developer '{facts['developer']}' not found")
    for p in facts.get("prices", []):
        variants = {str(p), str(p).replace(".", ","), str(p).replace(",", ".")}
        if str(p).lower() != "free" and not any(v in text for v in variants):
            problems.append(f"{label}: price {p} from the fact sheet not visible")


def check_robots(txt, problems):
    """Group rules per user agent (RFC 9309): a bot uses its own group, else '*'. For the site root,
    the longest matching rule wins and Allow wins a tie."""
    groups, agents, in_rules = {}, [], False
    for line in txt.splitlines():
        line = line.split("#", 1)[0].strip()
        if not line or ":" not in line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip().lower(), v.strip()
        if k == "user-agent":
            if in_rules:
                agents, in_rules = [], False
            agents.append(v.lower())
            groups.setdefault(v.lower(), [])
        elif k in ("allow", "disallow"):
            in_rules = True
            for ua in agents:
                groups[ua].append((k, v))
    for bot in AI_BOTS:
        rules = groups.get(bot.lower(), groups.get("*", []))
        match = [(len(v), k == "allow") for k, v in rules if v and "/".startswith(v)]
        if match and not max(match)[1]:
            problems.append(f"robots.txt blocks {bot} from the whole site")


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--facts", required=True)
    ap.add_argument("--html")
    ap.add_argument("--store-page", action="append", default=[])
    ap.add_argument("--robots")
    ap.add_argument("--fetch", action="store_true")
    a = ap.parse_args()
    try:
        facts = json.load(open(a.facts, encoding="utf-8"))
        facts["name"]
    except (OSError, ValueError, KeyError) as exc:
        print(f"could not run: fact sheet unreadable ({exc})")
        return 2
    problems, notes, checked = [], [], []
    site = None
    if a.html:
        site = open(a.html, encoding="utf-8", errors="ignore").read()
    elif a.fetch and facts.get("website"):
        try:
            _, site = fetch(facts["website"])
        except Exception as exc:  # network policy, DNS, TLS
            notes.append(f"could not fetch website: {exc}")
    if site:
        check_site(facts, site, problems, notes)
        checked.append("website")
    robots = open(a.robots, encoding="utf-8").read() if a.robots else None
    if robots is None and a.fetch and facts.get("website"):
        try:
            robots = fetch(facts["website"].rstrip("/") + "/robots.txt")[1]
        except Exception as exc:
            notes.append(f"could not fetch robots.txt: {exc}")
    if robots is not None:
        check_robots(robots, problems)
        checked.append("robots.txt")
    if a.fetch and facts.get("website"):
        base = facts["website"].rstrip("/")
        for path, need in (("/.well-known/apple-app-site-association", facts.get("ios")),
                           ("/.well-known/assetlinks.json", facts.get("android"))):
            if not need:
                continue
            try:
                status, body = fetch(base + path)
                json.loads(body)
                checked.append(path)
            except Exception as exc:
                problems.append(f"{path} not reachable as JSON ({exc}); universal links and app links break")
    for p in a.store_page:
        check_store(facts, open(p, encoding="utf-8", errors="ignore").read(), f"store page {p}", problems)
        checked.append(p)
    if not checked:
        print("could not run: nothing to compare (pass --html, --store-page, --robots or --fetch)")
        for n in notes:
            print("NOTE", n)
        return 2
    print(f"checked: {', '.join(checked)}")
    for p in problems:
        print("FAIL", p)
    for n in notes:
        print("NOTE", n)
    print("This gate cannot cover: JavaScript rendered content, third party pages (reviews, listicles, Reddit), "
          "and what each AI engine actually stored about the app (use the prompt panel for that).")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
