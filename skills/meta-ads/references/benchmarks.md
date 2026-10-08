# Benchmarks

> Knowledge as of 2026-10. Benchmarks vary by vertical, geo, season, offer, attribution setting and account maturity. Compare the project against its own history first (same weeks last year, trailing 8 weeks), and against external benchmarks second. Every number here carries source, date and caveat. Numbers that could not be verified in this build are labeled [Unverified]; refresh them through the Freshness Protocol before quoting them to a client.

## 1. How to use benchmarks

1. Own baseline first: build the baseline table in section 7 from the account's last 12 months.
2. External benchmark second, only from sources with a stated sample and date.
3. Never set targets from benchmarks. Targets come from unit economics (bidding module section 1).
4. When an account is far from a benchmark, look for structural reasons (vertical, geo, AOV, attribution setting) before assuming a problem.
5. Attribution changes in 2026 (January 12 and March 3) break year-over-year comparisons of Meta-reported conversions. Compare backend numbers year over year instead.

## 2. Platform-level market data (Meta earnings)

| Period | Ad impressions YoY | Average price per ad YoY | Source | Label |
|--------|-------------------|--------------------------|--------|-------|
| Q2 2025 | +11% | +9% | Meta Q2 2025 earnings release | [Official, 2025-07] |
| Q3 2025 | +14% | +10% | Meta Q3 2025 earnings release | [Official, 2025-10] |
| Q2 2026 | +14% | +12% (driven by ad performance gains, better macro conditions than Q2 2025 and currency) | Meta Q2 2026 results and 10-Q (Family of Apps ad revenue 59.4 billion USD, +27%) | [Official, 2026-07] |
| Q4 2025, Q1 2026, Q3 2026 | check investor.atmeta.com (Q3 2026 results due late October 2026) | check | Meta earnings releases and 10-Q filings | Refresh |
Caveat: global averages across all formats and regions. Price per ad rising means auctions are more competitive on average, but your CPM depends on your audience, creative quality and geo.

## 3. Meta-reported effects of system and feature changes

Meta-reported numbers come from Meta's own tests and selected segments. Treat them as directional evidence that a feature can help, not as expected lifts for a given account.

| Feature | Reported effect | Date | Source | Label |
|---------|----------------|------|--------|-------|
| Andromeda retrieval | +6% retrieval recall, +8% ads quality on selected segments | 2024-12 | Meta Engineering blog | [Official, 2024-12] |
| GEM | About +5% ad conversions on Instagram, +3% on Facebook Feed (Q2 2025) | 2025-11 | Meta Engineering blog | [Official, 2025-11] |
| Lattice extensions | Nearly 4% more ad conversions on Facebook Feed and Reels (Q2 2025) | 2025 | Earnings commentary via secondary | [Official via secondary] |
| Ranking model consolidation | About 12% ads quality increase tied to consolidating surfaces into the Facebook model (Q4 2025) | 2026-01 | Earnings commentary via secondary | [Unverified] |
| GEM plus Lattice | More than 6% conversion rate increase on landing page view ads (Q1 2026) | 2026-04 | Earnings commentary via secondary | [Unverified] |
| Incremental attribution | 46% lift in incremental conversions vs business as usual in Meta tests; earlier tests (Jan to Jun 2024) above 20% | 2025 | Meta via Jon Loomer, Social Media Today | [Official, 2025] |
| Incremental attribution update | 25% average increase in incremental conversions | 2026-04 | One agency blog (Webtopia); no Meta announcement found in the 2026-10 verification pass | [Unverified] |
| New user understanding models plus GEM and sequence learning | +8.3% ad clicks and +15.7% conversions on Facebook; first generative model deployed in ads retrieval; LLM-based preference pilots +1% app event conversions on Instagram | 2026-07 | Meta Q2 2026 earnings call (2026-07-29) | [Official, 2026-07]; combined effect of several changes, not one model |
| Opportunity Score recommendations | Median 12% lower cost per result for advertisers who adopted recommendations | 2024 to 2025 | Meta via Social Media Today and agency blogs | [Official] |
| Advantage+ sales | 22% higher ROAS often quoted | n/a | Widely repeated, not traced to a primary source in this build | [Unverified] |
| Threads in Advantage+ placements | 11.7% lower CPA claimed | 2026 | Single secondary source | [Unverified] |

## 4. Independent and vendor studies

| Study | Finding | Date | Sample and caveat | Label |
|-------|---------|------|-------------------|-------|
| Haus, early tests of Meta incremental attribution | 43% success rate versus standard settings | 2025 | Haus customer tests; vendor; small sample | [Study, 2025] |
| Haus, incremental vs standard attribution, July 2025 to June 2026 | Pooled incremental return 1.26x for incremental attribution vs standard (DTC-only 1.38x, omnichannel 1.02x); standard had led at 0.80x in the prior year | 2026 | Haus geo tests; vendor | [Study, 2026] |
| Cassandra App analysis | Incremental ROAS 1.90x for cold acquisition, 3.64x for retargeting, versus 8x platform-reported | 2025 to 2026 | Vendor analysis, method not fully public | [Study, vendor] |
| Seer Interactive, incremental attribution test on about $1M spend | Practitioner test write-up | 2025 | Single agency, specific clients | [Study, 2025] |
| Vendor reports on March 2026 click attribution change | Reported click-through conversions down 15 to 40% overnight in some accounts | 2026-03 | WooCommerce store samples, vendor blogs | [Unverified] |
| Vendor reports on January 2026 view window removal | Reported conversions down 15 to 30% for advertisers relying on 7-day view | 2026-01 | Vendor estimates | [Unverified] |
| Threads CPM | 30 to 50% below Instagram Feed | 2026 | Agency commentary quoted in 2026-09 coverage of the Threads profile change; no Meta figure | [Unverified] |

