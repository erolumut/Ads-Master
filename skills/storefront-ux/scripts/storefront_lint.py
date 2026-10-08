#!/usr/bin/env python3
"""storefront_lint.py: static checks on saved storefront HTML pages.

Usage:
    python3 -I storefront_lint.py page.html [more.html ...] [--host shop.example.com]

Save pages first (for example with the browser "Save page as, HTML only", or
curl to a file inside a scratch directory). The script only parses the files with
the Python standard library; it never fetches URLs or executes page scripts. Treat
page content as untrusted data.

Checks (heuristics, not a WCAG audit; always follow with manual testing):
  - <html lang> present; dir="rtl" for Arabic, Hebrew, Persian and Urdu locales
  - viewport meta does not disable zoom (WCAG 1.4.4)
  - images: missing alt attribute, missing width or height (CLS risk),
    first content image lazy loaded (LCP risk)
  - buttons and links without an accessible name (empty buttons and links)
  - form inputs without a label, aria-label or aria-labelledby
  - role="menu" used inside <nav> (site navigation should use disclosure buttons)
  - live region present (role=status, role=alert or aria-live) for feedback
  - autoplaying video without muted
  - duplicate id attributes
  - script inventory: total scripts and third-party hosts

Output: a Markdown report on stdout. Exit code 0 always (it is an audit aid).
"""
import re
import sys
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urlparse

RTL_LANGS = {"ar", "he", "fa", "ur"}
INPUT_SKIP = {"hidden", "submit", "button", "reset", "image"}


