# Research Dossier: Conversion Rate Optimization and Landing Pages

> Research date: 2026-10-08. Scope: CRO for paid and organic traffic, landing pages, forms, ecommerce checkout, SaaS pricing and signup, page speed, experimentation statistics, personalization and AI, tools and data access.
>
> Method and limits: web searches were run in extended mode for 2025 to 2026 topics and standard mode for established topics. The shared search budget for this build was exhausted after 19 searches, and direct page fetching (WebFetch) was blocked by DNS in the research environment, so findings rely on search result content (titles, publishers, snippets and summaries) rather than full-page reads. A verification pass on 2026-10-08 re-checked the Shopify deadline outcome, Shopify Rollouts, the Clarity, GrowthBook, PostHog, Playwright and Chrome DevTools MCP servers, the Wingify rebrand, the Digital Fairness Act, the FTC accessiBe order, the click to cancel rulemaking the Eppo acquisition and the UK DMCC, FTC fees and FCC consent rulings (sources 81 to 98). Long-standing primary sources (web.dev, Baymard, KDD papers, EU legal texts) are cited from prior knowledge where noted. Every claim carries an evidence label; anything single-sourced or not confirmable is marked [Unverified]. Re-verify starred items before external use.

## 1. Executive summary

1. AI-referred traffic flipped from a conversion liability to an asset in 12 months: Adobe measured US retail AI referrals converting 38% worse than non-AI traffic in March 2025, then 42% better in March 2026 and 54% better in May 2026 [Study, Adobe 2026]. Pages that receive AI referrals need specs, comparisons and a clear buy path.
2. Experimentation vendors consolidated sharply: OpenAI bought Statsig (September 2025, $1.1B), then Amplitude took over the Statsig brand and customers (5 May 2026); VWO and AB Tasty combined (January 2026) and rebranded as Wingify (16 September 2026) [press, 2025 to 2026]. Check contracts, roadmaps and data export before renewals.
3. Vendors are shipping CRO agents: Optimizely renamed Opal to Optimizely Agent Platform (1 September 2026) with Idea builder, a Build agent that drafts A/B tests, and a CRO Manager virtual teammate; Contentsquare launched Sense Analyst (March 2026); Clarity Copilot summarizes sessions and heatmaps [Official, 2026]. AI speeds research and variant drafting; statistics and compliance still need discipline.
4. Shopify forced the end of legacy post-purchase scripts: script tags and Additional Scripts stopped on Thank you and Order status pages on 28 August 2025 (Plus; remaining Plus stores auto-upgraded from January 2026) and 26 August 2026 (non-Plus) [Official, shopify.dev 2026]. No extension was announced; whether every unupgraded store was auto-upgraded on the day is reported inconsistently [Contested]. Expect silent tracking breaks in Q3 to Q4 2026 audits.
5. Shopify now has native A/B testing (Rollouts): server-side theme splits introduced in the Winter '26 Edition and expanded in June 2026 to whole themes plus checkout and account configurations; experiments are plan-gated (Grow or Advanced and higher, sources differ), report no confidence intervals and pass no variant data to GA4; a 2 October 2026 changelog entry reportedly adds discount and offer tests [Secondary, 2026; discount tests Unverified].
6. Checkout remains the biggest leak: Baymard's average documented cart abandonment is 70.22% (50 studies, updated September 2025), surprise costs remain the top fixable reason, and 64% of large desktop sites still rate mediocre or worse on checkout UX (November 2025) [Study, 2025].
7. The European Accessibility Act has applied since 28 June 2025, and 2026 brought visible enforcement: the Dutch ACM found 61% of about 100 large online stores not accessible (March 2026); a French court ordered Carrefour to fix its site and app within six months at EUR 500 per day of delay (June 2026) [secondary, 2026]. Accessible checkout and forms are now a legal and conversion requirement.
8. Most tests lose: Optimizely's 127k-experiment analysis found about 12% win on the primary metric; Kohavi estimated a large share of "wins" at common settings are false positives [Study, 2023]. Programs need pre-registration, SRM checks, and power, not more tests.
9. Speed evidence is strong but old: the best controlled cases (Rakuten 24 A/B test: RPV +53%, CVR +33%; Vodafone: LCP 31% better, 8% more sales) date from 2021 to 2022, and no major new controlled study surfaced in 2025 to 2026 [Study, web.dev]. LCP is still the most failed Core Web Vital on mobile (about 62% good in July 2025 CrUX) [Study, 2025].
10. Ad platforms now control which page a visitor sees: Google's final URL expansion (PMax, AI Max) and ChatGPT ad review crawlers mean every indexable page can become a paid landing page and every LP must be crawlable and consistent; OpenAI is even testing ads that open brand agents instead of landing pages [Unverified, 2026].

## 2. State of CRO in 2026 (with numbers)

### 2.1 Demand and traffic shifts
- AI-referred traffic to US retail sites grew 393% year over year in Q1 2026 and 127% year over year in August 2026; Adobe forecasts 130% growth for the 2026 holiday season. Volume is still small relative to search and email [Study, Adobe 2026].
- AI-referred shoppers showed 12% (March) to 15% (May) higher engagement and reportedly 37% more revenue per visit (secondary summary of Q1 2026 data) [Study, Adobe 2026; revenue per visit Unverified].
- ChatGPT ads (OpenAI) send clicks to advertiser landing pages; OpenAI's help center recommends product, collection or content pages over homepages, landing pages are policy-reviewed, and the OAI-AdsBot crawler must reach them [Official/secondary, 2026]. Self-serve with CPC bidding opened in May 2026; carousels and oCPC followed in mid 2026 [secondary, 2026].

### 2.2 Conversion baselines
- Unbounce's 2024 Conversion Benchmark Report: median landing page conversion rate 6.6% across 41,000 pages, 464M visits and 57M conversions (July 2023 to July 2024); ecommerce 4.2%, SaaS 3.8%, entertainment 12.3% [Study, 2024].
- Baymard: 70.22% average cart abandonment (50 studies) [Study, 2025-09]; average checkout 11.3 fields in 2024 vs about 8 needed [Study, 2024]; checkout design fixes could lift conversion 35.26% for an average large site (modeled) [Study, 2025].

