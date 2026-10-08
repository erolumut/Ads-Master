# Measurement Strategy and KPI Tree

Use this module to write the measurement plan: what the business optimizes, which conversions exist, how they are valued, where truth lives and how the different measurement methods are combined. Everything else in this skill implements the plan.

## 1. The measurement stack (layers)

| Layer | Question it answers | Components | Failure looks like |
|-------|--------------------|------------|--------------------|
| 1. Definition | What counts and what is it worth? | KPI tree, conversion definitions, value rules, MEASUREMENT.md | Six platforms each count a different "conversion" |
| 2. Collection | Did we observe it? | Data layer, GTM, gtag, pixels, Shopify Web Pixels, server events, SDKs | GA4 captures 60% of orders |
| 3. Consent and identity | Are we allowed to use it, and can we match it? | CMP, consent mode, hashed identifiers, click IDs, first-party cookies | Conversions vanish in EEA, low match rates |
| 4. Transport | Did each platform receive it once? | CAPIs, enhanced conversions, Data Manager, offline uploads, sGTM | Double counting, missing server events |
| 5. Storage and modeling | Can we analyze it? | GA4, BigQuery, warehouse, CRM | No raw data, 2-month retention |
| 6. Truth and decision | What caused it and where should money go? | Reconciliation, attribution, incrementality, MMM, dashboards | Budget moves on platform ROAS alone |

Work bottom up when fixing (a value rule is useless if collection is broken) and top down when planning (define before you collect).

## 2. KPI trees by business model

Write the tree in MEASUREMENT.md. Each leaf must be measurable in a named system.

### Ecommerce

```
Contribution margin after marketing (North Star for profit-led brands)
  = Revenue x contribution margin % (before marketing) minus marketing spend
  Revenue
    New customer revenue = new customers x first order AOV
      New customers = sessions from new users x new user CVR      (GA4, backend)
      nCAC = acquisition spend / new customers                     (backend + spend)
    Returning customer revenue = active customers x purchase frequency x AOV  (backend, email/CRM)
  Contribution margin %
    Gross margin (COGS), shipping, payment fees, returns, discounts  (finance)
  Marketing spend by channel                                         (platforms)
Guardrails: MER, aMER, refund rate, discount depth, stock-outs
```

### Lead gen (services, finance, education, B2B without product usage)

```
Gross profit from closed deals
  = closed deals x average deal gross profit
  Closed deals = qualified leads x close rate                     (CRM)
    Qualified leads = leads x qualification rate                   (CRM)
      Leads = sessions x lead CVR                                  (GA4, forms, calls)
  Cost per qualified lead, cost per closed deal, pipeline ROAS     (CRM + spend)
Guardrails: spam rate, speed to lead, show rate, lead to SQL time
```

### B2B SaaS

```
New ARR (or net new MRR) at target CAC payback
  New ARR = closed won deals x ARR per deal                        (CRM, billing)
    Opportunities x win rate
      SQLs x SQL to opportunity rate
        MQLs or PQLs (trial activated, demo booked)                (product analytics, CRM)
          Signups or demo requests                                 (GA4, product events)
  CAC payback months = CAC / (ARR per customer / 12 x gross margin %)
Guardrails: activation rate, sales cycle length, ICP fit share
```

### Local services

```
Booked jobs revenue
  Booked jobs = (calls + forms + bookings) x booking rate          (call tracking, CRM or job software)
  Average job value                                                (job software)
Guardrails: answered call rate, missed call rate, service area fit
```

### App

```
Cohort revenue at day 30, 90, 365 (or subscriptions)
  Installs x activation rate x payer conversion x ARPPU            (MMP or Firebase, stores)
  pLTV per install                                                 (model)
Guardrails: ATT opt-in rate, SKAN or AdAttributionKit null rate, refund rate
```

### Marketplace or publisher

```
Marketplace: GMV x take rate, split supply side (listings, active sellers) and demand side (buyers, orders)
Publisher: subscriptions x ARPU, plus ad revenue = sessions x pages x RPM
Guardrails: liquidity (fill rate), churn, ad blocker share
```

## 3. Conversion definitions

Every conversion in MEASUREMENT.md gets one row with all of these fields. If a field cannot be filled, the conversion is not ready for bidding.

| Field | Rule | Example |
|-------|------|---------|
| Name | Same name in every system where possible; GA4 uses snake_case recommended events | purchase |
| Business definition | What happened in the business, not in the browser | Paid order, excluding test and fully discounted orders |
| Trigger | Exact technical trigger | Shopify checkout_completed (browser) and orders/paid webhook (server) |
| Dedup key | Unique ID shared by every copy of the event | event_id = order ID; GA4 transaction_id = order ID |
| Value rule | Formula and currency | Revenue excluding tax and shipping, store currency; or gross profit |
| Count | Every or once per click or session | Every (purchase); one (lead) |
| Primary or secondary | Per platform | Primary on Google Ads Purchase goal and Meta optimization event |
| Consent behavior | What happens when denied | Cookieless ping to Google (advanced mode); no Meta pixel; server event sent only with ad consent |
| Owner | Who fixes it | Measurement agent with dev team |
| QA test | How to prove it works | Test order, Tag Assistant, Meta Test Events, BigQuery row |

