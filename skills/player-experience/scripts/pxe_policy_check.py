#!/usr/bin/env python3
"""Check a player experience policy file against the pxe 0.1 format.

The format lives in skills/player-experience/references/policy-format.md. This
checker applies section 5 of that file, with the allowed inputs of section 3 and
the allowed and forbidden action names of section 4.

Fails (exit 1) when:
  - a required section is missing, or modes are missing, duplicated or malformed
  - a rule names a shared mode, names no mode, or names a mode that is not declared
  - a rule input is outside the allowed play signals, or its name contains a
    forbidden token (spend, payer, ad value, device, location, age and so on),
    after lowercasing and removing underscores, hyphens, dots and spaces
  - a rule action is outside the allowed actions, or its name contains a forbidden
    token (force_loss, rig, score_bonus and so on)
  - a difficulty_offset value is outside minOffset and maxOffset, or the offsets are
    wider than two steps either way
  - there are two or more easing rules (negative offset) and one lacks maxPerSession 1
  - a rule lacks a reason or an explainKey
  - player.settings lacks auto or a fixed level, or explain, log or reset is not true
  - scores.modifyAfterFact is true, or assisted runs are allowed on shared boards
  - experiment.holdoutPercent is outside 1 to 20, there is no primary metric, or holdoutSalt is missing
  - the audience includes minors (minimumAge under 18) and minorsTier is not strict
  - the strict tier applies and a return reason has source streak or loss
  - a return reason lacks maxPerDay or quietHours
Warnings: readAfterDays under 28 (or missing), and a policy that eases but never raises.
Exit 2 when the file cannot be read or pxeVersion is missing or not supported.

  python3 -I pxe_policy_check.py policy.json
  python3 -I pxe_policy_check.py policy.json --json

With --json, stdout is one JSON document (findings, verdict and the cannot cover
sentence under "cannotCover"); the sentence is also written to stderr as the last line.

Standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SUPPORTED_VERSIONS = {"0.1"}
CANNOT_COVER = ("This check cannot cover: whether the game code actually follows the file, whether the reason "
                "texts are clear to players, server side or analytics use of data outside this file, and "
                "legal review.")

ALLOWED_INPUTS = ("fail_streak", "attempts_on_level", "fast_solve_streak", "hint_uses_level", "hint_uses_session",
                  "median_move_ms", "restarts_recent", "session_gap_hours", "sessions_today", "skill_rating",
                  "level_rating", "rating_gap", "quit_rate_recent")
OPERATORS = (">=", ">", "<=", "<", "==", "!=")
ALLOWED_ACTIONS = ("difficulty_offset", "offer_hint", "offer_break", "show_next_goal", "suggest_mode")
FORBIDDEN_TOKENS = ("spend", "spent", "purchase", "payer", "paying", "revenue", "ltv", "arpu", "arppu", "whale",
                    "iap", "ad_value", "advalue", "ecpm", "ad_ready", "rewarded_ready", "ad_available", "ad_fill",
                    "monetiz", "price", "device_model", "device_tier", "device_price", "country", "region", "geo",
                    "income", "age", "gender", "health", "mood", "vibration", "battery")
FORBIDDEN_ACTIONS = ("force_loss", "death", "kill", "rig", "score_bonus", "modify_score", "bias_pieces", "harvest")
REQUIRED_SECTIONS = ("policyRevision", "product", "audience", "modes", "difficulty", "player", "rules", "returnReasons",
                     "scores", "experiment")
STRICT_BLOCKED_SOURCES = ("streak", "loss")
MAX_OFFSET_STEPS = 2


def normalize(name: object) -> str:
    """Lowercase and remove underscores, hyphens, dots and spaces."""
    return re.sub(r"[\s_.\-]", "", str(name).lower())


def forbidden_hit(name: object, tokens: tuple[str, ...]) -> str | None:
    """Return the first forbidden token contained in the normalized name, if any."""
    flat = normalize(name)
    for token in tokens:
        if normalize(token) in flat:
            return token
    return None


def is_number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


class Findings:
    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, severity: str, scope: str, message: str) -> None:
        self.items.append({"severity": severity, "scope": scope, "message": message})

    def fail(self, scope: str, message: str) -> None:
        self.add("FAIL", scope, message)

    def warn(self, scope: str, message: str) -> None:
        self.add("WARN", scope, message)

    def count(self, severity: str) -> int:
        return sum(1 for i in self.items if i["severity"] == severity)


def check_modes(policy: dict, out: Findings) -> tuple[set[str], set[str]]:
    modes = policy.get("modes")
    declared: set[str] = set()
    shared: set[str] = set()
    if not isinstance(modes, list) or not modes:
        out.fail("modes", "no modes declared; every rule needs a declared, non shared mode")
        return declared, shared
    for m in modes:
        if not isinstance(m, dict) or not isinstance(m.get("id"), str) or not m["id"]:
            out.fail("modes", f"mode {m!r} needs a string id")
            continue
        if m["id"] in declared:
            out.fail("modes", f"duplicate mode id '{m['id']}'")
        declared.add(m["id"])
        if not isinstance(m.get("shared"), bool):
            out.fail(f"mode {m['id']}", "shared must be true or false")
        elif m["shared"]:
            shared.add(m["id"])
    return declared, shared


def check_difficulty(policy: dict, rules: list, out: Findings) -> tuple[float | None, float | None]:
    diff = policy.get("difficulty")
    uses_offset = any(isinstance(r, dict) and isinstance(r.get("then"), dict)
                      and r["then"].get("action") == "difficulty_offset" for r in rules)
    if not isinstance(diff, dict):
        if uses_offset:
            out.fail("difficulty", "missing, but a rule uses difficulty_offset; minOffset and maxOffset are required")
        return None, None
    lo, hi = diff.get("minOffset"), diff.get("maxOffset")
    if not (is_number(lo) and is_number(hi)):
        if uses_offset or "minOffset" in diff or "maxOffset" in diff:
            out.fail("difficulty", "minOffset and maxOffset must both be numbers")
        return None, None
    if lo > hi:
        out.fail("difficulty", f"minOffset {lo} is above maxOffset {hi}")
    if lo < -MAX_OFFSET_STEPS:
        out.fail("difficulty", f"minOffset {lo} is wider than {MAX_OFFSET_STEPS} steps below the default")
    if hi > MAX_OFFSET_STEPS:
        out.fail("difficulty", f"maxOffset {hi} is wider than {MAX_OFFSET_STEPS} steps above the default")
    return lo, hi


def check_rules(policy: dict, declared: set[str], shared: set[str], out: Findings) -> None:
    rules = policy.get("rules")
    if not isinstance(rules, list):
        out.fail("rules", "rules must be a list")
        return
    lo, hi = check_difficulty(policy, rules, out)
    easing: list[tuple[str, dict]] = []
    raising = 0
    for n, rule in enumerate(rules, 1):
        if not isinstance(rule, dict):
            out.fail(f"rule #{n}", "a rule must be an object")
            continue
        rid = rule["id"] if isinstance(rule.get("id"), str) and rule["id"] else f"#{n}"
        scope = f"rule {rid}"
        if "id" not in rule:
            out.fail(scope, "rule has no id")

        for key in ("reason", "explainKey"):
            if not isinstance(rule.get(key), str) or not rule[key].strip():
                out.fail(scope, f"no {key}; every action needs a reason code and a player facing explanation key")

        rule_modes = rule.get("modes")
        if not isinstance(rule_modes, list) or not rule_modes:
            out.fail(scope, "names no modes")
        else:
            for mid in rule_modes:
                if mid in shared:
                    out.fail(scope, f"names shared mode '{mid}'; shared modes never adapt")
                elif mid not in declared:
                    out.fail(scope, f"names mode '{mid}' that is not declared in modes")

        conditions = rule.get("when")
        if not isinstance(conditions, list) or not conditions:
            out.fail(scope, "when must be a non empty list of conditions")
        else:
            for cond in conditions:
                check_condition(cond, scope, out)

        mps = rule.get("maxPerSession")
        if "maxPerSession" in rule and (isinstance(mps, bool) or not isinstance(mps, int) or mps < 1):
            out.fail(scope, f"maxPerSession must be a whole number of 1 or more, got {mps!r}")

        then = rule.get("then")
        if not isinstance(then, dict) or not isinstance(then.get("action"), str):
            out.fail(scope, "then needs an action")
            continue
        action = then["action"]
        bad = forbidden_hit(action, FORBIDDEN_TOKENS + FORBIDDEN_ACTIONS)
        if bad:
            out.fail(scope, f"action '{action}' is forbidden (contains '{bad}')")
        elif action not in ALLOWED_ACTIONS:
            out.fail(scope, f"action '{action}' is not an allowed action ({', '.join(ALLOWED_ACTIONS)})")
        elif action == "difficulty_offset":
            value = then.get("value")
            if not is_number(value):
                out.fail(scope, "difficulty_offset needs a numeric value")
            else:
                if lo is not None and hi is not None and not (lo <= value <= hi):
                    out.fail(scope, f"difficulty_offset value {value} is outside minOffset {lo} to maxOffset {hi}")
                if value < 0:
                    easing.append((rid, rule))
                elif value > 0:
                    raising += 1
        elif action == "suggest_mode":
            target = then.get("mode")
            if target in shared:
                out.fail(scope, f"suggest_mode names shared mode '{target}'; shared modes never adapt")
            elif target not in declared:
                out.fail(scope, "suggest_mode needs a mode that names a declared non shared mode")

    if len(easing) > 1:
        for rid, rule in easing:
            mps = rule.get("maxPerSession")
            if isinstance(mps, bool) or mps != 1:
                out.fail(f"rule {rid}", f"easing rule without maxPerSession 1 while {len(easing)} easing rules exist; "
                                        "silent easing is bounded to once per session")
    if easing and not raising:
        out.warn("rules", "every rule eases and none raises difficulty; an engine that only eases can bore skilled players")


def check_condition(cond: object, scope: str, out: Findings) -> None:
    if not isinstance(cond, dict):
        out.fail(scope, f"condition {cond!r} must be an object with input, op and value")
        return
    name = cond.get("input")
    if not isinstance(name, str):
        out.fail(scope, "condition has no input name")
    else:
        bad = forbidden_hit(name, FORBIDDEN_TOKENS)
        if bad:
            out.fail(scope, f"input '{name}' is forbidden (contains '{bad}'); only play signals may be inputs")
        elif name not in ALLOWED_INPUTS:
            out.fail(scope, f"input '{name}' is not an allowed play signal")
    if cond.get("op") not in OPERATORS:
        out.fail(scope, f"operator {cond.get('op')!r} is not one of {', '.join(OPERATORS)}")
    if not is_number(cond.get("value")):
        out.fail(scope, f"condition value {cond.get('value')!r} must be a number")


def check_player(policy: dict, out: Findings) -> None:
    player = policy.get("player")
    if not isinstance(player, dict):
        out.fail("player", "player block is missing")
        return
    settings = player.get("settings")
    settings = settings if isinstance(settings, list) else []
    if "auto" not in settings:
        out.fail("player", "settings must include auto")
    if not [s for s in settings if s != "auto"]:
        out.fail("player", "settings must include at least one fixed level besides auto")
    for key in ("explain", "log", "reset"):
        if player.get(key) is not True:
            out.fail("player", f"{key} must be true; help must be visible and reversible")


def check_scores(policy: dict, out: Findings) -> None:
    scores = policy.get("scores")
    if not isinstance(scores, dict):
        out.fail("scores", "scores block is missing")
        return
    if scores.get("modifyAfterFact") is True:
        out.fail("scores", "modifyAfterFact is true; nothing may change a score after the fact")
    elif scores.get("modifyAfterFact") is not False:
        out.fail("scores", "modifyAfterFact must be declared as false")
    if scores.get("assistedRunsOnSharedBoards") is True:
        out.fail("scores", "assisted runs are allowed on shared boards; they must not be")


def check_experiment(policy: dict, out: Findings) -> None:
    exp = policy.get("experiment")
    if not isinstance(exp, dict):
        out.fail("experiment", "experiment block is missing; every policy ships with a persistent holdout")
        return
    hold = exp.get("holdoutPercent")
    if not is_number(hold) or not (1 <= hold <= 20):
        out.fail("experiment", f"holdoutPercent {hold!r} must be a number from 1 to 20")
    elif hold != int(hold):
        out.fail("experiment", f"holdoutPercent {hold!r} must be a whole number (the engine hashes into 100 buckets)")
    salt = exp.get("holdoutSalt")
    if not isinstance(salt, str) or not salt.strip():
        out.fail("experiment", "holdoutSalt is missing; a stable salt keeps the same holdout across policy revisions")
    primary = exp.get("primary")
    if not isinstance(primary, list) or not [p for p in primary if isinstance(p, str) and p.strip()]:
        out.fail("experiment", "no primary metric")
    days = exp.get("readAfterDays")
    if not is_number(days):
        out.warn("experiment", "readAfterDays is missing; read results after at least 28 days")
    elif days < 28:
        out.warn("experiment", f"readAfterDays {days} is under 28; early reads over fit to the first weeks")


def check_audience(policy: dict, out: Findings) -> bool:
    """Return True when the strict tier applies."""
    aud = policy.get("audience")
    if not isinstance(aud, dict):
        out.fail("audience", "audience block is missing")
        return False
    age = aud.get("minimumAge")
    tier = aud.get("minorsTier")
    minors = False
    if not is_number(age):
        out.fail("audience", f"minimumAge {age!r} must be a number")
    elif age < 18:
        minors = True
        if tier != "strict":
            out.fail("audience", f"minimumAge {age:g} includes minors and minorsTier is {tier!r}; it must be 'strict'")
    return minors or tier == "strict"


def check_return_reasons(policy: dict, strict: bool, out: Findings) -> None:
    reasons = policy.get("returnReasons", [])
    if not isinstance(reasons, list):
        out.fail("returnReasons", "returnReasons must be a list")
        return
    for n, rr in enumerate(reasons, 1):
        if not isinstance(rr, dict):
            out.fail(f"returnReason #{n}", "must be an object")
            continue
        scope = f"returnReason {rr.get('id') or '#' + str(n)}"
        source = normalize(rr.get("source", ""))
        if strict and source in STRICT_BLOCKED_SOURCES:
            out.fail(scope, f"source '{rr.get('source')}' is not allowed in the strict tier (no streak or loss pressure for minors)")
        mpd = rr.get("maxPerDay")
        if not is_number(mpd) or mpd < 1:
            out.fail(scope, "no maxPerDay; a return reason needs a daily cap")
        qh = rr.get("quietHours")
        if not isinstance(qh, list) or not qh:
            out.fail(scope, "no quietHours; a return reason needs a quiet window")
        elif len(qh) != 2 or not all(isinstance(t, str) and re.fullmatch(r"([01][0-9]|2[0-3]):[0-5][0-9]", t) for t in qh):
            out.fail(scope, f"quietHours must be two \"HH:MM\" times, got {qh!r}")
        if is_number(mpd) and mpd != int(mpd):
            out.fail(scope, f"maxPerDay must be a whole number, got {mpd!r}")


def check(policy: dict) -> Findings:
    out = Findings()
    for key in REQUIRED_SECTIONS:
        if key not in policy:
            out.fail("policy", f"missing section '{key}'")
    declared, shared = check_modes(policy, out)
    check_rules(policy, declared, shared, out)
    check_player(policy, out)
    check_scores(policy, out)
    check_experiment(policy, out)
    strict = check_audience(policy, out)
    check_return_reasons(policy, strict, out)
    return out


def could_not_run(message: str, as_json: bool) -> int:
    if as_json:
        print(json.dumps({"verdict": "could not run", "error": message, "cannotCover": CANNOT_COVER}, indent=2))
        print(CANNOT_COVER, file=sys.stderr)
    else:
        print(f"could not run: {message}")
        print(CANNOT_COVER)
    return 2


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Check a player experience policy against the pxe 0.1 format.")
    ap.add_argument("policy", help="path to the policy JSON file")
    ap.add_argument("--json", action="store_true", help="print the findings as one JSON document")
    args = ap.parse_args(argv)
    path = Path(args.policy)
    try:
        policy = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return could_not_run(f"{path}: {exc}", args.json)
    if not isinstance(policy, dict):
        return could_not_run("the policy must be a JSON object", args.json)
    version = str(policy.get("pxeVersion", ""))
    if version not in SUPPORTED_VERSIONS:
        shown = version or "missing"
        return could_not_run(f"pxeVersion {shown} is not supported by this checker ({sorted(SUPPORTED_VERSIONS)})", args.json)

    out = check(policy)
    fails, warns = out.count("FAIL"), out.count("WARN")
    verdict = "FAIL" if fails else "PASS"
    lines = [f"{i['severity']} {i['scope']}: {i['message']}" for i in out.items]
    if args.json:
        print(json.dumps({"product": policy.get("product"), "pxeVersion": version,
                          "policyRevision": policy.get("policyRevision"), "verdict": verdict,
                          "fails": fails, "warns": warns, "findings": out.items, "lines": lines,
                          "cannotCover": CANNOT_COVER}, indent=2))
        print(CANNOT_COVER, file=sys.stderr)
    else:
        rules = policy.get("rules")
        print(f"{policy.get('product', '?')}: pxe {version}, revision {policy.get('policyRevision', '?')}, "
              f"{len(policy.get('modes') or [])} modes, {len(rules) if isinstance(rules, list) else 0} rules")
        for line in lines:
            print(line)
        print(f"Verdict: {verdict}")
        print(CANNOT_COVER)
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
