# Experiments and Measurement

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). Experiment method follows Kohavi et al., Trustworthy Online Controlled Experiments (2020) as summarized in the research notes [Reported]. Tool facts are from search summaries [Reported, 2026-10]. No effect size here is a benchmark.

Gate: experiment designs and reads are G1. Starting, ramping or stopping a live experiment changes what players get and is G3. Metric definitions belong to `measurement` ([game KPIs](../../measurement/references/game-kpis.md)); the read goes into `ads-master/EXPERIMENTS.md`.

## 1. The template: Ascarza et al.

Ascarza, Netzer and Runge (IJRM 2025) is the design to copy [Reported, 2026-10]:

| Element | Their design | Our version |
|---------|-------------|-------------|
| Unit | Player | Player (install id) |
| Size | 300,000+ players | Whatever the game has; compute power first |
| Duration | 12 weeks | 8 to 12 weeks for long run retention |
| Control | Holdout with no easing | Persistent holdout with no adaptation |
| Treatment | Easier puzzles for higher churn risk players through more favorable piece allocation | Policy rules in private modes, visible and bounded ([policy design](adaptive-policy-design.md)) |
| Outcomes | Engagement, long run retention, in round purchases, total spending (short and long run) | Primary retention metrics, fun proxies, guardrails; revenue secondary |
| Heterogeneity | Stronger for progress prone players and past spenders | Segment by play signals only (progress, help use); spend segments may be read, never targeted |
| Reported result | Engagement and retention up; in round purchases down; total spending up; ad revenue +21% in the Columbia summary | [Reported, verify] for the +21% |

The lesson is the design, not the number: randomize, hold out, wait long enough, and read total outcomes, not the single round.

## 2. Holdouts

| Rule | Detail |
|------|--------|
| Size | `holdoutPercent` 1 to 20 (checker); Statsig recommends 1 to 2% for long holdouts [Reported, 2026-10] |
| Persistent | The same players stay out for the whole read; the engine assigns by a stable hash of the install id and the policy revision ([policy format](policy-format.md) section 6) |
| Holdout salt | The hash uses the install id and `experiment.holdoutSalt`, so revisions keep the same holdout; changing the salt draws a new holdout and restarts the read. Revisions during a read are still logged, because they change what the treatment arm receives |
| What holdout players get | The same game, curve, content and shared modes; no policy actions; their events still counted |
| Never | Exploration, early access, or any other test running on holdout players |
| Tools | Firebase personalization uses a holdout; Statsig and PostHog support holdouts [Reported, 2026-10] |

Size the holdout from power, not habit: a 1% holdout in a small game cannot detect anything in 12 weeks. Use the sample size notes in [game KPIs](../../measurement/references/game-kpis.md) section 10 and [game-liveops experiments](../../game-liveops/references/experiments-and-remote-config.md) section 3.2.

## 3. Metrics

### 3.1 Primary

| Metric | Why |
|--------|-----|
| D1, D7, D28 retention | The engine exists to keep players |
| Sessions per week | Opens, the stated aim |
| Session length (median) | Read only with fun proxies and guardrails |

Definitions (day boundary, classic versus rolling, mature cohorts) come from `measurement`'s KPI dictionary.

### 3.2 Fun proxies

| Proxy | Definition (draft for `measurement`) |
|-------|--------------------------------------|
| One tap rating | Share of shown rating prompts answered positively (the prompt is shown on a neutral moment, same rule for both arms) |
| Voluntary replay | Replays of passed levels or practice runs per player per week |
| Share | Shares per completer |
| Setting kept on `auto` | Share of treatment players who never switch to a fixed level |

Performance based DDA raised performance but not enjoyment in a 221 participant study [Reported, 2026-10]: performance metrics alone can look good while fun does not move. Read fun proxies every time.

### 3.3 Guardrails

| Guardrail | Breach meaning |
|-----------|----------------|
| Fail streak length (p90) | The policy is not helping when it should |
| Quit after fail rate | Frustration rising |
| Adaptation opt out rate (switch away from `auto`) | Players dislike what the engine does |
| Complaints and reviews mentioning difficulty or "rigged" | Trust damage |
| Notification opt outs | Return reasons too pushy |
| Hint offer decline rate | Offers too frequent |

