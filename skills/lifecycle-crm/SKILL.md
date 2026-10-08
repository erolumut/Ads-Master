---
name: lifecycle-crm
description: Retention and lifecycle marketing (CRM) for email, SMS, RCS, WhatsApp, push and in-app. Use to audit, launch, optimize or recover programs in Klaviyo, Braze, Customer.io, Iterable, Mailchimp, Omnisend, Attentive, Postscript or HubSpot; write flow specs with timing, content and offers (welcome, browse, cart and checkout abandonment, post purchase, replenishment timed to consumption, cross sell, winback, sunset, back in stock, reviews, referral, loyalty, subscriptions with Recharge or Skio, B2B nurture and lead scoring); build segments (engagement tiers after Apple MPP, RFM, predicted CLV); fix deliverability (Gmail, Yahoo, Outlook sender rules, SPF, DKIM, DMARC, one click unsubscribe, spam rate, BIMI); check consent (GDPR soft opt-in, CNIL pixels, PECR, CAN-SPAM, TCPA, 10DLC, Turkey IYS and KVKK, WhatsApp policy); grow lists with quality; analyze cohorts (repeat rate at 30, 45, 60, 90 days, LTV curves, holdouts); feed suppression, customer audiences and LTV values to paid media.
---

# Lifecycle and CRM (Retention)

> Knowledge as of 2026-10. Mailbox rules, messaging prices, consent law and ESP features change monthly. Run the Freshness Protocol before acting on any feature, setting, policy or benchmark.

## Mission and scope

Grow customer lifetime value and repeat purchase at a profit, with owned channels the business is allowed to use and that land in the inbox. The second order is the most valuable conversion in most DTC businesses; speed to lead and nurture quality are the equivalent in lead gen and B2B.

In scope:
- Strategy, metrics and incrementality for lifecycle programs (holdouts, incremental contribution).
- Flows and campaigns across email, SMS, RCS, WhatsApp, push and in-app (logic, timing, content, offers, copy drafts).
- Segmentation: engagement tiers, RFM, predicted CLV and churn, consumption based, affinity, zero party data.
- Deliverability: authentication, mailbox provider rules, monitoring, warmup, hygiene, sunset.
- Consent and law for messaging (with `compliance` as the approver).
- List growth strategy, incentives, consent text and quality measurement (on-site UI patterns belong to `storefront-ux`).
- Replenishment, subscriptions, loyalty, referral and review programs.
- B2B nurture, lead scoring and sales handoff.
- Cohort analysis, repeat rates, LTV curves and LTV by acquisition source.
- Lifecycle inputs to paid media: suppression, customer lists, value based audiences, LTV values.

Out of scope (hand off): pop up and account page UI, components and storefront code (`storefront-ux`); landing pages and checkout tests (`cro`); tracking implementation, conversion values and offline imports (`measurement`); ad account configuration (channel agents); discount levels, reward economics and promo calendar (`offer-strategy`); claims and legal approval (`compliance`); app SDK, push permission prompts and app store work (`mobile-app-growth`); budgets and priorities (`growth-orchestrator`).

## Intake (minimum facts; where to find them)

| Fact | Where in `ads-master/` | If missing |
|------|------------------------|-----------|
| Business model, products, AOV, contribution margin, markets | PROJECT_BRIEF.md sections 1 to 3 | Ask; required |
| ESP, SMS or WhatsApp tool, subscription and loyalty apps, CRM | PROJECT_BRIEF.md section 7 | Inspect site and repo (ads-setup scan); ask |
| Consent sources and jurisdictions (EU, UK, US states, Turkey İYS) | PROJECT_BRIEF.md section 9, MEASUREMENT.md | Ask; block sends until known |
| Revenue truth and metric definitions (new customer, repeat rate, contribution) | MEASUREMENT.md, METRICS.md | Propose definitions via journal |
| Orders history (24 months) and lifecycle exports (90 days) | data/imports/ (HOW_TO_EXPORT.md row `lifecycle-crm`) or connectors | Request exports; work from aggregates |
| Approved facts and claims | brand/PRODUCT_FACTS.md, brand/CLAIMS.md | No customer copy until present |
| Approver for customer messaging, automation stage | GUARDRAILS.md, guardrails.json | Default to stage 1 (read only) |
| Offers allowed (discount bounds, rewards) | STRATEGY.md, offer-strategy outputs | Draft without offers; request offer-strategy |
| Past tests and learnings | EXPERIMENTS.md, memory/lifecycle-crm.md | Start fresh |

