# Player Modeling and Churn

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). Every study below comes from a search summary of the named paper or thesis and carries [Reported, YYYY-MM]; model performance numbers are from one game each and do not transfer. Read the paper before quoting a number to anyone.

Gate: feature lists, churn definitions and model plans are G1. Training a model on player data needs the consent basis confirmed with `measurement` and `compliance`. Putting a model's output into a live policy is a policy revision (G3, [policy design](adaptive-policy-design.md) section 8).

## 1. The rule

**A prediction is a risk score for helping, never a lever on outcomes.** A churn score may decide that a struggling player is offered a hint, a break or one eased step, within the published policy bounds, in a private mode. It never makes a level harder, never changes a draw toward a loss, never times an offer, never touches a shared mode and never reads spend or ad signals.

| Allowed use of a churn score | Never |
|------------------------------|-------|
| Lower the fail streak threshold for a hint offer for at risk players | Raise difficulty for players unlikely to churn so they buy boosters |
| Offer a break sooner | Time an offer or an ad to the moment of highest risk |
| Pick which real content goes into the next goal | Score players by spend capacity |
| Prioritize level flags for the designer | Use the score in ranked matchmaking |
| Report risk distribution to the team | Show the score to the player as a label |

The best causal evidence points the same way: easing for higher churn risk players raised engagement, long run retention and total spending in a randomized experiment with a holdout (Ascarza, Netzer, Runge, IJRM 2025) [Reported, 2026-10]. Help is the use that works.

## 2. Features

### 2.1 Day 0 session features first

| Evidence | Label |
|----------|-------|
| Day 0 session features predict churn best; XGBoost ROC AUC 0.7565 in one free to play game (Oulu thesis 2026) | [Reported, 2026-10] |
| The best churn model varies by genre (Kim et al. 2017, PLOS ONE, 193k players) | [Reported, 2026-10] |
| Sequential plus aggregated features (Kristensen and Burelli 2022) | [Reported, 2026-10] |

AUC 0.7565 is one game's result, not a target.

### 2.2 Allowed feature families

Only play signals, matching the policy format's allowed inputs ([policy format](policy-format.md) section 3) plus their aggregates over time.

| Family | Examples |
|--------|----------|
| Session shape | Sessions on day 0, session length, gap between sessions (`session_gap_hours`), `sessions_today` |
| Progress | Levels passed, highest level, time to first win |
| Struggle | `fail_streak`, attempts per level, `quit_rate_recent`, `restarts_recent` |
| Help use | `hint_uses_level`, `hint_uses_session`, hint offers declined |
| Skill | `skill_rating`, `rating_gap` on recent levels |
| Pace | `median_move_ms`, solve time relative to the level median |

### 2.3 Forbidden features

The forbidden token list in the [policy format](policy-format.md) section 4 applies to models too: no spend, purchase, payer tier, revenue, LTV, ARPU, ad value, eCPM, ad readiness or fill, price, device model, tier or price, country, region, geo, income, age, gender, health, mood, battery or vibration. A model trained on them and then used to pick help still leaks them into outcomes. Age is used only to choose the tier (strict or not), never as a model feature. Apple 5.1.2(iii) says "Apps should not attempt to surreptitiously build a user profile based on collected data" [Official, 2026-06].

## 3. Churn definitions

Define churn before modeling, in `ads-master/METRICS.md` with `measurement`.

| Definition | Used by | Fits | Label |
|-----------|---------|------|-------|
| 7 days inactive | Roohi et al., Rovio and Aalto (CHI PLAY 2020) | Daily and level games with frequent play | [Reported, 2026-10] |
| 14 days inactive | Runge et al., Wooga (high value players) | Games with weekly rhythms | [Reported, 2026-10] |

| Decision | Rule |
|----------|------|
| Window | Pick one per game and keep it; changing it breaks every comparison |
| Mature cohort | Count only players whose last activity is at least one full window before the as of date |
| Level churn | Last level reached is N and inactive for the window ([calibration](difficulty-measurement-and-calibration.md)) |
| Daily games | Use the server day id ([game-liveops](../../game-liveops/references/daily-loops-and-streaks.md) section 2.2) |
| Return after churn | Track re-activations separately; a churned player who returns is a win for return reasons |

## 4. Model families

