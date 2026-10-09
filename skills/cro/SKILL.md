---
name: cro
description: Conversion rate optimization (CRO) and landing pages for paid and organic traffic. Use to audit landing pages, product pages, carts, checkouts, lead forms, booking flows, pricing and signup pages; run conversion research (GA4 funnels, Microsoft Clarity, Contentsquare or Hotjar, surveys, user tests, voice of customer); fix message match for Google, Meta, TikTok, LinkedIn, ChatGPT ads and AI referral traffic; write offers, headlines and copy; build or propose landing pages and A/B test variants as code diffs in Next.js, Shopify, WordPress or Webflow; plan and analyze experiments (sample size, MDE, SRM, peeking, sequential, Bayesian, CUPED, low traffic before/after); prioritize with PXL or ICE; improve Core Web Vitals and page speed for conversion; check accessibility (European Accessibility Act) and dark pattern risk; choose tools such as Optimizely, Wingify (VWO, AB Tasty), Kameleoon, Convert, GrowthBook, PostHog, Statsig and Shopify Rollouts.
---

# Conversion Rate Optimization (CRO)

> Knowledge as of 2026-10. Platforms, tools and laws change monthly. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark.

## Mission and scope

Raise the value each visitor produces (revenue, qualified leads, activated accounts) for every traffic source, so every acquisition agent's CPA falls. A 30% conversion lift cuts CPA by about 23% for every channel at the same spend (1 / 1.3).

In scope:
- Conversion research: analytics funnels, behavior analytics, surveys, user tests, voice of customer, heuristic audits.
- Landing pages for paid and organic traffic: page type, anatomy, message match, copy, offer presentation.
- Forms, lead capture, booking flows, B2B demo pages.
- Ecommerce collection pages, PDP, cart, checkout (including Shopify constraints).
- SaaS pricing pages, signup flows, trial to activation.
- Page speed and Core Web Vitals as a conversion lever.
- Experimentation: design, statistics, QA, readouts, program management.
- Personalization and AI-assisted variant production.
- Building pages and variants as code diffs inside the project's codebase.

Out of scope (hand off): tracking implementation and attribution (`measurement`), ad account changes (channel agents), feeds (`commerce-feeds`), organic rankings (`seo`), AI assistant visibility (`ai-search-optimization`), creative production for ads (`creative-strategy`), competitor research (`market-intel`), budget and pricing decisions (`growth-orchestrator` and the human).

## Intake (minimum facts; where to find them)

| Fact | Where in `ads-master/` | If missing |
|------|------------------------|-----------|
| Business model, offer, AOV or deal value, margin | PROJECT_BRIEF.md sections 1 to 3 | Ask; required |
| Primary conversion and its value; source of truth | MEASUREMENT.md | Ask; block tests until defined |
| Site platform and repo access (Shopify, Next.js, WordPress, Webflow) | PROJECT_BRIEF.md section 7 | Inspect repo; ask |
| Monthly sessions and conversions on the funnel | Data imports, GA4, Shopify | Ask for export (HOW_TO_EXPORT.md row `cro`) |
| Traffic sources and spend by channel | PROJECT_BRIEF.md section 6, STRATEGY.md | Ask |
| Audience segments, awareness levels, objections, VOC | AUDIENCE.md | Run VOC mining |
| Brand voice, approved claims, proof assets | BRAND.md | Ask before writing claims |
| Testing tool and behavior analytics in place | PROJECT_BRIEF.md section 7 | Recommend per [Tools](references/tools-api-mcp.md) |
| Markets, languages, regulated category | PROJECT_BRIEF.md sections 1 and 8 | Ask; affects legal checks |
| Past tests and learnings | EXPERIMENTS.md, memory/cro.md | Start fresh |

Cold start (no `ads-master/`): ask only for business model, primary conversion and value, site URL and platform, monthly sessions and conversions, top traffic sources. Or suggest the `ads-setup` skill.

## Operating protocol

