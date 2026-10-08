# Benchmarks

> Knowledge as of 2026-10. Compare a project against its own history first and benchmarks second. Every external number below carries source, date, sample and caveat. Benchmarks vary by vertical, geo, season, objective, attribution window and creative quality. Third-party CPM, CPC and CVR averages for TikTok could not be verified from primary sources in this research cycle (web fetch unavailable, search budget exhausted), so none are quoted as fact. Pull live industry benchmarks from the sources in section 4 at the time of the task.

## 1. Order of comparison
1. Same account, same campaign type, same season last year (seasonality-adjusted).
2. Same account, trailing 28 and 90 days.
3. TikTok's own industry benchmarks for the vertical and market (Creative Center, rep-provided).
4. Third-party studies with a stated method and sample.
5. Practitioner rules of thumb (lowest weight).

## 2. Verified platform figures (with caveats)

| Figure | Value | Source | Date | Sample / method | Caveat |
|--------|-------|--------|------|-----------------|--------|
| TopReach incremental reach | 59% incremental reach at 3x lower cost per reach vs buying TopView alone | TikTok (reported in trade press) | 2026-03 | TikTok internal | Platform-reported, brand campaigns only |
| GMV Max GMV uplift | About 20% GMV uplift in initial tests (also phrased "up to 20% incremental GMV") | TikTok internal data | 2024 to 2025 | Initial tests, not disclosed | Self-reported; "incremental" not independently verified |
| MCP connector usage | +200% advertiser usage since launch | TikTok internal | 2026-07 to 2026-09 | No base number | Growth from a small base is likely |
| US users and businesses | Over 200 million US users and 7.5 million businesses (earlier memo: 170 million Americans) | TikTok | 2026-03 | Self-reported | Definitions of "user" differ |
| TikTok Ad Network scale | Nearly 400,000 apps, 48 markets, 40+ app genres, 300 sub-categories (August coverage said "more than 400,000") | TikTok | 2026-10 | Self-reported | Inventory quality varies widely by app |
| 2026 TikTok global ad revenue projection | About $38 billion, 38% from the US | WARC via an aggregator | 2026 | Forecast | [Unverified], secondary citation |
| Symphony production time | 50% to 70% reduction in production time reported by creators | Third-party citing TikTok | 2026 | Not disclosed | [Unverified] |

## 3. Official operating thresholds (use as guardrails, not KPIs)

| Item | Threshold | Source |
|------|----------|--------|
| Minimum daily budget | Campaign above $50, ad group above $20 | TikTok Help Center, About budgets |
| Smart+ Web budget | 30x historical CPA ideal, at least 10x | TikTok Help Center, Smart+ Web best practices |
| Smart+ Web creatives | At least 6 at creation | Same |
| Smart+ edits | No significant edits in the first 7 days; bid edits up to 15% every 2 days afterwards | Same |
| Smart+ Lead Generation scaling | Budget increases no more than 50% per day | TikTok Help Center, Smart+ Lead Generation best practices |
| VBO for web budget | 10x target CPA for Complete Payment | TikTok Help Center, 2025-02 |
| Search Ads budget | About 20x the bid | TikTok Help Center, 2026-08 |
| GMV Max new product start | Max Delivery for the first 3 to 5 days, then Target ROI | TikTok Help Center |
| LIVE GMV Max creative supply | At least 50 to 70 videos "In queue" | TikTok Help Center |
| ROI protection | Credits when daily ROI is below 90% of target; generally more than 20 daily orders; no edits that day | TikTok Help Center, 2026-02 |
| Creative Boost minimum | $10 per day | TikTok Help Center |
| EVTA threshold | 6-second watch (or full ad if shorter) | TikTok Help Center |
| Dedup window | 48 hours from first event | TikTok Help Center, 2025-05 |
| Learning phase exit | About 50 conversions per ad group in 7 days | [Practitioner consensus]; one guide cites 25 [Contested] |

## 4. Where to get current vertical benchmarks (pull at task time)

| Source | What it gives | How to use |
|--------|--------------|-----------|
| TikTok Creative Center: Top Ads and its industry dashboards | Top ads by industry, region, objective, with performance indicators (CTR and view-based metrics where shown) | Filter to the project's industry and market for the last 30 days; record the values with the date pulled |
| TikTok account rep | Industry CPA, CTR, CVR and 6s view rate benchmarks for the vertical and market | Ask for the period, sample and attribution window behind every number |
| Ads Manager Split Test results | Your own controlled comparisons | Highest-quality benchmark for your account |
| Third-party benchmark reports from ad tech and analytics vendors | Cross-account medians | Use only when the method (sample size, period, attribution) is published |
| Peer data (agency, communities) | Anecdotes | Hypotheses only |