Cold start (no `ads-master/`): ask only for business model, ESP and SMS tools, markets, list sizes by channel, AOV and margin, and whether an orders export is available. Or suggest the `ads-setup` skill.

## Operating protocol

1. Load context: PROJECT_BRIEF.md, MEASUREMENT.md, METRICS.md, STRATEGY.md, PRIORITIES.md, GUARDRAILS.md, brand files, `memory/lifecycle-crm.md`, the last 10 journal entries, EXPERIMENTS.md, INCIDENTS.md.
2. Classify the task with the Task router and open only the references it names.
3. Stop condition check: consent failures (unlawful sends possible), deliverability incidents (Gmail spam rate over 0.3%, rejections), broken order events. If found, raise at the top of the response, write an INCIDENTS.md row and recommend pausing affected sends (human approves).
4. Measurement gate: ESP Placed Order counts and revenue reconcile with backend within about 5% for 30 days; otherwise request a `measurement` handoff and label all revenue numbers as unreconciled.
5. Diagnose with data: flow and campaign reports (reporting API or exports), deliverability dashboards, list growth, cohorts. State sources and date ranges.
6. Audit with the scored [Audit checklist](references/audit-checklist.md) for broad tasks.
7. Prioritize by value at stake x confidence x ease; consent and deliverability first, then core flows, then the second order engine, then campaigns, channels and programs.
8. Produce deliverables: audit, flow specs, segment definitions, copy drafts, consent text proposals, cohort report, holdout plans, audience specs for paid media.
9. Gate every external action: drafts in files (G1); ESP drafts as Draft or Manual (G2, stage 2+); activation, sends, imports, consent changes and audience uploads via a change request (G3).
10. QA against the Quality bar.
11. Log: output file, EXPERIMENTS.md rows, journal entry for other agents, memory only for data-confirmed patterns.
12. Handoffs: you cannot call other agents. Write a journal entry per request and end with "Handoffs requested".

Quality bar:
- Every number names source, date range and attribution window; incremental vs attributed is explicit.
- Every flow spec has trigger, filters, exits, timing, channel consent requirement, offer policy, holdout and rollback.
- Copy uses only PRODUCT_FACTS.md and CLAIMS.md; consent text and offers marked for compliance and offer-strategy review.
- No customer PII in any file; aggregates only.

## Lifecycle economics

```
Incremental contribution = (revenue per entrant treated - control) x treated entrants x margin - message cost - incremental discount cost
Retention lift value     = first time buyers x (new repeat rate - old repeat rate) x contribution per repeat order
Subscriber value (90d)   = subscriber to customer rate x first order contribution + repeat contribution in window
SMS message ROI          = incremental revenue x margin / (ESP fee + carrier fees + incentives)
12m contribution LTV     = cohort cumulative contribution per customer at month 12
LTV to CAC               = 12m contribution LTV / acquisition investment per new customer (METRICS.md)
```

Worked example: 6,000 first time buyers per month, 60 day repeat rate 14%, contribution per repeat order 24 USD. A post purchase rebuild plus replenishment reminders lift it to 16.5% in an 80/20 flow holdout. Monthly incremental value = 6,000 x 0.025 x 24 = 3,600 USD from the first repeat order, before downstream LTV. Report it with the experiment ID, the interval and the holdout split, not as "flows made 40,000 USD" (attributed revenue).

## Adaptation matrix

### By business model and budget tier

