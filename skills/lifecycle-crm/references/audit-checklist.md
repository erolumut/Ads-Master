# Lifecycle Audit Checklist (scored)

Run on every new project, then quarterly. Each item: check, why, how to verify, severity, fix. Mark Pass, Partial or Fail, and N/A where the item does not apply (for example SMS items with no SMS program). Data used and date ranges go in the audit header. Never pull customer level PII for an audit; aggregates and settings screens are enough.

Severity weights: Critical 5, High 3, Medium 2, Low 1. Pass = full weight, Partial = half, Fail = 0. Section score = earned / possible (excluding N/A).

## A. Measurement and data

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | Order and product events (Viewed Product, Added to Cart, Started Checkout, Placed Order, Fulfilled Order, refunds) flow into the ESP with correct revenue | Every flow and report depends on them | ESP metrics list and last event timestamps; compare ESP Placed Order count and revenue to backend for 30 days (gap under about 5%) | Critical | Fix integration; map metrics; handoff to measurement |
| A2 | Attribution window documented and click based for decisions; Apple Privacy opens excluded where the ESP allows | Avoid inflated revenue | ESP attribution settings screenshot | High | Set and document; report window in headers |
| A3 | At least one holdout (flow or global) exists or is planned for the top 3 flows | Incrementality unknown otherwise | EXPERIMENTS.md, flow splits | High | Add holdouts ([Strategy](lifecycle-strategy-and-metrics.md) section 3) |
| A4 | Cohort repeat rates (30, 45, 60, 90 days) and 12 month LTV are computed from backend data | Retention goals need a baseline | Cohort report exists | High | Run [Cohort analysis](cohort-and-ltv-analysis.md) |
| A5 | UTMs on all lifecycle links follow MEASUREMENT.md governance | Owned channel reporting in GA4 | Sample 10 links | Medium | Fix UTM templates |
| A6 | Profiles deduplicated (email and phone merge), test and employee profiles excluded | Clean segments and reports | Profile counts vs customers; exclusion property | Medium | Merge and flag |

## B. Consent and compliance

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | Consent stored per channel with timestamp, source, method, text version and jurisdiction | Legal proof; correct sends | Sample profile consent fields; form settings | Critical | Add fields and capture logic |
| B2 | No imported, purchased or scraped lists sent as subscribed | Law and deliverability | List import history, list sources | Critical | Suppress unconsented; re-permission only where lawful |
| B3 | Unsubscribe works in one click and propagates to all systems within 2 days; SMS STOP honored within the legal window | Gmail and Yahoo rules; CAN-SPAM; TCPA | Test unsubscribe and STOP end to end | Critical | Fix headers, sync |
| B4 | US SMS consent language meets TCPA express written consent standard and is displayed at capture | Statutory damages exposure | Form screenshots | Critical (if US SMS) | Replace with compliant text ([Consent and law](consent-and-law.md) 3.1) |
| B5 | SMS quiet hours enforced by recipient time zone (default 10:00 to 20:00) and state rules | Quiet hour suits | ESP SMS settings; send logs by local hour | High (if US SMS) | Configure quiet hours and time zone logic |
| B6 | Turkey: consents registered in İYS within 3 business days; İYS checked before sends; refusals synced both ways; KVKK and commercial message consents collected separately (not via a single OTP) | Invalid consent and fines | İYS integration logs; checkout flow review | Critical (if Turkey) | Integrate İYS; split consents |
| B7 | France: no individual open tracking for campaign optimization without tracking consent (CNIL, from 2026-07-14) | Regulatory exposure | ESP tracking settings for French recipients | High (if France) | Disable or collect consent |
| B8 | EU and UK: soft opt-in used only for existing customers, similar products, with opt-out at collection | ePrivacy, PECR | Checkout checkbox and privacy notice | High (if EU or UK) | Fix capture |
| B9 | Physical address and sender identity in every marketing email | CAN-SPAM, national rules | Template footer | Medium | Add |
| B10 | Subscription cancellation is online and as easy as sign up; save offers never the only exit | California ARL, ROSCA | Walk through the portal | High (if subscriptions) | Fix with storefront-ux and compliance |
| B11 | Review requests go to all buyers; no incentive conditioned on positive sentiment | FTC rule, DMCC | Flow logic | High | Remove gating |

