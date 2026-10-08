# Offer Economics: Formulas, Worked Examples and a Calculator

> Every offer is a price change in disguise. Model it in contribution per order and per new customer before anyone writes copy. Definitions follow `ads-master/METRICS.md`; if the project defines a metric differently, the project wins.

## 1. The cost stack of one order

Use net of VAT (or sales tax) values. List every variable cost; a missing line is the most common reason an offer "worked" in the dashboard and lost money in the bank.

| Line | Symbol | Notes |
|------|--------|-------|
| List price of merchandise | P | Net of VAT. For bundles, the bundle price |
| Discount given | D | Percent x P, fixed amount, or value of free units |
| Net merchandise revenue | R = P minus D | Before refunds |
| Shipping charged to customer | Sc | Zero under free shipping |
| Landed product cost | C | Purchase price plus inbound freight, duties, tariffs. Recheck after tariff or customs changes (US de minimis ended 2025-08-29, EU EUR 3 low value parcel duty from 2026-07-01) [Official, 2026-06] |
| Bonus product cost | B | Landed cost of free gifts and samples, not their retail value |
| Pick, pack, packaging | F | Per order plus per extra unit |
| Outbound shipping cost | S | What the carrier bills you, including surcharges |
| Payment fees | Pay | Percent of amount charged plus fixed fee; BNPL fees are higher than cards |
| Marketplace or app fees | M | Commission, subscription app take rate, bundle app fees |
| Expected returns cost | Ret | Return rate x (return label plus processing) plus unsellable share x C |
| Expected refunds | Ref | Return rate x refunded revenue |

Contribution layers (same as `growth-orchestrator` unit economics):

```
CM1 = R - C                                   (product margin on the order)
CM2 = R + Sc - Ref - C - B - F - S - Pay - M - Ret   (contribution before marketing)
CM3 = CM2 - marketing cost attributed to the order    (contribution after marketing)
Contribution margin % = CM2 / (R + Sc - Ref)
```

## 2. Acquisition investment (the number that decides first order offers)

```
Acquisition investment = media spend
                       + shipping subsidy        (carrier cost minus shipping charged, on acquisition offer orders)
                       + bonus product cost      (landed cost of gifts on acquisition offer orders)
                       + incremental discount cost (discount on new customer orders above the always-on baseline)
Blended first order acquisition cost = acquisition investment / new customers
```

Rules:
1. Count each offer cost once. Either deduct it inside CM2 or add it to acquisition investment, never both. Default for reporting: compute CM2 at full price and put offer costs in acquisition investment, so media and offer costs compete in one budget.
2. "Incremental" means above the baseline the business would have given anyway (for example a permanent 10% welcome code is baseline once it is always on; a new 25% launch code adds 15 points).
3. Use landed cost for gifts. A gift with EUR 15 retail value and EUR 4 landed cost costs EUR 4 plus any extra pick and shipping weight.
4. Attribute subsidies only to the orders that used the offer (order tags or discount codes), not to all orders.

## 3. Core formulas

| Question | Formula | Example (m = 53.5%) |
|----------|---------|---------------------|
| Extra unit volume a discount needs to keep contribution flat | lift = d / (m - d), where m = contribution per unit / list price before the discount | 20% off: 0.20 / 0.335 = 59.7% more units |
| Volume you can lose after a price increase before contribution falls | loss = i / (m + i) | +10% price: 0.10 / 0.635 = 15.7% |
| Breakeven ROAS on an offer order | 1 / contribution margin % of the offer order | Offer CM2 43.4%: 2.30 |
| Breakeven CPA on an offer order | CM2 of the offer order (first order only) | EUR 21.31 |
| Allowable acquisition investment per new customer | contribution LTV over the payback horizon minus target profit per customer | See section 6 |
| Equivalent unit discount of "buy X get Y free" | Y / (X + Y) | Buy 2 get 1: 33.3% per unit |
| Effective discount of a gift | landed gift cost / R | EUR 4 / EUR 60 = 6.7% |
| Discount rate (health metric) | total discounts / gross merchandise sales at list price | Track weekly |
| Price realization | net revenue per unit / list price | Falling realization with flat volume is margin leakage |

The d / (m - d) shortcut ignores that a lower price also lowers payment fees and refunds, so it overstates the lift needed slightly. Use the calculator (section 8) for the exact number: in the example below the exact breakeven lift for 20% off is 50.7%, not 59.7%.

## 4. Worked example: four first order offers on the same product

Inputs (illustrative, net of VAT, EUR): list price 60, landed cost 18, pick and pack 3, carrier cost 6, shipping charged 4.95 unless free, payment 2% plus 0.25, return rate 8%, return handling 8 per return, 20% of returns unsellable. Output from the calculator in section 8:

| Offer | Net revenue | CM2 | CM2 % | Offer cost per order (discount, subsidy, gift) |
|-------|-------------|-----|-------|-----------------------------------------------|
| A. Full price, pays shipping | 60.15 | 32.11 | 53.4% | 0 (baseline shipping subsidy 1.05) |
| B. 20% off, pays shipping | 49.11 | 21.31 | 43.4% | 12.00 discount |
| C. Free gift (cost 4, retail 15), pays shipping | 60.15 | 28.11 | 46.7% | 4.00 gift |
| D. Free shipping, full price | 55.20 | 27.26 | 49.4% | 6.00 subsidy |
| E. 10% off plus free shipping | 49.68 | 21.86 | 44.0% | 6.00 discount plus 6.00 subsidy |

Reading:
- The gift (C) gives a higher perceived value (EUR 15) than the discount (B, EUR 12) at a third of the cost. It wins if customers value the gift. Test perceived value first (survey or offer test), because a gift nobody wants converts like no offer.
- Free shipping (D) costs EUR 4.85 more per order than A. It needs about 18% more orders (32.11 / 27.26 minus 1) to break even, before any AOV effect.
- B needs about 51% more orders than A to break even on the first order. It only makes sense if the repeat contribution of the extra customers pays for it (section 6) and if the discount does not attract lower value customers (Lewis 2006 found a 35% acquisition discount produced customers worth about half as much over the long run as non-promotional customers, in newspaper and online grocery data [Study, 2006]).

## 5. Worked example: acquisition investment and payback

Month data: media EUR 24,000, 600 new customers, all on offer B (20% off a EUR 60 order, so EUR 12 incremental discount each), no gift, no extra shipping subsidy.

```
Acquisition investment = 24,000 + 600 x 12 = 31,200
Blended first order acquisition cost = 31,200 / 600 = EUR 52.00   (media CPA alone looks like EUR 40.00)
First order contribution after acquisition = full price CM2 32.11 - 52.00 = EUR -19.89 per new customer
```

Payback needs repeat contribution of EUR 19.89 per customer. If 35% of the cohort orders again within 90 days at full price (CM2 32.11), repeat contribution at 90 days is 0.35 x 32.11 = EUR 11.24, so payback is not reached at 90 days. Decision options: lower the discount, switch to a gift, raise repeat rate (handoff to `lifecycle-crm`), or accept a longer payback if `STRATEGY.md` allows it.

Compare: the same 600 customers on offer C (gift, EUR 4) cost 24,000 + 2,400 = 26,400, or EUR 44.00 each, and first order contribution after acquisition is 32.11 minus 44.00 = EUR -11.89, if the gift converts as well as the discount. That "if" is the test.

## 6. Allowable acquisition investment from LTV

```
Contribution LTV(h) = sum over the horizon h of (expected orders x CM2 per order)
Max acquisition investment per new customer = Contribution LTV(h) / required LTV to CAC ratio
Payback month = first month where cumulative contribution per customer >= acquisition investment per customer
```

| Horizon choice | Use when |
|----------------|----------|
| First order only (h = 1 order) | Cash constrained, no repeat data, one-off purchase categories |
| 90 days | Consumables with 30 to 60 day cycles; enough cohort history |
| 12 months | Proven retention, healthy cash, STRATEGY.md allows payback over 6 months |
| 24 months or more | Subscriptions and SaaS with stable churn curves; discount future contribution |

Always cohort by acquisition offer: customers won by a 30% code and by a free gift are different populations. Tag the first order with the offer ID (see [Testing and measurement](offer-testing-and-measurement.md)).

## 7. Free shipping threshold economics

```
Monthly change in contribution =
    + orders pushed up to the threshold x (extra merchandise x item contribution % - shipping revenue they no longer pay)
    + extra orders from higher conversion x CM2 of those orders
    - shipping revenue lost on orders that were already above the new threshold
    - extra returns from padded baskets (if returns are free and easy)
```

Worked example (illustrative): 1,000 orders per month, flat shipping EUR 4.95 today, 25% of orders already at EUR 70 or more. Proposal: free shipping from EUR 70.
- Lost shipping revenue on the 250 orders already above EUR 70: 250 x 4.95 = EUR 1,237.50.
- 12% of orders (120) move from about EUR 55 to EUR 72: extra EUR 17 merchandise at 50% item contribution = EUR 8.50, minus EUR 4.95 shipping they stop paying = EUR 3.55 each, EUR 426 in total.
- Breakeven extra orders = (1,237.50 minus 426) / EUR 30 average CM2 = 27 orders, a 2.7% conversion lift.
- Decision: run the threshold as a test with contribution per visitor as primary metric (see [Incentives](incentives-discount-bonus-shipping.md) section 4 for threshold placement and the returns caveat).

