# Research Dossier: Market and Competitive Intelligence for Growth Teams

Research date: 2026-10-08. Scope: ad transparency libraries and APIs, search and SEO competitive data, AI visibility benchmarking, offer and price monitoring, voice of customer mining, demand research, market sizing, positioning, win and loss, monitoring, tools and MCP servers, and the legal and ethical limits of collection. Companion: `research/00-market-overview-2026.md`.

Method and limitations: the live web sweep for this build ran 14 extended searches before the shared search budget was exhausted, and direct page fetches were blocked by the research environment's egress policy. Facts confirmed in live search results are marked (S). Established facts from official documentation known before this sweep are marked (K) and must be re-checked in the Freshness Protocol; tool features and API fields change frequently. Nothing here is invented; where a detail could not be confirmed it is labeled [Unverified]. A verification pass on 2026-10-08 re-checked the Meta Ad Library API access rules, Google Ads Transparency Center features, TikTok and LinkedIn libraries and the Semrush and Similarweb MCP servers (sources 61 to 69).

## 1. Executive summary
1. Ad transparency is richest in the EU. Since the Digital Services Act, very large platforms keep public ad repositories with targeting and reach information for EU delivered ads (Meta, TikTok, LinkedIn, Microsoft, Google and others) (K). Outside the EU, libraries mostly show active ads only. Competitive teams in any market can study a competitor's EU activity to infer tests, scale and targeting.
2. The Meta Ad Library remains the single most useful competitor source for paid social; its API covers EU delivered ads and political or issue ads, not non EU commercial ads (K).
3. Google's Ads Transparency Center shows competitor ads by domain and region, but no keywords or spend; Auction Insights remains the only official view of who competes in your own auctions (K).
4. Political ad data in the EU stopped growing: Meta ended political, electoral and social issue ads in the EU from 6 October 2025 and Google stopped political ads in the EU ahead of the TTPA (applied 10 October 2025) (S).
5. A new competitive arena opened: AI assistants. Zero click searches reached 68.01% of US Google searches in January to April 2026 (SparkToro), AI Overviews cut organic CTR (Pew, Seer, Ahrefs), and generative search is forecast at $5.1 billion of ad revenue in 2026 rising past $100 billion by 2030 (WPP Media) (S). Benchmarking competitor visibility in ChatGPT, Gemini, AI Overviews, AI Mode, Perplexity and Copilot is now a standard intelligence task.
6. ChatGPT ads launched in 2026 (pilot February, self serve May, more than 60 countries by October, visual ads near image generation announced 5 October 2026) (S). No public ChatGPT ad library was found in this sweep [Unverified]; competitor presence must be observed manually.
7. SEO suites and new AI visibility platforms now track AI mentions and citations, and several tools expose data to Claude through APIs and MCP servers; Semrush (2025-09) and Similarweb (2025-09-25) run official remote MCP servers that consume API units or data credits (S). Methods differ widely, so numbers are not comparable across vendors.
8. Voice of customer from reviews, communities and first-party surveys remains the highest value input for creative and positioning; review and community platforms restrict automated collection in their terms (K).
9. Search demand is fragmenting: dentsu forecasts traditional search growth of 3.4% in 2026 as AI, retail and social search compete (S). Demand research must span Google, marketplaces, social search and AI assistants.
10. Legal limits matter: platform terms, privacy law (GDPR, KVKK) for any personal data in reviews or comments, competition law on sharing sensitive information, and comparative advertising rules when intelligence turns into claims (K).

## 2. State of competitive intelligence in 2026 (with numbers)
| Indicator | Value | Source |
|-----------|-------|--------|
| US Google searches ending without a click | 68.01% (January to April 2026) vs 60.45% in 2024 | SparkToro via Search Engine Land, 2026 (S) |
| Clicks on traditional links when an AI summary is present | 8% of visits vs 15% without | Pew Research Center, published July 2025 (S) |
| Organic CTR on queries with AI Overviews | 1.76% to 0.61% in 2025 (minus 61%); 2.36% by February 2026 | Seer Interactive (S) |
| Position one CTR with AI Overview | minus 58% | Ahrefs, December 2025, 300,000 keywords (S) |
| Generative search ad revenue | $5.1B (2026), $32B (2028), over $100B (2030) | WPP Media midyear 2026 (S) |
| Search share of total ad revenue (traditional plus generative) | 21.8% in 2026 | WPP Media midyear 2026 (S) |
| Traditional search ad growth 2026 | 3.4% globally | dentsu, May 2026 (S) |
| US social ad revenue 2025 | $117.7B, larger than search ($114.2B) | IAB/PwC, April 2026 (S) |
| ChatGPT ads markets | More than 60 countries by October 2026 | OpenAI (S) |
| ChatGPT ads run rate | $1B annualized by 31 August 2026 (reported) | Secondary reports (S) [Unverified] |
| Ads in Google AI Overviews | 12 English language markets after December 2025 expansion | PPC Land, Search Engine Roundtable (S) |

