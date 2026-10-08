# Playbooks by Business Model, plus the 90 Day Program

> Knowledge as of 2026-10. Plays are drafted as change lists. Nothing is published, changed on the site, or posted off-site without explicit human approval.

## 1. Core plays (all business models)

### Play 1: Launch (no AI visibility program yet)
1. Intake and cold start facts (see SKILL.md Intake).
2. Access audit: robots.txt, CDN or WAF, rendering, indexing in Google and Bing ([Technical](technical-access-and-crawlers.md)).
3. Brand fact sheet ([Entity](entity-and-brand-authority.md)).
4. Prompt set v1 and baseline collection ([Measurement](measurement-and-prompt-tracking.md)).
5. GA4 AI channel group requirement to `measurement`; verify Search Console and Bing Webmaster Tools.
6. Source map for top prompts ([Off-site](off-site-and-community-presence.md)).
7. Prioritized 90 day plan (section 2).

### Play 2: Optimize (program running)
1. Monthly: compare mention rate, citation share and SoV by engine and prompt class with intervals.
2. Pick the 3 to 5 prompt clusters with the highest commercial value and the largest gap to the leading competitor.
3. For each cluster decide the dominant lever: access, owned content, off-site sources, entity accuracy or commerce data.
4. Ship changes in batches per cluster so effects can be read (avoid changing everything at once).
5. Read results after 4 to 8 weeks; log learnings to the journal; confirmed patterns to memory.

### Play 3: Scale (visibility proven in core prompts)
1. Expand the prompt set to adjacent use cases, segments and markets (new cohort, keep the original frozen).
2. Industrialize content: templates for comparisons, alternatives, use case and local pages with real data per page (no thin programmatic pages).
3. Increase digital PR cadence around original data.
4. Add engines and languages.
5. Automate collection and reporting via tool APIs or MCP connectors.

### Play 4: Recover (visibility or AI traffic dropped)

Decision tree:
1. Did AI referral traffic drop while mention rate held? Check GA4 configuration, referrer changes, UI linking changes (for example the 2026-05-07 homepage shift), and tracking breaks. Hand off to `measurement`.
2. Did mention rate drop on one engine only?
   1. Check access for that engine's bots in logs and CDN (new WAF rule, Cloudflare default change on 2026-09-15, plugin update).
   2. Check model or product change in the Freshness sources (model update, index change).
   3. Check source mix shift: were the domains that mentioned you dropped by the engine (Reddit drop in ChatGPT in 2025-09 is the classic case)?
3. Did mention rate drop on all engines?
   1. Check Google and Bing rankings and indexing (site migration, noindex, canonical errors). Hand off to `seo`.
   2. Check for new negative coverage, reviews or a competitor's surge in mentions.
4. Did accuracy drop (wrong facts)? Run the misinformation workflow ([Entity](entity-and-brand-authority.md) section 8).
5. Write the recovery change list, get approval, re-test weekly.

### Play 5: Crisis (critical misinformation or safety claim)
1. Same day: capture, reproduce, escalate to the human with evidence.
2. Trace sources; fix owned pages; contact publishers; submit engine feedback.
3. Publish a clear, factual statement page if the issue is public.
4. Monitor daily for two weeks, then weekly.

## 2. The 90 day program

