#!/usr/bin/env python3
"""seo_preflight.py: no-JavaScript SEO preflight crawler (Python 3 standard library only).

It fetches pages the way non rendering crawlers and most AI bots see them: raw HTML,
no JavaScript executed. It then reports technical SEO issues per page and site wide:
status codes, redirect chains, robots.txt rules per search and AI bot, sitemaps and
orphans, noindex (meta and X-Robots-Tag), canonicals, titles, meta descriptions, H1s,
visible word count and JS-only shells, images, JSON-LD, hreflang, html lang, viewport,
internal links, broken links and a soft 404 probe.

Usage:
  python3 seo_preflight.py https://www.example.com/ --limit 50
  python3 seo_preflight.py http://127.0.0.1:8000/ --limit 30 --delay 0.2 \
      --out preflight.md --json preflight.json --fail-on high

Politeness and safety: same host only, honors robots.txt for its own user agent
(token AdsMasterSEOPreflight, falling back to the * group), 1 request per second by
default (a larger robots.txt Crawl-delay wins), GET requests only, never submits forms,
never executes JavaScript. Run it on sites you own or are authorized to audit.

Exit codes: 0 done, 1 fatal error, 2 issues at or above --fail-on severity.
"""
import argparse
import gzip
import json
import random
import re
import string
import sys
import time
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib import error, parse, request

VERSION = "1.0"
UA_TOKEN = "AdsMasterSEOPreflight"
DEFAULT_UA = "Mozilla/5.0 (compatible; %s/%s; no-JS SEO preflight run for the site owner)" % (UA_TOKEN, VERSION)
MAX_HTML_BYTES = 5 * 1024 * 1024
GOOGLE_HTML_LIMIT = 2 * 1024 * 1024  # Googlebot for Search fetches the first 2 MB of HTML (documented 2026-02)
MAX_SITEMAP_BYTES = 20 * 1024 * 1024
MAX_CHILD_SITEMAPS = 20
SEVERITIES = ["Critical", "High", "Medium", "Low", "Info"]
SEV_RANK = {s: i for i, s in enumerate(SEVERITIES)}

# Bot token -> (severity if blocked from the start URL, what blocking means)
BOTS = [
    ("Googlebot", "Critical", "Google Search crawling and indexing"),
    ("Bingbot", "High", "Bing, Copilot and engines that use the Bing index"),
    ("OAI-SearchBot", "Medium", "ChatGPT search results and citations (policy decision, see ai-search-optimization)"),
    ("Claude-SearchBot", "Medium", "Claude search results and citations (policy decision)"),
    ("PerplexityBot", "Medium", "Perplexity index and citations (policy decision)"),
    ("ChatGPT-User", "Low", "User initiated fetches in ChatGPT; OpenAI says robots.txt may not apply"),
    ("GPTBot", "Info", "OpenAI model training; blocking is a policy choice"),
    ("ClaudeBot", "Info", "Anthropic model training; blocking is a policy choice"),
    ("Google-Extended", "Info", "Robots token only: Gemini training and grounding; no effect on Google Search"),
]

MOUNT_IDS = {"root", "app", "__next", "__nuxt", "___gatsby", "svelte", "q-app", "react-root", "main-app", "application"}
SKIP_EXT = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".avif", ".svg", ".ico", ".bmp", ".tif", ".tiff",
            ".pdf", ".zip", ".gz", ".css", ".js", ".mjs", ".map", ".mp4", ".webm", ".mov", ".mp3", ".wav",
            ".woff", ".woff2", ".ttf", ".otf", ".eot", ".xml", ".txt", ".json", ".csv", ".xlsx", ".docx")
LEGACY_IMG = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tif", ".tiff")
HREFLANG_RX = re.compile(r"^([a-z]{2,3})(-[a-z]{4})?(-([a-z]{2}|\d{3}))?$", re.I)

