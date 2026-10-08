# Optimization and Diagnostics

> Knowledge as of 2026-10. How to find what is wrong, fix it in the right order, and run the weekly optimization loop. Every diagnosis states the data source and date range.

## 1. The TikTok performance equation

```
CPA  = CPM / (1,000 x CTR x CVR)
ROAS = (1,000 x CTR x CVR x AOV) / CPM
Spend = f(budget, bid cap tightness, audience size, creative engagement, learning status)
```

Decompose any CPA or ROAS change into CPM, CTR, CVR and AOV before acting. Example: CPA rose 30%. CPM +5%, CTR -20%, CVR -3%. The problem is creative engagement (fatigue), not the landing page or auction.

| Driver moved | Usual cause on TikTok | First fix |
|--------------|----------------------|-----------|
| CPM up | Seasonality, narrow audience, declining creative engagement, competitors in sale events, placement shift | Check creative engagement and placement mix, broaden, refresh creative |
| CTR down | Creative fatigue, weaker hooks, offer stale | New hooks and concepts |
| CVR down | Landing page or listing change, price, stock, tracking break, placement shift to off-platform inventory | Measurement check, page check, placement breakdown |
| AOV down | Mix shift to cheaper products, discounting | Product set and offer review |

## 2. Diagnostic order (always this sequence)

1. Tracking: did event volume, dedup or values change? (measurement-events-api-attribution.md section 9). If broken, stop. Nothing else is trustworthy.
2. Delivery: account status, payment, disapprovals, budget caps, learning status.
3. External: seasonality, promotions, competitor sales, TikTok Shop mega sales, stock-outs, site outages, price changes.
4. Auction: CPM and placement mix.
5. Creative: hook rate, 6s rate, CTR, frequency, age of top ads.
6. Post-click: CVR, landing page speed, listing quality.
7. Structure and bidding: fragmentation, caps, recent edits.

## 3. Symptom playbook

| Symptom | Likely causes | Checks | Fixes (propose for approval) |
|---------|--------------|--------|-------------------------------|
| No delivery / near-zero spend | Ad rejected, account issue, Cost Cap or Min ROAS too tight, audience too small, budget below minimum, payment failure | Ad status, account banner, bid vs trailing CPA, audience size, billing | Fix policy issue, loosen cap 15% to 20% or switch to Maximum Delivery, broaden, raise budget to at least 10x CPA |
| Spend dumps fast, CPA terrible | Maximum Delivery in a competitive window, new ad group exploring, off-platform placement (TikTok Ad Network) | Hourly spend, placement breakdown | Cost Cap guardrail, exclude off-platform placements, dayparting only if justified |
| Stuck in learning / learning limited | Too few conversions, too many ad groups, frequent edits | Conversions per ad group per 7 days, edit history | Consolidate, move event up funnel, raise budget, stop edits for 7 days |
| CPA spike after a change | Learning reset, edit too large | Change log timing | Wait 3 to 5 days unless CPA > 2x target; revert if needed |
| CPA creep over 2 to 3 weeks | Creative fatigue | CTR and 6s rate trend per ad, frequency, ad age | Launch new concepts; do not just raise bids |
| ROAS down, CPA flat | AOV drop | AOV by campaign and product | Offer, bundle, product set changes |
| Platform conversions up, backend flat | Duplicate events, view-through inflation, attribution window change | Dedup check, attribution columns, window settings | Fix dedup, compare click-only, align windows |
| Backend up, TikTok flat | Tracking loss (consent, pixel removed, Events API down), halo not captured | Event volume, Events Manager diagnostics | Measurement handoff; survey and GA4 triangulation |
| Smart+ spends on one creative only | Normal exploitation; other assets weak or new | Creative report by material ID | Add new concepts as separate asset groups; use testing campaign to prove them |
| Smart+ leaking to unwanted placements | Automatic placement includes Lemon8 or TikTok Ad Network (default for Sales, Lead Generation and App Promotion; US inventory open since 2026-10-05) | Placement breakdown | Set the placement module to manual in the upgraded flow; where Smart+ Web offers no placement choice, TikTok's help says to build a non-Smart+ campaign to exclude TikTok Ad Network [Official]; ask the rep if neither works |
| GMV Max not spending | ROI target above achievable, low creative supply, product issues | Target vs trailing ROI, video queue | Lower target, add videos, fix products |
| Search Ads low impressions | Too few keywords, low bids, budget under 20x bid | Keyword status, search volume in Keyword Insights | Add keywords, raise bids, budget to 20x bid |
| Lead CPL fine, quality poor | Easy form, broad offer, off-platform placements | CRM join by ad | Qualifying questions, placement exclusions, CRM event optimization |
| Ad rejected | Policy (claims, music, landing page, restricted category) | Rejection reason | Edit and resubmit or appeal (policy-and-account-health.md) |
| Account suspended | Policy, payment, suspicious activity, linked banned assets | Account status page | Recovery playbook (scaling-playbooks.md section 7) |
| CPM spike across account | Seasonality (Q4, mega sales), market events | Compare with prior year, same weeks | Lower caps expectations, front-load creative, shift budget to best ad groups |

