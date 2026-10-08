# Routing and Multi Agent Workflows

How the main session conducts the Ads Master team. Every workflow is written as a delegation plan: step, agent slug, parallel or sequential, inputs, expected output path, and what each step passes to the next.

## 1. Architecture you must respect

| Fact | Consequence |
|------|-------------|
| In Claude Code a subagent cannot spawn other subagents | Only the main session delegates. Specialists, including the growth-orchestrator subagent, return "Handoffs requested" or a "Delegation plan" |
| Subagents start with a fresh context | Every brief must name the files to read and the output path. Never assume a specialist "knows" what another said |
| Specialists share state only through `ads-master/` | Outputs go to `ads-master/outputs/<slug>/`, events to `ads-master/journal/`. The next wave reads those files |
| Parallel delegation is possible from the main session | Put independent steps in the same wave and send them in one message |
| Long workflows can exceed one session | Write the delegation plan to `ads-master/outputs/growth-orchestrator/` first, so a later session can resume at the right wave |

### 1.1 Conductor loop (main session)
1. Load the `growth-orchestrator` skill. Read project state (see SKILL.md Operating protocol step 1).
2. Pick the workflow from section 4, or write a custom plan with the same table format.
3. Save the plan: `ads-master/outputs/growth-orchestrator/YYYY-MM-DD_growth-orchestrator_delegation-plan-<workflow>.md`.
4. Run wave 1. For each step send the Delegation brief template (SKILL.md). Wait for all outputs.
5. Check the gate condition. If it fails, stop and report; do not run later waves on bad data.
6. Run the remaining waves. Execute blocking handoffs between waves.
7. Synthesize: delegate to the growth-orchestrator subagent with "Synthesize the outputs listed below into <deliverable>" and the list of output paths, or do it in the main session following this skill.
8. Present the consolidated change list to the human. Nothing executes until approved.
9. Journal entry: what ran, outputs, decisions pending.

### 1.2 Wave sizing
| Situation | Max parallel delegations per wave | Why |
|-----------|-----------------------------------|-----|
| Normal | 4 to 6 | Keeps synthesis tractable and context small |
| Full audit with many active agents | Split into two waves of channel agents | Avoid overloading synthesis |
| Daily alerts | All active paid agents | Outputs are short exception lists |

### 1.3 Payload standards (what every step passes on)
| From | To | Payload (must be in the output file) |
|------|----|--------------------------------------|
| measurement | everyone | Verdict per conversion (verified, amber with known error %, broken), date range affected, which platform numbers to distrust, reconciliation factor platform vs backend |
| channel agents | growth-orchestrator | Spend, primary KPI vs target, marginal CPA or ROAS estimate at +20% budget, headroom signal (impression share lost to budget, audience saturation, frequency), change list, creative needs |
| market-intel | creative-strategy, channel agents, seo, ai-search-optimization | Competitor offers, angles, price moves, keyword and AI visibility gaps, VoC phrases |
| creative-strategy | channel agents | Concept slate with IDs, briefs, test plan, naming convention |
| cro | channel agents, growth-orchestrator | Page CVR by source, test plan, expected CVR lift, pages ready for traffic |
| seo, ai-search-optimization | growth-orchestrator, chatgpt-ads | Organic and AI visibility trend, at risk revenue, quick wins, prompts where competitors win |
| commerce-feeds | google-ads, meta-ads, tiktok-ads, microsoft-ads, chatgpt-ads | Feed health, disapprovals, margin custom labels, products ready |
| growth-orchestrator | main session, human | Budget plan, priorities, forecast, delegation plan for next wave |

## 2. Routing detail

