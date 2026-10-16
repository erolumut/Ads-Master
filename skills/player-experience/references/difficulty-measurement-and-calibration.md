# Difficulty Measurement and Calibration

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). Only developer.apple.com could be opened during the pass; every study below comes from search summaries of the named source and is labeled [Reported, YYYY-MM] or weaker until someone reads the paper. Formulas are standard methods, not findings. Thresholds marked "placeholder" are starting values to tune per game, never benchmarks.

Gate: reading exports, building a level table and writing a calibration report are G1. Publishing a new level difficulty table to remote config changes what players get and is G3 (change request with rollback). Level design itself belongs to the game repo.

## 1. Why measure from outcomes

A designer's intended difficulty and the difficulty players experience diverge. The engine can only adapt honestly if it knows how hard each level actually is, so the level table comes from play data first and opinion second.

| Evidence | What it supports | Label |
|----------|------------------|-------|
| King measures level difficulty from outcomes and pre tests levels with a CNN trained to play like humans; cheaper than MCTS and better correlated with average difficulty (Gudmundsson et al., IEEE CIG 2018) | Outcome based measures plus human like bots | [Reported, 2026-10] |
| King GDC "Sugary Statistics" (15,000 levels): a harder early level converted more in the short term, an easier version retained players longer; judge each level inside the whole progression | Judge levels on long run retention, not short term conversion | [Reported, 2026-10] |
| Rovio and Aalto (Roohi et al., CHI PLAY 2020): per level pass and churn predicted from RL agents plus a population simulation; 95k players, 168 levels; churn defined as 7 days inactive | Simulated players can predict per level churn before launch | [Reported, 2026-10] |
| Reguera et al., Scientific Reports 2020: engagement versus difficulty follows a power law across 12M Candy Crush players | Difficulty and engagement are linked, not linearly | [Reported, 2026-10] |
| Pelánek 2016 and Lichess Glicko 2: Elo style ratings estimate player skill and item difficulty together; puzzles need many attempts (research notes: hundreds of solves) for stable ratings | Joint ratings work, with a sample floor | [Reported, 2026-10] |

## 2. The five outcome measures

Every measure is per level, per mode, per engine version. Never pool a shared mode (daily, ranked) with a private mode: the private one may be adapted and the numbers then describe the policy, not the level.

| Measure | Definition | What it says | Trap |
|---------|-----------|--------------|------|
| Pass rate | Passed attempts / attempts | Raw difficulty of one attempt | Skilled players replay easy levels less, so the mix shifts |
| Attempts to pass | Attempts by players who passed / players who passed (median and p90) | Effort to get through | Ignores players who never passed; read with churn |
| First try pass | Players who passed on attempt 1 / players who attempted | Clarity of the level and its goal | Boosters and hints on attempt 1 inflate it; split assisted |
| Per level churn | Players whose last level reached is N and who were inactive for the churn window / players who reached N, mature cohort only | Where players leave | Censoring: recent players have not had time to churn; the content frontier inflates it |
| Quit rate | Attempts abandoned mid level / attempts | Frustration or confusion | Needs a `quit` event with level and move index; the last session often lacks an end event |

Definitions here are working drafts. `measurement` owns the final versions in `ads-master/METRICS.md` ([game KPIs](../../measurement/references/game-kpis.md)); `game-liveops` reads the same funnel ([difficulty signals](../../game-liveops/references/content-cadence-and-difficulty-signals.md)).

### 2.1 Assisted versus unassisted

Split every measure by whether the attempt was assisted (a hint, a booster, a continue, an adapted offset). Unassisted numbers describe the level; assisted numbers describe the level plus help. The calibration table uses unassisted attempts only, so the engine never learns from its own easing. Holdout players (see [experiments](experiments-and-measurement.md)) are the cleanest calibration source because the policy never touches them.

### 2.2 Walls and spikes

| Pattern | Reading | First check |
|---------|---------|-------------|
| Spike | One level far harder than its neighbors (pass rate well below, attempts well above) | Is it a designed peak? Is it flagged hard in the game? |
| Wall | Players stop at this level far more often than elsewhere (quit or churn rise), with or without a pass rate dip | Mechanic introduced here, unclear goal, bug, or too hard |
| Sawtooth | Regular peaks with easier levels after them | Usually the design working; see [curves](difficulty-curves-and-level-design-signals.md) |
| Flat high | Many hard levels in a row, no rest | Fatigue risk; designer review |
| Frontier churn | Churn at the last available levels | A content runway problem, not difficulty |

Flag on leaving, not on failing: a fail spike alone is often a designed peak; churn and quit spikes are the signal ([Practitioner consensus], shared with `game-liveops`).

## 3. Ratings: Elo and Rasch

Raw pass rate depends on who played the level. Ratings separate player skill from level difficulty so a level that only strong players reach does not look easy.

### 3.1 Elo style joint rating (online, simple)

Each player has a skill rating and each level a difficulty rating on one scale. After each unassisted attempt:

