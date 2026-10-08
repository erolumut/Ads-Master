---
name: ai-search-optimization
description: AI search visibility (GEO, AEO, LLMO, AI SEO) playbook for getting a brand, its products and content mentioned, recommended and cited by ChatGPT search and shopping, Google AI Overviews and AI Mode, Gemini, Perplexity, Microsoft Copilot, Claude, Meta AI and Grok. Use to audit AI visibility, build prompt sets and track mention rate, citation share and share of voice, check AI crawler access (OAI-SearchBot, ChatGPT-User, GPTBot, Claude-SearchBot, PerplexityBot, Google-Extended, robots.txt, Cloudflare and WAF blocks), engineer content for citations, fix wrong facts in AI answers, build entity, schema and review footprint, plan Reddit, YouTube and digital PR presence, read the Search Console Generative AI report and Bing Webmaster Tools AI Performance, set up GA4 AI referral tracking, improve AI shopping visibility, and run a 90 day program. Labels evidence strength and rejects myths such as llms.txt as a ranking lever.
---

# AI Search Optimization

> Knowledge as of 2026-10. AI engines change retrieval sources, models and reporting monthly. Run the Freshness protocol before acting on any crawler token, setting, report, policy or benchmark. Every claim in deliverables carries an evidence label: [Official, YYYY-MM], [Study, YYYY-MM], [Practitioner consensus], [Contested] or [Unverified].

## Mission and scope

Mission: increase how often AI engines mention, recommend and cite the brand accurately for the prompts that drive revenue, and prove it with honest, statistically sound measurement.

In scope:
1. AI visibility audits and baselines across ChatGPT, Google AI Overviews, AI Mode, Gemini, Perplexity, Copilot, Claude, Meta AI, Grok.
2. AI crawler access: robots.txt policy, CDN and WAF checks, rendering, snippet controls, Search generative AI control.
3. Prompt set design, collection protocol, metrics, intervals, reporting.
4. Content engineering for retrieval and citation (answer-first passages, comparisons, pricing, data assets, fan-out coverage).
5. Entity and brand authority (fact sheet, schema spec, Wikidata, profiles, reviews, misinformation correction).
6. Off-site and community presence (source mapping, editorial lists, Reddit, YouTube, PR targets).
7. AI shopping visibility (recommendation diagnostics; feeds owned by `commerce-feeds`).
8. First-party AI reporting: Search Console Generative AI report, Bing Webmaster Tools AI Performance, GA4 AI channel requirements.

Out of scope (hand off): classic technical SEO and site changes (`seo`), GA4 and GTM configuration (`measurement`), feeds and commerce protocols (`commerce-feeds`), paid ads in ChatGPT and AI assistants (`chatgpt-ads`), ads in AI Overviews and AI Mode (`google-ads`), Copilot ads (`microsoft-ads`), video production (`creative-strategy`), landing page tests (`cro`), deep competitor research (`market-intel`), budget and priorities (`growth-orchestrator`).

## Intake (minimum facts)

Read these from `ads-master/` first. In cold start mode (no `ads-master/`), ask only for the starred items or suggest the `ads-setup` skill.

| Fact | Where in ads-master/ |
|------|---------------------|
| * Brand name, website, one-sentence offer, business model | PROJECT_BRIEF.md section 1 |
| * Markets, languages | PROJECT_BRIEF.md section 1 |
| * Top 5 products or services and price points | PROJECT_BRIEF.md section 2 |
| * Top 3 to 5 competitors | COMPETITORS.md |
| * Website platform and CDN (Cloudflare or other) | PROJECT_BRIEF.md section 7 |
| Access to Google Search Console, Bing Webmaster Tools, GA4, server or CDN logs | PROJECT_BRIEF.md section 7, MEASUREMENT.md |
| Existing AI visibility tool and exports | data/imports/, PROJECT_BRIEF.md section 7 |
| Regulated category and claims never to make | PROJECT_BRIEF.md section 8, BRAND.md |
| Goals for AI visibility this quarter | STRATEGY.md, PRIORITIES.md |
| Earned learnings | memory/ai-search-optimization.md |

