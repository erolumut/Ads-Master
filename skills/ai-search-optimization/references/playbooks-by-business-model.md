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

## 8. Apps (mobile apps and games)

Ownership: `app-store-optimization` owns the store pages (metadata, screenshots, tags, review replies, review summary reports) and the App entity sheet. `mobile-app-growth` owns paid user acquisition, the MMP, deep links and paywalls. This agent owns how AI answers mention, recommend and describe the app: the app prompt panel, the source map, the AI-reader brief for store and website text, the website answer pages, and apps inside assistants ([Assistant apps](assistant-apps-and-connectors.md)).

### 8.1 Prompt classes for apps

| Class | Example prompts | What a good answer needs from you | Share of the app panel (house default) |
|-------|-----------------|-----------------------------------|----------------------------------------|
| Best X app for Y | "best habit tracker for iPhone", "best budgeting app for couples", "best offline map app for hiking" | Store listing and website state the job, audience, platforms and standout facts in plain text; presence on the lists engines cite | 30 to 40% |
| X vs Y | "Acme Habits vs Rival", "is Acme better than Rival on Android" | Honest, dated comparison page; identical prices everywhere | 10 to 15% |
| Is X safe or legit | "is Acme Habits safe", "does Acme sell my data", "is Acme a scam" | Privacy and security page in HTML that matches the store privacy labels; developer identity; support contact | 10 to 15% |
| X price | "how much is Acme premium", "is Acme free", "Acme yearly price" | Plans, prices per market and trial terms in HTML and in the store listing | 10% |
| Cancel X | "how to cancel Acme subscription", "Acme refund" | A help page with exact steps per platform (App Store, Google Play, web) | 5 to 10% |
| Alternatives to X | "apps like Rival", "free alternative to Rival" | Honest alternatives page; presence on the "alternatives" lists engines cite | 10 to 15% |

Add platform and market qualifiers (iPhone, iPad, Android, Apple Watch, country, language) as variants of a prompt, not as new classes. Games add "games like X", "best offline puzzle game", "is X pay to win".

Accuracy matters most in two classes. A wrong "cancel X" answer creates support load and complaints; a wrong "is X safe" answer (scam, data selling) is a Critical error under [Entity](entity-and-brand-authority.md) section 8.

### 8.2 The app source map

What ChatGPT cites for app prompts, from the only large study found [Study, 2026-05] (AppTweak; 125k+ ChatGPT responses to 9,489 app prompts and about 9k game prompts; US):

| Finding | Value |
|---------|-------|
| App Store and Google Play listings | About 47.5% of cited sources for app recommendations |
| Open web (sites, lists, reviews, forums) | About 27% |
| Answers with no citation | About 22.6% |
| By category | Wide spread: store listings about 65.8% of citations in Weather, about 29.3% in Food & Drinks |
| By list position | Citations fall with position: about 80 to 85% at the top position, under 25% by position 8 |

Caveats: a vendor study by an ASO tool company; US only; ChatGPT only; method partly undisclosed; one period. Use it for direction, then map your own category.

General citation studies disagree on the open web mix and none is app specific: Similarweb (2026-02) found Wikipedia 13.15% and Reddit 11.97% of ChatGPT browsing citations; Peec AI (2026-03) put Reddit, YouTube, LinkedIn and Wikipedia on top; Ahrefs (2025-06) put Wikipedia on top [Study, 2025 to 2026]. For software prompts, one press release says third-party best-of lists dominate and the vendor's own site gets about 12% [Unverified].

What no study shows yet: a link between store rating, review count or review recency and how often AI recommends an app. Do not promise one.

Procedure:
1. Run the app panel (8.1) and keep the cited URLs; `ai_prompt_panel.py` prints the most cited domains ([Measurement](measurement-and-prompt-tracking.md) section 10).
2. Classify each citation: our store listing, a competitor's store listing, our website, editorial list or review, Reddit or forum, YouTube, news, other. Count the answers with no citation.
3. Compare by engine and category with the study above. The class that carries most citations for your prompts gets the first sprint.
4. Refresh quarterly with the rest of the source map ([Off-site](off-site-and-community-presence.md) section 1).

### 8.3 The store page as a citation lever

Store listings are the largest cited class for ChatGPT app prompts in that study, so the store text is often what the model reads about the app (inference from [Study, 2026-05]). Whether AI crawlers can fetch and render apps.apple.com and play.google.com, and what they keep, is unknown as of 2026-10.

Write store text for two readers: store search (rules owned by `app-store-optimization`) and an AI reader.

| Field | What the AI reader needs |
|-------|--------------------------|
| Opening lines of the description | What the app does, for whom and on which platforms, in one or two plain sentences that name the app |
| Description body | Facts, limits and prices: plans and trial terms, what is free, offline or not, languages, regions, a data use summary, how to cancel. No keyword stuffing, no superlatives without proof |
| Privacy labels and data safety form | Identical to the website privacy page (the "is X safe" class reads both) |
| Developer name | The same name as on the website and in the App entity sheet |
| Review replies | Factual and specific; never text aimed at AI systems |
| Release notes | Dated, factual changes (prices, platforms, features) |

Handoff: `app-store-optimization` owns every store field, tags, review replies, review summary reports and the App entity sheet. This agent sends an AI-reader brief: the panel prompts where store pages are cited, wrong or missing facts in answers (with engine, date and run counts), the classes where answers fail (price, cancel, safety, platform), competitor facts that answers state and ours do not, and proposed wording from PRODUCT_FACTS.md. Store listing changes are G3 and pass `compliance`.

### 8.4 The app website

