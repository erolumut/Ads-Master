---
name: meta-ads
description: Meta advertising playbook for Facebook, Instagram, Threads, WhatsApp, Messenger and Audience Network via Ads Manager and the Marketing API. Use to audit, launch, optimize, scale, troubleshoot or recover Meta ad accounts; to plan Advantage+ sales, app and leads campaigns; choose bid strategies (highest volume, cost per result goal, ROAS goal, bid cap, value rules); structure accounts for Andromeda and GEM; build creative testing and diversity plans; set up Pixel plus Conversions API, EMQ, deduplication, attribution and incremental attribution; run lead ads, conversion leads, click to WhatsApp and Messenger ads; catalog and Advantage+ catalog ads; fix policy disapprovals, account restrictions and health or finance data restrictions; plan BFCM; and pull data via Marketing API, Ads Library or Meta Ads MCP servers. Triggers on Meta CPA or ROAS drops, learning limited, fatigue, scaling, Opportunity Score, Threads or WhatsApp Status ads.
---

# Meta Ads

> Knowledge as of 2026-10 (verification pass 2026-10-08). Platforms change monthly. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark. Most mid 2026 changes are now confirmed by Meta statements or multiple independent reports; the remaining [Unverified] or [Contested] items in the references must be confirmed in the live account first.

## Mission and scope

Mission: grow profitable, incremental results from Meta (Facebook, Instagram, Threads, WhatsApp, Messenger, Audience Network) by feeding the delivery system the best signal and the most diverse creative, inside the business's unit economics, and prove it with backend and incrementality evidence.

In scope: account structure, campaign settings, bidding and budgets, audiences and signals, Meta-specific creative mechanics and testing, Pixel and Conversions API setup standards, Meta attribution, lead ads and messaging, catalog ads, policy and account health, Meta APIs and MCP tools, audits, reporting, scaling and recovery.

Out of scope (hand off):
| Topic | Owner slug |
|-------|-----------|
| Angles, hooks, scripts, briefs, creative production, cross-channel creative analytics | creative-strategy |
| GA4, GTM, server-side infrastructure, consent, MMM builds, cross-channel attribution | measurement |
| Feed creation, feed rules, catalog attribute quality | commerce-feeds |
| Landing pages, forms on site, checkout, page speed | cro |
| Competitor ad research, offers, positioning | market-intel |
| Channel mix, budget across channels, forecasts, priorities | growth-orchestrator |
| TikTok, Google, LinkedIn, Microsoft, ChatGPT ads | the matching channel slug |

## Intake (minimum facts)

Read in this order: `ads-master/PROJECT_BRIEF.md`, `ads-master/MEASUREMENT.md`, `ads-master/STRATEGY.md`, `ads-master/PRIORITIES.md`, `ads-master/memory/meta-ads.md`, latest 10 files in `ads-master/journal/`.

Minimum facts needed (ask only for what is missing):
| Fact | Where to find it |
|------|------------------|
| Business model and primary conversion | PROJECT_BRIEF.md section 1, MEASUREMENT.md |
| AOV or deal value, contribution margin, target CPA or ROAS, LTV | PROJECT_BRIEF.md section 3 |
| Monthly Meta budget and flexibility | PROJECT_BRIEF.md section 5 |
| Markets, languages, currency | PROJECT_BRIEF.md section 1 |
| Ad account ID, business portfolio access level, data access method (MCP, API, exports) | PROJECT_BRIEF.md sections 6 and 7 |
| Tracking status: Pixel, CAPI, EMQ, dedup, CRM feedback | MEASUREMENT.md tracking table |
| Regulated category and claims limits | PROJECT_BRIEF.md section 8, BRAND.md |
| Creative assets available and production capacity | BRAND.md, ask human |

Cold start (no `ads-master/` folder): ask for the 8 facts above in one message, or suggest running the `ads-setup` skill. Proceed with clearly labeled assumptions if the human prefers.

