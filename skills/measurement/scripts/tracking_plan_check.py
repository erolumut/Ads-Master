#!/usr/bin/env python3
"""Check analytics payloads and code against a tracking plan allowlist.

Usage:
  tracking_plan_check.py --plan tracking-plan.json --payloads sample.jsonl
  tracking_plan_check.py --plan tracking-plan.json --code src/

Payload lines look like {"event": "purchase", "params": {...}} (a top level
"name" key is accepted too). Exit codes: 0 pass, 1 fail, 2 could not run.
"""
import argparse
import json
import os
import re
import sys

EMAIL = re.compile(r"[^@\s]+@[^@\s]+\.[a-z]{2,}", re.I)
PHONE = re.compile(r"\+?\d[\d\s().-]{8,}\d")
URL_QUERY = re.compile(r"https?://\S+\?\S+")
ID_OK = re.compile(r"^[A-Za-z0-9_.:-]{1,64}$")
EMIT = [
    re.compile(r"gtag\(\s*['\"]event['\"]\s*,\s*['\"]([A-Za-z0-9_]+)['\"]"),
    re.compile(r"event['\"]?\s*:\s*['\"]([A-Za-z0-9_]+)['\"]"),
    re.compile(r"\btrack\(\s*['\"]([A-Za-z0-9_]+)['\"]"),
    re.compile(r"fbq\(\s*['\"]track(?:Custom)?['\"]\s*,\s*['\"]([A-Za-z0-9_]+)['\"]"),
    re.compile(r"ttq\.track\(\s*['\"]([A-Za-z0-9_]+)['\"]"),
]
CODE_EXT = (".js", ".jsx", ".ts", ".tsx", ".mjs", ".liquid", ".php", ".py", ".vue", ".svelte", ".html")
SKIP_DIRS = {"node_modules", ".git", ".next", "dist", "build", "vendor", "__pycache__"}


def check_value(spec, val):
    t = spec.get("type")
    if t == "bool":
        return isinstance(val, bool)
    if t == "num":
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            return False
        return spec.get("min", float("-inf")) <= val <= spec.get("max", float("inf"))
    if t == "enum":
        return val in spec.get("values", [])
    if t == "id":
        return isinstance(val, (str, int)) and bool(ID_OK.match(str(val)))
    if t == "route":
        return isinstance(val, str) and val.startswith("/") and "?" not in val
    return False


def pii(val):
    s = str(val)
    return bool(EMAIL.search(s) or URL_QUERY.search(s) or (PHONE.search(s) and not s.replace(".", "").isdigit()))


def check_payloads(plan, path):
    errors, n = [], 0
    events = plan.get("events", {})
    with open(path, encoding="utf-8") as fh:
        for no, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            n += 1
            try:
                ev = json.loads(line)
            except ValueError:
                errors.append(f"line {no}: not JSON")
                continue
            name = ev.get("event") or ev.get("name")
            params = ev.get("params", {}) or {}
            if name not in events:
                errors.append(f"line {no}: undeclared event '{name}'")
                continue
            props = events[name].get("props", {})
            for k, v in params.items():
                if k not in props:
                    errors.append(f"line {no}: {name}.{k} undeclared")
                elif not check_value(props[k], v):
                    errors.append(f"line {no}: {name}.{k}={v!r} fails type {props[k].get('type')}")
                if pii(v):
                    errors.append(f"line {no}: {name}.{k} looks like PII")
    return n, errors


def check_code(plan, root):
    emitted = {}
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if not f.endswith(CODE_EXT):
                continue
            p = os.path.join(dirpath, f)
            try:
                text = open(p, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            for rx in EMIT:
                for m in rx.finditer(text):
                    emitted.setdefault(m.group(1), set()).add(os.path.relpath(p, root))
    declared = set(plan.get("events", {}))
    errors = [f"emitted but undeclared: {e} ({', '.join(sorted(emitted[e])[:3])})" for e in sorted(set(emitted) - declared)]
    errors += [f"declared but never emitted in code: {e}" for e in sorted(declared - set(emitted))]
    return len(emitted), errors


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--plan", required=True)
    ap.add_argument("--payloads")
    ap.add_argument("--code")
    a = ap.parse_args()
    if not (a.payloads or a.code):
        print("could not run: pass --payloads or --code")
        return 2
    try:
        plan = json.load(open(a.plan, encoding="utf-8"))
    except (OSError, ValueError) as exc:
        print(f"could not run: cannot read plan ({exc})")
        return 2
    failed = False
    if a.payloads:
        if not os.path.isfile(a.payloads):
            print(f"could not run: {a.payloads} missing")
            return 2
        n, errs = check_payloads(plan, a.payloads)
        print(f"payloads: {n} events checked, {len(errs)} problems")
        for e in errs:
            print("  FAIL", e)
        failed |= bool(errs)
    if a.code:
        if not os.path.isdir(a.code):
            print(f"could not run: {a.code} is not a directory")
            return 2
        n, errs = check_code(plan, a.code)
        print(f"code: {n} distinct event names found, {len(errs)} differences")
        for e in errs:
            print("  FAIL", e)
        failed |= bool(errs)
    print("This gate cannot cover: dynamic event names, events created only in a tag manager UI, "
          "and payloads not in the sample.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