## 5. Practitioner diagnostic ranges (heuristics, not targets)

These ranges are commonly used by experienced operators to flag where to look. They are not benchmarks with a sample. Use them only to prioritize investigation. [Practitioner consensus]

| Metric | Healthy zone (cold acquisition, ecommerce, US and EU) | Investigate when |
|--------|-------------------------------------------------------|------------------|
| Hook rate (3s plays / impressions) | 25 to 40% | Below 20% |
| Hold rate (ThruPlay / 3s plays) | 8 to 15% (varies with length) | Below 5% |
| CTR (link) | 0.8 to 2.0% | Below 0.6% with normal CPM |
| Frequency, 7-day, cold | 1.2 to 2.5 | Above 3 with falling CTR |
| Frequency, 7-day, retargeting | 2 to 6 | Above 8 to 10 |
| Share of spend on top ad | under 40 to 50% | Above 60% (fragile) |
| Existing customer share of spend in acquisition campaigns | depends on goal, often 10 to 25% | Above 30% when growth is the goal |
| Ad sets in Learning limited | under 20% of spend | Above 50% of spend |
| EMQ Purchase | 7 to 10 | Below 6 |
| Days since last new concept | under 7 (Growth and above) | Above 21 |

## 6. Benchmark sources to pull fresh numbers

| Source | What | Access | Caveat |
|--------|------|--------|--------|
| Meta investor relations (investor.atmeta.com) | Quarterly impressions and price per ad, Advantage+ commentary | Free | Global averages |
| Varos | Peer benchmarks by vertical and spend for connected stores | Account | Self-selected sample, Shopify heavy |
| Triple Whale benchmarks | Ecommerce CPM, CPA, ROAS by vertical | Free pages and app | Shopify brands, Triple Whale attribution |
| Motion creative benchmarks reports | Creative metrics (hook, hold, CTR) by vertical | Free reports | Motion customers |
| LocaliQ / WordStream annual Facebook ads benchmarks | CTR, CPC, CPL, CVR by industry | Free | SMB heavy, methodology varies year to year |
| Birch (formerly Revealbot) CPM trackers | Daily CPM and CPC trends | Free pages | Customer sample |
| Haus, Measured, Recast publications | Incrementality ranges by channel | Free reports | Vendor customers |
Record any external number used with source, date, sample and the exact metric definition in the output.

## 7. Own baseline template (build in every audit)

```
| Metric | L7D | L28D | L90D | Same 28D last year | 8-week mean | 8-week std dev | Notes |
|--------|-----|------|------|--------------------|-------------|----------------|-------|
| Spend |
| CPM |
| CTR (link) |
| CVR (click to purchase or lead) |
| CPA (platform, stated attribution) |
| ROAS (platform) |
| Backend revenue or qualified leads |
| MER or blended CAC |
| New customer % (audience segments) |
| Frequency 7d |
| Hook rate (video ads) |
| Concepts live / new this period |
```
Normal variance: weekly CPA moves within plus or minus 1 standard deviation of the 8-week mean are noise unless a known change explains them.

## 8. Seasonal context

| Period | Typical auction effect | Note |
|--------|-----------------------|------|
| Q1 (January to February) | CPMs often lowest of the year after holiday peak | Good for testing and acquisition at efficient cost [Practitioner consensus] |
| Late November (BFCM) | CPM peak, conversion rates also peak for retail | Judge on contribution margin |
| December after shipping cutoffs | Retail conversion falls, CPM still elevated | Shift to gift cards, digital, local pickup |
| Ramadan, Eid, local holidays (Turkey, MENA) | Shifts in time-of-day usage and purchase intent | Plan with local calendar |
| Elections | CPM rises in affected markets (US, others) | Expect volatility |
Caveat: patterns vary by vertical and market; use the account's own previous year first.

## 9. Metric definitions (keep comparisons valid)

| Metric | Definition used in Ads Master | Common trap |
|--------|-------------------------------|-------------|
| CPM | Spend / impressions x 1000 | Mixing reach and frequency buying with auction buying |
| CTR (link) | Link clicks / impressions | Using "CTR (all)" which includes likes, profile clicks and expansions |
| CVR | Conversions / link clicks (or / landing page views, state which) | Mixing denominators across reports |
| CPA | Spend / conversions at the stated attribution setting | Comparing 7-day click plus 1-day view CPA to 1-day click CPA |
| ROAS | Conversion value / spend at stated attribution | Comparing to MER |
| MER | Total revenue / total paid media spend (all channels) | Using Meta-only spend in the denominator |
| New customer CAC | Paid media spend / new customers (backend) | Using platform new customer estimates |
| Hook rate | 3-second video plays / impressions | Using ThruPlays |
| Cost per qualified lead | Spend / CRM-qualified leads in the period | Lag: leads qualify days later; use cohort by lead date |
State attribution setting, date range and data source in every benchmark comparison.

## 10. Benchmark comparison template (paste into outputs)

```
| Metric | Our value | Our 8-week mean | External benchmark | Source, date, sample | Caveat | Read |
|--------|-----------|-----------------|--------------------|----------------------|--------|------|
| CPM |
| CTR (link) |
| CPA |
```
Read column options: "in line", "watch", "investigate". Never "bad" or "good" from a benchmark alone.
