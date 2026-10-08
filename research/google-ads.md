# Google Ads: Market Research Dossier

> Compiled 2026-10-08 for the Ads Master google-ads package. Scope: Search, AI Max for Search, Performance Max, Demand Gen, YouTube, Shopping, Display, App, Local, and ads in AI Overviews and AI Mode.

## Method and limits

- First edition (2026-10-08): 19 web searches before the shared search budget ran out; direct page fetching (WebFetch, curl) was blocked by the environment's network policy, so 2025 to 2026 findings rested on search result summaries of official pages and trade press.
- Verification pass (same day): 50 further searches (extended mode for 2026 items) aimed at every [Unverified] and [Contested] item and at announcements from 2026-06 to 2026-10, plus direct reads of Google's official client library on GitHub (googleads/google-ads-python, release 33.0.0 with v23 to v25 type definitions and changelog) to check every GAQL field name. Google help, policy and developer pages were still read through search summaries, not full page loads. Sources 111 to 190 were added in this pass.
- Long-standing fundamentals (match type behavior, Quality Score, Ad Rank, budget mechanics, attribution models, policy structure) come from prior knowledge of Google documentation and are labeled [Official] only where the behavior has been stable for years.
- Evidence labels: [Official, YYYY-MM], [Study, YYYY-MM], [Practitioner report or consensus], [Contested], [Unverified]. "Official via trade press" means a Google statement (help text, notice email, Ads Liaison post) quoted by trade press.
- Still open after the pass: listed in the watch list. The human should re-check the open items and the remaining [Unverified] claims when Google publishes help pages for them.

## Executive summary

1. Search is now AI-matched by default. New Search campaigns start with AI Max on; AI Max (launched 2025-05, out of beta 2026-04) absorbed automatically created assets and campaign-level broad match through an auto-upgrade from 2026-09-01. DSA auto-migration moved to 2027-02, with new DSA creation ending 2027-01 [Official, Google Ads Help and Ads Liaison, 2026-06].
2. Keyword control shifted from match types to controls: brand inclusions and exclusions, URL inclusions and exclusions, locations of interest, text guidelines, text disclaimers and AI Brief (now in 7 more languages). Manual language targeting for Search ads was removed in late 2026-09 [Official, 2025 to 2026].
3. Performance Max became auditable and testable: channel performance reporting, search terms with cost (API `campaign_search_term_view`), asset-level metrics (performance labels retired), 10,000 negatives, asset A/B experiments rolling out to all from 2026-10-02, and an allowlisted channel prioritization alpha (2026-08) [Official and Practitioner reports].
4. Ads in AI Overviews run in 12 English-language markets with no 2026 expansion found; ads in AI Mode remain a US test. Broad match Search is eligible for AI Mode without AI Max, and a small test since 2026-09 lets exact and phrase keywords serve there for explicit intent. No reporting segment exists for either surface [Official via Ads Liaison, 2025-12 to 2026-09].
5. GML 2026 formats (Highlighted Answers, Conversational Discovery Ads) were still US tests in 2026-09; a Direct Offer asset for AI Mode entered testing in 2026-10 [Official, 2026-05; trade press 2026-09 to 2026-10].
6. Google's agents moved into the UI: Ask Advisor (beta, English, no MCC access) proposes changes and applies them only after user approval; AI summaries for experiments and AI campaign localization arrived in 2026-10 [Official, 2026-05; trade press 2026-09 to 2026-10].
7. Bidding behavior changed: target-based bidding now delivers toward the target on budget-limited tCPA and tROAS campaigns (2026-08-17 to 2026-08-27), Promotion mode (beta) and Smart Bidding Exploration for PMax without feeds (GA) arrived in 2026-06, campaign total budgets stay in open beta for Search, PMax and Shopping [Official, 2026].
8. First-party data plumbing moved to the Data Manager API: new Customer Match integrations from 2026-04-01 and new offline conversion integrations from 2026-06-15 can no longer use the Google Ads API; consent mode (ad_storage) became the single control for Google tag ads data on 2026-06-15; Customer Match accepts IP addresses from 2026-09 [Official, Google Ads Developer Blog and help pages, 2026].
9. Demand Gen is Google's single visual campaign: Video action campaigns upgraded by 2026-04, Display migration tool from 2026-06 with automatic migration in 2027, VTC optimization on by default (video only) and CPM billing for some placements from 2026-07-15 [Official and trade press, 2026].
10. Account operations got stricter: granular reporting history cut to 37 months (2026-06-01), in-account appeals closed for decisions older than 6 months (2026-07-21), Limited Ad Serving extended to all Google Ads, default-on changes (call recording 2026-07-01, local inventory ads 2026-08-31, automated promotions 2026-10-12) that each need an explicit decision [Official, 2026].

## State of the channel in 2026 (with numbers)

| Area | Status as of 2026-10 | Numbers | Label |
|---|---|---|---|
| AI Max for Search | GA for Search since 2026-04; on by default in new Search campaigns; auto-upgrade of ACA and campaign-level broad match from 2026-09-01 | Google cites +14% conversions or value at similar CPA or ROAS, +27% for exact and phrase heavy campaigns (2025-05) | [Official claim] |
| AI Max for Shopping and Travel | Closed betas, global, all languages, from 2026-04-30 | n/a | [Official, 2026-04] |
| DSA | Still running; creation re-enabled 2026-06-15, ends 2027-01; auto-migration 2027-02 | n/a | [Official via Ads Liaison, 2026-06] |
| Language targeting | Manual setting removed for Search ads (Search, AI Max, PMax Search inventory) in late 2026-09 | n/a | [Official, Ads Liaison 2026-08-14 and help page] |
| PMax negatives | Campaign negatives and shared lists, Search and Shopping inventory | Up to 10,000 per campaign | [Official, 2025] |
| PMax reporting and testing | Channel performance, search terms with cost, asset metrics; asset A/B experiments rolling out from 2026-10-02 | n/a | [Official 2025; trade press 2026-10] |
| Ads in AI Overviews | Live on mobile and desktop, no opt-out, no targeting | 12 countries, English | [Official, Google Ads Help] |
| Ads in AI Mode | US test; broad match, AI Max, PMax and Shopping eligible; exact and phrase in a small test since 2026-09 | n/a | [Official via Ads Liaison, 2026-06 and 2026-09] |
| Smart Bidding Exploration | Search tROAS GA 2025-07; PMax without feeds GA 2026-06; Shopping beta | Flex 10% to 30%; Google reports +18% converting query categories, +19% conversions (internal 2025-03-11 to 2025-04-11) | [Official claim] |
| Campaign total budgets | Open beta since 2026-01-15 for Search, PMax, Shopping; no GA found | 3 to 90 days (Search, Shopping, PMax) | [Official, 2026-01] |
| Target-based bidding update | Completed 2026-08-27 | Google example: tCPA 10 with actual 5 now delivers closer to 10 | [Official, 2026-06 to 2026-08] |
| Enhanced conversions | Single setting for web and leads since 2026-06 | Google cites 11% more Search conversions vs standard imports | [Official claim, 2026-09] |
| Offline uploads and Customer Match via API | Google Ads API restricted to previously active tokens (Customer Match 2026-04-01, offline clicks 2026-06-15); Data Manager API for new integrations | n/a | [Official, Google Ads Developer Blog 2026-05] |
| Demand Gen | Single visual campaign type | Google cites +30% average conversions from H2 2025 improvements | [Official claim via trade press, 2026-08] |
| Ask Advisor | Beta, English accounts, not in MCC; applies changes after approval | n/a | [Official, 2026-05; trade press 2026-09] |
| Conversion Lift | Self-serve for Search and PMax from 2026-10 | Minimum 1,000 conversions and 5,000 USD budget | [Official help; trade press 2026-10] |
| Reporting history | Granular data kept 37 months since 2026-06-01; monthly aggregates 11 years | n/a | [Official, 2026-05] |
| Google Ads API | Supported v23, v24, v25 (v25.2 on 2026-09-23); v20, v21, v22 sunset in 2026 | v22 sunset 2026-10-07 | [Official, 2026] |
| Appeals | 6-month window | From 2026-07-21 | [Official, 2026-07] |
| Search benchmarks (all industries, WordStream by LocaliQ 2026) | n/a | CTR 6.64%, CPC 5.42 USD, CVR 8.18%, CPL 66.69 USD (2025 edition: 6.66%, 5.26 USD, 7.52%, 70.11 USD) | [Study, 2026; read from search summaries] |

## Timeline of changes, January 2025 to October 2026