| Week | Workstream | Deliverables | Owner or handoff |
|------|-----------|--------------|------------------|
| 1 | Intake, access audit | Access findings and change list (robots.txt, CDN, rendering); fact sheet draft | This agent; `seo` for fixes |
| 1 | Measurement setup | GA4 AI channel spec; GSC and Bing WMT verification check; tracking tool selection or DIY plan | `measurement` |
| 2 | Prompt set and baseline | Prompt set v1 (frozen); baseline collection with intervals; competitor set | This agent |
| 2 to 3 | Source mapping | Cited domain classification; source opportunity table | This agent; `market-intel` for competitor depth |
| 3 | Entity hygiene | Organization schema spec, sameAs, Wikidata check, profile corrections list, review platform plan | This agent; `seo` for schema |
| 3 to 4 | Fan-out maps for top 20 prompts | Coverage sheet; content gap list | This agent |
| 4 | Plan approval | 90 day plan with ICE scores, experiments added to EXPERIMENTS.md | Human approves |
| 5 to 8 | Owned content sprint 1 | 4 to 10 page upgrades or new pages (pricing, comparisons, alternatives, category guide, stats page) | This agent drafts briefs; human editor; `seo` |
| 5 to 8 | Off-site sprint 1 | Correction outreach to cited lists; review request flow live; first PR pitch; community participation guidelines | This agent; human; `creative-strategy` for video |
| 6 | Mid-check | Access re-check; early movement on corrected facts | This agent |
| 8 | Monthly report 2 | Report with intervals; adjust priorities | This agent |
| 9 to 11 | Original data asset | Study design, data pull, HTML report, PR pitch list | This agent with human; `market-intel` |
| 9 to 12 | Owned content sprint 2 | Next 4 to 10 pages; refresh decision pages | This agent; `seo` |
| 12 | Quarterly review | Before vs after by engine and prompt class; learnings to memory; next quarter plan | This agent; `growth-orchestrator` |
| 13 | Prompt set v2 cohort | Add new prompts as a separate cohort | This agent |

Expected timelines [Practitioner consensus]: access fixes show in retrieval within days to weeks (OpenAI says about 24 hours for robots.txt changes) [Official]; owned content changes in 2 to 8 weeks; off-site mentions in 1 to 6 months; parametric recall in model generations (6 to 18 months).

## 3. Local services (plumbers, dentists, law firms, clinics, restaurants)

| Lever | Actions |
|-------|---------|
| Google Business Profile | Complete categories, services, hours, attributes, photos, products or services with prices, Q&A; weekly posts; respond to every review |
| Other local data sources | Bing Places (Copilot), Apple Business Connect (Siri, Apple Maps), Yelp, BBB, industry directories (Avvo, Healthgrades, Angi, TripAdvisor) as cited in your prompts |
| NAP consistency | Identical name, address, phone across all listings and the site |
| Reviews | Steady velocity from all customers; responses that mention the service and location naturally |
| Location and service pages | One page per real location; service pages with price ranges, process, licenses, service area, FAQs in visible text |
| Local mentions | Local news, sponsorships, community organizations, local "best of" lists |
| Prompts to track | "best <service> in <city>", "<service> near <neighborhood> open now", "how much does <service> cost in <city>", "<brand> reviews" |

Evidence note: local AI answers draw heavily on map and review data [Practitioner consensus]. ChatGPT's own index reportedly includes a local listings category [Study, 2026-07, Unverified detail].

## 4. Ecommerce

| Lever | Actions |
|-------|---------|
| Product data | Hand off to `commerce-feeds`: Merchant Center, ACP feed, UCP readiness, attribute completeness |
| Product and category pages | Standard in [Agentic commerce](agentic-commerce-visibility.md) section 4 |
| Buying guides and comparisons | Constraint-heavy guides ("for wide feet", "for small kitchens") with tables |
| Reviews | Product reviews with use-case language; Trustpilot or Google seller ratings |
| Third-party | Editorial reviews, YouTube creator reviews, Reddit presence, Amazon listing quality |
| Prompts to track | Shopping prompts by category, budget and attribute; "<brand> vs <brand>"; "is <brand> good quality" |

## 5. B2B SaaS

| Lever | Actions |
|-------|---------|
| Pricing transparency | Public pricing or clear ranges; LLMs say "pricing not available" otherwise and favor transparent competitors [Practitioner consensus] |
| Comparison and alternatives pages | For top 5 to 10 competitors, honest and dated |
| Use case and industry pages | One per real segment with customer proof |
| Docs and help center | Crawlable, server-rendered, versioned; consider llms.txt for docs only (low cost, low evidence) |
| Review platforms | G2, Capterra, TrustRadius, Gartner Peer Insights by category; review velocity program |
| Integrations | Integration directory pages; listings in partners' marketplaces |
| Community | Reddit, LinkedIn executive posts, YouTube demos, podcasts with transcripts |
| Original data | Benchmarks from product usage data (anonymized aggregates) |
| Prompts to track | "best <category> for <segment>", "<competitor> alternatives", "<brand> vs <competitor>", "<brand> pricing", "how to <job to be done>" |

