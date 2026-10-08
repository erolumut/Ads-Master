# Research Dossier: SEO (Google and Bing), October 2026

> Prepared 2026-10-08 for the Ads Master `seo` package. Evidence labels: [Official, YYYY-MM], [Study, YYYY-MM], [Practitioner consensus], [Contested], [Unverified]. Numbers carry source and date. Benchmarks vary by vertical, geo, season and query mix; compare a project against its own history first.

## Research method and limits
- 19 web searches were run (extended mode for 2025 to 2026 events) before a shared, session wide search budget was exhausted. Direct page fetching (WebFetch and curl) was blocked by the environment's network policy, so primary pages could not be opened; findings rely on search result syntheses of primary and secondary sources plus long standing official documentation known before this pass.
- The brief asked for at least 35 searches. That target was not met for the reason above. Claims that could not be confirmed this pass are labeled [Unverified]. A re-check list is in "Open questions and watch list".
- Verification pass (2026-10-08): about 20 additional extended web searches re-checked the Generative AI report (AI Mode split, API), the AI features control rollout, UK CMA conduct requirements and dates, the Googlebot file size documentation, structured data deprecations after June 2025, official MCP servers, Bing AI Performance after June 2026, Google I/O 2026 figures, Gemini model changes, preferred sources, AI Mode in France, google.com/goto links and the September 2026 spam update. Labels were upgraded or corrected where confirmed; Search Console and Bing facts now match the ai-search-optimization package.
- Source priority applied: Google and Microsoft documentation and blogs, then data studies with stated methods (Pew, Seer, Ahrefs, Amsive, Similarweb, the num=100 analysis), then industry press (Search Engine Land, Search Engine Journal, Search Engine Roundtable, PPC Land) for dates.

## 1. Executive summary
1. Google shipped five broad core updates in the period (March 2025, June 2025, December 2025, March 2026, May 2026), a first ever Discover only core update (February 2026, still US English only), and five spam updates (August 2025; March, June, August and September 2026). The September 2026 spam update completed on 2026-10-08 at 4:37 am ET after about 14 days [Official, Search Status Dashboard].
2. No broad core update was confirmed after May 2026 (through 2026-10-08) despite many blogs claiming July or August ones; treat those as unconfirmed volatility [Official, dashboard].
3. AI Overviews cut clicks on informational queries. Estimates range from about 15% lower CTR (Amsive, April 2025) to 34.5% (Ahrefs, April 2025), 58% (Ahrefs, December 2025 data) and 61% (Seer, data to September 2025). Pew found 8% vs 15% click rates with vs without an AI summary (March 2025 data) [Study].
4. The decline flattened in early 2026: Seer's v3 study (published 2026-04-24) shows organic CTR on AI Overview SERPs rising from about 1.3% (December 2025) to 2.4% (February 2026), still below non-AIO SERPs [Study, 2026-04].
5. Google now reports AI feature impressions: a Generative AI performance report (beta, launched 2026-06-03, all sites worldwide since 2026-08-31) shows impressions only, AI Overviews and AI Mode combined, by page, country and date (Discover has a separate report). No clicks, queries or AI Mode split, and no API or BigQuery export as of 2026-10 [Official, 2026-06 and 2026-08].
6. Site owners can exclude a site from AI Overviews, AI Mode and Discover AI features with a property-level Search Console setting (Include by default, Exclude, Inherit from parent) introduced 2026-06-03, without removing classic snippets; Google says it is not a ranking signal. It reached all websites worldwide on 2026-08-31 (no country restriction). The control implements the UK CMA publisher controls conduct requirement (imposed 2026-06-03; page-level controls due by about 2027-03) [Official, 2026-06 and 2026-08].
7. Google stopped honoring `num=100` around 2025-09-10 to 09-15. In a 319 property analysis 87.7% of sites lost Search Console impressions and 77.6% lost unique queries; average position improved. It is a measurement change, not a traffic change [Study, 2025-09].
8. Search Console gained more analysis features in 15 months than in the prior five years: hourly API data (2025), query groups (2025-10), custom annotations and branded query filter (2025-11, broader 2026-03), AI powered configuration and weekly or monthly views (2025-12), social channels (2025-12), Generative AI reports (2026-06) [Official].
9. Bing launched AI Performance in Bing Webmaster Tools (public preview, 2026-02-10): citations in Copilot and Bing AI answers, cited pages and grounding queries; grounding query to page mapping (2026-03-23); Intents, Topics, Citation Share and Compare (2026-06-16). No clicks and no API as of 2026-10 [Official, 2026-02 to 2026-06].
10. The winning playbook did not change in kind but in emphasis: technical correctness in raw HTML, fewer and better pages with information gain, bottom of funnel and commercial intent first, internal linking, earned brand mentions, and measurement by non-branded clicks and revenue per cluster rather than impressions or average position.

## 2. State of the channel in 2026
| Dimension | Data point | Source |
|-----------|-----------|--------|
| AI Overviews reach | 2 billion+ monthly users (July 2025); over 2.5 billion (Google I/O 2026, 2026-05-19) | [Official, 2025-07 and 2026-05] |
| AI Mode reach | 100 million+ monthly active users in US and India (July 2025); over 1 billion monthly users (I/O 2026, repeated on the 2026-07-22 earnings call); still only 0.34% of US Google searches January to April 2026 per SparkToro clickstream | [Official, 2025-07 and 2026-05]; [Study, 2026] |
| AI Mode availability | US 2025-05-20; 180+ countries in English by August 2025; 40+ more countries and 35+ languages on 2025-10-07; 53 more languages 2026-02; about 200 countries and 98 languages targeted at I/O 2026; France from 2026-07-22 | [Official, 2025 to 2026] |
| AI Overviews query type | 99.2% of AIO triggering keywords informational (Ahrefs sample) | [Study, 2025-04] |
| CTR effect of AIO, position 1 | 34.5% lower (Ahrefs, March 2025 data); 58% lower (Ahrefs, December 2025 data) | [Study, 2025-04; 2026-02] |
| CTR on AIO SERPs (informational) | 1.76% to 0.61% organic (Seer, mid-2024 to Sept 2025); rebound to 2.4% in Feb 2026 | [Study, 2025-11; 2026-04] |
| Click behavior | 8% of visits with AI summary clicked a traditional result vs 15% without; 1% clicked a link inside the summary; 26% vs 16% ended browsing | [Study, Pew 2025-07] |
| News zero-click | 69% of news related searches ended without a click to a news site in May 2025 vs 56% a year earlier | [Study, Similarweb 2025-07] |
| Google's position | Total organic clicks "relatively stable" year over year and higher quality clicks | [Official, 2025-08; Contested by publishers] |
| Search Console data | Impressions and query counts reset lower after num=100 (September 2025) | [Study, 2025-09] |
| Google search market share | Around 90% globally, dipping below 90% in late 2024 for the first time in about a decade per StatCounter | [Unverified this pass] |
| US zero-click rate | 68.01% of Google searches January to April 2026 vs 60.45% in 2024 | [Study, 2026] (SparkToro with Similarweb) |
| Regulation | US remedies ruling 2025-09-02 (no Chrome divestiture, data sharing and exclusivity limits) [Unverified details this pass]. UK CMA strategic market status designation for general search (2025-10); publisher controls conduct requirement imposed 2026-06-03 (nine months to implement, about 2027-03; key parts earlier); fair ranking conduct requirement imposed 2026-06-17 (six months, about 2026-12; data portability three months); choice screen consultation opened 2026-09-23 (comments to 2026-10-09, decision by year end) [Official, 2026-06 and 2026-09]. EU: ChatGPT designated a Very Large Online Search Engine under the DSA on 2026-08-31 [Official, 2026-08] | Monitor |