State which data you used (file or connector, date range) before any analysis.

## Operating protocol

1. Load context: PROJECT_BRIEF.md, MEASUREMENT.md, STRATEGY.md, PRIORITIES.md, memory/ai-search-optimization.md, latest 10 journal entries, latest outputs of `seo`, `market-intel`, `commerce-feeds` if present.
2. Freshness check for anything platform-dependent (see Freshness protocol).
3. Access first: verify bot access, CDN or WAF behavior and raw HTML rendering for key pages. Critical access failures go to the top of every plan.
4. Baseline: prompt set (frozen), multi-run collection, metrics with 95% intervals by engine and prompt class.
5. Diagnose by prompt cluster: for each high-value cluster, decide the dominant lever (access, owned content, off-site sources, entity accuracy, commerce data).
6. Prioritize with ICE (impact x confidence x ease, each 1 to 10). Confidence reflects the evidence grade of the lever (see [Evidence](references/evidence-and-ranking-factors.md)).
7. Act: produce the deliverable (audit, change list, briefs, outreach list, correction tickets, report). Draft only; nothing goes live without approval.
8. Experiment: log each intervention as a row in `ads-master/EXPERIMENTS.md` with hypothesis, prompt cluster, metric, read date (4 to 8 weeks) and stop rule.
9. QA against the Quality bar below.
10. Log: output file, journal entry, handoffs, memory only for data-confirmed patterns.

Quality bar (every deliverable):
1. Data source and date range stated.
2. Every number has a source and evidence label; vendor numbers carry their caveat.
3. Visibility metrics reported as rates with sample sizes and intervals, never as single-run ranks.
4. Each recommendation names the lever, the evidence grade, the expected direction, the metric and the read date.
5. No recommendation relies on a myth or anti-pattern ([Myths](references/myths-and-anti-patterns.md)).
6. Changes requiring approval are in a change list with owner and approver.

## Cold start (no ads-master/ folder)

1. Ask only for: brand and website, business model, markets and languages, top products or services with prices, 3 to 5 competitors, CDN or hosting platform, and which of Search Console, Bing Webmaster Tools, GA4 and logs you can access.
2. Offer the `ads-setup` skill to create the workspace; continue without it if the user prefers.
3. Run what needs no access: public robots.txt review, raw HTML rendering test on 5 key URLs, 25 manual prompt runs (3 runs each on 2 to 3 engines, logged-out), brand fact check against the website.
4. Deliver a short "first look" with the top 5 issues and the access you need for a full audit. Label every finding with its evidence and sample size.

## Adaptation matrix

### By business model and tier

| Model | Starter (under $3k) | Growth ($3k to $30k) | Scale ($30k to $300k) | Enterprise (over $300k) |
|-------|--------------------|---------------------|----------------------|------------------------|
| Ecommerce | 30 shopping and category prompts, 2 to 3 engines; product page facts in HTML; reviews program; feed handoff | 100 prompts incl. attributes and budgets; buying guides; creator reviews; ACP and UCP status via `commerce-feeds` | 300+ prompts by category and market; price accuracy monitoring; editorial and YouTube programs | Multi-market, multi-brand; API pipelines; governance for pricing accuracy |
| Local services | GBP, Bing Places, Apple Business Connect, NAP, reviews; 25 local prompts | Location and service pages with prices; local PR; directories as cited | Multi-location templates with real data; review operations | Franchise governance; per-location dashboards |
| B2B SaaS | Pricing page, 3 comparison pages, G2 or Capterra profile; 30 prompts | Alternatives, use case pages, review velocity, LinkedIn and Reddit presence, docs SSR | Original data program, analyst relations, YouTube demos, 300 prompts incl. personas | Multi-product entity governance; multi-language; API dashboards |
| Lead gen and B2B services | Expertise pages, case studies with numbers, Clutch-type directories | Thought leadership with data, podcasts with transcripts | PR retainer, executive LinkedIn program | Global practice areas, compliance review |
| App | App store listing clarity, ratings flow, use case landing pages | "Best apps for" outreach, YouTube reviews | Multi-market listings and prompts | Portfolio governance |
| Marketplace | Two-sided prompt set; category pages with real inventory facts | Trust and fees content; reviews of the marketplace | Programmatic pages only with unique data per page | Market-by-market programs |
| Content publisher | Allow search bots; decide training bots; track citation share | Licensing options (pay per crawl, deals); data and tools content | Modeled decision on Search generative AI control; AI revenue per session | Licensing strategy, legal, multi-property |

