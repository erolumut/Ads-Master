# Ethics, Law and Store Rules

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). Apple's App Review Guidelines (last updated 2026-06-08) were read at the source and are quoted [Official, 2026-06]. Every other legal fact comes from search summaries and carries [Reported, YYYY-MM]; items marked "verify" must be read at the source before anyone relies on them. This is our reading, not legal advice; `compliance` owns the verdict on any player facing text and a lawyer owns the verdict on any market launch.

Gate: verdicts and red list checks are G1. A design that touches minors, personalised prices or profiling goes to `compliance` before it ships.

## 1. The Block Blast claim, once

A viral video (2026-10) claimed a decompile of Block Blast shows difficulty and loss timing driven by each player's predicted ad value: a "high value ad harvest" rule, a "death algorithm" that makes the next turn unwinnable when an expensive rewarded ad is ready, and a secret score bonus after a revive. These claims are unverified: one creator, relayed by AdExchanger (2026-10-15) and MetaFilter (2026-10-14); no code, no independent test, no studio response [Reported, 2026-10]. The studio does confirm heavy experimentation (10,000+ A/B tests in 2025, 300+ running daily, a simulation tool) [Reported, 2026-01].

Whatever the truth about one game, the spend and ad linked versions are high legal risk: the AI Act Art 5, EU and UK consumer law, and Apple 2.3.1, 5.6 and 5.1.2(iii). We do not build them.

## 2. The industry record

| Item | What it is | Status | Label |
|------|-----------|--------|-------|
| EA, EOMM (WWW 2017) | Matchmaking that minimizes predicted churn; simulation on real EA data | Paper; deployment not shown; criticized | [Reported] |
| EA DDA for maximized engagement (WWW 2017 companion) | Level transition probabilities tuned for stay time; "up to 9%" engagement, neutral monetization | Vendor reported, verify | [Reported] |
| EA DDA patents (US 9,919,217; US 10,286,323) | Churn prediction adjusts game variables; spend reportedly an input | Claims not read | [Reported] |
| Zajonc v. EA (2020-11, dropped 2021-03) | Class action alleging DDA to push packs | Dropped after EA said the patent tech "never was in FIFA, Madden or NHL" and gave technical access | [Reported] |
| Activision US 9,789,406 (2017) | Matchmaking to drive purchases | Activision: "has not been implemented in-game" | [Reported] |
| Kabam US 9,555,324 | Item effectiveness from past spend, "imperceptibly" | Claims not read | [Reported] |
| Netmarble US 2024/0021050 A1 | Better odds after a purchase | Application status unknown | [Reported] |
| King patents (US 9,278,282 and others) | Track failures per level, adjust target, moves or give a booster | Retention tuning, no purchase targeting seen | [Reported] |

Large companies patent spend linked ideas and then publicly deny using them. The denial is the signal: the spend linked version is a liability, not a secret weapon.

## 3. Verdicts

Our reading, not legal advice (dossier section 5).

| Case | Practice | Verdict | Why |
|------|----------|---------|-----|
| a | Adaptive difficulty that helps a struggling player, disclosed, in private modes | Low risk | Play signals, visible, switchable, no harm mechanism |
| b | Difficulty or loss timing tuned to ad or spend value | High risk; do not build | AI Act, consumer law, Apple 5.6 and 2.3.1 |
| c | Secret score inflation | High risk | Deception, and it breaks every shared score |
| d | Personalised offers | Moderate | Disclose, consent, never for minors without strict limits; owned by `game-monetization` |
| e | On device ML profiling | Moderate to high | Consent and disclosure; on device is not an exemption |

## 4. EU law

### 4.1 AI Act Art 5

