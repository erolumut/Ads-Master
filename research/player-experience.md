# Player Experience Engine: Research Dossier (2026-10)

> Research pass 2026-10-16, five parallel questions. Only developer.apple.com could be opened from this environment; every other fact comes from search summaries of the named sources and is labeled [Reported, YYYY-MM] or weaker until someone reads the source. Apple quotes are [Official, 2026-06]. Numbers marked "verify" must not be quoted to anyone before the paper or page is read.

## 1. Why this dossier exists

A viral video (2026-10) claimed a decompile of Block Blast shows difficulty and loss timing driven by each player's predicted ad value: a "high value ad harvest" rule, a "death algorithm" that makes the next turn unwinnable when an expensive rewarded ad is ready, and a secret score bonus after a revive. The owner asked us to master the systems behind top games: read every move, understand the player, react automatically, adjust levels per player, raise app opens and session length.

The dossier answers four questions: what is true about the claim, what the evidence says works, what the law allows, and how to build the honest version well.

## 2. The Block Blast claim: what is verified

| Claim | Verdict | Basis |
|-------|---------|-------|
| On device XGBoost model | Unknown | No source mentions it |
| "Boost then kill" | Unknown | No source uses the term |
| "High value ad harvest" | Plausible, unverified | One creator (Ayomide Omolewa, a0.dev), relayed by AdExchanger 2026-10-15 and MetaFilter 2026-10-14 [Reported, 2026-10] |
| "Death algorithm" timed to a ready rewarded ad | Plausible, unverified | Same single source; a revive offer at failure is documented design, engineered failure is not shown |
| Secret score inflation after revive | Unknown | No source |
| Heavy experimentation | Confirmed by the studio | 10,000+ A/B tests in 2025, 300+ running daily, a simulation tool; "about 97% fail" [Reported, 2025-01 and 2026-01, company press release and interview] |

No code, no repository, no independent test and no studio response were found. A fair test would log many seeded games and compare piece distributions between ad watching and non ad watching accounts; nobody has published one.

Scale for context: about 70M DAU and 300M MAU (company, 2026-01); about USD 127M ad revenue January to May 2026 in 19 countries per Sensor Tower as relayed [Contested period]; 356.2M installs in 2025 (AppMagic) [Reported].

## 3. The industry record on monetization tuned difficulty

| Item | What it is | Status |
|------|-----------|--------|
| EA, EOMM (WWW 2017) | Matchmaking that minimizes predicted churn; simulation on real EA data | Paper; deployment not shown; criticized [Reported] |
| EA, DDA for maximized engagement (WWW 2017 companion) | Tune level transition probabilities for stay time; "up to 9%" engagement, neutral monetization | Vendor reported, verify [Reported] |
| EA DDA patents (US 9,919,217; US 10,286,323) | Churn prediction adjusts game variables; spend reportedly an input | Claims not read [Reported] |
| Zajonc v. EA (2020-11, dropped 2021-03) | Class action alleging DDA to push packs | Dropped after EA said the patent tech "never was in FIFA, Madden or NHL" and gave technical access [Reported] |
| Activision US 9,789,406 (2017) | Matchmaking to drive purchases | Activision: "has not been implemented in-game" [Reported] |
| Kabam US 9,555,324 | Item effectiveness from past spend, "imperceptibly" | Claims not read [Reported] |
| Netmarble US 2024/0021050 A1 | Better odds after a purchase | Application status unknown [Reported] |
| King patents (US 9,278,282 and others) | Track failures per level, adjust target, moves or give a booster | Retention tuning, no purchase targeting seen [Reported] |

The pattern: large companies patent these ideas and then publicly deny using the spend linked versions. That denial is itself the signal: the spend linked version is a liability, not a secret weapon.

## 4. What the evidence says works

### 4.1 The strongest causal result

Ascarza, Netzer and Runge, International Journal of Research in Marketing, 2025: a 12 week randomized field experiment, 300,000+ players, a free to play puzzle game, with a holdout. Players at higher churn risk received easier puzzles through more favorable piece allocation. Engagement and long run retention rose; purchases in the specific round fell, but total spending rose in the short and long run; effects were stronger for progress prone players and past spenders. The Columbia summary reports ad revenue +21% [Reported, verify]. Helping struggling players beats squeezing them, for players and for revenue.

### 4.2 Supporting findings