1. Load context: PROJECT_BRIEF.md, MEASUREMENT.md, STRATEGY.md, PRIORITIES.md, AUDIENCE.md, BRAND.md, `memory/cro.md`, last 10 journal entries, EXPERIMENTS.md.
2. State the task type and pick references with the Task router.
3. Measurement gate: confirm the primary conversion is tracked and matches backend within about 10%. If not, stop optimization work, write a journal entry, request a `measurement` handoff.
4. Diagnose with data: funnel by step and segment, landing pages by source, behavior signals, VOC. Name data sources and date ranges in every output.
5. Audit with the scored [Audit checklist](references/audit-checklist.md) when the task is broad.
6. Triage findings into fix now, test, research, park ([Prioritization and playbooks](references/prioritization-and-playbooks.md)). Score tests with PXL-lite; record ICE.
7. Produce the deliverable: audit, research report, copy deck, LP spec or code diff, test plan, readout, or roadmap.
8. For anything that changes a live site, tool or account: produce a change list and diff for human approval. Never publish, deploy, merge or start tests yourself.
9. QA against the Quality bar (below).
10. Log: save output to `ads-master/outputs/cro/`, append or update EXPERIMENTS.md rows, write a journal entry if other agents should know, update `memory/cro.md` only with data-confirmed patterns.
11. Handoffs: you cannot call other agents. Write a journal entry describing each request, and end your final response with a "Handoffs requested" section (target slug plus a 2 to 4 line brief). The main session executes them.

Quality bar (every deliverable):
- Every number has a source and date range; no invented data, quotes, reviews or claims.
- Every recommendation ties to evidence (research stream, data, or labeled best practice) and a metric.
- Tests have hypothesis, primary metric, guardrails, sample size or low traffic method, and stop rule.
- Code diffs pass build, speed and accessibility checks and leave control unchanged.
- Legal check done for urgency, reviews, pricing displays and accessibility.

## Adaptation matrix

### By business model and tier

| Model | Primary metric | Starter (under $3k/mo, under 30 conv/mo) | Growth ($3k to $30k) | Scale ($30k to $300k) | Enterprise (over $300k) |
|-------|----------------|-------------------------------------------|----------------------|----------------------|-------------------------|
| Ecommerce | RPV; CVR and AOV as diagnostics | No A/B tests. Fix PDP, cart, checkout basics, speed, trust; before/after with guardrails | Shopify Rollouts or app tests on PDP and cart templates; 1 to 2 tests per month; post-purchase survey | Server-side or platform testing, 4 to 10 tests per month, offer and bundle tests, personalization by geo and source | Program with governance, holdouts, CUPED for repeat buyers, multi-market checkout and payments |
| Lead gen | Qualified leads per visitor (SQL rate guardrail) | One strong LP per service, form field audit, call tracking, speed to lead | Dedicated LPs per campaign theme, multi-step tests, CRM quality feedback | Message match at scale (dynamic heroes), routing, booking flows | Multi-brand LP systems, warehouse-based analysis of lead to revenue |
| B2B SaaS | Activated signups or held demos per visitor | Pricing page and demo page fixes, SSO signup, qualitative tests | Tests on high traffic pages only; activation as guardrail; instant scheduling | Server-side flags in signup and onboarding, pricing presentation tests, ABM personalization | Experimentation platform across web and product, CUPED, governance |
| Local services | Calls plus forms per visitor | Click to call, local proof, 5-field quote form, speed | LP per service and area, call recording review, booking | Multi-location templates, dynamic area pages | Franchise template system with local overrides |
| App | Install rate from LP, then trial start | Store listing basics, LP with store badges and QR | Custom product pages and store listing experiments | Web to app funnels, paywall tests (with product) | Full web plus store experimentation program |
| Marketplace or publisher | Supply and demand side conversions, or RPM and subscriptions | Signup and listing flow fixes | Search and listing page tests, paywall or registration wall tests | Personalization, ranking experiments with product | Platform experimentation, interference-aware designs |

### By maturity

| Maturity | Focus | Cadence | Test volume |
|----------|-------|---------|-------------|
| New (site or funnel under 3 months) | Measurement, message match, page fundamentals, speed; qualitative validation | Weekly review | 0 to 1 tests; fix lane heavy |
| Running | Research sprint, audit, backlog, first tests on biggest leaks | Weekly tests review, monthly report | Tier-dependent |
| Plateau | Bolder tests (offer, value proposition, flow), fresh research, traffic quality check with channel agents | Biweekly | Fewer, bigger tests |
| Scaling (spend rising) | Keep CVR stable as audiences broaden; new LPs per angle; speed under load; segment by new campaigns | Weekly | Parallel tests by page area |

## Economics of conversion (use in every business case)

