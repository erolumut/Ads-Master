---
name: market-intel
description: Competitor and market intelligence playbook for paid media, SEO and AI search. Use to research competitors in Meta Ad Library and its API, Google Ads Transparency Center, TikTok Creative Center Top Ads and the TikTok Ad Library, LinkedIn Ad Library and Microsoft Ad Library; run SEO and paid search competitive analysis (Ahrefs, Semrush, Similarweb, SpyFu, Auction Insights); benchmark AI visibility of competitors in ChatGPT, Gemini, AI Overviews, AI Mode, Perplexity and Copilot; monitor offers and prices; mine reviews (G2, Trustpilot, Amazon, app stores), Reddit and social listening for voice of customer; research demand with Google Trends and keyword volumes; size markets (TAM, SAM, SOM); build positioning maps and win and loss analysis; set monitoring cadence and alerts within legal and ethical limits.
---

# Market Intelligence

> Knowledge as of 2026-10. Ad libraries, tool data sources and API access change often. Run the Freshness Protocol before relying on any library feature, API field, tool metric or legal limit.

## Mission and scope
Turn public and licensed market signals into decisions other agents act on: angles and hooks (creative-strategy), keywords and auction tactics (google-ads, microsoft-ads), content and links (seo), prompts and citations (ai-search-optimization), offers and prices (growth-orchestrator, cro), and market entry and channel headroom (growth-orchestrator).

In scope: competitor ad intelligence, search and SEO competition, AI visibility benchmarking, offer and pricing monitoring, positioning, voice of customer mining, demand and trend research, market sizing, win and loss analysis, monitoring and alerts.
Out of scope: changing live accounts or pages, buying data of unclear origin, any collection that breaches terms of service or privacy law.

## Intake (minimum facts; where they live)
| # | Fact | Where in ads-master/ | Cold start question |
|---|------|----------------------|---------------------|
| 1 | What we sell, to whom, price points | PROJECT_BRIEF.md 1, 2 | What do you sell and at what price? |
| 2 | Markets and languages | PROJECT_BRIEF.md 1 | Which countries and languages matter? |
| 3 | Named competitors (direct, indirect, alternatives) | COMPETITORS.md | Who do customers compare you with, and what do they use instead? |
| 4 | Brand and competitor domains and brand names | COMPETITORS.md | Websites and brand names to track |
| 5 | Decision this research serves | Task brief, PRIORITIES.md | What decision will this research change? |
| 6 | Segments and known pains | AUDIENCE.md | Who are the main customer segments? |
| 7 | Tools and connectors available | PROJECT_BRIEF.md 7 | Do you have Semrush, Ahrefs, Similarweb, an AI visibility tool, or API keys? |

If `ads-master/` is missing: ask these in one message or suggest `ads-setup`. With only items 1 to 3 you can deliver a first competitive baseline from public sources.

## Operating protocol
1. **Frame the decision.** Write: "This research informs <decision> for <owner slug> by <date>." List the 3 to 7 questions that decide it.
2. **Load state.** COMPETITORS.md, AUDIENCE.md, BRAND.md, memory, last outputs. Note what changed since the last report.
3. **Pick sources** from the Task router. Prefer official signals (ad libraries, Auction Insights, Merchant Center benchmarks, Search Console, Google Trends) over third party estimates.
4. **Collect** with capture dates, market, language and URLs. Respect terms of service and rate limits ([Tools, APIs and MCP](references/tools-api-mcp.md) legal notes).
5. **Code and count.** Use the coding frames in each module (angle taxonomy, VoC themes, offer components). Report counts and sample sizes.
6. **Triangulate** every estimate with a second source or an official signal. Label confidence: high (official or measured), medium (two consistent estimates), low (single estimate).
7. **Analyze.** Separate observation, inference, recommendation. Find gaps we can own.
8. **Recommend** with a "so what", an owner slug, expected impact and a test where possible (EXPERIMENTS.md row).
9. **Deliver** with the [Output templates](references/output-templates.md). Propose edits to COMPETITORS.md and AUDIENCE.md through the journal.
10. **Set monitoring** for anything that needs follow up ([Monitoring cadence and alerts](references/monitoring-cadence-and-alerts.md)).
11. **Log** journal entry, memory only for confirmed patterns.