| Finding | Source | Label |
|---------|--------|-------|
| King measures level difficulty from outcomes, pre tests levels with a CNN trained to play like humans (cheaper than MCTS, better correlation with average difficulty) | Gudmundsson et al., IEEE CIG 2018 | [Reported] |
| A harder early level converted more short term; an easier version retained players longer; judge levels inside the whole progression | King GDC "Sugary Statistics" (15,000 levels) via mobilegamer.biz | [Reported] |
| Per level pass and churn predicted from RL agents plus a population simulation (95k players, 168 levels; churn = 7 days inactive) | Roohi et al., Rovio and Aalto, CHI PLAY 2020 | [Reported] |
| Engagement vs difficulty follows a power law across 12M Candy Crush players | Reguera et al., Scientific Reports 2020 | [Reported] |
| Heuristic DDA is often noticeable ("rubber banding"); deep player models improved intrinsic motivation in an MMORPG field study | Pfau, Smeddinck, Malaka, CHI 2020 | [Reported] |
| DDA can make players overconfident | Constant and Levieux, CHI 2019 | [Reported] |
| Performance based DDA raised performance but not enjoyment (221 participants) | Controlled study via CEEOL | [Reported] |
| Near misses raise the urge to continue in slot tasks and are rated frustrating; persistence effect not shown in skill games | Clark 2009 (Neuron); Waterloo thesis; Finserås 2019; Yong 2018 | [Contested] |
| Flow (challenge matched to skill) is a useful heuristic with mixed empirical support | Engeser and Rheinberg 2008; Ubisoft survival analysis (Allart 2017) | [Contested] |
| Day 0 session features predict churn best; XGBoost ROC AUC 0.7565 in one free to play game | Oulu thesis 2026 | [Reported] |
| Elo style ratings estimate player skill and item difficulty together; puzzles need many attempts for stable ratings | Pelánek 2016; Lichess Glicko 2 | [Reported] |
| About one level in five is "hard" in top match 3 games; King's first hard level near level 10; 64% flag hard levels | Playliner via WN Hub | [Unverified] |

### 4.3 What top games do for opens and session length

| Mechanic | Games | Purpose | Player view |
|----------|-------|---------|-------------|
| Lives with refill timers (5 lives, about 30 minutes each) | Royal Match, Candy Crush, Color Block Jam | Return when full; refill revenue | Criticised as "wait to play" and "pay to skip" |
| Timed infinite lives as rewards | Royal Match | Longer sessions without churn at zero lives | Friendly |
| Layered event calendar (tournaments, win streaks, team events, album chase; weekend peaks) | Royal Match (Sensor Tower 2026), Monopoly Go (events every 1 to 3 days) | Opens and revenue | Neutral; pressure concerns for children |
| Win streak with escalating pre placed boosters | Royal Match | Longer sessions, stakes on the end of level offer | Mixed (loss aversion) |
| Team chest, team life requests | Royal Match | Opens through social obligation | Questionable for social pressure |
| Continue after fail (coins for 5 moves, rising price; rewarded revive) | Royal Match, Block Blast | Revenue | Criticised; rewarded revive seen as friendlier |
| New obstacle introduced alone; 200 new levels a month | Royal Match | Learnability; content runway | Friendly |
| Daily rewards, daily boosters, quick daily goals | Candy Crush, Monopoly Go | Opens | Mostly accepted |
| Streaks and badges, no purchase, no timer | NYT Games (11.2B solves in 2025) | Opens | Valued by players |
| Sticker albums with packs | Monopoly Go | Revenue and length | Criticised as gambling like |

Published retention for these games is thin and conflicting; treat every D1, D7 and D30 figure as a tracker estimate. GameAnalytics reports median D1 about 22% in 2025, declining [Reported].

## 5. The law and the stores

