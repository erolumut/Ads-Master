# The State of Digital Advertising and Search, October 2026

Research date: 2026-10-08. Purpose: shared market context for every Ads Master agent. Each channel dossier in `research/` goes deeper; this file sets the frame: where the money goes, how automation and AI search changed the work, what privacy and regulation changed, and what it all means for an operator.

Method and limitations: this overview draws on 14 extended live web searches run for the growth-orchestrator and market-intel builds before the shared search budget for this build was exhausted; direct page fetches were blocked by the research environment. Facts confirmed in live search results are marked (S) in the sources; facts from established prior knowledge are marked (K) and should be re-checked. Forecasts from different firms use different definitions (media owner revenue vs advertiser spend, with or without political ads), so totals are not directly comparable; growth rates and channel directions are the planning signal. Conflicts are labeled [Contested] and single source claims [Unverified]. Platform facts were cross-checked against the channel dossiers built in parallel in `research/` (meta-ads, google-ads, microsoft-ads, tiktok-ads, chatgpt-ads, linkedin-ads, measurement, seo, ai-search-optimization, commerce-feeds, cro, creative-strategy), which carry their own dated sources.

## Executive summary
1. **The market grew faster than expected in 2026.** WPP Media raised its 2026 global ad revenue growth forecast to 8.9% (about $1.3 trillion) in June 2026, from 7.1% in December 2025; the US is forecast at 11.9% excluding political and 13.9% including midterm spend [1][2][3]. dentsu, using a different definition, forecasts 5.0% to about $1.06 trillion with digital at about 69% of spend [4][5]. IAB raised its US 2026 forecast to 12.3% in September 2026 [9].
2. **Social is the largest digital channel in the US.** In 2025 US social ad revenue reached $117.7 billion (+32.6%), passing search at $114.2 billion (+11%); total US internet ad revenue was $294.6 billion (+13.9%) [7].
3. **Search is growing slower and splitting.** dentsu forecasts traditional search growth of 3.4% in 2026 as AI, retail and social search compete; WPP counts search including generative search at 21.8% of global ad revenue and forecasts generative search ad revenue of $5.1 billion in 2026, $32 billion in 2028 and over $100 billion by 2030 [1][4].
4. **AI automation is the default buying model.** Meta reported its Advantage+ end to end solutions passed a $75 billion annual run rate in Q2 2026 (some coverage says $60 billion) and claims $4.52 returned per $1 for Advantage+ users [12][13] [Contested figure, vendor claim]. Google pushes AI Max and new AI Mode ad formats; TikTok made GMV Max the default for Shop ads and expanded Smart+ [17][20][23].
5. **ChatGPT became an ad channel in under a year.** US pilot from 9 February 2026, self serve Ads Manager with CPC bidding from May 2026, more than 60 countries by October 2026, a reported $1 billion annualized run rate by 31 August 2026, and visual ads next to image generation announced on 5 October 2026 [24][25][26][27][28].
6. **Zero click is the new normal.** 68.01% of US Google searches ended without a click in January to April 2026 (SparkToro) vs 60.45% in 2024; AI Overviews cut organic CTR on affected queries (Pew, Seer, Ahrefs) [30][31][32][33].
7. **Commerce media and CTV are the fastest growing paid lines.** US commerce media reached $63.4 billion in 2025 (+18%); IAB expects commerce media +13.6% and CTV +15.6% in the US in 2026; dentsu forecasts retail media +12.3% and CTV +11.5% globally [4][7][9].
8. **Privacy changed shape, not direction.** Chrome kept third party cookies and Google retired most Privacy Sandbox APIs in October 2025, while the EU forced Meta to offer a less personalized ads choice from January 2026 and new EU political ad rules (TTPA) pushed Meta and Google out of EU political advertising from October 2025 [36][37][38][39][41].
9. **Measurement moved to incrementality and modeling.** With signal loss, AI answers that do not click, and black box automation, the teams that win run lift tests and MMM (Meridian, Robyn) and pass profit and lead quality signals into platforms (K).
10. **Operator implication:** the work shifted from targeting and bidding to inputs (data quality, creative volume, offers, feeds, first-party data), cross channel allocation on marginal returns, and visibility across a fragmented "total search" landscape.

## 1. Global ad spend and channel shares
### 1.1 Headline forecasts for 2026
| Forecaster (date) | 2026 total | 2026 growth | Notes |
|-------------------|-----------|-------------|-------|
| WPP Media This Year Next Year, midyear (June 2026) | About $1.3 trillion (media owner revenue, excludes US political) | +8.9% (up from 7.1% in December 2025) | US +11.9% ex political, +13.9% with political; APAC +6.7% [1][2][3] |
| dentsu Ad Spend Forecast (27 May 2026) | About $1.06 trillion | +5.0% (from 5.1% in December) | Digital about 69%; APAC +5.9%, Americas +4.8%, EMEA +3.6%; 2027 raised to +5.5% [4][5][6] |
| Magna summer update (June 2025, last full global forecast found) | Over $1 trillion for the first time | +6.3% | 2025: +4.9% to $979 billion; digital pure players about 73% of revenue [8] |
| IAB Outlook, US only (January 2026, revised September 2026) | n/a | +9.5% revised to +12.3% | Buyer survey [9][10][11] |

