# Evidence and Ranking Factors

> Knowledge as of 2026-10. This field is full of vendor claims and correlation studies sold as causation. This module grades every factor so the agent spends effort where evidence is strongest. Re-grade when new primary data appears.

## 1. Evidence grades used in this package

| Grade | Meaning | Example | How to use it |
|-------|---------|---------|---------------|
| A | Official documentation or a platform statement | Google AI features page, OpenAI bots page | Treat as the rule of the platform. Still verify it is current |
| B | Controlled experiment with a published method | Princeton GEO paper (simulated engine) | Strong for direction, weaker for size of effect on live engines |
| C | Large observational study with a stated method | Ahrefs 75k brands correlation, Seer CTR studies | Direction likely, causation not proven |
| D | Practitioner consensus | "Get on the listicles your category's AI answers cite" | Reasonable default. Validate with your own tracking |
| E | Vendor claim, single site, or unsourced statistic | "Schema increases AI citations 3x" | Hypothesis only. Do not cite to clients |

Map to inline labels: A = [Official], B and C = [Study], D = [Practitioner consensus], E = [Unverified]. Use [Contested] when credible sources conflict.

## 2. Factor table

| Factor | Grade | What the evidence says | Engines | Action |
|--------|-------|-----------------------|---------|--------|
| Crawl access for the engine's search and user-fetch bots | A | OpenAI: blocking OAI-SearchBot removes a site from ChatGPT search answers. Anthropic: blocking Claude-SearchBot or Claude-User reduces visibility. Google: page must be indexed and snippet-eligible | All | Fix first. Nothing else matters if access fails |
| Indexed and snippet-eligible in Google | A | Required for AI Overviews and AI Mode citations [Official, 2025] | Google AIO, AI Mode, Gemini | Classic technical SEO. Hand off to `seo` |
| Classic rankings in Google | C, [Contested] for size | Ahrefs 2025: 76% of AI Overview citations came from top 10 pages. Moz 2026: about 12% of AI Mode citations matched the organic top 10. A 2026 roundup cited 17% AIO overlap with top 10 [Study, secondary] | AIO, AI Mode, ChatGPT paid tier | Ranking still feeds citations, but AI Mode and fan-out widen the field. Rank for sub-queries, not just the head term |
| Scraped Google results inside ChatGPT | C | Paid ChatGPT drew about 75% of sources from scraped Google results in 2026-05 to 2026-07 data [Study, 2026-07, Resoneo] | ChatGPT paid | Google SEO is a ChatGPT lever for paid users |
| Bing rankings | C, declining for ChatGPT | Seer 2024: 87% of SearchGPT citations matched Bing top results. 2026: only about 1.5% of ChatGPT's own index URLs matched Bing top 20 [Study] | Copilot strongly, ChatGPT weakly now | Keep Bing healthy for Copilot. Do not treat Bing as the ChatGPT strategy |
| Branded web mentions (unlinked) | C | Ahrefs, about 75k brands: branded web mentions correlated 0.664 with AI Overview brand visibility, branded anchors 0.527, branded search volume 0.392. Ahrefs called all factors moderate to weak and correlational [Study, 2025] | AIO; likely others | Grow mentions on pages that engines retrieve. See off-site module |
| YouTube mentions | C | Ahrefs reported YouTube mentions as a strong correlate of visibility across ChatGPT, AI Mode and AIO in its 2025-12 brand study [Unverified exact figures]. YouTube led AI Overviews mention share (22.9%) in Ahrefs' September 2026 leaderboard and was AI Mode's top citation source (21.1%) in Semrush's 2026-08 study [Study, 2026-08 and 2026-09] | AIO, AI Mode, ChatGPT | Publish useful videos with accurate titles, descriptions and transcripts. Earn creator reviews |
| Backlinks | C | Weaker correlation than mentions in the Ahrefs brand study [Study, 2025] | All, indirectly via rankings | Keep earning links for rankings. Do not expect links alone to drive mentions |
| Content with quotations, statistics, cited sources | B | Princeton GEO (KDD 2024): quotation addition, statistics addition and citing sources gave the largest visibility gains, up to about 40% relative on a simulated GPT-3.5 engine using top 5 Google results; validated on Perplexity at up to about 37%. Keyword stuffing did not help. Lower-ranked sources gained most from citing sources [Study, 2024] | Likely general | Add real numbers, named expert quotes and sources to key passages. Never fabricate |
| Fluency and readability | B | Fluency and easy-to-understand rewrites gave smaller but positive gains in the GEO paper [Study, 2024] | General | Clear writing helps, but specificity helps more |
| Freshness | C | Analyses in 2025 reported AI assistants cite content that is fresher than classic organic results (Ahrefs reported about 25.7% fresher on average) [Study, 2025, verify exact figure] | ChatGPT strongest, others | Update decision pages (pricing, comparisons, best-of) on a schedule with real changes. Never fake dates |
| Structured data (schema.org) | [Contested] | Google: not required for AI features, keep it consistent with visible text [Official]. Bing said schema helps its LLMs understand content [Practitioner report, 2025-03]. AirOps: 61% of pages cited by ChatGPT had structured data vs 25% of Google top results [Study, 2026, correlational]. Ahrefs controlled study: 1,885 pages that added JSON-LD vs 4,000 controls showed no significant citation change (AI Mode +2.4%, ChatGPT +2.2%, AI Overviews minus 4.6%) [Study, 2026-05] | Bing and Copilot most plausible | Implement Organization, Product, Article, LocalBusiness correctly for entity clarity and rich results. Do not promise citation lift |
| llms.txt | C (null result) | SE Ranking, about 300k domains: no significant correlation with AI citations. Ahrefs, 137k domains: 97% of llms.txt files got zero requests in 2026-05; retrieval bots about 1% of requests. Google: not used for Search [Study, 2025 to 2026; Official statements] | None confirmed | Optional, low priority. Useful for developer docs consumed by coding agents |
| Reviews and ratings on third-party platforms | D | Review sites (G2, Capterra, Trustpilot, Google reviews) appear among cited sources for commercial prompts [Practitioner consensus; Study for citation lists] | All, especially shopping and local | Build genuine review volume and recency on the platforms your category's answers cite |
| Inclusion in third-party "best X" lists | D, strong practitioner signal | Listicles and comparison articles are among the most cited page types for "best" and "top" prompts [Practitioner consensus; multiple vendor studies] | All | Earn inclusion through product merit, PR and affiliate relationships with disclosure |
| Wikipedia and Wikidata presence | C for ChatGPT | Wikipedia was ChatGPT's top source in Profound's 2024 to 2025 data (47.9% of top-10 source share) [Study, 2025] | ChatGPT, Google Knowledge Graph | Only if notable. Follow conflict-of-interest rules. See entity module |
| Reddit presence | C, volatile | Top source for Perplexity and AIO in 2024 to 2025 data; ChatGPT Reddit citations fell sharply in 2025-09 [Study] | Perplexity, AIO, AI Mode | Participate genuinely in relevant threads. Never astroturf |
| Page speed and server response | D | Slow or timing-out pages fail user-triggered fetches [Practitioner consensus] | ChatGPT-User, Perplexity-User, Claude-User | Keep TTFB low for key pages. Avoid bot challenges on them |
| Server-side rendered content | B for crawlers | AI crawlers fetched but did not execute JS in 2024 logs [Study, 2024-12] | All non-Google, non-Apple | SSR or prerender all key content |
| Author bylines and E-E-A-T style signals | D | No direct evidence for AI citation lift. Supports Google quality systems [Practitioner consensus] | Google features | Keep real authors and credentials. Low cost, indirect benefit |
| Content length | E | No credible evidence that longer pages get cited more | n/a | Write to cover the sub-questions, not to a word count |