| Rule | What it means for us | Label |
|------|----------------------|-------|
| EU AI Act Art 5(1)(a) and (b): no AI system using manipulative or deceptive techniques, or exploiting vulnerabilities (age), that materially distorts behavior and causes significant harm; fines up to EUR 35M or 7%; applies since 2025-02-02 | The Commission guidelines (C(2025) 5052, 2025-07-29) reportedly cite a game that profiles children and builds personalised, unpredictable rewards through addictive reinforcement loops as a prohibited example, and name "temporal manipulation"; intent is not required; on device is still in scope | [Reported, 2025-07]; open the PDF |
| EU KIDS Act proposal, COM(2026) 681, 2026-09-17 | Reported content for minors in online games: real money value for currency, no variable rewards, no streaks or daily return rewards, nothing that undermines a minor's decision to stop or pushes play at set times through penalties or lost benefits, profiling based recommendations off by default | [Reported, 2026-09]; a proposal, not law; sources conflict on scope |
| EU Digital Fairness Act | Planned: dark patterns, addictive design, unfair personalisation, game currencies, pay to progress; no text tabled as of 2026-10-16 | [Reported, 2026-10] |
| UCPD and the CPC key principles on in-game currencies (2025-03-21); CPC action against nine companies (2026-09-30) | Misleading and aggressive practices; real money prices; no time pressure on children | [Reported] |
| Consumer Rights Directive personalised price disclosure | Tell the consumer when a price is personalised by automated means | [Reported]; article number to verify |
| UK DMCC Act 2024 | CMA fines directly, up to 10% of global turnover; first fine 2026-04 | [Reported, 2026-04] |
| FTC v. Epic (2022 to 2023) | USD 245M refunds for dark patterns; USD 275M COPPA penalty | [Reported] |
| Apple 2.3.1(a) | "Don't include any hidden, dormant, or undocumented features in your app"; "Egregious or repeated behavior is grounds for removal from the Apple Developer Program" | [Official, 2026-06] |
| Apple 5.6 | Apps "should never prey on users ... trick them into making unwanted purchases ... or engage in any other manipulative practices"; repeated manipulative behavior leads to removal from the program | [Official, 2026-06] |
| Apple 5.1.2(iii) | "Apps should not attempt to surreptitiously build a user profile based on collected data" | [Official, 2026-06] |
| Apple 5.1.1 | Consent for collecting usage data "even if such data is considered to be anonymous"; the privacy policy names all uses | [Official, 2026-06] |

Verdicts (our reading, not legal advice):

| Practice | Verdict |
|----------|---------|
| Adaptive difficulty that helps a struggling player, disclosed, in private modes | Low risk |
| Difficulty or loss timing tuned to ad or spend value | High risk: AI Act, consumer law, Apple 5.6 and 2.3.1; do not build |
| Secret score inflation | High risk: deception, and it breaks every shared score |
| Personalised offers | Moderate: disclose, consent, never for minors without strict limits |
| On device ML profiling | Moderate to high through consent and disclosure; on device is not an exemption |

## 6. Design principles we adopt

1. Fair core, adaptive edges: shared modes (daily, ranked, leaderboards, group boards) are identical for everyone: same seed, same parameters, same engine version. Adaptation lives only in private and practice modes.
2. Help, never harvest: adaptation inputs are play signals (fails, attempts, time, hints, quits, session gaps). Spend, ad value, ad readiness, device price, country wealth and any inferred sensitive trait are never inputs to difficulty, randomness or outcomes.
3. Ease at risk players, with a holdout: the best causal evidence supports easing for players at risk of quitting; always keep a persistent non adaptive holdout and read it over 8 to 12 weeks.
4. Visible and controllable: a difficulty setting (auto, easy, normal, hard) that always wins, a "why this level" line, an adaptation log the player can read, a reset.
5. Scores are true: nothing changes a score after the fact; an assisted run is labeled assisted and never enters a shared board.
6. Measure difficulty from outcomes: pass rate, attempts to pass and per level churn, pre tested with human like bots where possible; sawtooth curves with flagged hard levels; each new mechanic introduced alone.
7. Bounded randomness: bag style or history aware generators cap droughts; every board solvable; seeded and versioned.
8. Return reasons from the player's own state and real content: a new daily, a finished timer, a friend's move, an event that started; no guilt copy, no streak loss threats, caps and quiet hours; streaks with free rest days.
9. Session endings with a next goal, not a trap: show what comes next and let the player stop cleanly.
10. Minors: stricter tier by default (no streak pressure, no variable paid rewards, profiling off, no ad SDK profiling), following the KIDS Act direction before it is law.
11. Prove it helps fun, not only revenue: primary metrics D1, D7, D28 and sessions per week; fun proxies (one tap rating, voluntary replay, share); guardrails (fail streak length, quit after fail, opt outs, complaints); revenue is secondary.
12. Explainable first, learned later: rules plus Elo ratings first; gradient boosted churn models, bandits and uplift models only after randomized logged data exists, and still bound by principles 1 to 5.

## 7. Reference architecture (synthesis)