| Date | Change | Surface | Label | Source # |
|---|---|---|---|---|
| 2025-01 | Meridian open-source MMM generally available | Measurement | [Official, 2025-01] | 110 |
| 2025-01 | Performance Max features for 2025 announced, incl. campaign negative keywords in UI | PMax | [Official, 2025-01] | 17 |
| 2025-03 | Enhanced CPC fully retired for Search and Display (announced 2024-10) | Bidding | [Official] | prior knowledge |
| 2025-03 | PMax negative keyword limit raised to 10,000 per campaign | PMax | [Official, 2025; exact date Contested] | 15 |
| 2025-03 | Demand Gen channel controls (YouTube in-stream, in-feed, Shorts, Gmail, Discover, GDN) | Demand Gen | [Practitioner report] | 96 |
| 2025-04-30 | PMax channel performance, search terms and asset reporting announced | PMax | [Official, 2025-04] | 16, 54, 55 |
| 2025-05 | AI Max for Search announced, beta rollout globally | Search | [Official, 2025-05] | 49 |
| 2025-05 | Smart Bidding Exploration announced; Conversion Lift minimum lowered to 5,000 USD with Bayesian methods | Bidding, Measurement | [Official, 2025-05] | 19, 56, 125, 126 |
| 2025-05 | Google Marketing Live 2025: ads in AI Overviews expansion to desktop and more countries, ads in AI Mode test, Google tag gateway, Data Manager | AI surfaces, Measurement | [Official, 2025-05; details from prior knowledge] | prior knowledge |
| 2025-05 | PMax performance labels deprecated in favor of asset metrics | PMax | [Practitioner report; field absent from API v23 to v25] | 120 |
| 2025-06 | Video action campaign migration tool to Demand Gen available | Video | [Practitioner report, 2025-06] | 104 |
| 2025-07 | Smart Bidding Exploration GA for Search tROAS, campaign and portfolio level | Bidding | [Practitioner report, 2025-07] | 79 |
| 2025-07 | Brand inclusions and exclusions moved under AI Max for new Search campaigns | Search | [Official via trade press] | 50 |
| 2025-08 | Google Ads API v21: AI Max ad group controls, AI Max search term ad combination view | API | [Official, 2025-08] | 39 |
| 2025-08 | PMax shared negative keyword lists fully rolled out | PMax | [Practitioner report] | 15 |
| 2025-09 | Think Week: Ads Advisor and Analytics Advisor previewed; journey aware bidding pilots announced | UI, Bidding | [Practitioner reports] | 32, 71 |
| 2025-10 | Google open-sources the Google Ads API MCP server (read-only) | Tools | [Official, 2025-10] | 41, 42, 57, 58 |
| 2025-10 | Call-only ads deprecation announced (creation ends 2026-02, serving ends 2027-02) | Search | [Official] | 127 |
| 2025-11 | Ads Advisor and Analytics Advisor announced (Ads Advisor applies changes after approval); channel performance report in all PMax campaigns | UI, PMax | [Official, 2025-11] | 15, 32 |
| 2025-12 | Ads Advisor in all English Google Ads accounts | UI | [Practitioner report] | 32 |
| 2025-12 | Ads in AI Overviews live in 12 English-language countries | AI surfaces | [Official, Google Ads Help] | 27, 67, 78 |
| 2025-12 | Customer Match minimum list size 100 active users on Search, YouTube and Display | Audiences | [Practitioner report citing Google help] | 174 |
| 2025-12-09 | Data Manager API launched | Measurement | [Practitioner report] | 114 |
| 2026-01 | Direct Offers pilot in AI Mode with select US retailers; Universal Commerce Protocol introduced | AI surfaces, Shopping | [Official via trade press, 2026-01] | 3 |
| 2026-01-15 | Campaign total budgets open beta for Search, PMax, Shopping | Budgets | [Official, 2026-01] | 20, 21, 22, 66 |
| 2026-02 | Creation of new call-only ads removed | Search | [Official] | 127 |
| 2026-03-15 | Demand Gen lookalike segments become AI-powered audience signals | Demand Gen | [Practitioner report] | 96 |
| 2026-04 | Video action campaigns fully auto-upgraded to Demand Gen | Video | [Official] | 29 |
| 2026-04 | Enhanced conversions accept tag, Data Manager and API data at once with deduplication | Measurement | [Official] | 26 |
| 2026-04 | Demand Gen view-through conversion optimization on by default (open beta); Commerce Media Suite | Demand Gen | [Practitioner report, 2026-04] | 96 |
| 2026-04 | AI Max out of beta for Search; brand inclusion recommendation | Search | [Practitioner report, 2026-04] | 83 |
| 2026-04-01 | Google Ads API Customer Match uploads limited to tokens active from 2025-10-01 to 2026-03-31; Data Manager API for new integrations | API, Audiences | [Official] | 115, 142 |
| 2026-04-22 | Ads Advisor adds policy guidance, security monitoring (coming), automated certifications | UI, Policy | [Official, 2026-04] | 33 |
| 2026-04-30 | AI Max for Shopping and Travel closed betas, AI Brief, text disclaimers | Search, Shopping | [Official, 2026-04] | 12, 51, 52 |
| 2026-05 | Google Ads API v24.2: ad network type segment for PMax placement view | API | [Practitioner report] | 61 |
| 2026-05-07 | Journey aware bidding beta for Search tCPA (accounts with OCI or EC for leads) | Bidding | [Official via trade press] | 71, 149 |
| 2026-05-15 | Google announces offline click conversion upload allowlist in the Google Ads API from 2026-06-15 | API, Measurement | [Official] | 111, 140, 141 |
| 2026-05-20 | Google Marketing Live 2026: Ask Advisor, Highlighted Answers, Conversational Discovery Ads, ads in AI Mode, Direct Offers expansion with native checkout and travel, Universal Cart, UCP to YouTube Shopping ads and Demand Gen, AI-powered Shopping ads, Asset Studio with Gemini Omni, creator videos in paid campaigns, Demand Gen in Maps, Qualified Future Conversions, Meridian Studio, Business Agent for Leads, Analytics 360 relaunch | All | [Official, 2026-05] | 1, 2, 3, 4, 34, 53, 76, 77, 160 |
| 2026-05-28 | Data Manager API v1.7: IP ingestion for Customer Match, events to Google Marketing Platform | API | [Official] | 113 |
| 2026-06 | Display campaigns to Demand Gen migration tool (voluntary) | Display | [Official] | 97, 129, 173 |
| 2026-06 | UI renames "Maximize conversions with a target CPA" to "Target CPA" (and the ROAS equivalent) | Bidding | [Official wording via trade press] | 146 |
| 2026-06-01 | Granular reporting history limited to 37 months; aggregates 11 years; reach and frequency 3 years | Reporting | [Official] | 116, 117, 171, 172 |
| 2026-06-11 | DSA auto-migration moved to 2027-02; DSA creation re-enabled 2026-06-15, to end 2027-01 | Search | [Official via Ads Liaison] | 143, 144 |
| 2026-06-15 | Consent mode (ad_storage) single control for Google tag ads data; offline upload allowlist in effect; EC settings merged; product reporting includes all PMax networks | Measurement | [Official] | 26, 43, 111, 121, 170 |
| 2026-06 (mid) | Smart Bidding Exploration GA for PMax without feeds; Promotion mode beta for Search and PMax; target-based bidding update announced | Bidding | [Official announcement and Ads Liaison] | 131, 146, 147, 148 |
| 2026-06 | Ads Liaison: broad match campaigns eligible for AI Overviews and AI Mode without AI Max | AI surfaces | [Official via Ads Liaison] | 159 |
| 2026-06 | Google to auto-label unclassified conversion-based customer lists from 2026-08-18 | Audiences | [Practitioner report] | 167 |
| 2026-07 | Ask Advisor closed beta in Merchant Center (selected US merchants) | Tools | [Official] | 82, 124 |
| 2026-07 | Missed Opportunities moved from Labs into Recommendations (beta) | Recommendations | [Practitioner report] | 81 |
| 2026-07 | PMax "Partners" alpha: exclude Search Partners and Display | PMax | [Practitioner report] | 152 |
| 2026-07-01 | Call recording defaults to Yes in US and Canada where never set | Measurement | [Google notice via trade press] | 166 |
| 2026-07-15 | Demand Gen campaigns with VTC optimization billed on CPM on Discover | Demand Gen | [Google notice via trade press] | 95, 164 |
| 2026-07-21 | In-account appeals unavailable for policy decisions older than 6 months | Policy | [Official, 2026-07] | 64, 65 |
| 2026-07-22 | Google Ads API v25: lifecycle goal resources replaced by unified Goal and CampaignGoalConfig; lift study resources | API | [Official] | 60, 120 |
| 2026-08 | Limited Ad Serving policy extended to all Google Ads (rollout to 2028); certification process update; gambling, crypto, political content policy updates | Policy | [Official, 2026-08] | 37, 38 |
| 2026-08 | PMax channel prioritization alpha (Lower, Auto, Higher per channel), allowlisted | PMax | [Practitioner reports] | 80, 150, 151 |
| 2026-08 | Local Services Ads begin migrating to a PMax campaign type with pay-per-lead goals (select US categories first) | Local | [Official] | 128 |
| 2026-08 | Demand Gen VTC becomes video-first (image VTC not biddable); Display video assets move to CPM | Demand Gen | [Practitioner report citing Google help] | 165 |
| 2026-08 | Multimodal Video Creation in Asset Studio GA | Creative | [Practitioner report] | 84 |
| 2026-08-05 | Google Ads API v21 sunset (v20 sunset 2026-06-10) | API | [Official via trade press] | 94 |
| 2026-08-10 | Gemini-powered AI summaries and prompt dashboards in Google Ads | UI | [Practitioner report] | 84 |
| 2026-08-14 | Ads Liaison announces removal of manual language targeting for Search ads | Search | [Official] | 137, 145 |
| 2026-08-17 to 2026-08-27 | Target-based bid strategy update for budget-limited tCPA and tROAS | Bidding | [Official] | 24, 25, 146 |
| 2026-08-18 | Automatic customer type labeling of unclassified conversion-based customer lists | Audiences | [Practitioner report] | 84, 167 |
| 2026-08-18 | Content API for Shopping sunset; degradation from 2026-09-01; shutdown early 2027 | Shopping | [Official] | 135 |
| 2026-08-19 | Google Ads API v25.1: AI Max migration timestamp fields, text disclaimer assets, loyalty segmentation for value rules | API | [Official] | 93, 120 |
| 2026-08-20 | AI Max experiments with brand and location controls; multi-campaign budget and target tests (from 2026-09); Performance Planner one-click apply | Search | [Official] | 186, 187 |
| 2026-08-24 | Notice: LSA charges for missed calls (20 seconds, business hours) and follow-ups from 2026-10-01 | Local | [Google notice via trade press] | 188, 189 |
| 2026-08-31 | Local inventory ads on by default in Standard Shopping | Shopping | [Official] | 119, 163 |
| 2026-09-01 to 2026-09-30 | Auto-upgrade to AI Max of Search campaigns with ACA or campaign-level broad match | Search | [Official, 2026] | 5, 6, 48 |
| 2026-09 | Book button (partner bookings) on Search and PMax for eligible merchants | Local | [Official help] | 69, 122 |
| 2026-09 | AI Brief audience targeting in 7 more languages; new AI Max reporting; AI Max vs DSA test help article | Search | [Official, 2026-09] | 13, 178 |
| 2026-09 | Small test: exact and phrase keywords serve text ads in AI Mode for explicit intent | AI surfaces | [Official via Ads Liaison] | 157, 158 |
| 2026-09-02 | Developer Blog reminder: v22 sunset 2026-10-07 | API | [Official] | 118 |
| 2026-09-04 | Google Ads Developer Policies updated (own Google Cloud project, no programmatic proxies) | API | [Practitioner report] | 176 |
| 2026-09-07 | Limited Ad Serving applied to Demand Gen | Policy | [Practitioner report] | 96 |
| 2026-09-10 | Data Manager in GA and DV360; Data Strength Uplift in Google Ads; Meridian GeoX global | Measurement | [Practitioner reports] | 87, 90 |
| 2026-09-15 | PMax setting "Where should people go after clicking your ads?" | PMax | [Practitioner report] | 178 |
| 2026-09-22 | Learning period guidance updated to up to about 50 conversions or 3 cycles (UK page; US page differs) | Bidding | [Contested] | 175, 89 |
| 2026-09-23 | Google Ads API v25.2: Smart to PMax drafts, asset group tracking controls, percentile benchmarks, bid-too-low recommendations | API | [Official via trade press] | 59 |
| 2026-09-24 | Demand Gen update: one-tap image ads on Shorts and Gmail, affiliate locations in Maps | Demand Gen | [Unverified] | 89 |
| 2026-09-25 | Customer Match accepts IP addresses and interaction timestamps (not EEA, UK, Switzerland) | Audiences | [Official] | 113, 132, 169 |
| 2026-09 (late) | Manual language targeting removed for Search, AI Max and PMax Search inventory | Search | [Official] | 62, 136, 145 |
| 2026-10-01 | Editorial policy: business name may differ from domain under conditions | Policy | [Official] | 130, 162 |
| 2026-10-02 | PMax asset A/B experiments rolling out to all advertisers | PMax | [Practitioner report] | 85, 153 |
| 2026-10-02 | Loyalty member benefits in AI Mode and Gemini apps (US); loyalty program in 13 countries plus Japan points | Shopping | [Official help and trade press] | 134, 168 |
| 2026-10 (early) | Self-serve Conversion Lift for Search and PMax; AI-generated experiment summaries; AI Max reporting columns; Direct Offer asset test in AI Mode | Measurement, Search | [Practitioner reports] | 154, 155, 156, 179 |
| 2026-10-07 | Google Ads API v22 sunset | API | [Official] | 94, 118 |
| 2026-10-12 | Automated promotions from advertiser websites on by default for Search and PMax campaigns with location assets and no manual promotions | Assets | [Google notice via trade press] | 70, 91, 161 |
| 2026-10-19 | Google Ads Editor 2.10 and earlier no longer supported | Tools | [Practitioner report] | 179 |
| 2026-10-30 | Alcohol ads permitted on YouTube where locally allowed (personalized advertising policy update) | Policy | [Official, 2026-09] | 36 |
| 2027-01 (planned) | New DSA and new standalone Display campaign creation end | Search, Display | [Official via Ads Liaison; Display date from trade press] | 143, 173 |
| 2027-02 (planned) | DSA auto-migration to AI Max; existing call-only ads stop serving | Search | [Official] | 127, 143 |