Why totals differ: WPP and Magna measure media owner revenue; dentsu measures advertiser spend across 56 markets; IAB surveys US buyers. Use each source's growth rates by channel within its own frame.

### 1.2 US digital channel sizes (IAB/PwC, full year 2025, published April 2026) [7]
| Channel | 2025 revenue | Growth | Share of US internet ad revenue |
|---------|--------------|--------|-------------------------------|
| Social | $117.7B | +32.6% | about 40% |
| Search | $114.2B | +11.0% | 38.8% |
| Display (overlapping category) | $81.6B | +9.8% | n/a |
| Digital video (incl. CTV, social and short form video) | $78.0B | +25.4% | n/a |
| Commerce media | $63.4B | +18.0% | n/a |
| Podcast | $2.9B | +17.6% | n/a |
| Programmatic (buying method) | $162.4B | +20.5% | n/a |
| Total | $294.6B | +13.9% | quarterly growth rose from 12.2% (Q1) to 15.4% (Q4) |
Categories overlap (for example video inside social), so rows do not sum to the total. Creator advertising reached about $37 billion in 2025, projected at $44 billion in 2026 (IAB) [7][15].

### 1.3 Channel growth outlook for 2026
| Channel | IAB US (Sept 2026 revision) [9][10] | dentsu global (May 2026) [4][6] | WPP global (June 2026) [1][2] |
|---------|-------------------------------------|----------------------------------|-------------------------------|
| Social | +16.5% (January: +14.6%) | Strong; December forecast +11.4% | Largest channel; growth slows to single digits from 2027 |
| Search | Paid search +8.1% | +3.4% | Search incl. generative 21.8% of total ad revenue |
| CTV | +15.6% (January: +13.8%) | +11.5% (digital video +8.7%, linear TV 0.0%) | n/a in sources found |
| Commerce or retail media | +13.6% (January: +12.1%) | +12.3% (December: +14.1%); 2027 +11.4% | Retail media projected to overtake total TV ad revenue [14] |
| Digital video ex CTV | +9.4% | n/a | n/a |
| DOOH | +7.0% | n/a | OOH stands out [14] |
| Linear TV | minus 1.5% | 0.0% | n/a |

Reading the table: money keeps flowing to social, CTV and commerce media; search still grows but its share of growth shrinks and part of it moves into AI surfaces.

## 2. The AI automation shift across Meta, Google and TikTok
### 2.1 Meta
| Fact | Date | Source |
|------|------|--------|
| Revenue $60.8B (+28%); Family of Apps ad revenue $59.4B (+27%) | Q2 2026 (reported 29 July 2026) | [12][13][16] |
| Advantage+ end to end solutions over $75B annual run rate (other coverage: about $60B) | Q2 2026 call | [13] [Contested] |
| Advertisers using Advantage+ averaged $4.52 per $1, about 22% above manual campaigns (Meta claim) | Q2 2026 call | [13] (vendor claim) |
| Over 9 million small businesses use at least one AI creative tool; new end to end creative solution; Muse Image rollout | Q2 2026 call | [13] |
| Ranking model gains (GEM and related) credited with more clicks and conversions on Facebook (figures as reported) | Q2 2026 call | [13] [Unverified exact figures] |
| Reported goal to fully automate ad creation and targeting from a URL and budget by end of 2026 | Reported June 2025 | [17] |
| Marketers say full automation is not ready; brands cautious on AI generated creative; Meta says no penalty for opting out of AI features | April 2026 | [17] |
| Analyst view that Meta could overtake Google search ad revenue in 2026 | 2026 | [18] [Unverified projection] |
Operator meaning: Meta rewards broad structures fed by clean conversion data and many distinct creative concepts; manual micro targeting matters less every quarter.

### 2.2 Google
| Fact | Date | Source |
|------|------|--------|
| Ads in AI Overviews expanded to 11 more English markets (12 total: Australia, Canada, India, Indonesia, Kenya, Malaysia, New Zealand, Nigeria, Pakistan, Philippines, Singapore, US); sensitive categories excluded | 19 December 2025 | [19][20] |
| Google Marketing Live 2026: new ad formats inside AI Mode (names vary across reports), US first; access tied to AI Max for Search or Performance Max | 20 May 2026 | [21][22] [secondary] |
| AI Max auto upgrade of automatically created assets and campaign level broad match (September 2026); Dynamic Search Ads migration timing reported as September 2026 by some and February 2027 by others | 2026 | [22]; research/google-ads.md [Contested DSA date] |
| AI Mode available in over 200 countries and territories; very large AI Overviews and AI Mode audiences cited at the keynote | 2025 to 2026 | [21][23] [audience figures Unverified] |
| Meridian open source MMM generally available | January 2025 | (K) |
Operator meaning: search buying shifts from keyword lists to intent and assets judged by automation; feed quality, landing pages and value signals decide performance; new AI surfaces need separate measurement.

