# Research Dossier: AI Search Optimization (GEO, AEO, LLMO)

> Compiled 2026-10-08 for the Ads Master `ai-search-optimization` package. Evidence labels: [Official, YYYY-MM], [Study, YYYY-MM], [Practitioner consensus], [Contested], [Unverified]. Source numbers in brackets like (S12) refer to the numbered Sources list at the end.

## Research method and limits

1. 22 web searches were completed (extended mode for 2026 topics) before a shared per-turn search budget was exhausted. The brief's target was 35 or more. Direct page fetching was unavailable in this environment, so primary documents were read through search result extracts and trade press summaries.
2. Where a claim rests on secondary coverage, it is marked "secondary". Where it rests on model knowledge from before 2026-06 and could not be re-verified, it is labeled [Unverified] or dated to the original publication.
3. Not read in primary form this cycle: Kevin Indig (Growth Memo) 2026 studies, iPullRank 2026 material, Conductor 2026 studies, OpenAI help center shopping and merchant pages. These are flagged in the watch list for the next research cycle.
4. Verification pass (2026-10-08): about 18 additional extended web searches re-checked the Search Console Generative AI report and AI control, the Google AI contribution pilot, the Gemini models in AI Mode, the Merchant Center UCP integration hub, Claude's search provider, Cloudflare's 2026-09-15 defaults and bot classes, google.com/goto links, ChatGPT referral behavior, and new citation studies from Ahrefs, Semrush, Profound, SparkToro, Seer and BrightEdge (2026-03 to 2026-09). Labels below were upgraded or corrected where confirmed.

## Executive summary

1. ChatGPT no longer leans mainly on Bing. A source field exposed between 2026-05-21 and 2026-07-21 showed an internal OpenAI index (reported as "Labrador") supplying about 75% of free-tier sources, while paid mode drew about 75% from scraped Google results; only about 1.5% of Labrador URLs matched Bing's top 20 [Study, 2026-07] (S24, S25, S27).
2. Google now reports AI visibility: the Search Console Generative AI performance report launched 2026-06-03 and reached all sites worldwide on 2026-08-31. It shows impressions only, AI Overviews and AI Mode combined with no filter to split them (search type filter: Web text-based or Web multimodal), by page, country and date, with data from 2026-05-18 and no clicks or queries. It is not in the Search Console API or the BigQuery bulk export as of 2026-10 [Official, 2026-06 to 2026-08] (S6, S42, S43, S78).
3. Publishers can opt out of AI Overviews, AI Mode and Discover AI features with a property-level Search Console control (Settings, "Search generative AI"), launched 2026-06-03 under UK CMA pressure and worldwide by 2026-08-31. It does not cover the Gemini app or training; page-level control is due by 2027-03 [Official, 2026-06] (S7, S44 to S46).
4. Microsoft shipped the first citation-level first-party data: Bing Webmaster Tools AI Performance (public preview 2026-02-10) reports citations, cited pages and grounding queries; Intents, Topics, Citation Share and Compare were added 2026-06-16 [Official, 2026-02 and 2026-06] (S9, S47, S48).
5. Access is the most common silent failure. Cloudflare has blocked AI training crawlers by default for new domains since 2025-07-01. From 2026-09-15 its defaults block the Training and Agent bot classes on pages that show ads while allowing Search bots, for new domains, new sites of existing customers and existing free plan zones that had not changed their AI settings; paid customers who had chosen settings keep them. Cloudflare's Radar directory classes ChatGPT-User as Agent while its AI Crawl Control docs list ChatGPT-User and Claude-User as AI Assistant, and multi-purpose crawlers (Googlebot, Bingbot, Applebot) are blocked wherever Training is blocked [Official, 2026-07] (S76, S77, S55).
6. AI answers are not stable rankings: in SparkToro and Gumshoe's study (2,961 responses), there was under a 1 in 100 chance of the same brand list twice for the same prompt, and under 0.1% for the same order [Study, 2026] (S28). Measure mention rates across many runs.
7. Off-site brand mentions are the strongest measured correlate of AI Overview brand visibility (Spearman 0.664 for branded web mentions vs weaker link metrics; about 75k brands) [Study, 2025] (S17). Correlation, not proof, but consistent with how retrieval works.
8. Google AI Overviews cut clicks hard: Ahrefs measured about 58% lower CTR for the top-ranking page when an AI Overview appears (Dec 2023 vs Dec 2025, 300k keywords), up from 34.5% in its 2025-04 study; Seer found cited brands earn materially more organic and paid clicks than uncited brands on the same SERP [Study, 2025 to 2026] (S18 to S21).
9. llms.txt has no demonstrated effect: Google says it is not used for Search; an Ahrefs log study of 137k domains found 97% of llms.txt files received zero requests in 2026-05, and SE Ranking found no correlation with citations across about 300k domains [Study and Official statements, 2025 to 2026] (S38, S39, S52 to S54).
10. Agentic commerce shifted from in-chat checkout to discovery: OpenAI moved away from Instant Checkout in 2026-03 (merchant checkout and merchant apps instead) and kept the Agentic Commerce Protocol for discovery and app-based transactions, while Google's Universal Commerce Protocol (announced 2026-01-11) powers checkout in AI Mode and Gemini; the Merchant Center UCP integration hub began a gradual US rollout on 2026-10-06 (selected merchants, interest form, sandbox), with Canada and Australia expected in 2027 [Official, 2026-03 and 2026-10] (S58 to S62, S81, S82).

## State of the channel in 2026

### Usage and traffic

| Metric | Value | Source, date | Caveat |
|--------|-------|--------------|--------|
| ChatGPT weekly active users | 800M (2025-10); more than 1B (2026-08); 1.2B weekly people (2026-10-05) | OpenAI [Official, 2025-10 and 2026-10] | Weekly people, not engaged searchers |
| AI Overviews monthly users | Over 2B (2025-07); over 2.5B (I/O, 2026-05-19) | Google [Official, 2025-07 and 2026-05] | Users exposed, not engaged |
| AI Mode monthly users | Over 100M in US and India (2025-07); over 1B globally (I/O, 2026-05-19; repeated on the 2026-07-22 earnings call) | Google [Official, 2025-07 and 2026-05] | About 200 countries and 98 languages targeted at I/O 2026; live in France from 2026-07-22. AI Mode was only 0.34% of US Google searches January to April 2026 (SparkToro with Similarweb) [Study, 2026] |
| ChatGPT share of generative AI web traffic | About 76% (2025-06) to about 53% (2026-05) | Similarweb via secondary, 2026 [Study] | Visits to AI sites, not referrals |
| AI chatbot referral share | ChatGPT 79.4%, Gemini 10.9%, Perplexity 4.3%, Copilot 2.8%, Claude 2.6% | Statcounter via secondary, 2026-08 [Study] | Global panel |
| ChatGPT share of AI referrals (BrightEdge dataset) | 95.1% in August 2026; ChatGPT referrals up 101% January to August 2026 | BrightEdge, 2026-09-24 [Study, 2026-09] | Vendor customer data; different denominator from Statcounter |
| Google zero-click rate (US) | 68.01% of searches January to April 2026, up from 60.45% in 2024 | SparkToro with Similarweb clickstream, 2026 [Study, 2026] | Panel data; AI Overviews share of the rise not isolated |
| B2B AI referral share | ChatGPT 62.6%, Claude 18.5%, Gemini 10.6%, Perplexity 7.3% | B2B study blending GA4 and Similarweb, 2026 [Study, secondary] | Single vendor study |
| AI referrals as share of site sessions | Typically under 1% | Multiple analyses 2025 to 2026 [Practitioner consensus] | Undercounted: app and copy-paste traffic |
| ChatGPT referrals landing on homepages | About 25 to 32% before 2026-05-07, about 60% after; total ChatGPT referrals up 157.7% week over week; the higher homepage share held through August per later analyses | Similarweb, 2026-05 [Study] (S34) | Caused by more prominent inline brand links in answers from 2026-05-07. ChatGPT appends utm_source=chatgpt.com to referral links [Official] (S80) |

