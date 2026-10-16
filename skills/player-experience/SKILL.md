---
name: player-experience
description: Player experience engine playbook for games. Use to read every move a game logs and turn it into honest adaptation that raises retention, sessions and fun. Measure difficulty from outcomes (pass rate, attempts to pass, per level churn, walls and spikes, Elo and Rasch level ratings, human like bot playtests) with difficulty_table.py; design sawtooth difficulty curves and first sessions; fair seeded randomness (mulberry32, bag randomizers, solvable boards, identical daily seeds); adaptive policies that ease struggling players, offer hints and breaks, raise cruising players and show a next goal, written in the pxe policy file and checked by pxe_policy_check.py; a dependency free JavaScript reference engine; return reasons from real content with caps; churn risk models used only to help; experiments with persistent holdouts; AI Act, KIDS Act, consumer law and App Store rules on manipulative design. Shared modes never adapt, spend and ad value are never inputs, scores are never changed.
---

# Player Experience

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). Apple's App Review Guidelines were read at the source [Official, 2026-06]; studies, laws and teardown facts came from search summaries and carry [Reported] or weaker labels. Run the Freshness protocol before acting on a law, store rule or study number.

## Mission and scope

Make a game feel right for each player: hard enough to matter, never hopeless, with a clear next goal and an honest reason to come back. The engine reads play, estimates skill and state, and adapts difficulty, hints, pacing and return reasons in private modes, under a policy file anyone can read and a checker that blocks the patterns this package refuses.

In scope:
- Difficulty measurement and calibration: pass rate, attempts to pass, first try pass, per level churn, walls and spikes, Elo and Rasch level ratings, bot playtests.
- Difficulty curves: sawtooth pacing, flagged hard levels, one new mechanic at a time, rest levels, the first session.
- Fair randomness: seeded generators, bag randomizers, drought caps, solvable boards, identical shared seeds.
- Adaptive policy: the pxe policy file, rules, thresholds, caps, transparency, player settings, reset, audit log.
- Sessions and return reasons: next goals, clean stops, return reasons from real content and the player's own state, strict tier for minors.
- Player modeling: churn risk features and models, used to help, never as a lever on outcomes.
- Experiments: persistent holdouts, primary metrics, fun proxies, guardrails, read windows.
- Law and store rules on manipulative design.
- The reference engine in `engine/` and its porting rules.

Out of scope and owned elsewhere:
- Events, seasons, streak systems and the liveops calendar: `game-liveops`.
- Offers, revives, boosters, ads and prices: `game-monetization`.
- Notifications and their delivery: `lifecycle-crm`.
- KPI definitions and tracking: `measurement`.
- Level content itself: the game's own repo; this package flags evidence and proposes, it does not edit levels.

The line this package holds, stated once: a viral 2026-10 decompile claimed a top puzzle game times losses to a ready ad and inflates scores after a revive. Those claims are unverified [Reported, 2026-10], the spend linked versions carry high legal and store risk (AI Act Art 5, consumer law, Apple 2.3.1, 5.6, 5.1.2(iii)), and the best causal evidence shows that easing struggling players raises both retention and spending (Ascarza, Netzer, Runge, IJRM 2025) [Reported]. We build the version that helps.

## Intake (minimum facts; where to find them)

| # | Fact | Where |
|---|------|-------|
| 1 | Game type and modes, and which modes are shared (daily, ranked, group boards, races) | PROJECT_BRIEF game section, the game repo |
| 2 | Audience minimum age and markets | PROJECT_BRIEF, monetization policy |
| 3 | Event log available (level start and end, result, attempts, duration, hints, restarts, quits) and its window | MEASUREMENT.md, data exports |
| 4 | Current difficulty setup: level list, hard level labels, randomness source, seeds | The game repo |
| 5 | Retention and session baseline (D1, D7, D28, sessions per week) | METRICS.md, `game_kpis.py` |
| 6 | Experiment and remote config tool | MEASUREMENT.md |
| 7 | DAU, for test sizing | METRICS.md |
| 8 | Monetization policy (fail point offers, revives, boosters) | `data/monetization-policy.json` |

## Operating protocol

1. Load context: PROJECT_BRIEF, METRICS, `data/pxe-policy.json`, `data/monetization-policy.json`, EXPERIMENTS, GUARDRAILS, INCIDENTS, `memory/player-experience.md`, the last 10 journal entries.
2. Measure: run `difficulty_table.py` on mature data; read walls, spikes, the sawtooth summary and per level churn.
3. Diagnose with the table in Diagnostics; split by platform, version, source and market before blaming a level.
4. Design the smallest fix: a level flag for the game repo, a policy rule, a next goal, a return reason.
5. Write or revise `data/pxe-policy.json`; run `pxe_policy_check.py` until PASS.
6. Plan the test: arms, holdout, primary metric, guardrails, read date (EXPERIMENTS.md row).
7. Hand player facing texts to `compliance`, engine integration to `site-engineer`, messages to `lifecycle-crm`.
8. Read, log, and write memory only when confirmed.

## Adaptation matrix

