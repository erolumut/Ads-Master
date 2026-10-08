# Bidding and Budgets

> Scope: bid strategy selection, thresholds, setting and moving targets, portfolios and cross-account portfolios, seasonality adjustments, bid adjustments, budgets, pacing and forecasting.

## 1. Bid strategies available (as known 2026-10)

| Strategy | Optimizes for | Optional target | Use when |
|----------|--------------|-----------------|----------|
| Manual CPC | Your keyword bids | None | Very low volume, brand, tight control |
| Enhanced CPC | Manual bids adjusted by conversion likelihood | None | Low volume with some conversion data |
| Maximize clicks | Clicks within budget | Max CPC cap | New account without conversion history |
| Maximize conversions | Conversions within budget | Target CPA | 15 to 30+ conversions in 30 days |
| Maximize conversion value | Value within budget | Target ROAS | Ecommerce or value based lead gen with 30+ conversions in 30 days |
| Target impression share | Impression share at a position | Max CPC cap | Brand defense |
| Portfolio bid strategies | Any automated strategy across campaigns | Shared target | Pool signal across low volume campaigns |
| Cross-account portfolios | Portfolio across accounts in one manager account | Shared target | Multi account advertisers (since 2026-05) [Official, 2026-05] |

Reports in 2026 suggested Microsoft removed or changed the Max CPC option for some new campaigns [Unverified]. Check the bid strategy panel before writing a plan that depends on manual bids.

## 2. Strategy selection tree

```
Is UET recording the primary goal with trustworthy values?
  no  -> Manual CPC, Enhanced CPC or Maximize clicks with CPC cap; fix tracking
  yes -> continue
Conversions in the last 30 days for this campaign (or a portfolio you can join)?
  under 15 -> Enhanced CPC or Maximize clicks with cap; or join a portfolio
  15 to 30 -> Maximize conversions without a target for 2 to 4 weeks
  30+      -> Maximize conversions with tCPA, or Maximize conversion value with tROAS if values are reliable
Is this a brand campaign?
  yes -> Target impression share (top of page 90%+) with a CPC cap, or Manual CPC
Are several campaigns each under 30 conversions with the same economics?
  yes -> one portfolio bid strategy with a shared target
```

Thresholds are practitioner guidance [Practitioner consensus]; Microsoft's own minimums vary by strategy and change, so check the help page before stating a hard minimum.

## 3. Setting and moving targets

Initial target:
- tCPA = trailing 30 day Microsoft CPA x 1.1 (gives room to learn), capped at the business max CPA.
- tROAS = trailing 30 day Microsoft ROAS x 0.9, floored at breakeven ROAS (1 / contribution margin).
- If no Microsoft history: start without a target for 2 to 4 weeks, then set from that data.

Moving targets:
| Situation | Move | Wait before next move |
|-----------|------|----------------------|
| CPA under target and IS lost to budget under 10% | Raise budget first, or raise tCPA 10% to gain volume | 7 to 14 days |
| CPA under target and IS lost to budget high | Raise budget 15% to 20% | 7 days |
| CPA 10% to 25% above target | Lower tCPA 10%; check search terms, partners | 14 days |
| CPA over 25% above target for 14 days | Diagnose (tracking, partners, landing page) before touching target | After fix |
| Volume collapsed after a target change | Revert to previous target | Immediate |

Never move a target by more than 15% to 20% at once [Practitioner consensus]. Large moves reset learning and swing spend.

## 4. Seasonality adjustments
- Use seasonality adjustments for short, predictable conversion rate changes (flash sales, promotions of 1 to 7 days), not for normal seasons.
- Supported for individual campaigns, portfolio bid strategies and shared budgets (fully available since 2026-05) [Official, 2026-05].
- Formula: expected CVR change = forecast promo CVR / baseline CVR minus 1. Example: baseline 3.0%, expected 4.5% gives +50%.
- Log each adjustment in the journal with the reason; review the result after the event.

## 5. Data-driven attribution and bidding
Data-driven attribution rolled out to all advertisers by end of 2026-05 [Official, 2026-05]. Before switching the attribution model on goals used for bidding:
1. Record the current model and 30 day conversions.
2. Switch on the primary goal only; expect reported conversions to shift between campaigns (brand often loses credit, upper funnel gains).
3. Hold targets steady for 14 days while bidding relearns.
4. Coordinate with measurement so MEASUREMENT.md records the change.