### 2.1 Route by intent
| Request pattern | Primary agent | Also involve | Workflow |
|-----------------|---------------|--------------|----------|
| "Audit our marketing" or "where are we wasting money" | growth-orchestrator (conductor) | all active | Full growth audit (4.1) |
| "Audit our Meta account" | meta-ads | measurement if data doubts | single agent |
| "Launch in Germany" or "expand to the UK" | growth-orchestrator | market-intel, measurement, channel agents, seo | New market launch (4.2) |
| "We are launching a new product" | growth-orchestrator | market-intel, commerce-feeds, creative-strategy, cro, channels | New product launch (4.3) |
| "Can we double spend" or "scale to $X" | growth-orchestrator | measurement, channel agents, creative-strategy | Scaling plan (4.4) |
| "Sales dropped", "CPA doubled", "ROAS crashed" | measurement then channel | cro, creative-strategy, market-intel | Recovery (4.5) |
| "Conversions are zero", "pixel broken", "numbers do not match" | measurement | affected channel agents | Tracking break (4.6) |
| "We are invisible in ChatGPT" or "AI Overviews took our traffic" | ai-search-optimization | seo, market-intel, chatgpt-ads, commerce-feeds | AI search program (4.7) |
| "Plan Black Friday", "Ramadan", "back to school" | growth-orchestrator | all active | Seasonal plan (4.8) |
| "Weekly review", "how did we do" | ads-review skill | all active | 4.9 |
| "Monthly report", "reallocate budget" | ads-review skill (monthly) | all active | 4.10 |
| "Next quarter plan" | growth-orchestrator | all active | 4.11 |
| "New client", "set this up" | ads-setup skill | growth-orchestrator, measurement | Onboarding (4.12) |
| "Should we try Reddit or Pinterest or CTV" | growth-orchestrator (strategist) | measurement, creative-strategy | other-channels-quick-guides.md |
| "What is our breakeven ROAS" | growth-orchestrator (strategist) | none | unit-economics module |

### 2.2 Disambiguation rules
1. A drop in results is a measurement question until proven otherwise. Check tracking before tactics.
2. A single platform question goes straight to that agent. Do not run a workflow for "why is this ad set in learning limited".
3. Paid vs organic AI: ads inside assistants go to chatgpt-ads; being mentioned or cited organically goes to ai-search-optimization.
4. Landing page vs ad: if CTR is healthy and CVR is weak, cro; if CTR and hook rate are weak, creative-strategy.
5. Feed problems that look like channel problems (Shopping or PMax volume collapse, catalog ads disapproved) go to commerce-feeds first.
6. If the request names money ("budget", "spend", "ROAS target"), the orchestrator decides allocation even when a channel agent does the analysis.

## 3. The specialist roster at a glance
| Slug | Typical output file | Cadence when active |
|------|---------------------|---------------------|
| measurement | `<date>_measurement_health-check.md`, `_tracking-plan.md`, `_lift-test-design.md` | weekly health, monthly reconciliation |
| meta-ads | `_audit.md`, `_launch-plan.md`, `_weekly-review.md` | daily alerts, weekly |
| google-ads | `_audit.md`, `_search-terms-review.md`, `_weekly-review.md` | daily alerts, weekly |
| microsoft-ads | `_audit.md`, `_import-plan.md` | weekly |
| chatgpt-ads | `_test-plan.md`, `_weekly-review.md` | weekly |
| tiktok-ads | `_audit.md`, `_launch-plan.md` | daily alerts, weekly |
| linkedin-ads | `_audit.md`, `_abm-plan.md` | weekly |
| seo | `_audit.md`, `_content-plan.md`, `_monthly-report.md` | weekly, monthly |
| ai-search-optimization | `_visibility-baseline.md`, `_monthly-report.md` | monthly |
| commerce-feeds | `_feed-audit.md` | weekly diagnostics |
| cro | `_page-audit.md`, `_test-plan.md` | weekly |
| creative-strategy | `_concept-slate.md`, `_creative-analysis.md` | weekly |
| market-intel | `_competitive-baseline.md`, `_monthly-movement.md` | monthly, quarterly |
| mobile-app-growth | `_aso-audit.md`, `_app-growth-plan.md`, `_skan-schema.md` | daily alerts, weekly |
| site-engineer | `_release-qa.md`, `_launch-qa.md`, `_worst-case-test.md` | on every release |
| video-studio | `_production-plan.md`, `_render-batch.md` | weekly batch |
| offer-strategy | `_offer-architecture.md`, `_promo-calendar.md` | monthly |
| lifecycle-crm | `_lifecycle-audit.md`, `_flow-specs.md`, `_cohort-report.md` | weekly |
| compliance | `_claims-review.md`, `_policy-check.md` | on every publish |

