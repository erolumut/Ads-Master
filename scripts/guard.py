#!/usr/bin/env python3
"""Ads Master guard: the deterministic safety layer for Claude Code hooks.

Subcommands (one per hook event):
  pre            PreToolUse: classify the tool call into gates G0 to G4 and allow,
                 ask or deny according to ads-master/guardrails.json.
  post           PostToolUse: append write attempts to the audit log.
  stop           Stop: ask for a session report when writes happened this session.
  session-start  SessionStart: inject the project's automation stage and caps.

The guard only acts inside projects that have an ads-master/ workspace. Anywhere
else it exits silently, so a globally installed plugin never gets in the way of
unrelated work. It uses only the Python standard library.

Fail policy: unexpected errors exit 0 with no output (the normal permission
flow still applies). Gate decisions never depend on network calls.
"""
import datetime
import json
import os
import re
import sys

WORKSPACE = "ads-master"
DEFAULT_POLICY = {
    "automation_stage": 1,
    "currency": "",
    "caps": {
        "daily_budget_per_campaign": None,
        "daily_spend_per_account": None,
        "max_budget_increase_pct": 0,
    },
    "gates": {
        "G2_prepare": "ask",
        "G3_commit": "ask",
        "G4_forbidden": "deny",
        "unknown_write": "ask",
    },
    "required_create_status": "PAUSED",
    "auto_actions": [],
    "protect_paths": ["ads-master/guardrails.json", "ads-master/GUARDRAILS.md"],
    "extra_blocked_bash_patterns": [],
    "extra_ask_bash_patterns": [],
    "log_actions": True,
    "log_path": "ads-master/logs/actions.jsonl",
    "review_hints": True,
}

# Path pattern -> (reviewer, why). Advisory only: a PostToolUse hint, once per reviewer per session.
# Override or extend per project with "review_hint_rules": [[regex, reviewer, why], ...] in guardrails.json.
REVIEW_HINT_RULES = [
    (r"\.(liquid|tsx|jsx|vue|svelte|php|astro)$|/(templates|sections|snippets|layout|theme)/",
     "site-engineer", "site or theme code changed: release QA on desktop, phones and in-app browsers before it goes live"),
    (r"(gtm|datalayer|data-layer|pixel|capi|conversion|analytics|tracking|consent)[^/]*$",
     "measurement", "tracking code changed: check events, dedup keys and consent before release"),
    (r"ads-master/outputs/.*(copy|ad|ads|email|sms|landing|listing|creative|script|offer|price)[^/]*\.md$|ads-master/brand/",
     "compliance", "customer facing copy or claims changed: compliance review before publishing"),
    (r"(robots\.txt|sitemap|schema|json-?ld|metadata|hreflang|canonical)",
     "seo", "crawl or structured data files changed: SEO preflight before release"),
    (r"(feed|merchant|catalog)[^/]*\.(xml|csv|tsv|json|txt)$",
     "commerce-feeds", "product feed changed: feed QA and price and availability parity"),
    (r"(price|pricing|tarif)[^/]*\.(csv|json|xlsx|md)$",
     "pricing-strategy", "price file changed: parity check (ad, page, structured data, feed, checkout) and compliance on displayed prices"),
]

# ---------------------------------------------------------------- vocabulary

