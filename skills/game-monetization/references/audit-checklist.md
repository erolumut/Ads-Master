# Game Monetization Audit Checklist (scored)

> Knowledge as of 2026-10. Score every item Pass, Partial or Fail with evidence (file, script output, console screen, export and date). An item without evidence is a Fail. Items that do not apply (ads items for a game without ads, store items for a web only game) are N/A and leave the denominator. Severity weights: Critical 5, High 3, Medium 2, Low 1. Pass earns the full weight, Partial half, Fail 0. The rubric is at the end.

## A. Policy file and contract

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | A `monetization-policy.json` exists per product, declares `contractVersion` and `policyRevision` | Without it every check and dashboard is guesswork | File in the product repo and `ads-master/data/` | Critical | Draft it ([Policy file and conformance](policy-file-and-conformance.md) section 2) |
| A2 | The product's code imports the policy (constants such as tries per day are read from it or asserted equal to it) | A copied policy drifts | Product repo conformance test (contract section 9 item 1) | Critical | Import it; add the test |
| A3 | `monetization_check.py` passes | Fairness, consumer and store rules in one gate | Script output, exit 0 | Critical | Fix per the failure table |
| A4 | `monetization_conformance.py` passes with the tracking plan and every store's declarations | Coverage and declarations | Script output, exit 0 | High | Fix per the failure table |
| A5 | Every policy change raised `policyRevision` and has an `EXPERIMENTS.md` row and a change request | Results attributable to changes | Git history, EXPERIMENTS.md, journal | High | Adopt the protocol |
| A6 | Kill switch tested in the last 90 days and after the last SDK update | Fast containment | Test record | High | Test and record |
| A7 | `GAME_ECONOMY.md` matches the policy file | People read the sheet, code runs the file | Side by side read | Medium | Sync |

## B. Fairness

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | No purchase, ad or reward changes counted attempts on any ranked board | Ranked results are never purchasable | Checker, product conformance test item 2 | Critical | Remove the grant or move it to practice |
| B2 | Group rounds write only to group boards; the global board query excludes them | No money lift on a global board | Policy `writesTo`, product test item 3 | Critical | Restrict boards, fix the query |
| B3 | Derived boards (streaks, season tables) are declared, and streak protection is decided explicitly | A streak freeze can be a paid advantage | Policy `modes`, `DECISIONS.md` | High | Declare and decide |
| B4 | Rewarded ads never grant a counted try | Unequal access | Policy placements | Critical | Grant an uncounted replay instead |
| B5 | Pass tracks in ranked products grant only cosmetics, access or progression items unusable in ranked modes | Hidden pay to win | Catalog grants, pass design | High | Rework the track |

## C. Economy and catalog

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Every purchasable currency shows its real money price at purchase | EU CPC principles | Checker, UI screenshot | Critical | Show the price |
| C2 | No forced leftovers (pack sizes fit item prices) | CPC principles | Price table vs pack sizes | High | Resize packs or prices |
| C3 | Sources and sinks sheet built from the game's data for light, typical and engaged players, read monthly | Inflation and value | `GAME_ECONOMY.md`, journal | Medium | Build it |
| C4 | Every SKU store neutral with typed grants, integer prices, every store id | Catalog integrity | Checker | High | Fix the catalog |
| C5 | Ladder rungs each have a role; prices set with pricing-strategy | Coherent pricing | Ladder table, pricing-strategy output | Medium | Rebuild the ladder |
| C6 | No random paid items, or odds, label, age and country rules all met | Store and law | Checker, odds screen, listing | Critical | Remove or comply |

## D. Offers

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | No price escalation inside an attempt, including sibling offers | Pressure pattern | Checker | Critical | One price per moment |
| D2 | Moves, time and booster offers carry `maxPerAttempt` and a fixed shown price | Progression rule | Checker, UI | High | Add caps, show price |
| D3 | No countdown or scarcity copy where minors may play; none anywhere without a real deadline | Consumer law, CPC | Checker, copy review | Critical | Remove |
| D4 | Every offer has a daily or per attempt cap; no stacked pop ups; one offer per moment | Player trust (VZBV objections to Monopoly Go) | Policy, session recording | High | Cap and sequence |
| D5 | Ad removal and subscription copy says exactly what is removed ("No ads" only when true) | Misleading claims | Offer screen, listing, ads | High | Rewrite through compliance |
| D6 | Subscription paywalls meet store disclosure rules (renewal price most prominent, trial terms, Restore, Terms and Privacy) | Apple 3.1.2, Play billing | Paywall screenshot, store-submission dossier | Critical | Fix the paywall |
| D7 | Starter packs and piggy banks show price and content honestly; no invented reference prices | Consumer law | Offer screens, compliance log | Medium | Rewrite |

## E. Ads and mediation

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | One mediator with the choice recorded | Clean demand and reads | `DECISIONS.md` | Medium | Decide and record |
| E2 | Bidding first; waterfall lines have a recorded reason | Yield | Mediation config | Medium | Clean up |
| E3 | Ad unit names equal policy placement ids | Per placement economics | Mediation config vs policy | High | Rename or map |
| E4 | Category blocks and max content rating fit the audience | Brand and child safety | Mediation settings | High | Set them |
| E5 | Payout terms and thresholds recorded from the live accounts | Cash planning | Memory file | Low | Record |
| E6 | SDK size, cold start and crash rate measured per adapter | Vitals and retention | Build reports, vitals | Medium | Measure |

