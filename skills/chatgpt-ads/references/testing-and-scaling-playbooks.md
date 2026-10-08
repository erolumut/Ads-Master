# Testing and Scaling Playbooks

> Knowledge as of 2026-10. ChatGPT Ads has no published cross advertiser benchmarks (OpenAI, 2026-09) and few controlled public results. Every play below assumes you build your own baseline. Thresholds are practitioner defaults, not platform rules; adjust them to the project's unit economics in PROJECT_BRIEF.md.

## 0. Principles for testing a new channel
1. Decide the decision before spending: write hypothesis, primary metric, decision threshold, kill rule and scale rule in EXPERIMENTS.md first.
2. Separate learning tests (can you get delivery, clicks, sessions, any conversions) from decision tests (is CPA or ROAS acceptable and incremental).
3. Use backend verified click-through conversions as the primary metric; platform view-through and modeled conversions are secondary.
4. Run in whole budget weeks (Sunday to Saturday, account time zone) because daily budgets average over 7 days.
5. Change one lever per ad group per week.
6. Plan incrementality before scale, not after.

## 1. Test budget sizing by tier

| Tier | Recommended stance | Test budget | Duration | Design |
|------|--------------------|-------------|----------|--------|
| Starter (under $3k per month) | Usually wait; organic AI visibility first | If tested: $25 to $50 per day (currency minimum) | 4 weeks | Learning test, Clicks, 1 campaign, 2 to 4 ad groups |
| Growth ($3k to $30k) | Test if eligibility and fit score 3+ of 5 | 5% to 10% of paid budget, at least enough for 1,000 clicks | 4 to 6 weeks | Decision test on CPA, hint style test, pre/post plus geo read if possible |
| Scale ($30k to $300k) | Test in every eligible core market | 3% to 8% of paid budget | 6 to 8 weeks then ongoing | Decision test plus geo holdout or partner lift before passing 10% of paid |
| Enterprise (over $300k) | Managed or partner path plus self-serve for agility | Ring fenced innovation budget | Quarterly cycles | Geo lift with a partner, brand lift where awareness matters, multi market sequencing |

Sizing formulas (see bidding module): clicks needed = decision conversions / expected CVR; budget = clicks x CPC. If the budget cannot buy at least 30 click-through conversions at a plausible CVR, label the test a learning test.

Planning assumptions when you have no data (label them as assumptions in plans): CPC $3 to $5 US (OpenAI guidance); CTR 0.5% to 1.3% (panels); post-click CVR 30% to 60% of the account's Google non-brand CVR (early practitioner reports of lower intent on free tier traffic) [Unverified]. Replace with own data after 2 weeks.

## 2. Play: Fit and eligibility assessment (before any spend)
1. Run the eligibility gate (account setup module). Any fail is a no go.
2. Score fit 0 to 5 on each:
   - Intent fit: do people ask ChatGPT about this category before buying? Evidence: chatgpt.com referral traffic in GA4, prompt research from ai-search-optimization, customer survey.
   - Offer clarity: can the value be stated in 24 characters plus 48 characters with a price or proof?
   - Landing continuity: specific pages exist for each intent.
   - Measurement readiness: standard events, server events, consent.
   - Budget sufficiency: can the budget reach a decision?
3. Total 18+ of 25: go. 12 to 17: learning test only. Under 12: no go, revisit in a quarter.
4. Output a fit and eligibility memo with sources and dates.

## 3. Play: Launch (learning to decision test)
Week 0 (preparation):
1. Measurement live and verified (measurement QA checklist).
2. Build 1 campaign per market, Clicks objective, Manual: Max bid at guidance (US $3 to $5 or local equivalent), daily budget.
3. 3 to 6 ad groups: top intents; or the hint style head to head (P, S, C, K) on the top intent.
4. 3 to 5 ads per ad group, distinct angles.
5. Everything paused; change list to human; approval; activation.

Days 1 to 3:
- Confirm Serving status and first impressions within 24 hours. If none after 24 hours, run the delivery diagnostic (bidding module section 6).
- Confirm pixel and CAPI events arriving; GA4 sessions with paid UTMs; session rate.

Week 1 to 2:
- Delivery rate target 70%+ of budget. If under 50%, raise bids 20% or broaden hints.
- Hint style comparison after 100 clicks per ad group: keep the style with the best CTR x post-click CVR product.
- Pause ads with CTR under 50% of the ad group average after 1,000 impressions each.

Week 3 to 4 (or 6):
- Decision read: click-through CPA and backend verified CPA vs target, session rate, new customer share.
- Apply kill and scale rules (section 9).