### How engines retrieve (summary)

| Engine | Retrieval in 2026 | Evidence |
|--------|-------------------|----------|
| Google AI Overviews and AI Mode | Google index, query fan-out, Gemini models; indexed and snippet-eligible pages only | [Official] (S4, S5) |
| ChatGPT | Own index (Labrador) plus scraped Google results and a news provider; mix differs by tier and mode | [Study, 2026-07] (S24, S25) |
| Perplexity | Own index via PerplexityBot plus live fetch via Perplexity-User | [Official] (S3) |
| Copilot | Bing index; grounding queries visible in Bing Webmaster Tools | [Official, 2026] (S9) |
| Claude | Web search tool plus Anthropic index (Claude-SearchBot) and user fetch (Claude-User). Anthropic's subprocessor list names Brave Search (and TurboPuffer) under Web Search as of 2026-09-02; Profound measured 86.7% overlap between Claude-cited URLs and Brave's top results | [Official, 2026-09] (S2, S79); overlap [Study, 2025] |
| Gemini app | Google Search grounding; controlled by Google-Extended | [Official] (S8) |

### Citation source mix (dated and engine-specific)

| Finding | Source, date |
|---------|-------------|
| ChatGPT: Wikipedia 47.9% of top-10 source share; Perplexity: Reddit 46.7%; AIO: Reddit 21.0%; ChatGPT and Perplexity domain overlap about 11% | Profound, 2025 (data 2024-08 to 2025-06) (S29) |
| YouTube overtook Reddit as a cited social source around 2025-10 (16% vs 10% of answers) | Bluefish via Adweek, 2026 (secondary) |
| YouTube 26.47% vs Reddit 17.39% of citations | LLM Pulse, 2026-05 (secondary) |
| Reddit, YouTube, LinkedIn most cited across engines | Search Engine Land report, 2026 (S31) |
| Reddit's share of ChatGPT citations fell 3.83% to 0.52% in four days | Promptwatch via Search Engine Land, 2025-09 (secondary; cause contested) |
| Forums about 2%, brand-controlled sources 86% | Yext, 6.8M citations, 2025 (secondary) |
| Community platforms 52.5% vs brand domains 47.5% | OtterlyAI, 1M+ citations, 2026 (S32) |
| AI Mode cites 143% more unique domains than AI Overviews | Analysis via secondary, 2026-01 |
| ChatGPT: Reddit 28.9% and Wikipedia 23.1% of citations (community and reference sources about 59%); AI Mode: YouTube 21.1% top source; about 69% overlap in most-mentioned brands across 22 industries (data 2026-01 to 2026-06) | Semrush AI Visibility Index mini study, 2026-08 (S84) |
| ChatGPT cites about 15 sources per answer vs Gemini about 3 (126M US prompts, data 2026-01 to 2026-04) | Semrush AI Visibility Index, 2026-06-26 (S83) |
| Mention share of top sources, US, September 2026: ChatGPT Reddit 16.8%, Wikipedia 7.0%; AI Overviews YouTube 22.9%, Reddit 18.5%; Gemini Reddit 28.5%, YouTube 14.6% | Ahrefs Brand Radar monthly leaderboards, 2026-09 (S85); share of top sources only, refreshed monthly |
| AI Overviews appear on 83% of branded searches; Wikipedia, YouTube and LinkedIn most cited for branded AIOs (232.8M US desktop SERP crawls, 2026-07 to 2026-09) | Ahrefs, 2026-09 (S86) |
| Query language changes source mix; 3.25B citations, 7 models, 14 countries; first conversation turn cites about 2.5x more than turn 10 | Profound, 2026-03 (S87) |

## Timeline of changes, January 2025 to October 2026

