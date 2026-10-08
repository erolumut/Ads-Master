# Research Dossier: Growth Orchestration (channel mix, budget allocation, unit economics, operating system)

Research date: 2026-10-08. Scope: how top operators decide channel mix, allocate budgets, set unit economics targets, run multi channel teams and reviews, and how the 2025 to 2026 platform, privacy and tax changes alter those decisions. Companion: `research/00-market-overview-2026.md`.

Method and limitations: live web research ran until the shared search budget for this build was exhausted (14 extended searches for this dossier and the market overview), and direct page fetches were blocked by the research environment's egress policy. Every fact below that came from the live sweep is marked (S) in the source list; facts from established prior knowledge are marked (K) and should be re-checked in the Freshness Protocol. Evidence labels follow `docs/AUTHORING_SPEC.md`. Numbers were not invented; where sources conflict the item is marked [Contested].

## 1. Executive summary
1. Automation has moved targeting and bidding inside the platforms. Meta reported its Advantage+ end to end solutions passed a $75 billion annual revenue run rate in Q2 2026 (some coverage says $60 billion) [Official claim, 2026-07; Contested figure]. The orchestrator's leverage is now inputs: conversion signal quality, margin aware values, creative supply and budget allocation across channels.
2. Budgets keep moving to digital: WPP Media expects global ad revenue to grow 8.9% to about $1.3 trillion in 2026; dentsu expects 5.0% growth with digital at about 69% of spend [Study, 2026-06 and 2026-05]. Forecasters disagree on totals because of definitions; use growth rates by channel, not totals, for planning.
3. Search is splitting. dentsu forecasts traditional search growth of only 3.4% in 2026 as AI, retail and social search compete; WPP counts generative search at $5.1 billion in 2026 rising to over $100 billion by 2030 [Study, 2026]. Plan "total search": Google and Microsoft, AI assistant ads, marketplaces, social search and organic AI visibility.
4. ChatGPT became an ad channel in 2026: US pilot in February, self serve Ads Manager beta with CPC bidding in May, expansion to more than 60 countries by October, reported $1 billion annualized run rate by 31 August [Official and secondary reports, 2026]. It belongs in the test bucket (10%) with honest incrementality reads.
5. Measurement is the binding constraint more often than media: zero click searches reached about 68% of US Google searches in January to April 2026 (SparkToro), AI Overviews cut organic CTR on affected queries, consent rules and DMA choices reduce signal in the EU [Study, 2026]. Incrementality tests and MMM (Meridian, Robyn) are now accessible at Growth and Scale tiers.
6. Allocation on marginal returns is the main differentiator of top operators: they fit response curves or run budget step tests and equalize marginal CPA across channels instead of chasing the highest average ROAS [Practitioner consensus].
7. Unit economics must include taxes and fees on media in some markets. In Turkey, payments to foreign ad platforms carry 15% withholding (grossed up, up to about 17.6% extra cost) plus reverse charge VAT; the Digital Services Tax on platforms fell to 5% in 2026 and is set to fall to 2.5% in 2027 [Official, 2025-12; practitioner guidance].
8. EU rules reshape targeting: Meta's less personalized ads choice rolled out to EU users from January 2026 under the DMA, and Meta and Google stopped political, electoral and social issue ads in the EU around the October 2025 TTPA start [Official, 2025 to 2026].
9. Brand vs performance evidence still points to a deliberate split (Binet and Field average near 60:40 for B2C, about 46:54 for B2B), adjusted by category, stage and budget; small and new brands lean to activation [Study, 2013 to 2019]. No new 2025 to 2026 study with a published method could be verified in this sweep.
10. The operating system matters as much as tactics: one quarterly goal, max 5 priorities, weekly learning loop, monthly reallocation, quarterly reset and an experiment program with stop rules is what separates consistent teams from reactive ones [Practitioner consensus].

## 2. State of growth management in 2026 (with numbers)
### 2.1 Where the money goes
| Indicator | Value | Source |
|-----------|-------|--------|
| Global ad revenue 2026 | About $1.3 trillion, +8.9% (media owner revenue, excludes US political) | WPP Media midyear, 2026-06 (S) |
| Global ad spend 2026 (alternative definition) | About $1.06 trillion, +5.0%; digital about 69% | dentsu, 2026-05-27 (S) |
| US internet ad revenue 2025 | $294.6 billion, +13.9% | IAB/PwC, 2026-04 (S) |
| US social 2025 | $117.7 billion, +32.6%, about 40% of digital | IAB/PwC, 2026-04 (S) |
| US search 2025 | $114.2 billion, +11%, 38.8% of digital | IAB/PwC, 2026-04 (S) |
| US commerce media 2025 | $63.4 billion, +18% | IAB/PwC, 2026-04 (S) |
| US programmatic 2025 | $162.4 billion, +20.5% | IAB/PwC, 2026-04 (S) |
| US 2026 total ad spend growth (buyer survey) | +12.3% (revised up from +9.5% in January) | IAB, 2026-09 (S) |
| US 2026 channel growth (IAB revised) | Social +16.5%, CTV +15.6%, commerce media +13.6%, paid search +8.1%, digital video ex CTV +9.4%, DOOH +7.0%, linear TV minus 1.5% | IAB, 2026-09 (S) |
| Global 2026 channel growth (dentsu) | Retail media +12.3%, CTV +11.5%, search +3.4% | dentsu, 2026-05 (S) |
| Generative search ad revenue | $5.1 billion (2026), $32 billion (2028), over $100 billion (2030) | WPP Media, 2026-06 (S) |

