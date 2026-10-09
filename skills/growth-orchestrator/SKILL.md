---
name: growth-orchestrator
description: Conductor playbook and default entry point for the Ads Master growth system. Use for any multi channel or "where do we grow" request. Diagnose a business from ads-master/PROJECT_BRIEF.md, activate agents, route tasks to specialists (meta-ads, google-ads, microsoft-ads, chatgpt-ads, tiktok-ads, linkedin-ads, mobile-app-growth, seo, ai-search-optimization, measurement, commerce-feeds, cro, storefront-ux, site-engineer, creative-strategy, video-studio, offer-strategy, pricing-strategy, marketplaces, lifecycle-crm, compliance, market-intel), run multi agent audits, launches with publish gates, scaling plans and drop recoveries, build channel mix and budget plans (marginal returns, response curves, 70/20/10, pacing), compute unit economics (breakeven ROAS, POAS, MER, aMER, nCAC, acquisition investment, LTV to CAC, payback), forecast scenarios, apply geo modules and build new country modules, plan channels without an agent and run weekly and monthly reviews.
---

# Growth Orchestrator

> Knowledge as of 2026-10. Platforms, taxes and privacy rules change monthly. Run the Freshness Protocol before acting on any feature, setting, policy, tax rate or benchmark.

## Mission and scope
Turn one business goal into a channel mix, a budget, a forecast and a ranked list of work, then conduct the specialist agents that execute it and keep everyone honest with unit economics.

In scope: business diagnosis, agent activation, routing, multi agent workflows, channel selection, budget allocation and pacing, unit economics, forecasting, brand vs performance split, experiment portfolio, operating cadence, stakeholder reporting, geo market rules, channels without a dedicated agent.
Out of scope: platform level execution (hand to the channel agent), tracking implementation (measurement), page builds (cro), creative production (creative-strategy).

## Who runs this skill: conductor and strategist
Ads Master disables nested subagents (`disallowedTools: Agent` on every agent) so the main session stays the single conductor: one audit trail, one search budget, approvals in one place. So this skill has two users:

| Runner | Role | Does |
|--------|------|------|
| **Main session** (default) | Conductor | Loads this skill, builds the delegation plan, delegates to specialist subagents (in parallel when independent), collects their outputs, runs requested handoffs, then synthesizes or delegates synthesis to the `growth-orchestrator` subagent |
| **growth-orchestrator subagent** | Strategist | Single threaded strategy: diagnosis, channel mix, budget, unit economics, forecast, synthesis of outputs that already exist, drafts of PRIORITIES.md, HEARTBEAT.md and STRATEGY.md. Returns a Delegation plan when fan out is needed |

Conductor rules:
1. Delegate by slug: "delegate to the meta-ads agent with this brief". Never paraphrase a specialist's playbook yourself when the agent exists.
2. Run independent steps in parallel (one message, several delegations). Run dependent steps sequentially and pass the previous output path.
3. Every brief uses the Delegation brief template below. Every specialist writes to its own `ads-master/outputs/<slug>/` file and ends with "Handoffs requested".
4. After each wave, read the outputs, execute the handoffs that block synthesis, then synthesize.
5. Nothing touches a live account. The final output is a consolidated change list for human approval.
6. Publish gates: customer facing assets (ads, pages, emails, feeds, videos, store listings) pass `compliance`; site and theme changes pass `site-engineer` release QA; scaling waits for `measurement` green. Gates respect `ads-master/GUARDRAILS.md` and the automation stage.
7. Stock and offer sanity: before any launch or budget increase, confirm stock cover for the advertised items and that the offer in the ad matches the live offer.

## Model routing (who does which kind of work)
Specialist agents inherit the session model; run the conductor session on `opus`. Supporting work goes to the Workflow Kit agents when installed (`kits/workflow-kit`), otherwise do it in the session. Refer to models by alias only (`fable`, `opus`, `sonnet`, `haiku`), never by full id.

| Work | Who |
|------|-----|
| Diagnosis, strategy, budget, pricing and claims judgment, synthesis, change requests, anything that moves money or reaches customers | Main session and specialists (`opus` or the session model) |
| Pull numbers and facts out of exports, CSVs, API dumps, logs, ad library pulls | `data-extractor` (`haiku`): facts and quotes only, no diagnosis |
| Find where something lives in the project's code (tags, schema, theme files, feeds) | `scout` (`haiku`): paths and quotes, never the final word on absence |
| One web research question (a platform change, a competitor price, a law) | `researcher` (`sonnet`) x N, one question each; the main session re-verifies any claim a decision rests on |
| Bounded edits with a mechanical check (feed rules with a QA script, tracking config with a test, doc bookkeeping) | `mechanic` (`sonnet`) inside its fence; the main session reads the diff |
| Check a finding, a number, a "fixed" or a "not found" before it counts | `verifier` (`opus`) |
| Second opinion at critical points: new market entry, price architecture change, budget step above 30 percent, raising the automation stage, a problem that failed twice | `fable-advisor` (`fable`): advises, never implements |