### Search Console and Bing Webmaster Tools features added 2025 to 2026
| Date | Feature | What it enables | Limits | Label |
|------|---------|-----------------|--------|-------|
| 2025-04 | Hourly data in Search Console API | Near real time monitoring of launches and incidents | Recent days only | [Official; exact date Unverified] |
| 2025-06 | AI Mode counted in Performance (web) | AI Mode clicks and impressions included in totals | No filter to isolate | [Official, 2025-06] |
| 2025-10-27 | Query groups (Insights) | AI clusters of similar queries with group clicks, trending up and down | Large query volume properties only | [Official] |
| 2025-11 | Custom annotations | Mark releases and updates on charts (reported limits: 200 per property, 120 characters) | Delete, not edit | [Official, details secondary] |
| 2025-11-20 | Branded queries filter | AI classification of branded vs non-branded queries, including misspellings and brand products | Top level properties; eligibility; can misclassify | [Official] |
| 2025-12-04 | AI powered configuration (experimental) | Natural language to report filters and comparisons | Limited sites | [Official] |
| 2025-12-10 | Weekly and monthly views | Smoother trends; exports per view | Position averaged over period | [Official] |
| 2025-12 | Social channels (experimental) | Performance of linked social profiles in Search | Limited | [Official] |
| 2026-03-11 | Branded filter expanded to all eligible sites | Wider brand split | Same eligibility rules | [Official, secondary coverage] |
| 2026-06-03 | Generative AI performance reports (beta) | AI Overviews and AI Mode impressions combined by page, country, date (Discover separate) | Impressions only; no queries, clicks, AI Mode split or API; all sites worldwide from 2026-08-31 | [Official] |
| 2026-06 | "Search generative AI" setting | Exclude site from AI Overviews, AI Mode, Discover AI features | Property level (Include, Exclude, Inherit from parent); all sites worldwide from 2026-08-31 | [Official] |
| 2026-02-10 | Bing Webmaster Tools AI Performance (preview) | Citations, cited pages, grounding queries in Copilot and Bing AI answers | Citations only; sampled data; no API as of 2026-10 | [Official] |
| 2026-03-23 | Bing grounding query to page mapping | Query to cited pages and back | Verified sites | [Official] |
| 2026-06-16 | Bing Intents, Topics, Citation Share, Compare | Topic and competitor view of citations | Preview | [Official] |

### Spam policies in force (October 2026)
Cloaking; doorway abuse; expired domain abuse; hacked content; hidden text and links; keyword stuffing; link spam; machine-generated traffic; malware and malicious practices; misleading functionality; scaled content abuse; scraping; sneaky redirects; site reputation abuse; thin affiliation; user-generated spam; plus demotions for legal removals, personal information removals, policy circumvention, and scam and fraud [Official, spam policies]. No new policies were announced with the 2026 spam updates [Official coverage, 2026].

### Structured data support changes
- Removed or restricted before 2025: HowTo rich results (2023), FAQ rich results limited to authoritative government and health sites (2023-08), sitelinks search box (2024-11).
- Phased out 2025-06: book actions, course info, claim review, estimated salary, learning video, special announcement, vehicle listing [Official, 2025-06].
- Added or extended: product variants (ProductGroup, 2024), organization level return policies (2024), loyalty program (MemberProgram, member pricing) markup (2025-06) [Official].
- After June 2025: documentation for course info, estimated salary, learning video, special announcement and vehicle listing removed (2025-09); Practice problem removed from Search Console reports and the Rich Results Test (2026-01); Dataset markup limited to Dataset Search; FAQ rich results no longer shown from 2026-05-07 (Search Console FAQ reporting retired 2026-06, API support ended 2026-08) [Official, 2025-09 to 2026-05].

Implications:
- Informational content economics changed permanently. Commercial, transactional, local and branded intents carry a growing share of SEO value.
- Measurement must move to clicks and revenue by query class; impressions and position need context.
- Bing matters disproportionately for AI answers (Copilot and partners) relative to its search share.