READ_WORDS = {
    "get", "list", "search", "read", "fetch", "query", "describe", "report",
    "reports", "insights", "insight", "find", "lookup", "count", "download",
    "export", "preview", "validate", "check", "inspect", "view", "analyze",
    "analyse", "summary", "summarize", "stats", "metrics", "estimate",
    "forecast", "suggest", "recommendations", "diagnose", "audit", "show",
    "retrieve", "browse", "explain", "lint", "test", "ping", "whoami", "me",
}
FORBIDDEN_WORDS = {
    "delete", "remove", "destroy", "purge", "erase", "drop", "revoke",
    "transfer", "billing", "invoice", "payment", "owner", "ownership",
    "permission", "permissions", "grant", "role", "roles", "unlink",
    "disconnect",
}
COMMIT_WORDS = {
    "activate", "enable", "publish", "launch", "resume", "unpause", "start",
    "send", "submit", "deploy", "go", "live", "bid", "bids", "budget",
    "budgets", "price", "prices", "pricing", "discount", "discounts",
    "shipping", "approve", "release", "schedule", "pause", "stop", "disable",
    "apply", "mutate", "increase", "decrease", "raise", "lower", "spend",
}
PREPARE_WORDS = {
    "create", "add", "new", "draft", "upload", "duplicate", "copy", "clone",
    "push", "save", "import", "sync", "attach", "generate", "build", "stage",
}
MEDIA_WORDS = {"image", "images", "video", "videos", "asset", "assets", "creative",
               "creatives", "media", "file", "files", "thumbnail", "library"}
CHANGE_WORDS = {"update", "set", "edit", "modify", "patch", "put", "post",
                "change", "adjust", "write", "replace", "rename", "move",
                "assign", "configure", "run", "execute", "call", "invoke"}

BUDGET_KEYS = re.compile(
    r"(daily_budget|lifetime_budget|budget_amount|budget|amount_micros|"
    r"spend_cap|spending_limit|bid_amount|bid_cap|cpa_bid|target_cpa|"
    r"target_roas|price|compare_at_price)", re.I)

SECRET_PATTERNS = [
    re.compile(r"EAA[A-Za-z0-9]{40,}"),                    # Meta access token
    re.compile(r"shp(at|ca|pa|ss)_[a-fA-F0-9]{32}"),       # Shopify
    re.compile(r"sk-ant-[A-Za-z0-9_\-]{20,}"),             # Anthropic
    re.compile(r"sk-(proj-)?[A-Za-z0-9_\-]{32,}"),         # OpenAI style
    re.compile(r"AIza[0-9A-Za-z_\-]{35}"),                 # Google API key
    re.compile(r"ya29\.[0-9A-Za-z_\-]{30,}"),              # Google OAuth
    re.compile(r"1//0[0-9A-Za-z_\-]{30,}"),                # Google refresh token
    re.compile(r"AKIA[0-9A-Z]{16}"),                       # AWS key id
    re.compile(r"(sk|rk)_live_[0-9a-zA-Z]{20,}"),          # Stripe
    re.compile(r"xox[baprs]-[0-9A-Za-z\-]{10,}"),          # Slack
    re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}"),             # GitHub
    re.compile(r"-----BEGIN (RSA |EC |OPENSSH |)PRIVATE KEY-----"),
]

AD_API_HOSTS = re.compile(
    r"(graph\.facebook\.com|graph\.instagram\.com|googleads\.googleapis\.com|"
    r"business-api\.tiktok\.com|api\.linkedin\.com|bingads\.microsoft\.com|"
    r"campaign\.api\.bingads|api\.ads\.openai\.com|ads-api\.openai\.com|"
    r"merchantapi\.googleapis\.com|shoppingcontent\.googleapis\.com|"
    r"myshopify\.com/admin|a\.klaviyo\.com/api|api\.searchads\.apple\.com|"
    r"api\.appstoreconnect\.apple\.com|androidpublisher\.googleapis\.com)", re.I)