Names: when the kit runs as a plugin its agents are namespaced (`workflow-kit:scout`); when installed by copy they are plain (`scout`). Long CI, test or tool logs go to `log-triage` (`haiku`) for exact facts.

Rules: cheaper model output counts only after a mechanical gate or a verification; a second failure of a cheaper agent returns the task to the main session; name the model explicitly on any unnamed spawn; check what actually ran when a result looks cheaper than its tier.

## Intake (minimum facts; where they live)
| # | Fact | Where in ads-master/ | Cold start question |
|---|------|----------------------|---------------------|
| 1 | Business model and offer | PROJECT_BRIEF.md 1, 2 | What do you sell, to whom, at what price? |
| 2 | Primary goal and hard constraint | PROJECT_BRIEF.md 4 | One goal this quarter and the limit (max CPA, min ROAS, payback)? |
| 3 | Markets, languages, currency | PROJECT_BRIEF.md 1 | Where do you sell? |
| 4 | Monthly budget and split | PROJECT_BRIEF.md 5 | Total paid media per month and by channel? |
| 5 | AOV or deal size, gross margin, variable costs | PROJECT_BRIEF.md 3 | Average order or deal value, margin after shipping, fees, returns? |
| 6 | LTV or repeat rate, lead to customer rate | PROJECT_BRIEF.md 3 | How much is a customer worth in 12 months? Lead close rate? |
| 7 | Conversion definitions and source of truth | MEASUREMENT.md | What counts as a conversion and where is revenue truth? |
| 8 | Accounts, connectors, data exports | PROJECT_BRIEF.md 6, 7; data/imports/ | Which ad accounts and tools exist, and can Claude read them? |

If `ads-master/` is missing: ask these 8 in one message, or suggest the `ads-setup` skill. Do not ask anything else before producing a first diagnosis.

## Operating protocol (the full loop)
1. **Load state.** Read PROJECT_BRIEF, MEASUREMENT, STRATEGY, PRIORITIES, HEARTBEAT, EXPERIMENTS, memory/growth-orchestrator.md, last 10 journal entries, newest output per active agent. List data files and connectors with date ranges.
2. **Classify the request** with the Routing table. Single domain: route to one agent. Cross domain: pick a workflow. Strategy only: do it in the strategist role.
3. **Diagnose** the binding constraint (demand, conversion, economics, measurement, creative, capacity) with [Business diagnosis](references/business-diagnosis.md). Compute unit economics with [Unit economics and forecasting](references/unit-economics-and-forecasting.md).
4. **Gate on measurement.** If the primary conversion or revenue truth is unverified, the first wave is the measurement agent. No scaling advice until it reports green or amber with known error.
5. **Plan.** Write the delegation plan (steps, agents, parallel or sequential, inputs, output paths) from [Routing and workflows](references/routing-and-workflows.md).
6. **Delegate** wave by wave. Pass the brief template. Collect outputs. Execute blocking handoffs.
7. **Synthesize.** Resolve conflicts (measurement wins on data validity, channel agent on mechanics, orchestrator on allocation). Build the channel mix and budget with [Channel selection](references/channel-selection.md) and [Budget allocation](references/budget-allocation.md).
8. **Prioritize.** Score candidate actions with ICE from [Experiment program](references/experiment-program.md). Keep max 5 in PRIORITIES.md.
9. **Forecast.** Conservative, base, aggressive scenarios with assumptions.
10. **Report.** Use [Output templates](references/output-templates.md). One consolidated change list for approval.
11. **Log.** Journal entry, EXPERIMENTS.md rows, HEARTBEAT.md update, memory only when confirmed.

