# SaaS: Pricing Pages, Signup Flows and Trial to Paid

> In SaaS, the conversion that pays is a paying account, not a signup. CRO owns the path from landing page through signup to the first value moment (activation), in partnership with product and lifecycle teams. Every test reports downstream: activation rate and trial to paid, not only signup rate.

## 1. Funnel model and metrics

| Stage | Metric | Formula | Owner |
|-------|--------|---------|-------|
| Visit to signup or demo request | Visitor CVR | signups / unique visitors | cro |
| Signup to activation | Activation rate | activated accounts / signups (within N days) | cro with product |
| Activation to paid | Trial to paid or free to paid | paying accounts / trials started (cohort) | product, lifecycle |
| Demo request to held | Show rate | held demos / booked demos | sales ops |
| Held demo to opportunity | SQO rate | opportunities / held demos | sales |
| Paid to retained | Month 3 logo retention | active paying at month 3 / paid | product |

Define activation from data: the earliest action that best separates retained from churned users (for example "connected a data source and invited one teammate within 7 days"). If `ads-master/MEASUREMENT.md` has no activation definition, propose one to the human and the `measurement` agent.

Guardrail rule: a variant that raises signups but lowers activated signups per visitor is a loss. Primary metric for SaaS website tests is "activated signups per visitor" or "trials started per visitor" with trial to paid as a guardrail once cohorts mature.

## 2. Go-to-market motion decides the page

| Motion | Primary CTA | Pricing page | Signup |
|--------|-------------|--------------|--------|
| Product-led (self-serve, under about $100 per month) | Start free / Start trial | Full transparent pricing | Instant, SSO, minimal fields |
| Hybrid (self-serve plus sales for teams) | Start free + Talk to sales | Transparent self-serve tiers, "Contact sales" for Enterprise | Instant for self-serve, routed demo for larger companies |
| Sales-led (ACV over about $15k) | Book a demo | Starting prices or "from" prices, or packaging without prices [Contested] | Demo form with instant scheduling |

## 3. Pricing page anatomy

| Element | Rule |
|---------|------|
| Headline | Value framing, not "Pricing" alone: "Plans that grow with your team" is weak; "Start free. Upgrade when you add your second store." is specific |
| Billing toggle | Monthly and annual; show annual savings as currency and percent; default to the option that maximizes long-term revenue per visitor, test it |
| Tiers | 3 to 4 tiers. Name by customer type or outcome. Highlight one "Most popular" or "Recommended" tier with a visual frame |
| Price display | Large price, unit clear ("per user per month, billed annually"), currency localized by geo |
| Tier summary | One line "Best for ..." per tier, then 5 to 8 key features; full comparison table below |
| CTA per tier | Different verbs by tier ("Start free", "Start 14-day trial", "Talk to sales") |
| Risk reversal | "No card required", "Cancel anytime", "30-day money back" near CTAs |
| Calculator | For usage or seat pricing: inputs for seats or volume, live total |
| Comparison table | Grouped features, tooltips for jargon, sticky header with tier names and CTAs on scroll |
| Proof | Logos and one quote per tier from a customer of that size |
| FAQ | Billing, upgrades, downgrades, overages, refunds, security, data export, contract terms |
| Enterprise | What triggers Enterprise (SSO, SLA, volume), "Contact sales" with a short form |

Pricing psychology tools (test, do not assume) [Practitioner consensus]:
- Anchoring: show the highest tier or the cost of the alternative first on desktop (left to right ordering matters less on mobile stacks).
- Decoy: a tier that makes the target tier look like the obvious value.
- Good, better, best: most buyers pick the middle when the middle is clearly framed.
- Charm pricing ($49 vs $50) matters less in B2B; round numbers can signal premium.

Pricing transparency for sales-led B2B is [Contested]: showing "from" prices filters unqualified demo requests and increases trust; hiding prices increases demo volume but wastes sales time. Test with downstream pipeline as the metric.

Price changes themselves are business decisions: CRO tests presentation and packaging; changes to price levels need human approval and `growth-orchestrator` involvement.

## 4. Signup flow