| Date | Change | Engine or platform | Evidence |
|------|--------|-------------------|----------|
| 2025-02 | ChatGPT search available without login | OpenAI | [Official, 2025-02] |
| 2025-03-05 | AI Mode announced as a Labs experiment; Gemini 2.0 in AI Overviews | Google | [Official, 2025-03] |
| 2025-03 | Claude web search launches (US, paid plans); all plans 2025-05 | Anthropic | [Official, 2025] |
| 2025-03 | Bing's Fabrice Canel says schema helps Microsoft's LLMs understand content (SMX Munich) | Microsoft | [Practitioner report, 2025-03] |
| 2025-04 | ChatGPT memory can reference all past chats (Plus and Pro) | OpenAI | [Official, 2025-04] |
| 2025-04 | Ahrefs: AI Overviews reduce top-page clicks 34.5% | Study | [Study, 2025-04] (S18) |
| 2025-04-28 | Improved shopping results in ChatGPT search (not ads) | OpenAI | [Official, 2025-04] |
| 2025-05-20 | Google I/O: AI Mode to all US users; query fan-out and Deep Search described; agentic checkout announced | Google | [Official, 2025-05] (S5) |
| 2025-05-21 | Google Search Central guidance on succeeding in AI search: no special optimization needed | Google | [Official, 2025-05] |
| 2025-06 | AI Mode clicks and impressions counted in Search Console Web totals | Google | [Official, 2025-06; secondary] |
| 2025-07-01 | Cloudflare default blocking of AI crawlers for new domains; pay per crawl beta | Cloudflare | [Official, 2025-07] (S10) |
| 2025-07 | Perplexity Comet browser launches | Perplexity | [Official, 2025-07] |
| 2025-07-22 | Pew: 8% vs 15% click rate with vs without AI summary | Study | [Study, 2025-07] (S41) |
| 2025-07 | AI Overviews over 2B monthly users; AI Mode over 100M MAU in US and India | Google | [Official, 2025-07] |
| 2025-08-04 | Cloudflare accuses Perplexity of stealth crawling; delists it as verified bot; Perplexity disputes | Cloudflare, Perplexity | [Official, 2025-08; Contested] (S11, S57) |
| 2025-08 | Google says total organic click volume relatively stable, quality clicks up | Google | [Official, 2025-08] |
| 2025-08-11 | Bing Search APIs retired; Grounding with Bing Search in Azure AI agents | Microsoft | [Official, 2025] |
| 2025-08 | AI Mode expands to 180+ countries in English | Google | [Official, 2025-08] |
| 2025-09 | Google stops supporting the 100 results per page parameter; rank trackers and Search Console impressions shift | Google | [Practitioner consensus, 2025-09] |
| 2025-09 | Reddit citations in ChatGPT drop sharply in days | OpenAI | [Study, 2025-09, secondary; cause Contested] |
| 2025-09-24 | Cloudflare Content Signals Policy (search, ai-input, ai-train) in managed robots.txt for 3.8M+ domains | Cloudflare | [Official, 2025-09] (S56) |
| 2025-09-29 | Instant Checkout in ChatGPT with Etsy; Agentic Commerce Protocol with Stripe | OpenAI | [Official, 2025-09] |
| 2025-10 | OpenAI DevDay: apps in ChatGPT, 800M weekly users; ChatGPT Atlas browser (2025-10-21) | OpenAI | [Official, 2025-10] |
| 2025-10 | Wikimedia reports declining human pageviews linked to AI summaries | Wikimedia | [Official, 2025-10; Unverified exact figure] |
| 2025-11 | Seer: organic CTR on AIO queries 1.76% to 0.61%; cited brands 35% more organic, 91% more paid clicks | Study | [Study, 2025-11] (S21) |
| 2025-11-18 | Gemini 3 in AI Mode | Google | [Official, 2025-11] |
| 2025-11 | ChatGPT shopping research; Perplexity agentic shopping with PayPal | OpenAI, Perplexity | [Official, 2025-11; Perplexity date Unverified] |
| 2025-11 to 2025-12 | SparkToro and Gumshoe fieldwork on answer variance (published 2026) | Study | [Study, 2026] (S28) |
| 2025-11 | Adobe announces agreement to acquire Semrush | Industry | [Official, 2025-11; closing Unverified] |
| 2026-01-11 | Universal Commerce Protocol announced at NRF (Shopify, Etsy, Wayfair, Target, Walmart) | Google | [Official, 2026-01] (S58) |
| 2026-01 | OpenAI announces testing of ads in ChatGPT | OpenAI | [Official, 2026-01; owned by `chatgpt-ads`] |
| 2026-01-27 | Gemini 3 becomes the default model for AI Overviews; follow-up questions from an AI Overview continue in AI Mode | Google | [Official, 2026-01] |
| 2026-01-27 | Bing AI Performance report spotted in limited beta | Microsoft | [Secondary, 2026-01] (S48) |
| 2026-02-10 | Bing Webmaster Tools AI Performance public preview | Microsoft | [Official, 2026-02] (S9) |
| 2026-02 | Ahrefs update: about 58% lower CTR for position 1 with AIO | Study | [Study, 2026-02] (S19, S63) |
| 2026-02 | Forrester: about 30 Shopify merchants live on Instant Checkout | Study | [Study, 2026-02, secondary] |
| 2026-02 | AI Mode adds 53 languages (just under 100 in total) | Google | [Official, 2026-02, via trade press] |
| 2026-03 | Profound: query language reshapes AI citations (3.25B citations) | Study | [Study, 2026-03] (S87) |
| 2026-03-06 to 2026-03-24 | OpenAI moves away from Instant Checkout ("did not offer the level of flexibility that we aspire to provide"); merchant-handled checkout and merchant apps; ACP kept for discovery and app-based transactions | OpenAI | [Official, 2026-03] (TechCrunch, Digital Commerce 360) |
| 2026-03-23 | Bing AI Performance adds grounding query to page mapping (worldwide, verified sites) | Microsoft | [Official, 2026-03] |
| 2026-03 | UCP adds multi-item carts, real-time catalog and identity linking | Google | [Secondary, 2026-03] (S72) |
| 2026-03-24 | Revamped ChatGPT shopping focused on discovery; Shopify Agentic Storefronts on by default for eligible merchants | OpenAI, Shopify | [Secondary, 2026-03] |
| 2026 (spring) | Seer 2026 CTR update: 53 brands, 5.47M queries, 2.43B organic impressions | Study | [Study, 2026] (S20) |
| 2026-05 | Ahrefs llms.txt log study: 97% of 137k domains' files got zero requests | Study | [Study, 2026-05, secondary] |
| 2026-05 | Ahrefs schema study: 1,885 pages that added JSON-LD vs 4,000 controls showed no significant citation gain (AI Mode +2.4%, ChatGPT +2.2%, AI Overviews minus 4.6%) | Study | [Study, 2026-05] (S88) |
| 2026-05-19 | Google I/O 2026: AI Mode over 1B monthly users, AI Overviews over 2.5B; Gemini 3.5 Flash the default AI Mode model | Google | [Official, 2026-05] |
| 2026-05 | Google's John Mueller: llms.txt "not done for search"; separate markdown files a temporary measure | Google | [Practitioner report, 2026-05] (S52, S53) |
| 2026-05 | UCP checkout reported on YouTube Shopping | Google | [Secondary, 2026-05] |
| 2026-05-07 | ChatGPT referrals to homepages jump to about 60% | OpenAI | [Study, 2026-05] (S34) |
| 2026-05-18 | Start of data in Search Console Generative AI report | Google | [Official, 2026-06] (S6) |
| 2026-05-21 to 2026-07-21 | ChatGPT exposes retrieval source field; Labrador analyses | OpenAI | [Study, 2026-07] (S24, S25) |
| 2026-05-28 | Yoast AI Brand Insights adds Claude tracking | Vendor | [Official vendor, 2026-05] (S65) |
| 2026-06-03 | Search Console Generative AI report and Search generative AI control launched (UK first) after UK CMA conduct requirement | Google | [Official, 2026-06] (S6, S7, S46) |
| 2026-06-16 | Bing AI Performance adds Intents, Topics, Citation Share, Compare | Microsoft | [Official, 2026-06] |
| 2026-06-26 | Semrush AI Visibility Index expands to 126M US prompts | Study | [Study, 2026-06] (S83) |
| 2026-07-01 | Cloudflare announces 2026-09-15 defaults: Search, Agent and Training bot classes; Training and Agent blocked on pages with ads; Pay Per Use with Ceramic.ai and You.com | Cloudflare | [Official, 2026-07] (S76, S77) |
| 2026-07-22 | AI Overviews and AI Mode launch in France | Google | [Official, 2026-07, via trade press] |
| 2026-08 | Statcounter AI referral shares: ChatGPT 79.4%, Gemini 10.9% | Study | [Study, 2026-08, secondary] |
| 2026-08 | Semrush: ChatGPT vs AI Mode brand and source divergence (22 industries) | Study | [Study, 2026-08] (S84) |
| 2026-08-14 | Gemini 3.7 Flash selectable in AI Mode for subscribers | Google | [Official, 2026-08, via trade press] |
| 2026-08-26 | Google confirms google.com/goto passthrough links on results (organic, PAA, AI Overviews); tests show referrers still pass | Google | [Official, 2026-08, via Search Engine Roundtable] (S89) |
| 2026-08-31 | European Commission designates ChatGPT a Very Large Online Search Engine under the DSA | EU | [Official, 2026-08] |
| 2026-08-31 | Search Console AI report and AI control available to all sites worldwide | Google | [Official, 2026-08] (S42, S43) |
| 2026-09-15 | Cloudflare new default bot policy takes effect | Cloudflare | [Official, 2026-07, via trade press] |
| 2026-09-02 | Gemini 3.8 Flash selectable in AI Mode for Google AI Pro and Ultra subscribers (English, global); free users stay on the default model | Google | [Official, 2026-09] (Robby Stein on X, via trade press) |
| 2026-09 | Google confirms the Search Console "AI Contribution" pilot: about 100 invited publishers paid when content contributes to AI Overviews, AI Mode and Gemini; opaque formula; payment and usage are separate choices | Google | [Official, 2026-09] (confirmed to Search Engine Land and Digiday) (S90, S91) |
| 2026-09 | AI Mode answered 97% of sampled People Also Ask answers | Study | [Unverified, single secondary source] |
| 2026-09-24 | BrightEdge: ChatGPT 95.1% of AI referrals in August; referrals up 101% January to August | Study | [Study, 2026-09] (S92) |
| 2026-10-06 | Merchant Center UCP integration hub begins gradual US rollout (cart transfer, native checkout, identity linking; selection via interest form; sandbox); Canada and Australia expected 2027 | Google | [Official, 2026-10] (S81, S82, S60) |

