# Sources (annotated)

> Compiled 2026-10-16 from the research pass of the same day (five parallel questions) behind `research/player-experience.md`. Only developer.apple.com could be opened from this environment; every other source is known from search summaries of the named page or paper and carries [Reported] or weaker. "URL not recorded" means the notes named the publisher and date but not the link; search by title, DOI or arXiv id before relying on it. Items marked "verify" must be read at the source before anyone quotes them. A single source never earns more than [Unverified]; a page seen only as a search summary never earns [Official].

## Block Blast and its claims

| # | Source | Date | Supports | Label |
|---|--------|------|----------|-------|
| 1 | AdExchanger daily roundup | 2026-10-15 | Relays the viral decompile video by Ayomide Omolewa (a0.dev): "high value ad harvest", "death algorithm" timed to a ready rewarded ad | [Reported, 2026-10]; the claims themselves are unverified |
| 2 | MetaFilter thread 214827 | 2026-10-14 | Same claim, discussion | [Reported, 2026-10] |
| 3 | mobilegamer.biz, Hungry Studio interview | 2025 | Heavy experimentation (A/B tests, about 97% fail), algorithms govern block generation, pacing and difficulty | [Reported, 2025] |
| 4 | Business Wire, Block Blast press release | 2026-01-08 | About 70M DAU and 300M MAU; 10,000+ A/B tests in 2025, 300+ daily; simulation tool | [Reported, 2026-01] (company statement) |
| 5 | Sensor Tower and AppMagic via PocketGamer.biz and Applixir | 2026 | About USD 127M ad revenue January to May 2026 in 19 countries [Contested period]; 356.2M installs in 2025; revive capped at one per session (Applixir, vendor) [Unverified]; session about 12 minutes (Udonis, AppMagic) | [Reported, 2026-10] |

## Industry record on tuned difficulty

| # | Source | Date | Supports | Label |
|---|--------|------|----------|-------|
| 6 | Chen et al., EOMM: An Engagement Optimized Matchmaking Framework, WWW 2017 (arXiv 1702.06820) | 2017 | Churn minimizing matchmaking; simulation on EA data; deployment not shown | [Reported] |
| 7 | Xue et al., Dynamic Difficulty Adjustment for Maximized Engagement, WWW 2017 companion | 2017 | "Up to 9%" engagement, neutral monetization | [Reported], vendor, verify |
| 8 | EA patents US 9,919,217 and US 10,286,323 | n/a | Churn prediction adjusts game variables; spend reportedly an input | [Reported]; claims not read |
| 9 | Activision US 9,789,406 and coverage | 2017-10 | Matchmaking to drive purchases; "has not been implemented in-game" | [Reported] |
| 10 | Zajonc v. EA coverage (VGC) | 2021 | Class action 2020-11, dropped 2021-03 after EA said the tech "never was in FIFA, Madden or NHL" | [Reported] |
| 11 | Kabam US 9,555,324 | n/a | Item effectiveness from past spend, "imperceptibly" | [Reported]; claims not read |
| 12 | Netmarble US 2024/0021050 A1 | 2024 | Better odds after a purchase; status unknown | [Reported] |
| 13 | King patents US 9,278,282, 9,387,401, 10,376,779 | n/a | Track failures per level, adjust target or moves, give a booster | [Reported] |

## Studies on difficulty, adaptation and churn

