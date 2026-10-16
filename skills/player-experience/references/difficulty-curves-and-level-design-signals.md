# Difficulty Curves and Level Design Signals

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). Facts about named games come from search summaries and secondary trackers ([Reported, 2026-10] at best, often [Unverified]); they describe what exists, not a template. Thresholds marked "placeholder" are starting values, not benchmarks.

Gate: curve reviews, flags and proposals to the game repo are G1. A live change to the curve, a level's parameters or the policy that adapts it is G3 and belongs to the game repo's release process, with site or app release QA.

## 1. The boundary: engine versus designer

The engine adapts at the edges; the designer owns the shape. Keep the line sharp, or the engine silently redesigns the game.

| Owned by the level designer (game repo) | Owned by the engine (policy, within published bounds) |
|------------------------------------------|---------------------------------------------------------|
| The curve: where peaks and rest levels sit | A difficulty offset of one published step in private modes |
| Each level's goal, layout, mechanics and move or time budget | Offering a hint when a player is stuck |
| Which mechanic is introduced when, and how | Offering a break after repeated fails |
| Which levels are marked hard or super hard | Showing the next goal at a session end |
| The first session and the tutorial | Suggesting a practice mode |
| Daily and ranked content (identical for everyone) | Nothing in shared modes, ever |

If the engine eases a level for most players, the level is wrong, not the player: send a flag to the designer instead of letting the policy carry it forever.

## 2. Sawtooth curves

A sawtooth curve rises to a peak, drops to a rest level, then rises again, so effort and relief alternate.

| Evidence | Label |
|----------|-------|
| About one level in five is "hard" in top match 3 games; King's first hard level near level 10; 64% of games flag hard levels | [Unverified] (Playliner via WN Hub, secondary) |
| Royal Match labels hard and super hard levels and introduces each new obstacle alone; ships about 200 new levels a month | [Reported, 2026-10] |
| A harder early level converted more short term; an easier version retained longer; judge levels inside the whole progression | [Reported, 2026-10] (King GDC "Sugary Statistics") |
| Engagement versus difficulty follows a power law across 12M Candy Crush players | [Reported, 2026-10] (Reguera et al. 2020) |
| Flow (challenge matched to skill) is a useful heuristic with mixed empirical support | [Contested] (Engeser and Rheinberg 2008; Allart et al. 2017 supports it in two Ubisoft games) |

Use the "one in five" and "near level 10" figures only as a question to ask of your own curve, never as a target: the source is secondary and unverified.

### 2.1 Curve anatomy

| Part | Role | Signals that it works |
|------|------|-----------------------|
| Ramp | Each level a little harder than the last | Pass rate drifts down slowly, churn flat |
| Peak (hard) | A deliberate test of what was just learned | Pass rate dips, attempts rise, churn does not rise much more than at neighbors |
| Super hard peak | Rare, marked, a milestone | Same as peak with a visible label; designer chose it |
| Rest level | Relief after a peak; often a reward or a fun mechanic | High first try pass, short attempts |
| New mechanic level | One new thing, alone | First try pass may dip; quit should not spike |

### 2.2 Hard level frequency and flagging

1. Mark hard levels in the game itself (a visible label before the level starts). A labeled peak is a promise kept; an unlabeled peak feels like a trap ([Practitioner consensus]).
2. List designed peaks in the level table so [difficulty_table.py](../scripts/) output can be compared with them.
3. A `hard` or `super hard` label from the script on a level the designer did not mark is a finding: send it as a flag.
4. Two peaks in a row with no rest level between them is a review item (placeholder rule; tune per game).
5. Keep the hard label honest for adapted players too: if the policy offset made a peak easier, the label still says hard and the "why this level" line says it was eased (see [policy design](adaptive-policy-design.md)).

## 3. Introducing each mechanic alone

| Rule | Why | Check |
|------|-----|-------|
| One new mechanic per level that introduces it | Learnability; the player knows what caused a fail | Mechanic list per level in the table |
| The introducing level is easy | The player learns the rule, not the puzzle | First try pass on the level is high |
| Combine only after each part was seen alone | A fail stays attributable | Combination levels come after both intros |
| A peak tests a known mechanic, not a new one | The peak measures skill, not surprise | No intro on a peak level |
| Royal Match reportedly introduces each new obstacle alone | Shows the pattern at scale | [Reported, 2026-10] |

A quit spike at a mechanic introduction usually means the goal was unclear, not that the level was hard: the fix is a clearer tutorial frame, which is design work.

## 4. Rest levels after peaks

1. After each peak, plan at least one level with a high expected first try pass (placeholder; tune per game).
2. A rest level is still a level: it shows progress, often a reward. It is not filler.
3. The engine may help a player through a peak with a hint offer; it never removes the rest level or moves it.
4. Read rest levels too: a rest level with a quit spike is a hidden peak.

## 5. The first session