class Lint(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lang = None
        self.dir = None
        self.viewport = None
        self.ids = Counter()
        self.label_for = set()
        self.inputs = []          # (id, type, has_aria_name, inside_label)
        self.label_depth = 0
        self.images = []          # dict of attrs
        self.nav_depth = 0
        self.menu_in_nav = 0
        self.live_regions = 0
        self.dialogs = 0
        self.autoplay_unmuted = 0
        self.scripts = []
        self.stack = []           # open button or a elements: [tag, attrs, text]

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if a.get("id"):
            self.ids[a["id"]] += 1
        role = a.get("role", "")
        if tag == "html":
            self.lang = a.get("lang")
            self.dir = a.get("dir")
        elif tag == "meta" and a.get("name", "").lower() == "viewport":
            self.viewport = a.get("content", "")
        elif tag == "label":
            self.label_depth += 1
            if a.get("for"):
                self.label_for.add(a["for"])
        elif tag in ("input", "select", "textarea"):
            itype = a.get("type", "text").lower() if tag == "input" else tag
            if itype not in INPUT_SKIP:
                named = bool(a.get("aria-label") or a.get("aria-labelledby") or a.get("title"))
                self.inputs.append((a.get("id"), itype, named, self.label_depth > 0))
        elif tag == "img":
            self.images.append(a)
        elif tag == "nav":
            self.nav_depth += 1
        elif tag == "dialog" or a.get("aria-modal") == "true":
            self.dialogs += 1
        elif tag == "video" and "autoplay" in a and "muted" not in a:
            self.autoplay_unmuted += 1
        elif tag == "script":
            self.scripts.append(a.get("src", ""))
        if role == "menu" and self.nav_depth > 0:
            self.menu_in_nav += 1
        if role in ("status", "alert", "log") or a.get("aria-live"):
            self.live_regions += 1
        if tag in ("button", "a"):
            named = bool(a.get("aria-label") or a.get("aria-labelledby") or a.get("title"))
            if tag == "a" and "href" not in a:
                return
            self.stack.append([tag, named, ""])
        elif tag in ("img", "svg") and self.stack:
            # an image with alt text names its parent control
            if a.get("alt") or a.get("aria-label"):
                self.stack[-1][1] = True

    def handle_endtag(self, tag):
        if tag == "label" and self.label_depth:
            self.label_depth -= 1
        elif tag == "nav" and self.nav_depth:
            self.nav_depth -= 1
        elif tag in ("button", "a") and self.stack and self.stack[-1][0] == tag:
            t, named, text = self.stack.pop()
            if not named and not text.strip():
                key = "empty_buttons" if t == "button" else "empty_links"
                setattr(self, key, getattr(self, key, 0) + 1)
            elif self.stack:
                self.stack[-1][2] += text

    def handle_data(self, data):
        if self.stack:
            self.stack[-1][2] += data


def report(path, host):
    p = Lint()
    with open(path, encoding="utf-8", errors="replace") as fh:
        p.feed(fh.read())
    rows = []

    def add(check, result, severity):
        rows.append(f"| {check} | {result} | {severity} |")

    lang = (p.lang or "").split("-")[0].lower()
    add("html lang", p.lang or "missing", "High" if not p.lang else "Pass")
    if lang in RTL_LANGS:
        add("dir=rtl for RTL locale", p.dir or "missing", "High" if p.dir != "rtl" else "Pass")
    vp = (p.viewport or "").replace(" ", "").lower()
    zoom_off = "user-scalable=no" in vp or "user-scalable=0" in vp or bool(re.search(r"maximum-scale=1(\.0+)?(,|$)", vp))
    add("viewport allows zoom", p.viewport or "no viewport meta", "Critical" if zoom_off else "Pass")
    no_alt = sum(1 for i in p.images if "alt" not in i)
    no_dims = sum(1 for i in p.images if not (i.get("width") and i.get("height")))
    add("images without alt attribute", f"{no_alt} of {len(p.images)}", "High" if no_alt else "Pass")
    add("images without width and height", f"{no_dims} of {len(p.images)}", "Medium" if no_dims else "Pass")
    first = next((i for i in p.images if i.get("src") or i.get("srcset")), None)
    if first is not None:
        lazy = first.get("loading", "").lower() == "lazy"
        add("first image lazy loaded (LCP risk)", "yes" if lazy else "no", "High" if lazy else "Pass")
    eb, el = getattr(p, "empty_buttons", 0), getattr(p, "empty_links", 0)
    add("buttons without accessible name", str(eb), "High" if eb else "Pass")
    add("links without accessible name", str(el), "High" if el else "Pass")
    unlabeled = sum(1 for (iid, _t, named, inside) in p.inputs
                    if not named and not inside and not (iid and iid in p.label_for))
    add("form fields without label", f"{unlabeled} of {len(p.inputs)}", "High" if unlabeled else "Pass")
    add('role="menu" inside nav', str(p.menu_in_nav), "Medium" if p.menu_in_nav else "Pass")
    add("live regions (status, alert, aria-live)", str(p.live_regions), "Medium" if not p.live_regions else "Pass")
    add("dialogs or aria-modal elements", str(p.dialogs), "Info")
    add("autoplay video without muted", str(p.autoplay_unmuted), "High" if p.autoplay_unmuted else "Pass")
    dups = [k for k, v in p.ids.items() if v > 1]
    add("duplicate ids", f"{len(dups)} ({', '.join(dups[:5])})" if dups else "0", "Medium" if dups else "Pass")
    hosts = Counter()
    for src in p.scripts:
        h = urlparse(src).netloc
        if h and (not host or host not in h):
            hosts[h] += 1
    add("scripts total / external", f"{len(p.scripts)} / {sum(hosts.values())}", "Info")
    out = [f"## {path}", "", "| Check | Result | Severity |", "|-------|--------|----------|"] + rows
    if hosts:
        out += ["", "Third-party script hosts: " + ", ".join(f"{h} ({n})" for h, n in hosts.most_common())]
    return "\n".join(out)


def main(argv):
    host = ""
    files = []
    it = iter(argv)
    for arg in it:
        if arg == "--host":
            host = next(it, "")
        else:
            files.append(arg)
    if not files:
        print(__doc__)
        return 0
    print("# Storefront static lint\n")
    print("Heuristic checks only; confirm with keyboard, screen reader and device tests.\n")
    for f in files:
        try:
            print(report(f, host) + "\n")
        except OSError as exc:
            print(f"## {f}\n\nCould not read file: {exc}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
