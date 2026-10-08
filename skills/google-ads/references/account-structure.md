# Account Structure

> Knowledge as of 2026-10. Limits and defaults change often. Verify any limit in Google Ads Help before building, and run the Freshness Protocol in SKILL.md.

Structure decides how much signal each bid strategy gets, what you can control, and what you can measure. In 2026 Google's automation (Smart Bidding, AI Max, Performance Max, Demand Gen) learns per bid strategy, per conversion goal and per asset set. Every split you add divides that signal. Every split you remove takes away a control. Build the smallest structure that still gives you the controls and the reporting you actually use.

## 1. Principles

1. Signal density first. A campaign that cannot reach roughly 30 primary conversions in 30 days per bid strategy will bid noisily. Pool campaigns under a portfolio bid strategy or consolidate before you add more splits. [Practitioner consensus]
2. Segment only for a reason on the list in section 3. "It looks tidier" and "one campaign per product category" are not reasons.
3. Separate brand from non-brand everywhere it can leak: Search, Performance Max (brand exclusions), AI Max (brand exclusions), Shopping (negatives or brand exclusions). Blended brand and non-brand reporting hides the true cost of new demand.
4. Separate economics, not taxonomies. Split by margin band, target, geography with different unit economics, or customer type (new vs returning). Do not split by product category if the categories share the same target.
5. One goal per campaign. A campaign optimizes to the conversion goals it is set to use. Mixing a 2 dollar newsletter signup with a 2,000 dollar purchase in one goal teaches the bidder to buy signups.
6. Keep a control structure for testing. Leave room for experiment cells (custom experiments, AI Max experiments, PMax uplift experiments) without rebuilding the account.
7. Name everything so a script or a human can parse it. Naming conventions are a data model.

## 2. Data thresholds per bid strategy

| Bid strategy | Google stated requirement | Practitioner floor for stable results | Notes |
|---|---|---|---|
| Manual CPC | None | n/a | Enhanced CPC was removed for Search and Display; campaigns that used it now run as Manual CPC [Official, 2024-10 announcement, effective 2025-03] |
| Maximize clicks | None | n/a | Use for brand defense with a max CPC cap, new keyword discovery with no tracking, or traffic goals |
| Target impression share | None | n/a | Brand Search only. Set a max CPC limit. Never on non-brand |
| Maximize conversions (no target) | Conversion tracking active | 15+ conversions in 30 days | Spends the full budget. Use for launch or when budget is the binding constraint |
| Maximize conversions with target CPA | No hard minimum in current docs | 30+ conversions in 30 days per strategy [Practitioner consensus] | Portfolio strategies pool conversions across campaigns |
| Maximize conversion value (no target) | Conversion values present | 30+ conversions with value | Spends the full budget toward value |
| Maximize conversion value with target ROAS | Historically 15 conversions in 30 days for Search | 50+ conversions in 30 days, values that actually vary [Practitioner consensus] | Fixed values (every lead = 100) make tROAS a slower tCPA |
| Performance Max | Conversion tracking active | 30+ conversions per campaign per month; 50+ for tROAS [Practitioner consensus] | Below that, run one PMax campaign, not several |
| Demand Gen | Conversion tracking active | Budget at least 15x target CPA per day, judge after about 50 conversions [Practitioner consensus based on Google guidance] | Learning is slower than Search |
| App campaigns (installs) | Firebase or MMP linked | Daily budget at least 50x target CPI [Official guidance, verify] | Separate iOS and Android |
| App campaigns (in-app actions) | 10+ in-app conversions a day recommended | Daily budget at least 10x target CPA [Official guidance, verify] | Move to tROAS only with purchase values |

Learning period: Google updated its guidance in 2026-09 to "up to around 50 conversion events or 3 conversion cycles" on the UK English help page, while the US English page still said 1 to 2 conversion cycles [Contested, 2026-09: regional versions of the same help page differ]. Plan 2 to 3 weeks (or 50 conversions) before judging any bid strategy change, longer for long conversion lags.

## 3. When to segment (the only valid reasons)