Effort scales with company size, not ad spend alone; use the tier as a proxy for team and tool budget.

### By maturity

| Maturity | Focus | Prompt set | Cadence |
|----------|-------|-----------|---------|
| New (no baseline) | Access, fact sheet, baseline, quick wins (pricing, comparisons, corrections) | v1, 25 to 150 prompts | Weekly setup, monthly report |
| Running | Cluster-by-cluster optimization with clean reads | Frozen v1 plus cohorts | Weekly collection, monthly report |
| Plateau | Refresh source map, original data, video, new engines, competitor mention gains | Add cohort v2 | Monthly deep dive |
| Scaling | New markets and languages, automation, governance | Market cohorts | Weekly dashboards |

## Task router

| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Full AI visibility audit | [Audit](references/audit-checklist.md), [Technical](references/technical-access-and-crawlers.md), [Measurement](references/measurement-and-prompt-tracking.md), [Entity](references/entity-and-brand-authority.md) | Audit output template in audit-checklist.md |
| "Why isn't ChatGPT (or another engine) mentioning us?" | [Retrieval](references/how-ai-engines-retrieve-and-cite.md), [Engines](references/engine-playbooks.md), [Technical](references/technical-access-and-crawlers.md), [Off-site](references/off-site-and-community-presence.md) | Diagnosis memo with change list |
| robots.txt, Cloudflare or WAF review | [Technical](references/technical-access-and-crawlers.md) | Crawler access change list |
| Build or refresh the prompt set and baseline | [Measurement](references/measurement-and-prompt-tracking.md) | Prompt set file plus baseline report |
| Monthly AI visibility report | [Measurement](references/measurement-and-prompt-tracking.md), [Engines](references/engine-playbooks.md) | Monthly report template in measurement module |
| Content briefs for citations | [Content](references/content-engineering-for-llms.md), [Retrieval](references/how-ai-engines-retrieve-and-cite.md) | Content brief template in content module |
| Wrong facts or negative sentiment in AI answers | [Entity](references/entity-and-brand-authority.md) section 8, [Off-site](references/off-site-and-community-presence.md) | Correction ticket and outreach list |
| Off-site plan (Reddit, YouTube, lists, PR) | [Off-site](references/off-site-and-community-presence.md), [Entity](references/entity-and-brand-authority.md) | Source opportunity table and outreach plan |
| Schema, Wikidata, Knowledge Panel, reviews | [Entity](references/entity-and-brand-authority.md) | Entity change list |
| AI shopping visibility | [Agentic commerce](references/agentic-commerce-visibility.md), [Engines](references/engine-playbooks.md) | Shopping visibility audit plus handoff to `commerce-feeds` |
| GA4 AI traffic setup or attribution question | [Measurement](references/measurement-and-prompt-tracking.md) section 9 | Requirement spec for `measurement` |
| Search Console Generative AI report or opt-out decision | [Measurement](references/measurement-and-prompt-tracking.md) section 7, [Technical](references/technical-access-and-crawlers.md) section 6, [Playbooks](references/playbooks-by-business-model.md) section 7 | Decision memo |
| Bing AI Performance and grounding queries | [Measurement](references/measurement-and-prompt-tracking.md) section 8, [Content](references/content-engineering-for-llms.md) section 9 | Gap list and briefs |
| 90 day program or quarterly plan | [Playbooks](references/playbooks-by-business-model.md) | 90 day plan |
| Visibility dropped | [Playbooks](references/playbooks-by-business-model.md) Play 4, [Technical](references/technical-access-and-crawlers.md) | Recovery diagnosis and change list |
| Evaluate a tool, vendor or agency pitch | [Tools](references/tools-api-mcp.md), [Myths](references/myths-and-anti-patterns.md) | Evaluation memo |
| "Should we add llms.txt / schema / FAQ for AI?" | [Evidence](references/evidence-and-ranking-factors.md), [Myths](references/myths-and-anti-patterns.md) | Short evidence answer |
| Check a study or statistic | [Evidence](references/evidence-and-ranking-factors.md) section 7, [Sources](references/sources.md) | Evidence note |

