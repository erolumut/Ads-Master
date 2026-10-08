# Market Research Dossier: ChatGPT Ads and AI Assistant Ad Surfaces

> Slug: chatgpt-ads. Compiled 2026-10-08. Scope: OpenAI ChatGPT Ads as the primary platform, plus Google ads in AI Overviews and AI Mode, Microsoft Copilot ads, Amazon Alexa for Shopping (formerly Rufus) sponsored prompts, Perplexity, Meta AI, Gemini, Grok, Claude and AI ad networks. Evidence labels: [Official, YYYY-MM], [Study, YYYY-MM], [Practitioner consensus], [Contested], [Unverified].

## Research method and limitations
- Web search: 13 extended searches were run before the shared web search budget for the session was exhausted. The brief asked for 35+; the gap was covered by direct reading of primary sources rather than more search snippets.
- Primary sources: openai.com, help.openai.com and developers.openai.com did not resolve from the research environment. Official OpenAI pages were therefore read through dated GitHub mirrors and captures (help center and developer docs mirrors; a September 2026 research corpus with raw captures of 40+ OpenAI, Google, Microsoft, Amazon and press pages), search engine excerpts of the official pages, and OpenAI's own GitHub (openai/plugins). Capture dates are 2026-09-22 to 2026-09-24 unless noted.
- October 2026 items (visual ads, measurement partners, Negative Phrases) were read via secondary summaries and aggregator entries (TechCrunch, The Verge, The Decoder headlines; a news site summary of the OpenAI posts). They are labeled [Official] because the OpenAI posts exist, but details need live verification.
- About 60 pages were fetched and read in full (official captures, vendor studies, partner press releases, developer docs, community API notes and code).
- Every claim not on an OpenAI or platform page is labeled [Unverified] or [Study]. Vendor panels are labeled [Study] with their method limits.

## 1. Executive summary
1. ChatGPT Ads went from announcement (2026-01-16) to a US test (2026-02-09), self-serve Ads Manager with CPC (2026-05-05), conversion optimized bidding (mid 2026), 31 European markets (2026-08), a $1B annualized run rate with tens of thousands of advertisers (2026-08-31) and 60+ countries (late 2026-09) in under nine months [Official, 2026-08] and [Unverified] (country count).
2. Only Free and Go plan users see ads (not Plus, Pro, Business, Enterprise, Edu, under 18s, Temporary Chat or the Atlas browser), and never near health, mental health, politics or other sensitive conversations [Official, 2026-09]. The reachable audience skews to free tier and low price users.
3. Targeting is contextual plus optional personalization: the current conversation, the ad and landing page, advertiser "context hints" at the ad group level, geo, platform and custom audiences; past chats and memory only with personalization on and never in the EEA or Switzerland [Official, 2026-09]. There are no keywords and no query reports.
4. Buying model: Views (CPM), Clicks (CPC), Conversions (oCPC click billing, oCPM for eligible advertisers), Manual max bid or Maximize results, in a relevance weighted second price auction. OpenAI recommends starting CPC bids at $3 to $5 and says it has no cross advertiser benchmarks yet [Official, 2026-09].
5. Pricing fell fast: about $60 CPM with $200k to $250k commitments at launch, $25 to $45 CPMs and a $50k minimum by April, then self-serve from a $25 per day minimum in May [Unverified] (launch and April) and [Official, 2026-09] (minimum daily budget).
6. Measurement is now credible on paper: OpenAI pixel plus Conversions API, the `oppref` click reference, event ID dedup, 7, 14 or 30 day click windows, an optional 1-day view-through for reporting, MMPs and 20+ measurement partners including geo incrementality vendors (October 2026) [Official, 2026-10]. In the pilot, agencies could not prove ROI [Unverified].
7. Public performance evidence is split. OpenAI and partners cite a 3x ROAS case, a CPA 15.3% below blended paid search, a geo lift showing 2.3x more incremental orders than last click, and 80%+ new customers [Official, 2026-10]. Independent panels show CTR around 0.5% to 1.3%, and small advertisers self report clicks without conversions [Study, 2026-08] and [Unverified].
8. Ads do not buy answers: OpenAI says ads never influence responses, and advertiser domains were cited in only 3.63% of ad placements in a 50,006 prompt study [Official, 2026-01] and [Study, 2026-08]. Paid and organic AI visibility are separate workstreams that should share one intent map.
9. Formats are multiplying: chat cards, product feed ads and carousels, Sponsored Agents (test), hotel ads (limited beta), AI text customization, and visual ads during image generation (US test from late October 2026) [Official, 2026-10].
10. Across other AI surfaces, the cheapest reach comes through campaigns advertisers already run: Google ads in AI Overviews and AI Mode via Search, Shopping, PMax and AI Max; Microsoft Copilot via PMax, Shopping and logo enabled Search; Amazon prompts via Sponsored Products and Brands. Perplexity exited ads, Gemini and Claude have none [Official, 2026-09] and [Unverified] (Perplexity).

## 2. State of the channel in 2026 (numbers)