## Best practice consensus

1. Measurement before optimization: business outcomes as primary conversions, enhanced conversions on, consent mode v2 in the EEA, offline conversion import for lead gen [Official guidance, Practitioner consensus].
2. Consolidated structures with enough conversions per bid strategy (about 30 per 30 days for tCPA, 50 for tROAS) beat granular structures under Smart Bidding [Practitioner consensus].
3. Brand separated from non-brand with brand exclusions on PMax and AI Max [Practitioner consensus].
4. Broad match only with conversion-based Smart Bidding, paired with negative lists and weekly search term reviews [Official guidance].
5. Exact match retained for brand and top money queries to benefit from query priority [Practitioner consensus].
6. Value-based bidding with real values; profit values or margin bands for ecommerce with variable margins [Practitioner consensus].
7. RSAs with many distinct headlines, minimal pinning; assets (sitelinks, callouts, images, business name and logo) on every campaign [Official guidance].
8. PMax with real video, audience signals from first-party data, URL exclusions, placement exclusions and channel report reviews [Practitioner consensus].
9. Test major automation (AI Max, PMax, NCA) with built-in experiments before full adoption [Practitioner consensus].
10. Use seasonality adjustments only for short events and data exclusions for tracking breaks [Official guidance].
11. Keep auto-apply recommendations off for keywords, budgets and targets [Practitioner consensus].
12. Demand Gen and YouTube judged with lift studies rather than last-click CPA [Practitioner consensus].

## Contested topics

