# Bidding and Budgets

> Knowledge as of 2026-10. Sources: OpenAI Help Center (Ads in ChatGPT: The Basics 20001207, Create Campaigns 20001210, Daily Budgets 20001413, Budget Pacing 20001515, Maximize Results 20001425, Conversion-optimized Campaigns 20001412, Billing 20001216, FAQ 20001220), developer docs (Bidding and Budgets), trade press for history. Re-verify live.

## 1. Objectives, billing and strategies

| Objective (UI) | API `bidding_type` | Billing | Bid strategies | Max bid meaning | Label |
|----------------|-------------------|---------|----------------|-----------------|-------|
| Views | `impressions` | Per 1,000 impressions (CPM) | Fixed bid only | Max CPM (API: per impression in micros, $60 CPM = `60000`) | [Official, 2026-09] |
| Clicks | `clicks` | Per valid click (CPC) | Manual: Max bid (`fixed_bid`) or Maximize results (`maximize_clicks`) | Max CPC | [Official, 2026-09] |
| Conversions, click billing (oCPC) | `conversions` | Per valid click | Fixed bid as Bid Cap or Maximize results (`maximize_conversions`) | Bid Cap: the most you will bid for a conversion; actual cost set by auction | [Official, 2026-09] |
| Conversions, impression billing (oCPM) | `conversions` | Per impression | For eligible advertisers | Same | [Official, 2026-09] |

Key facts:
- Relevance weighted second price auction: the highest bid does not automatically win, and you pay based on the next competing bid adjusted for relevance [Official, 2026-09].
- Recommended starting CPC max bid: $3 to $5 USD [Official, 2026-09]. Ads Manager warns below $3 in the US [Unverified]. The API does not enforce a minimum bid [Unverified].
- Default max CPM bid reported at $60 [Unverified].
- Conversion campaigns: "There is no recommended bid amount at this time" [Official, 2026-09]. You never pay per conversion [Official, 2026-09].
- Conversion campaigns need conversion tracking and one standard event (custom events not supported); objective, billing model and event cannot change [Official, 2026-09].
- oCPM learns from a broader set of signals (after clicks and after views) [Official, 2026-09].
- Maximize results: preselected for eligible new ad groups; adjusts bids automatically for the most results within budget; does not guarantee CPA, CPC or ROAS; no hard bid limits; requires a daily budget [Official, 2026-09].
- Audience bid multipliers work only with fixed bid; switching to Maximize results requires clearing them [Official, 2026-09].
- OpenAI says CPC and outcome optimized bidding now account for the majority of campaigns (2026-08-31) [Official, 2026-08].

### Pricing history (context, not targets)
| Period | Reported pricing | Label |
|--------|-----------------|-------|
| Feb 2026 pilot | About $60 CPM, $200k to $250k minimum commitment, CPM only | [Unverified] |
| Mid April 2026 | CPMs reported $25 to $45, lows of $15; minimum reduced to $50k | [Unverified] |
| May 5, 2026 | CPC added; self-serve with no platform minimum spend beyond minimum daily budgets | [Official, 2026-05] and [Unverified] (minimum removal) |
| Practitioner reports | US CPC around $3 to $4 (one advertiser $3.37); about EUR 1 per click delivered in Czech and Slovak markets | [Unverified] |

## 2. Objective decision tree

1. Measurement live with a standard event? No: Clicks with fixed bid, attach the event for reporting. Yes: continue.
2. 30+ click-through conversions per 30 days on that event (or forecast at planned spend)? Yes: Conversions (oCPC). No: Clicks.
3. Is the goal reach with a brand lift partner (Kantar, Cint reported early stage [Unverified])? Views (CPM).
4. Need strict cost control per click? Manual: Max bid. Need volume and unknown market price? Maximize results with a daily budget.
5. Product feed? Feed campaigns support impressions, clicks and conversions; Maximize results availability depends on account and configuration [Official, 2026-09].

## 3. Setting bids

### Fixed CPC (Manual: Max bid)
Starting bid = min(OpenAI guidance, economic ceiling):
- US guidance: $3 to $5.
- Economic ceiling: max CPC = target CPA x expected post-click CVR. Example: target CPA $60, expected CVR 2% gives $1.20. If the ceiling is far below $3, expect thin US delivery; either accept low volume, use Maximize results with a small daily budget to discover price, or do not launch.
- Non-US markets: start below the US figure (for example 40% to 70% of it, converted to local currency), check impressions after 48 hours, raise in 20% steps only if delivery is thin [Practitioner consensus].

### Bid Cap for oCPC
Start at 1.0x to 1.2x target CPA if cost control matters; otherwise Maximize results [Practitioner consensus]. Bid Cap is used in click auctions, not the price per conversion [Official, 2026-09].

### Micros
API money fields are integer micros: 1,000,000 micros = 1 unit of account currency. $2.50 = `2500000`. A $60 CPM = `60000` per impression. Insights metrics (spend, cpc, cpm) are in major units, not micros [Official, 2026-09].

### The `bid_too_low` flag
Guidance only, not a serving restriction. It is not raised for inactive ad groups or within 24 hours of an ad group update, so its absence does not prove a bid is competitive [Official, 2026-09]. In cheaper markets it may stay on while delivery is fine; check impressions first [Unverified].

## 4. Budgets

| Type | Behavior | When to use | Label |
|------|----------|-------------|-------|
| Daily budget | A 7-day average. Daily spend can reach 2x the daily budget; spend over the 7-day budget week (Sunday to Saturday, account time zone) cannot exceed 7x. Unused budget can carry within the same week | Default for new advertisers and required for Maximize results | [Official, 2026-09] |
| Campaign total budget | Max spend across the full campaign, paced over the schedule; the stricter control | Fixed flights, launches, strict caps | [Official, 2026-09] |