## Intelligence questions by consumer
| Consumer (slug) | Questions market-intel answers |
|-----------------|--------------------------------|
| creative-strategy | Which angles, hooks, formats and offers do competitors run and keep running? Which customer pains and phrases appear most? What is nobody saying? |
| google-ads, microsoft-ads | Who enters our auctions, on which terms, with which copy and offers? Who bids on our brand? Where is impression share lost to competitors? |
| meta-ads, tiktok-ads, linkedin-ads | What creative volume and cadence do competitors run? Which formats dominate? What landing pages do they use? |
| chatgpt-ads | Which competitors advertise in ChatGPT or other assistants, in which contexts? |
| seo | Which keywords and topics do competitors win? Which SERP features and backlinks? |
| ai-search-optimization | Which brands do AI assistants mention and recommend for our prompts? Which sources do they cite? |
| cro | How do competitor pages, offers, guarantees and checkout flows compare? |
| commerce-feeds | How competitive are our prices in Shopping? What titles and promotions do competitors use? |
| growth-orchestrator | How big is the market and our share? Where is demand growing? What is the price corridor? Which markets or channels have headroom? |

## Defining the competitor set
Keep four lists in COMPETITORS.md (propose edits through the journal):
| List | Definition | How to find it |
|------|-----------|----------------|
| Direct | Same product, same customer, same price band | Customer interviews, reviews ("we switched from"), sales notes |
| Search competitors | Domains that win our money keywords (paid and organic) | Auction Insights, SEO tools organic competitors report, SERP sampling |
| AI competitors | Brands that AI assistants mention or recommend for our prompts | AI visibility benchmark |
| Alternatives and substitutes | Other ways to get the job done (DIY, spreadsheets, agencies, doing nothing, marketplaces) | VoC "what did you use before", JTBD interviews |
Review the set quarterly. A brand that appears in two lists is a priority competitor.

## Ad transparency availability by region (summary)
| Library | Outside EU and UK | EU (DSA) and UK | Notes |
|---------|-------------------|-----------------|-------|
| Meta Ad Library | Active ads only, creative and start date; political and issue ads archived with spend ranges | All ads incl. inactive for one year after last impression, with reach and targeting summaries for EU delivered ads; no new EU political or issue ads since 2025-10-06 [Official, DSA era] | API returns EU delivered ads and political or issue ads; requires identity confirmation (government ID, proof of residence) and ads_read |
| Google Ads Transparency Center | Ads by advertiser or domain, region, format, date; legal name and verification badge; inactive creatives for up to about 13 months; no spend or performance | Ads from unverified advertisers also shown in Europe and Türkiye; impression ranges published with a delay; EU political ad history removed around 2025-09 [Secondary, 2026] | No official API for commercial ads; political ads BigQuery dataset only [Practitioner consensus] |
| TikTok Creative Center (Top Ads) | High performing ads by region, industry, objective | Same | Inspiration tool, curated; not a full library |
| TikTok Ad Library (Commercial Content Library) | Limited | Ads shown in the EU (plus UK and Switzerland) with targeting and reach information | Commercial Content API on application; eligibility reported as researcher focused [Contested] |
| LinkedIn Ad Library | Ads run after 2023-06-01, kept one year after last impression; search by company, payer, keyword, country, date | EU served ads add impression ranges, impressions by country and targeting categories used (not the values chosen); no spend or results [Official, LinkedIn Help] | No public API |
| Microsoft Ad Library | None | Ads served on Bing in the EU and EEA (any advertiser location), searchable by ad content or advertiser, filter by date and country; advertiser name and location, payer [Official, Microsoft Advertising Help] | Public Ad Library API, no sign-up; targeting categories gender, age, location, Microsoft audiences, advertiser audiences |
Details, fields and API calls: [Competitor ad intelligence](references/competitor-ad-intelligence.md).

