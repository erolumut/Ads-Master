# Experiments and Remote Config

> Knowledge as of 2026-10. Firebase A/B Testing facts come from search summaries of the Firebase documentation (the page was not reachable from this environment) [Reported, 2026-10]. Game A/B practice (duration, novelty, holdouts) comes from the 2026-10-12 research notes on game analytics [Reported, 2026-10] and from practitioner consensus. Sample sizes in this module were computed for this file with the standard two proportion formula (alpha 0.05 two sided, power 0.8); they are arithmetic, not benchmarks. `measurement` owns metric definitions and the statistics of record; `cro` owns the general CRO test method this module adapts to games.

Gate: test plans and remote config drafts are G1. An unpublished config template or an experiment created but not started is G2. Starting, stopping or changing an experiment, publishing a config change that reaches players, rolling out a winner and turning a kill switch are G3. Monetization parameters (prices, caps, ad frequency) are tested with `game-monetization`, under its policy file and `policyRevision`.

## 1. What liveops tests

| Area | Example questions | Primary metric | Guardrails | With |
|------|-------------------|----------------|------------|------|
| Streak rules | Free rest days vs none; best streak shown | Recovery rate after a break; D7 | DAU, day over day return | Game repo |
| Daily tick and closure | Tick time; next tick shown at closure | Day over day return | Share rate | Game repo, `measurement` |
| Event formats | Milestone vs collection; ladder length | Event uplift vs holdout (sessions per DAU, D7 of starters) | Revenue per DAU, complaints | Game repo, `game-monetization` |
| Event cadence | One weekly event vs two | Weekly active days per player | Participation decay | Game repo |
| Season length and track | 21 days vs 28; free track length | Season completion; next season return | Pass conversion (with `game-monetization`) | Game repo, `game-monetization` |
| Cohort size | 30 vs 50 per competitive cohort | Event return across days | Share of cohorts won by top spenders (must be zero influence) | Game repo |
| Reminder timing | Habit time vs fixed time | Day over day return of opted in players | Opt out rate | `lifecycle-crm` |
| Unlock gates | Event unlock at level 10 vs 25 | D7, early churn | Event completion | Game repo |

Never tested: counted attempts per day, ranked scoring rules, anything that would give one arm a ranked advantage over the other on a shared board (contract section 3). Two arms on one ranked board must play under identical ranked rules.

## 2. Remote config discipline

| Rule | Why |
|------|-----|
| Every liveops tunable is a remote config key with a safe default in code | Change without a release; survive a config outage |
| Each event and season has a kill switch key | Stop a broken event in minutes (the monetization contract has its own `killSwitch` for offers and placements) |
| Keys are named by area and id (`liveops.event.<id>.enabled`, `liveops.streak.rest_days`) | Readable change logs |
| A config change that players notice is an experiment row or a G3 change request with a rollback | Cause and effect; approval |
| Staged rollout for risky changes (small share first, then wider) | Limits damage while watching guardrails [Practitioner consensus] |
| Ranked rules never change mid day | Fairness inside one day id; change at the tick only |
| Config and calendar agree | The calendar row id appears in the key or its note; `liveops_calendar_check.py` covers dates, not config |
| Record `calendar revision` with event telemetry | Reads can be tied to the calendar version, the way `policy_revision` ties revenue to the monetization policy |

Tools seen in game stacks (options, not endorsements): Firebase Remote Config with A/B Testing, Unity Gaming Services remote config and game overrides, GameAnalytics A/B testing, PostHog, GrowthBook or Statsig feature flags for web games, or the product's own feature flag table. Small studio default in the research notes: GameAnalytics or devtodev free tiers plus Firebase Remote Config, and PostHog for web games [Reported, 2026-10].

Firebase A/B Testing, per its documentation as summarized in search [Reported, 2026-10]: two weeks is the recommended minimum runtime for a typical Remote Config experiment; results update once a day; experiment data is processed for at most 90 days after the start, then the experiment stops automatically.

## 3. Test design

