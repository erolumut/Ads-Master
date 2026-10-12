# ASO Playbooks

> Knowledge as of 2026-10. Every play ends in a change request for human approval. Drafts in `ads-master/` are G1; unsubmitted versions, pages, events and listings are G2; submitting metadata, publishing listings, starting experiments, replying to reviews, deselecting tags and sending nominations are G3. Follow the project's automation stage in `ads-master/GUARDRAILS.md`.

Plays: 1 Launch, 2 Plateau, 3 Rating crisis, 4 New market, 5 Seasonal, 6 Weekly loop, 7 Organic drop recovery, 8 Change request template.

## Play 1: Launch (8 weeks before to day 90)

Entry: an app with a release date, PROJECT_BRIEF facts and the App entity section of PRODUCT_FACTS filled.

### Weeks minus 8 to minus 4
1. Term map v1 for the launch storefronts and locales ([Keyword research](keyword-research-and-rank-tracking.md) section 2): 50 to 150 terms, relevance first, competitor terms as `paid_only`.
2. Metadata v1 per store and locale ([App Store](app-store-search-and-metadata.md) section 3, [Google Play](google-play-search-and-listing.md) section 3); description written as the plain fact sheet (people and AI readers).
3. `aso_metadata_check.py` and `compliance` on every draft.
4. Screenshot concepts: two versions of frames 1 to 3 (v1 and v2) so the first PPO or Play experiment is ready on day 15.
5. Featuring nomination (App Launch type) submitted at least 6 to 8 weeks out where possible; never later than the Apple minimum ([Featuring](featuring-events-and-promotional-content.md) section 1). G3.
6. Pre-orders (App Store) or pre-registration (Play) with a custom store listing for pre-registered users; the paid side (ACpre) belongs to `mobile-app-growth`.

### Weeks minus 4 to 0
1. Localization for the top 3 markets by score ([Localization](localization-and-market-expansion.md) section 4).
2. Rating plan with the app team: ReviewGate rules, success moments, feedback entry in settings ([Ratings](ratings-reviews-and-ai-summaries.md) section 3).
3. Reply templates approved by `compliance`; reply owner and SLA agreed.
4. Rank tracking set up for every live and candidate term; baseline starts at launch.
5. Campaign links (`pt`, `ct`) and UTM links for the website and partners ([App web presence for AI](app-web-presence-for-ai.md)).
6. Change request for the launch metadata (G3), approved and logged.

### Days 0 to 14
1. Read back the live listing in every storefront.
2. Daily: crashes and ANRs, first reviews (reply within the SLA), store availability.
3. No metadata changes in the first 14 days unless something is wrong (indexing settles; the read needs a clean baseline).
4. Record the first tag set (US) and whether a review summary appears yet.

### Days 15 to 45
1. First PPO or Play experiment on screenshot frames 1 to 3 (concept level).
2. First keyword read: day 14 and 28 after launch for every term; move unranked high relevance terms, drop terms with impressions but low conversion.
3. First metadata change set (one per locale), logged with control terms.
4. Custom product pages and custom store listings for the top 2 search clusters and the first paid ad groups (with `mobile-app-growth`).

### Days 46 to 90
1. Second locale wave.
2. In-app event or promotional content for the first content drop.
3. Review themes monthly; first featuring request for a major update if the product earns it.
4. Write the 90 day ASO review: ranks, conversion by source, rating health, tests and learnings, next quarter plan.

Exit: term map stable, conversion by source at or above the first 30 days, rating 4.0 or higher, two tests closed.

## Play 2: Plateau (organic installs flat for 8 weeks or more)

1. Confirm it is a plateau: year over year, category trend (ASO tool), no measurement break, no lost featuring.
2. Decompose organic downloads: impressions by source x conversion by source. The constraint is the factor that stopped growing.
3. If impressions are flat:
   - Ranks: terms stuck at 11 to 30 with high popularity are the next target (metadata change set, CPP keyword pages for terms already ranked).
   - Coverage: clusters with no term ranked: new terms or new locales.
   - Ad pressure: more Apple Ads slots above you on core terms ([App Store](app-store-search-and-metadata.md) section 7): consider with `mobile-app-growth` whether brand or category defense pays.
   - Browse: events, nominations, promotional content.
4. If conversion is flat or falling:
   - Creative: screenshot concept test, 2026 search result asset, icon.
   - Rating health and summary text: a negative theme leading the summary.
   - Mix: more low intent sources (browse, referrals) lowering the blend.
5. If both are healthy, the market is saturated in current storefronts: new markets (Play 4) and new clusters adjacent to the core job.
6. Pick 2 bets by impact x confidence x ease; run each as an experiment with a stop rule.

## Play 3: Rating crisis

Trigger: rating down 0.2 or more in 7 days, a 1 star surge, or `review_themes.py` exit 1 (a negative theme up 5 points). Both triggers are stop conditions in `ads-master/INCIDENTS.md`.

| Step | Time | Action | Owner | Gate |
|------|------|--------|-------|------|
| 1. Detect | Hour 0 | Confirm with both stores' data; run `review_themes.py` on the last 35 days | app-store-optimization | G0 |
| 2. Declare | Hour 1 | Incident row in INCIDENTS.md; journal alert; tell the human | app-store-optimization | G1 |
| 3. Diagnose | Hours 1 to 24 | Release date vs theme start; crash and ANR rates (Xcode Organizer, Android vitals); backend status; price, paywall or policy change | App team, mobile-app-growth | G0 |
| 4. Contain | Day 1 | Pause rating prompts on the affected version (app team remote config); ask `mobile-app-growth` to pause paid traffic to a broken flow; hold promotional text and events that send traffic to it | App team, mobile-app-growth | G3 |
| 5. Communicate | Day 1 to 2 | Approved reply template for the theme on every affected review; status note in promotional text if useful (G3) | app-store-optimization drafts | G3 |
| 6. Fix | As fast as the app team ships | Hotfix release; expedited review request on Apple only for a real incident | App team | G3 |
| 7. Reply again | Fix day | Edit replies with the fix version | app-store-optimization drafts | G3 |
| 8. Rebuild | Fix day + 3 | Re-enable prompts for users who completed the fixed flow | App team | G3 |
| 9. Watch | Weekly until recovered | Theme share back below the pre-incident level; summary text recorded weekly | app-store-optimization | G0 |
| 10. Learn | After recovery | Post-incident note; QA gap to the app team; memory entry if the pattern repeats | app-store-optimization | G1 |