# Issue code -> (default severity, title, fix)
CHECKS = {
    "robots_unreachable": ("Critical", "robots.txt returned 5xx or failed", "Serve robots.txt with 200 (or 404 if none). Google pauses crawling while robots.txt errors."),
    "robots_missing": ("Info", "No robots.txt (404)", "Optional. Add one with a Sitemap line."),
    "bot_blocked": ("Info", "Bot disallowed by robots.txt", "Confirm the block is a deliberate policy. Unblock Googlebot and Bingbot on indexable pages."),
    "resources_blocked": ("High", "JS or CSS blocked for Googlebot", "Allow rendering resources in robots.txt."),
    "sitemap_missing": ("Medium", "No XML sitemap found", "Publish /sitemap.xml with canonical, indexable 200 URLs and declare it in robots.txt."),
    "sitemap_error": ("Medium", "Sitemap could not be parsed", "Return valid XML with 200 and the sitemaps.org namespace."),
    "sitemap_bad_url": ("Medium", "Sitemap lists a non-indexable URL", "List only 200, indexable, self canonical URLs."),
    "sitemap_orphan": ("Medium", "Sitemap URL with no internal links (orphan)", "Link it from relevant hubs or drop it from the sitemap."),
    "not_in_sitemap": ("Low", "Indexable page missing from sitemap", "Add canonical indexable pages to the sitemap (framework route or plugin)."),
    "soft404_risk": ("High", "Unknown URLs return 200 (soft 404 risk)", "Return a real 404 status for unknown routes (server or framework not-found handler)."),
    "fetch_error": ("High", "Request failed (network or timeout)", "Check server availability and firewall or bot rules."),
    "http_error": ("High", "Page returns 4xx or 5xx", "Fix the page, redirect it to the closest equivalent, or remove links to it."),
    "broken_link": ("High", "Internal link to a 4xx or 5xx URL", "Update or remove the link; redirect retired URLs."),
    "redirect_chain": ("Medium", "Redirect chain over 1 hop", "Redirect in one hop to the final URL."),
    "redirect_loop": ("High", "Redirect loop or too many hops", "Fix the redirect rules."),
    "link_to_redirect": ("Low", "Internal link points to a redirect", "Link directly to the final URL."),
    "redirect_offhost": ("Info", "Redirects to another host", "Confirm it is intended (www, locale or domain move)."),
    "noindex": ("Medium", "Page is noindex", "Remove noindex if the page should rank; keep it only for deliberate exclusions."),
    "noindex_in_sitemap": ("High", "noindex page listed in sitemap", "Remove noindex or remove the URL from the sitemap."),
    "canonical_missing": ("Medium", "No canonical tag", "Add an absolute self referencing canonical in the raw HTML."),
    "canonical_multiple": ("High", "Multiple canonical tags", "Keep exactly one canonical per page."),
    "canonical_relative": ("Low", "Canonical is relative", "Use an absolute URL."),
    "canonical_other": ("Low", "Canonical points to another URL", "Confirm the page is a true duplicate; otherwise self canonicalize."),
    "canonical_offhost": ("Medium", "Canonical points to another host", "Confirm cross domain canonical is intended."),
    "canonical_target_bad": ("High", "Canonical target is not 200 and indexable", "Point canonicals at live, indexable, self canonical URLs."),
    "title_missing": ("High", "Missing or empty title", "Write a unique, descriptive title per route in the raw HTML."),
    "title_multiple": ("Medium", "Multiple title elements", "Keep one title element in head."),
    "title_duplicate": ("Medium", "Duplicate title across pages", "Give each indexable page a unique title (per route metadata)."),
    "title_long": ("Low", "Title over 60 characters", "Front load the topic; expect truncation."),
    "title_short": ("Low", "Title under 10 characters", "Describe the page topic and intent."),
    "desc_missing": ("Low", "Missing meta description", "Write a unique description per page (snippet control, not a ranking factor)."),
    "desc_duplicate": ("Low", "Duplicate meta description across pages", "Write unique descriptions or omit them."),
    "desc_long": ("Low", "Meta description over 160 characters", "Shorten; key message first."),
    "desc_short": ("Low", "Meta description under 50 characters", "Summarize the page value."),
    "h1_missing": ("Low", "No H1 in raw HTML", "Add one visible main heading (clarity and accessibility; not a Google rule)."),
    "h1_multiple": ("Low", "More than one H1", "Fine for Google; keep one main heading for clarity unless the design needs more."),
    "js_shell": ("Critical", "JS-only shell: almost no text in raw HTML", "Server render, statically generate or prerender this route."),
    "thin_content": ("Medium", "Thin raw HTML text", "Add substantive content or noindex if the page has no search value."),
    "html_too_large": ("High", "HTML over 2 MB", "Googlebot fetches the first 2 MB; trim inline JSON and markup."),
    "img_no_alt": ("Medium", "Images without alt attribute", "Add descriptive alt text (empty alt only for decorative images)."),
    "img_legacy_format": ("Low", "Images in JPEG, PNG or GIF", "Serve AVIF or WebP with fallbacks via an image CDN or picture element."),
    "img_no_dimensions": ("Low", "Images without width and height", "Set width and height or aspect-ratio to prevent layout shift (CLS)."),
    "jsonld_invalid": ("High", "JSON-LD does not parse", "Fix the JSON syntax; invalid blocks are ignored."),
    "jsonld_retired_type": ("Info", "Markup type without Google rich results", "FAQPage rich results stopped 2026-05-07 and HowTo in 2023; keep only if useful elsewhere."),
    "hreflang_invalid": ("High", "Invalid hreflang code", "Use ISO 639-1 language plus optional ISO 3166-1 region (en-GB, not en-UK)."),
    "hreflang_no_self": ("Medium", "hreflang set without self reference", "Include the page itself in its hreflang set."),
    "hreflang_not_reciprocal": ("High", "hreflang not reciprocal", "Every alternate must link back to this page."),
    "hreflang_target_bad": ("High", "hreflang target not 200 and indexable", "Point hreflang at canonical, indexable 200 URLs."),
    "hreflang_no_xdefault": ("Low", "hreflang set without x-default", "Add x-default for the fallback page."),
    "lang_missing": ("Low", "html lang missing", "Set lang on the html element (also drives correct casing and hyphenation)."),
    "viewport_missing": ("High", "No viewport meta", "Add width=device-width, initial-scale=1."),
    "viewport_blocks_zoom": ("Medium", "Viewport disables zoom", "Remove user-scalable=no and maximum-scale=1; use 16px inputs instead."),
    "no_internal_links": ("High", "No crawlable internal links in raw HTML", "Render navigation as <a href> links in the server HTML."),
    "js_links": ("Medium", "Links without crawlable href", "Use <a href> with real URLs instead of onclick or javascript: links."),
    "hash_routing": ("High", "Hash based routing (#/ URLs)", "Use history API routes with real paths; Google ignores URL fragments."),
    "deep_page": ("Low", "More than 3 clicks from the start URL", "Link important pages from hubs and navigation."),
    "meta_refresh": ("Low", "Meta refresh redirect", "Use a server side 301 or 308 redirect."),
    "insecure_link": ("Low", "Internal link uses http on an https site", "Link to https URLs."),
    "robots_skipped": ("Info", "URL skipped: disallowed for this crawler", "Expected if the section is private."),
    "crawl_limit": ("Info", "Crawl limit reached", "Raise --limit for complete orphan and duplicate analysis."),
    "start_redirected": ("Info", "Start URL redirects to another host or scheme", "Crawled the final origin. Use it in internal links, sitemaps, canonicals and Search Console."),
}


def norm_url(url):
    """Normalize for comparison: lowercase scheme and host, drop default port and fragment."""
    p = parse.urlsplit(url.strip())
    scheme = (p.scheme or "http").lower()
    host = (p.hostname or "").lower()
    port = p.port
    netloc = host
    if port and not ((scheme == "http" and port == 80) or (scheme == "https" and port == 443)):
        netloc = "%s:%d" % (host, port)
    path = p.path or "/"
    return parse.urlunsplit((scheme, netloc, path, p.query, ""))


def same_site(url, origin):
    """Same hostname and same explicit port (default ports 80 and 443 count as none)."""
    a, b = parse.urlsplit(url), parse.urlsplit(origin)
    pa = None if a.port in (None, 80, 443) else a.port
    pb = None if b.port in (None, 80, 443) else b.port
    return (a.hostname or "").lower() == (b.hostname or "").lower() and pa == pb