Implication for channel mix: social and CTV take the largest share of incremental budget in the US; paid search keeps growing but slower; commerce media becomes a default line item for brands selling through retailers and marketplaces.

### 2.2 How platforms changed the orchestrator's job
| Shift | Evidence | Effect on orchestration |
|-------|----------|-------------------------|
| End to end automation on Meta | Advantage+ run rate claims; plan for fully automated ad creation by end of 2026 reported in 2025; marketers in April 2026 said it is not ready [Official claim 2026-07; Marketing Brew 2026-04] (S) | Allocate by objective and value signal, not by audience micro segments; creative volume is the scaling constraint |
| Google AI Max and AI Mode | AI Max for Search launched 2025 and absorbed automatically created assets and broad match in a September 2026 auto upgrade; Dynamic Search Ads migration timing is contested (September 2026 vs February 2027); new AI Mode ad formats announced at Marketing Live (May 2026), US first [secondary reports] (S) | Search budgets increasingly buy "intent" across query and AI surfaces; measure on incremental value |
| TikTok Smart+ and GMV Max | GMV Max became the required Shop ads format in 2025 (dates contested); Smart Promotion prerequisite for Shop campaigns from April 2026 per Seller University; US joint venture closed 22 January 2026 (S) | TikTok is a stable US channel again; automation default |
| ChatGPT ads | Pilot February 2026, self serve CPC May 2026, 60+ countries by October 2026, visual ads near image generation from October 2026 in the US (S) | New demand capture surface; test bucket; context based targeting |
| Privacy | Chrome kept third party cookies; Privacy Sandbox APIs retired October 2025 (S); EU DMA less personalized ads from January 2026 (S); US state laws expand (K) | Server-side signal, consent, first-party data and incrementality testing are prerequisites for scaling |

### 2.3 Measurement conditions in 2026
| Condition | Evidence | Planning consequence |
|-----------|----------|----------------------|
| Zero click search rising | 68.01% of US Google searches ended without a click in January to April 2026 vs 60.45% in 2024 (SparkToro clickstream via Search Engine Land) (S) | Organic forecasts must assume fewer clicks per impression; brand and AI visibility metrics join the scorecard |
| AI Overviews reduce clicks | Pew (July 2025): link clicks 8% of visits with an AI summary vs 15% without; Seer: organic CTR on AIO queries fell 61% in 2025 then partly recovered to 2.36% by February 2026; Ahrefs: position one CTR minus 58% (S) | Informational content loses traffic; commercial and comparison queries plus citations matter more |
| Cookies stay in Chrome, Sandbox gone | Google dropped the cookie prompt (April 2025) and retired Sandbox APIs (October 2025) (S) | No forced migration, but consent, Safari and Firefox limits, and DMA choices still reduce signal; invest in server-side events and first-party data |
| EU personalization limits | Meta less personalized ads choice from January 2026; Commission monitoring uptake (S) | Expect weaker targeting for part of EU audiences; creative and broad automation carry more weight |
| Accessible incrementality and MMM | Meridian GA (2025), Robyn, GeoLift; platform lift tools (K) | Scale tier teams can calibrate allocation with experiments twice a year |
| AI assistant referrals measurable but small | GA4 referral data from ChatGPT, Perplexity, Copilot, Gemini (K) | Track as a separate channel group; judge on assisted and direct conversions |

### 2.4 Geo realities that change targets
- **Turkey.** True media cost on foreign billed platforms is about 15% to 17.6% above platform spend because of the 15% withholding on online advertising payments (Presidential Decision 476, effective 2019), with 20% reverse charge VAT that VAT registered buyers can usually deduct (S). DST on platforms fell to 5% for 2026 and is scheduled at 2.5% from 2027 (S). High inflation means nominal CPC and CPA rise every month; plan in real terms. Installments drive conversion; marketplaces (Trendyol, Hepsiburada, Amazon.com.tr) hold large ecommerce demand (K). KVKK's 2024 amendment changed cross border transfer rules relevant to pixels and CAPI (K).
- **EU and UK.** Consent Mode and CMP setups are mandatory for signal; DMA choice flows reduce Meta personalization; TTPA ended political and social issue ads on Meta and Google in the EU (S). EU AI Act transparency duties for AI generated content are scheduled for August 2026 (K, timing under review).
- **US.** First market for new ad products (ChatGPT ads self serve, AI Mode formats, visual ads) (S); state privacy patchwork with universal opt out signals and strict health data laws (K).
- **MENA and GCC.** ChatGPT ads self serve opened to MENA on 31 August 2026 per reports (S, secondary). Snapchat and TikTok are strong in the Gulf; Ramadan dominates planning; BNPL and local payment methods affect conversion (K).

### 2.5 Allocation practice in 2026
- Marginal analysis is now practical without an MMM: weekly spend and conversion data across 12+ weeks gives a usable log curve when spend varied enough; budget step tests fill the gaps (K).
- MMM adoption moved down market with open source tools, but practitioners warn that MMM without experiments can mislead; calibration with lift tests is the norm among top teams [Practitioner consensus].
- Test buckets in 2026 typically include ChatGPT ads, TikTok (re-entering US plans after the joint venture closed), CTV and retail media, matching the fastest growing lines in IAB and dentsu forecasts (S).