## 8. Calculator (copy, edit inputs, run with Python 3)

```python
from dataclasses import dataclass

@dataclass
class Order:
    name: str
    list_price: float          # merchandise value at list price (net of VAT)
    discount_pct: float = 0.0  # 0.20 = 20% off
    cogs: float = 0.0          # landed product cost
    bonus_cogs: float = 0.0    # landed cost of free gifts (not retail value)
    pick_pack: float = 0.0
    ship_cost: float = 0.0     # carrier cost per order
    ship_charged: float = 0.0  # shipping paid by customer (net of VAT)
    pay_pct: float = 0.0
    pay_fixed: float = 0.0
    return_rate: float = 0.0
    return_cost: float = 0.0   # label plus processing per return
    unsellable: float = 0.0    # share of returns that cannot be resold

def contribution(o):
    merch = o.list_price * (1 - o.discount_pct)
    charged = merch + o.ship_charged
    kept_rev = merch * (1 - o.return_rate) + o.ship_charged
    cogs = o.cogs * (1 - o.return_rate) + o.cogs * o.return_rate * o.unsellable
    fees = charged * o.pay_pct + o.pay_fixed
    cm2 = (kept_rev - cogs - o.bonus_cogs - o.pick_pack - o.ship_cost
           - fees - o.return_rate * o.return_cost)
    return {"offer": o.name, "net_revenue": round(kept_rev, 2), "cm2": round(cm2, 2),
            "cm2_pct": round(cm2 / kept_rev, 3)}

base = dict(list_price=60, cogs=18, pick_pack=3, ship_cost=6, pay_pct=0.02,
            pay_fixed=0.25, return_rate=0.08, return_cost=8, unsellable=0.2)
offers = [Order("A full price", ship_charged=4.95, **base),
          Order("B 20% off", discount_pct=0.20, ship_charged=4.95, **base),
          Order("C gift", bonus_cogs=4.0, ship_charged=4.95, **base),
          Order("D free shipping", **base)]
rows = [contribution(o) for o in offers]
for r in rows:
    print(r)
a = rows[0]["cm2"]
for r in rows[1:]:
    print(r["offer"], "breakeven order lift vs A:", round(a / r["cm2"] - 1, 3))
```

Expected output for the inputs above: A 32.11, B 21.31, C 28.11, D 27.26; breakeven lifts vs A of 0.507 (B), 0.142 (C), 0.178 (D). If your numbers differ, check the inputs, not the formula.

## 9. Spreadsheet layout (when the human prefers a sheet)

| Column | Content |
|--------|---------|
| A | Offer ID (matches EXPERIMENTS.md and discount code) |
| B to M | Inputs from section 1 (one column each) |
| N | Net revenue: `=B*(1-C)*(1-K)+H` style formula mirroring the calculator |
| O | CM2 |
| P | CM2 % |
| Q | Offer cost per order (discount plus subsidy plus gift) |
| R | Breakeven order lift vs control: `=O_control/O_row-1` |
| S | Expected conversion lift (from test or assumption, labeled) |
| T | Expected contribution per 1,000 visitors: visitors x CVR x (1+S) x O |

Keep one tab per scenario (base, pessimistic, optimistic). State the source of every input in a notes row.

## 10. Sensitivity: what moves offer profitability most

| Input | Typical effect | Check |
|-------|----------------|-------|
| Contribution margin before the offer | Lower margin makes every discount far more expensive (lift needed grows non-linearly as d approaches m) | Recompute after cost increases, tariffs, carrier rate changes |
| Return rate on offer orders | Free shipping and deep discounts can raise returns (Shehu, Papies and Neslin 2020 found free shipping promotions shift baskets to riskier items and raise returns [Study, 2020]) | Compare return rate by offer cohort |
| Share of buyers who would have bought anyway | High share means most discount cost is subsidy, not incremental | Holdout or geo test |
| Repeat rate of offer acquired customers | Determines whether a loss on order one is recovered | 30, 60, 90 day cohort repeat by offer |
| Pull-forward | Promo sales borrowed from the weeks after | Compare 2 to 4 weeks pre and post against a baseline |
| Payment mix | BNPL and some local methods cost more per order | Fee by method from the PSP report |

## 11. Quality bar for any economics output
- [ ] Inputs listed with source and date (backend export, supplier invoice, carrier invoice, PSP report).
- [ ] CM2 computed for control and every variant; offer costs counted once.
- [ ] Acquisition investment and blended first order acquisition cost shown next to platform CPA.
- [ ] Breakeven lift stated; expected lift labeled as tested, benchmark or assumption.
- [ ] Repeat and payback view if the offer targets new customers.
- [ ] Downside scenario (lift half of expected, returns up 3 points) computed.
