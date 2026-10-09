# SaaS, B2B and Wholesale Pricing

> Owns: value metric choice, tier structure and packaging, price levels per tier, usage and credit pricing, regional pricing, B2B and wholesale price lists, discount governance and contract indexation. Hands to `offer-strategy`: trials, freemium, reverse trials, annual discount offers, see [Lead gen and SaaS offers](../../offer-strategy/references/lead-gen-and-saas-offers.md). Hands to `cro`: pricing page tests. Hands to `mobile-app-growth`: app store price tiers and paywalls.

## 1. State of SaaS pricing (2026)

| Finding | Source | Label |
|---------|--------|-------|
| Hybrid pricing (subscription plus usage) used by 37% of 230 companies, heading toward 47%; outcome based pricing expected to grow from 5% to 31%; 29% have AI credits or tokens in pricing today; median AI gross margin target 50% | Growth Unhinged, State of B2B SaaS and AI Monetization 2026 (survey April to May 2026) | [Study, 2026] |
| Investors favor hybrid (35%), outcome based (26%), usage (24%) over flat fee (10%) and seats (5%) | Same | [Study, 2026] |
| 78% of IT leaders were hit by unexpected AI or consumption charges in the last 12 months | Zylo 2026, via secondary | [Unverified] |
| Usage based adoption reported between 18% and 42% depending on definitions | Multiple secondary sources | [Contested] |
| Per resolution AI pricing examples: Intercom Fin USD 0.99 per resolution | Vendor pricing, via secondary | [Unverified, check vendor page] |
| AI in pricing: gen AI used by about 10 to 30% of pricing leaders, agentic AI under 10% today, expected 20 to 45%; strongest in market intelligence and cost tracking | McKinsey AI in Pricing survey, November 2025, n = 419; article 2026-04-07 | [Study, 2026] |

## 2. Value metric

The value metric is the unit the price scales with. Good metrics: grow with customer value, are easy to understand and predict, are measurable by the vendor, and are hard to game.

| Metric | Fits | Risk |
|--------|------|------|
| Seats | Collaboration tools where value grows with users | Seat compression when AI does the work; sharing logins |
| Contacts, records, locations | CRM, email, multi-location | Customers prune to save |
| Usage (events, API calls, GB) | Infrastructure, data | Bill shock, hard forecasting |
| Credits (prepaid pool across features) | AI features with variable cost | Confusing; customers self-police usage |
| Outcomes (resolutions, leads, bookings) | AI agents, performance services | Attribution disputes |
| Flat per account | Simple tools, SMB | Leaves money on the table with large customers |

Procedure: list candidate metrics, score each on the four criteria with customer interviews, check cost to serve per metric unit (AI inference costs), pick one primary metric plus at most one secondary (hybrid), keep a predictable base fee.

## 3. Tiers and packaging

- 3 tiers plus enterprise is the common structure. Tier names describe the customer (Starter, Team, Business) rather than abstract metals.
- Fences between tiers: features the next segment needs (SSO, audit logs, admin roles, integrations, limits on the value metric), not arbitrary limits.
- Price ratios between adjacent tiers commonly 2x to 3x [Practitioner consensus]. Middle tier is the hero.
- Annual billing discount usually 15 to 20% (two months free = 16.7%); annual plan breakeven math in offer-strategy.
- AI features: include a credit allowance per tier, sell top-ups; price per credit above marginal inference cost with the target gross margin.
- Add-ons for niche needs instead of tier bloat.
- Grandfather legacy plans for a defined period when repackaging; migration plan with notice.

## 4. Price level per tier

1. Value: estimate value per customer segment ([Value based pricing](value-based-pricing-and-wtp.md)), for example hours saved x loaded hourly cost, or revenue gained.
2. Alternatives: competitor tiers normalized per seat or per metric unit at annual billing, in the same currency ex VAT.
3. Cost: gross margin per tier including AI inference, support, payment fees (Stripe 1.5% + EUR 0.25 for standard EEA cards [Official]).
4. Research: conjoint or Gabor Granger per segment; Van Westendorp for range.
5. Set price points with round numbers; regional pricing (section 5).

## 5. Regional and currency pricing

- Price in local currency for main markets; purchasing power adjustments for lower income markets (for example Turkey) with fences (billing country, payment method) to limit arbitrage.
- In Turkey, TRY pricing needs a repricing rule (CPI 29.73% year on year, September 2026, TÜİK) or USD or EUR pricing with clear communication; consider annual prepaid in TRY with an indexation note.
- VAT: B2C digital services charge the customer's country VAT; B2B reverse charge in the EU. Show prices ex VAT for B2B, incl VAT for consumers where required.