| Family | Example in the dossier | Strength | Weakness | When |
|--------|------------------------|----------|----------|------|
| Rules plus Elo | Pelánek 2016 ratings | Explainable, no training data, runs on device | Coarse | First version, always |
| Logistic regression | Baseline | Explainable coefficients | Linear | First model |
| Gradient boosted trees | XGBoost in the Oulu thesis | Strong on tabular day 0 features | Needs explanation tooling | After the baseline |
| Neural networks | Best AUC for high value player churn at Wooga (Runge) | Sequences | Data hungry, opaque | Rarely needed |
| Survival ensembles | Periáñez et al. | Models time to churn, handles censoring | More complex | When timing matters |
| Sequential plus aggregated | Kristensen and Burelli 2022 | Uses move order | Engineering cost | Large games |
| Bandits (LinUCB, Thompson) | Research notes | Learn which help works online | Needs logged randomized data and guardrails | After rules plus holdout |
| Uplift models | Research notes | Estimate who is helped by an action | Needs randomized data | After experiments |
| Deep player models | Pfau et al. CHI 2020 improved intrinsic motivation in an MMORPG | Can feel less mechanical than heuristic DDA | Heavy | Research grade only |

## 5. Prediction is not uplift

A churn model says who is likely to leave. It does not say whether a hint, a break or an eased step changes that. Two players with the same risk can respond in opposite ways.

| Question | Data needed |
|----------|-------------|
| Who is at risk? | Observational logs (churn model) |
| Does the action help on average? | A randomized holdout (A/B with persistent control) |
| For whom does it help most? | Randomized data with enough sample per segment (uplift model) |

Ascarza et al. found the effects stronger for progress prone players and past spenders [Reported, 2026-10]. That is a result about who benefited from help in a randomized test; it is not permission to use spend as an input. Our engine finds progress prone players from play signals (progress and help use), never from spend.

Rules:
1. Never train an uplift model on observational data: the policy decided who got help, so the data confounds the action with the risk.
2. Keep a randomized exploration slice (part of the treatment group gets the action at random within the rule's bounds) if you plan uplift modeling; document it in the experiment row.
3. The persistent holdout is never used for exploration.

## 6. ML only after rules plus a holdout baseline

| Stage | What exists | What may be added |
|-------|-------------|-------------------|
| 1. Rules | Policy rules, Elo, transparency UI, persistent holdout | Nothing until the first read at 8 to 12 weeks |
| 2. Baseline read | Rules versus holdout on primary metrics, fun proxies, guardrails | A churn score as one more condition in an existing help rule |
| 3. Model in a rule | The score gates help; rules and bounds unchanged | A bandit choosing between allowed help actions |
| 4. Learned choice | Bandit inside the allowed actions and caps | Uplift targeting, with randomized data |

At every stage principles stay the same: play signals only, private modes only, bounded, visible, switchable, holdout kept. A model that cannot be explained in one line of the "why this level" copy should not decide.

## 7. On device versus server

| Aspect | On device | Server |
|--------|-----------|--------|
| Player state estimator (Elo, streaks, move time) | Yes (reference engine) | Not needed |
| Churn score | Possible: a GBM exported to ONNX Runtime Web (WASM) [Reported, 2026-10, research notes] | Batch scoring, pushed as a coarse risk band in config |
| Privacy | Raw signals stay on the device | Needs consented telemetry |
| Consent | Still required: Apple 5.1.1 requires consent for collecting usage data "even if such data is considered to be anonymous" [Official, 2026-06]; an on device system is still in scope of the AI Act [Reported, 2025-07], and the dossier's verdict is that on device is not an exemption from consent and disclosure | Required |
| Update speed | App or config release | Fast |
| Audit | Client log | Central |

Frustration and boredom are transient flags in the estimator, never stored profiles ([architecture](architecture-and-telemetry.md)).

## 8. Model card (fill before any model goes live)

```
Model: <name>, version <v>, trained <date range>, product <id>, engine <ENGINE_VERSION>
Target: churn = inactive <7 | 14> days, mature cohort as of <date>
Features: <list>; every feature from section 2.2; forbidden list checked: yes
Excluded: holdout players, shared mode play, assisted attempts (for skill features)
Performance: AUC <x> on <holdout sample>, calibration plot attached
Use: gates <rule id> (help action <offer_hint | offer_break | difficulty_offset -1>) in modes <private list>
Never used for: difficulty raises, offers, ads, shared modes, matchmaking
Explain line: "<copy key>"
Experiment: <EXPERIMENTS.md row>, holdout <x%>, read after <days>
Owner and review date: <name>, <date>
```
