# Benchmarks

> Rule: compare a project against its own history first, against its own Google data second, and against external benchmarks last. External Microsoft Advertising benchmarks are scarce, mostly vendor or platform sourced, and vary by vertical, geo, device and season. Every number below carries source, date and caveat. Ranges marked [Unverified] are planning assumptions to replace with account data within 30 days.

## 1. Platform sourced claims (directional only)

| Claim | Source | Date | Sample and caveat |
|-------|--------|------|-------------------|
| Ad relevance in Copilot about 25% better than traditional search | Microsoft, reported by Adweek and Microsoft blog | 2025-03 | Company research, method not public; not an account level expectation [Official, 2025-03] |
| CTR in Copilot ads roughly doubled vs traditional search ads | Microsoft via Adweek | 2025-03 | Company claim; placement mix and ad formats differ [Official, 2025-03] [Unverified] |
| Performance Max delivers about 8% more incremental conversions | Microsoft at Activate 2026, via trade recaps | 2026-05 | Company claim; method not public; validate with PMax uplift experiments [Official, 2026-06] [Unverified] |
| Fashion retailer 3x conversion lift in brand agent assisted sessions | Third party 2026 roundup | 2026 | Single self reported case; do not use for planning [Unverified] |

## 2. Planning assumptions (replace with data)

| Metric | Planning range | Basis | Label |
|--------|----------------|-------|-------|
| Microsoft search volume vs Google on the same keywords | 5% to 20% of Google clicks, higher for desktop heavy B2B and older audiences, lower for mobile heavy consumer | Practitioner rule of thumb | [Practitioner consensus] [Unverified] |
| Microsoft CPC vs Google CPC | 0.6x to 0.9x on matched non-brand keywords | Practitioner reports; varies widely by vertical | [Contested] some verticals show parity or higher |
| Conversion rate parity vs Google | 0.8x to 1.2x | Practitioner reports | [Practitioner consensus] |
| Desktop share of clicks | Higher than Google for the same account | Microsoft audience profile statements | [Practitioner consensus] |
| Syndicated partner share of Search clicks | Account specific; often a material minority | Publisher report | Measure, do not assume |

Market share context: Bing's share of global search is in the low single digits across all devices and materially higher on US desktop, per StatCounter style trackers [Unverified]. Check a current tracker before quoting and note that Copilot, Yahoo, AOL, DuckDuckGo and partners add reach beyond Bing branded search.

## 3. Operational thresholds used in this playbook
These are decision thresholds, not market benchmarks.

| Threshold | Value | Used for |
|-----------|-------|----------|
| Conversions for target based smart bidding | About 30 in 30 days per campaign or portfolio | Strategy selection |
| Minimum data for a bid adjustment | 30+ days and spend of at least 2x target CPA in the segment | Bid adjustments |
| Wasted search term spend | Under 15% of non-brand spend | Audit |
| Publisher exclusion trigger | Spend over 2x target CPA with zero conversions | Partner hygiene |
| Target move size | Max 15% to 20% per step | Bidding |
| IS lost to budget worth fixing | Over 15% on campaigns at or under target CPA | Scaling |
| MSCLKID capture rate | Over 85% of Microsoft paid leads | Measurement |
| Offline upload match rate | Over 90% | Measurement |
| Feed approval rate | 95%+ | Shopping and PMax |
| Platform vs backend conversion gap | Within 10% to 25% | Measurement |

## 4. Build the account's own benchmark

Baseline table (create in the first audit, refresh quarterly):
| Segment | Period | Clicks | CPC | CTR | CVR | CPA | ROAS | IS | Source |
|---------|--------|--------|-----|-----|-----|-----|------|----|--------|
| Brand | last 90 days | | | | | | | | Microsoft report export |
| Non-brand core | last 90 days | | | | | | | | |
| Partners | last 90 days | | | | | | | | |
| PMax or Shopping | last 90 days | | | | | | | | |
| Same period last year | | | | | | | | | |
| Google matched keywords | last 90 days | | | | | | | | Google export |

Rules:
- Use the same conversion definition across periods. If the goal changed, mark a break.
- Use full weeks and compare to the same season last year where available.
- Report ranges, not points, when conversions per segment are under 100.

## 5. Is a difference real? (quick significance check)

