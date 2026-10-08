# Performance Max, Shopping and Microsoft Merchant Center

> Scope: Merchant Center setup and feed health, Standard Shopping, Performance Max (feed and non-feed), new customer acquisition, guardrails, reporting, and Copilot commerce readiness. Feed engineering belongs to commerce-feeds.

## 1. Timeline of PMax and Shopping changes

| Date | Change | Label |
|------|--------|-------|
| 2024 (first half) | PMax globally available to all advertisers | [Official, 2024-07] |
| 2025-02 | LinkedIn profile targeting as a PMax audience signal, pilot in 6 markets | [Official, 2025-02] |
| 2025-04 | Test feed in Merchant Center; Primary feed for local inventory ads | [Official, 2025-04] |
| 2025-05 | PMax works with scripts and automated rules; more asset and audience reporting; LinkedIn signal; brand list import from Google and NCA goal announced as coming | [Official, 2025-05] |
| 2025-05 | Auction change: PMax and Standard Shopping targeting the same products in one account now compete (no automatic PMax priority) | [Official, 2025-06] |
| 2025-09 | Supplemental feeds GA in Merchant Center; budget suggestions and performance estimates for non-feed PMax; asset group level reporting; share of voice metrics | [Official, 2025-09] |
| 2026-01 | NCA goal open beta; share of voice metrics in PMax (search and shopping only, data from 2025-11-10); asset group level tracking template and custom parameters | [Official, 2026-01] |
| 2026-02 | NCA goal GA; PMax negative keywords open beta; Ad Preview Hub for Audience ads | [Official, 2026-02] |
| 2026-03 | Self-serve PMax negative keywords: campaign or shared lists, account level lists, up to 5,000 terms per list, same match behavior as Search, via UI, API, Editor and Google Import | [Official, 2026-03] |
| 2026-04 | Import PMax with NCA goals from Google; landing page (Final URL) report for PMax | [Official, 2026-04] |
| 2026-05 | Activate: PMax search insights, Microsoft claims about 8% more incremental conversions with PMax; Universal Commerce Protocol and Copilot Checkout; Merchant Center self-serve store name and domain changes | [Official, 2026-06] |
| 2026-06 | Product explorer in Merchant Center (catalogs under 100,000 SKUs) | [Official, 2026-06] |
| 2026-07 | Ad Preview Hub extended to PMax: previews on MSN, Bing Search and Outlook | [Official, 2026-07] |
| 2026-09 | PMax uplift experiments GA (announced for 2026-09-08); Experiments GA for Shopping and PMax | [Official, 2026-08] [Official, 2026-09] |

## 2. Microsoft Merchant Center

Setup:
1. Create a store in Microsoft Merchant Center; verify and claim the website domain.
2. Feed source: Google Merchant Center import (scheduled), Shopify integration, scheduled file fetch, API, or manual upload. Prefer the same source of truth as Google so product IDs match.
3. Use the Test feed option to validate a feed without affecting live listings [Official, 2025-04].
4. Add supplemental feeds for overrides (titles, custom labels, promotions) without rebuilding the primary feed [Official, 2025-09].
5. Local inventory: primary feed for local inventory ads [Official, 2025-04].
6. Use Product explorer to find products that are inactive, not serving or missing data; export filtered lists (stores under 100,000 SKUs) [Official, 2026-06].

Feed health thresholds (weekly in peak season, monthly otherwise):
| Metric | Healthy | Action threshold |
|--------|---------|------------------|
| Products approved / submitted | 95%+ | Under 90%: hand off to commerce-feeds |
| Products with impressions / approved | Depends on catalog; track trend | Drop of 20%+ in a week: check sync and campaign product splits |
| Price and availability mismatches | Near zero | Any spike: check fetch schedule and structured data |
| Custom labels populated | 100% for labels used in splits | Missing labels break margin based structures |

Custom label plan (set once, used by Shopping and PMax):
| Label | Values | Use |
|-------|--------|-----|
| custom_label_0 | margin tier: high, mid, low | Separate tROAS by margin |
| custom_label_1 | price band | Bid and structure by AOV |
| custom_label_2 | best seller, long tail, new | Hero vs tail splits |
| custom_label_3 | seasonal flag | Seasonal campaigns |
| custom_label_4 | clearance or promo | Promotion campaigns |

## 3. Standard Shopping vs PMax

| Question | Standard Shopping | Performance Max |
|----------|------------------|-----------------|
| Inventory | Shopping placements on search and partners | Search, Shopping, Audience Network, Copilot and partner placements |
| Control | Product groups, negatives, bids, priorities | Asset groups, listing groups, signals, negatives (since 2026-03), brand exclusions, NCA |
| Reporting | Full search terms, product level | Search insights, asset group, landing page, share of voice; less granular |
| Best for | Low budget, tight margin control, testing, B2B commerce with niche queries | Scale, full funnel coverage, new customer acquisition |
| Risk | Missing reach | Budget drift to remarketing, brand or audience placements |

Since the 2025-05 auction change, PMax and Standard Shopping targeting the same products compete on Ad Rank [Official, 2025-06]. Plan product splits so each product has one primary campaign, or run a deliberate Experiment.