| Point | Content | Label |
|-------|---------|-------|
| Art 5(1)(a) and (b) | No AI system using manipulative or deceptive techniques, or exploiting vulnerabilities (age), that materially distorts behavior and causes significant harm | [Reported, 2025-07] |
| Fines | Up to EUR 35M or 7% | [Reported, 2025-07] |
| In force | Applies since 2025-02-02 | [Reported, 2025-07] |
| Commission guidelines C(2025) 5052 (2025-07-29) | Reportedly cite a game that profiles children and builds personalised, unpredictable rewards through addictive reinforcement loops as a prohibited example, and name "temporal manipulation"; intent is not required; on device is still in scope | [Reported, 2025-07]; open the PDF |
| Guidelines on transparent personalised recommendation | The research notes report that the guidelines (dated 2025-02-04 in that note) treat transparent personalised recommendation as lawful | [Reported]; date and wording to verify |

What it means: an adaptive system whose purpose or effect is to push a player into harmful spending or play, especially a child, is in the prohibited zone regardless of intent. A visible, bounded system that helps a player and can be switched off is not built on manipulation.

### 4.2 KIDS Act proposal

COM(2026) 681, 2026-09-17. Reported content for minors in online games: real money value for currency, no variable rewards, no streaks or daily return rewards, nothing that undermines a minor's decision to stop or pushes play at set times through penalties or lost benefits, profiling based recommendations off by default [Reported, 2026-09]. A proposal, not law; sources conflict on scope. We follow the direction now ([sessions](sessions-opens-and-return-reasons.md) section 8).

### 4.3 Digital Fairness Act

Planned: dark patterns, addictive design, unfair personalisation, game currencies, pay to progress. No text tabled as of 2026-10-16 [Reported, 2026-10]. Check status in the Freshness protocol each month.

### 4.4 UCPD and CPC

| Item | Content | Label |
|------|---------|-------|
| Unfair Commercial Practices Directive | Misleading and aggressive practices are unfair | [Reported] |
| CPC key principles on in-game currencies (2025-03-21) | Real money prices; no time pressure on children; not binding | [Reported] |
| CPC coordinated action against nine companies (2026-09-30) | Enforcement on game practices | [Reported] |
| Consumer Rights Directive | Tell the consumer when a price is personalised by automated means | [Reported]; article number to verify |
| Italy AGCM probe of Activision Blizzard (2026-01) | Urgency and currency cost (research notes) | [Reported] |

### 4.5 GDPR basics as reported

The dossier lists GDPR Art 22 (automated decisions) and children's data as open items to verify. Working rules until verified:

| Rule | Basis |
|------|-------|
| A pseudonymous random install id, consent gated telemetry, state kept on the device where possible | Dossier architecture; Apple 5.1.1 [Official, 2026-06] |
| Collect only the play signals the policy needs | Data minimisation principle; check with `compliance` |
| No inference of sensitive traits or spend capacity | Dossier principle 2 |
| Whether adaptive difficulty is an Art 22 decision | Verify at the source |
| UK ICO Children's Code: profiling off by default, no nudges | [Reported] (research notes); standards to verify |
| US COPPA: research notes cite a compliance date of 2026-04-22 for the updated rule | [Reported]; verify |

Consent and privacy depth: [compliance privacy module](../../compliance/references/privacy-in-marketing-and-consent.md) and [measurement consent](../../measurement/references/consent-and-privacy.md).

## 5. UK and US

| Rule | Content | Label |
|------|---------|-------|
| UK DMCC Act 2024 | The CMA fines directly, up to 10% of global turnover; first fine 2026-04 | [Reported, 2026-04] |
| FTC v. Epic (2022 to 2023) | USD 245M refunds for dark patterns; USD 275M COPPA penalty | [Reported] |
| Candy Crush All Stars class action | Listed in the research notes | [Reported] |

## 6. Apple App Review Guidelines (quoted)