## 6. B2B services and lead gen (agencies, consultancies, financial and professional services)

| Lever | Actions |
|-------|---------|
| Expertise pages | Service pages with process, pricing models, typical outcomes with numbers, credentials |
| Case studies | Numbers, client names where allowed, dates; ideally also published by the client |
| Directories | Clutch, G2 services, industry associations, partner directories as cited |
| Thought leadership | Original research, named expert commentary in trade media, podcasts |
| LinkedIn | Executive posts with specific insight; company page facts |
| Prompts to track | "best <service> firm for <industry>", "how much does <service> cost", "<brand> reviews" |

Regulated services (financial, legal, health): every claim on the site and in pitches needs compliance approval; accuracy monitoring is critical.

## 7. Content publishers

| Decision | Guidance |
|----------|---------|
| Allow AI search bots? | Usually yes for citation traffic and brand; measure referral value |
| Allow training bots? | Licensing decision; consider Cloudflare pay per crawl or Pay Per Use, direct licensing, or blocking |
| Google Search generative AI control | Default Include. Exclude only after modeling lost AI impressions and possible side effects (Top Stories inside AI Overviews reported [Unverified]) and with approval |
| Google AI Contribution pilot | Google confirmed (2026-09) an invitation-only Search Console pilot paying about 100 publishers when their content contributes to AI Overviews, AI Mode and Gemini; an AI earnings widget shows monthly amounts; formula and per-page detail not disclosed; declining payment does not remove content from AI features [Official, 2026-09] (Search Engine Land, Digiday). Monitor for an invitation; do not treat it as a reason to stay in or opt out |
| Content strategy | Original reporting, data, expert analysis, tools; commodity explainers lose the most clicks to AI answers |
| Measurement | Citation share in your topics, AI impressions in GSC, referral sessions and revenue per AI session |

## 8. Apps

| Lever | Actions |
|-------|---------|
| App store listings | Clear use case language, screenshots with captions, recent ratings, responses to reviews |
| Web presence | Landing pages per use case with server-rendered text; comparison pages |
| Third-party | "Best apps for X" lists, YouTube reviews, Reddit |
| Deep links | Ensure links from AI answers open the right screen or store page |
| Prompts | "best app for <job>", "<app> vs <app>", "is <app> safe" |

## 9. Marketplaces

| Lever | Actions |
|-------|---------|
| Two-sided prompts | Track demand-side ("where to hire a <pro>") and supply-side ("best platform to sell <x>") prompts |
| Category and location pages | Real inventory counts, prices, reviews per page; avoid thin programmatic pages |
| Trust | Policies, guarantees, fees explained in text |
| Third-party | Reviews of the marketplace, press, Reddit |

## 10. Adaptation by budget tier (effort and tooling)

Tiers follow the Ads Master standard (monthly paid media budget as a proxy for company scale).

| Tier | Tracking | Content cadence | Off-site | Reporting |
|------|----------|-----------------|----------|-----------|
| Starter (under $3k) | DIY or entry tool, 25 to 50 prompts, 2 to 3 engines | 2 to 4 page upgrades per month | Reviews program, corrections, 1 community channel | Monthly one-page |
| Growth ($3k to $30k) | Paid tool, 50 to 150 prompts, 4 to 5 engines | 4 to 8 per month plus 1 data asset per quarter | PR monthly, listicle outreach, YouTube | Monthly report |
| Scale ($30k to $300k) | Enterprise tool or API pipeline, 150 to 500 prompts, multi-geo | Content program with templates and data | PR retainer, creator program, analyst relations | Monthly plus weekly alerts |
| Enterprise (over $300k) | 500 to 5,000 prompts, all markets, API and dashboards | Multi-team content operations | Global PR, governance for misinformation | Weekly dashboards, quarterly business review |

## 11. Adaptation by maturity

| Maturity | Focus |
|----------|-------|
| New (no baseline) | Access, fact sheet, baseline, quick wins (pricing page, comparisons, corrections) |
| Running | Cluster-by-cluster optimization with clean reads |
| Plateau | Source mapping refresh, original data, new formats (video), new engines; check whether competitors gained mentions on key cited domains |
| Scaling | New markets and languages, automation, governance |
