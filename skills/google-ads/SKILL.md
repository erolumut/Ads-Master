---
name: google-ads
description: Google Ads playbook for auditing, launching, optimizing, scaling and recovering accounts across Search, AI Max for Search, Performance Max, Demand Gen, YouTube, Shopping, Display, App, Local and ads in AI Overviews and AI Mode. Use for Google Ads audits, account structure, keyword and match type strategy, negative keywords, search terms and n-gram analysis, RSAs and assets, Quality Score, Smart Bidding (tCPA, tROAS, Maximize conversions or value), budgets and pacing, AI Max migration and controls, PMax channel and search term reporting, brand exclusions, conversion goals, enhanced conversions, offline conversion import, Customer Match, new customer acquisition, experiments, Conversion Lift, GAQL queries, Google Ads Scripts, API and MCP connectors, policy disapprovals, suspensions and appeals. Triggers on Google Ads, AdWords, PMax, AI Max, CPC, ROAS on Google, search terms, Merchant Center ads, YouTube ads, Google Ads export or account ID.
---

# Google Ads

> Knowledge as of 2026-10. Platforms change monthly. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark. Items labeled [Unverified] or [Contested] must be confirmed in the account or in Google's documentation before they drive a decision.

## Mission and scope

Run Google Ads at a top 1% level for any business model: every euro or dollar goes to the auctions, queries, products and audiences with the best marginal return against the business's real unit economics, measured on conversions the business can verify.

In scope (google-ads owns):
- Search (keywords, match types, negatives, RSAs, assets, Quality Score, brand and competitor campaigns), AI Max for Search, legacy DSA migration.
- Performance Max (all variants), Standard Shopping, AI Max for Shopping (beta), Local inventory ads, store goals, Local Services Ads inside Google Ads.
- Demand Gen (including GDN and Maps channels), YouTube video campaigns, Display migration, App campaigns.
- Ads in AI Overviews and AI Mode (execution: eligibility, campaign setup, reporting proxies).
- Bidding, budgets, pacing, conversion goals and values inside Google Ads, audiences and Customer Match usage, experiments, GAQL, Scripts, API and MCP usage, policy and account health.

Out of scope (hand off):
- Feed content, Merchant Center diagnostics, Merchant API: commerce-feeds.
- Tag implementation, GTM, server-side, consent mode setup, OCI pipelines, MMM builds: measurement.
- Landing pages, forms, checkout: cro. Creative production and briefs: creative-strategy.
- Cross-channel budget and targets: growth-orchestrator. Organic and AI visibility: seo, ai-search-optimization. ChatGPT and other assistant ads: chatgpt-ads. Microsoft Advertising: microsoft-ads.

## Intake (minimum facts)

| Fact | Where to find it | If missing |
|---|---|---|
| Business model, offer, markets, currency, languages | `ads-master/PROJECT_BRIEF.md` sections 1 and 2 | Ask |
| Unit economics: AOV or deal size, contribution margin, LTV, lead to customer rate, target CPA or ROAS, breakeven ROAS | PROJECT_BRIEF.md section 3 | Ask; compute breakeven from margin |
| Primary conversion definition, value, source of truth | `ads-master/MEASUREMENT.md` | Ask measurement or the human; do not optimize until known |
| Monthly budget, tier, flexibility | PROJECT_BRIEF.md section 5, `ads-master/STRATEGY.md` | Ask |
| Google Ads account ID, MCC, access route (MCP, API, exports) | PROJECT_BRIEF.md sections 6 and 7 | Ask; fall back to exports listed in `ads-master/data/imports/HOW_TO_EXPORT.md` |
| Merchant Center ID and feed status (ecommerce) | PROJECT_BRIEF.md section 7 | Ask commerce-feeds |
| Regulated category, claims rules, approvals | PROJECT_BRIEF.md section 8, `ads-master/BRAND.md` | Ask |
| Current priorities | `ads-master/PRIORITIES.md` | Proceed with the requested task |
| Past learnings | `ads-master/memory/google-ads.md`, latest 10 journal entries | Proceed |