## 3. Timeline of changes, January 2025 to October 2026
| Date | Change | Relevance to orchestration | Status |
|------|--------|---------------------------|--------|
| 2025-01 | Google Meridian open source MMM generally available | MMM accessible to Scale tier | K |
| 2025-03 | Google announces AI Mode (Labs) | Start of AI search shift | K |
| 2025-04 | European Commission fines Meta EUR 200 million under the DMA over "pay or consent" | EU personalization limits | S |
| 2025-04 | Google drops planned Chrome third party cookie choice prompt | Cookies remain; no Sandbox migration | S |
| 2025-05 | Google Marketing Live 2025: AI Max for Search; ads in AI Mode tests | Search automation | K |
| 2025-06 | Magna summer update: 2025 global ad revenue +4.9% to $979 billion; digital pure players about 73% | Baseline | S |
| 2025-06 | Reports that Meta aims to fully automate ad creation by end of 2026 | Automation roadmap | S |
| 2025-07 | Pew study: link clicks 8% with AI summary vs 15% without (March 2025 data) | Organic demand capture weakens | S |
| 2025-07-25 | Meta announces end of political, electoral and social issue ads in the EU from October 2025 | Category restrictions EU | S |
| 2025-07 to 2025-09 | TikTok GMV Max becomes mandatory for TikTok Shop ads (July 15 or September 1 depending on source) | Commerce automation | S [Contested date] |
| 2025-10-10 | EU TTPA (Regulation 2024/900) applies | Political ads rules | S |
| 2025-10-17 | Google retires remaining Privacy Sandbox APIs | Measurement stays on cookies, first-party and modeled signals | S |
| 2025-12-08 | European Commission announces Meta commitment to a less personalized ads choice from January 2026 | EU targeting | S |
| 2025-12-18 | TikTok signs US joint venture agreement | US platform risk falls | S |
| 2025-12-19 | Google expands ads in AI Overviews to 11 more English markets (12 total) | AI surface ads | S |
| 2025-12-25 | Turkey cuts DST to 5% from 2026 and 2.5% from 2027 (Decision No. 10767) | Turkey true media cost | S |
| 2025-12 | Ahrefs: AI Overviews reduce position one CTR by 58% (300,000 keywords) | Organic forecast | S |
| 2026-01 | Meta revised EU choice flows (full vs less personalized ads) roll out | EU signal | S |
| 2026-01-12 | Meta removes 7-day and 28-day view windows from the Ads Insights API | Reported conversions drop without real change; rebaseline targets | K (cross-checked with research/meta-ads.md, research/measurement.md) |
| 2026-01-16 | OpenAI announces ads testing in ChatGPT | New channel on the horizon | K (research/chatgpt-ads.md) |
| 2026-01-22 | TikTok US joint venture deal closes | US TikTok planning | S |
| 2026-01 | IAB 2026 Outlook: US ad spend +9.5% | Planning baseline | S |
| 2026-02-09 | ChatGPT ads US pilot starts (Free and Go users) with reported $60 CPM and $200,000 minimum via agencies | New channel | S [secondary] |
| 2026-03 | Meta click attribution limited to link clicks; 1-day engage-through window added | Second rebaseline of Meta reported results | K (research/meta-ads.md) |
| 2026-04 | IAB/PwC full year 2025: $294.6 billion | Channel shares | S |
| 2026-04 | TikTok Shop Smart Promotion prerequisite (per Seller University) | Commerce | S [Unverified detail] |
| 2026-05-05 | ChatGPT Ads Manager self serve beta, CPC bidding, no minimum, pixel and Conversions API | Test budget access | S |
| 2026-05-20 | Google Marketing Live 2026: AI Mode ad formats (US first), Universal Cart | Search plans | S [secondary] |
| 2026-05-13 | GA4 adds an AI Assistant default channel | AI referrals visible in standard reports | K (research/measurement.md) |
| 2026-05-27 | dentsu midyear: 2026 +5.0%, search +3.4% | Planning | S |
| 2026-06 | WPP Media midyear: +8.9%, $1.3 trillion, generative search forecasts | Planning | S |
| 2026-07-29 | Meta Q2 2026: revenue $60.8 billion (+28%); Advantage+ run rate claims | Meta scale | S |
| 2026-08-24 | ChatGPT ads begin serving in 31 European countries | EU AI ads | S [secondary] |
| 2026-08-31 | OpenAI reports $1 billion annualized ads run rate; self serve opens in Europe, India and MENA | Test availability by geo | S [secondary] |
| 2026-09 | Google AI Max auto upgrade (automatically created assets and broad match), 1 to 30 September; DSA migration date contested | Search structure | S [secondary; cross-checked with research/google-ads.md] |
| 2026-09-10 | IAB raises 2026 US forecast to +12.3% | Planning | S |
| 2026-09 to 2026-10 | ChatGPT ads expand to Southeast Asia and Taiwan; "more than 60 countries" | Geo availability | S |
| 2026-10-05 | OpenAI announces visual ads next to image generation results (US test); TikTok Ad Network opens to US advertisers | New formats and inventory | S |