## 6. B2B and wholesale price lists

Structure:

| Element | Design |
|---------|--------|
| List price | Published or semi-published price per unit per pack or case |
| Volume tiers | Break points by order quantity or annual volume (for example 1 to 9 cases list, 10 to 49 cases -5%, 50+ -10%) |
| Customer type | Retailer, distributor, foodservice, corporate; different list or discount per type (lawful dual pricing within competition rules; check with compliance) |
| Payment terms | Net 30 standard; early payment discount (for example 2% 10 net 30) |
| Logistics terms | Incoterms; minimum order per delivery; delivery fee below the minimum drop size |
| Promotions | Trade promotion funding rules with proof of performance |
| Indexation | Clause tied to CPI, PPI, FX or input cost index with a band and review frequency |

Discount governance:
- Price waterfall per account: list price - on invoice discounts - off invoice (rebates, promo funding, payment discount) = pocket price. Monitor pocket price dispersion; leakage hides in off invoice items.
- Approval matrix: sales rep up to x%, manager up to y%, director above.
- Enforce indexation: Simon-Kucher 2025 found only about half of companies with indexation clauses enforce them consistently [Study].

Minimum drop size: compute like the minimum viable basket, with a pallet or case delivery cost. Small B2B orders often lose money; set a minimum order value or a delivery fee below it.

Wholesale to retail math (label margin types):

```
RRP incl VAT -> shelf ex VAT = RRP / (1 + vat)
Retailer buy price = shelf ex VAT x (1 - retailer margin_on_price)
Brand wholesale list price = retailer buy price (before trade terms)
```

## 7. Price increases in SaaS and B2B

- Annual uplift clauses (CPI linked or fixed 3 to 7%) are standard in B2B contracts [Practitioner consensus].
- For SaaS list price increases: grandfather existing customers for 3 to 12 months or until renewal; communicate 30 to 90 days ahead; tie the increase to new value delivered.
- Model churn risk per segment against allowable loss ([Price changes](price-changes-and-inflation.md)).

## 8. SaaS pricing page and checks (for cro)

- Prices per tier with billing period and currency clear; ex VAT or incl VAT clear.
- Value metric visible next to price; usage limits explicit.
- Enterprise contact path.
- Annual vs monthly toggle with the real saving.
- AI credits explained with examples ("about N actions").
- Legal: auto-renewal disclosures and cancellation path (`compliance`).

## 9. Common mistakes

1. Pricing by seat for AI features that reduce seats.
2. Credits with no example of what they buy.
3. Too many tiers and add-ons.
4. B2B discount sprawl without a waterfall.
5. Indexation clauses never applied.
6. Regional prices without fences.

## 10. Worked tier example (illustrative)

| Tier | For | Price per month (annual billing) | Value metric limit | Key fences | AI credits |
|------|-----|----------------------------------|--------------------|------------|------------|
| Starter | Solo practitioners | EUR 29 | 1 calendar, 300 bookings | No integrations | 100 |
| Team (hero) | Clinics with 2 to 10 staff | EUR 89 | 10 calendars, 3,000 bookings | Integrations, reminders, reports | 1,000 |
| Business | Multi-site | EUR 249 | Unlimited calendars, 15,000 bookings | SSO, audit log, API | 5,000 |
| Enterprise | Groups | Quote | Custom | Contract, SLA | Pooled |

Checks: Team to Starter ratio 3.1x, Business to Team 2.8x; monthly billing at +20% (annual saving 16.7%); credit top-up price set so cost per credit (inference plus overhead) stays under 50% of price (matching the 50% AI gross margin target median from Growth Unhinged 2026).

## 11. Worked B2B price list (illustrative, food brand)

| Customer type | Unit | List price ex VAT | Volume tier | Payment terms | Delivery terms |
|---------------|------|-------------------|-------------|---------------|----------------|
| Independent retail | Case of 12 bars | [W] | 1 to 9 cases list; 10+ cases -4% | Net 30, 2% 10 | Free delivery from 10 cases; below: EUR [fee] |
| Gym and office (foodservice) | Case of 24 | [W2] | 5+ cases -5% | Net 30 | Minimum 5 cases |
| Distributor | Pallet | [W3] | Annual volume rebate 2 to 4% | Net 45 | Ex works |

Corridor check: [W] / 12 x (1 + 9% VAT) / (1 - retailer margin_on_price) should land near the RRP per bar. If it lands well below DTC per bar, the DTC ladder or the list needs a rethink.