What changed for intelligence teams:
- Social is now the largest US digital ad channel, so paid social libraries (Meta, TikTok) deserve as much attention as search tools.
- AI surfaces carry both organic answers and ads; competitive coverage must include them.
- EU repositories provide targeting and reach that were not public before the DSA; non EU teams can use them as a window into global competitors' testing.

### 2.1 Ad transparency landscape
| Platform | Outside EU | EU (DSA) | API | Notes |
|----------|-----------|----------|-----|-------|
| Meta | Active ads, creative, start date, platforms | Inactive ads retained about a year, reach, targeting summary, payer and beneficiary | Ad Library API (EU delivered and political or issue ads) | Most used competitor source (K) |
| Google | Ads by advertiser or domain, region, format, date; last shown; legal name and verification badge; no spend | Unverified advertisers also shown in Europe and Türkiye; impression ranges after a delay; EU political history removed around 2025-09 (S, secondary) | None for commercial ads; political BigQuery dataset only (S, secondary) | Domain search catches resellers (K); AI labels panel "How this ad was made" from 2026-07 (S) |
| TikTok | Creative Center Top Ads (curated) | Commercial Content Library with targeting and reach (EU/EEA, UK, Switzerland; no US) | Commercial Content API on application (docs updated 2026-09-01); eligibility reported as researcher focused [Contested] | Top Ads is inspiration, not a census (K) |
| LinkedIn | Ads run after 2023-06-01, kept one year after last impression | Impression ranges, impressions by country and targeting categories used for EU ads; no spend (S, LinkedIn Help) | None public | B2B critical (K) |
| Microsoft | Limited | EU ads | Unknown | Check coverage (K) |
| OpenAI (ChatGPT) | No public library found | None found | None | Manual observation only [Unverified] |

### 2.2 AI visibility measurement landscape
- Tools sample answers from assistants at scale and compute mention rates, share of voice and citations. Vendors differ on whether they query APIs or real user interfaces, on locations, and on logged in state; numbers are not comparable across vendors [Practitioner consensus].
- SEO suites added AI tracking features in 2025 to 2026 (for example Ahrefs Brand Radar and Semrush AI features) (K, scope [Unverified]).
- No assistant publishes official prompt volume data; tools that show "prompt volume" estimate it [Practitioner consensus].
- First-party signals exist for your own site: GA4 referrals from AI assistants, and some webmaster tools report AI citations (K, details [Unverified]).
- Citation patterns matter: assistants frequently cite review platforms, community threads, video and publisher lists, so competitive gaps are often in third party sources rather than on the brand's site [Practitioner consensus].

### 2.3 Voice of customer data access
| Source | Access route | Constraint |
|--------|-------------|------------|
| Own reviews | Platform exports or APIs for own profiles | Personal data handling |
| Competitor reviews | Manual reading, licensed tools | Terms of service of review platforms |
| Reddit | Manual reading; Data API under terms | Commercial API use needs an agreement (K) |
| YouTube | Data API (comments) | Quota and terms |
| TikTok, Instagram comments | Manual | Terms |
| Support, sales calls, surveys | First-party | Consent and privacy notices |

### 2.4 Legal landscape for collection
| Area | Rule of thumb | Where it bites |
|------|---------------|----------------|
| Platform terms | Most prohibit automated collection without permission | Scraping ad libraries, review sites, marketplaces |
| US computer fraud law | Narrowed for public data (Van Buren 2021; hiQ v. LinkedIn 2022) but contract claims remain (K) | Automated collection of public pages |
| Privacy law (GDPR, UK GDPR, KVKK, US states) | Personal data in public reviews is still personal data | Storing reviewer names, profiling individuals |
| Competition law | No exchange of competitively sensitive information | Price or bid sharing through intermediaries |
| Trade secrets | No soliciting confidential information | Former employees, agencies, partners |
| Comparative advertising and trademarks | Allowed under conditions; platform policies restrict trademark use in ad text | Turning intelligence into claims |

