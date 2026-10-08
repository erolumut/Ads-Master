# TikTok Ads: Market Research Dossier

> Compiled 2026-10-08 for the Ads Master `tiktok-ads` package. Covers January 2025 to October 2026. Evidence labels follow `docs/AUTHORING_SPEC.md`. Source numbers in brackets refer to the numbered list at the end (same numbering as `skills/tiktok-ads/references/sources.md`).

## Method and limits

- 21 web searches (extended mode for 2025 and 2026 items) were run before the shared search budget for this build was exhausted. Direct page fetching (WebFetch, curl) was blocked by network egress policy, so primary pages were read through search-indexed content rather than opened in full.
- Consequences: official Help Center facts below are taken from indexed page text with their "last updated" dates where visible. Items without a second confirming source or an official page are labeled [Unverified]. Vertical CPM, CPC and CVR benchmarks could not be verified and are deliberately not quoted.
- Priority for re-verification is listed in "Open questions and watch list".

## 1. Executive summary

1. Automation is the default buying model. Smart+ was rebuilt in October 2025 into one flow where each module (targeting, budget, placement, creative, catalog) can be fully automated, partially automated or manual [1, 4, 65]. Further layers followed through 2026: Auto-select creative (Smart+ App first, then Lead Gen), Asset Manager, AI campaign summaries, Music Autofix, Creative Upgrades and catalog auto-crawl [2, 3, 6, 64].
2. TikTok Shop advertising is GMV Max only. Since July 2025, GMV Max is the default and only supported campaign type for TikTok Shop ads with a Sales objective; legacy Video, LIVE and Product Shopping Ads can no longer be created or edited [26, 71, 72].
3. GMV Max moved toward profit, not just GMV. In 2026 TikTok added seller costs (affiliate commissions, coupons, platform fees) into GMV Max reporting and, via GMV Max Pro and the October 2026 update, into optimization [3, 54, 62, 69]. ROI protection credits expanded to all creation surfaces on 2026-02-25 [27].
4. The US ownership question is settled. The TikTok USDS Joint Venture closed on 2026-01-22 (Oracle, Silver Lake, MGX 15% each; ByteDance 19.9%) [44, 45]. Day-to-day ad buying did not change; algorithm control and retraining on US data moved to the JV; whether commercial operations sit with ByteDance entities is [Contested] [45, 46, 50].
5. Off-platform reach arrived in the US. On 2026-10-05 the TikTok Ad Network (formerly Pangle, nearly 400,000 apps) opened to US advertisers inside Ads Manager [49, 50, 51, 52]. One analyst warns Smart+ can pull it in automatically [53].
6. Agents are now first-class buyers. TikTok launched an official TikTok for Business MCP Server and Agentic Hub at TikTok World (May 2026), exposing about 400 API endpoints as MCP tools, available through partners including Claude [34, 35, 36, 37]. TikTok reports MCP use up more than 200% from July to September 2026 [49].
7. Search is a real layer. The Search Ads Toggle became Automatic Search Placement (no keyword control); the dedicated Search Ads Campaign has keywords, negatives, Smart+ expansion and a 20x-bid budget guideline [22, 23]. Search Hubs, Branded Buzz and Keyword Amplifier launched in May 2026 [3, 67].
8. Creative AI went agentic. Symphony Creative Studio was rebuilt on Dreamina Seedance 2.0 (May 2026); Symphony Agent launched at Cannes (June 2026) with AI labels and invisible watermarks on output [39, 57, 58, 59].
9. Creators consolidated into TikTok One. Creator Marketplace shut down on 2025-04-01; TikTok One is the creator and Spark Ads hub, with Custom Creator Networks piloted from June 2026 [40, 58, 60].
10. Measurement fundamentals did not change: default 7-day click and 1-day view, ad group level CTA, EVTA (6-second engaged view) and VTA settings, event_id deduplication within 48 hours [17, 19, 21, 68]. The operator edge is calibration: TikTok over-credits in platform and is under-credited by last click.

## 2. State of the channel in 2026 (with numbers)

| Fact | Number | Source | Label |
|------|--------|--------|-------|
| US users and businesses (TikTok claim at 2026 NewFronts) | Over 200 million US users, 7.5 million businesses; an earlier memo cited 170 million Americans | [46, 47] | [Official, 2026-03], self-reported |
| US ownership | JV closed 2026-01-22: Oracle 15%, Silver Lake 15%, MGX 15%, ByteDance 19.9%; CEO Adam Presser | [44, 45] | News, consistent |
| TikTok Ad Network | Nearly 400,000 apps, 48 markets (US is the 48th), 40+ app genres, 300 sub-categories; DoubleVerify and IAS controls | [49, 50, 52, 56] | [Official, 2026-10] |
| MCP adoption | +200% advertiser usage, July to September 2026, no base | [49] | [Official, 2026-10] |
| MCP scope | About 400 TikTok API for Business endpoints as MCP tools | [35] | [Official, 2026] |
| TopReach | 59% incremental reach at 3x lower cost per reach vs TopView alone | [3, 48] | [Official, 2026-03], platform-reported |
| GMV Max | About 20% GMV uplift in initial tests | [33, 79] | Platform-reported |
| ROI protection | Credits if daily ROI below 90% of target; generally 20+ daily orders | [27] | [Official, 2026-02] |
| Ad revenue projection 2026 | About $38 billion global, 38% US (WARC via aggregator) | Aggregator cited in search results | [Unverified] |
| Minimum daily budgets | Campaign above $50, ad group above $20 | [11] | [Official] |