## 4. Best practice consensus
1. Diagnose the binding constraint before choosing tactics; tracking and economics come before media [Practitioner consensus].
2. Derive every target from contribution margin: breakeven ROAS = 1 / contribution margin; target ROAS adds the desired profit [Practitioner consensus].
3. Judge acquisition on new customers (nCAC, aMER), not blended ROAS [Practitioner consensus].
4. Allocate on marginal returns using response curves, budget step tests, lift tests or MMM [Practitioner consensus; MMM tools such as Meridian and Robyn implement this, K].
5. Calibrate MMM with experiments; incrementality beats attribution when they disagree [Practitioner consensus].
6. Keep 10% to 20% of budget for tests at Growth tier and above (70/20/10) [Practitioner consensus].
7. Change budgets in steps of about 20% to avoid resetting automated learning [Practitioner consensus].
8. Use fewer, broader campaigns on automated platforms, with conversion volume high enough to learn (Meta learning phase about 50 events per ad set per week) [Official guidance, K].
9. Maintain a deliberate brand vs performance split and measure brand with share of search, brand lift and geo tests [Study, 2013 to 2021].
10. Run a fixed operating cadence: daily exceptions, weekly learning loop, monthly reallocation, quarterly reset [Practitioner consensus].
11. Feed margin and lead quality into platforms (POAS values, offline conversions) so automation optimizes for profit [Practitioner consensus].
12. Treat geo rules (tax, consent, currency) as inputs to targets, not as afterthoughts [Practitioner consensus].

## 5. Contested topics
| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| 60:40 brand split | IPA data shows long term effects; average best balance near 60:40 B2C | Average of large award entered brands; small brands cannot fund it | Start by tier and stage; ramp with geo tests |
| Full automation (Advantage+, Smart+, PMax, AI Max) | Platforms report better returns (Meta cited $4.52 per $1 for Advantage+ users vs manual, Q2 2026 as reported) | Black box, cannibalizes brand and retargeting, weak controls; marketers say not ready (April 2026) | Use automation with clean signals, exclusions, value rules and incrementality checks |
| Platform reported ROAS | Fast, granular, needed for daily ops | Overstates incrementality, especially view through and retargeting | Use for daily ops; plan budgets on reconciled and incremental numbers |
| MMM for mid size advertisers | Open source tools make it cheap | Needs 2+ years of data and variance; can mislead | Use at Scale tier with lift test calibration; at Growth use step tests |
| ChatGPT ads as a performance channel | Fast growing reach, high intent context, CPC available | Early measurement, limited targeting, reported costs vary widely | Test bucket with holdout or geo read |
| Zero click and SEO investment | Organic clicks shrinking on informational queries | Commercial queries still click; AI assistants cite sites | Shift SEO to commercial and citation worthy content; track AI visibility |
| Turkey withholding gross-up method | Gross up both withholding and VAT on invoice / 0.85 | Gross up withholding only; VAT on invoice amount | Confirm with mali müşavir; plan with the higher cost |

## 6. What top operators do differently
1. They model contribution margin per order, per product and per channel, and they pass margin into bidding.
2. They keep a written response curve or ceiling per channel and update it monthly.
3. They run at least two incrementality tests per year on their largest lines and re-plan on the results.
4. They plan creative supply as a function of spend (concepts per week per $10k) because creative is the scaling constraint on automated platforms.
5. They separate new customer economics from returning customer revenue in every report.
6. They hold a protected test budget and a scored backlog, and they publish losers as well as winners.
7. They plan peaks 8 to 10 weeks ahead with tracking freezes and pacing calendars.
8. They adjust targets for inflation and currency in high inflation markets every month.
9. They limit priorities to a handful and assign each one an owner.
10. They keep platform changes on a monthly watch list and test defaults before accepting them.

## 7. Common expensive mistakes
| Mistake | Why it costs | Prevention |
|---------|-------------|------------|
| Scaling on broken tracking | Algorithms optimize to wrong signals; budgets follow false winners | Measurement gate in every workflow |
| Using revenue ROAS targets without margin | Profitable looking campaigns lose money | Breakeven ROAS from contribution margin |
| Average ROAS allocation | Overfunds saturated channels | Marginal analysis |
| Spreading Starter budgets across many channels | No channel exits learning | Channel count rules |
| Retargeting heavy budgets | High attributed, low incremental return | Caps and holdouts |
| Ignoring taxes and fees on media (Turkey withholding, regulatory fees) | CAC understated by 15% or more | True media cost multiplier |
| Nominal comparisons in high inflation | False alarms about CPC growth | Real or hard currency views |
| Cutting brand when performance dips | Future search demand and nCAC worsen | Brand floor and long term metrics |
| New channel tests below minimum viable budget | Inconclusive results, wasted spend | MVB formula and 8 to 12 week plan |
| Too many priorities | Nothing finishes | Max 5 |