The first session decides much of what follows: the dossier reports that day 0 session features predict churn best in one free to play game (Oulu thesis 2026, XGBoost ROC AUC 0.7565) [Reported, 2026-10], and GameAnalytics reports a median D1 of about 22% in 2025, declining [Reported, 2026-10].

| First session rule | Why |
|--------------------|-----|
| Early levels are winnable on the first try for nearly everyone | The player learns they can win |
| No hard label inside the first session | A wall before the player cares is a lost player ([Practitioner consensus]) |
| Each early level teaches one thing | Section 3 |
| The session ends with a visible next goal | See [sessions and return reasons](sessions-opens-and-return-reasons.md) |
| No offer or interstitial before the player has played in a new install | Matches the [monetization contract](../../game-monetization/references/monetization-contract.md) offer point rules |
| The engine collects ratings but takes no difficulty action yet | Cold start ([calibration](difficulty-measurement-and-calibration.md) section 5) |

The King GDC finding cuts both ways: a harder early level converted more short term while an easier one retained longer [Reported, 2026-10]. The engine optimizes long run retention and fun proxies, so the first session leans easy.

## 6. Measuring curve changes with holdouts

A curve change is a design change; prove it like any other.

| Step | What |
|------|------|
| 1 | Write the hypothesis: "moving the first hard level from N to N+k raises D7 without lowering sessions per week" |
| 2 | Keep the persistent policy holdout untouched (it sees the new curve too, without adaptation), so policy and curve effects stay separable |
| 3 | Randomize the curve change by player, not by day; content must be stable for a player once seen |
| 4 | Primary: D7 and D28 retention, sessions per week. Guardrails: quit after fail, fail streak length, complaints |
| 5 | Read at 8 to 12 weeks for long run retention; earlier reads are for guardrail breaches only |
| 6 | Report effect with intervals, sample ratio check result and what else changed |

Details: [experiments and measurement](experiments-and-measurement.md). The liveops side of experiments: [game-liveops experiments](../../game-liveops/references/experiments-and-remote-config.md).

## 7. Signals to send to the designer

| Signal | Likely meaning | Message to the game repo |
|--------|----------------|--------------------------|
| A level is eased by the policy for a large share of players | The level is harder than intended | "Level N is eased for most players; consider retuning the level" |
| `wall` flag (players stop here far more than elsewhere) | Too hard, unclear goal or bug | Difficulty flag with funnel evidence |
| Quit spike at an intro level | Unclear mechanic | "The goal at N may be unclear" |
| `hard` label where none was designed | Unintended peak | "N reads as hard; was it meant to be?" |
| Rest level with low first try pass | Hidden peak | "N is not resting players" |
| Raise rules fire often early in the game | Early curve too flat for skilled players | "Early levels may bore skilled players" |
| Hint offers concentrated on one level | Stuck point | "Players get stuck at N" |

Use the `game-liveops` difficulty flag format ([difficulty signals](../../game-liveops/references/content-cadence-and-difficulty-signals.md) section 6). The flag is evidence and a question, not a fix.

## 8. Curve review procedure (monthly, or per content drop)

1. Export unassisted attempts for the level path, one engine version, with cohort dates.
2. Run `difficulty_table.py` ([calibration](difficulty-measurement-and-calibration.md) section 6) and plot pass rate and elo by level.
3. Overlay the designer's intended peaks and rest levels and the mechanic introduction list.
4. Mark mismatches: unintended `hard` labels, peaks without rest levels, intro levels with low first try pass, `wall` flags outside the frontier.
5. Overlay the policy action rate per level from the audit log sample: levels where easing fires for a large share of players are design questions.
6. Write the curve memo: findings, evidence, questions for the designer. No parameter recommendations.
7. File flags in the `game-liveops` format; log the memo in `ads-master/outputs/player-experience/`.

Curve memo template:

```
# Curve review: <product>, levels <a> to <b>, <date>
Data: <export>, engine <ENGINE_VERSION>, cohort <dates>, thresholds <min-attempts, hard, super-hard>
Sawtooth summary: hard share <x>, spacing <y> (script output)
Intended peaks: <list>; unintended hard labels: <list>
Rest level check: <peaks without rest>
Mechanic intros: <level: mechanic, first try pass>
Policy load: <levels eased for most players>
Questions for the designer: <one line each>
```

## 9. Things the engine never does to the curve

- Never makes a level harder because a player is likely to pay, watch an ad or has an ad ready. Spend and ad signals are forbidden inputs ([policy format](policy-format.md) section 4).
- Never inserts an unlabeled peak or removes a rest level.
- Never adapts a daily, ranked, race or group level.
- Never tunes near misses on purpose: near miss effects on persistence are [Contested] (Clark 2009 in slot tasks; Finserås 2019 and Yong 2018 found no persistence effect in skill games), and engineering them is on the red list ([ethics](ethics-law-and-store-rules.md)).
- Never hides that a level was eased: the log and the "why this level" line say so.
