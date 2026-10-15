# Game Monetization Playbooks

> Knowledge as of 2026-10. Every play ends in a change request for human approval. Drafts in `ads-master/` (policy drafts, sheets, specs) are G1; unsubmitted store products, paused ad units and draft prices in a console are G2; changing a live price, turning on an offer or a placement, editing mediation or remote config in production, submitting store products and sending any player message are G3. Follow the project's automation stage in `ads-master/GUARDRAILS.md`.

Plays: 1 First monetization for a new game, 2 Add rewarded ads, 3 Launch a season pass, 4 Monetization drop, 5 Entering the EU or Turkey, 6 Weekly economy loop, 7 Monthly economy review, 8 Change request template.

## Play 1: First monetization for a new game

Entry: a playable game, PROJECT_BRIEF section 11 filled (core rule, modes, counted attempts, platforms, audience age), measurement's game KPIs and event taxonomy agreed.

| Step | Action | Output | Gate |
|------|--------|--------|------|
| 1 | Classify the game: daily ranked or social, level based progression, hybrid casual, ads only, web portal ([Economy and catalog](economy-and-catalog.md) section 8) | Game type with reason | G1 |
| 2 | Map modes and boards; decide derived boards (streaks, season tables) and streak protection with the human | `modes` draft, `DECISIONS.md` entry | G1 |
| 3 | Pick the default stack for the type; write what is refused and why | Stack table | G1 |
| 4 | Draft the policy file: product, stores, modes, catalog, offers, placements, consent, declarations, kill switch | `monetization-policy.json` revision 1 | G1 |
| 5 | Run `monetization_check.py` until it passes | Script output | G0 |
| 6 | Hand off prices to `pricing-strategy` (store tiers per country, web parity) | Price table | G1 |
| 7 | Add the contract events to the tracking plan with `measurement`; run `monetization_conformance.py` | Plan update, script output | G1 |
| 8 | Offer copy to `compliance`; paywall and IAP setup to `store-submission` | Verdicts, dossier rows | G1 |
| 9 | Sources and sinks sheet (progression games) from playtest data | `GAME_ECONOMY.md` | G1 |
| 10 | Product repo implements: imports the policy, ledger, consent order, kill switch, conformance test (contract section 9) | Passing product tests | Product repo |
| 11 | Create store products unsubmitted and Stripe prices in test mode | Console drafts | G2 |
| 12 | Change request: turn on the catalog and offers for a share of players with a holdout | Change request | G3 |
| 13 | Read after 7 days minimum by `policy_revision`; then 14 and 28 days | Read memo | G0 |

Defaults that keep the first release fair and simple:
- Daily ranked games: no currency; season pass, plus subscription, group round, cosmetics; free uncounted replay; no paid or earned counted tries.
- Progression games: one soft currency with real money prices shown, fixed price continues with `maxPerAttempt`, boosters taught before they are sold, ads held back early.
- No random paid items, no lives gating play, no countdowns where minors may play.

Exit: both scripts pass, product conformance test green, first read written, no guard rail breached.

## Play 2: Add rewarded ads

Entry: a game with natural breaks and a fair thing to grant, consent flow ready or planned.

1. Choose the grant per mode ([Placement and frequency policy](placement-and-frequency-policy.md) section 3): continue or multiplier in progression, uncounted replay in ranked products. Never a counted try.
2. Choose the mediator (or the web ad route) and record the reason ([Ad monetization and mediation](ad-monetization-and-mediation.md) section 2).
3. Implement the consent order before any SDK call; test with consent denied (no ad request leaves the device).
4. Add the placement to the policy: `format: rewarded`, typed grants, `optIn: true`, `grantOn: completed`, `dailyCap`; raise `policyRevision`.
5. Tracking plan: `ad_requested`, `ad_shown`, `ad_rewarded`, `ad_failed`, `ad_revenue` with `placement_id`, `mode_id`, `point`, versions; run both scripts.
6. Server grants the reward after the completion callback; the client never grants.
7. Update `storeDeclarations.containsAds` and the store forms (age rating advertising answer, "contains ads"); record the declarations file; rerun conformance (store-submission submits, G3).
8. Ad unit created paused or unpublished (G2); change request to enable it for a share of players (G3).
9. Read for at least 7 days: ARPDAU total, impressions per DAU, opt in rate among eligible, fill, D1 and D7 against the holdout, complaints.
10. Ship or roll back by revision; journal; memory only when a second read confirms.