## 4. Workflows as delegation plans
Date placeholders: `<d>` = today's date YYYY-MM-DD. All paths are under `ads-master/outputs/`.

### 4.1 Full growth audit
Trigger: new client, plateau, "audit everything", quarterly reset. Time box: 1 to 2 sessions.
Gate: measurement verdict is verified or amber with a known error percentage.

| Step | Wave | Agent | Mode | Inputs | Output | Passes to |
|------|------|-------|------|--------|--------|-----------|
| 1 | 1 | measurement | sequential (gate) | MEASUREMENT.md, GA4 and backend exports 90d, platform conversion exports | `measurement/<d>_measurement_health-check.md` | Conversion verdicts, reconciliation factors |
| 2 | 2 | each active paid agent (meta-ads, google-ads, microsoft-ads, tiktok-ads, linkedin-ads, chatgpt-ads) | parallel | Platform exports 90d, step 1 verdict | `<slug>/<d>_<slug>_audit.md` | Score, top 5 issues, marginal CPA at +20%, headroom |
| 3 | 2 | seo | parallel | GSC 16 months, crawl | `seo/<d>_seo_audit.md` | Organic trend, at risk revenue |
| 4 | 2 | ai-search-optimization | parallel | Prompt list, AI referral data | `ai-search-optimization/<d>_ai-search-optimization_visibility-baseline.md` | AI share of voice vs competitors |
| 5 | 2 | cro | parallel | GA4 funnel 90d, top landing pages | `cro/<d>_cro_page-audit.md` | CVR gaps by source and page |
| 6 | 2 | commerce-feeds (if catalog) | parallel | Merchant Center diagnostics, feed | `commerce-feeds/<d>_commerce-feeds_feed-audit.md` | Feed issues blocking Shopping or catalogs |
| 7 | 2 | market-intel | parallel | COMPETITORS.md, ad libraries | `market-intel/<d>_market-intel_competitive-baseline.md` | Offers, angles, gaps |
| 8 | 3 | creative-strategy | sequential | Outputs 2, 5, 7 | `creative-strategy/<d>_creative-strategy_creative-audit.md` | Concept gaps, volume plan |
| 9 | 4 | growth-orchestrator | sequential (synthesis) | All outputs above | `growth-orchestrator/<d>_growth-orchestrator_growth-audit.md` | Scored audit, budget plan, 90 day roadmap, PRIORITIES draft |

Synthesis must contain: system score (audit-checklist.md), binding constraint, unit economics, channel scorecard, top 10 issues ranked by contribution margin impact, budget reallocation proposal, 90 day roadmap in three 30 day blocks, consolidated change list, experiments to add.

### 4.2 New market launch
Trigger: new country or language. Time box: plan in 1 session, launch over 2 to 6 weeks.
Gate: legal and tax checklist for the market completed (geo-market-modules.md) and consent setup confirmed by measurement.

| Step | Wave | Agent | Mode | Inputs | Output | Passes to |
|------|------|-------|------|--------|--------|-----------|
| 1 | 1 | market-intel | parallel | Target market, category, COMPETITORS.md | `market-intel/<d>_market-intel_market-entry-<geo>.md` | Market size, local competitors, price levels, demand by channel, local platforms |
| 2 | 1 | measurement | parallel | Geo privacy regime, current stack | `measurement/<d>_measurement_geo-tracking-plan-<geo>.md` | Consent mode, CMP config, currency and conversion values, server-side needs |
| 3 | 1 | growth-orchestrator | parallel (strategist) | PROJECT_BRIEF, geo module | `growth-orchestrator/<d>_growth-orchestrator_geo-economics-<geo>.md` | Local unit economics incl. taxes on ad spend, FX, breakeven ROAS, channel shortlist and budget |
| 4 | 2 | channel agents in the shortlist | parallel | Outputs 1 to 3 | `<slug>/<d>_<slug>_launch-plan-<geo>.md` | Structure, budget, targets, creative needs |
| 5 | 2 | seo | parallel | Output 1, site architecture | `seo/<d>_seo_international-plan-<geo>.md` | hreflang, local content, ccTLD or subfolder |
| 6 | 2 | commerce-feeds (if catalog) | parallel | Output 2, feed | `commerce-feeds/<d>_commerce-feeds_geo-feed-plan-<geo>.md` | Currency, language, shipping and tax in feed |
| 7 | 3 | creative-strategy | parallel | Outputs 1, 4 | `creative-strategy/<d>_creative-strategy_localization-brief-<geo>.md` | Localized concepts, not translations |
| 8 | 3 | cro | parallel | Outputs 1, 2 | `cro/<d>_cro_localized-pages-<geo>.md` | Local payment methods, trust signals, pages |
| 9 | 4 | growth-orchestrator | sequential | All | `growth-orchestrator/<d>_growth-orchestrator_launch-plan-<geo>.md` | Launch calendar, budget ramp, forecast, success criteria at weeks 4, 8, 12 |