## 3. Timeline of changes, January 2025 to October 2026
| Date | Change | Impact on market intelligence | Status |
|------|--------|-------------------------------|--------|
| 2025-03 | Google announces AI Mode (Labs) | New AI answer surface to benchmark | K |
| 2025-05 | Google brings AI Mode to all US users; ads in AI Mode tests announced | Paid and organic AI surface monitoring | K |
| 2025-06 | Magna: digital pure players about 73% of global ad revenue | Context for where competitors spend | S |
| 2025-07 | Pew study on AI summaries and clicks | Evidence for zero click effects | S |
| 2025-07-24 | Google Trends API alpha announced at Search Central Live; still alpha with tester applications as of 2026-08 | Consistent scaled trend data for approved users | S |
| 2025-07-25 | Meta announces end of EU political, electoral and social issue ads | EU political ad library data stops growing | S |
| 2025-09 (about 09-28) | Google stops EU political ads and removes EU political ad history from the Transparency Center and its BigQuery dataset | Historic EU political research needs other archives | S [secondary] |
| 2025-09 | Semrush adds MCP support (2025-09-10) and Similarweb launches its MCP server (2025-09-25) | Claude can query both directly | S |
| 2025-10-06 | Meta EU political and issue ads end | Same | S |
| 2025-10-10 | EU TTPA applies | Political ad transparency regime | S |
| 2025-12 | Ahrefs: AI Overviews cut position one CTR 58% | SEO competition context | S |
| 2025-12-08 | European Commission announces Meta less personalized ads choice from January 2026 | EU targeting changes visible in campaigns | S |
| 2025-12-19 | Ads in AI Overviews expand to 12 English markets | Competitor ads inside AI answers | S |
| 2026-01-22 | TikTok US joint venture closes | TikTok stays a US competitive channel | S |
| 2026-02 | Seer: AI Overview CTR partially recovers | Measurement nuance | S |
| 2026-02-09 | ChatGPT ads pilot begins in the US | New competitor ad surface without a public library | S |
| 2026-04 | IAB/PwC: social $117.7B passes search $114.2B in the US | Shift attention to social libraries | S |
| 2026-05-05 | ChatGPT Ads Manager self serve beta with CPC bidding | Smaller competitors can now advertise in ChatGPT | S |
| 2026-05-20 | Google Marketing Live: new AI Mode ad formats (US first) | Competitor presence in AI Mode to monitor | S [secondary] |
| 2026-05-27 | dentsu: search growth 3.4% in 2026 | Search fragmentation | S |
| 2026-06 | WPP Media: generative search forecasts | Size of AI search ad market | S |
| 2026 (first half) | SparkToro: 68.01% zero click | Organic competition context | S |
| 2026-07 | Google "How this ad was made" panel discloses generative AI use in ads (My Ad Center on Search, YouTube, Discover) | AI creative becomes visible in competitor research | S |
| 2026-08-24 | ChatGPT ads in 31 European countries | EU competitor monitoring in ChatGPT | S [secondary] |
| 2026-08-31 | ChatGPT self serve opens in Europe, India and MENA | Same | S [secondary] |
| 2026-09-01 | TikTok updates Commercial Content API documentation | Check field changes before building pulls | S |
| 2026-10-05 | OpenAI visual ads next to image generation (US test) | New format to observe | S |

## 4. Best practice consensus
1. Start every research task from the decision it serves and the owner who will act [Practitioner consensus].
2. Prefer official and first-party signals (Auction Insights, ad libraries, Search Console, Merchant Center benchmarks) over third party estimates (K).
3. Triangulate estimates and label confidence; third party traffic and spend data are directional [Practitioner consensus].
4. Mine angles, not executions: copying a competitor's ad copies their positioning [Practitioner consensus].
5. Use longevity and variant counts as signals of scaled winners, with EU reach data where available [Practitioner consensus].
6. Keep VoC verbatim, sourced and anonymized; count themes before concluding [Practitioner consensus].
7. Sample AI assistant answers repeatedly across engines with a stable prompt set; track mention, recommendation and citation share [Practitioner consensus].
8. Track share of search monthly as a leading indicator of market share (Binet, IPA EffWorks 2020) (K).
9. Monitor with thresholds tuned to action, not to volume [Practitioner consensus].
10. Stay inside platform terms and privacy law; use official APIs or licensed tools for automation (K).