Data rule: state the source (MCP server, API, CSV file name) and the date range of every number. If data is missing, say so; never fill gaps with invented figures.

## Operating protocol

1. Load context (Intake). Note the budget tier, business model and maturity.
2. Freshness check if the task depends on features, policies or settings (see Freshness protocol).
3. Get data: MCP connector, Marketing API (read only), or CSVs in `ads-master/data/imports/`. Record ranges and attribution settings. See [Tools, API and MCP](references/tools-api-mcp.md).
4. Verify measurement before judging performance: dedup, EMQ, attribution change dates, backend reconciliation. See [Measurement](references/measurement-capi-attribution.md).
5. Diagnose: decompose CPA or ROAS into CPM, CTR, CVR, AOV; check learning status, fatigue, structure, policy. See [Diagnostics](references/optimization-loop-and-diagnostics.md).
6. Prioritize by impact x confidence x ease. Measurement and structure fixes usually come before creative and bids, and creative before bid tweaks.
7. Act: produce the deliverable (audit, launch plan, change list, test plan, report) using the templates in the references.
8. QA against the Quality bar below and the Guardrails.
9. Log: output file, journal entry, EXPERIMENTS.md rows, memory only for confirmed patterns.
10. End the response with "Handoffs requested" when other agents are needed.

Quality bar for every deliverable:
- Every number has a source and date range; every platform claim has a label or a link.
- Recommendations are specific (exact setting names, values, levels) and reversible where possible.
- Expected impact stated as a range with confidence, plus the metric that will prove it.
- Change list is separate and ready for approval.

## State of the platform (Jan 2025 to Oct 2026, condensed)

| Date | Change | Label |
|------|--------|-------|
| 2024-12 | Andromeda retrieval engine (creative diversity becomes the main targeting input) | [Official] |
| 2025-01 | Health and wellness data restrictions on lower funnel events; "Credit" category broadened to financial products and services | [Official; verify financial scope by country] |
| 2025-02 | Advantage+ shopping renamed Advantage+ sales; Advantage+ default for Sales, App, Leads tested | [Official] |
| 2025 (H1) | Incremental attribution option in Ads Manager | [Official] |
| 2025-05 to 2026-Q1 | Unified Advantage+ API structure; legacy ASC and AAC creation phased out in v24 and v25 | [Official] |
| 2025-06 | WhatsApp Status ads and Promoted Channels announced | [Official] |
| 2025-07 | WhatsApp per-message pricing; Meta announces end of EU political and social issue ads from October 2025 | [Official] |
| 2025-10 | Creative testing tool (2 to 5 ads, even split) in Ads Manager | [Official via practitioners] |
| 2025-11 | GEM engineering details published | [Official] |
| 2025-12-16 | Meta AI chat interactions used for ad personalization (not EU, UK, South Korea at launch) | [Official] |
| 2026-01 | EU less personalized ads choice live; Threads ads to all users globally; Insights API stops 7-day view and 28-day view (Jan 12) | [Official] |
| 2026-02 | Automation Unification (2026-02-13): unified Advantage+ creation flow for Sales, Leads, App; creative enhancements on by default; WhatsApp Status ads rolling out globally | [Official, 2026-02 via secondary; UI details Practitioner consensus] |
| 2026-03-03 | Click-through attribution counts link clicks only; engage-through attribution (1 day); engaged-view threshold 5s | [Official via trade press] |
| 2026-04-29 | Official Meta Ads AI Connectors: hosted MCP server (mcp.facebook.com/ads) and Ads CLI, open beta | [Official, 2026-04] |
| 2026-06-01 | Automated "AI info" labels on ads whose media was made with third-party AI tools (C2PA metadata) | [Official, 2026-06] |
| 2026-07-01 | Location fees on ads delivered to Turkey and Austria (5%), France, Italy, Spain (3%), UK (2%) | [Official, 2026-03 announcement] |
| 2026-07-29 | Graph API v26.0: Instagram Explore Feed placement removed, Messenger Stories stripped; applies to all versions from 2026-10-27 | [Official, 2026-07] |
| 2026-08 | Ad set placement exclusions removed account by account from 2026-08-25; placement value rules (minus 90% floor) as alternative; Creative diversity column in Ads Manager | [Practitioner consensus; scope Contested]; column [Official] |
| 2026-09 | Creator Marketing Hub (09-15), Threads ads without an Instagram account (from about 09-21), Instagram live partnership ads (09-29), click to WhatsApp free window up to 7 days (09-28, reported) | [Official, 2026-09]; WhatsApp window [Contested] |
| 2026-10-06 | Advertising Week: image to video GA, Customer Lifecycle Strategy (new customers only) open to all, MCP server expanded, agentic Meta AI business assistant in testing | [Official, 2026-10] |

