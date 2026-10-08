# Guarantees and Risk Reversal

> A guarantee moves risk from the customer to you. It pays when the perceived risk is high, the product delivers, and the cost of honoring it is lower than the conversion it adds. Never present statutory rights as a special benefit.

## 1. Types of risk reversal

| Type | Example | Fits | Cost driver |
|------|---------|------|-------------|
| Unconditional money back | "Not happy within 60 days, full refund, keep nothing" | Consumables, low cost of goods, high confidence | Refund rate x (refund plus unrecoverable goods) |
| Satisfaction guarantee with return | "Return within 100 days for a refund" | Durable goods, apparel, sleep products | Return logistics, refurbishing |
| Try before you buy or trial period | "Sleep on it for 100 nights" | Mattresses, furniture, high ticket | Returns, resale value |
| Results guarantee (conditional) | "Lose X or get your money back if you followed the plan" | Services, coaching, B2B | Claim handling; must define conditions clearly |
| Performance or SLA guarantee | "Live in 14 days or month free" | B2B SaaS, agencies, installers | Credits paid out |
| Price match or price drop protection | "If the price drops within 14 days we refund the difference" | Promo heavy categories | Refund of difference; trains price watching |
| Free returns or exchanges | "Free exchanges, first return free" | Apparel, footwear | Return shipping and handling |
| Extended warranty | "3 year warranty" | Electronics, appliances | Repair or replacement cost |
| Pay after delivery or pay on results | Invoice later, success fees | B2B, services | Bad debt, cash flow |
| Cancel anytime | Subscriptions | Subscriptions, SaaS | Churn is visible sooner (healthy) |
| Free sample or paid trial size | Low cost first step | Consumables, beauty, food | Sample cost, low conversion to full size |

## 2. Evidence

| Finding | Source | Label |
|---------|--------|-------|
| Lenient return policies raise purchases more than they raise returns, on average; longer time windows are associated with fewer returns (endowment effect), while money and effort leniency raise purchases | Janakiraman, Syrdal and Freling 2016 meta-analysis, Journal of Retailing | [Study, 2016] |
| Lenient return policy raised purchase likelihood in remote purchase settings without a matching rise in returns | Wood 2001, Journal of Marketing Research | [Study, 2001] |
| Free shipping promotions raised returns and could be unprofitable net | Shehu, Papies and Neslin 2020 | [Study, 2020] |
| A weak returns policy is a reason to abandon a cart for a minority of shoppers (about 15% in secondary summaries of Baymard data) | Baymard via secondary sources | [Study, 2025, secondary] |

Interpretation: guarantees help most when the product delivers and the risk the customer fears is real. They do not fix a product with high defect or disappointment rates; they expose it.

## 3. Economics of a guarantee

```
Guarantee cost per order = claim rate x (refund value + unrecoverable product cost + handling)
Breakeven conversion lift = guarantee cost per order / CM2 per order (before the guarantee)
```

Worked example (illustrative): CM2 EUR 32 per order. A 60 day money back guarantee is expected to raise claims from 2% to 4% on EUR 60 orders; product is not recoverable; handling EUR 3. Incremental cost = 0.02 x (60 + 18 + 3) = EUR 1.62 per order. Breakeven conversion lift = 1.62 / 32 = 5.1%. If the guarantee lifts conversion by 8%, it pays; if it lifts by 3%, it does not.

Track: claim rate by cohort, reasons, serial claimers (policy for abuse), refund cost as a percent of revenue.

## 4. Legal rules (hand final wording to `compliance`)

| Rule | Where | Implication |
|------|-------|-------------|
| Presenting rights given to consumers by law as a distinctive feature of the trader's offer is always unfair | EU Unfair Commercial Practices Directive Annex I (blacklist); UK DMCC Act blacklist | "14 day returns" is not a guarantee in the EU and UK; it is the law. Only promote what goes beyond: longer windows, free return shipping, no questions asked |
| 14 day right of withdrawal for distance sales | EU Consumer Rights Directive; UK Consumer Contracts Regulations; Turkey (14 day cayma hakkı under Mesafeli Sözleşmeler Yönetmeliği) | Baseline, not a selling point |
| Legal guarantee of conformity, at least 2 years | EU Sale of Goods Directive 2019/771 (national laws may go further) | "2 year warranty" in the EU is the legal minimum; a commercial guarantee must state it does not affect legal rights |
| Commercial guarantee statements must be clear and binding | EU and UK consumer law | Write conditions, duration, territory, how to claim |
| Guarantee and warranty advertising must disclose conditions | US FTC Guides for the Advertising of Warranties and Guarantees (16 CFR Part 239); Magnuson-Moss Warranty Act | "Satisfaction guaranteed" requires the terms to be available and honored |
| Results guarantees with conditions | Everywhere | Conditions must be stated prominently, reasonable, and checkable; vague conditions are misleading |
| Price match and lowest price claims | Everywhere | Must be honored as stated; "lowest price guaranteed" is a claim needing substantiation |