## 5. Contested topics
| Topic | View A | View B | Working position |
|-------|--------|--------|------------------|
| Ad longevity as a profit signal | Long running ads must be profitable or they would be cut | Big brands leave ads running for brand reasons or neglect; automation keeps old ads alive | Treat as medium confidence; combine with variants and EU reach |
| Third party traffic and keyword estimates | Good enough for planning | Large errors for small sites and some markets | Use for relative comparison within one tool; label confidence |
| AI visibility metrics | Share of voice in AI answers predicts consideration | Answers vary by run, account and location; no official prompt volumes | Stable prompt sets, repeated sampling, report sample sizes; avoid cross vendor comparisons |
| Automated collection of public data | Public data is fair to collect (some US case law) | Terms of service, contract claims and privacy law still apply | Official APIs and licensed tools; manual sampling otherwise; counsel for anything else |
| Competitive response to promotions | Match quickly to protect share | Matching trains customers to wait and erodes margin | Decide with unit economics; prefer non price counters first |
| Copying competitor positioning in AI era | Being "like the leader" helps AI associate you with the category | Differentiation is what earns recommendations | Own a specific use case or segment where sources can support you |

## 6. What top operators do differently
1. They maintain four competitor lists (direct, search, AI, alternatives) and review them quarterly.
2. They run a monthly movement summary that leads with changes and assigns each change an owner.
3. They use EU ad repository data to study global competitors' tests, even when they do not sell in the EU.
4. They keep a living language bank of customer phrases and refresh it every quarter.
5. They benchmark AI visibility with citation source analysis, then work the sources (reviews, communities, publishers) rather than only their own pages.
6. They run win and loss interviews with a neutral interviewer and compare with CRM loss reasons.
7. They log competitor promotions for a full year to plan peaks.
8. They measure insight adoption, pruning research that nobody uses.
9. They document collection methods for legal review.
10. They feed intelligence directly into experiments, not just slide decks.

## 6b. Intelligence to action map
| Insight type | Owner agent | Typical test |
|--------------|-------------|--------------|
| Unused angle with strong VoC support | creative-strategy | New concept vs current best concept |
| Competitor scaled concept (long running, many variants) | creative-strategy | Our version of the angle with our proof |
| New auction entrant on core terms | google-ads | Bid and copy adjustments; offer test |
| Brand bidding | google-ads | Brand defense impression share; trademark complaint |
| Price undercut on hero SKUs | growth-orchestrator, cro | Value framing or bundle test before price change |
| AI assistants cite review platforms where we are weak | ai-search-optimization, growth-orchestrator | Review program; re-measure in 60 days |
| Competitor ads in ChatGPT on our prompts | chatgpt-ads | Paid presence test with holdout |
| Rising demand cluster | seo, google-ads | New landing page and keyword cluster |
| New segment signals in reviews | growth-orchestrator | Segment landing page and creative test |

## 6c. Regional notes for intelligence work
- **EU:** use DSA repositories for reach and targeting; remember political and issue ads disappeared from Meta and Google in the EU from October 2025, so issue adjacent competitors may have shifted to other channels.
- **Turkey:** marketplaces (Trendyol, Hepsiburada, Amazon.com.tr) hold product reviews and Q and A that reveal objections; Şikayetvar captures service complaints; search queries often include "şikayet" (complaint) and "yorum" (review). Turkish keyword research must cover diacritic and non diacritic spellings (K).
- **MENA and GCC:** Snapchat and TikTok are major competitor channels; review platforms differ (Noon, Amazon.sa and .ae); Arabic and English VoC must be coded separately (K).
- **US:** first market for new ad surfaces (ChatGPT ads, AI Mode formats, visual ads) where competitors test first (S).

## 7. Common expensive mistakes
| Mistake | Cost | Prevention |
|---------|------|-----------|
| Copying a competitor's winning ad | Weak differentiation, possible IP issues | Angle extraction and gap analysis |
| Trusting one tool's traffic or spend estimate | Wrong budget or market decisions | Triangulation and confidence labels |
| Reading Top Ads as a census | False picture of competitors | Use libraries for census, Top Ads for inspiration |
| One run per AI prompt | Noise read as trend | Repeated sampling |
| Paraphrased VoC | Generic copy | Verbatims with sources |
| Scraping behind logins or against terms | Legal risk, account bans | Official APIs, licensed tools, manual review |
| Storing reviewer names and handles | Privacy violations | Anonymize and minimize |
| Reacting to every competitor promo with discounts | Margin erosion | Unit economics check, non price counters |
| Ignoring marketplaces and AI answers as competitive arenas | Missed demand | Search and AI lists of competitors |
| Comparative claims without review | Legal and policy exposure | Approval flow and BRAND.md |