## Play 3: Launch a season pass

Entry: a season calendar from `game-liveops` and a content cadence that can fill a track.

| When | Action | Owner |
|------|--------|-------|
| 6 weeks before | Track design within the mode rules (ranked products: cosmetics and access only); pass price with pricing-strategy | This agent, pricing-strategy, game-liveops |
| 5 weeks before | Catalog entry (`kind: season`), offer at `on_season_start`, caps; policy revision; both scripts | This agent |
| 4 weeks before | Copy to compliance (price, duration, what late buyers get, no countdown with minors); store products created unsubmitted | compliance, store-submission (G2) |
| 3 weeks before | Store in-app event or promotional content for the season start (Apple in-app events, Play promotional content) | app-store-optimization |
| 2 weeks before | Product repo build with the pass, ledger entries, refund handling, events; conformance green | Product repo, site-engineer |
| 1 week before | Change request to enable the pass at season start for all or a share of players | Human approves (G3) |
| Day 0 to 7 | Daily: purchases, refunds, complaints, crashes; offer shown per DAU and acceptance | This agent |
| Season end | Read: pass conversion among active players, revenue per DAU vs previous season, D7 and season completion (game-liveops), refunds | This agent, game-liveops |

Rules: late buyers get every reward already earned; no retroactive loss at season end; the pass never grants ranked advantage.

## Play 4: Monetization drop

Trigger: ARPDAU down more than its normal weekly variation for 2 consecutive weeks, or a sudden drop on one day that is not a calendar effect.

1. Measurement first: tracking break, consent rate change, SDK update, a store or mediation reporting delay, timezone change. If revenue truth is broken, stop and hand off to `measurement`.
2. Split IAP and ads with the decomposition tree ([Benchmarks and reading results](benchmarks-and-reading-results.md) section 2).
3. Ads side: fill (a network down, a consent string rejected, Limited Ads after a TCF problem), eCPM (seasonality, a floor change, country mix), impressions per DAU (a placement broken, a grace or cap changed, a release that moved the entry point).
4. IAP side: payer share (offers not shown, a purchase flow broken, store outage), ARPPU (SKU mix, a price change, a pass ending), refunds (a refund wave after a bad release).
5. Mix: a UA burst bringing lower value cohorts (read by install cohort with `mobile-app-growth`), a featuring spike, a new country.
6. Policy history: what changed in the last 4 revisions; which tests are running.
7. Act on the cause: roll back a revision (G3), fix the broken flow (product repo), hand off the measurement or UA cause. A broken purchase flow or grants without receipts is an incident.
8. Read again after 7 days; write the post mortem in the journal.

Never answer a drop by adding pressure: no new countdowns, no extra pop ups, no higher continue prices.

## Play 5: Entering the EU or Turkey

Entry: a product that will sell, show ads to or collect data from players in EU countries or Turkey.

| Area | EU | Turkey | Owner |
|------|----|--------|-------|
| Virtual currencies | CPC key principles 2025-03-21: real money price shown, no forced currency purchases, withdrawal rights, protect children [Reported, 2026-10] | Follow the same design rules; local law confirmed by compliance | This agent, compliance |
| Minors and purchases | DSA Art. 28 guidelines (2025-07, non binding for micro and small companies unless very large) keep minors from paid random items and manipulative design [Reported, 2026-10] | Law 7578 (passed 2026-04-22): age rating and parental controls including purchase approval on game platforms; fines from TRY 1 million to 10 million and up to 30 million; a local representative above 100,000 daily Turkish users; duties mostly about 6 months after the implementing regulation (verify) [Reported, 2026-10] | compliance, product |
| Random items | Belgium no, Netherlands no tradeable prizes; PEGI defaults new games with paid random items to PEGI 16 from 2026-06-01 [Reported, 2026-10] | Not researched in this pass | compliance, store-submission |
| Consent | Google certified CMP with IAB TCF before ad SDKs [Reported, 2026-10] | KVKK consent rules through compliance and measurement | measurement, compliance |
| Web sales tax | VAT per buyer country; register and remit or use a merchant of record | VAT duties on digital sales; same decision | compliance, human |
| Withdrawal | Digital content consent step; withdrawal function for contracts that keep a right of withdrawal (from 2026-06-19) | Distance contract rules confirmed by compliance | compliance, site-engineer |
| Price claims | 30 day prior price for any reduction claim | 10 day rule | compliance |
| Store fees | Apple EU terms from 2026-10-01 [Official, 2026-10]; Google Play fees from 2026-06-30 [Reported, 2026-10] | Store default terms | pricing-strategy, mobile-app-growth |
| Upcoming | The Digital Fairness Act is not law; a proposal was expected in Q4 2026 covering dark patterns, addictive design, virtual currencies and minors [Reported, 2026-10] | BTK age verification rules pending (verify) | compliance (Freshness) |

