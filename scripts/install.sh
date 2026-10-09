#!/usr/bin/env bash
# Ads Master project installer.
# Copies the agents and skills into a project's .claude/ folder and creates the
# ads-master/ workspace. Safe to re-run: the workspace is never overwritten.
#
# Usage:
#   scripts/install.sh <project-dir> [--pack name] [--only slug1,slug2] [--kit workflow] [--update] [--no-workspace] [--no-hooks] [--dry-run]
#
#   --pack          Install a pack from docs/packs.json (ecommerce-dtc, marketplace-seller, lead-gen-local,
#                   b2b-saas, mobile-app, ai-visibility, full). Core is always included.
#   --only          Install hand picked agents (comma separated). Combines with --pack. Core is always included.
#   --kit           Also install a kit from kits/ (for example: workflow).
#   --update        Overwrite existing agent and skill files with this version (workspace untouched).
#   --no-workspace  Do not create ads-master/ (use when you will run the ads-setup skill later).
#   --no-hooks      Do not install the guardrail hooks into .claude/settings.json (not recommended).
#   --dry-run       Print what would happen.

set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET=""
ONLY=""
PACK=""
KITS=""
UPDATE=0
WORKSPACE=1
HOOKS=1
DRY=0

while [[ $# -gt 0 ]]; do
  case "$1" in
    --only) ONLY="$2"; shift 2 ;;
    --pack) PACK="$2"; shift 2 ;;
    --kit) KITS="$KITS $2"; shift 2 ;;
    --update) UPDATE=1; shift ;;
    --no-workspace) WORKSPACE=0; shift ;;
    --no-hooks) HOOKS=0; shift ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) sed -n '2,19p' "$0"; exit 0 ;;
    *) TARGET="$1"; shift ;;
  esac
done

if [[ -z "$TARGET" ]]; then
  echo "Usage: scripts/install.sh <project-dir> [--pack name] [--only a,b] [--kit workflow] [--update] [--no-workspace] [--no-hooks] [--dry-run]" >&2
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

ALL_AGENTS="$(cd "$SRC/agents" && ls *.md | sed 's/\.md$//')"
pack_members() {
  python3 - "$SRC/docs/packs.json" "$1" <<'PY'
import json, sys
packs = json.load(open(sys.argv[1]))
name = sys.argv[2]
if name not in packs or name.startswith("_"):
    sys.exit("unknown pack: " + name + " (choose from " + ", ".join(k for k in packs if not k.startswith("_")) + ")")
core = packs["core"]
items = core.get("agents", []) + core.get("skills", [])
if name != "core":
    items += packs[name].get("agents", [])
print(" ".join(items))
PY
}
ALWAYS="$(pack_members core)"

if [[ -n "$PACK" && "$PACK" == "full" ]]; then
  SELECTED="$ALL_AGENTS $ALWAYS"
elif [[ -n "$PACK" || -n "$ONLY" ]]; then
  SELECTED="$ALWAYS"
  if [[ -n "$PACK" ]]; then SELECTED="$SELECTED $(pack_members "$PACK")"; fi
  if [[ -n "$ONLY" ]]; then SELECTED="$SELECTED $(echo "$ONLY" | tr ',' ' ')"; fi
else
  SELECTED="$ALL_AGENTS $ALWAYS"
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

for kit in $KITS; do
  KDIR="$SRC/kits/$kit"
  [[ -d "$KDIR" ]] || KDIR="$SRC/kits/$kit-kit"
  if [[ ! -d "$KDIR" ]]; then echo "warning: unknown kit '$kit'" >&2; continue; fi
  for f in "$KDIR"/agents/*.md; do
    [[ -f "$f" ]] && copy_item "$f" "$TARGET/.claude/agents/$(basename "$f")"
  done
  for d in "$KDIR"/skills/*/; do
    [[ -d "$d" ]] && copy_item "${d%/}" "$TARGET/.claude/skills/$(basename "$d")"
  done
  for extra in scripts templates; do
    if [[ -d "$KDIR/$extra" ]]; then
      run "mkdir -p '$TARGET/.claude/$(basename "$KDIR")'"
      copy_item "$KDIR/$extra" "$TARGET/.claude/$(basename "$KDIR")/$extra"
    fi
  done
  if [[ -f "$KDIR/templates/workflow-kit.json" && ! -f "$TARGET/workflow-kit.json" ]]; then
    copy_item "$KDIR/templates/workflow-kit.json" "$TARGET/workflow-kit.json"
  fi
  if [[ -f "$KDIR/templates/settings-snippet.json" ]]; then
    if [[ $DRY -eq 1 ]]; then
      echo "[dry-run] merge $(basename "$KDIR") settings snippet into .claude/settings.json (missing keys only)"
    else
      python3 - "$KDIR/templates/settings-snippet.json" "$TARGET/.claude/settings.json" <<'PY'
import json, os, sys
snippet_path, path = sys.argv[1], sys.argv[2]
with open(snippet_path, encoding="utf-8") as fh:
    snippet = json.load(fh)
try:
    with open(path, encoding="utf-8") as fh:
        settings = json.load(fh)
except FileNotFoundError:
    settings = {}
added = []
for key, val in snippet.items():
    if key.startswith("//"):
        continue
    if isinstance(val, dict):
        cur = settings.setdefault(key, {})
        for k, v in val.items():
            if isinstance(v, str) and "<" in v:
                continue  # placeholder: the project decides
            if k not in cur:
                cur[k] = v
                added.append(f"{key}.{k}")
        if not cur:
            settings.pop(key)
    elif key not in settings:
        settings[key] = val
        added.append(key)
os.makedirs(os.path.dirname(path), exist_ok=True)
with open(path, "w", encoding="utf-8") as fh:
    json.dump(settings, fh, indent=2)
    fh.write("\n")
print("settings: added " + (", ".join(added) if added else "nothing (keys already set)"))
PY
    fi
  fi
  echo "kit installed: $(basename "$KDIR")"
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
    "PostToolUse": ("^(Bash|Write|Edit|MultiEdit|NotebookEdit)$|^mcp__.*", "post"),
    "Stop": (None, "stop"),
}
hooks = settings.setdefault("hooks", {})
for event, (matcher, sub) in wanted.items():
    groups = hooks.setdefault(event, [])
    existing = [g for g in groups if any("ads-master-guard.py" in h.get("command", "") for h in g.get("hooks", []))]
    if existing:
        for g in existing:
            if matcher:
                g["matcher"] = matcher
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
