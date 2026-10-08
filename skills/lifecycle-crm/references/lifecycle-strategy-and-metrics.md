# Lifecycle Strategy, Metrics and Playbooks

The operating model for retention: how to frame the program, what to measure, how to prove incrementality, and the step by step plays for launch, optimize, scale, recover and migrate. Read this first on any new project.

## 1. The lifecycle stage model

Every profile sits in exactly one stage. Flows move people between stages; campaigns serve each stage with the right frequency.

### Ecommerce and DTC

| Stage | Definition (default, tune per project) | Primary job | Main flows |
|-------|----------------------------------------|-------------|-----------|
| Visitor (known) | Identified profile, no consent or no order | Capture consent | Pop up and form strategy ([List growth](list-growth.md)) |
| Subscriber | Consent for at least one channel, 0 orders | First order | Welcome, browse and cart abandonment |
| First time buyer | Exactly 1 order, inside expected reorder window | Second order (the most valuable conversion in DTC) | Post purchase education, cross sell, replenishment |
| Repeat buyer | 2 or more orders, last order inside 1.5x the median reorder interval | Frequency and AOV | Replenishment, loyalty, VIP, referral |
| At risk | Last order between 1.5x and 3x the median reorder interval | Reactivate before lapse | Winback stage 1, survey |
| Lapsed | Last order beyond 3x the median reorder interval | Win back or let go | Winback stage 2, sunset |
| Subscriber (recurring) | Active subscription | Retain, expand | Subscription lifecycle ([Replenishment and subscriptions](replenishment-and-subscriptions.md)) |
| Unengaged | No click, order or site activity in 180 days (email) | Protect deliverability | Re-engagement then sunset |

Median reorder interval comes from the project's own orders ([Cohort and LTV analysis](cohort-and-ltv-analysis.md) section 4). Never use a generic "90 days" when data exists.

### Lead gen, B2B SaaS, local services

| Stage | Definition | Primary job |
|-------|-----------|-------------|
| Lead | Form fill, demo request, download, trial start | Qualify and respond fast |
| MQL | Fit and engagement score above threshold | Hand off to sales with context |
| SQL or opportunity | Sales accepted | Support the deal (content, proof) |
| Trial or onboarding (SaaS) | Account created, not activated | Activation milestone |
| Customer | Paid | Adoption, expansion, referral, reviews |
| At risk | Usage drop, support friction, renewal near | Save |
| Churned | Cancelled or not renewed | Win back, learn |

Details in [B2B nurture and lead scoring](b2b-nurture-and-lead-scoring.md).

## 2. Lifecycle metric dictionary

Use the project's `ads-master/METRICS.md` definitions when they exist. Otherwise propose these and log the choice in `DECISIONS.md` via the orchestrator.

| Metric | Formula | Notes |
|--------|---------|-------|
| Repeat rate at N days | Customers with a 2nd order within N days of first order / customers in the first order cohort | N = 30, 45, 60, 90; only mature cohorts (first order date at least N days ago) |
| Second order rate | Same as repeat rate at the business's natural window | The north star for most DTC lifecycle programs |
| Median days to second order | Median of (2nd order date minus 1st order date) among repeaters | Use median, not mean; mean is dragged by the long tail |
| 12 month contribution LTV | Sum over cohort of (net revenue minus COGS, fulfillment, payment fees, returns) in 12 months / cohort size | Contribution, not revenue, for any paid media use |
| Purchase frequency (12 month) | Orders / unique customers in a 12 month cohort window | |
| Churn (subscription) | Cancelled subscriptions in month / active at start of month | Split voluntary vs involuntary (payment failure) |
| Attributed flow or campaign revenue | Revenue the ESP attributes inside its window (email open or click, SMS click) | Directional only; overlaps with ads and organic |
| Incremental lifecycle revenue | (Revenue per recipient in treatment minus control) x treated recipients | Only from holdouts; the number to report to finance |
| Revenue per recipient (RPR) | Attributed revenue / recipients | Use for comparing flows and messages |
| Placed order rate | Unique placed orders attributed / recipients | Better than open or click rate for decisions |
| Click rate | Unique clickers / delivered | Primary engagement metric since Apple MPP |
| Open rate | Unique opens / delivered | Not a decision metric: inflated by Apple MPP and AI prefetch, restricted by CNIL for French recipients |
| Spam complaint rate | Complaints / delivered (Gmail Postmaster spam rate is complaints / mail delivered to inbox) | Target under 0.1%; 0.3% sustained triggers Gmail rejections [Official, Google, 2024 to 2025] |
| Unsubscribe rate | Unsubscribes / delivered | Investigate per campaign above about 0.5% [Practitioner consensus] |
| Hard bounce rate | Hard bounces / sent | Investigate above about 0.5% per send; list source problem [Practitioner consensus] |
| Active list (email) | Subscribed profiles with click, order or site activity in 90 days | Use this, not total list size |
| Net list growth | (New consented subscribers minus unsubscribes, bounces, suppressions) / list at start | Monthly |
| Subscriber to customer rate | New subscribers who order within 30 days / new subscribers | List quality metric by capture source |
| Owned channel revenue share | Attributed email plus SMS revenue / total revenue | Directional; DTC programs commonly sit around 20% to 40% [Practitioner consensus]; a very high share can mean over attribution |
| SMS cost per message and ROI | Carrier plus ESP message cost; attributed revenue / message cost | Include carrier pass-through fees (rising through 2026) |

