# Benchmarks

> Knowledge as of 2026-10. Benchmarks vary by vertical, country, season, brand strength, match type mix and attribution settings. Compare a project against its own history first and against external benchmarks second. Every benchmark below carries its source, date and caveat. Refresh annually.

## 1. How to use benchmarks (procedure)

1. Build the internal baseline first: last 90 days and the same 90 days last year, by campaign type and brand vs non-brand (GAQL Q1, Q2, Q27).
2. Compare against the closest external benchmark: same vertical, same country, same campaign type. If none exists, say so.
3. Treat any gap above 30% as a question to investigate, not as a verdict.
4. Never set targets from external benchmarks. Targets come from unit economics (see bidding module formulas).
5. In deliverables, label each benchmark: source, publication date, sample, caveat.

## 2. External Search benchmarks (all industries)

| Metric | Value | Source | Date | Sample and caveat |
|---|---|---|---|---|
| Average Search CTR | 6.66% | WordStream by LocaliQ, Google Ads Benchmarks 2025 | 2025 | US-centric advertiser sample across about 20 industries, data roughly April 2024 to March 2025; averages hide large differences by industry and by brand share [Study, 2025; figures from prior knowledge, Unverified this session: confirm against the current edition before quoting] |
| Average Search CPC | 5.26 USD | Same | 2025 | CPCs rose year over year in most industries in that report |
| Average Search conversion rate | 7.52% | Same | 2025 | Conversion definitions differ by advertiser |
| Average cost per lead | 70.11 USD | Same | 2025 | Lead definitions vary; not qualified leads |

A 2026 edition may exist; the agent must check before quoting. Use the industry tables in the current edition for vertical comparisons.

Other recurring benchmark sources to check (no figures quoted here because they were not verified this session):
| Source | What it covers | Cadence |
|---|---|---|
| Tinuiti Digital Ads Benchmark Report | Google Search, Shopping, PMax spend, CPC and click growth trends for large retail advertisers | Quarterly |
| Skai quarterly trends report | Search, retail media and social trends | Quarterly |
| Optmyzr studies | PMax, match types, AI Max and bidding analyses on large account samples | Irregular |
| Smarter Ecommerce (smec) research | PMax and Shopping analyses | Irregular |
| Google Ads API percentile benchmarks (v25.2) | Competitive benchmark percentiles by category for an account | Ongoing [Official via trade press, 2026-09] |
| Google Analytics benchmarking | Anonymized peer averages in GA4 | Ongoing |

## 3. Google's own uplift claims (vendor claims, not independent)

| Claim | Value | Source and date | Caveat |
|---|---|---|---|
| AI Max for Search | 14% more conversions or conversion value at similar CPA or ROAS on average; 27% for campaigns mostly using exact and phrase match | Google, 2025-05 | Google internal data; incrementality vs keyword cannibalization not shown. Test with AI Max experiments |
| Smart Bidding Exploration | 18% more unique converting query categories, 19% more conversions | Google, internal data 2025-03-11 to 2025-04-11 | Selection effects possible; judge on profit |
| Enhanced conversions | About 11% more Search conversions on average vs standard imports | Google 2026 materials via trade press, 2026-09 | Recovered conversions are partly modeled or matched, not incremental sales |
| Demand Gen H2 2025 improvements | 30% average conversion increase | Google via trade press, 2026-08 | Platform reported conversions |
| ABCD video framework | Ads following ABCD associated with higher short-term sales likelihood | Google and Kantar research (Think with Google) | Correlational creative research |

Rule: when quoting these to a client, say "Google reports" and add the caveat.

## 4. Operating thresholds (practitioner rules, not industry averages)

These are decision thresholds used throughout this package. They are [Practitioner consensus] unless noted. Adjust per account.