### 3.1 Unit of randomization

| Feature | Randomize by | Why |
|---------|--------------|-----|
| Single player rules (streak screen, reminders, unlock gates) | Player | No spillover |
| Anything players in a group, team or cohort see together (group boards, group streak view, team chest, encores, cohort size) | Group or team (cluster) | Members influence each other; splitting a group shows two rule sets on one screen and contaminates both arms |
| Ranked boards with scope `everyone` | Never split rules; test framing only | One board, one rule set |
| Store events | Not randomizable in the store; use pre and post or market holdouts with `measurement` | Store surfaces are shared |

Cluster tests need more players: the design effect is 1 + (m minus 1) x ICC, where m is the average cluster size and ICC the intra cluster correlation of the metric. With groups of 5 and an ICC of 0.05, the design effect is 1.2 (20% more players); with teams of 20 and the same ICC, 1.95 (almost double). Estimate the ICC from past data with `measurement`; when unknown, plan with 0.05 and report it [Practitioner heuristic].

### 3.2 Sample size (worked numbers)

Players needed per arm, alpha 0.05 two sided, power 0.8, two proportions (computed for this module):

| Baseline | Target | Absolute change | Players per arm |
|----------|--------|-----------------|-----------------|
| D7 10% | 12% | +2 points | about 3,841 |
| D7 10% | 11.5% | +1.5 points | about 6,693 |
| D7 5% | 6% | +1 point | about 8,158 |
| D1 40% | 43% | +3 points | about 4,233 |
| D1 40% | 42% | +2 points | about 9,492 |
| Season completion 25% | 27% | +2 points | about 7,549 |

For retention tests the unit is new or newly exposed players, so the binding constraint is players entering the test per week, not DAU. A product with 1,000 new players a week needs about 8 weeks to fill two arms of 3,841. That is why the adaptation matrix in the skill tells small products to test only large changes.

### 3.3 Duration

| Rule | Detail | Label |
|------|--------|-------|
| Full weeks | Run whole weeks so weekdays and weekends are balanced | [Practitioner consensus] |
| Minimum | One week minimum, two to four weeks typical in game testing; Firebase recommends two weeks minimum | [Reported, 2026-10] |
| Exposure plus outcome window | A D7 outcome needs 7 days after each player's exposure, so the read date is the last exposure plus 7 days | [Reported, 2026-10] |
| Novelty | Judge after the novelty window: compare the effect in week 1 with week 2 and later; an effect that fades is novelty | [Reported, 2026-10] |
| No peeking | Fix the sample and the read date in advance; stopping when a result looks good inflates false positives; use a sequential method only if planned | [Practitioner consensus] |
| Events | An event test covers at least two runs of the event, so one lucky week does not decide | [Practitioner heuristic] |

### 3.4 Checks before reading

1. Sample ratio mismatch: the split matches the plan (for example 50/50 within a chi square test); a mismatch means assignment or logging broke, so stop and fix.
2. Exposure logged: only players who actually saw the change count as exposed (intent to treat for the primary read, exposure for diagnosis).
3. Guardrails within limits: D1 and D7, sessions per DAU, revenue per DAU (with `game-monetization`), complaints and review themes.
4. Segment splits only when planned (new vs returning, payer vs non payer, market); unplanned splits are hypotheses for the next test.
5. Multiple metrics: one primary metric decides; secondary metrics explain.

Most tests fail, and that is normal: Block Blast was reported to run more than 50 A/B tests a week with about 97% failing [Unverified, single source], and Royal Match reportedly tested a lighter meta where the control won [Reported, 2026-10]. Velocity and kill rules matter more than any single test.

## 4. Experiment brief and EXPERIMENTS.md row