## 7b. Implications for the Ads Master orchestration design
| Finding | Design decision in the growth-orchestrator package |
|---------|-----------------------------------------------------|
| In Claude Code, subagents cannot spawn subagents | The main session is the conductor and loads the growth-orchestrator skill; the growth-orchestrator subagent does single threaded strategy and returns delegation plans |
| Measurement failures are the most common hidden cause of bad decisions | Every multi agent workflow starts with a measurement gate |
| Automation shifts leverage to inputs | Workflows route creative-strategy, commerce-feeds and measurement before scaling |
| Search is fragmenting into AI, retail and social surfaces | AI search program workflow combines seo, ai-search-optimization, chatgpt-ads, commerce-feeds and market-intel |
| New channels launch first in the US and roll out by geo | Channel selection checks geo availability and the geo module before test plans |
| Taxes and inflation distort CAC in some markets | Unit economics module includes a true media cost multiplier and inflation re-basing |
| Many promising channels lack a dedicated agent | Quick guides with a common test template and a procedure to add an agent |

## 7c. Operating system patterns observed among strong teams
- **Single scoreboard:** one page with CM3, MER, nCAC and new customers from backend data, reviewed weekly, with platform data as supporting detail [Practitioner consensus].
- **Written decision log:** each budget move recorded with hypothesis, metric and review date; outcomes reviewed monthly [Practitioner consensus].
- **Explicit ownership:** each KPI node has one owner; cross channel decisions sit with one person or role [Practitioner consensus].
- **Peak readiness rituals:** tracking freeze, feed freeze and promo economics sign off weeks before peak [Practitioner consensus].
- **Quarterly kill list:** channels, campaigns and tests that did not earn their keep are stopped deliberately and documented [Practitioner consensus].

## 8. Benchmarks (use only as priors; vary by vertical, geo, season)
| Benchmark | Value | Source and date | Sample | Caveat |
|-----------|-------|-----------------|--------|--------|
| LTV to CAC target | About 3:1 | Practitioner consensus | n/a | SaaS and subscription origin; ecommerce varies |
| CAC payback | Ecommerce under 6 months; SMB SaaS under 12; enterprise SaaS under 24 | Practitioner consensus | n/a | Depends on cash and financing |
| Experiment win rate | 10% to 30% | Practitioner consensus | n/a | Higher rates often mean weak controls |
| Retargeting share of paid spend | Under 10% to 20% | Practitioner consensus | n/a | Higher for high consideration with long cycles |
| Meta learning phase | About 50 optimization events per ad set within 7 days | Meta Business Help Center (K) | n/a | Re-check current guidance |
| TikTok budget minimums | $50 per day campaign, $20 per day ad group | TikTok Ads Help (K) | n/a | Re-check |
| LinkedIn budget minimum | $10 per day campaign | LinkedIn Help (K) | n/a | Re-check |
| Google daily budget overdelivery | Up to 2x daily, monthly cap about 30.4x average daily | Google Ads Help (K) | n/a | Re-check |
| Zero click share of US Google searches | 68.01% (January to April 2026) vs 60.45% in 2024 | SparkToro via Search Engine Land, 2026 (S) | Clickstream panel | Cannot isolate AI Overviews' share |
| Organic CTR on AI Overview queries | Fell 61% (1.76% to 0.61%) in 2025; partial rebound to 2.36% by February 2026 | Seer Interactive, 2025 to 2026 (S) | 3,119 queries, 42 organizations | Informational queries |
| Position one CTR with AI Overview | Minus 58% | Ahrefs, 2025-12 (S) | 300,000 keywords | Query mix effects |
| ChatGPT ads early pricing | $60 CPM at pilot launch; $3 to $5 suggested starting max CPC (self serve) | Secondary reports, 2026 (S) | n/a | [Unverified]; varies |
| Advantage+ returns | $4.52 per $1, about 22% higher than manual (Meta claim) | Meta Q2 2026 call as reported (S) | Meta internal | Vendor claim; not incrementality |

## 9. Tools, APIs and MCP servers
| Tool | What it does for the orchestrator | Access | Status |
|------|-----------------------------------|--------|--------|
| Google Ads API | Spend, conversions, budgets, experiments, Keyword Planner | Developer token | K |
| Google Ads MCP server (official, open source, read only, released 2025-10) | Read Google Ads data from Claude | Self hosted | K (research/google-ads.md) |
| TikTok for Business MCP server (official, announced May 2026) | TikTok Ads API endpoints as MCP tools | Via partners and developer access | K (research/tiktok-ads.md) |
| Google Analytics Data API and GA4 MCP server | Sessions, conversions, channel groups, AI referrals | OAuth | K [Unverified current scope] |
| Meta Marketing API (Insights) | Spend and results by campaign, breakdowns | App + token | K |
| Community Meta Ads MCP servers | Read Meta Ads data from Claude | Third party; review permissions | K [Unverified] |
| TikTok Business API, LinkedIn Marketing API, Microsoft Advertising API | Channel data | Developer access | K |
| Google Search Console API | Organic trend | OAuth | K |
| BigQuery (and MCP Toolbox for Databases) | Warehouse for blended reporting | GCP | K |
| Meridian (Google), Robyn (Meta) | MMM with response curves and budget optimizer | Open source | K |
| GeoLift (Meta), CausalImpact (Google) | Geo experiments and time series causal inference | Open source | K |
| Spreadsheets and Python | Curves, forecasts, unit economics | Local | n/a |
| Data connectors (Supermetrics, Funnel, Fivetran, Airbyte, Windsor.ai) | Pull platform data into sheets or warehouse | Paid | K |
| Incrementality and MMM vendors (for example Haus, Recast, Measured) | Managed tests and models | Paid | K |
Rules: read only access by default; agents never write to accounts; customer data stays out of version control.