### 2.3 TikTok
| Fact | Date | Source |
|------|------|--------|
| US joint venture (TikTok USDS Joint Venture LLC) closes; global TikTok entities manage advertising and ecommerce for the US | 22 January 2026 | [24a][24b] |
| GMV Max became the required format for TikTok Shop ads | July or September 2025 (sources differ) | [25a] [Contested date] |
| Smart Promotion becomes a prerequisite for TikTok Shop campaigns | From April 2026 (per Seller University) | [25b] [Unverified detail] |
| TikTok Ad Network (formerly Pangle, nearly 400,000 apps) opened to US advertisers inside Ads Manager | 2026-10-05 | [25c]; research/tiktok-ads.md |
| NewFronts pitch under the joint venture: stability, richer storytelling formats, personalized targeting | March 2026 | [25d] |
Operator meaning: TikTok is a stable US channel again; automation (Smart+, GMV Max) is the default; creative volume and creator content drive results.

## 3. AI search and zero click
| Evidence | Finding | Source |
|----------|---------|--------|
| SparkToro clickstream (US) | 68.01% of Google searches ended without a click in January to April 2026, vs 60.45% in 2024 (Datos) | [30] |
| Pew Research Center (published July 2025, March 2025 data, 900 US adults, 68,879 searches) | Traditional link clicks in 8% of visits with an AI summary vs 15% without; about 1% clicked a cited source; 26% of sessions ended on summary pages vs 16% | [31] |
| Seer Interactive (3,119 informational queries, 42 organizations) | Organic CTR on AI Overview queries fell 61% (1.76% to 0.61%) and paid CTR fell 68% (19.7% to 6.34%) in 2025; non AIO queries also lost 41% CTR year over year (Sept 2025 vs Sept 2024); organic CTR on AIO queries recovered to 2.36% by February 2026 vs a 3.82% no AIO baseline | [32][34] |
| Ahrefs | Position one CTR minus 34.5% (April 2025), then minus 58% (December 2025, 300,000 keywords); France: up to minus 23.1% soon after rollout | [33][35] |
| arXiv paper on click behavior with AI Overviews | Academic study published August 2026 | [35b] (not read) |
Caveats: AI Overviews appear more on informational queries that already had lower CTR; metrics differ (share of visits with a click vs CTR) [Contested magnitude]. Direction is not contested: fewer clicks per search on informational queries.

Operator meaning: organic traffic forecasts must assume lower CTR; brand, citations in AI answers, and presence on commercial queries matter more; paid search on AI Overview queries also sees lower CTR.

## 4. ChatGPT and AI assistant ads
| Date | Milestone | Source |
|------|-----------|--------|
| 16 January 2026 | OpenAI announces ads testing in ChatGPT for Free and Go users | research/chatgpt-ads.md |
| 9 February 2026 | US pilot starts for Free and Go users; reported $60 CPM and $200,000 minimum through agency partners | [26] [secondary] |
| 5 May 2026 | ChatGPT Ads Manager self serve beta: CPC bidding next to CPM, pixel and Conversions API; launch coverage said no minimum spend, while OpenAI help (September 2026) lists a $25 per day minimum daily budget | [27][28]; research/chatgpt-ads.md |
| 7 May 2026 | Pilot expands to UK, Mexico, Japan, Brazil, South Korea (reported) | [26] [secondary] |
| 24 August 2026 | Ads begin in 31 European countries (reported) | [26] [secondary] |
| 31 August 2026 | Reported $1 billion annualized run rate in under 200 days; self serve opens in Europe, India and MENA | [29] [secondary, Unverified] |
| September to October 2026 | Expansion to Southeast Asia and Taiwan; "more than 60 countries" | [25e] |
| 5 October 2026 | Visual ads alongside image generation results announced; US test with initial advertisers later in October | [28b] |
How it works (as reported): ads only for Free and Go users (paid tiers never see ads); labeled cards below answers; targeting by conversation context, not keywords; Reach objective buys CPM, Clicks objective buys CPC; suggested starting max CPC $3 to $5; measurement through pixel, Conversions API, UTMs and data partners [24c][27][29] [secondary for pricing].
[Contested]: self serve start date (April, May or July 2026 across reports) and country counts (47 to 63) [26][29].

Other AI ad surfaces: ads in Google AI Overviews (12 markets) and AI Mode (US first) [19][21]; Microsoft Copilot as a placement of Search, Shopping and PMax campaigns; Perplexity reportedly exited ads and Gemini and Claude carry no ads as of September 2026 (research/chatgpt-ads.md) [Unverified for Perplexity].
Operator meaning: AI assistant ads are a real test channel in 2026; context replaces keywords; measurement is early, so tests need holdouts or geo reads.

## 5. Retail and commerce media
- US commerce media: $63.4 billion in 2025 (+18%) [7]; IAB expected about $74 billion of retail media spend in 2026 in a separate July 2025 forecast [11b].
- dentsu: retail media +12.3% in 2026 and +11.4% in 2027 globally, down from a 14.1% forecast in December [4][6].
- WPP: retail media projected to overtake total TV ad revenue (June 2026 coverage) [14].
- Marketplaces outside the US carry the same logic: Trendyol, Hepsiburada and Amazon.com.tr in Turkey; Noon and Amazon in the Gulf (K).
Operator meaning: brands selling through retailers or marketplaces need a retail media line with TACoS and new to brand KPIs, and price parity discipline.

## 6. CTV and video
- IAB US CTV growth forecast raised to +15.6% for 2026 (September revision) [9].
- dentsu global: CTV +11.5%, digital video +8.7%, linear TV flat [4].
- Digital video including CTV was the strongest growing IAB category in 2025 at +25.4% to $78 billion [7].
- Programmatic reached $162.4 billion in the US in 2025 (+20.5%), driven partly by CTV [7].
Operator meaning: CTV becomes accessible to Scale tier advertisers (YouTube on TV screens, Amazon and streaming publishers, performance CTV in the US); geo lift is the standard read.

