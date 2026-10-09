# Operations: Fulfillment, Inventory, Returns, Account Health and Appeals

> Knowledge as of 2026-10. Operations decide the featured offer, delivery badges, seller scores and whether the account survives. Changes to fulfillment settings, shipping templates, inventory placement and any appeal submission are G3.

## 1. Fulfillment options compared

| Option | Marketplace | Pros | Cons | Use for |
|--------|-------------|------|------|---------|
| FBA (Fulfillment by Amazon) | Amazon | Prime badge, featured offer advantage, returns and customer service handled | Fees, capacity limits, storage and aged inventory fees, prep must be done by you in the US since 2026-01-01 | Fast moving small and standard size SKUs |
| FBM (merchant fulfilled) | Amazon | Control, no FBA storage | Must meet late shipment, cancellation and tracking metrics; refunds in 4 calendar days (US, from 2026-01-26 [Unverified]) | Bulky, slow, custom or high value items |
| Seller Fulfilled Prime | Amazon | Prime badge with own warehouse | Strict delivery performance | Strong 3PL with weekend coverage |
| Multi-Channel Fulfillment (MCF) | Amazon inventory for other channels | One stock pool | Amazon branded packaging options vary; some marketplaces forbid Amazon delivery | DTC overflow; check other marketplace rules |
| Amazon Warehousing and Distribution (AWD) | Upstream storage | Cheaper bulk storage, auto replenishment to FBA | Another fee layer | Brands with capacity limits |
| Pan-European FBA, Multi-Country Inventory | Amazon EU | Local stock in several countries | VAT registration in storage countries | EU scale |
| Logistiek via bol (LVB) | bol | Delivery promise, returns handled | Fees by size class; new tariffs for smallest classes from 2026-09-09 [Secondary] | Fast moving NL and BE SKUs |
| Trendyol Express (TEX) and HepsiJET | Turkey | Integrated cargo, tariff by desi | Tariff changes several times a year | Default carriers on Turkish marketplaces |
| Fulfilled by noon (FBN) | Gulf | Speed badges | Storage up 2026-10-01 | UAE and KSA |
| Allegro One Fulfillment | Poland | Smart! delivery | Storage fees (cut 2026-03-02) | Polish scale |
| ZEOS | Zalando and other channels | Fashion returns handling | Fees in Partner University | Fashion brands |
| Walmart Fulfillment Services (WFS) | Walmart US | 2 day badge | US only | Walmart hero SKUs |

## 2. Inventory planning

```
Days of cover = units available (marketplace warehouse + inbound) / average daily units (last 28 days, adjusted for trend and events)
Reorder point = (lead time days + inbound processing days + safety days) x daily units
Safety days: 14 standard, 21 to 28 before peak events, plus capacity limit buffer
```

| Rule | Why |
|------|-----|
| Keep hero SKUs at 4 to 8 weeks of cover in marketplace warehouses, plus upstream buffer | Stockouts lose rank and ads momentum; recovery can take weeks [Practitioner consensus] |
| Plan event stock 8 to 12 weeks ahead | Amazon capacity limits are monthly and in cubic feet [Secondary, 2026]; inbound delays spike before Q4 |
| Avoid more than 90 days of cover in FBA | Aged inventory surcharges and peak storage (October to December rates about 3x off-peak) |
| Watch the low inventory level fee on Amazon | Charged when historical supply is too low; now also on bulky [Secondary, 2026] |
| Watch IPI (Inventory Performance Index) | Low IPI triggers capacity restrictions; reported threshold 400 [Unverified] |
| Stranded and suppressed inventory zero | Units not sellable cost storage and lose sales |
| Never send unprepped units to US FBA | Amazon stopped US prep and labeling services on 2026-01-01; inbound defect fees rose [Secondary, 2026] |

Stockout protocol: (1) pause ads on the SKU when cover drops under 14 days or lower budgets to slow sales if replenishment arrives in time, (2) raise price only within corridor and law (no price gouging rules during emergencies), (3) offer variants, (4) log incident, (5) after restock, restart ads with launch-like bids for 1 to 2 weeks.

## 3. Returns

| Marketplace | Return rules | Cost lines |
|-------------|--------------|-----------|
| Amazon | Amazon return policy; FBA returns processed by Amazon; Returns processing fee in some categories above a return rate threshold [Official, 2024, prior knowledge]; SAFE-T claims for FBM (US claim window 30 days from 2026-01-21 [Unverified]) | Refund, return shipping, processing fee, unsellable units |
| bol | Statutory 14 day withdrawal plus bol policy (bol often 30 days) [Practitioner consensus] | Return handling, LVB return fees |
| Turkey | 14 day withdrawal; return shipping cost borne by the seller per the Ministry's 2025 decision [Contested]; Distance Contracts Regulation amendment in force 2026-01-01 | Return cargo by desi, commission refunded on return (Hepsiburada) |
| EU generally | 14 day withdrawal right; an online withdrawal function (withdrawal button) for distance contracts concluded online applies from 2026-06-19 under Directive (EU) 2023/2673 [Official, prior knowledge]; marketplaces implement it in their own flows, so check how each one handles it with `compliance` | |

