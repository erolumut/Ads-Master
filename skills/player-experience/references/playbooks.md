# Player Experience Playbooks

> Knowledge as of 2026-10 (research pass 2026-10-16). Each play lists its trigger, steps, gates and outputs. Thresholds are placeholders to tune per game. Plays end with handoffs; this package does not design levels, send messages or price offers.

Gate summary: every analysis, draft policy and flag is G1. Any live change (policy revision, level table, setting UI, return reason schedule) is G3 with a change request, the checker output and a rollback. Player facing copy passes `compliance`.

## Play 1. First policy for a new level game

Trigger: a level based game (Royal Match style path) with no adaptation yet.

1. List modes. Mark every shared mode `shared: true`, including race events, team events and derived boards ([policy design](adaptive-policy-design.md) section 2).
2. Set `audience`. If minors can play or age is unknown, `minorsTier: "strict"`.
3. Ship the six events and the estimator first, with no rules active, for the cold start window ([calibration](difficulty-measurement-and-calibration.md) section 5).
4. Run `difficulty_table.py` on the first weeks of unassisted attempts; file walls to the designer.
5. Write the minimal rule set: hint when stuck, break after a long fail streak, ease one step after fails (`maxPerSession: 1`), raise one step after fast solves, next goal at session end. Range `minOffset -1`, `maxOffset 1`.
6. Draft explain keys and the log, setting and reset UI; send the copy to `compliance`.
7. Set the holdout from a power calculation (1 to 20 percent), `readAfterDays` 56 or more, primary D1, D7, D28 and sessions per week, fun proxies and guardrails.
8. Run `pxe_policy_check.py`; resolve FAILs, justify WARNs.
9. G3 change request with the ramp plan (for example 10, 50, 100 percent of the treatment share) and the kill switch.
10. Watch guardrails daily for a week; main read at 8 to 12 weeks ([experiments](experiments-and-measurement.md)).

Outputs: `data/pxe-policy.json` revision 1, checker output, experiment row, copy for compliance. Handoffs: `compliance` (copy), `site-engineer` or the game repo (integration), `measurement` (events and metrics).

## Play 2. Practice mode adaptation for a daily game

Trigger: a daily social game (shared daily round, groups, seasons) wants adaptation.

1. Confirm the daily, group boards and season tables are shared. They never adapt; this is not negotiable.
2. Identify private surfaces: practice levels, archive replays, uncounted "play again" runs.
3. Apply rules only there: hint when stuck, ease one step after fails in practice, suggest practice after a hard daily (`suggest_mode` naming the practice mode; the offer appears in practice, never in the daily run).
4. Make sure practice and archive runs never write to a ranked board, consistent with the [monetization contract](../../game-monetization/references/monetization-contract.md) section 3.
5. Return reasons: `daily_ready` from content only, `maxPerDay` 1, quiet hours, opted in adults only; minors get content reasons only.
6. Holdout and read as in Play 1; primary metric includes daily completion and day over day return (from `game-liveops`).

Outputs: policy with shared daily, practice rules, return reason list. Handoffs: `game-liveops` (daily loop), `lifecycle-crm` (sends).

## Play 3. A wall at level N

Trigger: `difficulty_table.py` flags `wall` at N, or reviews say "stuck at N".

1. Check the export: one mode, one engine version, unassisted, cohort dates. Exclude the content frontier.
2. Read N against its neighbors: pass rate, first try pass, median attempts, quit at level, elo.
3. Check for a new mechanic at N, a release, an incident or a UA mix change.
4. Write the difficulty flag in the `game-liveops` format with hypotheses ranked: unclear goal, too hard, bug, new mechanic.
5. Meanwhile, allowed engine help: confirm the hint and break rules cover N. Do not widen the offset range or add silent easing to hide the wall.
6. After the designer's fix, re-run the table after enough attempts and confirm the flag cleared.

Outputs: flag file, table output. Handoffs: game repo (level), `game-liveops` (signals).

## Play 4. D1 drop after an update

Trigger: D1 falls after a release.

1. Confirm with `measurement` that the drop is real (definitions, tracking changes, cohort mix).
2. Split by engine version and policy revision: did the update bump either? A generator change makes new levels; a revision bump re-draws the holdout.
3. Compare treatment and holdout D1 after the release. If both dropped, the cause is the release, not the policy. If only treatment dropped, suspect the policy or its interaction with new content.
4. Check the first session (curve module section 5): new early levels, a new mechanic too early, an offer before play.
5. Run `difficulty_table.py` on post release attempts for the first 20 levels; compare with the previous table.
6. If the policy is implicated, roll back to the previous revision (G3) and read again.

Outputs: diagnosis memo with sources and date ranges. Handoffs: game repo, `measurement`, `mobile-app-growth` if the mix changed.

