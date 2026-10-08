#!/usr/bin/env bash
# Ads Master project installer.
# Copies the agents and skills into a project's .claude/ folder and creates the
# ads-master/ workspace. Safe to re-run: the workspace is never overwritten.
#
# Usage:
#   scripts/install.sh <project-dir> [--only slug1,slug2] [--update] [--no-workspace] [--no-hooks] [--dry-run]
#
#   --only          Install a subset of agents (utility skills and the orchestrator are always included).
#   --update        Overwrite existing agent and skill files with this version (workspace untouched).
#   --no-workspace  Do not create ads-master/ (use when you will run the ads-setup skill later).
#   --no-hooks      Do not install the guardrail hooks into .claude/settings.json (not recommended).
#   --dry-run       Print what would happen.

set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET=""
ONLY=""
UPDATE=0
WORKSPACE=1
HOOKS=1
DRY=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --only) ONLY="$2"; shift 2 ;;
    --update) UPDATE=1; shift ;;
    --no-workspace) WORKSPACE=0; shift ;;
    --no-hooks) HOOKS=0; shift ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) sed -n '2,16p' "$0"; exit 0 ;;
    *) TARGET="$1"; shift ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo "Usage: scripts/install.sh <project-dir> [--only a,b] [--update] [--no-workspace] [--dry-run]" >&2
  exit 1
fi
if [[ ! -d "$TARGET" ]]; then
  echo "Target directory not found: $TARGET" >&2
  exit 1
fi
TARGET="$(cd "$TARGET" && pwd)"
if [[ "$TARGET" == "$SRC" ]]; then
  echo "Target is the Ads Master repo itself. Open this repo in Claude Code instead (agents load from .claude/)." >&2
  exit 1
fi

run() {
  if [[ $DRY -eq 1 ]]; then echo "[dry-run] $*"; else eval "$@"; fi
}

ALWAYS="growth-orchestrator measurement ads-setup ads-review"
ALL_AGENTS="$(cd "$SRC/agents" && ls *.md | sed 's/\.md$//')"

if [[ -n "$ONLY" ]]; then
  SELECTED="$(echo "$ONLY" | tr ',' ' ') $ALWAYS"
else
  SELECTED="$ALL_AGENTS ads-setup ads-review"
fi
SELECTED="$(echo $SELECTED | tr ' ' '\n' | sort -u | tr '\n' ' ')"

run "mkdir -p '$TARGET/.claude/agents' '$TARGET/.claude/skills'"

copy_item() {
  local src="$1" dst="$2"
  if [[ -e "$dst" && $UPDATE -eq 0 ]]; then
    echo "skip (exists, use --update): ${dst#$TARGET/}"
    return
  fi
  run "rm -rf '$dst'"
  run "cp -R '$src' '$dst'"
  echo "installed: ${dst#$TARGET/}"
}

for slug in $SELECTED; do
  if [[ -f "$SRC/agents/$slug.md" ]]; then
    copy_item "$SRC/agents/$slug.md" "$TARGET/.claude/agents/$slug.md"
  fi
  if [[ -d "$SRC/skills/$slug" ]]; then
    copy_item "$SRC/skills/$slug" "$TARGET/.claude/skills/$slug"
  fi
  if [[ ! -f "$SRC/agents/$slug.md" && ! -d "$SRC/skills/$slug" ]]; then
    echo "warning: unknown slug '$slug'" >&2
  fi
done

if [[ $WORKSPACE -eq 1 ]]; then
  TEMPLATE="$SRC/skills/ads-setup/template"
  run "mkdir -p '$TARGET/ads-master'"
  # Never overwrite files the project already has.
  if command -v rsync >/dev/null 2>&1; then
    run "rsync -a --ignore-existing '$TEMPLATE/' '$TARGET/ads-master/'"
  else
    run "cp -Rn '$TEMPLATE/.' '$TARGET/ads-master/' 2>/dev/null || true"
  fi
  echo "workspace ready: ads-master/ (existing files kept)"
fi

if [[ $HOOKS -eq 1 ]]; then
  run "mkdir -p '$TARGET/.claude/hooks'"
  run "cp '$SRC/scripts/guard.py' '$TARGET/.claude/hooks/ads-master-guard.py'"
  if [[ $DRY -eq 1 ]]; then
    echo "[dry-run] merge Ads Master hooks into .claude/settings.json"
  else
    python3 - "$TARGET/.claude/settings.json" <<'PY'
import json, os, sys
path = sys.argv[1]
try:
    with open(path, encoding="utf-8") as fh:
        settings = json.load(fh)
except FileNotFoundError:
    settings = {}
guard = 'python3 "${CLAUDE_PROJECT_DIR}/.claude/hooks/ads-master-guard.py"'
wanted = {
    "SessionStart": ("startup|resume|clear|compact", "session-start"),
    "PreToolUse": ("^(Bash|Write|Edit|MultiEdit|NotebookEdit)$|^mcp__.*", "pre"),
    "PostToolUse": ("^Bash$|^mcp__.*", "post"),
    "Stop": (None, "stop"),
}
hooks = settings.setdefault("hooks", {})
for event, (matcher, sub) in wanted.items():
    groups = hooks.setdefault(event, [])
    if any("ads-master-guard.py" in h.get("command", "") for g in groups for h in g.get("hooks", [])):
        continue
    group = {"hooks": [{"type": "command", "command": f"{guard} {sub}", "timeout": 10}]}
    if matcher:
        group = {"matcher": matcher, **group}
    groups.append(group)
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    json.dump(settings, fh, indent=2)
    fh.write("\n")
print("hooks: Ads Master guard registered in .claude/settings.json")
PY
  fi
fi

echo
echo "Done. Next steps:"
echo "  1. cd '$TARGET' && claude"
echo "  2. Run /ads-setup to scan the codebase and fill ads-master/PROJECT_BRIEF.md"
echo "  3. Ask: \"Run a full growth audit\" (the growth-orchestrator skill takes it from there)"