| Guideline | Quote | Meaning for us |
|-----------|-------|----------------|
| 2.3.1(a) | "Don't include any hidden, dormant, or undocumented features in your app"; "Egregious or repeated behavior is grounds for removal from the Apple Developer Program" | Adaptation is documented and visible; no hidden switch keyed to money or ads |
| 5.6 | Apps "should never prey on users ... trick them into making unwanted purchases ... or engage in any other manipulative practices"; repeated manipulative behavior leads to removal from the program | No difficulty, loss timing or offer timing aimed at purchases |
| 5.1.1 | Consent for collecting usage data "even if such data is considered to be anonymous"; the privacy policy names all uses | Telemetry is consent gated; the privacy policy names adaptation |
| 5.1.2(iii) | "Apps should not attempt to surreptitiously build a user profile based on collected data" | The estimator is visible and resettable; no hidden profiles |

All [Official, 2026-06]. Google Play Families and Deceptive Behavior policies and PEGI 2026 criteria are open items to verify (dossier section 9).

## 7. Red list: never build

| Pattern | What it is | Why it is out |
|---------|-----------|---------------|
| Death algorithm | Making a turn unwinnable or a loss likelier when an ad or offer is ready | Manipulation, AI Act Art 5, Apple 5.6 and 2.3.1, consumer law |
| Ad harvest | Difficulty or fail timing tuned to a player's ad value or ad readiness | Same; ad signals are forbidden inputs |
| Score inflation | Changing a score after the fact, secretly or not | Deception; breaks shared boards; `scores.modifyAfterFact` must be false |
| Value based difficulty | Difficulty, odds or draws from spend, payer tier, LTV, device value, country or any personal trait | Exploits players by value; forbidden inputs |
| Engineered near misses | Generating near misses on purpose to raise the urge to continue | Near miss effects are [Contested]: they raise the urge to continue in slot tasks and are rated frustrating (Clark 2009), persistence effect not shown in skill games (Finserås 2019, Yong 2018); deliberately engineering them is a manipulation pattern either way |
| Rubber banding in ranked | Adapting difficulty, matchmaking or draws in a ranked, daily, race or group mode | Shared modes are identical for everyone |
| Hidden adaptation | Any adaptation without the explain line, log, setting and reset | Apple 2.3.1 and 5.1.2(iii) |
| Spend linked matchmaking | Matching to drive purchases (Activision patent idea) | Publicly denied by its own patentee; manipulation |
| Better odds after purchase | Netmarble application idea | Value based randomness |
| Loss threat return reasons | "Your streak dies tonight" | Pressure; blocked for minors by the checker |

`pxe_policy_check.py` blocks the names and inputs of most of these mechanically ([policy format](policy-format.md) section 4). The ones it cannot see (code that ignores the file) are covered by the engine conformance tests, the rigged stream test ([fair randomness](fair-randomness-and-solvability.md) section 5.3) and the [audit](audit-checklist.md).

## 8. Green list: build these

| Pattern | Condition |
|---------|-----------|
| Ease a struggling player by one step | Private modes, play signals, visible, capped, holdout |
| Hint offer when stuck | The player can decline |
| Break offer after a long fail streak | Never paired with an offer |
| Raise difficulty for a cruising player | Visible line, same bounds |
| Next goal at session end | Real content |
| Return reasons from real content and own state | Caps, quiet hours, no guilt, `lifecycle-crm` handles sends |
| Streaks with free rest days and a permanent best | No paid repair by default |
| Visible bot strength against a single player | Labeled; never secret in rated play (Avlu fit, dossier section 8) |
| Labeled assisted runs | Never on shared boards |
| Strict tier for minors | KIDS Act direction |
| Persistent holdout | Every policy |

## 9. Verdict template

```
# PXE verdict: <practice>, <product>, <date>
Case: a | b | c | d | e | other
Modes affected: <list, shared flags>
Inputs: <list>; forbidden inputs present: no | yes (stop)
Visible: explain line <key>, log yes/no, setting yes/no, reset yes/no
Minors: can play yes/no; strict tier applied yes/no
Rules cited: <AI Act Art 5 | UCPD | CPC | DMCC | Apple 2.3.1 | 5.6 | 5.1.1 | 5.1.2(iii)>
Open items to verify: <list>
Verdict: build | build with changes | needs compliance or legal review | do not build
```