| Topic | Side A | Side B | Package position |
|---|---|---|---|
| AI Max adoption | Google: +14% conversions or value at similar efficiency, more coverage of conversational queries | Practitioners: part of AI Max volume is cannibalized from existing keywords; generated copy and URL expansion create brand and compliance risk | Adopt per campaign after an AI Max experiment; controls first |
| DSA migration timing | Google's early 2026 post: DSA moves with the September 2026 upgrade | Ads Liaison 2026-06-11: auto-migration in 2027-02, creation ends 2027-01 | Resolved: 2027-02 (Official via Ads Liaison); test AI Max now |
| AI Mode ad eligibility | Only PMax and AI Max qualify | Broad match Search, Shopping and PMax qualify | Resolved: broad match qualifies without AI Max (Ads Liaison, 2026-06); exact and phrase only in a 2026-09 test |
| AI Mode reporting | No dedicated report exists | Some vendors claim AI Mode data is visible | Resolved for practice: no segment in Google Ads reporting as of 2026-10; vendor numbers are estimates |
| Feed-only PMax | Better Shopping concentration and ROAS control | Google recommends full assets for reach and performance | Test per account |
| PMax for lead gen | Works with OCI and strong signals | Generates junk leads | Only with OCI and qualified primary |
| Brand bidding | Protects demand from competitors and is cheap | Often low incrementality | Keep brand, test incrementality with geo or time holdouts |
| Ask Advisor writes | Ads Advisor coverage: applies changes with consent | Ask Advisor FAQ: "cannot execute account changes on your behalf" | Resolved: it applies changes after the user approves (Google FAQ and blog); package rule still requires the change list first |
| Learning period length | US help page: a few conversion cycles (1 to 2 typical) | UK help page since 2026-09: up to about 50 conversions or 3 cycles | Still Contested; plan 2 to 3 weeks or 50 conversions |
| Search partners | Adds cheap volume | Lower quality in many verticals | Off at launch; test with segment data |
| Journey aware bidding start | Beta from 2026-05-07 | Rolled out with GML 2026-05-20 | Resolved: beta announced on Google's blog 2026-05-07, still beta in 2026-07 |
| Late offline uploads | Trade reports: uploads more than 7 days after the conversion are ignored by data-driven attribution | No Google page found stating it | Unverified; upload within 24 hours anyway |

## What top operators do differently

1. They bid on profit: margin band campaigns or profit values, NCA values from real LTV data, POAS reporting.
2. They run the CRM loop daily: offline conversions by stage within 24 hours, value by stage, conversion adjustments for refunds and disqualified leads.
3. They govern queries even under automation: weekly search terms, monthly n-grams across Search, AI Max, Shopping and PMax, brand lists and URL exclusions everywhere.
4. They test every big automation step with built-in experiments and judge at account level.
5. They separate reporting: brand, non-brand, PMax, Shopping, visual, new vs returning customers.
6. They treat the feed and the landing page as bidding inputs, with handoffs to feed and CRO specialists.
7. They monitor with scripts and alerts (tracking anomalies, pacing, disapprovals) instead of waiting for weekly reviews.
8. They allocate budget by marginal return (lost impression share, simulators, Missed Opportunities) and stop scaling at breakeven.
9. They keep a change log and annotate Google-initiated changes (AI Max auto-upgrade, bidding updates) so trend breaks are explained.
10. They maintain account health proactively: verification, certifications, transparency pages, appeals within the window.

## Common expensive mistakes

| Mistake | Cost mechanism | Fix |
|---|---|---|
| Micro conversions (page views, add to cart) as primary | Smart Bidding buys cheap low-value actions | Primary = business outcome |
| Duplicate purchase tracking (GA4 import and Google tag both primary) | Inflated ROAS, overbidding | One primary |
| PMax without brand exclusions | Paying PMax prices for brand traffic; inflated PMax ROAS | Brand lists, separate brand Search |
| Lead gen PMax or broad without OCI | Junk and spam leads | OCI with qualified primary |
| Location option "Presence or interest" for local businesses | Clicks from outside the market | Presence |
| Display Network expansion left on in Search | Low intent clicks | Off |
| Auto-apply adding broad keywords and raising budgets | Unapproved spend | Turn off auto-apply for these types |
| Aggressive targets set from goals, not history | Spend collapse | Start at observed, step 10% to 15% |
| Ignoring the September 2026 AI Max auto-upgrade | Unplanned query expansion, generated copy, URL expansion to wrong pages | Inventory, controls, experiments |
| Integrations left on a sunset API version (v22 ended 2026-10-07) or a new upload integration built on the Google Ads API after 2026-06-15 | Offline conversions stop silently, bidding degrades | Data Manager API, monitor uploads and the allowlist error |
| Default-on changes left unreviewed (call recording 2026-07-01, local inventory ads 2026-08-31, automated promotions 2026-10-12, AI Max on new Search campaigns) | Privacy exposure, wrong offers, unplanned traffic | Decide each setting explicitly and log it |
| Missing the 6-month appeal window | Decisions become non-appealable in-account | Appeal promptly with evidence |
| Creating new accounts after suspension | Circumventing systems suspensions across linked accounts | Fix and appeal |
| Not applying data exclusions after tracking outages | Bidding learns from bad data | Data exclusions |
| Reporting blended ROAS | Hides poor non-brand economics | Segment reporting |

## Benchmarks

| Benchmark | Value | Source | Date | Caveat |
|---|---|---|---|---|
| Search CTR, all industries | 6.64% (2025 edition: 6.66%) | WordStream by LocaliQ | 2026 (data 2025-04 to 2026-03) | About 13,500 US search campaigns; read from search summaries; average vs median unclear |
| Search CPC, all industries | 5.42 USD (2025: 5.26 USD) | WordStream by LocaliQ | 2026 | Varies widely by vertical |
| Search conversion rate | 8.18% (2025: 7.52%) | WordStream by LocaliQ | 2026 | Conversion definitions vary |
| Cost per lead | 66.69 USD (2025: 70.11 USD) | WordStream by LocaliQ | 2026 | Not qualified leads; first decline in five years per publisher |
| PMax CTR trend | 1.29% to 1.68% year over year, CPA up, ROAS slightly down | Optmyzr, 21,000+ accounts | Q1 2026 | Tool user base |
| AI Max uplift | +14% (+27% exact and phrase heavy) | Google | 2025-05 | Vendor claim |
| Smart Bidding Exploration | +18% converting query categories, +19% conversions | Google internal, 2025-03-11 to 2025-04-11 | 2025-05 | Vendor claim |
| Enhanced conversions | 11% more Search conversions vs standard imports | Google | 2026-09 | Vendor claim, partly modeled |
| Demand Gen H2 2025 improvements | +30% average conversions | Google via trade press | 2026-08 | Vendor claim |
| Conversion Lift minimums | 1,000 conversions, 5,000 USD | Google Ads Help | 2025 to 2026 | Account availability varies |
| PMax negative keyword capacity | 10,000 per campaign | Google Ads Help | 2025 | Search and Shopping inventory only |
| AI Overviews ads markets | 12 countries, English | Google Ads Help | 2025-12, unchanged 2026-10 | Check for expansion |

Operating thresholds used by the package (zero-conversion term spend under 15%, brand IS above 90%, lost IS budget under 10% on profitable campaigns, cost-weighted QS 6+) are [Practitioner consensus] decision rules, not industry averages.

## Tools, APIs and MCP servers

| Tool | Type | Read or write | Notes |
|---|---|---|---|
| Google Ads API (v23 to v25) | Official API | Both | GAQL via GoogleAdsService; v22 sunset 2026-10-07; v25 breaking changes for lifecycle goals; field names confirmable from the official client library type files on GitHub |
| Data Manager API | Official API | Write (data uploads) | Required for new Customer Match (2026-04-01) and offline conversion (2026-06-15) integrations; no developer token, project quotas, IP ingestion (v1.7) |
| googleads/google-ads-mcp | Official MCP server | Read-only | Apache 2.0, Python, released 2025-10; GAQL search plus account listing or metadata tools |
| Community MCP servers (cohnen/mcp-google-ads, promobase/google-ads-mcp, getmcpads-com/google-ads-mcp-server) | Open source | Read, some write | Review code and scopes; writes must be approval-gated |
| Hosted and vendor MCPs (Adspirer, Ryze AI, Optmyzr MCP) | Vendor | Read, approval-gated writes | Vendor data access |
| Google Ads Scripts | In-account JavaScript | Both | Alerts, reports, n-grams |
| Google Ads Editor | Desktop bulk editor | Write by human | CSV change lists |
| Ask Advisor and Ads Advisor | In-product agents | Suggest, and write after user approval | English beta, not in MCC accounts |
| BigQuery Data Transfer for Google Ads, Looker Studio | Reporting | Read | Long history and joins |
| Optmyzr, Adalysis, Opteo | Third-party management | Both | Rules, audits, ad testing |
| Search Ads 360 | Enterprise platform | Both | Multi-engine |

## Official sources to monitor

