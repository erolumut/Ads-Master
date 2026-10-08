---
name: tiktok-ads
description: TikTok advertising playbook for TikTok Ads Manager and TikTok Shop. Use to audit, launch, optimize, scale, troubleshoot or recover TikTok accounts for ecommerce, TikTok Shop sellers, apps, lead gen, B2B and brand campaigns. Covers Smart+ (upgraded modular controls), manual campaigns, GMV Max (Product and LIVE, ROI protection, GMV Max Pro), Spark Ads, TikTok One creators and affiliates, Search Ads and Automatic Search Placement, TopView and TopReach, TikTok Ad Network (Pangle), bidding (Maximum Delivery, Cost Cap, Minimum ROAS, Highest Value, Target ROI), budgets and learning phase, Pixel and Events API deduplication, attribution windows and EVTA, lift studies, Symphony AI creative, creative fatigue, ad policies, suspensions and appeals, the TikTok Marketing API and the TikTok for Business MCP server. Trigger phrases include TikTok ads, TikTok Shop ads, GMV Max, Smart+, Spark Ads, TikTok pixel, TikTok audit, TikTok ROAS, TikTok lead forms, TikTok creative.
---

# TikTok Ads

> Knowledge as of 2026-10. Platforms change monthly. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark. Research note: in the 2026-10 cycle, primary pages could not be fetched directly and the search budget was capped, so several items carry [Unverified] labels. Verify those in the live account before relying on them.

## Mission and scope

Run TikTok as a profitable, measurable growth channel: find the creative and creator engine that scales, feed the algorithm clean signal, set targets from real unit economics, and protect the account.

In scope: TikTok Ads Manager (auction, Reach and Frequency, reservation formats), Smart+ (Sales, Lead Generation, App Promotion, Traffic, Search), manual campaigns, GMV Max (Product, LIVE), TikTok Shop ads economics, Spark Ads, TikTok One and affiliate creators, Search Ads Campaign, Automatic Search Placement, Search Hubs, TopView and TopReach, TikTok Ad Network (formerly Pangle), Lead Generation (Instant Form, website, DM, Agentic Leads), app campaigns, Pixel and Events API requirements, attribution and lift, policies and account health, Marketing API and MCP.

Out of scope (hand off): building the tracking stack (measurement), catalog and Shop listing data (commerce-feeds), cross-channel concepts and production systems (creative-strategy), landing pages (cro), channel budget split (growth-orchestrator), competitor research beyond TikTok ad libraries (market-intel), organic TikTok content strategy beyond Spark Ads candidates (creative-strategy).

## Intake (minimum facts; where to find them)

| Fact | Where in `ads-master/` | If missing (cold start) ask |
|------|------------------------|------------------------------|
| Business model, markets, currency | PROJECT_BRIEF.md sections 1, 5 | "What do you sell, where, and in which currency?" |
| Destination: website, TikTok Shop, app, lead form | PROJECT_BRIEF.md 6, 7 | "Do you sell on your site, TikTok Shop, both, or drive app installs or leads?" |
| Unit economics: AOV, contribution margin, target CPA or ROAS, breakeven | PROJECT_BRIEF.md 3 | "AOV and contribution margin after shipping, fees and returns?" |
| Monthly TikTok budget and tier | PROJECT_BRIEF.md 5 | "Monthly TikTok budget?" |
| Primary conversion and source of truth | MEASUREMENT.md | "What counts as a conversion and where is the truth (Shopify, CRM)?" |
| Pixel, Events API, dedup status | MEASUREMENT.md tracking table | "Is the TikTok Events API live with event_id deduplication?" |
| Account access: Business Center owner, advertiser ID, Shop ID | PROJECT_BRIEF.md 6, 7 | "Who owns the Business Center? Advertiser ID?" |
| Data access: MCP, API, connector or CSV | PROJECT_BRIEF.md 7, data/imports/ | "Can I use the TikTok for Business MCP server, or will you export CSVs?" |
| Regulated category and claims | PROJECT_BRIEF.md 8, BRAND.md | "Any regulated category or forbidden claims?" |
| Creative capacity: creators, editors, monthly video output | BRAND.md, STRATEGY.md | "How many new videos can you produce per week?" |
| Channel role and KPI | STRATEGY.md | "Is TikTok for new customer acquisition, Shop GMV, installs or leads?" |

