# Incentives: Discount vs Bonus Product vs Free Shipping vs Payment Terms

> An incentive answers "why buy now, and why here". Pick the cheapest incentive that changes behavior, and prove it changes behavior. Economics formulas live in [Offer economics](offer-economics.md).

## 1. Incentive menu

| Incentive | Cost to you | Perceived value | Best for | Main risks |
|-----------|-------------|-----------------|----------|-----------|
| Percent off | Discount x every order that uses it, including buyers who would have paid full price | Clear, comparable | Low price items, broad promos, clearance | Trains waiting for sales, reference price erosion, attracts deal seekers |
| Amount off (EUR 10 off) | Fixed per order | Strong on higher price items | Orders above about EUR 100, first order codes with a minimum spend | Minimum spend gaming |
| Tiered spend (spend 100 save 15, spend 150 save 30) | Discount on qualifying orders only | Pushes AOV | Catalogs with add-on items | Complexity, stacking errors |
| Free gift with purchase (GWP) | Landed gift cost | Retail value of the gift | Brands with low cost, high perceived value items or samples; protecting reference price | Gift nobody wants, stockouts of the gift, EU "free" rules |
| Bonus units (buy 2 get 1, extra 20% in the pack) | Landed cost of extra units | High when the product is consumed | Consumables, multipacks | Lowers purchase frequency if customers stockpile |
| Free shipping (always) | Carrier cost on every order | Very high; surprise shipping fees drive abandonment | Low weight, mid to high AOV | Kills margin on small orders |
| Free shipping threshold | Carrier cost above the threshold | High | Raising AOV toward a natural basket size | Basket padding with later returns |
| Faster shipping upgrade | Difference between service levels | High near deadlines | Gift seasons, shipping cutoffs | Carrier capacity at peak |
| Loyalty points or store credit | Redeemed value x redemption rate (breakage lowers cost) | Medium | Repeat purchase, protecting price | Liability on the balance sheet, complexity |
| Payment terms (installments, BNPL) | Higher payment fee | High for high ticket | Orders above about EUR 150, markets where installments are normal (Turkey, Netherlands in3, Nordics) | Fees, regulation, customer harm |
| Price lock, early bird, founding member price | Revenue forgone on early buyers | High for launches | Pre-orders, launches, SaaS | Must be honored; real deadlines only |
| Service add-ons (installation, setup, onboarding call) | Labor cost | High when effort is the barrier | Services, B2B, complex products | Capacity |

## 2. Choosing the incentive (decision tree)

1. Is there a real barrier other than price (shipping cost, risk, effort, payment)? Remove that barrier first: free shipping threshold, guarantee, installation, installments. These usually cost less per incremental order than a discount.
2. Is the goal AOV or units? Use a threshold, tiered spend or a bundle, not a flat percent.
3. Is the goal new customers? Prefer a first order gift or a capped amount off with a minimum spend; protect the list price for returning customers.
4. Is the goal clearing stock? Use percent off on the specific SKUs, time boxed, and keep the core range at full price.
5. Is the product sold by retail partners or marketplaces at a reference price? Prefer value adds (gift, exclusive bundle, extended guarantee) over visible price cuts. See [Channel conflict](channel-conflict-and-price-parity.md).
6. Is the margin below about 40% contribution? Avoid percent off above 10% unless the economics show repeat recovery; use bonus product with low landed cost instead.

## 3. Evidence on discount framing and promotion effects