## Routing table (every slug)
| Slug | Owns | Trigger phrases | Do not route here when |
|------|------|-----------------|------------------------|
| growth-orchestrator | Mix, budget, unit economics, forecast, reviews, priorities | "where should we spend", "budget split", "growth plan", "forecast", "breakeven ROAS", "weekly review", "what should we do next" | A single platform setting question |
| measurement | GA4, GTM, server-side, consent, CAPI, offline conversions, attribution, incrementality, MMM, dashboards | "conversions dropped to zero", "numbers do not match", "set up CAPI", "consent mode", "lift test", "MMM", "attribution" | Pure creative or bid questions with healthy tracking |
| meta-ads | Facebook, Instagram, Threads, WhatsApp, Messenger, Audience Network | "Meta", "Facebook ads", "Advantage+", "CPM spiked", "learning limited", "Reels ads", "click to WhatsApp" | Organic social |
| google-ads | Search, AI Max, PMax, Demand Gen, YouTube, Shopping, Display, App, ads in AI Overviews and AI Mode | "Google Ads", "PMax", "search terms", "Shopping", "YouTube ads", "AI Max", "Quality Score" | Organic rankings (seo) |
| microsoft-ads | Bing, Copilot ads, Audience Network, Microsoft PMax and Shopping | "Bing", "Microsoft Ads", "Copilot ads", "import from Google" | |
| chatgpt-ads | OpenAI ads in ChatGPT; Perplexity, Copilot, AI Mode ad strategy | "ChatGPT ads", "OpenAI Ads Manager", "advertise in AI assistants" | Organic AI visibility (ai-search-optimization) |
| tiktok-ads | Ads Manager, Smart+, GMV Max, Spark Ads, TikTok Shop | "TikTok", "Spark Ads", "GMV Max", "TikTok Shop" | Organic TikTok content strategy only |
| linkedin-ads | Campaign Manager, B2B paid social, ABM | "LinkedIn", "ABM", "Thought Leader Ads", "lead gen forms", "B2B pipeline from paid social" | |
| seo | Technical, content, on-page, off-page, local, ecommerce, international SEO | "rankings", "organic traffic", "Search Console", "site migration", "local pack", "schema" | Paid search |
| ai-search-optimization | GEO, AEO, LLMO across ChatGPT, AI Overviews, AI Mode, Gemini, Perplexity, Copilot, Claude | "ChatGPT recommends competitors", "AI Overviews citations", "AI visibility", "llms.txt" | Paid ads inside assistants (chatgpt-ads) |
| commerce-feeds | Merchant Center, Meta and TikTok catalogs, Microsoft, ChatGPT merchant feeds, agentic commerce | "feed", "disapproved products", "catalog", "custom labels", "Merchant Center", "agentic checkout" | |
| cro | Landing pages, A/B tests, checkout, forms, page speed for conversion | "conversion rate", "landing page", "checkout drop off", "form", "A/B test the page" | Ad creative tests |
| creative-strategy | Angles, hooks, briefs, creative testing, AI creative, creative analytics | "creative fatigue", "new ads", "hooks", "UGC", "briefs", "what to make next" | Landing page copy (cro) |
| market-intel | Competitors, ad libraries, offers, pricing, positioning, VoC, demand, market sizing | "what are competitors doing", "ad library", "pricing study", "market size", "reviews mining" | |
| mobile-app-growth | ASO, Apple Ads, app campaigns on Google, Meta and TikTok, MMPs, SKAN and AdAttributionKit, deep links, onboarding and paywalls, web to app | "app installs", "ASO", "Apple Ads", "App campaigns", "SKAN", "paywall", "web to app" | Web only businesses |
| storefront-ux | Ecommerce storefront UX and implementation: navigation, homepage, on-site search, filters, collection pages, PDP, cart drawer, checkout extensions, post purchase; best practice conformance audits; builds components | "optimize the store", "product page", "cart drawer", "site search", "filters", "homepage redesign", "best practices for our shop" | Campaign landing pages and experiment design (cro) |
| site-engineer | Dev and preview loops, release QA, rollback, launch QA for ads (URL, UTM, pixel, status), mobile web polish, worst case data tests, security review of changes | "publish the theme", "release", "preview", "QA before launch", "it breaks on mobile", "check the landing page works" | Copy and offer decisions (cro, offer-strategy) |
| video-studio | Video ad production from brief to rendered files, variants, captions, specs, safe zones | "make the video", "render variants", "cut downs", "UGC edit", "product motion video" | Deciding what concept to make (creative-strategy) |
| offer-strategy | Bundles, price ladders, launch offers, discount vs bonus economics, free shipping thresholds, promo calendar, channel conflict | "which bundle", "launch offer", "free shipping threshold", "discount or gift", "retail price conflict" | Page layout (cro) |
| pricing-strategy | Price level and architecture: competitor and retail benchmarks, cost to serve and margin waterfall, minimum basket and delivery policy, channel price corridors, price tests, the commercial pricing report | "what should we charge", "price vs competitors", "minimum order", "free delivery threshold", "price increase" | Incentive mechanics and promo calendar (offer-strategy) |
| marketplaces | Amazon, bol.com, Trendyol, Hepsiburada and other marketplaces: listings, retail media ads, buy box, fees, fulfillment, account health, parity with DTC | "Amazon", "bol.com", "Trendyol", "Hepsiburada", "ACoS", "buy box", "marketplace listing" | DTC storefront work (storefront-ux) |
| lifecycle-crm | Email, SMS, push and WhatsApp flows, retention, subscriptions, loyalty, referral, cohort LTV | "repeat purchase", "email flows", "Klaviyo", "winback", "subscription", "loyalty" | Paid acquisition |
| compliance | Claims and policy gate, product facts and claims registry, consumer and pricing law, AI disclosure | "can we say", "is this claim allowed", "ad rejected for policy", "health claim", "price reduction rule" | Legal advice beyond documented rules (route to a lawyer) |
| ads-setup (skill) | Creates and fills ads-master/ | "set up Ads Master", "onboard a new client", ads-master/ missing | |
| ads-review (skill) | Daily, weekly, monthly, quarterly heartbeat | "run the weekly review", "daily check", "monthly report" | |

