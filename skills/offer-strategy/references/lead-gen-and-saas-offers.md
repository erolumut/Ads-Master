# Lead Gen, Services and SaaS Offers

> In lead gen the offer is the first step you ask for, not the product. Judge it on qualified pipeline per euro, not on form fills. In SaaS the offer is the entry model (trial, freemium, reverse trial, demo), the packaging and the billing terms.

## 1. Lead gen offer ladder

Order offers by commitment. Match the step to the traffic's awareness and the sales motion.

| Rung | Offer | Commitment | Lead quality | Use for |
|------|-------|-----------|--------------|---------|
| 1 | Content lead magnet (guide, checklist, template) | Very low | Low | Cold audiences, list growth; needs nurture |
| 2 | Tool or calculator (price, ROI, savings, sizing) | Low | Medium; self-qualifying inputs | Solution aware, comparison stage |
| 3 | Quiz or assessment with a personal result | Low | Medium; zero-party data | Ecommerce routing, services triage |
| 4 | Webinar, workshop, live demo for groups | Medium | Medium | B2B education |
| 5 | Sample, swatch kit, trial pack | Medium (shipping details) | Medium to high | Physical products with fit risk |
| 6 | Free audit, assessment, inspection, consultation | High | High if qualified | Services, agencies, B2B |
| 7 | Quote, proposal, booking | High | High | Bottom of funnel |
| 8 | Paid pilot, paid assessment, deposit | Highest | Highest | Complex B2B, high ticket services |

Rules:
1. Lead offer value must be specific: "Get your roof inspected with photos within 48 hours" beats "Free consultation".
2. Qualify through the offer: an ROI calculator asks for size and spend; an audit asks for the URL and budget. `cro` designs the form; offer-strategy decides what is offered and to whom.
3. Never pay for leads with generic gift cards unless sales confirms quality; incentivized leads often fail qualification [Practitioner consensus].
4. Every lead offer needs a next step offer (rung up) defined before launch.

## 2. Lead offer economics

```
Cost per qualified lead (CPQL) = media + offer fulfillment cost (sample, audit hours) / qualified leads
Value per lead = lead to customer rate x average first year contribution per customer
Max CPQL = value per lead / required LTV to CAC ratio
Offer fulfillment cost per lead = hours to deliver x loaded hourly cost (audits, consultations) + physical cost (samples)
```

Worked example (illustrative): free home energy audit. Media EUR 12,000 per month, 200 audit requests, 70% qualified (140), audit cost EUR 45 each (EUR 6,300 on 140 audits), 25% of qualified audits close, first year contribution per job EUR 1,400.
- CPQL = (12,000 + 6,300) / 140 = EUR 130.71.
- Customers = 35; acquisition cost per customer = 18,300 / 35 = EUR 522.86; contribution per customer EUR 1,400; ratio 2.7.
- Option tested: replace the free audit with a EUR 49 audit credited against the job. Expected effects: fewer requests, higher close rate. Model both before the test; judge on contribution per euro of media plus fulfillment.

## 3. Quiz and assessment offers
- Use when the product needs a choice (shade, size, routine, plan) or when the service needs triage.
- Every result maps to a specific offer (product, bundle or plan) with a reason.
- Collect only data you use; zero-party data consent goes through `lifecycle-crm` and `measurement`.
- Measure: completion rate, result to purchase or booking rate, AOV vs non-quiz orders, return rate (quizzes should lower returns on fit-driven categories).
- Benchmarks from quiz vendors are self-reported; compare against your own non-quiz traffic [Unverified].

## 4. Local services offers

| Offer | When | Economics note |
|-------|------|----------------|
| Fixed price for a defined job | Standard jobs (boiler service, drain clearing) | Margin protection by scope |
| Free estimate vs paid diagnostic credited to the job | High no-show or tire-kicker rate | Paid diagnostics improve quality; test |
| Same day or next day guarantee | Urgent categories | Capacity planning |
| Satisfaction guarantee on first job | Trust barrier | Redo cost |
| Membership or maintenance plan | Recurring needs | Smooths seasonality; strong LTV |
| Seasonal tune-up promotions | Off-peak capacity | Fill idle crews; avoid discounting peak |
| Financing for high ticket jobs | Replacements, renovations | Provider fees; credit law |

## 5. SaaS entry models

| Model | Definition | Best for | Watch |
|-------|-----------|----------|-------|
| Opt-in free trial (no card) | Time limited full access, no payment details | High volume self-serve, low touch | Lower trial to paid, more signups |
| Opt-out free trial (card required) | Card upfront, converts unless cancelled | Strong intent traffic, clear value fast | Fewer signups; consent and reminder rules |
| Freemium | Free plan forever with limits | Network effects, viral loops, low marginal cost | Low free to paid; cost of free users |
| Reverse trial | Full premium trial, then drop to free plan | Products with a useful free tier and premium value that is felt in days | Needs a good free tier |
| Demo led | Sales call before access | High ACV, complex onboarding | Speed to demo matters |
| Paid pilot | Short paid engagement | Enterprise | Procurement time |
| Usage or credit based start | Pay as you go, credits bundle | AI products, APIs | Bill shock; credit expiry rules |

Benchmarks (definitions vary; compare like with like):

