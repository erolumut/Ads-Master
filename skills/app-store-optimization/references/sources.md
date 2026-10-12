# Sources (annotated)

> Compiled 2026-10-12 from the 2026-10-12 research notes (Apple and Google Play passes, search summaries only, no page read in full) and the sources moved from `mobile-app-growth` (2026-10-08 pass). "URL not recorded" means the notes named the publisher and date but did not capture a link; search by title before relying on it. Vendor studies have commercial interests and non random samples. The research narrative and the verification queue are in `research/app-store-optimization.md`.

How to read the "Supports" column: it names the claims a source backs and the label we gave them. A single source never earns more than [Unverified]; an official page seen only as a search summary never earns [Official] for a 2025 to 2026 change.

## Apple: official pages

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | App Store search | Apple Developer | https://developer.apple.com/app-store/search/ | ongoing, seen 2026-10-12 | Text relevance (name, subtitle, keywords, primary category) and user behavior (downloads, ratings); keyword field 100 characters, comma separated; do not repeat name or subtitle words or the category; promotional text does not affect search [Official, long standing] |
| 2 | Manage app tags | App Store Connect Help | https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags | seen 2026-10-12 | Tags built by LLMs from metadata with curation; deselect only; US only; deselecting all may hurt discoverability [Reported, 2026-10 with 16, 17] |
| 3 | Product Page Optimization | Apple Developer | https://developer.apple.com/app-store/product-page-optimization/ | ongoing | Up to 3 treatments, one test at a time, up to 90 days [Official] |
| 4 | Showcase your apps with new assets on the App Store | Apple Developer News | https://developer.apple.com/news/?id=ljpl7kyn | 2026-10-05 | Product page headers, search result assets, Asset Library, preview tool (moved from the 2026-10-08 pass) |
| 5 | WWDC26 App Store guide | Apple Developer | https://developer.apple.com/wwdc26/guides/app-store/ | 2026-06 | 2026 assets in custom product pages, PPO and Apple Ads; Asset Library; streamlined submission; Time Allowances (moved) |
| 6 | Manage your App Store assets | App Store Connect Help | https://developer.apple.com/help/app-store-connect/manage-app-information/manage-your-app-store-assets/ | 2026-10 | Asset Library roles and workflow, pre-approval (moved) |
| 7 | Apple Newsroom, WWDC26 announcement | Apple | URL not recorded | 2026-06-08 | New header and search result creative assets [Reported, 2026-10 with 4, 5] |
| 8 | WWDC26 session 205 | Apple Developer | URL not recorded (developer.apple.com/videos) | 2026-06 | Same assets, preview tool |
| 9 | Ratings and reviews overview | App Store Connect Help | https://developer.apple.com/help/app-store-connect/monitor-ratings-and-reviews/ratings-and-reviews-overview | ongoing | Review summaries, Report a Concern path, responses, rating reset (moved) |
| 10 | App Review Guidelines | Apple Developer | https://developer.apple.com/app-store/review/guidelines/ | ongoing | 2.3, 2.3.3, 2.3.7, 2.3.8, 2.3.10, 2.3.12, 4.1, 5.2, 5.6.1, 5.6.3 |
| 11 | Apple Developer News (feed) | Apple | https://developer.apple.com/news/ | 2025-01 to 2026-10 | Custom product pages to 70 with keywords (2025-10-29), independent In-App Event submission, 50 metadata languages (2026-03-31), App Store Connect analytics additions, iPhone Duo screenshot requirement (moved) |
| 12 | Getting featured on the App Store | Apple Developer | https://developer.apple.com/app-store/getting-featured/ (path taken from the page name in the notes; verify) | seen 2026-10-12 | Lead time "at least 2 weeks", up to 3 months ideal [Contested with 13] |
| 13 | Nominate your app for featuring | App Store Connect Help | URL not recorded | seen 2026-10-12 | Roles, nomination types, field limits, "at least 3 weeks" [Reported, 2026-10; lead time Contested] |
| 14 | Campaign links | App Store Connect Help | URL not recorded | ongoing | `pt` provider token, `ct` campaign token up to 30 characters, `mt=8` |
| 15 | Visual Intelligence documentation | Apple Developer | https://developer.apple.com/documentation/visualintelligence | 2026 | Scene passed to apps through App Intents (used by [On-device assistants](on-device-assistants.md)) |