### Product surface map (October 2026)

| Surface | Status 2026-10 | Who it is for | Source |
|---------|---------------|---------------|--------|
| Smart+ (upgraded, modular) | Live for eligible advertisers; Sales, Lead Generation, App Promotion; separate Smart+ Traffic flow | All performance advertisers with signal | [1, 4, 83] |
| Manual auction campaigns | Live | Testing lanes, regulated categories, low-signal accounts | [13] |
| GMV Max (Product, LIVE) | Only Sales option for TikTok Shop destination | Shop sellers | [26, 29] |
| GMV Max Pro / cost-aware optimization | Limited rollout | Larger Shop sellers | [62, 69] |
| Seller Scale Up | Reported lighter GMV option for small merchants | Small Shop sellers | [79] [Unverified] |
| Creative Boost (LIVE GMV Max) | Allowlist | LIVE sellers | [30] |
| Search Ads Campaign | Live, powered by Smart+, multi ad group workflow | Brands with search demand | [22, 24] |
| Automatic Search Placement | Live (formerly Search Ads Toggle) | Most conversion campaigns | [23] |
| Search Hubs, Branded Buzz, Keyword Amplifier | Announced 2026-05 | Brands | [3, 67] |
| TopView, TopFeed, TopReach (+Creative Sequencing, Max Reach) | Live; TopView bookable in Ads Manager per Q3 preview | Brand | [2, 3] |
| Logo Takeover, Prime Time, Pulse | Rep-led | Brand, tentpoles | [48] |
| Streaming Ads | Q3 2026 preview | Streaming services | [2] |
| Spark Ads | Live | Everyone | [10] |
| TikTok One (creators) | Live; replaced Creator Marketplace 2025-04-01 | Creator programs | [40, 60] |
| Custom Creator Networks | Pilot from 2026-06 | Large brands | [58] |
| Symphony Creative Studio, Symphony Agent | Live; Seedance 2.0 based; Agent from 2026-06 | Creative production | [39, 57, 58] |
| Lead Generation (Instant Form, website, DM) and Smart+ Lead Gen | Live | Lead gen | [8] |
| Agentic Leads | Announced 2026-10-05; rollout [Contested] | Lead gen | [49, 54] |
| Buy Direct, Shopping Assistant | Announced 2026-10-05; early access [Contested] | Ecommerce brands on Shopify, Salesforce, Shoplazza, Stripe | [54, 80] |
| TikTok Ad Network (formerly Pangle) | US opened 2026-10-05; 48 markets | Apps, reach, tested web cells | [49, 50] |
| Official MCP Server and Agentic Hub | Live since 2026-05 | Agent-driven operations | [34, 35, 36] |

### Ownership and regulatory state
- US: JV closed 2026-01-22; algorithm control and US data moved to the JV with Oracle as security partner; commercial control of ads and commerce [Contested] [44, 45, 46].
- US off-platform inventory: reports say the Pangle network sits outside the JV; confirm contracting entity before buying TikTok Ad Network in the US [50] [Unverified].
- EU: Digital Services Act duties (ad repository, minors, special category data) shape targeting and transparency; details of 2025 enforcement actions were not re-verified this cycle [Unverified].
- Canada: status of the 2024 wind-down order not re-verified [Unverified].