# ---------------------------------------------------------------- robots.txt (RFC 9309)
class Robots:
    def __init__(self, text=""):
        self.groups = []  # (agents, rules[(allow, pattern, regex)], crawl_delay)
        self.sitemaps = []
        self._parse(text or "")

    @staticmethod
    def _rx(pattern):
        anchored = pattern.endswith("$")
        body = pattern[:-1] if anchored else pattern
        rx = "".join(".*" if c == "*" else re.escape(c) for c in body)
        return re.compile(rx + ("$" if anchored else ""))

    def _parse(self, text):
        agents, rules, delay, last_agent = [], [], None, False
        for raw in text.splitlines():
            line = raw.split("#", 1)[0].strip()
            if ":" not in line:
                continue
            key, val = line.split(":", 1)
            key, val = key.strip().lower(), val.strip()
            if key == "user-agent":
                if agents and not last_agent:
                    self.groups.append((agents, rules, delay))
                    agents, rules, delay = [], [], None
                agents.append(val.lower())
                last_agent = True
            elif key in ("allow", "disallow"):
                last_agent = False
                if agents and val:
                    rules.append((key == "allow", val, self._rx(val)))
            elif key == "crawl-delay":
                last_agent = False
                try:
                    delay = float(val)
                except ValueError:
                    pass
            elif key == "sitemap" and val:
                self.sitemaps.append(val)
        if agents:
            self.groups.append((agents, rules, delay))

    def group_for(self, token):
        t = token.lower()
        matched = [g for g in self.groups if t in g[0]]
        label = token
        if not matched:
            matched = [g for g in self.groups if "*" in g[0]]
            label = "*" if matched else "none"
        rules = [r for g in matched for r in g[1]]
        delay = next((g[2] for g in matched if g[2] is not None), None)
        return label, rules, delay

    def check(self, token, url):
        """Return (allowed, matching_rule, group_label). Longest match wins; allow wins ties."""
        label, rules, _ = self.group_for(token)
        p = parse.urlsplit(url)
        path = (p.path or "/") + ("?" + p.query if p.query else "")
        best = None
        for allow, pat, rx in rules:
            if rx.match(path):
                if best is None or len(pat) > len(best[1]) or (len(pat) == len(best[1]) and allow and not best[0]):
                    best = (allow, pat)
        if best is None:
            return True, None, label
        return best[0], ("Allow: " if best[0] else "Disallow: ") + best[1], label


# ---------------------------------------------------------------- HTTP
class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Response:
    def __init__(self, url, status, headers, body, err=None):
        self.url, self.status, self.headers, self.body, self.error = url, status, headers, body, err

    def header(self, name):
        if not self.headers:
            return None
        return self.headers.get(name)

    def header_all(self, name):
        if not self.headers:
            return []
        return self.headers.get_all(name) or []


class Fetcher:
    def __init__(self, ua, delay, timeout, local):
        handlers = [NoRedirect()]
        if local:
            handlers.append(request.ProxyHandler({}))
        self.opener = request.build_opener(*handlers)
        self.ua, self.delay, self.timeout = ua, delay, timeout
        self.last = 0.0
        self.count = 0

    def get(self, url, max_bytes=MAX_HTML_BYTES):
        wait = self.delay - (time.monotonic() - self.last)
        if wait > 0:
            time.sleep(wait)
        self.count += 1
        req = request.Request(url, headers={
            "User-Agent": self.ua,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        })
        try:
            resp = self.opener.open(req, timeout=self.timeout)
            status = getattr(resp, "status", None) or resp.getcode()
            body = resp.read(max_bytes + 1)
            headers = resp.headers
        except error.HTTPError as e:
            status, headers = e.code, e.headers
            try:
                body = e.read(max_bytes + 1)
            except Exception:
                body = b""
        except (error.URLError, OSError, ValueError) as e:
            self.last = time.monotonic()
            return Response(url, 0, None, b"", str(getattr(e, "reason", e)))
        self.last = time.monotonic()
        return Response(url, status, headers, body)


def decode(body, content_type):
    m = re.search(r"charset=([\w-]+)", content_type or "", re.I)
    enc = m.group(1) if m else None
    if not enc:
        m = re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", body[:4096], re.I)
        enc = m.group(1).decode("ascii", "ignore") if m else "utf-8"
    try:
        return body.decode(enc, errors="replace")
    except LookupError:
        return body.decode("utf-8", errors="replace")


# ---------------------------------------------------------------- HTML parsing
class PageParser(HTMLParser):
    HIDDEN = {"script", "style", "noscript", "template", "svg", "title"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titles, self._title, self.in_title = 0, [], False
        self.metas, self.links, self.anchors, self.imgs = [], [], [], []
        self.h1 = 0
        self.jsonld, self._jsonld, self.in_jsonld = [], [], False
        self.html_lang = None
        self.hidden = 0
        self.text = []
        self.scripts, self.script_srcs, self.stylesheets = 0, [], []
        self.mounts = set()
        self.base = None
        self.js_links = 0
        self.in_svg = 0

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v or "") for k, v in attrs}
        if tag in self.HIDDEN:
            self.hidden += 1
        if tag == "svg":
            self.in_svg += 1
        if tag == "html" and "lang" in a:
            self.html_lang = a["lang"].strip()
        elif tag == "title":
            if not self.in_svg:  # inline SVG icons carry their own <title>
                self.titles += 1
                self.in_title = True
        elif tag == "meta":
            self.metas.append(a)
        elif tag == "base" and a.get("href"):
            self.base = a["href"]
        elif tag == "link":
            self.links.append(a)
            if "stylesheet" in a.get("rel", "").lower().split() and a.get("href"):
                self.stylesheets.append(a["href"])
        elif tag == "a":
            href = a.get("href")
            if href is None or href.strip().lower().startswith("javascript:"):
                if href is not None or "onclick" in a:
                    self.js_links += 1
            else:
                self.anchors.append((href.strip(), a.get("rel", "").lower()))
        elif tag == "h1":
            self.h1 += 1
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "script":
            self.scripts += 1
            if a.get("src"):
                self.script_srcs.append(a["src"])
            if a.get("type", "").lower().strip() == "application/ld+json":
                self.in_jsonld, self._jsonld = True, []
        elif tag == "div" and a.get("id", "").lower() in MOUNT_IDS:
            self.mounts.add(a["id"])

    def handle_endtag(self, tag):
        if tag in self.HIDDEN and self.hidden > 0:
            self.hidden -= 1
        if tag == "svg" and self.in_svg > 0:
            self.in_svg -= 1
        if tag == "title":
            self.in_title = False
        elif tag == "script" and self.in_jsonld:
            self.jsonld.append("".join(self._jsonld))
            self.in_jsonld = False

    def handle_data(self, data):
        if self.in_title:
            self._title.append(data)
        if self.in_jsonld:
            self._jsonld.append(data)
        elif self.hidden == 0:
            self.text.append(data)

    @property
    def title(self):
        return re.sub(r"\s+", " ", "".join(self._title)).strip()


def jsonld_types(obj, out):
    if isinstance(obj, list):
        for o in obj:
            jsonld_types(o, out)
    elif isinstance(obj, dict):
        t = obj.get("@type")
        if isinstance(t, list):
            out.extend(str(x) for x in t)
        elif t:
            out.append(str(t))
        for k in ("@graph", "mainEntity", "itemListElement"):
            if k in obj:
                jsonld_types(obj[k], out)