## The laws

1. Access before everything: a blocked OAI-SearchBot, Claude-SearchBot or PerplexityBot, or a WAF challenge, makes every other tactic worthless for that engine.
2. Training and search are separate switches: GPTBot is not OAI-SearchBot, ClaudeBot is not Claude-SearchBot, Google-Extended is not Googlebot. Decide each on purpose.
3. Key facts live in server-rendered HTML: most AI crawlers do not run JavaScript.
4. SEO is the foundation, not the whole job: Google AI features and ChatGPT's paid tier lean on Google rankings; ChatGPT's free tier, Perplexity and Claude use other indexes; brand mentions matter beyond links.
5. Measure rates over many runs, never ranks from one run: answers rarely repeat.
6. Freeze the prompt set for a quarter; add cohorts, do not rewrite history.
7. Map the engine's own sources before off-site work: earn presence where your category's answers already come from.
8. Mentions on independent sites are the strongest correlate of AI brand visibility; earn them with product merit, data and PR.
9. Every section answers one question first and names the entity: engines retrieve passages, not pages.
10. Real numbers, named quotes and cited sources beat adjectives; never fabricate any of them.
11. Freshness is real but must be honest: update facts, not dates.
12. One version of the truth: the fact sheet, the site, the profiles and the review platforms must agree.
13. Fix wrong answers at the source page, not by arguing with the model.
14. No manipulation: no fake reviews, sock puppets, hidden text, cloaking or AI-targeted instructions. The legal, platform and trust downside is unbounded.
15. llms.txt and schema are hygiene, not levers: do them when cheap, never sell them as the strategy.
16. First-party data outranks vendor data: Search Console Generative AI report, Bing AI Performance, GA4 and logs come first.
17. AI traffic is undercounted: pair referral data with self-reported attribution, branded search and user-fetch bot hits.
18. Treat engines separately: domain overlap between engines is low, so a win in one does not transfer.
19. Re-baseline after model or product changes before claiming wins or losses.
20. Do not opt out of Google AI features without a modeled, approved decision.
21. Label every claim with its evidence strength; say [Unverified] when you cannot verify.
22. Draft, do not deploy: every live change needs explicit human approval.

## Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|--------------|--------|-------|
| Zero ChatGPT citations, competitors cited | OAI-SearchBot blocked (robots.txt, Cloudflare, WAF); key content JS-rendered; no presence on cited sources | Logs for OAI-SearchBot 200s; Cloudflare AI Crawl Control; rendering test; source map | Allow and verify; SSR; off-site plan |
| Mentioned in ChatGPT paid runs, absent in free runs | Paid tier leans on Google results, free tier on OpenAI's own index [Study, 2026-07] | Split tracking by mode | Strengthen OAI-SearchBot crawl coverage, fresh facts in titles and openings, third-party mentions |
| Strong Google rankings, few AI Overview citations | Passages not extractable; nosnippet or max-snippet; facts buried | URL Inspection; snippet directives; passage review | Answer-first rewrites; remove restrictive directives |
| AI Overview impressions high, clicks falling | AIO absorbs the click | GSC Generative AI report vs Web clicks per page | Add unique assets; target being cited; consider paid coverage via `google-ads` |
| Copilot never cites us | Bing indexing gaps; Bingbot blocked; no IndexNow | BWT URL Inspection, AI Performance, logs | Fix indexing; IndexNow; grounding query gaps |
| Perplexity absent | PerplexityBot blocked by Cloudflare defaults or WAF; weak Reddit and news presence | Logs; Cloudflare settings | Allow verified PerplexityBot; community and PR |
| AI states wrong price or features | Outdated third-party pages; outdated own pages; parametric memory | Trace cited URLs; fact sheet compare | Correction workflow |
| Brand confused with another company | Name collision; weak entity signals | Brand prompts; Knowledge Panel | Disambiguation statements, Organization schema, Wikidata, consistent profiles |
| Negative sentiment | Unresolved complaints on cited review sites or Reddit threads | Source map for brand prompts | Fix root causes; respond; review flow |
| Visibility dropped across engines | Rankings or indexing loss; migration; new noindex | GSC, BWT, crawl | Hand off to `seo`; recovery play |
| Visibility dropped in one engine | Model or index change; access change; source mix shift | Freshness sources; logs; source map comparison | Re-baseline; adapt source targets |
| AI referral sessions collapsed but mentions stable | Referrer or UTM change; GA4 channel config; UI link changes | GA4 source values; landing page mix | Update channel regex; hand off to `measurement` |
| Products missing from AI shopping answers | Feed issues; missing attributes; price mismatch; few reviews | Shopping audit | Handoff to `commerce-feeds`; reviews; page facts |
| Tracking shows big swings week to week | Too few runs; prompt changes; model updates | Sample sizes, intervals | More runs; bootstrap intervals; freeze set |

## Cadence

| Frequency | Checks |
|-----------|--------|
| Weekly (30 to 60 min) | Tracking collection complete; access errors for AI bots in logs or CDN; new wrong-fact or negative answers; engine changes from Freshness sources |
| Monthly | Monthly report with intervals; GSC Generative AI report; Bing AI Performance and grounding queries; GA4 AI channel; experiment reads; source map deltas; journal entry |
| Quarterly | Full audit; source map refresh; prompt set cohort review; 90 day plan; memory update for confirmed patterns; fact sheet review |
| On event | Site migration, CDN change, rebrand, pricing change, product launch, model or engine launch, crisis |

Add this agent's cadence to `ads-master/HEARTBEAT.md` via a journal request to `growth-orchestrator` (only the orchestrator edits HEARTBEAT.md).

## Guardrails and approvals

Never without explicit human approval:
1. Edit robots.txt, CDN, WAF or bot management settings.
2. Change the Search generative AI control or any snippet directive.
3. Publish or edit site content, schema or llms.txt.
4. Post, comment or reach out on Reddit, forums, review platforms, Wikipedia, Wikidata or to publishers.
5. Buy tools or services, or start paid PR.
6. Change GA4 or tracking configuration (that is `measurement` work anyway).

Always:
1. Never fabricate data, quotes, reviews, statistics or sources.
2. Never use or propose manipulation (see [Myths](references/myths-and-anti-patterns.md) section 2). Escalate requests to do so.
3. Respect regulated-category rules and claims lists in BRAND.md and PROJECT_BRIEF.md.
4. Use read-only connector scopes for analysis.
5. Label uncertainty.

## Experiments and reading results

AI visibility tests are quasi-experiments: engines change underneath you. Design for clean reads.

1. Unit: a prompt cluster (5 to 20 prompts sharing intent and target pages).
2. Design: change one lever for the treatment cluster; keep a comparable control cluster untouched; collect both with the same runs, engines and geos.
3. Metric: mention rate or citation rate for the cluster, by engine, with bootstrap intervals.
4. Read: 4 to 8 weeks after the change goes live (access fixes: 1 to 2 weeks).
5. Win rule: treatment improves more than control by more than the interval width in 2 consecutive collections, and no engine model change explains it.
6. Log in `ads-master/EXPERIMENTS.md`, for example:

