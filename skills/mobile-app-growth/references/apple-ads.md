# Apple Ads (formerly Apple Search Ads)

> Knowledge as of 2026-10. Key changes: product renamed Apple Ads in 2025; Maximize Conversions bidding in beta 2025-12, open to all advertisers 2026-02, CPA caps being phased out; multiple ad positions in App Store search results from 2026-03-03 (UK and Japan first, all markets by end of March, iOS and iPadOS 26.2+); budget recommendations for Search tab, Today tab and product page campaigns (2026-05, secondary coverage); new Apple Ads Platform API launched 2026-08 with Campaign Management API v5 shutting down 2027-01-26; new creative assets usable in Today tab and search ads (WWDC26, fall 2026); Apple Maps ads in the US and Canada (summer 2026). Verify each item in the live account.

## 1. Products, placements and billing

| Item | Detail | Evidence |
|------|--------|----------|
| Apple Ads Advanced | Full control: campaigns, ad groups, keywords, bids, audiences, all placements | [Official] |
| Apple Ads Basic | Search results only, automated, pay per install (CPI), budget capped at $10,000 per app per month, for app owners | [Practitioner consensus, 2026, verify cap] |
| Search results | Ads at the top of results and, since 2026-03, in additional positions lower in the results, blended with organic listings; you cannot bid for a position; weak matches are excluded regardless of bid | [Official, 2026-01] |
| Search tab | Ad at the top of the suggested apps list before a search | [Official] |
| Today tab | Ad on the Today tab front page; shows app name, icon, subtitle and links to a custom product page | [Official] |
| Product pages | Ad in "You Might Also Like" on other apps' product pages | [Official] |
| Billing | Cost per tap on every Advanced placement: invoices show CPT-KW (search results), CPT-ST (Search tab), CPT-TT (Today tab), CPT-WB (product pages while browsing); CPI-KW for Basic | [Official, Apple Ads invoices help] |
| Bid strategies | Max CPT bid (manual) on all placements; Maximize Conversions with target CPA on search results only | [Official, 2026-02] |

Guides that describe Today tab or Search tab as CPM priced are outdated; CPM is only a reporting metric now [Practitioner consensus, 2026].

## 2. How the auction works

- Relevance first: Apple only shows an ad when the app is relevant to the query (metadata, category, user behavior). A high bid cannot buy an irrelevant query.
- Then bid and relevance together decide order and price; you pay at most your max CPT bid, usually less.
- With multiple ad positions, campaigns are automatically eligible for all positions; reports show results by ad position via the Platform API [Official, 2026; position reporting per secondary coverage].
- Apple Ads uses first-party App Store data; targeting does not use third-party data, and Apple Ads attribution through the AdServices framework does not require ATT consent [Official].

## 3. Account structure (the standard four plus placements)

| Campaign | Match and keywords | Purpose | Bidding |
|----------|-------------------|---------|---------|
| BRAND | Exact: your brand and misspellings | Protect brand and capture navigational intent | Max CPT near the low end of suggested range; test incrementality |
| CATEGORY (generic) | Exact: category and feature terms proven in Discovery | Main volume engine | Max CPT by keyword, or Maximize Conversions once volume allows |
| COMPETITOR | Exact: competitor brand terms | Conquest | Lower bids, tight CPA guardrails, competitor specific CPP |
| DISCOVERY | Ad group A: broad match versions of category terms. Ad group B: Search Match on, no keywords | Find new terms | Lower bids; harvest weekly |
| TODAY TAB | Placement campaign, CPP required in practice | Launches, seasonal moments, brand reach | Max CPT; judge on downstream installs and lift |
| SEARCH TAB | Placement campaign | Cheap incremental reach; low tap-through rate | Max CPT; strict CPA |
| PRODUCT PAGES | Placement campaign | Users browsing similar apps | Max CPT; strict CPA |

Rules:
- One country or region group per campaign when economics differ; one device family where iPad behaves differently.
- Cross-negatives: add every exact keyword running in BRAND, CATEGORY and COMPETITOR as an exact negative in DISCOVERY, and brand terms as negatives in CATEGORY and COMPETITOR. This keeps each query in one campaign.
- Search Match only in DISCOVERY (it is on by default in new ad groups; turn it off elsewhere).
- Ad groups by theme (5 to 30 keywords), each mapped to a custom product page ad variation.
- Naming: `AA_<CC>_<PLACEMENT>_<TYPE>_<THEME>_<BID>` for example `AA_US_SR_CATEGORY_budgeting_MAXCPT`.

## 4. Keywords, match types and search terms

