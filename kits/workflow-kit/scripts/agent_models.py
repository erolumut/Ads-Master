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

This shows what is CONFIGURED. What actually ran is in the subagent's result or transcript and
in /status; compare the two at sign-off. Standard library only.
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


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="project root (default: current directory)")
    ap.add_argument("--dir", action="append", help="agent directory to scan (repeatable)")
    ap.add_argument("--strict", action="store_true", help="exit 1 when any agent is flagged")
    ap.add_argument("--json", action="store_true", help="print JSON")
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
    return 1 if (args.strict and flagged) else 0


if __name__ == "__main__":
    sys.exit(main())
