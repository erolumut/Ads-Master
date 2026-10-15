# Liveops Audit Checklist (scored)

> Knowledge as of 2026-10. Score every item Pass, Partial or Fail with evidence (a build screen, an export, a file and its date). An item without evidence is a Fail. Items that do not apply (store items for a web only product, teams for a product without teams) are N/A and leave the denominator. The rubric is at the end and matches the other Ads Master audits.

Severity weights: Critical 5, High 3, Medium 2, Low 1. Pass earns the full weight, Partial half, Fail 0.

## A. Measurement readiness

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | D1, D7, D30 (classic), stickiness, participation, season completion and churn by level are defined in `METRICS.md` with timezone and day id rule | Every read depends on one definition | METRICS.md rows | Critical | Request to `measurement` ([Retention diagnostics](retention-diagnostics.md) section 7) |
| A2 | Level or day funnel available with reached, completed, attempts, quits and churned on mature cohorts | Difficulty flags need it | Export or dashboard | High | Data request |
| A3 | Liveops telemetry (event shown, joined, progressed, completed, reward claimed; streak and share events) in the tracking plan | No event, no read | Tracking plan | High | Propose names to `measurement` |
| A4 | Calendar revision or event id carried on liveops events | Reads tie to the calendar | Event properties | Medium | Add property |

## B. Daily loop and streaks

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Daily promise written in one sentence and tested on new players | Players read nothing | Doc, test notes | Medium | Write and test |
| B2 | Server side day id; one rule shared by streaks and boards; next tick shown in local time | Fairness, support load | Build, METRICS.md | High | Day id rule ([Daily loops](daily-loops-and-streaks.md) section 2.2) |
| B3 | Share artifact spoiler free, plain text first, with a referral parameter, no reward for sharing | Organic growth, platform policy | Build, link test | High | Checklist 2.4 |
| B4 | A broken streak keeps everything earned; best streak shown permanently | No punishment | Build | Critical | Streak rules 3.2 |
| B5 | Rest days free, automatic and equal for all; `streak_protection` declared competitive or not | Contract and fairness | Build, monetization policy | High | Declare and fix |
| B6 | No paid or ad gated streak repair (or a recorded G3 product decision with compliance, never for minors, never with a competitive streak) | Pressure pattern | Build, DECISIONS.md | High | Remove or document |
| B7 | Login calendar cumulative, never reset on a missed day | Absence punishment | Build | Medium | Cumulative form |
| B8 | Notification permission asked after value, with no reward for granting it | Apple 5.1.2(i), grant rate | iOS and Android builds | High | Move the ask; remove rewards |

## C. Events and seasons

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | At most one event per time scale live at once | Stack crowding | Calendar, checker warnings | Medium | Re-plan |
| C2 | Every event has a free path a non payer can finish; premium never gates the free track | Fairness, consumer law | Event specs, build | Critical | Redesign ladders |
| C3 | Competitive formats declare a ranked board fed only by play no purchase changes | Contract ranked rule | Specs, monetization policy, `monetization_check.py` | Critical | Milestone version or dedicated event levels |
| C4 | Event spec exists for every event type (section 3 of the events module) | Implementation quality | Specs folder | Medium | Write specs |
| C5 | Every new event type read against a holdout in its first two runs | Uplift, not participation | EXPERIMENTS.md | High | Add holdouts |
| C6 | Season length chosen from the product's own rhythm; free track completion target declared and read | Completion, fairness | Season plan, reads | Medium | Size from data |
| C7 | Earned season currency expires only with clear notice; purchased currency never expires | Apple 3.1.1, consumer law | Build, economy sheet | Critical | Fix with `game-monetization` |
| C8 | Event reads filed within 7 days after each event | Learning loop | Reads table, outputs | Medium | Weekly loop |

## D. Social structures

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Group or team health measured (active members, solo rate, healthy group share) | Social retention base | Dashboard | Medium | Request metrics |
| D2 | Leagues and team ranks never fed by purchasable play | Contract | Specs | Critical | Redesign |
| D3 | No absence penalties in teams or leagues (paused, not demoted) | Punishment | Rules | High | Soft rules ([Teams](teams-groups-and-leagues.md) section 5) |
| D4 | Group copy never names who broke a group streak | Social pressure, minors | Build | High | Counts only |
| D5 | Bots disclosed or absent in competitive cohorts | Trust | Build | High | Disclose |
| D6 | Chat and UGC with filter, report and block (Apple 1.2) and minors defaults | Safety, review | Build, `compliance` | Critical | Fix before launch |

## E. Content cadence and difficulty signals

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Fixed, announced content cadence kept for the last 3 cycles | Trust, planning | Release history | Medium | Cadence plan |
| E2 | Content runway of at least two cycles for the fast segment | Frontier churn | Runway report | High | Pipeline with the game repo |
| E3 | `level_flags.py` (or the same rules) run weekly on mature cohorts | Early warning | Journal | High | Weekly loop |
| E4 | Every churn spike filed as a difficulty flag with evidence; no parameter changes proposed by Ads Master | Boundary | Outputs | High | Flag format |
| E5 | Frontier walls separated from difficulty spikes | Wrong fixes | Flags | Medium | Frontier band |