## Coding frames (quick reference)
| Frame | Codes |
|-------|-------|
| Angle | Pain or problem, desired outcome, identity or aspiration, social proof, authority or expert, comparison or us vs them, price or value, urgency or scarcity, novelty or mechanism, risk reversal or guarantee, founder or story, education |
| Format | Static image, carousel, short video under 15s, video 15 to 60s, long video, UGC, creator, founder to camera, demo, before and after (check policy), meme or native, catalog or dynamic, document or lead form |
| Offer component | Price, discount depth, bundle, free shipping threshold, trial length, guarantee, financing or installments, bonus, gift, subscription terms, urgency device |
| VoC theme | Trigger, pain, desired outcome, objection, anxiety, alternative considered, decision criterion, delight, disappointment, exact phrase |
| Funnel stage of ad | Unaware, problem aware, solution aware, product aware, most aware |

## Confidence labels for every number
| Label | Use when | Example |
|-------|----------|---------|
| High | Official or first-party measurement | Auction Insights overlap rate, ad library ad count, Search Console clicks |
| Medium | Two independent estimates agree within about 30% | Semrush and Similarweb traffic estimates for a competitor |
| Low | Single third party estimate or small sample | One tool's paid keyword spend estimate |

## Local and regional sources worth adding
| Market | Sources |
|--------|---------|
| Turkey | Şikayetvar (complaints), marketplace reviews and Q and A (Trendyol, Hepsiburada, Amazon.com.tr), Google Trends TR, KAP filings for listed companies, Ekşi Sözlük for sentiment (public pages only) |
| MENA and GCC | Noon and Amazon.sa or .ae reviews, Arabic social listening, Snapchat and TikTok Creative Center by region |
| EU | DSA ad repositories with targeting data, Trustpilot, national comparison sites |
| US | G2, Capterra, Amazon reviews, Reddit, BBB, app stores |

## Adaptation matrix
| Model | Starter (under $3k) | Growth ($3k to $30k) | Scale ($30k to $300k) | Enterprise (over $300k) | Primary sources |
|-------|---------------------|----------------------|------------------------|--------------------------|-----------------|
| Ecommerce | Top 3 competitors: ad libraries, prices, top reviews; quarterly | Top 5 to 8; monthly ad and price monitoring; Merchant Center price competitiveness | Automated price tracking, ad library API pulls (EU), share of search, AI shopping visibility | Category share models, retail media and marketplace intel per market | Meta Ad Library, Google Transparency Center, Merchant Center, Amazon and marketplace pages, reviews |
| Lead gen | Search competitors via Auction Insights and SERP checks | Landing page and offer teardowns, call tracking of competitors not allowed (use public info only) | Local market share of search, review velocity | Multi region intel | Auction Insights, Google Business Profiles, review sites |
| B2B SaaS | G2 or Capterra review mining of top 3; pricing pages | Win and loss interviews, LinkedIn Ad Library, comparison pages | AI visibility benchmark, analyst and community share of voice | Full competitive program with battlecards | G2, Capterra, TrustRadius, LinkedIn Ad Library, Reddit, pricing pages |
| Local services | Google Maps pack competitors, reviews | Offer and price comparison, Local Services Ads presence | Multi location benchmarks | Franchise level | Google Business Profile, Maps, review sites |
| App | App store pages and reviews; Apple Ads competitor presence | TikTok Creative Center Top Ads; Meta Ad Library | Store ranking trackers, creative volume | Global market by market | App Store, Google Play, Creative Center |
| Marketplace or publisher | Supply and demand side competitors | Traffic and channel mix estimates | Category share | Market by market | Similarweb, SEO tools, ad libraries |

Maturity overlay:
| Maturity | Focus |
|----------|-------|
| New account or market | Full baseline: competitors, offers, prices, VoC, demand, positioning map |
| Running | Monthly movement summary plus alerts |
| Plateau | Deep dives: win and loss, VoC refresh, AI visibility, new competitor discovery |
| Scaling | Headroom research: market size, new segments, new geos, channel saturation signals |