BASH_RULES = [
    # (gate, pattern, reason). Order: G4, then G3, then G2. First match wins.
    ("G4", r"\bshopify\s+theme\s+delete\b", "Deleting a Shopify theme"),
    ("G4", r"\bshopify\s+store\s+delete\b", "Deleting a Shopify store resource"),
    ("G4", r"curl\b[^|;&]*-X\s*DELETE\b[^|;&]*", "HTTP DELETE call"),
    ("G4", r"\brm\s+-[a-zA-Z]*r[a-zA-Z]*\s+[^|;&]*\bads-master\b", "Removing the ads-master workspace"),
    ("G4", r"\bwp\b[^|;&]*\bdb\s+(drop|reset)\b", "Dropping or resetting a WordPress database"),
    ("G3", r"\bshopify\s+theme\s+publish\b", "Publishing a Shopify theme"),
    ("G3", r"\bshopify\s+theme\s+push\b[^|;&]*(--live|--allow-live|--publish|\s-l\b|\s-a\b|\s-p\b)", "Pushing to or publishing the live Shopify theme"),
    ("G3", r"\bshopify\s+theme\s+dev\b[^|;&]*(--allow-live\b|\s-a\b)", "Developing against the live Shopify theme"),
    ("G3", r"\bshopify\s+store\s+(bulk\s+)?execute\b[^|;&]*--allow-mutations\b", "Running mutations against a Shopify store"),
    ("G3", r"\bSHOPIFY_FLAG_(PUBLISH|LIVE|ALLOW_LIVE|ALLOW_MUTATIONS)\w*\s*=", "Shopify CLI flag set through the environment"),
    ("G3", r"\bvercel\b[^|;&]*(--prod\b|\s--production\b|\spromote\b|\srollback\b|\srolling-release\b)", "Production deploy, promote or rollback (Vercel)"),
    ("G3", r"\bnetlify\s+deploy\b[^|;&]*--prod\b", "Production deploy (Netlify)"),
    ("G3", r"\bnetlify\s+api\s+restoreSiteDeploy\b", "Restoring a published Netlify deploy"),
    ("G3", r"\bfirebase\s+deploy\b", "Firebase deploy"),
    ("G3", r"\bwrangler\s+(deploy|publish)\b", "Cloudflare deploy"),
    ("G3", r"\bfastlane\s+(deliver|supply|pilot)\b", "App store submission"),
    ("G3", r"\bwp\s+(@(prod|production|live)\b|[^|;&]*--ssh=)[^|;&]*\b(update|create|delete|install|activate|deactivate|import|search-replace|set|add|remove|generate)\b", "Write command against production or remote WordPress"),
    ("G3", r"\bgit\s+push\b[^|;&]*\b(origin\s+)?(main|master|production|live)\b", "Push to a production branch"),
    ("G3", r"(status\W{1,4}ACTIVE|\"status\"\s*:\s*\"ENABLED\"|effective_status=ACTIVE)", "Setting an entity live"),
    ("ASK_EXTRA", None, None),
    ("G2", r"\bshopify\s+theme\s+push\b[^|;&]*(--unpublished|--development|\s-u\b|\s-d\b)", "Pushing an unpublished or development Shopify theme"),
    ("G3", r"\bshopify\s+theme\s+push\b", "Pushing to an existing Shopify theme (could be the live one)"),
    ("G2", r"\bshopify\s+theme\s+(duplicate|share)\b", "Creating a theme copy in the library"),
    ("G2", r"\bnetlify\s+deploy\b", "Preview deploy (Netlify)"),
    ("G2", r"\bvercel\b(\s+deploy)?\b", "Preview deploy"),
]


# ---------------------------------------------------------------- helpers

def is_workspace(path):
    ws = os.path.join(path, WORKSPACE)
    return os.path.isfile(os.path.join(ws, "guardrails.json")) or os.path.isfile(os.path.join(ws, "PROJECT_BRIEF.md"))


def project_dir(event):
    """Return the project root that holds an Ads Master workspace, or None.

    CLAUDE_PROJECT_DIR is authoritative when set. Without it, walk up from cwd a
    few levels. A folder only counts when ads-master/ holds guardrails.json or
    PROJECT_BRIEF.md, so a clone of the Ads Master repo named ads-master in a
    parent folder is never mistaken for a workspace.
    """
    env_root = os.environ.get("CLAUDE_PROJECT_DIR")
    if env_root:
        root = os.path.abspath(env_root)
        return root if is_workspace(root) else None
    cur = os.path.abspath(event.get("cwd") or os.getcwd())
    for _ in range(4):
        if is_workspace(cur):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return None