## Play 5. Raising session length without pressure

Trigger: the owner wants longer sessions.

1. Baseline: median session length, sessions per week, quit after fail, voluntary replay, one tap rating, from `measurement`.
2. Look for honest levers ([sessions](sessions-opens-and-return-reasons.md) section 7): rest levels after peaks, a visible milestone a few levels away, timed infinite lives as earned rewards, voluntary replay, practice mode.
3. Look for friction: quits at intro levels, fail streaks without hints, exit interstitials.
4. Propose one change at a time with a hypothesis and guardrails. Refuse levers on the red list (lives that run out to force a wait, escalating stakes tied to offers, removing rest levels).
5. Test against the holdout; read session length only together with fun proxies and guardrails.

Outputs: proposal memo, experiment row. Handoffs: game repo, `game-liveops` (events), `game-monetization` (if lives or rewards touch the economy).

## Play 6. Return reasons rollout

Trigger: the game wants more opens.

1. Inventory real content moments: new daily, new levels, event start, a friend's move, a timer the player started.
2. Write each as a return reason with source, condition, caps, quiet hours and a copy draft ([sessions](sessions-opens-and-return-reasons.md) section 5.3).
3. Remove anything sourced from streak loss or absence; in the strict tier, keep only content reasons.
4. Add the list to the policy `returnReasons`; run the checker.
5. Hand off to `lifecycle-crm` for channel, consent, frequency and send; copy to `compliance`.
6. Measure opens within 24 hours of the moment, treatment versus holdout, plus notification opt outs as a guardrail.

Outputs: return reason list, policy update. Handoffs: `lifecycle-crm`, `compliance`.

## Play 7. Minors launch

Trigger: the game will be rated for or reachable by players under 18.

1. Set `minimumAge` from the store rating and `minorsTier: "strict"`.
2. Apply the strict tier table ([sessions](sessions-opens-and-return-reasons.md) section 8): cumulative counters instead of streak pressure, no daily return rewards, no loss or streak reasons, no variable paid rewards, profiling off by default, no ad SDK profiling.
3. Lower the break offer threshold; keep hint and ease rules (help is allowed).
4. Confirm the economy side with `game-monetization` (no countdowns aimed at minors, real money prices).
5. Ask `compliance` for the market review: AI Act Art 5 vulnerability, KIDS Act direction (a proposal), UK Children's Code, COPPA, store family policies. Several are open items to verify ([ethics](ethics-law-and-store-rules.md)).
6. Run the checker; it fails a non strict tier with minors and streak or loss reasons in strict.

Outputs: strict tier policy, compliance request. Handoffs: `compliance`, `game-monetization`, `lifecycle-crm`.

## Play 8. Monthly policy review

Trigger: the first week of each month.

1. Run `pxe_policy_check.py` on the live revision; record the output.
2. Run `difficulty_table.py` on the last 28 days; compare with last month.
3. Read the action mix from the audit log sample: which rules fire, how often, for what share of players. A level eased for most players goes to the designer.
4. Read guardrails and fun proxies against the holdout; note the read status (running, due, done).
5. Check opt outs from `auto` and complaints mentioning difficulty or "rigged".
6. Run the rigged stream test quarterly at least ([fair randomness](fair-randomness-and-solvability.md) section 5.3).
7. Freshness: AI Act guidelines, KIDS Act progress, DFA status, Apple guideline updates, CPC actions.
8. Write the review to `ads-master/outputs/player-experience/` and update `ads-master/memory/player-experience.md` with thresholds used and learnings.

Outputs: monthly review. Handoffs as findings require.

## Play 9. "Can we do what Block Blast is said to do?"

Trigger: someone shares the viral decompile claim and asks for the same.

1. State the facts once: the claims are unverified (one creator, no code, no independent test); the spend and ad linked variants are high legal risk (AI Act Art 5, consumer law, Apple 2.3.1, 5.6, 5.1.2(iii)).
2. Show the evidence that helping works: Ascarza et al., randomized, 300,000+ players, easing at risk players raised retention and total spending [Reported, 2026-10].
3. Offer the honest build: Play 1 with a holdout.
4. Record the request and the verdict with the [verdict template](ethics-law-and-store-rules.md).

Outputs: verdict note. Handoffs: `compliance` if the request persists.

## Play 10. Bot strength in a board game

Trigger: a board game platform (rated play between people, bots for solo play) wants adaptive bots.

1. Rated and ranked play: bots never adapt secretly; strength is fixed per labeled bot level.
2. Casual play against a bot: strength may adapt openly ("bot level 3, adjusts to you"), with a fixed level option.
3. The clock never plays for a player and engines stay deterministic; the bot is an ordinary engine client.
4. Log bot level with each match; never mix adapted bot results into ratings.

Outputs: bot policy memo. Handoffs: the game repo.