## Adaptation matrix

### By business model and budget tier

| Model | Starter (under $3k) | Growth ($3k to $30k) | Scale ($30k to $300k) | Enterprise (over $300k) |
|-------|--------------------|----------------------|------------------------|--------------------------|
| Ecommerce | 1 Advantage+ sales campaign, highest volume, ATC or IC event if under 10 purchases per week; 3 to 6 concepts; KPI: CPA vs breakeven, MER | Main Advantage+ sales + catalog; purchase optimization; highest value test at 30+ purchases per week; 8 to 15 concepts, 3 to 6 new per week; weekly cadence | Main (highest value) + cost-controlled scaler + catalog by margin + testing lane; value rules from backend; 20 to 40 concepts, 10 to 25 new per week; quarterly lift test | Per market cluster Scale template; API reporting to warehouse; always-on lift or GeoLift plus MMM; localized creative pipeline |
| Lead gen (B2C) | 1 Leads campaign, higher intent instant form or website; KPI: cost per qualified lead from CRM | Leads campaign + CRM stage events; conversion leads when eligible; placement value rules on low quality | Cost per result goal on qualified events; multiple form variants via A/B tests; call center speed SLAs | Multi-market, CRM value-based optimization, holdout tests |
| B2B SaaS | Website lead or trial event, one campaign, customer list suggestions; KPI: cost per SQL | Optimize to trial or MQL; send SQL and won via CAPI; 5 to 8 concepts aimed at job roles | SQL or pipeline value optimization; ABM coordination with linkedin-ads | Pipeline value bidding, geo tests for incrementality |
| Local services | Leads, Calls or click to message, radius 15 to 40 km; KPI: cost per booked job | Add CRM stages, WhatsApp automation, location-specific creative | Per region campaigns only if budgets reach threshold; call tracking to CAPI | Franchise templates, dynamic location ads, central creative |
| App | Advantage+ app, optimize to install; MMP connected; KPI: CPI and D7 events | App event optimization at 50+ events per week; SKAdNetwork checks | Value optimization (purchase or subscription value); creative volume high | Per OS and market economics, incrementality via geo |
| Marketplace or publisher | One side at a time; optimize to registration or first transaction; KPI: cost per activated user | Separate supply and demand campaigns with different events; catalog for demand side | Value by category margin; cohort LTV events | Market-level programs, MMM |

### By maturity

| Maturity | Focus | Structure changes | Bidding | Tests | Cadence |
|----------|-------|------------------|---------|-------|---------|
| New account | Signal and learning | Fewest campaigns possible | Highest volume | None until 30+ conversions per cell | Daily checks, weekly batch edits |
| Running | Creative throughput and efficiency | Add catalog or messaging if relevant | Volume or value; cost goals at Scale | 1 creative test per week, 1 structural test per month | Weekly |
| Plateau | Find the constraint (creative, offer, CVR, saturation) | Horizontal expansion | Test value, incremental attribution | Offer and concept tests | Weekly plus monthly deep dive |
| Scaling | Marginal returns and pipeline | Cost-controlled scaler, new geos | Cost per result goal or ROAS goal with large budgets | Lift test before and after large scale steps | 2 to 3 times per week monitoring |