| Finding | Evidence | Label | How to use it |
|---------|----------|-------|---------------|
| Percent framing feels bigger on low price items, amount framing on high price items (the "rule of 100") | Chen, Monroe and Lou 1998 framing experiments; popularized by Jonah Berger | [Study, 1998], lab, older | Under about EUR 100 show percent; above show the amount. Test if it matters. |
| Prices ending in 9 lift demand | Anderson and Simester 2003 catalog field experiments | [Study, 2003] | Use charm endings where the brand allows; luxury brands often use round prices |
| Left-digit bias is real and firms under-exploit it | Lacetera, Pope and Sydnor 2012 (used car mileage); Strulov-Shlain 2023 (retail scanner data) | [Study] | Cross a left digit downward (EUR 49 vs EUR 51) only when the margin math holds |
| "Free" carries more pull than its money value (zero price effect) | Shampanier, Mazar and Ariely 2007 | [Study, 2007], lab | Free shipping and free gifts often beat equal value discounts; test it |
| Deep acquisition discounts attract lower value customers | Lewis 2006: a 35% acquisition discount gave customers about half the long-term value | [Study, 2006], newspaper and online grocer | Cap first order discounts; cohort by offer |
| Free shipping promotions raise returns and can be unprofitable net | Shehu, Papies and Neslin 2020, field data and a field experiment | [Study, 2020] | Track returns by offer; tighten return frictions for padded baskets |
| Threshold free shipping raised orders and sales vs fixed fees without a returns penalty in one large EU retailer | University of Groningen SOM report (26.21 million orders) | [Study, 2021], one retailer | Thresholds can work; test with returns as guardrail |
| Shoppers pad baskets to hit thresholds and return the padding when returns are easy | University of Maryland dissertation; IIMA working paper (padding 15.7% to 23.0% of below threshold demand with easy returns) | [Study], working papers | Watch return rate of threshold-crossing orders |
| Extra costs are the top cart abandonment reason (39% of abandoners in recent Baymard surveys, 48% in the February 2024 US survey) | Baymard via eMarketer and secondary write-ups | [Study, 2024 to 2025] | Show shipping cost or threshold early on PDP and cart (display work goes to `storefront-ux` and `cro`) |
| BNPL access raises spending and merchant sales | Di Maggio, Katz and Williams (NBER w30508, 2022, not peer reviewed): spending up after first BNPL use; Berg, Burg, Keil and Puri (Journal of Financial Economics, 2025): about 20% sales lift, driven by lower credit customers | [Study] | Offer BNPL on high ticket items; weigh fees and customer harm |

Treat lab framing effects as test ideas, not laws. Real purchase settings shrink many of them (see [Bundles and price ladders](bundles-and-price-ladders.md) section 5 on decoys).

## 4. Free shipping threshold design

Procedure:
1. Pull 90 days of orders: AOV distribution (histogram in EUR 5 buckets), share of orders by bucket, shipping cost by order size and zone, return rate by order size.
2. Find the natural basket: the median order and the 60th to 75th percentile. Set the first test threshold 15% to 30% above the median order value, close to a price point reachable with one typical add-on item [Practitioner consensus].
3. Make sure an add-on exists: list 3 to 10 items priced at the typical gap (threshold minus median). Without "gap fillers" the threshold only taxes small orders. Hand gap filler placement to `storefront-ux`.
4. Compute the economics with section 7 of [Offer economics](offer-economics.md): lost shipping revenue on orders already above, gains from pushed-up orders, breakeven conversion lift.
5. Test (geo split, time split, or app based A/B; see [Testing](offer-testing-and-measurement.md)). Primary metric: contribution per visitor. Guardrails: return rate, conversion rate of small baskets, AOV.
6. Re-check the threshold when AOV, carrier rates or the product mix shift by more than about 10%.

| Situation | Threshold approach |
|-----------|--------------------|
| AOV well above shipping cost x 10 | Consider free shipping on all orders and test removing the threshold |
| Low AOV consumables | Threshold at about 2 units; or free shipping only on subscriptions |
| Heavy or bulky items | Zone based or product based free shipping; never a blanket threshold |
| Marketplace competitors ship free at any value | Match on hero SKUs, use threshold on the rest |
| High return categories (apparel, footwear) | Threshold plus paid returns or return fee on padded baskets; watch padding |
| Cross-border orders | Recompute with duties and the EU EUR 3 per item type duty (from 2026-07-01) or US duties (de minimis ended 2025-08-29) [Official, 2026-06] |

Shipping display must show the total early: drip pricing rules apply to mandatory charges, and several US state laws exempt only actual shipping charges from all-in pricing (see [Price display law handoff](price-display-law-handoff.md)).

## 5. Bonus product (gift with purchase) design