## 7. Creator economy
- IAB: creator advertising about $37 billion in 2025, projected $44 billion in 2026; creator marketing described as a core media channel while search slows [7][15].
- Platform tools (Meta partnership ads, TikTok Spark Ads) turn creator content into paid media (K).
Operator meaning: creators are both a demand creation channel and the main source of native creative for paid social.

## 8. Privacy, regulation and measurement shifts
| Change | Date | Effect | Source |
|--------|------|--------|--------|
| Google drops planned Chrome third party cookie choice prompt | April 2025 | Cookies remain in Chrome by default | [36][37] |
| European Commission DMA decision fines Meta EUR 200 million over "pay or consent" | April 2025 | Pressure on personalized ads in the EU | [39][40] |
| Meta announces end of political, electoral and social issue ads in the EU | 25 July 2025 (effective 6 October 2025) | Category gone from Meta in the EU | [41][42] |
| EU TTPA (Regulation 2024/900) applies | 10 October 2025 | Political ad transparency and consent rules; Google also exited EU political ads | [41][43] |
| Google retires Privacy Sandbox APIs (Attribution Reporting, Topics, Protected Audience and others) | 17 October 2025 | No Sandbox replacement; measurement relies on first-party data, modeling and server-side signals | [36] |
| Meta commits to a less personalized ads choice for EU users | 8 December 2025 (rollout from January 2026) | Part of EU users see less personalized ads; Commission monitors uptake | [38][39][40] |
| Turkey cuts Digital Services Tax to 5% (2026) and 2.5% (2027) | 25 December 2025 | Platform cost base in Turkey; 15% withholding on foreign ad payments unchanged | [44][45] |
| US state privacy laws keep expanding (Indiana, Kentucky, Rhode Island from 1 January 2026) | 2025 to 2026 | Opt out of targeted ads, universal opt out signals | (K) |
Measurement direction: incrementality testing (platform lift, geo tests), open source MMM (Meridian, Robyn), server-side conversion APIs, offline and CRM conversion imports, and profit based values (POAS) are now table stakes at Growth tier and above (K).

### 8.1 Measurement changes operators must rebaseline for (cross-checked with the channel dossiers)
| Change | Date | Effect | Where documented |
|--------|------|--------|------------------|
| Meta removed 7-day view and 28-day view windows from the Ads Insights API | 2026-01-12 | Reported conversions fall with no real change; dashboards need rebaselining | research/meta-ads.md, research/measurement.md [Official via trade coverage] |
| Meta click-through attribution counts link clicks only; other interactions move to a 1-day engage-through window | 2026-03 | Same; compare backend before reacting | research/meta-ads.md [Official via trade coverage] |
| IAB TCF v2.3 mandatory for new consent strings | 2026-03-01 | Non compliant CMP setups risk limited ads | research/measurement.md [Official] |
| GA4 adds an AI Assistant channel to the default channel group (not retroactive) | 2026-05-13 | AI referral reporting out of the box; custom groups still needed for history | research/measurement.md [Official plus secondary] |
| Google offline conversion and enhanced conversions for leads uploads move to the Data Manager API | 2026-06-15 | Silent upload failures are a top audit item | research/measurement.md [Official] |
| Search Console Generative AI performance report (impressions for AI Overviews and AI Mode) | Launched 2026-06-03, all sites by 2026-08-31 | First-party AI visibility data from Google, impressions only | research/seo.md, research/ai-search-optimization.md [Official] |
| Bing Webmaster Tools AI Performance (citations in Copilot and Bing AI answers) | Public preview 2026-02-10 | First-party citation data from Microsoft | research/seo.md [Official] |
| Google Ads Conversion Lift available from a $5,000 budget with enough conversions | 2025 (announcement date contested) | Incrementality tests reachable for Growth tier | research/measurement.md [Official help page] |

### 8.2 Platform status at a glance (October 2026)
| Platform | What changed most in 2026 | Dossier |
|----------|---------------------------|---------|
| Meta | Advantage+ default for sales, app and leads; attribution window changes; Threads ads global (from 2026-01-21); WhatsApp Status ads rolling out; creative diversity drives delivery | research/meta-ads.md |
| Google | AI Max auto upgrade (September 2026); PMax channel reporting and negatives; AI Overviews ads in 12 markets; AI Mode ad formats announced at GML 2026 (Highlighted Answers, Conversational Discovery Ads, Direct Offers) with the US first; official read only Google Ads MCP server (2025-10) | research/google-ads.md |
| Microsoft | AI Max GA (August 2026); experiments GA (September 2026); Copilot as a placement; Xandr Invest DSP wound down | research/microsoft-ads.md |
| TikTok | US joint venture closed (2026-01-22); GMV Max only for Shop ads; TikTok Ad Network (about 400,000 apps) opened to US advertisers on 2026-10-05; official TikTok for Business MCP server (May 2026) | research/tiktok-ads.md |
| OpenAI | ChatGPT ads announced 2026-01-16, US test 2026-02-09, self serve 2026-05-05 with a $25 per day minimum, conversion bidding, product feed ads beta (June 2026), visual ads (October 2026), 60+ countries | research/chatgpt-ads.md |
| LinkedIn | Thought Leader Ads central; LinkedIn targeting data extends to Microsoft Ads (company lists up to 10,000, 2026-09); no official MCP server found | research/linkedin-ads.md |
| Commerce protocols | OpenAI Agentic Commerce Protocol (2025-09) with Instant Checkout scaled back in 2026-03; Google Universal Commerce Protocol (2026-01-11) powering checkout in AI Mode for select US merchants; Microsoft Copilot Checkout (2026-01-08); Merchant API replaced the Content API for Shopping (2026-08-18) | research/commerce-feeds.md, research/ai-search-optimization.md |
| AI answers | Brand lists vary between runs (SparkToro and Gumshoe: under 1 in 100 chance of the same list twice); ChatGPT free tier draws mostly on an internal index per a 2026 study | research/ai-search-optimization.md [Study, 2026] |
| Conversion | Adobe: US retail AI referrals converted 42% better than non AI traffic in March 2026 (38% worse in March 2025) | research/cro.md [Study, 2026] |