## 3. Timeline of changes, January 2025 to October 2026
| Date | Change | Type | Label |
|------|--------|------|-------|
| 2025-01 | Quality Rater Guidelines update: generative AI, scaled content abuse, site reputation abuse, expired domain abuse, filler and exaggerated claims; Lowest for low effort AI or auto generated main content | Guidelines | [Official, 2025-01] |
| 2025-01 | Google requires JavaScript to load Search results; scrapers and some rank trackers disrupted | SERP access | [Practitioner consensus] |
| 2025-03 | AI Overviews on Gemini 2.0; AI Mode Labs experiment announced | AI features | [Official, 2025-03] |
| 2025-03-13 to 03-27 | March 2025 core update | Ranking | [Official] |
| 2025-04 | Search Console API hourly data | Search Console | [Official, 2025-04] |
| 2025-04 | Ahrefs (34.5%) and Amsive (15.5% average, non-brand 20%) AIO CTR studies | Studies | [Study] |
| 2025-05-20 | AI Mode available to all US users (I/O 2025) | AI features | [Official] |
| 2025-05 | Google guidance: succeeding in AI search experiences needs no special optimization | Guidance | [Official, 2025-05] |
| 2025-06 | AI Mode data counted in Search Console Performance (web) | Search Console | [Official, 2025-06] |
| 2025-06 | Google phases out seven structured data features (book actions, course info, claim review, estimated salary, learning video, special announcement, vehicle listing) | Structured data | [Official, 2025-06] |
| 2025-06-30 to 07-17 | June 2025 core update | Ranking | [Official] |
| 2025-07 | Similarweb zero-click data for news (69%) | Study | [Study, 2025-07] |
| 2025-07 | Google Analytics MCP server (official, read-only) | Tools | [Official, 2025-07] |
| 2025-07 | Web Guide Labs experiment; Google Trends API alpha announced | Features | [Unverified exact dates] |
| 2025-07-22 | Pew Research AI summary click study | Study | [Study] |
| 2025-08 | Google Search blog: organic clicks relatively stable, higher quality clicks | Statement | [Official, 2025-08] |
| 2025-08 | Preferred sources for Top Stories (US, India) | SERP | [Official, 2025-08; expansion Unverified] |
| 2025-08-11 | Microsoft retires public Bing Search APIs | Tools | [Official, announced 2025-05] |
| 2025-08-26 to 09-22 | August 2025 spam update (about 27 days) | Ranking | [Official] |
| 2025-09-10 to 09-15 | num=100 parameter stops working; GSC impressions drop | Measurement | [Study] |
| 2025-09 | Quality Rater Guidelines update (AI Overview examples, YMYL refinements) | Guidelines | [Official, 2025-09; details Unverified] |
| 2025-09 | Chrome DevTools MCP public preview | Tools | [Unverified exact date] |
| 2025-10-07 | AI Mode expands to 40+ countries and 35+ languages | AI features | [Official, via PPC Land] |
| 2025-10-27 | Search Console Insights query groups | Search Console | [Official] |
| 2025-11 | Search Console custom annotations; Seer v2 study (61%) published | Search Console; Study | [Official]; [Study] |
| 2025-11-20 | Search Console branded queries filter (AI classification) | Search Console | [Official] |
| 2025-11-18 | Gemini 3 in AI Mode | AI features | [Official, 2025-11] |
| 2025-12-04 | Search Console AI powered configuration (experimental) | Search Console | [Official] |
| 2025-12-10 | Search Console weekly and monthly views | Search Console | [Official] |
| 2025-12 | Search Console social channels (experimental); AI features in Discover reported | Search Console; Discover | [Official]; [Unverified] |
| 2025-12-11 to 12-29 | December 2025 core update | Ranking | [Official] |
| 2026-01 | Practice problem structured data removed from Search Console reports and Rich Results Test | Structured data | [Official, 2026-01] |
| 2026-01-27 | Gemini 3 becomes the default model for AI Overviews | AI features | [Official, 2026-01] |
| 2026-02 | Googlebot documentation: 2 MB fetch limit for HTML and text files (64 MB PDF), 15 MB default for other crawlers; expanded 2026-03-31 | Crawling | [Official, 2026-02] |
| 2026-02 | Ahrefs update: 58% lower position 1 CTR with AIO (December 2025 data) | Study | [Study, 2026-02] |
| 2026-02-05 to 02-27 | February 2026 Discover core update (US English first): local relevance, less clickbait, more in-depth expert content | Ranking (Discover) | [Official, 2026-02] |
| 2026-02-10 | Bing Webmaster Tools AI Performance (public preview) | Bing | [Official] |
| 2026-03-11 | Branded queries filter expanded to all eligible sites | Search Console | [Official, secondary coverage] |
| 2026-03-23 | Bing grounding query to page mapping | Bing | [Official, 2026-03] |
| 2026-03-24 to 03-25 | March 2026 spam update (about 19.5 hours) | Ranking | [Official] |
| 2026-03-27 to 04-08 | March 2026 core update | Ranking | [Official] |
| 2026-04-24 | Seer v3: AIO SERP CTR rebound to 2.4% | Study | [Study] |
| 2026-04-30 | Preferred sources available in all languages where Search is offered | SERP | [Official, 2026-04] |
| 2026-05-07 | FAQ rich results no longer shown in Google Search | Structured data | [Official, 2026-05] |
| 2026-05-19 | Google I/O 2026: AI Overviews over 2.5B and AI Mode over 1B monthly users; Gemini 3.5 Flash default in AI Mode | AI features | [Official, 2026-05] |
| 2026-05-21 to 06-02 | May 2026 core update | Ranking | [Official] |
| 2026-06-02 to 06-03 | Search Console AI features opt-out setting and Generative AI performance reports (subset first; UK tested first per reports) | Search Console | [Official, 2026-06] |
| 2026-06-03 | UK CMA publisher controls conduct requirement (AI features opt-out, fine-tuning opt-out, attribution); nine months to implement (about 2027-03) | Regulation | [Official, 2026-06] |
| 2026-06-17 | UK CMA fair ranking conduct requirement; six months to implement (about 2026-12) | Regulation | [Official, 2026-06] |
| 2026-06-16 | Bing AI Performance additions (Intents, Topics, Citation Share, Compare) | Bing | [Official, 2026-06] |
| 2026-06-24 to 06-26 | June 2026 spam update | Ranking | [Official] |
| 2026-07 | Claims of a July core update | Ranking | Not on the Search Status Dashboard; unconfirmed |
| 2026-07-22 | AI Overviews and AI Mode launch in France | AI features | [Official, 2026-07] |
| 2026-08-18 to 08-21 | August 2026 spam update | Ranking | [Official] |
| 2026-08-26 | Google confirms google.com/goto passthrough links on results | SERP | [Official, 2026-08] |
| 2026-08-31 | Generative AI report and AI features control available to all websites worldwide (AI Overviews and AI Mode impressions always combined; the 2026-09-07 "change" claim was not confirmed) | Search Console | [Official, 2026-08] |
| 2026-09-02 | Gemini 3.8 Flash selectable in AI Mode for Google AI Pro and Ultra subscribers | AI features | [Official, 2026-09] |
| 2026-09 | Search Console "AI Contribution" pilot pays about 100 invited publishers | Search Console | [Official, 2026-09] |
| 2026-09-23 | UK CMA choice screen conduct requirement consultation | Regulation | [Official, 2026-09] |
| 2026-09-24 to 10-08 | September 2026 spam update (about 14 days, completed 4:37 am ET; volatility October 4 to 6); no core update since May 2026 as of 2026-10-08 | Ranking | [Official] |

