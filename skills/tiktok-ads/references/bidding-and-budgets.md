# Bidding, Budgets and the Learning Phase

> Knowledge as of 2026-10. Official numbers below come from TikTok Business Help Center pages (dates in brackets). Several pages were last updated in 2025; confirm in Ads Manager before quoting a minimum or a ratio to a client.

## 1. Hard minimums [Official, About budgets, accessed 2026-10]

| Budget type | Campaign level | Ad group level |
|-------------|---------------|----------------|
| Daily | Must exceed $50 (or local equivalent) | Must exceed $20 |
| Lifetime | Total must exceed the daily minimum x days [Contested: one source cites $500 campaign lifetime minimum] | Minimum = total days (including past days) x minimum daily budget. Example: a 31-day ad group needs at least $620 |

- When an ad group exhausts its budget, delivery pauses until you raise the budget or extend the schedule [Official].
- GMV Max Creative Boost has a $10 per day minimum (or equivalent) [Official, GMV Max help].

## 2. Budget sizing formulas

| Situation | Formula | Source |
|-----------|---------|--------|
| Smart+ Web daily campaign budget | Ideal 30x historical CPA, never below 10x historical CPA | [Official, Smart+ Web best practices] |
| Value-based optimization (VBO) for web | Daily budget = 10x target CPA for Complete Payment | [Official, 2025-02] |
| Cost Cap ad group | Daily budget at least 10x the CPA bid | [Practitioner consensus] |
| Maximum Delivery ad group | Daily budget around 10x the average daily CPA of the past 7 days to pass learning | [Practitioner consensus] |
| Search Ads Campaign | Budget about 20x the bid | [Official, 2026-08] |
| Learning target | Budget needed per ad group = (50 conversions / 7 days) x CPA = about 7.1x CPA per day as the theoretical floor | Derived from the 50 conversions in 7 days benchmark [Practitioner consensus] |

Worked example: target CPA $40. Smart+ Web floor = $400 per day, ideal = $1,200 per day. A Starter account with $2,000 per month ($66 per day) cannot feed a Purchase-optimized Smart+ campaign. Use one manual ad group optimized to Initiate Checkout or Add to Cart for 2 to 4 weeks, then move to Purchase, or accept a long learning period and judge on 14-day windows.

## 3. Bid strategies

| Strategy (UI) | Goal | Availability | Use when | Risk |
|---------------|------|-------------|----------|------|
| Maximum Delivery | Spend the full budget and get as many results as possible, no CPA target | Most objectives | Launch, learning, small budgets, creative tests | CPA volatility in competitive periods (Q4) [Official] |
| Cost Cap | Keep average cost per result close to the target CPA you set | Most conversion objectives | Stable accounts with known CPA, scaling without CPA blowouts | Under-delivery when the cap is below market price |
| Bid Cap | Cap the bid per auction (mainly reach, view, click goals) | Selected objectives [Unverified per account] | Brand and traffic buying with strict unit costs | Sharp delivery drop |
| Minimum ROAS | Maximize purchase value while keeping ROAS at or above the floor; optimizes per transaction, may not spend the full budget | Sales and App Promotion with value-based optimization [Official] | Accounts passing accurate purchase values with stable AOV | Underspend; floor set from inflated 7-day view numbers |
| Highest Value | Spend the full budget while targeting the highest-value purchasers | Sales and App Promotion, value-based [Official] | When you are unsure what Minimum ROAS to set [Official, 2025-02] | Can buy expensive revenue |
| GMV Max Target ROI | Hit a gross revenue / cost target across TikTok Shop | GMV Max only | Always-on TikTok Shop | Target too high starves delivery |
| GMV Max Max Delivery | Spend the full budget and maximize gross revenue | GMV Max (LIVE, or per product in Product GMV Max) | New shops or products for the first 3 to 5 days, sales events [Official] | Days on Max Delivery are not eligible for ROI protection [Official] |

Leaving the bid field empty in manual flows usually defaults the ad group to Maximum Delivery [Unverified, third-party].

### 3.1 Choosing a strategy