def load_policy(root):
    policy = json.loads(json.dumps(DEFAULT_POLICY))
    path = os.path.join(root, WORKSPACE, "guardrails.json")
    try:
        with open(path, encoding="utf-8") as fh:
            user = json.load(fh)
    except (OSError, ValueError):
        return policy, False
    for key, val in user.items():
        if isinstance(val, dict) and isinstance(policy.get(key), dict):
            policy[key].update(val)
        else:
            policy[key] = val
    return policy, True


def words(name):
    name = re.sub(r"([a-z])([A-Z])", r"\1_\2", name)
    return [w for w in re.split(r"[^A-Za-z0-9]+", name.lower()) if w]


def redact(text):
    for pat in SECRET_PATTERNS:
        text = pat.sub("[REDACTED]", text)
    text = re.sub(r"(access_token|token|secret|password|api_key)=([^&\s\"']+)", r"\1=[REDACTED]", text, flags=re.I)
    return text


def short(obj, limit=300):
    try:
        text = obj if isinstance(obj, str) else json.dumps(obj, ensure_ascii=False, sort_keys=True)
    except (TypeError, ValueError):
        text = str(obj)
    text = redact(text)
    return text if len(text) <= limit else text[:limit] + "..."


def to_number(val):
    try:
        return float(str(val).replace(",", "").strip())
    except ValueError:
        return None


def budget_values(tool_input):
    """Yield (key, value) pairs for budget like fields anywhere in the input."""
    stack = [tool_input]
    while stack:
        cur = stack.pop()
        if isinstance(cur, dict):
            for k, v in cur.items():
                if isinstance(v, (dict, list)):
                    stack.append(v)
                elif BUDGET_KEYS.search(str(k)):
                    num = to_number(v)
                    if num is not None:
                        yield k, num
        elif isinstance(cur, list):
            stack.extend(cur)


def over_cap(tool_input, policy, tool_name=""):
    """Return a reason when a budget value clearly exceeds the campaign cap."""
    cap = policy.get("caps", {}).get("daily_budget_per_campaign")
    if not cap:
        return None
    budget_tool = "budget" in tool_name.lower()
    for key, num in budget_values(tool_input):
        k = str(key).lower()
        if "budget" not in k and not (budget_tool and k.endswith("amount_micros")):
            continue
        if k.endswith("_micros"):
            major = num / 1_000_000
            if major > cap:
                return f"{key}={major:g} exceeds the cap of {cap}"
            continue
        # Units are ambiguous (major vs minor units, e.g. Meta uses cents).
        # Deny only when the value exceeds the cap under both readings.
        if num > cap and num / 100 > cap:
            return f"{key}={num:g} exceeds the cap of {cap} in both major and minor units"
    return None


def wants_active(tool_input):
    text = json.dumps(tool_input, default=str).lower()
    return bool(re.search(r"\"(status|effective_status|configured_status)\"\s*:\s*\"(active|enabled|live|published)\"", text))


def declares_paused(tool_name, tool_input):
    text = (tool_name + " " + json.dumps(tool_input, default=str)).lower()
    return bool(re.search(r"paused|\"status\"\s*:\s*\"(paused|draft)\"|unpublished|development|draft", text))


# ---------------------------------------------------------------- classify