Interpretation: TikTok in 2026 is a mature, automation-first ad platform with a commerce stack (Shop, GMV Max, Buy Direct), a search layer, off-platform inventory and agent access. The advertiser's competitive edge has moved from campaign settings to creative throughput, creator supply, measurement quality and margin-aware targets.

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Impact for advertisers | Source | Label |
|------|--------|------------------------|--------|-------|
| 2025-01-17 to 2025-01-20 | US Supreme Court upheld the divest-or-ban law; TikTok briefly went dark in the US; enforcement delayed by executive order (extended through 2025) | One lost delivery day, hedged US budgets for 2025 | [45] | [Unverified exact sequence], widely reported |
| 2025-02 | Attribution help article updated: CTA, EVTA and VTA windows set at ad group level after SAN transition | Window settings per ad group | [17] | [Official, 2025-02] |
| 2025-02 | VBO for web tips updated: Min ROAS from 7-day actual, Highest Value if unsure, 10x CPA budget | Value bidding guidance | [15] | [Official, 2025-02] |
| 2025-02-27 | TikTok announced Creator Marketplace sunset in favor of TikTok One | Creator workflows move | [60] | News |
| 2025-03 | No new campaigns on legacy Creator Marketplace (early March cutoffs) | Migrate creator campaigns | [41, 60] | [Official, 2025-03] |
| 2025-04-01 | Creator Marketplace shut down; redirects to TikTok One | TikTok One is the only native creator hub | [60] | [Official, 2025-04] |
| 2025-05 | Event deduplication article updated (event_id, _ttp fallback, 48-hour window) | Dedup rules | [21] | [Official, 2025-05] |
| 2025-06 to 2025-07 | Phased move of TikTok Shop ads to GMV Max (reported 2025-06-01 new sellers, 2025-06-25 legacy removal, 2025-07-15 all sellers; one source cites 2025-08-05 global lock-in) | Shop ads lose manual targeting and formats | [71, 72, 73] | [Official, 2025-07]; dates [Contested] |
| 2025-09-17 | Community AdsMCP TikTok server listed | Early agent access (unofficial) | [78] | Community |
| 2025-10-07 | Smart+ upgraded flow: full, partial or manual per module; Symphony inside Smart+; GMV Max updates | Automation with controls | [1, 65] | [Official, 2025-10] |
| 2026-01-21 | Auto-select creative (Smart+ App first) and ad previews | AI creative selection | [64, 66] | Trade press reporting official rollout |
| 2026-01-22 | US JV closed | Ban risk removed | [44] | News |
| 2026-02-25 | ROI protection extended to GMV Max campaigns created in Seller Center (PC, mobile) and Ads Manager | Protection on all surfaces | [27] | [Official, 2026-02] |
| 2026-03-24 | TopReach (TopView + TopFeed) announced | Brand reach efficiency | [3, 48] | [Official, 2026-03] |
| 2026-03-26 to 2026-03-30 | NewFronts: Logo Takeover, Prime Time, TopReach, Pulse enhancements; JV pitch | Premium formats | [46, 47, 48] | [Official, 2026-03] |
| 2026-04-15 | Symphony integrates ByteDance next-generation video model | AI video for ads | [57] | Trade press |
| 2026-05-13 | TikTok World: TopReach Creative Sequencing; Search Hubs + Branded Buzz (Brand Discovery Bundle) + Keyword Amplifier; Smart+ more manual controls, Music Autofix, Auto Selection, Asset Manager, AI summaries; GMV Max Pro; Symphony Creative Studio on Seedance 2.0; official MCP server and Agentic Hub | Broadest product wave of the period | [3, 34, 37, 61, 62] | [Official, 2026-05] |
| 2026-05 | GMV Max metric includes affiliate commissions, coupons and platform fees | Profit-aware reporting | [69] | Trade press reporting official update |
| 2026-06 | Automatic Search Placement help updated (formerly Search Ads Toggle) | Search placement semantics | [23] | [Official, 2026-06] |
| 2026-06-22 | Cannes: Symphony Agent, Custom Creator Networks (Starbucks pilot), Dentsu integration | Agentic creative and creator matching | [58] | Trade press reporting official launch |
| 2026-07 | Q3 Product Preview: TopReach Max Reach, TopView bookable in Ads Manager, Smart+ Catalog Creative Upgrades, Auto-selection for Lead Gen, Streaming Ads | Self-serve premium and Smart+ expansion | [2] | [Official, 2026-07] |
| 2026-08 | Search Ads Campaign help updated: multiple ad groups per campaign, 20x-bid budget guideline | Search scaling | [22] | [Official, 2026-08] |
| 2026-08 | Seedance 2.5 in Symphony; Mini Dramas format (July) | AI video and serialized content | SocialBee via search | [Unverified] |
| 2026-09 | Broader upgraded Smart+ rollout claimed (2026-09-07 and 2026-09-30 in different blogs) | Rollout timing unclear | [81] | [Contested] |
| 2026-10-05 | Advertising Week: Buy Direct (in-feed checkout with Shopify, Salesforce, Shoplazza, Stripe), Shopping Assistant, Agentic Leads, TikTok Ad Network to US, GMV Max cost-aware optimization, MCP growth | Commerce and agentic expansion; off-platform US reach | [49, 50, 54, 55] | [Official, 2026-10]; rollout dates [Contested] |

## 4. Best practice consensus

| Area | Consensus | Label |
|------|-----------|-------|
| Creative | TikTok-first, 9:16, sound on, person in frame early, hook in the first 3 seconds, creator-led | [Practitioner consensus], TikTok creative guidance |
| Creative volume | Accounts are creative-constrained; refresh faster than on Meta; separate testing lane | [Practitioner consensus] |
| Structure | Fewer ad groups with more signal; Smart+ for scaling once signal exists; manual for tests and controls | [Official, 2025-10] guidance plus consensus |
| Budgets | At least 10x CPA per ad group; Smart+ Web 30x ideal | [Official] [7, 15] |
| Learning | About 50 conversions in 7 days; avoid edits in the first 7 days | [Practitioner consensus], [Official] for no-edit guidance [7] |
| Bidding | Maximum Delivery to start; Cost Cap or Min ROAS from trailing actuals | [Official] [13, 15] |
| Targeting | Broad or automatic with legal guardrails | [Practitioner consensus] |
| Measurement | Pixel plus Events API with event_id dedup; hashed identifiers; triangulate | [Official] [21], consensus |
| Shop | GMV Max with Target ROI; Max Delivery for 3 to 5 days on new products; large creative supply (50 to 70 videos in queue for LIVE) | [Official] [28, 31] |
| Lead gen | Qualifying questions, CRM feedback, judge on qualified pipeline | [Practitioner consensus] |
| Search | Dedicated Search Ads Campaign for brand and product terms; Automatic Search Placement for the rest | [Official] [22, 23] |

## 5. Contested topics (both sides)