| Reason | Example | Split into |
|---|---|---|
| Different conversion goal | Lead gen for two service lines with different qualified lead definitions | Separate campaigns with campaign-specific goals |
| Different target (CPA or ROAS differs by 30% or more) | 20% margin category vs 60% margin category | Separate campaigns or PMax by custom label margin band |
| Budget that must be protected | Brand, hero products, a new market with a fixed test budget | Separate campaign, own budget |
| Different geo with different economics, language, legal or landing pages | US vs DE, or a regulated state | Separate campaigns per market |
| Different creative or landing experience that needs its own asset set | B2B enterprise page vs SMB self-serve page | Separate ad groups (Search) or asset groups (PMax) |
| Measurement need | Brand vs non-brand reporting, incrementality test cell, competitor terms | Separate campaigns with labels |
| Network or format control | Demand Gen Maps only, YouTube only, Shopping only feed campaign | Separate campaign or ad group with channel controls |

When none of these applies, consolidate.

## 4. When to consolidate

Consolidate when two or more of these are true:
- A campaign has fewer than 30 conversions in 30 days and shares its target with another campaign.
- Ad groups split only by match type (legacy SKAG or match type silos).
- The same keyword or theme exists in several campaigns and they compete (check the search terms report for the same query served by multiple campaigns).
- Campaigns are limited by budget individually while the account as a whole is not.
- Several PMax campaigns share the same goal, the same target and the same feed and each has under 30 conversions a month.

Consolidation method: move keywords into the surviving campaign, keep the campaign with the longest clean conversion history, use a portfolio strategy if the old campaigns must survive for reporting, and expect 1 to 3 weeks of learning.

## 5. Segmentation decision tree

1. Is conversion tracking verified and the primary goal correct? If no, stop and fix tracking first (see [conversion tracking](conversion-tracking-and-value.md)).
2. Is the term brand? Yes: Brand Search campaign, exact and phrase, target impression share or Maximize clicks with a CPC cap, or tCPA if brand is expensive. Add the brand list as an exclusion on PMax and AI Max campaigns.
3. Does the product, service or audience have a different target or goal? Yes: new campaign. No: go to 4.
4. Does it need a different landing page or message? Yes: new ad group (Search) or asset group (PMax). No: add keywords or search themes to the existing group.
5. Will the new campaign reach 30 conversions in 30 days? No: use a portfolio bid strategy shared with sibling campaigns, or do not split.
6. Is the budget limited (Search lost IS budget above 10%) on a profitable campaign? Fix budget before adding more campaigns.

## 6. Naming convention

Use a fixed, parseable pattern. Scripts and GAQL `LIKE` filters depend on it.

```
{Market}_{Lang}_{Channel}_{Intent}_{Theme}_{Bid}_{Version}
US_EN_SRCH_BR_Brand-Core_tIS_v1
US_EN_SRCH_NB_Running-Shoes_tROAS_v3
US_EN_SRCH_COMP_Competitors_tCPA_v1
US_EN_PMAX_NB_Margin-High_tROAS_v2
US_EN_SHOP_NB_Catchall-LowData_MaxClicks_v1
US_EN_DGEN_NEW_Video-Lookalike-Signals_tCPA_v1
US_EN_APP_ACI_iOS_tCPI_v1
```

Codes: SRCH Search, PMAX Performance Max, SHOP Standard Shopping, DGEN Demand Gen, VID YouTube video campaigns, DISP Display, APP App. Intent: BR brand, NB non-brand, COMP competitor, RMK remarketing, NEW new customer acquisition. Ad groups: `{Theme}_{Subtheme}`. Asset groups: `{Category or Audience}_{Angle}`.

Labels (apply to campaigns): `brand`, `nonbrand`, `competitor`, `test_cell_A`, `test_cell_B`, `ai_max_on`, `auto_migrated_ai_max_2026-09`, `do_not_touch` (for campaigns under a lift study).

## 7. Templates by business model and tier

Tiers: Starter under 3k USD a month, Growth 3k to 30k, Scale 30k to 300k, Enterprise over 300k.

### 7.1 Ecommerce

