# Channel Price Corridors (DTC, Retail, Marketplace, Wholesale)

> Owns: the price relationship between channels (the corridor), the brand's own price per channel, recommended retail prices as recommendations, assortment differentiation to avoid like-for-like conflict, and the channel section of the report. Hands to `offer-strategy`: promotions and their channel conflict check, see [Channel conflict and price parity](../../offer-strategy/references/channel-conflict-and-price-parity.md). Hands to `marketplaces`: listing level pricing, buy box and fee operations. Hands to `compliance`: competition law questions (RPM, MAP, parity clauses) and legal review of any partner communication.

## 1. The corridor concept

A corridor is the range in which the brand sets its OWN prices per channel relative to a reference (usually the observed retail shelf price per unit). It is an internal policy for the brand's own channels. It is never an instruction to independent resellers.

```
Corridor for the brand's own DTC (example):  observed retail shelf per unit x (0.80 to 1.00) for multi-packs,
                                              x (1.00 to 1.10) for single units if sold at all
Corridor for the brand's own marketplace store: DTC price +/- marketplace fee difference, never below DTC hero per unit
```

The brand chooses the corridor so that:
1. DTC remains attractive (assortment, convenience, bundles) without being the cheapest way to buy the same thing.
2. Retail partners see no undercutting on comparable packs.
3. Marketplace prices do not drag the market below DTC and retail.
4. Contribution per unit per channel is understood (retail CM per unit vs DTC CM2 per unit minus acquisition cost).

## 2. Channel economics comparison

Use the script's retail block ([Cost to serve](cost-to-serve-and-margin-waterfall.md) section 6):

| Channel | Customer price per unit | Brand revenue per unit (ex VAT) | Brand costs per unit | Brand CM per unit | Acquisition cost per unit | CM after acquisition |
|---------|-------------------------|-------------------------------|----------------------|-------------------|---------------------------|----------------------|
| Retail | Shelf | Net net sell-in | COGS + logistics to DC | | Trade marketing | |
| DTC hero | Hero per unit | Net revenue / units | COGS + cost to serve / units | | Media per order / units | |
| Marketplace | Listing price | Net revenue - fees | COGS + fulfillment | | Retail media | |
| Wholesale or B2B | Price list | Net invoice | COGS + logistics | | Sales cost | |

Illustrative (script demo): retail CM EUR 0.80 per bar; DTC CM2 EUR 0.91 to 1.20 per bar before acquisition. DTC is worth more per bar only while acquisition cost stays under EUR 0.11 to 0.40 per bar (EUR 2.64 to 9.60 per 24 pack order). Many brands discover that retail volume is the better contribution per unit and DTC is a margin-neutral brand and data channel. That is a strategic choice for the human, presented in the report.

## 3. Legal frame (summary; `compliance` gives the answer)

| Topic | EU | Turkey | UK | US |
|-------|----|--------|----|----|
| Resale price maintenance (fixed or minimum resale prices) | Hardcore restriction under Article 101 TFEU and Vertical Block Exemption Regulation 2022/720 (in force 2022-06-01); recommended and maximum prices allowed if not turned into fixed or minimum prices through pressure or incentives [Official, prior knowledge] | Hardcore under Law 4054 and Communiqué 2002/2; Competition Board fines are frequent (Seher Gıda settlement TRY 173.8M; tire sector decision 2026-06-04 with Brisa at TRY 1.019B, RPM among the issues investigated) [Official and press, 2025 to 2026] | Competition Act 1998; CMA treats RPM as an object infringement | Rule of reason federally (Leegin 2007) but some states treat minimum RPM as per se illegal; MAP policies common [Prior knowledge] |
| MAP (minimum advertised price) | Treated like RPM when it restricts online advertised prices [Practitioner consensus, EU guidance] | Same risk | Same risk | Unilateral MAP policies widely used |
| Monitoring reseller prices | Lawful as information; unlawful when used to pressure discounters (EU fines Gucci, Chloé, Loewe EUR 157.4M 2025-10-14; Italy Morellato 2026-03-17) [Official] | Same | Same | |
| Price parity clauses (platforms) | Wide parity clauses excluded from block exemption; DMA limits gatekeepers | Turkish Competition Board scrutiny of platform parity | DMCC and CMA | Litigation (De Coster v Amazon class certified 2025-08-06) |
| Dual pricing (different wholesale price by channel) | Allowed under VBER 2022 if not aimed at restricting online sales | Check with counsel | | |

Hard rules for the agent:
- Never suggest telling a reseller or retailer what to charge, setting a minimum, capping their discounts, or threatening supply based on their price.
- Recommended retail prices (RRP, adviesprijs, tavsiye edilen satış fiyatı) are fine as genuine recommendations; never pair them with monitoring plus consequences.
- The brand controls its own channels' prices fully. Differentiation (packs, assortment, service) is the lawful way to manage conflict.

## 4. Conflict-free designs

| Design | How | Example |
|--------|-----|---------|
| Channel exclusive packs | DTC sells pack sizes or mixed boxes not stocked in retail | DTC 24 mixed box; retail single bars and 3 packs |
| Exclusive flavors or editions | DTC first or only | Seasonal flavor on DTC |
| Subscription value | Price advantage only for commitment (subscription) | Subscribe and save on DTC, designed with `offer-strategy` |
| Service bundles | Value adds rather than price cuts | Free delivery above threshold, sample bar |
| Marketplace specific pack | Different count to fit fees and avoid direct parity | 18 pack on bol.com |
| Coordinated calendar | Own promos timed so they do not undercut partner promos (own decision, no agreement on partner prices) | |