The website sits in the open web class (about 27% in the study, shared with lists and forums) and is the source you fully control.

1. One canonical, server-rendered page per app: the one-sentence description, platforms and minimum OS, plans and prices per market with currency and date, trial terms, what is free, links to both store listings, support and privacy links.
2. Answer pages for the 8.1 classes: pricing, "is <app> safe" (privacy and security facts), "how to cancel" (steps per platform), and honest, dated comparison and alternatives pages ([Content](content-engineering-for-llms.md) sections 5 and 6).
3. SoftwareApplication or MobileApplication JSON-LD that matches the visible facts. It serves consistency and Bing or Copilot, not citations ([Entity](entity-and-brand-authority.md) section 2.1).
4. Smart App Banner for mobile visitors: a UX element with no evidence that it is an AI signal.
5. apple-app-site-association and assetlinks.json reachable, so links open the app when installed.
6. Store buttons through your own tagged redirects ([Measurement](measurement-and-prompt-tracking.md) section 11).
7. AI search and user-fetch bots allowed ([Technical](technical-access-and-crawlers.md)).
8. `app_entity_check.py` passes after every price, name or platform change.

Detail on the app web presence (store page as citation, schema, redirects) and where it ends and this package begins: [App web presence for AI](../../app-store-optimization/references/app-web-presence-for-ai.md) in `app-store-optimization`.

### 8.5 Lists, YouTube, Reddit and reviews, done honestly

| Source | Do | Never |
|--------|----|-------|
| "Best apps for X" articles | Pitch with facts, a test account and what changed; correct wrong prices or features with evidence | Pay for undisclosed placement |
| YouTube | Own tutorials and comparisons with accurate captions; independent creator reviews with disclosure and no script control | Scripted "reviews" without disclosure |
| Reddit and forums | Staff with disclosed affiliation answer where the app is relevant, including when another app fits better; help with complaints in public | Seed threads, run sock puppets, buy accounts or upvotes |
| Store reviews | Ask every user at a natural moment through the platform prompts (owned by `app-store-optimization` and `mobile-app-growth`); reply factually | Gate by sentiment, incentivize ratings, post AI-written or fake reviews |

Full red lines: [Off-site](off-site-and-community-presence.md) section 9 and [Myths](myths-and-anti-patterns.md) section 2.

### 8.6 How people use AI to choose apps

AppTweak survey [Study, 2026-09] (1,000 US adults recruited on Prolific; margin of error about 3 points; self-reported):

| Finding | Share |
|---------|-------|
| Used AI to find or choose an app | 58% |
| Do so half the time or more | 21% |
| Learned about their most recent download from AI | 10% (Google search 10.7%, social media 10.4%) |
| Check the store after an AI recommendation | 59% |
| Would consider AI for their next app | 53% |

Caveats: self-reported recall, US only, an online opt-in panel rather than a probability sample, and a vendor with a stake in the topic. Use it to justify measuring AI as a discovery channel, not to forecast installs.

Implication: for most AI-sent users the store page is both a cited source and the landing page, so its first screen must confirm what the answer said (same name, price and platforms).

### 8.7 Measuring app visibility and AI-driven installs

| Metric | Source |
|--------|--------|
| Mention, recommendation and top 3 rates by app prompt class and engine | `ai_prompt_panel.py` ([Measurement](measurement-and-prompt-tracking.md) section 10) |
| Store listing citation rate (answers citing our listing / answers) | Panel cited URLs; list both listing URLs in the config (section 10.2 of the measurement module) |
| Accuracy on price, cancel, safety and platform facts | Panel answers vs the App entity sheet |
| Installs through tagged redirects, MMP AI attribution, self-reported "AI assistant" in onboarding | [Measurement](measurement-and-prompt-tracking.md) section 11 |

### 8.8 Apps inside assistants

When users want a task done inside the chat and it needs the app's live data or account, an assistant app or connector can pay. A directory listing alone does not create recommendations in ordinary answers. Decision table, spec, test protocol and the G3 rule: [Assistant apps](assistant-apps-and-connectors.md).

### 8.9 App plays

Launch (no AI program for the app yet):
1. App entity sheet with `app-store-optimization` (fields in [Entity](entity-and-brand-authority.md) section 2.1) and its JSON mirror for the script.
2. App panel v1: 25 to 60 prompts across the six classes, platforms and the top market; 3 runs each on ChatGPT and the next engine by GA4 AI referrals; baseline with intervals.
3. Source map (8.2) and the AI-reader brief to `app-store-optimization` (8.3).
4. Website app page and answer pages (8.4); `app_entity_check.py` passes.
5. Tagged store redirects and an "AI assistant" answer in onboarding attribution, via `measurement` and `mobile-app-growth`.
6. An assistant app decision memo only if the job test in [Assistant apps](assistant-apps-and-connectors.md) section 5 passes.

Optimize: per class, pick the dominant lever (store text, website page, list outreach, YouTube, reviews), change one lever per prompt cluster, read at 4 to 8 weeks with intervals.

Recover (mention rate or accuracy dropped):
1. Did a store field, price, name or developer name change? Check the App entity sheet date, the store version history and `app_entity_check.py`.
2. Did an engine or model change? Re-baseline using the Freshness sources.
3. Did a cited list or thread drop or misstate the app? Diff the source map.
4. Did new reviews or the store's AI review summary shift sentiment? Hand to `app-store-optimization` (it can report a wrong summary; the fix is the root cause in the app).
5. Did measurement break, so installs now count as direct? [Measurement](measurement-and-prompt-tracking.md) section 11.

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