# ---------------------------------------------------------------- crawler
class Preflight:
    def __init__(self, args):
        self.args = args
        self.start = norm_url(args.url)
        sp = parse.urlsplit(self.start)
        self.origin = "%s://%s" % (sp.scheme, sp.netloc)
        local = (sp.hostname or "") in ("localhost", "127.0.0.1", "::1") or (sp.hostname or "").endswith(".localhost")
        self.fetcher = Fetcher(args.user_agent, args.delay, args.timeout, local)
        self.robots = Robots("")
        self.robots_status = None
        self.pages = {}       # requested normalized URL -> record
        self.by_final = {}    # final URL -> record
        self.inlinks = {}     # target URL -> set(source URLs)
        self.skipped = []     # (url, rule)
        self.issues = []
        self.sitemap_urls = {}  # url -> lastmod
        self.sitemap_files = []
        self.sitemap_errors = []
        self.soft404 = None
        self.limit_hit = False
        self.aborted = None

    def issue(self, code, url, detail="", severity=None):
        sev = severity or CHECKS[code][0]
        self.issues.append({"code": code, "severity": sev, "url": url, "detail": detail})

    def log(self, msg):
        if not self.args.quiet:
            print(msg, file=sys.stderr)

    def own_allowed(self, url):
        ok, rule, _ = self.robots.check(UA_TOKEN, url)
        return ok, rule

    # robots and sitemaps
    def load_robots(self):
        r = self.fetcher.get(self.origin + "/robots.txt", max_bytes=512 * 1024)
        self.robots_status = r.status
        if r.status == 200:
            self.robots = Robots(decode(r.body, r.header("Content-Type")))
        elif r.status == 0 or r.status >= 500:
            self.issue("robots_unreachable", self.origin + "/robots.txt", "status %s %s" % (r.status, r.error or ""))
            return False
        else:
            self.issue("robots_missing", self.origin + "/robots.txt", "status %s" % r.status)
        _, _, delay = self.robots.group_for(UA_TOKEN)
        if delay and delay > self.fetcher.delay:
            self.fetcher.delay = min(delay, 30.0)
        return True

    def load_sitemaps(self):
        candidates = [s for s in self.robots.sitemaps]
        if not candidates:
            candidates = [self.origin + "/sitemap.xml", self.origin + "/sitemap_index.xml"]
        seen, queue = set(), list(candidates)
        while queue and len(seen) < MAX_CHILD_SITEMAPS + 2:
            sm = queue.pop(0)
            if sm in seen:
                continue
            seen.add(sm)
            if not same_site(sm, self.origin):
                self.sitemap_errors.append("%s: other host, not fetched" % sm)
                continue
            ok, rule = self.own_allowed(sm)
            if not ok:
                self.sitemap_errors.append("%s: disallowed for this crawler (%s)" % (sm, rule))
                continue
            r = self.fetcher.get(sm, max_bytes=MAX_SITEMAP_BYTES)
            if r.status != 200:
                if sm in self.robots.sitemaps:
                    self.sitemap_errors.append("%s: status %s" % (sm, r.status))
                continue
            data = r.body
            if data[:2] == b"\x1f\x8b":
                try:
                    data = gzip.decompress(data)
                except OSError:
                    self.sitemap_errors.append("%s: bad gzip" % sm)
                    continue
            if b"<!DOCTYPE" in data[:2048] or b"<!ENTITY" in data:
                self.sitemap_errors.append("%s: DOCTYPE or ENTITY not allowed in sitemaps, skipped" % sm)
                continue
            try:
                root = ET.fromstring(data)
            except ET.ParseError as e:
                self.sitemap_errors.append("%s: XML parse error %s" % (sm, e))
                continue
            self.sitemap_files.append(sm)
            tag = root.tag.rsplit("}", 1)[-1]
            for child in root:
                loc = lastmod = None
                for el in child:
                    name = el.tag.rsplit("}", 1)[-1]
                    if name == "loc" and el.text:
                        loc = el.text.strip()
                    elif name == "lastmod" and el.text:
                        lastmod = el.text.strip()
                if not loc:
                    continue
                if tag == "sitemapindex":
                    queue.append(loc)
                else:
                    self.sitemap_urls[norm_url(loc)] = lastmod
        if not self.sitemap_files:
            self.issue("sitemap_missing", self.origin + "/sitemap.xml", "; ".join(self.sitemap_errors))
        elif self.sitemap_errors:
            for e in self.sitemap_errors:
                self.issue("sitemap_error", self.origin, e)

    # fetching with redirect chain
    def fetch_follow(self, url):
        chain, current, seen = [], url, set()
        while True:
            r = self.fetcher.get(current)
            chain.append((current, r.status))
            if r.status in (301, 302, 303, 307, 308) and r.header("Location"):
                nxt = norm_url(parse.urljoin(current, r.header("Location")))
                seen.add(current)
                if nxt in seen or len(chain) > 10:
                    return r, chain, "loop"
                if not same_site(nxt, self.origin):
                    chain.append((nxt, None))
                    return r, chain, "offhost"
                ok, _ = self.own_allowed(nxt)
                if not ok:
                    chain.append((nxt, None))
                    return r, chain, "blocked"
                current = nxt
                continue
            return r, chain, None

    def crawl(self):
        queue = [(self.start, 0, "link")]
        queued = {self.start}
        sitemap_seeded = False
        while True:
            if not queue:
                if self.args.no_sitemap_crawl or sitemap_seeded:
                    break
                sitemap_seeded = True
                for u in sorted(self.sitemap_urls):
                    if u not in queued and same_site(u, self.origin):
                        queued.add(u)
                        queue.append((u, None, "sitemap"))
                if not queue:
                    break
            if len(self.pages) >= self.args.limit:
                self.limit_hit = True
                break
            url, depth, source = queue.pop(0)
            ok, rule = self.own_allowed(url)
            if not ok:
                self.skipped.append((url, rule))
                continue
            rec = self.fetch_page(url, depth, source)
            self.log("[%d/%d] %s %s" % (len(self.pages), self.args.limit, rec["status"], url))
            if rec.get("parsed"):
                for link in rec["internal_links"]:
                    if link not in queued:
                        queued.add(link)
                        nd = None if depth is None else depth + 1
                        if not link.lower().split("?")[0].endswith(SKIP_EXT):
                            queue.append((link, nd, "link"))

    def fetch_page(self, url, depth, source):
        r, chain, redirect_issue = self.fetch_follow(url)
        final = chain[-1][0]
        rec = {"url": url, "final_url": final, "status": r.status, "chain": chain, "depth": depth,
               "found_via": source, "error": r.error, "redirect_issue": redirect_issue, "parsed": False}
        self.pages[url] = rec
        hops = len([c for c in chain if c[1] in (301, 302, 303, 307, 308)])
        rec["hops"] = hops
        if redirect_issue == "loop":
            self.issue("redirect_loop", url, " > ".join(c[0] for c in chain))
            return rec
        if redirect_issue == "offhost":
            self.issue("redirect_offhost", url, "to %s" % chain[-1][0])
            return rec
        if redirect_issue == "blocked":
            self.skipped.append((chain[-1][0], "redirect target disallowed"))
            return rec
        if hops > 1:
            self.issue("redirect_chain", url, " > ".join("%s (%s)" % (c[0], c[1]) for c in chain))
        if r.status == 0:
            self.issue("fetch_error", url, r.error or "")
            return rec
        if r.status >= 400:
            sev = "Critical" if url == self.start else None
            self.issue("http_error", url, "status %s" % r.status, sev)
            return rec
        if final in self.by_final and self.by_final[final] is not rec:
            rec["duplicate_of"] = final
            return rec
        self.by_final[final] = rec
        ctype = (r.header("Content-Type") or "").lower()
        rec["content_type"] = ctype
        xrt = ", ".join(r.header_all("X-Robots-Tag"))
        rec["x_robots_tag"] = xrt
        if "html" not in ctype:
            return rec
        self.analyze_html(rec, r, final)
        return rec

    def analyze_html(self, rec, r, final):
        body = r.body[:MAX_HTML_BYTES]
        rec["html_bytes"] = len(r.body)
        if len(r.body) > GOOGLE_HTML_LIMIT:
            self.issue("html_too_large", final, "%d bytes" % len(r.body))
        html = decode(body, rec.get("content_type"))
        p = PageParser()
        try:
            p.feed(html)
            p.close()
        except Exception as e:  # malformed markup should not stop the crawl
            rec["parse_error"] = str(e)
        rec["parsed"] = True
        base = parse.urljoin(final, p.base) if p.base else final

        # robots directives
        directives = []
        for m in p.metas:
            if m.get("name", "").lower() in ("robots", "googlebot"):
                directives.append(m.get("content", "").lower())
        xrt = rec.get("x_robots_tag", "").lower()
        xr_parts = []
        for part in xrt.split(","):
            part = part.strip()
            if ":" in part:
                agent, val = part.split(":", 1)
                if agent.strip() in ("googlebot", "bingbot", "robots", "*"):
                    xr_parts.append(val.strip())
                elif agent.strip() in ("unavailable_after",):
                    xr_parts.append(part)
            elif part:
                xr_parts.append(part)
        meta_noindex = any(("noindex" in d or re.search(r"\bnone\b", d)) for d in directives)
        header_noindex = any(("noindex" in x or x == "none") for x in xr_parts)
        rec["noindex"] = meta_noindex or header_noindex
        rec["noindex_source"] = ", ".join(s for s, f in (("meta", meta_noindex), ("X-Robots-Tag", header_noindex)) if f)
        for m in p.metas:
            if m.get("http-equiv", "").lower() == "refresh":
                self.issue("meta_refresh", final, m.get("content", ""))

        # canonical
        canon = [l.get("href", "").strip() for l in p.links if "canonical" in l.get("rel", "").lower().split()]
        rec["canonical_raw"] = canon
        rec["canonical"] = None
        if not canon:
            rec["canonical_state"] = "missing"
        elif len(canon) > 1:
            rec["canonical_state"] = "multiple"
            self.issue("canonical_multiple", final, " | ".join(canon))
        if canon:
            c = canon[0]
            if not re.match(r"^https?://", c, re.I):
                self.issue("canonical_relative", final, c)
            cabs = norm_url(parse.urljoin(base, c))
            rec["canonical"] = cabs
            if len(canon) == 1:
                if cabs == final:
                    rec["canonical_state"] = "self"
                elif not same_site(cabs, self.origin):
                    rec["canonical_state"] = "offhost"
                    self.issue("canonical_offhost", final, cabs)
                else:
                    rec["canonical_state"] = "other"
                    self.issue("canonical_other", final, cabs)

        # title and description
        rec["title"] = p.title
        rec["title_count"] = p.titles
        rec["title_len"] = len(p.title)
        desc = [m.get("content", "") for m in p.metas if m.get("name", "").lower() == "description"]
        rec["description"] = re.sub(r"\s+", " ", desc[0]).strip() if desc else ""
        rec["desc_len"] = len(rec["description"])
        if not p.title:
            self.issue("title_missing", final)
        else:
            if p.titles > 1:
                self.issue("title_multiple", final, "%d title elements" % p.titles)
            if len(p.title) > 60:
                self.issue("title_long", final, "%d chars" % len(p.title))
            if len(p.title) < 10:
                self.issue("title_short", final, repr(p.title))
        if not rec["description"]:
            self.issue("desc_missing", final)
        elif rec["desc_len"] > 160:
            self.issue("desc_long", final, "%d chars" % rec["desc_len"])
        elif rec["desc_len"] < 50:
            self.issue("desc_short", final, "%d chars" % rec["desc_len"])

        # headings and text
        rec["h1_count"] = p.h1
        if p.h1 == 0:
            self.issue("h1_missing", final)
        elif p.h1 > 1:
            self.issue("h1_multiple", final, "%d H1" % p.h1)
        text = re.sub(r"\s+", " ", " ".join(p.text))
        words = len(re.findall(r"\w+", text, re.UNICODE))
        rec["word_count"] = words
        rec["mount_ids"] = sorted(p.mounts)
        rec["script_count"] = p.scripts
        if words < self.args.thin_words:
            if p.mounts or (p.scripts > 0 and words < 30):
                rec["js_shell"] = True
                sev = "Critical" if not rec["noindex"] else "Low"
                self.issue("js_shell", final, "%d words, mount %s, %d scripts" % (words, ",".join(sorted(p.mounts)) or "none", p.scripts), sev)
            else:
                self.issue("thin_content", final, "%d words" % words)

        # images
        no_alt, legacy, no_dim = [], [], []
        for img in p.imgs:
            src = img.get("src") or img.get("data-src") or ""
            if "alt" not in img:
                no_alt.append(src)
            if src.lower().split("?")[0].endswith(LEGACY_IMG):
                legacy.append(src)
            if not (img.get("width") and img.get("height")) and "aspect-ratio" not in img.get("style", ""):
                no_dim.append(src)
        rec["images"] = len(p.imgs)
        rec["images_no_alt"] = len(no_alt)
        if no_alt:
            self.issue("img_no_alt", final, "%d of %d: %s" % (len(no_alt), len(p.imgs), ", ".join(no_alt[:3])))
        if legacy:
            self.issue("img_legacy_format", final, "%d: %s" % (len(legacy), ", ".join(legacy[:3])))
        if no_dim:
            self.issue("img_no_dimensions", final, "%d: %s" % (len(no_dim), ", ".join(no_dim[:3])))

        # JSON-LD
        types, errors = [], []
        for block in p.jsonld:
            try:
                jsonld_types(json.loads(block), types)
            except ValueError as e:
                errors.append(str(e))
        rec["jsonld_types"] = sorted(set(types))
        rec["jsonld_errors"] = errors
        for e in errors:
            self.issue("jsonld_invalid", final, e)
        retired = [t for t in rec["jsonld_types"] if t in ("FAQPage", "HowTo")]
        if retired:
            self.issue("jsonld_retired_type", final, ", ".join(retired))

        # hreflang, lang, viewport
        rec["hreflang"] = []
        for l in p.links:
            if "alternate" in l.get("rel", "").lower().split() and l.get("hreflang"):
                rec["hreflang"].append((l["hreflang"].strip(), norm_url(parse.urljoin(base, l.get("href", "")))))
        rec["html_lang"] = p.html_lang
        if not p.html_lang:
            self.issue("lang_missing", final)
        vp = [m.get("content", "").lower().replace(" ", "") for m in p.metas if m.get("name", "").lower() == "viewport"]
        rec["viewport"] = vp[0] if vp else None
        if not vp:
            self.issue("viewport_missing", final)
        elif "user-scalable=no" in vp[0] or "user-scalable=0" in vp[0] or re.search(r"maximum-scale=1(\.0)?(,|$)", vp[0]):
            self.issue("viewport_blocks_zoom", final, vp[0])

        # links
        internal, external, hash_routes, insecure = [], 0, 0, 0
        for href, rel in p.anchors:
            if href.startswith("#/") or href.startswith("#!"):
                hash_routes += 1
                continue
            if href.startswith(("mailto:", "tel:", "sms:", "#", "data:")):
                continue
            absu = parse.urljoin(base, href)
            if not absu.lower().startswith(("http://", "https://")):
                continue
            if same_site(absu, self.origin):
                n = norm_url(absu)
                internal.append(n)
                self.inlinks.setdefault(n, set()).add(final)
                if self.origin.startswith("https://") and absu.lower().startswith("http://"):
                    insecure += 1
            else:
                external += 1
        rec["internal_links"] = sorted(set(internal))
        rec["internal_link_count"] = len(internal)
        rec["external_link_count"] = external
        if not internal:
            self.issue("no_internal_links", final)
        if p.js_links:
            self.issue("js_links", final, "%d anchors" % p.js_links)
        if hash_routes:
            self.issue("hash_routing", final, "%d #/ links" % hash_routes)
        if insecure:
            self.issue("insecure_link", final, "%d links" % insecure)
        if rec["depth"] is not None and rec["depth"] > 3:
            self.issue("deep_page", final, "depth %d" % rec["depth"])
        rec["resources"] = [norm_url(parse.urljoin(base, s)) for s in p.script_srcs + p.stylesheets]

    # post crawl checks
    def soft404_probe(self):
        token = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))
        url = self.origin + "/seo-preflight-404-check-" + token
        ok, _ = self.own_allowed(url)
        if not ok:
            return
        r, chain, _ = self.fetch_follow(url)
        self.soft404 = {"url": url, "status": r.status, "chain": chain}
        if r.status == 200:
            self.issue("soft404_risk", url, "final status 200 after %d hop(s)" % (len(chain) - 1))

    def post_checks(self):
        indexable = {}
        for rec in self.by_final.values():
            if rec.get("parsed") and rec["status"] == 200 and not rec.get("noindex") and rec.get("canonical_state") in ("self", "missing"):
                indexable[rec["final_url"]] = rec
        # noindex pages
        for rec in self.by_final.values():
            if rec.get("noindex"):
                u = rec["final_url"]
                if u == self.start or rec["url"] == self.start:
                    self.issue("noindex", u, rec["noindex_source"], "Critical")
                elif u in self.sitemap_urls or rec["url"] in self.sitemap_urls:
                    self.issue("noindex_in_sitemap", u, rec["noindex_source"])
                else:
                    self.issue("noindex", u, rec["noindex_source"])
            if rec.get("parsed") and rec.get("canonical_state") == "missing" and not rec.get("noindex"):
                self.issue("canonical_missing", rec["final_url"])
        # canonical targets
        for rec in self.by_final.values():
            c = rec.get("canonical")
            if c and rec.get("canonical_state") == "other":
                t = self.pages.get(c) or self.by_final.get(c)
                if t and (t["status"] != 200 or t.get("hops") or t.get("noindex")):
                    self.issue("canonical_target_bad", rec["final_url"], "%s status %s hops %s noindex %s" % (c, t["status"], t.get("hops"), t.get("noindex")))
        # duplicates among indexable pages
        for field, code in (("title", "title_duplicate"), ("description", "desc_duplicate")):
            groups = {}
            for u, rec in indexable.items():
                v = rec.get(field, "").strip().lower()
                if v:
                    groups.setdefault(v, []).append(u)
            for v, urls in groups.items():
                if len(urls) > 1:
                    for u in urls:
                        self.issue(code, u, "shared by %d pages: %r" % (len(urls), v[:70]))
        # broken links and links to redirects
        for target, sources in self.inlinks.items():
            rec = self.pages.get(target)
            if not rec:
                continue
            if rec["status"] == 0 or rec["status"] >= 400:
                self.issue("broken_link", target, "status %s, linked from %d page(s): %s" % (rec["status"], len(sources), ", ".join(sorted(sources)[:3])))
            elif rec.get("hops"):
                self.issue("link_to_redirect", target, "linked from %d page(s): %s" % (len(sources), ", ".join(sorted(sources)[:3])))
        # sitemap hygiene and orphans
        crawled_final = set(self.by_final)
        for u in self.sitemap_urls:
            rec = self.pages.get(u)
            if not rec:
                continue
            if rec["status"] != 200 or rec.get("hops"):
                self.issue("sitemap_bad_url", u, "status %s, hops %s" % (rec["status"], rec.get("hops")))
            elif rec.get("canonical_state") in ("other", "offhost"):
                self.issue("sitemap_bad_url", u, "canonicalized to %s" % rec.get("canonical"))
            if not self.inlinks.get(u) and u != self.start and rec["status"] == 200:
                self.issue("sitemap_orphan", u, "0 internal links from %d crawled pages" % len(crawled_final))
        if self.sitemap_files:
            for u, rec in indexable.items():
                if u not in self.sitemap_urls and rec["url"] not in self.sitemap_urls:
                    self.issue("not_in_sitemap", u)
        # hreflang
        for rec in self.by_final.values():
            hl = rec.get("hreflang") or []
            if not hl:
                continue
            u = rec["final_url"]
            codes = [c for c, _ in hl]
            for code in codes:
                if code.lower() != "x-default" and (not HREFLANG_RX.match(code) or code.lower().endswith("-uk")):
                    self.issue("hreflang_invalid", u, code)
            if u not in [h for _, h in hl]:
                self.issue("hreflang_no_self", u)
            if len(hl) > 1 and "x-default" not in [c.lower() for c in codes]:
                self.issue("hreflang_no_xdefault", u)
            for code, target in hl:
                if target == u:
                    continue
                t = self.pages.get(target) or self.by_final.get(target)
                if not t:
                    continue
                if t["status"] != 200 or t.get("hops") or t.get("noindex") or t.get("canonical_state") in ("other", "offhost"):
                    self.issue("hreflang_target_bad", u, "%s (%s): status %s" % (target, code, t["status"]))
                    continue
                back = [h for _, h in (t.get("hreflang") or [])]
                if u not in back:
                    self.issue("hreflang_not_reciprocal", u, "%s (%s) does not link back" % (target, code))
        # robots: bots and blocked resources
        self.bot_table = []
        for token, sev, meaning in BOTS:
            ok, rule, label = self.robots.check(token, self.start)
            blocked = [u for u in self.by_final if not self.robots.check(token, u)[0]]
            self.bot_table.append({"bot": token, "group": label, "start_allowed": ok, "rule": rule,
                                   "crawled_pages_blocked": len(blocked), "meaning": meaning})
            if not ok:
                self.issue("bot_blocked", self.start, "%s blocked (%s): %s" % (token, rule, meaning), sev)
            elif blocked and token in ("Googlebot", "Bingbot"):
                self.issue("bot_blocked", blocked[0], "%s blocked on %d crawled page(s)" % (token, len(blocked)), "Medium")
        res_blocked = set()
        for rec in self.by_final.values():
            for res in rec.get("resources", []):
                if same_site(res, self.origin) and not self.robots.check("Googlebot", res)[0]:
                    res_blocked.add(res)
        if res_blocked:
            self.issue("resources_blocked", self.origin, ", ".join(sorted(res_blocked)[:5]))
        for url, rule in self.skipped:
            self.issue("robots_skipped", url, rule or "")
        if self.limit_hit:
            self.issue("crawl_limit", self.start, "limit %d" % self.args.limit)

    def resolve_start(self):
        """Follow start URL redirects across hosts once (example.com to www, http to https)."""
        current, chain = self.start, []
        for _ in range(6):
            r = self.fetcher.get(current)
            chain.append((current, r.status))
            loc = r.header("Location") if r.status in (301, 302, 303, 307, 308) else None
            if not loc:
                break
            nxt = norm_url(parse.urljoin(current, loc))
            if not nxt.lower().startswith(("http://", "https://")) or nxt in [c[0] for c in chain]:
                break
            current = nxt
        final = chain[-1][0]
        if not same_site(final, self.start) or parse.urlsplit(final).scheme != parse.urlsplit(self.start).scheme:
            self.issue("start_redirected", self.start, " > ".join("%s (%s)" % c for c in chain))
            self.start = final
            sp = parse.urlsplit(final)
            self.origin = "%s://%s" % (sp.scheme, sp.netloc)

    def run(self):
        self.resolve_start()
        if not self.load_robots():
            self.bot_table = []
            self.aborted = "robots.txt unreachable (status %s); crawl stopped, as Google pauses crawling in this state" % self.robots_status
            return
        ok, rule = self.own_allowed(self.start)
        if not ok:
            self.issue("robots_skipped", self.start, "start URL disallowed for %s: %s" % (UA_TOKEN, rule))
        self.load_sitemaps()
        self.crawl()
        self.soft404_probe()
        self.post_checks()