| Area | Threshold | Meaning |
|---|---|---|
| Brand search impression share | Above 90% | Below this, competitors or budget limits are taking brand traffic |
| Brand CTR | Typically 20% to 40%+ on exact brand terms | Much lower suggests competitor or aggregator pressure, or a brand name shared with generic terms |
| Non-brand Search lost IS (budget) | Under 10% on campaigns at target | Above: budget is binding |
| Non-brand Search lost IS (rank) | Under 40% | Above: target, bid or quality constraints |
| Zero-conversion search term spend | Under 10% to 15% of Search spend (30-day, terms above 1x target CPA) | Above 25%: weak negatives or broad match without signal |
| Cost-weighted Quality Score | 6 or higher on non-brand | Below 5: structure or landing page issues |
| RSA ad strength | Good or Excellent on most ads | Not a performance metric, but Poor often means too few assets |
| Conversions per bid strategy | 30+ per 30 days (tCPA), 50+ (tROAS) | Below: pool or simplify |
| PMax Display plus YouTube cost share | Investigate above 30% when their conversion value share is under 10% | Possible low quality inventory |
| PMax brand term share of conversions | Investigate above 20% | Brand cannibalization |
| Shopping product coverage | 80%+ of active products with impressions in 30 days | Below: zombie products, feed or target problems |
| Lead to qualified lead rate from Google Ads | Compare to other channels; flag under half of the account average | Spam or wrong intent |
| Conversion tracking lag | Know the median days from click to conversion | Do not judge campaigns before 1 to 2 lag cycles |
| Optimization score | Not a KPI | Use as a list of suggestions; reject those that conflict with goals |

## 5. Relative cost patterns (directional)

| Pattern | Typical relation | Use |
|---|---|---|
| Brand vs non-brand CPC | Brand CPC usually a fraction of non-brand CPC unless competitors bid on the brand | Rising brand CPC with competitor overlap in auction insights signals conquesting |
| Competitor terms CPA | Often 1.5x to 3x non-brand CPA | Budget competitor campaigns separately with their own kill rule |
| Remarketing CPA | Lower than cold audience acquisition but less incremental | Do not compare on platform CPA alone |
| Demand Gen vs Search CPA | Demand Gen usually higher on click-through CPA | Judge with lift tests |
| Mobile vs desktop conversion rate | Varies by vertical; B2B often converts better on desktop | Smart Bidding adjusts automatically |

## 6. Building an internal benchmark table (template)

```
| Segment | Period | Spend | Clicks | CTR | CPC | Conv | CVR | CPA | Value | ROAS | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Brand Search | 2026-07-01 to 2026-09-30 | | | | | | | | | | GAQL Q27, export date |
| Non-brand Search | same | | | | | | | | | | |
| PMax | same | | | | | | | | | | |
| Standard Shopping | same | | | | | | | | | | |
| Demand Gen | same | | | | | | | | | | |
| Same period last year | 2025-07-01 to 2025-09-30 | | | | | | | | | | |
```

Store confirmed baselines (not one-off numbers) in `ads-master/memory/google-ads.md` under "Account and setup facts worth remembering".

## 7. Seasonality references

- Retail peaks: Black Friday and Cyber Monday week, pre-Christmas, local holidays; CPCs and conversion rates both rise.
- Lead gen: January and September often see demand spikes for education, finance and B2B; summer dips in B2B.
- Compare year over year at the same weekday alignment, not the same date.
- Use seasonality adjustments only for short, sharp events (see bidding module).

## 8. Benchmark refresh checklist (annual or when a new report lands)

1. Check whether WordStream by LocaliQ published a new Google Ads benchmark edition; update section 2 with the new figures, date, sample and method.
2. Check Tinuiti and Skai latest quarterly reports for CPC and spend trends in Search and Shopping.
3. Check Google Ads API release notes for benchmark resources and the Google Ads UI for benchmark features.
4. Update the date at the top of this file. Log the refresh in the journal.

## 9. Before trusting any benchmark

| Question | Why |
|---|---|
| What is the sample (size, countries, account sizes)? | US small business samples rarely match an EU enterprise account |
| What period does it cover? | CPCs and conversion rates shift every year and every season |
| How are conversions defined? | A newsletter signup and a purchase are both "conversions" in many reports |
| Is brand traffic included? | Brand inflates CTR and conversion rate |
| Which campaign types? | Search, Shopping and PMax benchmarks are not interchangeable |
| Who published it and why? | Vendors publish data that supports their product; that does not make it wrong, but label it |

## 10. Vertical notes (directional, Practitioner consensus)

| Vertical | Pattern |
|---|---|
| Legal, insurance, finance | Highest CPCs; lead quality varies widely; OCI essential |
| Home services | High intent, call heavy; LSA competes with Search; location precision matters |
| Ecommerce apparel and beauty | Lower CPCs, feed and creative driven; PMax and Shopping dominate |
| B2B software | High CPCs, long cycles; brand and competitor terms matter; Search volume limited |
| Travel | Seasonal; AI Max for Travel and Direct Offers changing formats in 2026 |
| Healthcare | Policy restrictions, no ads in AI Overviews for sensitive verticals |