## Apple: press and vendor coverage

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 16 | At WWDC, Apple says it will use AI to tag apps | TechCrunch via Yahoo Finance | https://finance.yahoo.com/news/wwdc-apple-says-ai-tag-181733246.html | 2025-06 | Tags announcement; ranking effect claims [Unverified] |
| 17 | TechCrunch follow up on App Store tags | TechCrunch | URL not recorded | 2025-06-14 | Tags coverage |
| 18 | App Store review summaries launch coverage | TechCrunch | URL not recorded | 2025-03-05 | LLM summaries, iOS 18.4, refreshed at least weekly |
| 19 | iOS 18.4 beta introduces AI powered review summaries in the App Store | Macworld | https://www.macworld.com/article/2628166/ios-18-4-beta-introduces-ai-powered-review-summaries-in-the-app-store.html | 2025-03 | Review summaries (moved) |
| 20 | iOS 27 Personalized Collections and App Notes | AppTweak | URL not recorded | 2026-06-15 | US English first, placement undocumented [Reported, 2026-10 with 21, 22] |
| 21 | Personalized Collections coverage | Gummicube | URL not recorded | 2026-06 | Same; tags ranking claims [Unverified] |
| 22 | Personalized Collections link post | Michael Tsai | URL not recorded | 2026-06 | Same |
| 23 | Do app stores read text in your screenshots? | Lomio | https://lomio.io/blog/do-app-stores-read-screenshot-text | 2026 | Test of 64 caption phrases across 8 apps (attributed to ConsultMyApp in the 2026-10-12 notes) [Contested] |
| 24 | The biggest App Store algorithm change is here | Appfigures | https://appfigures.com/resources/guides/app-store-algorithm-update-2025 | 2025-06 | Caption OCR indexing view [Contested] |
| 25 | Natural language App Store search report | BGR | URL not recorded | date not recorded | iOS 18.1 natural language search [Unverified] |
| 26 | Custom product pages raised to 70 | Adapty | URL not recorded | 2025-10 | 70 page cap [Contested: 70 vs 35] |
| 27 | Custom product pages raised to 70 | Moburst | URL not recorded | 2025-10 | Same |
| 28 | The App Store is getting even more ads in March 2026 | AppleInsider | https://appleinsider.com/articles/26/01/22/the-app-store-will-have-even-more-ads-in-march-2026-starting-with-the-uk | 2026-01-22 | Multiple ad slots from 2026-03-03, iOS 26.2+ (moved) |
| 29 | Apple will add more App Store search ads | Search Engine Land | https://searchengineland.com/apple-will-add-more-app-store-search-ads-466424 | 2025-12 | Announcement (moved) |
| 30 | App Store ad slots coverage | MacDailyNews, AppTweak, PPC Land, heise | URL not recorded | 2026-01-23 onward | UK first, all storefronts by end of March [Reported, 2026-10] |
| 31 | Brand keyword test with organic rank 1 | SplitMetrics | URL not recorded | 2025 to 2026 | Little harm, little gain from brand ads [Unverified] |
| 32 | Cross-localization test (9 secondary locales for the US) | AppTweak and Phiture | URL not recorded | 2022 | Storefront to locale mapping [Unverified, stale] |
| 33 | Mini Apps Partner Program coverage | Apple Developer News via coverage | https://developer.apple.com/news/ | 2025-11 | 15% commission; no discovery effect found [Reported, 2026-10] |