| # | Source | Date | Supports | Label |
|---|--------|------|----------|-------|
| 14 | Ascarza, Netzer, Runge, International Journal of Research in Marketing (doi 10.1016/j.ijresmar.2025.01.006) | 2025 | 12 week RCT, 300,000+ players, holdout; easier piece allocation for higher churn risk players raised engagement, long run retention and total spending; in round purchases fell; stronger for progress prone players and past spenders | [Reported, 2026-10] |
| 15 | Columbia Business School brief on 14 | 2025 | Ad revenue +21% | [Reported], verify |
| 16 | Gudmundsson et al., IEEE CIG 2018 (King) | 2018 | Human like CNN playtesting correlates with average level difficulty, cheaper than MCTS | [Reported] |
| 17 | King GDC "Sugary Statistics" (GDC Vault 1034392) and mobilegamer.biz coverage | n/a | 15,000 levels; harder early level converted more short term, easier retained longer | [Reported], details to verify |
| 18 | Roohi et al., CHI PLAY 2020, Rovio and Aalto (arXiv 2008.12937) | 2020 | RL agents plus population simulation predict pass and churn; 95k players, 168 levels; churn = 7 days inactive | [Reported] |
| 19 | Reguera et al., Scientific Reports | 2020 | Engagement versus difficulty power law, 12M Candy Crush players | [Reported] |
| 20 | Pfau, Smeddinck, Malaka, CHI 2020 | 2020 | Heuristic DDA noticeable; deep player models improved intrinsic motivation in an MMORPG field study | [Reported] |
| 21 | Constant and Levieux, CHI 2019 | 2019 | DDA can cause overconfidence | [Reported] |
| 22 | Controlled DDA study via CEEOL (221 participants) | n/a | Performance up, enjoyment not different | [Reported] |
| 23 | Clark et al., Neuron | 2009 | Near misses raise desire to continue in slot tasks (with perceived control) | [Contested] |
| 24 | Waterloo thesis; Finserås et al. 2019; Yong 2018 | 2018 to 2019 | Near misses rated frustrating with strong urge to continue; no persistence effect in skill games | [Contested] |
| 25 | Engeser and Rheinberg | 2008 | Flow as heuristic, mixed support | [Contested] |
| 26 | Allart et al., FDG 2017 (Ubisoft survival analysis) | 2017 | Flow supported in two games | [Reported] |
| 27 | Oulu thesis | 2026 | Day 0 session features predict churn best; XGBoost ROC AUC 0.7565 in one game | [Reported] |
| 28 | Pelánek, Computers and Education | 2016 | Elo style joint ratings of skill and item difficulty | [Reported] |
| 29 | Lichess Glicko 2 puzzle ratings | n/a | Puzzles need many (hundreds of) attempts for stable ratings | [Reported] |
| 30 | Kim et al., PLOS ONE | 2017 | Churn models across genres, 193k players; best model varies | [Reported] |
| 31 | Runge et al. (Wooga) | n/a | High value player churn, 14 days; neural network best AUC; currency incentive A/B | [Reported] |
| 32 | Periáñez et al. | n/a | Survival ensembles for churn | [Reported] |
| 33 | Kristensen and Burelli | 2022 | Sequential plus aggregated features | [Reported] |
| 34 | Playliner via WN Hub | n/a | About one level in five hard in top match 3; King's first hard level near 10; 64% flag hard levels | [Unverified] (secondary) |
| 35 | Fan wikis on the 7 bag randomizer | n/a | Bag randomizers cap droughts | [Unverified] |

## Market mechanics

| # | Source | Date | Supports | Label |
|---|--------|------|----------|-------|
| 36 | Sensor Tower, Royal Match event calendar | 2026 | Six tournament formats stacked with win streak, co-op, milestone, merge and album chase; weekend peaks | [Reported, 2026-10] |
| 37 | Naavik digests on Royal Match, Royal Kingdom and Monopoly Go | n/a | Royal Pass +2% D30; Monopoly Go ARPDAU estimate; Royal Kingdom first year | [Reported] |
| 38 | Deconstructor of Fun, win streak | 2024-08 | Escalating pre placed boosters, lost on fail | [Reported] |
| 39 | NYT Games 2025 totals via NBC and TODAY | 2025 | 11.2B solves in 2025; streaks valued | [Reported] |
| 40 | DarkPattern.games | n/a | Player votes on lives, "wait to play", "pay to skip" | [Reported] |
| 41 | Zagal, Björk, Lewis, dark game design patterns | 2013 | Dark pattern taxonomy | [Reported] |
| 42 | GameAnalytics 2026 benchmarks | 2026 | Median D1 about 22% in 2025, declining | [Reported] |
| 43 | Sensor Tower via PocketGamer.biz on Monopoly Go | n/a | Events every 1 to 3 days; partner events +34% revenue; 70% return daily | [Reported] |
| 44 | Rollic VP on Color Block Jam | n/a | About 10% D90 called healthy | [Reported] |

## Law and stores