## 10. Official sources to monitor
| Area | Source | Cadence |
|------|--------|---------|
| Market forecasts | WPP Media This Year Next Year (June, December); dentsu Ad Spend (May, December); IAB Outlook (January, September); IAB/PwC revenue report (April) | Semiannual |
| Google | Google Ads Help "What's new", Ads and Commerce Blog, Search Central Blog, Google Marketing Live (May) | Monthly |
| Meta | Meta for Business news, Business Help Center, quarterly earnings | Monthly |
| OpenAI | openai.com news, ChatGPT Ads help center | Monthly |
| TikTok | TikTok Business news, Seller University | Monthly |
| EU | DMA site, DSA pages, EUR-Lex | Quarterly |
| US | IAPP state tracker, FTC press | Quarterly |
| Turkey | Resmî Gazete, GİB, KVKK, TÜİK CPI release (monthly), BDDK | Monthly |
| Gulf | SDAIA (Saudi Arabia), UAE Media Council, TDRA | Quarterly |

## 11. Open questions and watch list
- Does ChatGPT ads performance hold up in incrementality tests outside the US? How do visual ads near image generation perform?
- How many EU users chose Meta's less personalized ads, and what is the measurable effect on CPA? The Commission is monitoring uptake.
- Will Google expand AI Mode ad formats beyond the US in 2026 or 2027, and with which reporting?
- Will Meta ship URL to campaign full automation broadly, and what controls remain?
- How will the 2027 Turkish DST cut to 2.5% change platform pass through fees?
- Will the EU AI Act Article 50 timing change, and how will platforms label AI generated ads?
- New brand vs performance research with a published method in 2025 to 2026 (IPA, WARC, LinkedIn B2B Institute): none verified in this sweep.

