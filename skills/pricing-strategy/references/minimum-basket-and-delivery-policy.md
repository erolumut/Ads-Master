# Minimum Basket and Delivery Policy

> Owns: the minimum order value or minimum units, the delivery fee schedule, the free delivery threshold value, carrier formats and express options, and the economics behind each. Hands to `offer-strategy`: free shipping as a promotion (first order free delivery, event free shipping, threshold tests as offers) and gap filler merchandising, see [Incentives](../../offer-strategy/references/incentives-discount-bonus-shipping.md). Hands to `storefront-ux`: threshold progress bars, cart messages. Hands to `compliance`: how delivery costs and minimums are displayed.

## 1. Policy elements

| Element | Options | Decided by |
|---------|---------|-----------|
| Minimum order | None; minimum value (for example EUR 25); minimum units; bundle-only assortment (no single units sold) | Minimum viable basket from the script |
| Delivery fee below threshold | Flat fee; tiered by basket value; real carrier cost passed through; "small order fee" | Carrier band cost and competitor reference |
| Free delivery threshold | None; threshold value; free delivery always (price built in); membership (unlimited delivery for a fee) | Threshold economics, AOV distribution, competitors |
| Formats | Letterbox parcel, box parcel, pick-up point, express or same day | Carrier contract and product size |
| Markets | Domestic vs cross-border thresholds | Zone cost differences |

## 2. Decision procedure

1. Run the script with the current single unit price and scan basket sizes ([Cost to serve](cost-to-serve-and-margin-waterfall.md) section 7). Read the minimum viable basket under charged delivery (MVB_charged) and under free delivery (MVB_free).
2. Pull the basket distribution from the order export: share of orders by units and value band, mean, median and mode basket.
3. Pull competitor delivery terms (fee, threshold, minimum) from the benchmark.
4. Choose the minimum policy:
   - If single units lose money even with the fee charged (the common case for low price consumables), sell bundles only or set a minimum at MVB_charged.
   - If under 10% of orders sit below MVB_charged, a small order fee may be enough.
5. Choose the threshold:
   - Economic floor: the smallest threshold whose free delivery basket clears the CM2 floor (script section 3). Never below MVB_free.
   - Commercial placement: near the competitor reference, and about 15 to 30% above current AOV or just above the median basket so that a meaningful share of orders can reach it with one more item [Practitioner heuristic; test].
   - Ladder alignment: the hero rung should qualify; the entry rung usually should not.
6. Set the delivery fee below the threshold: cover most of the carrier cost for that band, rounded to a price point, not above competitor references by more than about EUR 1 without a reason.
7. Model the dead zone (section 4) and the expected mix shift.
8. Write the policy into the report with economics and the display handoff.

## 3. Evidence

| Finding | Source | Label |
|---------|--------|-------|
| Contingent free shipping (threshold) increases basket sizes compared with unconditional free shipping; customers spend effort to reach the threshold, and merchandise profits are higher under contingent free shipping | Chen and Ngwe, HBS working paper 19-034 (2019) | [Study] |
| Nonlinear shipping fees change purchase incidence and order size; threshold policies shift baskets just above the threshold | Lewis, Singh and Fay, Marketing Science (2006) | [Study, prior knowledge] |
| Threshold policies raised orders without a returns penalty in a large EU dataset (26.21M orders); free shipping promotions can raise returns and be unprofitable net | Groningen report; Shehu, Papies and Neslin (2020), via offer-strategy dossier | [Study] |
| Extra costs (shipping, fees) are the top fixable reason for cart abandonment (39% of abandoners in recent Baymard data) | Baymard via offer-strategy dossier | [Study, 2024 to 2025] |
| Dutch online spending in H1 2026 EUR 17.1B, flat; transactions +3% to 170.4M; smaller baskets expected to persist | Thuiswinkel Market Monitor via Emerce, 2026 | [Study, 2026] |
| A Dutch webshop reported more returns with a EUR 50 free shipping threshold and free returns, and fewer multi-size orders after switching to fixed shipping | Practitioner report | [Unverified, single case] |
| "58% of shoppers add items to reach a threshold" | Vendor benchmark without a traceable study | [Unverified]; do not cite as causal |

Contested: whether free delivery thresholds raise contribution depends on product returns behavior and the share of orders already above the threshold. Test before scaling.

## 4. Threshold dead zone

Orders just above the threshold earn less CM2 than orders just below it, because the customer added a little revenue and you gave up the whole delivery fee. Illustrative script output (EUR 2.79 bar, EUR 4.95 fee, EUR 50 threshold):

| Bars | Basket incl VAT | Delivery charged | CM2 |
|------|-----------------|------------------|-----|
| 16 | 44.64 | 4.95 | 21.50 |
| 18 | 50.22 | 0.00 | 20.28 |
| 20 | 55.80 | 0.00 | 23.58 |

