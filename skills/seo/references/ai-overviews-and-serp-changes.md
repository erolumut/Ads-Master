# AI Overviews, AI Mode and SERP Changes

> Scope: how Google's AI features work for site owners, what the data says about clicks, how Search Console and GA4 report them, the 2026 opt-out decision, the num=100 change, other SERP layout changes, and how to adapt strategy and measurement. Getting cited and recommended inside AI answers (GEO, prompt tracking, non-Google assistants) belongs to ai-search-optimization; this file covers the overlap and the handoff.

## 1. Timeline of Google AI search features
| Date | Event | Label |
|------|-------|-------|
| 2024-05 | AI Overviews launched in the US | [Official] |
| 2024-10 | AI Overviews expanded to 100+ countries | [Official] |
| 2025-03 | AI Overviews on Gemini 2.0; AI Mode announced as a Labs experiment | [Official, 2025-03] |
| 2025-05-20 | AI Mode available to all US users (Google I/O 2025); AI Overviews in 200+ countries and 40+ languages | [Official, 2025-05] |
| 2025-05 | Google publishes guidance on succeeding in AI search experiences: same fundamentals, no special optimization required | [Official, 2025-05] |
| 2025-06 | AI Mode clicks, impressions and positions counted in Search Console Performance (web search type) | [Official, 2025-06] |
| 2025-07 | Google reports AI Overviews at 2 billion+ monthly users and AI Mode at 100 million+ monthly active users in the US and India (Q2 earnings) | [Official, 2025-07] |
| 2025-08 | Google says total organic click volume is relatively stable year over year and click quality is higher (Search blog) | [Official, 2025-08]; disputed by publisher data |
| 2025-08 to 2025-10 | AI Mode expands: 180+ countries in English, then 40+ more countries and 35+ languages on 2025-10-07 | [Official, 2025-10] |
| 2025-11 | Gemini 3 in AI Mode | [Unverified exact date] |
| 2025-12 | Generative AI features appear in Discover | [Unverified, reported by industry roundups] |
| 2026-01 | AI Overviews moved to Gemini 3 globally | [Unverified, secondary report] |
| 2026-05-19 | Google I/O 2026: AI Overviews reported at about 2.5 billion monthly users and AI Mode at about 1 billion | [Unverified, secondary reports of Google figures] |
| 2026-06-02 to 2026-06-03 | Search Console "Search generative AI" setting to exclude a site from AI Overviews, AI Mode and Discover AI features; Generative AI performance reports (impressions) launched to a subset of sites first | [Official, 2026-06]; later worldwide rollout reported by Search Engine Journal, status [Contested] |
| 2026-06-03 | UK CMA imposed its first conduct requirement on Google (publisher controls); substantive obligations in force 2026-12-03 | [Unverified, secondary reports] |

## 2. How AI features select and show content [Official, AI features and your website]
- No special markup or "AI optimization" is required. A page must be indexed and eligible to show a snippet. Standard SEO best practices apply.
- AI Overviews and AI Mode may use query fan-out: issuing multiple related searches across subtopics to find supporting pages. Pages can be cited for sub-questions they answer well even if they do not rank top 10 for the main query.
- Links appear in several formats (inline citations, link cards, source lists). Formats change often.
- Controls:
| Control | Effect on AI features | Effect on classic results |
|---------|----------------------|---------------------------|
| `noindex` | Excluded | Excluded |
| `nosnippet` | Excluded from AI Overviews and AI Mode as a source | No text snippet; lower CTR |
| `data-nosnippet` on sections | Those sections not used | Those sections not used in snippets |
| `max-snippet:[n]` | Limits text usable | Limits snippet |
| Search Console "Search generative AI" setting set to Exclude (2026) | Site content not used for AI Overviews, AI Mode and Discover AI features; site receives no AI feature impressions or clicks | Google states no ranking impact on classic results |
| `Google-Extended` in robots.txt | Does not affect AI Overviews or AI Mode; controls Gemini training and grounding outside Search | None |
| Blocking Googlebot | Excluded | Excluded from Search entirely |