## 4. Best practice consensus
1. Technical correctness first: crawlable links, correct status codes, server rendered critical content and tags, clean canonicals, controlled facets, accurate sitemaps [Official docs; Practitioner consensus].
2. Content must add information gain: first-hand experience, original data, expert judgment; rewriting top results adds nothing [Official helpful content guidance; Practitioner consensus].
3. AI assistance is acceptable with human expertise and review; mass unreviewed AI content is scaled content abuse and rated Lowest by raters [Official, 2023 and 2025-01].
4. Third party content hosted to exploit a domain's signals is site reputation abuse regardless of first-party oversight [Official, 2024-11].
5. Internal linking to priority pages is the cheapest durable lever [Practitioner consensus].
6. Bottom of funnel and commercial intent pages first for revenue businesses [Practitioner consensus].
7. Measure non-brand clicks and conversions per cluster; annotate num=100 and updates; stop reporting raw impressions and average position as success metrics [Practitioner consensus].
8. Core Web Vitals (LCP 2.5 s, INP 200 ms, CLS 0.1 at p75) matter as tie breakers and for conversion [Official; Practitioner consensus].
9. Earned links and mentions through PR, data and partnerships; no paid links without qualification [Official spam policies].
10. Migrations need full redirect maps, staging QA and monitoring [Official site move docs; Practitioner consensus].
11. Local: primary GBP category, reviews and proximity dominate; fake reviews are illegal in major markets (US FTC rule effective 2024-10-21, UK DMCC Act from 2025-04-06) [Official].
12. Bing Webmaster Tools, sitemaps with accurate lastmod and IndexNow are cheap and increasingly relevant for AI answers [Official Bing guidance; Practitioner consensus].

### Implementation consensus for codebases
| Stack | Consensus practice | Most common failure found in audits |
|-------|-------------------|-------------------------------------|
| Next.js App Router | Server components for indexable content; `generateMetadata` per route; `app/sitemap.ts` and `app/robots.ts`; ISR for large catalogs; JSON-LD rendered server side with `<` escaped | Canonical set in root layout inherited by every page; content fetched client side; streaming responses returning 200 for not found states |
| React or Vue SPA without SSR | Migrate indexable routes to SSR or SSG; prerender as a bridge; dynamic rendering only as a temporary workaround | Hash routes, buttons instead of links, 200 status for unknown routes |
| Shopify | Accept forced URL prefixes; link canonical product URLs in collection grids; control tag and filter URLs; `seo.hidden` metafield to exclude pages | Duplicate collection product paths, app script bloat hurting INP, duplicate Product JSON-LD from apps |
| WordPress | One SEO plugin; noindex thin archives; page caching; core or plugin sitemap, not both | "Discourage search engines" left checked after launch; duplicate schema from theme and plugin |
| Webflow | CMS bound SEO fields; site level redirects; JSON-LD in head custom code with CMS fields | Unescaped CMS values breaking JSON-LD; staging subdomain indexed |
| Any CDN or WAF | Verify and allow Googlebot and Bingbot; serve cacheable HTML | Bot protection challenging crawlers (403, 429) after security changes |

## 5. Contested topics
| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Are AI Overviews reducing total organic clicks? | Google: total clicks relatively stable, higher quality (2025-08) | Pew, Seer, Ahrefs, Similarweb show large CTR declines on affected queries | Both can be true: query mix and impressions shifted. Plan on lower CTR for informational queries; measure your own |
| Is the AI Overview CTR decline still worsening? | Ahrefs February 2026 update: 58% and spreading to more markets | Seer April 2026: rebound to 2.4% CTR on AIO SERPs | Treat 2026 as stabilization with high uncertainty; re-baseline quarterly |
| Should sites opt out of AI features? | Protect content value and licensing leverage | Lose AI impressions and clicks while competitors fill answers; Top Stories effects | Default stay in; opt out only with data and leadership sign-off |
| Do links still matter much? | Google says fewer links needed than assumed | Practitioner tests and ranking correlations show links still differentiate competitive SERPs | Links are a multiplier for strong pages; earn, do not buy |
| Brand bias in core updates | Big brands and forums gained since 2023 | Google says it rewards helpfulness, not size | Build brand signals (reviews, mentions, navigational demand) as part of SEO |
| Subdomain vs subfolder | Google: both fine | Many migrations to subfolders show gains | Default subfolder |
| Leaked API attributes (2024) as ranking factors | Practitioners map attributes to tactics | Google: not all attributes used, weights unknown | Use as hypotheses, not playbook facts |
| GEO as a separate discipline | Vendors and some practitioners | Google: AI features need normal SEO | SEO foundation plus ai-search-optimization for assistant visibility |
| July and August 2026 core updates | Several blogs report them | The Search Status Dashboard shows none | Resolved: unconfirmed volatility |
| AI Mode reporting separation in the Generative AI report | One blog: combined only since 2026-09-07 | Google help page and most guides: AI Overviews and AI Mode combined from launch, filter only by text or multimodal search type | Resolved: combined, no split as of 2026-10 |
| Did Googlebot's file size behavior change in 2026? | Google (Mueller): documentation clarification, no behavior change | DebugBear: a Google contact said earlier docs were wrong and Googlebot reads only the first 2 MB | Plan for the documented 2 MB limit either way |

## 6. What top operators do differently
1. They diagnose by pipeline stage and by query class before touching content, and they quantify revenue at stake per fix.
2. They read code: they find the root layout canonical bug, the streaming 200 status, the client only rendered content, the WAF rule blocking Googlebot, in hours not weeks.
3. They classify every target query by intent and AI feature exposure and build their own CTR curves, so forecasts survive AI Overviews.
4. They prune and consolidate as aggressively as they publish; they gate programmatic pages behind data thresholds and index ratios.
5. They put SEO checks into CI and run daily diff crawls on key templates.
6. They run SEO split tests by page group and roll out only proven template changes.
7. They treat digital PR as a data product (original datasets, methodology pages) that also feeds AI citations.
8. They manage brand demand and reviews as SEO inputs.
9. They wait for rollouts to finish, separate artifacts (num=100, tracking), and communicate recovery timelines in core update cycles.
10. They use Bing Webmaster Tools AI Performance and Search Console Generative AI reports as early indicators for AI visibility work.

