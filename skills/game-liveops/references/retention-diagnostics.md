# Retention Diagnostics

> Knowledge as of 2026-10. KPI definitions are owned by `measurement` (its game KPI dictionary and `game_kpis.py`, and the project's `ads-master/METRICS.md`); this module reads them and says what to do with them. Benchmarks come from secondary summaries of vendor reports [Reported, 2026-10] and vary by genre, market, platform, traffic source and season; compare a product with its own history first and benchmarks second.

Gate: diagnostics, memos and flags are G0 and G1. Any fix that reaches players goes through its own module and a G3 change request.

## 1. The KPIs liveops reads

| KPI | Definition (summary; METRICS.md wins) | Trap |
|-----|---------------------------------------|------|
| D1, D7, D30 (classic) | Players active on exactly day N after install / players installed that day, by install cohort; install is the first activity day in the project's timezone; a cohort counts for day N only when day N is complete | Rolling or return retention (day N or later) is a different, higher number; calendar day vs 24 hour windows differ; installs at 23:55 inflate calendar D1; tools disagree on the install event and the timezone |
| Stickiness | Average DAU over 30 days / MAU of the same 30 days | Falls during UA spikes (many new players, not a habit problem) |
| DAU, WAU, MAU | Distinct players with a qualifying activity event per day, rolling 7 and 30 days | Define "active" once; a server notification is not activity |
| Sessions per DAU, session length | Sessions / DAU; median session length | The last session lacks an end event; use medians |
| Event participation | Participants / average DAU over the event window | Participation is not uplift |
| Season completion | Players who reached the final free tier / season participants | Define "participant" (any season progress) before the season starts |
| Churn by level | Players whose last level was N and who were inactive 7 or more days / players who reached N | Censoring: players need 7 days to count; the frontier inflates it |
| Day over day return (daily games) | Players active on day d and d+1 / players active on day d | The daily loop's own curve |
| Resurrection | Players returning after 14 or more inactive days / players inactive 14 or more days at the start of the period | The return side of churn; events and store events aimed at lapsed users move it |

Liveops never redefines a KPI. A definition it needs that `METRICS.md` lacks goes to `measurement` as a request with the proposed formula.

## 2. Benchmarks (context only)

| Metric | Value | Source | Caveat |
|--------|-------|--------|--------|
| D1, D7, D30 medians (mobile games, data to end 2024) | About 22%, 3.4% to 3.9%, about 0.7%; top 10%: about 40%, 12%, 4% | GameAnalytics 2025 report via a secondary summary [Reported, 2026-10] | Vendor sample of games using its SDK; genre mix unknown |
| D1, all genres, 2025 | 27% | Adjust gaming insights 2026 via search [Reported, 2026-10] | Vendor sample, method differs from GameAnalytics |
| Session median and sessions per day | 5 to 6 minutes, about 4 sessions a day | Research notes [Unverified] | Single summary |
| Soft launch gates often quoted | D1 above 40% casual, above 35% midcore; D7 above 20% casual; D30 5% to 15% | Practitioner guides via search [Reported, 2026-10] | These are top decile numbers next to the medians above |

Rules for using them:
1. A daily social game behaves like a daily puzzle or a habit app, not like a level based casual game; casual puzzle gates (D1 40%) are not applied to it blindly (proposal decision). Build its gates from its own first cohorts and from daily product analogs.
2. Benchmarks are context in a report, never a target in a plan without a DECISIONS.md entry.
3. Two vendor medians that differ by 5 points for the same metric show the size of the method gap; the same gap can exist between two dashboards in one company.

## 3. Reading cohorts

### 3.1 The cohort triangle

Rows are install weeks (or days), columns are D1, D3, D7, D14, D30. Read it three ways:

| Read | Question | Typical cause of a change |
|------|----------|---------------------------|
| Down a column | Did newer cohorts retain worse at the same age? | UA mix, a release, onboarding, a store page promise the game does not keep |
| Along a row | Where in its life does a cohort fall off? | D1: first session; D1 to D7: early loop and content; D7 to D30: meta, events, seasons, social |
| Diagonals (calendar dates) | Did every cohort dip on the same dates? | An outage, a bad daily round, an event ending, a holiday, a tick change |

### 3.2 Mix before blame

Before any retention change is called a product problem, split the cohort by:
- Acquisition source (organic, paid network, campaign, share links, store featuring) with `mobile-app-growth` and `measurement`.
- Market and platform (web, iOS, Android).
- App version.
- Entry point (a share link landing on today's round retains differently from an ad install).

If every segment held and only the mix moved, the blended curve fell because of mix, not because the game got worse. Report the mix, do not change the game.

### 3.3 Stage decomposition

| Stage | Window | Main levers | Owner of the fix |
|-------|--------|-------------|------------------|
| First session | Install to end of first session | Tutorial, time to fun, load time, first result | Game repo |
| Day 1 | First 24 to 48 hours | Reason to return tomorrow (the daily loop), first reminder permission ask after value | Game repo, `game-liveops`, `lifecycle-crm` |
| Early loop | D1 to D7 | Daily content, streak rules, first event, first group or team join, difficulty curve | Game repo, `game-liveops` |
| Habit | D7 to D30 | Events, seasons, social structures, content cadence | `game-liveops`, game repo |
| Long term | D30 and later | Seasons, leagues, content runway, community | `game-liveops`, game repo |
| Store and UA promise | Before install | Ads and store page that show the real game | `creative-strategy`, `app-store-optimization`, `mobile-app-growth` |

## 4. Symptom tree

| Symptom | First checks | Likely causes | Next step |
|---------|--------------|---------------|-----------|
| D1 down for new cohorts | Mix (3.2), release notes, crash and load metrics, store page changes | UA source shift, a build regression, a promise gap in ads | Hand mix to `mobile-app-growth`; build issues to the game repo; promise gaps to `creative-strategy` |
| D7 down, D1 stable | Daily loop metrics, streak break and recovery rates, first event timing, level churn D1 to D7 range | Early content too hard or too thin, streak punishment, first event too late, no group joined | Playbook: rescue falling D7 ([Playbooks](playbooks.md)) |
| D30 down, D7 stable | Event participation decay, season completion, frontier share, team health | Event fatigue, runway, dead teams | Rotate formats, runway report, team health actions |
| Stickiness down, DAU up | New player share | UA spike | Read cohort curves, not stickiness |
| Stickiness down, DAU flat | Sessions per DAU, day over day return | Habit weakening: content or loop | Daily loop audit |
| Participation down across events | Repeat decay, stack crowding, unlock gates | Fatigue, too many events, gates too high | Rest formats, one event per scale |
| Season completion down | Final tier distribution, join week, active days | Track too long, late joiners, catch up missing | Track sizing ([Events and seasons](events-and-seasons.md) section 6.4) |
| Churn spike at one level | `level_flags.py`, release, incident | Difficulty, bug, unclear goal | Difficulty flag to the game repo |
| Churn wall at the last levels | Frontier share | Out of content | Runway report |
| A bad day in a daily game | Daily completion, tries used, share rate, churn after the day | The round was too hard or broken | Day flag to the game repo; consider an `admin` compensation only through the grant log |
| Reminder opt outs rising | Send volume per player, step down rules | Fatigue | `lifecycle-crm` |
| Lapsed players not returning after events | Resurrection, store event purpose settings | Events not reaching lapsed players | Apple purpose "bring back lapsed users", Play lapsed targeting [Reported, 2026-10], `lifecycle-crm` winback |

## 5. Churn by level

1. Get the level funnel from `measurement` (the churn by last level table of `game_kpis.py`, or the level dashboard export with completions, attempts and quits).
2. Confirm cohort maturity: churn counts only players who had at least 7 days to come back.
3. Run `level_flags.py` ([Content cadence and difficulty signals](content-cadence-and-difficulty-signals.md) section 7).
4. Separate frontier walls (runway) from churn spikes (difficulty, bug, clarity).
5. Split payers and non payers when a monetization signal moved.
6. File a difficulty flag per spike with the context; never a parameter change.
7. Re-read after the game repo's decision ships, on mature cohorts only.

## 6. What to flag to the game repo, what liveops fixes, what goes elsewhere

| Finding | Liveops action | Game repo | Other agent |
|---------|----------------|-----------|-------------|
| Churn or quit spike at a level or day | Flag with evidence | Decides and fixes difficulty, clarity, bugs | `game-monetization` if continue pressure |
| Frontier wall | Runway report, cadence plan | Content pipeline | |
| Streak punishment | Streak rule change set | Implements | `compliance` for copy |
| Event fatigue | Format rotation, calendar change | Implements formats | |
| Season track too long | Track sizing proposal | Implements | `game-monetization` (pass value) |
| Dead groups and teams | Health actions spec | Implements | |
| Reminder fatigue | Reminder moment changes | | `lifecycle-crm` |
| UA mix shift | Report | | `mobile-app-growth`, `measurement` |
| Store promise gap | Report review themes | | `app-store-optimization`, `creative-strategy` |
| KPI definition gap | Request | | `measurement` |

## 7. Data request to measurement

```
Data request: <product>, game-liveops, <date>
Tables: (1) classic D1, D7, D30 by install day and week, split by source, market, platform, app version;
(2) DAU, WAU, MAU and stickiness daily; (3) level or day funnel with players reached, completed,
attempts, quits, churned (7 day inactivity, mature cohorts), continues; (4) event participation
and completion per calendar row id; (5) season progress distribution and completion;
(6) streak distribution, break and recovery rates; (7) resurrection after 14 days
Timezone and day id rule: <as in METRICS.md>
Window: <dates>   Holdout flags: <experiment ids>
Definitions: METRICS.md rows <names>; missing rows proposed: <formulas>
```

## 8. Weekly retention memo template

```
# Weekly retention memo: <product>, week <YYYY-Www>
Data: <source, date range, METRICS.md definitions, timezone>
FACTS
- D1 / D7 / D30 of mature cohorts vs the 8 week median (classic): <...>
- Stickiness: <...> (new player share <...>)
- Daily loop: completion, day over day return, share rate, streak recovery: <...>
- Events live: participation, completion, uplift vs holdout where read: <...>
- Season: progress distribution vs plan: <...>
- Level or day flags this week: <list with severity>
INTERPRETATION
- <stage where the change sits; mix vs product>
RECOMMENDATION (gate per line)
- <G1 drafts, G3 change requests>
Handoffs requested: <slugs and briefs, or none>
```

## 9. Mistakes to prevent

1. Comparing classic D7 from one tool with rolling D7 from another.
2. Reading last week's cohort at D7 before day 7 is complete.
3. Calling a mix shift a product decline.
4. Using casual puzzle gates for a daily social game.
5. Averaging retention rates across markets instead of summing numerators and denominators.
6. Reporting participation as the event's success.
7. Fixing a frontier wall with difficulty changes.
