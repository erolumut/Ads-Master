# Subscriptions and Repeat Offers

> A subscription is an offer: a price, a cadence, a commitment and a way out. Offer-strategy owns its economics and terms; `lifecycle-crm` owns the flows that deliver it (reminders, winback, skip and swap prompts); `storefront-ux` owns how it appears on the PDP and in the account.

## 1. Subscription offer models

| Model | Mechanics | Fits | Economics note |
|-------|-----------|------|----------------|
| Subscribe and save | Ongoing discount (often 10% to 15%) for recurring delivery | Consumables with predictable use | Per order contribution drops; frequency and retention must pay for it |
| First order subscription incentive | Bigger discount on the first subscription order (for example 25% first, 10% ongoing) | Acquisition of subscribers | Watch first order churn (cancel after the first box) |
| Prepaid plans | Pay 3, 6 or 12 months upfront, often at a deeper discount | High retention products, gifting | Cash upfront, lower churn; refund obligations if cancelled; fulfillment liability |
| Build a box or curated box | Customer picks items each cycle | Food, beauty, pet | Higher engagement, higher ops cost |
| Membership (paid loyalty) | Fee for perks (free shipping, member prices, early access) | Frequent buyers, wide catalogs | Member price display rules in the UK from 2026-04-06 (show ordinary price next to loyalty price) [Official, 2026-04] |
| Replenishment reminder (no commitment) | Reminder at the expected run-out date | Brands avoiding subscription friction | No discount cost; lower capture; delivered by `lifecycle-crm` |
| Service plans | Maintenance plans (HVAC, lawn, cleaning) | Local services | Smooths demand; strong LTV |
| SaaS plans | Monthly and annual billing | Software | See [Lead gen and SaaS offers](lead-gen-and-saas-offers.md) |
| App subscriptions | Store billed plans with intro offers | Apps | Owned with `mobile-app-growth` |

## 2. Subscriber economics (worked example)

Inputs (illustrative, EUR, net of VAT): one-time price 30 with CM2 13.15; subscribe and save at 15% off (25.50) gives CM2 8.74 per order. A one-time buyer averages 1.4 orders in 12 months, so 12 month contribution is 13.15 x 1.4 = 18.41.

Expected subscriber orders in 12 monthly cycles with per-cycle retention q: `E = (1 - q^12) / (1 - q)`.

| Per-cycle retention q | Expected orders (12 cycles) | 12 month contribution | vs one-time buyer (18.41) |
|-----------------------|-----------------------------|-----------------------|---------------------------|
| 0.50 | 2.00 | 17.48 | Worse |
| 0.53 | 2.13 | 18.59 | Breakeven |
| 0.60 | 2.49 | 21.80 | Better |
| 0.70 | 3.29 | 28.73 | Better |
| 0.80 | 4.66 | 40.70 | Much better |
| 0.85 | 5.72 | 49.98 | Much better |

Reading: the 15% subscription discount pays back if subscribers stay for about 2.1 orders on average, which needs per-cycle retention above about 0.53. The answer comes from frequency, not per order margin; secondary analyses of Recharge and Klaviyo data make the same point (subscribers place many more orders than one-time buyers, while the discount lowers per order economics) [Unverified, 2026].

Also check:
- Does the subscription discount cannibalize customers who would have repurchased at full price anyway? Compare one-time buyers' repeat rate before the subscription launch.
- First order churn: share of subscribers who cancel before the second shipment. If above about 30%, the first order incentive is attracting discount seekers [Practitioner consensus].
- Cadence fit: the default cadence must match consumption. Too fast leads to overstock, skips and cancellations; too slow loses orders. Derive from the median days between orders of repeat buyers.

## 3. Discount ladder for subscriptions

| Element | Typical range | Rule |
|---------|---------------|------|
| Ongoing subscribe and save | 5% to 15% | Set from the retention breakeven above; lower for high margin brands with strong repeat |
| First subscription order extra | 0% to 25% extra | Only with a first order churn guardrail |
| Prepaid 3 months | Extra 5% to 10% vs monthly | Cash and churn benefit justify it |
| Prepaid 12 months | Extra 10% to 20% | Fulfillment liability; refund terms |
| Free shipping on subscriptions | Often yes | Cheaper than a bigger discount when shipping cost is low |
| Loyalty perk at order 3 or 6 | Gift or upgrade | Targets the drop-off points in the survival curve |

Ranges are practitioner norms, not benchmarks [Practitioner consensus]. Use your own survival curve.

## 4. Retention mechanics that are part of the offer
- Skip, swap, delay and change cadence: let customers adjust instead of cancel. Recharge reports that active subscribers who skip are stickier and have higher lifetime value (internal finding, no published method) [Unverified]. Swapping is a portal setting that is off by default in Recharge [Official, help center].
- Cancellation save offers: a pause or a one-time discount at cancel. They must not obstruct cancellation (see section 6). Offer at most one save step, then cancel.
- Price change policy: grandfather existing subscribers for a period or give advance notice; several US state auto-renewal laws require notice before a price change (verify current state rules with `compliance`).
- Prepaid edge cases: in Recharge, prepaid plans queue future orders at zero value and cancelled prepaid subscriptions need queued orders cancelled and unshipped products refunded manually [Official, help center].