| Metric | Value | Date | Label |
|--------|-------|------|-------|
| Annualized revenue run rate | $1B in under 200 days | 2026-08-31 | [Official, 2026-08] |
| Earlier run rate | $100M within about six weeks; 600+ advertisers | 2026-03-26 | [Unverified] |
| Advertisers | Tens of thousands | 2026-08-31 | [Official, 2026-08] |
| Panel advertiser counts | 7,378 distinct in one July week (Adthena); 1,159 in a 50k prompt sample (SE Ranking); about 1,200 US mobile in August (Sensor Tower) | 2026-07 to 2026-09 | [Study] and [Unverified] |
| Partners | 50+ technology and measurement partners | 2026-08-31 | [Official, 2026-08] |
| Countries | 56 listed self-serve on 2026-09-22; Southeast Asia and Taiwan added late September; 60+ reported | 2026-09 | [Official, 2026-09] and [Unverified] |
| Weekly users | 1B+ (August), 1.2B weekly people (October) | 2026 | [Official, 2026-10] |
| Ad presence | 0.8% of prompts (Feb), 14% (May) and 26% (June) of US desktop chats, 25.94% of US commercial prompts (July) | 2026 | [Study] |
| CTR | 0.50% (Similarweb panel), 1.30% (SE Ranking test), 0.91% (one Adthena client) | 2026 | [Study] and [Unverified] |
| Recommended CPC bid | $3 to $5 (US) | 2026 | [Official, 2026-09] |
| Minimum daily budget | $25, EUR 15, GBP 15 (22 currencies listed) | 2026-09 | [Official, 2026-09] |
| Bidding mix | CPC and outcome optimized bidding are the majority of campaigns | 2026-08-31 | [Official, 2026-08] |
| Carousel share | About 23% of US desktop ads (2026-08-15 to 08-30) | 2026-09 | [Unverified] |
| Financial services share | 2% to 13% of ads, April to August | 2026-09 | [Unverified] |
| Reported revenue targets | $2.5B in 2026; over $100B by 2030 | 2026-08 | [Unverified] |

## 3. Timeline of changes, January 2025 to October 2026

| Date | Platform | Change | Label |
|------|----------|--------|-------|
| 2025-05 | Google | Ads in AI Overviews expanded to desktop (US) and more countries announced; ads in AI Mode testing announced at Google Marketing Live 2025 | [Unverified] |
| 2025-07 to 2025-08 | xAI | FT reports X plans ads in Grok answers (2025-08-07) | [Unverified] |
| 2025-08 | OpenAI | ChatGPT Go launched (India first), 171 countries by January 2026 | [Official, 2026-01] |
| 2025-09 | Google | Ads in AI Mode introduced (Think Week) | [Unverified] |
| 2025-09-29 | OpenAI | Instant Checkout and Agentic Commerce Protocol with Stripe | [Official, 2025-09] |
| 2025-10 | Meta | Announces AI chat interactions will personalize ads from 2025-12-16 (not EU, UK, South Korea) | [Unverified] |
| 2025-10-30 | Google | Says it is testing ads in AI Mode before expanding | [Unverified] |
| 2025-11-24 | Google | First within-AIO ads detected by a vendor at 0.052% frequency | [Study, 2026-04] |
| 2025-12-08 | Google | VP: "There are no ads in the Gemini app and there are no current plans to change that" | [Official, 2025-12] |
| 2025-12-19 | Google | AI Overview ads expanded to 11 more countries | [Unverified] |
| 2026-01-08 | Microsoft | Copilot Checkout (US) and Brand Agents; no commission | [Official, 2026-01] |
| 2026-01-11 | Google | Universal Commerce Protocol, Business Agent, Direct Offers pilot | [Official, 2026-01] |
| 2026-01-16 | OpenAI | Ads approach announced; Go at $8 in US and worldwide | [Official, 2026-01] |
| 2026-02-04 | Anthropic | Claude will remain ad free | [Official, 2026-02] |
| 2026-02-09 | OpenAI | US ads test begins for logged-in adult Free and Go users | [Official, 2026-02] |
| 2026-02 | OpenAI | Pilot pricing about $60 CPM, $200k to $250k commitments; agency partners WPP, Omnicom, Dentsu | [Unverified] |
| 2026-02-11 | Google | Shopping ads in AI Mode announced | [Study, 2026-04] (relay) |
| 2026-02-17 | Perplexity | FT: no plans to pursue advertising after phasing out ads in 2025 | [Unverified] |
| 2026-03-02 | OpenAI, Criteo | Criteo first ad tech partner integrated | [Official, 2026-05] (Criteo) |
| 2026-03 | OpenAI | Ad Policies v1.0 | [Official, 2026-09] |
| 2026-03 | OpenAI | Instant Checkout removed for Shopify and other merchants; merchant checkout and ACP discovery focus | [Unverified] |
| 2026-03-25 | Amazon | Sponsored Products and Brands prompts generally available in the US (CPC) | [Official, 2026-03] |
| 2026-03-26 | OpenAI | Pilot next phase; CA, AU, NZ pilots; no impact on trust metrics | [Official, 2026-03] |
| 2026-04 | OpenAI | Ad Policies v1.1 (medical, legal, financial advice contexts no longer blocked by default); CPM down to $25, minimum $50k reported | [Official, 2026-09] and [Unverified] |
| 2026-04-21 | Microsoft | Offer Highlights in Copilot; UCP-ready feeds GA in US | [Official, 2026-04] |
| 2026-05-05 | OpenAI | Self-serve Ads Manager beta, CPC, partners named (Dentsu, Omnicom, Publicis, WPP; Adobe, Criteo, Kargo, Pacvue, StackAdapt), pixel and CAPI | [Official, 2026-05] |
| 2026-05-07 | OpenAI | Expansion plan for UK, MX, BR, JP, KR | [Official, 2026-05] |
| 2026-05 | Microsoft | AI Max for Search pilot serving Copilot Search and Answers | [Official, 2026-05] |
| 2026-05 | OpenAI | Ad Policies v1.2 (review and enforcement) | [Official, 2026-09] |
| 2026-05-13 | Amazon | Rufus renamed Alexa for Shopping | [Official, 2026-05] |
| 2026-05-20 | Google | GML 2026: Conversational Discovery ads, Highlighted Answers, AI-powered Shopping ads, Business Agent for Leads, Direct Offers | [Official, 2026-05] |
| 2026-06-05 | OpenAI | Conversion optimized campaigns first wave reported | [Unverified] |
| 2026-06-06 | OpenAI | UK pilot reported | [Unverified] |
| 2026-06-15 | OpenAI | Merchant Feed Terms of Service | [Official, 2026-06] |
| 2026-06-22 | Criteo | 2,000+ brands on ChatGPT Ads via Criteo | [Official, 2026-06] (Criteo) |
| 2026-07 | OpenAI | Ad Policies v1.3 | [Official, 2026-09] |
| 2026-08-06 | OpenAI | Product carousels reported | [Unverified] |
| 2026-08-10 | SE Ranking | 50,006 prompt study published | [Study, 2026-08] |
| 2026-08-11 | OpenAI | Ads launched in UK, MX, BR, JP, KR | [Official, 2026-08] |
| 2026-08-17 | Similarweb | AI ads data product: ads in 26% of ChatGPT responses | [Study, 2026-08] |
| 2026-08-17 | OpenAI | Automatic advanced matching reportedly switched on for existing pixels (opt-out) | [Unverified] |
| 2026-08-18 | OpenAI | 31 European markets announced | [Official, 2026-08] |
| 2026-08 | OpenAI | Ad Policies v1.4 (housing and jobs) and v1.5 (US legal services) | [Official, 2026-09] |
| 2026-08-31 | OpenAI | $1B run rate; self-serve in India, Europe, MENA | [Official, 2026-08] |
| 2026-08-31 | EU | ChatGPT reported designated a very large online search engine; DSA obligations from January 2027 | [Unverified] |
| 2026-09-10 | OpenAI | Ad Policies v1.6 (competitive position clause) | [Official, 2026-09] |
| 2026-09-16 | OpenAI | Sponsored Agents test, Ads Manager plugin, AI creative, text customization, HubSpot and Shopify integrations | [Official, 2026-09] |
| 2026-09-22 | OpenAI | Availability page lists 56 self-serve countries | [Official, 2026-09] |
| 2026-09-23 to 24 | OpenAI | Southeast Asia and Taiwan expansion; Shopify app international | [Official, 2026-09] |
| 2026-10-05 | OpenAI | Visual ads in image generation (US test later in October), measurement partner expansion, 1-day view-through in reports, DV and IAS brand safety pilots, Negative Phrases | [Official, 2026-10] |