| Source | URL | Cadence |
|---|---|---|
| Google Ads Help (announcements, help articles) | https://support.google.com/google-ads | Weekly |
| Google Ads product announcements | https://business.google.com/us/accelerate/announcements/ | Weekly |
| Google Ads and Commerce blog | https://blog.google/products/ads-commerce/ | Weekly |
| Advertising Policies Help and change log | https://support.google.com/adspolicy | Monthly |
| Google Ads API release notes | https://developers.google.com/google-ads/api/docs/release-notes | Each release |
| Google Ads API sunset dates | https://developers.google.com/google-ads/api/docs/sunset-dates | Quarterly |
| Google Ads API deprecations and unversioned changes | https://developers.google.com/google-ads/api/docs/deprecations | Monthly |
| Data Manager API guides | https://developers.google.com/data-manager/api/devguides/events/google-ads/offline/upgrade | Each upload change |
| Official Python client library (type files and changelog, fetchable from GitHub raw) | https://github.com/googleads/google-ads-python | Each API release |
| Google Ads Help announcements feed | https://support.google.com/google-ads/announcements/9048695 | Weekly |
| Google Ads Developer Blog | https://ads-developers.googleblog.com/ | Weekly |
| Official Google Ads MCP server | https://github.com/googleads/google-ads-mcp | Monthly |
| Google Ads Status Dashboard | https://ads.google.com/status/publisher/ | On incidents |
| Google Marketing Live | https://business.google.com/us/accelerate/googlemarketinglive/ | Annually (May) |

## Open questions and watch list

Resolved in the 2026-10-08 verification pass: DSA timing (2027-02), Ask Advisor write capability (after approval), AI Mode eligibility for broad match (yes, without AI Max), the 37-month retention limit (Official), scope of the 2026-06-15 upload and consent changes (Official), Conversion Lift minimums (1,000 conversions, 5,000 USD), journey aware bidding start (2026-05-07), Customer Match IP identifiers (Official), Book button and automated promotions defaults (Official notices), the 2026 WordStream benchmark edition, and all GAQL field names in the package.

Still open:
1. Exact date of the 2027-01 DSA creation cutoff on a Google help page.
2. Ads in AI Mode beyond the US, ads within AI Overviews beyond the 12 English-language countries, and any reporting segment for either surface.
3. Scope and duration of the exact and phrase match AI Mode test.
4. Rollout and controls for Highlighted Answers, Conversational Discovery Ads, AI-powered Shopping ads, Direct Offers and the Direct Offer asset.
5. End date of the transitional Google Ads API allowlist for offline click uploads and Customer Match (a 2027-03 partner deadline is reported, not confirmed).
6. Whether uploads more than 7 days after a conversion are excluded from data-driven attribution.
7. Journey aware bidding GA date and campaign types.
8. PMax channel prioritization beyond the allowlisted alpha; PMax asset experiments in MCC and the API.
9. Ask Advisor in other languages and in manager accounts.
10. Display to Demand Gen automatic migration date in 2027 and the standalone Display creation cutoff.
11. Campaign total budgets GA for Search, PMax and Shopping.
12. Learning period guidance (US and UK help pages disagree).
13. API v23 and v24 sunset dates and breaking changes in v26.
14. LSA to PMax migration phases outside the US.
15. Business name policy start date (2026-10-16 or 2026-10-19 reported).

## Sources