## 9. Regional notes
| Region | What stands out in 2026 |
|--------|------------------------|
| US | Fastest growth among large markets (WPP +11.9% ex political); first market for ChatGPT ads, AI Mode ad formats and visual ads in ChatGPT; midterm political spend in 2026 [1][3][27] |
| EU and UK | Consent and DMA limits on personalization; no political or issue ads on Meta and Google in the EU; ChatGPT ads arrived in August 2026 [26][39][41] |
| Turkey | DST cut to 5% in 2026; 15% withholding and reverse charge VAT on foreign ad invoices; high inflation requires monthly re-basing of targets; ChatGPT ads list includes Türkiye per reports [26][44][46] |
| MENA and GCC | ChatGPT self serve opened to MENA markets (31 August 2026, reported) [29]; Snapchat and TikTok strong in the Gulf (K) |
| APAC | dentsu's strongest region (+5.9%); WPP +6.7%; ChatGPT ads expanding in Southeast Asia and Taiwan [3][4][25e] |

## 10. Timeline, January 2025 to October 2026
| Date | Event |
|------|-------|
| 2025-01 | Google Meridian MMM generally available (K) |
| 2025-03 | Google announces AI Mode (K) |
| 2025-04 | EUR 200 million DMA fine for Meta; Google drops Chrome cookie prompt [36][40] |
| 2025-05 | Google brings AI Mode to all US users; AI Max for Search announced (K) |
| 2025-06 | Magna: 2025 +4.9% to $979 billion; Meta full automation goal reported [8][17] |
| 2025-07 | Pew AI summary click study; Meta announces EU political ads exit [31][41] |
| 2025-07 to 2025-09 | GMV Max mandatory for TikTok Shop ads (date contested) [25a] |
| 2025-10-10 | TTPA applies [43] |
| 2025-10-17 | Privacy Sandbox APIs retired [36] |
| 2025-12 | dentsu December forecast; Ahrefs minus 58% CTR study; Meta EU less personalized ads commitment; AI Overview ads in 12 markets; Turkey DST cut [5][33][38][19][44] |
| 2026-01 | IAB Outlook +9.5%; Meta EU choice flows roll out; Meta removes 7-day and 28-day view windows from the Insights API (12 January); OpenAI announces ChatGPT ads (16 January); Threads ads open globally (21 January); TikTok US joint venture closes (22 January) [10][39][24a] |
| 2026-02 | ChatGPT ads US pilot (9 February); Seer reports partial CTR recovery [26][34] |
| 2026-04 | IAB/PwC 2025 report ($294.6 billion); Marketing Brew on Meta automation readiness [7][17] |
| 2026-05 | ChatGPT Ads Manager self serve (5 May); Google Marketing Live AI Mode ads (20 May); dentsu midyear (27 May) [27][21][4] |
| 2026-06 | WPP Media midyear +8.9% [1] |
| 2026-07 | Meta Q2: $60.8 billion revenue, Advantage+ run rate claims [12] |
| 2026-08 | ChatGPT ads in 31 European countries (24 August); $1 billion run rate and self serve in Europe, India, MENA (31 August) [26][29] |
| 2026-09 | IAB raises US forecast to +12.3% (10 September); Google AI Max auto upgrade window (1 to 30 September) [9][22] |
| 2026-10 | ChatGPT visual ads next to image generation announced (5 October); TikTok Ad Network opens to US advertisers (5 October); ChatGPT ads in 60+ countries [28b][25c][25e] |

## 11. What it means for an operator
| Area | Then (2023 to 2024 habits) | Now (late 2026) |
|------|----------------------------|------------------|
| Targeting | Interest stacks, lookalikes, keyword lists | Broad or automated targeting; creative and context do the targeting |
| Bidding | Manual bids, many campaigns | Value based automated bidding; margin and lead quality in conversion values |
| Creative | A few ads refreshed quarterly | Weekly concept testing; AI assisted production; creators as supply |
| Search | Google keywords and SEO rankings | Total search: Google, Microsoft, AI Overviews and AI Mode, ChatGPT and assistants, marketplaces, social search, organic AI visibility |
| Measurement | Platform ROAS and last click | Reconciled backend truth, incrementality tests, MMM, server-side signals |
| Allocation | Average ROAS by channel | Marginal returns by channel, with test budgets |
| Compliance | Cookie banner | Consent signals, DMA choices, political ad bans in the EU, state privacy laws, tax on ad spend in some markets |
| Team | Channel specialists | Orchestrated specialists with shared data, cadence and priorities |

