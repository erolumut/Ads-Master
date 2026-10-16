# Player Experience Audit Checklist (scored)

> Knowledge as of 2026-10 (research pass 2026-10-16). Score every item Pass, Partial or Fail with evidence (a build screen, an export with its date range, a policy file and its revision, checker output, a log sample). An item without evidence is a Fail. Items that do not apply (shared modes for a game without any, minors for an adult only product with verified age) are N/A and leave the denominator. The rubric matches the other Ads Master audits.

Severity weights: Critical 5, High 3, Medium 2, Low 1. Pass earns the full weight, Partial half, Fail 0. Auditing is G1: read only, nothing changes in the game or its config.

## A. Fair core

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | Every shared mode (daily, ranked, races, group and global boards, tournaments, derived boards) is declared `shared: true` | Shared modes never adapt | Policy file, mode list in the build | Critical | Declare; [policy design](adaptive-policy-design.md) section 2 |
| A2 | The engine returns no action in shared modes, and the server rejects offsets or assisted runs on shared boards | Mode gate in code, not convention | Conformance test, server code | Critical | [Architecture](architecture-and-telemetry.md) section 7 |
| A3 | Shared content uses server issued seeds and one pinned engine version per period | Same game for everyone | Server logs, build | Critical | [Fair randomness](fair-randomness-and-solvability.md) section 6 |
| A4 | Shared results are revalidated by replaying the move log on the same engine | A modified client cannot post an impossible result | Server code, test | High | Add revalidation |
| A5 | Scores are never changed after the fact; assisted runs are labeled and absent from shared boards | Scores are true | Policy `scores` block, build | Critical | Fix code and policy |

## B. Inputs and outcomes

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | `pxe_policy_check.py` PASS on the live policy revision | Mechanical floor | Checker output with date | Critical | Fix FAILs |
| B2 | No code path outside the policy reads spend, ad value, ad readiness, device value, location or personal traits to change difficulty, draws or outcomes | The checker cannot see code that ignores the file | Code search for forbidden tokens near game core and offer code; review with the game repo | Critical | Remove; [ethics](ethics-law-and-store-rules.md) red list |
| B3 | Rigged stream test (regenerate streams from logged seeds; compare ad watching and non ad watching players) run in the last 90 days | Proves no hidden steer | Test report | High | [Fair randomness](fair-randomness-and-solvability.md) section 5.3 |
| B4 | No engineered near misses; no unwinnable boards | Red list | Generator spec, solver report | Critical | Solver gate; remove near miss tuning |
| B5 | Struggling players get help (hint, break, one eased step), never harder content | Help, never harvest | Policy rules, log sample | High | Rewrite rules |

## C. Randomness and solvability

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | All game randomness from a seeded integer generator; no `Math.random()` or clock in the game core | Replay and parity | Code search, golden vectors | High | Use the engine `rng.js` |
| C2 | Golden vectors pass on every shipped platform | Cross platform parity | CI output | High | [Architecture](architecture-and-telemetry.md) section 5 |
| C3 | Drought cap written and tested | Fairness at the tail | Generator spec, test | Medium | Bag randomizer |
| C4 | Every served board proven solvable | Floor of fairness | Solver report | High | Solver gate |
| C5 | Generator, bag or solver changes bump `engineVersion` | Old runs stay reproducible | Changelog | Medium | Version discipline |

## D. Difficulty measurement

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Pass rate, attempts to pass, first try pass and quit or churn per level are defined in `METRICS.md` | One definition | METRICS.md | High | Request to `measurement` |
| D2 | `difficulty_table.py` (or an equivalent) run in the last 14 days on unassisted attempts for one mode and engine version, thresholds recorded | Current table | Output file, memory note | High | [Calibration](difficulty-measurement-and-calibration.md) section 6 |
| D3 | Level ratings exist (Elo or Rasch), with a sample floor; levels below it take no difficulty action | No action on noise | Level table | Medium | Calibration |
| D4 | New levels get bot priors or ship without difficulty actions until rated | Cold start | Table `prior` field | Low | Section 4 of calibration |
| D5 | Walls and unintended hard levels are filed to the game repo with evidence | Designer owns the curve | Flags in outputs | Medium | [Curves](difficulty-curves-and-level-design-signals.md) section 7 |

## E. Curve and first session

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Hard levels are labeled in game before they start | A labeled peak is a promise | Build | Medium | Label |
| E2 | Each new mechanic introduced alone, on an easy level | Learnability | Level list | Medium | Designer review |
| E3 | Rest levels follow peaks | Relief | Curve chart | Low | Designer review |
| E4 | First session: early levels winnable first try, no hard label, no offer before play, next goal shown | First session decides much of what follows | Build, funnel | High | Redesign first session |