## C. Deliverability and infrastructure

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Branded sending domain with SPF, DKIM (2048 bit) and DMARC aligned | Gmail, Yahoo, Microsoft requirements | DNS lookup; ESP domain status; Postmaster v2 compliance status | Critical | Authenticate ([Deliverability](email-deliverability.md) 1.5) |
| C2 | RFC 8058 one click unsubscribe headers on marketing mail | Gmail and Yahoo bulk rules | Raw message headers | Critical | Enable in ESP |
| C3 | Gmail spam rate under 0.1% over the last 30 days (never 0.3%) | Rejection risk | Postmaster Tools v2 | Critical | Play 4 in [Strategy](lifecycle-strategy-and-metrics.md) |
| C4 | Yahoo complaint rate under 0.1% to 0.2%; Outlook delivering without 5.7.515 bounces | Provider specific blocks | Sender Hub; bounce logs | High | Fix authentication and segments |
| C5 | DMARC moving to enforcement (quarantine or reject) with reports monitored | Spoofing protection; BIMI | DMARC record and report tool | Medium | Plan enforcement |
| C6 | Transactional and marketing streams separated | Protect receipts | Sending domains or IPs | Medium | Separate subdomain |
| C7 | Sunset flow running monthly; unengaged over 180 days suppressed from campaigns | Reputation | Segment sizes, flow status | High | Build sunset ([Core flows](core-flows.md) 9) |
| C8 | Hard bounce under 0.5% per send; capture verification and bot protection on forms | List quality | Bounce report; form settings | Medium | Verification, honeypot, double opt-in for risky sources |
| C9 | BIMI configured where DMARC is at enforcement | Brand recognition | BIMI record check | Low | Add with VMC or CMC |

## D. List growth

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Capture rate tracked by source and device, with subscriber to customer rate per source | Quality over volume | Form analytics plus cohort by source | High | Add source property |
| D2 | Pop up targeting excludes subscribers, checkout and cart; mobile friendly and accessible (storefront-ux implements) | Conversion and SEO | Site review | Medium | Spec to storefront-ux |
| D3 | Two step capture (email then SMS or WhatsApp) with separate consent per channel | Higher consented reach | Form review | Medium | Add step 2 |
| D4 | Incentive economics known (acquisition investment) and incentive delivered instantly | Margin and trust | offer-strategy notes; welcome E1 | Medium | Model with offer-strategy |
| D5 | Post purchase and back in stock capture points exist | High intent sources | Site review | Medium | Add |

## E. Core flow coverage

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Welcome series live with purchaser vs non purchaser branches | First order and expectations | Flow list | Critical | Build |
| E2 | Checkout and cart abandonment live with buyer exclusion re-checked at each step | Highest intent revenue | Flow logic | Critical | Build or fix |
| E3 | Browse abandonment live | Mid intent recovery | Flow list | High | Build |
| E4 | Post purchase split by first time vs repeat buyer, timed to delivery | Second order engine | Flow logic | Critical | Build |
| E5 | Replenishment timed to consumption per SKU (consumables) | Repeat orders | Flow delays vs reorder interval data | Critical (if consumable) | Build ([Replenishment](replenishment-and-subscriptions.md)) |
| E6 | Cross sell based on the project's own affinity data | AOV and frequency | Flow content vs affinity table | Medium | Build table |
| E7 | Winback timed from the median reorder interval | Reactivation | Flow trigger | High | Build |
| E8 | Back in stock, price drop (with prior price rule) | High conversion | Flow list | Medium | Build |
| E9 | Review request timed to usage, all buyers | Proof and SEO | Flow logic | Medium | Build |
| E10 | Subscription flows: upcoming charge, dunning, cancellation, cancelled winback | Churn | Flow list | Critical (if subscriptions) | Build |
| E11 | Lead gen and B2B: speed to lead response and nurture tracks | Pipeline | CRM workflows | Critical (if lead gen) | Build ([B2B](b2b-nurture-and-lead-scoring.md)) |

## F. Flow quality

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | No discount in first abandonment message; discounts only tested with holdouts | Margin, training customers to wait | Flow content | High | Restructure |
| F2 | Codes unique, single use, with expiry | Leakage | Discount settings | High | Switch to unique codes |
| F3 | Dynamic product blocks exclude out of stock and already purchased items | Relevance | Test profiles | Medium | Fix feed rules |
| F4 | Copy uses only PRODUCT_FACTS.md and CLAIMS.md; compliance reviewed | Legal risk | Compare copy to registry | Critical | Rewrite; compliance review |
| F5 | Rendering QA on mobile, dark mode and top clients; live text for offers | Engagement; AI summaries | Test sends | Medium | Fix templates |
| F6 | Flows do not double message (cross flow filters, Smart Sending, channel cascade) | Fatigue and complaints | Profile journey review | High | Add filters |
| F7 | Flow RPR within the top half of the account's own flow history and not far below benchmarks | Upside sizing | Reporting API | Medium | Rebuild top gaps |

## G. Campaigns and frequency

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Campaigns sent by engagement tier, not to the full list | Deliverability and revenue per send | Campaign audiences | Critical | Tiering ([Segmentation](segmentation-and-personalization.md) 1) |
| G2 | Frequency set per tier and validated by unsubscribe and complaint trends | Gmail Manage subscriptions exposure | Unsub by campaign | High | Adjust |
| G3 | Campaign calendar aligned with promo calendar (offer-strategy) and product launches | Coordination | Calendar | Medium | Build |
| G4 | Campaign versions by category affinity or lifecycle stage at scale | Relevance | Campaign variants | Medium | Add versions |
| G5 | Every campaign has a hypothesis or test element logged | Learning | EXPERIMENTS.md | Low | Add |