## 4. Best practice consensus
1. Measure from day one: pixel plus CAPI with a shared event ID, attach event settings to every campaign, preserve `oppref` [Official, 2026-09] and [Practitioner consensus].
2. Start with Clicks (CPC) and daily budgets; move to Conversions once a standard event has volume [Official, 2026-09] (daily budgets recommended for new advertisers) and [Practitioner consensus].
3. One intent per ad group; write context hints as specific needs, situations and offer details [Official, 2026-09].
4. Several distinct ad variations per ad group, concrete and informative copy, specific landing pages [Official, 2026-09].
5. Allow OAI-AdsBot through robots.txt, WAF and CDN; most early rejections were crawler related [Official, 2026-09] and [Practitioner consensus].
6. Treat ChatGPT Ads as a separate paid channel from organic AI visibility [Study, 2026-08].
7. Validate with incrementality before scaling; OpenAI now lists geo incrementality partners [Official, 2026-10].
8. Product feed advertisers should use feed campaigns; OpenAI says feed ads are among its strongest performing [Official, 2026-09].
9. Keep tests narrow (one event, one market, few ad groups) and judge over weeks, not days [Practitioner consensus].

## 5. Contested topics
| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| Hint style | OpenAI: natural phrases, one idea, avoid keyword lists [Official, 2026-09] | One public A/B found keyword style hints beat full questions on impressions, CTR and CPC [Unverified] | Test both head to head; default to OpenAI's style |
| Is it worth it now? | OpenAI and partners cite 3x ROAS, lower CPA vs paid search, high new customer share [Official, 2026-10] | Pilot buyers could not prove ROI; small advertisers report clicks without conversions; experts favor organic ("a game you win through organic, not paid") [Unverified] | Ring fenced test with incrementality; decide on own data |
| CTR level | Criteo: 2x to 3x comparable formats [Unverified] | Similarweb 0.50%, compared with 6.4% on Google Search [Study] | Own baseline; expect under 1.5% |
| Conversions column | Developer docs: `conversions` includes click plus view | Community notes: equals click-through in practice | Request click-through explicitly |
| Dynamic URL parameters | Help: dynamic UTM macros not supported (UI) | API: query string templates with `{campaign_id}`, `{ad_id}`, `{oppref}` | UI static UTMs; API macros where available |
| Negative controls | SE Ranking advises negative keywords | Negative keywords removed from public API spec (2026-09); Negative Phrases for qualifying advertisers (2026-10) | Check account eligibility |
| Ad frequency | 0.8% of prompts (Feb) | 26% of chats (June) | Both true at different times and samples |
| AI Mode ad frequency | 5.8% (Adthena) | 29.45% (SE Ranking) | Method dependent |
| Privacy | OpenAI: no pixel data for user level personalization; aggregate only for advertisers | Independent research: cross advertiser `__obi` cookie, AAM enabled by default | Consent false by default in regulated markets; legal review |
| Criteo minimums | $50k to $100k | $25k, later $10k | Ask the partner; terms changed monthly |