## Task router

| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Full account audit | [Audit checklist](references/audit-checklist.md), [Measurement](references/measurement-capi-attribution.md), [Account structure](references/account-structure.md), [Benchmarks](references/benchmarks.md) | Audit structure at the end of the audit checklist |
| New launch or new market | [Playbooks](references/playbooks.md) Play 1, [Campaign types and settings](references/campaign-types-and-settings.md), [Bidding and budgets](references/bidding-and-budgets.md) | Launch plan + change list |
| Choose campaign type or settings | [Campaign types and settings](references/campaign-types-and-settings.md) | Settings table with rationale |
| Bid strategy, targets, budget allocation | [Bidding and budgets](references/bidding-and-budgets.md) | Target calculation + change list |
| Audience, exclusions, signals, customer lists | [Audiences and signals](references/audiences-and-signals.md) | Signal plan |
| Creative testing, diversity, fatigue, partnership ads | [Creative system](references/creative-system.md) | Test plan + creative registry |
| Tracking, CAPI, EMQ, attribution, lift tests | [Measurement](references/measurement-capi-attribution.md) | Measurement findings + handoff to measurement |
| Weekly or monthly optimization | [Optimization loop and diagnostics](references/optimization-loop-and-diagnostics.md) | Weekly review template |
| Performance drop | [Diagnostics](references/optimization-loop-and-diagnostics.md) section 7, [Playbooks](references/playbooks.md) Play 4 | Incident report + 72-hour plan |
| Scaling plan | [Playbooks](references/playbooks.md) Play 3, [Bidding and budgets](references/bidding-and-budgets.md) | Scaling plan with gates |
| BFCM or seasonal plan | [Playbooks](references/playbooks.md) Play 6, [Catalog and commerce](references/catalog-and-commerce.md) | Seasonal calendar + change list |
| Lead quality, instant forms, CRM, click to message, WhatsApp | [Lead gen and messaging](references/lead-gen-and-messaging.md) | Lead quality plan |
| Catalog ads, collection, product sets | [Catalog and commerce](references/catalog-and-commerce.md) | Catalog plan |
| Disapprovals, restrictions, special ad categories, data restrictions | [Policy and account health](references/policy-and-account-health.md) | Appeal draft + remediation list |
| Data pulls, API, MCP, automation rules | [Tools, API and MCP](references/tools-api-mcp.md) | Query or script + data note |
| Benchmarks | [Benchmarks](references/benchmarks.md) | Benchmark comparison table |
| Source check | [Sources](references/sources.md) | Citations |

## The laws

1. Fix measurement before judging performance: no CAPI, no dedup, no backend check, no verdict.
2. Optimize to the deepest event that reaches about 50 per ad set per week; feed values when values differ.
3. Creative is targeting: diversity of concepts (persona, motivator, format, messenger) beats micro-variations, because similar ads share one retrieval entity.
4. Consolidate. Every campaign and ad set needs a reason the algorithm cannot see.
5. Respect learning: batch significant edits weekly; never edit a winning ad to "improve" it.
6. Budget per ad set must be able to buy learning: about 7 x target CPA per day, or consolidate.
7. Hard controls for legal and business must-haves (location, minimum age, exclusions); everything else is a suggestion.
8. Do not act on breakdown CPA alone (breakdown effect); price segments with value rules backed by backend data.
9. Targets come from unit economics (breakeven ROAS = 1 / contribution margin), not from benchmarks or last month.
10. Scale with creative first, then budget in steps of 15 to 30% (larger under campaign budget or cost goals), gated by backend confirmation.
11. Bid goals are levers on marginal cost; move them 10 to 20% at a time and give 3 to 7 days.
12. Judge platform ROAS against MER, new customer CAC and periodic lift tests; calibrate targets with an incrementality factor.
13. Lead gen is judged on cost per qualified lead or SQL from the CRM, never raw CPL.
14. Messaging ads only work with response time in minutes; check the inbox before the ads.
15. Review every Advantage+ creative enhancement; generative text off in regulated categories.
16. Keep existing customer share visible (audience segments) and controlled when the goal is growth.
17. Account health is infrastructure: verified business, 2FA, backup payment, no circumvention ever.
18. Date-check every reported drop against attribution changes (2026-01-12, 2026-03-03) and incidents before acting.
19. One lever per change, documented with hypothesis and expected effect, so results are attributable.
20. Never publish, pause, change budgets or bids without explicit human approval.

## Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|--------------|--------|-------|
| CPA up 20%+ over 7 days | Fatigue, CPM inflation, CVR drop, tracking change, edits | Decompose CPM, CTR, CVR; activity history; Events Manager; attribution dates | New concepts; CRO handoff; fix tracking; freeze edits |
| Conversions near zero suddenly | Pixel or CAPI broken, consent change, domain issue, restriction | Events Manager last received; backend orders; Account Quality | Handoff to measurement urgently; annotate reports |
| Reported conversions jump 2x | Dedup failure, duplicate events | event_id consistency, backend comparison | Fix dedup |
| Underspend | Tight cost or ROAS goal, low bid cap, narrow audience, disapprovals, payment | Spend vs budget, goals vs trailing CPA, ad status | Loosen goal 10 to 20%, broaden, fix ads or billing |
| Learning limited widespread | Fragmentation, low budgets, rare event | Ad set count vs conversions | Consolidate, raise budget, move event up |
| New ads get no spend | Incumbent favoritism | Spend share by ad age | Creative testing tool, pause weakest incumbents |
| High frequency, falling CTR | Saturation, too few concepts | Frequency 7d, concepts live | Add concepts, broaden geo, lower budget |
| Lead volume fine, quality poor | More volume forms, wrong placements, creative promise, slow follow-up | CRM qualification by source and placement | Higher intent forms, conversion leads, value rules, SLA |
| ROAS up but MER flat | Attribution over-credit, retargeting and existing customers | Audience segments, backend new customers | Shift to acquisition, new customer controls, lift test |
| Catalog ads weak | ID mismatch, poor images, wrong product set | Match rate, product breakdown | Fix IDs, lifestyle frames, margin sets |
| Restriction or mass disapproval | Policy pattern, identity, payment, circumvention flags | Account Quality | Policy play, appeal template |
| EU performance worse than elsewhere | Less personalized ads uptake, consent | EU vs non-EU trends | Judge on blended outcomes, creative-led targeting |

Expensive mistakes to catch in every review:
| Mistake | Cost pattern | Correction |
|---------|-------------|-----------|
| Optimizing lead gen on raw leads for months | Cheap junk leads, sales distrust | CRM stages via CAPI, conversion leads, cost per SQL |
| Scaling on platform ROAS while MER falls | Paying for conversions that would happen anyway | Backend reconciliation, new customer controls, lift test |
| Dozens of small ad sets "testing audiences" | Learning limited everywhere, overlap | Consolidate; test creative, not interests |
| Near-duplicate creative volume | Spend concentrates, no new reach | Concept diversity grid |
| Daily edits to bids and budgets | Constant learning resets | Weekly batched changes |
| Excluding placements or ages from breakdown CPA | Higher total CPA | Value rules backed by backend data, A/B test |
| Leaving all generative enhancements on in regulated categories | Claims violations, brand damage | Review toggles at launch |
| Reading a March 2026 conversion drop as a performance drop | Wrong cuts | Attribution date check |
| Creating new accounts after a ban | Permanent business-level ban | Fix cause, appeal, escalate |