| Model | Primary lifecycle KPI | Starter (under $3k/mo paid) | Growth ($3k to $30k) | Scale ($30k to $300k) | Enterprise (over $300k) |
|-------|----------------------|-----------------------------|----------------------|----------------------|-------------------------|
| Ecommerce (one time purchase) | Second order rate at 60 to 90 days; 12m contribution LTV | Klaviyo, Omnisend or Mailchimp; welcome, checkout and cart, browse, post purchase, sunset; 1 to 2 campaigns per week to engaged | All core flows, engagement tiers, SMS for high intent, review flow, first holdouts | Affinity versions, predicted CLV segments, global control group, paid media suppression and value audiences | Braze or Iterable or Klaviyo enterprise, multi market consent, AI decisioning under holdouts, warehouse LTV models |
| Ecommerce (consumable) | Reorder rate within 1.5x interval; subscription share | Welcome plus replenishment by days of supply | Replenishment by empirical SKU interval, subscribe and save, dunning | Personal reorder intervals, subscription save flows, loyalty | Predicted next order date at scale, multi brand subscription programs |
| Subscription DTC | Monthly churn (voluntary and involuntary); shipments per subscriber | Native or simple subscription app, upcoming charge and dunning flows | Recharge, Skio or Loop events in ESP; cancellation reasons; save flow compliant with ARL | Churn prediction, tier perks, winback by reason | Pricing and cadence tests with offer-strategy, MMM input of retention |
| Lead gen and local services | Lead to customer rate; speed to lead | Instant response, quote follow-up, review requests | CRM nurture by stage, lead scoring, SMS reminders | Scoring from closed won data, offline conversion loop | Multi location templates, routing and SLAs at scale |
| B2B SaaS | Activation rate, trial to paid, MQL to SQL, net revenue retention | HubSpot or Customer.io onboarding and trial emails | Fit and engagement scoring, nurture tracks, PLG triggers | Product usage events, expansion and churn risk plays, ABM with linkedin-ads | Warehouse driven lifecycle, Salesforce or Braze, governance |
| App | D7 and D30 retention, subscription conversion | Push and email onboarding with mobile-app-growth | Behavioral push, in-app, lapsed user winback | Braze or Iterable cross channel, intelligent timing | Decisioning and experimentation platform |
| Marketplace or publisher | Repeat buyers or readers per month; supply side activation | Newsletter welcome and digest | Personalized digests, saved search alerts | Two sided lifecycle (buyers and sellers), paywall lifecycle | Recommendation driven messaging at scale |

### By list size (email engaged profiles)

| List size | What changes |
|-----------|-------------|
| Under 5k engaged, or under 500 customers | Core flows only; no predictive analytics (Klaviyo needs 500+ purchasers and 180 days of history); holdouts impractical, use before and after with care; shared sending fine |
| 5k to 50k | Engagement tiers, monthly sunset, flow level A/B tests, flow holdouts on cart and welcome pooled over months |
| 50k to 500k | Global control group feasible, predictive segments, campaign versions by affinity, SMS and WhatsApp as second channel, provider level deliverability monitoring |
| Over 500k | Dedicated IP pools considered with warmup, throttled sends by provider, AI decisioning with holdouts, warehouse models, multi stream architecture |

### By maturity

| Maturity | Focus | Cadence | Tests |
|----------|-------|---------|-------|
| New (no program or new ESP) | Consent, authentication, core flows (Play 1) | Weekly build reviews | Few; QA first |
| Running | Audit, rebuild top flows, tiers, holdouts | Weekly report, monthly cohort report | 1 to 2 flow tests per month |
| Plateau | Second order engine, offer detox, new channels, predictive segments | Biweekly | Bigger tests (offers, new flows, channel cascade) |
| Scaling (list or spend growing fast) | Deliverability under volume, list quality by source, paid media suppression, peak plays | Weekly with deliverability watch | Parallel tests by flow |

## Task router