```
Fewer than ~25 conversions per week in the ad group?
  -> Maximum Delivery. Do not add caps until volume exists.
Stable CPA for 14+ days and you need to scale without blowing CPA?
  -> Cost Cap at 1.0x to 1.2x the trailing 14-day CPA, budget >= 10x the cap.
Purchase values passed accurately (Events API value + currency, dedup working)?
  -> Value-based: Highest Value first, then Minimum ROAS at or slightly below the
     trailing 7-day actual ROAS for the same market and event [Official, 2025-02].
TikTok Shop?
  -> GMV Max: Max Delivery for 3 to 5 days on new products, then Target ROI.
```

### 3.2 Setting the numbers
- Smart+ targets: set the target CPA or Minimum ROAS from similar campaigns that ran on Maximum Delivery [Official, Smart+ Web best practices].
- Minimum ROAS: base it on the actual ROAS of the past 7 days for the same market and optimization goal; set it relatively low to pass learning faster [Official, 2025-02]. TikTok's 2022 blog suggested 80% of the observed 7-day ROAS as a start point [Official, 2022, older guidance].
- Cost Cap: start at the trailing CPA, not the business target. If the business target is 30% lower than the trailing CPA, step the cap down 10% to 15% at a time.
- GMV Max Target ROI: start at the trailing actual ROI (or breakeven ROI x 1.1 if new) and move in steps the platform allows; see tiktok-shop-and-gmv-max.md.

## 4. Changing bids and budgets

| Change | Rule | Source |
|--------|------|--------|
| Any edit in first 7 days | Edits to bid, audience or creative in the first 7 days may impact learning; let campaigns run 7 days without significant edits | [Official, Smart+ Web best practices] |
| Bid edits after day 7 | Up to 15% every 2 days while monitoring | [Official, Smart+ Web best practices] |
| Budget increases (Smart+ Lead Generation) | No more than 50% per day | [Official, Smart+ Lead Generation best practices] |
| Budget increases (manual ad groups) | 20% to 30% every 48 to 72 hours on stable ad groups; duplicate instead for jumps above 50% | [Practitioner consensus] |
| Budget cuts | Cuts do not reset learning the way large increases can, but cuts above 50% often cause a delivery stall; prefer pausing weak ad groups | [Practitioner consensus] |
| GMV Max Target ROI edits | Edits beyond stated limits and pausing make that day ineligible for ROI protection | [Official, 2026-02] |

Underspending with view-through on: TikTok suggests toggling off view-through tracking, which may increase delivery [Official, Smart+ Web best practices].

## 5. Campaign Budget Optimization (CBO) vs ad group budgets (ABO)

| Use CBO when | Use ABO when |
|--------------|-------------|
| Ad groups are interchangeable (same event, same geo, same margin) | You need guaranteed spend per test cell, market or product |
| Scaling winners | Creative or audience testing where each cell must get spend |
| Smart+ automatic budget | Lead gen per region with fixed sales capacity |

Under CBO, one ad group often takes most of the spend. That is expected. Judge the campaign, not each ad group, unless an ad group is starved for 7+ days with better CPA, then move it to its own campaign.

## 6. Dayparting and schedule
- Dayparting is set in the ad group schedule ("Dayparting", select hours by day of week in the account time zone). Availability can differ in Smart+ and CBO flows [Unverified].
- Use dayparting when: lead gen with call center hours (calls within 5 minutes convert better), local services, LIVE GMV Max windows aligned with live sessions, regulated categories with time restrictions.
- Avoid dayparting when: ecommerce with fewer than 100 conversions per week per ad group. It cuts signal and the algorithm already shifts delivery by hour.
- Test design: 2 identical ad groups, one dayparted, for 14 days, compare CPA on backend data.

## 7. Delivery type and pacing
- Standard delivery spreads budget through the day; Accelerated (where available) spends as fast as possible. Use Accelerated only for short events such as drops or limited LIVE windows [Unverified availability per objective].
- Lifetime budgets suit fixed-date campaigns (launches, sales). Daily budgets suit always-on.

## 8. The learning phase