By tier:
| Tier | What to do differently in 2026 |
|------|-------------------------------|
| Starter (under $3k) | One capture channel plus one creation channel at most; clean conversion tracking; strong offer; let automation work with broad settings; monitor AI visibility manually |
| Growth ($3k to $30k) | Server-side events, margin aware values, weekly creative testing, 10% test budget (ChatGPT ads, TikTok, CTV via YouTube), share of search tracking |
| Scale ($30k to $300k) | Lift tests twice a year, MMM start, retail media and CTV lines, AI visibility program, creative production system |
| Enterprise (over $300k) | MMM calibrated with experiments, portfolio allocation across markets, governance for AI generated creative and regulatory variance |

## 12. The 10 biggest strategic implications
1. **Inputs beat settings.** On automated platforms the levers are conversion signal quality, profit and lead quality values, creative diversity, offers and feeds. Teams that still optimize settings lose to teams that optimize inputs.
2. **Plan for "total search".** Traditional search grows about 3% to 8% while generative search becomes a multi billion dollar ad market; budget and visibility plans must cover AI Overviews, AI Mode, ChatGPT and assistants, marketplaces and social search, not only Google keywords.
3. **Organic traffic is no longer a free baseline.** With about 68% zero click searches and lower CTR under AI Overviews, forecast organic conservatively and invest in being cited and recommended, not only ranked.
4. **Test AI assistant ads now, measure them honestly.** ChatGPT ads went from pilot to 60+ countries in eight months; early movers learn context targeting while costs settle. Use holdouts or geo reads; do not trust early attributed numbers alone.
5. **Social and creators are the growth engine for demand creation.** Social passed search in US revenue and creator spend keeps rising; creative volume and creator supply are capacity planning items.
6. **Commerce media and CTV deserve their own lines.** Fastest growing channels in IAB and dentsu forecasts; they need TACoS, new to brand, reach and geo lift measurement rather than last click.
7. **Measurement maturity is the main competitive moat.** Reconciled backend data, server-side events, incrementality tests and MMM decide who can scale; without them, automation optimizes toward the wrong outcomes.
8. **Allocate on marginal returns across channels.** Growth rates differ sharply by channel; the next dollar's return, not the average, decides where it goes.
9. **Regulatory and regional variance is a planning input.** EU personalization limits and political ad exits, US state privacy laws, Turkey's withholding on ad payments and inflation, and Gulf creator licensing change targets and channel choices.
10. **The operating system is the strategy.** One goal, few priorities, weekly learning loops, monthly reallocation and an experiment program turn a fast changing market into compounding learning.

## 13. Open questions to watch
- Will ChatGPT ads publish transparency tooling or an ad library, and how will incrementality look outside the US?
- When will Google expand AI Mode ad formats beyond the US, and how will reporting separate them?
- Will Meta ship URL to campaign automation broadly, and what controls will remain for advertisers?
- How many EU users chose Meta's less personalized ads, and what does it do to EU CPA?
- Will social growth slow to single digits from 2027 as WPP forecasts, and where will the budget go next?
- How will the Turkish DST cut to 2.5% in 2027 and any platform fee changes affect true media costs?