Never: ask for 5 star reviews, sentiment gate the prompt, reset the Apple rating as a cover, or reply with promises about unreleased fixes. An Apple rating reset is a human decision after a real rebuild, never during an incident ([Ratings](ratings-reviews-and-ai-summaries.md) section 4).

## Play 4: New market

1. Score candidate storefronts ([Localization](localization-and-market-expansion.md) section 4); human approves the wave.
2. Readiness gate with `compliance` (age rating, licensing, claims) and the product team (language support, payments).
3. Native keyword research per locale; term map rows; competitor listings from `market-intel`.
4. Metadata, screenshots and previews per level (L2 to L4); `aso_metadata_check.py` per locale (bytes for non Latin scripts).
5. Submit per storefront (G3); read back; canary test if relying on Apple cross-localization.
6. Reply templates in the language; review themes taxonomy extended with local words.
7. Read day 14 and 28 against English control terms in that storefront.
8. Hand off to `mobile-app-growth` for paid launch when local conversion holds.

## Play 5: Seasonal moment

Examples: New Year, back to school, Ramadan, Black Friday, a sports final, the app's own anniversary.

| When | Action |
|------|--------|
| 10 to 12 weeks before | Pick the moment and the job it serves; check last year's data (memory, journal) |
| 8 weeks before | Featuring nomination if the content is real (Apple); event and promotional content plan; seasonal CPP brief |
| 6 weeks before | Seasonal terms in the term map (popularity history from Google Trends and the ASO tool); decide whether a metadata change set is worth it (only if seasonal terms are high relevance and the season lasts more than 4 weeks) |
| 4 weeks before | Assets through the Asset Library and Play promotional content drafts; compliance on offers |
| 2 to 3 weeks before | Submit events, seasonal CPP, promotional content (G3); seasonal metadata change set if chosen |
| During | Promotional text updated; reply SLA tightened; daily review check |
| End date | Promotional text and events end on time; revert seasonal metadata in the next release |
| 2 weeks after | Read: event metrics, seasonal term ranks, conversion by source vs last year; memory if confirmed |

Rule: seasonal metadata is a change set like any other: logged, with control terms and a planned revert.

## Play 6: Weekly ASO loop (Growth tier)

| Step | Time | Detail |
|------|------|--------|
| 1. Data | 10 min | Exports or connectors; note the date range and changes in the period |
| 2. Funnel | 10 min | Impressions, views, conversion and downloads by source and store vs the prior 4 weeks |
| 3. Ranks | 10 min | Term map buckets, movement vs control terms, open reads due this week |
| 4. Reviews | 15 min | `review_themes.py`; replies due; summary text changes |
| 5. Tests and pages | 10 min | PPO and Play experiments status; CPP and CSL registry; reads due |
| 6. Vitals and incidents | 5 min | Android vitals, wake locks, crash themes |
| 7. Competitors | 5 min | Metadata and creative changes from the ASO tool |
| 8. Change requests and journal | 10 min | Draft, route to compliance, request approval; handoffs |

At Starter tier, run it every 2 weeks; keep the daily review check.

## Play 7: Organic drop recovery

1. Scope: which store, storefront, source and terms? Organic search only, or browse too?
2. Availability: app live in all storefronts, no review hold, no removal, compatible with current OS versions.
3. Changes: metadata, creative or category changes in the last 28 days (change log). A drop across many terms within days of a metadata change points to it: prepare the revert from `from_value` (G3).
4. Quality gates: crash, ANR and wake lock rates; a vitals breach explains a Play drop.
5. Ratings: rating drop or a new negative theme in the summary.
6. Market: control terms moved too (algorithm, seasonality), more ad slots on core terms, a competitor launch or featuring.
7. Act on the cause; log the incident if a stop condition applies; read again after 14 days.

## Play 8: Change request (all ASO changes)

Use `ads-master/templates/CHANGE_REQUEST.md`. One line per change:

| # | Store and storefront | Entity | Change | From | To | Reason with data (source, range) | Expected effect | Risk | Rollback | Gate | Approval |
|---|----------------------|--------|--------|------|----|----------------------------------|-----------------|------|----------|------|----------|
| 1 | App Store US en-US | Version 4.13 keyword field | Replace 3 terms | `...,todo,widget,...` | `...,mood,journal,...` | Term map 2026-10-01: mood cluster unranked, popularity 3 of 5 | Mood journal rank 11 to 30 by day 28 | Lose rank on "todo" (rank 64, low value) | Revert to previous text from the change log | G3 | |
| 2 | Google Play | Custom store listing CSL-03 | Publish keyword listing | none | draft v1 | Search term "expense tracker" conversion 30% below average, 28 days | Conversion +15% relative on the term | None until published | Unpublish | G3 | |
| 3 | App Store US | Tag "Budgeting" | Deselect | selected | deselected | App has no budgeting feature (PRODUCT_FACTS row 12) | Fewer mismatched searchers | Unknown discoverability effect | Reselect | G3 | |

Read back every executed change and log it with a timestamp in the journal and the metadata change log.