Record every external benchmark in the output with: source, URL, date pulled, sample, attribution window, region, vertical.

## 5. Build the project's own baselines

Procedure:
1. Export 90 days of ad-level daily data (impressions, spend, clicks, conversions, value, 2s views, 6s views, average watch time).
2. Exclude ads with fewer than 5,000 impressions (noise).
3. Compute per-ad metrics: hook rate (2s / impressions), 6s rate, hold rate (6s / 2s), CTR, CVR, CPA, ROAS, CPM.
4. Compute spend-weighted percentiles (P25, P50, P75) per metric, per campaign type (Smart+, manual, GMV Max, lead gen).
5. Compute a seasonality index from last year's weekly CPM where available.
6. Store the baseline table in the output report and the summary in memory (account facts) once two quarters agree.

Spend-weighted percentile snippet:

```python
import numpy as np, pandas as pd
def wpct(values, weights, q):
    idx = np.argsort(values); v, w = np.array(values)[idx], np.array(weights)[idx]
    cw = np.cumsum(w) / w.sum()
    return float(np.interp(q, cw, v))
ads = pd.read_csv("ads-master/data/imports/2026-10-01_tiktok_ad_90d.csv")
ads = ads[ads["impressions"] >= 5000]
ads["hook_rate"] = ads["video_views_2s"] / ads["impressions"]
for q in (0.25, 0.5, 0.75):
    print(q, wpct(ads["hook_rate"], ads["spend"], q))
```

## 6. Baseline template (fill per project)

```
Baseline: <account> | Data: <files>, <date range> | Attribution: 7d click + 1d view
| Campaign type | Metric | P25 | P50 | P75 | Trend vs prior 90d | Notes |
| Smart+ Web | CPM | | | | | |
| Smart+ Web | Hook rate | | | | | |
| Smart+ Web | 6s rate | | | | | |
| Smart+ Web | CTR | | | | | |
| Smart+ Web | CVR | | | | | |
| Smart+ Web | CPA | | | | | |
| GMV Max | ROI | | | | | |
| Lead gen | CPL / CPQL | | | | | |
```

## 7. Vertical patterns (qualitative)

| Vertical | Pattern on TikTok | Label |
|----------|------------------|-------|
| Beauty, personal care, fashion accessories | Strong fit for TikTok Shop, affiliates and LIVE; demo-driven creative; fast fatigue | [Practitioner consensus] |
| Home, gadgets, cleaning | Result-first and ASMR demos; strong Shop fit | [Practitioner consensus] |
| Food and beverage, consumables | Creator taste tests; repeat purchase makes purchaser exclusion optional | [Practitioner consensus] |
| Apparel | Try-on content; returns erode Shop ROI, model returns in breakeven ROI | [Practitioner consensus] |
| Apps and games | Gaming installs scale on TikTok and the ad network; subscription apps need AEO or VBO to avoid low-quality installs | [Practitioner consensus] |
| Education, insurance, home services lead gen | Cheap leads, quality varies; qualifying forms and CRM optimization required | [Practitioner consensus] |
| B2B SaaS | Works for awareness and mid-market or SMB offers with founder or practitioner creators; enterprise ABM fits LinkedIn better | [Practitioner consensus] |
| Finance, health, supplements | Policy-heavy; slower approvals; claims restricted | [Practitioner consensus] |
| Luxury and high-ticket | Brand formats and creators drive search and site visits; last-click looks weak; use lift tests | [Practitioner consensus] |

## 8. Ads Master default decision thresholds (tune per account)

| Decision | Default | Module |
|----------|---------|--------|
| Kill an ad | 2x to 3x target CPA spend, zero conversions | creative-for-tiktok.md |
| Scale an ad | CPA at or below 0.8x target with 10+ conversions in 7 days | creative-for-tiktok.md |
| Fatigue flag | CTR down 20%+ and 6s rate down 15%+ vs first 7 days | creative-for-tiktok.md |
| Budget step (manual) | +20% to 30% every 48 to 72 hours | bidding-and-budgets.md |
| Retargeting share | 10% to 20% of TikTok spend unless incrementality shows more | audiences-and-targeting.md |
| Testing share of spend | 10% to 20% at Growth and Scale | scaling-playbooks.md |
| Performance alert | CPA up 50%+ or ROAS down 33%+ over 3+ days | scaling-playbooks.md |

These are house defaults, not industry benchmarks. Replace them with project-specific thresholds once 90 days of data exist and record the change in memory.