Implications:
- A threshold pays only if it (a) moves orders from below MVB into viable baskets, (b) lifts conversion enough, or (c) moves customers to the hero rung.
- Align the threshold with a ladder rung price (hero 24 at EUR 59.95 above a EUR 50 threshold) so that most free delivery orders are hero orders with good CM2, not random top-ups.
- Avoid thresholds that sit a few euros above the hero price: customers add a low margin item or abandon.

## 5. Delivery fee design

| Situation | Fee design |
|-----------|-----------|
| Low price consumables, letterbox capable | Letterbox fee near carrier cost (for example EUR 3.95 to 4.95 incl VAT) for small packs; free above threshold |
| Bulky or heavy items | Fee by weight or volume band; threshold may not be viable; consider "delivery included" pricing |
| Premium positioning | Free delivery always, price built into the product (only when CM2 at the entry rung clears the floor with carrier cost included) |
| Marketplace competitive category | Match marketplace norms (Amazon and bol customers expect free delivery above low thresholds) |
| Cross-border EU | Separate fee and threshold per zone; carrier cost to Germany or Belgium differs from domestic |
| Turkey | "Kargo bedava" thresholds are common; cost moves monthly with inflation; marketplace contracted rates differ from list rates by 30 to 50% |
| Subscription or membership | Free delivery as a subscription benefit; unlimited delivery memberships (Dutch grocery example: AH delivery bundle reported at EUR 12 per month [Unverified, consumer site]) |

Benchmark context (Dutch online grocery, reported by consumer sites, verify before citing): Albert Heijn minimum order around EUR 50 with free delivery reported from EUR 70; Picnic minimum reported EUR 25 to 35 with free delivery; Jumbo minimum and slot based fees [Unverified, 2026, conflicting sources]. These anchor Dutch shoppers' expectations for food delivery.

## 6. Legal display (handoff to compliance)

- CJEU C-62/25 (judgment 2026-04-09, ECLI:EU:C:2026:256): flat handling or delivery charges that apply only to orders below a minimum amount do not have to be included in the product's selling price under the Price Indication Directive 98/6/EC, provided they are avoidable and stated clearly and separately before checkout [Official, via Thuiswinkel.org 2026-04-22]. Consequence: a small order fee is lawful when displayed clearly; hiding it until the last checkout step is not.
- Drip pricing: mandatory fees must be in the headline price (UK blacklist since 2025-04-06; EU Digital Fairness Act proposal planned for late 2026, consultation showed 79% support for a drip pricing ban among respondents who wanted action) [Official and consultation summary]. Optional delivery fees are not mandatory fees, but must be clear.
- "Free delivery" claims: conditions (threshold, zones, formats) must be next to the claim.
- Partial returns pushing an order below the threshold: shipping can only be charged back if the terms say so clearly [Unverified, WebwinkelKeur guidance]; confirm with `compliance`.
- Turkey: distance sales and price tag rules require the total price including taxes and delivery to be shown before the order; Ministry of Trade inspections are active (about TRY 2.6B in administrative fines across 360,000 firms in the first nine months of 2026) [Press, 2026-10].

## 7. Policy templates

```markdown
## Delivery and minimum basket policy: <market>
Data: order export <dates>; carrier contract <name, as of date>; script run <date>
- Minimum order: <none | EUR X | bundle only>. Reason: single unit CM2 <value>; MVB charged <N units / EUR>.
- Delivery fee below threshold: <EUR X incl VAT> (carrier cost <EUR Y ex VAT> for <format>).
- Free delivery from: <EUR Z>. Economic floor <EUR>; hero rung <EUR>; median basket <EUR>; competitor references <list>.
- Formats: <letterbox up to N units | box | pick-up>.
- Expected effect: share of orders below MVB from <a%> to <b%>; blended CM2 per order from <x> to <y> (assumption, label).
- Dead zone note: <analysis>.
- Display handoff: compliance (C-62/25, unit price, free claim wording), storefront-ux (progress bar).
- Review: <date>; kill criterion <metric and threshold>.
```

## 8. Testing the policy

- Prefer time or geo based designs over visitor level splits for delivery fees: switchback weeks (alternate policy by week, 6 to 8 cycles), or market split for cross-border stores ([Elasticity and tests](elasticity-and-price-tests.md)).
- Primary metric: contribution per visitor (or per session) including delivery revenue and carrier cost.
- Guardrails: conversion rate, return rate, share of orders in the dead zone, customer service contacts about delivery.
- Minimum duration: two full weekly cycles per arm; avoid event weeks.

## 9. Common mistakes

1. Setting the threshold from a competitor without running own economics.
2. Threshold below MVB_free: every free delivery order near the threshold loses money.
3. Ignoring carrier format steps (letterbox vs box) when setting the fee.
4. Showing the delivery fee only at the last checkout step.
5. Raising the threshold without checking how many hero orders fall below it.
6. Same threshold across zones with different carrier costs.
7. Treating free delivery as free: it is a price cut equal to the carrier cost on every qualifying order.