## 4. Play: Hint style test
- Hypothesis: "If we write context hints as <style>, then CTR and post-click CVR improve vs <control style>, because the system matches more relevant conversations."
- Design: same campaign, same ads, one ad group per style, equal fixed bids, `utm_content` per group.
- Metric: clicks x post-click CVR per 1,000 impressions (relevant clicks), secondary CTR and CPC.
- Duration: at least 7 days and 100 clicks per group; extend to 14 days if under.
- Note: delivery volume per group is itself a result (the system decides relevance). A style that gets no impressions at the same bid is losing.
- Log result in EXPERIMENTS.md; confirm twice before writing to memory.

## 5. Play: Move to Conversions (oCPC)
Trigger: one standard event with 30+ click-through conversions in the last 30 days from ChatGPT Ads, stable tracking for 14 days.
1. Clone the best Clicks campaign structure into a new campaign: objective Conversions, click billing, event `order_created` (or the main standard event).
2. Strategy: Maximize results with daily budget equal to the Clicks campaign's average daily spend; or Bid Cap at 1.0x to 1.2x target CPA.
3. Reduce the Clicks campaign to 30% to 50% of budget; run both 2 to 3 weeks.
4. Compare click-through CPA and backend CPA; keep the winner; pause (not archive) the loser.
5. Do not judge oCPC in the first 7 days.
oCPM (impression billing) is for eligible advertisers; use only when view-through conversions are measured and you accept impression billing risk.

## 6. Play: Product feed campaign (ecommerce)
1. Feed via hosted URL or SFTP refreshed daily (items expire after 2 weeks); `is_ads_eligible` set; prices current.
2. Labels in `ads_metadata` for margin band and bidding tier.
3. Campaign type Product feed, country level geo, Clicks with Maximize results or fixed bid; ad groups: hero, core margin, long tail.
4. Template using `{{product.title}}` and `{{product.price}}`.
5. Weekly: product level Insights (`segments[]=product`), zero impression products (`includes[]=zero_impression_products`), carousel card metrics.
6. Move to oCPC on `order_created` once 30+ purchases per 30 days.
7. Hand feed quality issues to commerce-feeds.

## 7. Play: Incrementality measurement

Choose the design by budget and geography:

| Design | When | How | Caveats |
|--------|------|-----|---------|
| Geo holdout (US) | Scale tier, national business, enough conversions per geo | Randomly assign matched DMAs or states to test (ads on) and control (excluded via `excluded_locations`) for 4 weeks plus 1 week cool down; compare backend conversions per capita vs pre period (difference in differences or synthetic control) | Needs the channel to drive a detectable share; if ChatGPT click-through conversions are under 5% of total conversions in test geos, detection is unlikely |
| Partner geo lift | Scale and Enterprise | Haus, Measured or WorkMagic geo incrementality (early stage per OpenAI, October 2026) | Vendor method; ask for pre-registered design and power analysis |
| Time switchback | Growth tier, single geo | Alternate on and off weeks for 6 to 8 weeks | Ads serve up to 24 hours after pause; 30-day click window spills over; seasonality noise; weakest design |
| Pre/post with control channel | Starter and Growth | Compare total conversions and branded search before and after launch vs a stable control metric | Directional only |
| Customer level holdout via audiences | Not reliable today | Exclusion audiences can hold out known customers, but inclusion needs 25,000 matched and EEA cannot use audiences | Use only for existing customer suppression |

Power check before running a geo holdout:
```
expected incremental conversions per week in test geos = ChatGPT click-through conversions per week x assumed incrementality (0.5 planning assumption)
baseline weekly conversions in test geos = B, weekly standard deviation = s
detectable if expected incremental conversions x weeks > 2 x s x sqrt(weeks) (rough two sigma rule)
```
If not detectable, extend duration, increase test spend, or use a partner lift study.

Reading results:
- iCPA = test spend / incremental conversions.
- Incrementality factor = incremental conversions / platform click-through conversions.
- Apply the factor to future platform CPA when reporting to growth-orchestrator; store it in MEASUREMENT.md "Incrementality evidence" with date and confidence.

Public evidence to calibrate expectations (all vendor reported): WorkMagic geo lift for one advertiser estimated 2.3x more incremental orders than last click captured; DV Rockerbox reported one advertiser's attributed CPA 15.3% below its blended paid search benchmark [Official, 2026-10] (OpenAI cited partner results, read via secondary summary). Treat as possibility, not prediction.