| Task | Read these references | Output template |
|------|----------------------|-----------------|
| Full lifecycle audit | [Audit checklist](references/audit-checklist.md), [Strategy and metrics](references/lifecycle-strategy-and-metrics.md) | Audit output template (audit-checklist.md) |
| Launch a program or migrate ESP | [Strategy and metrics](references/lifecycle-strategy-and-metrics.md) Plays 1 and 6, [Core flows](references/core-flows.md), [Deliverability](references/email-deliverability.md) | 90 day plan plus flow specs |
| Write or rebuild a flow | [Core flows](references/core-flows.md), [Segmentation](references/segmentation-and-personalization.md) | Flow spec template (core-flows.md section 14) |
| Replenishment or subscription program | [Replenishment and subscriptions](references/replenishment-and-subscriptions.md), [Cohort and LTV](references/cohort-and-ltv-analysis.md) | Flow specs plus economics |
| Segments, RFM, predicted CLV, personalization | [Segmentation](references/segmentation-and-personalization.md) | Segment definition sheet |
| Deliverability drop or setup | [Deliverability](references/email-deliverability.md), Play 4 in [Strategy](references/lifecycle-strategy-and-metrics.md) | Incident note plus fix plan |
| SMS, RCS, WhatsApp, push program | [SMS, WhatsApp and push](references/sms-whatsapp-and-push.md), [Consent and law](references/consent-and-law.md) | Channel plan with cost model |
| Consent review, new market, Turkey İYS | [Consent and law](references/consent-and-law.md) | Consent gap list for compliance |
| List growth plan | [List growth](references/list-growth.md) | Capture plan plus spec for storefront-ux |
| Loyalty, referral, reviews | [Loyalty, referral and reviews](references/loyalty-referral-and-reviews.md) | Program spec |
| B2B nurture or lead scoring | [B2B nurture and lead scoring](references/b2b-nurture-and-lead-scoring.md) | Scoring model plus nurture map |
| Cohorts, repeat rate, LTV | [Cohort and LTV analysis](references/cohort-and-ltv-analysis.md) | Cohort report template |
| Holdout or incrementality test | [Strategy and metrics](references/lifecycle-strategy-and-metrics.md) section 3 | EXPERIMENTS.md row plus test plan |
| Suppression, audiences, LTV values for ads | [Lifecycle and paid media](references/lifecycle-and-paid-media.md) | Audience register plus handoffs |
| Choose or connect tools, MCP, API pulls | [Tools, APIs and MCP](references/tools-api-mcp.md) | Tool recommendation or data pull note |
| Weekly or monthly reporting | [Strategy and metrics](references/lifecycle-strategy-and-metrics.md) section 7, [Cohort and LTV](references/cohort-and-ltv-analysis.md) section 9 | Weekly report, monthly cohort report |

## The laws

1. No consent, no send: consent is per channel, per jurisdiction, with proof; Turkey consents must be in İYS.
2. Deliverability before revenue: authenticate, add one click unsubscribe, keep Gmail spam rate under 0.1%.
3. Flows before campaigns: core flows earn most of the revenue per send; build them first.
4. The second order is the target: post purchase and replenishment beat any campaign trick for DTC LTV.
5. Time to consumption, not to the calendar: replenishment dates come from SKU reorder data.
6. Opens are not a KPI: Apple MPP, AI prefetch and CNIL rules broke them; decide on clicks, orders and revenue per recipient.
7. Engagement decides frequency: tier the list; mail the unengaged less, then sunset them.
8. Attributed is not incremental: prove lifecycle revenue with holdouts before claiming it to finance.
9. Contribution, not revenue: judge flows, offers and LTV on margin after discounts and message costs.
10. No discount in the first abandonment touch: discounts go late, unique, expiring and tested.
11. One message, one job: one primary action per message; no triple sends across channels.
12. Transactional stays transactional: keep promotions out of receipts and shipping messages.
13. Respect the clock: SMS only inside quiet hours for the recipient's time zone.
14. Fully loaded cost per message: SMS and WhatsApp prices rose in 2025 and 2026; read ROI after cost.
15. Never buy or scrape lists; judge capture sources on subscriber to customer rate.
16. Cancel must be easy: subscription save offers never block the exit.
17. Ask every buyer for a review; never condition incentives on positive sentiment.
18. Suppress buyers from acquisition ads and keep existing customer lists fresh.
19. LTV values to bidding only after validation against realized cohorts.
20. AI drafts, humans approve: AI generated flows, segments and copy stay draft until G3 approval.
21. Facts only from PRODUCT_FACTS.md, claims only from CLAIMS.md.
22. Aggregates only in files: no emails, phones or names in outputs, journal or memory.

## Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| Owned revenue down week over week | Event or integration break, deliverability, traffic drop into flows, seasonality, attribution setting change | ESP vs backend orders; flow entrants; provider level clicks; YoY | Play 5 in [Strategy](references/lifecycle-strategy-and-metrics.md) |
| Gmail spam rate above 0.1% | Unengaged sends, list import, frequency spike, misleading subject | Postmaster v2; segment of recent sends | Engaged only sends, sunset, Play 4 |
| Outlook bounces 550 5.7.515 | Authentication or alignment failure | DMARC reports | Authenticate branded domain |
| High open rate, falling clicks and orders | MPP inflation hides real disengagement | Apple Privacy open share | Click based tiers |
| Cart flow revenue high but total revenue flat | Attribution overlap; discount pulls forward orders | Flow holdout; discount share | Holdout; move discount later |
| Repeat rate falling for new cohorts | Discount heavy acquisition, product issues, weak post purchase | Cohort cut by source and first order discount | offer-strategy and channel handoffs; rebuild post purchase |
| Unsubscribes jump | Frequency or relevance, Gmail Manage subscriptions | Unsub by tier and campaign | Lower frequency for E2 and E3; preference center |
| SMS revenue per message below cost | Low intent sends, MMS overuse, rising carrier fees | Fully loaded cost per message | Restrict SMS to high intent flows; SMS vs RCS test |
| WhatsApp sends failing (error 131049) | Frequency capping, US marketing pause, quality | WhatsApp Manager | Segment by country, utility vs marketing, reduce volume |
| Subscription churn up | Payment failures, price change, product fatigue, hard cancellation backlash | Voluntary vs involuntary split; reasons | Dunning, flexibility, reason based winback |
| Lead to SQL rate falling | Scoring drift, form changes, source mix | Scoring lift review; source mix | Recalibrate model; quality feedback to channels |
| Klaviyo predictive fields empty | Data thresholds unmet | Purchasers count, history length | Use RFM until thresholds are met |

## Benchmarks to use with caution (compare to own history first)

| Benchmark | Value | Source, date | Caveat |
|-----------|-------|--------------|--------|
| Flows share of sends vs email revenue | 5.3% of sends, about 41% of email revenue; flow placed order rate 2.11% vs 0.16% for campaigns; RPR $1.94 vs $0.11 | Klaviyo 2026 benchmark, 183K+ brands, via secondary [Study, vendor 2026] | Attributed, not incremental |
| Flow RPR averages | Back in stock $9.14; abandoned cart $3.65 (top 10% $28.89); welcome $2.65 (top 10% $21.18); browse $1.07 (top 10% $7.21); winback $0.84 | Klaviyo data reproduced by agencies [Unverified, 2026] | Secondary; AOV dependent |
| Automations share | 2% of email sends, 30% of email revenue, 16x revenue per send; cart plus welcome 76% of automation orders; back in stock 6.46% conversion | Omnisend 2026 report, 150K brands, 2025 data [Study, vendor 2026] | Vendor dataset |
| SMS campaigns vs automations | 12.39% CTR, 0.12% conversion vs 20.34% CTR, 0.77% conversion; $0.15 vs $0.74 per send | Omnisend, 321M SMS, 2025 data [Study, vendor 2026] | Seasonal swings large |
| Apple share of tracked opens | About 62% (Gmail about 27%, Outlook about 6%) | Litmus July 2026 via secondary [Study, 2026-07] | Opens inflated by MPP |
| Pop up submit rate | Klaviyo median about 2.3% | Secondary [Unverified] | Definition is submits / views |
| Repeat purchase (12 months) | 18.8% across 156K DTC customers; 76.4% of second orders within 90 days | Vendor dataset [Unverified, 2026] | Reused by several vendors |
| Spam rate thresholds | Under 0.1% target; 0.3% enforcement line | Google and Yahoo [Official] | Hard rules, not benchmarks |

## What top operators do differently
- Run holdouts on flows and a global control group, and report incremental contribution to finance.
- Build replenishment and cross sell from their own order data (SKU intervals, next product affinity).
- Treat deliverability as a weekly KPI with provider level views, and sunset relentlessly.
- Segment campaigns into versions by lifecycle stage and affinity instead of blasting.
- Use discounts late, unique and tested; replace many with value adds (early access, gifts, service).
- Feed cohort LTV by acquisition source back into budget allocation every month.
- Keep consent records audit ready and multi jurisdiction (İYS, CNIL, TCPA) before scaling channels.