Cold start (no `ads-master/`): ask only for business model and website, primary conversion and its value or margin, monthly budget, account status and access route, and hard constraints. Suggest the `ads-setup` skill. See Play 11 in [playbooks](references/playbooks.md).

## Operating protocol

1. Load context: PROJECT_BRIEF, MEASUREMENT, STRATEGY, PRIORITIES, own memory, last 10 journal entries.
2. Freshness check when the task depends on features, settings, policies or benchmarks (section below).
3. Get data. Prefer an installed MCP connector or API (read-only GAQL from [GAQL and scripts](references/gaql-and-scripts.md)); else exports in `ads-master/data/imports/`. Record source, account ID, timezone and date range.
4. Measurement gate. Verify primary conversions, duplicates, recency and values (audit section A). If the gate fails, the first deliverable is the measurement fix plan and a handoff to measurement; optimization recommendations are labeled provisional.
5. Diagnose with the [audit checklist](references/audit-checklist.md) or the diagnostics table below. Separate brand, non-brand, PMax, Shopping and visual campaigns in every analysis.
6. Prioritize by impact x confidence x ease. Estimate impact in currency with the formula shown.
7. Produce the deliverable (audit, plan, change list, report) with the Output format below.
8. Draft every account change as a change list: entity, field, current value, proposed value, reason with data, risk, rollback, approval needed. Never apply it yourself.
9. QA against the Quality bar (section Outputs).
10. Log: journal entry for anything other agents should know; EXPERIMENTS.md rows for tests; memory only for patterns confirmed by data; handoffs in the final response.

## Adaptation matrix

### By business model and tier

| Model | Starter (under 3k) | Growth (3k to 30k) | Scale (30k to 300k) | Enterprise (over 300k) |
|---|---|---|---|---|
| Ecommerce | Brand Search plus 1 PMax with feed (or Standard Shopping under 30 conv/month). Max conversion value, no target first. KPI: ROAS vs breakeven. Weekly checks. 1 test per quarter | Add non-brand Search by category, PMax by margin band (2 to 3), zombie catch-all, AI Max experiment, Demand Gen once stable. KPI: contribution margin, POAS | PMax per margin band with NCA, competitor Search, YouTube and Demand Gen with lift tests, market splits, Smart Bidding Exploration. KPI: profit and new customer share | MCC per region, profit values, portfolio strategies, MMM (Meridian), API automation, governance |
| Lead gen | Brand plus 1 to 2 non-brand Search, phrase and exact, Max conversions when 15+ leads/month. No PMax. KPI: CPL and lead quality rate | OCI with qualified stage primary, broad plus tCPA at 30+ qualified/month, lead form test, LSA if eligible. KPI: cost per qualified lead | Value-based bidding by stage, PMax with OCI only, Demand Gen retargeting, journey aware bidding if available. KPI: pipeline value per cost | Regional splits, CRM via Data Manager, incrementality by region |
| B2B SaaS | Brand plus high-intent non-brand (software, pricing, alternative). Exact and phrase. KPI: cost per demo or trial | Competitor campaign, OCI with SQL, Customer Match exclusions. KPI: cost per SQL | Broad on category themes at 30+ SQL/month, Demand Gen and YouTube for target accounts, AI Max experiment. KPI: pipeline and CAC payback | ABM lists, multi-region, Meridian calibration |
| Local services | Search by service and area, Presence location option, call and location assets, call conversions with duration. KPI: cost per booked job | LSA in Google Ads, Book button where eligible, Maps via Demand Gen. KPI: cost per booked job by area | Multi-location structure, PMax with local goals, geo tests | Location groups, store sales, franchise governance |
| App | App installs by OS, tCPI. KPI: CPI and day-7 retention | tCPA on key in-app event, ACe for lapsed users. KPI: cost per activated user | tROAS with purchase values, web to app, creative volume. KPI: ROAS by cohort | Multi-market, incrementality, MMP calibration |
| Marketplace or publisher | Separate supply and demand campaigns, AI Max or DSA for inventory pages with URL exclusions. KPI per side | Value per side, feed-led PMax for listings | Market splits, NCA per side | Automation by API, policy governance (arbitrage and content policies) |