## Google Play: official pages

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 34 | I/O 2026: What's new in Google Play | Android Developers Blog | https://android-developers.googleblog.com/2026/05/io-2026-whats-new-in-google-play.html and https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play | 2026-05-19 | Ask Play overlay and Highlights, Play Shorts, Gemini keyword listings and CSV translation, Gemini app discovery, Engage SDK on listings, new metrics [Reported, 2026-10 with 48, 49] |
| 35 | Play Console Help answers 9898842, 9859152, 13393723 | Google | https://support.google.com/googleplay/android-developer/answer/9898842 (and the same path with 9859152, 13393723) | seen 2026-10-12 | Title 30, short 80, full 4000; full and half width count equally |
| 36 | Play Console Help answers 4448378, 9958766, 9042516 | Google | https://support.google.com/googleplay/android-developer/answer/4448378 (and the same path with 9958766, 9042516) | seen 2026-10-12 | Search weighs titles, developer names, descriptions, ratings, reviews, downloads; key text in the top half; padding can lead to suspension; no self nominations for featuring |
| 37 | Store listing experiments | Play Console Help 12053285 | https://support.google.com/googleplay/android-developer/answer/12053285 | seen 2026-10-12 | One default graphics or up to five localized experiments; two variants; install, open and pre-registration click metrics; 6 month auto stop [Reported, 2026-10 with 55, 56] |
| 38 | Custom store listings | Play Console Help 9867158; Google Ads Help 16742242 | https://support.google.com/googleplay/android-developer/answer/9867158 and https://support.google.com/google-ads/answer/16742242 | seen 2026-10-12 | Up to 50; targeting incl. buyer segments and App campaign ad group IDs; one per country; not auto translated |
| 39 | Ratings and reviews | Play Console Help 138230, 9898684 | https://support.google.com/googleplay/android-developer/answer/138230 (and 9898684) | ongoing | Recency weighting, no reset, one editable reply |
| 40 | Reply to reviews | Google Play Developer API | https://developers.google.com/android-publisher/reply-to-reviews | ongoing | Reply up to 350 characters; list returns the last 7 days [Official] |
| 41 | Android vitals | Android Developers | https://developer.android.com/topic/performance/vitals | ongoing | Crash 1.09%, ANR 0.47%, 8% per device, 28 days; discoverability effects |
| 42 | Vitals help answers 9844486, 17492799 | Play Console Help | https://support.google.com/googleplay/android-developer/answer/9844486 (and 17492799) | seen 2026-10-12 | Same thresholds and listing warnings |
| 43 | Excessive partial wake locks guide | Android Developers Blog | URL not recorded (android-developers.googleblog.com, 2025-09) | 2025-09 | 2 hours in 24 hours, over 5% of sessions, enforcement from 2026-03-01 [Unverified] |
| 44 | Play engagement tools | Google Play Console | https://play.google.com/console/about/engagement | seen 2026-10-12 | Promotional content and featuring chance, Play Points, 80 character tagline [Unverified] |
| 45 | AppFunctions | Android Developers | https://developer.android.com/ai/appfunctions | 2026 | Android 16+ API, Jetpack library, Gemini integration in private preview (used by [On-device assistants](on-device-assistants.md)) |
| 46 | Play In-App Review API | Android Developers | https://developer.android.com/guide/playcore/in-app-review | ongoing | Quota, no button trigger, no questions before the card (moved) |
| 47 | Developer Program Policy (Metadata policy) | Google Play Policy Center | https://play.google.com/about/developer-content-policy/ | ongoing | Title, icon, developer name restrictions [Official] |