## F. Calendar and store events

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | `LIVEOPS_CALENDAR.md` exists, covers 3 months ahead, approved this month | Coordination | File | High | Template ([Calendar](liveops-calendar-and-store-events.md) section 9) |
| F2 | `liveops_calendar_check.py` exits 0 on the current calendar | Store limits | Script output | High | Fix FAIL rows |
| F3 | Apple events: right badge, deep link tested, no prices in metadata, within 31 days and 14 days of promotion | Rejection | App Store Connect, checker | High | Fix rows |
| F4 | No daily tasks or price only promotions submitted as in-app events | Poor candidates per Apple | App Store Connect | Medium | Remove |
| F5 | Play promotional content checked against the live console for the quarter | Rules [Reported] | Console notes | Medium | Verify |
| F6 | Game Center (store builds): leaderboards, a challenge on the daily or weekly board, activities with deep links | Games app surfaces | Build | Medium | Spec to the game repo |
| F7 | Store event dates match in-game dates (Guideline 2.3.13) | Rejection, trust | Calendar vs build | High | Align |

## G. Experiments and remote config

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Every liveops tunable is a remote config key with a safe default; each event has a kill switch | Speed, safety | Config template | High | Add keys |
| G2 | Group features randomized by group, not by player | Contamination | Experiment briefs | High | Cluster design |
| G3 | Tests sized in advance, run full weeks, read after the outcome window and novelty | Valid reads | EXPERIMENTS.md | High | Brief template |
| G4 | No experiment changes ranked rules between arms | Fairness | Briefs | Critical | Stop and redesign |
| G5 | Config changes logged as experiment rows or change requests | Cause and effect | Change log | Medium | Process |

## H. Player trust and minors

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | No countdown on offers; end dates shown as text | Pressure, contract | Build | High | Remove timers |
| H2 | Minors checklist passes ([Player trust](player-trust-and-pressure-patterns.md) section 3) | Law, stores | Checklist | Critical | Fix per item |
| H3 | No pop up offers at session start beyond what the policy allows | vzbv objection pattern | Build, policy | High | Move offers |
| H4 | Pressure audit run this season | Drift | Journal | Medium | Audit |

## I. Coordination

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Reminder moments requested through `lifecycle-crm`, opted in, capped, with step down rules | Consent, fatigue | Requests, journal | High | Request format |
| I2 | Event offers and pass prices come from `game-monetization`, with `monetization_check.py` passing | Ownership, fairness | Policy, outputs | High | Handoff |
| I3 | Every customer facing line (events, reminders intents, store metadata) has a `compliance` verdict | Law, stores | Compliance log | Critical | Review |
| I4 | Change requests with approvals exist for the last 5 live changes | Control | Journal, actions log | High | Enforce |

## Audit report template

```
# Liveops audit: <product>, <platforms>, <date>
Data used: <exports, connectors, builds, date ranges>; Freshness check: <date>
Game type, tier and maturity: <type>, <tier>, <stage>
Score: <overall %>, grade <A to F>; section scores A to I
Critical fails (first)
Top 5 fixes (impact x confidence x ease)
Findings by section (item, result, evidence, fix)
Difficulty flags filed (if any)
30, 60, 90 day plan
Change requests (G3 lines)
Handoffs requested
Data gaps and [Unverified] items
```

## Quick audit (30 minutes, cold start)

Score these first and list the rest as data gaps: A1, B4, B8, C2, C3, E2, F2, G4, H2, I3.

## Scoring example

Section B with B2 (High 3, Pass), B4 (Critical 5, Partial), B5 (High 3, Fail), B8 (High 3, Pass), B1 N/A and the rest Pass (B3 High 3, B6 High 3, B7 Medium 2): earned = 3 + 2.5 + 0 + 3 + 3 + 3 + 2 = 16.5; possible = 3 + 5 + 3 + 3 + 3 + 3 + 2 = 22; section score 75%.

## Scoring rubric

1. Section score = sum of earned weights / sum of possible weights for applicable items (Pass = weight, Partial = half, Fail = 0).
2. Overall score = sum of earned weights across all sections / sum of possible weights.
3. Grades:

| Overall | Grade | Meaning |
|---------|-------|---------|
| 90% to 100% | A | Mature liveops; focus on tests and new formats |
| 75% to 89% | B | Solid; fix High items within 30 days |
| 60% to 74% | C | Leaking retention; fix Critical and High items before adding events |
| 40% to 59% | D | Foundations missing (definitions, calendar, fairness); fix before any new event |
| under 40% | F | Rebuild the daily loop and measurement first |

4. Override: any Critical item at Fail caps the grade at C and goes first in the report, whatever the total.