### 4.3 New product launch
Gate: price, margin and positioning confirmed by the human.

| Step | Wave | Agent | Mode | Inputs | Output | Passes to |
|------|------|-------|------|--------|--------|-----------|
| 1 | 1 | market-intel | parallel | Product spec, competitors | `market-intel/<d>_market-intel_launch-intel-<product>.md` | Positioning map, price corridor, competitor claims, demand signals |
| 2 | 1 | growth-orchestrator | parallel (strategist) | Product unit economics | `growth-orchestrator/<d>_growth-orchestrator_product-economics-<product>.md` | Breakeven ROAS, launch CAC tolerance, budget |
| 3 | 1 | commerce-feeds (if catalog) | parallel | Product data | `commerce-feeds/<d>_commerce-feeds_launch-feed-<product>.md` | Feed ready, labels |
| 4 | 2 | creative-strategy | parallel | Outputs 1, 2 | `creative-strategy/<d>_creative-strategy_launch-concepts-<product>.md` | 5 to 10 concepts across awareness levels |
| 5 | 2 | cro | parallel | Output 1 | `cro/<d>_cro_launch-page-<product>.md` | Page plan, test plan |
| 6 | 3 | channel agents | parallel | Outputs 2 to 5 | `<slug>/<d>_<slug>_launch-plan-<product>.md` | Campaigns, budget, KPI |
| 7 | 3 | seo, ai-search-optimization | parallel | Output 1 | `<slug>/<d>_<slug>_launch-plan-<product>.md` | Product pages, comparison content, AI visibility seeding |
| 8 | 4 | growth-orchestrator | sequential | All | `growth-orchestrator/<d>_growth-orchestrator_launch-plan-<product>.md` | Calendar, test gates, forecast |

### 4.4 Scaling plan
Trigger: unit economics healthy and the human wants more volume. Gate: incrementality evidence or at least a reconciled MER trend from measurement.

| Step | Wave | Agent | Mode | Inputs | Output | Passes to |
|------|------|-------|------|--------|--------|-----------|
| 1 | 1 | measurement | sequential (gate) | Lift tests, MMM, MER trend | `measurement/<d>_measurement_incrementality-status.md` | Incrementality factors by channel, confidence |
| 2 | 2 | channel agents | parallel | Step 1, 90d exports | `<slug>/<d>_<slug>_headroom.md` | Marginal CPA at +20%, +50%; impression share lost to budget; frequency; audience size |
| 3 | 2 | growth-orchestrator | parallel (strategist) | PROJECT_BRIEF unit economics, cash constraints | `growth-orchestrator/<d>_growth-orchestrator_scale-economics.md` | Max acceptable marginal CPA, payback limits |
| 4 | 3 | creative-strategy | sequential | Step 2 | `creative-strategy/<d>_creative-strategy_scale-volume-plan.md` | Concepts per week needed at new spend |
| 5 | 3 | cro, commerce-feeds | parallel | Step 2 | `<slug>/<d>_<slug>_scale-readiness.md` | Page and feed capacity |
| 6 | 4 | growth-orchestrator | sequential | All | `growth-orchestrator/<d>_growth-orchestrator_scaling-plan.md` | Budget step schedule (+20% per step, 7 to 14 day holds), stop rules, forecast |

Stop rule template: stop stepping a channel when marginal CPA over the last step exceeds max acceptable marginal CPA for 2 consecutive weeks, or MER falls below target MER.