def classify_mcp(tool_name, tool_input, policy):
    parts = tool_name.split("__", 2)
    op = parts[2] if len(parts) == 3 else tool_name
    ws = set(words(op))
    if not ws or (ws & READ_WORDS and not ws & (FORBIDDEN_WORDS | COMMIT_WORDS | PREPARE_WORDS | CHANGE_WORDS)):
        return "G0", "read operation"
    if ws & FORBIDDEN_WORDS:
        return "G4", "destructive, billing or ownership operation"
    reason = over_cap(tool_input, policy, tool_name)
    if reason:
        return "G4", reason
    if wants_active(tool_input):
        return "G3", "sets an entity live"
    if ws & PREPARE_WORDS and not ws & COMMIT_WORDS and declares_paused(tool_name, tool_input):
        return "G2", "creates or uploads a paused or draft object"
    if "upload" in ws and ws & MEDIA_WORDS and not ws & COMMIT_WORDS:
        return "G2", "uploads a media asset to a library (no delivery)"
    if ws & COMMIT_WORDS or any(True for _ in budget_values(tool_input)):
        return "G3", "changes spend, prices, status or reaches customers"
    if ws & PREPARE_WORDS:
        return "G3", "creates an object without declaring it paused or draft"
    if ws & CHANGE_WORDS:
        return "G3", "modifies a live object"
    if ws & READ_WORDS:
        return "G0", "read operation"
    return "UNKNOWN", "operation not recognized"


def classify_bash(command, policy):
    for pat in policy.get("extra_blocked_bash_patterns", []):
        if re.search(pat, command, re.I):
            return "G4", "matches a blocked pattern in guardrails.json"
    for gate, pat, reason in BASH_RULES:
        if gate == "ASK_EXTRA":
            # Project specific ask patterns run before the built in G2 rules.
            for extra in policy.get("extra_ask_bash_patterns", []):
                if re.search(extra, command, re.I):
                    return "G3", "matches an ask pattern in guardrails.json"
            continue
        if re.search(pat, command, re.I):
            return gate, reason
    if AD_API_HOSTS.search(command):
        if re.search(r"(-X\s*(POST|PUT|PATCH)|--data|-d\s|-F\s|--form|--request\s+(POST|PUT|PATCH))", command, re.I):
            if re.search(r"status\W{1,4}(ACTIVE|ENABLED)", command, re.I):
                return "G3", "API call that sets an entity live"
            if re.search(r"status\W{1,4}PAUSED", command, re.I):
                return "G2", "API call that creates or edits a paused object"
            return "G3", "write call to an ad, commerce or messaging API"
        return "G0", "read call to an ad or commerce API"
    return None, None


def check_write(tool_name, tool_input, root, policy):
    path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
    rel = os.path.relpath(os.path.abspath(path), root) if path else ""
    content = ""
    for key in ("content", "new_string", "new_source"):
        if isinstance(tool_input.get(key), str):
            content += tool_input[key]
    for edit in tool_input.get("edits", []) or []:
        if isinstance(edit, dict) and isinstance(edit.get("new_string"), str):
            content += edit["new_string"]
    base = os.path.basename(path)
    if content and not (base == ".env" or (base.startswith(".env.") and not base.endswith(".example"))):
        for pat in SECRET_PATTERNS:
            if pat.search(content):
                return "deny", f"Content looks like a secret ({pat.pattern[:24]}...). Secrets belong in .env or a secret manager, never in files Claude writes."
    for protected in policy.get("protect_paths", []):
        if rel.replace(os.sep, "/") == protected:
            return "ask", f"{protected} is the project's safety policy. Agents must not relax it on their own; a human confirms this edit."
    return None, None


# ---------------------------------------------------------------- decide

def decide(gate, policy, auto_ok=False):
    stage = int(policy.get("automation_stage", 1) or 1)
    gates = policy.get("gates", {})
    if gate == "G4":
        return gates.get("G4_forbidden", "deny") if gates.get("G4_forbidden") in ("deny", "ask") else "deny"
    if gate == "G2":
        if stage < 2:
            return "deny"
        return gates.get("G2_prepare", "ask")
    if gate == "G3":
        if auto_ok and stage >= 5:
            return "allow"
        if stage < 4:
            return "deny"
        return "ask" if gates.get("G3_commit", "ask") != "deny" else "deny"
    if gate == "UNKNOWN":
        if stage < 2:
            return "ask"
        return gates.get("unknown_write", "ask")
    return None


