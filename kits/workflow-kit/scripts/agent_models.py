#!/usr/bin/env python3
"""List subagents with their pinned model and effort (Workflow Kit, model-routing skill).

Reads the frontmatter of every agent file and the model related settings, then flags:
  - a full model id (claude-...) where an alias belongs (fable, opus, sonnet, haiku, inherit)
  - an unknown model or effort value
  - no model (the agent runs on CLAUDE_CODE_SUBAGENT_MODEL or the main session's model)
  - an editing agent that can still spawn subagents (no tools list and no disallowedTools: Agent)

  python3 agent_models.py                       scan .claude/agents and agents/
  python3 agent_models.py --dir path/to/agents  scan specific directories (repeatable)
  python3 agent_models.py --strict              exit 1 on any flag
  python3 agent_models.py --json                machine readable output
  python3 agent_models.py --audit               routing audit of the latest session: requested vs
                                                configured vs served model and effort per subagent
  python3 agent_models.py --audit --all         every session of this project
  python3 agent_models.py --audit --transcripts DIR   transcripts folder (default
                                                ~/.claude/projects/<project path with - for symbols>)

The plain listing shows what is CONFIGURED. --audit reads the local session transcripts to show
what was REQUESTED (the spawn's model parameter), CONFIGURED (the agent's frontmatter) and SERVED
(the model ids in the subagent's own transcript). The transcript format is internal to Claude Code
and may change; when it cannot be read the audit reports "could not run", never "ok".

Exit codes: 0 pass, 1 flagged (with --strict), 2 could not run. Standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ALIASES = {"fable", "opus", "sonnet", "haiku", "inherit", "best", "sonnet[1m]", "opus[1m]"}
EFFORTS = {"low", "medium", "high", "xhigh", "max"}
FULL_ID = re.compile(r"^(claude-|anthropic\.|us\.anthropic\.|eu\.anthropic\.)", re.I)
CANNOT_COVER_LIST = ("This gate cannot cover: what actually ran (use --audit), agents defined in "
                     "~/.claude/agents or plugins not scanned, and whether the routing choice fits the work.")
CANNOT_COVER_AUDIT = ("This gate cannot cover: sessions on other machines or cloud containers, transcripts "
                      "already deleted, the main session's own model switches, and whether a served "
                      "model was the right one for the work.")
FAMILIES = ("fable", "opus", "sonnet", "haiku")
MODEL_ENV = (
    "ANTHROPIC_MODEL", "ANTHROPIC_DEFAULT_FABLE_MODEL", "ANTHROPIC_DEFAULT_OPUS_MODEL",
    "ANTHROPIC_DEFAULT_SONNET_MODEL", "ANTHROPIC_DEFAULT_HAIKU_MODEL",
    "CLAUDE_CODE_SUBAGENT_MODEL", "CLAUDE_CODE_SUBAGENT_MODEL_FORCE", "CLAUDE_CODE_EFFORT_LEVEL",
)


def frontmatter(text: str) -> dict[str, str]:
    """Top level scalar keys of a YAML frontmatter block; folded and list values are joined."""
    if not text.startswith("---"):
        return {}
    lines = text.splitlines()
    data: dict[str, str] = {}
    key = None
    for raw in lines[1:]:
        if raw.strip() == "---":
            break
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", raw)
        if m:
            key, value = m.group(1), m.group(2).strip()
            data[key] = "" if value in (">", "|", ">-", "|-") else value.strip("\"'")
        elif key and raw.startswith((" ", "\t")):
            item = raw.strip()
            item = item[2:] if item.startswith("- ") else item
            data[key] = (data[key] + (", " if data[key] else "") + item.strip("\"'")).strip()
    return data


def read_settings(root: Path) -> dict:
    merged: dict = {"env": {}}
    for name in (".claude/settings.json", ".claude/settings.local.json"):
        p = root / name
        if not p.is_file():
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            merged.setdefault("errors", []).append(f"{name}: {exc}")
            continue
        for k in ("model", "advisorModel", "autoCompactWindow", "effortLevel"):
            if k in data:
                merged[k] = data[k]
                merged.setdefault("source", {})[k] = name
        for k, v in (data.get("env") or {}).items():
            if k in MODEL_ENV:
                merged["env"][k] = f"{v} ({name})"
    for k in MODEL_ENV:
        if os.environ.get(k):
            merged["env"][k] = f"{os.environ[k]} (shell env)"
    return merged


def scan(dirs: list[Path], root: Path) -> list[dict]:
    rows: list[dict] = []
    for d in dirs:
        if not d.is_dir():
            continue
        for f in sorted(d.rglob("*.md")):
            fm = frontmatter(f.read_text(encoding="utf-8"))
            if not fm.get("name") and not fm.get("description"):
                continue
            model = fm.get("model", "")
            effort = fm.get("effort", "")
            tools = fm.get("tools", "")
            disallowed = fm.get("disallowedTools", "")
            flags: list[str] = []
            if not model:
                flags.append("no model: runs on CLAUDE_CODE_SUBAGENT_MODEL or the main model")
            elif FULL_ID.match(model):
                flags.append(f"full model id '{model}': use an alias")
            elif model.lower() not in ALIASES:
                flags.append(f"unknown model '{model}'")
            if effort and effort.lower() not in EFFORTS:
                flags.append(f"unknown effort '{effort}'")
            tool_list = {t.strip() for t in re.split(r"[,\s]+", tools) if t.strip()}
            no_spawn = bool(tools) and not ({"Agent", "Task"} & tool_list)
            no_spawn = no_spawn or bool({"Agent", "Task"} & {t.strip() for t in re.split(r"[,\s]+", disallowed)})
            if not no_spawn:
                flags.append("can spawn subagents (add a tools list or disallowedTools: Agent)")
            rows.append({
                "file": str(f.relative_to(root)) if f.is_relative_to(root) else str(f),
                "name": fm.get("name", f.stem),
                "model": model or "(unset)",
                "effort": effort or "(default)",
                "tools": tools or "(all)",
                "flags": flags,
            })
    return rows


def family(model: str) -> str:
    low = model.lower()
    return next((f for f in FAMILIES if f in low), "")


def read_jsonl(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open(encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except ValueError:
                continue
    return rows


def spawn_inputs(files: list[Path]) -> dict[str, dict]:
    """tool_use id -> input of every Agent or Task spawn found in these transcripts."""
    spawns: dict[str, dict] = {}
    for f in files:
        for row in read_jsonl(f):
            msg = row.get("message") if isinstance(row.get("message"), dict) else {}
            for part in msg.get("content") or []:
                if isinstance(part, dict) and part.get("type") == "tool_use" and part.get("name") in ("Agent", "Task"):
                    spawns[part.get("id", "")] = part.get("input") or {}
    return spawns


def audit(root: Path, transcripts: Path, all_sessions: bool, configured: dict[str, str]) -> tuple[list[dict], str]:
    if not transcripts.is_dir():
        return [], f"transcripts folder not found: {transcripts}"
    sessions = sorted((p for p in transcripts.glob("*.jsonl")), key=lambda p: p.stat().st_mtime, reverse=True)
    if not sessions:
        return [], f"no session transcripts in {transcripts}"
    if not all_sessions:
        sessions = sessions[:1]
    rows: list[dict] = []
    for main_file in sessions:
        sub_dir = main_file.with_suffix("") / "subagents"
        sub_files = sorted(sub_dir.glob("agent-*.jsonl")) if sub_dir.is_dir() else []
        spawns = spawn_inputs([main_file, *sub_files])
        for sf in sub_files:
            meta_path = sf.with_name(sf.name[: -len(".jsonl")] + ".meta.json")
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.is_file() else {}
            except (OSError, ValueError):
                meta = {}
            agent_type = meta.get("agentType", "?")
            requested = (spawns.get(meta.get("toolUseId", "")) or {}).get("model", "")
            short = agent_type.split(":")[-1]
            conf = configured.get(agent_type) or configured.get(short) or ""
            served: list[str] = []
            efforts: list[str] = []
            for row in read_jsonl(sf):
                if row.get("type") != "assistant":
                    continue
                model = (row.get("message") or {}).get("model", "")
                if model and not model.startswith("<") and model not in served:
                    served.append(model)
                eff = row.get("effort")
                if eff and eff not in efforts:
                    efforts.append(str(eff))
            expected = requested or (conf if conf and conf != "inherit" else "")
            flags: list[str] = []
            if requested and conf and conf != "inherit" and family(requested) != family(conf):
                flags.append(f"spawn parameter '{requested}' overrode frontmatter '{conf}'")
            if expected and served and family(expected) and any(family(m) != family(expected) for m in served):
                flags.append(f"served {', '.join(served)} but {expected} was expected")
            if not served:
                flags.append("no served model found in the transcript")
            if not expected and agent_type in ("general-purpose", "?"):
                flags.append("unnamed spawn without an explicit model (inherited)")
            rows.append({
                "session": main_file.stem[:8], "agent": agent_type, "description": meta.get("description", ""),
                "requested": requested or "-", "configured": conf or "-", "served": ", ".join(served) or "-",
                "effort": ", ".join(efforts) or "-", "depth": meta.get("spawnDepth", "?"), "flags": flags,
            })
    return rows, ""


def print_audit(rows: list[dict]) -> None:
    head = ("session", "agent", "requested", "configured", "served", "effort")
    widths = [max(len(h), *(len(str(r[h])) for r in rows)) if rows else len(h) for h in head]
    print("  ".join(h.ljust(w) for h, w in zip(head, widths)))
    for r in rows:
        print("  ".join(str(r[h]).ljust(w) for h, w in zip(head, widths)) + (f"  # {r['description'][:50]}" if r["description"] else ""))
        for fl in r["flags"]:
            print(f"    ! {fl}")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="project root (default: current directory)")
    ap.add_argument("--dir", action="append", help="agent directory to scan (repeatable)")
    ap.add_argument("--strict", action="store_true", help="exit 1 when any agent is flagged")
    ap.add_argument("--json", action="store_true", help="print JSON")
    ap.add_argument("--audit", action="store_true", help="requested vs configured vs served model per subagent")
    ap.add_argument("--all", action="store_true", help="with --audit: every session, not only the latest")
    ap.add_argument("--transcripts", help="with --audit: transcripts folder")
    args = ap.parse_args(argv)

    root = Path(args.root).resolve()
    dirs = [Path(d) if Path(d).is_absolute() else root / d for d in (args.dir or [".claude/agents", "agents"])]
    seen: set[Path] = set()
    unique_dirs = []
    for d in dirs:
        r = d.resolve()
        if r not in seen:
            seen.add(r)
            unique_dirs.append(d)
    rows = scan(unique_dirs, root)
    settings = read_settings(root)

    if args.audit:
        configured = {r["name"]: r["model"] for r in rows if r["model"] != "(unset)"}
        tdir = Path(args.transcripts) if args.transcripts else (
            Path.home() / ".claude" / "projects" / re.sub(r"[^A-Za-z0-9]", "-", str(root)))
        audit_rows, err = audit(root, tdir, args.all, configured)
        if err:
            print(f"COULD NOT RUN: {err}")
            print(CANNOT_COVER_AUDIT)
            return 2
        if args.json:
            print(json.dumps({"audit": audit_rows}, indent=2))
        else:
            print_audit(audit_rows)
        flagged = sum(1 for r in audit_rows if r["flags"])
        if not args.json:
            print(f"\n{'FLAGGED' if flagged else 'OK'}: {len(audit_rows)} subagent run(s), {flagged} flagged")
            print(CANNOT_COVER_AUDIT)
        return 1 if (args.strict and flagged) else 0

    if args.json:
        print(json.dumps({"agents": rows, "settings": settings}, indent=2))
    else:
        if not rows:
            print("no agent files found in: " + ", ".join(str(d) for d in unique_dirs))
        else:
            w = max(len(r["name"]) for r in rows)
            print(f"{'agent'.ljust(w)}  {'model'.ljust(8)}  {'effort'.ljust(9)}  tools")
            for r in rows:
                print(f"{r['name'].ljust(w)}  {r['model'].ljust(8)}  {r['effort'].ljust(9)}  {r['tools']}")
                for fl in r["flags"]:
                    print(f"{' ' * w}  ! {fl}")
        print()
        print("settings:")
        for k in ("model", "advisorModel", "autoCompactWindow", "effortLevel"):
            if k in settings:
                print(f"  {k}: {settings[k]} ({settings['source'][k]})")
        if settings["env"]:
            for k, v in sorted(settings["env"].items()):
                pin = "  <- pin: drop when the alias catches up" if k.startswith("ANTHROPIC_DEFAULT_") else ""
                print(f"  env {k}: {v}{pin}")
        else:
            print("  no model env pins")
        if "CLAUDE_CODE_SUBAGENT_MODEL_FORCE" in settings["env"]:
            print("  ! CLAUDE_CODE_SUBAGENT_MODEL_FORCE is set: agent model frontmatter is ignored")
        for e in settings.get("errors", []):
            print(f"  ! cannot read {e}")
    flagged = sum(1 for r in rows if r["flags"])
    if not args.json:
        print(f"\n{len(rows)} agent(s), {flagged} flagged")
        print(CANNOT_COVER_LIST)
    if not rows:
        return 2
    return 1 if (args.strict and flagged) else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 (an unexpected crash is "could not run", never "fail")
        print(f"COULD NOT RUN: unexpected error: {exc!r}")
        print(CANNOT_COVER_LIST)
        sys.exit(2)
