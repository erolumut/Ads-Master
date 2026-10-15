# Content Cadence and Difficulty Signals

> Knowledge as of 2026-10. The Royal Match cadence comes from its store release notes as listed by a third party archive [Reported, 2026-10]; other teardown facts are [Reported, 2026-10] or [Unverified] as marked. Level funnel definitions follow the game analytics conventions in the 2026-10-12 research notes and are owned by `measurement`. This module never designs levels or tunes difficulty: it measures, flags and hands the evidence to the game repo.

Gate: cadence plans, runway reports and difficulty flags are G1. A content drop going live, a change to a release date players were told, or a remote config change that reaches players is G3. Level parameters are never changed by Ads Master (outside its boundary).

## 1. The cadence principle

A fixed, predictable rhythm of new content keeps players planning their return around it; irregular big drops create spikes and long empty middles [Practitioner consensus].

| Example | Cadence | Label |
|---------|---------|-------|
| Royal Match | Release notes repeat "new levels every two weeks", about 100 new levels per update, usually with a new area or event; uploads in early 2026 landed roughly two weeks apart but not on a strict schedule | [Reported, 2026-10] |
| Royal Match level count | More than 12,400 levels by November 2025 | [Reported, 2026-10] |
| Daily puzzles (Wordle, LinkedIn games, NYT) | New content every day at a fixed tick | [Reported, 2026-10] |
| Color Block Jam | Reportedly grew with little live ops and heavy paid UA; early levels nearly ad free | [Unverified, vendor source] |

Rules:
1. Announce the cadence and keep it. A player told "new levels every other Thursday" plans around it; a slip costs trust more than a smaller drop would.
2. Separate content from code. Content that can ship as data (level files, puzzle seeds, event configs) through the server or remote config does not wait for a binary review; code changes ship in builds [Practitioner consensus]. The game repo decides what is data.
3. Every drop has a calendar row, a store decision (in-app event Major Update or Premiere badge, Play promotional content, or none) and a read.

## 2. Content runway

Runway answers: how long until the most engaged players run out of content?