## Fast recipes (when time is short)
**Ad library teardown in 30 minutes (one competitor)**
1. Meta Ad Library: country = main market, advertiser = competitor page, active ads. Count active ads, note the oldest start dates, group by concept.
2. Google Ads Transparency Center: search the domain, region = main market, last 30 days; note formats and text ad themes.
3. TikTok Creative Center Top Ads (industry and region) and the TikTok Ad Library if EU; LinkedIn Ad Library for B2B.
4. Code each concept with the angle, format and offer frames. Mark ads older than 30 days and concepts with 3+ variants.
5. Visit the top 3 landing pages; note offer, price, guarantee, proof.
6. Write: what they push, what they keep running, what is missing, 3 recommendations with owners.

**Share of search in 15 minutes**
1. Google Trends: our brand and up to 4 competitor brand terms, market, past 5 years, category filter if ambiguous.
2. Export; compute each brand's share of the total per month; plot 12 month rolling average.
3. Cross check absolute volumes with Keyword Planner ranges or Search Console brand impressions.
4. Report share and trend; flag a 2 point or larger drop over two quarters.

**Price corridor in 20 minutes (ecommerce)**
1. Pick 10 hero SKUs or close equivalents. Capture competitor prices, shipping, discount and installment terms with date and URL.
2. Add Merchant Center price competitiveness data if available.
3. Compute our price index (our price / median competitor price x 100) per SKU.
4. Flag SKUs over 110 or under 90; hand to growth-orchestrator with margin impact.

**AI visibility quick check in 30 minutes**
1. Take 10 priority prompts (category, best for use case, comparison, problem).
2. Run each 3 times in ChatGPT, Gemini or AI Mode, Perplexity and Copilot (logged out where possible), same market.
3. Record brands mentioned, order, recommendation, and cited domains.
4. Compute mention rate and recommendation rate per brand; list top cited domains; hand to ai-search-optimization.

## Task router
| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Competitor ad teardown (Meta, Google, TikTok, LinkedIn, Microsoft) | [Competitor ad intelligence](references/competitor-ad-intelligence.md), [Tools, APIs and MCP](references/tools-api-mcp.md) | Ad library teardown |
| Search and SEO gaps, brand bidding, auction entrants | [Search and SEO competitive analysis](references/search-and-seo-competitive-analysis.md) | Search competition report |
| AI assistant visibility benchmark | [AI visibility benchmarking](references/ai-visibility-benchmarking.md) | AI visibility benchmark |
| Offer, pricing, positioning, win and loss | [Offer, pricing and positioning](references/offer-pricing-and-positioning.md) | Offer matrix, positioning map, win and loss report |
| Voice of customer from reviews, Reddit, social, support | [Voice of customer mining](references/voice-of-customer-mining.md) | VoC report |
| Demand, trends, seasonality, share of search | [Demand and trend research](references/demand-and-trend-research.md) | Demand report |
| TAM, SAM, SOM, market entry | [Market sizing](references/market-sizing.md) | Market sizing |
| Monitoring and alerts setup | [Monitoring cadence and alerts](references/monitoring-cadence-and-alerts.md) | Monitoring plan, monthly movement summary |
| End to end plays (baseline, launch intel, promo response, AI loss) | [Playbooks](references/playbooks.md) | Per play |
| Audit the intelligence program | [Audit checklist](references/audit-checklist.md) | AUDIT_REPORT.md |
| Tools, APIs, MCP servers, legal limits | [Tools, APIs and MCP](references/tools-api-mcp.md) | n/a |
| Sources and dates | [Sources](references/sources.md) | n/a |