## 7. Common expensive mistakes
| Mistake | Cost | Prevention |
|---------|------|-----------|
| Launching a redesign or migration with noindex or `Disallow: /` from staging | Sitewide deindexing within days | Environment specific config, launch smoke tests |
| Incomplete redirect maps (homepage or category catch-alls) | Lost rankings and links for months | URL universe from all sources, 1:1 mapping, validator |
| Root layout canonical inherited by every page (Next.js) | Pages dropped as duplicates | Per route canonicals, crawl check |
| Client side rendered content and links | Partial indexing, invisibility to Bing and AI crawlers | SSR, SSG or ISR for indexable routes |
| Mass AI or programmatic content without gates | Scaled content abuse demotion, sitewide quality loss | Gates, review, batch rollout, kill switch |
| Hosting partner coupon or casino sections on a news or edu domain | Site reputation abuse manual action | Section operator audit |
| Buying links or niche edits | Wasted spend, manual actions | Earned links only |
| Reporting impressions and average position across the num=100 boundary | False narratives of collapse or improvement | Annotate, use clicks |
| Treating every drop as an algorithm update | Wrong fixes | Diagnosis procedure, regression checks first |
| Indexing all facet combinations | Crawl waste, duplicate clusters | Facet matrix and gates |
| Keyword stuffed GBP names and fake reviews | Suspensions, legal exposure | Guidelines compliance |
| Opting out of AI features or adding nosnippet sitewide without analysis | Lost visibility and clicks | Data review and approval |
| Blocking the AI Training class at Cloudflare (or leaving the legacy Block AI bots setting on) | Cloudflare applies the strictest rule to multi-purpose crawlers, so Googlebot and Bingbot can receive 403s; ad page defaults from 2026-09-15 are reported inconsistently [Contested] | Keep Training unblocked at the edge, use Google-Extended for Gemini training, monitor Crawl Stats |
| Chasing top of funnel volume outside the ICP | Traffic without revenue, AI Overview exposure | Opportunity scoring by value |

## 8. Benchmarks
All benchmarks vary by vertical, geo, season, device and query mix.

| Benchmark | Value | Source and date | Sample | Caveat |
|-----------|-------|-----------------|--------|--------|
| Click on traditional result with AI summary vs without | 8% vs 15% of visits | Pew Research, 2025-07 (March 2025 data) | 900 US adults, 68,879 searches | Panel, one month, AIO only |
| Click on link inside AI summary | About 1% of visits | Pew, 2025-07 | Same | Same |
| Position 1 CTR reduction with AIO | 34.5% | Ahrefs, 2025-04 | 300k keywords | Informational, correlation |
| Position 1 CTR reduction with AIO | 58% (pos 2 about 51%, pos 3 46%, pos 5 33%, pos 10 19%) | Ahrefs update, 2026-02 (Dec 2025 data) | Same method | Secondary coverage of figures |
| Average CTR change with AIO | Minus 15.5% overall; non-brand minus 20%; branded plus 18.7%; positions below 3 minus 27% | Amsive, 2025-04 | 700k keywords, 10 sites | Small site set |
| Organic CTR on AIO informational queries | 1.76% to 0.61% (minus 61%); paid minus 68% | Seer, 2025-11 (data to 2025-09) | 3,119 queries, 42 orgs | Baselines differ across Seer pages |
| Organic CTR on AIO SERPs, early 2026 | 1.3% (Dec 2025) to 2.4% (Feb 2026) | Seer v3, 2026-04 | 5.47M queries, 53 brands | Two months |
| Clicks per impression, AIO cited vs uncited | About 120% higher when cited; still about 38% below no-AIO SERPs | Seer v3, 2026-04 | Same | Correlation |
| News zero-click share | 69% (May 2025) vs 56% (May 2024) | Similarweb, 2025-07 | News searches | Modeled panel |
| Sites losing GSC impressions after num=100 | 87.7%; 77.6% lost unique queries | LOCOMOTIVE analysis via Search Engine Land, 2025-09 | 319 properties | Methodology not fully published |
| Core Web Vitals "good" thresholds | LCP 2.5 s, INP 200 ms, CLS 0.1 at p75 | web.dev, ongoing | n/a | Thresholds, not benchmarks |
| Spam update durations 2026 | 19.5 hours (March) to about 14 days (September) | Dashboard coverage | n/a | Varies |
| Core update durations 2025 to 2026 | About 12 to 18 days | Dashboard coverage | n/a | Varies |
| Google title rewrites | About 61% of titles changed | Zyppy, 2021 | About 81k titles | Old data |
| Migration temporary dip | Often 10% to 30% for 2 to 8 weeks | Practitioner consensus | n/a | Highly variable |

## 9. Tools, APIs and MCP servers
| Tool | Type | Use | Status |
|------|------|-----|--------|
| Search Console API (Search Analytics, URL Inspection, Sitemaps) | Official API | Performance data, index status (URL Inspection 2,000 per day per property) | Stable; hourly data added 2025 |
| Search Console bulk export to BigQuery | Official | Full daily rows | Stable |
| Search Console Generative AI report | Official UI | AI feature impressions | Beta 2026; no API or BigQuery export as of 2026-10 (UI and CSV) |
| Indexing API | Official | JobPosting and livestream only | Restricted |
| PageSpeed Insights API, CrUX API, CrUX History API, CrUX BigQuery | Official | CWV lab and field | Stable |
| Bing Webmaster Tools and API, AI Performance | Official | Bing data, URL submission, AI citations | AI report preview since 2026-02 |
| IndexNow | Open protocol | Push URL changes to Bing, Yandex, Seznam, Naver and others | Stable; Google not participating |
| Business Profile APIs | Official | Local metrics and management | Approval required |
| Google Trends API | Official | Trend data | Alpha (2025), limited |
| Google Analytics MCP | Official MCP | GA4 reporting | Released 2025; Google-maintained |
| Chrome DevTools MCP | Official MCP | Performance traces for LCP and INP, rendering | Preview from 2025-09 |
| Playwright MCP | Official MCP (Microsoft) | Rendered DOM checks | Stable |
| Search Console MCP | Community | Search Analytics and inspection via MCP | No official Google server as of 2026-10 (vendor and registry checks 2026-08 to 2026-10) |
| Ahrefs API and MCP | Vendor official | Keywords, links, competitors | Remote MCP at api.ahrefs.com/mcp/mcp (OAuth or MCP key) |
| Semrush API and MCP | Vendor official | Keywords, positions, audits | Remote MCP at mcp.semrush.com/v1/mcp (OAuth or API key; API units) |
| DataForSEO APIs and MCP | Vendor official (open source MCP) | SERP, keywords, backlinks, on-page | Stable; SERP depth pricing changed after num=100 [Unverified] |
| Screaming Frog SEO Spider (CLI), Log File Analyser | Desktop and CLI | Crawls, extraction, AI assisted per page analysis | Stable |
| Sitebulb, Lumar, Botify, Oncrawl, JetOctopus | Crawlers and platforms | Audits, monitoring, logs | Stable |

