# Core Flows: Triggers, Timing, Content and Offers

Specs for every core automated flow. Each spec lists trigger, filters, timing, messages, content, offer policy, channel mix, exits and KPIs. Timings are starting defaults [Practitioner consensus] to be tuned with the project's own data and holdouts. Trigger and metric names follow Klaviyo with Shopify; equivalents exist in Braze (Canvas), Customer.io (Campaigns and Journeys), Iterable (Journeys), Omnisend (Automations), Mailchimp (Marketing Automation Flows) and HubSpot (Workflows).

All customer facing copy uses only facts in `ads-master/brand/PRODUCT_FACTS.md` and claims in `ads-master/brand/CLAIMS.md`, and passes `compliance` before activation. Activation is G3.

## 0. Flow priority by business model

| Rank | Ecommerce (one time purchase) | Ecommerce (consumable) | Subscription DTC | Lead gen and local services | B2B SaaS | App |
|------|-------------------------------|------------------------|------------------|----------------------------|----------|-----|
| 1 | Checkout and cart abandonment | Welcome | Welcome to first order | Speed to lead (instant response) | Trial onboarding to activation | Onboarding (push plus email) |
| 2 | Welcome | Replenishment | Subscription onboarding | Quote or booking follow-up | Demo request nurture | Activation nudges |
| 3 | Browse abandonment | Checkout and cart abandonment | Dunning (failed payment) | Review request after job | Trial to paid conversion | Paywall or trial conversion |
| 4 | Post purchase (first time buyer) | Post purchase education | Upcoming charge reminder | Reactivation of old quotes | Expansion and adoption | Lapsed user winback |
| 5 | Back in stock, price drop | Cross sell | Cancellation and save flow | Referral | Churn risk save | Referral |
| 6 | Winback | Winback | Winback of cancelled | Seasonal service reminders | Renewal | Reviews and ratings (with mobile-app-growth) |
| 7 | Sunset and re-engagement | Sunset | Loyalty | | | |

## 1. Global flow rules

- Exclusions on every marketing flow: placed order since flow start (where relevant), unsubscribed for the channel, suppressed, in a global control group, employees and test profiles.
- Smart Sending (Klaviyo) or frequency capping (Braze, Iterable, Customer.io): keep on for promotional flows; off for transactional and high intent steps where a delay loses the sale. Klaviyo Smart Sending defaults to a 16 hour window for email [Official, Klaviyo help; verify current default and SMS window].
- One promotional flow at a time per profile when possible: use flow filters such as "Has not been in flow X in the last N days" or priority logic.
- Transactional content (order confirmation, shipping) stays transactional. Mixing heavy promotion into receipts risks reclassification as marketing (consent and CAN-SPAM implications) and Gmail Purchases view treatment [Practitioner consensus; Klaviyo guidance 2025].
- Dynamic product blocks pull from the catalog: suppress out of stock items and items the customer already bought (unless consumable).
- Every step has an exit or filter re-check before send (for example "Placed Order zero times since starting this flow").
- Channel order: email first for low urgency; SMS or WhatsApp only for high intent steps and only with channel consent. Use "if not clicked email within X hours, then SMS" splits to avoid double messaging.
- Quiet hours for SMS: send between 10:00 and 20:00 recipient local time as the default window (federal TCPA solicitation window is 8:00 to 21:00; Florida, Oklahoma and some other states use 8:00 to 20:00) [Official, 47 CFR 64.1200(c); state laws; see [Consent and law](consent-and-law.md)].
- Holdout branch on every high volume flow (10% to 20%) for at least one quarter ([Strategy](lifecycle-strategy-and-metrics.md) section 3).

## 2. Welcome series (new subscriber, no order)

| Field | Spec |
|-------|------|
| Trigger | Added to List (email newsletter list) or Subscribed to SMS; separate branch per capture source if offers differ |
| Filters | Placed Order zero times over all time (send purchasers to a different branch); not in flow in last 30 days |
| Length | 3 to 5 emails over 7 to 14 days; 1 to 2 SMS if consented |
| Exit | Placed Order; unsubscribed |