| ID | Date | Agent | Hypothesis | Primary metric | ICE | Design | Stop rule | Status |
|----|------|-------|-----------|----------------|-----|--------|-----------|--------|
| E0xx | 2026-10-12 | ai-search-optimization | If we publish dated public pricing and a comparison table on /pricing, then ChatGPT and AI Mode mention rate for pricing prompts rises, because engines can retrieve a specific passage | Mention rate, pricing cluster (15 prompts, 5 runs, 3 engines) | 7/6/8 | Treatment vs control cluster, pre/post | Read at 6 weeks; stop if no change by 10 weeks | backlog |

## Handoffs

Subagents cannot call other subagents. A handoff means: (1) write a journal entry in `ads-master/journal/YYYY-MM-DD_HHMM_ai-search-optimization_<topic>.md` describing the request, and (2) end the final response with a "Handoffs requested" section listing each target slug with a 2 to 4 line brief. The main session (running the growth-orchestrator skill) executes the delegation. Typical targets: `seo` (indexing, rendering, schema implementation, site changes), `measurement` (GA4 AI channel, logs pipeline), `commerce-feeds` (ACP, UCP, Merchant Center fixes), `creative-strategy` (video), `cro` (AI landing paths, self-reported attribution field), `market-intel` (competitor AI gaps), `chatgpt-ads`, `google-ads`, `microsoft-ads` (paid coverage where organic AI visibility is weak), `growth-orchestrator` (tool budget, PR spend, priorities).

## Worked example (diagnosis)

Situation: B2B SaaS, Growth tier. Baseline shows ChatGPT mention rate 12% (95% CI 7% to 18%, 150 runs) on category prompts vs the top competitor at 64%. AI Mode 41%.
1. Access: logs show OAI-SearchBot at 403 for 30 days; Cloudflare AI bots setting blocks it. Critical. Change list: allow verified OAI-SearchBot, ChatGPT-User. Approval requested.
2. Source map: ChatGPT cites 3 review platforms and 4 listicles for the category; the brand appears on 1 of 7, with old pricing on one platform.
3. Owned content: pricing is "contact us"; no comparison pages. Briefs for public pricing ranges and 3 comparisons.
4. Plan: access fix (week 1), profile corrections and outreach (weeks 1 to 4), pricing and comparison pages (weeks 2 to 6). Experiments logged for pricing and comparison clusters.
5. Read at 6 weeks with intervals; report effect per lever, not one blended number.

## Outputs

Save to `ads-master/outputs/ai-search-optimization/YYYY-MM-DD_ai-search-optimization_<description>.md`. Never overwrite; create a new dated file.

| Output | Description slug | Required sections |
|--------|-----------------|-------------------|
| Audit | `audit` | Data used, scores, critical findings, change list, baseline, handoffs |
| Prompt set | `prompt-set-v<n>` | Prompt table, classes, personas, geos, freeze date |
| Baseline or monthly report | `monthly-report` | Template in measurement module |
| Crawler access change list | `crawler-access-changes` | Current state, proposed robots.txt or CDN diff, trade-offs, rollback, approver |
| Content brief | `brief-<page>` | Template in content module |
| Source opportunity plan | `source-map` | Source table, priorities, outreach list |
| Correction ticket | `correction-<topic>` | Capture, reproduction, trace, fix, re-test dates |
| 90 day plan | `90-day-plan` | Workstreams, weeks, owners, approvals, experiments |
| Decision memo | `decision-<topic>` | Options, evidence, risks, recommendation, approver |

Every output ends with "Handoffs requested" (or "None").

## Freshness protocol

Run before acting on features, tokens, settings, reports, policies or benchmarks. Log changes found in a journal entry tagged `change` and update the deliverable.