## 6. Bid adjustments

Available dimensions: device, location, ad schedule, audience, age, gender, LinkedIn company, industry and job function.

Interaction with automated bidding: on fully automated strategies, many bid adjustments are not applied, with device -100% exclusions an exception on several strategies [Unverified]. Verify on the help page for the strategy in use. If adjustments are ignored, use audience targeting, exclusions and separate campaigns instead.

Adjustment formula (manual, Enhanced CPC):
```
adjustment = (segment conversion value per click / campaign conversion value per click) minus 1
for lead gen: adjustment = (campaign CPA / segment CPA) minus 1
cap between -50% and +50% in one step; require 30+ days and spend of at least 2x target CPA in the segment
```
Example: campaign CPA $120, job function "Finance" CPA $80. (120 / 80) minus 1 = +50%. Apply +40% (one step cap leaves margin), review in 30 days.

Stacking: Microsoft multiplies adjustments. Device +20% and audience +30% gives 1.2 x 1.3 = 1.56, a +56% bid. Check the combined effect on high value segments to avoid runaway CPCs.

## 7. Budgets and pacing

| Item | Practice |
|------|----------|
| Daily budget | Microsoft may spend above the daily budget on some days while keeping monthly spend in line [Unverified] for the exact multiplier; pace against the monthly plan, not single days |
| Shared budgets | Use for groups of campaigns with the same goal; supports seasonality adjustments since 2026-05 |
| Budget suggestions | PMax budget suggestions and performance estimates exist for non-feed campaigns [Official, 2025-09]; treat as directional |
| Limited by budget | A status, not an instruction; raise only if marginal CPA is at or below target |

Pacing check (daily, Growth and above):
```
expected spend to date = monthly budget x (days elapsed / days in month)
pacing ratio = actual spend to date / expected spend to date
0.9 to 1.1 fine; under 0.8 underdelivery (check IS lost to rank, disapprovals); over 1.15 overdelivery (check budgets, imports)
```

## 8. Forecasting Microsoft volume from Google

Method A (preferred): Microsoft Keyword Planner and performance estimates on your keyword list, with your bids.

Method B (when only Google data exists):
```
Microsoft clicks estimate = Google clicks on same keywords x Microsoft volume ratio
Microsoft volume ratio: start at 0.10 to 0.20 for desktop heavy B2B and older demographics, 0.05 to 0.12 for mobile heavy consumer categories [Practitioner consensus, Unverified ranges]
Microsoft spend estimate = Microsoft clicks estimate x (Google CPC x Microsoft CPC ratio)
Microsoft CPC ratio: start at 0.6 to 0.9 and replace with your own data after 14 days [Practitioner consensus, Unverified ranges]
Microsoft conversions estimate = Microsoft clicks estimate x Google CVR x CVR parity (start at 1.0)
```
Worked example: Google non-brand 10,000 clicks per month at $4.00 CPC and 4% CVR. Ratio 0.12, CPC ratio 0.75, parity 1.0. Microsoft clicks 1,200, CPC $3.00, spend $3,600, conversions 48, CPA $75 vs Google CPA $100. Present as a range (ratio 0.08 to 0.16) and replace with real data after 30 days.

## 9. Marginal return budget allocation
1. For each campaign, collect weekly spend and conversions for the last 8 to 12 weeks.
2. Fit conversions = a x spend^b (log log regression); b under 1 means diminishing returns.
3. Marginal CPA at current spend = spend / (b x conversions).
4. Shift budget from campaigns with marginal CPA above target to campaigns with marginal CPA below target, in steps of 10% to 20% per week.
5. Hand the curve to growth-orchestrator for cross channel decisions.

## 10. Common bidding mistakes
| Mistake | Fix |
|---------|-----|
| Imported Google tCPA on a fresh Microsoft account | Start without a target, set from Microsoft data |
| Bid adjustments on automated strategies that ignore them | Use targeting, exclusions or separate campaigns |
| Seasonality adjustment for a whole quarter | Only short events; let bidding learn normal seasons |
| Raising budget on campaigns limited by rank | Fix quality, bids or targets first |
| tROAS on revenue when margins vary widely | Use margin based values or split by margin tier |