## F. Placements and frequency

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Rewarded: opt in, server granted on completion, daily cap | Player choice, fraud | Checker, server code review | High | Fix |
| F2 | Interstitial: grace, cooldown, session cap, reset after rewarded; natural breaks only | Retention | Checker, session recording | High | Fix |
| F3 | No ad inside a counted attempt or between a fail and its continue offer | Fairness, decision space | Session recording | Critical | Move the placement |
| F4 | Banners only on menus and loading screens | Accidental taps | Checker, screens | Medium | Move |
| F5 | Payers and ad removal buyers see no interstitials | Trust | Config, test account | Medium | Exclude |
| F6 | Every frequency change tested 7 days or more with D1 and D7 guard rails | No silent retention loss | EXPERIMENTS.md | High | Test before shipping |

## G. Consent and minors

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | No ad SDK initializes and no identifier is read before consent in the EEA and UK, or before ATT on iOS | CNIL fine precedent; store rules | Test with consent denied (network capture) | Critical | Fix the order |
| G2 | Google certified CMP with IAB TCF in the EEA and UK | Ad demand and law | CMP config | High | Install |
| G3 | Under 13 or unknown age: child directed treatment, no personalized ads, certified SDKs where the store requires | COPPA, Families | Config, SDK list | Critical | Fix |
| G4 | Parental purchase approval where the law asks (US under 16 guidance, Turkey Law 7578) | Law | Purchase flow test | High | Build the flow |
| G5 | Store age rating answers match the policy audience | Declarations | `monetization_conformance.py` with declarations | High | Fix the console answers (G3) |

## H. Payment operations

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | Server grant ledger idempotent on store and transaction key; client never grants | Duplicate and fake grants | Code review, contract test item 4 | Critical | Build the ledger |
| H2 | Refund and dispute notifications wired for every store; entitlements revoke | Revenue truth, abuse | Notification logs | Critical | Wire them |
| H3 | Consumable clawback rules written and shown to players | Fairness, disputes | Rules page, ledger | Medium | Write and show |
| H4 | Disputes never punished beyond the refunded item | Regulators | Support macros, code | High | Remove punishments |
| H5 | EU withdrawal handling reviewed by compliance per market | Consumer law | Compliance verdict | High | Review |
| H6 | Daily, weekly and monthly reconciliation running | Grants without receipts | Journal | High | Start the runbook |

## I. Web monetization (web or PWA games)

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Tax decision (register and remit, or merchant of record) made before the first sale | VAT per buyer country | `DECISIONS.md`, compliance | Critical | Decide |
| I2 | Webhooks verified server side; grants after verification | Fraud | Code review | High | Fix |
| I3 | Access to play never depends on ad availability | Ad blockers, beta programs | Test with an ad blocker | Medium | Fix |
| I4 | No portal exclusivity signed without review | Distribution lock in | Contract register | High | Review with growth-orchestrator |

## J. Measurement and reading

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| J1 | Definitions in `METRICS.md` from measurement's `game-kpis`; no local redefinitions | One owner per number | Report vs METRICS.md | High | Align |
| J2 | Revenue reported net of fees, tax and refunds, with the basis stated | Truth | Report | High | Restate |
| J3 | Impression level ad revenue reaches analytics and the MMP per placement | Per placement economics | `ad_revenue` events | Medium | Hand off to measurement |
| J4 | Weekly read uses the decomposition tree and per placement and per offer tables | Find the factor that moved | Last 4 weekly reads | Medium | Adopt the template |
| J5 | Tests read by `policy_revision` with a holdout | Attribution | EXPERIMENTS.md | High | Add holdouts |

## K. Store declarations and disclosures

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| K1 | A declarations file exists per store, recorded from the live console in the last 90 days | The record the check reads | Files, dates | High | Record (store-submission) |
| K2 | "Contains ads", in-app purchases and loot box answers match the policy | Store policy, UK ASA label | `monetization_conformance.py` | Critical | Fix the answer (G3) |
| K3 | Odds shown before purchase for every random item | Apple 3.1.1, Play | Screen | Critical | Show odds |

## Audit report template

```
# Monetization audit: <game>, <platforms and stores>, <date>
Data used: <files, exports, consoles, date ranges>; Freshness check: <date>
Scripts: monetization_check.py <exit>, monetization_conformance.py <exit> (paste the FAIL lines)
Score: <overall %>, grade <A to F>; section scores A to K
Critical fails (first)
Top 5 fixes (impact x confidence x ease)
Findings by section (item, result, evidence, fix)
30, 60, 90 day plan
Change requests (G3 lines)
Handoffs requested
Data gaps and [Unverified] items
```

## Quick audit (45 minutes, cold start)

With the policy file, the tracking plan and one store console, score these first and list the rest as data gaps: A1, A3, A4, B1, B2, C1, D1, D3, F3, G1, H1, H2, K2.

## Scoring example

Section B with B1 (Critical 5, Pass), B2 (Critical 5, Partial: the boards are right, the global query is untested), B3 (High 3, Fail), B4 (Critical 5, Pass), B5 N/A: earned = 5 + 2.5 + 0 + 5 = 12.5; possible = 5 + 5 + 3 + 5 = 18; section score 69%.

## Scoring rubric

1. Section score = sum of earned weights / sum of possible weights for applicable items.
2. Overall score = sum of earned weights across all sections / sum of possible weights (no extra section weights).
3. Grades:

| Overall | Grade | Meaning |
|---------|-------|---------|
| 90% to 100% | A | Fair, lawful and measured; focus on tests and new markets |
| 75% to 89% | B | Solid; fix High items within 30 days |
| 60% to 74% | C | Leaking revenue or trust; fix Critical and High items before new offers |
| 40% to 59% | D | Foundations missing (policy, ledger, consent); fix before any test |
| under 40% | F | Stop new monetization work; rebuild the foundations |

4. Override: any Critical item at Fail caps the grade at C and goes first in the report. A Fail on B1, B2, B4, G1 or H1 is also an incident: raise it in `ads-master/INCIDENTS.md` and propose the kill switch for the affected offer or placement (G3).