| Term | Definition |
|------|-----------|
| Content ready | Levels, puzzles or event content built, tested and approved, not yet live |
| Frontier | The last available level (or the last scheduled day for seeded daily content) |
| Frontier share | Players at the frontier (completed the last available level) / DAU |
| Consumption rate | Levels per week completed by the fast segment (for example the 90th percentile of active players' weekly progress) |
| Runway (weeks) | (Frontier level minus the fast segment's current level, plus content ready) / consumption rate of the fast segment |

Worked example (illustrative): the 90th percentile player is at level 2,320, the frontier is 2,400, 100 levels are ready, and that segment completes 45 levels a week. Runway = (2,400 minus 2,320 plus 100) / 45 = 4.0 weeks. With a two week cadence, that is two drops of slack.

Rules:
- Runway of at least two release cycles for the fast segment [Practitioner heuristic].
- A rising frontier share is a content problem, not a difficulty problem: players waiting at the wall churn for a different reason than players stuck on a hard level (section 5.3).
- Daily seeded games have near infinite runway in volume but finite runway in quality and variety; the runway check becomes "days generated, validated and reviewed ahead" (the game repo's pipeline).

## 3. Cadence by game type

| Game type | Content unit | Typical rhythm | Runway check | Store moment |
|-----------|--------------|----------------|--------------|--------------|
| Daily social mini game | One seeded round per day per mini game; new mini games occasionally | Daily, plus a new theme or mini game each season | Days validated ahead; variety across the season | New Season badge for seasons; Premiere for a new mini game |
| Level based puzzle | Level packs, new areas, new obstacles | Fixed interval (two weeks is the reported hit rhythm) | Weeks of levels ahead of the 90th percentile | Major Update when a pack adds a real new area or mechanic |
| Hybrid casual | Modes, skins, short level sets | Monthly or by test result | New mode pipeline | Rarely |
| Board and multiplayer | New games, variants, puzzles, tournament formats | New game as a major moment; daily puzzle daily; tournaments weekly | Games in development, puzzle scenarios ahead | Premiere for a new game; Competition for a tournament |
| Web or PWA first | Same | Same; no store review wait for content or code | Same | Own site, share pages, communities |

## 4. Difficulty signals (what liveops reads)

Liveops reads the level funnel and the daily funnel that `measurement` publishes. Definitions below are summaries; `METRICS.md` wins.

### 4.1 Level based games

| Signal | Definition | What it says | Trap |
|--------|-----------|--------------|------|
| Completion rate | Players who completed level N / players who reached N | How many get through | Ignores how many tries it took |
| Attempts per completion | Attempts on N / players who completed N | Effort | A designed hard level is supposed to be high |
| Fail rate | Failed attempts / attempts | Difficulty | Fails are not quits |
| Quit rate | Attempts abandoned without a result / attempts | Frustration or confusion | Needs a quit event; the last session lacks an end event |
| Churn at level | Players whose last level reached is N and who were inactive 7 or more days / players who reached N, counting only players who reached N at least 7 days before the as of date | Where players leave | Censoring: recent players have not had 7 days to churn; the frontier inflates it |
| Continue and booster use | Continues or boosters used on N / attempts on N (from `game-monetization`) | Where players pay or watch to pass | A spike here with a churn spike is a difficulty paywall risk |
| Time per attempt | Median seconds per attempt | Clarity and effort | Long times can mean the goal is unclear |

### 4.2 Daily games

| Signal | Definition | What it says |
|--------|-----------|--------------|
| Daily completion rate | Players who completed today's round / players who started it | Today's difficulty for everyone at once |
| Tries used | Distribution of counted tries used | Whether the day was harder than usual |
| Solve time | Median time to complete | Effort |
| Share rate | Shares / completers | Days players are proud of share more |
| Day over day return | Players active on day d and d+1 / players active on day d | Whether a hard day cost tomorrow |
| Churn after day | Players whose last active day was d and who were inactive 7 or more days / players active on d | Whether a day ended relationships |

A daily game has one level a day that everyone plays: a bad day hits all players at once, so the daily funnel is read every morning (cadence in the skill).

## 5. Flag rules

### 5.1 Principles

1. **Flag on leaving, not on failing.** Hit puzzle games design near miss fails on purpose (Royal Match reportedly designs levels to be lost by 1 to 2 moves [Reported, 2026-10]). A fail spike alone is often the design working. Churn and quit spikes are the signal; attempts spikes are context.
2. **Compare with neighbors, not with the game average.** Difficulty is a saw tooth by design; a level is suspicious when it is far above the levels around it.
3. **Absolute and relative.** A churn rate twice its neighbors' median that is still 0.2 points above them is noise; require both a ratio and an absolute gap.
4. **Minimum sample.** Below a minimum number of players reaching the level, report "low sample", never a flag.
5. **Mature cohorts only.** Churn needs the inactivity window to pass; use players who reached the level at least 7 days before the as of date.
6. **Frontier is not difficulty.** Churn at the last available levels is a runway problem (section 2).
7. **Split payers and non payers when a monetization signal moves.** Difficulty tuned to sell boosters is a monetization design choice; liveops flags the risk to `game-monetization` and the game repo, it does not judge or tune it. Color Block Jam is reported to tune difficulty for booster purchases [Unverified, vendor source].

### 5.2 Default thresholds (starting points, tune per game)

These are [Practitioner heuristic] defaults for `level_flags.py`; record the values used in every flag so reads are comparable.

| Flag | Rule | Severity |
|------|------|----------|
| `churn_spike` | Churn rate at least 2.0 times the neighborhood median and at least 1.0 point above it; not frontier; sample met | High |
| `frontier_wall` | Churn condition met inside the frontier band (last 10 levels by default) | Medium (runway) |
| `quit_spike` | Quit rate at least 2.0 times the neighborhood median and at least 2.0 points above it | Medium |
| `attempts_spike` | Attempts per completion at least 2.0 times the neighborhood median | Low alone; Medium with a churn or quit spike |
| `continue_pressure` | Continues per attempt at least 2.0 times the neighborhood median | Medium; hand to `game-monetization` |
| `funnel_inconsistent` | More players reached level N+1 than completed N (beyond 2%), or completed above reached, or churned above reached | Data error: fix the export first |
| `low_sample` | Players reached below the minimum (200 by default) | Info |

Neighborhood: up to 5 levels on each side with enough sample; at least 3 neighbors needed, otherwise "no context".

### 5.3 Reading a churn spike

| Pattern | Likely cause | Who acts |
|---------|--------------|----------|
| Churn spike plus quit spike, attempts normal | The goal or a mechanic is unclear, or a bug | Game repo (UX, bug check); attach session replays if the game has them |
| Churn spike plus attempts spike | Too hard relative to neighbors | Game repo (difficulty review) |
| Churn spike plus continue pressure | Difficulty paywall risk | Game repo and `game-monetization` together |
| Churn spike only, everything else normal | A new mechanic introduced, a tutorial gap, a long session cliff, or an outside cause (release, outage) | Game repo; check the release and incident log first |
| High churn in the frontier band | Out of content | Liveops (runway), game repo (pipeline) |
| Spike appears in one cohort only | UA source or market mix, app version | `measurement` and `mobile-app-growth` |

## 6. The difficulty flag (format sent to the game repo)

The flag is evidence and a question, not a fix.

```
# Difficulty flag: <product>, level <N> (or day <d>), <date>
Severity: high | medium | low
Data: <export name from measurement>, players reached <n>, cohort window <dates>, as of <date>, segment <all | non payers | payers>
Signals vs neighborhood median (levels <a> to <b>):
  churn at level <x%> vs <m%> (ratio <r>)
  quit rate <...>   attempts per completion <...>   continue use <...>
Frontier: no | yes (frontier share <...>)
What else changed: release <version/date>, event live <id>, incident <id>, UA mix <note>
Hypotheses (ranked): unclear goal | difficulty spike | bug | new mechanic | content end | outside cause
Evidence attached: funnel chart, replays or screenshots if available
Not recommended by Ads Master: any change to level parameters (outside our boundary)
Question for the game repo: <one sentence>
Follow up: liveops re-reads <date> after the game repo's decision
```

File it at `ads-master/outputs/game-liveops/YYYY-MM-DD_game-liveops_difficulty-flag-<level>.md`, add a journal entry and, if the product keeps one, link it in the game repo's issue tracker through the human.

## 7. level_flags.py

`<skill>/scripts/level_flags.py` reads a level (or day) funnel CSV exported by `measurement` and prints the flags in section 5.2. Standard library only; run with `python3 -I`.

Input columns (header row, one row per level or day):

| Column | Required | Meaning |
|--------|----------|---------|
| `level` (or the column named by `--key`, for example `day`) | Yes | Integer level index or day number |
| `players_reached` | Yes | Players who started the level at least once |
| `players_completed` | Yes | Players who completed it |
| `attempts` | Yes | Attempts on the level |
| `churned` | Yes | Players whose last level was this one and who were inactive 7 or more days (mature cohort) |
| `quits` | No | Attempts abandoned without a result |
| `continues` | No | Continues or boosters used on the level (from the monetization events) |

Options: `--key`, `--window` (default 5), `--min-reached` (200), `--churn-ratio` (2.0), `--churn-gap` (0.01), `--quit-ratio` (2.0), `--quit-gap` (0.02), `--attempts-ratio` (2.0), `--continue-ratio` (2.0), `--frontier` (10; 0 for daily games), `--json <path>` to write the flags for the flag document.

Exit codes: 0 no high severity flag and no data error; 1 a `churn_spike` or a data error; 2 could not run (file missing, required columns missing, non numeric values).

Example:

```
python3 -I <skill>/scripts/level_flags.py ads-master/data/imports/level_funnel_2026-10-12.csv --frontier 10
python3 -I <skill>/scripts/level_flags.py ads-master/data/imports/daily_funnel.csv --key day --frontier 0 --min-reached 500
```

The script ranks anomalies; it does not explain them. A flag goes to the game repo only with the context in section 6.

## 8. Daily content checks (owned by the game repo, read by liveops)

Before a seeded day goes live, the game repo's pipeline should verify that the day is solvable, not a duplicate of a recent day, inside the intended difficulty band, free of offensive words (for word games) and safe to share without spoilers. Liveops does not run these checks; it asks for the pipeline's status in the weekly loop and reads the day's funnel the next morning. A day that broke the daily completion rate is flagged with the section 6 format (day instead of level).

## 9. Anti patterns

| Anti pattern | Why it is wrong | Instead |
|--------------|-----------------|---------|
| "Level 212 is too hard, set moves from 25 to 28" written by Ads Master | Outside the boundary; the game repo owns difficulty | A flag with evidence and a question |
| Flagging every fail spike | Near miss design is intentional | Flag churn and quit spikes |
| Reading churn on last week's players | Censoring hides churn | Mature cohorts only |
| Treating the frontier as a hard level | Content end, not difficulty | Runway report |
| One average across payers and non payers | Payers pass paid walls; the average hides the wall | Split by payer status |
