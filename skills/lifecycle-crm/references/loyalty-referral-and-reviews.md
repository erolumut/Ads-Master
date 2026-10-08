# Loyalty, Referral and Reviews

When loyalty programs pay, how to design and measure them, referral mechanics and fraud control, review request timing and the rules that govern incentives. Reward levels and liability are decided with `offer-strategy`; claims and incentive disclosures with `compliance`; loyalty UI in account pages with `storefront-ux`.

## 1. Does this business need a loyalty program?

| Signal | Loyalty likely pays | Loyalty likely wastes margin |
|--------|--------------------|------------------------------|
| Natural purchase frequency | 3 or more orders per year possible (consumables, apparel, beauty, food, pet) | Once every few years (furniture, mattresses, big electronics) |
| Repeat rate today | Meaningful repeat base to grow | Almost no repeaters (fix product or post purchase first) |
| Margin | Room for 2% to 10% reward cost | Thin margin, price led category |
| Competition | Competitors train customers to expect rewards | Category without programs and strong brand pull |
| Data | Orders, identity and email connected | Guest checkout heavy with no accounts |

If frequency is low, prefer referral, reviews and service perks over points.

## 2. Program types

| Type | Mechanic | Fit |
|------|---------|-----|
| Points | Earn per currency spent and per action; redeem for discounts or products | Broad DTC |
| Tiers (VIP) | Status by spend, order count or points; perks by tier | Customers with spend variance; LoyaltyLion added order count based tiers in 2026-08 [Official, LoyaltyLion product updates] |
| Paid membership | Fee for benefits (free shipping, member prices) | High frequency, strong value (marketplaces, retailers) |
| Cashback or store credit | Credit on next order | Simple; drives second order |
| Experiential perks | Early access, exclusive products, events | Brands with community; protects margin |
| Subscriptions as loyalty | Subscriber perks | Consumables |

## 3. Economics

```
Reward cost rate = value of rewards redeemed / revenue from members
Breakage = points issued but never redeemed (reduces cost, but low redemption also means low engagement)
Liability = outstanding points x expected redemption rate x value per point (finance must book it)
Program incrementality = (repeat rate or contribution of members) - (matched non members or holdout), not raw member vs non member
```

Self selection trap: members always look better because loyal customers join programs. Vendor statistics such as "redeemers repeat 50% vs 10.7% for non redeemers" [Unverified, vendor compilation 2026] are correlation. Measure with a holdout (randomly withhold program invitations or a perk) or a pre and post with matched cohorts.

Benchmarks to treat as directional only [Unverified, vendor guides 2026]: active redemption 20% to 30% in healthy programs, participation 40% to 50% of customers on average and 60% to 75% for the best programs.

## 4. Tools (October 2026)

| Tool | Notes |
|------|------|
| Smile.io | Shopify loyalty and referrals; Shopify Plus Partner (2025-10); Loyalty Hub inside Shopify customer accounts; Sidekick extension (2026-06) [Official, Smile news center] |
| LoyaltyLion | AI Campaigns (2026-01: points multiplier events, reward discounting, birthday bundles); order count tiers and auto applied vouchers (2026-08) [Official, LoyaltyLion] |
| Yotpo (Loyalty and Reviews) | Reported pricing shift toward active member based pricing and cost increases; standalone email and SMS products reportedly sunset 2025-12-31; deeper Klaviyo integration; acquisition rumors in 2026 [Unverified, secondary aggregators]. Check contract terms and roadmap before renewals |
| Rivo, Gameball, Growave, BON | Shopify loyalty alternatives |
| Okendo, Judge.me, Stamped, Reviews.io, Trustpilot, Bazaarvoice | Reviews and UGC; Klaviyo also has native reviews (Reviews API since 2024-10, Get and Update Reviews since 2025-01) [Official, Klaviyo API changelog] |
| ReferralCandy, Friendbuy, Talkable, Mention Me | Referral programs (Mention Me strong in UK and EU) |
| Klaviyo Customer Hub and Customer Agent | Loyalty display and actions (applying loyalty points) inside Klaviyo's customer experience surfaces [Official, Klaviyo 2026-06] |

Integration requirement: loyalty events (points earned, tier changed, reward available, points expiring) must reach the ESP as events or profile properties.

## 5. Loyalty flows

| Flow | Trigger | Content |
|------|---------|---------|
| Program welcome | Joined program | How to earn, first easy reward |
| Points earned | Order or action | Balance, distance to next reward |
| Reward available | Balance crosses threshold | Reward and how to use, no expiry pressure unless true |
| Points expiring | 30 and 7 days before | Reminder with best use |
| Tier upgrade | Tier change | Recognition, new perks |
| Tier at risk | Spend below retention threshold near period end | What keeps the tier |
| Anniversary | Join date | Thank you and perk |