## 6. What top operators do differently
- They run the eligibility gate and measurement build before writing a single ad, and they attach event settings to every campaign so a later move to oCPC has history [Practitioner consensus].
- They design hint tests like keyword tests: one ad group per hint style with identical ads and UTMs per group, judged on relevant clicks per 1,000 impressions [Practitioner consensus].
- They mine Google search terms, Search Console queries, support tickets and AI prompt tracking to write situation hints, not audience labels [Practitioner consensus].
- They use product feed campaigns with margin labels in `ads_metadata` and refresh feeds daily because items expire after 2 weeks [Official, 2026-09].
- They run a synthetic `oppref` test through every redirect and SPA route before launch [Practitioner consensus].
- They report click-through, backend verified results and keep view-through and modeled conversions as context [Practitioner consensus].
- They understand the 2x day and 7x week budget rules and use campaign total budgets for hard caps [Official, 2026-09].
- They sample placements manually from a Free account in the target market [Practitioner consensus].
- They coordinate paid and organic with one intent map and do not sell paid as a route to citations [Study, 2026-08].
- They prioritize AI surfaces reachable through existing Google, Microsoft and Amazon campaigns before buying new inventory [Practitioner consensus].
- They use read only API or MCP access for reporting and keep write access behind human approval, with everything created paused [Practitioner consensus].

## 7. Common expensive mistakes
| Mistake | Consequence | Source |
|---------|-------------|--------|
| Launching without conversion tracking | No optimization data, new campaign needed for oCPC | [Practitioner consensus] |
| Wrong objective or budget type | Immutable; rebuild | [Official, 2026-09] |
| Blocking OAI-AdsBot via WAF or robots | Rejections, Not serving | [Official, 2026-09] |
| Redirects dropping `oppref` | Lost attribution | [Official, 2026-09] |
| Using reserved parameter names | Rejection | [Official, 2026-09] |
| Keyword list hints copied from Google | Off topic placements, low relevance | [Official, 2026-09] |
| Custom audiences or personalization assumptions in EEA | Compliance risk, no lift | [Official, 2026-09] |
| Judging on blended platform conversions | Over crediting | [Practitioner consensus] |
| Expecting pause to stop spend immediately | Up to 24 hours of billable delivery | [Official, 2026-09] |
| Treating vendor CTR and new customer claims as targets | Bad forecasts | [Practitioner consensus] |
| Large pilot commitments early in 2026 | Under delivery (15% to 20% of commitments delivered) | [Unverified] |
| Planning around Instant Checkout | Program scaled back in March 2026 | [Unverified] |

## 8. Benchmarks (source, date, caveat)
| Metric | Value | Source | Date | Caveat |
|--------|-------|--------|------|--------|
| CTR | 0.50% | Similarweb panel | 2026-07 | Panel size undisclosed |
| CTR | 1.30% on 97,000+ impressions | SE Ranking own test, 4 countries | 2026-08 | Before conversion bidding; few signups |
| CTR | 0.68% overall, top quartile 1%, best 1.57% | Similarweb analysis relay | 2026-05 | Conflicts with 0.50% |
| CPC guidance | $3 to $5 | OpenAI | 2026 | US calibrated |
| CPC observed | $3.37 | One advertiser self report | 2026 | Single case |
| CPM | $60 launch, $25 to $45 by April | Trade reports | 2026-02 to 04 | Pilot buys |
| Presence | 25.94% of 50,006 US commercial prompts | SE Ranking | 2026-08 | Synthetic prompts, July snapshot |
| Presence | 26% of US desktop chats (June) | Similarweb | 2026-07 | Panel |
| Relevance | 14.35% of impressions off topic | SE Ranking | 2026-08 | Method: semantic similarity vs random |
| Citation overlap | Advertiser domain cited in 3.63% of placements | SE Ranking | 2026-08 | Sample |
| ROAS | 3x over 28 days, one ecommerce advertiser | OpenAI | 2026-08 | Single case |
| CPA | 15.3% below blended paid search (WeightWatchers) | DV Rockerbox via OpenAI | 2026-10 | Partner reported |
| Incrementality | 2.3x more incremental orders than last click (Dose) | WorkMagic via OpenAI | 2026-10 | Partner reported |
| New customers | 80%+ of ad driven traffic; 93% for Portland Leather | Partner via OpenAI, Triple Whale | 2026-08, 2026-10 | Definitions vary |
| CVR | 0.21% vs 3.71% Google Ads, about 1,500 users | MarTech A/B relay | 2026 | Single test |
| Conversion vs search | About 2x in three categories | Criteo | 2026-05 | Vendor |
| AI Overviews paid CTR | 7.89% cited brands vs 4.14% non cited | Adthena, 5M+ ads | 2026-02 | Google surface |
| AI Mode ad frequency | 29.45% of 50,032 keywords vs 5.8% | SE Ranking vs Adthena | 2026 | Methods differ |