| Step | Timing | Content | Offer policy |
|------|--------|---------|-------------|
| E1 | Immediately | Deliver the promised incentive or content first line; brand promise in one sentence; bestsellers or quiz entry; set expectations (what and how often) | Only the promised incentive. Unique single use code with expiry |
| SMS1 | Immediately after SMS opt-in confirmation | Confirmation plus incentive; brand name; STOP instructions (required) | Same incentive |
| E2 | Day 1 to 2 | Proof: reviews, UGC, founder or method story (facts only from PRODUCT_FACTS.md) | Reminder of code if unused |
| E3 | Day 3 to 4 | Objection handling: FAQ, sizing, shipping and returns policy, guarantees as approved | None new |
| E4 | Day 5 to 7 | Product education or category guide by zero party data answers | Code expiry reminder |
| E5 (optional) | Day 10 to 14 | Last call or best value bundle | Optional escalation tested with holdout (offer-strategy owns economics) |

Variants: purchaser joins the list (skip incentive, send brand and how to use content); lead magnet signup (deliver asset, nurture by topic). Benchmarks: Klaviyo averages reproduced by third parties put welcome revenue per recipient at about $2.65 (top 10% about $21.18) [Unverified secondary of Klaviyo data, 2026]; Omnisend reports welcome emails at 2.11% conversion and $6.16 per email (2025 data) [Study, vendor, 2026].

## 3. Checkout abandonment and cart abandonment

Use both when the platform sends both events. Checkout abandonment (Started Checkout) is higher intent and should take precedence.

| Field | Checkout abandonment | Cart abandonment (Added to Cart) |
|-------|---------------------|----------------------------------|
| Trigger | Started Checkout | Added to Cart |
| Filters | Placed Order zero times since starting this flow; not in checkout flow in last 7 days | Started Checkout zero times since starting this flow (else checkout flow handles it); Placed Order zero times since start |
| Length | 3 emails, 1 to 2 SMS | 2 to 3 emails, 0 to 1 SMS |

| Step | Timing | Content | Offer policy |
|------|--------|---------|-------------|
| E1 | 1 to 4 hours | Cart contents with images and a button that restores the cart; service reassurance (shipping, returns); no discount | No discount in step 1 |
| SMS1 | 30 minutes to 2 hours (only with SMS consent, inside quiet hours) | Short reminder with cart link | None |
| E2 | 20 to 24 hours | Reviews for items in cart; FAQ; low stock only if true in real time | None, or free shipping threshold reminder |
| E3 | 48 to 72 hours | Final reminder; alternative products; help contact | Optional incentive only for non converters and only if a holdout proves margin positive; unique code with 48 hour expiry |

Benchmarks [Unverified secondary of Klaviyo data, 2026]: abandoned cart average RPR about $3.65, top 10% about $28.89; Omnisend 2025 data: abandoned cart emails converted at 1.51% and $2.54 per email; cart and welcome together drove 76% of automation orders [Study, vendor, 2026]. Abandonment flows carry the highest attribution inflation; run a holdout before claiming the revenue.

Common mistakes: discount in E1 (trains customers to abandon), sending SMS outside quiet hours, no exclusion of buyers who completed on another device, showing items now out of stock.

## 4. Browse abandonment and site abandonment

| Field | Spec |
|-------|------|
| Trigger | Viewed Product (browse) or Active on Site (site abandonment) |
| Filters | Added to Cart zero times since start; Placed Order zero times since start; not in browse flow in last 14 days; Viewed Product at least 1 time (optionally 2 or more for higher intent); email consent |
| Length | 1 to 2 emails; SMS rarely (low intent) |

| Step | Timing | Content |
|------|--------|---------|
| E1 | 2 to 6 hours | Product viewed, 2 to 3 alternatives, one benefit and one proof point |
| E2 | 24 to 48 hours | Category guide or bestsellers in viewed category |

No discounts. Benchmark: browse abandonment RPR about $1.07 average, top 10% about $7.21 [Unverified secondary, 2026]. Requires the onsite tracking snippet and identified visitors (cookied from email clicks or form submits). Consent for onsite tracking follows the CMP; coordinate with `measurement`.