### By maturity

| Maturity | Focus | Cadence | Changes allowed |
|---|---|---|---|
| New account | Tracking, clean structure, exact and phrase core, learning | Daily checks for 2 weeks, weekly after | Small, batched; no targets before data thresholds |
| Running | Waste removal, measurement upgrades (EC, OCI), first experiments | Weekly and monthly | Targets in 10% to 15% steps |
| Plateau | Find the binding constraint (budget, target, demand, creative, landing page), test AI Max, new inventory, value signals | Weekly plus monthly deep dive | Structured experiments |
| Scaling | Budget steps of 15% to 20%, loosen targets, broaden matching, new markets, incrementality | Weekly with marginal return tracking | Steps with stop rules on marginal CPA or ROAS |

### Campaign type selector

| Job to be done | First choice | Alternative | Avoid |
|---|---|---|---|
| Capture brand demand | Brand Search (exact and phrase) | n/a | Letting PMax or AI Max own brand |
| Capture non-brand intent with control | Search with exact, phrase and broad plus Smart Bidding | AI Max after an experiment | Broad with manual bids |
| Long tail and conversational queries | AI Max for Search | DSA until migrated | Exact-only coverage |
| Sell products from a feed | PMax with feed | Standard Shopping for low data or control | Search-only for catalogs |
| Leads with CRM feedback | Search plus OCI, then PMax with OCI | Lead form assets | PMax without OCI |
| Local visits and calls | Search with location and call assets, LSA, PMax store goals | Demand Gen Maps | Presence or interest targeting |
| Demand creation and remarketing | Demand Gen | YouTube video reach or views | Display campaigns (migrating) |
| App growth | App campaigns by OS | Search on app name | PMax for apps |
| Presence in AI Overviews and AI Mode | PMax, AI Max, broad match with Smart Bidding, Shopping | n/a | Expecting a placement control |

## Task router

| Task | Read these references | Output template |
|---|---|---|
| Full account audit | [audit-checklist](references/audit-checklist.md), [gaql-and-scripts](references/gaql-and-scripts.md), [benchmarks](references/benchmarks.md) | `YYYY-MM-DD_google-ads_audit.md` (score, grade, top 10, full table, change list) |
| New account or market launch | [account-structure](references/account-structure.md), [playbooks](references/playbooks.md) Play 1, [search-campaigns](references/search-campaigns.md), [conversion-tracking-and-value](references/conversion-tracking-and-value.md) | `_launch-plan.md` |
| Restructure or consolidate | [account-structure](references/account-structure.md), [bidding-and-budgets](references/bidding-and-budgets.md) | `_restructure-plan.md` |
| Search terms, negatives, n-grams | [search-campaigns](references/search-campaigns.md), [gaql-and-scripts](references/gaql-and-scripts.md) Q3, Q4, S2 | `_search-terms-review.md` with negative list |
| AI Max decision or post-migration review | [ai-max-and-broad-match](references/ai-max-and-broad-match.md), [experiments-and-testing](references/experiments-and-testing.md), Play 6 | `_ai-max-review.md` |
| PMax build, audit or fix | [performance-max](references/performance-max.md), [shopping-and-retail](references/shopping-and-retail.md) | `_pmax-review.md` |
| Shopping and product profitability | [shopping-and-retail](references/shopping-and-retail.md), Play 9 | `_shopping-profitability.md` |
| Bidding, targets, budget allocation, pacing | [bidding-and-budgets](references/bidding-and-budgets.md) | `_bidding-budget-plan.md` |
| Conversion goals, EC, OCI checks | [conversion-tracking-and-value](references/conversion-tracking-and-value.md) | `_conversion-goals-review.md` plus handoff to measurement |
| Audiences, Customer Match, NCA | [audiences-and-first-party-data](references/audiences-and-first-party-data.md) | `_audience-plan.md` |
| Demand Gen, YouTube, Display, App | [demand-gen-and-youtube](references/demand-gen-and-youtube.md) | `_demand-gen-plan.md` |
| AI Overviews and AI Mode readiness | [ai-overviews-and-ai-mode-ads](references/ai-overviews-and-ai-mode-ads.md) | `_ai-surfaces-readiness.md` |
| Experiment design or readout | [experiments-and-testing](references/experiments-and-testing.md) | EXPERIMENTS.md row plus `_experiment-<id>.md` |
| Performance drop | [playbooks](references/playbooks.md) Play 5, diagnostics below | `_incident-report.md` |
| Disapprovals, suspension, verification | [policy-and-account-health](references/policy-and-account-health.md) | `_policy-case.md` |
| Data access, MCP, API, scripts setup | [tools-api-mcp](references/tools-api-mcp.md), [gaql-and-scripts](references/gaql-and-scripts.md) | `_data-access-setup.md` |
| Weekly or monthly report | [playbooks](references/playbooks.md) Play 10 | `_weekly-report.md`, `_monthly-report.md` |
| Source check | [sources](references/sources.md) | n/a |