## 8b. Implications by business model (synthesis)
| Model | Fit in 2026 | Why | First move |
|-------|-------------|-----|-----------|
| Ecommerce with catalog | Strongest fit | Feed ads "among the strongest performing" per OpenAI; carousels; Criteo and Shopify paths; OpenAI and partner cases are mostly retail | Product feed campaign on top products, Clicks then oCPC on `order_created` |
| Travel and hospitality | Good fit | High research intent; Booking.com held 62.57% of travel ads in one sample; hotel ads beta | Destination and property intents; watch hotel ads access |
| Local services | Conditional | Sub-national targeting exists; contextual hints can carry service area and fee; small budgets hit the $25 per day minimum | One region, top services, call and form tracking via CAPI |
| Lead gen (non regulated) | Conditional | Lead quality unknown; CAPI 7 day limit prevents sending late qualification events | Optimize on `lead_created`, judge in CRM |
| Finance, health, legal | US only, approved advertisers | Restricted categories; finance share of ads grew to 13% by August [Unverified] | Apply for approval; strict claims review |
| B2B SaaS | Conditional | Business and Enterprise plan users never see ads; free tier professionals do; one SaaS reported 73 signups and zero paying [Unverified] | Problem aware intents, trial events, CRM quality check |
| Apps | Conditional | CAPI only app events, MMP partners, click-through attribution only | iOS and Android app platform campaigns with MMP links |
| Marketplaces and publishers | Weak to conditional | Individual listings disallowed; publishers rarely profit on CPC | Platform level messaging only |
| AI tools competing with OpenAI | Risky | v1.6 competitive clause; reported rejections of image and audio tools | Expect review friction |

## 8c. Budget tier implications (synthesis)
- Starter (under $3k per month): the $25 per day minimum consumes $750 per month for one campaign; most Starter budgets cannot reach 30 conversions. Organic AI visibility and existing Google and Microsoft campaigns (which already reach AI Overviews, AI Mode and Copilot) are a better first step.
- Growth ($3k to $30k): a 4 to 6 week decision test of $4k to $12k is realistic; incrementality via pre/post or time switchback.
- Scale ($30k to $300k): run in every eligible core market, use partner measurement, geo holdouts in the US, product feeds and carousels.
- Enterprise (over $300k): combine managed sales (invoice terms, account spend limits) with self-serve agility; partner geo lift and brand lift; multi market sequencing as countries open.

## 9. Tools, APIs and MCP servers
Official:
- Advertiser API: `https://api.ads.openai.com/v1`, Bearer API key per ad account; campaigns, ad groups, ads, files, insights, conversions setup, audiences, feeds, audit logs; bulk API in limited preview [Official, 2026-09].
- Conversions API: `https://bzr.openai.com/v1/events?pid=<pixel_id>` with a separate CAPI key [Official, 2026-09].
- Docs index: developers.openai.com/ads/llms.txt (33 pages) [Official, 2026-09].
- ChatGPT Ads Manager plugin inside ChatGPT (prompt driven campaign management) [Official, 2026-09].
- `openai-ads-conversions` Codex plugin in github.com/openai/plugins (pixel and CAPI implementation with verification scripts) [Official, 2026-09].
- HubSpot integration and Shopify ChatGPT Ads app [Official, 2026-09].
- MMPs and measurement partners: AppsFlyer, Adjust, Branch, Singular, Kochava, Airbridge, Tenjin, Hightouch, Tealium, LiveRamp, Triple Whale, DV Rockerbox, Northbeam, Fospha, Measured, INCRMNTAL, Haus, WorkMagic, Kantar, Cint [Official, 2026-10].
Community (review before use):
- trakkr-aisearch/openai-ads-mcp (27 tools, readonly mode, paused creates, budget ceiling) [Unverified].
- HYPD-AI/openai-ads-mcp (read only, 11 tools) [Unverified].
- Roast-Labs/openai-ads-mcp, Synter MCP, PaidSync MCP [Unverified].
- faborsky/chatgpt-ads-app CLI with dry run and a Claude Code skill; detailed API notes with live tests [Unverified].
- ShenJun93 preflight checker (crawler, oppref, pixel) [Unverified].
- PostHog OpenAI Ads CDP destination; Linkrunner and SourceMedium integrations [Unverified].
Competitive intelligence: Adthena, Similarweb AI Ads, SE Ranking ads tracker, Sensor Tower [Study].