## H. Segmentation and personalization

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | Engagement tiers built on clicks, orders, site activity (not raw opens) | MPP | Segment definitions | High | Redefine |
| H2 | RFM or predicted CLV segments used for VIP and at risk treatment | Value focus | Segment list | Medium | Build |
| H3 | Zero party data captured and used within 30 days | Relevance, consent value | Properties and flows | Medium | Add questions and branches |
| H4 | AI personalization or decisioning runs with a holdout and within approved offer bounds | Measured lift; margin safety | Tool settings | High (if used) | Add holdout and bounds |

## I. SMS, WhatsApp and push

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | 10DLC or toll-free registration current; content matches registered use case | Carrier blocking | Provider console | Critical (if US SMS) | Update registration |
| I2 | Fully loaded cost per message known; revenue per message read against it | Profitability | Billing plus reports | High | Add carrier fees to model |
| I3 | Channel cascade avoids duplicate sends across email, SMS, WhatsApp, push | Fatigue | Flow logic | High | Add splits |
| I4 | WhatsApp templates categorized correctly; quality rating healthy; no marketing templates to US numbers | Policy, delivery | WhatsApp Manager | High (if WhatsApp) | Recategorize, segment |
| I5 | Two way SMS welcome to build known sender status (iOS 26 unknown senders) | Visibility | Welcome content | Low | Add reply prompt |
| I6 | Push permission strategy and cadence agreed with mobile-app-growth | Opt-outs, uninstalls | App settings | Medium (if app) | Handoff |

## J. Retention economics

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| J1 | Lifecycle KPIs in STRATEGY.md or PRIORITIES.md (second order rate target, repeat at 90 days, LTV) | Focus | Files | High | Propose to orchestrator |
| J2 | Incremental contribution, not attributed revenue, used for budget decisions | Avoid over crediting | Reports | High | Holdouts |
| J3 | Discount dependency measured (share of revenue on codes, margin per flow) | Margin | Reports | Medium | Play 8 |
| J4 | Subscription churn split voluntary vs involuntary; dunning recovery measured | Fixable churn | Subscription reports | High (if subscriptions) | Build |

## K. Paid media integration

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| K1 | Recent buyer exclusions on acquisition campaigns, refreshed at least weekly | Wasted spend | Channel audiences | High | Sync audiences |
| K2 | Existing customer lists maintained for new customer goals (Google, Meta) | Clean new customer optimization | Platform settings | High | Handoff to channel agents |
| K3 | Google Customer Match sync path on Data Manager API or vendor confirmed | Uploads may fail since 2026-04-01 | Vendor confirmation | Medium | Migrate |
| K4 | No sensitive segments uploaded; audience register maintained | Policy and law | Register | High | Build register |
| K5 | LTV by acquisition source shared monthly with growth-orchestrator; LTV values validated before bidding use | Budget allocation and value bidding | Reports | Medium | Monthly cohort report |

## L. Loyalty, referral and reviews

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| L1 | Loyalty program incrementality measured (holdout or matched cohort), liability tracked | Margin | Reports | Medium (if loyalty) | Measure |
| L2 | Loyalty events in the ESP with reward and expiry flows | Engagement | Event list | Medium | Integrate |
| L3 | Referral fraud controls (self referral, code leakage, return window) | Leakage | Program settings | Medium | Add controls |

## Scoring rubric

| Overall score | Grade | Meaning | Action |
|---------------|-------|---------|--------|
| 85% to 100% | A | Top tier program | Optimize with tests and AI decisioning under holdouts |
| 70% to 84% | B | Solid, gaps in depth | Fix High items in 30 days |
| 50% to 69% | C | Core gaps | 90 day rebuild plan (Play 2) |
| Below 50% | D | Foundation missing | Launch play (Play 1); fix Critical items first |

Override rule: any Critical item in sections B or C marked Fail caps the grade at C and goes to the top of the report, because consent and deliverability failures block every other gain. A failing B item that could cause unlawful sends is a stop condition: pause the affected sends (with human approval) and log it in `ads-master/INCIDENTS.md`.

## Audit output template

```
# Lifecycle audit: <brand> <YYYY-MM-DD>
Scope and data: <ESP>, <SMS tool>, <orders source>, date ranges <...>; access level (read only)
Score summary: overall <x%> grade <A to D>; section scores A to L
Critical and high failures (with evidence and fix)
Full results table (section, item, result, evidence, fix, owner, gate)
Value at stake (top 5 fixes, estimated with own data; label assumptions)
90 day plan (weeks, owners, gates)
Experiments to log (holdouts, offer tests)
Handoffs requested
```