## 3. Traffic and click impact data

| Finding | Source and date | Sample | Caveat |
|---------|----------------|--------|--------|
| Top-ranking page CTR about 34.5% lower when an AI Overview is present | Ahrefs, 2025-04 | 300k keywords | Observational |
| Top-ranking page CTR about 58% lower when an AI Overview is present (Dec 2023 vs Dec 2025, adjusted for SERP trends); position 2 down 50.8%, position 3 down 46.4% | Ahrefs, 2026-02 update | 150k AIO keywords vs 150k informational non-AIO | Applies to position 1 on AIO queries, not whole-site traffic |
| Users clicked a traditional result in 8% of visits with an AI summary vs 15% without; clicked a link inside the summary about 1% of the time | Pew Research, 2025-07 | About 900 US adults' browsing, 2025-03 | US only, desktop and mobile panel |
| Organic CTR on AIO queries fell from 1.76% to 0.61%, paid CTR from 19.7% to 6.34%; cited brands got 35% more organic and 91% more paid clicks than uncited | Seer Interactive, 2025-11 | 3,119 informational queries, 42 organizations | Correlational |
| 2026 update: on AIO SERPs, cited brands about 20,743 organic clicks per million impressions vs about 9,445 uncited and about 33,500 with no AIO; paid CTR on AIO queries rose from 14.64% to 16.21% Jan 2025 to Feb 2026 | Seer Interactive, 2026 | 53 brands, 5.47M queries, 2.43B organic impressions | Reported via secondary summaries; verify tables |
| Google says total organic click volume from Search was relatively stable year over year and click quality rose | Google (Liz Reid), 2025-08 | Not disclosed | Platform statement without data |
| AI Overviews appeared on 13.14% of queries in 2025-03, up from 6.49% in 2025-01 | Semrush, 2025 | 10M+ keywords | Prevalence changes monthly |