## 3. What the click data says
All studies below measure correlation, use different samples and periods, and mostly cover informational queries. Use them for direction and scenario ranges, then build your own curves.

| Study | Date | Sample | Finding | Caveat |
|-------|------|--------|---------|--------|
| Pew Research Center | Published 2025-07-22 (data March 2025) | 900 US adults, 68,879 Google searches | Users clicked a traditional result in 8% of visits when an AI summary appeared vs 15% without; clicks on links inside the summary in about 1% of visits; sessions ended on the results page 26% vs 16% | Browsing panel, one month, AI Overviews only (not AI Mode) |
| Ahrefs | 2025-04 | 300,000 keywords (150k with AIO, 150k informational without), GSC data March 2024 vs March 2025 | Position 1 CTR about 34.5% lower when an AI Overview is present | Correlation; informational only |
| Ahrefs update | Published 2026-02 (data December 2025) | Same method, December 2023 vs December 2025 | About 58% lower CTR for the top ranking page with AIO; reported declines of about 51% at position 2, 46% at 3, 33% at 5, 19% at 10 | Secondary coverage of figures; verify on Ahrefs |
| Amsive | 2025-04 | 700,000 keywords across 10 sites, 5 industries; 10,000 AIO triggering keywords | Average CTR down about 15.5% with AIO; non-branded down about 20%; branded keywords with AIO up about 18.7%; positions below top 3 down about 27%; up to about 37% down when a featured snippet also appears | Small site set |
| Seer Interactive v2 | 2025-11 (data June 2024 to September 2025) | 3,119 informational queries, 42 organizations | Organic CTR on AIO queries down 61% (1.76% to 0.61%); paid CTR down 68%; non-AIO queries also down 41% year over year; brands cited in AIO earned 35% more organic clicks | Seer's own page reports different baselines; causality of citation not proven |
| Seer Interactive v3 | 2026-04-24 (data January 2025 to February 2026) | 5.47 million queries, 53 brands | Organic CTR on AIO SERPs rebounded from about 1.3% (December 2025) to 2.4% (February 2026), still below non-AIO; cited pages get about 120% more clicks per impression than uncited, still about 38% below no-AIO SERPs | Two months of rebound; Seer calls it leveling off, not recovery |
| Similarweb | 2025-07 (data May 2025) | News related searches | Zero-click share for news searches 69% vs 56% a year earlier; organic visits to news sites fell from over 2.3 billion (mid-2024 peak) to under 1.7 billion | News only; modeled panel data |
| Search Engine Land analysis of num=100 effect (Tyler Gargula, LOCOMOTIVE) | 2025-09 | 319 properties | 87.7% of sites lost impressions; 77.6% lost unique queries | Measurement change, not traffic change |

Google's counter position: total organic clicks relatively stable and higher quality clicks (August 2025). Publisher and third party data disagree [Contested].

Practical takeaways:
1. Expect fewer clicks per impression on informational queries with AI Overviews; the size ranges from about 15% to over 60% depending on query class, brand and position.
2. Branded and commercial queries are far less affected; some branded queries gained CTR in the Amsive sample.
3. Being cited helps relative to not being cited but rarely restores pre-AIO CTR.
4. Your own data beats any study: build CTR curves by AIO presence from your Search Console and rank tracker data.

## 4. How reporting works
Search Console Performance report [Official, Search Console help on AI features]:
- AI Overviews: a link in an AI Overview gets the position of the AI Overview block on the page; all links in the same overview share that position. Impressions follow the standard rule (the link must be visible, which can require expanding the overview). Clicks on links in the overview count as clicks.
- AI Mode: counted in the web search type since June 2025. Follow-up questions are new queries. Standard impression and click rules apply.
- No filter in the main Performance report isolates AI Overviews or AI Mode.
- Generative AI performance report (beta, from 2026-06-03): impressions only, for Search (AI Overviews and AI Mode) and Discover, by page, country, device (Search only) and date (hourly, daily, weekly, monthly). No clicks, CTR, position or queries at launch; data backfilled to about 2026-05-18; these impressions are already part of the overall totals [Official, 2026-06; details from secondary coverage]. Whether AI Mode and AI Overview impressions are shown separately is reported inconsistently, and API access was not available at launch [Contested; check your property].

