# Performance Max

> Knowledge as of 2026-10. PMax gained more controls and reporting between January 2025 and October 2026 than in its first three years. Verify limits and alpha or beta status in Google Ads Help before acting.

## 1. What PMax is and when to use it

Performance Max is a goal-based campaign that serves across Search, Shopping, YouTube, Display, Discover, Gmail and Maps from one budget and one bid strategy, using asset groups, an optional product feed, audience signals and search themes.

Use PMax when:
- Ecommerce with a Merchant Center feed and at least 30 conversions a month in the account.
- Local businesses with store goals or location-based conversions.
- Lead gen only with offline conversion import (qualified lead or sale as primary) and customer list exclusions. Without that, PMax tends to find cheap, low quality leads (form spam, bots, accidental submissions). [Practitioner consensus]
- Accounts that want reach beyond Search with one budget and do not have the resources to run Demand Gen, YouTube and Display separately.

Do not use PMax as the first campaign for: a brand new account without conversion history, lead gen without qualification feedback, regulated categories where generated assets or placements are a compliance risk, or when the business needs strict query control.

## 2. Timeline of controls and reporting (2025 to 2026)

| Date | Change | Label |
|---|---|---|
| 2024-10 | PMax no longer automatically takes priority over Standard Shopping for the same products. Ad Rank decides | [Official, 2024] |
| 2025-01 | PMax features for 2025 announced, including campaign-level negative keywords in the UI and more controls | [Official, 2025-01] |
| 2025-03 | Negative keyword limit raised to 10,000 per PMax campaign, applies to Search and Shopping inventory | [Official, 2025] |
| 2025-04-30 | Channel performance reporting, search terms reporting and expanded asset reporting announced | [Official, 2025-04] |
| 2025-08 | Shared negative keyword lists for PMax fully rolled out | [Practitioner report, 2025-08] |
| 2025-11 | Channel performance report available in all PMax campaigns, also through manager accounts | [Official, 2025] |
| 2026-05 | Google Ads API v24.2 adds `ad_network_type` segmentation for PMax placement reporting | [Practitioner report, 2026-05] |
| 2026-06 (mid) | Smart Bidding Exploration out of beta for PMax without product feeds. Promotion mode beta for Search and PMax with Target ROAS | [Official announcement and Ads Liaison, reported by Search Engine Land, 2026-06] |
| 2026-06-15 | Product reporting in the API (shopping_performance_view) starts including data from all PMax networks, not only Shopping inventory | [Official, Google Ads Developer Blog 2026-04] |
| 2026-07 | "Partners" alpha test lets some advertisers exclude Search Partners and Display inventory from PMax | [Practitioner report, Digiday 2026-07] |
| 2026-08 | Channel prioritization alpha: a "Channels" setting with a Lower, Auto or Higher control per channel (Search, Search Partners, Discover, YouTube, Maps, Gmail, Display). Higher loosens the CPA or ROAS tolerance for that channel, Lower tightens it. It is not a budget split. Allowlisted accounts only, access through a Google rep; no Google announcement, beta or GA date as of 2026-10 | [Practitioner reports, Search Engine Land and Search Engine Roundtable, 2026-08 to 2026-09] |
| 2026-08 onward | Local Services Ads migrate to a specialized PMax campaign type with pay-per-lead goals, starting with select US home and storefront categories | [Official, Google Ads Help, 2026-08] |
| 2026-09 | Language setting no longer applies to PMax ads on the Search Network (other channels still use it) | [Official, 2026-09] |
| 2026-09-15 | New campaign setting "Where should people go after clicking your ads?" | [Practitioner report, Search Engine Roundtable 2026-09] |
| 2026-09-23 | API v25.2: create PMax drafts from Smart campaigns, asset group tracking templates and URL parameters, segments for product data and video usage | [Official via trade press, 2026-09] |
| 2026-10-02 | A/B asset experiments for asset groups rolling out to all advertisers (beta since 2025); MCC and API support to follow in the coming weeks | [Practitioner report, Search Engine Land 2026-10-02; earlier beta in Google Ads Help] |
| 2026-10-12 | Automated promotions (offers pulled from your site) on by default for eligible Search and PMax campaigns with location assets and no manual promotion assets | [Official notice quoted by Search Engine Roundtable, 2026-10-05] |

## 3. Campaign setup decisions