## 10. Official sources to monitor
| Source | URL | Cadence |
|--------|-----|---------|
| Search Status Dashboard | https://status.search.google.com/ | Weekly and on alerts |
| Google Search ranking updates | https://developers.google.com/search/updates/ranking | Monthly |
| Search Central blog | https://developers.google.com/search/blog | Weekly |
| Search documentation updates | https://developers.google.com/search/updates | Monthly |
| Spam policies | https://developers.google.com/search/docs/essentials/spam-policies | Quarterly |
| AI features and your website | https://developers.google.com/search/docs/appearance/ai-features | Monthly |
| Structured data search gallery | https://developers.google.com/search/docs/appearance/structured-data/search-gallery | Quarterly |
| Quality Rater Guidelines | https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf | On update |
| Search Console Help | https://support.google.com/webmasters | Monthly |
| Google Business Profile Help | https://support.google.com/business | Quarterly |
| Bing Webmaster blog | https://blogs.bing.com/webmaster | Monthly |
| IndexNow | https://www.indexnow.org/documentation | Quarterly |
| web.dev and CrUX release notes | https://web.dev/articles/vitals, https://developer.chrome.com/docs/crux/release-notes | Quarterly |
| Search Off the Record podcast and Search Central social accounts | Google | Monthly |
| Change detection (secondary) | Search Engine Roundtable, Search Engine Land, Search Engine Journal, PPC Land | Weekly; confirm with primary |

## 11. Open questions and watch list
1. Generative AI report: will clicks, CTR, queries, an AI Mode vs AI Overviews split or API access be added? (None as of 2026-10-08.)
2. AI features opt-out: available worldwide since 2026-08-31; page level controls due under the CMA requirement by about 2027-03; effects on Top Stories and Discover.
3. UK CMA conduct requirements: fair ranking compliance due about 2026-12, publisher controls fully by about 2027-03, choice screen decision by end of 2026; any EU or US equivalents; effect on AI Overviews attribution and controls.
4. Next core update timing (none confirmed since May 2026 as of 2026-10-08).
5. Discover core update expansion beyond US English and whether Discover gets recurring separate updates.
6. Further structured data deprecations (FAQ ended 2026-05; Practice problem 2026-01; watch Q&A, Math solver, Course list).
7. Googlebot 2 MB HTML fetch limit (documented 2026-02): watch for further changes; Google said the figure may change.
8. Bing AI Performance API and click data (promised for 2026, not shipped as of 2026-10).
9. Official MCP servers for Search Console and Bing Webmaster Tools (none as of 2026-10).
10. AI Mode becoming more prominent or default in some markets (I/O 2026 described AI Overviews and AI Mode as one integrated experience); measure your own AI Mode share.
11. Rank tracking economics after num=100: depth, pricing, data accuracy; parsers updated for google.com/goto links.
12. Preferred sources and Discover follow features expansion and measurable impact.
13. Cloudflare 2026-09-15 AI crawler defaults: confirm whether ad-page Training blocks catch Googlebot and Bingbot on default zones (reports conflict).