## 5. Corridor setting procedure

1. Map observed prices per unit per channel and pack (benchmark data, dated).
2. Compute brand CM per unit per channel.
3. Identify like-for-like comparisons (same pack in two channels).
4. Choose differentiation for every like-for-like conflict, or set the brand's own price at or above the observed shelf price per unit for that pack.
5. Set the corridor for own channels: hero DTC per unit within [low, high] of the shelf reference; marketplace own store price relative to DTC.
6. Set monitoring (via `market-intel`) of shelf and marketplace prices for information; define what the brand will do with its OWN prices when the observed shelf price moves (review own price; never respond toward the retailer).
7. Write the channel section of the report with the retailer's likely view and the brand's talking points about assortment (not about the retailer's price).

## 6. Marketplace specifics (summary)

- Amazon: the featured offer (buy box) considers price competitiveness against other places customers can buy, including the brand's own site; DTC promos can suppress the featured offer [Official policy, via offer-strategy research]. Amazon EU fees fell for low price items from 2026-01-05 (grocery 5% referral up to EUR 10) [Official].
- bol.com: fixed fee per item plus category commission (reported, verify in the seller account); price competitiveness affects buy box ("koopblok") [Unverified].
- Trendyol and Hepsiburada: high category commissions (Trendyol food rates are unconfirmed: sources range from 5% to 20% and vary by seller level and brand category) plus service fees; campaign participation pushes prices down; read the commission table in the seller panel and the campaign terms before setting the marketplace pack price [Unverified].
- Price the marketplace pack so CM per unit after fees is at or above the DTC CM2 per unit target, or treat marketplace as a reach channel with a lower target agreed by the human.

## 7. Wholesale and distributor tiers

See [SaaS and B2B pricing](saas-and-b2b-pricing.md) section 6 for price lists. Corridor rule: wholesale price x typical retailer margin should land near the RRP; if a distributor sits between, model both margins (distributor margin on their sell price, retailer margin on shelf price).

```
Shelf ex VAT = RRP / (1 + vat)
Retailer buy price = shelf ex VAT x (1 - retailer margin_on_price)
Distributor buy price = retailer buy price x (1 - distributor margin_on_price)
Brand ex works price = distributor buy price (minus logistics if the brand delivers)
```

Label every margin as margin_on_price or markup_on_cost.

## 8. Channel section template

```markdown
## Channel corridor
| Pack | DTC per unit | Retail shelf per unit (store, date) | Marketplace per unit (seller, date) | Gap DTC vs shelf | CM per unit DTC / retail |
Like-for-like conflicts: <list>
Differentiation: <packs, flavors, subscriptions>
Own-channel corridor: DTC hero per unit within <x to y%> of observed shelf; marketplace own store not below DTC hero per unit.
Retailer view: <what they will see>; talking points about assortment and roles (not their prices).
Legal: no reseller price instructions; RRP stays a recommendation; compliance reviewed <date>.
```

## 9. Common mistakes

1. DTC launches the same pack the retailer sells at a lower per unit price.
2. "MAP policy" emails to EU resellers.
3. Using monitoring tools to chase discounters.
4. Marketplace pack priced below DTC to win the buy box, then DTC loses its customers.
5. Ignoring that the retailer also sees the DTC launch ads.

## 10. Worked corridor (illustrative, script demo inputs)

| Pack | DTC per bar | Retail shelf per bar (illustrative) | Gap | DTC CM2 per bar | Retail brand CM per bar | Conflict? |
|------|-------------|------------------------------------|-----|-----------------|-------------------------|-----------|
| Single bar | not sold on DTC | 2.99 | n/a | n/a | 0.80 | No |
| Trial 12 | 2.75 | 2.99 | -8.2% | 1.20 | 0.80 | Low: pack not in retail |
| Hero 24 | 2.50 | 2.99 | -16.5% | 0.99 | 0.80 | Medium: visible per bar gap |
| Stock up 48 | 2.29 | 2.99 | -23.4% | 1.00 | 0.80 | Medium to high |
| Stock up 96 | 2.08 | 2.99 | -30.3% | 0.91 | 0.80 | High: keep for subscribers only or drop |

Options for the human:
1. Keep the ladder, sell only mixed or exclusive boxes on DTC (no identical SKU set to retail), keep 96 for subscribers.
2. Narrow the ladder: hero 24 at EUR 62.49 (EUR 2.60 per bar, gap -13%), stock up 48 at EUR 114.95 (EUR 2.39, gap -20%).
3. Price DTC at shelf parity per bar and win on assortment and convenience only; lower DTC volume, no conflict.

## 11. Retailer conversation guide (brand's own policy only)

Topics the brand may raise: the role of each channel, the DTC assortment (exclusive boxes), joint category growth, promotions the brand funds, its own recommended retail price as a recommendation. Topics to avoid: the retailer's shelf price as an expectation, any link between supply terms and the retailer's prices, any information about other retailers' future prices. Before the meeting, `compliance` reviews the talking points.