The sample policy names `quit_after_fail_rate` and `adaptation_opt_out_rate` as guardrails.

### 3.4 Secondary

Revenue (IAP and ads), split as `game-monetization` defines it. Revenue never decides a policy alone; a policy that raises revenue while a guardrail breaches is rolled back.

## 4. Sample ratio checks

Before reading any result, check the split matches the design (Kohavi) [Reported].

| Check | How |
|-------|-----|
| Sample ratio mismatch (SRM) | Chi square test of observed arm counts versus expected (for example 95 to 5); a very small p value means assignment or logging is broken |
| Exposure | Treatment players who never met a rule condition still count in treatment (intent to treat) |
| Logging parity | Both arms send the same events; holdout events are not dropped |
| Pre period balance | Arms look alike on the week before assignment |

An SRM failure stops the read. Fix the assignment or the logging, then restart the clock.

## 5. Read windows

| Read | When | Purpose |
|------|------|---------|
| Daily guardrail watch | First 7 days after a ramp | Roll back on a breach |
| Early look | Week 2 to 4 | Guardrails and SRM only; no ship decision |
| Main read | 8 to 12 weeks (`readAfterDays` 56 in the sample; under 28 warns) | Retention and fun proxies |
| Long tail | Keep the holdout running after the main read | Detect decay or novelty effects |

Early reads over fit to the first weeks (the checker's own warning text). Do not peek and stop on a good day.

## 6. Experiment row (`EXPERIMENTS.md`)

```
id: pxe-<product>-<yyyymmdd>-<slug>
hypothesis: <rule change> raises <primary> without breaching <guardrails>
policy: pxeVersion 0.1, revision <n> (control: no actions, persistent holdout <x%>)
engine: ENGINE_VERSION <v>, level table <version>
modes: <private modes>; shared modes untouched
assignment: hash(install id, policy revision), SRM check daily
primary: d1, d7, d28 retention, sessions per week
fun proxies: one tap rating, voluntary replay, share, auto kept
guardrails: quit_after_fail_rate, adaptation_opt_out_rate, fail streak p90, complaints
secondary: revenue split
read after: <days>, owner <name>, status planned | running | read | shipped | rolled back
```

## 7. What to report

| Section | Content |
|---------|---------|
| Design | Arms, sizes, dates, policy revision, engine version, modes |
| Validity | SRM result, logging parity, any revision break, outages |
| Primary | Effect with interval for each metric, per arm values, source and date range |
| Fun proxies | Same format |
| Guardrails | Each one, breached or not |
| Secondary | Revenue split, labeled secondary |
| Segments | By play signal segments (progress, help use, skill band); never targeting by spend |
| Decision | Ship, iterate, roll back; with the reason |
| What this cannot say | Effects outside the tested modes and markets; anything below power |

No invented numbers: every figure names its export and date range.

## 8. Ties to measurement's game KPIs

| Need | Owner | Where |
|------|-------|-------|
| Retention definitions, day boundary, mature cohorts | `measurement` | [game KPIs](../../measurement/references/game-kpis.md) sections 2 and 3 |
| Level design dashboard | `measurement` with `game-liveops` | [game KPIs](../../measurement/references/game-kpis.md) section 8.4 |
| Event tracking plan for the engine events | `measurement` | [game tracking](../../measurement/references/game-tracking.md) |
| Event uplift holdouts for liveops | `game-liveops` | [experiments and remote config](../../game-liveops/references/experiments-and-remote-config.md) section 5 |
| Engine events and fields | This package | [architecture](architecture-and-telemetry.md) section 3 |

Propose new metrics (fun proxies, adaptation opt out) to `measurement` as drafts; do not define them in a report first.

## 9. Common errors

| Error | Fix |
|-------|-----|
| Holdout re-drawn by a changed salt | Keep the salt stable; log any change as a decision and restart the read |
| Holdout too small for the game | Power calculation first |
| Shipping on a week 2 lift | Wait for the main read |
| Reading only treated players (those who met a rule) | Intent to treat over the whole arm |
| Revenue as the deciding metric | Retention and fun first |
| Same players in two engine tests | One test per player at a time, or a factorial design declared up front |
| Uplift claims from observational logs | Randomized data only ([player modeling](player-modeling-and-churn.md) section 5) |