GA4:
- Clicks from AI Overviews and AI Mode arrive as `google / organic`. There is no reliable referrer distinction.
- Browsers hide text fragment directives (`#:~:text=`) from page scripts, so fragment based detection is unreliable; do not build reporting on it.
- Track AI assistants (chatgpt.com, perplexity.ai, copilot, gemini.google.com) as a custom channel group: hand to measurement and ai-search-optimization.

Bing: Bing Webmaster Tools AI Performance (public preview since 2026-02-10) reports citations in Copilot and Bing AI answers: total citations, average cited pages per day, and grounding queries (retrieval phrases generated by the system, not user queries); grounding query to page mapping added March 2026; further features (citation share, intents, topics) reported for mid-2026 [Official, 2026-02; later features Contested]. No clicks in that report.

## 5. Adapting strategy
### 5.1 Classify your query portfolio
Build a table of your top 500 to 5,000 non-brand queries (GSC plus rank tracker) with:
- `aio_present` (rank tracker SERP feature or SERP API), `aio_cites_us`
- intent class (informational, commercial, transactional, local, navigational)
- clicks, impressions, CTR, position (last 90 days, after September 2025)
- conversion rate of the landing page

Then compute per class: share of clicks, CTR at position 1 to 3, and trend. This tells you where clicks still exist and where the business case for content has changed.

### 5.2 Portfolio decisions
| Query class | Typical AIO exposure | Strategy |
|-------------|---------------------|----------|
| Simple informational (definitions, facts) | High | Do not invest unless it supports a funnel or you are the primary source; consolidate thin explainers |
| Complex informational (how to with nuance, troubleshooting) | High but users still click for depth | Invest where you have first-hand expertise; add tools, visuals, video; structure for citation |
| Commercial investigation (best, vs, alternatives, reviews) | Medium and growing | Invest with first-hand testing and transparent comparisons; earn third party mentions (AI answers cite reviews and forums) |
| Transactional (buy, pricing, near me) | Lower; shopping and local units dominate | Invest in category, PDP, merchant listings, local SEO |
| Branded | Low | Protect: brand SERP, sitelinks, reviews, knowledge panel, entity consistency |

### 5.3 Page level practices that help in both classic and AI results
- Answer the main question clearly in the first lines; give each section a self contained answer to one sub-question.
- Use tables for comparisons and specs, lists for steps, and clear headings.
- Provide original data, first-hand evidence and named experts (information gain).
- Keep facts current and dated; AI answers favor sources consistent with other trusted sources.
- Keep entity information consistent (Organization structured data, `sameAs`, GBP, profiles).
- Make critical content available in raw HTML (AI systems and non-Google crawlers may not render JavaScript).

### 5.4 Demand creation
As AI answers absorb generic informational demand, brand demand and direct relationships matter more. Coordinate with growth-orchestrator on brand search growth as a KPI, and with creative-strategy on assets people search for by name (tools, reports, templates).

## 6. Should a site opt out of AI features? Decision process
Default answer: no. Opting out removes AI feature impressions and the clicks they produce, while competitors' content still fills the answer.

Consider opting out only if all hold:
1. The business model depends on page views of content that AI answers substitute fully (for example, certain reference or news publishers), and
2. Generative AI report and GSC data show AI features drive few clicks relative to the content's value, and
3. A licensing, legal or strategic position requires it (decided by leadership, not SEO alone), and
4. You accept that Top Stories and Discover AI surfaces may be affected (reports suggest Top Stories can render inside AI Overviews on some news SERPs) [Unverified].

Process: measure 8 or more weeks of Generative AI report impressions and per-page clicks, model the loss, present to growth-orchestrator and leadership, get written approval, change the setting, annotate the date, and monitor for 8 weeks. Partial alternatives: `data-nosnippet` on premium sections, `max-snippet` limits.

