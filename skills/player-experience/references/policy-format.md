# Player Experience Policy Format (pxe 0.1)

> The one file that says how a game may adapt to a player. The engine (`engine/`) reads it at runtime; `scripts/pxe_policy_check.py` checks it before it ships. Written 2026-10-16. Changing a field name is a version bump (`0.2`); the checker refuses versions it does not know (exit 2).

## 1. Principles the format enforces

1. Shared modes never adapt. A mode marked `shared: true` (daily, ranked, group or global boards, tournaments, races) gets the same seed, parameters and engine version for everyone. The engine returns no action there; the checker fails any rule that names one.
2. Play signals only. Inputs come from a fixed list of play signals (section 3). Money, ads, device value, location and inferred personal traits are never inputs, under any name.
3. Help is visible. Every action has a reason code and a player facing explanation key; the player can see the log, choose a fixed difficulty and reset.
4. Bounded. Difficulty moves in small published steps; easing happens at most once per session silently; nothing changes a score after the fact.
5. Measured. Every policy ships with a persistent holdout that never adapts.
6. Minors get the strict tier.

## 2. Shape

```json
{
  "pxeVersion": "0.1",
  "policyRevision": 3,
  "product": "example-puzzle",
  "audience": { "minimumAge": 13, "minorsTier": "strict" },
  "modes": [
    { "id": "daily", "shared": true },
    { "id": "levels", "shared": false },
    { "id": "practice", "shared": false }
  ],
  "difficulty": { "steps": [-2, -1, 0, 1, 2], "default": 0, "minOffset": -1, "maxOffset": 1 },
  "player": { "settings": ["auto", "easy", "normal", "hard"], "explain": true, "log": true, "reset": true },
  "rules": [
    {
      "id": "ease_after_fails",
      "modes": ["levels", "practice"],
      "when": [ { "input": "fail_streak", "op": ">=", "value": 3 } ],
      "then": { "action": "difficulty_offset", "value": -1 },
      "reason": "struggling",
      "explainKey": "pxe.reason.struggling",
      "maxPerSession": 1
    },
    {
      "id": "offer_hint_when_stuck",
      "modes": ["levels"],
      "when": [ { "input": "attempts_on_level", "op": ">=", "value": 2 }, { "input": "hint_uses_level", "op": "==", "value": 0 } ],
      "then": { "action": "offer_hint" },
      "reason": "stuck",
      "explainKey": "pxe.reason.stuck",
      "maxPerSession": 3
    },
    {
      "id": "raise_after_fast_solves",
      "modes": ["levels", "practice"],
      "when": [ { "input": "fast_solve_streak", "op": ">=", "value": 3 } ],
      "then": { "action": "difficulty_offset", "value": 1 },
      "reason": "cruising",
      "explainKey": "pxe.reason.cruising",
      "maxPerSession": 1
    }
  ],
  "returnReasons": [
    { "id": "daily_ready", "source": "content", "maxPerDay": 1, "quietHours": ["21:00", "09:00"] }
  ],
  "scores": { "modifyAfterFact": false, "assistedRunsLabeled": true, "assistedRunsOnSharedBoards": false },
  "experiment": { "holdoutPercent": 5, "holdoutSalt": "pxe-holdout-2026", "readAfterDays": 56, "primary": ["d7_retention"], "guardrails": ["quit_after_fail_rate", "adaptation_opt_out_rate"] }
}
```

## 3. Allowed inputs (play signals)

| Input | Meaning |
|-------|---------|
| `fail_streak` | Consecutive fails, any level, this session |
| `attempts_on_level` | Attempts on the current level so far |
| `fast_solve_streak` | Consecutive wins under the level's median time |
| `hint_uses_level` | Hints used on the current level |
| `hint_uses_session` | Hints used this session |
| `median_move_ms` | Median time between moves in the last attempt |
| `restarts_recent` | Restarts in the last 10 minutes |
| `session_gap_hours` | Hours since the previous session ended |
| `sessions_today` | Sessions started today (local day) |
| `skill_rating` | The player's Elo style rating in this game |
| `level_rating` | The current level's rating from the calibration table |
| `rating_gap` | `level_rating` minus `skill_rating` |
| `quit_rate_recent` | Share of the last 10 attempts abandoned mid level |

Operators: `>=`, `>`, `<=`, `<`, `==`, `!=`. Values are numbers.

## 4. Forbidden inputs and actions

The checker fails any input or action whose name contains, in any case or separator style, one of: `spend`, `spent`, `purchase`, `payer`, `paying`, `revenue`, `ltv`, `arpu`, `arppu`, `whale`, `iap`, `ad_value`, `advalue`, `ecpm`, `ad_ready`, `rewarded_ready`, `ad_available`, `ad_fill`, `monetiz`, `price`, `device_model`, `device_tier`, `device_price`, `country`, `region`, `geo`, `income`, `age`, `gender`, `health`, `mood`, `vibration`, `battery`. Only names listed in section 3 are allowed; anything else is a FAIL, not a warning.

Allowed actions: `difficulty_offset` (with `value` inside `minOffset` to `maxOffset`), `offer_hint`, `offer_break`, `show_next_goal`, `suggest_mode` (with `mode` naming a non shared mode). Any other action fails, and these names fail even if someone adds them: `force_loss`, `death`, `kill`, `rig`, `score_bonus`, `modify_score`, `bias_pieces`, `harvest`.

## 5. Rules the checker applies

| Check | Result |
|-------|--------|
| `pxeVersion` not supported | Exit 2 |
| A rule names a shared mode, or no `modes` | FAIL |
| Input outside section 3, or forbidden name | FAIL |
| Action outside section 4, or forbidden name | FAIL |
| `difficulty_offset` value outside `minOffset` and `maxOffset`, or offsets wider than two steps either way | FAIL |
| More than one easing rule (negative offset) without `maxPerSession` 1 | FAIL |
| Rule without `reason` or `explainKey` | FAIL |
| `player.settings` missing `auto` or any fixed level, or `explain`, `log`, `reset` false | FAIL |
| `scores.modifyAfterFact` true, or assisted runs allowed on shared boards | FAIL |
| `experiment.holdoutPercent` outside 1 to 20, no primary metric, or no `holdoutSalt` | FAIL |
| `audience.minimumAge` under 18 and `minorsTier` not `strict` | FAIL |
| Strict tier with a return reason whose `source` is `streak` or `loss` | FAIL |
| Return reason without `maxPerDay` or `quietHours` | FAIL |
| `readAfterDays` under 28 | WARN |
| No raising rule (every rule eases) | WARN: an engine that only eases can bore skilled players |

## 6. What the engine guarantees at runtime

1. `evaluate(state, mode)` returns no action in a shared mode, whatever the rules say.
2. A player setting other than `auto` disables difficulty actions; hint, break and next goal offers still respect their caps.
3. Holdout players (stable FNV-1a hash of the install id and `experiment.holdoutSalt`, modulo 100, below `holdoutPercent`) get no actions; their events are still counted. The salt stays the same across policy revisions so the holdout persists through a long read; change it only to start a new holdout on purpose, and log that as a decision.
4. Every returned action carries the rule id, reason code and explain key, and is appended to the audit log.
5. Offsets are clamped to `minOffset` and `maxOffset`; silent easing happens at most once per session.
6. Randomness comes from a seeded generator; the same seed and engine version give the same sequence on every platform.
