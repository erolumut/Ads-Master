#!/usr/bin/env python3
"""Parallel session ledger (Workflow Kit, parallel-sessions skill).

The ledger is a git-ignored Markdown file at the repo root (default PARALLEL-SESSIONS.md, or
ledger.path in workflow-kit.json) with three sections: ACTIVE, MSG, ARCHIVE. Append only.

  python3 ledger.py init [--gitignore]
  python3 ledger.py checkin  --handle H --scope S --intent I [--risky R] [--eta E] [--branch B] [--workdir W]
  python3 ledger.py progress --handle H --note N
  python3 ledger.py msg      --from A --to B --text T
  python3 ledger.py signoff  --handle H --done D [--left L] [--landmines M] [--cleanup C]
  python3 ledger.py show

signoff appends the SIGN-OFF lines to your ACTIVE block and moves it to ARCHIVE.
Standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

KIT_TEMPLATE = Path(__file__).resolve().parent.parent / "templates" / "PARALLEL-SESSIONS.md"
FALLBACK = """# Parallel Session Ledger

> Git-ignored, one machine only, append only. CHECK-IN at start, RE-READ before risky ops, MSG on overlap, SIGN-OFF then ARCHIVE.

## ACTIVE

_(empty)_

## MSG

_(empty)_

## ARCHIVE

_(empty)_
"""
EMPTY = "_(empty)_"
SECTIONS = ("ACTIVE", "MSG", "ARCHIVE")


def now() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M")


def ledger_path(root: Path, override: str | None) -> Path:
    if override:
        return root / override
    cfg = root / "workflow-kit.json"
    if cfg.is_file():
        try:
            path = (json.loads(cfg.read_text(encoding="utf-8")).get("ledger") or {}).get("path")
            if path:
                return root / path
        except (OSError, ValueError):
            pass
    return root / "PARALLEL-SESSIONS.md"


def git(root: Path, *args: str) -> str:
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=10)
        return out.stdout.strip() if out.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def split(text: str) -> tuple[str, dict[str, str]]:
    """Return the header and each section's body (text between its heading and the next)."""
    parts = re.split(r"^## (ACTIVE|MSG|ARCHIVE)\s*$", text, flags=re.M)
    header, bodies = parts[0], {}
    for i in range(1, len(parts) - 1, 2):
        bodies[parts[i]] = parts[i + 1]
    for s in SECTIONS:
        if s not in bodies:
            raise SystemExit(f"error: ledger has no '## {s}' section; fix it by hand or re-run init on a new file")
    return header, bodies


def join(header: str, bodies: dict[str, str]) -> str:
    out = header.rstrip("\n") + "\n\n"
    for s in SECTIONS:
        out += f"## {s}\n" + "\n" + bodies[s].strip("\n") + "\n\n"
    return out.rstrip("\n") + "\n"


def add_to(body: str, block: str) -> str:
    """Append a block to a section body, dropping the empty marker and keeping HTML comments."""
    body = body.replace(EMPTY, "").strip("\n")
    return (body + "\n\n" + block.strip("\n")).strip("\n") if body else block.strip("\n")


def find_block(body: str, handle: str) -> tuple[int, int] | None:
    m = re.search(rf"^### @{re.escape(handle)}\b.*$", body, flags=re.M)
    if not m:
        return None
    nxt = re.search(r"^(### @|<!--)", body[m.end():], flags=re.M)
    end = m.end() + nxt.start() if nxt else len(body)
    return m.start(), end


def load(path: Path) -> str:
    if not path.is_file():
        raise SystemExit(f"error: {path} not found; run: python3 ledger.py init")
    return path.read_text(encoding="utf-8")


def cmd_init(root: Path, path: Path, args) -> int:
    if path.exists():
        print(f"exists: {path}")
    else:
        template = Path(args.template) if args.template else KIT_TEMPLATE
        text = template.read_text(encoding="utf-8") if template.is_file() else FALLBACK
        path.write_text(text, encoding="utf-8")
        print(f"created: {path}")
    if args.gitignore:
        gi = root / ".gitignore"
        rel = path.relative_to(root).as_posix()
        lines = gi.read_text(encoding="utf-8").splitlines() if gi.is_file() else []
        if rel not in lines and f"/{rel}" not in lines:
            with gi.open("a", encoding="utf-8") as fh:
                if lines and lines[-1] != "":
                    fh.write("\n")
                fh.write(f"{rel}\n")
            print(f"added {rel} to .gitignore")
    return 0


def cmd_checkin(root: Path, path: Path, args) -> int:
    header, bodies = split(load(path))
    if find_block(bodies["ACTIVE"], args.handle):
        raise SystemExit(f"error: @{args.handle} already has an ACTIVE block; sign off first or pick another handle")
    branch = args.branch or git(root, "branch", "--show-current") or "<unknown>"
    block = "\n".join([
        f"### @{args.handle} · {now()}",
        f"- branch: {branch}",
        f"- working dir: {args.workdir or str(root)}",
        f"- scope: {args.scope}",
        f"- intent: {args.intent}",
        f"- risky ops: {args.risky}",
        f"- ETA: {args.eta}",
    ])
    others = re.findall(r"^### @(\S+)", bodies["ACTIVE"], flags=re.M)
    bodies["ACTIVE"] = add_to(bodies["ACTIVE"], block)
    path.write_text(join(header, bodies), encoding="utf-8")
    print(f"checked in @{args.handle}")
    if others:
        print("other active sessions: " + ", ".join("@" + o for o in others) + " (read their scope before editing)")
    return 0