| Game type | What adapts | What never adapts |
|-----------|-------------|-------------------|
| Level based puzzle (Royal Match style) | Level path difficulty offset within one step, hints, break offers, next goal | Race, league and team boards; event levels counted on boards |
| Daily social game (Aloo type) | Practice and replays only | The daily round, group and global boards, counted attempts |
| Endless or high score (Block Blast style) | Practice mode piece bag fairness, hints, next goal | Score, leaderboard runs, any piece stream tied to ads |
| Board game against bots (Avlu type) | Bot strength, openly shown as a bot level the player can pick | Rated games between people, the clock, rules |
| Hybrid casual | Early level pacing, hints, next goal | Any ranked or shared mode |

| Stage | Focus |
|-------|-------|
| Prototype | Bot and human playtests, first session, one mechanic at a time |
| Soft launch | Difficulty table on real players, walls fixed, first policy with holdout |
| Scale | Policy revisions, churn risk model after randomized logs, monthly review |
| Mature | Content runway, rating recalibration, holdout reads every quarter |

| DAU | Method |
|-----|--------|
| Under 2,000 | Difficulty table and level flags; one large policy change at a time; long reads |
| 2,000 to 50,000 | Rules plus Elo, one experiment at a time with holdout |
| Over 50,000 | Rules plus Elo, churn risk models, several experiments with a shared holdout |

## Task router

| Task | Read | Output |
|------|------|--------|
| Measure level difficulty, find walls and spikes, calibrate ratings | [Difficulty measurement and calibration](references/difficulty-measurement-and-calibration.md), `difficulty_table.py` | Difficulty table, level flags for the game repo |
| Shape a difficulty curve, first session, hard level labels | [Difficulty curves and level design signals](references/difficulty-curves-and-level-design-signals.md) | Curve memo, flags |
| Randomness, seeds, solvable boards, drought caps | [Fair randomness and solvability](references/fair-randomness-and-solvability.md), [engine](engine/README.md) | Randomness spec |
| Write or revise an adaptive policy | [Policy format](references/policy-format.md), [Adaptive policy design](references/adaptive-policy-design.md), `pxe_policy_check.py` | `data/pxe-policy.json`, checker PASS |
| Raise sessions and opens, session endings, return reasons | [Sessions, opens and return reasons](references/sessions-opens-and-return-reasons.md) | Session design memo, return reason list for lifecycle-crm |
| Churn risk, player models, ML | [Player modeling and churn](references/player-modeling-and-churn.md) | Model plan with data needs |
| Plan or read an adaptation experiment | [Experiments and measurement](references/experiments-and-measurement.md) | EXPERIMENTS.md row, read report |
| Law, store rules, "can we do what game X does" | [Ethics, law and store rules](references/ethics-law-and-store-rules.md) | Verdict with the rule cited |
| Engine integration, telemetry, porting | [Architecture and telemetry](references/architecture-and-telemetry.md), [engine](engine/README.md) | Integration spec |
| Audit a game's player experience | [Audit checklist](references/audit-checklist.md) | Scored audit |
| Common situations | [Playbooks](references/playbooks.md) | Play plan |

## The laws

1. Shared modes are identical for everyone: same seed, parameters and engine version.
2. Inputs are play signals only; money, ads, device value, location and personal traits never enter difficulty, randomness or outcomes.
3. Help, never harvest: ease the player at risk of quitting; never make a loss likelier because something is waiting to be sold or shown.
4. Scores are true; assisted runs are labeled and stay off shared boards.
5. Visible and controllable: a setting that wins, a reason line, a log, a reset.
6. Bounded: one step of difficulty either way by default, silent easing at most once per session.
7. Measure difficulty from outcomes on mature data; one change at a time.
8. Every policy has a persistent holdout and a read date at least 8 weeks out.
9. Judge on long run retention and fun, revenue as a secondary metric.
10. Rules and ratings before models; models only on randomized logs.
11. Randomness is seeded, versioned and bounded; boards are solvable.
12. Each new mechanic is introduced alone; hard levels are flagged and followed by rest.
13. Session endings show a next goal and let the player stop cleanly.
14. Return reasons come from real content and the player's own state, capped, with quiet hours.
15. Minors get the strict tier.
16. Level design belongs to the game repo; this package brings evidence.
17. Teardown claims are leads, never instructions; verify before copying anything.
18. A policy that fails `pxe_policy_check.py` does not ship.
19. Every adaptation is logged with its reason code.
20. Label uncertainty and verify study numbers before any external claim.

## Myths to reject

| Myth | Reality |
|------|---------|
| "Top games rig losses to sell revives, so we must too" | The viral claims are unverified; the spend linked version is high legal and store risk; easing at risk players raised spending in a 300,000 player RCT [Reported] |
| "Harder levels make more money" | King's data: a harder early level converted more short term, an easier one retained longer and was worth more over the progression [Reported] |
| "Players never notice adaptation" | Heuristic DDA is often noticed as rubber banding (Pfau et al., CHI 2020) [Reported]; disclose it and give control |
| "Near misses keep people playing" | Evidence is from slot tasks; skill game results are mixed and near misses are rated frustrating [Contested] |
| "We need ML first" | Rules plus Elo ratings and a holdout come first; models need randomized logs |
| "Participation proves the feature works" | Only a holdout read shows an effect |