## 14. Sources
1. This Year Next Year 2026 Midyear Forecast. WPP Media. https://www.wppmedia.com/news/report-this-year-next-year-midyear-2026 (2026-06) (S)
2. Global Midyear Ad Forecast 2026. WPP Media. https://www.wppmedia.com/thought-leadership/this-year-next-year/midyear-2026 (2026-06) (S)
3. WPP ups global ad spend forecasts to 8.9% on AI gold rush. Mi3. https://www.mi-3.com.au/19-06-2026/industry-dynamics-dont-seem-make-much-sense-wpp-ups-global-ad-spend-forecasts-89-ai-gold (2026-06-19) (S)
4. Ad Spend Growth Is Projected to Slow to 5.0% in 2026, Still Outpacing Economic Growth. dentsu. https://www.dentsu.com/news-releases/ad-spend-growth-is-projected-to-slow-to-5-percent-in-2026-still-outpacing-economic-growth (2026-05-27) (S)
5. Global Ad Spend Set to Surpass $1 Trillion for the First Time in 2026 as the Algorithmic Era Redefines Growth. dentsu. https://www.dentsu.com/news-releases/global-ad-spend-set-to-surpass-one-trillion-for-the-first-time-in-2026-as-the-algorithmic-era-redefines-growth (2025-12) (S)
6. Dentsu downgrades ad spending forecast as geopolitical tensions pressure growth. eMarketer. https://www.emarketer.com/content/dentsu-downgrades-ad-spending-forecast-geopolitical-tensions-pressure-growth (2026-05) (S)
7. IAB/PwC Internet Advertising Revenue Report: Full Year 2025. IAB. https://www.iab.com/insights/internet-advertising-revenue-report-full-year-2025/ (2026-04) (S)
8. Magna latest to downgrade global ad spending forecast, expects $979B. Marketing Dive. https://www.marketingdive.com/news/magna-latest-to-downgrade-global-ad-spending-forecast-expects-979b/750871/ (2025-06) (S)
9. IAB Raises 2026 U.S. Ad Spend Forecast to +12.3% YoY Growth. IAB. https://www.iab.com/news/iab-raises-2026-u-s-ad-spend-forecast/ (2026-09) (S)
10. IAB 2026 Outlook. IAB. https://www.iab.com/insights/2026-outlook/ (2026-01) (S)
11. IAB Revises Ad Forecast, Shows Growth For Most Media. MediaPost. https://www.mediapost.com/publications/article/417763/iab-revises-ad-forecast-shows-growth-for-most-med.html (2026-09-10) (S)
11b. IAB: Retail Commerce Media To Drive $74B Ad Spend In 2026. MediaPost. https://www.mediapost.com/publications/article/407741/iab-forecast-retail-media-to-drive-74b-ad-spend.html (2025) (S)
12. Meta Reports Second Quarter 2026 Results. Meta. https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx (2026-07-29) (S)
13. Meta Q2 2026 Earnings Call Transcript. Meta. https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf (2026-07-29) (S)
14. OOH Stands Out, Retail Media To Overtake Total TV Ad Revenue: WPP Media. LBB Online. https://lbbonline.com/news/wpp-media-advertising-forecast-report-2026 (2026-06) (S)
15. Creator marketing now a core media channel while search slows: IAB. Marketing Dive. https://www.marketingdive.com/news/creator-marketing-now-a-core-media-channel-while-search-slows-iab/817832/ (2026) (S)
16. Meta Boosts Advertising In Q2, Tries To Reassure Investors On AI. MediaPost. https://www.mediapost.com/publications/article/416925/meta-boosts-advertising-in-q2-tries-to-reassure-i.html (2026-07-31) (S)
17. How Meta's AI push is changing ad creation. Marketing Brew. https://www.marketingbrew.com/stories/2026/04/07/meta-ai-ad-creation (2026-04-07) (S)
18. Meta could overtake Google search ad revenue in 2026, Bernstein says. TradingView (Stocktwits). https://www.tradingview.com/news/stocktwits:29919a030094b:0-meta-could-overtake-google-search-ad-revenue-in-2026-bernstein-says-ai-is-driving-the-shift/ (2026) (S)
19. Google quietly expands AI Overview ads to 11 countries without fanfare. PPC Land. https://ppc.land/google-quietly-expands-ai-overview-ads-to-11-countries-without-fanfare/ (2025-12) (S)
20. Google Expands Ads In AI Overviews To More Countries. Search Engine Roundtable. https://www.seroundtable.com/google-expands-ads-in-ai-overviews-40629.html (2025-12) (S)
21. Google AI Mode ads: what changed at Marketing Live 2026. Yellowhead. https://www.yellowhead.com/blog/google-ai-mode-ads/ (2026-05) (S)
22. Google Marketing Live 2026: 7 Updates to Act On. Dataslayer. https://www.dataslayer.ai/blog/google-marketing-live-2026-updates-marketers (2026-05) (S)
23. AI Mode is now available in more languages and locations. Google. https://blog.google/products-and-platforms/products/search/ai-mode-expands-languages-locations/ (2025) (S)
24a. The deal to secure TikTok's future in the US has finally closed. CNN. https://www.cnn.com/2026/01/22/tech/tiktok-us-deal-closes (2026-01-22) (S)
24b. TikTok's US overhaul gives advertisers greater certainty, though questions remain. eMarketer. https://www.emarketer.com/content/tiktok-s-us-overhaul-gives-advertisers-greater-certainty--though-questions-remain (2026) (S)
24c. Building advertising for the way people use AI. OpenAI. https://openai.com/index/new-chatgpt-ads-format-and-measurement/ (2026) (S)
25a. TikTok Shop Makes GMV Max Ads Mandatory From Sept 1. CedCommerce. https://cedcommerce.com/blog/tiktok-shop-mandates-gmv-max-use-for-ads-what-this-means-for-your-strategy/ (2025) (S)
25b. TikTok Shop Campaign x Smart Promotion. TikTok Shop Seller University. https://seller-us.tiktok.com/university/essay?knowledge_id=6371753145599758&lang=en (2026) (S)
25c. TikTok opens ad network of nearly 400,000 apps to US advertisers. PPC Land. https://ppc.land/tiktok-opens-ad-network-of-nearly-400-000-apps-to-us-advertisers (2026) (S)
25d. TikTok pitches advertisers on bold new chapter under US joint venture. Marketing Dive. https://www.marketingdive.com/news/tiktok-pitches-advertisers-on-bold-new-chapter-under-us-joint-venture/815632/ (2026-03) (S)
25e. ChatGPT Ads expands to Southeast Asia and Taiwan. OpenAI. https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/ (2026) (S)
26. Where ChatGPT Ads Are Sold: Every Market, Every Date. Digital Applied. https://www.digitalapplied.com/blog/where-chatgpt-ads-are-sold-every-market-and-date (2026) (S)
27. OpenAI Opens Ad Platform To CPC Bidding, Self-Serve Buys. MediaPost. https://www.mediapost.com/publications/article/414857/openai-opens-ad-platform-to-cpc-bidding-self-serv.html (2026-05-06) (S)
28. OpenAI opens ChatGPT Ads Manager to all US businesses with CPC bidding. PPC Land. https://ppc.land/openai-opens-chatgpt-ads-manager-to-all-us-businesses-with-cpc-bidding/ (2026-05) (S)
28b. OpenAI launches visual ads that appear alongside image generation results. TechCrunch. https://techcrunch.com/2026/10/05/openai-launches-visual-ads-that-appear-alongside-image-generation-results/ (2026-10-05) (S)
29. ChatGPT Ads Hits $1B: And Small Advertisers Can Finally Get In. Panstag. https://www.panstag.com/2026/09/chatgpt-ads-1-billion-self-serve-expansion.html (2026-09) (S, secondary)
30. Google zero-click searches reach 68% in early 2026: Study. Search Engine Land. https://searchengineland.com/google-zero-click-searches-2026-study-479717 (2026) (S)
31. Pew Research Confirms Google AI Overviews Is Eroding Web Ecosystem. Search Engine Journal. https://www.searchenginejournal.com/pew-research-confirms-google-ai-overviews-is-eroding-web-ecosystem/551825/ (2025-07) (S)
32. Google AI Overview Study: SEO and PPC CTR impact. Seer Interactive. https://www.seerinteractive.com/insights/ctr-aio (2025 to 2026) (S)
33. Ahrefs Study: Google AI Overviews Cut Clicks By 58%. MediaNama. https://www.medianama.com/2026/02/223-google-ai-overviews-click-through-rates-58-study/ (2026-02) (S)
34. New data: Google AI Overviews are hurting click-through rates. Search Engine Land. https://searchengineland.com/google-ai-overviews-hurt-click-through-rates-454428 (2025) (S)
35. AI Overviews Cut CTR by 23.1% in France. Ahrefs. https://ahrefs.com/blog/ai-overviews-france-impact/ (2026) (S)
35b. Investigating Click Behaviors On Google Search Result Pages That Produce an AI Overview. arXiv. https://arxiv.org/pdf/2608.04831 (2026-08) (S, not read)
36. Google Privacy Sandbox officially shuts down: What it means and what's next. Usercentrics. https://usercentrics.com/knowledge-hub/what-is-google-privacy-sandbox/ (2025) (S)
37. Google Drops Plans for Third-Party Cookie Choice Prompt in Chrome. OneTrust. https://www.onetrust.com/blog/google-drops-plans-for-third-party-cookie-choice-prompt-in-chrome/ (2025-04) (S)
38. Meta agrees to offer less-personalized ad option for EU users. Anadolu Agency. https://www.aa.com.tr/en/europe/meta-agrees-to-offer-less-personalized-ad-option-for-eu-users/3765367 (2025-12) (S)
39. Meta Platforms Form 10-Q (quarter ended 30 June 2026). SEC. https://www.sec.gov/Archives/edgar/data/0001326801/000162828026050705/meta-20260630.htm (2026) (S)
40. Meta commits to give EU users choice on personalised ads under DMA. EU Reporter. https://www.eureporter.co/business/digital-economy/2025/12/09/meta-commits-to-give-eu-users-choice-on-personalised-ads-under-dma/ (2025-12-09) (S)
41. Ending Political, Electoral and Social Issue Advertising in the EU in Response to Incoming European Regulation. Meta. https://about.fb.com/news/2025/07/ending-political-electoral-and-social-issue-advertising-in-the-eu/ (2025-07) (S)
42. Meta to stop selling political ads in the EU from October. TechCrunch. https://techcrunch.com/2025/07/25/meta-to-stop-selling-political-ads-in-the-eu-from-october (2025-07-25) (S)
43. Google to Stop Showing Political Ads to Users in European Union. Giga Law. https://giga.law/daily-news/2024/11/15/google-to-stop-showing-political-ads-to-users-in-european-union (2024-11-15) (S)
44. Dijital hizmet vergisi oranı yeniden belirlendi. Anadolu Ajansı. https://aa.com.tr/tr/ekonomi/dijital-hizmet-vergisi-orani-yeniden-belirlendi/3780348 (2025-12) (S)
45. Turkey Plans Gradual Reduction of Digital Services Tax to 2.5% by 2027. VATupdate. https://www.vatupdate.com/2026/01/07/turkey-plans-gradual-reduction-of-digital-services-tax-to-2-5-by-2027/ (2026-01-07) (S)
46. 20% VAT and 15% Withholding Tax should be calculated for Google and YouTube Advertising Invoices in Türkiye. Karen Audit. https://www.karenaudit.com/en/20-vat-and-15-withholding-tax-should-be-calculated-for-google-and-youtube-advertising-invoices-in-turkiye/ (n.d.) (S)
47. Meridian. Google. https://developers.google.com/meridian (2025-01) (K)
48. Robyn. Meta. https://facebookexperimental.github.io/Robyn/ (ongoing) (K)
49. US State Privacy Legislation Tracker. IAPP. https://iapp.org/resources/article/us-state-privacy-legislation-tracker/ (ongoing) (K)
50. Regulation (EU) 2024/900 on the transparency and targeting of political advertising. EUR-Lex. https://eur-lex.europa.eu/eli/reg/2024/900/oj (2024-03) (K)