```
# Experiment brief: <id>, <product>, <date>
Hypothesis: If we <change>, then <primary metric> will <move by at least X>, because <evidence>.
Primary metric: <definition from METRICS.md>   Guardrails: <list with limits>
Unit: player | group | team   Split: <arms and shares>   Design effect: <value and ICC source>
Sample: <per arm, from section 3.2 or measurement's calculator>   Entry rate: <players per week>
Duration: <full weeks>   Read date: <last exposure + outcome window>
Config: <keys and values per arm>   Kill switch: <key>
Fairness: no ranked rule differs between arms; boards shared across arms: <none | list and why it is safe>
Minors: <arms are identical for minors | minors excluded>
Approval: G3 change request line <id>
Stop rule: <guardrail breach or SRM stops the test; no early win stop>
```

EXPERIMENTS.md row (append, update only your own rows; the example uses the illustrative numbers from [Daily loops and streaks](daily-loops-and-streaks.md) section 8):

| ID | Date | Agent | Hypothesis | Primary metric | ICE | Design | Stop rule | Status |
|----|------|-------|------------|----------------|-----|--------|-----------|--------|
| E041 | 2026-10-15 | game-liveops | If streak breaks keep a free rest day, recovery rate rises 5 points, because 82% of breaks end the relationship today | Recovery rate within 7 days | 4/3/4 | A/B by group, 50/50, 3 weeks | Guardrail: DAU down 2% or SRM | backlog |

## 5. Holdouts for event uplift

Participation tells you how many joined; only a holdout tells you what the event caused.

### 5.1 Per event holdout

- A share of eligible players (or groups) does not see the event. Compare the exposed and the holdout on the primary metric over the event window and the week after.
- Size the holdout from section 3.2 with unequal allocation. Detecting a change from 10% to 11.5% needs about 35,340 eligible players in total with a 10% holdout (about 3,534 held out), against about 13,380 with a 50/50 split; with a 5% holdout it needs about 66,528. Small products use a larger holdout share or read across several runs.
- Run the holdout on the first two runs of every new event type, then periodically (for example one run in four) to catch fatigue [Practitioner heuristic].

### 5.2 Program holdout

A small long term holdout that sees none of the liveops layer (events, seasons, reminders) for a quarter measures the whole program's effect, including cannibalization between events. Use it only where it is fair:
- Never hold anyone out of ranked play, the daily round, or anything a group shares.
- Never hold out players under 18 in a way that changes what they are offered; prefer excluding minors from holdouts entirely.
- Grant the holdout's missed free rewards after the read as an `admin` grant in the grant log (contract runbook rule 7), so no player is worse off for being in a test.

### 5.3 Reading uplift

| Metric | Formula | Note |
|--------|---------|------|
| Uplift | Exposed metric minus holdout metric, with a confidence interval | Absolute points for rates |
| Relative uplift | Uplift / holdout metric | For comparison across events |
| Incremental sessions | (Sessions per player exposed minus holdout) x exposed players | For cost and content value |
| Cannibalization | Change in other events' participation in the exposed arm | Stack crowding |

Store events cannot be randomized: read them with pre and post comparisons against the same weekday pattern, with `measurement` and `app-store-optimization` (event impressions, opens, downloads, redownloads in App Store Connect [Official, 2026-10]).

## 6. Decision rules

| Result | Decision |
|--------|----------|
| Primary metric up beyond the minimum effect, guardrails held, effect not fading in week 2 | Roll out (G3), staged; log the learning; memory entry after a second confirmation |
| Primary up, a guardrail breached | Do not ship; redesign to protect the guardrail |
| Flat (inside the minimum effect) | Keep the simpler or cheaper arm; do not rerun the same idea larger without a new reason |
| Down | Kill; note why in EXPERIMENTS.md |
| SRM, logging break, outage in the window | Invalid; fix and rerun |

## 7. Pitfalls

1. Randomizing group features by player.
2. Reading D7 before every exposed player has had 7 days.
3. Stopping on day 3 because the dashboard turned green.
4. Testing a ranked rule (counted attempts, scoring) as an experiment.
5. Treating event participation as uplift.
6. Holdouts that cost players rewards without compensation.
7. Ten simultaneous tests on overlapping players with no interaction plan.
8. A config change outside the change log, discovered from a support ticket.
