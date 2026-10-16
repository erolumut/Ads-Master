# Adaptive Policy Design

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). The file format is defined in [policy format](policy-format.md) (pxe 0.1) and checked by `pxe_policy_check.py` in [../scripts](../scripts/). Thresholds in this module are placeholders to tune per game, never benchmarks. Studies carry their dossier labels.

Gate: drafting or revising a policy file and running the checker are G1. Shipping a policy revision to players is a live change and is G3: a change request with the checker output, the rollback plan and the experiment row. Player facing copy passes `compliance` before it ships.

## 1. What a policy is for

A policy maps play signals to small, visible, bounded actions in private modes. It exists to help a player who is struggling, keep a cruising player interested and end sessions cleanly. It never decides outcomes, never touches shared modes and never reads money or ad signals.

| Evidence that shapes the rules | Label |
|-------------------------------|-------|
| Easing for players at higher churn risk raised engagement, long run retention and total spending in a 12 week randomized experiment with 300,000+ players and a holdout (Ascarza, Netzer, Runge, IJRM 2025) | [Reported, 2026-10] |
| Heuristic DDA is often noticeable ("rubber banding"); deep player models improved intrinsic motivation in an MMORPG field study (Pfau, Smeddinck, Malaka, CHI 2020) | [Reported, 2026-10] |
| DDA can make players overconfident (Constant and Levieux, CHI 2019) | [Reported, 2026-10] |
| Performance based DDA raised performance but not enjoyment (221 participants, controlled study) | [Reported, 2026-10] |
| Whether disclosing adaptation changes its effect is unresolved | [Contested] (research notes) |

What follows from this: ease rarely and in small steps, say so, let the player choose, and measure enjoyment proxies, not only performance.

## 2. The policy format in practice

Start from the sample in [policy format](policy-format.md) section 2 (also `../scripts/samples/policy-valid.json`). Fill it in this order:

| Order | Block | Decide | Typical mistake |
|-------|-------|--------|-----------------|
| 1 | `modes` | Every mode, with `shared: true` for daily, ranked, races, group and global boards, tournaments | Forgetting a derived board (a streak or season table fed by a shared mode is shared) |
| 2 | `audience` | `minimumAge` from the store rating and the product; `minorsTier: "strict"` whenever minors can play | Setting 18 when the store listing allows younger players |
| 3 | `difficulty` | `steps` the game supports, `default`, and the published range `minOffset` to `maxOffset` | A range wider than one step at launch |
| 4 | `player` | `settings` with `auto` and every fixed level; `explain`, `log`, `reset` all true | Hiding the setting in a submenu |
| 5 | `rules` | Rule patterns in section 3 | Easing rules without a cap |
| 6 | `returnReasons` | Content and own state sources only, caps and quiet hours ([sessions](sessions-opens-and-return-reasons.md)) | A `streak` or `loss` source with minors |
| 7 | `scores` | `modifyAfterFact: false`, `assistedRunsLabeled: true`, `assistedRunsOnSharedBoards: false` | Treating a booster run as unassisted |
| 8 | `experiment` | `holdoutPercent` 1 to 20, `readAfterDays` (56 in the sample; under 28 warns), primary metrics, guardrails | No guardrail metrics |

Allowed inputs are only the play signals in section 3 of the format. Allowed actions are only `difficulty_offset`, `offer_hint`, `offer_break`, `show_next_goal` and `suggest_mode` (to a non shared mode). Anything else fails the checker.

## 3. Rule patterns

Every threshold below is a placeholder. Start there, then tune from the holdout comparison and the guardrails, never from intuition alone.

### 3.1 Ease after fails

```json
{ "id": "ease_after_fails", "modes": ["levels", "practice"],
  "when": [ { "input": "fail_streak", "op": ">=", "value": 3 } ],
  "then": { "action": "difficulty_offset", "value": -1 },
  "reason": "struggling", "explainKey": "pxe.reason.struggling", "maxPerSession": 1 }
```

| Tune | Guidance |
|------|----------|
| Threshold | Placeholder 3 fails. Lower it if quit after fail is high before the third fail; raise it if eased players replay less |
| Step | One step. The format clamps to the published range |
| Cap | `maxPerSession: 1`; the checker fails a second easing rule without it |
| Combine | Add `rating_gap` (level much harder than the player) to avoid easing a player who is just unlucky |
| Never | A cold start player (no rating yet), a shared mode, a level marked as a deliberate tutorial test |