| Metric | Value | Source, date | Caveat |
|--------|-------|--------------|--------|
| Median free to paid conversion across models | 8% | ChartMogul and ProductLed, 200 B2B products [Study, 2025] | Few products sit at the median |
| Entry model share | Free trial 57%, freemium 26%, reverse trial 7% of products | Same | Small reverse trial sample |
| Reverse trial "good" and "great" | 4% to 6% good, 8% to 12% great | Same | Not significant vs other models |
| Opt-out vs opt-in trial to paid | About 49% vs about 18% | First Page Sage, 86 companies, data to late 2025 [Study, 2025] | Agency dataset; widely recycled |
| Freemium organic signup to paid | About 2.6% | Same | Definitions differ |

## 6. SaaS packaging and pricing (2026 state)

| Trend | Evidence | Label |
|-------|----------|-------|
| Hybrid pricing (base plus usage or credits) is the most common structure | Growth Unhinged 2026 survey of 230 companies (April to May 2026): hybrid 37%, up from 25% a year earlier on that measure; investors favor hybrid (35%), outcome based (26%), usage (24%) | [Study, 2026] |
| Seats survive as one component | CRV: over 80% of SaaS still use seats as one component; seats as the only value metric about 8% | [Study, 2026, secondary] |
| Credits are the AI pricing workhorse | Metronome catalog of 50+ AI companies: single-track models are a minority; credits map compute cost, bundle resources and gate premium access | [Study, 2026, vendor] |
| Vendors are cutting free AI credits and pricing agents as SKUs | PricingSaaS Q2 2026 trends report | [Study, 2026, vendor] |
| Billing infrastructure consolidation | Stripe completed its Metronome acquisition on 2026-01-14 | [Unverified, secondary] |
| Outcome based pricing remains niche | ICONIQ and Gartner figures relayed secondhand | [Unverified] |

Packaging procedure:
1. Choose the value metric (seats, usage, outcomes, records, locations) that grows with customer value and is easy to predict.
2. Build 3 plans plus enterprise. The middle plan carries the features most buyers need; the top plan carries scale, security and admin.
3. Put AI or usage heavy features on credits with a monthly included allowance and clear overage pricing; show usage in product to avoid bill shock.
4. Annual discount: 15% to 20% ("2 months free" is 16.7%) is common practice [Practitioner consensus]. Check it with the churn math below.
5. Grandfather existing customers or give long notice on price increases; publish the change log.
6. Hand pricing page layout to `cro` and `storefront-ux` (for commerce) and product changes to the human.

## 7. Annual vs monthly economics (worked example)

Monthly plan EUR 50. Annual plan at "2 months free" = EUR 500 per year (16.7% off). Expected paid months in the first 12 months on monthly billing with monthly churn c: `E = (1 - (1 - c)^12) / c`.

| Monthly churn | Expected paid months (monthly plan) | Revenue in year 1 (monthly) | Annual plan revenue |
|---------------|-------------------------------------|-----------------------------|---------------------|
| 2% | 10.76 | 538 | 500 |
| 3% | 10.21 | 510 | 500 |
| 3.4% | 9.99 | 500 | 500 |
| 5% | 9.19 | 460 | 500 |
| 8% | 7.90 | 395 | 500 |

Reading: at monthly churn above about 3.4%, the annual plan earns more in year 1 even before counting cash upfront and lower churn at renewal. At very low churn, a smaller annual discount (10% to 12%) may be enough. Test the annual discount size on the pricing page with conversion to annual and year 1 revenue per signup as metrics.

## 8. SaaS offer levers beyond price

| Lever | Example | Use |
|-------|---------|-----|
| Onboarding included | Setup call, data migration | Effort barrier |
| Trial extension on request | +7 days for active trials | Rescue slow evaluators |
| Usage credit at signup | First 1,000 credits free | AI and API products |
| Founding customer pricing | Locked price for 24 months | Launches; must be honored |
| Multi-year discount | Discount for 2 or 3 year term | Enterprise; churn protection |
| Nonprofit, education, startup programs | Discounted plans with eligibility | Market expansion |
| Exit and data portability promise | Export anytime | Switching risk |

## 9. App offers (with `mobile-app-growth`)
- Intro offers (free trial, pay as you go, pay up front) and promo offers for lapsed subscribers are configured in App Store Connect and Google Play Console; eligibility rules differ by store.
- Web checkout for app subscriptions (where allowed by store rules and court rulings in a market) changes fees and therefore allowable discounts; coordinate with `mobile-app-growth` before designing web-only offers [Unverified, rules vary by market].
- Paywall offer tests run in the app; offer-strategy provides the economics (trial length, intro price, annual discount) and the guardrails.

## 10. Lead gen and SaaS offer brief template

```
Offer ID:
Motion: self-serve | sales assisted | demo led | local service
Entry offer (rung):              Next step offer:
Who it is for (segment, awareness level):
What exactly they get, by when:
Qualification built into the offer:
Fulfillment cost per lead or trial:
Economics: CPQL target, lead to customer rate, value per lead, max CPQL; or trial to paid, annual mix, year 1 revenue per signup
Guardrails: SQL rate, show rate, refund or chargeback rate, support load
Legal: trial auto-renew disclosures, reminders, cancellation path (see subscriptions-and-repeat-offers.md section 6)
Owners: cro (page and form), lifecycle-crm (nurture), linkedin-ads or google-ads (traffic)
```