### 2.3 Experimentation programs
- Win rate about 12% on primary metrics across about 127,000 Optimizely experiments; multi-variation tests showed higher expected impact; only about a third of experiments test more than one variation; healthy conclusive rate 35% to 40%; personalized experiments win 12.5% vs 10.7% untargeted [Study, Optimizely 2023-12].
- Optimizely's 2026 update covers 173k experiments across 1,200+ companies (2018 to 2026) and reports that well designed experiments win much more often than poorly designed ones [Study, 2026; definitions Unverified].
- SRM appears in about 6% of Microsoft experiments (KDD 2019); LinkedIn reported about 10% of triggered experiments historically [Study, 2019].

### 2.4 Speed
- CrUX July 2025 mobile: about 62% of pages good LCP, 77% good INP, 81% good CLS [Study, 2025-07, secondary]. The FID to INP switch (12 March 2024) cut mobile pass rates by about 5 points (Web Almanac 2025) [Study, 2025].
- Contentsquare's analysis of 997 sites: retail CVR 2.5% for good INP vs 2.0% for poor or needs improvement (correlational) [Study, vendor].

### 2.5 Tools market
- Hotjar merged into the Contentsquare Group on 1 July 2025; pricing now split into Experience Analytics (from about $49 per month), Voice of Customer (from about $99 per month) and Product Analytics (custom). Free plan reportedly offers 200k sessions per month with partial replay capture [secondary, 2026].
- Microsoft Clarity remains free, with Copilot features and a 2026 push into AI Visibility (citations, topic insights, bot activity) [Official/secondary, 2026].
- Wingify (VWO plus AB Tasty) claims over $105M revenue, 4,000 customers and about 700 employees at the September 2026 rebrand [press, 2026-09].

### 2.6 Regulation
- EAA applies since 28 June 2025; technical basis EN 301 549 (WCAG 2.1 AA), with an update incorporating WCAG 2.2 expected in the Official Journal in late 2026 [Contested dates]. Penalties are national. Microenterprises (under 10 employees and under EUR 2M turnover) have limited relief for services [secondary, 2026].
- Enforcement examples: Netherlands ACM (March 2026), Sweden PTS 28 supervision cases (by March 2026), France Carrefour order (4 June 2026), Auchan claim dismissed (May 2026, appealed), German cease and desist letters to smaller shops [secondary, 2026].

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Impact on CRO | Evidence |
|------|--------|---------------|----------|
| 2025-01 to 2025-04 | FTC proposes (January) then finalizes (April, 3-0 vote) the accessiBe order: $1 million, no unsubstantiated WCAG compliance claims for automated overlays | Overlays are not a compliance fix | [Official, FTC 2025-04] |
| 2025-01-24 | Eleventh Circuit vacates the FCC one-to-one TCPA consent rule | Lead gen consent language keeps multi-seller forms legal; express written consent still required | [Official, court ruling] |
| 2025-03 | Adobe: AI referrals to US retail convert 38% worse than non-AI traffic | Baseline for AI traffic reversal | [Study, Adobe] |
| 2025-04-06 | UK DMCC Act consumer enforcement begins: drip pricing and fake reviews banned, CMA fines directly up to 10% of turnover | UK pricing and review display | [Official, 2025-04] |
| 2025-05 | Contentsquare launches Sense AI agent | AI summaries for replay and zoning | [press, 2025-05] |
| 2025-05-05 | Datadog announces acquisition of Eppo ("Eppo by Datadog") | Warehouse-native experimentation consolidates | [press, 2025-05] |
| 2025-05-12 | FTC fees rule for live-event tickets and short-term lodging takes effect (total price upfront) | Price display for covered sellers | [Official, 2025-05] |
| 2025-06-28 | European Accessibility Act applies | Accessible ecommerce and forms required for EU consumers | [Official, Directive 2019/882] |
| 2025-07 | CrUX: mobile good LCP about 62%, INP 77%, CLS 81% | LCP still the main failure | [Study, secondary] |
| 2025-07 | Amazon Prime Day: AI traffic converts 23% worse than non-AI (avg of 4 days) | Pre-reversal baseline | [Study, Adobe via CMSWire] |
| 2025-07-01 | Hotjar merged into Contentsquare Group | Pricing and plan changes; Sense features by plan | [secondary, 2026] |
| 2025-07-08 | Eighth Circuit vacates the FTC click to cancel rule (procedural grounds) | ROSCA and state laws still apply | [Official, court ruling 2025-07] |
| 2025-08-28 | Shopify Plus deadline: Thank you and Order status pages to checkout extensibility | Legacy scripts removed on upgrade | [Official, shopify.dev] |
| 2025-09 | Sense Analyst first beta customers | Agentic analytics | [Official, Contentsquare] |
| 2025-09-02 | OpenAI acquires Statsig ($1.1B stock) | Vendor risk for Statsig users | [press, TechCrunch] |
| 2025-09-22 | Baymard cart abandonment list update (70.22%, 50 studies) | Current reference | [Study, Baymard] |
| 2025-09-29 | ChatGPT Instant Checkout and Agentic Commerce Protocol announced (OpenAI later moved away from standalone Instant Checkout in March 2026) | Purchases inside assistants; data consistency matters | [Official, 2025-09] |
| 2025-11 | Baymard checkout benchmark update: 64% desktop, 63% mobile mediocre or worse | Checkout still the main leak | [Study, Baymard] |
| 2025 | Web Almanac 2025: INP switch lowered mobile CWV pass rates about 5 points | INP needs attention | [Study, HTTP Archive] |
| 2026-01 | Shopify Winter '26 Edition introduces Rollouts (early access) | Native theme A/B testing | [Secondary, 2026] |
| 2026-01-20 | VWO and AB Tasty agree to combine | Vendor consolidation | [press, GlobeNewswire] |
| 2026-01-22 | Optimizely Experimentation Program Overview agent | AI program reporting | [Official, release notes] |
| 2026-03 | Adobe: AI referrals convert 42% better than non-AI | Reversal | [Study, Adobe] |
| 2026-03 | Netherlands ACM: 61% of about 100 large online stores not accessible | EAA enforcement | [secondary] |
| 2026-03 | Sweden PTS: 28 supervision cases against online shops | EAA enforcement | [secondary] |
| 2026-03 | Contentsquare introduces Sense Analyst | AI analyst for experience data | [Official, Contentsquare] |
| 2026-03 (11 or 13 March by source) | FTC publishes an advance notice of proposed rulemaking on negative option marketing (comments closed 2026-04-13) | Click to cancel may return | [Official, 2026-03] |
| 2026-Q1 | AI traffic to US retail +393% YoY | Growing segment | [Study, Adobe] |
| 2026-04 | Optimizely Idea builder for Web Experimentation | AI test ideation from page, goal, heatmaps | [Official, release notes] |
| 2026-04 | Microsoft Advertising announces expansion of Clarity AI Visibility | AI citation reporting | [secondary] |
| 2026-04-28 | Optimizely contextual multi-armed bandits | Segment-level allocation | [Official, release notes] |
| 2026-05 | Adobe: AI-referred retail visitors convert 54% higher | Reversal widens | [Study, Adobe] |
| 2026-05 | Clarity AI citation tracking reported generally available | AI visibility data in Clarity | [Unverified, secondary] |
| 2026-05 | Auchan accessibility claim dismissed in Lille (appealed) | Legal uncertainty | [secondary] |
| 2026-05-05 | Amplitude takes over Statsig brand, platform and customers | Customers face renewal changes | [press/Official] |
| 2026-05-06 | OpenAI opens ChatGPT ads to CPC bidding and self-serve | More advertisers need ChatGPT-ready LPs | [press, MediaPost] |
| 2026-06 | Clarity content recommendations for AI visibility | AI search actions | [secondary] |
| 2026-06-04 | Caen court orders Carrefour site and app accessibility within 6 months, EUR 500 per day | Private enforcement risk | [secondary] |
| 2026-06-05 | Shopify Rollouts expanded to whole themes plus checkout and customer account configurations | Broader native testing | [Secondary, multiple 2026] |
| 2026-06-13 | VWO app moves to app.wingify.com (log in again; campaigns and SmartCode unchanged) | Account admin change | [Official, Wingify 2026-06] |
| 2026-06-17 | Shopify Summer '26 Edition (naming contested) | Rollouts GA reported | [Contested] |
| 2026-06-22 | Optimizely Idea builder for Feature Experimentation | AI ideation server side | [Official] |
| 2026-07 | Prime Day 2026: AI traffic +98.3% YoY, 50.7% conversion advantage on day 1 | Peak event confirms trend | [Study, Adobe via CMSWire] |
| 2026-07-07 | Contentsquare Sense Analyst open beta for new Growth customers | AI analysis for smaller plans | [Official, Contentsquare] |
| 2026-08 | ChatGPT ads add oCPC bidding and carousel formats | Product LP readiness | [secondary] |
| 2026-08 | Adobe: AI traffic +127% YoY | Continued growth | [Study, Adobe via Bloomberg] |
| 2026-08-25 | Optimizely CRO Manager virtual teammate | Agent stages experiments | [Official] |
| 2026-08-26 | Shopify non-Plus deadline for Thank you and Order status upgrade (passed; no extension announced) | Tracking breaks for unprepared stores | [Official, shopify.dev; day-of auto-upgrade Contested] |
| 2026-09 | Optimizely Build agent turns ideas into draft A/B tests | AI-built variants | [Official] |
| 2026-09 | OpenAI tests Sponsored Agents (ad click opens a brand agent) | Potential "agent as landing page" | [Unverified, secondary] |
| 2026-09 to 11 | EN 301 549 update incorporating WCAG 2.2 published or expected in the EU Official Journal | Accessibility standard tightening | [Contested dates] |
| 2026-09-01 | Optimizely Opal renamed Optimizely Agent Platform | Naming in docs and UI | [Official] |
| 2026-09-02 to 03 | Optimizely governance agent and flag implementation agent that outputs a SKILL.md file | Agents integrate with coding tools | [Official] |
| 2026-09-16 | VWO and AB Tasty unveiled as Wingify ("Agentic Experience Optimization Platform") with Wingz AI; products remain separate suites during integration | Rebrand, migration | [Official, press release 2026-09] |
| 2026-09-17 | Optimizely sub-agents and retrieval over artifacts | Agent platform maturity | [Official] |
| 2026-09-28 | Adobe forecasts AI-assisted shopping +130% for holidays | Prepare AI referral pages before peak | [Study, Adobe via Bloomberg] |
| 2026-10-02 | Shopify changelog entry: coordinate discounts with theme and checkout changes and test offers on a share of traffic (Rollouts) | Native offer testing | [Unverified, single secondary source] |
| 2026-Q4 (planned) | European Commission Digital Fairness Act proposal (dark patterns, unfair personalization); not yet proposed as of early October 2026 | Subscription and interface rules | [Official, work programme 2026] |

