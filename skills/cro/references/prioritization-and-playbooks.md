# Prioritization, Roadmap and Playbooks

> A CRO program wins by running the right tests in the right order at a steady pace, and by fixing obvious problems without testing them. This module covers scoring, the roadmap, velocity, and the step by step plays.

## 1. Triage before scoring

Every finding goes into one of four lanes:

| Lane | Criteria | Action |
|------|----------|--------|
| Fix now (just do it) | Bug, broken flow, missing information, accessibility failure, legal risk, clear usability defect with no plausible downside | Ship after human approval, measure before/after |
| Test | Plausible upside and plausible downside, enough traffic | Add to test backlog, score |
| Research | Unclear cause or unclear solution | Add a research task (recordings, survey, user test) |
| Park | Low impact or no evidence | Keep in backlog with reason |

Instrumentation problems (tracking gaps, missing events) block everything else. Hand them to `measurement` first.

## 2. Scoring frameworks

| Framework | Factors | Strength | Weakness |
|-----------|---------|----------|----------|
| ICE (Sean Ellis) | Impact, Confidence, Ease, 1 to 10 each | Fast, used in EXPERIMENTS.md | Subjective, scores drift |
| PIE (WiderFunnel) | Potential, Importance, Ease | Good for choosing which pages to work on | Ignores evidence quality |
| PXL (CXL) | Binary and weighted questions (above the fold? noticeable in 5 s? adds or removes element? backed by user testing, qualitative, analytics, heatmaps? ease) | Objective, rewards evidence and visibility | Longer to score |
| RICE | Reach, Impact, Confidence, Effort | Good for product teams | Reach and impact overlap for CRO |

Recommended: score with PXL-lite below, then record ICE in EXPERIMENTS.md (Impact = reach plus visibility, Confidence = evidence, Ease = effort) so all agents share one format.

### 2.1 PXL-lite scorecard (max 20)

| Question | Points |
|----------|--------|
| Change is above the fold on mobile | 2 |
| Change is noticeable within 5 seconds | 2 |
| Adds or removes an element (not only restyles) | 1 |
| Runs on a high traffic page or template (top 20% of sessions or revenue) | 2 |
| Addresses a problem found in analytics | 1 |
| Addresses a problem found in recordings or heatmaps | 1 |
| Addresses a problem found in surveys, VOC or user testing | 2 |
| Supported by a past test or memory entry for this project | 2 |
| Affects money pages (PDP, cart, checkout, pricing, lead form) | 2 |
| Bold enough to reach the MDE your traffic can detect | 2 |
| Ease: under 1 day of build (3), under 1 week (2), under 1 sprint (1), more (0) | 0 to 3 |

Convert to ICE: Impact = round((above fold + noticeable + traffic + money page) / 8 x 10); Confidence = round(evidence points / 6 x 10); Ease = round(ease / 3 x 10).

## 3. Roadmap structure

Build a 6 to 12 week roadmap with three swimlanes:
1. Fix lane: just-do-it items, shipped in batches with before/after monitoring.
2. Test lane: experiments by page area so tests can overlap without interference (for example PDP above the fold, cart, checkout, LP hero).
3. Research lane: next questions to answer.

Themes beat random tests. Pick 2 to 3 themes per quarter from research (for example "shipping cost anxiety", "trust for new visitors", "mobile PDP clarity") and run a series of tests per theme. Iterate on winners and on informative losers.

## 4. Velocity and program metrics

| Metric | Definition | Starting target |
|--------|-----------|-----------------|
| Tests launched per month | Count of tests reaching planned sample | Growth: 2 to 4; Scale: 4 to 10; Enterprise: 10+ |
| Valid test rate | Tests with no SRM, planned duration met, primary metric pre-registered | 90% or more |
| Win rate | Significant wins on primary metric / concluded tests | Expect 10% to 30%; much higher suggests false positives |
| Conclusive rate | Wins plus significant losses / concluded tests | Optimizely suggests 35% to 40% as healthy [Study, 2023] |
| Cumulative impact | Sum of discounted expected annual impact of shipped winners | Report quarterly |
| Fix lane throughput | Just-do-it items shipped per month | Track |
| Time to launch | Days from approved idea to live test | Under 14 days |

Do not chase raw velocity. Optimizely's analysis reports that velocity alone at scale can double cost for the same impact; better test design and multi-variation tests raise expected impact [Study, 2023].

## 5. Playbooks

### Play 1: New landing page for a paid campaign (launch)
1. Intake: channel, audience segment and awareness level, offer, ad angles and creatives, conversion event, budget (from channel agent or human).
2. Pick the page type with [Landing page anatomy](landing-page-anatomy.md). Decide dedicated LP vs PDP.
3. Pull VOC for the segment; write a copy deck with [Offer and copy](offer-and-copy.md).
4. Build or spec the page with [Build recipes](landing-page-build-recipes.md): server rendered, fast, tracked, accessible.
5. Message match check against the actual ads ([Message match](message-match-by-channel.md)): score 7 or more.
6. QA: devices, in-app browsers, form to CRM, conversion fires once, LCP under 2.5 s.
7. Human approval to publish. Journal entry with URL, date, and what the channel agent should point traffic to.
8. Week 1 to 2: monitor CVR vs the old page or benchmark, form analytics, recordings (30 sessions). Fix bugs fast.
9. Week 3+: start the first test from the research backlog (usually hero or offer).