## 7b. Priorities by business model
| Model | Highest value intelligence | Main sources |
|-------|----------------------------|--------------|
| Ecommerce | Offer and price corridor, promo calendar, scaled creative concepts, Shopping price competitiveness, marketplace reviews | Meta Ad Library, Transparency Center, Merchant Center, marketplaces, review mining |
| Lead gen | Auction entrants and brand bidding, offer and guarantee comparisons, local review standing | Auction Insights, SERP sampling, Google Business Profiles |
| B2B SaaS | Win and loss, G2 and Capterra review themes, pricing page changes, AI assistant recommendations, LinkedIn ad themes | Interviews, review platforms, page monitors, AI benchmark, LinkedIn Ad Library |
| Local services | Map pack competitors, review velocity, offers | Google Maps, review sites |
| App | Store page messaging, review themes, Apple Ads competitor presence, TikTok creative norms | App stores, Creative Center |
| Marketplace or publisher | Supply and demand side alternatives, traffic sources, SEO footprint | SEO suites, Similarweb, communities |

## 7c. Metric glossary
| Metric | Definition |
|--------|-----------|
| Overlap rate | Share of our auctions where a competitor also showed (Google Ads Auction Insights) |
| Position above rate | Share of shared auctions where the competitor's ad ranked above ours |
| Outranking share | Share of auctions where we ranked higher or showed when they did not |
| Share of search | Brand's branded search volume divided by the total branded volume of the category set |
| Mention rate (AI) | Share of sampled AI answers that mention the brand |
| Recommendation rate (AI) | Share of sampled AI answers that recommend the brand |
| Citation share (AI) | Share of answers with citations that cite the brand's domain |
| Price index | Our effective price divided by the median competitor effective price, times 100 |
| Ad longevity | Days between an ad's delivery start and stop (or today) |

## 8. Benchmarks and rules of thumb (priors only; vary by vertical, geo and season)
| Item | Value | Source and date | Caveat |
|------|-------|-----------------|--------|
| Zero click share of US Google searches | 68.01% (Jan to Apr 2026) | SparkToro, 2026 (S) | Clickstream panel; US |
| Link clicks with AI summary present | 8% vs 15% | Pew, 2025 (S) | March 2025 data, 900 US adults |
| Organic CTR on AIO queries | 0.61% (2025) to 2.36% (Feb 2026) | Seer, 2025 to 2026 (S) | Informational queries |
| Position one CTR effect of AIO | minus 58% | Ahrefs, 2025-12 (S) | Query mix |
| VoC sample per segment | 100 to 200+ coded verbatims from 3+ sources | Practitioner consensus | Smaller niches need fewer |
| Win and loss interviews | 10 to 20 per quarter | Practitioner consensus | B2B |
| AI visibility runs per prompt | 3 or more per engine per period | Practitioner consensus | More for volatile categories |
| Ad longevity threshold for "likely winner" | 30 to 90+ days with multiple variants | Practitioner consensus | Signal, not proof |
| Small site traffic estimate reliability | Low below roughly 50k visits per month | Practitioner consensus | Tool dependent |
| Survey purchase intent haircut | 30% to 50% | Practitioner consensus | Category dependent |