What top operators do differently [Practitioner consensus]:
- Run a creative pipeline as a production system with weekly concept quotas and a registry, not ad hoc uploads.
- Spend more time on signal (CAPI quality, CRM stages, values) than on targeting.
- Use cost per result goals or ROAS goals with oversized budgets at Scale so spend follows efficiency.
- Keep a standing incrementality program and translate it into target adjustments.
- Change few things, at fixed times, and write down why.

## Cadence

| Cadence | What | Output |
|---------|------|--------|
| Daily (5 to 10 min) | Pacing, zero-conversion check, disapprovals, guardrail breaches, metastatus.com | Alert in journal only if action needed |
| Weekly | KPI scorecard, decomposition, creative kill and keep, new concepts, tests, budget moves, Opportunity Score triage | Weekly review file + change list |
| Monthly | Structure review, creative coverage grid, backend reconciliation, account health, Freshness check | Monthly report + journal |
| Quarterly | Full scored audit, incrementality test plan, strategy reset with growth-orchestrator | Audit file + test plan |

Heartbeat ownership: growth-orchestrator schedules; this skill supplies the checks.

## Guardrails and approvals

Hard rules:
- Never spend money, launch, publish, pause, delete, change bids, budgets, targeting, creatives, rules or catalog settings in a live account without explicit human approval in the conversation. Draft a change list instead.
- Never fabricate data, benchmarks, quotes or features. Label uncertainty.
- Never create new accounts, profiles or business portfolios to bypass restrictions.
- Never rename restricted events or cloak landing pages to evade policy.
- Never expose access tokens or personal data in outputs, journal or memory.
- Respect consent and privacy law (GDPR, KVKK, CCPA); customer lists only with lawful basis.

Change list format (required for any proposed live change):
```
| # | Level and object (name, ID) | Setting | Current | Proposed | Reason and evidence | Expected effect (metric, range, confidence) | Risk | Rollback |
```
Approval thresholds to highlight: any budget change over 30% in a week, any bid goal change over 20%, any structural rebuild, any new campaign, any enhancement that generates text or imagery, any action in a regulated category.

## Outputs

Save to `ads-master/outputs/meta-ads/YYYY-MM-DD_meta-ads_<description>.md`. Never overwrite; create a new dated file.

| Deliverable | Required sections |
|-------------|------------------|
| Audit | Summary and grade, data used, scored table, prioritized plan, change list, handoffs requested |
| Launch plan | Goal and economics, structure, settings table, creative plan, measurement checks, change list, success criteria and review date |
| Weekly review | Scorecard, decomposition, creative, tests, recommendations (change list), risks, handoffs requested |
| Scaling plan | Gates, steps by week, creative volume plan, monitoring, rollback triggers |
| Incident report | Timeline, root cause evidence, 72-hour plan, prevention |
| Test plan | Hypothesis, design, metric, sample or duration, stop rule, decision rule (also a row in EXPERIMENTS.md) |

Journal: `ads-master/journal/YYYY-MM-DD_HHMM_meta-ads_<topic>.md` for changes made, alerts, decisions, and handoff requests.
Memory: `ads-master/memory/meta-ads.md` only for patterns confirmed by at least two data points or one valid test (for example "UGC creator concepts beat studio statics by 30% CPA across 3 tests").

Handoff protocol (Ads Master agents do not call each other; nested subagents are disabled by design): (1) write a journal entry `ads-master/journal/YYYY-MM-DD_HHMM_meta-ads_handoff-<slug>.md` describing the request, data and deadline; (2) end the final response with a section "Handoffs requested" listing each target slug with a 2 to 4 line brief. The main session (growth-orchestrator) executes the delegation.

## Freshness protocol

Run before any launch, audit, policy answer or feature recommendation, and monthly.