| Topic | Side A | Side B | Ads Master stance |
|-------|--------|--------|-------------------|
| Smart+ vs manual | TikTok: automation finds more conversions; recommends split tests to prove lift [7] | Operators: Smart+ concentrates spend on early winners, hides placement leakage and limits learning about audiences | Smart+ for scaling once signal exists; manual testing lane; split test before migrating most spend |
| GMV Max incrementality | TikTok: about 20% GMV uplift in tests; Spillover reporting shows halo [33, 79] | Sellers: GMV Max claims organic and affiliate sales it did not cause; ROI protection is conditional [70] | Track total Shop GMV; run planned holdouts; treat GMV Max ROI as an upper bound |
| ROI protection | Advertiser protection against shortfalls [27] | Platform control: requires 20+ orders and edit discipline, disadvantages small sellers [70] | Use it, but never plan profitability on credits |
| View-through and EVTA | Captures real effect of watched-not-clicked ads [19] | Inflates ROAS, especially 7-day view [Practitioner] | Optimize on 7-day click + 1-day view or EVTA; never set targets from 7-day view |
| TikTok Ad Network | Incremental reach off TikTok, brand safety controls [49] | Off-platform impressions may not perform like TikTok; footprint is not incrementality [53] | Explicit test cell; off by default for web sales and lead gen |
| Learning threshold | About 50 conversions in 7 days [84] | 25 conversions or 7 days, whichever first [85] | Plan for 50; treat 25 as a minimum |
| Attribution options | Help article lists CTA 1/7, EVTA 1/7, VTA off/1 [17] | Guides list 14 and 28-day click and 7-day view options [68] | Check the live UI per account |
| JV commercial control | Operational control moved to a US-majority entity [45] | Commercial operations (ads, e-commerce) remain with ByteDance entities [46] | Watch contracting entity and data terms; no change to buying for now |
| AI avatars and generated ads | Faster, cheaper production; 50% to 70% time savings claimed [Unverified] | Stock avatars are non-exclusive and can erode trust; risk of deception | AI for variations and localization; humans for core concepts; always label |
| Buy Direct rollout | Beginning to roll out to US users and brands | No launch date announced; early access only [54, 80] | Test when offered; do not plan around it |

## 6. What top operators do differently

1. Run a creative supply chain, not a campaign: weekly concept quotas by tier, creator rosters, a creative register that joins concept, hook and creator to results.
2. Use Spark Ads from creators and organic winners as the default ad unit, and answer comments with video replies that become new ads.
3. Keep two lanes: Smart+ (or GMV Max) for scaling, a manual testing lane for clean creative reads.
4. Size budgets to the learning math before launch and consolidate ruthlessly.
5. Calibrate: hold a range from last click to platform, use post-purchase surveys and lift tests, and set in-platform targets from the calibrated number.
6. Compute Shop breakeven ROI with every cost (referral fee, affiliate commission, coupons, shipping, returns) and edit GMV Max in one daily window.
7. Isolate search intent with a Search Ads Campaign for brand and product terms; use Creative Center Keyword Insights for both keywords and hooks.
8. Treat off-platform inventory and new formats as experiments with stop rules.
9. Own the assets: Business Center, pixel, catalog, identities, creator contracts with AI rights.
10. Automate reading, not writing: MCP or API for daily reads and alerts, human approval for every write.

## 7. Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|-----------|
| Purchase optimization on budgets far below 10x CPA | Permanent learning, volatile CPA | Shallower event or consolidation |
| Duplicate events without shared event_id | Doubled ROAS, overspend | Dedup check before scaling |
| Caps from 7-day view numbers | Non-delivery or overspend | Click-based calibration |
| Off-platform placements left on for lead gen | Junk leads | Placement exclusions, CRM read |
| Sharp GMV Max ROI target hikes and pauses | Stalled delivery, lost ROI protection | One edit window, gradual changes |
| Ignoring affiliate and coupon costs | Shop losses hidden by ROI | Breakeven ROI formula |
| Spark codes expiring mid-flight | Losing top ads | Expiry register and reminders |
| Repurposed horizontal or polished ads | High CPM, low hook rate | TikTok-first briefs |
| Daily edits | Learning resets | Change batching |
| Unlicensed music, unsupported claims | Rejections, account risk | Pre-flight QA |
| New accounts to dodge a suspension | Ban spreads to new assets | Fix and appeal |
| Reporting CPL instead of CPQL | Wasted lead budgets | CRM join |

## 8. Benchmarks (source, date, caveat)

| Benchmark | Value | Source | Date | Caveat |
|-----------|-------|--------|------|--------|
| TopReach incremental reach | +59% at 3x lower cost per reach vs TopView alone | [3, 48] | 2026-03 | Platform-reported |
| GMV Max uplift | About 20% GMV in initial tests | [33, 79] | 2024 to 2025 | Platform-reported; incrementality not independently verified |
| MCP usage growth | +200% | [49] | 2026-07 to 2026-09 | No base number |
| Smart+ Web budget | 30x CPA ideal, 10x minimum | [7] | About 2025 | Guidance, not a performance benchmark |
| VBO budget | 10x target CPA | [15] | 2025-02 | Guidance |
| Search Ads budget | 20x bid | [22] | 2026-08 | Guidance |
| LIVE GMV Max creative supply | 50 to 70 videos in queue | [31] | Accessed 2026-10 | Guidance |
| Learning exit | About 50 conversions in 7 days | [84] | 2026 | Practitioner consensus; 25 cited by [85] |
| EMQ | Above 7 strong, below 5 weak | [75] | 2025 to 2026 | Third-party; [74] warns against chasing 10 |
| Vertical CPM, CPC, CTR, CVR | Not quoted | n/a | n/a | No source with a published method was verified this cycle; pull from Creative Center and rep data at task time |