| Tier | Structure | Bidding | Notes |
|---|---|---|---|
| Starter | 1 Brand Search (exact and phrase). 1 PMax with feed for top sellers (or Standard Shopping if under 30 conversions a month). Brand exclusion on PMax | Brand: Max clicks with CPC cap. PMax: Maximize conversion value, no target for 3 to 4 weeks, then tROAS | Do not run Demand Gen or YouTube yet. Feed quality is the lever, hand off to commerce-feeds |
| Growth | Brand Search. Non-brand Search by category intent (broad match with tROAS, or phrase and exact if under 30 conversions). PMax split into 2 or 3 campaigns by margin band custom label. Standard Shopping catch-all for low data or new products. Demand Gen once PMax and Search are stable | tROAS per margin band (see bidding module formulas) | Test AI Max on non-brand Search with an AI Max experiment. Use NCA goal if new customers matter |
| Scale | Add competitor Search, PMax per major category or margin band with new customer acquisition, Demand Gen and YouTube for demand creation with lift studies, AI Max on non-brand Search, market splits | Portfolio tROAS by margin band, seasonality adjustments for sales | Run brand and PMax incrementality tests yearly |
| Enterprise | MCC per region, campaigns per market and language, feed labels per market in Merchant Center, profit based values (POAS), Meridian or another MMM | Value rules plus profit values, portfolio strategies | Change governance and API automation required |

PMax margin band pattern: custom_label_0 = margin band (high, mid, low), custom_label_1 = performance tier (hero, sidekick, villain, zombie). One PMax per margin band with its own tROAS. Zombies (no impressions in 30 days) go to a separate low target campaign or Standard Shopping to force exposure.

### 7.2 Lead generation (services, finance, education, home services)

| Tier | Structure | Bidding | Notes |
|---|---|---|---|
| Starter | Brand Search. 1 or 2 non-brand Search campaigns by service line, phrase and exact match, ad groups by intent theme. Call assets, location assets | Maximize conversions once at least 15 qualified leads a month are tracked. Otherwise Manual CPC or Max clicks with a cap | No PMax until offline conversion import (OCI) or strong spam filtering exists. PMax lead gen without qualification feedback tends to buy junk leads [Practitioner consensus] |
| Growth | Non-brand Search per service line with broad match plus tCPA once at least 30 qualified conversions a month. OCI with qualified lead as primary. PMax for leads only with OCI and customer list exclusions. Local Services Ads if eligible | tCPA on qualified lead, or Maximize conversion value with stage values | Lead form asset test in Search |
| Scale | Value-based bidding on stage values (lead, MQL, SQL, won). Journey aware bidding if accepted into the beta (Search tCPA, announced 2026-05-07, gated to accounts with OCI or enhanced conversions for leads) [Official via trade press, 2026-05]. Demand Gen for retargeting and lookalike signals. Geo campaigns by service area economics | tROAS on predicted lead value | Lead quality reporting from CRM weekly |
| Enterprise | Separate campaigns per region and product line, CRM integration through Data Manager, call tracking with qualified call import | Portfolio tROAS | Incrementality tests per region |

### 7.3 B2B SaaS

- Brand Search, separate and cheap.
- Competitor Search, separate budget and separate target (expect CPA 1.5x to 3x non-brand) [Practitioner consensus].
- High-intent non-brand: "software", "tool", "platform", "pricing", "alternative to", "vs" queries.
- Problem and category non-brand: broad match only once the account has 30+ SQL or trial-qualified conversions a month.
- Remarketing and account lists: Demand Gen and YouTube with Customer Match of target accounts and pipeline contacts.
- Primary conversion: SQL or qualified trial (product qualified lead) imported offline. Secondary: demo request, signup.
- Exclude: job seekers ("jobs", "salary", "careers", "login", "download free" if not product-led), existing customers (Customer Match exclusion), students.
- PMax: only after 50+ qualified conversions a month and with OCI. Use brand exclusions and customer list exclusions.

### 7.4 Local services and multi-location