Rules:
- Campaign total can switch to daily (irreversible); daily cannot switch to campaign total (new campaign) [Official, 2026-09].
- A campaign can stop delivering when its weekly allowance is used even while marked active [Official, 2026-09].
- Mid day increase: that day's cap uses the highest daily budget active that day (raising $100 to $110 allows up to $220 that day) [Official, 2026-09].
- Mid week change: the 7-day limit is prorated from the change through the next Sunday midnight [Official, 2026-09].
- Fixed bid plus daily budget: the daily budget must be at least the highest effective per event bid across non-archived ad groups, including audience bid adjustments [Official, 2026-09].
- A campaign total budget cannot be set below the amount already spent; setting it equal to spent stops delivery [Official, 2026-09].
- Budget updates set a new amount, they do not add [Official, 2026-09].
- Ads may serve up to 24 hours after a pause; that spend is billable [Official, 2026-09].

### Minimum daily budgets by billing currency [Official, 2026-09]
| Currency | Minimum | Currency | Minimum | Currency | Minimum |
|----------|---------|----------|---------|----------|---------|
| USD | 25 | GBP | 15 | EUR | 15 |
| AUD | 25 | CAD | 25 | NZD | 25 |
| CHF | 20 | DKK | 110 | NOK | 160 |
| SEK | 175 | PLN | 65 | CZK | 350 |
| HUF | 5,500 | RON | 80 | ILS | 60 |
| AED | 65 | SAR | 50 | QAR | 70 |
| INR | 725 | JPY | 2,500 | KRW | 25,000 |
| BRL | 40 | MXN | 150 | | |

### Pacing [Official, 2026-09]
- Pacing spreads spend over time and shifts delivery as opportunities change; it does not guarantee even spend or full budget use.
- Campaign total budgets pace over the remaining schedule: with an end date, up to 365 days; without one, a default 60 day pacing period. OpenAI recommends setting an end date.
- Ahead of pace slows delivery; behind pace lets it catch up.
- Changing total budget or end date recalculates pacing.
- Changing bid strategy does not override total budget pacing; low bids can still cause underspend.
- For conversion optimized campaigns the goal is better conversion outcomes, not full budget use [Official, 2026-09].

### Account level spend limits
Spend limit windows (date ranges capping total account spend) exist only for some accounts, notably postpaid invoice accounts; card billed self-serve accounts cannot use them [Official, 2026-09]. They cap the account, not individual campaigns. Up to 60 future windows, no overlaps [Official, 2026-09].

## 5. Budget sizing formulas

| Purpose | Formula |
|---------|---------|
| Clicks needed for a decision | Decision conversions / expected post-click CVR |
| Decision test budget | Clicks needed x expected CPC |
| Daily budget | Decision test budget / test days, rounded up to at least the currency minimum |
| Max affordable CPC | Target CPA x expected CVR |
| Breakeven CPA | AOV x contribution margin (ecommerce) or deal value x close rate x margin (lead gen) |
| Learning test budget | Enough for 300 to 500 clicks across the planned ad groups (direction on CTR, session rate, CVR) |

Typical decision thresholds [Practitioner consensus]:
- 30 to 50 click-through conversions per arm for CPA decisions.
- 100 clicks and 7 days per ad group for CTR and hint style decisions.
- 2 full budget weeks minimum because budgets average over Sunday to Saturday weeks.

Worked example (lead gen): target cost per qualified lead $200, lead to qualified 40%, so target CPL $80. Expected CPC $4, expected CVR to lead 4%, implied CPL $100. Decision test: 40 leads / 0.04 = 1,000 clicks x $4 = $4,000 over 4 weeks (about $145 per day, above the $25 minimum). Kill if CPL above $160 (2x target) after $3,200 with tracking verified.

## 6. Delivery troubleshooting

Check in order [Official, 2026-09]:
1. Account: active, verification and brand review complete, billing valid, spend limit not exhausted.
2. Campaign: active, within dates, budget available (including weekly allowance), valid targeting.
3. Ad group: active, bidding compatible with objective, eligible products in the product set.
4. Ad: active, approved, landing page accessible.
5. Then bids: `bid_too_low`, fixed bid level vs guidance, currency and micros conversion.
6. Then targeting breadth: geo, platform, included audiences and exclusions together; hints too narrow.
7. Change one setting at a time; compare the same reporting scope and time zone over a suitable interval.
8. Wait at least 24 hours after launch before reporting delivery issues; reporting can lag by up to 7 hours [Official, 2026-09].

An empty `serving_issues` array is not a promise of impressions [Official, 2026-09].

| Signal | Interpretation | Action |
|--------|---------------|--------|
| Spend under 50% of budget for 7 days | Bid or relevance limited | Raise fixed bid 20%, broaden hints, add ads, consider Maximize results |
| Spend at 2x daily on some days | Normal 7-day averaging | None; use campaign total budget for strict caps |
| Spend $0 but impressions present | Spend lag of 7 to 8 hours | Wait |
| Delivery concentrated in one ad group | System predicts relevance there | Accept if CPA is fine; otherwise split budget into separate campaigns |
| Delivery collapsed after bid cut | Bid below market | Restore last working bid |

## 7. Bid and budget change rules (approval required)
- Change bids by 10% to 20% per step, no more than twice per week per ad group.
- Scale budgets by 20% to 30% per week when CPA is at or below target for 2 consecutive weeks.
- Never change objective or event to fix performance; build a new campaign and run both briefly.
- When moving from Clicks to Conversions, clone structure, keep the Clicks campaign at reduced budget for 2 weeks, then decide.
- Record every change in the journal with date, before and after values.