### 4.1 Rules
1. SSO first: "Continue with Google" and "Continue with Microsoft" for B2B; Apple for consumer apps.
2. Email signup fields: email and password only, or passwordless magic link. Ask name, company and role after account creation, inside onboarding.
3. Email verification: let users in first; verify within the session or before sensitive actions.
4. Show what happens next ("You will be inside the app in 30 seconds. No card required.").
5. Pre-fill from the landing page (email entered on the LP carries into signup).
6. Mobile: if the product is desktop-first, let mobile visitors sign up and send a "continue on desktop" email.
7. Bot and abuse protection: invisible challenge, disposable email blocking only when abuse is real.

### 4.2 Credit card upfront (opt-out trial) vs no card (opt-in trial)
| Option | Effect | Use when |
|--------|--------|----------|
| No card required (opt-in) | More trials, lower trial to paid rate | Product shows value fast without setup; broad top of funnel |
| Card required (opt-out) | Fewer trials, higher trial to paid rate, some involuntary conversions and refunds | High intent traffic, product value proven, clear cancellation |
| Freemium | Large free base, low free to paid, viral and SEO benefits | Network effects, low marginal cost |
| Reverse trial (full features for N days, then free plan) | Combines trial urgency with freemium safety | Feature-gated upgrades |

Compare options on paid accounts per visitor and 90-day revenue per visitor, not on trial count [Practitioner consensus]. Published benchmark ranges for trial to paid vary widely by source and method [Unverified]; use the project's own cohorts.

Subscription cancellation must be easy (state automatic renewal laws, EU consumer law). Do not test cancellation friction.

## 5. Onboarding to activation (website and in-app touchpoints CRO can influence)
- Welcome screen asks one question that personalizes the setup path (role or goal).
- Checklist with 3 to 5 steps that lead to the activation event; show progress.
- Templates or sample data so the user sees value before importing their own.
- Empty states that explain the next action.
- Lifecycle emails tied to behavior, not time only (owned by lifecycle team; CRO supplies copy and tests).
- Measure time to activation; reduce it.

## 6. Demo-led flows
See [Forms](forms-and-lead-capture.md) section 7. Key additions for SaaS:
- Route by company size and use case: small companies to self-serve or a recorded demo, target accounts to instant booking with an AE.
- Offer an interactive product tour (Navattic, Storylane, Arcade type tools) for visitors not ready for a call.
- Pricing page "Talk to sales" form should be 3 to 4 fields with instant scheduling.

## 7. SaaS homepage and feature pages
- Hero: outcome for a named segment, product UI visual, primary CTA plus secondary ("See how it works").
- Logo bar of customers similar to the target ICP.
- Sections by job to be done, not by feature list.
- Integrations section (logos) for tools-heavy categories.
- Security and compliance badges (SOC 2 Type II, ISO 27001, GDPR, HIPAA where real).
- Comparison pages ("X vs Y", "Alternatives to Y") are high intent landing pages for search and AI referrals; keep them factual and dated.

## 8. Experimentation in SaaS
- Signup volumes are often too low for website A/B tests on paid conversion. Use activation-weighted metrics, larger MDEs, longer tests, or the low traffic protocol in [Experimentation statistics](experimentation-statistics.md).
- Server-side feature flags (PostHog, GrowthBook, LaunchDarkly, Optimizely Feature Experimentation, Statsig now under Amplitude) let tests run in signup and onboarding without flicker.
- Pricing page tests: assign by user (logged in) or stable device ID; ensure the same visitor sees the same price across sessions and devices where possible; never show different prices for the same plan to logged-in users in ways that create unfairness or legal risk; disclose clearly.
- Measure trial to paid on cohorts that finished the trial window; do not call pricing tests on signups alone.

## 9. Templates

### 9.1 Pricing page audit summary
```
# Pricing page audit: <product> | Date | Data range
Motion: PLG | hybrid | sales-led
Visitor to signup by tier CTA (last 90 days):
Toggle default and annual share:
Top 5 objections (from chat, sales notes, surveys):
Findings (scored with audit-checklist section H):
Proposed changes: just do it | test | research
```

### 9.2 Activation definition proposal
```
Candidate events: event -> % of retained users who did it in first 7 days -> % of churned users who did it
Chosen activation event and window:
Expected baseline activation rate:
Instrumentation needed (hand to measurement):
```