### 4.5 Recovery from a performance drop
Trigger: CPA or ROAS worse by 25% or more for 7 days on meaningful volume, or revenue down 20% week over week without seasonality explanation.
Gate: measurement confirms the drop is real.

| Step | Wave | Agent | Mode | Inputs | Output | Passes to |
|------|------|-------|------|--------|--------|-----------|
| 1 | 1 | measurement | sequential (gate) | Platform vs backend daily 30d, tag health, consent rates, recent deploys | `measurement/<d>_measurement_drop-check.md` | Real or tracking artifact; date it started |
| 2 | 2 | affected channel agents | parallel | Step 1, change history, auction insights, CPM, CTR, frequency | `<slug>/<d>_<slug>_drop-diagnosis.md` | Root cause candidates with evidence, change list |
| 3 | 2 | cro | parallel | Site CVR by device and source, deploy log, speed | `cro/<d>_cro_drop-diagnosis.md` | Site side causes |
| 4 | 2 | market-intel (if competitor suspected) | parallel | Ad libraries, prices, promos | `market-intel/<d>_market-intel_competitor-check.md` | Competitor promo or entry |
| 5 | 3 | creative-strategy (if fatigue) | sequential | Step 2 | `creative-strategy/<d>_creative-strategy_refresh-plan.md` | Replacement concepts |
| 6 | 4 | growth-orchestrator | sequential | All | `growth-orchestrator/<d>_growth-orchestrator_recovery-plan.md` | Root cause, recovery change list, budget protection (what to cut while fixing), recheck date |

Root cause order to test: tracking, site or checkout, feed or policy, offer or price vs competitors, creative fatigue, auction or seasonality, algorithm reset from recent changes.

### 4.6 Tracking break
Trigger: conversions at zero or down 50% vs the 7 day average, platform vs backend gap jumps, CAPI or tag errors.

| Step | Wave | Agent | Mode | Inputs | Output | Passes to |
|------|------|-------|------|--------|--------|-----------|
| 1 | 1 | measurement | sequential (lead) | Tag diagnostics, server logs, CMP logs, deploy history | `measurement/<d>_measurement_incident.md` | Root cause, fix plan, affected window, data backfill options |
| 2 | 2 | affected channel agents | parallel | Step 1 | `<slug>/<d>_<slug>_tracking-impact.md` | Bidding protection list: campaigns on value or CPA bidding to switch, cap or hold; data exclusion windows (for example Google Ads data exclusions) |
| 3 | 3 | growth-orchestrator | sequential | 1, 2 | `growth-orchestrator/<d>_growth-orchestrator_incident-summary.md` | Business impact, decisions for the human |

Rule: during a confirmed tracking break, recommend no budget increases and no new tests on affected conversions.

### 4.7 AI search program
Trigger: AI referrals growing, organic clicks falling with stable impressions, or AI assistants recommending competitors.

| Step | Wave | Agent | Mode | Inputs | Output | Passes to |
|------|------|-------|------|--------|--------|-----------|
| 1 | 1 | ai-search-optimization | parallel | Priority prompts (from AUDIENCE.md questions), competitors | `ai-search-optimization/<d>_ai-search-optimization_visibility-baseline.md` | Share of voice, citations, sources AI uses |
| 2 | 1 | seo | parallel | GSC, crawl | `seo/<d>_seo_ai-overview-impact.md` | AIO exposure, click loss, technical access for AI crawlers |
| 3 | 1 | market-intel | parallel | Competitors | `market-intel/<d>_market-intel_ai-visibility-benchmark.md` | Who wins which prompts and why |
| 4 | 2 | chatgpt-ads | parallel | Steps 1, 3 | `chatgpt-ads/<d>_chatgpt-ads_test-plan.md` | Paid presence where organic is weak |
| 5 | 2 | commerce-feeds (if catalog) | parallel | Step 1 | `commerce-feeds/<d>_commerce-feeds_ai-shopping-feeds.md` | ChatGPT merchant and agentic commerce readiness |
| 6 | 2 | measurement | parallel | GA4 | `measurement/<d>_measurement_ai-referral-tracking.md` | AI referral channel group, assisted conversions |
| 7 | 3 | growth-orchestrator | sequential | All | `growth-orchestrator/<d>_growth-orchestrator_ai-search-program.md` | 90 day program, KPIs, budget |