```
expected = 1 / (1 + 10 ^ ((level_rating-skill_rating) / 400))
outcome  = 1 if passed else 0
skill_rating += K_player * (outcome-expected)
level_rating -= K_level  * (outcome-expected)
```

| Choice | Guidance | Label |
|--------|----------|-------|
| Scale | Start everyone and every level at the same value (1500 is the chess habit, any constant works) | Method |
| `K_player` | Larger for new players so they converge fast, smaller later | [Practitioner consensus] |
| `K_level` | Small; a level has many attempts, so it should move slowly | [Practitioner consensus] |
| Sample floor | Do not trust a level rating until it has many attempts; puzzles need many attempts for stable ratings | [Reported, 2026-10] (Pelánek 2016, Lichess) |
| Outcome | Pass or fail only; time and moves left can enter later as a graded outcome, documented | Method |

The engine's `rating.js` (in [../engine](../engine/)) is the reference implementation of the player side; `difficulty_table.py` replays the same update offline with K 24 for players and K 8 for levels (section 6). `skill_rating`, `level_rating` and `rating_gap` are allowed policy inputs ([policy format](policy-format.md) section 3).

### 3.2 Rasch (batch, more stable)

The Rasch model fits the same idea in one batch over all attempts:

```
P(pass | player p, level l) = 1 / (1 + exp(-(theta_p-b_l)))
```

`theta_p` is player ability, `b_l` is level difficulty. Fit weekly on the server over unassisted, non holdout and holdout attempts in private modes. Rasch is better for the weekly level table; Elo is better for the live player estimate on the device.

| Use | Elo | Rasch |
|-----|-----|-------|
| Live player skill on device | Yes | No |
| Weekly level table | Acceptable | Preferred |
| New level with few attempts | Weak | Weak (needs priors or bots) |
| Explaining to a designer | Simple | Simple once plotted |

### 3.3 What ratings are not

A rating is a play signal about one game. It never encodes spend, ad value, device, location or any personal trait, and it is never shown as a judgment of the player. A player who resets their adaptation (see [policy design](adaptive-policy-design.md)) resets their skill rating to the default.

## 4. Human like bot playtests

Before a level ships, a bot estimates its difficulty so the table has a prior on day one.

| Approach | What it is | Strength | Weakness | Label |
|----------|-----------|----------|----------|-------|
| Human like CNN (King) | A network trained on human moves plays the level many times | Correlates with average human difficulty; cheaper than tree search | Needs a move log corpus | [Reported, 2026-10] (Gudmundsson et al. 2018) |
| RL agents plus population simulation (Rovio and Aalto) | Agents of varied skill play; a population model turns pass rates into churn | Predicts per level pass and churn | Engineering cost; needs calibration against real players | [Reported, 2026-10] (Roohi et al. 2020) |
| Search based solver (MCTS or exhaustive) | Finds whether and how a board can be solved | Proves solvability | Plays unlike a human; poor proxy for felt difficulty | [Reported, 2026-10] (contrast drawn by King) |
| Studio simulation tool | Block Blast's developer reports a simulation tool alongside heavy A/B testing | Shows the industry habit | No public method | [Reported, 2026-01] |

Procedure:
1. Keep a solver for solvability (see [fair randomness](fair-randomness-and-solvability.md)) and a human like bot for difficulty. They answer different questions.
2. Run each new level many times with the bot on the pinned engine version; record bot pass rate and moves used.
3. Map bot pass rate to a starting `level_rating` with a regression fitted on levels that already have real data.
4. Mark the level `prior: bot` in the table until it passes the sample floor; then switch to the real rating.
5. Each month, compare bot priors with real ratings for levels that crossed the floor. If the error grows, retrain or refit the mapping.

## 5. Cold start

| Cold start | Approach |
|------------|----------|
| New player | Start at the default skill rating with a high `K_player`; use the first levels (tutorial) as the calibration set; the policy waits for a minimum number of attempts before any difficulty action (a `when` condition on attempts) |
| New level | Bot prior (section 4), marked as prior; the policy may offer hints but no difficulty offset until the level has a real rating |
| New game | No table yet: run the first weeks without difficulty rules (hints and breaks only), collect data from everyone, then fit the first table |
| New engine version | Levels regenerated under a new version are new levels for the table; ratings never carry over silently |

Placeholder: no difficulty action before a player's tenth attempt in a game, tune per game. This is a starting value, not evidence.

## 6. Reading `difficulty_table.py`

The script lives in [../scripts](../scripts/) (`difficulty_table.py`). Standard library only; run with `python3 -I`. It reads facts and prints a table plus flags; it never recommends level parameters. A sample input is in `../scripts/samples/events.csv`.

### 6.1 Input

One row per attempt, with a header row.

| Column | Required | Meaning |
|--------|----------|---------|
| `player_id` | Yes | Pseudonymous id (never a name, email or ad id) |
| `level` | Yes | Integer level index |
| `result` | Yes | `win`, `fail` or `quit` (a quit counts as an attempt that did not pass) |
| `attempts_before` | No | Attempts this player made on the level before this one |
| `duration_ms` | No | Read and checked, not used in this version |
| `ts` | No | Epoch seconds or ISO 8601; without it the file order is the time order |