1. See what we announced at Google Marketing Live 2026. Google Ads Help. https://support.google.com/google-ads/answer/17100114. 2026-05.
2. Google Marketing Live 2026: News and announcements. Google. https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/. 2026-05.
3. A new generation of ads for the AI era of Search. Google. https://blog.google/products/ads-commerce/google-marketing-live-search-ads/. 2026-05.
4. Google Marketing Live 2026 highlights. Google. https://business.google.com/us/accelerate/googlemarketinglive/. 2026-05.
5. Google's Dynamic Search Ads are upgrading to AI Max. Google. https://blog.google/products/ads-commerce/dsa-upgrade-to-ai-max-2026/. 2026.
6. Dynamic Search Ads are upgrading to AI Max (announcement). Google. https://business.google.com/en-all/accelerate/announcements/dsa-upgrade-to-ai-max-2026/. 2026.
7. How AI Max for Search campaigns works. Google Ads Help. https://support.google.com/google-ads/answer/15910187. Living page.
8. About AI Max for Search campaigns. Google Ads Help. https://support.google.com/google-ads/answer/15910366. Living page.
9. Set up AI Max for Search campaigns. Google Ads Help. https://support.google.com/google-ads/answer/15909989. Living page.
10. About AI Max experiments. Google Ads Help. https://support.google.com/google-ads/answer/16450159. Living page.
11. Get started with AI Max for Search campaigns. Google Ads API. https://developers.google.com/google-ads/api/docs/campaigns/ai-max-for-search-campaigns/getting-started. Living page.
12. Steer performance with new AI Max features. Google. https://blog.google/products/ads-commerce/ai-max-new-features/. 2026-04.
13. AI Brief in more languages and new AI Max reporting. Google. https://blog.google/products/ads-commerce/ai-max-language-reporting-features/. 2026-09.
14. Apply brand exclusions to Performance Max or Search campaigns. Google Ads Help. https://support.google.com/google-ads/answer/14505308. Living page.
15. Google Ads Highlights of 2025. Google Ads Help. https://support.google.com/google-ads/answer/16756291. 2025-12.
16. Channel performance and more reporting coming to Performance Max. Google. https://blog.google/products/ads-commerce/channel-performance-reporting-coming-to-performance-max/. 2025-04.
17. Kick off 2025 with new Performance Max features. Google. https://blog.google/products/ads-commerce/new-performance-max-features-2025/. 2025-01.
18. Find or create placement reports for your Performance Max campaigns. Google Ads Help. https://support.google.com/google-ads/answer/11465047. Living page.
19. Expand your universe of conversions with Smart Bidding Exploration. Google. https://blog.google/products/ads-commerce/smart-bidding-exploration-ai/. 2025-05.
20. Campaign total budgets now available in Search, Performance Max and Shopping. Google. https://blog.google/products/ads-commerce/campaign-total-budgets/. 2026-01.
21. Campaign total budgets announcement. Google. https://business.google.com/us/accelerate/announcements/campaign-total-budgets/. 2026-01-15.
22. About campaign total budgets. Google Ads Help. https://support.google.com/google-ads/answer/10486938. Living page.
23. How budget changes take effect. Google Ads Help. https://support.google.com/google-ads/answer/10487143. Living page.
24. Changes to target based bid strategies. Google Ads Help. https://support.google.com/google-ads/answer/17061251. 2026-07.
25. FAQ about changes to target-based bid strategies. Google Ads Help. https://support.google.com/google-ads/answer/17125145. 2026-07.
26. Updates to your enhanced conversions settings. Google Ads Help. https://support.google.com/google-ads/answer/16884284. 2026.
27. About ads and AI Overviews. Google Ads Help. https://support.google.com/google-ads/answer/16297775. Living page.
28. About Demand Gen campaigns. Google Ads Help. https://support.google.com/google-ads/answer/13695777. Living page.
29. Video action campaigns are being upgraded to Demand Gen. Google Ads Help. https://support.google.com/google-ads/answer/15110871. 2025 to 2026.
30. Video action campaigns upgraded to Demand Gen in SA360. Search Ads 360 Help. https://support.google.com/sa360/answer/16247101. 2025.
31. Google Maps in Demand Gen. Google. https://business.google.com/us/accelerate/announcements/google-maps-in-demand-gen/. 2026.
32. Google's AI advisors: agentic tools to drive impact and insights. Google. https://blog.google/products/ads-commerce/ads-advisor-and-analytics-advisor/. 2025-11.
33. 3 new ways Ads Advisor is making Google Ads safer and faster. Google. https://blog.google/products/ads-commerce/ads-advisor-google-ads/. 2026-04.
34. Introducing Google Ask Advisor for marketers. Google. https://blog.google/products/ads-commerce/ask-advisor/. 2026-05.
35. Ask Advisor. Google. https://business.google.com/us/ad-tools/ask-advisor/. 2026.
36. Update to Google Ads Personalized Advertising Policy (September 2026). Advertising Policies Help. https://support.google.com/adspolicy/answer/17598957. 2026-09.
37. Update to Limited Ad Serving Policy (August 2026). Advertising Policies Help. https://support.google.com/adspolicy/answer/17344822. 2026-08.
38. Update to the Google Ads certification process (August 2026). Advertising Policies Help. https://support.google.com/adspolicy/answer/17251524. 2026-08.
39. Google Ads API release notes. Google. https://developers.google.com/google-ads/api/docs/release-notes. Ongoing.
40. Deprecation and sunset. Google. https://developers.google.com/google-ads/api/docs/sunset-dates. Ongoing.
41. Google Ads MCP server. Google. https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server. 2025 to 2026.
42. googleads/google-ads-mcp. GitHub. https://github.com/googleads/google-ads-mcp. 2025-10 onward.
43. Product reporting changes for Google Ads starting June 15, 2026. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/04/product-reporting-changes-for-google.html. 2026-04.
44. October 2026 changes to the Display and Video 360 API and SDF. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/08/october-2026-changes-to-display-video.html. 2026-08.
45. AdsApp.Budget. Google Ads Scripts. https://developers.google.com/google-ads/scripts/docs/reference/adsapp/adsapp_budget. Living page.
46. Campaign budgets overview. Google Ads API. https://developers.google.com/google-ads/api/docs/campaigns/budgets/overview. Living page.
47. Google Ads Status Dashboard. Google. https://ads.google.com/status/publisher/. Live.
48. Google sets AI Max migration timeline for Search campaigns. Search Engine Land. https://searchengineland.com/google-sets-ai-max-migration-timeline-for-search-campaigns-485006. 2026.
49. AI Max for Search: Everything you need to know. Search Engine Land. https://searchengineland.com/ai-max-for-search-everything-you-need-to-know-462923. 2025.
50. Google Ads moves brand controls under AI Max in new search campaigns. Search Engine Land. https://searchengineland.com/google-ads-brand-controls-ai-max-new-search-campaigns-458954. 2025-07.
51. Google AI Max gets new controls, Shopping rollout and travel consolidation. Search Engine Land. https://searchengineland.com/google-ai-max-gets-new-controls-shopping-rollout-and-travel-consolidation-476025. 2026-04.
52. Google launches AI Max for Shopping and Travel campaigns. Search Engine Journal. https://www.searchenginejournal.com/google-launches-ai-max-for-shopping-and-travel-campaigns/573375/. 2026-04.
53. Google launches Ask Advisor across Ads, Analytics and Merchant Center. Search Engine Land. https://searchengineland.com/google-launches-ask-advisor-across-ads-analytics-and-merchant-center-478114. 2026-05.
54. Google Performance Max channel, search, asset insights coming soon. Search Engine Land. https://searchengineland.com/google-performance-max-channel-search-asset-insights-454695. 2025-04.
55. Channel reporting is coming to Performance Max campaigns. Search Engine Journal. https://www.searchenginejournal.com/channel-reporting-is-coming-to-performance-max-campaigns/545709/. 2025-04.
56. Google unveils Smart Bidding Exploration. Search Engine Land. https://searchengineland.com/google-smart-bidding-exploration-455756. 2025-05.
57. Google open-sources ads API MCP server. Search Engine Land. https://searchengineland.com/google-open-sources-ads-api-mcp-server-463219. 2025-10.
58. Google open-sources an MCP server for the Google Ads API. MarkTechPost. https://www.marktechpost.com/2025/10/10/google-open-sources-an-mcp-server-for-the-google-ads-api-bringing-llm-native-access-to-ads-data/. 2025-10-10.
59. Google Ads API v25.2 adds competitive benchmarks and PMax upgrades. Search Engine Land. https://searchengineland.com/google-ads-api-v25-2-adds-competitive-benchmarks-and-pmax-upgrades-491541. 2026-09.
60. Google Ads API v25 kills two lifecycle goal resources. PPC Land. https://ppc.land/google-ads-api-v25-kills-two-lifecycle-goal-resources-forcing-code-rewrites/. 2026-07.
61. Google Ads API v24.2: AI transparency and PMax segmentation. PPC Land. https://ppc.land/google-ads-api-v24-2-ai-transparency-and-pmax-segmentation-finally-arrive/. 2026.
62. Google Ads to eliminate language targeting in late September. MediaPost. https://www.mediapost.com/publications/article/417817/google-ads-to-eliminate-language-targeting-in-late.html. 2026-09-11.
63. Google Ads, platforms see major bidding changes. MediaPost. https://www.mediapost.com/publications/article/415821/google-ads-platforms-see-major-bidding-changes.html. 2026-06-16.
64. Google Ads sets 6 month timeline for appeals. Search Engine Roundtable. https://www.seroundtable.com/google-ads-appeals-limit-41730.html. 2026-07.
65. Google Ads kills appeals for policy decisions over 6 months old. PPC Land. https://ppc.land/google-ads-kills-appeals-for-policy-decisions-over-6-months-old/. 2026-07.
66. Google Ads campaign total budgets live as an open beta. Search Engine Roundtable. https://www.seroundtable.com/google-ads-campaign-total-budgets-40774.html. 2026-01.
67. Google expands ads in AI Overviews to more countries. Search Engine Roundtable. https://www.seroundtable.com/google-expands-ads-in-ai-overviews-40629.html. 2025-12.
68. Google Ads new Demand Gen Maps channel. Search Engine Roundtable. https://www.seroundtable.com/google-ads-demand-gen-maps-channel-40640.html. 2025-12 to 2026.
69. Google Book buttons expand to Search and Performance Max. Search Engine Roundtable. https://www.seroundtable.com/google-ads-book-buttons-41964.html. 2026-09.
70. Google Ads to automated promotions for some Search campaigns on October 12th. Search Engine Roundtable. https://www.seroundtable.com/google-ads-automated-promotions-october-12-42223.html. 2026-10.
71. Google targets hidden conversions with new bidding and budgeting tools. PPC Land. https://ppc.land/google-targets-hidden-conversions-with-new-bidding-and-budgeting-tools/. 2026.
72. Google's Ask Advisor unifies ads, analytics and commerce in one AI agent. PPC Land. https://ppc.land/googles-ask-advisor-unifies-ads-analytics-and-commerce-in-one-ai-agent/. 2026-05.
73. Google's Video Action campaigns to merge with Demand Gen. PPC Land. https://ppc.land/googles-video-action-campaigns-to-merge-with-demand-gen/. 2025.
74. How to advertise in Google AI Mode for ecommerce. Search Engine Journal. https://www.searchenginejournal.com/how-to-advertise-in-google-ai-mode-for-ecommerce/582810/. 2026.
75. Microsoft Advertising rolls out AI Max globally. Search Engine Journal. https://www.searchenginejournal.com/microsoft-advertising-rolls-out-ai-max-globally/586459/. 2026.
76. Google Marketing Live 2026: 11 biggest announcements. WordStream. https://www.wordstream.com/blog/google-marketing-live-2026. 2026-05.
77. Google Marketing Live 2026: all you need to know. PPC News Feed. https://ppcnewsfeed.com/blog/google-marketing-live-2026/. 2026-05.
78. Ads in AI Overviews now live in 12 countries. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2025-12/ads-in-ai-overviews-now-live-in-12-countries/. 2025-12.
79. Smart Bidding Exploration now live for tROAS campaigns. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2025-07/smart-bidding-exploration-now-live-for-troas-campaigns/. 2025-07.
80. Performance Max adds channel prioritization controls. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-08/performance-max-adds-channel-prioritization-controls/. 2026-08.
81. Missed Opportunities moved to Recommendations. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-07/missed-opportunities-moved-recommendations/. 2026-07.
82. Ask Advisor available in Google Merchant Center. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-07/ask-advisor-available-google-merchant-center/. 2026-07.
83. AI Max brand inclusion recommendation now available. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-04/ai-max-brand-inclusion-recommendation-now-available/. 2026-04.
84. Google Ads updates: August 2026. PPC News Feed. https://ppcnewsfeed.com/google-ads-updates/2026-08/. 2026-08.
85. Every Google Ads change in 2026 (updated weekly). Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/google-ads-changes-2026. 2026.
86. Google Ads mid-June 2026 updates: DSA migration delay, Smart Bidding, consent mode. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/google-ads-june-2026-dsa-migration-smart-bidding-consent-mode. 2026-06.
87. Google Ads September 2026: Data Strength tools. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/google-ads-data-strength-september-2026-ecommerce. 2026-09.
88. Google Ads update September 2026: AI Max migration, PMax sliders, Book button. rulers. https://rulers.digital/en/blog/google-ads-update-september-2026. 2026-09.
89. Google Ads updates, verified: September 2026. LGG Media. https://www.lgg.media/blog/google-ads-updates-september-2026/. 2026-09.
90. September 2026 Google Ads update. Granular Marketing. https://granularmarketing.com/google-ad-updates/september-2026-google-ads-update-new-measurement-tools/. 2026-09.
91. October 2026 Google Ads update: automated promotions. Granular Marketing. https://granularmarketing.com/google-ad-updates/october-2026-google-ads-update-automated-promotions-from-your-website/. 2026-10.
92. Google Ads July 2026: API v25, appeal caps, recommendations. Digital Applied. https://www.digitalapplied.com/blog/google-ads-july-2026-ops-sweep-api-v25-appeals-missed-opportunities. 2026-07.
93. Google Ads API v25.1 adds AI Max migration date fields. Digital Applied. https://www.digitalapplied.com/blog/google-ads-api-v251-ai-max-migration-date-fields. 2026-08.
94. Google Ads API sunset dates: v22 stops working in October. Digital Applied. https://www.digitalapplied.com/blog/google-ads-api-versions-sunset-dates-v22-deadline. 2026.
95. Google Ads Demand Gen shifts to CPM billing. Digital Applied. https://www.digitalapplied.com/blog/google-ads-demand-gen-cpm-billing-2026-advertiser-playbook. 2026.
96. Google Demand Gen April 2026 update. ALM Corp. https://almcorp.com/blog/google-demand-gen-april-2026-update/. 2026-04.
97. Google Display ads are moving to Demand Gen. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/google-display-ads-demand-gen-migration-2026-ecommerce. 2026.
98. AI Overviews ads: what is confirmed, what is not. Honeyb. https://www.honeyb.ai/blog/ai-overviews-ads. 2026-07.
99. Google AI Mode ads. Adthena. https://www.adthena.com/resources/blog/google-ai-mode-ads/. 2026-08.
100. Google AI Mode tracker 2026. Keywords Everywhere. https://keywordseverywhere.com/news/google-ai-mode/. 2026-09.
101. The end of keywords? Ginny Marvin on the shift to AI Max. Smarter Ecommerce. https://smarter-ecommerce.com/blog/en/google-ads/the-end-of-keywords-ginny-marvin-on-the-shift-to-ai-max-for-search/. 2025.
102. Smart Bidding Exploration: when to use it and when not. Thomas Eccel. https://www.thomaseccel.com/blogs/news/smart-bidding-exploration-google-ads-when-to-use-it-and-when-not. 2025.
103. Google launches Smart Bidding Exploration. PMG. https://www.pmg.com/insights-and-news/google-launches-smart-bidding-exploration. 2025.
104. Google video action campaigns migrating to Demand Gen. Smartly. https://www.smartly.io/resources/google-video-action-campaigns-migrating-demand-gen. 2025.
105. Google Ads MCP: official, open source and read-only. Carly. https://www.usecarly.com/blog/google-ads-mcp/. 2026.
106. Google Ads MCP server: official vs hosted. Adspirer. https://www.adspirer.com/blog/google-ads-mcp. 2026.
107. getmcpads-com/google-ads-mcp-server. GitHub. https://github.com/getmcpads-com/google-ads-mcp-server. 2026.
108. promobase/google-ads-mcp. GitHub. https://github.com/promobase/google-ads-mcp. 2026.
109. 2025 Google Ads Benchmarks: Competitive Data and Insights for Your Industry. WordStream by LocaliQ. https://www.wordstream.com/resources/google-ads-industry-benchmarks. 2025.
110. Meridian. GitHub (Google). https://github.com/google/meridian. 2025 onward.
111. Changes to Offline Click Conversion Import Support in the Google Ads API. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/05/changes-to-offline-click-conversion.html. 2026-05-15.
112. Upcoming Improvements to Offline Conversion Imports. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/03/upcoming-improvements-to-offline.html. 2026-03.
113. Data Manager API now supports sending events to Google Marketing Platform destinations and IP ingestion for Google Ads Customer Match. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/05/data-manager-api-now-supports-sending.html. 2026-05.
114. Upgrade from the Google Ads API (offline conversions). Data Manager API docs. https://developers.google.com/data-manager/api/devguides/events/google-ads/offline/upgrade. n.d..
115. Feature deprecations and unversioned changes. Google Ads API docs. https://developers.google.com/google-ads/api/docs/deprecations. n.d..
116. New Data Retention Policy for Google Ads starting June 1, 2026. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/05/new-data-retention-policy-for-google.html. 2026-05.
117. Google Ads Data Retention Policy. Google Ads Help. https://support.google.com/google-ads/answer/15188209. n.d..
118. Google Ads API v22 sunset reminder. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/09/google-ads-api-v22-sunset-reminder.html. 2026-09-02.
119. Enabling Local Inventory Ads by Default for Shopping Campaigns starting on August 31, 2026. Google Ads Developer Blog. https://ads-developers.googleblog.com/2026/07/enabling-local-inventory-ads-by-default.html. 2026-07.
120. googleads/google-ads-python (v25 type definitions, ChangeLog 33.0.0). GitHub (Google). https://github.com/googleads/google-ads-python. checked 2026-10-08.
121. Updates to Google Analytics data controls. Analytics Help. https://support.google.com/analytics/answer/17016975. 2026-04.
122. About partner bookings. Google Ads Help. https://support.google.com/google-ads/answer/17199940. 2026.
123. Ask Advisor in Google Ads (beta). Google Ads Help. https://support.google.com/google-ads/answer/16574983. 2026.
124. About Ask Advisor in Merchant Center. Merchant Center Help. https://support.google.com/merchants/answer/17091244. 2026.
125. Set up Conversion Lift based on users. Google Ads Help. https://support.google.com/google-ads/answer/12005564. n.d..
126. About Bayesian methodology in Conversion Lift. Google Ads Help. https://support.google.com/google-ads/answer/16627074. n.d..
127. Action Required: Transition from call ads to call assets. Google Ads Help. https://support.google.com/google-ads/answer/16598240. 2025-10 onward.
128. Local Services Ads transition to Performance Max campaigns with pay-per-lead goals. Google Ads Help. https://support.google.com/google-ads/answer/17213585. 2026-08.
129. Google Display Ads campaigns have a new home in Demand Gen. Google Ads Help. https://support.google.com/google-ads/answer/17051545. 2026.
130. Update to Editorial Policy (October 2026). Advertising Policies Help. https://support.google.com/adspolicy/answer/18287059. 2026-10-01.
131. Promotion mode. Google (business.google.com). https://business.google.com/us/accelerate/announcements/promotion-mode/. 2026-06.
132. Prepare your data for import. Google Ads Data Manager Help. https://support.google.com/google-ads-data-manager/answer/14184381. n.d..
133. Customer Match policy. Advertising Policies Help. https://support.google.com/adspolicy/answer/6299717. n.d..
134. Step 4: Set up Customer Match lists for members. Merchant Center Help. https://support.google.com/merchants/answer/16467744. 2026.
135. Deprecation and sunset (Content API for Shopping). Google for Developers. https://developers.google.com/shopping-content/guides/deprecation-and-sunset. 2026.
136. About language targeting. Google Ads Help. https://support.google.com/google-ads/answer/1722078. n.d..
137. AdsLiaison post on removing language targeting. X (Google Ads Liaison). https://x.com/adsliaison/status/2088017049960231270. 2026-08.
138. New features and announcements. Google Ads Help. https://support.google.com/google-ads/announcements/9048695. n.d..
139. CampaignSearchTermView (v25 reference). Google Ads API docs. https://developers.google.com/google-ads/api/reference/rpc/v25/CampaignSearchTermView. 2026-07-22.
140. Google is moving offline conversion imports out of the Google Ads API. Search Engine Land. https://searchengineland.com/google-is-moving-offline-conversion-imports-out-of-the-google-ads-api-477669. 2026-05.
141. Google blocks new offline conversion imports via Ads API from June 15. PPC Land. https://ppc.land/google-blocks-new-offline-conversion-imports-via-ads-api-from-june-15/. 2026-05.
142. Google to disable Customer Match uploads in Ads API. Search Engine Land. https://searchengineland.com/google-to-disable-customer-match-uploads-in-ads-api-470796. 2026.
143. Google delays Dynamic Search Ads migration to AI Max. Search Engine Land. https://searchengineland.com/google-delays-dynamic-search-ads-migration-to-ai-max-480049. 2026-06.
144. Google Provides More Time For Dynamic Search Ads Migration. Search Engine Journal. https://www.searchenginejournal.com/google-extends-dynamic-search-ads-migration-deadline/579074/. 2026-06.
145. Google Ads Is Retiring Language Targeting In Search Campaigns. Search Engine Journal. https://www.searchenginejournal.com/google-is-removing-language-targeting-from-search-campaigns/585592/. 2026-08.
146. Google Ads Changes With Bidding For Campaigns Limited By Budget. Search Engine Roundtable. https://www.seroundtable.com/google-ads-bidding-campaigns-limited-budget-41618.html. 2026-06.
147. Google expands Smart Bidding Exploration, adds Promotion Mode. Search Engine Land. https://searchengineland.com/google-expands-smart-bidding-exploration-adds-promotion-mode-480165. 2026-06.
148. Google Ads Promotion Mode Beta, Smart Bidding Exploration Expands and Bidding Target Optimization Changes. Search Engine Roundtable. https://www.seroundtable.com/google-ads-promotion-mode-smart-bidding-bidding-target-41501.html. 2026-06.
149. Google Ads Rolls Out Journey-Aware Bidding And New Pacing Controls. Search Engine Journal. https://www.searchenginejournal.com/google-ads-introduces-journey-aware-bidding-and-new-budget-pacing-updates/574141/. 2026-05.
150. Google tests channel prioritization controls for Performance Max. Search Engine Land. https://searchengineland.com/google-tests-channel-prioritization-controls-for-performance-max-485825. 2026-08.
151. Google Ads Channel Settings Prioritization Slider (Alpha Test). Search Engine Roundtable. https://www.seroundtable.com/google-ads-channel-settings-prioritization-slider-41949.html. 2026-08.
152. Google quietly gives ground on PMax controls. Digiday. https://digiday.com/media-buying/google-quietly-gives-ground-on-pmax-controls/. 2026-07.
153. Google Ads brings A/B testing to Performance Max asset groups. Search Engine Land. https://searchengineland.com/google-ads-brings-a-b-testing-to-performance-max-asset-groups-493229. 2026-10-02.
154. Google opens Conversion Lift to Search and Performance Max. Search Engine Land. https://searchengineland.com/google-opens-conversion-lift-to-search-and-performance-max-494195. 2026-10.
155. Google Ads Conversion Lift Measurement Now Self-Service. Search Engine Roundtable. https://www.seroundtable.com/google-ads-conversion-lift-measurement-self-service-42250.html. 2026-10.
156. Google Ads adds AI-powered insights to experiment reporting. Search Engine Land. https://searchengineland.com/google-ads-adds-ai-powered-insights-to-experiment-reporting-494562. 2026-10.
157. Google tests traditional Search campaigns in AI Mode. Search Engine Land. https://searchengineland.com/google-tests-traditional-search-campaigns-in-ai-mode-487199. 2026-09.
158. Exact and phrase match keywords gain AI Mode ads in Google test. PPC Land. https://ppc.land/exact-and-phrase-match-keywords-gain-ai-mode-ads-in-google-test/. 2026-09.
159. Ginny Marvin clarifies AI Max, AI Search ads and what advertisers should prioritize after GML. Search Engine Land. https://searchengineland.com/ginny-marvin-clarifies-ai-max-ai-search-ads-and-what-advertisers-should-prioritize-after-gml-479838. 2026-06.
160. Google tests new conversational ad formats in AI Mode and Search. Search Engine Land. https://searchengineland.com/google-tests-new-conversational-ad-formats-in-ai-mode-and-search-478115. 2026-05.
161. Google Ads will auto-apply website coupons to some campaigns from October 12. PPC Land. https://ppc.land/google-ads-will-auto-apply-website-coupons-to-some-campaigns-from-october-12/. 2026-10.
162. Google Ads To Allow Some Advertisers To Use Business Names That Differ From Destination Domains. Search Engine Roundtable. https://www.seroundtable.com/google-ads-business-name-policy-42214.html. 2026-10.
163. Google confirms Local Inventory Ads will be enabled by default. Search Engine Land. https://searchengineland.com/google-confirms-local-inventory-ads-will-be-enabled-by-default-482779. 2026-07.
164. Google Ads shifts Demand Gen billing to CPM for some Discover campaigns. Search Engine Land. https://searchengineland.com/google-ads-shifts-demand-gen-billing-to-cpm-for-some-discover-campaigns-480300. 2026-06 to 2026-07.
165. Google updates Demand Gen view-through conversion optimization. Search Engine Land. https://searchengineland.com/google-updates-demand-gen-view-through-conversion-optimization-485127. 2026-08.
166. Google Ads Call Recording To Default To Yes On July 1st. Search Engine Roundtable. https://www.seroundtable.com/google-ads-call-recording-default-yes-41262.html. 2026-05.
167. Google Ads to automatically classify conversion-based customer lists. Search Engine Land. https://searchengineland.com/google-ads-to-automatically-classify-conversion-based-customer-lists-480433. 2026-06.
168. Google Merchant Center Loyalty Customer Match Expands To AI Mode and More Regions. Search Engine Roundtable. https://www.seroundtable.com/google-loyalty-customer-match-expands-42216.html. 2026-10-02.
169. Google Customer Match gains raw IP matching, minus users in 32 countries. PPC Land. https://ppc.land/google-customer-match-gains-raw-ip-matching-minus-users-in-32-countries/. 2026-09.
170. Google Signals loses ad data control on June 15: what it really means. PPC Land. https://ppc.land/google-signals-loses-ad-data-control-on-june-15-what-it-really-means/. 2026-06.
171. Google Ads cuts granular data access to 37 months starting June 2026. PPC Land. https://ppc.land/google-ads-cuts-granular-data-access-to-37-months-starting-june-2026/. 2026-05.
172. Google Ads Is Cutting Off Access To Older Reporting Data. Search Engine Journal. https://www.searchenginejournal.com/google-ads-will-limit-access-to-older-reporting-data/574467/. 2026-05.
173. Google Is Retiring Standalone Display Campaigns In Favor Of Demand Gen. Search Engine Journal. https://www.searchenginejournal.com/google-is-retiring-standalone-display-campaigns-in-favor-of-demand-gen/575889/. 2026-06.
174. Google Ads lowers customer lists. Search Engine Roundtable. https://www.seroundtable.com/google-ads-lowers-customer-lists-40648.html. 2025-12.
175. Google Updates Bid Strategy Learning Period to Around 50 Conversions. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-09/google-updates-bid-strategy-learning-period/. 2026-09-22.
176. Google Ads Developer Policies Updated for Enhanced Security. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-09/google-ads-developer-policies-updated-security/. 2026-09-04.
177. Google Ads Expands Promotion Mode to Daily Budgets. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2026-09/google-ads-expands-promotion-mode-daily-budgets/. 2026-09.
178. Daily Search Forum Recap: September 23, 2026. Search Engine Roundtable. https://www.seroundtable.com/recap-09-23-2026-42145.html. 2026-09-23.
179. Google Ads Updates: October 2026. PPC News Feed. https://ppcnewsfeed.com/google-ads-updates/2026-10/. 2026-10.
180. Google Ads Benchmarks 2026: Competitive Data and Insights for Every Industry. WordStream by LocaliQ. https://www.wordstream.com/blog/2026-google-ads-benchmarks. 2026.
181. Search Advertising Benchmarks for Every Industry (2026 Data). LocaliQ. https://localiq.com/blog/search-advertising-benchmarks/. 2026.
182. The State of Google Ads Q1 2026. Optmyzr. https://www.optmyzr.com/blog/state-of-google-ads-q1-2026/. 2026.
183. New Optmyzr Data: Google Ads Engagement Jumps While Efficiency Stays Flat. Search Engine Journal. https://www.searchenginejournal.com/optmyzr-report-finds-google-ads-engagement-rising-while-efficiency-holds/573718/. 2026.
184. Is Performance Max Cannibalizing Your Search Campaigns? Optmyzr. https://www.optmyzr.com/blog/is-pmax-cannibalizing-search/. 2025.
185. How Google's June 2026 Privacy Update Will Affect Phone Call Conversion Attribution. Invoca. https://www.invoca.com/blog/how-googles-june-2026-privacy-update-will-affect-phone-call-conversion-attribution. 2026.
186. AI Max testing and planning tools (post by Brandon Ervin, Search Ads product lead). Google (blog.google). https://blog.google/products/ads-commerce/ai-max-testing-planning-tools/. 2026-08-20.
187. Google Ads Launches New Search and AI Max Experimentation Tools. Search Engine Journal. https://www.searchenginejournal.com/google-ads-launches-new-search-and-ai-max-experimentation-tools/586549/. 2026-08-24.
188. Google To Charge For Missed and Subsequent Calls On LSAs. Search Engine Roundtable. https://seroundtable.com/google-lsa-missed-subsequent-calls-41940.html. 2026-08-25.
189. Google LSA advertisers face missed call charges from October 1. PPC Land. https://ppc.land/google-lsa-advertisers-face-missed-call-charges-from-october-1/. 2026-08.
190. AI Max experiments arrive in Google Ads: Here’s how they work. Search Engine Land. https://searchengineland.com/ai-max-experiments-arrive-in-google-ads-heres-how-they-work-459935. 2025.
