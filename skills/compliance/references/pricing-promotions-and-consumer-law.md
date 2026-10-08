# Pricing, Promotions and Consumer Law

> Knowledge as of 2026-10. Rule pack for price reductions, reference prices, urgency and scarcity, drip pricing, "free", comparative advertising, superlatives, subscriptions and cancellation, and the UK DMCC Act. Applies to ads, landing pages, carts, feeds (sale_price, promotions) and emails. Offer economics belong to offer-strategy; this pack decides whether the presentation is lawful.

## 1. Price reductions and reference prices

| Rule ID | Rule | Threshold or example | Source |
|---------|------|----------------------|--------|
| PRICE-EU-01 | Any announcement of a price reduction must indicate the prior price: the lowest price the trader applied in a period of at least 30 days before the reduction | Item sold at 79 for 20 days, 99 for the 10 days before the sale: prior price is 79, not 99 | Price Indication Directive 98/6/EC Art 6a, added by Omnibus Directive 2019/2161, applied from 2022-05-28 [Official] |
| PRICE-EU-02 | Percentages and promotional statements ("lowest price", "-30%") must be calculated from that prior price; showing the 30 day low in small print while computing from a higher crossed out price is unlawful | "-30%" must be 30% off 79 | CJEU C-330/23 Aldi Süd (2024-09-26) [Official] |
| PRICE-EU-03 | Member state options: shorter periods for goods on the market under 30 days; progressive reductions may keep the price before the first reduction; perishable goods may be exempted. Personalised prices and loyalty schemes giving systematic lower prices are generally outside Art 6a; comparisons with RRP are not a price reduction announcement only if clearly distinguished | Commission guidance on Art 6a (2021/C 526/02) [Official]; German courts split on RRP strike-through prices (OLG Düsseldorf I-20 U 43/25, 2025-12-18 unlawful where it looks like the retailer's own reduction; OLG Köln 6 U 92/25, 2026-06-15 lawful); BGH cases pending [Contested] |
| PRICE-UK-01 | Reference prices must be genuine and not misleading (CMA pricing practices guidance; DMCC Act Part 4 unfair commercial practices); government announced (2026-08-09) a consultation in autumn 2026 on adding fake "was" prices, invented discounts and misleading RRPs to the automatically unfair list | Was price used for a meaningful period before the sale and genuinely charged | DMCC Act 2024; Carson McDowell 2026 [Official via secondary] |
| PRICE-TR-01 | From 2026-08-01: the "price before discount" is the lowest price actually applied in the last 10 days before the discount starts (previously 30 days), aligned with the Fiyat Etiketi Yönetmeliği; compare only within the same sales channel; perishable goods and services use the last price before the discount; conditional campaigns ("sepette indirim", spend X get Y) follow the discount ad rules; burden of proof on the advertiser | Product at 1,000 TRY for 7 days then 900 TRY for 3 days before the campaign: reference price is 900 TRY | Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği Art 14 as amended (RG 33297, 2026-07-01) [Official via law firm summaries and ministry press] |
| PRICE-US-01 | Former price comparisons must use a price at which the item was openly and actively offered in good faith for a reasonably substantial period; comparisons to "retail value" or competitors need proof; some states (for example California) set specific look-back rules | 16 CFR 233 FTC Guides Against Deceptive Pricing [Official, canonical]; California B&P 17501 (3 months) |

Evidence to attach for any reduction: price history export per channel and per SKU covering the look-back window (30 days EU, 10 days TR), the computed reference price, and the promotion dates. Feeds: Google Merchant Center `sale_price` and promotions must match the same history. Handoff: commerce-feeds and offer-strategy.

EU enforcement data: the 2025 Black Friday and Cyber Monday price sweep (25 countries, 314 traders) found one in three traders failed to display discounts correctly and 10% used drip pricing [Official, Commission 2026-03-26].

## 2. Urgency, scarcity and dark patterns

| Rule ID | Rule | Source |
|---------|------|--------|
| URG-EU-01 | Falsely stating that a product is available only for a very limited time, or only on particular terms for a very limited time, to elicit an immediate decision is always unfair | UCPD Annex I no.7 [Official] |
| URG-EU-02 | Countdown timers that reset, fake stock counters, fake "X people viewing", confirmshaming and pre-ticked add-ons are misleading or aggressive practices; additional payments via pre-ticked boxes are banned | UCPD Art 6 to 9; CRD Art 22 [Official]; EU 2022 dark patterns sweep found fake timers on 42 of 399 shops [Official, 2023-01] |
| URG-UK-01 | DMCC Act 2024 (consumer enforcement since 2025-04-06; CMA can fine up to 10% of global turnover). CMA cases on time limited sales and urgency: Wayfair and Appliances Direct (ongoing, update 2026-06), Wowcher and LivingSocial (initial stage) | Jones Day 2026-04; Macfarlanes 2026 [Official via secondary] |
| URG-TR-01 | Misleading urgency is an unfair commercial practice under Law 6502 and the regulation's annex | [Official, canonical] |
| URG-ALL-01 | Platform rules: Google Ads misrepresentation and dishonest pricing practices; Meta misleading claims | Platform policies |

Allowed urgency: real deadlines that the system enforces (sale ends Sunday 23:59 CET and the price reverts), real stock counts from inventory, real shipping cut-offs.

## 3. Drip pricing, total price and hidden fees

| Rule ID | Rule | Source |
|---------|------|--------|
| DRIP-EU-01 | Prices to consumers include all taxes and unavoidable charges; additional charges not disclosed before the contract are not payable | PID; CRD Art 6(1)(e) and 6(6) [Official] |
| DRIP-UK-01 | Headline prices must include mandatory fees. CMA direct fines: AA Driving School and BSM GBP 4.2 million plus over GBP 760,000 redress (2026-04, mandatory GBP 3 booking fee omitted); StubHub about GBP 900,000 (2026-06, delivery and service fees); Marks Electrical GBP 720,000 (2026-06, auto opt-in to extra services); Euro Car Parks almost GBP 500,000 (2025-12, failing to answer an information request); three more drip pricing investigations opened 2026-07 | Jones Day 2026-04; HSF Kramer 2026-07 [Official via secondary] |
| DRIP-US-01 | FTC Rule on Unfair or Deceptive Fees (live event tickets and short term lodging, effective 2025-05-12): total price shown more prominently; California SB 478 all-in pricing (2024-07-01) for most sectors | [Official] |
| DRIP-GOOG-01 | Google Ads dishonest pricing practices (enforced from 2025-10-28): disclose the payment model and full expense; no omission of taxes and fees; no bait and switch; no "free" for paid apps; free trials must state length and auto charge | Google Ads Help [Official] |

## 4. "Free"

| Rule ID | Rule | Source |
|---------|------|--------|
| FREE-EU-01 | Describing a product as "free" or "without charge" if the consumer has to pay anything other than the unavoidable cost of responding and collecting or paying for delivery is always unfair | UCPD Annex I no.20 [Official] |
| FREE-UK-01 | CAP 3.21 to 3.26: same principle; free trials and "free with purchase" must state conditions; do not inflate the price of the paid item | CAP Code [Official] |
| FREE-US-01 | FTC Guide on "Free": conditions disclosed clearly at the outset; no increase in the regular price of the item that must be bought; a "free" offer should not be advertised for more than 6 months in any 12 month period in the same trade area | 16 CFR 251 [Official, canonical] |
| FREE-SUB-01 | Free trials that convert to paid: state trial length, price after trial, billing date and how to cancel next to the CTA; get express consent (US ROSCA; EU CRD; UK subscription regime from 2027) | See section 7 |

## 5. Comparative advertising and superlatives

| Rule ID | Rule | Source |
|---------|------|--------|
| COMP-EU-01 | Comparative advertising is permitted when it: is not misleading; compares goods or services meeting the same needs; objectively compares material, relevant, verifiable and representative features (price may be one); creates no confusion; does not discredit or denigrate the competitor's marks or goods; does not take unfair advantage of a mark's reputation; does not present goods as imitations | Directive 2006/114/EC Art 4 [Official, canonical] |
| COMP-UK-01 | Same conditions (Business Protection from Misleading Marketing Regulations 2008); CAP 3.33 to 3.44; verifiability means the consumer can check the comparison (give the source) | [Official] |
| COMP-US-01 | Truthful comparative advertising is encouraged (FTC 1979 policy statement); competitor challenges through NAD or Lanham Act 43(a) lawsuits are the main risk | [Official, canonical] |
| COMP-TR-01 | Comparative ads allowed under conditions similar to the EU directive; supplement comparisons allowed from 2026-08-01 except on health claim matters | Ticari Reklam Yönetmeliği [Official via secondary; verify article] |
| SUP-ALL-01 | Superlatives ("best", "#1", "fastest", "lowest price") are objective claims when measurable; Germany treats sole position claims (Alleinstellungswerbung) strictly: a clear and lasting lead must be proven | DE case law [Practitioner consensus] |

Comparison file checklist: competitor product and version, date, method, sample, independent test or reproducible public data, price date and channel, and a plan to refresh (prices change daily). Naming a competitor: NEEDS HUMAN OR LEGAL REVIEW always.

## 6. UK DMCC Act 2024: what changed for marketing

| Item | Status 2026-10 | Source |
|------|----------------|--------|
| CMA direct enforcement of consumer law, fines up to 10% of global turnover | In force since 2025-04-06; four penalties to 2026-10 totalling about GBP 6.3 million | Macfarlanes, Jones Day [Official via secondary] |
| Schedule 20 banned practices (32 practices, including fake reviews, drip pricing elements, false urgency) | In force since 2025-04-06 | DMCC Act |
| Fake reviews | CMA opened five investigations 2026-03-27 (Autotrader, Feefo, Dignity, Just Eat, Pasta Evangelists); earlier 54 letters sent about missing anti-fake-review policies, 90% changed | HSF Kramer 2026-03 [Official via secondary] |
| Subscription contracts regime | Not in force. Government response 2026-04-02 targeted Spring 2027; PM announcement (2026-08-09/10) brought it forward to January 2027; regulations and guidance not yet laid | TLT 2026-08; Taylor Wessing 2026-04; HLWS1503 [Official] |
| Pricing consultation | Autumn 2026 consultation on fake was prices, invented discounts, misleading RRPs | 2026-08-09 announcement [Official via secondary] |

## 7. Subscriptions, renewals and cancellation

| Rule ID | Rule | Source |
|---------|------|--------|
| SUB-EU-01 | Withdrawal button: for distance contracts concluded through an online interface with a right of withdrawal, a function labelled "withdraw from contract here" (or unambiguous equivalent), two steps (declare, then "confirm withdrawal"), continuously available and prominent during the withdrawal period, no login or app download required where not needed to contract, with confirmation on a durable medium. Applies from 2026-06-19; transposition uneven (Germany § 356a BGB published 2026-02-05; France and Italy transposed; Belgium and Ireland late) | Directive (EU) 2023/2673 adding CRD Art 11a; Crowell 2026 [Official] |
| SUB-EU-02 | "Order with obligation to pay" button and pre-contract information (price, renewal, duration, cancellation) | CRD Art 6 and 8(2) [Official] |
| SUB-DE-01 | Cancellation button (Kündigungsbutton) for online subscriptions since 2022-07-01; after the initial term, contracts renew only month to month and can be ended with 1 month notice (since 2022-03-01) | BGB § 312k, § 309 no.9 [Official, canonical] |
| SUB-EU-03 | Digital Fairness Act proposal expected Q4 2026 (dark patterns, influencer marketing, addictive design, personalisation, subscription cancellation and renewal); legal form not announced; not law | Legislative Train 2026; PL&B 2026-05 [Official] |
| SUB-US-01 | ROSCA: clear disclosure of material terms before billing information, express informed consent before charging, simple cancellation. FTC click to cancel amendments vacated (8th Circuit, 2025-07-08); new ANPRM published 2026-03-13 (comments closed 2026-04-13); no proposed rule as of 2026-09. Enforcement continues: Amazon Prime settlement USD 2.5 billion (USD 1 billion civil penalty, USD 1.5 billion redress, 2025-09); JustAnswer (2026-01) | FTC 2026-03; Cooley 2026-03-19; FTC Amazon case [Official] |
| SUB-US-02 | State auto renewal laws: California AB 2863 (effective 2025-07-01: express consent, annual reminders, save offers only with a visible cancel button on the same page, cancel by the same medium); New York amendments (2025-11-05: price increases need consent or a 14 day cancel window with pro rata refund); New York City DCWP rule (2026-10-01: no forced exit survey); Minnesota (2025-01-01: save offers only with prior separate consent); Colorado (B2B too from 2026-02); Maryland (2026-06); Connecticut annual reminder (2026-07); Louisiana (summer 2026) | Kelley Drye 2026; Sidley 2024 [Official via secondary] |
| SUB-TR-01 | Mesafeli sözleşmeler and subscription rules under Law 6502: termination must be as easy as subscription; renewal terms disclosed | [Practitioner consensus; verify the regulation] |

Subscription offer copy checklist: price and billing period next to the CTA; trial length and price after trial; renewal date; how to cancel (link); no pre-ticked upsells; cancellation path tested on mobile.

## 8. Other consumer law items in marketing copy

| Topic | Rule | Source |
|-------|------|--------|
| Hidden advertising | Editorial content paid for by the trader without clear disclosure is always unfair (advertorials, paid search results without disclosure) | UCPD Annex I no.11 and 11a [Official] |
| Legal rights as features | Presenting rights given by law as a distinctive feature ("2 year warranty" in the EU where the legal guarantee is 2 years, "14 day returns" as a perk when it is the legal withdrawal right) | UCPD Annex I no.10 [Official] |
| Bait advertising | Advertising a product at a price without reasonable stock | UCPD Annex I no.5 and 6 |
| Origin claims | "Made in USA" needs all or virtually all US content; FTC Made in USA Labeling Rule (2021) allows civil penalties | 16 CFR 323 [Official] |
| Prize promotions | Rules vary widely (Germany, Turkey require specific terms; some countries require permits for lotteries); route to human | [Practitioner consensus] |
| Penalties EU | Widespread infringements: fines of at least 4% of annual turnover in the member states concerned, or EUR 2 million when turnover data is unavailable | UCPD Art 13 as amended by 2019/2161 [Official] |

## 9. Worked examples

| Copy | Market | Verdict | Rule | Fix |
|------|--------|---------|------|-----|
| "Was €99, now €69 (-30%)" where the item was €79 for 3 weeks before | EU | BLOCKED | PRICE-EU-01, -02 | "€69, lowest price in last 30 days €79 (-13%)" |
| "%40 indirim" computed from a list price never charged in the last 10 days | TR | BLOCKED | PRICE-TR-01 | Recompute from the 10 day low in that channel |
| "Sale ends in 02:59:59" timer that restarts per visitor | All | BLOCKED | URG-EU-01, URG-UK-01 | Fixed server end time |
| "£29 per month" with a mandatory £3 setup fee at checkout | UK | BLOCKED | DRIP-UK-01 | "£29 per month plus £3 one-off setup" in the headline, or include it |
| "Free 30 day trial" with auto renewal at $19.99 | US | APPROVED WITH EDITS | SUB-US-01, SUB-US-02 | "Free for 30 days, then $19.99/month. Cancel anytime in Settings." next to the CTA; express consent checkbox |
| "Cheaper than Brand X" | UK | NEEDS HUMAN OR LEGAL REVIEW | COMP-UK-01 | Dated price comparison basket and source shown |
| "2-year warranty included" | EU | APPROVED WITH EDITS | Annex I no.10 | "2-year legal guarantee" (not presented as an extra) unless it is a commercial guarantee beyond law |

## 10. Price evidence checklist (attach to every discount review)

| # | Evidence | Why |
|---|----------|-----|
| 1 | Price history export per SKU and per channel covering the look-back window (EU at least 30 days, TR 10 days, UK the period the was price applied) | Proves the reference price |
| 2 | Promotion start and end timestamps with time zone | Proves the deadline and the look-back anchor |
| 3 | Computed reference price and percentage (show the formula) | Matches CJEU C-330/23 and TR Art 14 |
| 4 | Channel list where the promotion runs (site, app, marketplaces, feeds) | TR compares within the channel; feeds must match |
| 5 | Conditional terms (minimum basket, member only, code) | TR conditional campaigns and EU transparency |
| 6 | Stock available at the promoted price | Bait advertising (UCPD Annex I no.5) |
| 7 | Feed export showing sale_price and promotion dates | Merchant Center consistency |
| 8 | Screenshot of the live price display incl. fees | Drip pricing and total price rules |

Reference price formula:

```
reference_price = min(price_t for t in [start_date-lookback_days, start_date))  # per channel and SKU
discount_pct = round((reference_price-promo_price) / reference_price * 100)    # never round up past the true value
lookback_days = 30 (EU), 10 (TR from 2026-08-01); UK and US: the genuine prior selling price for a meaningful period
```

## 11. Sale event timeline (EU and TR)

| When | Action | Owner |
|------|--------|-------|
| T minus 45 days | Confirm promotion list and markets | offer-strategy |
| T minus 30 days (EU) | Freeze list prices; any increase now raises the 30 day low problem | offer-strategy |
| T minus 10 days (TR) | Freeze prices per channel | offer-strategy |
| T minus 7 days | Compliance review of ads, pages, emails, feed promotions with price evidence | compliance |
| T minus 2 days | Timers and stock badges tested on staging | site-engineer, cro |
| T | Live spot check of five SKUs per channel | compliance |
| T plus 7 days | Archive evidence with the review log | compliance |