## The laws
1. Research serves a decision; name it first or do not start.
2. Public and licensed data only; terms of service and privacy law are hard limits, not suggestions.
3. Official signals beat estimates: Auction Insights, ad libraries, Merchant Center benchmarks, Search Console and Google Trends outrank third party traffic guesses.
4. Triangulate every estimate; label confidence high, medium or low.
5. Capture date, market, language and URL on every data point; markets move daily.
6. Observation, inference and recommendation are separate lines.
7. Count, then conclude: frequencies and sample sizes, not anecdotes.
8. Ad longevity and iteration volume suggest profitability; they do not prove it.
9. Copying a competitor's ad copies their positioning; find the gap instead.
10. Verbatim customer language is the most valuable output; keep it exact and anonymized.
11. AI assistant answers are probabilistic; sample repeatedly across engines and regions.
12. Share of search is a cheap leading indicator of market share; track it monthly.
13. Report change first; static profiles go to the appendix.
14. Every insight has an owner slug and, where possible, a test.
15. Prices and promotions need daily or weekly capture during peaks; monthly is enough otherwise.
16. Competitor trademarks and comparative claims go through platform policy and legal checks before use.
17. Delete raw personal data you do not need; store coded themes and anonymized quotes.
18. Keep the competitor set current: add new entrants from auctions, ad libraries and AI answers each quarter.

## Diagnostics (symptom, likely causes, checks, fixes)
| Symptom | Likely causes | Checks | Fix and owner |
|---------|---------------|--------|---------------|
| CPCs jump on core terms | New auction entrant, competitor promo, broad match expansion by rivals | Auction Insights week over week, ad copy in SERP and Transparency Center | Alert google-ads; adjust bids or terms; offer response |
| Brand search CPC rising | Competitor or affiliate bidding on brand | Auction Insights on brand campaign, SERP checks by geo | google-ads trademark complaint where eligible, affiliate terms, brand defense |
| Meta or TikTok CPA rising with no internal cause | Competitor creative surge or big promo, seasonal CPM rise | Ad library counts by advertiser, new ads per week, promo copy | creative-strategy response; growth-orchestrator promo economics |
| Conversion rate drop with stable traffic | Competitor price cut or better offer | Price tracking, offer matrix | cro and growth-orchestrator |
| Organic clicks falling | AI Overviews, competitor content, SERP features | GSC, SERP feature tracking, competitor content gap | seo, ai-search-optimization |
| AI assistants recommend competitors | Competitors cited by sources AI trusts (reviews, Reddit, comparison sites) | AI visibility benchmark, cited domains | ai-search-optimization |
| Reviews mention a new competitor | Market entry | Review mining, ad libraries, search volume of their brand | Add to COMPETITORS.md proposal |
| Leads say "too expensive" more often | Price corridor shift or value gap | Win and loss, price monitoring | growth-orchestrator, cro |

## Cadence
| When | What | Output |
|------|------|--------|
| Weekly (Scale and above, or during peaks) | Price and promo checks, auction entrants, ad volume spikes | Alerts in journal |
| Monthly | Movement summary: new offers, ads, prices, rankings, AI recommendations, reviews, share of search | `_monthly-movement.md` |
| Quarterly | Landscape refresh: competitor profiles, positioning map, VoC refresh, AI visibility benchmark, market size update, competitor set review | `_competitive-landscape-<YYYY-QN>.md` |
| Event driven | Launch intel, competitor launch, pricing change, new market | Per play |

## Guardrails and approvals
- Read only. Never change accounts, pages, bids or budgets. Recommendations become change requests owned by the executing agent.
- Legal and ethical limits (details in [Tools, APIs and MCP](references/tools-api-mcp.md)): no scraping behind logins, no bypassing technical barriers, no fake accounts or misrepresentation, respect robots rules and rate limits, comply with GDPR, KVKK and similar laws for any personal data, no requests for confidential information from competitor staff, no sharing of competitively sensitive data with competitors (competition law).
- Paid tools and API keys are used only when the human has provided them; costs above the agreed tool budget need approval.
- Comparative advertising and trademark use: check platform trademark policies and local law before recommending; claims go into BRAND.md only after human approval.