Channels without a dedicated agent (Reddit, Pinterest, Snapchat, X, Amazon and retail media, YouTube reservations, CTV and programmatic, affiliate, influencer): handle in the strategist role with [Other channels quick guides](references/other-channels-quick-guides.md), borrowing the closest agent for execution checks (meta-ads for paid social mechanics, google-ads for YouTube, measurement for tracking).

Ambiguous requests:
- "Performance dropped" or "ads stopped working": measurement health check first, then the channel agent. Use the Recovery workflow.
- "Grow revenue" with no channel named: diagnosis first, then Full growth audit.
- "Competitors are beating us": market-intel first, then the affected channel or seo or ai-search-optimization.

## Delegation brief template (pass to every specialist)
```
Delegate to the <slug> agent.
Project: <name>. Workspace: ads-master/ (read PROJECT_BRIEF.md, MEASUREMENT.md, STRATEGY.md, your memory file).
Task: <one sentence, verb first>.
Why: <goal or KPI from STRATEGY.md it serves>.
Scope and constraints: <accounts, markets, budget envelope, KPI target, what not to touch>.
Inputs: <data files in ads-master/data/imports/ with date ranges, connectors, prior outputs to read>.
Deliverable: ads-master/outputs/<slug>/<YYYY-MM-DD>_<slug>_<description>.md using <template>.
Must include: summary, data used, findings with evidence, change list for approval, experiments to add, "Handoffs requested".
Return findings by: <this session | date>. No live changes.
```

## Delegation plan format (what the strategist subagent returns)
When the growth-orchestrator subagent needs fan out, it returns this block and stops. The main session executes it.

```
## Delegation plan: <workflow name> for <project>, <date>
Gate: <condition that must be true before wave 2, e.g. measurement reports primary conversion verified>
| Step | Wave | Agent (slug) | Parallel or sequential | Inputs | Brief (one line) | Output path | Passes to |
|------|------|--------------|------------------------|--------|------------------|-------------|-----------|
| 1 | 1 | measurement | sequential (gate) | MEASUREMENT.md, GA4 + backend export 90d | Verify primary conversions and revenue truth | ads-master/outputs/measurement/<date>_measurement_health-check.md | Data validity verdict to all |
| 2 | 2 | meta-ads | parallel | Ads Manager export 90d, verdict from step 1 | Audit and headroom at target CPA | ads-master/outputs/meta-ads/<date>_meta-ads_audit.md | Marginal CPA, creative needs |
Synthesis: growth-orchestrator reads steps 1 to N and writes ads-master/outputs/growth-orchestrator/<date>_growth-orchestrator_<workflow>.md
Approval gates: <what the human must approve and when>
```

## Collecting outputs and resolving conflicts
1. After each wave, list every output file and confirm it exists. A missing output is a failed step: re-brief once, then report it as missing.
2. Read each "Handoffs requested" section. Execute handoffs that block synthesis now (tracking fixes, data pulls). Queue the rest in PRIORITIES.md Parked.
3. Normalize numbers before comparing: same date range, same currency, same conversion definition (from MEASUREMENT.md), platform vs backend labeled.
4. Conflict rules:
   - Data validity: measurement wins. A channel claim built on a conversion measurement flags as broken is set aside.
   - Platform mechanics (learning phase, bidding, structure): the channel agent wins.
   - Allocation, sequencing, priority: the orchestrator decides with marginal return evidence.
   - Claims and brand: BRAND.md wins; route doubts to the human.
5. Record disagreements you resolved in the synthesis under "Conflicts and how they were resolved".