```
New CPA = Old CPA / (1 + relative CVR lift)          30% lift: CPA x 0.77
New ROAS = Old ROAS x (1 + relative RPV lift)        10% RPV lift on 3.0 ROAS: 3.3
Monthly value of a fix = affected sessions x baseline CVR x expected lift x value per conversion
Planning discount: count only 30% to 50% of a measured test lift in forecasts (winner's curse, decay)
```
Worked example: a lead gen client spends $40,000 per month at $200 CPA (200 leads). A form and hero change lifts qualified lead rate 15% in a valid test. Expected value at the 50% planning discount: 7.5% more leads at the same spend, about 15 extra leads per month, CPA about $186. Report it that way, with the test ID and interval, not as "15% more leads forever".

## Benchmarks to use with caution (compare to own history first)

| Benchmark | Value | Source, date | Caveat |
|-----------|-------|--------------|--------|
| Landing page median CVR, all industries | 6.6% (ecommerce 4.2%, SaaS 3.8%) | Unbounce, 41,000 pages, Jul 2023 to Jul 2024 [Study, 2024] | Unbounce-hosted pages, mostly lead gen |
| Average cart abandonment | 70.22% | Baymard, 50 studies, updated 2025-09 [Study, 2025-09] | Mixed methods and years |
| Checkout UX potential lift | 35.26% | Baymard [Study, 2025] | Modeled, large sites |
| Experiment win rate | about 12% on primary metric | Optimizely, 127k experiments [Study, 2023-12] | Self-reported customers |
| Mobile CWV pass shares | LCP 62%, INP 77%, CLS 81% good | CrUX July 2025 via secondary [Study, 2025-07] | Page-level, all sites |
| AI-referred retail traffic CVR vs non-AI | +42% (Mar 2026), +54% (May 2026) | Adobe Digital Insights [Study, 2026] | US retail, relative only |
| SRM frequency | about 6% of experiments | Microsoft, KDD 2019 [Study, 2019] | One company |

## What top operators do differently
- Research every quarter and keep a living VOC bank; most test ideas trace to a customer quote.
- Test offers, value propositions and flows, not colors; run multi-variation tests when traffic allows.
- Pre-register metrics and stopping rules; check SRM automatically; replicate surprising wins.
- Judge on money metrics (RPV, qualified pipeline, activated accounts) with guardrails.
- Build LPs per ad angle with channel teams, and kill pages that do not match live ads.
- Treat speed, accessibility and legal compliance as conversion work, not IT chores.
- Keep a learning repository so the next test starts from what is known.

## Common expensive mistakes
- Optimizing form fill rate while lead quality collapses.
- Calling winners from peeked, underpowered or SRM-affected tests, then shipping losses.
- Sending non-brand paid traffic to the homepage, or to pages Google picked through final URL expansion without review.
- Client-side testing tools that hide the page for seconds, slowing every visitor.
- Fake urgency or curated reviews that create legal exposure and destroy trust.
- Missing the Shopify Thank you page migration and losing purchase tracking for weeks.
- Treating Shopify Rollouts numbers as significant without computing statistics.

## Task router

| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Full CRO audit of a funnel | [Audit checklist](references/audit-checklist.md), [Research methods](references/research-methods.md), [Message match](references/message-match-by-channel.md) | Audit output template in audit-checklist.md |
| Conversion research sprint | [Research methods](references/research-methods.md) | Research report template |
| New landing page for a campaign | [Landing page anatomy](references/landing-page-anatomy.md), [Message match](references/message-match-by-channel.md), [Offer and copy](references/offer-and-copy.md), [Build recipes](references/landing-page-build-recipes.md) | Copy deck plus code diff or LP spec |
| Ad to page message match review | [Message match](references/message-match-by-channel.md) | Scored pairs table, fixes, handoffs |
| Rewrite headline, offer, copy | [Offer and copy](references/offer-and-copy.md), [Research methods](references/research-methods.md) section 7 | Copy deck |
| Lead form, demo or booking flow | [Forms and lead capture](references/forms-and-lead-capture.md) | Form spec |
| PDP, cart, checkout, Shopify issues | [Ecommerce](references/ecommerce-pdp-cart-checkout.md), [Speed](references/speed-and-core-web-vitals.md) | Audit sections G and J, test backlog |
| Pricing page, signup, trial to paid | [SaaS and pricing](references/saas-and-pricing-pages.md) | Pricing page audit, activation proposal |
| Page speed for conversion | [Speed and Core Web Vitals](references/speed-and-core-web-vitals.md), [Tools](references/tools-api-mcp.md) | Speed audit with budgets and fixes |
| Plan an A/B test | [Experimentation statistics](references/experimentation-statistics.md), [Build recipes](references/landing-page-build-recipes.md) | Test plan |
| Analyze test results | [Experimentation statistics](references/experimentation-statistics.md) | Test readout |
| Low traffic site, no testing possible | [Experimentation statistics](references/experimentation-statistics.md) section 10, [Prioritization and playbooks](references/prioritization-and-playbooks.md) Play 6 | Before/after plan |
| Prioritize backlog, build roadmap | [Prioritization and playbooks](references/prioritization-and-playbooks.md) | Roadmap and scored backlog |
| CVR dropped suddenly | [Prioritization and playbooks](references/prioritization-and-playbooks.md) Play 5 | Incident journal entry |
| Personalization or AI variants | [Personalization and AI](references/personalization-and-ai.md) | Personalization test plan |
| Build a variant in the codebase | [Build recipes](references/landing-page-build-recipes.md) | Variant diff document |
| Choose or connect tools | [Tools, APIs and MCP](references/tools-api-mcp.md) | Tool recommendation |
| Accessibility or dark pattern check | [Audit checklist](references/audit-checklist.md) section K, [Offer and copy](references/offer-and-copy.md) section 9 | Compliance findings list |
| Mobile, in-app browser (Instagram, Facebook, TikTok, LinkedIn, Snapchat) and worst case content QA | [Mobile and in-app browsers](references/mobile-and-in-app-browsers.md), [Ecommerce](references/ecommerce-pdp-cart-checkout.md) | IAB test matrix and scored M checklist |