### Attribution windows inside ESPs

ESPs credit a conversion when a profile buys within a window after receiving, opening or clicking a message. Defaults differ by ESP and change over time [Unverified current defaults; check Settings > Attribution in Klaviyo, equivalent in others]. Rules:

1. Record the window in every report header (for example "Klaviyo, 5 day email click, Apple Privacy opens excluded").
2. Prefer click based windows for decisions. Open based credit counts machine opens.
3. Never add ESP attributed revenue to ad platform attributed revenue. Both overlap with each other and with organic.
4. Report incremental revenue from holdouts to finance and growth-orchestrator; report attributed revenue for operational comparisons only.

## 3. Proving incrementality (holdouts)

Attributed revenue answers "which message touched the buyer". Holdouts answer "would they have bought anyway". Top programs run both.

### 3.1 Holdout designs

| Design | How | Use for | Minimum |
|--------|-----|---------|---------|
| Global control group | Randomly exclude 5% to 10% of profiles from all marketing messages (transactional still sent) for a quarter | Total program incrementality | Large lists (over about 100k engaged profiles) |
| Flow holdout | Random split at flow entry: 80% to 90% get the flow, 10% to 20% get nothing; compare placed order rate and revenue per entrant over a fixed window | Cart, browse, welcome, winback, replenishment | Enough entrants to detect the lift (below) |
| Message level holdout | A/B split with a no-message branch for one step (for example email 3 of a welcome series) | Pruning steps, testing discounts | Same |
| Offer holdout | Same message, discount vs no discount | Discount economics | Same; read margin, not revenue |
| Geo or time holdout | Pause a campaign stream in matched regions or weeks | When randomization is impossible (SMS short codes, some platforms) | Several matched units; weaker evidence |

Klaviyo flows support random sample splits and A/B tests inside flows; Braze Canvas has control groups at the Canvas and step level; Iterable and Customer.io support holdout or control groups in journeys [Official, product docs; verify current UI names].

### 3.2 Sample size quick math

For a conversion metric with baseline rate p and an absolute difference d you want to detect (80% power, 5% two sided alpha):

```
n per group ~= 16 x p x (1 - p) / d^2
```

Worked example: cart abandonment flow, placed order rate 4% in the holdout, you want to detect a 1 point lift (4% to 5%): n = 16 x 0.04 x 0.96 / 0.0001 = 6,144 entrants per group. With a 90/10 split the holdout needs 6,144 entrants, so total entrants about 61,000. At 2,000 entrants per week that is about 30 weeks: too long. Options: 70/30 split (about 20,500 total entrants, about 10 weeks), test a bigger change, or pool similar flows.

### 3.3 Reading a holdout

```
Incremental orders = (orders per entrant in treatment - orders per entrant in control) x treatment entrants
Incremental revenue = (revenue per entrant treatment - revenue per entrant control) x treatment entrants
Incremental contribution = incremental revenue x contribution margin - message cost - incremental discount cost
Incrementality ratio = incremental revenue / attributed revenue for the same flow and window
```

Typical findings [Practitioner consensus, varies widely]: cart and checkout abandonment flows show real but much smaller incremental revenue than attributed revenue; welcome series for non buyers usually show strong incrementality; post purchase upsell to recent buyers often shows low incrementality; discounts in flows often move timing rather than create orders. Measure your own; do not assume.