## Quality bar (check before delivering)
- [ ] Decision served is named; recommendations map to it.
- [ ] Every data point has source, capture date, market and language.
- [ ] Estimates triangulated and labeled with confidence.
- [ ] Counts and sample sizes reported for VoC and ad analyses.
- [ ] Observation, inference, recommendation separated.
- [ ] "What changed since last report" section present.
- [ ] Each recommendation has an owner slug and expected impact; testable ones have an EXPERIMENTS.md row.
- [ ] No personal data beyond need; quotes anonymized.
- [ ] Legal and ToS checks noted for any automated collection.

## Outputs
- Path: `ads-master/outputs/market-intel/YYYY-MM-DD_market-intel_<description>.md`. Never overwrite.
- Common descriptions: `competitive-baseline`, `ad-library-teardown-<competitor>`, `search-competition`, `ai-visibility-benchmark`, `offer-pricing-matrix`, `positioning-map`, `voc-<segment>`, `demand-<topic>`, `market-sizing-<market>`, `win-loss-<quarter>`, `monthly-movement`, `competitive-landscape-<YYYY-QN>`, `launch-intel-<product>`, `market-entry-<geo>`.
- Required sections: Summary, Decision served, Data used, What changed, Findings (observation, inference, recommendation, owner), Proposals for approval (COMPETITORS.md, AUDIENCE.md, BRAND.md edits; experiments), Handoffs requested.

## Freshness protocol
Check before relying on a feature or source; log changes in the monthly movement summary and the journal.
| Source | What to verify | Where |
|--------|----------------|-------|
| Meta Ad Library and API | Which ads are visible by region, EU data fields, API access requirements and version | facebook.com/ads/library, Ad Library API docs, Meta Transparency Center |
| Google Ads Transparency Center | Filters, regions, EU details, data downloads | adstransparency.google.com and its help pages |
| TikTok Creative Center and Ad Library | Top Ads filters and metrics, Commercial Content Library coverage, research API access | ads.tiktok.com/business/creativecenter, library.tiktok.com |
| LinkedIn Ad Library | Search filters, EU targeting fields, retention | linkedin.com/ad-library |
| Microsoft Ad Library | Coverage and fields | adlibrary.ads.microsoft.com |
| SEO tools (Ahrefs, Semrush, Similarweb, SpyFu) | Data source changes, database size, AI features, API units, MCP availability | Vendor changelogs |
| AI visibility tools | Engines covered, sampling method, prompt volume data | Vendor docs |
| Google Trends | API access status, data changes | Google Trends help, Search Central blog |
| Legal | Platform terms, scraping case law, GDPR and KVKK guidance | Platform terms pages, regulators |

## Reference index
- [Competitor ad intelligence](references/competitor-ad-intelligence.md): every ad library, what it shows by region, API pulls, teardown method, angle taxonomy, longevity heuristics.
- [Search and SEO competitive analysis](references/search-and-seo-competitive-analysis.md): Auction Insights, paid and organic gaps, brand bidding, SERP and AI Overview presence, tool accuracy.
- [AI visibility benchmarking](references/ai-visibility-benchmarking.md): prompt sets, sampling, metrics, citation source analysis, tools.
- [Offer, pricing and positioning](references/offer-pricing-and-positioning.md): offer teardown, price monitoring, positioning maps, messaging, win and loss.
- [Voice of customer mining](references/voice-of-customer-mining.md): sources, collection rules, coding frame, quantification, outputs.
- [Demand and trend research](references/demand-and-trend-research.md): Google Trends, keyword volumes, seasonality index, share of search, trend validation.
- [Market sizing](references/market-sizing.md): TAM, SAM, SOM top down and bottom up, worked examples, channel headroom.
- [Monitoring cadence and alerts](references/monitoring-cadence-and-alerts.md): what to monitor, thresholds, tooling, monthly summary.
- [Tools, APIs and MCP](references/tools-api-mcp.md): tool and API catalog, example calls, MCP servers, legal and ethical limits, resilient and polite collection (challenge detection, request budgets, source lineage).
- [Output templates](references/output-templates.md): templates for every deliverable.
- [Playbooks](references/playbooks.md): end to end plays.
- [Audit checklist](references/audit-checklist.md): scored audit of the intelligence program.
- [Sources](references/sources.md): annotated sources with dates.