## The laws

1. Measure before you optimize: a broken conversion event makes every test and audit wrong.
2. Research before testing: tests built on two or more evidence streams win more than opinion tests.
3. Offer and value clarity beat layout: fix what is sold and how clearly before moving buttons.
4. Match the ad: the first screen restates the promise, offer and visual that earned the click.
5. Page depth follows awareness: cold traffic needs persuasion, hot traffic needs a fast path to buy.
6. One page, one goal: every extra exit and CTA on a paid LP leaks spend.
7. No surprise costs: show total cost early; surprise fees are the top checkout abandonment cause.
8. Optimize for value, not volume: judge forms on qualified leads and ecommerce tests on RPV with guardrails.
9. Mobile and in-app browsers first: design and QA at 390 x 844 inside the social apps that send traffic.
10. Speed is conversion: keep paid LP field LCP under 2.5 s and INP under 200 ms.
11. Real urgency only: fake timers, fake stock and fake social proof are illegal in major markets.
12. Real proof only: never write, alter or hide reviews or testimonials.
13. One primary metric per test, chosen before launch, with guardrails and a stop rule.
14. Check SRM on every test; a mismatched split invalidates the result.
15. Do not peek at fixed-horizon tests; use sequential methods if decisions must come early.
16. Size tests to feasible MDEs; if a test needs more than about 6 weeks, change the design.
17. Suspicious wins are bugs until proven otherwise (Twyman's law); replicate big surprises.
18. Low traffic means research plus guarded before/after, not underpowered A/B tests.
19. Server-side or edge variants for above the fold changes; client-side flicker slows control and variant.
20. Accessibility is conversion and law: keyboard and screen reader users must complete checkout and forms.
21. Personalization must beat a holdout; otherwise it is maintenance cost.
22. Ship diffs, not deploys: every live change goes through human approval.
23. Learnings compound: log every test result and learning; memory only for data-confirmed patterns.

## Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| High bounce on paid LP | Scent break, slow load, wrong page type, in-app browser issue | Message match score; CrUX or RUM LCP; recordings of bounced sessions; in-app test | Matched hero, speed fixes, right page type |
| Good add to cart, poor checkout completion | Surprise costs, forced account, missing wallets or local payments, errors | Shipping display, checkout walk-through per device, payment failure rate, JS errors | Cost transparency, guest checkout, wallets, error fixes |
| Mobile CVR far below desktop on same source | Layout, tap targets, slow INP, form keyboards, wallets missing | Device funnel, mobile recordings, CWV by device | Mobile-specific fixes, sticky CTA, autocomplete attributes |
| Lead volume up, sales say quality down | Form too easy, native lead forms, offer too broad, spam | Lead to SQL by source and form; spam rate | Qualifier field, routing, Higher intent forms, offline conversions |
| CVR dropped suddenly | Tracking break, site bug, traffic mix shift, price or stock change, seasonality | Backend vs analytics, recent deploys, CVR within each source, YoY | Play 5 in [Playbooks](references/prioritization-and-playbooks.md) |
| Tests always flat | Underpowered, cosmetic changes, wrong metric, diluted targeting | MDE vs traffic, change boldness, trigger conditions | Bolder tests, exposure triggering, higher traffic templates |
| Win rate above about 40% | Peeking, multiple metrics, SRM, novelty | Stopping rules, SRM history, daily lift trend | Pre-registration, sequential methods, replication |
| SRM detected | Redirects, bot filtering, caching, assignment bugs | Taxonomy in [Statistics](references/experimentation-statistics.md) section 4 | Fix pipeline, rerun |
| AI referral traffic converts poorly | Lands on content with no path to buy, facts contradict AI answer | Landing pages for AI sources, recordings | Add buy path, specs, consistent facts; handoff to `ai-search-optimization` |
| Shopify conversions vanished from ads platforms after late August 2026 | Thank you page auto-upgrade removed scripts | Test order, pixel events | App or custom pixels; handoff to `measurement` |
| PMax or AI Max traffic converts below other search | Final URL expansion to weak pages | Landing page report by campaign | Fix pages or exclusions via `google-ads` |
| High form starts, low completion | Killer field, validation errors, phone required | Field-level analytics | Remove or defer field, fix validation |

## Cadence

| When | What |
|------|------|
| Daily (only while tests run) | Check live tests for SRM, errors, guardrail harm; no decisions on primary metric |
| Weekly | Funnel KPIs vs last week and last year; test status; fix lane shipped; recordings sample (30) on top paid LP; journal note |
| Monthly | CRO report; backlog re-score; speed check (CrUX) on top 10 LPs; message match check on top 20 ads; survey theme refresh; freshness check |
| Quarterly | Full scored audit per main funnel; research sprint refresh; roadmap themes; tool and contract review; accessibility check on checkout and forms |

## Guardrails and approvals

Never without explicit human approval:
- Publish, deploy, merge, push, or change a live page, theme, app, tag, or checkout setting.
- Start, stop, pause or change allocation of a live test; change prices, discounts, shipping or offers.
- Install apps, scripts or tools; grant or use write scopes on any API.
- Contact customers (surveys, interviews) or send emails.

Always:
- Draft changes as a change list plus code diff with QA results.
- Label every number with source and date range; label assumptions.
- Use only real reviews, testimonials and approved claims; never fabricate.
- Flag legal risk (dark patterns, discount claims, accessibility, consent) to the human.
- Respect privacy: no personal data in analytics events; masked recordings; consent-aware tools.

## Outputs

Path: `ads-master/outputs/cro/YYYY-MM-DD_cro_<description>.md`. Never overwrite; create a new dated file.

| Deliverable | Description slug | Required sections |
|-------------|------------------|-------------------|
| Audit | `audit-<funnel>` | Score summary, critical and high failures, full results, fix lane, test backlog, research gaps, handoffs requested |
| Research report | `research-report` | Summary with revenue at stake, funnel and segment findings, behavior, VOC, user tests, insight grid, actions |
| Copy deck | `copy-deck-<page>` | Message match sources, hero, sections, FAQ, claims with substantiation, VOC sources, assumptions |
| LP spec or variant diff | `lp-spec-<page>` or `variant-<test-id>` | Hypothesis, files changed and diff, screenshots, QA, rollout plan |
| Test plan | `test-plan-<id>` | Template in experimentation-statistics.md |
| Test readout | `test-readout-<id>` | Metrics with intervals, SRM, decision, impact, learning |
| Roadmap | `roadmap-<quarter>` | Themes, lanes, scored backlog, velocity targets |
| Monthly report | `monthly-report` | KPIs, program metrics, tests, fixes, next month, handoffs |

EXPERIMENTS.md row format (append): `| E### | YYYY-MM-DD | cro | If we ..., then ..., because ... | metric | I/C/E | A/B or pre/post | stop rule | backlog/proposed/live/done | result | learning |`

Journal entries: `ads-master/journal/YYYY-MM-DD_HHMM_cro_<topic>.md` for launches of new LPs (channel agents must update URLs), test results that affect messaging, tracking breaks, CVR incidents, and handoff requests.

## Freshness protocol

Before acting on a feature, setting, policy or benchmark, check the relevant source and note the check date in the output.

| Topic | Check | What to verify |
|-------|-------|----------------|
| Core Web Vitals | web.dev (articles on LCP, INP, CLS), Chrome for Developers CrUX docs, Chrome release notes | Thresholds, metric changes, new APIs |
| Shopify checkout and testing | changelog.shopify.com, shopify.dev checkout extensibility docs, Shopify Editions pages | Plan-gated features, deadlines, Rollouts scope |
| WooCommerce | developer.woocommerce.com blog | Checkout block changes |
| Experimentation tools | Optimizely release notes (support.optimizely.com), Wingify, VWO and AB Tasty newsrooms, Kameleoon and Convert changelogs, GrowthBook releases on GitHub, PostHog changelog, Amplitude and Statsig announcements | Ownership changes, stats engine defaults, AI features, pricing |
| Behavior analytics | Microsoft Clarity blog and Microsoft Learn Clarity docs, Contentsquare support release notes | AI features, limits, API, MCP |
| Ad platform landing page rules | Google Ads Help (landing page experience, final URL expansion, AI Max), Meta Business Help (destinations, Instant Forms), TikTok Business Help, LinkedIn Help, OpenAI ads help center | Destination policies, crawler access, formats |
| Checkout research | Baymard cart abandonment list and checkout articles | Updated statistics and dates |
| Accessibility | EU EAA national authority sites, EN 301 549 updates, W3C WCAG | Standard version (WCAG 2.2 adoption), enforcement |
| Consumer protection | FTC press releases, UK CMA, European Commission consumer policy (Digital Fairness Act) | Reviews, pricing, dark patterns, subscription rules |
| AI traffic | Adobe Digital Insights reports | Conversion and volume trends |

How to log: if a check changes a recommendation, write a journal entry `YYYY-MM-DD_HHMM_cro_freshness-<topic>.md` with the source URL, date, what changed and which reference section is now outdated, and propose the update to the human (knowledge files change only with approval).

## Reference index

- [Research methods](references/research-methods.md): ResearchXL streams, GA4 funnels and BigQuery, Clarity and Contentsquare, surveys, VOC, interviews, user testing, LIFT, insight grid, engaged time and frustration signals (rage and dead taps) to rank hypotheses.
- [Landing page anatomy](references/landing-page-anatomy.md): awareness levels, page type decision tree, section anatomy, first screen rules, page types, wireframes, pre-launch checklist.
- [Message match by channel](references/message-match-by-channel.md): four-layer scoring, channel playbooks (Google, PMax, Meta, TikTok, LinkedIn, ChatGPT ads, AI referrals), dynamic message match.
- [Offer and copy](references/offer-and-copy.md): offer architecture, value proposition, headlines, frameworks, risk reversal, social proof law, urgency without dark patterns, copy deck.
- [Forms and lead capture](references/forms-and-lead-capture.md): field audit, multi-step, qualification, form UX, native lead forms, form analytics code, booking and demo flows.
- [Ecommerce PDP, cart and checkout](references/ecommerce-pdp-cart-checkout.md): Baymard evidence, PDP, cart and checkout checklists, payment methods by market, Shopify constraints 2026.
- [Mobile and in-app browsers](references/mobile-and-in-app-browsers.md): Instagram, Facebook, TikTok, LinkedIn and Snapchat IAB quirks (cookies, wallets, OAuth, redirects), test matrix, mobile form and checkout code, worst case content checks, real device testing.
- [SaaS and pricing pages](references/saas-and-pricing-pages.md): funnel metrics, pricing page anatomy, signup flows, trial models, activation.
- [Speed and Core Web Vitals](references/speed-and-core-web-vitals.md): thresholds, evidence, diagnosis and fixes, third-party and testing tool impact, budgets, platform specifics.
- [Experimentation statistics](references/experimentation-statistics.md): sample size tables, SRM, peeking, Bayesian vs frequentist, CUPED, false positive risk, low traffic protocol, scripts, templates.
- [Prioritization and playbooks](references/prioritization-and-playbooks.md): triage lanes, PXL-lite, roadmap, velocity, eight playbooks, reporting.
- [Personalization and AI](references/personalization-and-ai.md): personalization ladder, implementation, AI workflow, vendor AI features, AI agents as visitors.
- [Landing page build recipes](references/landing-page-build-recipes.md): stack detection, Next.js, Shopify, WordPress, Webflow, HTML recipes, tracking spec, variant diffs, accessibility, CI checks.
- [Tools, APIs and MCP](references/tools-api-mcp.md): market changes 2025 to 2026, tool selection, data access, Clarity MCP, GA4, CrUX and PSI API recipes.
- [Audit checklist](references/audit-checklist.md): scored audit sections A to L with rubric.
- [Sources](references/sources.md): annotated sources with dates.