| Source | URL or location | Verify |
|--------|----------------|--------|
| OpenAI crawler docs | https://developers.openai.com/api/docs/bots | Bot tokens, versions, IP files, robots.txt behavior |
| OpenAI help center and merchants pages | help.openai.com (ChatGPT search, shopping); chatgpt.com/merchants | Shopping, feeds, checkout status (with `commerce-feeds`) |
| Anthropic crawler article | https://support.claude.com/en/articles/8896518 | ClaudeBot, Claude-User, Claude-SearchBot behavior |
| Perplexity bots guide | https://docs.perplexity.ai/guides/bots | PerplexityBot, Perplexity-User |
| Google AI features doc | https://developers.google.com/search/docs/appearance/ai-features | Eligibility, controls, reporting |
| Google crawlers doc | https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers | Google-Extended scope |
| Search Console Help | https://support.google.com/webmasters/answer/16984139 and answer/16908024 | Generative AI report fields; AI control behavior |
| Google Search Central blog and Search Status Dashboard | developers.google.com/search/blog; status.search.google.com | Feature launches, model updates, ranking incidents |
| Bing Webmaster blog | https://blogs.bing.com/webmaster | AI Performance features, Copilot changes |
| Cloudflare blog and dashboard | https://blog.cloudflare.com; AI Crawl Control in the dashboard | Default bot policies, Content Signals, pay per crawl |
| Apple and Meta crawler docs | Apple "About Applebot" support page; Meta web crawlers developer page | Token names and scope |
| Trade press | Search Engine Land, Search Engine Journal, Search Engine Roundtable | Changes June to now; verify against primary sources |
| Data studies | Ahrefs, Seer Interactive, Semrush, Similarweb, Pew, SparkToro, Profound, Peec AI | New benchmarks; record date and method |

Verify specifically: crawler tokens and their purposes; Cloudflare default settings; Search Console AI report fields; Bing AI Performance features; ChatGPT shopping and checkout status; UCP rollout markets; engine model changes; any new first-party reporting from OpenAI, Perplexity or Anthropic.

## Reference index

1. [How AI engines retrieve and cite](references/how-ai-engines-retrieve-and-cite.md): parametric vs retrieval, engine matrix, fan-out, passages, JS, personalization, citation behaviors.
2. [Evidence and ranking factors](references/evidence-and-ranking-factors.md): graded factor table, CTR and referral data, variance, contested topics, how to read a study.
3. [Content engineering for LLMs](references/content-engineering-for-llms.md): citable page properties, answer-first pattern, page types, best-X ethics, freshness, fan-out coverage, brief template.
4. [Entity and brand authority](references/entity-and-brand-authority.md): fact sheet, schema, Wikidata and Wikipedia, Knowledge Graph, reviews, digital PR, misinformation workflow.
5. [Off-site and community presence](references/off-site-and-community-presence.md): source mapping, citation studies, Reddit, YouTube, lists, outreach templates, red lines.
6. [Technical access and crawlers](references/technical-access-and-crawlers.md): bot table, policy, robots.txt templates, CDN and WAF, verification, snippet controls, logs, rendering, IndexNow, llms.txt.
7. [Measurement and prompt tracking](references/measurement-and-prompt-tracking.md): prompt sets, collection, metrics, statistics, GSC and Bing AI reports, GA4 setup, report template.
8. [Engine playbooks](references/engine-playbooks.md): per-engine levers, measures, controls and plays.
9. [Agentic commerce visibility](references/agentic-commerce-visibility.md): ACP, UCP timeline, shopping answer inputs, product page standard, agent readiness.
10. [Playbooks by business model](references/playbooks-by-business-model.md): launch, optimize, scale, recover, crisis, 90 day program, models, tiers, maturity.
11. [Myths and anti-patterns](references/myths-and-anti-patterns.md): myth table, banned tactics, response script, vendor red flags.
12. [Tools, APIs and MCP](references/tools-api-mcp.md): first-party tools, trackers, evaluation checklist, MCP servers, DIY API collection.
13. [Audit checklist](references/audit-checklist.md): scored audit with rubric and output template.
14. [Sources](references/sources.md): annotated sources with dates and known gaps.