Log every holdout in `ads-master/EXPERIMENTS.md` and share the incrementality ratio with `measurement` (it feeds MMM priors and the owned channel line in blended reports).

## 4. Program economics

```
Value of a subscriber (90 day) = subscriber to customer rate (90 day) x first order contribution + repeat contribution in window
Value of list growth = new subscribers per month x value of a subscriber
Retention lift value = cohort size x (new repeat rate - old repeat rate) x contribution per repeat order
LTV uplift from second order = (LTV of 2+ order customers - LTV of 1 order customers) x additional second orders
SMS message ROI = (incremental revenue x margin) / (ESP message fees + carrier fees + incentive cost)
```

Worked example (illustrative numbers, replace with project data): 4,000 first time buyers per month, 90 day repeat rate 18%, contribution per repeat order 22 EUR. A post purchase and replenishment rebuild lifts 90 day repeat rate to 21% (validated by a flow holdout). Monthly value = 4,000 x 0.03 x 22 = 2,640 EUR in the first repeat order alone, plus the higher LTV of customers who reach order two. Report it with the experiment ID and interval.

## 5. Strategy framing: what to fix first

Order of operations for almost every program:

1. Consent and compliance (you cannot optimize a list you are not allowed to mail).
2. Deliverability and authentication (mail that does not arrive cannot convert).
3. Measurement: events (Viewed Product, Added to Cart, Started Checkout, Placed Order, Fulfilled Order) flowing, revenue mapped, holdout plan.
4. Core flows live and correct (welcome, cart and checkout, browse, post purchase, winback, sunset).
5. Second order engine: post purchase education, replenishment timed to consumption, cross sell by product affinity.
6. Segmented campaigns with engagement based frequency.
7. List growth quality (capture rate and subscriber to customer rate).
8. SMS, WhatsApp, push where consent and economics support them.
9. Loyalty, referral, subscriptions, reviews.
10. Paid media integration (suppression, value based audiences, LTV values).
11. Predictive and AI personalization, with holdouts.

## 6. Playbooks

### Play 1: Launch a lifecycle program (new ESP or no program), 90 days

| Week | Actions | Exit criteria |
|------|---------|---------------|
| 0 | Intake, consent audit, data audit (events, catalog, order sync), deliverability DNS check | Consent sources documented; SPF, DKIM, DMARC aligned on a branded sending domain |
| 1 to 2 | Build welcome, checkout and cart abandonment, browse abandonment specs; draft copy using PRODUCT_FACTS.md; compliance review | Flow specs approved |
| 2 to 3 | Create flows as Draft or Manual (G2), QA with test profiles, set holdouts | QA checklist passed |
| 3 | Human approves activation (G3); warm sending to engaged segments only | Flows live; spam rate under 0.1% |
| 4 to 6 | Post purchase (first time buyer vs repeat), winback, sunset; campaign calendar to engaged tiers | All core flows live |
| 6 to 8 | List growth plan with storefront-ux (form UI) and offer-strategy (incentive) | Capture rate baseline measured |
| 8 to 12 | Replenishment, cross sell, review request; first holdout readouts; SMS or WhatsApp if consented | First incrementality numbers in EXPERIMENTS.md |

### Play 2: Audit and optimize a running program

1. Run the [Audit checklist](audit-checklist.md). Score each section.
2. Pull 90 days of flow and campaign data (reporting API or export) plus 12 months of orders for cohorts.
3. Rank flows by entrants x (top decile RPR minus current RPR) to size the gap; benchmarks only as a sanity check.
4. Fix critical items first (consent, deliverability, broken triggers, double sends, discount leakage).
5. Rebuild the top 3 flows by value at stake; add holdouts.
6. Move campaigns to engagement tiers; cut sends to unengaged.
7. Re-measure at 30 and 60 days against the pre period and the holdout.

### Play 3: Scale (list over about 250k, or growth stage revenue)

- Segment campaigns by lifecycle stage and product affinity; 3 to 5 versions per send rather than one blast.
- Add predictive segments (predicted CLV, churn risk, expected next order date) when the ESP's data requirements are met ([Segmentation](segmentation-and-personalization.md)).
- Introduce a global control group and quarterly incrementality readouts.
- Dedicated sending IP only when volume justifies it (commonly cited as consistent volume in the hundreds of thousands per month) and with a warmup plan [Practitioner consensus].
- Add SMS or WhatsApp as a second channel with channel preference logic (send to SMS only if not engaged by email in X hours).
- Sync value based audiences and suppressions to paid media weekly ([Lifecycle and paid media](lifecycle-and-paid-media.md)).