## 7. The num=100 change (September 2025)
What happened: around 2025-09-10 to 2025-09-15, Google stopped honoring the `&num=100` parameter that let tools fetch 100 results per request. Google said it was not an officially supported feature.

Effects:
- Search Console impressions fell for most sites (87.7% of 319 properties in one analysis), unique query counts fell (77.6%), and average position improved because fewer deep page impressions were recorded. Short and mid tail queries lost the most impressions.
- Interpretation: scrapers and rank trackers loading 100 results had been generating impressions for positions 11 to 100. Post-change data is closer to real human impressions [Study, 2025-09; Practitioner consensus].
- Rank trackers now need multiple requests for deep positions; many reduced default tracking depth or raised prices.

How to handle in reporting:
1. Annotate 2025-09-10 to 2025-09-15 in all dashboards.
2. Do not compare impressions, unique queries or average position across the boundary. Compare clicks and conversions.
3. For year over year comparisons in 2026, compare from 2025-09-15 forward or use clicks only.
4. Track rankings at a depth that matters (top 20 or top 50) for priority queries; use Search Console for the long tail.
5. Some reports say the parameter occasionally still works; do not depend on it [Unverified].

## 8. Other SERP changes that affect clicks
| Change | Date | Effect | Action |
|--------|------|--------|--------|
| Continuous scroll removed, back to paginated results | 2024 | Fewer impressions beyond page 1 | Track top 10 and 20 |
| Sitelinks search box removed | 2024-11 | Markup no longer needed | Remove WebSite SearchAction only if you want; harmless |
| Google requires JavaScript to load results | 2025-01 | Scraper disruption | Use licensed SERP APIs |
| Seven structured data features phased out (book actions, course info, claim review, estimated salary, learning video, special announcement, vehicle listing) | 2025-06 | Fewer rich result types | See structured data reference |
| Web Guide (Labs): AI organized results | 2025-07 | Experimental | Monitor |
| Preferred sources for Top Stories (users pick favored publishers) | 2025-08, US and India first | Publishers can ask readers to add them | See publisher section |
| Discover: follow publishers and creators, social posts in feed | 2025-09 | More competition in Discover | See publisher section |
| Search Console branded filter, query groups, annotations, weekly and monthly views, AI powered configuration | 2025-10 to 2025-12 | Better analysis | See measurement reference |
| Discover core update | 2026-02 | Local relevance, less clickbait | See publisher section |
| Ads in AI Overviews and AI Mode | 2025 to 2026 | Paid units inside AI answers | google-ads owns |

## 9. Bing and Copilot
- Bing powers Copilot answers and parts of other assistants' retrieval. Bing launched Copilot Search in 2025 [Official, 2025].
- Requirements are classic: crawlable, indexable, fast, accurate `lastmod`, IndexNow, clear content.
- Use Bing Webmaster Tools AI Performance to see which pages are cited and for which grounding queries; feed findings to ai-search-optimization and to content refresh priorities.
- Microsoft retired the public Bing Search APIs on 2025-08-11 [Official, 2025-05 announcement]; tools that relied on them changed data sources.

## 10. Boundary with ai-search-optimization
| This agent (seo) | ai-search-optimization |
|------------------|------------------------|
| Indexing, rendering, snippet eligibility for Google AI features | Prompt research and tracking across ChatGPT, Perplexity, Gemini app, Copilot, Claude, AI Mode |
| Search Console Generative AI report and Bing AI Performance as part of SEO reporting | Citation share, brand mentions in AI answers, sentiment, competitor recommendations |
| Opt-out trade-off analysis inputs | Policy for non-Google AI crawlers, llms.txt, licensing |
| Content quality and structure | Off-site presence that drives AI recommendations (reviews, forums, listicles, Wikipedia, Reddit) |

Handoff brief template: priority topics, pages with AI feature impressions, pages cited in Bing AI Performance, queries where AIO present and we are not cited, competitors cited instead.