For conversion rate differences between two segments (for example Microsoft vs Google, or experiment arms):
```python
from math import sqrt
def z_test(conv_a, clicks_a, conv_b, clicks_b):
    p_a, p_b = conv_a / clicks_a, conv_b / clicks_b
    p = (conv_a + conv_b) / (clicks_a + clicks_b)
    se = sqrt(p * (1-p) * (1 / clicks_a + 1 / clicks_b))
    return (p_a-p_b) / se  # |z| > 1.96 is roughly 95% confidence

print(z_test(48, 1200, 400, 10000))  # Microsoft 4.0% vs Google 4.0% -> z near 0
```
Rule of thumb: under 30 conversions per arm, treat differences as noise unless they exceed 50%.

## 6. Benchmark sources to check (and how to use them)
| Source type | What it gives | Caveat |
|------------|---------------|--------|
| Microsoft Advertising insights and blog | Audience and seasonal trends, product claims | Platform sourced, promotional |
| Microsoft Keyword Planner and performance estimates | Account specific volume, CPC and click forecasts | Best forward looking source for your keywords |
| Auction insights | Competitor overlap and outranking in your auctions | Only your auctions |
| Agency and tool vendor benchmark reports | Cross account CPC, CTR, CVR by vertical | Sample, method and date vary; check recency and sample size before quoting |
| StatCounter and similar | Search engine market share | Measures page views, not ad inventory |

## 7. Internal baselines worth building (beyond averages)

| Baseline | How to build | Why it matters |
|----------|-------------|----------------|
| Day of week and hour CVR curve | 90 days, conversions / clicks by day and hour, Microsoft only | Microsoft's B2B and desktop skew often shifts conversion peaks into office hours; compare with Google before copying ad schedules |
| Device CVR and CPA | 90 days by device | Desktop share is higher on Microsoft; device adjustments start here |
| Age and gender CPA | 90 days, segments with 2x target CPA spend only | Microsoft keeps these adjustments on Search |
| LinkedIn industry and job function CPA | 90 days, Bid only layers | Unique B2B baseline; feeds linkedin-ads planning |
| Partner vs owned and operated CPA | Network segment, 90 days | Partner decision |
| Brand CPC and IS trend | Weekly | Detects competitor conquesting on brand |
| Lead to SQL rate by campaign | CRM join on MSCLKID | Lead quality baseline |
| Seasonal index | Weekly conversions / annual weekly average, last 2 years | Budget planning and seasonality adjustments |

## 8. Interpreting gaps (worked examples)

Example 1: Microsoft CPA $95 vs Google $80 on the same non-brand keywords. Microsoft CPC is $2.10 vs $3.00 (ratio 0.70) but CVR is 2.2% vs 3.75% (parity 0.59). The CPC advantage is real; the CVR gap is the problem. Check network segment: partners carry 45% of clicks at 1.1% CVR. Excluding the worst 12 publishers is the first fix, not a bid cut.

Example 2: Microsoft ROAS 6.0 vs Google 4.5 on Shopping. Microsoft spend is only 8% of Google's and IS lost to budget is 38%. The return gap suggests headroom; raise budget in 15% to 20% steps while watching marginal ROAS, and confirm with a PMax or Shopping uplift experiment before claiming incrementality.

Example 3: B2B lead gen CPL on Microsoft $140 vs Google $110, but SQL rate is 31% vs 18% (CRM, 90 days, MSCLKID join). Cost per SQL: Microsoft $452 vs Google $611. Microsoft is the better channel on pipeline even though CPL looks worse. Bid to SQL via offline import.

All three are illustrative calculations, not benchmarks.

## 9. Benchmark hygiene rules
1. Every external number in a deliverable carries source, publication date, sample description and the caveat that results vary by vertical, geo, device and season.
2. Numbers older than 24 months are context only; do not set targets from them.
3. Platform sourced claims (Microsoft, partners selling tools) are labeled as such and never used as a target.
4. When two sources disagree, show both and the account's own number; mark [Contested].
5. Replace every planning assumption in section 2 with account data after 30 days and record the replacement in the journal.
6. Keep currency and tax treatment consistent (net of VAT where the backend reports net).
7. For multi market accounts, benchmark per market; never blend US and European CPCs.
8. Record internal baselines quarterly in `ads-master/outputs/microsoft-ads/` so trend comparisons stay possible after staff or agency changes.
9. When Copilot, partners or Audience Network shares change materially, re-baseline; blended averages hide placement mix shifts.
10. Before presenting, ask: would the decision change if the benchmark were 30% higher or lower? If yes, get account data first.

## 10. Reporting benchmarks to stakeholders
- Always show: account history, Google parity, then any external benchmark with source and date.
- Never present a platform claim (Copilot CTR, PMax incrementality) as the expected outcome for the project.
- When the account beats or misses a benchmark, explain with account facts (query mix, device mix, brand share), not the benchmark.