def stage_hint(gate, policy):
    stage = int(policy.get("automation_stage", 1) or 1)
    if gate == "G2" and stage < 2:
        return " The project is at automation stage 1 (read only): draft a change request in ads-master/ instead, or raise the stage in ads-master/guardrails.json."
    if gate == "G3" and stage < 4:
        return f" The project is at automation stage {stage}: G3 actions (spend, live status, prices, publishing, customer messages) need stage 4. Draft a change request for the human instead."
    if gate == "G4":
        return " G4 actions are never performed by an agent. Ask the human to do it in the platform UI."
    return ""


def log(root, policy, record):
    if not policy.get("log_actions", True):
        return
    path = os.path.join(root, policy.get("log_path") or DEFAULT_POLICY["log_path"])
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "a", encoding="utf-8") as fh:
            fh.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def emit(event_name, decision, reason):
    out = {"hookSpecificOutput": {"hookEventName": event_name,
                                  "permissionDecision": decision,
                                  "permissionDecisionReason": "Ads Master guard: " + reason}}
    sys.stdout.write(json.dumps(out))


# ---------------------------------------------------------------- commands

def cmd_pre(event, root, policy):
    tool = event.get("tool_name", "")
    tinput = event.get("tool_input", {}) or {}
    gate, reason = None, None
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        decision, why = check_write(tool, tinput, root, policy)
        if decision:
            log(root, policy, {"ts": now(), "session": event.get("session_id"), "event": "pre",
                               "tool": tool, "gate": "file", "decision": decision,
                               "reason": why, "target": short(tinput.get("file_path", ""))})
            emit("PreToolUse", decision, why)
        return
    if tool == "Bash":
        gate, reason = classify_bash(tinput.get("command", ""), policy)
    elif tool.startswith("mcp__"):
        gate, reason = classify_mcp(tool, tinput, policy)
    if not gate or gate == "G0":
        return
    auto_ok = any(re.search(p, tool + " " + json.dumps(tinput, default=str), re.I)
                  for p in policy.get("auto_actions", []) if isinstance(p, str))
    decision = decide(gate, policy, auto_ok)
    if decision is None:
        return
    summary = short(tinput.get("command") if tool == "Bash" else tinput)
    log(root, policy, {"ts": now(), "session": event.get("session_id"), "event": "pre",
                       "tool": tool, "gate": gate, "decision": decision,
                       "reason": reason, "input": summary})
    if decision == "allow":
        return
    emit("PreToolUse", decision, f"{gate} ({reason}).{stage_hint(gate, policy)}")


def review_hints(event, root, policy, path):
    if not policy.get("review_hints", True) or not path:
        return None
    rel = os.path.relpath(os.path.abspath(path), root) if os.path.isabs(path) else path
    rel = rel.replace(os.sep, "/")
    if rel.startswith("..") or re.search(r"ads-master/(logs|journal|memory)/", rel):
        return None
    rules = list(REVIEW_HINT_RULES)
    for r in policy.get("review_hint_rules", []) or []:
        if isinstance(r, (list, tuple)) and len(r) == 3:
            rules.append(tuple(r))
    matched = []
    for pattern, reviewer, why in rules:
        try:
            if re.search(pattern, rel, re.I) and reviewer not in [m[0] for m in matched]:
                matched.append((reviewer, why))
        except re.error:
            continue
    if not matched:
        return None
    session = event.get("session_id") or ""
    seen = set()
    logp = os.path.join(root, policy.get("log_path") or DEFAULT_POLICY["log_path"])
    try:
        with open(logp, encoding="utf-8") as fh:
            for line in fh:
                if '"hint"' in line and session and session in line:
                    try:
                        seen.add(json.loads(line).get("reviewer"))
                    except ValueError:
                        pass
    except OSError:
        pass
    fresh = [(r, w) for r, w in matched if r not in seen]
    if not fresh:
        return None
    for r, _ in fresh:
        log(root, policy, {"ts": now(), "session": session, "event": "hint", "reviewer": r, "target": short(rel)})
    lines = "; ".join(f"`{r}` ({w})" for r, w in fresh)
    return (f"Ads Master review hint for {rel}: before calling this done, run {lines}. "
            "Advisory only; shown once per reviewer per session.")