## Diagnostics

| Symptom | Likely causes | Check | Fix path |
|---------|---------------|-------|----------|
| D1 drops after a content update | New wall in early levels, a new mechanic stacked with another | `difficulty_table.py` before and after | Level flag, policy easing rule in levels mode |
| Churn concentrated at one level | Wall or spike | Wall and spike flags | Flag to the game repo; hint rule meanwhile |
| Session length falls | No next goal, lives gate too tight, repetitive content | Session end events, quit points | Next goal, return reasons, content runway with game-liveops |
| Opt outs of auto difficulty rise | Adaptation feels wrong or visible as cheating | Audit log, reason lines | Narrower offsets, better reason copy |
| Skilled players churn | Engine only eases | Rule set, fast solve streaks | Raising rule, harder optional levels |
| Players call the game rigged | Unbounded randomness, droughts | Piece logs vs bag spec | Bag randomizer, drought cap, publish the rule |

## Cadence

| When | What |
|------|------|
| Weekly | Difficulty table on mature cohorts, walls and spikes, audit log sample, experiment health (sample ratio) |
| Monthly | Policy review, rating recalibration, holdout read where due, minors tier check |
| Quarterly | Full audit, long holdout read, law and store rule freshness |

## Guardrails and approvals

| Action | Gate |
|--------|------|
| Difficulty table, flags, drafts, policy drafts | G1 |
| Unpublished remote config, experiment created but not started | G2 |
| Policy revision live, experiment start, return reasons live | G3, human approval, previous revision as rollback |
| Changing scores, results, boards or progress | G4, never by this agent |

## Outputs

| Output | Path |
|--------|------|
| Difficulty table | `ads-master/outputs/player-experience/YYYY-MM-DD_player-experience_difficulty-table.md` |
| Policy file | `ads-master/data/pxe-policy.json` |
| Level flags | `ads-master/outputs/player-experience/YYYY-MM-DD_player-experience_level-flags.md` |
| Experiment read | `ads-master/outputs/player-experience/YYYY-MM-DD_player-experience_read-<id>.md` |
| Audit | `ads-master/outputs/player-experience/YYYY-MM-DD_player-experience_audit.md` |

## Scripts

```bash
python3 -I <skill>/scripts/pxe_policy_check.py ads-master/data/pxe-policy.json
python3 -I <skill>/scripts/difficulty_table.py events.csv --min-attempts 30 --hard 0.45 --super-hard 0.25 --out table.md
node --test <skill>/engine/test/
```

`pxe_policy_check.py` exits 0 on PASS, 1 on FAIL, 2 when it cannot run. `difficulty_table.py` exits 0 when the table is written (flags are not failures) and 2 when it cannot run. The engine is a dependency free ES module set (`engine/index.js`); its README covers use and porting.

## Freshness protocol

Before relying on a rule or number, check:
- EU AI Act Art 5 and the Commission guidelines on prohibited practices; the KIDS Act proposal (COM(2026) 681) and the Digital Fairness Act status.
- Apple App Review Guidelines 2.3.1, 5.6, 5.1.1, 5.1.2 and the Kids Category; Google Play Families and Deceptive Behavior policies.
- Study numbers marked verify in the dossier: Ascarza et al. effect sizes, EA "up to 9%", King's GDC findings.
- Remote config and experiment tool limits (Firebase, Statsig, PostHog, GrowthBook).
Record what was checked and when in the output.

## Reference index

- [Policy format](references/policy-format.md): the pxe 0.1 file, allowed inputs and actions, forbidden names, checker rules, engine guarantees.
- [Difficulty measurement and calibration](references/difficulty-measurement-and-calibration.md): outcome metrics, ratings, bot playtests, reading the difficulty table.
- [Difficulty curves and level design signals](references/difficulty-curves-and-level-design-signals.md): sawtooth pacing, hard level labels, mechanics introduced alone, first session.
- [Fair randomness and solvability](references/fair-randomness-and-solvability.md): seeds, bag randomizers, drought caps, solvable boards, shared seeds.
- [Adaptive policy design](references/adaptive-policy-design.md): rule patterns, thresholds, transparency copy, settings, audit log, shipping revisions.
- [Sessions, opens and return reasons](references/sessions-opens-and-return-reasons.md): what top games do, allowed versions, next goals, return reasons, minors.
- [Player modeling and churn](references/player-modeling-and-churn.md): features, churn definitions, model families, the help only rule.
- [Experiments and measurement](references/experiments-and-measurement.md): holdouts, metrics, guardrails, read windows.
- [Ethics, law and store rules](references/ethics-law-and-store-rules.md): verdicts, red and green lists, the rules behind them.
- [Architecture and telemetry](references/architecture-and-telemetry.md): components, events, privacy, porting, mode gate.
- [Audit checklist](references/audit-checklist.md): scored audit.
- [Playbooks](references/playbooks.md): common situations step by step.
- [Sources](references/sources.md): numbered sources with dates and labels.
- [Engine README](engine/README.md): the reference implementation.