## 4. Weekly optimization loop (Growth tier and above)

1. Pull data: campaign, ad group, ad (with 2s, 6s views, average watch time, CTR, CPA/ROAS, frequency), placement breakdown, last 7 and 28 days, plus backend orders or CRM stages for the same range.
2. Check measurement health (section 2 step 1).
3. Score each campaign vs target (platform and calibrated). Flag those more than 20% above or below target.
4. Creative review: rank ads by spend; apply kill/keep/scale rules (creative-for-tiktok.md section 5.3); list fatigued ads.
5. Budget proposals: shift from campaigns above target CPA to those below; respect step limits.
6. Test review: close tests that hit their stop rule; log results in EXPERIMENTS.md.
7. Creative pipeline: request new concepts to cover fatigue (creative-strategy handoff with performance notes).
8. Write the weekly report and change list for approval.

## 5. Daily checks (5 minutes)

| Check | Threshold for alert |
|-------|--------------------|
| Spend pacing | Off plan by more than 25% |
| Conversions | Zero conversions for 24 hours on a campaign that normally gets 5+ per day |
| Disapprovals | Any new rejection on an active top-spend ad |
| Account status | Any warning or suspension banner |
| GMV Max | Daily ROI below 70% of target with no edits |
| Budget capped | Top campaigns hitting budget before 6 pm local with CPA below target (opportunity) |

## 6. Optimization levers ranked by typical impact on TikTok

| Rank | Lever | Typical effect | Notes |
|------|-------|---------------|-------|
| 1 | New creative concepts | Largest | Most accounts are creative-constrained, not budget-constrained |
| 2 | Creator and Spark Ads program | Large | Trust and native feel |
| 3 | Measurement fixes (Events API, dedup, values) | Large and compounding | Better signal improves every campaign |
| 4 | Consolidation (fewer ad groups, more signal) | Medium to large | Exits learning |
| 5 | Optimization event depth (Purchase vs ATC, qualified lead vs lead) | Medium | Move deeper when volume allows |
| 6 | Bid strategy and caps | Medium | Guardrails, not growth drivers |
| 7 | Offer and landing page or listing | Medium to large | Hand to cro or commerce-feeds |
| 8 | Placement exclusions | Small to medium | Mostly off-platform inventory |
| 9 | Targeting tweaks | Small | Broad usually wins at scale |
| 10 | Dayparting | Small | Only for lead gen and LIVE |

## 7. Data pull specification (exports or API)

| Level | Dimensions | Metrics |
|-------|-----------|---------|
| Campaign | campaign_id, campaign_name, objective, day | spend, impressions, clicks, ctr, cpm, conversions, cost_per_conversion, conversion value, ROAS |
| Ad group | adgroup_id, name, optimization event, bid strategy, attribution setting, day | same plus frequency, reach |
| Ad | ad_id, ad_name, identity (Spark or not), creative material ID, day | same plus 2s views, 6s views, average watch time, 100% views |
| Placement | placement | spend, conversions, CPA |
| GMV Max | campaign, product, creative | cost, GMV, orders, ROI |

If no connector exists, ask the human for exports per `ads-master/data/imports/HOW_TO_EXPORT.md` and name files `YYYY-MM-DD_tiktok_<level>.csv`.

## 8. Analysis snippets

Python (pandas) to compute creative metrics from an ad-level export:

```python
import pandas as pd
df = pd.read_csv("ads-master/data/imports/2026-10-01_tiktok_ad.csv")
# Rename columns to match your export headers first.
df["hook_rate"] = df["video_views_2s"] / df["impressions"]
df["six_s_rate"] = df["video_views_6s"] / df["impressions"]
df["hold_rate"] = df["video_views_6s"] / df["video_views_2s"]
df["ctr"] = df["clicks"] / df["impressions"]
df["cpa"] = df["spend"] / df["conversions"].where(df["conversions"] > 0)
q = df[df["impressions"] > 5000][["hook_rate", "six_s_rate", "hold_rate", "ctr"]].quantile([0.25, 0.5, 0.75])
print(q)  # account percentiles become your thresholds
```

Fatigue detector logic (per ad, daily data): compare the last 7 days CTR and 6s rate with the ad's first 7 active days; flag when CTR falls 20%+ and 6s rate falls 15%+ while spend is comparable (within 50%).

## 9. When not to act
- Fewer than 3 days of data after a change, unless CPA is above 2x target.
- Weekend dips in B2B lead gen.
- Single-day CPA spikes inside learning.
- Platform-wide reporting delays (TikTok attribution can update for up to the window length; yesterday's numbers are incomplete).