- Search per service, radius or ZIP targeting matching the service area, location option "Presence".
- Local Services Ads (LSA) for eligible categories. LSA campaigns migrate automatically into a specialized PMax campaign type with pay-per-lead goals inside Google Ads: select US home and storefront categories from 2026-08, more in late 2026, non-US through 2027 [Official, Google Ads Help, 2026-08]. Export LSA history before the migration date.
- Call assets with call reporting, ad schedule matching opening hours, call conversions with a minimum duration matched to a real lead (default 60 seconds).
- Book button (partner bookings through Reserve with Google) now shows on Search and PMax ads for eligible merchants automatically; opt out in Google Ads; add the "Appointments booked" goal to campaigns to bid on it [Official, Google Ads Help "About partner bookings", 2026-09]. Healthcare is excluded.
- PMax with store goals for retail with physical stores and store visit data.
- Demand Gen with the Maps channel (requires location assets) for local awareness [Official beta, 2026].
- Multi-location: one campaign per region with a location group, or one campaign per location only if each has its own budget owner.

### 7.5 App

- App campaigns for installs (ACi), split by OS. iOS measurement through SKAdNetwork and on-device measurement; Android through Firebase or an MMP.
- Bid ladder: tCPI until 10+ in-app conversions a day, then tCPA on the key in-app event, then tROAS when purchase values flow.
- App campaigns for engagement (ACe) for lapsed users, with deep links.
- App pre-registration for Android launches.
- Brand Search for the app name if competitors bid on it.
- Web to app: send web traffic to app where the app converts better, with deep links.

### 7.6 Marketplace or content publisher

- Two-sided marketplace: separate supply (sellers, hosts, drivers) and demand (buyers) campaigns with separate conversion goals. Never mix both goals in one campaign.
- Long tail inventory: AI Max (or legacy DSA until it migrates) with page feeds and URL inclusions for category and listing pages. Use URL exclusions for help, blog, careers, login.
- Publishers monetizing traffic: check the Google Ads policies on destination requirements (insufficient original content) and the arbitrage policy before buying traffic. Value per session must be computed from real revenue data. Treat this as high policy risk.

## 8. Account and MCC hygiene

- One manager account (MCC) owned by the business, with the agency MCC linked as a sub-manager. Never let an agency own the only admin access.
- Users: Admin only for the owner and 1 or 2 senior operators. Standard for operators. Read only for analysts and Claude connectors unless writes are approved.
- 2-step verification on all users with access to the account.
- Auto-tagging on. Tracking template and final URL suffix at account level for UTMs.
- Account-level settings to review: auto-applied recommendations, account-level automated assets (Automated promotions turns on by default from 2026-10-12 for Search and PMax campaigns with location assets and no manual promotions [Official notice quoted by Search Engine Roundtable, 2026-10-05]), brand lists, account-level negative keyword list, conversion goals, customer data terms, Customer Match acceptance.
- Billing: monthly invoicing for large spenders, backup payment method for card billing.

## 9. Worked example: consolidating an over-split ecommerce account

Situation: 14 Search campaigns (one per category), each Max conversion value with tROAS 400%, each 5 to 20 conversions a month, 6 PMax campaigns each 10 to 25 conversions a month, 1 brand campaign. Total 240 conversions a month.

Plan:
1. Keep Brand Search as is.
2. Merge 14 Search campaigns into 3 by margin band. Each now receives 40 to 70 conversions a month. Ad groups keep the category themes.
3. Merge 6 PMax into 2 (high margin, mid and low margin) by custom_label_0. Each gets 50 to 80 conversions a month. Add brand exclusions.
4. Use a portfolio tROAS per margin band so Search and Shopping style campaigns with the same target share learning, if bid limits are needed.
5. Run the change on a Monday, outside promotions, annotate it in the journal, and do not change targets for 14 days.
6. Success metric: conversion value at the same or better ROAS after 4 weeks, compared to the 4 weeks before, adjusted for seasonality using last year's same period.

## 10. Structure audit questions

| Question | Healthy answer |
|---|---|
| Can you report brand and non-brand cost and conversions separately in under 2 minutes? | Yes, by label or naming |
| Does any bid strategy have fewer than 15 conversions in 30 days? | No, or it is pooled in a portfolio |
| Does any query trigger ads in 3 or more campaigns? | No |
| Is each campaign's goal the business outcome (sale, qualified lead) and not a micro conversion? | Yes |
| Is there a protected budget for brand? | Yes |
| Are test cells labeled and documented in EXPERIMENTS.md? | Yes |
| Are PMax and AI Max campaigns excluding the brand list? | Yes, unless brand is intentionally included |