Cold start with no `ads-master/`: ask only the first 6 rows, state assumptions, and suggest running the `ads-setup` skill.

## Operating protocol

1. Load context: PROJECT_BRIEF, MEASUREMENT, STRATEGY, PRIORITIES, `memory/tiktok-ads.md`, last 10 journal entries.
2. Freshness check if the task touches features, policies, defaults or benchmarks (section "Freshness protocol").
3. Data: pull via MCP or API (read-only) or read CSVs in `data/imports/`. Write down source, date range and attribution setting.
4. Measurement gate: run the weekly health checks in [Measurement](references/measurement-events-api-attribution.md). If broken, stop optimization work, write a journal alert and request a measurement handoff.
5. Diagnose with the decomposition CPA = CPM / (1,000 x CTR x CVR) and the diagnostic order in [Optimization](references/optimization-and-diagnostics.md).
6. Prioritize: score each action by impact x confidence x ease (1 to 5 each). Creative and measurement fixes usually rank first.
7. Act: produce the deliverable (audit, plan, change list, brief, report). Every live change is a row in a change list for human approval.
8. QA against the Quality Bar (below).
9. Log: output file, journal entry, EXPERIMENTS.md rows for tests, memory only for confirmed patterns.
10. Handoffs: subagents cannot call each other. Write a journal entry describing each request, then end the final response with a "Handoffs requested" section (target slug plus a 2 to 4 line brief). The main session running growth-orchestrator executes them.

Quality Bar for every deliverable:
- States data source, date range, attribution window and which numbers are platform vs calibrated.
- Every number has a source; no invented benchmarks.
- Every recommendation has a reason, an expected effect, a risk and a rollback trigger.
- Respects tier constraints (budget per ad group at least 10x CPA, creative cadence).
- Labels claims about platform features with evidence labels and dates.

## Adaptation matrix

### By business model and tier

| Model | Starter (under $3k/mo) | Growth ($3k to $30k) | Scale ($30k to $300k) | Enterprise (over $300k) |
|-------|------------------------|----------------------|------------------------|-------------------------|
| Ecommerce (website) | 1 manual Sales campaign, 1 broad ad group, Maximum Delivery, Purchase if 25+/week else Initiate Checkout; 3 to 5 creatives; KPI: CPA vs breakeven; weekly review | Smart+ Sales (Web or Catalog) + manual test lane; Spark Ads; 5 to 10 new ads/week; KPI: calibrated CPA, MER contribution | Smart+ by product line, Catalog Ads, Search Ads Campaign, creator roster, Cost Cap or Min ROAS guardrails, survey + geo test; 15 to 40 ads/week | Per market campaigns, brand layer (TopReach, R&F), Search Hubs, lift calendar, API/MCP reporting, MMM inputs; 40+ ads/week |
| TikTok Shop seller | Product GMV Max on Max Delivery 3 to 5 days then Target ROI; affiliates via open collaboration; KPI: ROI vs breakeven ROI | Product GMV Max by margin band, LIVE GMV Max weekly, affiliate targeted invites, creative queue management | GMV Max Pro or cost-aware settings if offered, ROI protection discipline (20+ orders/day), Creative Boost, LIVE program | Multi-market Shop, brand formats feeding Shop search, holdout reads of total GMV |
| Lead gen (B2C services) | 1 Lead Gen campaign, Instant Form with 2 qualifying questions, geo + age floor; KPI: CPQL | Smart+ Lead Generation or 2 to 3 ad groups by offer, CRM integration, CRM events back | CRM event optimization, regional campaigns aligned with sales capacity, Agentic Leads test cell | Multi-product, offline conversions, lift on qualified pipeline |
| B2B SaaS | Usually skip or awareness test with founder content; KPI: cost per demo with CRM proof | Website form leads, callout hooks, Spark from founder or practitioners; KPI: cost per SQL | Retarget engagers with proof content, Search Ads on category terms, CRM events | Brand formats for category creation; coordinate with linkedin-ads |
| Local services | Radius targeting, Instant Form or call, dayparting to staffed hours; KPI: cost per booked job | Per-city ad groups only where budget allows 10x CPA each | Multi-location campaigns, DM and messaging lead destinations | Franchise structure per region |
| App | Smart+ App or manual App promotion per OS, optimize to install; KPI: CPI and Day 7 retention | AEO on key event, MMP cohorts, Auto-select creative | VBO, app retargeting, TikTok Ad Network test cell, SKAN tuning | Per-market, per-OS portfolios, incrementality via geo holdouts |
| Marketplace or publisher | Traffic with Landing page view, or Sales on transactions; KPI: revenue per session vs CPC | Value-based optimization with revenue passed back; supply and demand campaigns split | Catalog or Search Ads on inventory terms | Market-level brand plus performance |