### 4.8 BFCM or seasonal plan
Start 8 to 10 weeks before the peak. Gate: tracking verified and feed healthy 4 weeks before the peak.

| Step | Wave | Agent | Mode | Inputs | Output | Passes to |
|------|------|-------|------|--------|--------|-----------|
| 1 | 1 | measurement | parallel | Last season data, current health | `measurement/<d>_measurement_peak-readiness.md` | Tracking freeze date, server capacity, seasonality adjustments (Google Ads) |
| 2 | 1 | commerce-feeds | parallel | Feed, promo plan | `commerce-feeds/<d>_commerce-feeds_peak-feed-plan.md` | Sale price, promotions feed, stock |
| 3 | 1 | market-intel | parallel | Last season competitor promos | `market-intel/<d>_market-intel_peak-promo-intel.md` | Expected discount depth, dates |
| 4 | 2 | growth-orchestrator | sequential (strategist) | Steps 1 to 3, last season | `growth-orchestrator/<d>_growth-orchestrator_peak-budget.md` | Daily budget calendar, MER floor, promo economics |
| 5 | 3 | creative-strategy | parallel | Step 4 | `creative-strategy/<d>_creative-strategy_peak-creative.md` | Teaser, launch, last chance, post peak sets |
| 6 | 3 | channel agents | parallel | Step 4 | `<slug>/<d>_<slug>_peak-plan.md` | Budget ramps, bid targets, audience lists (email capture before peak) |
| 7 | 3 | cro | parallel | Step 4 | `cro/<d>_cro_peak-pages.md` | Promo pages, speed, code freeze |
| 8 | 4 | growth-orchestrator | sequential | All | `growth-orchestrator/<d>_growth-orchestrator_peak-plan.md` | Calendar, pacing table, daily war room checklist |

Seasonal notes: in MENA run the same plan for Ramadan, Eid and White Friday; in Turkey for 11.11 and Efsane Cuma or Black Friday campaigns of marketplaces; in the US and EU for BFCM and Q4 gifting.

### 4.9 Weekly review (ads-review weekly mode)
| Step | Wave | Agent | Mode | Output |
|------|------|-------|------|--------|
| 1 | 1 | every active specialist | parallel | `<slug>/<d>_<slug>_weekly-review.md` |
| 2 | 2 | handoffs that block synthesis (usually measurement) | sequential | per agent |
| 3 | 3 | growth-orchestrator | sequential | `growth-orchestrator/<d>_growth-orchestrator_weekly-review.md` + PRIORITIES.md |

### 4.10 Monthly review
Weekly flow plus: every agent runs its Freshness Protocol; growth-orchestrator produces budget reallocation on marginal returns, unit economics update and next month forecast (`_monthly-review.md`, MONTHLY_REVIEW.md template); market-intel monthly movement; measurement reconciliation.

### 4.11 Quarterly strategy reset
| Step | Wave | Agent | Mode | Output |
|------|------|-------|------|--------|
| 1 | 1 | all active agents | parallel | full audit using their audit-checklist.md |
| 2 | 1 | market-intel | parallel | landscape refresh |
| 3 | 1 | measurement | parallel | incrementality and MMM plan for the quarter |
| 4 | 2 | growth-orchestrator | sequential | `growth-orchestrator/<d>_growth-orchestrator_strategy-draft-<YYYY-QN>.md` (draft STRATEGY.md for approval), HEARTBEAT.md update |

### 4.12 New client onboarding
1. Main session runs `ads-setup` (creates and fills `ads-master/`).
2. Wave 1: measurement health check (gate) and growth-orchestrator diagnosis in parallel.
3. Wave 2: Full growth audit (4.1) at reduced depth: top 5 issues per agent.
4. Synthesis: first STRATEGY.md draft, HEARTBEAT.md activation, PRIORITIES.md for week 1.