| Decision | Recommended default | Notes |
|---|---|---|
| Goal | Sales or Leads with campaign-specific goal = the one primary business conversion | Do not include micro conversions |
| Bidding | Maximize conversion value (ecommerce) or Maximize conversions (lead gen), no target for the first 2 to 4 weeks, then add tROAS or tCPA at about the observed level | Set the target at observed performance, then tighten 10% to 15% every 2 weeks |
| Customer acquisition | "Bid higher for new customers" with a realistic new customer value, or "Only bid for new customers" when retention is handled elsewhere | Requires customer lists or conversion-based new customer detection; see bidding module |
| Feed | Link Merchant Center; use listing groups to include or exclude products | Feed quality is the strongest lever for Shopping traffic; hand off feed work to commerce-feeds |
| Final URL expansion | Off for lead gen and when landing pages must be controlled. On for ecommerce with URL exclusions | Exclude blog, careers, account, policy and support pages |
| Brand exclusions | Add your brand list unless PMax is meant to serve brand | Brand exclusions apply to Search and Shopping inventory |
| Negative keywords | Shared lists plus campaign negatives (up to 10,000) | Search and Shopping inventory only |
| Account-level negatives | Brand safety terms | Applies across Search, Shopping and PMax |
| Locations | Presence for local, lead gen, shipping-limited | Same as Search |
| Device and age exclusions | Use only with evidence or legal need | PMax supports device targeting and age exclusions since 2025 [Official, 2025] |
| Placement exclusions | Account-level placement exclusion list (apps, kids content, low quality sites) | Applies to Display and YouTube inventory |
| Auto-generated assets | Review video and image enhancements; turn off if quality is poor | Brand guidelines (colors, fonts) can steer generation |

## 4. Asset groups

Specs (verify current limits) [Official]:
| Asset | Count | Length |
|---|---|---|
| Headlines | 3 to 15 | 30 characters |
| Long headlines | 1 to 5 | 90 characters |
| Descriptions | 2 to 5 (one up to 60 characters) | 90 characters |
| Images | up to 20 (landscape 1.91:1, square 1:1, portrait 4:5) | |
| Logos | up to 5 (square 1:1, landscape 4:1) | |
| Videos | up to 5 (horizontal, vertical, square; at least 10 seconds) | If none, Google may generate videos |
| Business name | 1 | 25 characters |
| Search themes | up to 50 per asset group [Practitioner consensus, verify current limit] | |
| Audience signal | 1 per asset group | |

Asset group strategy:
- One asset group per distinct offer, product category with a distinct message, or audience with a distinct message. Not one per product.
- Feed-led ecommerce: asset groups by category with listing groups matching the category, plus creative per category.
- Each asset group needs real video (horizontal and vertical) to avoid low quality auto-generated videos on YouTube. [Practitioner consensus]
- Refresh: replace assets with low performance after at least 5,000 impressions, and add new creative monthly at Scale tier.

## 5. Search themes and audience signals

- Search themes tell PMax about queries it might not find from your assets and feed. They are signals, not keywords. Search themes compete with Search keywords under the same prioritization rules as broad match: an identical Search keyword wins. [Official]
- Add 10 to 25 themes per asset group drawn from converting Search queries and category language. Do not add brand themes to a non-brand PMax.
- Audience signals are starting points, not targeting. Best signals: Customer Match lists (purchasers, high value customers), your website visitors who converted, custom segments built from converting search terms and competitor URLs. Weak signals: broad affinity audiences.
- Signals matter most in the first weeks and at low data levels.

## 6. Reporting you must use

| Report | Path | What to do with it |
|---|---|---|
| Channel performance | Insights and reports, Channel performance (or campaign level) | See cost, conversions and value by Search, Shopping, YouTube, Display, Discover, Gmail, Maps. Flag if Display or YouTube take over 30% of spend with weak conversion value |
| Search terms | Insights and reports, Search terms | Same granularity as Search campaigns, with a source column showing keywordless targeting vs search themes. Privacy thresholds apply [Official, 2025] |
| Search term insights (categories) | Insights | Category level trends |
| Asset reporting | Asset group, Assets | Conversions and value per asset (2025). Performance labels (Low, Good, Best) were deprecated in 2025; judge on metrics [Practitioner report, 2025-05; label field absent from API v23 to v25] |
| Placements | Report editor, Performance Max placements | Where Display and YouTube ads served (impressions), build exclusion lists |
| Listing groups and products | Listing groups, Products | Spend concentration, zombie products |
| Auction insights | Campaign | Competitors on Search and Shopping inventory |
| Experiments | Experiments | PMax uplift and asset experiments |