## 12. Sources
1. Search Status Dashboard: Ranking history. Google. https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history. Ongoing.
2. Google Search ranking updates. Google Search Central. https://developers.google.com/search/updates/ranking. Ongoing.
3. Latest Google Search documentation updates. Google. https://developers.google.com/search/updates. Ongoing.
4. Spam policies for Google web search. Google. https://developers.google.com/search/docs/essentials/spam-policies. Updated 2024-03 and 2024-11.
5. Creating helpful, reliable, people-first content. Google. https://developers.google.com/search/docs/fundamentals/creating-helpful-content. Ongoing.
6. A guide to Google Search ranking systems. Google. https://developers.google.com/search/docs/appearance/ranking-systems-guide. Ongoing.
7. Search Quality Rater Guidelines. Google. https://guidelines.raterhub.com/searchqualityevaluatorguidelines.pdf. 2025-01 and 2025-09 versions.
8. AI features and your website. Google. https://developers.google.com/search/docs/appearance/ai-features. 2025.
9. Introducing Search Generative AI performance reports in Search Console. Google Search Central blog. https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports. 2026-06-03.
10. Streamline your Search Console analysis with the new AI-powered configuration. Google Search Central blog. https://developers.google.com/search/blog/2025/12/ai-powered-configuration. 2025-12.
11. Introducing social channels in Search Console. Google Search Central blog. https://developers.google.com/search/blog/2025/12/social-channels-search-console. 2025-12.
12. Introducing weekly and monthly views in Search Console. Google Search Central blog. https://developers.google.com/search/blog/2025/12/weekly-monthly-views-search-console. 2025-12.
13. Google's February 2026 Discover core update. Google Search Central blog. https://developers.google.com/search/blog/2026/02/discover-core-update. 2026-02.
14. Understand JavaScript SEO basics. Google. https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics. Ongoing.
15. Managing crawling of faceted navigation URLs. Google. https://developers.google.com/search/docs/crawling-indexing/crawling-managing-faceted-navigation. 2024-12.
16. Large site owner's guide to managing crawl budget. Google. https://developers.google.com/search/docs/crawling-indexing/large-site-managing-crawl-budget. Ongoing.
17. Site moves with URL changes. Google. https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes. Ongoing.
18. Tell Google about localized versions of your page. Google. https://developers.google.com/search/docs/specialty/international/localized-versions. Ongoing.
19. Structured data search gallery. Google. https://developers.google.com/search/docs/appearance/structured-data/search-gallery. Ongoing.
20. Understanding Core Web Vitals and Google search results. Google. https://developers.google.com/search/docs/appearance/core-web-vitals. Ongoing.
21. Web Vitals. web.dev. https://web.dev/articles/vitals. Ongoing.
22. Interaction to Next Paint. web.dev. https://web.dev/articles/inp. 2024.
23. Search Console API searchanalytics.query. Google. https://developers.google.com/webmaster-tools/v1/searchanalytics/query. Ongoing.
24. URL Inspection API. Google. https://developers.google.com/webmaster-tools/v1/urlInspection.index/inspect. Ongoing.
25. CrUX API. Chrome for Developers. https://developer.chrome.com/docs/crux/api. Ongoing.
26. Tips to improve your local ranking on Google. Google Business Profile Help. https://support.google.com/business/answer/7091. Ongoing.
27. Introducing AI Performance in Bing Webmaster Tools (Public Preview). Bing Webmaster blog. https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview. 2026-02-10.
28. Bing Webmaster Tools adds AI citation performance data. Search Engine Journal. https://www.searchenginejournal.com/bing-webmaster-tools-adds-ai-citation-performance-data/566874/. 2026-02.
29. Bing AI Performance report. Semrush blog. https://www.semrush.com/blog/bing-ai-performance-report/. 2026.
30. IndexNow documentation. IndexNow.org. https://www.indexnow.org/documentation. Ongoing.
31. Google users are less likely to click on links when an AI summary appears in the results. Pew Research Center. https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/. 2025-07-22.
32. Google AI Overview study: SEO and PPC CTR impact. Seer Interactive. https://www.seerinteractive.com/insights/ctr-aio. 2025 to 2026.
33. Google AI Overviews drive 61% drop in organic CTR, 68% in paid. Search Engine Land. https://searchengineland.com/google-ai-overviews-drive-drop-organic-paid-ctr-464212. 2025-11.
34. AI Overview CTR fell 61%, but clicks didn't collapse. Search Engine Journal. https://www.searchenginejournal.com/ai-overview-ctr-fell-61-but-clicks-didnt-collapse/572993/. 2026-04.
35. AI Overviews reduce clicks by 34.5%. Ahrefs. https://ahrefs.com/blog/ai-overviews-reduce-clicks/. 2025-04 (updated 2026-02).
36. Ahrefs study: Google AI Overviews cut clicks by 58%. MediaNama. https://www.medianama.com/2026/02/223-google-ai-overviews-click-through-rates-58-study/. 2026-02.
37. Google AI Overviews study. Amsive. https://www.amsive.com/insights/research/google-ai-overviews-study/. 2025-04-16.
38. Similarweb: no clicks from Google grew from 56% to 69% since AI Overviews. Search Engine Roundtable. https://www.seroundtable.com/similarweb-google-zero-click-search-growth-39706.html. 2025-07.
39. 77% of sites lost keyword visibility after Google removed num=100: data. Search Engine Land. https://searchengineland.com/google-num100-impact-data-462231. 2025-09.
40. Were we wrong about the Great Decoupling after all? Analyzing the impact of num=100. Brodie Clark Consulting. https://brodieclark.com/the-great-decoupling-num100/. 2025-09.
41. Why Google Search Console impressions fell (and why that's good). Search Engine Land. https://searchengineland.com/why-google-search-console-impressions-dropped-interpret-data-463677. 2025.
42. Google organic CTR by position study. Advanced Web Ranking. https://www.advancedwebranking.com/seo/organic-ctr. Ongoing.
43. Google releases December 2025 core update. Search Engine Journal. https://www.searchenginejournal.com/google-releases-december-2025-core-update/563134/. 2025-12.
44. Google December 2025 core update rollout is now complete. Search Engine Land. https://searchengineland.com/google-december-2025-core-update-rollout-is-now-complete-466362. 2025-12.
45. Google February 2026 Discover core update is now complete. Search Engine Land. https://searchengineland.com/google-february-2026-discover-core-update-is-now-complete-469450. 2026-02.
46. Google March 2026 spam update rolls out. Search Engine Roundtable. https://www.seroundtable.com/google-march-2026-spam-update-41109.html. 2026-03.
47. Google confirms March 2026 core update is complete. Search Engine Journal. https://www.searchenginejournal.com/google-confirms-march-2026-core-update-is-complete/571459/. 2026-04.
48. Google May 2026 broad core update is done rolling out. Search Engine Roundtable. https://www.seroundtable.com/google-may-2026-core-update-done-41435.html. 2026-06.
49. Google June 2026 spam update is done rolling out. Search Engine Roundtable. https://www.seroundtable.com/google-june-2026-spam-update-done-41580.html. 2026-06.
50. Google August 2026 spam update is done rolling out. Search Engine Roundtable. https://www.seroundtable.com/google-august-2026-spam-update-done-41906.html. 2026-08.
51. Google September 2026 spam update has finished rolling out. Search Engine Roundtable. https://www.seroundtable.com/google-september-2026-spam-update-done-42235.html. 2026-10-08.
52. Google September 2026 spam update phase three hit October 4 to 6. Search Engine Roundtable. https://www.seroundtable.com/google-september-2026-spam-update-phase-3-42239.html. 2026-10.
53. Google search algorithm updates tracker. Rank Math. https://rankmath.com/google-updates/. Ongoing.
54. Could Google's next core update arrive in September 2026? Search Engine Watch. https://searchenginewatch.com/could-googles-next-core-update-arrive-in-september-2026/. 2026-09.
55. Google Search Console adds branded queries filter. Search Engine Land. https://searchengineland.com/google-search-console-adds-branded-queries-filter-464928. 2025-11.
56. Google Search Console adds Query groups. Search Engine Land. https://searchengineland.com/google-search-console-adds-query-groups-463820. 2025-10.
57. Google Search Console adds weekly and monthly aggregation views. PPC Land. https://ppc.land/google-search-console-adds-weekly-and-monthly-aggregation-views/. 2025-12.
58. Google Search Console AI reports rolled out worldwide. Search Engine Journal. https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/. 2026.
59. How to track Google AI Mode traffic in Search Console. Search Engine Journal. https://www.searchenginejournal.com/how-to-track-google-ai-mode-traffic-in-search-console/586194/. 2026.
60. Google will let websites opt out of AI Mode and Overviews in Search. 9to5Google. https://9to5google.com/2026/06/02/google-ai-mode-overviews-opt-out/. 2026-06-02.
61. What opting out of Google's AI search features means now. Search Engine Journal. https://www.searchenginejournal.com/what-opting-out-of-googles-ai-search-features-means-now/584321/. 2026-06.
62. Google gives site owners a toggle to exit AI Overviews and AI Mode. PPC Land. https://ppc.land/google-gives-site-owners-a-toggle-to-exit-ai-overviews-and-ai-mode/. 2026-06.
63. Google expands AI Mode to over 40 countries and territories. PPC Land. https://ppc.land/google-expands-ai-mode-to-over-40-countries-and-territories/. 2025-10-07.
64. Google AI Mode tracker 2026. Keywords Everywhere. https://keywordseverywhere.com/news/google-ai-mode/. 2026-09.
65. December 2025 SEO news. Lumar. https://www.lumar.io/blog/industry-news/december-2025-seo-news-google-core-update-ai-mode-discover-chatgpt-shopping-more/. 2025-12.
66. Google Analytics MCP server. Google. https://github.com/googleanalytics/google-analytics-mcp. 2025.
67. Chrome DevTools MCP. Chrome DevTools team. https://github.com/ChromeDevTools/chrome-devtools-mcp. 2025.
68. DataForSEO MCP server. DataForSEO. https://github.com/dataforseo/mcp-server-typescript. 2025.
69. Screaming Frog SEO Spider. Screaming Frog. https://www.screamingfrog.co.uk/seo-spider/. Ongoing.
70. Local Search Ranking Factors. Whitespark. https://whitespark.ca/local-search-ranking-factors/. Latest edition.
71. Generative AI performance report (Search). Search Console Help. https://support.google.com/webmasters/answer/16984139. 2026-06, updated 2026-08-31.
72. Google Search Console AI Reports Rolled Out Worldwide. Search Engine Journal. https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/. 2026-09.
73. Google Search Console AI performance reports and Search generative AI control rolling out globally. Search Engine Land. https://searchengineland.com/google-search-console-ai-performance-reports-and-search-generative-ai-control-rolling-out-globally-486269. 2026-08.
74. CMA secures fairer deal for publishers and improves Google search services in UK. GOV.UK (CMA). https://www.gov.uk/government/news/cma-secures-fairer-deal-for-publishers-and-improves-google-search-services-in-uk. 2026-06-03.
75. Google search fair ranking conduct requirement. GOV.UK (CMA). https://www.gov.uk/find-digital-markets-measures/google-search-fair-ranking-conduct-requirement. 2026-06-17.
76. CMA strengthens proposals allowing people choice over their search service. GOV.UK (CMA). https://www.gov.uk/government/news/cma-strengthens-proposals-allowing-people-choice-over-their-search-service. 2026-09-23.
77. Google's general search and search advertising services (case page). GOV.UK (CMA). https://www.gov.uk/cma-cases/googles-general-search-and-search-advertising-services. Ongoing.
78. Google rewrites Googlebot's rulebook: 2MB limits, IP moves, and what crawlers really are. PPC Land. https://ppc.land/google-rewrites-googlebots-rulebook-2mb-limits-ip-moves-and-what-crawlers-really-are/. 2026-02.
79. What Googlebot's 2MB Crawl Size Limit Means For SEO. DebugBear. https://www.debugbear.com/blog/googlebot-crawler-file-size-limit. 2026-02.
80. Google Updates Googlebot File Size Limit Docs. Search Engine Journal. https://www.searchenginejournal.com/google-updates-googlebot-file-size-limit-docs/566485/. 2026-02.
81. Google phases out practice problem and dataset structured data. PPC Land. https://ppc.land/google-phases-out-practice-problem-and-dataset-structured-data/. 2026-01.
82. FAQ rich results deprecated May 2026. Claudio Novaglio. https://www.claudio-novaglio.com/en/blog/seo-ranking/faq-rich-results-deprecated-2026. 2026-05.
83. Google Completes September 2026 Spam Update After Nearly 14 Days. Search Engine Journal. https://www.searchenginejournal.com/google-september-2026-spam-update-complete/592283/. 2026-10-08.
84. Google September 2026 spam update done rolling out. Search Engine Land. https://searchengineland.com/google-september-2026-spam-update-done-rolling-out-493550. 2026-10-08.
85. Bing AI dashboard maps grounding queries to cited pages. Search Engine Journal. https://searchenginejournal.com/bing-ai-dashboard-maps-grounding-queries-to-cited-pages/570323/. 2026-03.
86. AI Performance (help). Bing Webmaster Tools. https://www.bing.com/webmasters/help/ai-performance-9f8e7d6c. Living document.
87. Google Search's I/O 2026 updates. Google. https://blog.google/products-and-platforms/products/search/search-io-2026/. 2026-05-19.
88. Google makes Gemini 3 the default model for AI Overviews globally. Dataconomy. https://dataconomy.com/2026/01/28/google-makes-gemini-3-the-default-model-for-ai-overviews-globally/. 2026-01-28.
89. Google preferred sources global language expansion. 9to5Google. https://9to5google.com/2026/04/30/google-preferred-sources-global-language-expansion/. 2026-04-30.
90. Google confirms google.com/goto search links. Relevant Audience. https://www.relevantaudience.com/seo/google-search-goto-passthrough-urls-confirmed/. 2026-09.
91. Google tests paying publishers for using its content in AI Mode, AI Overviews and Gemini. Search Engine Land. https://searchengineland.com/google-tests-paying-publishers-for-using-its-content-in-ai-mode-ai-overviews-and-gemini-488382. 2026-09.
92. In 2026, less than one third of Google searches still send a click. SparkToro. https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/. 2026.
93. Semrush MCP. Semrush Developer. https://developer.semrush.com/api/basics/semrush-mcp/. 2026.
94. Ahrefs remote MCP server listing. mcpservers.org. https://mcpservers.org/remote-mcp-servers/ahrefs. 2026.
95. Google Search Console MCP: no official server exists. Carly. https://www.usecarly.com/blog/google-search-console-mcp/. 2026.
96. Cloudflare's AI Crawler Rules Can Block Googlebot. Search Engine Journal. https://www.searchenginejournal.com/cloudflares-ai-crawler-rules-can-block-googlebot/581385/. 2026.
97. Your site, your rules: new AI traffic options for all customers. Cloudflare. https://blog.cloudflare.com/content-independence-day-ai-options/. 2026-07-01.