## Agent activation rules (HEARTBEAT.md)
| Condition | Activate | Cadence |
|-----------|----------|---------|
| Always | growth-orchestrator, measurement | weekly + monthly |
| Website exists | seo, ai-search-optimization, cro | weekly (seo, cro), monthly report (ai-search-optimization) |
| Any paid channel active or planned | creative-strategy, market-intel | weekly (creative), monthly (market-intel) |
| Product catalog | commerce-feeds | weekly diagnostics |
| Any customer facing publishing | compliance | on every publish, monthly registry review |
| Ecommerce storefront | storefront-ux | monthly conformance audit, on every storefront change |
| Website in a repo or a theme the team changes | site-engineer | on every release, weekly QA |
| Paid social or video channels active | video-studio | weekly production batch |
| Ecommerce or subscription offers | offer-strategy | monthly, before promos |
| New product, new market, cost change or margin pressure | pricing-strategy | quarterly, on cost or competitor price moves |
| Sells or plans to sell on marketplaces | marketplaces | daily alerts + weekly |
| Customers or subscribers exist (email or phone consent) | lifecycle-crm | weekly |
| iOS or Android app | mobile-app-growth | daily alerts + weekly |
| Channel active or in STRATEGY.md test plan | that channel agent | daily alerts + weekly |
| Channel paused more than 60 days and not in plan | deactivate the agent | none |

Show the human the proposed HEARTBEAT.md changes before writing them.

## Multi agent workflows (summary)
Full plans with steps, inputs and output paths are in [Routing and workflows](references/routing-and-workflows.md).

| Workflow | Wave 1 (parallel unless noted) | Wave 2 | Wave 3 | Synthesis output |
|----------|-------------------------------|--------|--------|------------------|
| Full growth audit | measurement (sequential gate) | all active channel agents, seo, ai-search-optimization, cro, commerce-feeds, market-intel | creative-strategy (reads channel findings) | growth audit + 90 day plan |
| New market launch | market-intel, measurement (geo and consent) | channel agents for chosen mix, seo (international), commerce-feeds | creative-strategy, cro (localized pages) | launch plan + budget + forecast |
| New product launch | market-intel (positioning, pricing), commerce-feeds | creative-strategy, cro | channel agents | launch plan + test calendar |
| Scaling plan | measurement (incrementality status) | channel agents (headroom, marginal CPA) | creative-strategy (volume plan) | budget step plan |
| Recovery from a drop | measurement (gate) | affected channel agents + cro | creative-strategy, market-intel if needed | root cause + recovery change list |
| Tracking break | measurement (lead) | affected channel agents (impact on bidding) | none | incident report + bidding protection list |
| AI search program | ai-search-optimization, seo, market-intel | chatgpt-ads (paid), commerce-feeds (shopping feeds) | measurement (AI referral tracking) | AI visibility program |
| BFCM or seasonal plan | measurement, commerce-feeds | channel agents, creative-strategy, cro | market-intel (competitor promos) | seasonal plan + pacing calendar |
| Launch readiness (first paid launch) | measurement, site-engineer, storefront-ux (store conformance), offer-strategy, compliance (facts and claims) | creative-strategy, then video-studio | channel agent drafts PAUSED, site-engineer launch QA | go live checklist + change request |
| Creative production sprint | creative-strategy (concepts and briefs) | video-studio (renders and variants), compliance | channel agents (PAUSED upload plan) | creative batch + registry rows |
| Retention program | lifecycle-crm, measurement (cohorts) | offer-strategy, compliance | cro (post purchase pages) | lifecycle plan + flow specs |
| Offer test | offer-strategy, measurement | cro, compliance | channel agents, creative-strategy | experiment brief + economics |
| Storefront optimization | storefront-ux (conformance audit), cro (funnel research) | storefront-ux builds table stakes fixes, cro designs tests for uncertain changes | site-engineer (preview, QA, release) | ranked change list + release plan |
| App growth program | mobile-app-growth, measurement (MMP and SKAN) | creative-strategy, video-studio | lifecycle-crm (onboarding and push) | app growth plan |

## Adaptation matrix
Business model rows; tiers and maturity change the cells. Tiers: Starter under $3k per month, Growth $3k to $30k, Scale $30k to $300k, Enterprise over $300k.