### By maturity

| Maturity | Focus | Structure changes | Cadence | Tests |
|----------|-------|-------------------|---------|-------|
| New account | Measurement gate, first winners, learning exit | 1 campaign, 1 to 2 ad groups | Daily checks, weekly review | Concept tests only |
| Running | Creative system and calibration | Add Smart+ scaling lane and testing lane | Weekly | Creative concepts, Smart+ vs manual split test |
| Plateau | New pockets of demand | Search Ads, new concepts, creators, Catalog, new markets | Weekly + monthly deep dive | Offer tests, audience vs broad, lift test |
| Scaling | Marginal CPA control | Duplicate-to-scale, Cost Cap guardrails, brand layer | Twice weekly at Scale tier | Budget step tests, geo holdout |

## Task router

| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Full account audit | [Audit checklist](references/audit-checklist.md), [Measurement](references/measurement-events-api-attribution.md), [Account structure](references/account-structure-and-campaign-types.md) | Audit report (scored) |
| Launch plan (website) | [Account structure](references/account-structure-and-campaign-types.md), [Bidding](references/bidding-and-budgets.md), [Creative](references/creative-for-tiktok.md), [Playbooks](references/scaling-playbooks.md) | Launch plan + change list |
| TikTok Shop / GMV Max setup or review | [TikTok Shop and GMV Max](references/tiktok-shop-and-gmv-max.md), [Spark and creators](references/spark-ads-and-creators.md) | GMV Max plan or weekly review |
| Smart+ vs manual decision | [Account structure](references/account-structure-and-campaign-types.md), [Bidding](references/bidding-and-budgets.md) | Decision memo + split test row |
| Bid strategy or budget changes | [Bidding](references/bidding-and-budgets.md), [Optimization](references/optimization-and-diagnostics.md) | Change list |
| Performance drop diagnosis | [Optimization](references/optimization-and-diagnostics.md), [Measurement](references/measurement-events-api-attribution.md), [Playbooks](references/scaling-playbooks.md) | Diagnosis report + change list |
| Creative review, fatigue, briefs | [Creative](references/creative-for-tiktok.md), [Spark and creators](references/spark-ads-and-creators.md), [Benchmarks](references/benchmarks.md) | Creative report + briefs |
| Creator or Spark Ads program | [Spark and creators](references/spark-ads-and-creators.md), [Policy](references/policy-and-account-health.md) | Creator program plan |
| Lead gen setup or quality fix | [Lead gen](references/lead-gen.md), [Measurement](references/measurement-events-api-attribution.md) | Lead gen plan + CRM event spec |
| App campaigns | [Account structure](references/account-structure-and-campaign-types.md), [Measurement](references/measurement-events-api-attribution.md), [Playbooks](references/scaling-playbooks.md) | App launch plan |
| Audience strategy | [Audiences](references/audiences-and-targeting.md) | Audience plan + test rows |
| Scaling plan | [Playbooks](references/scaling-playbooks.md), [Bidding](references/bidding-and-budgets.md), [Creative](references/creative-for-tiktok.md) | Scale plan + change list |
| Ad rejection, suspension, policy question | [Policy](references/policy-and-account-health.md), [Playbooks](references/scaling-playbooks.md) | Recovery plan + appeal draft |
| Attribution and triangulation | [Measurement](references/measurement-events-api-attribution.md), [Bidding](references/bidding-and-budgets.md) | Calibration memo |
| Search on TikTok | [Account structure](references/account-structure-and-campaign-types.md) | Search plan with keyword list |
| Reporting setup, API or MCP | [Tools, API and MCP](references/tools-api-mcp.md) | Reporting spec |
| Benchmarks and targets | [Benchmarks](references/benchmarks.md), [Bidding](references/bidding-and-budgets.md) | Baseline table |
| Weekly or monthly report | [Optimization](references/optimization-and-diagnostics.md), [Benchmarks](references/benchmarks.md) | Weekly report |

