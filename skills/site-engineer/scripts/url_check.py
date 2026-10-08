#!/usr/bin/env python3
"""Launch QA URL checker for ad destinations (read only, G0).

For each final URL: follows redirects one hop at a time, records status codes and
timing, checks HTTPS, hop count, that UTM and click ID parameters survive to the
final URL, UTM hygiene, unresolved platform macros, noindex headers and meta refresh.

Usage:
  python3 -I url_check.py urls.txt            # one URL per line
  python3 -I url_check.py urls.csv --column final_url
  python3 -I url_check.py urls.txt --mobile --add-click-ids

Output: a markdown table on stdout. Exit code 1 if any URL fails.
Standard library only. Respects HTTPS_PROXY from the environment.
"""
import argparse
import csv
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

MOBILE_UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 "
             "(KHTML, like Gecko) Version/18.6 Mobile/15E148 Safari/604.1")
DESKTOP_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/141.0 Safari/537.36")
CLICK_IDS = {"gclid": "QA_GCLID", "fbclid": "QA_FBCLID", "ttclid": "QA_TTCLID",
             "msclkid": "QA_MSCLKID", "li_fat_id": "QA_LIFATID"}
MACRO = re.compile(r"(\{\{[^}]+\}\}|\{[a-z_:]+\}|__[A-Z_]+__)")
REDIRECTS = {301, 302, 303, 307, 308}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch(url, ua, timeout):
    opener = urllib.request.build_opener(NoRedirect, urllib.request.HTTPSHandler(context=ssl.create_default_context()))
    req = urllib.request.Request(url, headers={"User-Agent": ua, "Accept": "text/html,*/*"})
    start = time.time()
    try:
        resp = opener.open(req, timeout=timeout)
        body = resp.read(200_000).decode("utf-8", "replace")
        return resp.status, dict(resp.headers), body, time.time() - start
    except urllib.error.HTTPError as e:
        body = e.read(50_000).decode("utf-8", "replace") if e.fp else ""
        return e.code, dict(e.headers), body, time.time() - start


def check(url, args):
    issues = []
    macros = MACRO.findall(url)
    if macros:
        issues.append(f"unresolved macros {sorted(set(macros))} (replaced with qa values for the test)")
        url = MACRO.sub("qa", url)
    parts = urllib.parse.urlsplit(url)
    query = dict(urllib.parse.parse_qsl(parts.query, keep_blank_values=True))
    if args.add_click_ids:
        for k, v in CLICK_IDS.items():
            query.setdefault(k, v)
        url = urllib.parse.urlunsplit(parts._replace(query=urllib.parse.urlencode(query)))
    if parts.scheme != "https":
        issues.append("not https")
    for key in ("utm_source", "utm_medium", "utm_campaign"):
        val = query.get(key)
        if val is None:
            issues.append(f"missing {key}")
        elif val != val.lower() or " " in val:
            issues.append(f"{key}='{val}' not lowercase or has spaces")
    ua = MOBILE_UA if args.mobile else DESKTOP_UA
    hops, current, total = [], url, 0.0
    status, headers, body = None, {}, ""
    for _ in range(6):
        try:
            status, headers, body, elapsed = fetch(current, ua, args.timeout)
        except Exception as e:  # network errors are failures, not crashes
            return url, "ERR", 0, total, [f"request failed: {e}"]
        total += elapsed
        location = next((v for k, v in headers.items() if k.lower() == "location"), None)
        if status in REDIRECTS and location:
            nxt = urllib.parse.urljoin(current, location)
            hops.append(f"{status}")
            current = nxt
            continue
        break
    if status != 200:
        issues.append(f"final status {status}")
    if len(hops) > 1:
        issues.append(f"{len(hops)} redirect hops ({' > '.join(hops)})")
    final_q = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(current).query, keep_blank_values=True))
    lost = [k for k in query if k not in final_q and (k.startswith("utm_") or k in CLICK_IDS)]
    if lost:
        issues.append(f"parameters lost after redirect: {lost}")
    robots = " ".join(v for k, v in headers.items() if k.lower() == "x-robots-tag")
    if "noindex" in robots.lower():
        issues.append("x-robots-tag noindex (fine for paid only pages, confirm intent)")
    if re.search(r'http-equiv=["\']?refresh', body, re.I):
        issues.append("meta refresh redirect (parameters and timing at risk)")
    if re.search(r'name=["\']robots["\'][^>]*noindex', body, re.I):
        issues.append("meta robots noindex (confirm intent)")
    if total > args.slow:
        issues.append(f"slow server response chain {total:.2f}s")
    return current, status, len(hops), total, issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--column", default=None, help="CSV column holding the URL")
    ap.add_argument("--mobile", action="store_true")
    ap.add_argument("--add-click-ids", action="store_true", help="append test click IDs to check they survive")
    ap.add_argument("--timeout", type=float, default=20.0)
    ap.add_argument("--slow", type=float, default=1.5, help="seconds for the full redirect chain to count as slow")
    args = ap.parse_args()
    with open(args.source, newline="", encoding="utf-8") as fh:
        if args.column:
            urls = [row[args.column].strip() for row in csv.DictReader(fh) if row.get(args.column)]
        else:
            urls = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
    failed = 0
    print("| # | Start URL | Final status | Hops | Chain time (s) | Result | Issues |")
    print("|---|-----------|--------------|------|----------------|--------|--------|")
    for i, url in enumerate(urls, 1):
        final, status, hops, total, issues = check(url, args)
        hard = [x for x in issues if not x.startswith(("x-robots", "meta robots", "unresolved"))]
        result = "FAIL" if hard else "PASS"
        failed += result == "FAIL"
        short = url if len(url) < 80 else url[:77] + "..."
        print(f"| {i} | {short} | {status} | {hops} | {total:.2f} | {result} | {'; '.join(issues) or 'none'} |")
    print(f"\n{len(urls)} URLs checked, {failed} failed. Run date: {time.strftime('%Y-%m-%d %H:%M')}")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