## Common expensive mistakes
- Sending to the full list after an import or a quiet period, then hitting Gmail and Yahoo complaint limits.
- Discount in the first cart email, training customers to abandon.
- Counting ESP attributed revenue as incremental and adding it to ad platform revenue.
- Optimizing on open rates inflated by Apple MPP.
- SMS outside quiet hours or with weak consent language (statutory damages per message).
- WhatsApp marketing templates aimed at US numbers during the pause, or AI general assistants on WhatsApp.
- Hiding the cancel button in subscription portals.
- Using the retired HubSpot legacy score in live workflows.
- Uploading health related segments to ad platforms.

## Cadence

| When | What |
|------|------|
| Daily (5 minutes, when sending) | Bounces, complaints and Postmaster spam rate after major sends; SMS and WhatsApp failures; flow errors; INCIDENTS check |
| Weekly | Weekly report (owned revenue attributed, flow and campaign RPR, deliverability by provider, list health, SMS cost); experiment status; journal entry |
| Monthly | Cohort report (repeat at 30, 45, 60, 90 days, LTV by source); sunset run; list growth by source; audience refresh check with channel agents; freshness check |
| Quarterly | Full scored audit; holdout readouts and incrementality ratios; flow rebuild roadmap; consent and İYS sync audit; tool and contract review |

## Guardrails and approvals

Follow `docs/GUARDRAILS_MODEL.md` and the project's `ads-master/GUARDRAILS.md`.

| Action | Gate | Rule |
|--------|------|------|
| Read reports, settings, aggregates | G0 | Automatic |
| Flow specs, copy, segment definitions, consent text drafts in files | G1 | Automatic |
| Create flows, templates or campaigns in the ESP as Draft or Manual, unscheduled | G2 | Stage 2+, confirmation |
| Activate a flow or message, schedule or send a campaign, send SMS or WhatsApp via API or MCP | G3 | Change request; approver for customer messaging |
| Import, subscribe, suppress or change consent; upload audiences to ad platforms; change codes or rewards | G3 | Consent evidence and compliance check |
| Delete flows, lists, profiles or data; billing; ownership | G4 | Never |

Always: snapshot the current flow or campaign before changes, read back after any approved write (status, audience, schedule, links, codes), log the approval in a journal entry, and keep rollback steps in the change request. Customer facing copy passes `compliance`.

## Outputs

Path: `ads-master/outputs/lifecycle-crm/YYYY-MM-DD_lifecycle-crm_<description>.md`. Never overwrite.

| Deliverable | Description slug | Required sections |
|-------------|------------------|-------------------|
| Audit | `lifecycle-audit` | Score summary, critical and high failures, results table, value at stake, 90 day plan, handoffs |
| Flow specs | `flow-specs-<flow>` | Spec template per flow, QA checklist, change request draft |
| Cohort report | `cohort-report` | Template in cohort-and-ltv-analysis.md section 9 |
| Weekly report | `weekly` | FACTS, INTERPRETATION, RECOMMENDATION |
| Deliverability incident | `deliverability-incident` | Evidence, cause, fix, ramp plan |
| Channel plan | `channel-plan-<channel>` | Consent, cost model, flows, cadence |
| Audience register | `audience-register` | Definition, source, lawful basis, refresh, platforms |
| Holdout plan or readout | `holdout-<id>` | Design, sample size, metrics, result, decision |

EXPERIMENTS.md row: `| E### | YYYY-MM-DD | lifecycle-crm | If we ..., then ..., because ... | metric | I/C/E | holdout or A/B | stop rule | status | result | learning |`

## Freshness protocol

Check before acting and note the check date in the output.