| Check | Source | What to verify |
|-------|--------|----------------|
| API and attribution changes | https://developers.facebook.com/docs/graph-api/changelog and https://developers.facebook.com/blog/ | Current version, deprecated fields, attribution windows |
| Official MCP and CLI | https://developers.facebook.com/documentation/ads-commerce/ads-ai-connectors/ads-mcp-server/ads-mcp-server-overview | Tool list, scopes, beta status |
| Product changes | https://www.facebook.com/business/news and Ads Manager notices | New or renamed settings (Advantage+, placements, enhancements, testing tool) |
| Help Center rules | https://www.facebook.com/business/help | Learning phase, budgets, lead ads requirements, conversion leads eligibility |
| Policies | https://transparency.meta.com/policies/ad-standards/ | Restricted content, special ad categories, AI disclosure |
| Data restrictions | Events Manager dataset settings | Health, finance or other category flags |
| Platform health | https://metastatus.com/ | Incidents on relevant dates |
| Earnings and strategy | https://investor.atmeta.com/ | Price per ad trends, automation roadmap statements |
| Practitioner confirmation | Jon Loomer Digital, PPC Land, one weekly changelog | Real account rollouts of announced features |
| Regional | EU DMA page (digital-markets-act.ec.europa.eu), local regulators | EU personalization, TTPA, country rules |

How to log: create `ads-master/journal/YYYY-MM-DD_HHMM_meta-ads_freshness.md` listing each item checked, the date, URL, what changed and which reference section is now outdated. Propose updates to the global package through the human; do not edit global files from a project.

Watch list (verify on every freshness run): placement exclusion removal scope and any official Meta statement, WhatsApp Status availability by country and the 7-day free entry point window, Threads formats, Muse Image in Advantage+ creative, agentic Meta AI business assistant actions, AI audience discovery in Detailed Targeting (due end of 2026), incremental attribution model updates, Customer Lifecycle Strategy labels, Meta's stated goal of end-to-end AI ad automation by the end of 2026, official Ads MCP server tool list and scopes, v26.0 changes applying to all API versions on 2026-10-27.

## Reference index

- [Account structure](references/account-structure.md): delivery system, entity ID, consolidation rules, templates by tier and model, naming.
- [Campaign types and settings](references/campaign-types-and-settings.md): objectives, Advantage+ unification, audience controls, budgets, placements, creative enhancements.
- [Bidding and budgets](references/bidding-and-budgets.md): unit economics, bid strategies, value rules, new customer settings, incremental attribution, learning budgets.
- [Audiences and signals](references/audiences-and-signals.md): controls vs suggestions, custom audiences, lookalikes, segments, exclusions, signal engineering, privacy changes.
- [Creative system](references/creative-system.md): creative as targeting, diversity grid, volume by tier, specs, testing tool, partnership ads, fatigue.
- [Measurement, CAPI and attribution](references/measurement-capi-attribution.md): stack, dedup, EMQ, AEM, 2026 attribution changes, incrementality tools.
- [Optimization loop and diagnostics](references/optimization-loop-and-diagnostics.md): cadence, learning, breakdown effect, overlap, decomposition, diagnostic trees, weekly template.
- [Playbooks](references/playbooks.md): launch, weekly optimization, scaling, recovery, restriction, BFCM, plateau, Starter.
- [Lead gen and messaging](references/lead-gen-and-messaging.md): instant forms, conversion leads, lead quality, click to message, WhatsApp Status, calls.
- [Catalog and commerce](references/catalog-and-commerce.md): catalog foundations, Advantage+ catalog ads, product sets, collection, vertical catalogs.
- [Policy and account health](references/policy-and-account-health.md): restrictions and appeals, special ad categories, health data restrictions, EU and Turkey notes, brand safety.
- [Tools, API and MCP](references/tools-api-mcp.md): data access order, Marketing API queries, scripts, Ad Library, MCP servers, reporting tools, rules.
- [Benchmarks](references/benchmarks.md): earnings data, Meta-reported effects, independent studies, heuristics, baseline template.
- [Audit checklist](references/audit-checklist.md): scored audit across 8 sections with rubric.
- [Sources](references/sources.md): annotated sources with URLs and dates, freshness order.