## 4. Best practice consensus

Research and prioritization:
- Use several research streams (analytics, behavior, surveys, user testing, heuristics, technical) and require triangulation before testing [Practitioner consensus, CXL ResearchXL].
- Score backlogs with evidence-weighted frameworks (PXL) rather than gut ICE alone [Practitioner consensus].
- Fix bugs, missing information and legal issues without testing; test uncertain changes [Practitioner consensus].

Landing pages:
- Match the ad's promise, offer and visual on the first screen; one goal per paid LP; navigation removed on dedicated LPs [Practitioner consensus].
- Page length follows awareness and decision complexity [Practitioner consensus].
- Proof near claims and CTAs; risk reversal under the CTA [Practitioner consensus].

Ecommerce:
- Guest checkout default, about 8 fields, address autocomplete, wallets and local payment methods, total cost shown early, delivery dates over vague shipping labels [Study, Baymard].
- PDPs need many images including in-scale, specs, delivery estimate, reviews with negatives visible [Study, Baymard; FTC rule].

Forms and lead gen:
- Justify every field; multi-step for longer forms with easy first questions; judge on qualified leads; instant booking for qualified demo requests; fast follow-up [Practitioner consensus; HBR 2011 speed to lead].

Experimentation:
- One primary metric, guardrails, pre-computed sample size, whole-week durations, SRM checks, no peeking on fixed-horizon tests, sequential methods if early stops are needed [Study, Kohavi et al.; Johari et al.].
- Treat surprising wins as bugs first (Twyman's law) [Study, Kohavi].
- On low traffic, prefer research plus guarded before/after over underpowered tests [Practitioner consensus].

Speed:
- Optimize field p75 LCP, INP, CLS on mobile; LCP image in HTML with high fetch priority; defer third parties; avoid client-side test flicker [Official, web.dev; Practitioner consensus].

Compliance:
- Real urgency, real reviews, all-in prices, no pre-ticked add-ons, easy cancellation; accessible checkout and forms; no overlays as compliance claims [Official, FTC, EU law; Practitioner consensus].

## 5. Contested topics (both sides)

| Topic | Side A | Side B | Working position for the agent |
|-------|--------|--------|--------------------------------|
| Long vs short landing pages | Long pages win for complex, expensive, unfamiliar offers | Short pages win for high intent and known offers; long pages bury CTAs | Match length to awareness and decision cost; test after offer and hero are right |
| Multi-step vs single-step forms | Multi-step raises completion through commitment and less visual load | Published wins are mostly vendor case studies; extra steps add clicks and drop-off | Multi-step for 5+ fields or qualification; test with SQL rate |
| Bayesian vs frequentist | Bayesian is intuitive and decision focused | Bayesian is not immune to peeking; frequentist controls error rates explicitly | Discipline over method: pre-register metrics, thresholds and stopping rules |
| 90% confidence for low traffic | Faster decisions on reversible, low-risk changes | Raises false positive risk sharply at low win rates (Kohavi FPR math) | Allow only for reversible, low-risk changes with guardrails; never for pricing or major flows |
| Pricing transparency in B2B | Showing prices filters bad leads and builds trust | Hiding prices increases demo volume and allows value selling | Test on pipeline and win rate, not demo count |
| Card required for trials | Opt-out trials convert far better to paid | Opt-in trials grow top of funnel and goodwill | Compare paid accounts and 90-day revenue per visitor |
| Client-side vs server-side testing | Client-side lets marketers ship tests without developers | Flicker and anti-flicker snippets slow every visitor; SRM risk | Server side or edge for above the fold and core flows; client side for minor below the fold changes |
| AI-generated variants and auto-allocation | More variants, faster learning, personalization at scale | Generic copy, invented claims, multiple comparisons, short-term optimization | Human-reviewed AI drafts, few variants, guardrails and holdouts |
| Native lead forms vs website | Native forms cut CPL dramatically | Quality and contact rates fall | Judge on cost per SQL or opportunity |
| Heatmaps | Quick visual insight | Easy to misread; aggregated across mixed intent | Use for scroll depth and false affordances; triangulate |
| Benchmarks | Provide targets | Vary by vertical, traffic mix and method | Own history first; benchmarks for sanity checks only |
| Value of speed | Strong case studies | Mostly correlational or old | Treat as a strong prior; measure locally with A/B or slowdown tests |
| Number of fields in checkout | Fewer is always better | Some fields reduce errors and failed deliveries | Remove fields without purpose; keep those that prevent errors |

## 6. What top operators do differently

1. Run research continuously: quarterly surveys, monthly recording reviews, a living VOC bank feeding copy for ads and pages.
2. Test big levers first: offer, value proposition, page structure, flow, pricing presentation, then layout details.
3. Run multi-variation tests where traffic allows and iterate on themes, not one-off tests.
4. Pre-register everything and automate SRM alerts; replicate surprising wins; discount forecasts for the winner's curse.
5. Use money metrics with guardrails (RPV with AOV and returns; qualified pipeline with lead volume).
6. Work with channel teams: one LP per ad angle, message match scored monthly, final URL expansion pages reviewed.
7. Build pages as fast, server-rendered components; run tests server side; enforce performance budgets in CI.
8. Treat accessibility and consumer law as part of conversion work and audit checkout with assistive technology.
9. Keep a learning repository and a quarterly holdout to measure cumulative impact.
10. Use AI to compress research and production time (session summaries, VOC coding, variant drafting, code diffs) while keeping humans on claims and decisions.

## 7. Common expensive mistakes

1. Optimizing for form fills or signups while lead quality or activation falls.
2. Peeking at fixed-horizon tests and shipping false winners; ignoring SRM.
3. Underpowered tests on low-traffic sites that produce noise and false confidence.
4. Homepage as the landing page for non-brand paid traffic; untreated final URL expansion pages.
5. Client-side testing tools with long anti-flicker timeouts degrading LCP for all visitors.
6. Fake countdown timers, fake stock counters, curated reviews and drip pricing creating legal exposure.
7. Missing the Shopify Thank you page migration and losing purchase tracking (and ad optimization signals) for weeks.
8. Hiding shipping costs until checkout.
9. Using accessibility overlays instead of fixing source code.
10. Personalization rules without holdouts, accumulating maintenance cost with no proven value.
11. Celebrating relative lifts without reporting intervals and absolute impact.
12. Copying competitor pages or "best practice" layouts without research for the specific audience.

## 8. Benchmarks (source, date, sample, caveat)

| Metric | Value | Source and date | Sample | Caveat |
|--------|-------|-----------------|--------|--------|
| Landing page median CVR | 6.6% all industries; ecommerce 4.2%; SaaS 3.8%; entertainment 12.3%; legal 6.3%; professional services 6.1%; travel 4.8%; education and finance about 8.4% | Unbounce Conversion Benchmark Report, 2024 | 41,000 pages, 464M visits, 57M conversions, Jul 2023 to Jul 2024 | Unbounce-hosted pages; industry figures from secondary reproductions |
| Cart abandonment | 70.22% | Baymard, updated 2025-09 | 50 studies | Mixed definitions and years |
| Checkout potential uplift | 35.26% | Baymard, 2025 | Usability testing based model | Modeled, large sites |
| Average checkout fields | 11.3 (2024), 11.8 (2021), 12.7 (2019) | Baymard | Top grossing US and EU sites | Field counting rules |
| Checkout UX mediocre or worse | 64% desktop, 63% mobile, 46% apps | Baymard benchmark, 2025-11 | Large retailers | Expert review based |
| Abandonment reasons (excluding just browsing) | Extra costs 48%, account required 26%, trust 25%, slow delivery 23%, too long 22%, total cost not visible 21%, errors 17%, returns 15%, payment methods 13%, declined 9% | Baymard, 2024 survey | US adults | Denominators differ across publications; 2025 page shows about 39% to 40% extra costs on all-shopper base |
| Experiment win rate | about 12% primary metric | Optimizely, 2023-12 | about 127,000 experiments | Self-reported, Optimizely customers |
| Personalized vs untargeted win rate | 12.5% vs 10.7% | Optimizely, 2023-12 | Same | Same |
| SRM incidence | about 6% (Microsoft), about 10% historically (LinkedIn triggered experiments) | KDD 2019 and LinkedIn | Company-level | Not industry rates |
| CWV mobile good shares | LCP 62%, INP 77%, CLS 81% | CrUX July 2025 (secondary) | All CrUX pages | Page-level, varies by platform |
| AI-referral conversion vs non-AI (US retail) | -38% (Mar 2025), +42% (Mar 2026), +54% (May 2026), +50.7% (Prime Day 2026 day 1) | Adobe Digital Insights | Adobe Analytics retail clients | Relative only; non-AI includes all other channels |
| AI referral traffic growth | +393% YoY (Q1 2026), +127% YoY (Aug 2026) | Adobe | Same | Small base |
| Speed case: Rakuten 24 | RPV +53.37%, CVR +33.13% | web.dev | One-month A/B test | Single company |
| Speed case: Vodafone Italy | LCP -31%, sales +8% | web.dev, 2021 | A/B test | Single company |
| Speed: Deloitte "Milliseconds Make Millions" | 0.1 s faster: retail CVR +8.4%, travel +10.1% | Deloitte and Google, 2020 | 37 brands, observational | Correlational |
| INP and CVR (retail) | 2.5% good INP vs 2.0% poor | Contentsquare | 997 sites | Correlational, vendor |
| Speed to lead | Contact within 1 hour: nearly 7x more likely to qualify | HBR, 2011 | 2,241 US companies | Old, B2B |
| Usability testing | 5 users find most problems in a round | Nielsen Norman Group, 2000 | Model | Per segment and task |

## 9. Tools, APIs and MCP servers

| Category | Tools | API and MCP access | Notes |
|----------|-------|--------------------|-------|
| Behavior analytics | Microsoft Clarity | Data Export API (recent days only, about 10 requests per project per day); official MCP package `@microsoft/clarity-mcp-server` (v2.x tools: query-analytics-data, list-session-recordings, query-documentation-data; v1.x: get-clarity-data) [Official package, 2026] | Free; Copilot features; AI Visibility |
| Behavior analytics | Contentsquare (incl. Hotjar) | Connectors to ChatGPT, Claude, Copilot and IDEs on all plans with tool call limits [Official support, 2026] | Sense Chat, Sense Analyst |
| Behavior and product analytics | PostHog | API; official hosted MCP server (mcp.posthog.com, EU mcp-eu.posthog.com) [Official, 2026] | Experiments, flags, replay, surveys |
| Experimentation | Optimizely | REST APIs; Agent Platform agents | Contextual bandits, Stats Engine |
| Experimentation | Wingify (VWO, AB Tasty) | APIs per product | Rebranded 2026-09-16; suites still separate |
| Experimentation | Kameleoon, Convert | APIs | Check AI features |
| Experimentation | GrowthBook | Open source, API, MCP server `@growthbook/mcp` [Official package; config Unverified] | Warehouse native |
| Experimentation | Statsig (Amplitude) | API, warehouse native | Ownership change May 2026 |
| Experimentation | Shopify Rollouts | Admin UI | No CI; compute stats externally |
| Analytics | GA4 | Data API v1beta `runReport`, v1alpha `runFunnelReport`; Google Analytics MCP server [Unverified status]; BigQuery export | Coordinate with measurement |
| Speed | CrUX API, CrUX History API, PageSpeed Insights API, Lighthouse CLI and CI, WebPageTest | Public APIs with key | Field and lab |
| QA and screenshots | Playwright, Chrome DevTools | Playwright MCP (Microsoft, 2025-03) and Chrome DevTools MCP (Google, preview 2025-09-23, stable by 2026-06) [Official] | Local QA of variants |
| Commerce data | Shopify Admin GraphQL | Read scopes; Shopify Dev MCP `@shopify/dev-mcp` for docs and schema [Official] | AOV, product mix |
| Forms | Zuko | API [Unverified] | Field-level analytics |
| Surveys | Fairing, KnoCommerce, Typeform | APIs | Post-purchase VOC |

## 10. Official sources to monitor

| Source | What to watch |
|--------|---------------|
| web.dev and Chrome for Developers (CrUX, Core Web Vitals, Speculation Rules) | Metric changes, thresholds, new APIs, case studies |
| HTTP Archive Web Almanac | Annual state of performance and third parties |
| Shopify changelog, shopify.dev checkout docs, Shopify Editions | Checkout extensibility, Rollouts, plan gating |
| WooCommerce developer blog | Checkout block changes |
| Optimizely release notes (Web, Feature Experimentation, Agent Platform) | AI agents, stats features |
| Wingify, VWO and AB Tasty newsrooms | Product convergence, pricing |
| Amplitude and Statsig blogs | Platform roadmap after May 2026 |
| GrowthBook releases, PostHog changelog, Kameleoon and Convert changelogs | Stats defaults, MCP, AI |
| Microsoft Clarity blog and Microsoft Learn docs | Copilot, AI Visibility, API and MCP |
| Contentsquare support release notes | Sense features and plan availability |
| Baymard Institute | Checkout and abandonment updates |
| Adobe Digital Insights | AI traffic conversion trends |
| OpenAI ads help center | Landing page rules, crawler, formats |
| Google Ads Help, Meta Business Help, TikTok and LinkedIn help centers | Landing page policies, final URL expansion, lead forms |
| European Commission, national EAA authorities (ACM, PTS and others), EUR-Lex | Accessibility enforcement, Digital Fairness Act |
| FTC, UK CMA | Reviews, pricing, dark patterns, subscriptions |
| W3C WAI | WCAG updates |

## 11. Open questions and watch list

1. Shopify Rollouts: plan availability (Grow vs Advanced) [Contested], whether statistical significance reporting is added, and the scope and plan limits of the 2026-10-02 discount testing entry [Unverified].
2. Post-deadline Shopify behavior: how many non-Plus stores lost tracking after 26 August 2026 (no extension was announced; day-of auto-upgrade reports conflict) [Contested].
3. OpenAI Sponsored Agents: if ad clicks open brand agents, CRO expands to agent prompts, knowledge bases and in-chat conversion paths [Unverified].
4. Amplitude's plans for Statsig vs Amplitude Experiment; risk of product consolidation [Contested].
5. Wingify integration: pricing changes at renewal and when VWO and AB Tasty become one product (Wingify says several quarters from mid 2026) [Unverified].
6. EN 301 549 update with WCAG 2.2 and its Official Journal citation date [Contested].
7. EU Digital Fairness Act: proposal planned for Q4 2026 (Commissioner McGrath, May 2026), legal form open; whether subscription cancellation gets standalone rules [Official timing, scope Unverified].
8. AI referral conversion advantage: whether it persists as AI traffic broadens beyond early adopters [Open].
9. Agentic checkout adoption and how much purchase volume moves off-site [Open].
10. New controlled evidence on INP and conversion; most published data is correlational [Open].
11. Clarity MCP server: tool set changes between v1 and v2 and whether write or recording-level analysis tools are added [Open].
12. Whether vendor AI agents (Optimizely Build agent, Wingz, Sense Analyst) measurably raise win rates or only velocity [Open].

## 12. Sources

1. 50 Cart Abandonment Rate Statistics 2026. Baymard Institute. https://baymard.com/lists/cart-abandonment-rate. Updated 2025-09-22.
2. Checkout UX Best Practices 2025. Baymard Institute. https://baymard.com/research-articles/current-state-of-checkout-ux. 2025-11.
3. Checkout Optimization: Minimize Form Fields. Baymard Institute. https://baymard.com/blog/checkout-flow-average-form-fields. 2024.
4. Reasons for Cart Abandonment (checkout usability report and benchmark). Baymard Institute. https://baymard.com/blog/ecommerce-checkout-usability-report-and-benchmark. Ongoing.
5. Form Design: 6 Best Practices for Better E-Commerce UI. Baymard Institute. https://baymard.com/blog/form-design. Ongoing.
6. Cart Abandonment Rate & Reasons 2025: Baymard Statistics Explained. Growthegy. https://www.growthegy.com/2026/05/26/cart-abandonment-science-why-customers-leave-checkout/. 2026-05-26.
7. The Quick Guide to Microsoft Clarity's Copilot. Microsoft Clarity Blog. https://clarity.microsoft.com/blog/the-quick-guide-to-microsoft-claritys-copilot/. 2025.
8. Copilot Overview. Microsoft Learn. https://learn.microsoft.com/en-us/clarity/copilot/overview. 2025.
9. Understanding Your Influence in AI Answers with Microsoft Clarity. Microsoft Clarity Blog. https://clarity.microsoft.com/blog/understanding-your-influence-ai-citations/. 2026.
10. Microsoft Clarity Adds Citations for AI Visibility. Media Copilot. https://mediacopilot.ai/microsoft-clarity-citations-ai-visibility/. 2026.
11. Microsoft Clarity MCP Server. FlowHunt. https://www.flowhunt.io/mcp-servers/microsoft-clarity/. 2025 to 2026.
12. Shopify Aug 26, 2026 Deadline: Thank You Page Upgrade. Huptech Web. https://www.huptechweb.com/blogs/shopify-august-26-2026-checkout-deadline. 2026.
13. Shopify Thank you page upgrade: what stops on 26 August. true.noise. https://truenoise.co.uk/blog/shopify-thank-you-order-status-upgrade. 2026.
14. Shopify Checkout Extensibility in 2026: What's New? Codersy. https://www.codersy.com/blog/shopify-plus/shopify-checkout-extensibility-in-2026-what-store-owners-need-to-know. 2026.
15. Shopify Checkout Upgrade 2026: What You Need to Know. Visualsoft. https://www.visualsoft.co.uk/blog/shopifys-big-checkout-upgrade-what-you-need-to-know-before-2026. 2026.
16. Shopify Rollouts: Native A/B Testing Explained 2026. Storepilot. https://www.usestorepilot.com/blog/shopify-rollouts-ab-testing/. 2026.
17. Native A/B Testing on Shopify: How Rollouts Works and What It Can't Do. Conspire Agency. https://www.conspireagency.com/blogs/shopify/native-a-b-testing-on-shopify-how-rollouts-works-and-what-it-cant-do-yet. 2026.
18. Shopify Native A/B Testing Is Here. Should You Drop Your CRO App? Black Belt Commerce. https://www.blackbeltcommerce.com/shopify-native-ab-testing-vs-cro-apps/. 2026.
19. European Accessibility Act 2026: Requirements and Penalties. Level Access. https://www.levelaccess.com/compliance-overview/european-accessibility-act-eaa/. 2026.
20. The European Accessibility Act, One Year On (2026 Review). EqualWeb. https://www.equalweb.com/blog/european-accessibility-act-one-year-on/. 2026.
21. European Accessibility Act enforcement: cases so far. Atyantik. https://atyantik.com/blog/european-accessibility-act-enforcement/. 2026.
22. Inclusivity-by-design: the European Accessibility Act as a new imperative for e-commerce. Freshfields. https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/inclusivity-by-design-the-european-accessibility-act-as-a-new-imperative-for-e-102lu76. 2025.
23. 2026 Optimizely Opal release notes. Optimizely Support. https://support.optimizely.com/hc/en-us/articles/37791100847373-2026-Optimizely-Opal-release-notes. 2026.
24. 2026 Optimizely Web Experimentation release notes. Optimizely Support. https://support.optimizely.com/hc/en-us/articles/23949705057421-2026-Optimizely-Web-Experimentation-release-notes. 2026.
25. 2026 Optimizely Feature Experimentation release notes. Optimizely Docs. https://docs.optimizely.com/feature-experimentation/release-notes/2026-optimizely-feature-experimentation-release-notes. 2026.
26. Optimizely Agent Platform: October 2026 State of Play. Optimizely World (Scott Reed). https://world.optimizely.com/blogs/scott-reed/dates/2026/10/optimizely-agent-platform---october-2025-state-of-play. 2026-10.
27. Top 10 takeaways from running 127,000 experiments. Optimizely. https://www.optimizely.com/insights/top-10-takeaways-from-the-experimentation-playbook/. 2023-12.
28. 173k experiments later, here's what we learned. Optimizely. https://www.optimizely.com/field-notes/guides/173000-experiments. 2026.
29. The agentic AI experimentation report. Optimizely. https://www.optimizely.com/insights/agentic-ai-experimentation-benchmark/. 2026.
30. Lessons learned from running 127,000 experiments (post and comments). Ron Kohavi, LinkedIn. https://www.linkedin.com/posts/ronnyk_lessons-learned-from-running-127000-experiments-activity-7143376795940106240-faUh. 2023-12.
31. OpenAI acquires product testing startup Statsig and shakes up its leadership team. TechCrunch. https://techcrunch.com/2025/09/02/openai-acquires-product-testing-startup-statsig-and-shakes-up-its-leadership-team/. 2025-09-02.
32. Statsig is joining OpenAI. Statsig. https://www.statsig.com/blog/openai-acquisition. 2025-09 (editor's note 2026-05).
33. Amplitude and Statsig partnership. Amplitude. https://amplitude.com/blog/amplitude-and-statsig-partnership. 2026-05.
34. Amplitude and Statsig deal raises questions for customers. MarTech. https://martech.org/amplitude-and-statsig-deal-raises-questions-for-customers/. 2026-05.
35. Amplitude and Statsig Enter Into a Strategic Partnership. Convert. https://www.convert.com/blog/a-b-testing/statsig-moves-to-amplitude/. 2026.
36. VWO and AB Tasty Join Forces to Redefine the Future of Digital Experience Optimization. GlobeNewswire. https://www.globenewswire.com/news-release/2026/01/20/3221331/0/en/VWO-and-AB-Tasty-Join-Forces-to-Redefine-the-Future-of-Digital-Experience-Optimization.html. 2026-01-20.
37. VWO & AB Tasty Merge to Create $100M Digital Experience Optimization Platform. CMSWire. https://www.cmswire.com/digital-experience/vwo-ab-tasty-merge-to-create-100m-digital-experience-optimization-platform/. 2026-01.
38. Inside Wingify: The Digital Experience Optimization Suite. VWO Blog. https://vwo.com/blog/wingify-the-unified-digital-experience/. 2026-09.
39. AB Tasty and VWO unite as Wingify to launch Agentic Experience Optimisation platform. AdTech Juice. https://www.adtechjuice.com/ab-tasty-and-vwo-unite-as-wingify-to-launch-agentic-experience-optimisation-platform. 2026-09.
40. VWO Merges With AB Tasty: Inside the 2026 Consolidation Wave. Convert. https://www.convert.com/blog/optimization/vwo-merges-with-ab-tasty-consolidation-wave/. 2026.
41. Hotjar Pricing 2026: Every Tier, Verified From the Source. Humblytics. https://humblytics.com/blog/hotjar-pricing. 2026.
42. Introduction to Sense Analyst. Contentsquare Support. https://support.contentsquare.com/hc/en-us/articles/44881074763921-Introduction-to-Sense-Analyst. 2026.
43. Releases and Updates for 2026. Contentsquare Support. https://support.contentsquare.com/hc/en-us/articles/42751336307217-Releases-and-Updates-for-2026. 2026.
44. Contentsquare Rolls Out AI Agent Sense Analyst. Contentsquare. https://contentsquare.com/press/analytics-on-autopilot-contentsquare-rolls-out-ai-agent-sense-analyst/. 2026-03.
45. Contentsquare Launches Sense, an AI-Powered Agent. The AI Insider. https://theaiinsider.tech/2025/05/17/contentsquare-launches-sense-an-ai-powered-agent-to-disrupt-digital-experience-analytics/. 2025-05-17.
46. The business impact of Core Web Vitals. web.dev. https://web.dev/case-studies/vitals-business-impact. 2022 to 2023.
47. How Rakuten 24's investment in Core Web Vitals increased revenue per visitor by 53.37% and conversion rate by 33.13%. web.dev. https://web.dev/case-studies/rakuten. 2022.
48. How to Optimize Interaction to Next Paint (INP). web.dev. https://web.dev/explore/how-to-optimize-inp. 2024.
49. Interaction to Next Paint (INP). web.dev. https://web.dev/articles/inp. 2024-03 (canonical, not re-fetched).
50. Interaction to next paint (INP): does it matter? Contentsquare. https://contentsquare.com/blog/interaction-to-next-paint/. 2024.
51. Core Web Vitals Benchmarks 2026: What Good Looks Like. Digital Applied. https://www.digitalapplied.com/blog/core-web-vitals-benchmarks-2026-pass-rate-reference. 2026.
52. Case studies: the benefits of optimizing Core Web Vitals. RUMvision. https://www.rumvision.com/blog/benefits-of-optimizing-core-web-vitals/. 2025.
53. Adobe: AI-referred traffic to retail sites doubles in a year. Digital Commerce 360. https://www.digitalcommerce360.com/2026/06/17/adobe-ai-referred-traffic-to-retail-sites-doubles-in-a-year/. 2026-06-17.
54. Quarterly AI Traffic Report, April 2026. Adobe Digital Insights. https://business.adobe.com/resources/sdk/.2026-q2-ai-traffic-report/q2-2026-adi-ai-sourced-traffic-insights.pdf. 2026-04.
55. AI Traffic Growth Nears 100% on Amazon Prime Day, and Converts Better Than Every Other Channel. CMSWire. https://www.cmswire.com/digital-experience/adobe-ai-shopping/. 2026-07.
56. AI Shopping Agent Use to Rise 130% During Holidays, Adobe Says. Bloomberg. https://www.bloomberg.com/news/articles/2026-09-28/ai-assisted-shopping-to-rise-130-during-holidays-adobe-says. 2026-09-28.
57. AI traffic grows but retail sites lag in AI search visibility. Adobe. https://business.adobe.com/blog/ai-traffic-surge-retail-sites-not-machine-readable. 2026.
58. What's a good conversion rate? (Based on 41,000 landing pages). Unbounce. https://unbounce.com/landing-pages/whats-a-good-conversion-rate/. 2024.
59. Ads in ChatGPT: The Basics. OpenAI Help Center. https://help.openai.com/en/articles/20001207-ads-in-chatgpt-the-basics. 2026.
60. Create Ads for ChatGPT Ads. OpenAI Help Center. https://help.openai.com/en/articles/20001212-create-ads-for-chatgpt. 2026.
61. OpenAI Opens Ad Platform To CPC Bidding, Self-Serve Buys. MediaPost. https://www.mediapost.com/publications/article/414857/openai-opens-ad-platform-to-cpc-bidding-self-serv.html. 2026-05-06.
62. OpenAI brings product carousels to ChatGPT ads. Digiday. https://digiday.com/marketing/openai-brings-product-carousels-to-chatgpt-ads/. 2026.
63. ChatGPT Ads May Replace Landing Pages With AI Agents. TechWyse. https://www.techwyse.com/news/platform-updates/chatgpt-ads-business-agents-replace-landing-pages. 2026-09.
64. OpenAI Has a New Ads Crawler: Your Landing Page Can Influence When ChatGPT Shows Your Ad. NetContentSEO. https://netcontentseo.com/article/openai-has-a-new-ads-crawler-your-landing-page-can-influence-when-chatgpt-shows-your-ad-906. 2026.
65. OpenAI drops 25,000-user floor for ChatGPT ad exclusion audiences. PPC Land. https://ppc.land/openai-drops-25-000-user-floor-for-chatgpt-ad-exclusion-audiences/. 2026.
66. OpenAI's ChatGPT Ads Manager Plugin, Audience Updates, Product Feeds and More. Search Engine Roundtable. https://www.seroundtable.com/openai-chatgpt-ads-updates-42017.html. 2026.
67. Diagnosing Sample Ratio Mismatch in Online Controlled Experiments: A Taxonomy and Rules of Thumb for Practitioners. Fabijan et al., KDD 2019. https://www.lukasvermeer.nl/publications/papers/2019/07/25/diagnosing-sample-ratio-mismatch-in-online-controlled-experiments.html. 2019-07.
68. SRM Frequently Asked Questions. Lukas Vermeer. https://lukasvermeer.nl/srm/docs/faq/. Ongoing.
69. Seven Rules of Thumb for Web Site Experimenters. Kohavi, Deng, Longbotham, Xu (KDD 2014). https://exp-platform.com/rules-of-thumb/. 2014.
70. Product Experimentation Pitfalls: Experimenting Without Enough Traffic. Optimizely. https://www.optimizely.com/2018/05/09/experimenting-without-enough-traffic/. 2018-05.
71. How to run A/B testing on low traffic. Data Analysis Journal. https://dataanalysis.substack.com/p/how-to-run-an-ab-testing-on-low-traffic. 2023.
72. Do Some Sources Of Experiment Ideas Lead To Higher Win Rates Than Others? GoodUI. https://goodui.org/blog/do-some-sources-of-experiment-ideas-lead-to-higher-win-rates-than-others/. 2024.
73. How Not To Run an A/B Test. Evan Miller. https://www.evanmiller.org/how-not-to-run-an-ab-test.html. 2010 (canonical, not re-fetched).
74. The Short Life of Online Sales Leads. Harvard Business Review. https://hbr.org/2011/03/the-short-life-of-online-sales-leads. 2011-03 (canonical, not re-fetched).
75. Why You Only Need to Test with 5 Users. Nielsen Norman Group. https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/. 2000 (canonical, not re-fetched).
76. Directive (EU) 2019/882, European Accessibility Act. EUR-Lex. https://eur-lex.europa.eu/eli/dir/2019/882/oj. 2019 (canonical, not re-fetched).
77. Directive (EU) 2019/2161, Omnibus Directive. EUR-Lex. https://eur-lex.europa.eu/eli/dir/2019/2161/oj. 2019 (canonical, not re-fetched).
78. Regulation (EU) 2022/2065, Digital Services Act. EUR-Lex. https://eur-lex.europa.eu/eli/reg/2022/2065/oj. 2022 (canonical, not re-fetched).
79. Web Content Accessibility Guidelines (WCAG) 2.2. W3C. https://www.w3.org/TR/WCAG22/. 2023-10 (canonical, not re-fetched).
80. CrUX API documentation. Chrome for Developers. https://developer.chrome.com/docs/crux/api. Ongoing (canonical, not re-fetched).
81. checkout.liquid layout (script tag sunset dates). Shopify Dev Docs. https://shopify.dev/docs/storefronts/themes/architecture/layouts/checkout-liquid. 2026.
82. Shopify Thank You and Order Status Page Upgrade (2026). Consentmo. https://www.consentmo.com/blog-posts/shopify-thank-you-order-status-upgrade-august-2026. 2026.
83. Shopify Rollouts: How to Safely A/B Test Themes, Checkout, and Customer Accounts. Thoughtbulb. https://thoughtbulb.dev/blog/shopify-rollouts-theme-checkout-ab-testing-2026/. 2026.
84. Shopify A/B Testing: Native Rollouts vs Apps (2026). Ecomhint. https://ecomhint.com/blog/shopify-ab-testing. 2026.
85. Shopify Rollouts Now Tests Discounts on Live Traffic. Ecommerce Paradise. https://ecommerceparadise.com/shopify-rollouts-tests-discounts/. 2026-10.
86. AB Tasty and VWO Unite Under Wingify. Newswire (press release). https://www.newswire.ca/news-releases/ab-tasty-and-vwo-unite-under-wingify-launching-a-unified-platform-new-brand-identity-and-a-website-827260962.html. 2026-09-16.
87. Microsoft Clarity Data Export MCP Server README (v1.0.5). unpkg mirror of npm. https://unpkg.com/@microsoft/clarity-mcp-server@1.0.5/README.md. 2025.
88. Use experiments over PostHog MCP. PostHog. https://posthog.com/docs/experiments/surfaces/mcp. 2026.
89. GrowthBook MCP Server. mcp.so. https://mcp.so/servers/growthbook-mcp. 2025 to 2026.
90. Give your AI eyes: Introducing Chrome DevTools MCP. Addy Osmani. https://addyosmani.com/blog/devtools-mcp/. 2025-09.
91. FTC Puts the Brakes on accessiBe's Misleading Claims, Orders $1 Million Penalty. GRC Report. https://www.grcreport.com/post/ftc-puts-the-brakes-on-accessibes-misleading-claims-orders-1-million-penalty. 2025-04.
92. Digital Fairness Act (legislative train). European Parliament. https://www.europarl.europa.eu/legislative-train/theme-protecting-our-democracy-upholding-our-values/file-digital-fairness-act. 2026.
93. EU proposal on Digital Fairness Act expected by the end of 2026. Privacy Laws and Business. https://www.privacylaws.com/news/eu-proposal-on-digital-fairness-act-expected-by-the-end-of-2026/. 2026-05.
94. FTC Issues New Advance Notice of Proposed Rulemaking on Negative Option Marketing. Cooley. https://www.cooley.com/news/insight/2026/2026-03-19-ftc-issues-new-advance-notice-of-proposed-rulemaking-on-negative-option-marketing. 2026-03-19.
95. Datadog acquires experiment platform provider Eppo. Seeking Alpha. https://seekingalpha.com/news/4440981-datadog-acquires-experiment-platform-provider-eppo. 2025-05-05.
96. Direct consumer enforcement: one year on. CMA blog. https://competitionandmarkets.blog.gov.uk/2026/04/17/direct-consumer-enforcement-one-year-on/. 2026-04-17.
97. FTC finalizes junk fees rule; new pricing disclosure requirements take effect May 12, 2025. Barnes and Thornburg. https://btlaw.com/en/insights/alerts/2025/ftc-finalizes-junk-fees-rule-new-pricing-disclosure-requirements-take-effect-may-12-2025. 2025.
98. Eleventh Circuit Vacates FCC's TCPA One-to-One Consent Rule. Morrison Foerster. https://www.mofo.com/resources/insights/250130-eleventh-circuit-vacates-fcc-s-tcpa-one-to-one-consent-rule. 2025-01-30.