| Decision | Rule |
|----------|------|
| Gift choice | High perceived value, low landed cost, relevant to the product (sample of a second product line is ideal: it also cross sells) |
| Value claim | State the real retail value only if the item is genuinely sold at that price; otherwise do not state a value |
| Threshold | Gift on orders above a threshold, or with a specific hero product |
| Stock | Reserve gift stock for the full promo plus 20%; plan what happens when it runs out (end the promo, do not silently drop the gift) |
| Fulfillment | Add the gift as a zero priced line (automatic) so the warehouse picks it; check weight against shipping bands |
| Returns | Decide whether the gift must be returned with a refund; write it in the terms |
| Measurement | Track gift orders with an order tag; compare repeat purchase of the gifted product line |

## 6. Discount guardrails

- Cap first order discounts at the level the economics allow (typical practice 10% to 20% for DTC; label as [Practitioner consensus]).
- One public code per purpose; unique single use codes for partners and influencers so leakage to coupon sites can be traced.
- Exclude new launches, low margin SKUs and gift cards from sitewide discounts.
- Never stack welcome code plus sitewide sale plus loyalty points unless modeled. Configure combinations explicitly (Shopify: product, order and shipping discount classes) and test the cart.
- Keep a discount rate target (discounts / gross sales at list) and a promo days per quarter budget. When either is exceeded, stop adding promos and review reference prices.
- Promo end dates are real: no "extended by popular demand" unless that was disclosed as possible and it does not mislead.
- In the EU and UK, every announced price reduction refers to the lowest price in the prior 30 days; in Turkey, since 2026-08-01, the lowest price in the prior 10 days for advertised discounts [Official, 2026-07, secondary sources]. Get `compliance` sign off.

## 7. Payment incentives (BNPL and installments)

| Item | Detail |
|------|--------|
| Effect | Higher spend and sales for some segments (Berg et al. 2025 about 20% merchant sales lift; Adobe: BNPL drove USD 1.03B of US online spend on Cyber Monday 2025) [Study, 2025; Study, 2025-12] |
| Cost | Merchant fee per transaction above card fees; check your PSP contract per method |
| Placement | Messaging on PDP and cart for items above the provider minimum; placement work goes to `storefront-ux` |
| UK | Deferred payment credit regulated by the FCA from 2026-07-15; lenders carry most duties, but merchant promotions and refund processes must fit the lender rules [Official, 2026-07] |
| EU | Consumer Credit Directive 2 (2023/2225) rules apply from 2026-11-20, bringing interest-free BNPL into scope with disclosure and creditworthiness duties for lenders [Official, 2023] |
| US | State licensing and CFPB positions shift; check with `compliance` |
| Turkey | Card installments ("taksit") are a core offer lever; installment caps by category are set by the banking regulator (BDDK) and change; verify current caps before promising installments [Unverified] |
| Rule | Never present credit as "free money"; disclose terms the provider requires; keep BNPL messaging away from vulnerable audiences |

## 8. Incentive selection worksheet (copy into the offer brief)

```
Offer ID:
Goal (new customers | AOV | units | clearance | reactivation | launch):
Barrier being removed (price | shipping | risk | effort | payment | urgency):
Candidates considered (min 3):
| Candidate | Cost per order | Breakeven lift | Perceived value | Channel conflict risk | Legal flags |
Chosen and why:
Expected lift and its source (test, benchmark, assumption):
Guardrails (return rate, discount rate, repeat rate):
Stop rule:
Approvals needed (prices and discounts are G3):
```

## 9. Incentive defaults by business model

| Model | First choice | Second choice | Avoid |
|-------|--------------|---------------|-------|
| Ecommerce consumables | Bundle or multipack, subscription offer | Gift with purchase (sample of another line) | Deep percent off on first order |
| Ecommerce fashion | Free exchanges, threshold shipping | Seasonal sale windows | Constant sitewide codes |
| Ecommerce high ticket | Installments, guarantee, delivery and setup | Amount off with minimum | Percent off on everything |
| Lead gen services | Specific free or credited diagnostic | Fixed price package | Gift card for a form fill |
| B2B SaaS | Trial or pilot design, onboarding included | Annual discount | Deep first year discounts that reset renewal expectations |
| Local services | Same day slot, satisfaction guarantee | Off-peak seasonal offer | Discounting peak season |
| App | Intro offer and trial length | Annual plan discount | Lifetime deals that cap revenue |
| Marketplace sellers | Platform events with funded discounts | Coupons | Prices below DTC that break parity |