## Best practice consensus

1. Verify and allow the search and user-fetch bots of every engine you want visibility in; check the CDN and WAF, not just robots.txt [Official] (S1 to S3, S10).
2. Serve all citable content in server-rendered HTML; AI crawlers other than Googlebot and Applebot did not execute JavaScript in 2024 log data [Study, 2024-12] (S40).
3. Keep classic SEO strong: Google AI features require indexed, snippet-eligible pages, and Google says no special optimization is required [Official] (S4).
4. Structure content as self-contained, answer-first passages that name the entity and state specific, sourced facts [Practitioner consensus; Study for statistics and quotations] (S15).
5. Earn mentions on the third-party domains each engine cites for the category (listicles, review platforms, YouTube, Reddit, Wikipedia) [Study, 2025 to 2026] (S17, S29 to S32).
6. Maintain one consistent set of brand facts across the site, schema, profiles and review platforms [Practitioner consensus].
7. Measure with prompt sets, repeated runs and rates, not single answers [Study, 2026] (S28).
8. Use first-party data: Search Console Generative AI report, Bing AI Performance, GA4 AI channel group, server logs [Official, 2026] (S6, S9).
9. Do not invest in llms.txt as a visibility lever [Study and Official statements, 2025 to 2026] (S52 to S54).
10. Refuse manipulation: fake reviews (FTC rule effective 2024-10), astroturfing and hidden instructions carry legal, platform and trust risk [Official, 2024].

## Contested topics (both sides)