# ---------------------------------------------------------------- output
def md_escape(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def build_report(pf):
    a = pf.args
    lines = []
    sev_counts = {s: 0 for s in SEVERITIES}
    for i in pf.issues:
        sev_counts[i["severity"]] += 1
    html_pages = [r for r in pf.by_final.values() if r.get("parsed")]
    lines.append("# SEO preflight (no JavaScript): %s" % pf.start)
    lines.append("")
    lines.append("Generated %s by seo_preflight.py %s. User agent: `%s`. Delay %.2f s. Requests made: %d." % (
        time.strftime("%Y-%m-%d %H:%M"), VERSION, a.user_agent, pf.fetcher.delay, pf.fetcher.count))
    lines.append("")
    lines.append("What this shows: raw HTML as non rendering crawlers and most AI bots receive it. Google renders JavaScript later; confirm rendered output with Search Console URL Inspection before closing a finding.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Item | Value |")
    lines.append("|------|-------|")
    lines.append("| URLs fetched (incl. redirects and errors) | %d |" % len(pf.pages))
    lines.append("| HTML pages parsed | %d |" % len(html_pages))
    lines.append("| Crawl status | %s |" % (pf.aborted or ("limit reached (orphan and duplicate checks are partial)" if pf.limit_hit else "complete")))
    lines.append("| robots.txt status | %s |" % pf.robots_status)
    lines.append("| Sitemaps parsed | %d (%d URLs) |" % (len(pf.sitemap_files), len(pf.sitemap_urls)))
    lines.append("| Soft 404 probe | %s |" % (("status %s" % pf.soft404["status"]) if pf.soft404 else "not run"))
    lines.append("| Issues | %s |" % ", ".join("%s %d" % (s, sev_counts[s]) for s in SEVERITIES))
    lines.append("")

    lines.append("## Robots.txt access by bot (start URL)")
    lines.append("")
    lines.append("| Bot | Group used | Start URL | Rule | Crawled pages blocked | Meaning |")
    lines.append("|-----|-----------|-----------|------|----------------------|---------|")
    for b in getattr(pf, "bot_table", []):
        lines.append("| %s | %s | %s | %s | %d | %s |" % (b["bot"], b["group"], "allowed" if b["start_allowed"] else "BLOCKED",
                                                       md_escape(b["rule"] or "none"), b["crawled_pages_blocked"], b["meaning"]))
    lines.append("")
    lines.append("robots.txt shows intent only. CDN or WAF rules (for example Cloudflare AI crawler defaults) can still block bots; check server or CDN logs per user agent.")
    lines.append("")

    lines.append("## Issues by check")
    lines.append("")
    lines.append("| Severity | Check | URLs | Examples | Fix |")
    lines.append("|----------|-------|------|----------|-----|")
    grouped = {}
    for i in pf.issues:
        grouped.setdefault((i["severity"], i["code"]), []).append(i)
    for (sev, code), items in sorted(grouped.items(), key=lambda kv: (SEV_RANK[kv[0][0]], -len(kv[1]), kv[0][1])):
        ex = "; ".join("%s %s" % (x["url"], ("(" + x["detail"] + ")") if x["detail"] else "") for x in items[:3])
        lines.append("| %s | %s | %d | %s | %s |" % (sev, CHECKS[code][1], len(items), md_escape(ex), CHECKS[code][2]))
    lines.append("")

    lines.append("## Pages")
    lines.append("")
    lines.append("| URL | Status | Hops | Words | Title len | Desc len | H1 | Canonical | Noindex | JSON-LD | Int. links |")
    lines.append("|-----|--------|------|-------|-----------|----------|----|-----------|---------|---------|-----------|")
    for url, r in sorted(pf.pages.items()):
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            md_escape(url), r["status"], r.get("hops", 0), r.get("word_count", ""), r.get("title_len", ""), r.get("desc_len", ""),
            r.get("h1_count", ""), r.get("canonical_state", ""), ("yes (" + r["noindex_source"] + ")") if r.get("noindex") else "",
            md_escape(", ".join(r.get("jsonld_types", [])) + (" ERR" if r.get("jsonld_errors") else "")), r.get("internal_link_count", "")))
    lines.append("")

    chains = [r for r in pf.pages.values() if r.get("hops")]
    if chains:
        lines.append("## Redirects")
        lines.append("")
        for r in chains:
            lines.append("- %s: %s" % (r["url"], " > ".join("%s (%s)" % (c[0], c[1] if c[1] is not None else "not followed") for c in r["chain"])))
        lines.append("")
    if pf.sitemap_urls:
        lines.append("## Sitemap coverage")
        lines.append("")
        in_sm = set(pf.sitemap_urls)
        crawled = set(pf.pages)
        lines.append("- URLs in sitemap: %d. Crawled: %d. In sitemap but not reached through links: %d." % (
            len(in_sm), len(in_sm & crawled), len([u for u in in_sm if not pf.inlinks.get(u)])))
        lines.append("- Sitemap URLs with lastmod: %d of %d." % (len([v for v in pf.sitemap_urls.values() if v]), len(in_sm)))
        lines.append("")
    lines.append("## Next steps")
    lines.append("")
    lines.append("1. Fix Critical and High items first; they block crawling, indexing or rendering.")
    lines.append("2. For JS-only shells, compare with the rendered HTML (URL Inspection live test) and plan SSR, SSG or prerendering (see references/ai-built-and-js-sites.md).")
    lines.append("3. Bot blocks for AI crawlers are a policy decision: hand off to ai-search-optimization.")
    lines.append("4. Re-run this preflight after each fix and before every release.")
    return "\n".join(lines) + "\n"