- Match types: exact and broad, plus Search Match (automatic matching from your metadata and category) [Official].
- Negatives: exact or broad at campaign or ad group level.
- Harvest weekly from DISCOVERY search terms:
  - Promote: at least 5 installs (or 2 trials or 1 payer for deep funnel apps) at or below target CPA in 14 days, add as exact to CATEGORY or COMPETITOR and as exact negative in DISCOVERY.
  - Negate: at least 30 taps and zero installs, or CPA above 2x target with at least 10 installs, or irrelevant.
- Search popularity (1 to 5) and Search Popularity data in the Platform API help prioritize [Official, secondary for API field].
- Competitor brand keywords: allowed in Apple Ads keywords but subject to Apple's trademark complaint process; never put competitor names in metadata. Use a competitor specific CPP that compares fairly and only with claims in brand/CLAIMS.md.

## 5. Bidding

### 5.1 Manual Max CPT

- Start at the middle of Apple's suggested bid range for CATEGORY, low end for BRAND, below middle for COMPETITOR and DISCOVERY.
- Change bids every 3 to 7 days, by 10% to 20% per change, on keywords with at least 20 taps in the window.
- Bid formula from target CPA: max CPT = target CPA x tap to install rate (keyword level). With target CPA (install) $3.00 and 55% conversion rate, max CPT about $1.65. For deep funnel targets: max CPT = target cost per trial start x tap to install rate x install to trial rate.
- Watch impression share and rank for top keywords (Custom Reports or API). Low share with good CPA means room to bid up.

### 5.2 Maximize Conversions (search results only)

| Setting or behavior | Detail | Evidence |
|---------------------|--------|----------|
| Inputs | Target CPA and daily budget | [Official, 2026] |
| Optimization event | Installs (downloads) only today; no trial, purchase or retention signal | [Practitioner consensus, 2026] |
| Target behavior | Weekly average, not a per install cap; Apple bids above the target where it expects a conversion; daily CPA drifts | [Official] |
| Ad groups | Apple creates a locked Automated ad group with Search Match on (cannot be edited, but search terms are visible); a manual ad group can run alongside and negatives still apply | [Practitioner consensus, 2026] |
| Budget | Enough for at least 5 conversions per day | [Official best practices] |
| Changes | Let it run at least 2 weeks before adjusting target CPA; changes during learning reset it | [Official + Practitioner] |
| CPA caps | Being phased out ("will soon be unavailable") | [Official] |

When to use: CATEGORY campaigns with at least 5 installs per day at a stable CPA, where install quality is uniform across terms. When not to: deep funnel apps where install quality varies sharply by keyword (it will chase cheap installs); keep manual bids on those keywords and judge on cost per trial or payer from the MMP.

## 6. Creative: custom product pages and new assets

- Each ad group can use the default product page or a custom product page as its ad variation [Official]. CPPs work in search results, Search tab and Today tab [Official].
- New creative assets (images and videos for headers and search results) can appear in Apple Ads on the Today tab and in search, managed through the App Store Connect Asset Library, which supports pre-approval for future campaigns [Official, 2026-06 WWDC26 guide; shipped in App Store Connect 2026-10-05]. One source says Apple Ads custom creative is not yet part of the release [Contested]; check the Apple Ads UI.
- Match the CPP to the ad group theme (see [Experiments and custom pages](store-listing-experiments-and-custom-pages.md)).

## 7. Audiences and settings

| Setting | Use |
|---------|-----|
| Customer type: all users, new users, returning users, users of my other apps | New users for acquisition; returning users for win-back with a lapsed user CPP |
| Age range and gender | Avoid unless legally required; shrinks reach and only applies where Apple has the data |
| Locations | Country or region; city level only for local apps |
| Devices | iPhone vs iPad split when economics differ |
| Ad scheduling | Dayparting only with 4+ weeks of hourly data showing a CPA gap above 30% |

## 8. Measurement

- AdServices framework: the app requests an attribution token and sends it to Apple's Attribution API (directly or through the MMP) to get campaign, ad group, keyword and ad IDs for installs from Apple Ads, without ATT [Official].
- MMP integration: AppsFlyer, Adjust, Branch, Singular, Kochava and others ingest Apple Ads attribution and cost.
- Apple Ads registered with AdAttributionKit in 2025-04 (starting with SKAdNetwork versions 1 to 3 interoperability) [Practitioner consensus via Singular].
- RevenueCat and similar tools join Apple Ads attribution to subscription revenue, which is the cleanest way to judge keywords on cost per payer.
- Organic cannibalization: brand and some category keywords capture users who would have installed anyway. Run a brand incrementality test (section 11) before celebrating brand ROAS.

## 9. Weekly optimization loop (45 to 60 minutes)