## 4. AI referral traffic data

| Finding | Source and date | Caveat |
|---------|----------------|--------|
| ChatGPT sent 79.4% of AI chatbot referrals, Gemini 10.9%, Perplexity 4.3%, Copilot 2.8%, Claude 2.6% | Statcounter, 2026-08, via secondary | Global panel, all site types |
| ChatGPT's share of generative AI web traffic fell from about 76% (2025-06) to about 53% (2026-05) while visits stayed flat; Gemini passed a quarter of traffic | Similarweb, 2026, via secondary | Web visits to the AI sites, not referrals |
| B2B referral mix: ChatGPT 62.6%, Claude 18.5%, Gemini 10.6%, Perplexity 7.3% | B2B study blending GA4 and Similarweb, 2026 | Single study, vendor |
| From 2026-05-07, ChatGPT referrals landing on homepages rose from about 26 to 32% to about 60% | Similarweb, 2026-05 | Likely a UI linking change |
| AI referrals typically under 1% of total site sessions | Multiple 2025 to 2026 analyses [Practitioner consensus] | Undercounted: app traffic often arrives without a referrer |
| AI search visitors converted 23 times better than organic on Ahrefs' own site | Ahrefs, 2025-06 | Single site, small volume |
| AI search visitor projected 4.4 times as valuable as an organic visitor | Semrush, 2025-06 | Modeled projection |

Rule: report AI referral conversion rates from the project's own GA4 data. Quote vendor multipliers only with their caveats.

## 5. Variance evidence

1. SparkToro and Gumshoe (2026, fieldwork 2025-11 to 2025-12): about 600 volunteers, 12 prompts, 2,961 responses across ChatGPT, Claude and Google AI. Less than 1 in 100 chance of the same brand list twice; under 0.1% for the same list in the same order. A consistent core of top brands still appeared. Not peer reviewed; partner sells tracking [Study, 2026].
2. Consequence: "AI rank position" is not a stable metric. Report mention rate, citation share and share of voice with sample sizes and intervals.

## 6. Contested topics (present both sides)