Steps: add the regions to `product.regions`; rerun `monetization_check.py` (it fails random items sold in BE); compliance verdict per market on offers and the purchase flow; parental approval flow for Turkey before Turkish sales where the law requires it; store declarations recorded; change request to open the market (G3).

## Play 6: Weekly economy loop (Growth tier)

| Step | Time | Detail |
|------|------|--------|
| 1. Data | 10 min | Exports or connectors; date range; revenue basis (net) |
| 2. Headline | 10 min | ARPDAU split vs trailing 4 and 8 weeks; D1 and D7 guard rails from measurement |
| 3. Tree | 10 min | Which factor moved |
| 4. Placements | 10 min | Per placement table; fill and eCPM changes |
| 5. Offers | 10 min | Per offer table; acceptance and revenue per shown |
| 6. Payments | 5 min | Refunds, chargebacks, reconciliation gaps |
| 7. Tests | 5 min | Revisions running, days in, reads due |
| 8. Change requests and journal | 10 min | Drafts, compliance routing, handoffs |

At Starter tier run it every 2 weeks; keep the daily refund and grant check.

## Play 7: Monthly economy review

1. Sources and sinks: stockpile percentiles (P50, P90, P99) for each currency; inflation flag.
2. Catalog: SKU revenue share, dead SKUs (no purchases in 60 days), refund rate by SKU.
3. Ladder: rung usage; the share of first purchases by rung.
4. Ads: paid out vs mediation reported revenue; payout status per network; SDK updates pending.
5. Segments: payer share and concentration; spend protection triggers; tier cutoffs if the quarter turned.
6. Fairness: confirm no new grant reaches a ranked board; review derived boards.
7. Freshness: store rules, mediation terms, CPC, ASA, PEGI, Turkey, Epic v Apple status ([SKILL Freshness protocol](../SKILL.md)).
8. Both scripts on the live files; audit quick items.
9. Output: `YYYY-MM-DD_game-monetization_economy-review.md` with change requests.

## Play 8: Change request (all monetization changes)

Use `ads-master/templates/CHANGE_REQUEST.md`. One line per change:

| # | Platform | Entity | Change | From | To | Reason with data (source, range) | Expected effect | Risk | Rollback | Gate | Approval |
|---|----------|--------|--------|------|----|----------------------------------|-----------------|------|----------|------|----------|
| 1 | Policy file revision 7 to 8 | Offer `moves_on_fail` | Add `maxPerAttempt` 2 | none | 2 | Checker warning; 3% of attempts saw 3 or more continue offers, 2026-09-14 to 2026-10-11 export | Fewer repeated prompts, flat revenue per shown | Small revenue loss | Revision 7 | G3 | |
| 2 | Stripe and both stores | SKU `season_pass` | New season price | EUR 2.99 | EUR 3.49 | pricing-strategy report 2026-10-08 | Revenue per DAU up, conversion down less than 10% | Conversion drop | Previous price ids | G3 | |
| 3 | Mediator | Unit `rewarded_replay` | Enable for 50% of players | paused | live 50% | Consent flow verified 2026-10-10; conformance pass | Ad ARPDAU from 0 | D7 effect | Disable unit | G3 | |

Example rows; the values are illustrative, not findings. Read back every executed change (console, config, policy revision live) and log it in the journal with a timestamp.
