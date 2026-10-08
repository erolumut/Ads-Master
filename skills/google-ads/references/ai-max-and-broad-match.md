# AI Max for Search and Broad Match

> Knowledge as of 2026-10. AI Max is the fastest moving part of Google Ads. Check the AI Max help articles, the Google Ads and Commerce blog and the Google Ads API release notes before changing settings. Several items below are from trade press and are labeled.

## 1. What AI Max is

AI Max for Search campaigns is a one-click feature suite added to a standard Search campaign. It is not a separate campaign type. [Official, 2025-05]

| Feature | What it does | Level | Default when AI Max is turned on |
|---|---|---|---|
| Search term matching | Keywordless matching: uses your keywords, ads, assets and landing pages to find relevant queries beyond your keywords, and upgrades existing keywords to broad-style matching | Campaign, can be turned off per ad group | On |
| Text customization | Generates headlines and descriptions from your site, landing pages, existing ads and keywords (the successor of automatically created assets) | Campaign | On |
| Final URL expansion | Sends the click to the landing page on your domain judged most relevant to the query and the ad group theme | Campaign, requires text customization | Optional |
| URL inclusions | Adds specific URLs the expansion did not pick | Ad group | Optional |
| URL exclusions | Blocks URLs from final URL expansion | Campaign | Optional, requires text customization and final URL expansion |
| Brand inclusions | Restricts matching to queries about listed brands | Campaign or ad group (ad group list overrides the campaign list for that ad group) | Optional |
| Brand exclusions | Blocks queries about listed brands | Campaign | Optional |
| Locations of interest | Targets queries that mention or imply a location, per ad group | Ad group, AI Max only | Optional |
| Text guidelines | Term exclusions and messaging restrictions for generated text | Campaign | Optional |
| AI Brief | Natural language instructions for messaging, matching and audience | Campaign | Closed beta since 2026-04, expanding to more languages in 2026-09 [Official, 2026] |
| Text disclaimers | Required disclosure text that stays with generated ads and expanded URLs | Campaign | New in 2026 [Official, 2026-04] |

Sources: Google Ads Help "About AI Max for Search campaigns", "How AI Max for Search campaigns works", "Set up AI Max for Search campaigns"; Google Ads and Commerce blog 2025 and 2026.

Facts from the help center that change decisions [Official]:
- Turning off text customization disables final URL expansion.
- With final URL expansion on, pinned RSA assets are not used when a more relevant URL is chosen.
- Brand inclusions added at ad group level override only for that ad group; the campaign list applies to the other ad groups.
- To add new brand lists to a Search campaign you must enable AI Max. Existing brand lists on legacy campaigns can stay.
- Locations of interest work at ad group level and only inside AI Max. If the campaign location option is "Presence", people outside the targeted area still do not see ads.
- The features need conversion-based Smart Bidding to work as intended.
- New Search campaigns start with AI Max turned on by default; choose the features to keep during setup [Official, Google Ads Help "Set up AI Max for Search campaigns"]. Every new Search build must record an explicit AI Max decision.

## 2. Timeline that matters for audits

| Date | Event | Label |
|---|---|---|
| 2024 | Brand restrictions for broad match in Search launched (brand lists) | [Official, 2024] |
| 2025-05 | AI Max for Search announced and rolled out in beta globally. Google cites 14% more conversions or conversion value at similar CPA or ROAS on average, and 27% for campaigns mostly using exact and phrase match | [Official, 2025-05] |
| 2025-07 | Brand inclusions and exclusions moved under AI Max for new Search campaigns | [Official via Search Engine Land, 2025-07] |
| 2025-08 | Google Ads API v21 adds ad group level AI Max controls (disable search term matching per ad group; brand lists, locations and URL rules on ad groups) and the AI Max search term, headline and landing page combination view | [Official, 2025-08] |
| 2026-04 | AI Max out of beta for Search. AI Brief announced (closed beta). AI Max for Shopping and Travel announced as closed betas. Text disclaimers added. Brand inclusion recommendation appears | [Official, 2026-04] |
| 2026-06-11 | DSA auto-migration moved from September 2026 to February 2027 to avoid Q4 disruption. Creating new DSA campaigns was allowed again from 2026-06-15. ACA and campaign-level broad match kept the September 2026 date | [Official, Google Ads Liaison, reported by Search Engine Land and Search Engine Journal, 2026-06] |
| 2026-08-03 | New campaign-level broad match settings and legacy ACA setups can no longer be created | [Unverified, agency summaries 2026-08] |
| 2026-08-19 | Google Ads API v25.1 adds output-only campaign fields `aca_migration_date_time` and `broad_match_migration_date_time` that record when a campaign was migrated to AI Max | [Official, v25 field docs] |
| 2026-08-20 | AI Max experiments (already a 50/50 split inside the original campaign since 2025) can now run with brand and location controls enabled; multi-campaign A/B tests of budget and ROI target changes roll out from 2026-09; Performance Planner previews bidding and budget target changes and can apply them in one click | [Official, Google Ads and Commerce blog 2026-08-20; Search Engine Journal 2026-08-24] |
| 2026-09-01 to 2026-09-30 | Auto-upgrade of Search campaigns using automatically created assets (ACA) or the campaign-level broad match setting into AI Max | [Official, 2026] |
| 2026-09 | AI Brief audience targeting extended to Dutch, French, German, Italian, Japanese, Portuguese and Spanish; new AI Max reporting feature for the Search ads journey; help article on testing AI Max against DSA with experiments; in-account notices invite voluntary DSA upgrades | [Official, Google Ads and Commerce blog 2026-09; Search Engine Roundtable 2026-09-23] |
| 2026-09 | Small test: exact and phrase keywords in standard Search can serve text ads in AI Mode for explicit intent | [Official, Ads Liaison via trade press, 2026-09] |
| 2026-10 | New AI Max reporting columns show targeting, location and brand settings across campaigns | [Practitioner report, Search Engine Land 2026-10] |
| 2027-01 (planned) | Creation of new DSA campaigns ends | [Official via Ads Liaison as reported by Search Engine Roundtable, 2026-06; not yet on a help page as of 2026-10] |
| 2027-02 (planned) | Auto-migration of remaining DSA campaigns to AI Max | [Official, Google Ads Liaison and Google Ads Developer Blog, 2026-06] |