| Topic | Source | Verify |
|-------|--------|--------|
| Gmail rules and tools | Google sender guidelines and FAQ (support.google.com/a/answer/81126 and 14229414), Postmaster Tools help, Google Workspace Updates blog | Thresholds, enforcement, Postmaster v1 and v2 status |
| Yahoo, Microsoft, Apple | Yahoo Sender Hub, Microsoft Defender for Office 365 blog and Outlook postmaster, Apple Support 102322 | Requirement changes, SNDS migration |
| Klaviyo | developers.klaviyo.com changelog and API revision, help center, klaviyo.com/whats-new, newsroom | Feature status (Composer, MCP, WhatsApp, RCS markets), rate limits |
| Other ESPs | Braze press and docs, Customer.io release notes, Iterable newsroom, Omnisend What's new, Mailchimp release notes, Attentive and Postscript release notes, HubSpot product updates | Agent and MCP features, pricing |
| US SMS | FCC TCPA orders and Federal Register, CTIA guidelines, TCR and carrier notices (via provider) | Revocation rule effective date, quiet hours rulings, fees |
| WhatsApp | Meta developer docs (pricing, policy), WhatsApp Business Messaging Policy | Pricing changes, US pause, chatbot policy |
| EU and UK | CNIL, EDPB, ICO, EU Digital Omnibus legislative file | Pixel rules, soft opt-in, Omnibus outcome |
| Turkey | iys.org.tr announcements, Ticaret Bakanlığı, KVKK decisions, Resmi Gazete | İYS rules, fines, KVKK decisions |
| Subscriptions | FTC negative option docket (P064202), California ARL updates, Recharge and Skio announcements | Rulemaking progress, product changes |
| Paid media lists | Google Ads API and Data Manager API docs, Meta customer list terms | Upload paths, policy restrictions |

How to log: if a check changes a recommendation, write `ads-master/journal/YYYY-MM-DD_HHMM_lifecycle-crm_freshness-<topic>.md` with source URL, date, what changed and which reference section is outdated, and propose the knowledge update to the human.

## Reference index

- [Lifecycle strategy and metrics](references/lifecycle-strategy-and-metrics.md): stage model, metric dictionary, attribution windows, holdouts and sample size, economics, fix order, eight playbooks, weekly report.
- [Core flows](references/core-flows.md): flow priority by model, global rules, welcome, checkout and cart, browse, back in stock, post purchase, cross sell, winback, sunset, date based, VIP, spec template, QA checklist.
- [Replenishment and subscriptions](references/replenishment-and-subscriptions.md): consumption timing, SKU interval SQL, subscribe and save economics, subscription KPIs, tools, lifecycle flows, auto renewal law.
- [Segmentation and personalization](references/segmentation-and-personalization.md): engagement tiers after MPP, RFM SQL, predicted CLV requirements, consumption and affinity segments, zero party data, personalization ladder, AI tools.
- [Email deliverability](references/email-deliverability.md): Gmail, Yahoo, Microsoft, Apple rules, DNS and headers, thresholds, monitoring, inbox changes, BIMI, warmup, hygiene, diagnostics.
- [SMS, WhatsApp and push](references/sms-whatsapp-and-push.md): channel selection, US SMS registration and fees, consent mechanics, iOS 26, RCS, WhatsApp pricing and policy, push and in-app, copy patterns.
- [Consent and law](references/consent-and-law.md): consent record standard, EU, France CNIL, UK, US, Canada, Turkey İYS and KVKK, TCPA status, WhatsApp, reviews, pre-send checklist.
- [List growth](references/list-growth.md): principles, capture points, offers, targeting rules for storefront-ux, consent text, benchmarks, list quality metrics, tests.
- [Loyalty, referral and reviews](references/loyalty-referral-and-reviews.md): when loyalty pays, program types, economics, tools, loyalty flows, referral design and fraud, review timing and rules.
- [B2B nurture and lead scoring](references/b2b-nurture-and-lead-scoring.md): funnel definitions, speed to lead, scoring models and SQL, nurture tracks, PLG and local services lifecycle, closed loop.
- [Lifecycle and paid media](references/lifecycle-and-paid-media.md): suppression, Customer Match and Meta list rules, data handling, LTV values, cohort feedback to budgets.
- [Cohort and LTV analysis](references/cohort-and-ltv-analysis.md): data requirements, repeat rate SQL, Python cohort script, time to second order, LTV curves, cuts, predicted LTV, report template.
- [Tools, APIs and MCP](references/tools-api-mcp.md): ESP landscape 2026, selection, MCP servers, Klaviyo API rate limits and example, gate mapping, exports.
- [Audit checklist](references/audit-checklist.md): scored sections A to L with rubric and output template.
- [Sources](references/sources.md): annotated sources with dates and reliability notes.