| Fact | Detail | Label |
|------|--------|-------|
| Scope | Learning runs per ad group, not per campaign | [Practitioner consensus] |
| Exit benchmark | TikTok's Learning Phase FAQ: "achieving 50 conversions is the most significant indicator of passing the learning phase"; practitioners frame it as about 50 per ad group within about 7 days | [Official, Help Center Learning Phase FAQ; 7-day framing Practitioner consensus] |
| Alternative threshold | One third-party guide cites 25 conversions; the same page calls 50 the full mark, and no TikTok page supports 25 | [Unverified, likely wrong]; plan on 50 |
| Risk signal | TikTok's Campaign Creation FAQ: an ad group that struggles to reach at least 20 conversions in the first 10 days has a high chance of not passing learning; do not edit before about 20 conversions | [Official, Help Center] |
| Duration by type | Search Ads learning about 5 days; value-based optimization for app at least 7 days | [Official, Help Center pages for those campaign types] |
| Fixes TikTok names | Broaden targeting, raise the bid, refresh creative; or optimize to an upper-funnel event (add to cart, product page view) during learning | [Official, Learning Phase FAQ and Campaign Creation FAQ] |
| Status | Visible in the delivery or status column of Ads Manager | [Practitioner consensus] |
| Resets | Significant edits to bid, audience, optimization event or creative in the first 7 days | [Official, Smart+ Web best practices] |

Learning phase triage:
1. Count conversions per ad group per 7 days. If under 25, consolidate ad groups or move the optimization event up the funnel.
2. Check budget vs CPA. If daily budget is under 10x CPA, raise budget or consolidate.
3. Check creative count. Fewer than 3 active creatives per manual ad group (or fewer than 6 in Smart+) limits exploration.
4. Check caps. Cost Cap or Minimum ROAS set tighter than the trailing actual will hold the ad group in learning.
5. Do not judge CPA during learning on fewer than 3 days of data; use the 7-day window.

## 9. Unit economics to targets

| Metric | Formula |
|--------|---------|
| Contribution margin per order (CM) | AOV x (gross margin %) minus shipping, payment fees, pick and pack, expected returns cost |
| Breakeven CPA | CM per order (first order) or CM x expected repeat factor (if payback window allows) |
| Breakeven ROAS | 1 / contribution margin % |
| Target CPA | Breakeven CPA x (1 minus required profit share) |
| Platform target vs true target | Platform CPA target = true target x calibration factor (platform conversions / incremental conversions from lift test or triangulation) |

Worked example: AOV $80, contribution margin 40% ($32). Breakeven ROAS = 2.5. If the business wants 25% of CM as profit on first order, target CPA = $24, target ROAS = 3.33. If a lift test shows TikTok's 7-day click + 1-day view reporting overstates incremental purchases by 1.4x, the in-platform target ROAS becomes 3.33 x 1.4 = 4.66 for 7-day click + 1-day view reporting. Write both numbers in the plan.

TikTok Shop variant: breakeven ROI = 1 / (margin after referral fee, affiliate commission, shipping subsidy, coupons and returns). GMV Max Pro was announced to factor affiliate costs, coupons and platform fees into optimization [Official, 2026-05; limited rollout].

## 10. Seasonal planning
- Expect CPM and CPA pressure in Q4 (Black Friday to Christmas) and around TikTok Shop mega sales. Maximum Delivery shows more cost volatility in high-competition periods [Official].
- 3 weeks before peak: lock creative inventory (2x normal), raise budgets in steps, switch fragile Cost Caps to Maximum Delivery or loosen caps 15% to 20%, pre-build Search Ads for promo terms.
- After peak: cut budgets in 2 or 3 steps, reset caps to post-peak trailing CPA, refresh creative before January.

## 11. Bid and budget change list template

```
| # | Level | Entity (name / ID) | Setting | Current | Proposed | Why (data, date range) | Expected impact | Risk | Rollback |
|---|-------|--------------------|---------|---------|----------|------------------------|-----------------|------|----------|
| 1 | Ad group | US_SALES_MANUAL_TEST / 1789... | Daily budget | $200 | $260 (+30%) | CPA $31 vs $40 target, 7d, 62 conv | +15 to 20 conv/wk | CPA drift | Revert after 72h if CPA > $44 |
```

Every row needs human approval before it is applied. Log approved changes in the journal with the time of change so later analysis can separate effects.