1. Data: Apple Ads report (or Platform API pull) for the last 7 and 28 days, joined with MMP or RevenueCat downstream metrics by keyword.
2. Pacing: spend vs budget per campaign; campaigns capped by budget with CPA below target are the first candidates for budget increases.
3. Search terms: promote and negate (section 4).
4. Bids: adjust keywords with enough taps; pause keywords with CPA above 2x target and at least 10 installs or 0 installs after 50 taps.
5. Downstream: rank keywords by cost per trial start and cost per payer, not CPI. Cut keywords that install cheaply but never convert.
6. Impression share: top 20 keywords; flag where competitors outbid you.
7. CPP performance: conversion by ad variation; swap losers.
8. Write the change list (approval required) and a journal entry.

## 10. Benchmarks (2025 data, directional)

| Metric | Value | Source |
|--------|-------|--------|
| Search results TTR, all categories | 9.7% | SplitMetrics 2026 report on 2025 data [Study, 2026] |
| Average CPT, top 15 categories | $2.25 (Sports $14.41, Finance $6.06, Medical $4.45) | SplitMetrics [Study, 2026] |
| Average CPA (install) | $3.76 (SplitMetrics); $2.51 (MobileAction, from $2.76 in 2024) | [Study, 2026] |
| CPT by quarter | Low $1.26 in Q2, $1.88 in Q4 2025 | MobileAction [Study, 2026] |
| Median CPT | $0.92 global, $1.91 US | AppTweak [Study, 2026] |
| Conversion rate (tap to install) | 56% global median (AppTweak); 62% (Adapty, 90 countries) | [Study, 2026] |
| Search tab vs search results TTR | 0.29% vs 7.40% global | AppTweak via Sonar [Study, 2026] |
| US CPT, April to June 2026 | Health and Fitness about $1.50, Games $3.02, Finance $3.80, Sports about $16.96 | SplitMetrics [Study, 2026-07] |
| After multiple ad slots (2026-03) | Discovery campaigns gained the most reach; CPT fell for brand, generic and competitor campaigns | AppTweak [Study, 2026] |

Caveat: medians vs averages, US vs global and category mix explain most of the spread. Compare with the account's own history first.

## 11. Plays

### Launch (week 0 to 4)
1. Prerequisites: AdServices attribution live through the MMP or RevenueCat; target CPA from [Unit economics](app-growth-model-and-unit-economics.md); 2 to 4 CPPs ready.
2. Build BRAND, CATEGORY (20 to 50 exact terms from ASO research), COMPETITOR (top 5 to 10 competitors, if the human approves), DISCOVERY (broad + Search Match). All created PAUSED (G2).
3. Budgets: CATEGORY 50% to 60%, DISCOVERY 15% to 20%, BRAND 10% to 15%, COMPETITOR 10% to 15%.
4. Activate after approval (G3). Daily checks for 7 days: spend, taps, installs, zero install keywords.
5. Week 2: first harvest; week 3: bid adjustments; week 4: consider Maximize Conversions on CATEGORY if at least 5 installs per day.

### Scale
1. Raise budgets on capped campaigns with CPA under target by 20% to 30% per week.
2. Expand CATEGORY with harvested terms; add countries ranked by ASO opportunity and price points.
3. Test Today tab with a seasonal CPP and a holdout read (installs in test countries vs control trend).
4. Add Search tab and product page campaigns with strict CPA rules.

### Recover (CPA up 30% or more week over week)
1. Check tracking first: AdServices token flow, MMP integration status, app version release dates.
2. Check auction: impression share, CPT trend, new competitors on key terms, multiple ad slots effects.
3. Check page: conversion rate drop after a metadata or screenshot change, rating drop, price change.
4. Fix the cause; do not cut bids across the board.

### Brand incrementality test
1. Pick 2 to 4 comparable countries or alternate weeks.
2. Pause BRAND in the test cells for 2 to 3 weeks (G3 approval).
3. Compare total brand query installs (paid + organic) vs control. If total installs drop less than paid brand installs, the difference was cannibalized.
4. Keep BRAND on where competitors bid on your brand or where the test shows lift.

## 12. API and automation

- Apple Ads Platform API (launched 2026-08, base `api.ads.apple.com/v1` per third-party guides, covers App Store and Apple Maps ads, adds Insights, ad position reporting, Search Popularity and Change History) [Official launch; endpoint details Unverified].
- Campaign Management API v5 stops working on 2027-01-26 [Official, 2026-04]. Any script, connector or MCP server built on v5 must migrate; some vendors list 2026-12-26 as their own cutoff [Contested].
- OAuth client credentials with the `searchadsorg` scope and an `X-AP-Context` header carrying the ad account ID are reported as unchanged [Unverified].
- See [Tools, API and MCP](tools-api-mcp.md) for MCP servers and read-only setup.
