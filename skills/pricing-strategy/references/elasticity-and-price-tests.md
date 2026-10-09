# Elasticity Estimation and Price Tests

> Owns: estimating price elasticity from data, choosing a lawful price test design, sizing it, reading results in contribution terms. Hands to `offer-strategy`: offer and promo tests, see [Offer testing and measurement](../../offer-strategy/references/offer-testing-and-measurement.md). Hands to `cro`: on-page experiment tooling and statistics. Hands to `measurement`: geo test infrastructure and data quality. Hands to `compliance`: legal review of any test that shows different prices to different people.

## 1. Elasticity basics

```
Own price elasticity e = %change in quantity / %change in price   (usually negative)
Arc elasticity between (P1, Q1) and (P2, Q2): e = ((Q2 - Q1) / ((Q1 + Q2) / 2)) / ((P2 - P1) / ((P1 + P2) / 2))
Log-log regression: ln(Q) = a + e ln(P) + controls (season, promo, distribution, ads, competitor price)
Contribution optimal price with constant elasticity e (|e| > 1) and unit cost c: P* = c x e / (1 + e)
```

Reference point: a meta-analysis of 1,851 price elasticities found a mean of about -2.6 for brand level sales (Bijmolt, van Heerde and Pieters, 2005) [Study, prior knowledge]. Promotional (temporary) elasticities are much larger than regular price elasticities; never use promo lift to estimate the effect of a permanent change.

The constant elasticity formula P* is a sanity check, not a recommendation: it assumes a stable curve and ignores reference prices, competitor reactions and channel effects.

## 2. Estimating from historical data

Data needs: weekly units and prices per SKU and channel for 52+ weeks, promo flags and depth, distribution (number of stores, stock outs), marketing spend, competitor prices if available, seasonality markers.

Procedure:
1. Clean: remove stock out weeks, separate regular and promo weeks.
2. Fit log-log regression for regular price variation only (if any exists). Often there is too little regular price variation: then elasticity cannot be estimated from history. Say so.
3. Promo elasticity: fit separately with promo depth; report as promo response, not elasticity.
4. Cross price effects: include competitor price and own other pack prices to see cannibalization within the ladder.
5. Validate: out of sample weeks; sign and size plausibility (elasticity between -0.5 and -5 for most consumer goods).

Minimal stdlib sketch for log-log OLS (paste into a scratch script; inputs from `ads-master/data/imports/`):

```python
import csv, math
rows = [r for r in csv.DictReader(open("weekly_sku.csv")) if r["promo"] == "0" and float(r["units"]) > 0]
x = [math.log(float(r["price"])) for r in rows]
y = [math.log(float(r["units"])) for r in rows]
n = len(x); mx = sum(x) / n; my = sum(y) / n
sxx = sum((a - mx) ** 2 for a in x); sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
e = sxy / sxx
print(f"n={n} elasticity={e:.2f}  (no controls; use only as a first read)")
```

## 3. Test designs (from safest to riskiest)

| Design | How | Legal and trust risk | Traffic need | Best for |
|--------|-----|----------------------|--------------|----------|
| New SKU or pack test | Launch a new pack at the test price; compare with the existing ladder | Low | Low to medium | Ladder and per unit curve |
| Time based (pre and post, switchback) | Change the price for everyone; alternate periods or compare with a baseline and control SKUs | Low (same price for everyone at a time); watch prior price rules if price later falls | Low | Low traffic stores |
| Geo split | Different prices by market or region where markets are separate (countries, Turkish regions for local businesses) | Low to medium; same price within a market | Medium; 10+ comparable regions or two countries | Marketplace and multi-country stores |
| Channel split | Price differs by channel (DTC vs marketplace) | Low | Medium | Channel corridor |
| Discount based split | Same list price; one group gets a code or automatic discount | Medium (offer test, run with `offer-strategy`) | Medium to high | Testing lower effective prices |
| Visitor level list price A/B | Different visitors see different list prices at the same time | High: trust, feed mismatch (Merchant Center disapprovals), personalized pricing disclosure rules, reputational (Instacart ended item price tests in 2025 after a study found up to 23% differences for identical items; New York AG letter 2026-01-08) [Official and press] | High | Rarely recommended; only with compliance sign off |
| Survey based (conjoint, Gabor Granger) | No live price change | None | n/a | Before live tests ([Value based pricing](value-based-pricing-and-wtp.md)) |

Default recommendation: new pack tests and time or geo designs. Visitor level list price tests need `compliance` sign off and a plan for feeds and ads.

## 4. Personalized and dynamic pricing rules (2026)