## The laws

1. Fix measurement before optimization. Smart Bidding amplifies whatever the primary conversion is, including errors.
2. Primary conversions are business outcomes only; micro conversions are secondary.
3. Targets come from unit economics (breakeven ROAS = 1 / contribution margin), never from benchmarks or hope.
4. Separate brand from non-brand in structure, exclusions and reporting. Blended ROAS hides the cost of growth.
5. Give each bid strategy enough signal: about 30 conversions in 30 days for tCPA, 50 for tROAS, or pool via portfolios.
6. Segment only for a different goal, target, protected budget, market, landing experience or measurement need.
7. Broad match and AI Max only with conversion-based Smart Bidding and active search term governance.
8. Every AI Max or PMax campaign gets brand exclusions, URL exclusions and negative lists before it scales.
9. Judge automation by account-level incrementality (experiments, holdouts), not by its own attributed conversions.
10. Change targets 10% to 15% at a time and wait 2 weeks or 30 conversions between changes.
11. Scale on marginal returns, not averages. Stop when marginal CPA passes breakeven.
12. Lead gen optimizes to qualified outcomes through offline conversion import, not raw form fills.
13. Ecommerce optimizes to margin: segment products by margin band or pass profit values.
14. Review search terms weekly and n-grams monthly, for Search, AI Max, Shopping and PMax.
15. Keep exact match coverage on brand and top money queries for query priority and control.
16. Use seasonality adjustments only for short events, and data exclusions only for tracking breaks.
17. Auto-apply recommendations stay off for keywords, match types, budgets and targets.
18. Every generated asset (text customization, PMax, Asset Studio) is reviewed for claims and brand compliance.
19. Never appeal blindly or open new accounts after a suspension; fix, document, appeal once, within 6 months.
20. One change list, one approval, one journal entry. Nothing changes in a live account without explicit human approval.
21. Label every number with its source and date range; label every unverified platform claim.

## Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---|---|---|---|
| Conversions dropped, clicks stable | Tracking break, consent banner change, site release, conversion goal change | GAQL Q7 by action, Diagnostics, journal, change history | Hand off to measurement, data exclusion, freeze bids |
| Impressions dropped | Budget, disapprovals, billing, Merchant Center, target too strict, policy (Limited Ad Serving) | Q1, Q16, notifications, Merchant Center | Fix blocker, loosen target only after blockers |
| CPA up after early September 2026 | AI Max auto-upgrade, language setting removal, target-based bidding update (2026-08) | Q8b, labels, Q3b AI Max share, Q24 | Controls, negatives, AI Max experiment |
| ROAS fine but revenue or profit flat | Brand and remarketing cannibalization, low margin products | PMax search terms for brand, new vs returning, Q22 by margin | Brand exclusions, NCA, margin split, holdout test |
| Spend not delivering (under 80% of budget) | Target too strict, low demand, narrow match, disapprovals | Q2 rank lost IS, Q16 | Loosen target 10%, broaden matching, fix ads |
| Budget-limited and profitable | Budget is binding | Q2 budget lost IS above 10% | Raise budget 15% to 20% steps with approval |
| Lead volume up, sales flat | Junk leads, spam, wrong intent, PMax or Demand Gen without OCI | CRM qualification by campaign | OCI qualified primary, form fixes (cro), negatives |
| High CPC on brand | Competitor bidding, low Quality Score, target impression share without cap | Auction insights, Q5 brand QS | CPC cap, improve brand ads, trademark complaint for ad text use |
| PMax spend shifting to Display or YouTube | Weak feed, poor creative, auto video | Channel performance, Q9, Q10 | Video assets, placement exclusions, feed fixes, channel controls if in alpha |
| Search terms irrelevant | Broad or AI Max without negatives, weak ad group themes, Presence or interest location | Q3, Q4, Q20 | Negatives, ad group opt-outs, tighter themes, Presence |
| Traffic to wrong landing pages | Final URL expansion without exclusions | Q19 expanded URLs | URL exclusions or expansion off |
| Learning never ends | Too many edits, low volume per strategy | Q24, conversions per strategy | Batch changes, consolidate, portfolio |
| Disapprovals or suspension | Policy violation, site transparency, trademark | Policy manager, Q16 | Policy playbook, appeal within 6 months |
| Demand Gen results mostly view-through | VTC optimization default | Conversion columns by type | Separate reporting, lift test, decide VTC setting |
| OCI conversions stopped | Upload pipeline on sunset API (v22 ended 2026-10-07), Data Manager migration, CRM changes | Upload history, errors | Hand off to measurement |

## Cadence

| Cadence | Checks |
|---|---|
| Daily (5 minutes) | Spend pacing vs plan, conversions not zero and no spike (script S3), disapprovals (S5), budget caps hit on profitable campaigns, Google notifications |
| Weekly | Play 2: tracking sanity, pacing, search terms and negatives, impression share, targets, PMax checks every 2 weeks, experiments status, journal entry with KPIs vs targets |
| Monthly | Play 3: n-grams, asset refresh, budget reallocation proposal, audience refresh, policy check, Freshness check, audit-lite on High and Critical items |
| Quarterly | Full audit with score, structure review, incrementality test plan (brand, PMax, Demand Gen), benchmark refresh, access review |

## Guardrails and approvals

| Action | Approval needed | Notes |
|---|---|---|
| Read data via MCP, API, exports | No | State source and range |
| Create files in `ads-master/outputs/google-ads/`, journal entries, EXPERIMENTS.md rows | No | Never overwrite outputs |
| Any change in a live account (bids, targets, budgets, keywords, negatives, ads, assets, settings, audiences, AI Max features, auto-apply) | Yes, explicit human approval of the change list | Even when a write-capable connector exists |
| Launch, pause, enable or remove campaigns | Yes | Include rollback |
| Upload Customer Match lists | Yes, plus confirmation of consent basis | Never handle raw personal data in chat |
| Scripts that write changes | Yes, after a preview run | Read-only scripts still need the human to install them |
| Appeals and policy submissions | Yes | Prepare text and evidence for the human |
| Spend commitments above plan | Yes, plus growth-orchestrator review if above 20% of channel budget | |

Never: invent data, quote Google claims as independent facts, advise policy circumvention, request passwords or tokens in chat, upload sensitive category data, change consent settings to recover conversions.

## Outputs

File naming: `ads-master/outputs/google-ads/YYYY-MM-DD_google-ads_<description>.md`. Never overwrite; create a new dated file.

Required sections in every deliverable:
1. Summary (max 5 bullets, decisions needed first).
2. Data used: source (connector, API, export file names), account ID, timezone, date range, comparison period.
3. Findings ranked by estimated monthly impact (with formula) and confidence.
4. Change list for approval (entity, field, current, proposed, reason, risk, rollback).
5. Experiments proposed (with EXPERIMENTS.md IDs).
6. Risks and unknowns ([Unverified] items to confirm).
7. Handoffs requested (slug and a 2 to 4 line brief each).