### Play 4: Recover from a deliverability crash

Symptoms: open and click rates fall sharply across providers or at one provider, Gmail Postmaster spam rate spikes, bounces with 4.7.x or 5.7.x codes, Outlook 550 5.7.515.

1. Stop: pause campaigns to anyone outside the 30 day engaged tier. Keep transactional and high intent flows (cart, checkout, post purchase).
2. Diagnose with [Email deliverability](email-deliverability.md) section 9.
3. Fix authentication or unsubscribe header failures first (hard requirements).
4. Rebuild reputation: send only to 30 day clickers and buyers for 1 to 2 weeks, then widen by tier while spam rate stays under 0.1%.
5. Clean: suppress hard bounces, role addresses from bad sources, and profiles unengaged beyond 180 days.
6. Write an incident row in `ads-master/INCIDENTS.md` and a journal entry.

### Play 5: Revenue from lifecycle dropped

1. Check measurement first: did the order sync, event names, attribution window or Apple Privacy open exclusion change?
2. Check volume: flow entrants down (traffic drop, form broken, trigger broken) vs RPR down (offer, content, deliverability).
3. Check deliverability by provider (Gmail, Yahoo, Outlook, Apple).
4. Check for seasonality and promo calendar (compare same weeks last year).
5. Check catalog and inventory (back in stock, out of stock items in abandonment emails).
6. Fix the largest gap; write a journal entry.

### Play 6: Migrate ESP

1. Export: profiles with consent fields (channel, status, timestamp, source, method, jurisdiction), suppressions (unsubscribes, bounces, complaints), events if possible, templates, flow logic diagrams.
2. Never import suppressed or unconsented profiles as subscribed. Carry suppressions first.
3. Authenticate the new sending domain; warm up by engagement tier.
4. Rebuild flows from specs (do not copy broken logic); run both ESPs in parallel only with strict exclusion to prevent double sends.
5. Recreate SMS keywords, short codes or 10DLC registration; WhatsApp numbers and templates move with the WABA, not the ESP account [Practitioner consensus; verify with provider].
6. Turkey: keep İYS integration live through the cutover; confirm the new provider is an authorized integrator path.
7. Verify revenue attribution and holdouts in the new tool before switching off the old one.

### Play 7: Seasonal peak (BFCM, Ramadan, 11.11, Singles Day, Christmas)

- Build the list 6 to 10 weeks before (early access lists, wishlist and back in stock capture).
- Ramp volume gradually to engaged tiers; avoid sudden 3x sends to the full list (complaint and throttling risk).
- Pre-schedule SMS within quiet hours per recipient time zone.
- Coordinate offers with offer-strategy; suppress recent full price buyers from deep discounts when possible.
- After peak: welcome and post purchase flows for the new cohort, then winback at the right interval. Peak cohorts often repeat less; measure them separately.

### Play 8: Discount detox

When most flow and campaign revenue rides on discounts:

1. Measure margin, not revenue, per flow.
2. Run offer holdouts (discount vs no discount, or discount vs value add like free gift or early access).
3. Replace blanket codes with unique single use codes and expiry.
4. Move discounts later in sequences (message 2 or 3) and only for non converters.
5. Use acquisition investment (METRICS.md) to account for discount cost in first order economics with offer-strategy.

## 7. Reporting template (weekly)

```
# Lifecycle weekly: <brand> <YYYY-MM-DD>
Data: <ESP> flows and campaigns <date range>; orders <source> <date range>; attribution <window>
FACTS
- Owned revenue (attributed): <x> (<+/-%> vs last week, vs same week LY)
- Flow RPR top 5 and bottom 5; campaign RPR by tier
- Deliverability: Gmail spam rate <x>, Yahoo complaint <x>, bounces <x>, unsub <x>
- List: net growth <x>, active list <x>, SMS and WhatsApp consented <x>
- Cohorts: repeat rate at 30/60/90 days for latest mature cohorts vs prior
INTERPRETATION
RECOMMENDATION (each with gate level and approval needed)
Handoffs requested
```