| Jurisdiction | Rule | Status |
|--------------|------|--------|
| EU | Consumer Rights Directive (as amended by the Omnibus Directive 2019/2161): traders must inform consumers when a price is personalized on the basis of automated decision making [Official, prior knowledge]. GDPR applies to profiling. Digital Fairness Act proposal planned for late 2026: consultation showed 77% of respondents supporting a general restriction on personalized pricing based on personal data or profiling, with consumer authorities split [Official consultation summary]. Not yet tabled as of 2026-10-09 | In force (disclosure); DFA pending |
| UK | DMCC unfair practices regime (2025-04-06); CMA work on algorithmic pricing | In force |
| US, New York | Algorithmic Pricing Disclosure Act in effect 2025-11-10; One Fair Price Act passed legislature June 2026, awaited signature [via offer-strategy research] | In force / pending |
| US, other states | Maryland (food retailers, 2026-10-01), Connecticut, New Jersey (signed 2026-07-23, most provisions 2027-08-01) surveillance pricing restrictions [via offer-strategy research] | Phasing in |
| Turkey | Consumer law and Ministry of Trade price inspections; unfair price increase enforcement; no specific personalized pricing statute found [Unverified] | Watch |

Dynamic pricing (price changes over time for everyone, based on demand, stock or competitor prices) is generally lawful but must respect prior price rules for discounts, unfair pricing rules in Turkey, and consumer trust. Personalized pricing (different prices for different people based on their data) needs disclosure in the EU and is restricted in several US states. The agent never designs personalized pricing based on personal data without `compliance` sign off.

## 5. Sizing a test

Primary metric: contribution per visitor (or per store week for geo tests), not conversion rate. A higher price can lower conversion and still raise contribution.

```
Contribution per visitor = conversion rate x CM2 per order
Breakeven conversion change for price change i at CM2 margin m:  conversion may fall by up to i / (m + i) (same as allowable volume loss)
```

Rules of thumb:
- For visitor level tests, detecting a 10% relative change in contribution per visitor at typical ecommerce variance needs tens of thousands of visitors per arm; low traffic sites should use time or pack based designs [Practitioner consensus; compute with the `cro` sample size method].
- Switchback: at least 6 to 8 alternating periods of one week, balanced across weekdays and pay cycles; exclude event weeks.
- Geo: match regions on pre-period sales; use synthetic control or difference in differences (`measurement`).
- Run at least two full weekly cycles; read 90 day cohort contribution for subscription and replenishment products.

## 6. Reading results

| Read | Decision |
|------|----------|
| Contribution per visitor up, conversion down less than allowable | Keep the higher price |
| Contribution flat, conversion down | Not worth the risk; keep old price or test architecture instead |
| Contribution down | Revert |
| Mixed by segment or channel | Consider fences (pack, channel), not personalized prices |

Write the readout with the effect size, interval, sample, dates, guardrails, and what changes in the report. Append the result to EXPERIMENTS.md; update `memory/pricing-strategy.md` only when confirmed.

## 7. Test plan template

```markdown
## Price test plan: <id>
Question: <what price decision this informs>
Design: <pack | switchback | geo | channel | discount split | visitor A/B (needs compliance sign off)>
Arms: <prices incl VAT per arm>; per unit prices; reference price implications
Primary metric: contribution per visitor (CM2); secondary: conversion, AOV, units per order
Guardrails: return rate, complaints, retail sell-out, feed disapprovals
Duration and sample: <weeks, visitors or regions>; minimum detectable effect
Legal: compliance review <date>; prior price rule check; disclosure needs
Feeds and ads: commerce-feeds plan for price consistency
Stop rules: <conditions>
Decision rule: <what result leads to which price>
Owner, approver, EXPERIMENTS.md id
```

## 8. Common mistakes

1. Using promo lift as elasticity.
2. Visitor level list price tests that put two prices for one product in feeds and ads.
3. Judging a price test on conversion rate.
4. Too short tests that end in a pay week or holiday.
5. Ignoring cannibalization between ladder rungs.
6. Running a price test on a SKU that is also on a retail promotion.

## 9. Elasticity by situation (directional, own data first)

| Situation | Expect elasticity to be | Why |
|-----------|-------------------------|-----|
| Strong brand, habitual purchase, low share of wallet | Lower (closer to -1) | Low attention to price |
| Commodity like product, many substitutes on the same shelf | Higher (-2 to -4) | Easy comparison |
| Marketplace listing with buy box competition | Very high around competitor price | Algorithmic placement |
| Subscription renewals | Low per cycle, but churn spikes after visible increases | Inertia then trigger |
| B2B with contracts | Low short term, high at renewal | Lock-in |