## 5. Back in stock, price drop, low inventory

| Flow | Trigger | Timing | Content | Notes |
|------|---------|--------|---------|------|
| Back in stock | Subscribed to Back in Stock (Klaviyo) or equivalent | When inventory crosses a threshold; batch to avoid selling out before later subscribers get the message | Item back, direct link, size or variant | Highest conversion automation in Omnisend 2025 data: 6.46% [Study, vendor, 2026]; Klaviyo third party average RPR about $9.14 [Unverified] |
| Price drop | Catalog price decreased for a viewed or carted item (Klaviyo Price Drop trigger) | Within 24 hours of drop | Old vs new price, item link | Price reduction claims must follow prior price rules (EU Omnibus: lowest price in the prior 30 days; Turkey has its own prior price rule); check with `compliance` and `offer-strategy` |
| Low inventory | Inventory below threshold for viewed or carted items | Once | Real stock signal only | Never fake scarcity (consumer law) |

## 6. Post purchase (first time buyer vs repeat buyer)

Split by order count. The first time buyer branch is the second order engine.

| Field | Spec |
|-------|------|
| Trigger | Placed Order (or Fulfilled Order for education timed to delivery) |
| Split | Order count = 1 vs 2 or more; product category; subscription vs one time |
| Exit | Next Placed Order (then the profile re-enters with the new count); refund or cancellation |

First time buyer branch:

| Step | Timing | Content | Offer |
|------|--------|---------|-------|
| E1 | 1 to 2 days after order (after confirmation) | Thank you, what happens next, how to get the most out of the product, support contact | None |
| E2 | Delivery day (Fulfilled Order plus carrier transit, or delivery event) | How to use, setup guide, video | None |
| E3 | Delivery plus 5 to 10 days | Usage tips, first results to expect (only approved claims), community | None |
| E4 | Delivery plus 10 to 21 days | Review request ([Loyalty, referral and reviews](loyalty-referral-and-reviews.md)) | No incentive conditioned on positive sentiment |
| E5 | 50% to 70% of the median days to second order | Cross sell by product affinity (bought A, next most likely B from the project's own order pairs) | Optional, tested |
| E6 | Around the median days to second order | Replenishment or second order nudge ([Replenishment](replenishment-and-subscriptions.md)) | Optional, tested |

Repeat buyer branch: shorter, more personal, loyalty status, early access, referral ask, VIP recognition at thresholds.

Transactional messages (confirmation, shipping updates) are not marketing; keep them in the transactional stream and minimize promotion.

## 7. Cross sell and upsell

- Build affinity tables from the project's orders: for each first product, the most common second order product within 120 days (SQL in [Cohort and LTV analysis](cohort-and-ltv-analysis.md) section 6).
- Trigger: Placed Order with product A, wait for usage time, send B with a reason ("goes with", "next step in routine").
- Exclude anyone who already bought B. Cap to one cross sell flow at a time.
- Measure with a holdout; cross sell to recent buyers often has low incrementality.

## 8. Winback

| Field | Spec |
|-------|------|
| Trigger | Segment: last order date between 1.5x and 3x the median reorder interval (rolling), or metric based "Placed Order, then no order for N days" |
| Filters | Not a subscriber with active subscription; not in winback in last 180 days; email engaged or SMS consented |
| Length | 2 to 4 messages over 2 to 4 weeks |

| Step | Timing | Content | Offer |
|------|--------|---------|-------|
| W1 | Entry | "We have new things" or "Here is what changed": new products, improvements | None |
| W2 | +7 days | Personalized picks from purchase history; reviews | None or value add |
| W3 | +14 days | Incentive for non converters only | Tested discount or gift, unique code, expiry |
| W4 | +21 to 28 days | Feedback survey ("why did you stop?") with zero party data capture | None |

Benchmark: winback RPR about $0.84 average [Unverified secondary, 2026]. Non responders move to sunset. Winback for subscriptions is a separate flow.

## 9. Sunset and re-engagement

Protects deliverability. Mandatory for every email program.

| Field | Spec |
|-------|------|
| Entry segment | Email subscribed AND no click AND no order AND no Active on Site in the last 120 to 180 days AND subscribed more than 60 days ago. Do not use opens alone (Apple MPP marks most Apple Mail recipients as openers); if using opens, exclude Apple Privacy opens |
| Messages | 2 to 3 over 14 days: "Still want to hear from us?", preference center (frequency, topics), final notice |
| Outcome | Clickers or updaters return to active; non responders are suppressed from marketing email (keep the profile and consent record) |

Run monthly. Expect active list size to drop and revenue per recipient, inbox placement and spam rate to improve.

## 10. Birthday, anniversary and date based

- Trigger: date property (birthday collected as zero party data, first order date anniversary).
- Timing: 7 days before (gift window) and on the day. Omnisend 2025 data shows birthday emails with average order value above $744 in its dataset [Study, vendor, 2026; skewed by vertical mix].
- Consent: collecting birth date is personal data; ask month and day only unless age matters (age gating handled with `compliance`).

## 11. VIP and loyalty milestones

- Trigger: order count or lifetime spend crosses a threshold, loyalty tier change, points balance near a reward.
- Content: recognition, early access, service perks before discounts.
- Details in [Loyalty, referral and reviews](loyalty-referral-and-reviews.md).

## 12. Subscription lifecycle flows

Upcoming charge reminder, failed payment (dunning), skip and swap prompts, cancellation and save, cancelled winback. Specs in [Replenishment and subscriptions](replenishment-and-subscriptions.md) section 5.

## 13. Lead gen, B2B and SaaS flows

Speed to lead, nurture tracks, trial onboarding, MQL handoff. Specs in [B2B nurture and lead scoring](b2b-nurture-and-lead-scoring.md).

## 14. Flow spec template (copy into the deliverable)

```
## Flow: <name>  (ID or planned ID)
Objective and primary KPI: <e.g. 2nd order rate within 60 days; placed order rate per entrant>
Trigger: <metric or list or segment> | Trigger filters: <...>
Flow filters (re-checked each step): <...>
Exclusions: unsubscribed for channel, suppressed, global control, employees, in <other flow> last N days
Holdout: <x%> random split at entry, readout after <n> entrants or <date>
Channels and consent required: email (marketing consent) | SMS (TCPA express written or local equivalent) | WhatsApp (opt-in) | push
Steps:
| # | Delay | Channel | Conditional split | Subject / preview or SMS text | Content blocks | Offer (code type, expiry) | Smart Sending | Quiet hours |
Dynamic content rules: <catalog feed, out of stock suppression, already bought suppression>
Facts and claims used: <PRODUCT_FACTS.md rows, CLAIMS.md IDs>
Compliance review: <status, reviewer, date>
QA: test profiles per branch, links, UTMs, rendering (dark mode, mobile), unsubscribe and STOP, timezone
Status plan: Draft (G1 spec) -> created as Draft or Manual in ESP (G2) -> Live (G3 approval ID)
Rollback: set flow to Manual or Draft; note queued messages will still send unless cancelled
Measurement: attribution window, holdout readout date, owner
```

## 15. QA checklist before any flow goes live

- [ ] Trigger fires on a test profile in each branch; filters exclude buyers and unsubscribed profiles
- [ ] Every link resolves, has UTMs per `MEASUREMENT.md` governance, restores cart where applicable
- [ ] Unsubscribe link and one click unsubscribe header present (marketing email); SMS includes STOP language where required
- [ ] Physical postal address and sender identity present (CAN-SPAM, ePrivacy national rules)
- [ ] Dynamic blocks show correct products, prices and currency; out of stock items hidden
- [ ] Codes are unique, single use, with expiry; discount exists in the store and is limited to intended products
- [ ] Rendering checked on mobile, dark mode and the top clients (Apple Mail, Gmail app, Outlook)
- [ ] SMS quiet hours and time zone handling verified
- [ ] Holdout branch configured and documented in EXPERIMENTS.md
- [ ] Compliance sign off recorded; change request approved for activation (G3)