How each legacy setting was mapped in the 2026 upgrade [Official, Google DSA and AI Max announcement]:
| Legacy setting | AI Max features turned on |
|---|---|
| Automatically created assets | Search term matching and text customization (final URL expansion may also be enabled because it depends on text customization) |
| Campaign-level broad match | Search term matching only. Text customization and final URL expansion stay off |
| Dynamic Search Ads (when migrated) | Search term matching, text customization and final URL expansion, with legacy URL targeting preserved as URL controls |

Audit implication: any Search campaign that had ACA or campaign-level broad match on 2026-08-31 is now running AI Max. Check each one: which features are on, whether brand exclusions and URL exclusions exist, and what share of spend moved to AI Max matched terms.

## 3. Reporting

| Report | Where | What to look at |
|---|---|---|
| Search terms report with match type "AI Max" and a source column | Insights and reports, Search terms | Spend share, CPA and ROAS of AI Max terms vs keyword terms. Source shows whether the term came from broad match expansion or keywordless matching [Official, 2025 and 2026]. API: `segments.search_term_match_source` (AI_MAX_KEYWORDLESS, AI_MAX_BROAD_MATCH), see Q3b |
| AI Max columns (2026-10) | Campaigns table, columns | Which AI Max targeting, location and brand settings each campaign uses; use for the post-upgrade inventory |
| Landing pages report with a "Selected by" column | Landing pages | Performance of pages chosen by final URL expansion vs your final URLs |
| Search term, headline and landing page combinations | AI Max reporting, API `ai_max_search_term_ad_combination_view` | Which generated headlines and expanded URLs serve for which queries |
| Asset report | Ads and assets | Generated assets ("Automatically created" source) with performance |
| Experiments | Campaigns, Experiments, AI Max experiment | Incremental conversions and value vs control |

Privacy thresholds hide low-volume terms in every search terms report. Not every query that spends will be visible.

## 4. When to turn AI Max on

Decision tree:
1. Is conversion tracking verified and is the primary goal a real business outcome? No: do not enable. Fix tracking.
2. Is the campaign on conversion-based Smart Bidding (Maximize conversions or value, with or without targets)? No: do not enable.
3. Does the campaign get at least 30 conversions in 30 days, or share a portfolio that does? No: enable search term matching only on the broadest ad groups, or wait.
4. Is the website accurate, current and compliant? No: keep text customization and final URL expansion off. Google's Ads Liaison has advised against text customization when landing pages are outdated or inaccurate. [Official commentary, 2025]
5. Is the business regulated (health, finance, legal, gambling, pharma, alcohol) or bound by strict brand or legal copy? Yes: search term matching may be acceptable, keep text customization off unless text guidelines and text disclaimers cover your requirements and legal approves.
6. Are there pages you never want as landing pages (careers, blog, login, support, out of stock, policy pages)? Add URL exclusions before turning on final URL expansion.
7. Run an AI Max experiment (50/50) for 4 to 6 weeks. Adopt only if incremental conversions or value meet the target efficiency.

Recommended feature mix by business model:
| Business model | Search term matching | Text customization | Final URL expansion |
|---|---|---|---|
| Ecommerce with large catalog and clean site | On | On with text guidelines | On with URL exclusions (blog, help, account, out of stock collections) |
| Lead gen with few landing pages | On after experiment | Test | Off (send traffic to dedicated landing pages, not the site) |
| B2B SaaS | On for category themes only, off for competitor ad groups | Off or text guidelines strict | Off unless product pages are strong |
| Local services | On with locations of interest | Optional | Off unless service pages per city exist |
| Regulated verticals | Experiment carefully | Off by default | Off by default |
| Marketplace or large inventory | On | On | On with URL inclusions and exclusions (replaces DSA) |

## 5. Controls checklist after enabling or after auto-upgrade