## Google Play: press and vendor coverage

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 48 | I/O 2026 Play coverage | 9to5Google | URL not recorded | 2026-05-19 | Ask Play overlay, Play Shorts |
| 49 | I/O 2026 Play coverage | Android Central | URL not recorded | 2026-05 | Same |
| 50 | "Ask Play about this app" box spotted | Android Authority | URL not recorded | 2025-05 | Early Ask Play box [Unverified] |
| 51 | Ask Play input tests | AppTweak | URL not recorded | 2026 | Description, key features, website as inputs |
| 52 | Ask Play inputs | Phiture | URL not recorded | 2026 | Metadata, reviews, other Google context |
| 53 | Play "Users are saying" summaries | GSMArena | URL not recorded | late 2025 | Summary paragraph, chips, "Summarised by Google AI" |
| 54 | Play review summaries | Storyboard18 | URL not recorded | late 2025 | Same |
| 55 | New Google Play Console metrics for ASO | Yellowhead | https://www.yellowhead.com/blog/new-google-play-console-metrics-aso/ | 2026-08 | Experiment metric change (moved) |
| 56 | ASO Monthly 121 | Phiture | https://phiture.com/asostack/aso-monthly-121/ | 2026-08 | Experiment overhaul report (moved) |
| 57 | Metadata policy update coverage | Yellowhead, Android Central, XDA | URL not recorded | 2021 | Emoji, all caps, "free", "download now" limits |
| 58 | Gemini app actions beta (food delivery, grocery, rideshare; US and Korea) | InfoQ, heise | URL not recorded | 2026-02 | Agent actions in curated apps (used by [On-device assistants](on-device-assistants.md)) |

## AI discovery of apps

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 59 | Which sources do AI search engines cite when recommending mobile apps | AppTweak | https://www.apptweak.com/en/aso-blog/which-sources-do-ai-search-engines-cite-when-recommending-mobile-apps | 2026-05 | Store listings about 47.5% of ChatGPT cited sources for app prompts; 125k+ responses, US, method partly undisclosed [Study, 2026-05] |
| 60 | AI app discovery survey | AppTweak | https://www.apptweak.com/en/aso-blog/ai-app-discovery-survey | 2026-09 | 1,000 US adults, self reported: 58% used AI to find or choose an app; 59% check the store after an AI recommendation [Study, 2026-09] |

## Law and policy context (moved)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 61 | Trade Regulation Rule on the Use of Consumer Reviews and Testimonials (16 CFR Part 465) | US Federal Trade Commission | URL not recorded | effective 2024-10 | Ban on buying fake reviews and suppressing negative ones [Official] |
| 62 | Apple Ads Maximize Conversions and placements | Apple Ads | https://ads.apple.com/app-store/best-practices/maximize-conversions | 2026 | Context for paid search on the same page (owned by `mobile-app-growth`) |

## Tools (directories and vendor pages)

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 63 | App Store Connect MCP Server (yuraist) | Glama | https://glama.ai/mcp/servers/yuraist/appstoreconnect-mcp | 2026 | Community server [Unverified] (moved) |
| 64 | AppStore MCP Server (forgeopslabs) | mcpservers.org | https://mcpservers.org/servers/forgeopslabs/appstore-mcp | 2026 | Community server (moved) |
| 65 | play-console-mcp (wiseappsai) | Drio | https://www.getdrio.com/mcp/io-github-wiseappsai-play-console-mcp/md | 2026 | Read only mode (moved) |
| 66 | google-play-mcp (AgiMaulana) | Claude Marketplaces | https://claudemarketplaces.com/mcp/io.github.agimaulana/google-play-mcp | 2026 | Community server (moved) |

## Where the evidence is thin (feeds the verification queue)

- App Store tags: ranking or filter effect; inputs beyond metadata; whether the US only limit changed.
- Apple review summaries: storefront list, review threshold, refresh cycle, the API resource.
- Screenshot caption indexing: no controlled test since the 2026 asset changes.
- Custom product page cap: 70 vs 35 in the live console.
- Featuring lead time: 2 vs 3 weeks.
- 2026 header and search result assets: specs, OS versions, storefronts.
- Play wake lock enforcement and thresholds.
- Ask Play inputs and markets; Gemini app discovery rollout.
- Cross-localization mapping for the 11 languages added in 2026-03.

## Source hygiene for this package

1. Before a G3 change rests on a claim marked [Reported] or [Unverified], read the official page in full or check the live console, and record the result with the `ads-verify` skill in `ads-master/VERIFIED.md`.
2. Vendor tests (AppTweak, Phiture, Gummicube, SplitMetrics, Yellowhead, ConsultMyApp) are useful early signals; record sample, method and date with every number taken from them.
3. When an official page and a vendor disagree, the live console wins for that account, then the official page, then the vendor.
4. Add new sources here with a number, date and the label they support; never renumber existing rows.