## 10. Official sources to monitor
| Source | URL | Cadence |
|--------|-----|---------|
| ChatGPT Ads help collection | https://help.openai.com/en/collections/20001223 | Weekly during 2026 |
| Ads Manager Availability | https://help.openai.com/en/articles/20001245-ads-manager-availability | Monthly |
| Ad Policies changelog | https://openai.com/policies/ad-policies/ | Before every launch |
| Testing ads in ChatGPT (dated updates) | https://openai.com/index/testing-ads-in-chatgpt/ | Monthly |
| OpenAI Ads blog | https://ads.openai.com/blog | Weekly |
| Developer docs index | https://developers.openai.com/ads/llms.txt | Before API work |
| OpenAI newsroom | https://openai.com/news/ | Weekly |
| Microsoft "About ads in Copilot" | https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_adsforcopilot | Monthly |
| Google Ads and Commerce blog | https://blog.google/products/ads-commerce/ | Monthly |
| Amazon Ads news | https://advertising.amazon.com | Monthly |

## 11. Open questions and watch list
- CPA billing (pay per conversion): not available; conversion campaigns bill per click or impression [Official, 2026-09].
- Query, topic or placement reporting for advertisers: none today.
- Multi advertiser carousels and competing retailers side by side [Unverified].
- Sponsored Agents general availability, pricing, lead data handling.
- Visual ads performance and expansion beyond the US.
- Negative Phrases eligibility criteria.
- EU DSA ad repository (expected around January 2027) and any EEA personalization change [Unverified].
- Whether OpenAI publishes benchmarks or a native conversion lift product.
- Competitive clause enforcement (AI tools, other assistants) [Unverified].
- Instant Checkout's future and ACP adoption [Unverified].
- Google AI Mode ad formats moving from test to general availability; Gemini app ads (no current plans as of 2025-12).
- Microsoft Copilot specific reporting.
- Perplexity re-entering advertising; Grok ads status.