def build_json(pf):
    pages = []
    for url, r in sorted(pf.pages.items()):
        d = {k: v for k, v in r.items() if k not in ("internal_links", "resources")}
        d["chain"] = [list(c) for c in r["chain"]]
        d["inlinks"] = len(pf.inlinks.get(url, ()))
        pages.append(d)
    return {"tool": "seo_preflight.py", "version": VERSION, "start_url": pf.start, "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "requests": pf.fetcher.count, "limit_hit": pf.limit_hit, "robots_status": pf.robots_status,
            "robots_sitemaps": pf.robots.sitemaps, "bots": getattr(pf, "bot_table", []),
            "sitemaps": pf.sitemap_files, "sitemap_url_count": len(pf.sitemap_urls), "soft404": pf.soft404,
            "skipped": pf.skipped, "issues": pf.issues, "pages": pages}


def main(argv=None):
    ap = argparse.ArgumentParser(description="No-JavaScript SEO preflight crawler (stdlib only).")
    ap.add_argument("url", help="Start URL, for example https://www.example.com/ or http://127.0.0.1:8000/")
    ap.add_argument("--limit", type=int, default=50, help="Max URLs to fetch (default 50)")
    ap.add_argument("--delay", type=float, default=1.0, help="Seconds between requests (default 1.0)")
    ap.add_argument("--timeout", type=float, default=15.0, help="Request timeout in seconds (default 15)")
    ap.add_argument("--user-agent", default=DEFAULT_UA, help="User agent string")
    ap.add_argument("--thin-words", type=int, default=150, help="Word count below which raw HTML is thin (default 150)")
    ap.add_argument("--no-sitemap-crawl", action="store_true", help="Do not fetch sitemap URLs that links did not reach")
    ap.add_argument("--out", help="Write the Markdown report here (default: stdout)")
    ap.add_argument("--json", help="Also write a JSON report here")
    ap.add_argument("--fail-on", choices=["critical", "high", "medium", "none"], default="none",
                    help="Exit 2 when an issue at or above this severity exists (for CI)")
    ap.add_argument("--quiet", action="store_true", help="No progress lines on stderr")
    args = ap.parse_args(argv)
    if not re.match(r"^https?://", args.url, re.I):
        ap.error("url must start with http:// or https://")
    if args.delay < 0.1 and not re.search(r"//(localhost|127\.0\.0\.1|\[::1\])", args.url):
        ap.error("--delay under 0.1 s is only allowed for local servers")
    pf = Preflight(args)
    try:
        pf.run()
    except KeyboardInterrupt:
        print("Interrupted; writing partial report.", file=sys.stderr)
        if not hasattr(pf, "bot_table"):
            pf.bot_table = []
    report = build_report(pf)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report)
    else:
        sys.stdout.write(report)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(build_json(pf), fh, indent=2, default=list)
    if args.fail_on != "none":
        limit = SEV_RANK[args.fail_on.capitalize()]
        if any(SEV_RANK[i["severity"]] <= limit for i in pf.issues):
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