## 6. Referral programs

Design:
- Double sided incentive (give X, get Y). Give side drives conversion; get side drives sharing.
- Timing: ask after delivery plus a positive moment (after a 4 or 5 star review, NPS 9 to 10, or second order), not in the order confirmation.
- Placement: post purchase flow, account page (storefront-ux), loyalty hub, thank you page.
- Reward on completed and not returned orders (wait past the return window for high value rewards).
- Personal referral links and codes; limit reward per referrer per period.

Fraud controls: block self referrals (same payment card, address, device, IP), new accounts with the same household, coupon site leakage of codes (unique links, cap uses), reward only first orders by new customers (new customer definition from METRICS.md).

Metrics: referral share of new customers, referral CAC (reward cost plus tool cost / referred new customers), referred customer LTV vs other channels, share rate (referrers / eligible customers).

Coordinate with `measurement` so referred customers are counted once (not also credited to paid channels) and with `growth-orchestrator` for blended CAC.

## 7. Reviews

### 7.1 Request timing

| Product type | First request | Reminder |
|--------------|---------------|----------|
| Instant use (apparel, accessories) | Delivery plus 3 to 7 days | +7 days |
| Routine products (skincare, supplements) | Delivery plus 14 to 30 days (enough use to judge, only approved claims about results) | +10 days |
| Durable or technical | Delivery plus 14 to 21 days | +14 days |
| Services and local | Same day or next day after job | +3 days |

Tie the trigger to delivery (Fulfilled Order plus transit time or carrier delivered event), not order date.

### 7.2 Rules

- Ask everyone, not only happy customers (review gating is prohibited by the FTC rule and platform policies) [Official, FTC 2024].
- Incentives (points, entry) only if not conditioned on positive sentiment and disclosed; some platforms (Google, Amazon) forbid incentives entirely [Official, platform policies].
- Never write, edit or suppress reviews; respond to negative reviews and route issues to support.
- EU: disclose how reviews are verified if you publish them (Omnibus Directive); UK: fake and concealed incentivized reviews banned under the DMCC Act from 2025-04-06 [Official].
- Product questions surfaced in reviews feed `creative-strategy` (VOC) and `cro`.

### 7.3 Review flow spec

| Step | Timing | Content |
|------|--------|---------|
| RV1 | Per table above | One click star rating in email (where supported), photo upload prompt |
| RV2 | Reminder | Short reminder |
| Branch: 4 to 5 stars | Immediately | Thank you; referral ask; UGC permission request |
| Branch: 1 to 3 stars | Immediately | Apology, support contact, fix offer (not an incentive to change the review) |

## 8. Worked example: points economics

Illustrative: earn 1 point per 1 EUR, 100 points = 5 EUR reward (5% headline reward rate). If 60% of points are eventually redeemed (40% breakage), the effective reward cost is 3% of member revenue. At a 50% contribution margin, the program must create at least 6% incremental member contribution (relative to the holdout or matched cohort) to pay for rewards alone, before tool fees. Model three scenarios with offer-strategy (redemption 40%, 60%, 80%) and book the liability at the expected redemption rate with finance.

## 9. Program spec template

```
## Loyalty or referral program spec: <name>
Objective: <second order rate, purchase frequency, referral share of new customers>
Mechanics: earn rules <...>; redeem rules <...>; tiers <thresholds and perks>; expiry <...>
Economics: headline reward rate <x%>, expected redemption <x%>, effective cost <x%>, liability method (finance)
Measurement: holdout or matched cohort design, primary metric, readout date
Flows: welcome, points earned, reward available, expiring, tier change, referral ask, review ask
Fraud controls: <self referral checks, caps, return window>
Legal: terms and conditions, incentive disclosures (compliance), points as liability (finance)
Owners: lifecycle-crm (flows), offer-strategy (economics), storefront-ux (account and loyalty UI), compliance (terms)
```

## 10. Loyalty, referral and reviews audit questions

- Is the program's incrementality measured beyond member vs non member comparison?
- Is loyalty liability tracked with finance?
- Are loyalty events in the ESP and are flows live for reward available and points expiring?
- Is the referral reward protected against self referral and code leakage?
- Are reviews requested from all buyers at a usage based time, with no sentiment conditioned incentive?
- Are review insights flowing to creative-strategy and cro?