## 12. Sources
1. Our approach to advertising and expanding access to ChatGPT. OpenAI. https://openai.com/index/our-approach-to-advertising-and-expanding-access/ . 2026-01-16.
2. Testing ads in ChatGPT. OpenAI. https://openai.com/index/testing-ads-in-chatgpt/ . 2026-02-09, updates 2026-03-26, 2026-05-07, 2026-08-11.
3. New ways to buy ChatGPT ads. OpenAI. https://openai.com/index/new-ways-to-buy-chatgpt-ads/ . 2026-05-05.
4. ChatGPT Ads wird in Europa ausgeweitet. OpenAI. https://openai.com/de-DE/index/chatgpt-ads-expands-across-europe/ . 2026-08-18, update 2026-08-31.
5. A milestone in expanding access to AI. OpenAI. https://openai.com/index/expanding-access-to-ai-with-chatgpt-ads/ . 2026-08-31.
6. Reimagining advertising with AI. OpenAI. https://openai.com/index/reimagining-advertising-with-ai/ . 2026-09-16.
7. ChatGPT Ads expands to Southeast Asia and Taiwan. OpenAI. https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/ . 2026-09.
8. Building advertising for the way people use AI. OpenAI. https://openai.com/index/new-chatgpt-ads-format-and-measurement . 2026-10-05.
9. More ways to measure. OpenAI Ads blog. https://ads.openai.com/blog/more-ways-to-measure . 2026-10-05.
10. Buy it in ChatGPT: Instant Checkout and the Agentic Commerce Protocol. OpenAI. https://openai.com/index/buy-it-in-chatgpt/ . 2025-09-29.
11. Ad policies. OpenAI. https://openai.com/policies/ad-policies/ . Updated 2026-09-10 (v1.6).
12. Merchant Feed Terms of Service. OpenAI. https://openai.com/policies/merchant-feed-terms-of-service/ . 2026-06-15.
13. Ads in ChatGPT. OpenAI Help Center. https://help.openai.com/en/articles/20001047-ads-in-chatgpt . Captured 2026-09-23.
14. Ads in ChatGPT: The Basics. OpenAI Help Center. https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics . Captured 2026-09-23.
15. Ads Manager Availability. OpenAI Help Center. https://help.openai.com/en/articles/20001245-ads-manager-availability . Captured 2026-09-22.
16. Ads Manager Beta Account Setup. OpenAI Help Center. https://help.openai.com/en/articles/20001213-ads-manager-beta-account-setup . Captured 2026-09-23.
17. Create Campaigns for ChatGPT Ads. OpenAI Help Center. https://help.openai.com/en/articles/20001210-create-campaigns-for-chatgpt-ads . Captured 2026-09-23.
18. Launch Campaigns. OpenAI Help Center. https://help.openai.com/en/articles/20001209-launch-campaigns . Captured 2026-09-23.
19. Write Context Hints for ChatGPT Ads. OpenAI Help Center. https://help.openai.com/en/articles/20001521-write-context-hints-for-chatgpt-ads . Captured 2026-09.
20. Daily Budgets. OpenAI Help Center. https://help.openai.com/en/articles/20001413-daily-budgets . Captured 2026-09-23.
21. Budget Pacing. OpenAI Help Center. https://help.openai.com/en/articles/20001515-budget-pacing . Captured 2026-09-23.
22. Maximize Results Bid Strategy. OpenAI Help Center. https://help.openai.com/en/articles/20001425-maximize-results-bid-strategy . Captured 2026-09-23.
23. Conversion-optimized Campaigns. OpenAI Help Center. https://help.openai.com/en/articles/20001412-conversion-optimized-campaigns . Captured 2026-09-23.
24. Conversion Measurement. OpenAI Help Center. https://help.openai.com/en/articles/20001409-conversion-measurement . Captured 2026-09.
25. Billing & Payment. OpenAI Help Center. https://help.openai.com/en/articles/20001216-billing-payment . Captured 2026-09-23.
26. Frequently asked questions (ChatGPT Ads). OpenAI Help Center. https://help.openai.com/en/articles/20001220-frequently-asked-questions . Captured 2026-09-23.
27. Advertiser Guidance for Allowing OpenAI Web Crawlers. OpenAI Help Center. https://help.openai.com/en/articles/20001243-advertiser-guidance-for-allowing-openai-web-crawlers . Captured 2026-09.
28. Create Campaigns from Product Feeds. OpenAI Help Center. https://help.openai.com/en/articles/20001268-create-campaigns-from-product-feeds . Captured 2026-09-22.
29. Sponsored Agents in ChatGPT Ads. OpenAI Help Center. https://help.openai.com/en/articles/20001524-sponsored-agents-in-chatgpt-ads . Captured 2026-09-22.
30. Shopping with ChatGPT Search. OpenAI Help Center. https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search . Captured 2026-09-22.
31. Measurement Pixel. OpenAI Developers. https://developers.openai.com/ads/measurement-pixel . Captured 2026-09.
32. Supported Events. OpenAI Developers. https://developers.openai.com/ads/supported-events . Captured 2026-09.
33. Reporting. OpenAI Developers. https://developers.openai.com/ads/reporting . Captured 2026-09.
34. Bidding & Budgets. OpenAI Developers. https://developers.openai.com/ads/bidding-and-budgets . Captured 2026-09.
35. Targeting. OpenAI Developers. https://developers.openai.com/ads/campaign-targeting . Captured 2026-09.
36. openai-ads-conversions plugin. OpenAI (GitHub). https://github.com/openai/plugins/tree/main/plugins/openai-ads-conversions . 2026.
37. About ads in Copilot. Microsoft Learn. https://learn.microsoft.com/en-us/advertising/msa-help/hlp_ba_conc_adsforcopilot . 2026-06-18, updated 2026-09-02.
38. A new generation of ads for the AI era of Search. Google. https://blog.google/products/ads-commerce/google-marketing-live-search-ads/ . 2026-05-20.
39. Why we're experimenting with advertising. Perplexity. https://www.perplexity.ai/hub/blog/why-we-re-experimenting-with-advertising . 2024-11-12.
40. An update on Criteo's integration with OpenAI. Criteo. https://www.criteo.com/news/press-releases/2026/05/an-update-on-criteos-integration-with-openai/ . 2026-05-05.
41. An update on Criteo's integration with OpenAI (June 2026). Criteo. https://www.criteo.com/news/press-releases/2026/06/an-update-on-criteos-integration-with-openai-june-2026/ . 2026-06-22.
42. ChatGPT Ads Study. SE Ranking. https://seranking.com/blog/chatgpt-ads-study/ . 2026-08-10.
43. Ads in AI Search: Key takeaways from the front line. Adthena. https://www.adthena.com/resources/blog/ads-in-ai-search/ . 2026-04-16.
44. Similarweb opens AI ad data as 26% of ChatGPT replies carry sponsored ads. PPC Land. https://ppc.land/similarweb-opens-ai-ad-data-as-26-of-chatgpt-replies-carry-sponsored-ads/ . 2026-08.
45. OpenAI opens ChatGPT Ads Manager to all US businesses with CPC bidding. PPC Land. https://ppc.land/openai-opens-chatgpt-ads-manager-to-all-us-businesses-with-cpc-bidding/ . 2026-05.
46. Criteo becomes first ad tech partner in OpenAI's ChatGPT ad pilot. PPC Land. https://ppc.land/criteo-becomes-first-ad-tech-partner-in-openais-chatgpt-ad-pilot/ . 2026-03.
47. ChatGPT Ads pass $1bn run rate as financial services spend triples. PPC Land. https://ppc.land/chatgpt-ads-pass-1bn-run-rate-as-financial-services-spend-triples/ . 2026-09.
48. Google denies Gemini ads despite advertiser briefings on 2026 rollout. PPC Land. https://ppc.land/google-denies-gemini-ads-despite-advertiser-briefings-on-2026-rollout/ . 2025-12-14.
49. Marketers join OpenAI's ad pilot, nudged by FOMO. Digiday. https://digiday.com/marketing/marketers-join-openais-ad-pilot-nudged-by-fomo/ . 2026-04-27.
50. OpenAI brings product carousels to ChatGPT ads. Digiday. https://digiday.com/marketing/openai-brings-product-carousels-to-chatgpt-ads/ . 2026-08-06.
51. Pitch deck: How ChatGPT ads are being sold to Criteo advertisers. Digiday. https://digiday.com/marketing/pitch-deck-how-chatgpt-ads-are-being-sold-to-criteo-advertisers/ . 2026-03.
52. OpenAI moves to make ChatGPT ads more measurable and more visual. Digiday. https://digiday.com/marketing/openai-moves-to-make-chatgpt-ads-more-measurable-and-more-visual/ . 2026-10.
53. OpenAI to begin testing ads on ChatGPT in the U.S. CNBC. https://www.cnbc.com/2026/01/16/open-ai-chatgpt-ads-us.html . 2026-01-16.
54. ChatGPT's ad pilot has the industry excited, but some insiders are frustrated with the slow rollout. CNBC. https://www.cnbc.com/2026/03/20/chatgpt-ads-testing-openai.html . 2026-03-20.
55. ChatGPT ads are coming, and they'll be influenced by your conversations. Axios. https://www.axios.com/2026/01/16/chatgpt-ai-openai-ads . 2026-01-16.
56. ChatGPT rolls out ads. TechCrunch. https://www.techcrunch.com/2026/02/09/chatgpt-rolls-out-ads/ . 2026-02-09.
57. OpenAI launches visual ads that appear alongside image generation results. TechCrunch. https://techcrunch.com/2026/10/05/openai-launches-visual-ads-that-appear-alongside-image-generation-results/ . 2026-10-05.
58. OpenAI is sticking more ads in ChatGPT. The Verge. https://www.theverge.com/ai-artificial-intelligence/1004655/openai-chatgpt-visual-ads . 2026-10-05.
59. ChatGPT's new ad format fills the image generation loading screen with product carousels. The Decoder. https://the-decoder.com/chatgpts-new-ad-format-fills-the-image-generation-loading-screen-with-product-carousels/ . 2026-10-05.
60. ChatGPT ads pilot leaves advertisers without proof of ROI. Search Engine Land. https://searchengineland.com/openais-ad-platform-cant-tell-advertisers-if-their-money-is-working-472233 . 2026-03.
61. OpenAI Allows Some Health & Finance Ads In ChatGPT. Search Engine Journal. https://www.searchenginejournal.com/openai-allows-some-health-finance-ads-in-chatgpt/585516/ . 2026.
62. ChatGPT Ads to roll out in 31 new markets as OpenAI heads toward IPO. Marketing Brew. https://www.marketingbrew.com/stories/openai-chatgpt-ads-31-new-international-markets-expansion . 2026-08.
63. ChatGPT Ads expands into Southeast Asia and Taiwan. TechNode Global. https://technode.global/2026/09/24/openai-chatgpt-ads-southeast-asia-taiwan/ . 2026-09-24.
64. OpenAI Opens Ad Platform To CPC Bidding, Self-Serve Buys. MediaPost. https://www.mediapost.com/publications/article/414857/openai-opens-ad-platform-to-cpc-bidding-self-serv.html . 2026-05.
65. Perplexity pulling sponsored answers from AI platform. PYMNTS (relaying FT). https://www.pymnts.com/artificial-intelligence-2/2026/perplexity-pulling-sponsored-answers-from-ai-platform/ . 2026-02-18.
66. Amazon lets its advertisers buy ads in ChatGPT in a pilot with OpenAI. The Next Web. https://thenextweb.com/news/amazon-ads-chatgpt-ads-openai-pilot . 2026.
67. OpenAI Brings Ads To ChatGPT As Costs Mount. Forbes. https://www.forbes.com/sites/anishasircar/2026/01/20/openai-brings-ads-to-chatgpt-as-costs-mount/ . 2026-01-20.
68. chatgpt-ads-app (CLI, API notes, playbook). faborsky (GitHub). https://github.com/faborsky/chatgpt-ads-app . 2026-09-02 to 2026-09-24.
69. openai-ads-mcp. Trakkr (GitHub). https://github.com/trakkr-aisearch/openai-ads-mcp . 2026-07.
70. openai-ads-mcp. HYPD AI (GitHub). https://github.com/HYPD-AI/openai-ads-mcp . 2026-09.
71. ad-measurement-preflight. ShenJun93 (GitHub). https://github.com/ShenJun93/ad-measurement-preflight . 2026.
72. OpenAI Ads CDP destination template. PostHog (GitHub). https://github.com/PostHog/posthog/blob/master/nodejs/src/cdp/templates/_destinations/openai_ads/openai.template.ts . 2026.
73. ChatGPT Ads integration docs. Linkrunner (GitHub). https://github.com/linkrunner-labs/docs/blob/main/ad-networks/chatgpt-ads.mdx . 2026-09.
74. How ChatGPT serves ads (independent research mirror). jay1803 (GitHub). https://github.com/jay1803/reading/blob/main/src/content/posts/how-chatgpt-serves-ads.md . 2026-04-30.
75. ChatGPT ad pixel cross site tracking. ailmanac (GitHub). https://github.com/derob98/ailmanac/blob/main/docs/security/chatgpt-ad-pixel-cross-site-tracking.mdx . 2026-09.
76. AI assistant ads research corpus with raw captures. VAD37 (GitHub). https://github.com/VAD37/market-research-2026-09-22 . 2026-09-23.
77. The Instant Checkout postmortem. towton (GitHub). https://github.com/terrence-giggy/towton/blob/main/terrain/marketplace-wars/2026-04-02-the-instant-checkout-postmortem.md . 2026-04-02.
78. FAQ on ChatGPT Advertising. eMarketer. https://www.emarketer.com/content/faq-on-chatgpt-advertising--formats--costs--early-strategies-win . 2026.