## 9. Tools, APIs and MCP servers
| Category | Tools | Access | Status |
|----------|-------|--------|--------|
| Ad libraries | Meta Ad Library and API, Google Ads Transparency Center, TikTok Creative Center and Ad Library (Commercial Content API for researchers), LinkedIn Ad Library, Microsoft Ad Library, other DSA repositories | Public; API access requirements vary | K |
| Auction and own data | Google Ads and Microsoft Ads Auction Insights, Search Console, Merchant Center price competitiveness and market insights | Account access | K |
| SEO suites | Semrush, Ahrefs, Similarweb, SpyFu, DataForSEO | Subscriptions, APIs | K |
| AI visibility | Profound, Peec AI, Otterly.AI, Scrunch, Evertune, Semrush AI features, Ahrefs Brand Radar; manual panels | Subscriptions | K [Unverified features] |
| Demand | Google Trends (API alpha), Keyword Planner (Google Ads API), Pinterest Trends, TikTok Creative Center, Amazon Brand Analytics | Mixed | K |
| VoC | Review platforms (G2, Capterra, TrustRadius, Trustpilot, app stores, marketplaces), Reddit (Data API terms), YouTube Data API, listening tools (Brandwatch, Talkwalker, Meltwater, Brand24) | Mixed | K |
| Price and page monitoring | Prisync, Price2Spy, Competera, Keepa, Visualping, Distill, Wayback Machine CDX | Mixed | K |
| MCP servers | Ahrefs MCP, DataForSEO MCP, Apify MCP, Firecrawl MCP, Bright Data MCP, Playwright MCP, community Search Console MCP, Google Ads MCP (own accounts); official remote Semrush MCP (mcp.semrush.com/v2/mcp) and Similarweb MCP (mcp.similarweb.com) | Self hosted or vendor | K; Semrush and Similarweb S |
Usage rules: read only, official or licensed sources, human approved keys, provenance logged per number.

## 10. Official sources to monitor
| Source | What to watch | Cadence |
|--------|---------------|---------|
| Meta Ad Library and API docs, Meta Transparency Center | Coverage, fields, access rules | Quarterly |
| Google Ads Transparency Center and Google Ads Help (Auction Insights, trademarks) | Filters, EU details, policy | Quarterly |
| TikTok Creative Center, TikTok Ad Library, TikTok research API pages | Metrics and coverage | Quarterly |
| LinkedIn Ad Library, Microsoft Ad Library | Coverage and fields | Quarterly |
| OpenAI ads announcements and help center | Ad surfaces and markets (for competitor observation) | Monthly |
| Google Search Central and Ads blogs | AI Overviews and AI Mode changes | Monthly |
| SEO tool changelogs (Semrush, Ahrefs, Similarweb) | Data and AI feature changes | Monthly |
| EU DSA and DMA pages, EUR-Lex | Repository and targeting rules | Quarterly |
| Privacy regulators (EDPB, ICO, KVKK) | Scraping and personal data guidance | Quarterly |

## 11. Open questions and watch list
- Will OpenAI publish an ad library or transparency tool for ChatGPT ads, especially in the EU under the DSA?
- How will Google report and expose ads in AI Mode for transparency outside the US?
- Will AI visibility vendors converge on comparable methods (sampling, locations, logged in vs logged out)?
- Will official prompt volume data appear from any assistant?
- How will the EU repositories change if platforms reduce personalization (Meta less personalized ads)?
- Legal developments on automated collection of public data in the US and EU.