Export one mode and one engine version at a time, unassisted attempts only (section 2.1).

### 6.2 What it computes per level

| Column | Definition in the script |
|--------|--------------------------|
| attempts | Every event on the level |
| players | Distinct players with at least one event on the level |
| pass rate | Wins / attempts |
| first try pass | Wins on a player's first attempt / first attempts (`attempts_before == 0` when filled, otherwise the first event in time order) |
| median attempts | Median, over players who passed, of attempts up to and including their first win |
| quit at level rate | Players whose last event overall is on this level and is a fail or quit / players who reached it |
| elo | Level rating from replaying every attempt in time order: players and levels start at 1500, expected win chance `1 / (1 + 10 ** ((level-player) / 400))`, the player moves by K 24 times (score minus expected), the level by K 8 times (expected minus score) |

Only differences between level ratings carry meaning, and levels with few attempts stay near 1500. "Quit at level rate" is the script's stand in for per level churn: it uses last event overall, not a mature inactivity window, so a recent export overstates it at the frontier. Read it with the cohort dates.

### 6.3 Options, labels and flags

| Option | Default in the script | What it sets |
|--------|-----------------------|--------------|
| `--min-attempts` | 30 | Below this, the level is `insufficient data` and is not judged |
| `--hard` | 0.45 | Pass rate below this is `hard` |
| `--super-hard` | 0.25 | Pass rate below this is `super hard` |
| `--json` | off | Print one JSON document; the "cannot cover" sentence is under `cannotCover` and also on stderr |
| `--out` | none | Also write the printed output to a file |

The defaults are practitioner starting points written into the script, not benchmarks. Record the values used with every table.

| Label | Meaning | What to do |
|-------|---------|------------|
| `ok` | Pass rate at or above `--hard` | Nothing |
| `hard` | Pass rate below `--hard` | Fine if the designer marked it as a peak; check a rest level follows |
| `super hard` | Pass rate below `--super-hard` | Must be a deliberate, labeled peak; check quit at level |
| `insufficient data` | Attempts below `--min-attempts` | Do not act; the absence of a flag is not a finding |

| Flag | Rule in the script | Who acts |
|------|--------------------|----------|
| `spike` | Pass rate at least 0.15 below both neighboring levels (both with enough attempts) | Designer review; often intended |
| `wall` | Quit at level rate at least 2 times the median of all judged levels, and at least 0.05 | Designer review first; the policy may offer a hint, never a hidden change |
| `sawtooth` (summary, not a flag) | Share of hard levels and the spacing between them | Compare with the intended curve ([curves](difficulty-curves-and-level-design-signals.md)) |

Exit codes: 0 the table was written (flags are not failures); 2 could not run.

### 6.4 Procedure

1. Export the attempt log for one mode and one engine version, unassisted attempts, with the cohort dates written down.
2. Run, for example `python3 -I ../scripts/difficulty_table.py events.csv --min-attempts 50 --json --out table.json`, with the thresholds recorded in `ads-master/memory/player-experience.md` from the last run.
3. Read `insufficient data` rows first: they are where nothing can be claimed.
4. Read `wall` flags next. A wall at the last levels may be the content frontier, not difficulty; check before filing. File real walls as a difficulty flag for the game repo in the `game-liveops` format.
5. Compare `hard` and `super hard` labels with the designer's own hard markers. A label the designer did not intend is a finding.
6. Read the `sawtooth` summary against the intended curve.
7. Save the output under `ads-master/outputs/player-experience/` with the export name and date range, and quote the script's `cannotCover` sentence in the report.

Never change a threshold to make a flag disappear. A threshold change is a recorded decision with the reason and the date.

## 7. Calibration cadence

| When | What | Output |
|------|------|--------|
| Every release with new levels | Bot priors for the new levels | Table rows marked `prior: bot` |
| Weekly | Rasch fit on unassisted private mode attempts; `difficulty_table.py` run | Level table version N+1 (draft, G1) |
| Weekly | Diff against the previous table; levels that moved more than a placeholder amount need a reason | Change list |
| Monthly | Bot prior error check | Note in memory |
| On policy revision | Recheck that the table version and policy revision are both logged | Audit log entry |

Publishing the table to remote config is G3. The table carries its own version and the engine logs it with every adapted level, so any result can be traced to the table that produced it ([architecture](architecture-and-telemetry.md)).

## 8. Common errors

| Error | Effect | Fix |
|-------|--------|-----|
| Pooling assisted and unassisted attempts | The table learns from its own easing and drifts easier | Unassisted only |
| Pooling shared and private modes | Shared levels look adapted; private levels look fair | One table per mode type |
| Mixing engine versions | Two different levels share a row | Key on engine version |
| Churn without a mature cohort | Recent levels look like walls | Mature cohort only |
| Trusting a rating below the floor | Noise drives adaptation | `insufficient data` stops actions |
| Pass rate only | A level that people quit looks fine | Read quit and churn with it |
| Short term conversion as the target | Harder levels look better | Judge on long run retention (King GDC, [Reported, 2026-10]) |