| # | Source | Date | Supports | Label |
|---|--------|------|----------|-------|
| 45 | Apple App Review Guidelines, https://developer.apple.com/app-store/review/guidelines/ | last updated 2026-06-08, read 2026-10-16 | 2.3.1(a), 5.6, 5.1.1, 5.1.2(iii) as quoted in the [ethics module](ethics-law-and-store-rules.md) | [Official, 2026-06] |
| 46 | AI Act, Regulation (EU) 2024/1689 | 2024 | Art 5(1)(a) and (b); fines up to EUR 35M or 7%; applies since 2025-02-02 | [Reported] |
| 47 | Commission guidelines on prohibited AI practices C(2025) 5052 | 2025-07-29 | Game profiling children with personalised unpredictable rewards as a prohibited example; "temporal manipulation"; intent not required; on device in scope | [Reported, 2025-07]; open the PDF |
| 48 | KIDS Act proposal COM(2026) 681 coverage (William Fry, PocketGamer.biz) | 2026-09-17 | Minors in games: real money currency value, no variable rewards, no streaks or daily return rewards, profiling off by default | [Reported, 2026-09]; a proposal; scope conflicts |
| 49 | Digital Fairness Act, Parliament legislative train | 2026-10 | Planned scope; no text tabled as of 2026-10-16 | [Reported, 2026-10] |
| 50 | CPC key principles on in-game virtual currencies | 2025-03-21 | Real money prices; no time pressure on children | [Reported] |
| 51 | CPC coordinated action against nine companies | 2026-09-30 | Enforcement | [Reported] |
| 52 | Consumer Rights Directive, personalised price disclosure | n/a | Disclose automated personalised prices | [Reported]; article number to verify |
| 53 | UK DMCC Act 2024 coverage (CMS, Osborne Clarke) | 2026-04 | CMA direct fines up to 10% of global turnover; first fine 2026-04 | [Reported, 2026-04] |
| 54 | FTC v. Epic coverage | 2022 to 2023 | USD 245M refunds for dark patterns; USD 275M COPPA penalty | [Reported] |
| 55 | Italy AGCM probe of Activision Blizzard (research notes) | 2026-01 | Urgency and currency cost | [Reported] |
| 56 | UK ICO Children's Code (research notes) | n/a | Profiling off by default, no nudges | [Reported]; standards to verify |
| 57 | COPPA updated rule compliance date (research notes) | 2026-04-22 | Children's data in the US | [Reported]; verify |

## Method and tools

| # | Source | Date | Supports | Label |
|---|--------|------|----------|-------|
| 58 | Kohavi, Tang, Xu, Trustworthy Online Controlled Experiments | 2020 | Holdouts, sample ratio mismatch checks | [Reported] |
| 59 | Statsig holdout documentation (research notes) | n/a | Holdouts of 1 to 2% recommended | [Reported, 2026-10] |
| 60 | PostHog holdouts (research notes) | n/a | Holdout support | [Reported, 2026-10] |
| 61 | Firebase Remote Config and personalization (research notes) | n/a | Web fetch minimum 12 hours; personalization uses a holdout | [Reported, 2026-10] |
| 62 | ONNX Runtime Web (research notes) | n/a | Gradient boosted models in the browser via WASM | [Reported, 2026-10] |

## Which module rests on which sources

| Module | Main sources |
|--------|--------------|
| [Difficulty measurement and calibration](difficulty-measurement-and-calibration.md) | 16, 17, 18, 19, 28, 29 |
| [Difficulty curves and level design signals](difficulty-curves-and-level-design-signals.md) | 17, 19, 23 to 26, 34, 27, 42 |
| [Fair randomness and solvability](fair-randomness-and-solvability.md) | 1, 2, 14, 15, 35 |
| [Adaptive policy design](adaptive-policy-design.md) | 14, 20, 21, 22 |
| [Sessions, opens and return reasons](sessions-opens-and-return-reasons.md) | 4, 5, 36 to 44, 48 |
| [Player modeling and churn](player-modeling-and-churn.md) | 14, 18, 27, 28, 30 to 33, 45, 62 |
| [Ethics, law and store rules](ethics-law-and-store-rules.md) | 1, 2, 4, 6 to 13, 23, 24, 45 to 57 |
| [Experiments and measurement](experiments-and-measurement.md) | 14, 15, 22, 58 to 61 |
| [Architecture and telemetry](architecture-and-telemetry.md) | 28, 45, 48, 56, 61, 62 |

## How to strengthen a label

| From | To | What it takes |
|------|----|---------------|
| [Reported] study | [Study, YYYY-MM] | Read the paper itself; record method, sample and the exact effect with its interval |
| [Reported] law | [Official, YYYY-MM] | Read the official text (EUR-Lex, the Commission PDF, legislation.gov.uk, the FTC order) and quote the article |
| [Unverified] secondary | [Reported] | A second independent dated source |
| [Contested] | Stays contested | Present both sides; do not pick one for convenience |
| Vendor number | Stays vendor | Name the vendor and its interest every time |

Record every upgrade in `ads-master/VERIFIED.md` (per project) or in this file and the dossier (in this repo), with the date read.

## Open items to verify at the source

From the dossier section 9: the Ascarza et al. effect sizes (+21% ad revenue), the EA "up to 9%", King's GDC talk details, the AI Act guidelines' game example and wording, the KIDS Act text for game provisions and dates, the CRD article number, the DFA status, GDPR Art 22 and children's data, UK ICO Children's Code standards, Google Play Families and Deceptive Behavior policies, PEGI 2026 criteria, Turkey (Law 7578, KVKK). Clear them with the `ads-verify` skill and record results in `ads-master/VERIFIED.md`.