## 9. Tools, APIs and MCP servers

| Tool | Type | Capabilities | Source |
|------|------|-------------|--------|
| TikTok for Business MCP Server | Official MCP | About 400 endpoints: campaign management, reporting, audiences, creative operations; partners include Claude, Perplexity, Manus, Replit, Snowflake, IAB Tech Lab Agent Registry | [34, 35, 36, 37] |
| TikTok for Business Agentic Hub | Official marketplace | AI Skills and agent tools discovery | [36, 37] |
| TikTok API for Business v1.3 | Official API | Management, reporting (sync and async), audiences, Events API, GMV Max, Smart+ | [34] |
| Events API | Official server events | event/track with hashed identifiers, event_id dedup | [21] |
| ysntony/tiktok-ads-mcp | Community MCP | 6 read-only tools | [77] |
| AdsMCP TikTok Ads server | Community MCP | Management, analytics, creative, audiences, reports | [78] |
| Creative Center | Official research | Top Ads, Keyword Insights, Trend Discovery, CML, Symphony Assistant | [38, 39] |
| Symphony Creative Studio and Symphony Agent | Official AI creative | Generation, avatars, dubbing, agentic workflows | [39, 57, 58, 59] |
| TikTok One | Official creator hub | Creator search, campaigns, Spark authorization | [40, 41] |
| Data connectors (Supermetrics, Funnel, Windsor.ai, Fivetran, Airbyte) | Third-party | Reporting pipelines | Vendor docs (not captured this cycle) |

## 10. Official sources to monitor

| Source | URL | Cadence |
|--------|-----|---------|
| TikTok Business Help Center | https://ads.tiktok.com/help | Monthly; check "last updated" on core articles |
| TikTok for Business blog | https://ads.tiktok.com/business/en/blog | Monthly; quarterly Product Preview |
| TikTok Newsroom | https://newsroom.tiktok.com | Event weeks: NewFronts (March), TikTok World (May), Cannes (June), Q3 preview (July), Advertising Week (October) |
| TikTok API for Business docs | https://business-api.tiktok.com/portal/docs | Monthly; version and changelog |
| MCP server docs | https://business-api.tiktok.com/portal/docs/tiktok-ads-mcp-server/v1.3 | Monthly |
| Creative Center | https://ads.tiktok.com/business/creativecenter | Weekly for trends |
| TikTok Shop Seller Center and Academy | Market-specific Seller Center domains | Monthly; fees and GMV Max |
| Trade press for early signals | ppc.land, socialmediatoday.com, mediapost.com, marketingdive.com | Weekly scan |

## 11. Open questions and watch list

1. Learning phase: current official threshold wording (50 vs 25 conversions) [12, 84, 85].
2. Attribution: full option list per account; whether settings can change after launch; reported "Attribution Portfolio" with assisted conversions (May 2026) [Unverified].
3. Smart+: asset group limits (30 vs 50); TikTok Ad Network auto-inclusion and opt-out; module availability by market [4, 53, 64, 82].
4. GMV Max: GMV Max Pro and cost-aware optimization availability; whether platform-deducted costs change how Target ROI should be set; product exclusivity across campaigns; Spillover reporting availability [62, 69, 79].
5. Buy Direct, Shopping Assistant and Agentic Leads: markets, dates, measurement, policy for AI-led conversations [54, 55, 80].
6. US JV: who contracts ads and e-commerce; any change to data terms; delivery effects of retraining the recommendation algorithm on US data [45, 46].
7. TikTok Ad Network in the US: performance vs TikTok placements; brand safety outcomes; contracting entity [50, 53].
8. EU: DSA enforcement outcomes on ad transparency, consent and minors; any EU-specific product limits [Unverified].
9. Canada: status of the 2024 wind-down order and any effect on ads [Unverified].
10. AI content: any new disclosure requirements for ads built with Symphony or third-party AI tools [58, 59].
11. Benchmarks: a method-published 2026 source for TikTok CPM, CTR and CVR by vertical.

## 12. Sources

