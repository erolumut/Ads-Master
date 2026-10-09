#!/usr/bin/env bash
# Workflow Kit pre-commit dispatcher (review-gates skill).
#
# Validate only: maps staged paths to checks from precommit.json and runs each matching check
# once. It never rewrites, formats or re-stages a file. It refuses staged .env files (anything
# named .env or .env.* except *.example). Agents never bypass it with --no-verify.
#
#   precommit_dispatch.sh [--config precommit.json] [--list]
#     --list   print which checks would run, run nothing
#
# Exit codes: 0 pass, 1 a check failed or a secret file is staged, 2 could not run.
set -u

CANNOT_COVER="This gate cannot cover: unstaged changes, checks missing from precommit.json, behavior that only shows at runtime, and commits made with --no-verify."
config="precommit.json"
list_only=0
while [ $# -gt 0 ]; do
  case "$1" in
    --config) config="$2"; shift 2 ;;
    --list) list_only=1; shift ;;
    -h|--help) sed -n '2,12p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done

could_not_run() {
  echo "COULD NOT RUN: $1"
  echo "$CANNOT_COVER"
  exit 2
}

git rev-parse --git-dir >/dev/null 2>&1 || could_not_run "not inside a git repository"
command -v python3 >/dev/null 2>&1 || could_not_run "python3 not found"
cd "$(git rev-parse --show-toplevel)" || could_not_run "cannot enter the repo root"

staged="$(git diff --cached --name-only --diff-filter=ACMR)"
if [ -z "$staged" ]; then
  echo "OK: nothing staged"
  echo "$CANNOT_COVER"
  exit 0
fi

# 1. Secret files: .env and .env.* are refused, *.example is allowed.
secrets="$(printf '%s\n' "$staged" | grep -E '(^|/)\.env($|\.)' | grep -vE '\.example$' || true)"
if [ -n "$secrets" ]; then
  echo "error staged secret file(s), unstage them (git restore --staged <file>):"
  printf '  %s\n' $secrets
  echo "FAIL: secret files staged"
  echo "$CANNOT_COVER"
  exit 1
fi

[ -f "$config" ] || could_not_run "$config not found (copy templates/precommit.json to the repo root)"

# 2. Map staged paths to checks. Python reads the JSON and does the glob matching.
plan="$(STAGED="$staged" python3 - "$config" <<'PY'
import fnmatch, json, os, re, shlex, sys

def expand(p):
    m = re.search(r"\{([^{}]*)\}", p)
    if not m:
        return [p]
    out = []
    for alt in m.group(1).split(","):
        out += expand(p[:m.start()] + alt + p[m.end():])
    return out

def match(path, pats):
    for pat in pats:
        for p in expand(pat):
            vs = {p, p.replace("**/", "")} if "**/" in p else {p}
            if p == "**" or any(fnmatch.fnmatch(path, v) for v in vs):
                return True
    return False

try:
    checks = json.load(open(sys.argv[1], encoding="utf-8"))["checks"]
except Exception as exc:
    print(f"!cannot parse {sys.argv[1]}: {exc}")
    sys.exit(0)
staged = [s for s in os.environ["STAGED"].splitlines() if s]
for c in checks:
    files = [f for f in staged if match(f, c.get("paths", []))]
    if not files:
        continue
    cmd = c["command"].replace("{files}", " ".join(shlex.quote(f) for f in files))
    print(f"{c.get('name', cmd)}\t{cmd}")
PY
)"
case "$plan" in
  "!"*) could_not_run "${plan#!}" ;;
esac
if [ -z "$plan" ]; then
  echo "OK: no check maps to the staged paths"
  echo "$CANNOT_COVER"
  exit 0
fi

failed=0
unrunnable=0
ran=0
while IFS="$(printf '\t')" read -r name cmd; do
  [ -z "$name" ] && continue
  if [ "$list_only" -eq 1 ]; then
    echo "would run: $name -> $cmd"
    continue
  fi
  case "$cmd" in
    *"<"*">"*) echo "could not run: $name (placeholder command: $cmd)"; unrunnable=$((unrunnable + 1)); continue ;;
  esac
  echo "run: $name"
  bash -c "$cmd"
  code=$?
  ran=$((ran + 1))
  if [ "$code" -eq 1 ]; then
    echo "fail: $name"
    failed=$((failed + 1))
  elif [ "$code" -ne 0 ]; then
    echo "could not run: $name (exit $code)"
    unrunnable=$((unrunnable + 1))
  fi
done <<EOF
$plan
EOF

[ "$list_only" -eq 1 ] && { echo "$CANNOT_COVER"; exit 0; }
if [ "$failed" -gt 0 ]; then
  echo "FAIL: $failed of $ran check(s) failed, $unrunnable could not run"
  echo "$CANNOT_COVER"
  exit 1
fi
if [ "$unrunnable" -gt 0 ]; then
  echo "COULD NOT RUN: $unrunnable check(s); none failed, but a skipped check is not a pass"
  echo "$CANNOT_COVER"
  exit 2
fi
echo "OK: $ran check(s) passed"
echo "$CANNOT_COVER"
exit 0