Return rate guardrail: track return rate by SKU and reason monthly. A return rate rising 3 or more points above baseline is a listing, sizing or quality problem to fix before scaling ads.

## 4. Account health targets (all marketplaces)

| Marketplace | Metrics | Targets |
|-------------|---------|---------|
| Amazon | AHR, ODR, late shipment, pre-fulfillment cancel, valid tracking, on-time delivery, policy compliance, customer service dissatisfaction | AHR healthy (200+), ODR under 1%, LSR under 4%, cancel under 2.5%, VTR over 95% [Official thresholds, prior knowledge; AHR scale Secondary] |
| bol | Delivery on time, cancellations, customer question response, returns handling, partner rating | Partner Platform norms [Unverified exact thresholds]; rating 8.5+ of 10 [Practitioner consensus] |
| Trendyol | Seller score from reviews, returns, complaints, cargo performance | 9.0 or higher [Practitioner consensus] |
| Hepsiburada | Store score, cargo handover time, cancel and return rate | Stable or rising |
| Allegro | Ratings, Super Seller criteria | Super Seller [Practitioner consensus] |

Note: from July 2026, Amazon no longer gates featured offer eligibility on seller performance, but performance still weighs in the ranking and drives account health enforcement [Secondary, 2026-07].

## 5. Most common account health threats

| Threat | Typical cause | Prevention |
|--------|---------------|-----------|
| Intellectual property complaints | Selling branded goods without authorization; using protected images or terms | Supplier invoices from authorized sources; own photos; trademark checks |
| Product authenticity complaints ("inauthentic") | Customers or brands claim counterfeit | Keep invoices for 365 days or more; buy only from authorized distribution |
| Product safety and compliance | Missing documents (GPSR in the EU, CPSC certificates in the US, CE marking, SASO in KSA) | Compliance file per SKU before listing |
| Restricted products and claims | Pesticide claims ("antibacterial"), medical claims, supplements | Claims through `compliance`; avoid restricted terms |
| Listing policy violations | Variation abuse, duplicate listings, wrong category | Catalog hygiene |
| Review manipulation | Incentives or gating | [Reviews and ratings](reviews-and-ratings.md) |
| Related accounts | Multiple accounts without approval, shared details with suspended accounts | One account per legal entity unless approved |
| Verification failures | Identity, address, bank verification | Keep documents current |
| Price gouging and pricing policy | Excessive prices in emergencies | Price floors and ceilings |

## 6. Appeals: Plan of Action (POA)

Only facts. Never admit to things that did not happen, never blame Amazon or customers, never send fake documents (that leads to permanent bans).

```
# Plan of Action draft: <account> <marketplace> <issue> | Date | Status: DRAFT (needs human approval to submit)
## Issue summary (policy, ASINs or orders affected, notice date, notice text reference)
## Root cause (specific, verified facts; what exactly went wrong and why)
## Corrective actions already taken (dates, what was done, evidence attached: invoices, test reports, screenshots)
## Preventive measures (process changes, owners, tools, checks; how they stop recurrence)
## Documents attached (list; each verified real and unaltered)
## Requested outcome (reinstate ASIN, reinstate account)
```

Procedure:
1. Read the notice and the cited policy fully; identify exactly what Amazon asks for (some notices only need documents, not a POA).
2. Collect evidence from the business, never invent.
3. Draft POA; `compliance` reviews claims and product safety items.
4. Human approves and submits (G3). Agents never submit.
5. Track in `INCIDENTS.md`; follow up in the Account Health dashboard; do not submit repeated appeals that repeat the same content.
6. For complex suspensions (related accounts, authenticity on large volume), recommend a specialist lawyer or appeal consultant.

bol, Trendyol and Hepsiburada: respond via the partner support channels with the same structure (cause, actions, prevention, documents).

## 7. Customer service

| Rule | Detail |
|------|--------|
| Response time | Within 24 hours on all marketplaces, including weekends in peak (Amazon measures response time; bol and Turkish platforms track question response) |
| Allowed content | Order related communication only; no marketing, no links to own site, no review requests outside allowed tools |
| Data | Buyer personal data only for fulfillment and service; never exported to CRM (Amazon Data Protection Policy, KVKK, GDPR) |
| Templates | Prepare templates for delivery delay, damage, wrong item, return instructions; `compliance` approves |

Customer messages are G3 if sent by an agent; usually the human or the customer service team sends them.

## 8. Daily operations checklist (peak) and weekly (normal)

| Check | Daily in peak | Weekly normally |
|-------|---------------|-----------------|
| Account health notices and warnings | Yes | Yes |
| Featured offer or buybox share on hero SKUs | Yes | Yes |
| Days of cover on top 20% SKUs | Yes | Yes |
| Inbound shipment status | Yes | Yes |
| Late shipment or handover risk (FBM, Turkish marketplaces) | Yes | Yes |
| Customer questions unanswered over 12 hours | Yes | Yes |
| Return reasons new themes | | Yes |
| Stranded or suppressed listings | Yes | Yes |