1. TikTok Announces New Automation Updates for Advertisers: Smarter Ads, More Control, and Measurable Impact. TikTok Newsroom. https://newsroom.tiktok.com/tiktok-announces-new-automation-updates-for-advertisers?lang=en. 2025-10.
2. TikTok Product Preview: What's New For Brands In Q3 2026. TikTok for Business. https://ads.tiktok.com/business/en/blog/tiktok-product-preview. 2026-07.
3. TikTok World '26: Turning Discovery Into Business Growth with AI-Powered Innovations, Vertical Experiences and High Impact Brand Solutions. TikTok Newsroom. https://newsroom.tiktok.com/tiktok-world-26-eu?lang=en-150. 2026-05.
4. Smart+ Upgraded Experience. TikTok Business Help Center. https://ads.tiktok.com/help/article/about-updates-to-smart-plus?lang=en. Accessed 2026-10.
5. Create Upgraded Smart+ Campaign. TikTok Business Help Center. https://ads.tiktok.com/help/article/how-to-create-a-campaign-in-the-upgraded-smart-experience. Accessed 2026-10.
6. How to use auto-selected creatives for Smart+. TikTok Business Help Center. https://ads.tiktok.com/help/article/how-to-use-auto-selected-creatives. Accessed 2026-10.
7. Best practices for Smart+ Web Campaigns. TikTok Business Help Center. https://ads.tiktok.com/help/article/best-practices-for-smart-plus-web-campaigns. About 2025.
8. Best practices for Smart+ Lead Generation Campaigns. TikTok Business Help Center. https://ads.tiktok.com/help/article/best-practices-for-smart-lead-generation-campaigns. Accessed 2026-10.
9. Smart+ Web Campaigns guide (PDF). TikTok for Business. https://ads.tiktok.com/business/library/ENG_SmartP_Web_Guide_2025.pdf. 2025.
10. How To Build Campaigns Your Way With Smart+. TikTok for Business. https://ads.tiktok.com/business/en-US/blog/smart-plus-ai-performance-solution. 2025 to 2026.
11. About budgets for ads in TikTok Ads Manager. TikTok Business Help Center. https://ads.tiktok.com/resources/help/article/budget. Accessed 2026-10.
12. About Learning Phase. TikTok Business Help Center. https://ads.tiktok.com/help/article/learning-phase. Accessed 2026-10.
13. Bidding strategies. TikTok Business Help Center. https://ads.tiktok.com/help/article/bidding-strategies?lang=en. Accessed 2026-10.
14. Best practices for bidding strategies in TikTok Ads Manager. TikTok Business Help Center. https://ads.tiktok.com/help/article/bidding-best-practices. 2025-12.
15. Tips for Value-based Optimization for web. TikTok Business Help Center. https://ads.tiktok.com/help/article/tips-for-value-based-optimization-for-web. 2025-02.
16. Getting the most out of TikTok ads with value-based optimisation. TikTok for Business. https://ads.tiktok.com/business/en/blog/getting-the-most-out-of-tiktok-ads-with-value-based-optimisation. 2022.
17. About the attribution window on TikTok Ads Manager. TikTok Business Help Center. https://ads.tiktok.com/help/article/about-the-attribution-window-on-tiktok-ads-manager. 2025-02.
18. How to Create Attribution Windows for your Ad Group. TikTok Business Help Center. https://ads.tiktok.com/help/article/attribution-settings-at-the-ad-group-level?lang=en. Accessed 2026-10.
19. About Engaged View-through Attribution. TikTok Business Help Center. https://ads.tiktok.com/resources/help/article/about-engaged-view-through-attribution. Accessed 2026-10.
20. Evolving Our Mobile Measurement Framework For App Advertisers. TikTok for Business. https://ads.tiktok.com/business/en/blog/mobile-measurement-san-app-advertisers. 2023.
21. About event deduplication. TikTok Business Help Center. https://ads.tiktok.com/resources/help/article/event-deduplication. 2025-05.
22. How to set up a Search Ads Campaign in TikTok Ads Manager. TikTok Business Help Center. https://ads.tiktok.com/resources/help/article/how-to-set-up-a-search-ads-campaign-in-tiktok-ads-manager?lang=en. 2026-08.
23. Automatic Search Placement FAQs. TikTok Business Help Center. https://ads.tiktok.com/help/article/faqs-for-automatic-search-placement?lang=en. 2026-06.
24. Search Ads Campaign Availability. TikTok Business Help Center. https://ads.tiktok.com/help/article/search-ads-campaign-availability?lang=en. Accessed 2026-10.
25. Introducing Search Ads Campaign on TikTok. TikTok for Business. https://ads.tiktok.com/business/en-US/blog/introducing-search-ads-campaign. 2024.
26. About GMV Max campaigns in TikTok Ads Manager. TikTok Business Help Center. https://ads.tiktok.com/help/article/about-gmv-max-campaigns-in-tiktok-ads-manager?lang=en. Accessed 2026-10.
27. About ROI protection for GMV Max campaigns. TikTok Business Help Center. https://ads.tiktok.com/help/article/about-roi-protection-for-gmv-max-campaigns?lang=en. 2026-02.
28. Best practices for Max delivery optimization. TikTok Business Help Center. https://ads.tiktok.com/help/article/best-practices-for-max-delivery-optimization. Accessed 2026-10.
29. About LIVE GMV Max. TikTok Business Help Center. https://ads.tiktok.com/help/article/about-live-gmv-max?lang=en. Accessed 2026-10.
30. How to set up LIVE GMV Max Creative boost. TikTok Business Help Center. https://ads.tiktok.com/help/article/how-to-set-up-live-gmv-max-creative-boost?lang=en. Accessed 2026-10.
31. Best practices for increasing creative supply in LIVE GMV Max. TikTok Business Help Center. https://ads.tiktok.com/help/article/best-practices-for-increasing-creative-supply-in-live-gmv-max?lang=en. Accessed 2026-10.
32. Best practices for increasing creative supply in Product GMV Max. TikTok Business Help Center. https://ads.tiktok.com/help/article/best-practices-for-increasing-creative-supply-in-product-gmv-max?lang=en. Accessed 2026-10.
33. GMV Max: Your TikTok Shop Growth Engine. TikTok for Business. https://ads.tiktok.com/business/en-US/blog/gmv-max-automate-shop-roi. 2024 to 2025.
34. TikTok for Business MCP Server (docs v1.3). TikTok API for Business. https://business-api.tiktok.com/portal/docs/tiktok-ads-mcp-server/v1.3. 2026.
35. About TikTok for Business MCP Server. TikTok Business Help Center. https://ads.tiktok.com/resources/help/article/about-tiktok-for-business-mcp-server?lang=en. 2026.
36. About TikTok for Business Agentic Hub and MCP Server. TikTok Business Help Center. https://ads.tiktok.com/resources/help/article/about-tiktok-for-business-agentic-hub-and-mcp-server?lang=en. 2026.
37. Evolving TikTok For Business MCP: New AI platforms To Streamline Your Ad Workflows. TikTok for Business. https://ads.tiktok.com/business/en/blog/tiktok-agentic-hub-ai-agents-skills-mcp. 2026.
38. Announcing Symphony Creative Studio. TikTok for Business. https://ads.tiktok.com/business/en-US/blog/symphony-creative-studio. 2024.
39. Symphony Creative Studio (product home). TikTok for Business. https://ads.tiktok.com/creative/creativestudio/home/en. Accessed 2026-10.
40. How creators can sign up for TikTok One. TikTok Business Help Center. https://ads.tiktok.com/resources/help/article/how-creators-can-sign-up-for-tiktok-one. Accessed 2026-10.
41. How creators can upgrade to TikTok One. TikTok Business Help Center. https://ads.tiktok.com/help/article/how-creators-can-upgrade-to-tiktok-one. 2025.
42. TikTok Unveils AI-Powered Updates for Advertisers: Driving Discovery, Action, and Measurable Business Outcomes. TikTok Newsroom. https://newsroom.tiktok.com/tiktok-unveils-ai-powered-updates-for-advertisers-driving-discovery-action-and-measurable-business-outcomes?lang=en. Date unverified.
43. TikTok for Business Blog (index, TikTok Ad Network listing). TikTok for Business. https://ads.tiktok.com/business/en-US/blog. 2026-10.
44. TikTok finalizes deal to form new American entity. NPR. https://www.npr.org/2026/01/22/nx-s1-5685456/tiktok-finalizes-deal-to-form-new-american-entity. 2026-01-22.
45. TikTok USDS. Wikipedia. https://en.wikipedia.org/wiki/TikTok_USDS. Accessed 2026-10.
46. TikTok pitches advertisers on bold new chapter under US joint venture. Marketing Dive. https://www.marketingdive.com/news/tiktok-pitches-advertisers-on-bold-new-chapter-under-us-joint-venture/815632/. 2026-03.
47. TikTok Boasts Of Joint Venture And Improvements For Advertisers. MediaPost. https://www.mediapost.com/publications/article/413892/tiktok-boasts-of-joint-venture-and-improvements-fo.html. 2026-03-27.
48. TikTok NewFront Highlights U.S. Venture, Ad Reach. MediaPost. https://www.mediapost.com/publications/article/413918/tiktok-newfront-highlights-us-venture-ad-reach.html. 2026-03-30.
49. TikTok broadens agentic AI play, brings global ad network to US. Marketing Dive. https://www.marketingdive.com/news/tiktok-broadens-agentic-ai-play-brings-global-ad-network-to-us/832007/. 2026-10.
50. TikTok opens ad network of nearly 400,000 apps to US advertisers. PPC Land. https://ppc.land/tiktok-opens-ad-network-of-nearly-400-000-apps-to-us-advertisers/. 2026-10.
51. TikTok Unveils Third-Party Ad Network Updates. MediaPost. https://www.mediapost.com/publications/article/418518/tiktok-unveils-third-party-ad-network-updates.html. 2026-10-06.
52. TikTok launches an external ad network across nearly 400k apps. Music Ally. https://musically.com/2026/10/06/tiktok-launches-an-external-ad-network-across-nearly-400k-apps/. 2026-10-06.
53. TikTok Now Sells Ads in 400,000 Other Apps. Should Your Budget Leave TikTok? Mintec. https://mintec.co/blog/tiktok-ad-network-us-launch/. 2026-10.
54. TikTok adds Buy Direct, Agentic Leads and GMV Max changes. Relevant Audience. https://www.relevantaudience.com/tiktok-ads/tiktok-advertising-week-2026-buy-direct-agentic-leads-gmv-max/. 2026-10.
55. TikTok AI-Powered Updates for Advertisers unveiled. ChannelX. https://channelx.world/2026/10/tiktok-ai-powered-updates-for-advertisers-unveiled/. 2026-10.
56. TikTok opens third-party ad network to U.S. advertisers. The Desk. https://thedesk.net/2026/10/tiktok-opens-pangle-to-us-advertisers/. 2026-10.
57. TikTok Expands 'Symphony,' Offers AI Video For Brands, Creators. MediaPost. https://www.mediapost.com/publications/article/414301/tiktok-expands-symphony-offers-ai-video-for-bra.html. 2026-04-15.
58. TikTok Unveils AI Ad Agent, Dentsu Integration, Creator Networks. MediaPost. https://www.mediapost.com/publications/article/415987/tiktok-unveils-ai-ad-agent-dentsu-integration-cu.html. 2026-06-23.
59. TikTok Symphony Creative Studio: The Working Guide to Avatars, Rights, and the AI Label. Riffkit. https://riffkit.ai/blog/tiktok-symphony-creative-studio-guide. 2026.
60. TikTok sunsets its Creator Marketplace for TikTok One, a broader solution with AI tools. TechCrunch. https://techcrunch.com/2025/02/27/tiktok-sunsets-its-creator-marketplace-for-tiktok-one-a-broader-solution-with-ai-tools. 2025-02-27.
61. Major ad tool announcements from TikTok World 2026. Yahoo Tech. https://tech.yahoo.com/social-media/articles/major-ad-tool-announcements-tiktok-191510004.html. 2026-05.
62. TikTok World 2026 Ad Updates: What TopReach, Smart+, Symphony, GMV Max and Search Hubs Mean for Marketers. ALM Corp. https://almcorp.com/blog/tiktok-world-2026-ad-tool-announcements/. 2026-05.
63. TikTok lets advertisers block up to 40% of regions in TopView buys. PPC Land. https://ppc.land/tiktok-lets-advertisers-block-up-to-40-of-regions-in-topview-buys/. 2026.
64. TikTok just made its Smart+ automation actually usable for advertisers. PPC Land. https://ppc.land/tiktok-just-made-its-smart-automation-actually-usable-for-advertisers/. 2026-01.
65. TikTok Upgrades Smart+ Ad Suite Ahead of Holiday Season. Influencer Marketing Hub. https://influencermarketinghub.com/tiktok-smart-plus-ad-suite-automation/. 2025-10.
66. TikTok Adds More Control Options to Smart+ Campaigns. Social Media Today. https://www.socialmediatoday.com/news/tiktok-adds-more-control-options-to-smart-campaigns/810168/. 2026-01.
67. Everything you need to know about TikTok Search Ads in 2026. Datashake. https://www.datashake.fr/en/articles/everything-about-tiktok-search-ads. 2026.
68. TikTok introduces Attribution Manager with flexible windows. Search Engine Land. https://searchengineland.com/tiktok-introduces-attribution-manager-with-flexible-windows-386066. 2022-06-27.
69. TikTok Updates GMV Max to Include Seller Costs. The Keyword. https://www.thekeyword.co/news/tiktok-gmv-max-update-seller-costs. 2026-05.
70. TikTok's GMV Max ROI guarantee: advertiser protection or platform control? PPC Land. https://ppc.land/tiktoks-gmv-max-roi-guarantee-advertiser-protection-or-platform-control/. 2025 to 2026.
71. GMV Max Becomes the Default (and Only) TikTok Shop Ad Format. Ethan Kramer. https://www.ethankramer.com/blog/tiktok-shop-gmv-max-default-update-2025. 2025.
72. TikTok Shop Replaces Traditional Ads with GMV Max: What Sellers Must Know in 2025. TBA Global. https://tbaglobal.com/tiktok-shop-replaces-traditional-ads-with-gmv-max-what-sellers-must-know-in-2025/. 2025.
73. TikTok Shop GMV Max: What Changed, How It Works, and What Sellers Do Now. Agentative. https://agentative.ai/blog/tiktok-shop-gmv-max-sellers-guide. 2026.
74. Event Match Quality (EMQ): What Actually Matters on Meta and TikTok. Triple Whale. https://www.triplewhale.com/blog/event-match-quality. 2025.
75. TikTok Events API. Journify. https://www.journify.io/resources/tiktok-events-api/. 2025 to 2026.
76. Engaged Ad Interaction Attribution With Meta and TikTok. Kochava. https://www.kochava.com/blog/open-beta-engaged-ad-interaction-attribution-with-meta-tiktok/. 2023 to 2024.
77. tiktok-ads-mcp. GitHub (ysntony). https://github.com/ysntony/tiktok-ads-mcp. Accessed 2026-10.
78. TikTok Ads MCP Server by AdsMCP Team. PulseMCP. https://www.pulsemcp.com/servers/adsmcp-tiktok-ads. 2025-09-17.
79. GMV Max 2026: TikTok's Latest Updates to Maximize TikTok Shop Growth. Ecomdy Media. https://ecomdymedia.com/blog/gmv-max-2026-tiktok-shop-updates. 2026.
80. TikTok Advertising Week 2026: Buy Direct, Shopping Assistant, and the new ad network. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/tiktok-advertising-week-2026-buy-direct-shopping-assistant-and-the-new-ad-network-every-ecommerce-brand-must-know. 2026-10.
81. TikTok Smart+ Just Changed How Every Ecommerce Brand Should Build Campaigns. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/tiktok-smart-just-changed-how-every-ecommerce-brand-should-build-campaigns-what-to-do-before-q4. 2026-09 to 2026-10.
82. TikTok Smart+ 2026 Guide: Controls, Creative and Budgets. Segwise. https://segwise.ai/blog/tiktok-smart-campaigns-guide-benefits. 2026.
83. Upgraded Smart+ Campaigns. Sprinklr Help. https://www.sprinklr.com/help/articles/publish-tiktok-ads/upgraded-smart-campaigns/695ce24bf0afa271d1900581. 2026.
84. TikTok Learning Phase: What Advertisers Need to Pass It. Mega Digital. https://megadigital.ai/en/blog/tiktok-learning-phase/. 2026.
85. TikTok ad learning phase. TikAdTools. https://tikadtools.com/blog/tiktok-ad-learning-phase/. 2026.
86. TikTok introduces Symphony Digital Avatars. VentureBeat. https://venturebeat.com/ai/tiktok-introduces-symphony-digital-avatars-ai-dubbing. 2024-06.
87. TikTok ads bidding. WordStream. https://www.wordstream.com/blog/tiktok-ads-bidding. Accessed 2026-10.