GAQL for these is in [GAQL and scripts](gaql-and-scripts.md): queries for PMax channel split, asset performance, placements and search term insights.

## 7. Cannibalization and overlap

Risks:
1. Brand: PMax buys branded queries and reports them as PMax conversions. Fix: brand exclusions plus a separate brand Search campaign. Verify in the PMax search terms report.
2. Remarketing: PMax shows ads to people who would convert anyway (cart abandoners, existing customers). Fix: new customer acquisition goal, customer list exclusions where available, and incrementality tests.
3. Search: PMax and non-brand Search compete for the same queries. Identical keywords win for Search. Otherwise Ad Rank decides. Check search terms in both campaigns for overlap.
4. Standard Shopping: since 2024 both compete on Ad Rank. Use Standard Shopping only for a defined job (low data products, a separate target, a test).

Check: compare total account conversions, not only PMax conversions, before and after any PMax launch or scale. A PMax launch that reports 100 conversions while account total rises by 30 means 70 were moved, not created.

## 8. Optimization procedure (bi-weekly)

1. Pull channel performance, last 28 days vs previous 28. Note channel mix shifts.
2. Search terms: add negatives for irrelevant terms above 1x target CPA with no conversions. Check brand leakage.
3. Asset report: replace assets with weak performance and at least 5,000 impressions. Add a new angle every month.
4. Products: identify zombies (no impressions in 30 days) and villains (spend above 2x target CPA with no conversions). Move zombies to a separate campaign with a lower target or Standard Shopping; tighten or exclude villains. Hand off feed fixes (titles, images, prices) to commerce-feeds.
5. Placements: exclude low quality apps and sites in the account-level exclusion list.
6. Targets: if the campaign spends under 80% of budget and beats target by 15% or more, loosen the target 10% to scale. If it misses target by 15% or more for 2 weeks, tighten 10%.
7. Log changes and results in the journal.

## 9. PMax by business model

| Model | Pattern |
|---|---|
| Ecommerce Starter | 1 PMax with feed for top sellers, brand exclusion, Maximize conversion value |
| Ecommerce Growth and Scale | 2 to 4 PMax by margin band or category with distinct targets, NCA goal, one campaign for zombies or new products |
| Feed-only PMax | PMax with only the feed and minimal assets to concentrate on Shopping inventory [Contested: some practitioners report better ROAS and control, Google recommends full assets; test it] |
| Lead gen | One PMax with OCI qualified lead as the goal, customer list exclusion, URL expansion off, strong forms with spam protection |
| Local and multi-location | PMax with store goals or local actions, location assets, Book button where eligible |
| B2B SaaS | Rarely. Only with 50+ qualified conversions a month and OCI |
| App | Use App campaigns, not PMax |

## 10. Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---|---|---|---|
| ROAS strong but account revenue flat | Brand and remarketing cannibalization | Search terms (brand share), new vs returning customer split, account total conversions | Brand exclusions, NCA goal, holdout test |
| Spend shifts to Display or YouTube with low value | Weak feed, few conversions, auto videos, broad signals | Channel performance report, placements | Better video, placement exclusions, feed fixes, test channel sliders if in alpha |
| Few products get all spend | Algorithm concentrates on proven products | Products report | Split campaigns by performance tier with separate targets |
| Lead volume up, sales flat | Optimizing to raw leads, spam | CRM qualification rate by campaign | OCI with qualified stage as primary, form validation |
| Sudden drop | Tracking break, feed disapprovals, budget or target change, policy | Conversion diagnostics, Merchant Center diagnostics, change history | Fix root cause, apply data exclusion for tracking outages |
| Learning never ends | Frequent changes, too little data | Change history, conversions per month | Fewer edits, consolidate, raise budget or loosen target |

## 11. PMax experiments

- PMax uplift experiment: measures the incremental effect of adding PMax to an account with Search or Shopping.
- Asset experiments (A/B for asset groups): test new headlines, descriptions, images or videos against the current set in one asset group. Rolling out to all advertisers from 2026-10-02 after a beta that started in 2025 [Practitioner report, Search Engine Land 2026-10-02; Google Ads Help lists the earlier beta]. Rules reported: one experiment per campaign at a time, the asset group is locked during the test, adjustable traffic split, 4 to 6 weeks recommended. Assets made in Asset Studio can go into the treatment arm. Check the Experiments page; MCC and API access lag the UI.
- Final URL expansion experiments: test expansion on vs off.
- Run 4 to 8 weeks, do not change the campaign during the test, judge on account-level conversions and value. See [experiments](experiments-and-testing.md).