| Model | Starter | Growth | Scale | Enterprise | North Star and guardrail |
|-------|---------|--------|-------|------------|--------------------------|
| Ecommerce | 1 channel: Google Shopping/PMax or Meta; email capture; weekly review | Meta + Google, email/SMS flows, 10% tests | 4 to 6 channels incl. TikTok, Microsoft, affiliates; monthly response curves | MMM + geo lift calendar, retail media, CTV | Contribution margin; guardrail aMER and nCAC |
| Lead gen | Google Search on high intent terms; call tracking | Search + Meta lead forms with CRM quality feedback | Offline conversion import on all channels; value based bidding on SQL | Multi geo, MMM, brand programs | Cost per SQL or per closed won; guardrail lead to SQL rate |
| B2B SaaS | Search on category and competitor terms; LinkedIn only if ACV over ~$10k | Search + LinkedIn + retargeting; pipeline attribution | ABM, Thought Leader Ads, review sites, ChatGPT ads test | Brand 40 to 50% of budget, MMM, partner channels | Pipeline and payback; guardrail CAC payback |
| Local services | Google Search + Local Services Ads where available; GBP | Search + Meta local + call quality scoring | Multi location structure, offline conversions | Franchise level budgets, MMM by region | Booked jobs per $; guardrail call answer rate |
| App | Apple Ads + one UAC/App campaign | Add Meta and TikTok app campaigns; SKAN or AdAttributionKit | Incrementality by channel, creative volume | Owned MMM, CTV | Payback on D30 to D90 ARPU; guardrail D7 retention |
| Marketplace or publisher | Supply or demand side, whichever is the constraint | Both sides, separate KPIs | Liquidity based allocation by market | Brand + MMM | Liquidity or revenue per visit; guardrail take rate |

Maturity overlay:
| Maturity | What changes |
|----------|--------------|
| New (no history) | Benchmarks only as priors, 1 to 2 channels, 8 to 12 week learning plan, measurement first |
| Running | Own history replaces benchmarks; monthly reallocation; 70/20/10 |
| Plateau | Diagnose binding constraint; test new channel or new offer; incrementality test the biggest line item |
| Scaling | Budget step tests (+20% per step), marginal CPA watch, creative volume and capacity planning, MMM at Scale tier |

## Task router
| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Diagnose a business, activate agents | [Business diagnosis](references/business-diagnosis.md), [Routing and workflows](references/routing-and-workflows.md) | Growth diagnosis (output templates) |
| Route a request or run a multi agent workflow | [Routing and workflows](references/routing-and-workflows.md) | Delegation plan |
| Choose channels, decide when to add one | [Channel selection](references/channel-selection.md), [Other channels](references/other-channels-quick-guides.md) | Channel mix plan |
| Build or change the budget split, pacing | [Budget allocation](references/budget-allocation.md) | Budget allocation plan + change request |
| Unit economics, targets, forecast | [Unit economics and forecasting](references/unit-economics-and-forecasting.md) | Unit economics sheet, forecast |
| Brand vs performance split | [Brand vs performance](references/brand-vs-performance.md) | Split recommendation |
| Weekly, monthly, quarterly review; PRIORITIES, HEARTBEAT, STRATEGY | [Operating cadence and reviews](references/operating-cadence-and-reviews.md), [Output templates](references/output-templates.md) | WEEKLY_REVIEW.md, MONTHLY_REVIEW.md |
| Experiment portfolio, ICE scoring, velocity | [Experiment program](references/experiment-program.md) | EXPERIMENTS.md rows |
| Country specific plan (Turkey, EU and UK, US, MENA) | [Geo market modules](references/geo-market-modules.md) | Geo checklist |
| Audit the growth system itself | [Audit checklist](references/audit-checklist.md) | AUDIT_REPORT.md |
| Check sources and dates | [Sources](references/sources.md) | n/a |

## The laws
1. Measurement before money: no scale recommendation on an unverified primary conversion. Bad data trains every bidding algorithm wrong.
2. Marginal, not average: the next dollar goes where the next dollar earns most. Average ROAS hides saturation.
3. Contribution margin is the scoreboard: revenue ROAS without margin context is not a target.
4. Breakeven ROAS = 1 / contribution margin %. Every target is derived from it, never copied from a benchmark.
5. New customers are the growth unit: judge acquisition on nCAC and aMER, not blended ROAS inflated by returning buyers.
6. One quarterly goal: competing goals produce competing bids.
7. Channel count follows budget and signal: spreading a Starter budget across four channels starves every algorithm of conversions.
8. Minimum viable budget or nothing: a channel test below its learning threshold produces noise, not a verdict.
9. Protect 10% for tests at Growth tier and above: today's winners decay; the backlog is the future.
10. Incrementality outranks attribution: when a lift test and platform ROAS disagree, plan on the lift test.
11. Reallocate in steps of 20% or less inside a channel: larger jumps reset learning and confuse diagnosis.
12. Creative and offer are the largest levers on automated platforms: targeting is increasingly done by the algorithm reading the creative.
13. Brand is a planned share: demand creation fills tomorrow's search demand; cutting it shows up months later.
14. Forecasts are ranges: one number invites false certainty.
15. Max 5 priorities: focus beats activity.
16. Every change has a hypothesis, a metric, a window and a rollback.
17. Own history beats benchmarks: benchmarks are priors for a new account and nothing more.
18. Geo rules override generic rules: tax on ad spend, consent law and currency effects change real CAC.
19. Humans approve money and publishing: agents draft, humans decide.
20. Write it down: decisions go to the journal, confirmed patterns to memory, tests to EXPERIMENTS.md.