Decision tree:
```
Feed approved rate 95%+ and conversion tracking with values verified?
  no -> fix first (commerce-feeds, measurement)
Monthly purchases from Microsoft 30+ or Google PMax proven profitable?
  no -> Standard Shopping with Manual or Enhanced CPC, then Maximize conversion value
  yes -> PMax by margin tier, with Standard Shopping kept for hero SKUs or tests if needed
Is new customer growth the goal and are customer lists available?
  yes -> enable NCA goal (bid higher for new, or new only)
```

## 4. PMax build standard

Structure:
- One PMax per margin tier or business line (custom_label_0), not per product category unless budgets differ.
- Asset groups by theme or category with matching final URLs; 1 to 5 per campaign at Growth tier.
- Non-feed PMax for lead gen only with qualified conversion goals and strong negatives.

Assets per asset group (fill all):
| Asset | Count | Notes |
|-------|-------|-------|
| Headlines | up to 15 | Include brand, category, offer |
| Long headlines | up to 5 | Benefit plus proof |
| Descriptions | up to 5 | Offer, proof, objection |
| Images | 5 to 20 across landscape and square | Product in use, lifestyle, brand |
| Logos | 1 to 5 | Square and landscape |
| Videos | Optional but recommended | Without video, the system may auto-generate |
| Business name | 1 | Exact brand |

Audience signals: remarketing lists, customer match, in-market segments, custom segments, and LinkedIn profile signals (company, industry, job function) for B2B commerce [Official, 2025-05].

Guardrails (all required before launch):
- [ ] Brand exclusions via brand lists (importable from Google since 2025-05)
- [ ] Negative keyword list linked (up to 5,000 terms per list) [Official, 2026-03]
- [ ] URL expansion settings and URL exclusions reviewed
- [ ] Asset group tracking template and custom parameters set for analytics [Official, 2026-01]
- [ ] Ad Preview Hub checked for how auto-assembled creative renders [Official, 2026-07]
- [ ] Sensitive industry: review autogenerated assets [Official, 2026-04]

## 5. New customer acquisition (NCA)

GA since 2026-02 for advertisers with purchase conversion goals [Official, 2026-02].
| Mode | Use when | Setting logic |
|------|----------|---------------|
| Bid higher for new customers | Repeat customers are valuable but acquisition is the growth lever | Set new customer value from 12 month LTV minus first order margin; start conservative |
| New customers only | Repeat customers are reached cheaply by email and CRM | Expect lower volume and higher CPA |
| Off | Customer lists unavailable or unreliable | Fix lists first |

Requirements: customer lists or UET based existing customer definitions kept fresh (upload at least monthly). Without fresh lists, the system misclassifies returning buyers as new.

Measure: new customer share from backend (first order flag), not only platform labels.

## 6. PMax reporting and review routine (weekly)
1. Share of voice: impression share, click share, IS lost to budget and rank (search and shopping only) [Official, 2026-01].
2. Search insights: categories and queries driving conversions; add negatives for irrelevant clusters.
3. Landing page report: spend and conversions by final URL; exclude URLs that waste spend (blog, careers, support) [Official, 2026-04].
4. Asset group report and asset performance; replace low performers monthly.
5. Product level performance via Product explorer and product reports.
6. Brand leakage check: share of conversions on brand queries.

## 7. Testing PMax
- Uplift experiments for PMax measure incremental conversions with a holdout (GA from 2026-09) [Official, 2026-08]. Use before scaling PMax budget more than 50%.
- Optimization experiments (GA 2026-09) compare settings side by side and let you apply the winner or create a new campaign [Official, 2026-09].
- Classic test: PMax vs Standard Shopping on a 50/50 product split by custom label for 4 to 6 weeks; primary metric contribution margin.

## 8. Copilot commerce readiness
Microsoft announced the Universal Commerce Protocol and Copilot Checkout at Activate 2026 so that product data powers shopping inside Copilot [Official, 2026-06]. Readiness steps:
- [ ] Feed complete: GTIN, brand, detailed titles, rich descriptions, multiple images, price, availability, shipping and returns.
- [ ] Product attributes that answer conversational questions (size, material, compatibility, use case).
- [ ] Structured data on product pages matches the feed.
- [ ] Policies and returns pages clear and crawlable.
- [ ] Hand off protocol and checkout integration questions to commerce-feeds; eligibility and partners change quickly [Unverified] for current enrollment steps.

## 9. Common expensive mistakes
| Mistake | Cost | Fix |
|---------|------|-----|
| PMax without brand exclusions | Pays for brand clicks that would convert anyway | Brand lists plus brand negatives |
| Same products in PMax and Shopping by accident | Unplanned auction competition, muddy data | Product split by label |
| NCA on with stale customer lists | Pays new customer premium for repeat buyers | Monthly list refresh |
| Feed import from Google left on default without monitoring | Silent disapprovals | Weekly Product explorer review |
| Judging PMax on platform ROAS only | Overstates incrementality | Uplift test, backend new customer revenue |
| Ignoring landing page report | Spend on non commercial URLs | URL exclusions |