| Component | Runs | Job |
|-----------|------|-----|
| Game core | Client and server (same code) | Pure `generate(seed, params, engineVersion)`, solver, move log; integer only randomness |
| Telemetry | Client | `level_start`, `level_end` (result, attempts, duration), `hint_used`, `restart`, `quit` (level, move index), `session_start` (gap); pseudonymous install id, consent gated |
| Player state estimator | Client | Elo skill, rolling window, fail streak, median move time; frustration and boredom as transient flags, never stored profiles |
| Policy engine | Client | Versioned JSON rules mapping state to bounded actions (difficulty offset within a published range, hint offer, break offer, next goal); never touches shared modes |
| Remote config and experiments | Server or CDN | Policy version, thresholds, level difficulty table; control, treatment and persistent holdout; sample ratio check |
| Offline calibration | Server, batch | Weekly level ratings (Elo or Rasch), bot playtests for new levels |
| Adaptation audit log | Client full, server sampled | Policy version, inputs summary, action, reason code |
| Transparency UI | Client | Difficulty setting, why this level, log, reset |
| Mode gate | Client and server | Ranked and daily ignore the estimator and policy; the server issues seeds and re validates results with the same engine |

Minimal first version for a web puzzle game: the six events, Elo for player and level, four rules (offer a hint or break after K fails on one level; offer a harder level after a fast solve streak; clamp the offset to one step; never lower silently more than once per session), the transparency UI, one experiment tool with a holdout, a weekly level table.

## 8. Fit by game type

- Daily social games (one shared round a day, groups, seasons): the daily and group boards are shared, so no adaptation there; adaptation fits practice and replays only. The monetization contract already forbids paid counted tries; the engine extends the same rule to difficulty.
- Board game platforms (rated play between people): the clock never plays for a player and engines stay deterministic; bots against a single player can adapt strength openly (a visible bot level), never secretly in rated play.
- Future level games (Royal Match style): the full engine applies to the level path; ranked races stay fair (see game-liveops events and seasons).

## 9. Open items to verify at the source

The Ascarza et al. effect sizes (+21% ad revenue), the EA "up to 9%", King's GDC talk details, the AI Act guidelines' game example and wording, the KIDS Act text (COM(2026) 681) for game provisions and dates, the CRD article number, the DFA status, GDPR Art 22 and children's data, UK ICO Children's Code standards, Google Play Families and Deceptive Behavior policies, PEGI 2026 criteria, Turkey (Law 7578, KVKK).

## Sources (search summaries unless marked)

AdExchanger daily roundup 2026-10-15; MetaFilter thread 214827 (2026-10-14); mobilegamer.biz Hungry Studio interview (2025); Business Wire Block Blast 70M DAU (2026-01-08); Sensor Tower and AppMagic via PocketGamer.biz and Applixir; Chen et al., EOMM, WWW 2017 (arXiv 1702.06820); Xue et al., WWW 2017 companion; EA patents US 9,919,217 and 10,286,323; Activision US 9,789,406 and coverage (2017-10); Zajonc v. EA coverage (VGC, 2021); Kabam US 9,555,324; King patents US 9,278,282, 9,387,401, 10,376,779; Ascarza, Netzer, Runge, IJRM 2025 (doi 10.1016/j.ijresmar.2025.01.006) and Columbia brief; Gudmundsson et al., IEEE CIG 2018; King GDC "Sugary Statistics" (GDC Vault 1034392) and mobilegamer.biz coverage; Roohi et al., CHI PLAY 2020 (arXiv 2008.12937); Reguera et al., Scientific Reports 2020; Pfau et al., CHI 2020; Constant and Levieux, CHI 2019; Clark et al., Neuron 2009; Finserås et al. 2019; Engeser and Rheinberg 2008; Allart et al., FDG 2017; Pelánek, Computers and Education 2016; Kohavi et al., Trustworthy Online Controlled Experiments (2020); Sensor Tower Royal Match calendar 2026; Naavik digests on Royal Match, Royal Kingdom and Monopoly Go; Deconstructor of Fun win streak (2024-08); NYT Games 2025 totals via NBC and TODAY; DarkPattern.games; Zagal, Björk, Lewis 2013; GameAnalytics 2026 benchmarks; AI Act Regulation 2024/1689 and Commission guidelines C(2025) 5052; KIDS Act COM(2026) 681 coverage (William Fry, PocketGamer.biz); DFA (Parliament legislative train); CPC key principles 2025-03-21; UK DMCC Act coverage (CMS, Osborne Clarke); FTC v. Epic coverage; Apple App Review Guidelines, last updated 2026-06-08 [Official, read at source].