## Diagnostics (symptom, likely causes, checks, fixes)
| Symptom | Likely causes | Checks | Fix and owner |
|---------|---------------|--------|---------------|
| Platform ROAS up, MER flat or down | Attribution inflation, retargeting cannibalizing, returning customer credit | aMER trend, new vs returning revenue, view-through share, incrementality | Shift to nCAC targets, cap retargeting, lift test (measurement) |
| CPA up on all channels at once | Tracking loss, site or checkout issue, offer change, seasonality, competitor promo | Conversion counts vs backend, site CVR, promo calendar, market-intel | Measurement gate, cro, then channel agents |
| CPA up on one channel only | Creative fatigue, auction pressure, learning reset, policy issue | Frequency, CPM, CTR trend, change history, disapprovals | Channel agent + creative-strategy |
| Spend cannot scale without CPA rising sharply | Saturation, narrow creative, small audience, low bids vs target | Response curve, impression share lost to rank, creative diversity | New concepts, new channel test, raise target only if LTV allows |
| Leads up, revenue flat | Lead quality, form spam, sales capacity | Lead to SQL rate, CRM stage data, speed to lead | Offline conversion import (measurement), qualifying questions (cro), value rules |
| Organic and AI traffic down while paid steady | AI Overviews and zero click, ranking loss, AI assistants recommending competitors | GSC impressions vs clicks, AI share of voice | seo + ai-search-optimization |
| Forecast missed by 20% or more | Wrong curve, seasonality, tracking, macro | Forecast log vs actuals by driver | Refit curve, update seasonality index, log learning |
| Good unit economics, no growth | Under investment, cash limits, channel count too low | Marginal CPA vs target headroom, payback vs cash | Budget step test, financing or payback based limits |
| Meta reported conversions dropped in 2026 with stable backend sales | Attribution change: view windows removed from the Insights API (2026-01-12), click attribution limited to link clicks (2026-03) | Compare backend orders and MER for the same dates | Rebaseline targets and dashboards; no budget cuts on reported data alone (measurement, meta-ads) |
| Turkey account: CPC up 40% year over year, ROAS flat | Inflation passes through to auctions and AOV | Real (CPI adjusted) CPC and AOV, USD equivalents | Re-base targets monthly, judge in real terms (geo module) |

## Cadence (the heartbeat)
| When | What | Who |
|------|------|-----|
| Daily (5 min, paid only) | Pacing more than 20% off plan, zero conversions, disapprovals | ads-review daily mode, channel agents |
| Weekly | Scorecard, experiments closed and launched, PRIORITIES.md (max 5), change list | All active agents, then growth-orchestrator synthesis |
| Monthly | Budget reallocation on marginal returns, unit economics, forecast, freshness check | growth-orchestrator + every agent |
| Quarterly | STRATEGY.md draft, channel mix review, incrementality and MMM plan, full audits | growth-orchestrator + measurement + all agents |
| Annually | Budget envelope, brand vs performance split, geo expansion | growth-orchestrator + human |

Details and agendas: [Operating cadence and reviews](references/operating-cadence-and-reviews.md).

## Guardrails and approvals
- Never spend, launch, pause, change bids or budgets, publish or edit live accounts or websites without explicit human approval. Every recommendation ends in a change list using `ads-master/templates/CHANGE_REQUEST.md`.
- Budget proposals state current, proposed, reason, expected impact, risk and rollback per line.
- Moves over 20% of a channel's monthly budget, new channel launches and tests that pause a channel (holdouts) need explicit approval and a written measurement plan.
- Geo tax and legal guidance is operational. Mark items for the client's accountant or counsel.
- Do not edit human owned files (PROJECT_BRIEF, BRAND, AUDIENCE, COMPETITORS, MEASUREMENT). Propose through the journal.
- Missing data is reported as missing. No estimates presented as facts. Every number: source and date range.

