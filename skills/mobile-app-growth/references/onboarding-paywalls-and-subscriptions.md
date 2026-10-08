# Onboarding, Paywalls and Subscriptions

> Knowledge as of 2026-10. Key changes: Apple offer codes for all IAP types (2025-10-29; IAP promo codes ended 2026-03-26); monthly subscriptions with a 12-month commitment (iOS 26.4, not US or Singapore, 2026-04-27); Retention Messaging in App Store Connect and API (fall 2026); Subscription Bundles and Suites, Group Purchases and Volume Purchasing (2026-10-22) for iOS 27; Google Play default account recovery extended from 30 to 60 days, delayed charging for low risk users, an in-app subscription management API "coming soon" (I/O 2026); Google Play 10% service fee on auto-renewing subscriptions from 2026-06-30 in the US, UK and EEA. Retention flows (push, email, in-app messages) belong to lifecycle-crm; pricing strategy across channels is shared with offer-strategy.

## 1. Onboarding: get to value before asking for anything

Define the activation event per app: the first moment a user gets the core value (first scan, first workout logged, first level won, first saved search). Measure time to activation and the share activated by D1.

Onboarding sequence (default for subscription apps):
1. Value promise screen (one sentence, one visual).
2. 3 to 7 personalization questions (goal, level, frequency). Questions raise commitment and feed the paywall copy [Practitioner consensus].
3. A "building your plan" moment that shows the personalized result.
4. Activation: let the user do the core action once, or show a preview of the result.
5. Paywall (onboarding placement).
6. Permissions in context: notifications after the first value moment with an explanation screen; ATT after value (see [Measurement](mobile-measurement-skan-aak-mmp.md) section 6); location or camera only when the feature needs it.
7. Account creation late, unless the product requires it first. If any third party login is offered, include Sign in with Apple or an equivalent (Guideline 4.8) [Official].

Diagnostics:
| Symptom | Check | Fix |
|---------|-------|-----|
| D0 drop before paywall above 40% | Screen by screen funnel in analytics | Cut screens, move account creation later |
| High paywall views, low trial starts | Paywall variant data, price display, trial clarity | Paywall test (section 4) |
| Trial starts high, D0 cancellations high | RevenueCat cancellation timing | Expectation mismatch between ad, store page and paywall; send a value reminder before the trial ends (lifecycle-crm) |
| Low D1 retention | Activation rate | Shorten time to value |

## 2. Monetization models

| Model | When it fits | Evidence |
|-------|-------------|----------|
| Hard paywall (pay or trial before core use) | Clear single job utilities, AI tools, fitness plans | Median install to paid by D35 10.7% (down from 12.1%) vs 2.1% for freemium [Study, RevenueCat 2026-03] |
| Freemium with soft paywall | Products whose habit forms before payment (productivity, social, content) | Year-one retention 28% freemium vs 27% hard paywall for annual plans, nearly identical [Study, RevenueCat 2026-03] |
| Weekly plans | Utilities, AI and quick jobs | 55.5% of subscription revenue in Adapty's 2025 data; weekly with trial 12-month LTV $54.50 vs $7.40 without [Study, Adapty 2026] |
| Annual first | Health and fitness, education, long term habits | Annual plans 60.6% of Health and Fitness revenue [Study, Adapty 2026] |
| Consumable IAP and ads | Games, creator and AI credit apps | Hybrid monetization; see game economics in [Unit economics](app-growth-model-and-unit-economics.md) |
| Monthly with 12-month commitment (Apple) | Price sensitive markets where annual upfront is a barrier | Available iOS 26.4+, not in the US or Singapore [Official, 2026-04] |

Trials: RevenueCat 2026 reports a 42.5% median trial to paid rate for 17 to 32 day trials vs 25.5% for 4 days or less, while short trials grew to 46.5% of trials [Study, 2026-03]. Adapty 2026 finds trials raise LTV in Utilities, Health and Fitness, Education and Photo and Video, and lower it in Productivity, Lifestyle, Graphics and Design and Entertainment, where direct buyers are worth more [Study, 2026]. Test trial length per category; never copy a benchmark.

## 3. Paywall anatomy and rules

Elements, top to bottom:
1. Outcome headline personalized from onboarding answers.
2. Proof: rating count, outcome stat or testimonial, only from brand/PRODUCT_FACTS.md and brand/CLAIMS.md.
3. Plan selector: 2 to 3 plans, one preselected; show the billed amount for each.
4. Trial terms: when the trial ends, what is charged, how to cancel (a timeline graphic works).
5. Primary button with a clear action ("Start my 7-day free trial").
6. Restore purchases, terms of use and privacy policy links.
7. Close button visible (hard paywalls still need a clear way out of the screen, even if it leads to a limited mode or back).

Store rules:
- Apple: subscription pricing must be clear; the amount the user will be billed must be the most prominent pricing element, and calculated prices (per week equivalents) must not be more prominent [Official, App Review Guideline 3.1.2 and Apple subscription guidance, verify wording]. Misleading free trial claims are rejected.
- Google Play: Subscriptions policy requires clear offer terms, including trial length, price after the trial and cancellation information [Official].
- Korea: free to paid trials and discounted offers need additional consent within 30 days of payment or conversion (Apple, 2025-02) [Official].
- Price increases: Apple handles consent rules per storefront; for example, increases in Austria, Germany and Poland required subscriber consent from 2025-08-04 [Official, 2025-05]. Hand customer communication to lifecycle-crm.