1. Brand exclusions: add your own brand list to non-brand AI Max campaigns (unless you intentionally run brand in this campaign). Add competitor brand lists only if you do not want competitor queries.
2. Negative keywords: the shared lists still apply. Re-run the n-gram analysis after 14 days of AI Max traffic.
3. Ad group level: turn off search term matching in ad groups that must stay tight (competitors, regulated products, high CPC exact themes).
4. URL exclusions: careers, blog (unless content converts), login, account, support, legal, out of stock, internal search results.
5. Text guidelines: exclude terms you cannot claim (cheapest, guaranteed, best, cure, free if not free) and add messaging restrictions.
6. Text disclaimers: add for regulated copy requirements.
7. Locations of interest: use only when the queries name places that matter (travel, real estate, local services).
8. AI Brief (if in beta): describe the audience, what you sell, what not to say, which queries to avoid.
9. Document the state (features on and off, lists attached) in the journal with the date.

## 6. Measuring incrementality of AI Max

AI Max can claim conversions that exact or phrase keywords would have won anyway. Judge it on incremental value, not on its own column.

Method A: AI Max experiment (preferred). Built in, splits traffic, reports differences in conversions, value, CPA, ROAS. Run 4 to 6 weeks, 50/50 split, do not change the campaign during the test.

Method B: pre-post with a control group when an experiment is not possible (auto-upgraded campaigns). Compare the upgraded campaign's total conversions and CPA for 4 weeks before and after, against a control campaign of similar type that was not upgraded, adjusted for seasonality. Weak evidence; label as such.

Method C: query overlap analysis. From the search terms report, take AI Max terms that are close variants of existing keywords. Their spend is likely cannibalized, not incremental.

Adopt AI Max when: incremental conversions at a marginal CPA within 1.2x target (or marginal ROAS within 0.8x target), with no brand or compliance issues in the generated copy.

## 7. Broad match without AI Max

Broad match plus Smart Bidding is still the core of non-brand Search for accounts with data:
- Use with tCPA or tROAS. Never with Manual CPC.
- Keep exact match for brand and top money queries to gain query priority.
- Pair with shared negative lists and weekly search term reviews.
- Broad match uses signals such as the other keywords in the ad group and the landing page content. Keep ad groups thematically tight so those signals point the right way.
- Brand lists can restrict broad match to brand queries (brand campaign using broad with brand inclusions) or exclude brands. Since 2025-07 new brand lists on Search require AI Max.

## 8. AI Max for Shopping and Travel (2026 betas)

- AI Max for Shopping campaigns uses Merchant Center feeds to match longer, conversational queries. Closed beta, globally, all languages, announced 2026-04-30. [Official, 2026-04]
- AI Max for Travel consolidates hotel, flight and car rental formats into a Search-based setup. Closed beta. [Official, 2026-04]
- If invited: run as an experiment, check feed titles and descriptions first (hand off to commerce-feeds), compare query mix and ROAS vs the control.

## 9. AI Max and AI surfaces

AI Max, broad match, Shopping and PMax are the routes into ads in AI Overviews and AI Mode. Eligibility details are in [AI Overviews and AI Mode ads](ai-overviews-and-ai-mode-ads.md). An exact-match-only account has the least exposure to these surfaces.

## 10. Common AI Max failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| CPA up 20% or more after September 2026 | Auto-upgrade expanded matching; search terms from keywordless matching with poor intent | Review AI Max terms, add negatives, turn off search term matching in weak ad groups, run an experiment to decide |
| Brand queries showing in non-brand AI Max campaign | No brand exclusion | Add brand list exclusion; keep brand campaign with exact brand keywords |
| Traffic sent to blog or careers pages | Final URL expansion without exclusions | URL exclusions; or turn off final URL expansion |
| Off-brand or non-compliant generated headlines | Text customization without guidelines | Text guidelines, pin critical copy, or turn text customization off |
| AI Max spends but reports few conversions | Weak landing pages or wrong matching | Landing pages report "Selected by", exclude bad URLs |
| Ads appearing for other cities | Locations of interest or Presence or interest location option | Set location option to Presence; review locations of interest |
| API errors when managing assets after enabling | Automation not updated for AI Max fields | Update to a current API version; check the AI Max getting started guide |

## 11. Change list template (for approval)

```
Campaign: US_EN_SRCH_NB_Running-Shoes_tROAS_v3
Current: AI Max ON since 2026-09-14 (auto-upgrade from ACA). Search term matching ON, text customization ON, final URL expansion ON. No brand exclusions. No URL exclusions.
Evidence: last 28 days, AI Max terms = 31% of spend, ROAS 2.1 vs 4.4 for keyword terms (source: search terms report, export 2026-10-07).
Proposed:
1. Add brand list "Own brand" as brand exclusion.
2. Add URL exclusions: /blogs/*, /pages/careers, /account/*, /search*.
3. Turn off final URL expansion (keep text customization) for 4 weeks.
4. Create AI Max experiment 50/50 to compare AI Max on vs off from 2026-10-13 to 2026-11-10.
Risk: lower volume during test. Rollback: re-enable features.
Approval needed: yes.
```