## 8. Play: Scale
Preconditions: click-through CPA at or below target for 2 consecutive weeks, backend reconciliation within 20%, session rate 70%+, no open policy issues.
1. Increase budgets 20% to 30% per week per campaign.
2. Add intents: new ad groups from prompt research and search term mining.
3. Add product feed and carousels if not live.
4. Add platforms (app vs web split) when segment data shows CPA gaps.
5. Add markets only after home market proof; new self-serve accounts may be limited to the home country until verification and home country spend.
6. At 10% of paid budget or $30k per month: incrementality read required before further increases.
7. At Enterprise scale: consider managed sales for invoice terms and account spend limits, and partner measurement.

## 9. Kill and scale rules (defaults; tune to unit economics)

| Rule | Trigger | Action |
|------|---------|--------|
| Kill: no conversions | Spend reaches 3x target CPA with zero click-through conversions and tracking verified | Pause campaign, post-mortem, journal |
| Kill: CPA | Click-through CPA above 2x target after 30+ conversions or after the planned decision budget | Pause or cut to learning budget |
| Kill: incrementality | iCPA above 2x target from a valid test | Pause or cap at retargeting style budget |
| Kill: session loss | Session rate under 40% after fixes | Pause until landing and tracking fixed |
| Hold | CPA between 1.0x and 2.0x target | Optimize hints, creative, landing; re-read in 2 weeks |
| Scale | CPA at or below target for 2 weeks and session rate 70%+ | +20% to 30% budget per week |
| Scale with care | CPA at target but new customer share under 30% | Check overlap with retention and brand traffic before scaling |
| Learning test end | Learning budget spent | Decide whether a decision test is justified; never scale on learning data |

## 10. Play: Recover

| Situation | Steps |
|-----------|-------|
| Delivery collapsed | Check serving issues, billing, brand review, weekly budget allowance, recent bid cuts; restore last working bid; check whether a policy or availability change happened (Freshness Protocol) |
| Tracking broke (conversions dropped to zero) | Recent events endpoint; pixel load; consent changes; CAPI key revoked; event setting detached; oppref stripped by a new redirect. Pause oCPC campaigns if broken more than 48 hours to protect learning |
| Mass ad rejections | Crawler access (WAF, robots), landing page change, policy version change; fix and resubmit in small batches |
| Account suspended | Do not create new accounts to circumvent; gather evidence; contact ads-support@openai.com; review advertiser policy |
| CPA spike | Check landing page, price changes, stock, competitor offers, seasonality, new placements (visual ads, carousels); compare by platform and ad group |
| Budget overspend surprise | Explain 2x daily and 7x weekly rules; switch to campaign total budgets for strict caps |

## 11. Play: Plateau
- Expand hint coverage with new situations (When angle) and new customer needs (Who angle).
- Add 2 new creative angles per ad group per month.
- Test AI text customization (opt-in) as an A/B.
- Test platform splits and sub-national geos.
- Add product feed or carousels; test Views (CPM) for launches with brand lift.
- Re-check eligibility for newly opened markets.

## 12. Weekly optimization routine (30 to 60 minutes)
1. Pull last 7 days and prior 7 days by campaign and ad group (Ads Manager CSV or Insights API).
2. Check delivery rate, CTR, CPC, post-click CVR, click-through CPA, spend vs plan.
3. Check serving issues and review status.
4. Check session rate (GA4 sessions / clicks) and backend conversions.
5. Decide max 3 changes; draft change list; get approval.
6. Update EXPERIMENTS.md rows; write the weekly journal entry.

## 13. EXPERIMENTS.md row templates
| ID | Date | Agent | Hypothesis | Primary metric | ICE | Design | Stop rule | Status |
|----|------|-------|-----------|----------------|-----|--------|-----------|--------|
| E0xx | YYYY-MM-DD | chatgpt-ads | If we launch ChatGPT Ads Clicks on top 3 intents, then we acquire customers at or below $X CPA, because buyers research the category in ChatGPT before purchase | Backend verified click-through CPA | 6/4/7 | Learning then decision test, 4 to 6 weeks, pre/post with control metric | Kill at 3x CPA with zero conversions or 2x CPA after 30 conversions | backlog |
| E0xx | YYYY-MM-DD | chatgpt-ads | If we write hints as situations instead of product descriptions, then relevant clicks per 1,000 impressions rise 20%, because matching keys on user needs | Clicks x CVR per 1,000 impressions | 5/5/9 | A/B by ad group, same ads and bids | 14 days or 100 clicks per group | backlog |
| E0xx | YYYY-MM-DD | chatgpt-ads | If we hold out 20% of DMAs, we can measure ChatGPT Ads iCPA within +/- 30% | iCPA | 7/5/4 | Geo holdout 4 weeks plus 1 cool down | Pre-registered end date | backlog |