## F. Policy and transparency

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Difficulty setting (`auto`, `easy`, `normal`, `hard`) reachable from pause or fail screens | Control that counts | Build | High | Move setting |
| F2 | "Why this level" line shown on every adapted level | Visible adaptation | Build | Critical | Add explain line |
| F3 | Player readable adaptation log and a reset | Apple 5.1.2(iii) | Build | High | Add |
| F4 | Explain texts have a `compliance` verdict | Customer facing copy | Compliance log | High | Review |
| F5 | At least one raising rule (the engine does not only ease) | Skilled players | Policy | Low | Add raise rule |
| F6 | Audit log carries policy revision, engine version, table version, rule id, reason; server sample configured | Traceability | Log sample | Medium | [Policy design](adaptive-policy-design.md) section 7 |
| F7 | Last 5 policy revisions shipped through a G3 change request with checker output | Control | Journal, actions log | High | Enforce |

## G. Sessions and return reasons

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Return reasons come from real content or the player's own state only | Honest opens | Return reason list | High | [Sessions](sessions-opens-and-return-reasons.md) section 5 |
| G2 | No guilt copy, no streak loss threats, caps and quiet hours on every reason | Pressure patterns | Copy, policy | High | Rewrite; cap |
| G3 | Sessions end with a next goal and a one tap exit; no exit interstitial | Clean stops | Build | Medium | Section 4 |
| G4 | Streaks have free automatic rest days and a permanent best; streaks never change difficulty | No punishment | Build | Medium | `game-liveops` streak rules |
| G5 | Sends handled by `lifecycle-crm` with consent and frequency rules | Ownership | Handoff record | Medium | Hand off |

## H. Minors

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | If minors can play (or age is unknown), `minorsTier: "strict"` | KIDS Act direction, AI Act Art 5 vulnerability | Policy, store rating | Critical | Set strict |
| H2 | Strict tier: no streak or loss return reasons, no daily return rewards, no variable paid rewards, profiling off by default, no ad SDK profiling | Section 8 of sessions | Build, SDK config | Critical | Remove |
| H3 | Break offers sooner in the strict tier | Respect the decision to stop | Policy | Medium | Tune |

## I. Experiments and privacy

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Persistent holdout 1 to 20 percent, sized by power | Proof that adaptation helps | Policy, power note | Critical | [Experiments](experiments-and-measurement.md) section 2 |
| I2 | Fun proxies and guardrails read with primary metrics | Performance is not fun | Last read report | High | Add metrics |
| I3 | SRM check on every read; reads at 8 to 12 weeks | Valid reads | Read reports | High | Method |
| I4 | Telemetry consent gated; pseudonymous install id; no ad, device or location ids on engine events | Apple 5.1.1, privacy | Tracking plan, SDK config | Critical | [Architecture](architecture-and-telemetry.md) section 4 |
| I5 | Privacy policy names adaptation and the events used | Apple 5.1.1 | Privacy policy | High | Update with `compliance` |
| I6 | Any churn model has a model card and uses only allowed features | Help only rule | Model card | High | [Player modeling](player-modeling-and-churn.md) section 8 |

## Audit report template

```
# Player experience audit: <product>, <platforms>, <date>
Data used: <exports, builds, policy revision, engine version, date ranges>; Freshness check: <date>
Game type and modes: <type>; shared modes <list>; private modes <list>
Score: <overall %>, grade <A to F>; section scores A to I
Critical fails (first)
Top 5 fixes (impact x confidence x ease)
Findings by section (item, result, evidence, fix)
Checker output: pxe_policy_check.py <PASS | FAIL>, cannot cover sentence quoted
Difficulty table: difficulty_table.py run <date>, thresholds <values>, flags <list>
Change requests (G3 lines)
Handoffs requested (game repo, compliance, lifecycle-crm, measurement, game-monetization)
Data gaps and [Unverified] items
```

## Quick audit (30 minutes, cold start)

Score these first and list the rest as data gaps: A1, A2, A5, B1, B2, F2, H1, H2, I1, I4.

## Scoring example

Section F with F1 (High 3, Pass), F2 (Critical 5, Partial: explain line on eased levels only, missing on raised ones), F3 (High 3, Fail), F4 (High 3, Pass), F5 (Low 1, Pass), F6 (Medium 2, Pass), F7 (High 3, Partial): earned = 3 + 2.5 + 0 + 3 + 1 + 2 + 1.5 = 13; possible = 3 + 5 + 3 + 3 + 1 + 2 + 3 = 20; section score 65%.

## Scoring rubric

1. Section score = sum of earned weights / sum of possible weights for applicable items (Pass = weight, Partial = half, Fail = 0).
2. Overall score = sum of earned weights across all sections / sum of possible weights.
3. Grades:

| Overall | Grade | Meaning |
|---------|-------|---------|
| 90% to 100% | A | Honest, measured adaptation; focus on experiments and content |
| 75% to 89% | B | Solid; fix High items within 30 days |
| 60% to 74% | C | Gaps in control or measurement; fix Critical and High items before new rules |
| 40% to 59% | D | Foundations missing (mode gate, holdout, transparency); stop adapting until fixed |
| under 40% | F | Turn adaptation off (kill switch) and rebuild from the minimal first version |

4. Override: any Critical item at Fail caps the grade at C and goes first in the report, whatever the total. A Fail on A2, B2 or B4 is also an incident: log it in `ads-master/INCIDENTS.md` and recommend the kill switch until fixed.