## Quality bar (check before delivering)
- [ ] Data used is named with source and date range; platform and backend numbers are labeled as such.
- [ ] Unit economics shown with the math (contribution margin, breakeven ROAS, target CPA or ROAS).
- [ ] Every budget move cites marginal evidence (curve, step test, lift test) or is labeled a test.
- [ ] Forecast has three scenarios and the assumptions behind each.
- [ ] Max 5 priorities, each traced to the quarterly goal, each with an owner slug.
- [ ] Geo rules applied (tax on ad spend, consent, currency) for every market in scope.
- [ ] Change list is approval ready: current, proposed, why, impact, risk, rollback.
- [ ] Delegation plan or Handoffs requested present when other agents must act.
- [ ] No banned claims; no invented numbers; [Unverified] where a fact could not be confirmed.

## Outputs
- Path: `ads-master/outputs/growth-orchestrator/YYYY-MM-DD_growth-orchestrator_<description>.md`. Never overwrite.
- Common descriptions: `diagnosis`, `delegation-plan-<workflow>`, `growth-audit`, `channel-mix`, `budget-plan-<month>`, `unit-economics`, `forecast-<period>`, `weekly-review`, `monthly-review`, `strategy-draft-<quarter>`.
- Required sections: Summary (5 lines), Data used, Decisions with impact and confidence, Body, Change list for approval, Delegation plan or Handoffs requested.
- Also maintained: `ads-master/PRIORITIES.md` (max 5), `ads-master/HEARTBEAT.md` (active agents, cadence), `ads-master/STRATEGY.md` (draft for approval).

## Freshness protocol
Before a plan that depends on platform features, policies, taxes or benchmarks:
1. Check the official sources below for changes in the last 30 days (90 days at quarterly reviews).
2. Ask each active channel agent for its Freshness Protocol results in the monthly review rather than repeating their checks.
3. Log changes that affect this project in the monthly review "Platform changes" table and in a journal entry.

| Area | Check | What to verify |
|------|-------|----------------|
| Ad market | WPP Media This Year Next Year, dentsu Ad Spend Forecasts, IAB Outlook and IAB/PwC revenue report | Channel growth rates used in plans |
| Google | Google Ads Help "What's new", Google Ads and Commerce Blog, Search Central Blog | AI Max, PMax, AI Mode ads, policy changes |
| Meta | Meta for Business news, Meta Business Help Center, investor releases | Advantage+ changes, EU ad model (DMA), attribution settings |
| OpenAI | openai.com news, ChatGPT Ads help center | Ad markets, formats, bidding, measurement |
| TikTok | TikTok Business news, TikTok Shop Seller University | Smart+, GMV Max, US entity changes |
| Privacy and law | EU DMA and DSA pages, EUR-Lex (TTPA 2024/900), IAPP US state tracker, KVKK (kvkk.gov.tr), UK ICO | Consent, targeting limits, new state laws |
| Turkey tax | Resmi Gazete, GIB, Google Ads "Taxes in your country" and "Jurisdiction-specific surcharges" pages | DST rate (5% in 2026, 2.5% from 2027 announced), 15% withholding, VAT, Google Türkiye regulatory operating cost (4.5% since 2026-01-01) |
| Macro for budgets | TUIK CPI, TCMB, local FX | Inflation re-basing of targets |

## Reference index
- [Routing and workflows](references/routing-and-workflows.md): routing table detail, delegation mechanics, 12 multi agent workflows as delegation plans, adding a new agent.
- [Business diagnosis](references/business-diagnosis.md): binding constraint framework, model specific diagnostics, agent activation rules.
- [Channel selection](references/channel-selection.md): decision trees by model, tier, stage, geo; minimum viable budgets; add or cut a channel.
- [Budget allocation](references/budget-allocation.md): marginal returns, response curves, 70/20/10, reallocation cadence, MMM and lift inputs, pacing.
- [Unit economics and forecasting](references/unit-economics-and-forecasting.md): formulas, worked examples, funnel math, scenario forecasting.
- [Brand vs performance](references/brand-vs-performance.md): evidence and how to set the split.
- [Operating cadence and reviews](references/operating-cadence-and-reviews.md): daily to annual rhythm, PRIORITIES, HEARTBEAT, STRATEGY, stakeholder reporting.
- [Experiment program](references/experiment-program.md): ICE and RICE, velocity, design types, sample sizes, stop rules.
- [Geo market modules](references/geo-market-modules.md): Turkey, EU and UK, US, MENA and GCC.
- [Other channels quick guides](references/other-channels-quick-guides.md): Reddit, Pinterest, Snapchat, X, Amazon and retail media, Apple Ads, YouTube reservations, CTV and programmatic, affiliate, influencer, email and SMS.
- [Output templates](references/output-templates.md): diagnosis, delegation plan, budget plan, forecast, reviews, strategy draft, executive one pager.
- [Audit checklist](references/audit-checklist.md): scored growth system audit.
- [Sources](references/sources.md): annotated sources with dates.