| Topic | Side A | Side B | Agent position |
|-------|--------|--------|----------------|
| "GEO is just SEO" | Google says no special optimization is needed beyond SEO fundamentals [Official, 2025] | Off-site mentions, passage structure, non-Google indexes (ChatGPT's own index), and prompt-level measurement are distinct work [Study, 2026] | SEO is the foundation and covers most of Google AI. ChatGPT, Perplexity, Claude and brand-mention work need additional effort |
| Schema for AI | Correlation studies show cited pages often have schema | Google says it is not required; no controlled test shows citation lift | Do it for entity clarity and rich results; never sell it as an AI lever |
| Reddit as a lever | Reddit is among the most cited domains | Reddit citations swing with platform deals and retrieval changes; manipulation risk is high | Genuine participation only; diversify sources |
| Does AI traffic convert better? | Single-site and modeled studies say yes | Self-selection; brand-aware users; small samples | Measure in own data |
| Should brands allow training crawlers? | Allowing GPTBot, ClaudeBot, CCBot, Google-Extended grows future parametric recall [Practitioner consensus] | Publishers lose licensing leverage and traffic | Brands selling products: usually allow. Publishers: decide by licensing strategy |
| Opting out of Google AI features | Protects content value for some publishers | Loses AI impressions and traffic; may affect Top Stories inside AIO [Unverified]; competitors fill the gap | Default Include. Exclude only after a modeled decision and with approval |
| Top-10 overlap | 76% (Ahrefs 2025, AIO) | About 12% (Moz 2026, AI Mode) | Overlap is falling as fan-out widens. Track sub-query rankings |
| Brand vs community sources | Yext: 86% brand-controlled sources | OtterlyAI: 52.5% community platforms | Depends on prompt type and category; measure your own |

## 7. How to read a GEO study (checklist before quoting)

1. Which engine, which mode (free, paid, logged-out), which country and language?
2. When was data collected? Anything older than six months may be stale.
3. What is the metric (mention, citation, position-weighted share)? Different metrics are not comparable.
4. Sample size per engine and per prompt, and how prompts were chosen (vendor prompt sets skew to their customers' categories).
5. Correlation or experiment? Who sells what based on the result?
6. Does it control for brand size? Big brands get more mentions, links and AI visibility at the same time.
7. Is the result replicated by an independent source?
8. Label it in deliverables with [Study, YYYY-MM] and one line of caveat.

## 8. What would change these grades

| If this appears | Then |
|-----------------|------|
| An engine documents llms.txt use | Raise llms.txt to "do for all sites" |
| A controlled test shows schema lifts citations on a live engine | Raise schema grade for that engine |
| OpenAI publishes its index or a webmaster tool | Prioritize that data over third-party trackers |
| Google adds clicks or queries to the Generative AI report | Rebuild the reporting template around it |
| An engine adds paid placement inside organic answers without labels | Flag as a policy risk in deliverables |

## 9. Lever emphasis by engine (where effort pays most)

Weights are practitioner judgments built from the evidence above [Practitioner consensus]. Use them to split effort, then let the project's own tracking data override them.

| Lever | Google AIO and AI Mode | ChatGPT free | ChatGPT paid | Perplexity | Copilot | Claude | Gemini app |
|-------|-----------------------|--------------|--------------|------------|---------|--------|-----------|
| Crawl access for the engine's bots | Required | Required | Required | Required | Required | Required | Required (Googlebot plus Google-Extended) |
| Google rankings for sub-queries | Very high | Low | High | Medium | Low | Unknown | Very high |
| Bing rankings and indexing | Low | Low | Low | Low | Very high | Unknown | Low |
| Third-party mentions on cited domains | High | Very high | High | High | High | High | High |
| Answer-first passages and specific facts | High | High | High | High | High | High | High |
| Freshness of decision pages | Medium | High | Medium | High | Medium | Medium | Medium |
| Reviews on cited platforms | Medium | High | High | Medium | Medium | Medium | Medium |
| Reddit and forum presence | Medium | Low to medium (volatile) | Medium | High | Low | Unknown | Medium |
| YouTube with transcripts | High | Medium | Medium | Medium | Low | Low | High |
| Wikipedia and Wikidata | Medium | High | High | Medium | Medium | Medium | Medium |
| Structured data | Low to medium | Unknown | Low | Unknown | Medium | Unknown | Low to medium |
| llms.txt | None | None | None | None | None | None | None |

## 10. Benchmarks quick reference (always quote with caveat)

| Benchmark | Value | Source, date | Caveat |
|-----------|-------|--------------|--------|
| Same brand list on a repeated prompt | Under 1% | SparkToro and Gumshoe, 2026 | Not peer reviewed; volunteer settings |
| Position 1 CTR change with AI Overview | About 58% lower | Ahrefs, 2026-02 | AIO keywords only |
| Click rate with vs without AI summary | 8% vs 15% | Pew, 2025-07 | US panel |
| Cited vs uncited brand organic clicks on AIO SERPs | About 20,743 vs 9,445 per million impressions | Seer, 2026 | Secondary read; correlational |
| ChatGPT share of AI chatbot referrals | 79.4% | Statcounter, 2026-08 | Global panel, all sites |
| Gemini share of AI chatbot referrals | 10.9% | Statcounter, 2026-08 | Same |
| ChatGPT free-tier sources from own index | About 75% | Resoneo via Peec AI and SEL, 2026-07 | Vendor analysis; window ended 2026-07-21 |
| llms.txt files with zero requests | 97% | Ahrefs, 2026-05 | Secondary read |
| Branded mentions correlation with AIO visibility | 0.664 | Ahrefs, 2025 | Spearman, correlational |
| Domain overlap ChatGPT vs Perplexity | About 11% | Profound, 2025 | Similar prompts, dated |
| Pages cited by ChatGPT with structured data | 61% (vs 25% of Google top results) | AirOps via roundup, 2026 | Correlational, secondary |

Rule: compare the project with its own history first; use these only to frame expectations.