## 5. Repeat offers outside subscriptions (economics owned here, flows owned by `lifecycle-crm`)

| Repeat offer | Economics guardrail | Notes |
|--------------|--------------------|-------|
| Second order incentive | Cost below the CM2 gain from the lift in second order rate | Second order is the biggest drop-off for most DTC brands; test timing with `lifecycle-crm` |
| Replenishment reminder offer | Only if the reminder alone does not reach the target rate | Start with no discount |
| Winback discount | Max discount from the expected value of a reactivated customer | Tier by recency; no discount for recently lapsed |
| Cross sell offer | Bundle or gift with the second category | Prefer gift over discount |
| Loyalty points | Points cost = earn rate x redemption rate x value per point | Breakage reduces cost; report the liability |
| Referral reward | Reward cost per referred new customer below blended first order acquisition cost | Double sided rewards; fraud controls |
| VIP early access | No discount, access only | Protects price, rewards the best customers |

Rule for every repeat offer: define the maximum discount per segment as a number in the offer brief and pass it to `lifecycle-crm`; flows must not invent new discounts.

## 6. Subscription law (hand final terms to `compliance`)

| Jurisdiction | Rule | Status Oct 2026 |
|--------------|------|-----------------|
| US federal | ROSCA requires clear disclosure of material terms before billing, express informed consent, and a simple cancellation method; FTC civil penalties up to USD 53,088 per violation | In force [Official] |
| US federal | FTC "click to cancel" amendments to the Negative Option Rule vacated by the Eighth Circuit on 2025-07-08; FTC published a new ANPRM on 2026-03-13 (comments closed 2026-04-13); no proposed rule yet | Monitor [Official, 2026-03] |
| US federal | Amazon agreed in September 2025 to pay up to USD 2.5B (USD 1B civil penalty, USD 1.5B refunds) over Prime sign-up and cancellation practices; order requires a clear decline button and cancellation as easy as sign-up | Settled [Official, 2025-09] |
| US federal | 2026 ROSCA actions include JustAnswer (January), Hims and Hers (July), with a broad view of "material terms" beyond price | Active [Official, 2026] |
| US states | California auto-renewal law amendments (consent, online cancellation, annual reminders, price change notice) effective 2025-07-01; Massachusetts negative option regulations enforceable from 2025-09-02; New York City click to cancel rule in effect October 2026 | In force [Official and press, 2025 to 2026] |
| EU | Consumer law already bans misleading subscription traps; Germany requires a cancellation button since 2022-07-01; the Digital Fairness Act is expected to add easy cancellation duties | DFA proposal expected Q4 2026 |
| UK | DMCC Act subscription contracts regime (reminders, cooling-off at renewal, easy exit) delayed to spring 2027 per government statement of 2026-04-02 | Not yet in force [Official, 2026-04] |
| Turkey | Distance contract and consumer law apply; subscription cancellations must be possible through the same channel as sign-up under consumer rules [Unverified detail] | Check with `compliance` |

Offer-level rules that follow:
1. Show price, cadence, discount duration (does the 25% apply only to the first order?), renewal terms and how to cancel next to the subscribe button.
2. Never preselect subscription over one-time purchase without clear disclosure; many regulators see a preselected subscription as a dark pattern.
3. Cancellation must be at least as easy as sign-up. One save offer, then cancel.
4. Free trials that convert to paid need explicit consent, a reminder before billing (required by several US states and by Amazon's order style terms), and a simple cancel.

## 7. Subscription offer brief template

```
Offer ID:
Product(s) and default cadence (with consumption evidence):
Price: one-time / subscription / first subscription order / prepaid options:
Discount duration (first order only | ongoing | first N orders):
Shipping on subscription orders:
Perks by order number:
Skip, swap, pause, cadence change: enabled? limits?
Cancellation flow: steps, one save offer, confirmation message:
Economics: CM2 per order (one-time vs subscription), breakeven retention q, expected orders over 12 cycles:
Guardrails: first order churn, refund rate, support contacts about billing:
Legal: disclosures, reminder schedule, compliance sign off ID:
Owners: lifecycle-crm (flows), storefront-ux (PDP selector, account portal), site-engineer (app setup and QA)
Approvals: prices and offers are G3
```

## 8. Subscription health metrics

| Metric | Definition | Watch for |
|--------|-----------|-----------|
| Subscription take rate | Subscription orders / eligible orders | Falling after a discount cut |
| First order churn | Cancelled before second shipment / new subscribers | Above about 30% |
| Survival curve | Share active after cycle n, by acquisition offer | Steep drop at cycle 2 or 3 |
| Revenue churn and reactivation | Lost and regained recurring revenue | Rising after price change |
| Skip rate | Skipped orders / scheduled orders | Rising skips predict churn; consider cadence change |
| Failed payment rate | Failed charges / attempted charges | Vendor claims of large churn share from failed payments are unverified; still fix dunning |
| Subscriber CM2 per order | After the subscription discount | Below the floor |