### Primary versus secondary

| Platform | Mechanism | Rule |
|----------|-----------|------|
| Google Ads | Conversion action "Primary" (used for bidding when in the campaign's goal) or "Secondary" (observation) | One primary action per goal per campaign; never a GA4 key event and a Google Ads tag for the same conversion both primary |
| Meta | Ad set optimization event plus attribution setting | One optimization event per ad set; other events are reporting only |
| TikTok | Optimization event per ad group | Same as Meta |
| Microsoft | Conversion goals with "Include in conversions" | Mirror Google |
| LinkedIn | Conversions attached to campaigns | Attach only the conversion the campaign optimizes plus reporting conversions as needed |
| GA4 | Key events | Mark only events that represent business outcomes or the documented proxy; a key event is not automatically a Google Ads primary conversion |

### Signal density: choosing the optimization event

Pick the deepest event that has enough volume for the bidding system:

| Platform | Volume the system needs | Source and label |
|----------|-------------------------|------------------|
| Meta | About 50 optimization events per ad set in a 7-day period to exit learning | Meta Business Help Center, learning phase [Official, long standing] |
| Google Ads tCPA or tROAS | 15 to 30 or more conversions in 30 days per campaign or portfolio; more is better for value bidding | Google guidance has varied by product; operators target 30+ [Practitioner consensus] |
| TikTok | About 50 conversions per ad group in 7 days recommended | TikTok Ads help [Official, verify current] |
| LinkedIn, Microsoft | Lower volumes work with manual or max conversions; use portfolios | [Practitioner consensus] |

Proxy ladder when the deep event is too thin (ecommerce): purchase -> begin_checkout -> add_to_cart -> view_item (do not go below add_to_cart). Lead gen: closed won -> opportunity -> SQL -> qualified lead (form plus validation) -> raw lead. Document the proxy to outcome rate monthly; if it drifts more than 25% the proxy is broken.

## 4. Values

| Value type | When | How | Risk |
|-----------|------|-----|------|
| Revenue | Starter, uniform margins | Order value excluding tax and shipping | Optimizes to low margin items |
| Gross profit | Margins vary by SKU or category | Revenue minus COGS, server-side lookup or Google cart data with COGS | Margin data leaking to the browser |
| Contribution margin | Shipping, fees, returns vary a lot | Gross profit minus shipping, payment, returns allowance | Complex, needs finance sign off |
| New customer premium | Acquisition is the goal | Add value for new customers (Google NCA "value new customers higher", custom value) | Overpaying if LTV is overestimated |
| Predicted LTV | Subscription, high repeat | pLTV at a fixed horizon (90 or 180 days) sent at conversion or via adjustment | Model error, volatility |
| Lead stage value | Lead gen, SaaS | value = P(close given stage) x average gross profit per deal | Stale probabilities |

Details and formulas: [Value and profit optimization](value-and-profit-optimization.md).

## 5. Sources of truth hierarchy

| Question | Source of truth | Secondary | Never use as truth |
|----------|-----------------|-----------|--------------------|
| How much did we sell? | Backend (Shopify, ERP, Stripe) | GA4 | Ad platform totals |
| Was the lead good? | CRM stage and closed won | Call outcome systems | Form fills |
| Which channel touched the user? | GA4 or warehouse with UTMs and click IDs | Platform reports | Survey alone |
| Did ads cause the sale? | Experiments (lift, geo, holdout) | MMM calibrated to experiments | Platform attribution |
| Where should the next dollar go? | MMM response curves plus experiment calibration plus marginal CPA by channel | Platform marginal reports | Average ROAS |
| What did the customer say? | Post-purchase survey | Sales call notes | Nothing else captures this |

## 6. Triangulation

No single method is right. Combine them on purpose:

| Method | Strength | Weakness | Use it for | Cadence |
|--------|----------|----------|-----------|---------|
| Platform attribution | Fast, granular, feeds bidding | Self-graded, overlapping credit, modeled | In-platform optimization (ad, ad set, keyword) | Daily |
| GA4 or warehouse attribution | One ruler across channels | Misses views and blocked users, last touch bias for some channels | Cross-channel trends, landing pages, funnel | Weekly |
| Post-purchase survey | Captures dark social, podcasts, word of mouth, TV | Recall bias, low response for some segments | Upper funnel and offline channel credit | Weekly, monthly |
| Incrementality tests | Causal | Expensive, slow, point in time | Calibrating channels, big budget calls | Quarterly per major channel |
| MMM | Covers all channels including offline, response curves | Needs history and variation, uncertainty | Annual and quarterly allocation | Monthly to quarterly refresh |
| Blended metrics (MER, aMER, nCAC) | Cannot be gamed by attribution | Cannot assign credit | Health and guardrails | Daily to weekly |

### Incrementality factor (the bridge)

```
Incrementality factor (IF) = incremental conversions measured in the test / conversions the platform attributed in the same cells and period
Calibrated CPA  = platform CPA / IF
Calibrated ROAS = platform ROAS x IF
```

Example: Meta reports 400 purchases in the test regions over 4 weeks; the geo test shows 248 incremental purchases. IF = 0.62. Platform ROAS 3.1 becomes calibrated ROAS 1.92. If breakeven ROAS is 2.2, the channel is below breakeven at the margin even though the platform shows 3.1. Record IF in MEASUREMENT.md (Incrementality evidence) with date and confidence; refresh at least every 6 to 12 months or after big changes (new creative strategy, new campaign type, major attribution change).

Use the IF only for the scope it was measured on (channel, campaign type, objective, region). Do not apply a Meta Advantage+ sales test result to a lead gen campaign.

## 7. Measurement maturity levels

| Level | Description | Typical tier | Next step |
|-------|-------------|--------------|-----------|
| 0 | No reliable tracking; platform pixels only | Starter | Measurement plan, GA4, primary conversions with dedup |
| 1 | GA4 and pixels firing; not reconciled | Starter, Growth | Reconcile to backend, fix gaps |
| 2 | Reconciled, browser and server events, consent mode | Growth | Values, offline loop, survey |
| 3 | Profit or LTV values, offline stages, monitoring | Growth, Scale | First incrementality tests |
| 4 | Incrementality factors per major channel, BigQuery models | Scale | MMM, test calendar |
| 5 | Calibrated MMM in planning, always-on experiments, data contracts | Enterprise | Continuous improvement |

## 8. Post-purchase and self-reported attribution design

- Ask on the order confirmation page or in the first email: "How did you first hear about us?" Single choice, randomized order, include "Friend or family", "Podcast", "Search engine", "AI assistant (ChatGPT, Gemini, other)", "TikTok", "Instagram", "Facebook", "YouTube", "Influencer or creator", "TV or streaming", "Other (write in)".
- Add a second question only if needed ("What made you buy today?").
- Report response rate and responses by platform-attributed channel. Use survey share vs platform share to spot channels that platforms under or over credit (for example TikTok and podcasts are often under credited by click based tools [Practitioner consensus]).
- For lead gen, add "How did you hear about us?" as a required CRM field captured by sales, plus the hidden field click IDs.
- Never treat survey share as incrementality. It measures memory, not cause.

## 9. Writing the measurement plan (template)

```
# Measurement plan: <project> (YYYY-MM-DD)
1. Business goal and North Star:
2. KPI tree (section 2 format):
3. Conversion definitions table (section 3 fields)
4. Values and currency; refund and cancellation handling
5. Sources of truth and reconciliation method (section 5)
6. Data flows (text diagram):
   Browser: CMP -> consent default -> GTM -> GA4, Google Ads, Meta pixel (event_id) ...
   Server: order webhook -> event sender -> Meta CAPI, TikTok Events API, GA4 MP (same event_id)
   CRM: form -> hidden click IDs -> CRM -> stage changes -> Data Manager or native connector
7. Consent design by region
8. Platform matrix: platform | events | primary | values | dedup | attribution setting
9. Monitoring and alerts
10. Calibration plan (tests and MMM)
11. Open risks
```

## 10. Worked example: ecommerce, Growth tier

Facts: Shopify store, $40k per month spend (Meta $25k, Google $13k, TikTok $2k), AOV $85, gross margin 55%, contribution margin before marketing 38%, ships to US and EU.

1. North Star: contribution margin after marketing. Guardrails: aMER at or above 1.8 (computed from margin: new customer first order must recover about half of acquisition cost given 2.1 orders per customer in 12 months, per backend cohort data).
2. Conversions: purchase (primary on all three), add_to_cart and begin_checkout (secondary), subscribe newsletter (secondary, not a key event).
3. Dedup: event_id = Shopify order ID on browser and server for Meta and TikTok; GA4 transaction_id = order ID.
4. Value: revenue excluding tax and shipping now; move to gross profit values via server-side lookup in quarter 2 because margins range from 30% to 70%.
5. Consent: advanced consent mode in EEA with a certified CMP; US: honor GPC and "Do not sell or share" for Meta and TikTok.
6. Truth: Shopify orders; monthly reconciliation; post-purchase survey through a survey app.
7. Calibration: Meta geo holdout in month 3 (largest spend); Google brand search holdout test in month 4.