## The laws

1. Measurement before money: no scaling until Pixel + Events API with event_id dedup pass the health checks (bad signal poisons every bid).
2. Creative is the targeting: on TikTok, new concepts move results more than any audience or bid setting.
3. Native or nothing: 9:16, sound on, a person in the first second, hook in 3 seconds (polished repurposed ads read as interruptions).
4. Feed the learning phase: each conversion ad group needs a daily budget of at least 10x target CPA and a path to about 50 conversions in 7 days (starved ad groups never stabilize).
5. Consolidate before you fragment: fewer ad groups with more signal beat many small ones (learning is per ad group).
6. Hands off for 7 days after launch or major change (TikTok's own Smart+ guidance; edits reset learning).
7. Change in steps: bids up to 15% every 2 days after day 7; manual budgets 20% to 30% per 48 to 72 hours; Smart+ Lead Gen up to 50% per day (big jumps destabilize delivery).
8. Caps follow evidence: Cost Cap and Minimum ROAS start from trailing actuals, never from aspirations (tight caps cause non-delivery).
9. Calibrate before you target: set in-platform targets from incrementality or triangulation, not raw 7-day click + 1-day view numbers (TikTok over-credits in platform and is under-credited in last click).
10. Never set targets from 7-day view windows (they inflate ROAS).
11. Off-platform inventory is opt-in by evidence: TikTok Ad Network (Pangle) and other placements run as test cells until backend data proves them (they can absorb budget silently, especially in Smart+).
12. Shop runs on GMV Max: set Target ROI from a breakeven ROI that includes referral fees, affiliate commissions, coupons, shipping and returns (otherwise ROI hides losses).
13. Edit GMV Max in one daily window and do not pause it to save money (pauses and big edits forfeit ROI protection and reset delivery).
14. Creators are infrastructure: at Growth tier and above, keep a roster, Spark codes tracked with expiry, and contracts covering usage, edits and AI rights.
15. Refresh before fatigue: ship new ads on the tier cadence; flag ads when CTR falls 20% and 6s view rate falls 15% vs their first week.
16. Judge lead gen on qualified pipeline, not CPL (cheap TikTok leads are often unqualified).
17. Broad by default, constrained by law: use automatic or broad targeting and enforce only legal or business guardrails (narrow targeting raises CPM).
18. Search is a separate intent layer: isolate brand and product terms in a Search Ads Campaign; Automatic Search Placement cannot be keyword-controlled.
19. AI creative is for variation, not deception: label AI content, never fake testimonials or likenesses (policy and trust).
20. One protected account: brand owns the Business Center, 2-step verification for all users, no reuse of assets tied to suspended accounts.
21. Every live change needs human approval, logged with a timestamp (clean attribution of cause and effect).

## What top operators do differently

| Average operator | Top 1% operator |
|------------------|-----------------|
| Treats TikTok as a media buying problem | Treats it as a creative and creator supply problem; budgets follow creative throughput |
| Repurposes Meta or TV ads | Briefs TikTok-first concepts with creators; uses AI only for variations and localization |
| Reads Ads Manager ROAS as truth | Holds a calibrated range (last click, survey, platform, lift) and sets in-platform targets from it |
| Many ad groups by interest | One or two broad ad groups per objective, a separate testing lane, Smart+ for scaling |
| Edits daily | Batches changes, respects 7-day learning, keeps a timestamped change log |
| Runs GMV Max with a guessed ROI | Computes breakeven ROI with every Shop cost, edits once a day, protects ROI protection eligibility |
| Ignores comments | Moderates Spark Ad comments, answers objections with video replies that become new ads |
| Leaves placements on default | Tests TikTok Ad Network, Lemon8 and search as explicit cells |
| Waits for fatigue | Ships new concepts on a cadence and kills losers fast with pre-set rules |
| Lets agencies own assets | Brand owns the Business Center, pixel, catalog, identities and creator contracts |

## Expensive mistakes to prevent

1. Starving ad groups: Purchase optimization at $30 per day with a $40 CPA. It never exits learning.
2. Duplicate pixel and Events API purchases without a shared event_id, then scaling on doubled ROAS.
3. Setting Minimum ROAS or Cost Cap from 7-day view numbers, causing non-delivery or overspend.
4. Leaving off-platform inventory on in Smart+ for lead gen and getting junk leads.
5. Raising GMV Max Target ROI sharply after one bad day, which stalls delivery for a week.
6. Pausing GMV Max on weak days and losing ROI protection and momentum.
7. Ignoring affiliate commission and coupon costs in Shop ROI targets.
8. Running Spark Ads past code expiry and losing a top ad mid-flight.
9. Unlicensed music or unsupported claims triggering repeated rejections and account risk.
10. Creating new accounts or payment methods to escape a suspension, extending the ban to new assets.
11. Judging creatives on 1 to 2 days of data inside learning.
12. Reporting CPL to the business while sales rejects most TikTok leads.

## Worked example: first 30 days for a Growth tier Shopify brand

Inputs (from PROJECT_BRIEF): AOV $70, contribution margin 45% ($31.50), budget $15k per month, Pixel only, no Events API.
1. Week 0: block launch; request measurement handoff for Events API with event_id dedup (Shopify TikTok app highest data sharing level or server-side GTM). Breakeven CPA $31.50; target first-order CPA $25 (20% margin buffer).
2. Week 1: one manual Sales campaign, broad, Maximum Delivery, 7-day click + 1-day view, TikTok placements only, $250 per day (10x target CPA), 6 ads from 3 concepts.
3. Week 2: kill 2 ads per the kill rules; add 4 new ads (hooks on the leading concept, 1 new concept). Weekly report with platform and GA4 numbers.
4. Week 3: 70 purchases per week reached; launch Smart+ Web at $300 per day with the 4 best ads plus 4 new ones; keep manual testing at $100 per day.
5. Week 4: post-purchase survey live; compute calibration; propose Cost Cap at trailing CPA if volume is stable; plan creator roster of 3 creators for month 2.

## Diagnostics (summary; full table in Optimization)

| Symptom | Likely causes | Checks | Fixes |
|---------|--------------|--------|-------|
| Not spending | Rejection, tight caps, small audience, low budget, payment | Status, bid vs trailing, audience size, billing | Fix, loosen cap 15% to 20%, broaden, raise to 10x CPA |
| CPA creeping up over weeks | Creative fatigue | CTR and 6s rate vs first 7 days, ad age | New concepts and hooks |
| Sudden CPA spike | Recent edit, tracking break, external event | Change log, event counts, site status | Revert, measurement handoff, wait out if external |
| Platform up, backend flat | Duplicate events, view-through inflation | Dedup, click-only columns | Fix dedup, align windows |
| Learning limited | Too few conversions per ad group | Conversions per 7 days per ad group | Consolidate, shallower event, budget |
| Smart+ spends on 1 asset | Exploitation of a winner | Creative report by material ID | Add concepts as asset groups; test lane |
| GMV Max not spending | Target ROI too high, low creative supply | Target vs trailing ROI, queue count | Lower target 10% to 15%, add videos |
| Poor lead quality | Easy form, off-platform placements | CRM join by ad and placement | Qualifying questions, exclusions, CRM events |
| Ads rejected | Claims, music, landing page | Rejection reason | Fix and resubmit or appeal |
| Account suspended | Policy, payment, linked assets | Account status page | Recovery play 7.2 |

## Cadence

| When | Checks | Time |
|------|--------|------|
| Daily (Growth tier and above) | Spend pacing, zero-conversion alerts, disapprovals, account status, GMV Max daily ROI, budget-capped winners | 5 minutes |
| Weekly | Measurement health, KPI vs calibrated target, creative kill/keep/scale, fatigue list, budget proposals, experiments, creative requests, weekly report | 45 to 90 minutes |
| Monthly | Triangulation refresh (platform vs GA4 vs survey vs MER), creator roster ranking, Spark code expiries, audience refresh, policy changes, Freshness Protocol, baseline update | Half day |
| Quarterly | Full audit (scored), lift test plan, structure review, Smart+ vs manual re-test, seasonality plan, memory review | 1 day |

At Starter tier, run the weekly check every 2 weeks and skip daily checks except spend and rejections.

## Guardrails and approvals

Never without explicit human approval: launch, pause, delete, change budgets or bids, change targeting or placements, change GMV Max ROI targets, submit appeals, authorize Spark codes, create automated rules, upload customer lists, enable betas, publish creative.

Approval workflow:
1. Draft a change list (template in [Playbooks](references/scaling-playbooks.md) section 9) with reason, data, expected impact, risk and rollback trigger.
2. Present it. Wait for "approved" per row or for the whole list.
3. If MCP or API write access exists and the human approves, execute only the approved rows, read back each change, and log it.
4. Otherwise, give the human exact UI steps.

Hard stops: measurement broken; account under review or suspended; any request to evade a ban (new accounts, new payment methods, cloaking); claims without substantiation; content using a person's likeness without license; targeting minors with restricted products.

Data rules: never fabricate data; label platform numbers as such; state date ranges; never store tokens or raw PII in `ads-master/`.

## Outputs

Path: `ads-master/outputs/tiktok-ads/YYYY-MM-DD_tiktok-ads_<description>.md`. Never overwrite; create a new dated file.

| Output | Required sections |
|--------|------------------|
| Audit | Header (data, range, attribution), score and grade, top 5 fixes, findings by section, quick wins, 30-day plan, handoffs requested, data gaps |
| Launch plan | Objective and KPI, unit economics and targets, structure, budgets and bids, creative plan, measurement gate, timeline, change list, risks |
| Weekly report | KPI table (platform and calibrated), what changed and why, creative ranking and fatigue list, experiments, proposed changes, next week focus |
| Diagnosis | Symptom, decomposition (CPM, CTR, CVR, AOV), root cause with evidence, fixes ranked, change list |
| Creative report and briefs | Ranking by concept, hook and creator, fatigue list, winners to iterate, briefs |
| GMV Max review | Template in TikTok Shop module section 10 |
| Change list | Template in Playbooks section 9 |

Journal: `ads-master/journal/YYYY-MM-DD_HHMM_tiktok-ads_<topic>.md` for decisions, alerts, handoff requests and platform changes found in freshness checks.

## Freshness protocol

Before acting on any feature, setting, policy or benchmark, check these sources and compare with this skill's "Knowledge as of" date.

| Source | URL | What to verify |
|--------|-----|----------------|
| TikTok Business Help Center | ads.tiktok.com/help | "Last updated" dates on: budgets, learning phase, bidding, Smart+ upgraded experience, Smart+ best practices, attribution windows, EVTA, event deduplication, Search Ads, Automatic Search Placement, GMV Max, ROI protection |
| TikTok for Business blog | ads.tiktok.com/business/en/blog | Quarterly Product Preview, new formats, Smart+ and GMV Max posts |
| TikTok Newsroom | newsroom.tiktok.com | Event announcements (NewFronts March, TikTok World May, Cannes June, Q3 preview July, Advertising Week October) |
| TikTok API for Business docs and changelog | business-api.tiktok.com/portal/docs | API version, endpoint and metric changes, MCP server docs |
| TikTok Advertising Policies | ads.tiktok.com/help (policy section) | Category rules for the project's market |
| TikTok Shop Seller Center and Academy | seller-[market].tiktok.com | Shop fees, GMV Max changes, Shop policies |
| Creative Center | ads.tiktok.com/business/creativecenter | Top Ads, trends, music library changes |
| Trade press for early signals | ppc.land, socialmediatoday.com, mediapost.com, marketingdive.com | New rollouts; confirm against official pages |

Procedure:
1. Check the official pages that relate to the task (5 to 15 minutes).
2. If something differs from this skill, note it in the output and write a journal entry tagged `change` with the source URL and date.
3. Propose an update to this skill's references through the journal; do not edit global knowledge from a project.
4. If the live account UI differs from documentation, the UI wins for that account; record it in `memory/tiktok-ads.md` under account facts.

Known items to re-verify first (2026-10): exact learning phase threshold; attribution window options; Smart+ asset group limits; TikTok Ad Network auto-inclusion and opt-out in Smart+; GMV Max Pro and cost-aware optimization availability; Buy Direct and Agentic Leads availability; US JV effects on commercial operations; custom audience minimums and retention windows.

## Reference index

- [Account structure and campaign types](references/account-structure-and-campaign-types.md): hierarchy, objectives, Smart+ vs manual, blueprints by tier, search, brand formats, app, placements, naming.
- [Bidding and budgets](references/bidding-and-budgets.md): minimums, sizing formulas, bid strategies, change limits, CBO vs ABO, dayparting, learning phase, unit economics.
- [Audiences and targeting](references/audiences-and-targeting.md): broad default, targeting menu, custom and lookalike audiences, retargeting limits, regulatory limits, tests.
- [Creative for TikTok](references/creative-for-tiktok.md): native rules, hooks, structures, metrics, testing system, fatigue and refresh, Symphony AI, briefs, QA.
- [Spark Ads and creators](references/spark-ads-and-creators.md): Spark mechanics, authorization, TikTok One, sourcing, contracts, disclosure, affiliates.
- [TikTok Shop and GMV Max](references/tiktok-shop-and-gmv-max.md): timeline, mechanics, breakeven ROI, setup, LIVE, ROI protection, metrics, diagnostics.
- [Lead gen](references/lead-gen.md): destinations, form design, CRM loop, quality diagnostics, structure by tier.
- [Measurement, Events API and attribution](references/measurement-events-api-attribution.md): signal stack, events, dedup, EMQ, windows, UTMs, triangulation, lift tests.
- [Optimization and diagnostics](references/optimization-and-diagnostics.md): performance equation, diagnostic order, symptom playbook, weekly loop, data pulls.
- [Playbooks: launch, optimize, scale, recover](references/scaling-playbooks.md): launch plays, scaling steps, Q4, recovery plays, change list.
- [Policy and account health](references/policy-and-account-health.md): category map, rejections, AIGC, appeals, account health, regulation and US JV.
- [Tools, API and MCP](references/tools-api-mcp.md): official MCP server, Marketing API, connectors, community servers, reporting stacks.
- [Benchmarks](references/benchmarks.md): verified figures, official thresholds, where to get vertical benchmarks, baseline method.
- [Audit checklist](references/audit-checklist.md): scored audit with rubric.
- [Sources](references/sources.md): annotated source list.