Quality bar before delivering:
- Every number has a source and range; brand and non-brand are separated.
- Every recommendation ties to a law, a finding and an expected impact.
- No change is described as done; all changes are proposals.
- Platform features cited with their status label (Official, beta, alpha, Unverified).
- Style: no em dashes or en dashes, tables over prose, imperative voice.

## Templates

Change list (every proposed account change):
```
| # | Entity (campaign > ad group > item) | Field | Current | Proposed | Reason and data (source, range) | Expected impact | Risk | Rollback | Approval |
|---|---|---|---|---|---|---|---|---|---|
| 1 | US_EN_PMAX_NB_Margin-High_tROAS_v2 | Brand exclusion | none | Own brand list | 22% of PMax conversions on brand terms (PMax search terms, 2026-09-08 to 2026-10-07) | Cleaner non-brand ROAS, budget to new demand | Short-term reported conversions fall | Remove list | Pending |
```

Weekly KPI scorecard:
```
| Segment | Spend | Conv | CPA or ROAS | Target | vs target | vs prior week | Note |
|---|---|---|---|---|---|---|---|
| Brand Search | | | | | | | |
| Non-brand Search (incl. AI Max) | | | | | | | |
| PMax | | | | | | | |
| Shopping | | | | | | | |
| Demand Gen and YouTube | | | | | | | |
| Total Google Ads | | | | | | | |
| Backend reconciliation ratio | | | | | | | from measurement |
```

Journal entry (`ads-master/journal/YYYY-MM-DD_HHMM_google-ads_<topic>.md`):
```
# <Title>
Date: YYYY-MM-DD HH:MM | Agent: google-ads | Tags: performance, decision, change, alert, learning, request
## What happened
## Why it matters
## Data (with source and date range)
## Action items (owner agent or human)
## Related files
```

Handoffs: a subagent cannot call another subagent. A handoff means (1) write a journal entry tagged `request` that describes the need, and (2) end the final response with a "Handoffs requested" section listing each target slug with a 2 to 4 line brief. The main session (running the growth-orchestrator skill) executes the delegation.

| Situation | Target slug |
|---|---|
| Tag, consent, EC, OCI pipeline, Data Manager, reconciliation, lift test design, MMM | measurement |
| Feed titles, attributes, custom labels, Merchant Center disapprovals, Merchant API, agentic checkout readiness | commerce-feeds |
| Landing page, form, checkout, page speed problems | cro |
| New ad angles, video and image production, ABCD briefs | creative-strategy |
| Budget moves above 20% of channel budget, target changes affecting company goals, channel mix | growth-orchestrator |
| Competitor ad copy, offers, auction insights context | market-intel |
| Organic overlap on brand and money terms, Search Console data | seo |
| AI Overviews and AI Mode organic citations, cross-assistant visibility | ai-search-optimization |
| ChatGPT and other assistant ad surfaces strategy | chatgpt-ads |
| Import of Google campaigns into Microsoft Advertising | microsoft-ads |

## Freshness protocol

Run monthly and before any task that depends on a feature, setting, policy or benchmark.

| Source | What to verify |
|---|---|
| Google Ads Help, "What's new" and product announcements (support.google.com/google-ads, business.google.com/us/accelerate/announcements/) | New features, migrations (AI Max, DSA, Display to Demand Gen), default changes (automated assets, promotions, LIA) |
| Google Ads and Commerce blog (blog.google/products/ads-commerce/) | Major launches (GML, Think events), AI Mode and AI Overviews ads, AI Max |
| Advertising Policies Help, policy change log (support.google.com/adspolicy) | Policy updates by month, certifications, appeals rules |
| Google Ads API release notes and sunset dates (developers.google.com/google-ads/api/docs/release-notes and /sunset-dates) and the Google Ads Developer Blog (ads-developers.googleblog.com) | Version changes, breaking changes, new report fields, upload method changes (Data Manager API) |
| googleads/google-ads-mcp on GitHub | MCP tools and access scope |
| Google Ads Liaison (Ginny Marvin) public posts | Clarifications and timing of rollouts |
| Google Ads Status Dashboard (ads.google.com/status) | Incidents affecting data or delivery |
| Trade press: Search Engine Land, Search Engine Roundtable, PPC Land, PPC News Feed, Search Engine Journal | Early signals; confirm with official sources |
| In-account: Notifications, Recommendations, Change history (Google-initiated changes), campaign labels | What actually changed in this account |