## 4. Paywall and pricing experiments

Tools: RevenueCat (Paywalls, Experiments, Targeting, Web Billing), Superwall (remote paywalls and experiments), Adapty (paywall builder, A/B tests, web paywalls). All support remote configuration without an app release.

Test order:
1. Placement and timing (onboarding end vs after first activation).
2. Plan mix and default plan (annual preselected vs weekly).
3. Trial vs no trial, and trial length.
4. Price points per tier of storefronts.
5. Copy and design.

Design rules:
- Primary metric: net revenue per paywall view or per install at a fixed horizon (D30 minimum, D60 to D90 for annual heavy apps), including refunds. Conversion rate alone is misleading: a cheaper plan can win conversion and lose revenue.
- Guardrail metrics: refund rate, D7 retention, trial cancellation within 24 hours.
- Sample: compute from the revenue variance; as a floor, aim for at least 300 to 500 conversions per variant for conversion reads and longer for revenue reads [Practitioner consensus].
- Run full weeks; do not stop on the first good day; avoid overlapping tests on the same users.
- Log each test in EXPERIMENTS.md with stop rule and owner.

Benchmarks for context: Adapty 2026 reports onboarding paywalls with trials convert at 1.35% on average (highest placement and trial combination in its dataset), 90% of trial starts on day 0 and 44.5% of purchases on day 0 [Study, 2026]. Different denominators across vendors make these non comparable to RevenueCat's install based figures.

## 5. Store offer types (use the right tool)

| Goal | Apple | Google Play |
|------|-------|-------------|
| New subscriber incentive | Introductory offers: free trial, pay as you go, pay up front (one per subscription group per user) [Official] | Free trial and introductory price phases in offers on a base plan [Official] |
| Existing or lapsed subscriber offer in app | Promotional offers (signed server side) [Official] | Developer determined offers [Official] |
| Lapsed subscriber reactivation | Win-back offers (iOS 18+), shown in the App Store and in-app, eligibility rules set in App Store Connect [Official, 2024-06] | Win-back offers for lapsed subscribers [Official] |
| Codes for campaigns and partners | Offer codes, now for all IAP types (consumables, non-consumables, non-renewing subscriptions) since 2025-10-29 [Official] | Promo codes [Official] |
| Save at cancellation | Retention Messaging: custom message, imagery and optional offer at the moment of cancellation, in App Store Connect or the Retention Messaging API (fall 2026) [Official, 2026-06] | In-app subscription management API so users can change plan or accept a downgrade when they tap cancel ("coming soon") [Official, 2026-05] |
| Multi product | Subscription Bundles and Suites (request access) [Official, 2026-06] | Multiple base plans and add-ons [Official] |
| Teams and families | Family Sharing; Group Purchases (later 2026); Volume Purchasing via Apple School Manager and Apple Business (2026-10-22) [Official] | Family library rules [Official] |

## 6. Churn management

| Type | Lever | Owner |
|------|-------|-------|
| Involuntary (failed payment) | Apple: Billing Grace Period on (3, 16 or 28 days) and billing retry; Google: grace period and account hold (default recovery now 60 days; top developers saw up to 18% lower involuntary churn), delayed charging for low risk users [Official, 2026-05] | mobile-app-growth sets store settings; lifecycle-crm messages the user |
| Voluntary at trial end | Value reminders before trial end, show progress | lifecycle-crm |
| Voluntary at renewal | Retention Messaging (Apple), downgrade offers, annual switch offers | mobile-app-growth (offer config) with lifecycle-crm |
| Post churn | Win-back offers, lapsed user CPP or custom store listing, ACe and Apple Ads returning users | mobile-app-growth |

Server side: process App Store Server Notifications V2 and Google RTDN (through RevenueCat or your backend) so that cancellations, refunds and billing issues reach analytics and the MMP within hours.

## 7. Metrics to report weekly

| Metric | Source |
|--------|--------|
| Install to trial (D0, D7, D30) | RevenueCat or analytics |
| Trial to paid (completed trials only) | RevenueCat |
| Install to paid D35 | RevenueCat |
| Paywall view rate and conversion by placement | Paywall tool |
| Net revenue per install D7, D30 by channel and OS | RevenueCat joined with MMP |
| Refund rate | Store reports or RevenueCat |
| Active subscriptions, MRR, churn, reactivations | RevenueCat or store analytics |
| Plan mix (weekly, monthly, annual) | RevenueCat |

## 8. Handoffs

| Situation | Hand off to |
|-----------|-------------|
| Push, email, in-app message flows for trial reminders, win-back, onboarding nudges | lifecycle-crm |
| Price ladder, bundles, discount vs bonus economics across web and app | offer-strategy |
| Claims on the paywall (results, health, finance) | compliance |
| Web paywall pages, checkout speed, form UX | cro, site-engineer |
| Subscription events in the MMP and ad platforms | measurement |