def cmd_post(event, root, policy):
    tool = event.get("tool_name", "")
    tinput = event.get("tool_input", {}) or {}
    if tool in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        hint = review_hints(event, root, policy, tinput.get("file_path") or tinput.get("notebook_path") or "")
        if hint:
            sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                                                 "additionalContext": hint}}))
        return
    if tool == "Bash":
        gate, _ = classify_bash(tinput.get("command", ""), policy)
    elif tool.startswith("mcp__"):
        gate, _ = classify_mcp(tool, tinput, policy)
    else:
        return
    if not gate or gate == "G0":
        return
    resp = event.get("tool_response")
    text = short(resp, 200) if resp is not None else ""
    failed = bool(re.search(r"\b(error|failed|exception|denied|invalid)\b", text, re.I))
    log(root, policy, {"ts": now(), "session": event.get("session_id"), "event": "post",
                       "tool": tool, "gate": gate, "result": "error" if failed else "ok",
                       "input": short(tinput.get("command") if tool == "Bash" else tinput),
                       "response": text})


def cmd_stop(event, root, policy):
    if event.get("stop_hook_active"):
        return
    session = event.get("session_id")
    if not session:
        return
    path = os.path.join(root, policy.get("log_path") or DEFAULT_POLICY["log_path"])
    try:
        with open(path, encoding="utf-8") as fh:
            writes = [json.loads(line) for line in fh if session in line]
    except (OSError, ValueError):
        return
    writes = [w for w in writes if w.get("event") == "post" and w.get("gate") in ("G2", "G3")]
    if not writes:
        return
    reports = os.path.join(root, WORKSPACE, "logs", "session-reports")
    try:
        for name in os.listdir(reports):
            with open(os.path.join(reports, name), encoding="utf-8") as fh:
                if session in fh.read():
                    return
    except OSError:
        pass
    reason = (f"Ads Master guard: this session performed {len(writes)} platform or production write(s). "
              f"Before finishing, write ads-master/logs/session-reports/<YYYY-MM-DD_HHMM>.md with: session id {session}, "
              "what was requested, what changed (object, before, after), approvals used, read-back verification, "
              "open risks, and the next action. Then stop.")
    sys.stdout.write(json.dumps({"decision": "block", "reason": reason}))


def cmd_session_start(event, root, policy):
    stage = policy.get("automation_stage", 1)
    caps = policy.get("caps", {})
    cur = policy.get("currency", "")
    ctx = (f"Ads Master workspace detected at {WORKSPACE}/. Automation stage {stage} "
           f"(1 read only, 2 platform drafts, 3 automated reports, 4 controlled writes, 5 limited automation). "
           f"Caps: daily budget per campaign {caps.get('daily_budget_per_campaign')} {cur}, "
           f"daily spend per account {caps.get('daily_spend_per_account')} {cur}, "
           f"max budget increase {caps.get('max_budget_increase_pct')} percent. "
           "Ads Master hooks enforce gates G0 to G4 from ads-master/guardrails.json. Project facts are in "
           "ads-master/PROJECT_BRIEF.md and the safety policy is in ads-master/GUARDRAILS.md. Project policy: platform "
           "entities are created PAUSED, every write is read back and verified, and G3 actions go through a change "
           "request that a human approves.")
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart",
                                                         "additionalContext": ctx}}))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    try:
        raw = sys.stdin.read()
        event = json.loads(raw) if raw.strip() else {}
        root = project_dir(event)
        if not root:
            return 0
        policy, _ = load_policy(root)
        {"pre": cmd_pre, "post": cmd_post, "stop": cmd_stop,
         "session-start": cmd_session_start}.get(sys.argv[1], lambda *a: None)(event, root, policy)
    except Exception:  # never break a session because of the guard itself
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