| Topic | For | Against | Resolution used in package |
|-------|-----|---------|----------------------------|
| Is GEO different from SEO? | Off-site mentions, non-Google indexes (ChatGPT's Labrador), passage structure and statistical measurement are distinct work (S17, S24, S28) | Google: no special optimization beyond SEO fundamentals (S4) | SEO is the foundation; AI visibility adds off-site, entity and measurement work |
| Schema and AI citations | AirOps: 61% of ChatGPT-cited pages had structured data vs 25% of Google top results (secondary); Bing says schema helps | Google: not required. Ahrefs controlled study (2026-05): adding JSON-LD to 1,885 pages produced no significant citation gain vs 4,000 controls | Implement for entity clarity and rich results; never promise citation lift |
| Overlap of AI citations with top 10 | Ahrefs 2025: 76% of AIO citations from top 10 | Moz 2026: about 12% of AI Mode citations in top 10; a roundup cites 17% for AIO | Overlap shrinking as fan-out widens; rank for sub-queries |
| Reddit as a lever | Most cited domain in several datasets (S29, S31) | Volatile (ChatGPT drop 2025-09); partnership-funded studies; manipulation risk | Genuine participation only; diversify |
| Brand-owned vs community sources | Yext: 86% brand-controlled | OtterlyAI: 52.5% community (S32) | Depends on prompt type; map your own |
| AI traffic conversion | Ahrefs own site 23x; Semrush modeled 4.4x value | Single site, modeled, self-selected | Measure own data |
| Allowing training crawlers | Builds future parametric recall for brands | Publishers lose licensing leverage | Brands usually allow; publishers decide by licensing |
| Perplexity stealth crawling | Cloudflare evidence of undeclared crawlers (S11) | Perplexity says the bot was not theirs and no content was opened (S57) | Treat as unresolved; verify bots via signatures and IP files |
| Instant Checkout status | Described as "shut down" by several blogs | OpenAI said it is moving away from it in favor of merchant checkout and merchant apps; no formal shutdown announcement (TechCrunch, 2026-03-24) | Resolved for planning: treat ChatGPT as discovery, checkout on site or in merchant apps |
| Cloudflare 2026-09-15 scope for existing sites | Existing free plan zones that had not changed settings are covered (Cloudflare wording quoted by trade press) | Paid customers with chosen settings unchanged (Cloudflare press release) | Largely resolved; still check each zone, and check how ChatGPT-User and Claude-User are classed (Agent in Radar, AI Assistant in AI Crawl Control docs) |

## What top operators do differently

1. They check logs and CDN dashboards for AI bot status codes before touching content, and re-check after every CDN, plugin or migration change.
2. They split ChatGPT tracking by mode (free, paid, think) because retrieval differs, and split Google into AI Overviews and AI Mode.
3. They run 3 to 10 runs per prompt, freeze the prompt set, and report intervals; they never sell a "rank".
4. They build fan-out maps per prompt and use Bing grounding queries as a real fan-out log.
5. They map cited domains per engine and run PR, review and community work against that list, not a generic outreach list.
6. They publish original data in HTML with quotable sentences and pitch it to the journalists who write the cited pages.
7. They publish public pricing (or clear ranges) and honest comparison and alternatives pages with dates.
8. They maintain a brand fact sheet and correct third-party profiles within days of any change.
9. They treat wrong AI answers as source problems and trace citations before acting.
10. They keep the homepage answer-ready (what, who for, price, proof) because AI referrals increasingly land there (S34).
11. They pair AI referral data with self-reported attribution and branded search trend.
12. They decline vendor scores without method disclosure and document why.

## Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|-----------|
| Cloudflare or WAF silently blocking OAI-SearchBot, Claude-SearchBot or PerplexityBot | Invisible in those engines for months | Monthly log check by token |
| Blocking Google-Extended "to protect content" while wanting Gemini visibility | Loses Gemini app grounding | Documented crawler policy with trade-offs |
| Client-side rendered pricing, specs or reviews | Facts invisible to AI crawlers | Rendering test in every audit |
| Reporting single-run screenshots as wins or losses | Wrong decisions, lost credibility | Rates with intervals |
| Buying llms.txt, schema or "AI ranking" packages as the strategy | Spend with no measurable effect | Evidence grading |
| Astroturfing Reddit or buying reviews | Bans, FTC exposure, reputational damage | Red lines and audit detection |
| Opting out of Google AI features without modeling | Lost impressions and clicks to competitors | Decision memo with approval |
| Adding Generative AI impressions to Web totals | Inflated reporting | Use Web search type as the denominator |
| Optimizing for Bing only to win ChatGPT | Misses the free tier's own index | Track ChatGPT directly |
| Ignoring wrong pricing on review platforms | AI repeats old prices | Fact sheet sync cadence |

## Benchmarks

| Benchmark | Value | Source, date, sample | Caveat |
|-----------|-------|---------------------|--------|
| AIO CTR effect on position 1 | About 58% lower | Ahrefs, 2026-02, 150k AIO vs 150k informational keywords, Dec 2023 vs Dec 2025 | AIO keywords only |
| AIO CTR effect (earlier) | 34.5% lower | Ahrefs, 2025-04 | Superseded |
| Click rate with vs without AI summary | 8% vs 15%; 1% click inside summary | Pew, 2025-07, about 900 US adults | US panel |
| Organic and paid CTR on AIO queries | 1.76% to 0.61% organic; 19.7% to 6.34% paid | Seer, 2025-11, 3,119 queries, 42 orgs | Informational queries |
| Cited vs uncited organic clicks per million impressions | About 20,743 vs 9,445 (33,500 with no AIO) | Seer, 2026, 53 brands | Secondary read; correlational |
| Paid CTR on AIO queries | 14.64% to 16.21% (2025-01 to 2026-02) | Seer, 2026 | Secondary read |
| Same brand list across repeated runs | Under 1% | SparkToro and Gumshoe, 2026, 2,961 responses | Not peer reviewed |
| Schema added vs controls (AI citations) | No significant change (AI Mode +2.4%, ChatGPT +2.2%, AIO minus 4.6%) | Ahrefs, 2026-05, 1,885 treated vs 4,000 control pages | Short window; one tool's prompt index |
| AI Overviews on branded searches | 83% | Ahrefs, 2026-09, 232.8M US desktop SERP crawls | Branded only |
| US Google zero-click rate | 68.01% (Jan to Apr 2026) vs 60.45% (2024) | SparkToro with Similarweb, 2026 | Clickstream panel |
| ChatGPT share of AI referrals | 95.1% (August 2026) | BrightEdge, 2026-09 | Vendor customer base |
| Branded mention correlation with AIO visibility | 0.664 | Ahrefs, 2025, about 75k brands | Correlational |
| Princeton GEO method effect | Up to about 40% relative visibility gain (quotations, statistics, cited sources) | Aggarwal et al., KDD 2024, GEO-bench about 10k queries | Simulated GPT-3.5 engine on top 5 Google results |
| ChatGPT free-tier sources from own index | About 75% | Resoneo via Peec AI and SEL, 2026-07 | Vendor; window ended 2026-07-21 |
| SearchGPT citations matching Bing top results | 87% | Seer, 2024 | Pre-Labrador |
| ChatGPT sources from Google and Bing for known fan-outs | About 40% | Grow and Convert, 2025 | Method specific |
| llms.txt files with zero requests | 97% of 137k domains | Ahrefs, 2026-05 | Secondary read |
| AI Overviews prevalence | 13.14% of queries (2025-03), up from 6.49% (2025-01) | Semrush, 2025, 10M+ keywords | [Unverified exact figures]; changes monthly |
| AI referral share by engine | ChatGPT 79.4%, Gemini 10.9%, Perplexity 4.3%, Copilot 2.8%, Claude 2.6% | Statcounter, 2026-08 | Secondary |

All benchmarks vary by vertical, geo, season and method. Compare a project with its own history first.

## Tools, APIs and MCP servers

| Category | Options | Notes |
|----------|---------|-------|
| First-party | Google Search Console (Generative AI report, AI control), Bing Webmaster Tools (AI Performance), GA4, server and CDN logs, Cloudflare AI Crawl Control | AI reports have no clicks; neither the Search Console Generative AI report nor Bing AI Performance has an API as of 2026-10 (UI and CSV export only) |
| Prompt tracking | Profound, Peec AI, Otterly.AI, Scrunch AI, Semrush AI Toolkit, Ahrefs Brand Radar, Similarweb, Conductor, BrightEdge, seoClarity, Yext Scout, Evertune, AthenaHQ, Goodie, Gumshoe, Yoast AI Brand Insights, LLMrefs, Rankscale | Evaluate method: engines, modes, runs, geo, raw export |
| MCP servers | Ahrefs remote MCP (official, https://api.ahrefs.com/mcp/mcp, OAuth or MCP key), Semrush MCP (official, https://mcp.semrush.com/v1/mcp, OAuth, consumes API units), DataForSEO MCP (official), Google Analytics MCP (official), Cloudflare MCP servers (official); no official Google Search Console or Bing Webmaster MCP as of 2026-10, only community servers | Verify current endpoints and scopes; read-only for analysis |
| LLM APIs for DIY tracking | OpenAI Responses API web search tool, Gemini API grounding with Google Search, Perplexity Sonar API, Anthropic web search tool, Azure Grounding with Bing Search | Proxy only: not identical to consumer products |
| Technical | curl, Screaming Frog (text vs JS rendering), log analyzers, Rich Results Test, Schema Markup Validator, Cloudflare Radar bot directory | Rendering and access verification |

## Official sources to monitor

| Source | URL | Cadence |
|--------|-----|---------|
| OpenAI crawlers | https://developers.openai.com/api/docs/bots | Monthly |
| Anthropic crawler article | https://support.claude.com/en/articles/8896518 | Monthly |
| Perplexity bots | https://docs.perplexity.ai/guides/bots | Monthly |
| Google AI features doc | https://developers.google.com/search/docs/appearance/ai-features | Monthly |
| Google crawlers (Google-Extended) | https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers | Quarterly |
| Search Console Help (Generative AI report, AI control) | https://support.google.com/webmasters/answer/16984139 and /16908024 | Monthly |
| Google Search Central blog and Search Status Dashboard | developers.google.com/search/blog; status.search.google.com | Weekly |
| Bing Webmaster blog | https://blogs.bing.com/webmaster | Monthly |
| Cloudflare blog | https://blog.cloudflare.com | Monthly |
| OpenAI help center and merchants page | help.openai.com; chatgpt.com/merchants | Monthly (with `commerce-feeds`) |
| Trade press | Search Engine Land, Search Engine Journal, Search Engine Roundtable | Weekly |

## Open questions and watch list

1. Will OpenAI publish webmaster data (citations, crawl stats) or a documented index? Any official naming of Labrador would change ChatGPT strategy.
2. Does Google add clicks, queries or AI Mode vs AI Overviews separation to the Generative AI report, or an API? (None of these as of 2026-10-08.)
3. Page-level Google AI opt-out (CMA publisher controls conduct requirement imposed 2026-06-03; nine months to implement, about 2027-03) and how it interacts with Top Stories inside AI Overviews [Unverified for Top Stories].
4. Cloudflare 2026-09-15 defaults: classification of user-fetch bots is inconsistent (ChatGPT-User is Agent in Radar, AI Assistant in AI Crawl Control docs; one community report shows Claude-User treated as an AI Crawler on a Free plan); measure the effect on live citations for ad-supported sites.
5. Google "AI Contribution" pilot paying about 100 invited publishers via Search Console (confirmed 2026-09): eligibility rules, formula and any expansion.
6. Gemini model changes in AI Mode (3.5 Flash default from 2026-05; 3.7 Flash and 3.8 Flash selectable for subscribers 2026-08 and 2026-09) and their effect on citation patterns (re-baseline after each).
7. ChatGPT's retrieval mix after 2026-07-21 when the source field stopped being exposed.
8. Claude's search provider: Brave Search is listed as a web search subprocessor (2026-09-02) but Anthropic does not describe its role; watch for changes.
9. UCP: Merchant Center integration hub US rollout pace (from 2026-10-06); Canada and Australia expected 2027.
10. ACP discovery feed requirements after the 2026-03 pivot (owned by `commerce-feeds`).
11. Whether any engine adopts llms.txt or Cloudflare Content Signals.
12. Bing AI Performance API and click data (Microsoft said API access would come during 2026; not shipped as of 2026-09).
13. Reddit citation share stability across engines; YouTube's rise.
14. Primary reads still needed: Kevin Indig Growth Memo 2026 citation studies, iPullRank 2026 relevance engineering material, Conductor 2026 benchmarks, Seer Interactive (no new CTR study found after 2026-04), and the findings of Semrush's 2026-09 YMYL mini study.

## Sources

1. (S1) Overview of OpenAI Crawlers. OpenAI. https://developers.openai.com/api/docs/bots. Living document, read 2026-10.
2. (S2) Does Anthropic crawl data from the web and how can site owners block the crawler. Anthropic. https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler. Living document, read 2026-10.
3. (S3) Perplexity crawlers. Perplexity. https://docs.perplexity.ai/guides/bots. Living document.
4. (S4) AI features and your website. Google Search Central. https://developers.google.com/search/docs/appearance/ai-features. 2025, updated 2026.
5. (S5) AI Mode in Google Search: updates from Google I/O 2025. Google. https://blog.google/products-and-platforms/products/search/google-search-ai-mode-update/. 2025-05.
6. (S6) Generative AI performance report (Search). Search Console Help. https://support.google.com/webmasters/answer/16984139. 2026-06, updated 2026-08.
7. (S7) Search generative AI control. Search Console Help. https://support.google.com/webmasters/answer/16908024. 2026-06, updated 2026-08.
8. (S8) Google common crawlers. Google Search Central. https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers. Living document.
9. (S9) Introducing AI Performance in Bing Webmaster Tools Public Preview. Microsoft Bing. https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview. 2026-02-10.
10. (S10) Content Independence Day: no AI crawl without compensation. Cloudflare. https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/. 2025-07-01.
11. (S11) Perplexity is using stealth, undeclared crawlers to evade website no-crawl directives. Cloudflare. https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/. 2025-08-04.
12. (S12) Introducing ChatGPT search. OpenAI. https://openai.com/index/introducing-chatgpt-search/. 2024-10-31.
13. (S13) llms.txt proposal. llmstxt.org. https://llmstxt.org. 2024-09.
14. (S14) IndexNow. IndexNow.org. https://www.indexnow.org. Living document.
15. (S15) GEO: Generative Engine Optimization. Aggarwal et al., KDD 2024. https://arxiv.org/abs/2311.09735. 2023-11 (KDD 2024).
16. (S16) The Princeton GEO study: methodology, results and critique. blck alpaca. https://blckalpaca.at/en/knowledge-base/seo-geo/geo-generative-engine-optimization/the-princeton-geo-study-methodology-results-and-critique.md. 2026.
17. (S17) An Analysis of AI Overview Brand Visibility Factors (75K Brands Studied). Ahrefs. https://ahrefs.com/blog/ai-overview-brand-correlation/. 2025.
18. (S18) AI Overviews Reduce Clicks by 34.5%. Ahrefs. https://ahrefs.com/blog/ai-overviews-reduce-clicks/. 2025-04.
19. (S19) AI Overviews reduce clicks: update. Ahrefs. https://ahrefs.com/blog/ai-overviews-reduce-clicks-update. 2026-02.
20. (S20) AIO Impact on Google CTR: 2026 Update. Seer Interactive. https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-2026-update. 2026.
21. (S21) Google AI Overviews drive drop in organic and paid CTR. Search Engine Land. https://searchengineland.com/google-ai-overviews-drive-drop-organic-paid-ctr-464212. 2025-11.
22. (S22) 87% of SearchGPT Citations Match Bing's Top Results. Seer Interactive. https://www.seerinteractive.com/insights/87-percent-of-searchgpt-citations-match-bings-top-results. 2024.
23. (S23) Only 40% of ChatGPT Sources Come from Google and Bing for Known Fan-Out Queries. Grow and Convert. https://www.growandconvert.com/ai/fan-out-query-serp-study/. 2025.
24. (S24) ChatGPT built its own search index. Peec AI. https://peec.ai/blog/chatgpt-built-its-own-search-index. 2026-07.
25. (S25) Inside ChatGPT's retrieval stack: the index, cache and pages it actually reads. Search Engine Land. https://searchengineland.com/chatgpt-retrieval-stack-index-cache-pages-485036. 2026.
26. (S26) OpenAI's ChatGPT using SerpApi to scrape Google search results. Search Engine Roundtable. https://www.seroundtable.com/chatgpt-serpapi-scrape-google-39989.html. 2025.
27. (S27) What search engine does ChatGPT use? No longer Bing. Falia. https://falia.co/en/insights/ai-visibility/what-search-engine-does-chatgpt-use/. 2026.
28. (S28) AI recommendations change with nearly every query: SparkToro. Search Engine Journal. https://www.searchenginejournal.com/ai-recommendations-change-with-nearly-every-query-sparktoro/566242. 2026.
29. (S29) AI Platform Citation Patterns. Profound. https://www.tryprofound.com/blog/ai-platform-citation-patterns. 2025.
30. (S30) The Data on Reddit and AI Search. Profound. https://www.tryprofound.com/blog/the-data-on-reddit-and-ai-search. 2025.
31. (S31) AI search engines cite Reddit, YouTube and LinkedIn most: study. Search Engine Land. https://searchengineland.com/ai-search-engines-cite-reddit-youtube-and-linkedin-most-study-473138. 2026.
32. (S32) The AI Citations Report 2026. OtterlyAI. https://otterly.ai/blog/the-ai-citations-report-2026/. 2026.
33. (S33) Google Gemini sends more traffic to sites than Perplexity: report. Search Engine Journal. https://www.searchenginejournal.com/google-gemini-sends-more-traffic-to-sites-than-perplexity-report/570714/. 2026.
34. (S34) ChatGPT referral traffic near triples overnight. Similarweb. https://www.similarweb.com/blog/insights/ai-news/chatgpt-referral-traffic-triples/. 2026-05.
35. (S35) AI Referral Traffic by Industry: 2026 Data. Similarweb. https://aisearch.similarweb.com/blog/ai-referral-traffic-by-industry/. 2026.
36. (S36) ChatGPT's AI referral share fell from 89% to 63%. Goodie. https://higoodie.com/blog/ai-search-traffic-report-2026/. 2026.
37. (S37) AI traffic research study. SE Ranking. https://seranking.com/blog/ai-traffic-research-study/. 2025 to 2026.
38. (S38) We serve an llms.txt: AI crawlers hit our pages 151 times in 14 days and never once asked for it. Saaslinks. https://saaslinks.net/blog/llms-txt-server-log-study. 2026.
39. (S39) llms.txt: we publish one, and no AI crawler has ever read it. Prosopo. https://prosopo.io/blog/llms-txt/. 2026.
40. (S40) The rise of the AI crawler. Vercel. https://vercel.com/blog/the-rise-of-the-ai-crawler. 2024-12.
41. (S41) Google users are less likely to click on links when an AI summary appears in the results. Pew Research Center. https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/. 2025-07-22.
42. (S42) Google Search Console AI performance reports and Search generative AI control rolling out globally. Search Engine Land. https://searchengineland.com/google-search-console-ai-performance-reports-and-search-generative-ai-control-rolling-out-globally-486269. 2026-08.
43. (S43) Google Search Console AI reports rolled out worldwide. Search Engine Journal. https://www.searchenginejournal.com/google-search-console-ai-reports-rolled-out-worldwide/587836/. 2026-08.
44. (S44) Google gives sites AI search opt-out, but not the data to use it. Search Engine Journal. https://www.searchenginejournal.com/google-gives-sites-ai-search-opt-out-but-not-the-data-to-use-it/577978/. 2026-06.
45. (S45) Google's AI opt-out leaves publishers with a difficult choice. Digiday. https://digiday.com/media/googles-ai-opt-out-leaves-publishers-with-a-choice-they-cant-safely-use/. 2026-06.
46. (S46) Google AI Overviews opt-out hits Search Console: Gemini excluded as publishers weigh trade-offs. Tech Times. https://www.techtimes.com/articles/317979/20260608/google-ai-overviews-opt-out-hits-search-console-gemini-excluded-publishers-weigh-trade-offs.htm. 2026-06-08.
47. (S47) Bing Webmaster Tools AI Performance reports go live. Search Engine Roundtable. https://www.seroundtable.com/bing-webmaster-tools-ai-performance-report-40911.html. 2026-02.
48. (S48) Bing Webmaster Tools adds AI citation performance data. Search Engine Journal. https://www.searchenginejournal.com/bing-webmaster-tools-adds-ai-citation-performance-data/566874/. 2026-02.
49. (S49) Query fan-out technique in AI Mode: new details from Google. Search Engine Journal. https://www.searchenginejournal.com/query-fan-out-technique-in-ai-mode-new-details-from-google/552532/. 2025.
50. (S50) How to optimize for query fan-out. Search Engine Land. https://searchengineland.com/guide/how-to-optimize-for-query-fan-out. 2025 to 2026.
51. (S51) Google AI Mode's query fan-out technique. Aleyda Solis. https://www.aleydasolis.com/en/ai-search/google-query-fan-out/. 2025.
52. (S52) Google confirms llms.txt has no current implementation. Search Engine Journal. https://www.searchenginejournal.com/google-says-llms-txt-is-purely-speculative-for-now/577576/. 2026.
53. (S53) Google's Mueller says llms.txt can't help LLMs differentiate sites. Search Engine Journal. https://www.searchenginejournal.com/googles-mueller-says-llms-txt-cant-help-llms-differentiate-sites/579304/. 2026.
54. (S54) Google Search team does not endorse llms.txt files. Search Engine Roundtable. https://www.seroundtable.com/google-does-not-endorse-llms-txt-40789.html. 2026.
55. (S55) Cloudflare sets deadline for mixed AI crawlers. Technology.org. https://www.technology.org/2026/07/03/cloudflare-blocks-mixed-use-ai-crawlers/. 2026-07-03.
56. (S56) Cloudflare enters the robots.txt fray with a Content Signals Policy for AI bots. Search Engine World. https://www.searchengineworld.com/cloudflare-enters-the-robots-txt-fray-with-a-content-signals-policy-for-ai-bots. 2025-09.
57. (S57) Cloudflare accuses AI startup of stealth crawling behavior across millions of sites. TechRepublic. https://www.techrepublic.com/article/news-cloudflare-accuses-perplexity-stealth-crawling-violations/. 2025-08.
58. (S58) Google announces a new protocol to facilitate commerce using AI agents. TechCrunch. https://www.techcrunch.com/2026/01/11/google-announces-a-new-protocol-to-facilitate-commerce-using-ai-agents/. 2026-01-11.
59. (S59) Google UCP: merchant guide to agentic commerce. commercetools. https://commercetools.com/blog/google-ucp-merchant-guide-to-agentic-commerce. 2026.
60. (S60) Google Merchant Center UCP integration hub: how to join. UCP Checker. https://ucpchecker.com/blog/google-merchant-center-ucp-integration-hub. 2026-10.
61. (S61) ChatGPT for ecommerce: what to do now that Instant Checkout is gone. Digital Silk. https://www.digitalsilk.com/digital-trends/digital-trends-chatgpt-ecommerce/. 2026.
62. (S62) ChatGPT Instant Checkout: ACP protocol retailer guide (2026). Ekamoira. https://www.ekamoira.com/blog/chatgpt-instant-checkout-agentic-commerce-protocol-2026. 2026-02.
63. (S63) Google AI Overviews reduce clicks by 58%, study finds. MediaNama. https://www.medianama.com/2026/02/223-google-ai-overviews-click-through-rates-58-study/. 2026-02.
64. (S64) Google AI Overviews reduce organic CTR 61%, paid traffic 68%. PPC Land. https://ppc.land/google-ai-overviews-reduce-organic-ctr-61-paid-traffic-68/. 2025.
65. (S65) Track your brand visibility in Claude with Yoast AI Brand Insights. Yoast. https://yoast.com/yoast-ai-brand-insights-28-may-2026/. 2026-05-28.
66. (S66) Google Search Console performance report gains multimodal search type filter. Search Engine Roundtable. https://www.seroundtable.com/google-search-console-multimodal-search-type-filter-42156.html. 2026.
67. (S67) Cloudflare's September 15 AI crawler wall: what agent builders need to know. fastCRW. https://fastcrw.com/blog/cloudflare-ai-crawler-block-september-2026. 2026.
68. (S68) Google Search Console generative AI performance report and AI control live. Search Engine Roundtable. https://www.seroundtable.com/google-search-console-generative-ai-tools-live-41984.html. 2026.
69. (S69) Google just released an AI opt-out feature. Your competitors hope you use it. Search Engine Land. https://searchengineland.com/google-ai-opt-out-feature-competitors-480375. 2026-06.
70. (S70) AEO and AI search citation statistics 2026. Rise at Seven. https://riseatseven.com/blog/aeo-ai-search-statistics/. 2026.
71. (S71) Similarweb 2026 generative AI landscape: what it means. Salience. https://salience.co.uk/insight/similarweb-2026-generative-ai-landscape. 2026.
72. (S72) Google UCP update 2026: cart, catalog, loyalty guide. Passionfruit. https://www.getpassionfruit.com/blog/what-is-google-s-ucp-update-carts-catalogs-and-loyalty-in-ai-shopping. 2026.
73. (S73) Google's Universal Commerce Protocol and Merchant Center. ChannelEngine. https://www.channelengine.com/en/blog/google-universal-commerce-protocol-merchant-center-ai-shopping. 2026.
74. (S74) ChatGPT built its own search index: why Bing visibility isn't a ChatGPT strategy anymore. Blumint. https://blumint.co/blog/chatgpt-search-index. 2026.
75. (S75) Cloudflare accuses Perplexity of secretly crawling sites despite explicit blocks. The Decoder. https://the-decoder.com/cloudflare-accuses-perplexity-of-secretly-crawling-sites-despite-explicit-blocks/. 2025-08.
76. (S76) Your site, your rules: new AI traffic options for all customers. Cloudflare. https://blog.cloudflare.com/content-independence-day-ai-options/. 2026-07-01.
77. (S77) Cloudflare Allows the Agentic Internet to Flourish with a Simple Philosophy: Your Content, Your Rules. Cloudflare press release. https://www.cloudflare.com/press/press-releases/2026/cloudflare-allows-the-agentic-internet-to-flourish-with-a-simple-philosophy-your-content-your-rules/. 2026-07-01.
78. (S78) Google Search Console AI Performance Reports: what they track (and the clicks problem). Crawlraven. https://crawlraven.com/blog/gsc-ai-performance-reports. 2026.
79. (S79) Claude web search explained. Profound. https://www.tryprofound.com/blog/what-is-claude-web-search-explained. 2025 to 2026.
80. (S80) Publishers and Developers FAQ. OpenAI Help Center. https://help.openai.com/en/articles/12627856-publishers-and-developers-faq. Living document.
81. (S81) How to onboard to the UCP integration hub in Merchant Center. Google Merchant Center Help. https://support.google.com/merchants/answer/16992327. 2026-10.
82. (S82) Google rolls out Merchant Center UCP integration hub in the U.S. Search Engine Land. https://searchengineland.com/google-rolls-out-merchant-center-ucp-integration-hub-in-the-u-s-493889. 2026-10.
83. (S83) Semrush Releases Expanded 2026 AI Visibility Index, Analyzing 126 Million AI Search Prompts. Business Wire via StreetInsider. https://www.streetinsider.com/Business+Wire/Semrush+Releases+Expanded+2026+AI+Visibility+Index,+Analyzing+126+Million+AI+Search+Prompts/26695555.html. 2026-06-26.
84. (S84) ChatGPT vs Google AI Mode (AI Visibility Index mini study). Semrush. https://ai-visibility-index.semrush.com/downloads/chatgpt-vs-ai-mode. 2026-08.
85. (S85) The 50 Most-Cited Websites in ChatGPT (September 2026). Ahrefs. https://ahrefs.com/blog/most-cited-domains-in-chatgpt/. 2026-09.
86. (S86) AI Overviews Currently Appear for 83% of Branded Searches. Ahrefs. https://ahrefs.com/blog/ai-overviews-on-branded-searches/. 2026-09.
87. (S87) How query language reshapes AI citations. Profound. https://www.tryprofound.com/blog/how-query-language-reshapes-ai-citations. 2026-03.
88. (S88) Study says adding schema did not improve AI citations. Search Engine Roundtable. https://www.seroundtable.com/study-schema-citations-study-41311.html. 2026-05.
89. (S89) Google confirms google.com/goto search links. Relevant Audience. https://www.relevantaudience.com/seo/google-search-goto-passthrough-urls-confirmed/. 2026-09.
90. (S90) Google tests paying publishers for using its content in AI Mode, AI Overviews and Gemini. Search Engine Land. https://searchengineland.com/google-tests-paying-publishers-for-using-its-content-in-ai-mode-ai-overviews-and-gemini-488382. 2026-09.
91. (S91) Google tests paying publishers for AI answers via Search Console. Search Engine Journal. https://www.searchenginejournal.com/google-tests-paying-publishers-for-ai-answers-via-search-console/589414/. 2026-09.
92. (S92) BrightEdge Data: ChatGPT Referral Traffic More Than Doubles in 2026, Reaching Record 95.1% Share of AI Traffic. BrightEdge via GlobeNewswire. https://www.globenewswire.com/news-release/2026/09/24/3368345/0/en/brightedge-data-chatgpt-referral-traffic-more-than-doubles-in-2026-reaching-record-95-1-share-of-ai-traffic.html. 2026-09-24.
93. (S93) In 2026, less than one third of Google searches still send a click. SparkToro. https://sparktoro.com/blog/in-2026-less-than-one-third-of-google-searches-still-send-a-click/. 2026.
94. (S94) Google brings Gemini 3.8 Flash to Search's AI Mode. ALM Corp. https://almcorp.com/news/google-brings-gemini-3-8-flash-to-ai-mode/. 2026-09-21.
95. (S95) Google Search's I/O 2026 updates. Google. https://blog.google/products-and-platforms/products/search/search-io-2026/. 2026-05-19.
96. (S96) Google makes Gemini 3 the default model for AI Overviews globally. Dataconomy. https://dataconomy.com/2026/01/28/google-makes-gemini-3-the-default-model-for-ai-overviews-globally/. 2026-01-28.
97. (S97) Bing AI dashboard maps grounding queries to cited pages. Search Engine Journal. https://searchenginejournal.com/bing-ai-dashboard-maps-grounding-queries-to-cited-pages/570323/. 2026-03.
98. (S98) Canada and Australia face 2027 wait for Google's Merchant Center UCP hub. PPC Land. https://ppc.land/canada-and-australia-face-2027-wait-for-googles-merchant-center-ucp-hub/. 2026-10.

Note on source numbering: the "Sources by module" table in `skills/ai-search-optimization/references/sources.md` uses that file's own numbering (1 to 124), which extends this list with additional secondary sources and the 2026-10-08 verification pass additions (96 to 124).