### 4.13 Launch readiness (first paid launch)
Gate order matters: nothing goes live before tracking, site, offer and claims are green.
| Step | Wave | Agent | Mode | Inputs | Brief | Output | Passes to |
|------|------|-------|------|--------|-------|--------|-----------|
| 1 | 1 | measurement | parallel | MEASUREMENT.md, test orders | Verify purchase or lead events end to end, dedup, consent | `measurement/<d>_measurement_launch-tracking.md` | Event verdict |
| 2 | 1 | site-engineer | parallel | repo or theme, product pages | Purchase path, mobile, speed, worst case data, release state | `site-engineer/<d>_site-engineer_launch-qa.md` | Site verdict |
| 3 | 1 | offer-strategy | parallel | PROJECT_BRIEF unit economics, prices | Offer and bundle for launch with acquisition investment math | `offer-strategy/<d>_offer-strategy_launch-offer.md` | Offer spec |
| 4 | 1 | compliance | parallel | PRODUCT_FACTS, CLAIMS, current copy | Clean claims on site and in planned ads | `compliance/<d>_compliance_claims-review.md` | Approved claims |
| 5 | 2 | creative-strategy | sequential | steps 3 and 4 | 3 to 4 distinct concepts and briefs within budget tier | `creative-strategy/<d>_creative-strategy_launch-briefs.md` | Briefs |
| 6 | 3 | video-studio | sequential | step 5 | Produce, QA and name the assets | `video-studio/<d>_video-studio_launch-batch.md` | Asset list with IDs |
| 7 | 4 | channel agent | sequential | steps 1 to 6 | Draft the campaign as PAUSED (stage 2+) or as a change request (stage 1) | `<channel>/<d>_<channel>_launch-plan.md` | Change request |
| 8 | 5 | site-engineer | sequential | step 7 | Launch QA: URLs, UTMs, pixel firing, status PAUSED, budget within cap | `site-engineer/<d>_site-engineer_ad-launch-qa.md` | Go or no go |
Synthesis: go live checklist and one change request for the human.

### 4.14 Creative production sprint
1. creative-strategy: concept slate and briefs from the latest creative analysis and VoC.
2. video-studio and compliance in parallel: produce assets; claims and disclosure review on scripts and final cuts.
3. Channel agents: upload plan (PAUSED) and test design; registry rows in `ads-master/creative-library/registry.csv`.

### 4.15 Retention program
1. lifecycle-crm and measurement in parallel: lifecycle audit and cohort repeat rates (30, 45, 60, 90 days).
2. offer-strategy and compliance: replenishment and winback offers; consent and claims check.
3. cro: post purchase and reorder pages. Synthesis: flow specs and a 90 day retention plan.

### 4.16 Offer test
1. offer-strategy and measurement: hypothesis, economics (acquisition investment per new customer), sample size or duration.
2. cro and compliance: page variant and price display rules (prior price rule for reductions).
3. Channel agents and creative-strategy: message alignment in ads. Synthesis: experiment brief in EXPERIMENTS.md.

### 4.17 App growth program
1. mobile-app-growth and measurement: ASO audit, MMP and SKAN or AdAttributionKit setup, unit economics by cohort.
2. creative-strategy and video-studio: app ad concepts and store screenshots and previews.
3. lifecycle-crm: onboarding, push and win back. Synthesis: app growth plan with budget by network.

## 5. Adding a new agent for a channel without one
Use when a channel in other-channels-quick-guides.md gets a recurring budget above about 10% of paid media or more than $5k per month.
1. Copy the closest package (Reddit, Pinterest, Snapchat or X: copy meta-ads; Amazon or retail media: copy google-ads Shopping parts plus commerce-feeds; CTV or programmatic: copy google-ads YouTube parts).
2. Rename the slug in four places: `agents/<slug>.md`, `skills/<slug>/`, skill `name`, `research/<slug>.md`.
3. Rewrite mission, KPIs, intake, adaptation matrix and task router first, then references (audit-checklist.md and sources.md are mandatory).
4. Add it to the routing table in this skill's SKILL.md, to `AGENT_REGISTRY.md`, to HEARTBEAT.md in the workspace template, and a memory file `memory/<slug>.md`.
5. Run `python3 scripts/validate.py`.
6. Until the agent exists, the growth-orchestrator handles the channel in the strategist role with the quick guide, and the human executes approved changes.