### 3.2 Hint when stuck

```json
{ "id": "offer_hint_when_stuck", "modes": ["levels"],
  "when": [ { "input": "attempts_on_level", "op": ">=", "value": 2 },
            { "input": "hint_uses_level", "op": "==", "value": 0 } ],
  "then": { "action": "offer_hint" },
  "reason": "stuck", "explainKey": "pxe.reason.stuck", "maxPerSession": 3 }
```

A hint is an offer the player can decline, not an automatic reveal. It is the gentlest help and should fire before any difficulty offset. A long `median_move_ms` on the current attempt is a second signal for "stuck" (placeholder: well above the player's own median).

### 3.3 Break offer

```json
{ "id": "offer_break_after_streak", "modes": ["levels", "practice"],
  "when": [ { "input": "fail_streak", "op": ">=", "value": 5 },
            { "input": "restarts_recent", "op": ">=", "value": 3 } ],
  "then": { "action": "offer_break" },
  "reason": "long_streak", "explainKey": "pxe.reason.break", "maxPerSession": 1 }
```

A break offer says "this one will still be here" and shows the next goal. It never pairs with a purchase or an ad. It is the honest answer to tilt: the player stops on their own terms.

### 3.4 Raise after fast solves

```json
{ "id": "raise_after_fast_solves", "modes": ["levels", "practice"],
  "when": [ { "input": "fast_solve_streak", "op": ">=", "value": 3 } ],
  "then": { "action": "difficulty_offset", "value": 1 },
  "reason": "cruising", "explainKey": "pxe.reason.cruising", "maxPerSession": 1 }
```

The checker warns when every rule eases: an engine that only eases can bore skilled players. Raising is offered openly ("you are flying, want a tougher one?") or applied with the same visible "why this level" line as easing.

### 3.5 Next goal

```json
{ "id": "next_goal_at_end", "modes": ["levels"],
  "when": [ { "input": "sessions_today", "op": ">=", "value": 1 } ],
  "then": { "action": "show_next_goal" },
  "reason": "next_goal", "explainKey": "pxe.reason.next_goal", "maxPerSession": 1 }
```

The game decides when a session is ending (a menu return, a break accepted); the policy decides that the next goal is shown. Next goal content comes from real content and the player's own state ([sessions](sessions-opens-and-return-reasons.md) section 4).

### 3.6 Suggest practice

`suggest_mode` with `mode: "practice"` after a fail in a shared mode is allowed only if the rule names non shared modes in its `modes` list; the offer appears in the private mode the player moves to, never inside the shared run. A shared mode returns no action, whatever the rules say.

## 4. Silent easing limits

| Limit | Source |
|-------|--------|
| Offsets clamped to `minOffset` and `maxOffset`; offsets wider than two steps either way fail | Format section 5 |
| Silent easing at most once per session | Format sections 1 and 6 |
| More than one easing rule requires each to carry `maxPerSession: 1` | Format section 5 |
| Every action has a reason and an explain key and goes to the log, silent or not | Format section 6 |

"Silent" means the change is not announced in the moment. It is never hidden: the "why this level" line and the log always show it. Anything beyond one silent easing per session must be an offer the player accepts.

## 5. Transparency UI copy patterns

Each `explainKey` resolves to a short line in the player's language. Drafts below are patterns, not approved copy; send them to `compliance` before shipping.

| Reason key | Pattern for "why this level" | Pattern for the log |
|-----------|-------------------------------|---------------------|
| `pxe.reason.struggling` | "Made a little easier after a few tries. Change this in Settings." | "Level 42: eased one step after 3 tries" |
| `pxe.reason.stuck` | "Want a hint? You have tried this one a few times." | "Level 42: hint offered" |
| `pxe.reason.break` | "Tough run. This level will wait for you." | "Break offered after 5 tries" |
| `pxe.reason.cruising` | "You are solving these fast, so this one is a bit tougher." | "Level 43: one step harder after 3 fast solves" |
| `pxe.reason.next_goal` | "Next: the castle gate opens at level 45." | "Next goal shown" |

Copy rules:
1. Plain words, one line, no guilt, no countdown, no "you lost".
2. State what changed and why, in terms of the player's own play ("after a few tries"), never of a model ("our AI predicted").
3. Always say where to change it.
4. Never imply a purchase is the fix.
5. Same copy for every player at the same reason; no variant by any money or ad signal.

## 6. Player settings and reset

| Setting | Behavior (format section 6) |
|---------|-----------------------------|
| `auto` | The policy may apply difficulty actions within the published range |
| `easy`, `normal`, `hard` | A fixed level. Difficulty actions are disabled; hint, break and next goal offers still respect their caps |
| Explain | "Why this level" line visible on adapted levels |
| Log | A readable list of adaptations: date, level, action, reason |
| Reset | Clears the player's estimator state (rating, streaks) and the log view; the next session starts at the default |

Put the setting where a player looks when frustrated: the pause menu and the fail screen, plus Settings. A setting the player must hunt for does not count as control ([Practitioner consensus]).

## 7. The audit log

| Field | Client (full) | Server (sampled) |
|-------|---------------|------------------|
| Timestamp, session id | Yes | Yes |
| `pxeVersion`, `policyRevision`, `ENGINE_VERSION`, level table version | Yes | Yes |
| Mode id (and its `shared` flag) | Yes | Yes |
| Rule id, action, value, reason code, explain key | Yes | Yes |
| Inputs summary (the play signals the rule read, rounded) | Yes | Yes |
| Holdout flag | Yes | Yes |
| Player setting at the time | Yes | Yes |

The log contains play signals only; it never carries an ad id, a device id, a location or a payment field. The server sample serves audits and the rigged stream test ([fair randomness](fair-randomness-and-solvability.md) section 5.3). Retention period and consent: [architecture](architecture-and-telemetry.md).

## 8. Shipping a policy revision

| Step | What | Gate |
|------|------|------|
| 1 | Write the change and its reason in the experiment row (`ads-master/EXPERIMENTS.md`) | G1 |
| 2 | Bump `policyRevision`; a field name change is a format bump (`pxeVersion`), not a revision | G1 |
| 3 | Run `python3 -I ../scripts/pxe_policy_check.py data/pxe-policy.json` and attach the output; exit 0 is PASS, 1 FAIL, 2 could not run (unknown `pxeVersion` included) | G1 |
| 4 | Resolve every FAIL; justify every WARN in writing | G1 |
| 5 | Send new or changed explain keys to `compliance` | G1 |
| 6 | Diff the revision against the live one: rules added, removed, thresholds changed | G1 |
| 7 | Change request: the diff, checker output, rollout plan (percentage ramp), rollback (the previous revision stays in remote config), the experiment read date | G3 |
| 8 | On approval, publish through remote config; the engine logs the new revision with every action | G3 |
| 9 | Watch guardrails daily for the first week; roll back on a breach | G2 read, G3 rollback |

Holdout persistence: the format assigns holdout players by a stable hash of the install id and `experiment.holdoutSalt`, so policy revisions keep the same holdout. Change the salt only to start a new holdout on purpose, log it as a decision, and restart the read ([experiments](experiments-and-measurement.md)).

## 9. How the checker gates it

`pxe_policy_check.py` applies [policy format](policy-format.md) section 5. It is the mechanical floor, not the whole review.

| The checker fails | The checker cannot cover |
|-------------------|--------------------------|
| Rules on shared modes or with no mode | Whether the game code actually follows the file |
| Inputs outside the play signal list, or names with a forbidden token | Whether the explain texts are clear to players |
| Actions outside the allowed list, or forbidden action names | Server side or analytics use of data outside this file |
| Offsets outside the range or wider than two steps | Legal review |
| Uncapped multiple easing rules | |
| Missing reason or explain key | |
| Missing player controls | |
| Score changes or assisted runs on shared boards | |
| Holdout outside 1 to 20 percent, no primary metric | |
| Minors without the strict tier; streak or loss return reasons in strict | |
| Return reasons without caps or quiet hours | |

The right column is the script's own "cannot cover" sentence. Quote it in every change request, and cover it with the engine conformance tests and the [audit](audit-checklist.md).

## 10. Anti patterns

| Anti pattern | Why it is out |
|--------------|---------------|
| Easing to keep a player alive until an offer appears | Ties help to monetization; red list ([ethics](ethics-law-and-store-rules.md)) |
| Harder levels for players likely to pay or with an ad ready | Forbidden inputs; high legal risk |
| A policy per segment defined by spend | Spend is never an input, directly or through a segment |
| Many small silent easings | Rubber banding is noticeable [Reported, 2026-10]; the format caps it |
| Adapting a level that is part of a race or team event | Shared; the event board is not private |
| Tuning thresholds on short term revenue | Optimize retention and fun proxies; revenue is secondary |