## 12. Sources
1. This Year Next Year 2026 Midyear Forecast. WPP Media. https://www.wppmedia.com/news/report-this-year-next-year-midyear-2026 (2026-06) (S)
2. Ad Spend Growth Is Projected to Slow to 5.0% in 2026. dentsu. https://www.dentsu.com/news-releases/ad-spend-growth-is-projected-to-slow-to-5-percent-in-2026-still-outpacing-economic-growth (2026-05-27) (S)
3. IAB/PwC Internet Advertising Revenue Report: Full Year 2025. IAB. https://www.iab.com/insights/internet-advertising-revenue-report-full-year-2025/ (2026-04) (S)
4. IAB Raises 2026 U.S. Ad Spend Forecast to +12.3%. IAB. https://www.iab.com/news/iab-raises-2026-u-s-ad-spend-forecast/ (2026-09) (S)
5. Magna latest to downgrade global ad spending forecast, expects $979B. Marketing Dive. https://www.marketingdive.com/news/magna-latest-to-downgrade-global-ad-spending-forecast-expects-979b/750871/ (2025-06) (S)
6. Google zero-click searches reach 68% in early 2026. Search Engine Land. https://searchengineland.com/google-zero-click-searches-2026-study-479717 (2026) (S)
7. Pew Research confirms Google AI Overviews is eroding web ecosystem. Search Engine Journal. https://www.searchenginejournal.com/pew-research-confirms-google-ai-overviews-is-eroding-web-ecosystem/551825/ (2025-07) (S)
8. Google AI Overview Study: SEO and PPC CTR impact. Seer Interactive. https://www.seerinteractive.com/insights/ctr-aio (2025 to 2026) (S)
9. New data: Google AI Overviews are hurting click-through rates. Search Engine Land. https://searchengineland.com/google-ai-overviews-hurt-click-through-rates-454428 (2025) (S)
10. AI Overviews Cut CTR by 23.1% in France. Ahrefs. https://ahrefs.com/blog/ai-overviews-france-impact/ (2026) (S)
11. Investigating Click Behaviors On Google Search Result Pages That Produce an AI Overview. arXiv. https://arxiv.org/pdf/2608.04831 (2026-08) (S, abstract not read)
12. Google quietly expands AI Overview ads to 11 countries. PPC Land. https://ppc.land/google-quietly-expands-ai-overview-ads-to-11-countries-without-fanfare/ (2025-12) (S)
13. Google Expands Ads In AI Overviews To More Countries. Search Engine Roundtable. https://www.seroundtable.com/google-expands-ads-in-ai-overviews-40629.html (2025-12) (S)
14. AI Mode is now available in more languages and locations. Google. https://blog.google/products-and-platforms/products/search/ai-mode-expands-languages-locations/ (2025) (S)
15. Google AI Mode ads: what changed at Marketing Live 2026. Yellowhead. https://www.yellowhead.com/blog/google-ai-mode-ads/ (2026-05) (S)
16. Building advertising for the way people use AI. OpenAI. https://openai.com/index/new-chatgpt-ads-format-and-measurement/ (2026) (S)
17. ChatGPT Ads expands to Southeast Asia and Taiwan. OpenAI. https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/ (2026) (S)
18. OpenAI Opens Ad Platform To CPC Bidding, Self-Serve Buys. MediaPost. https://www.mediapost.com/publications/article/414857/openai-opens-ad-platform-to-cpc-bidding-self-serv.html (2026-05-06) (S)
19. OpenAI launches visual ads alongside image generation results. TechCrunch. https://techcrunch.com/2026/10/05/openai-launches-visual-ads-that-appear-alongside-image-generation-results/ (2026-10-05) (S)
20. Where ChatGPT Ads Are Sold: Every Market, Every Date. Digital Applied. https://www.digitalapplied.com/blog/where-chatgpt-ads-are-sold-every-market-and-date (2026) (S)
21. Ending political, electoral and social issue advertising in the EU. Meta. https://about.fb.com/news/2025/07/ending-political-electoral-and-social-issue-advertising-in-the-eu/ (2025-07) (S)
22. Meta to stop selling political ads in the EU from October. TechCrunch. https://techcrunch.com/2025/07/25/meta-to-stop-selling-political-ads-in-the-eu-from-october (2025-07-25) (S)
23. Google to stop showing political ads to users in the European Union. Giga Law. https://giga.law/daily-news/2024/11/15/google-to-stop-showing-political-ads-to-users-in-european-union (2024-11-15) (S)
24. Meta commits to give EU users choice on personalised ads under DMA. EU Reporter. https://www.eureporter.co/business/digital-economy/2025/12/09/meta-commits-to-give-eu-users-choice-on-personalised-ads-under-dma/ (2025-12-09) (S)
25. The deal to secure TikTok's future in the US has finally closed. CNN. https://www.cnn.com/2026/01/22/tech/tiktok-us-deal-closes (2026-01-22) (S)
26. Meta Reports Second Quarter 2026 Results. Meta. https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx (2026-07-29) (S)
27. How Meta's AI push is changing ad creation. Marketing Brew. https://www.marketingbrew.com/stories/2026/04/07/meta-ai-ad-creation (2026-04-07) (S)
28. Meta Ad Library. Meta. https://www.facebook.com/ads/library/ (ongoing) (K)
29. Meta Ad Library API. Meta. https://www.facebook.com/ads/library/api/ (ongoing) (K)
30. Meta Ad Library Report. Meta. https://www.facebook.com/ads/library/report/ (ongoing) (K)
31. Meta Transparency Center. Meta. https://transparency.meta.com/ (ongoing) (K)
32. Google Ads Transparency Center. Google. https://adstransparency.google.com/ (launched 2023, ongoing) (K)
33. TikTok Creative Center. TikTok. https://ads.tiktok.com/business/creativecenter/ (ongoing) (K)
34. TikTok Ad Library. TikTok. https://library.tiktok.com/ (ongoing) (K)
35. LinkedIn Ad Library. LinkedIn. https://www.linkedin.com/ad-library/ (ongoing) (K)
36. Microsoft Ad Library. Microsoft. https://adlibrary.ads.microsoft.com/ (ongoing) (K)
37. Regulation (EU) 2022/2065 (Digital Services Act). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2022/2065/oj (2022-10) (K)
38. Regulation (EU) 2024/900 (political advertising). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2024/900/oj (2024-03) (K)
39. Directive 2006/114/EC (misleading and comparative advertising). EUR-Lex. https://eur-lex.europa.eu/eli/dir/2006/114/oj (2006) (K)
40. Google Trends. Google. https://trends.google.com/ (ongoing) (K)
41. Google Ads API documentation. Google. https://developers.google.com/google-ads/api/docs/start (ongoing) (K)
42. Semrush. https://www.semrush.com/ (ongoing) (K)
43. Ahrefs. https://ahrefs.com/ (ongoing) (K)
44. Similarweb. https://www.similarweb.com/ (ongoing) (K)
45. SpyFu. https://www.spyfu.com/ (ongoing) (K)
46. DataForSEO. https://dataforseo.com/ (ongoing) (K)
47. Reddit Data API Terms. Reddit. https://redditinc.com/policies/data-api-terms (ongoing) (K)
48. YouTube Data API. Google. https://developers.google.com/youtube/v3 (ongoing) (K)
49. Trustpilot developer documentation. Trustpilot. https://developers.trustpilot.com/ (ongoing) (K)
50. hiQ Labs v. LinkedIn (case summary). Wikipedia. https://en.wikipedia.org/wiki/HiQ_Labs_v._LinkedIn (2022) (K)
51. Playwright MCP. Microsoft. https://github.com/microsoft/playwright-mcp (ongoing) (K)
52. Internet Archive Wayback Machine. https://web.archive.org/ (ongoing) (K)
53. KVKK. Personal Data Protection Authority (Turkey). https://www.kvkk.gov.tr/ (ongoing) (K)
54. Obviously Awesome. April Dunford. https://www.aprildunford.com/ (2019) (K)
55. TikTok pitches advertisers on bold new chapter under US joint venture. Marketing Dive. https://www.marketingdive.com/news/tiktok-pitches-advertisers-on-bold-new-chapter-under-us-joint-venture/815632/ (2026-03) (S)
56. Global Midyear Ad Forecast 2026. WPP Media. https://www.wppmedia.com/thought-leadership/this-year-next-year/midyear-2026 (2026-06) (S)
57. IAB 2026 Outlook. IAB. https://www.iab.com/insights/2026-outlook/ (2026-01) (S)
58. Sikayetvar. https://www.sikayetvar.com/ (ongoing) (K)
59. Pinterest Trends. Pinterest. https://trends.pinterest.com/ (ongoing) (K)
60. Apify. https://apify.com/ (ongoing) (K)
61. LinkedIn's Ad Library. LinkedIn Help. https://www.linkedin.com/help/linkedin/answer/a1517918 (checked 2026-10) (S)
62. Getting Started, Commercial Content API. TikTok for Developers. https://developers.tiktok.com/docs/en/commercial-content-api-getting-started (2026-09) (S)
63. Meta Ad Library API. Meta. https://www.facebook.com/ads/library/api (checked 2026-10) (S)
64. Meta Ad Library API: Access, Limits and Example Requests (2026). Swipekit. https://swipekit.app/articles/meta-ad-library-api (2026) (S)
65. Google Ads Transparency Center: Official Access and Research Guide. AdMapix. https://www.admapix.com/blog/ad-intelligence/google-ads-transparency-center-guide (2026) (S)
66. Google introduces new AI labels for Ads. Google. https://blog.google/products/ads-commerce/google-ads-ai-transparency-labels/ (2026-07) (S)
67. Semrush MCP. Semrush Developer. https://developer.semrush.com/api/v4/introduction/semrush-mcp/ (2026) (S)
68. Announcing Similarweb MCP Server. Similarweb. https://www.similarweb.com/blog/updates/announcements/mcp-server-launch/ (2025-09-25) (S)
69. Similarweb MCP Server. Similarweb Developers. https://developers.similarweb.com/docs/similarweb-mcp (2026) (S)
70. Google opens alpha testing for new Trends API targeting developers and journalists. PPC Land. https://ppc.land/google-opens-alpha-testing-for-new-trends-api-targeting-developers-and-journalists/ (2025-07) (S)
71. Feature Request and Inquiry: Public Availability of Auction Insights Metrics via Google Ads API. Google Ads API Forum. https://groups.google.com/g/adwords-api/c/30s21wGZkOU (2025) (S)