## 12. Sources
1. This Year Next Year 2026 Midyear Forecast. WPP Media. https://www.wppmedia.com/news/report-this-year-next-year-midyear-2026 (2026-06) (S)
2. Global Midyear Ad Forecast 2026. WPP Media. https://www.wppmedia.com/thought-leadership/this-year-next-year/midyear-2026 (2026-06) (S)
3. WPP ups global ad spend forecasts to 8.9% on AI gold rush. Mi3. https://www.mi-3.com.au/19-06-2026/industry-dynamics-dont-seem-make-much-sense-wpp-ups-global-ad-spend-forecasts-89-ai-gold (2026-06-19) (S)
4. Ad Spend Growth Is Projected to Slow to 5.0% in 2026. dentsu. https://www.dentsu.com/news-releases/ad-spend-growth-is-projected-to-slow-to-5-percent-in-2026-still-outpacing-economic-growth (2026-05-27) (S)
5. Global Ad Spend Set to Surpass $1 Trillion for the First Time in 2026. dentsu. https://www.dentsu.com/news-releases/global-ad-spend-set-to-surpass-one-trillion-for-the-first-time-in-2026-as-the-algorithmic-era-redefines-growth (2025-12) (S)
6. Ad Spend May 2026. dentsu insight. https://insight.dentsu.com/ad-spend-may-2026/ (2026-05) (S)
7. Dentsu downgrades ad spending forecast. eMarketer. https://www.emarketer.com/content/dentsu-downgrades-ad-spending-forecast-geopolitical-tensions-pressure-growth (2026-05) (S)
8. Magna latest to downgrade global ad spending forecast, expects $979B. Marketing Dive. https://www.marketingdive.com/news/magna-latest-to-downgrade-global-ad-spending-forecast-expects-979b/750871/ (2025-06) (S)
9. IAB/PwC Internet Advertising Revenue Report: Full Year 2025. IAB. https://www.iab.com/insights/internet-advertising-revenue-report-full-year-2025/ (2026-04) (S)
10. IAB Raises 2026 U.S. Ad Spend Forecast to +12.3%. IAB. https://www.iab.com/news/iab-raises-2026-u-s-ad-spend-forecast/ (2026-09) (S)
11. IAB Revises Ad Forecast, Shows Growth For Most Media. MediaPost. https://www.mediapost.com/publications/article/417763/iab-revises-ad-forecast-shows-growth-for-most-med.html (2026-09-10) (S)
12. IAB 2026 Outlook. IAB. https://www.iab.com/insights/2026-outlook/ (2026-01) (S)
13. IAB: CTV, Social, and Commerce Media Will Drive Growth in 2026. AdTechRadar. https://adtechradar.com/2026/01/29/iab-2026-ad-spend-digital-growth-linear-tv-decline/ (2026-01-29) (S)
14. IAB: Retail Commerce Media To Drive $74B Ad Spend In 2026. MediaPost. https://www.mediapost.com/publications/article/407741/iab-forecast-retail-media-to-drive-74b-ad-spend.html (2025) (S)
15. Creator marketing now a core media channel while search slows. Marketing Dive. https://www.marketingdive.com/news/creator-marketing-now-a-core-media-channel-while-search-slows-iab/817832/ (2026) (S)
16. OOH Stands Out, Retail Media To Overtake Total TV Ad Revenue. LBB Online. https://lbbonline.com/news/wpp-media-advertising-forecast-report-2026 (2026-06) (S)
17. Meta Reports Second Quarter 2026 Results. Meta. https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx (2026-07-29) (S)
18. Q2 2026 Earnings Call Transcript. Meta. https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf (2026-07-29) (S)
19. Meta Boosts Advertising In Q2, Tries To Reassure Investors On AI. MediaPost. https://www.mediapost.com/publications/article/416925/meta-boosts-advertising-in-q2-tries-to-reassure-i.html (2026-07-31) (S)
20. How Meta's AI push is changing ad creation. Marketing Brew. https://www.marketingbrew.com/stories/2026/04/07/meta-ai-ad-creation (2026-04-07) (S)
21. Building advertising for the way people use AI. OpenAI. https://openai.com/index/new-chatgpt-ads-format-and-measurement/ (2026) (S)
22. ChatGPT Ads expands to Southeast Asia and Taiwan. OpenAI. https://openai.com/index/chatgpt-ads-expands-southeast-asia-taiwan/ (2026) (S)
23. OpenAI Opens Ad Platform To CPC Bidding, Self-Serve Buys. MediaPost. https://www.mediapost.com/publications/article/414857/openai-opens-ad-platform-to-cpc-bidding-self-serv.html (2026-05-06) (S)
24. OpenAI launches visual ads alongside image generation results. TechCrunch. https://techcrunch.com/2026/10/05/openai-launches-visual-ads-that-appear-alongside-image-generation-results/ (2026-10-05) (S)
25. Where ChatGPT Ads Are Sold: Every Market, Every Date. Digital Applied. https://www.digitalapplied.com/blog/where-chatgpt-ads-are-sold-every-market-and-date (2026) (S)
26. The deal to secure TikTok's future in the US has finally closed. CNN. https://www.cnn.com/2026/01/22/tech/tiktok-us-deal-closes (2026-01-22) (S)
27. TikTok pitches advertisers on bold new chapter under US joint venture. Marketing Dive. https://www.marketingdive.com/news/tiktok-pitches-advertisers-on-bold-new-chapter-under-us-joint-venture/815632/ (2026-03) (S)
28. TikTok Shop Smart Promotion. TikTok Shop Seller University. https://seller-us.tiktok.com/university/essay?knowledge_id=6371753145599758&lang=en (2026) (S)
29. Google quietly expands AI Overview ads to 11 countries. PPC Land. https://ppc.land/google-quietly-expands-ai-overview-ads-to-11-countries-without-fanfare/ (2025-12) (S)
30. Google AI Mode ads: what changed at Marketing Live 2026. Yellowhead. https://www.yellowhead.com/blog/google-ai-mode-ads/ (2026-05) (S)
31. Google zero-click searches reach 68% in early 2026. Search Engine Land. https://searchengineland.com/google-zero-click-searches-2026-study-479717 (2026) (S)
32. Google AI Overview Study: SEO and PPC CTR impact. Seer Interactive. https://www.seerinteractive.com/insights/ctr-aio (2025 to 2026) (S)
33. Pew Research confirms Google AI Overviews is eroding web ecosystem. Search Engine Journal. https://www.searchenginejournal.com/pew-research-confirms-google-ai-overviews-is-eroding-web-ecosystem/551825/ (2025-07) (S)
34. Meta agrees to offer less personalized ad option for EU users. Anadolu Agency. https://www.aa.com.tr/en/europe/meta-agrees-to-offer-less-personalized-ad-option-for-eu-users/3765367 (2025-12) (S)
35. Meta commits to give EU users choice on personalised ads under DMA. EU Reporter. https://www.eureporter.co/business/digital-economy/2025/12/09/meta-commits-to-give-eu-users-choice-on-personalised-ads-under-dma/ (2025-12-09) (S)
36. Meta Platforms Form 10-Q for the quarter ended 30 June 2026. SEC. https://www.sec.gov/Archives/edgar/data/0001326801/000162828026050705/meta-20260630.htm (2026) (S)
37. Ending political, electoral and social issue advertising in the EU. Meta. https://about.fb.com/news/2025/07/ending-political-electoral-and-social-issue-advertising-in-the-eu/ (2025-07) (S)
38. Google to stop showing political ads to users in the European Union. Giga Law. https://giga.law/daily-news/2024/11/15/google-to-stop-showing-political-ads-to-users-in-european-union (2024-11-15) (S)
39. Google Privacy Sandbox officially shuts down. Usercentrics. https://usercentrics.com/knowledge-hub/what-is-google-privacy-sandbox/ (2025) (S)
40. Google drops plans for third-party cookie choice prompt in Chrome. OneTrust. https://www.onetrust.com/blog/google-drops-plans-for-third-party-cookie-choice-prompt-in-chrome/ (2025-04) (S)
41. Dijital hizmet vergisi oranı yeniden belirlendi. Anadolu Ajansı. https://aa.com.tr/tr/ekonomi/dijital-hizmet-vergisi-orani-yeniden-belirlendi/3780348 (2025-12) (S)
42. Dijital Hizmet Vergisi Oranı Düşürüldü: 2026 Yılında Yüzde 5. Alomaliye. https://www.alomaliye.com/2025/12/25/dijital-hizmet-vergisi-orani-dusuruldu-2026-yilinda-yuzde-5-2027-yilinda-yuzde-2-5/ (2025-12-25) (S)
43. Turkey Finalizes Guidance on New Withholding Tax on Online Advertising Services. Thomson Reuters. https://tax.thomsonreuters.com/blog/turkey-finalizes-guidance-on-new-withholding-tax-on-payments-relating-to-online-advertising-services/ (2019) (S)
44. 20% VAT and 15% Withholding Tax for Google and YouTube Advertising Invoices in Türkiye. Karen Audit. https://www.karenaudit.com/en/20-vat-and-15-withholding-tax-should-be-calculated-for-google-and-youtube-advertising-invoices-in-turkiye/ (n.d.) (S)
45. Taxes in your country. Google Ads Help. https://support.google.com/google-ads/answer/2375370?hl=en (ongoing) (S)
46. Meta ve Google Ads Reklam Faturalarında KDV-2 ve Stopaj. Celikel CPA. https://celikelcpa.com/tr/blog/sosyal-medya-reklam-giderleri-meta-google-kdv-2-tevkifati/ (n.d.) (S)
47. Regulation (EU) 2024/900 on transparency and targeting of political advertising. EUR-Lex. https://eur-lex.europa.eu/eli/reg/2024/900/oj (2024-03) (K)
48. US State Privacy Legislation Tracker. IAPP. https://iapp.org/resources/article/us-state-privacy-legislation-tracker/ (ongoing) (K)
49. Meridian. Google. https://developers.google.com/meridian (2025-01 GA) (K)
50. Robyn. Meta. https://facebookexperimental.github.io/Robyn/ (ongoing) (K)
51. GeoLift. Meta. https://github.com/facebookincubator/GeoLift (ongoing) (K)
52. IPA effectiveness publications (Binet and Field). IPA. https://ipa.co.uk/ (2013 to 2018) (K)
53. LinkedIn B2B Institute research (5 Principles of Growth in B2B, 95:5 Rule). LinkedIn. https://business.linkedin.com/marketing-solutions/b2b-institute (2019, 2021) (K)
54. KVKK. Personal Data Protection Authority. https://www.kvkk.gov.tr/ (ongoing) (K)
55. Turkey Plans Gradual Reduction of Digital Services Tax to 2.5% by 2027. VATupdate. https://www.vatupdate.com/2026/01/07/turkey-plans-gradual-reduction-of-digital-services-tax-to-2-5-by-2027/ (2026-01-07) (S)
56. Dijital Hizmet Vergisi Uygulama Genel Tebliği. Resmî Gazete. https://resmigazete.gov.tr/eskiler/2020/03/20200320-4.htm (2020-03-20) (S)
57. Insight: Taxation of Turkey's Digital Economy. Bloomberg Tax. https://news.bloombergtax.com/daily-tax-report-international/insight-taxation-of-turkeys-digital-economy (n.d.) (S)
58. Meta's 2026 DMA report reveals WhatsApp ads, a EUR 200m fine and a defiant stance on personalized advertising. PPC Land. https://ppc.land/metas-2026-dma-report-reveals-whatsapp-ads-a-eu200m-fine-and-a-defiant-stance-on-personalized-advertising/ (2026) (S)
59. Meta to stop selling political ads in the EU from October. TechCrunch. https://techcrunch.com/2025/07/25/meta-to-stop-selling-political-ads-in-the-eu-from-october (2025-07-25) (S)
60. AI Overviews Cut CTR by 23.1% in France. Ahrefs. https://ahrefs.com/blog/ai-overviews-france-impact/ (2026) (S)
61. New data: Google AI Overviews are hurting click-through rates. Search Engine Land. https://searchengineland.com/google-ai-overviews-hurt-click-through-rates-454428 (2025) (S)
62. AI Mode is now available in more languages and locations. Google. https://blog.google/products-and-platforms/products/search/ai-mode-expands-languages-locations/ (2025) (S)
63. Google Expands Ads In AI Overviews To More Countries. Search Engine Roundtable. https://www.seroundtable.com/google-expands-ads-in-ai-overviews-40629.html (2025-12) (S)
64. TikTok opens ad network of nearly 400,000 apps to US advertisers. PPC Land. https://ppc.land/tiktok-opens-ad-network-of-nearly-400-000-apps-to-us-advertisers (2026) (S)
65. TikTok's US overhaul gives advertisers greater certainty, though questions remain. eMarketer. https://www.emarketer.com/content/tiktok-s-us-overhaul-gives-advertisers-greater-certainty--though-questions-remain (2026) (S)
66. Meta could overtake Google search ad revenue in 2026, Bernstein says. TradingView. https://www.tradingview.com/news/stocktwits:29919a030094b:0-meta-could-overtake-google-search-ad-revenue-in-2026-bernstein-says-ai-is-driving-the-shift/ (2026) (S)
67. Dentsu: Global Events to Send Ad Spending Past $1 Trillion for the First Time in 2026. ANA. https://www.ana.net/magazines/show/id/news-2025-12-04-dentsu-global-ad-spend (2025-12-04) (S)
68. Digital Markets Act. European Commission. https://digital-markets-act.ec.europa.eu/ (ongoing) (K)
69. Regulation (EU) 2022/2065 (Digital Services Act). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2022/2065/oj (2022-10) (K)
70. Ehrenberg-Bass Institute for Marketing Science. https://marketingscience.info/ (ongoing) (K)