## 5. Designing the guarantee (procedure)
1. Identify the top 3 purchase risks from VOC (fit, efficacy, durability, setup effort, wasted money, switching cost). Source: reviews, support tickets, post-purchase surveys (`market-intel` and `cro` research).
2. Pick the guarantee that targets the top risk. Fit risk: free exchanges. Efficacy risk: results or satisfaction guarantee. Effort risk: setup included or done-for-you. Switching risk (B2B): migration included, exit clause.
3. Set the window to cover the time the customer needs to experience the value (consumables: one full usage cycle; sleep: about 30 nights minimum; SaaS: through activation).
4. Model cost with claim rates from your own history or a conservative assumption (double the current return rate as a stress case).
5. Write the terms: what qualifies, how to claim, what must be returned, refund method and timing, exclusions. Keep it short and specific.
6. Get `compliance` sign off; the human approves (policy changes are G3 when published).
7. Ship the display through `storefront-ux` and `cro` (PDP, cart, checkout reassurance), and `creative-strategy` for ads.
8. Measure: conversion lift (test or pre and post with control), claim rate, abuse, refund cost, review sentiment.

## 6. B2B and services risk reversal

| Lever | Example | Risk to you |
|-------|---------|------------|
| Paid pilot with credit | 30 day pilot fee credited to the annual contract | Low |
| Performance SLA credits | Service credits if uptime or delivery misses | Medium, capped |
| Out clause | Cancel after 90 days with 30 days notice | Revenue predictability |
| Implementation guarantee | "Live in 30 days or we keep working at no cost" | Delivery capacity |
| Success based fees | Part of the fee tied to an agreed metric | Measurement disputes; define the metric precisely |
| Fixed price quote | No overruns for defined scope | Scope creep; write the scope tightly |
| Satisfaction guarantee on first job (local services) | Redo free if not satisfied | Labor |

## 7. Guarantee copy and claims checklist
- [ ] States exactly what the customer gets and how (refund, exchange, credit) and by when.
- [ ] Does not present statutory rights as an extra (EU, UK).
- [ ] Conditions stated next to the claim, not only in the footer.
- [ ] Matches the terms page word for word on window and conditions.
- [ ] Logged in `ads-master/brand/CLAIMS.md` as approved before use in ads.
- [ ] Support team briefed; claim process tested end to end.

## 8. Guarantee change request snippet

```
| # | Object | Current | Proposed | Rollback | Evidence | Approver |
| 1 | Returns policy page | 30 days, customer pays return | 60 days, first return free | Restore prior policy text (snapshot attached) | Cost model v1, expected breakeven lift 5.1% | Prices, discounts, shipping approver |
```

## 9. Guarantee by business model

| Model | Strongest risk reversal | Window | Watch |
|-------|-------------------------|--------|-------|
| Ecommerce consumables | Money back on the first order, keep the product | One full usage cycle (30 to 60 days) | Serial claimers; limit to first order per household |
| Ecommerce durables and apparel | Free exchanges, longer return window, first return free | 30 to 100 days | Return shipping cost and resale value |
| High ticket home (mattress, furniture) | Trial period with pickup | 30 to 365 nights | Logistics of pickups; donation or resale channel |
| Lead gen services | Satisfaction guarantee on first job, fixed price | Per job | Redo labor |
| B2B SaaS | Implementation guarantee, out clause, SLA credits | 30 to 90 days | Contract wording |
| Consumer SaaS and apps | Cancel anytime, prorated refunds on annual plans | Billing cycle | Store refund rules for apps |
| Marketplace sellers | Platform buyer protection plus your own extended return | Platform rules | Platform terms may override yours |

## 10. Return policy design levers (from the leniency evidence)

| Lever | Leniency type | Expected effect (Janakiraman et al. 2016) | Use |
|-------|---------------|--------------------------------------------|-----|
| Longer return window | Time | Raises purchase; associated with fewer returns | Usually the cheapest lenient lever |
| Free return shipping | Money | Raises purchase and returns | Use when fit risk blocks purchase |
| No restocking fee | Money | Raises purchase | Default for consumer goods |
| Easy return process (labels, drop-off points) | Effort | Raises purchase and returns | Pair with exchange-first flows |
| Exchange-first (credit or exchange before refund) | Money and effort | Keeps revenue | Must not block statutory refund rights |
| Scope (all items vs full price only) | Scope | Clearance exclusions reduce cost | State exclusions clearly |

## 11. Abuse controls that keep a guarantee affordable
- Limit "keep the product" money back offers to the first order per customer or household.
- Ask for a short reason on claims; use it as VOC, not as a barrier.
- Flag accounts above a claim threshold (for example 3 claims in 12 months) for manual review.
- Require original packaging only where resale depends on it, and say so up front.
- Never refuse statutory withdrawal or conformity claims to control abuse; use the commercial guarantee terms only.

## 12. Testing a guarantee
- Visitor level A/B on PDP and cart reassurance copy (`cro` runs it), or geo split when terms change for a whole market.
- Primary metric: contribution per visitor over the purchase window plus expected claim cost at the observed claim rate.
- Read claims at the end of the guarantee window, not at the end of the test: a 60 day guarantee test is not finished until 60 days after the last order in the test.
- Guardrails: claim rate, return rate, review rating, support contacts.
