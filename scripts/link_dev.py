#!/usr/bin/env python3
"""Rebuild .claude/agents and .claude/skills as folders of relative symlinks.

This repo is also a workspace, so Claude Code must load the Ads Master agents
and skills plus every kit (kits/*/agents, kits/*/skills). Each kit is also
linked at .claude/<kit> so skills find their scripts and templates the same way
as in an installed project.

Usage:
  python3 scripts/link_dev.py          # rebuild the links
  python3 scripts/link_dev.py --check  # exit 1 if links are missing or stale
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLAUDE = os.path.join(ROOT, ".claude")


def wanted():
    out = {}
    sources = [("agents", "agents"), ("skills", "skills")]
    kits = os.path.join(ROOT, "kits")
    kit_names = sorted(os.listdir(kits)) if os.path.isdir(kits) else []
    for kit in kit_names:
        sources += [(f"kits/{kit}/agents", "agents"), (f"kits/{kit}/skills", "skills")]
        out[kit] = os.path.join("..", "kits", kit)
    for src, dest in sources:
        base = os.path.join(ROOT, src)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            full = os.path.join(base, name)
            if (dest == "agents" and name.endswith(".md")) or (dest == "skills" and os.path.isdir(full)):
                key = f"{dest}/{name}"
                if key in out:
                    raise SystemExit(f"name collision: {key} exists in two sources")
                out[key] = os.path.join("..", "..", src, name)
    return out


def current():
    out = {}
    for dest in ("agents", "skills"):
        d = os.path.join(CLAUDE, dest)
        if os.path.isdir(d) and not os.path.islink(d):
            for name in os.listdir(d):
                p = os.path.join(d, name)
                if os.path.islink(p):
                    out[f"{dest}/{name}"] = os.readlink(p)
    for name in os.listdir(CLAUDE):
        p = os.path.join(CLAUDE, name)
        if os.path.islink(p) and name not in ("agents", "skills"):
            out[name] = os.readlink(p)
    return out


def main():
    want = wanted()
    if "--check" in sys.argv:
        have = current()
        bad = sorted(k for k in set(want) | set(have) if want.get(k) != have.get(k))
        if bad:
            print("dev links out of date (run python3 scripts/link_dev.py):", ", ".join(bad[:10]))
            return 1
        print(f"dev links ok ({len(want)} links)")
        return 0
    for dest in ("agents", "skills"):
        d = os.path.join(CLAUDE, dest)
        if os.path.islink(d):
            os.remove(d)
        os.makedirs(d, exist_ok=True)
        for name in os.listdir(d):
            p = os.path.join(d, name)
            if os.path.islink(p):
                os.remove(p)
    for key, target in want.items():
        p = os.path.join(CLAUDE, key)
        if os.path.islink(p):
            os.remove(p)
        os.symlink(target, p)
    print(f"linked {len(want)} items into .claude/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