def cmd_progress(root: Path, path: Path, args) -> int:
    header, bodies = split(load(path))
    span = find_block(bodies["ACTIVE"], args.handle)
    if not span:
        raise SystemExit(f"error: no ACTIVE block for @{args.handle}")
    s, e = span
    block = bodies["ACTIVE"][s:e].rstrip("\n") + f"\n- PROGRESS {now()}: {args.note}\n\n"
    bodies["ACTIVE"] = bodies["ACTIVE"][:s] + block + bodies["ACTIVE"][e:].lstrip("\n")
    path.write_text(join(header, bodies), encoding="utf-8")
    print(f"progress noted for @{args.handle}")
    return 0


def cmd_msg(root: Path, path: Path, args) -> int:
    header, bodies = split(load(path))
    bodies["MSG"] = add_to(bodies["MSG"], f"- {now()} · MSG @{args.sender} -> @{args.to}: {args.text}")
    path.write_text(join(header, bodies), encoding="utf-8")
    print("message added")
    return 0


def cmd_signoff(root: Path, path: Path, args) -> int:
    header, bodies = split(load(path))
    span = find_block(bodies["ACTIVE"], args.handle)
    if not span:
        raise SystemExit(f"error: no ACTIVE block for @{args.handle}")
    s, e = span
    block = bodies["ACTIVE"][s:e].rstrip("\n") + "\n" + "\n".join([
        f"- SIGN-OFF {now()}",
        f"  - done: {args.done}",
        f"  - left open: {args.left}",
        f"  - landmines: {args.landmines}",
        f"  - cleanup: {args.cleanup}",
    ])
    rest = (bodies["ACTIVE"][:s] + bodies["ACTIVE"][e:]).strip("\n")
    bodies["ACTIVE"] = rest
    if not re.search(r"^### @", rest, flags=re.M):
        bodies["ACTIVE"] = (EMPTY + "\n\n" + bodies["ACTIVE"]).strip("\n")
    bodies["ARCHIVE"] = add_to(bodies["ARCHIVE"], block)
    path.write_text(join(header, bodies), encoding="utf-8")
    print(f"signed off @{args.handle}; block moved to ARCHIVE")
    return 0


def cmd_show(root: Path, path: Path, args) -> int:
    _, bodies = split(load(path))
    active = re.findall(r"^### @(.+)$", bodies["ACTIVE"], flags=re.M)
    print("ACTIVE: " + ("; ".join(active) if active else "none"))
    msgs = [l for l in bodies["MSG"].splitlines() if l.startswith("- ")]
    print(f"MSG: {len(msgs)} message(s)" + ("; last: " + msgs[-1][2:] if msgs else ""))
    print(f"ARCHIVE: {len(re.findall(r'^### @', bodies['ARCHIVE'], flags=re.M))} block(s)")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="repo root (default: current directory)")
    ap.add_argument("--ledger", help="ledger path relative to root (overrides workflow-kit.json)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("init", help="create the ledger from the template if missing")
    p.add_argument("--template", help="template file (default: the kit's templates/PARALLEL-SESSIONS.md)")
    p.add_argument("--gitignore", action="store_true", help="add the ledger to .gitignore")

    p = sub.add_parser("checkin", help="add your CHECK-IN block to ACTIVE")
    p.add_argument("--handle", required=True)
    p.add_argument("--scope", required=True)
    p.add_argument("--intent", required=True)
    p.add_argument("--risky", default="none")
    p.add_argument("--eta", default="unknown")
    p.add_argument("--branch")
    p.add_argument("--workdir")

    p = sub.add_parser("progress", help="add a PROGRESS line to your block")
    p.add_argument("--handle", required=True)
    p.add_argument("--note", required=True)

    p = sub.add_parser("msg", help="add a message to MSG")
    p.add_argument("--from", dest="sender", required=True)
    p.add_argument("--to", required=True)
    p.add_argument("--text", required=True)

    p = sub.add_parser("signoff", help="add SIGN-OFF and move your block to ARCHIVE")
    p.add_argument("--handle", required=True)
    p.add_argument("--done", required=True)
    p.add_argument("--left", default="nothing")
    p.add_argument("--landmines", default="none")
    p.add_argument("--cleanup", default="nothing to clean")

    sub.add_parser("show", help="summarize the ledger")

    args = ap.parse_args(argv)
    root = Path(args.root).resolve()
    path = ledger_path(root, args.ledger)
    handlers = {
        "init": cmd_init, "checkin": cmd_checkin, "progress": cmd_progress,
        "msg": cmd_msg, "signoff": cmd_signoff, "show": cmd_show,
    }
    for attr in ("handle", "to", "sender"):
        value = getattr(args, attr, None)
        if value is not None:
            setattr(args, attr, value.lstrip("@"))
    return handlers[args.cmd](root, path, args)


if __name__ == "__main__":
    sys.exit(main())