### Play 2: 30-day CRO sprint on a running funnel (optimize)
- Days 1 to 3: intake, measurement sanity check, funnel analysis by segment ([Research methods](research-methods.md)).
- Days 4 to 8: heuristic audit with [Audit checklist](audit-checklist.md), recordings, start on-site polls and post-purchase survey.
- Days 9 to 12: synthesize insight grid, triage into lanes, score.
- Days 13 to 15: ship fix-lane batch (with approval), build first 1 to 2 tests.
- Days 16 to 30: run tests, monitor SRM and guardrails, continue survey collection, prepare next tests.
- Day 30: report (section 6), update roadmap, write memory entries only for data-confirmed patterns.

### Play 3: Plateau breakthrough (tests keep coming back flat)
1. Check test power: are tests sized for an MDE the traffic can detect? Flat results from underpowered tests mean nothing.
2. Check boldness: are tests cosmetic (colors, button copy)? Move to offer, value proposition, page structure and flow tests.
3. Go back to research: run a fresh survey and 5 user tests on the money page. Talk to 5 customers.
4. Test the offer: bundles, guarantee, trial terms, pricing presentation (with approval).
5. Check traffic quality with channel agents: CVR plateaus often follow audience broadening; segment by campaign.
6. Try radical redesign tests on one template (one big variant vs control), accepting less learning per test.

### Play 4: Scaling the experimentation program (scale)
1. Move from client-side to server-side or edge testing for core templates.
2. Standardize: test plan template, readout template, metric definitions, QA checklist, SRM alerting.
3. Build a learning repository: every concluded test with screenshots, result, learning, tags.
4. Add multi-variation tests where traffic allows.
5. Add CUPED or variance reduction for logged-in or repeat-visitor metrics.
6. Add holdouts for personalization and cumulative impact measurement (for example 5% global holdout from all shipped changes for a quarter).
7. Governance: test calendar to avoid collisions with promos and launches.

### Play 5: Conversion rate drop recovery (recover)
Run in this order; stop at the first confirmed cause.
1. Tracking: did conversions drop in the backend (orders, CRM leads) too? If backend is stable, it is a tracking break (consent change, tag removed, Shopify Thank you page upgrade after 26 August 2026, GTM publish). Hand to `measurement` immediately.
2. Site breakage: errors by browser and device, checkout test order, form test submission, payment gateway status, JavaScript errors in Clarity, recent deploys or app installs.
3. Speed: CrUX and RUM for the last 28 days vs prior; a new tag or app.
4. Traffic mix: sessions by channel, campaign, device and country vs prior period. A paid campaign broadening audiences or a new low-intent source lowers site CVR without any site problem. Compare CVR within each source.
5. Offer and price: price changes, stock outs, shipping cost changes, promo ended, competitor promo (`market-intel`).
6. Seasonality: same period last year; holidays.
7. Write a journal entry with the cause, evidence and fix; alert the affected channel agents.

### Play 6: Low traffic site (Starter tier)
1. Skip A/B testing for now unless the decision tree in [Experimentation statistics](experimentation-statistics.md) section 10 allows it.
2. Do the research sprint (5 days) and the audit.
3. Ship fix-lane changes in weekly batches with before/after monitoring and a comparison series.
4. Validate big changes with 5-user tests and five-second tests.
5. Focus on offer clarity, trust, speed and forms; these rarely backfire.
6. Revisit testing when monthly conversions per page or template exceed about 400 to 800.

### Play 7: Shopify store 7-day CRO audit
Day 1: measurement check and post-August 2026 Thank you page tracking check. Day 2: funnel by device, top landing pages by paid spend. Day 3: PDP and collection heuristic audit. Day 4: cart and checkout audit (express wallets, shipping transparency, branding), app and script audit for speed. Day 5: recordings and reviews mining. Day 6: synthesis and scoring. Day 7: report with fix lane, test backlog, and Rollouts or app-based test plan.

### Play 8: B2B demo funnel
1. Get CRM data: lead to SQL, SQL to opportunity, by source and form.
2. Audit demo page, pricing page and forms (section F and H of the audit).
3. Implement instant scheduling for qualified leads; measure held demos per visitor.
4. Test form fields and qualification routing with cost per opportunity as the metric.
5. Add a self-serve alternative (product tour, pricing) for not-ready visitors.
6. Coordinate with `linkedin-ads` and `google-ads` on offline conversion imports so bidding learns from SQLs.

## 6. Reporting templates

Weekly CRO note (journal, short): tests live with status and SRM check, tests concluded with decision, fixes shipped, KPI vs last week and vs same week last year, blockers, handoffs.

Monthly CRO report (`ads-master/outputs/cro/YYYY-MM-DD_cro_monthly-report.md`):
```
# CRO monthly report: <month>
Data sources and date ranges:
## KPIs (table: KPI, this month, last month, same month last year, target)
## Program metrics (tests launched, valid rate, win rate, conclusive rate, cumulative impact)
## Concluded tests (result, decision, learning)
## Fixes shipped (date, change, before/after with comparison series)
## Next month roadmap (fix, test, research lanes)
## Risks and handoffs
```