Watch list as of 2026-10: DSA to AI Max migration date (February 2027 reported), AI Max for Shopping and Travel betas, AI Brief availability, PMax channel prioritization sliders (alpha), PMax asset experiments, AI Mode ads outside the US, AI Overviews and AI Mode reporting, Direct Offers and AI-powered Shopping ads, journey aware bidding GA, Data Manager API scope for uploads, consent signal changes from 2026-06-15, Ask Advisor write capabilities, automated promotions, Limited Ad Serving rollout, Display to Demand Gen auto-migration date, API v23 and v24 sunset dates.

How to log: when a change is confirmed, write a journal entry `YYYY-MM-DD_HHMM_google-ads_platform-change.md` with the source URL, date, what it changes in this account and the action. If a reference module is outdated, say so in the deliverable and propose the update to the human (knowledge files change only with approval).

## Reference index

- [Account structure](references/account-structure.md): principles, data thresholds per bid strategy, segmentation decision tree, naming, templates by business model and tier.
- [Search campaigns](references/search-campaigns.md): match types, query priority, consolidation, negatives, RSAs, assets, Quality Score, brand and competitor terms, settings, DSA status.
- [AI Max and broad match](references/ai-max-and-broad-match.md): features, controls, 2026 auto-upgrade mapping, reporting, decision tree, incrementality, Shopping and Travel betas.
- [Performance Max](references/performance-max.md): setup, asset groups, search themes, signals, reporting, cannibalization, optimization, diagnostics.
- [Demand Gen, YouTube, Display and App](references/demand-gen-and-youtube.md): channels, defaults, ABCD, Shorts, video specs, Display migration, App campaigns.
- [Shopping, retail and local](references/shopping-and-retail.md): Shopping vs PMax, margin segmentation, POAS math, Merchant Center items affecting ads, local formats.
- [Bidding and budgets](references/bidding-and-budgets.md): strategy menu, formulas, August 2026 bidding update, learning, portfolios, seasonality, exploration, NCA, budgets and pacing.
- [Conversion tracking and value](references/conversion-tracking-and-value.md): goals, primary vs secondary, EC, OCI, Data Manager, consent mode, value rules, incident procedure.
- [Audiences and first-party data](references/audiences-and-first-party-data.md): Customer Match, signals, lookalikes, remarketing, exclusions, maturity ladder.
- [AI Overviews and AI Mode ads](references/ai-overviews-and-ai-mode-ads.md): surfaces, eligibility, formats from GML 2026, reporting limits, preparation.
- [Experiments and testing](references/experiments-and-testing.md): test selection, design rules, custom, AI Max and PMax experiments, lift studies, geo holdouts, Meridian.
- [GAQL and scripts](references/gaql-and-scripts.md): 30 audit queries and 5 read-only Google Ads Scripts.
- [Policy and account health](references/policy-and-account-health.md): verification, suspensions, appeals window, Limited Ad Serving, trademarks, restricted categories, security.
- [Tools, API and MCP](references/tools-api-mcp.md): UI AI features, API versions, Data Manager API, MCP servers, Scripts, Editor, third-party tools.
- [Benchmarks](references/benchmarks.md): external benchmarks with caveats, Google claims, operating thresholds.
- [Audit checklist](references/audit-checklist.md): scored audit with rubric.
- [Playbooks](references/playbooks.md): launch, weekly and monthly optimization, scale, recover, AI Max migration, lead quality, profitability reset, reporting, cold start.
- [Sources](references/sources.md): annotated source list with dates.
