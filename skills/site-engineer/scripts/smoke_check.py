#!/usr/bin/env python3
"""Post release smoke check against any environment (read only, G0).

The same config runs against local, preview and production: only BASE_URL
changes. For each page: status code, required patterns, patterns that must
appear exactly once (a pixel or tag ID: twice means double counting), and
patterns that must never appear (noindex on a money page, template braces,
placeholder text, test keys). Optionally compares a health endpoint's build
SHA with the commit you expect to be live.

Usage:
  python3 -I smoke_check.py smoke.json --base-url https://www.example.com
  BASE_URL=https://preview.example.com python3 -I smoke_check.py smoke.json
  python3 -I smoke_check.py smoke.json --expect-sha 1a2b3c4   # health check
  python3 -I smoke_check.py --example > smoke.json             # starter config

Exit codes: 0 pass, 1 fail, 2 could not run (no config, no base URL, or no
page reachable at all). Standard library only. Respects HTTPS_PROXY.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

UA = ("Mozilla/5.0 (iPhone; CPU iPhone OS 18_6 like Mac OS X) AppleWebKit/605.1.15 "
      "(KHTML, like Gecko) Version/18.6 Mobile/15E148 Safari/604.1 AdsMasterSmoke/1.0")

EXAMPLE = {
    "_comment": "Patterns are regular expressions matched against the HTML. Keep IDs in the project, never secrets.",
    "defaults": {
        "must_not_contain": ["<meta[^>]+noindex", r"\{\{\s*\w+", "lorem ipsum", "pk_test_|sk_test_"]
    },
    "pages": [
        {"path": "/", "expect_status": 200, "must_contain": ["<title>[^<]{5,}</title>"]},
        {"path": "/products/hero-pack", "expect_status": 200,
         "must_contain": ["application/ld\\+json", "add[- _]?to[- _]?cart"],
         "must_contain_once": ["G-XXXXXXXXXX", "fbq\\(['\"]init['\"]"]},
        {"path": "/cart", "expect_status": 200},
        {"path": "/old-landing-page", "expect_status": 301}
    ],
    "health": {"path": "/api/health", "sha_field": "buildSha"}
}


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch(url, timeout, follow):
    handlers = [] if follow else [NoRedirect()]
    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/json"})
    start = time.time()
    try:
        with opener.open(req, timeout=timeout) as resp:
            body = resp.read(3_000_000).decode("utf-8", "replace")
            return resp.status, body, time.time() - start, None
    except urllib.error.HTTPError as exc:
        body = exc.read(200_000).decode("utf-8", "replace") if exc.fp else ""
        return exc.code, body, time.time() - start, None
    except (urllib.error.URLError, OSError, ValueError) as exc:
        return None, "", time.time() - start, str(exc)


def check_page(base, page, defaults, timeout):
    url = base.rstrip("/") + page.get("path", "/")
    expect = page.get("expect_status", 200)
    follow = not (300 <= int(expect) < 400)
    status, body, secs, err = fetch(url, timeout, follow)
    problems = []
    if err:
        return url, None, secs, [f"unreachable: {err}"], True
    if status != expect:
        problems.append(f"status {status}, expected {expect}")
    if 200 <= (status or 0) < 300:
        for pat in page.get("must_contain", []):
            if not re.search(pat, body, re.I):
                problems.append(f"missing /{pat}/")
        for pat in page.get("must_contain_once", []):
            n = len(re.findall(pat, body, re.I))
            if n != 1:
                problems.append(f"/{pat}/ found {n} times, expected exactly 1")
        for pat in defaults.get("must_not_contain", []) + page.get("must_not_contain", []):
            if re.search(pat, body, re.I):
                problems.append(f"forbidden /{pat}/ present")
    return url, status, secs, problems, False


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("config", nargs="?")
    ap.add_argument("--base-url", default=os.environ.get("BASE_URL"))
    ap.add_argument("--expect-sha", help="commit expected live; compared with the health endpoint")
    ap.add_argument("--timeout", type=float, default=20.0)
    ap.add_argument("--example", action="store_true", help="print a starter config and exit")
    a = ap.parse_args()
    if a.example:
        print(json.dumps(EXAMPLE, indent=2))
        return 0
    if not a.config or not os.path.isfile(a.config):
        print("could not run: pass a config file (see --example)")
        return 2
    if not a.base_url:
        print("could not run: pass --base-url or set BASE_URL")
        return 2
    try:
        cfg = json.load(open(a.config, encoding="utf-8"))
    except ValueError as exc:
        print(f"could not run: config is not valid JSON ({exc})")
        return 2
    defaults = cfg.get("defaults", {})
    rows, failed, unreachable = [], False, 0
    pages = cfg.get("pages", [])
    for page in pages:
        url, status, secs, problems, down = check_page(a.base_url, page, defaults, a.timeout)
        unreachable += down
        failed |= bool(problems)
        rows.append(f"| {url} | {status if status is not None else 'n/a'} | {secs:.2f}s | "
                     f"{'PASS' if not problems else 'FAIL: ' + '; '.join(problems)} |")
    health = cfg.get("health")
    if health and a.expect_sha:
        url = a.base_url.rstrip("/") + health.get("path", "/api/health")
        status, body, secs, err = fetch(url, a.timeout, True)
        verdict = "FAIL"
        try:
            live = str(json.loads(body).get(health.get("sha_field", "buildSha"), ""))
            verdict = "PASS" if live and (live.startswith(a.expect_sha) or a.expect_sha.startswith(live)) \
                else f"FAIL: live {live or 'empty'}, expected {a.expect_sha}"
        except ValueError:
            verdict = f"FAIL: no JSON ({err or status})"
        failed |= verdict != "PASS"
        rows.append(f"| {url} | {status} | {secs:.2f}s | health SHA {verdict} |")
    print(f"# Smoke check: {a.base_url}\n\n| URL | Status | Time | Result |\n|-----|-------:|-----:|--------|")
    print("\n".join(rows))
    print("\nThis gate cannot cover: JavaScript rendered content, events that fire only after interaction "
          "(use the tracking plan check or Playwright), checkout payment steps, and in-app browser quirks.")
    if pages and unreachable == len(pages):
        print("could not run: no page reachable")
        return 2
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
