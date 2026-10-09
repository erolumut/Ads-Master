# Channel Conflict with DTC and Retail

> Knowledge as of 2026-10. Price decisions belong to `pricing-strategy` (corridor, positioning) and `offer-strategy` (promotions, calendar). This module tells the marketplaces agent how conflict shows up on marketplaces, what is lawful, and how to design around it. Competition law questions go to `compliance` and to counsel.

## 1. How conflict shows up

| Symptom | Mechanism | Where |
|---------|-----------|-------|
| Featured offer suppressed or lost on Amazon during a DTC sale | Amazon compares prices it finds elsewhere; if your Amazon price is much higher than a recent or external price, the featured offer can be removed | Amazon (Fair Pricing and price competitiveness behavior) [Official, prior knowledge] |
| Amazon 1P drops retail price to match a DTC or retailer promotion | Vendor pricing: Amazon sets retail price and matches competitors | Vendor Central |
| Walmart suppresses an item | Item priced above other sites | Walmart Marketplace [Official, prior knowledge] |
| Retail partners complain or delist | Marketplace or DTC price under shelf price | Offline and online retail |
| Resellers undercut each other and the brand | Too many resellers with parallel sourcing; repricers race to the bottom | Amazon, Trendyol, Hepsiburada, bol |
| DTC traffic falls when marketplace grows | Customers prefer marketplace for speed, trust, loyalty programs | All |
| Marketplace campaign forces a price | Joining platform campaigns requires price at or below campaign level for a period | Trendyol, Hepsiburada, bol, Allegro, Amazon deals |

## 2. What the law allows (summary; not legal advice)

| Jurisdiction | Rule | Label |
|-------------|------|-------|
| EU | Resale price maintenance (fixed or minimum resale prices) is a hardcore restriction; recommended prices are allowed if truly non-binding; MAP style policies that restrict online advertised prices are treated like RPM in most cases; selective distribution may restrict sales via third-party marketplaces under conditions (Coty, CJEU 2017); wide parity obligations imposed by online intermediation services fall outside the Vertical Block Exemption Regulation (2022) | [Official, prior knowledge] |
| EU enforcement 2025 | Commission fined Gucci, Chloé and Loewe EUR 157.4M for RPM (2025-10-14) | [Official, via offer-strategy research] |
| UK | Similar RPM prohibition; CMA enforcement history | [Official, prior knowledge] |
| Turkey | RPM prohibited; Competition Board enforces regularly, including online price monitoring and discount caps; Law 7416 limits large marketplaces (own brand sales, use of seller data, tied services) | [Official, prior knowledge and Secondary] |
| US | Unilateral MAP policies (announce policy, stop supplying violators) are generally allowed federally (Colgate doctrine); minimum resale price agreements judged under rule of reason federally (Leegin) but some states treat RPM as per se illegal | [Official, prior knowledge] |
| Gulf | Competition laws exist in UAE and KSA; check with counsel before any reseller price policy | [Unverified detail] |

Rule for this system: never draft messages to resellers about their prices, never propose discount caps or price monitoring with sanctions in the EU, UK or Turkey. In the US, MAP policy drafting goes to counsel through `compliance`.

## 3. Lawful design levers

| Lever | How it reduces conflict | Example |
|-------|------------------------|---------|
| Assortment split | Different SKUs per channel avoid direct price comparison | DTC exclusive bundles and colors; marketplace multipacks with own GTIN |
| Pack and size architecture | Different unit counts and price points | 3-pack on Amazon, single unit and refill subscription on DTC |
| Value-add instead of price cut on DTC | Gift with purchase, free engraving, extended guarantee | DTC promotion without visible price drop |
| Coordinated calendar | Marketplace events and DTC events aligned so prices do not cross | Plan Prime Day and Black Friday prices for all channels together |
| Price corridor per hero SKU | Defined floor and ceiling per channel, set by the brand for its own sales | Own DTC and own marketplace offers stay within 0 to 5% of each other [illustrative] |
| Distribution control (lawful) | Fewer, authorized distributors; selective distribution where lawful; contracts on quality standards, not prices | Authorized reseller program with service standards |
| Brand tools | Brand Registry, Transparency, Project Zero (Amazon); brand authorization on Turkish marketplaces; bol brand content | Remove counterfeits, keep content control |
| Marketplace exclusive products | Products designed for marketplace price points | Private label sub-brand |

## 4. Unauthorized resellers: lawful handling

1. Identify: who sells, where they source (test buys), condition, authenticity.
2. Counterfeit or materially different goods: file through Brand Registry, Project Zero, platform IP tools; keep evidence.
3. Genuine goods resold: exhaustion of trademark rights generally allows resale of genuine goods first sold in the EEA (EU) or first sale doctrine (US); action is limited. Fix supply leaks in your distribution (contracts, allocation, serialization) rather than chasing resellers' prices.
4. Never file false IP complaints to remove competitors (account and legal risk).
5. Escalate patterns to `market-intel` (monitoring) and `compliance` (legal options).

## 5. Price parity checks before any visible price change

| Check | Data | Pass |
|-------|------|------|
| Featured offer risk | Amazon price vs DTC and other channels after the change | Amazon price not materially above other public prices for the same item |
| 1P matching risk | Vendor SKUs affected | Amazon matching would not break margin agreements |
| Retail partner shelf prices | Partner price list | No undercut of agreed shelf price on own channels (brand sets its own prices only) |
| Reference price law | 30 day (EU, UK) or 10 day (TR) prior price per channel | Discount claims valid |
| Marketplace campaign commitments | Joined campaigns and price locks | No conflict |
| Feed and ads | Shopping feeds and marketplace prices in sync | `commerce-feeds` informed |

Output: a channel price map per hero SKU (DTC, each marketplace, retail) with dates and sources, reviewed monthly.

## 6. Cannibalization vs incrementality

Questions to answer before scaling a marketplace for a DTC brand:
- Of marketplace buyers, how many would have bought on DTC? Proxy: branded search share on the marketplace (SQP brand queries) vs category queries. High branded share means more cannibalization risk; category share means new demand.
- Does marketplace presence raise DTC brand search (halo) or lower it? Track Google Search Console brand clicks and DTC direct traffic before and after marketplace launch, with a control market if possible.
- Contribution comparison: marketplace CM3 per unit vs DTC contribution per unit after acquisition investment. A sale shifted from DTC to a marketplace with lower contribution is a loss even if marketplace ROAS looks good.

Design: launch marketplaces country by country and compare DTC trends in launched vs not yet launched countries (staggered rollout as a natural experiment) [Practitioner method; handoff to `measurement`].

## 7. Decision procedure for a conflict incident

```
1. Detect: featured offer loss, partner complaint, DTC drop, price undercut alert
2. Snapshot: prices on all channels (date, time, source), featured offer status, stock
3. Classify cause: own price change | promotion | reseller | platform campaign | 1P matching | repricer
4. Options (at least 3): revert own price, exclude SKU from promotion, swap to exclusive SKU, adjust campaign participation, change distribution allocation
5. Model contribution impact per option across channels
6. Change request (G3) with rollback; journal entry; handoff to pricing-strategy and offer-strategy
7. Post-incident: update the channel price map and calendar rules
```

## 8. Template: channel price map

```
| SKU | GTIN | DTC price | Amazon (store) | bol | Trendyol | Hepsiburada | Retail shelf (public) | Corridor rule | Last check | Issues |
```

Keep it in `ads-master/outputs/marketplaces/YYYY-MM-DD_marketplaces_channel-price-map.md` and refresh monthly and before every event.

## 9. Worked example: exclusive pack design [Illustrative]

Situation: a DTC skincare brand sells a 50 ml serum at EUR 29.95 on DTC and wants Amazon.de and bol without a direct price comparison.

| Option | Amazon.de and bol | DTC | Conflict risk | Contribution note |
|--------|-------------------|-----|---------------|-------------------|
| Same SKU, same price | 50 ml at EUR 29.95 | 50 ml at EUR 29.95 | Medium: any DTC promotion can suppress the Amazon featured offer | Marketplace CM3 lower than DTC per unit, but new demand |
| Same SKU, lower marketplace price | 50 ml at EUR 26.95 | EUR 29.95 | High: DTC loses, retail partners complain | Cannibalization likely |
| Marketplace 2-pack with own GTIN | 2 x 50 ml at EUR 54.95 | Single at EUR 29.95, set with cleanser at EUR 44.95 | Low: different configurations | Higher AOV covers fulfillment fee |
| DTC exclusive refill subscription | Not listed | Refill 50 ml at EUR 24.95 subscription | Low | Repeat economics on DTC |

Decision rule: choose the option with the highest combined contribution across channels after the expected cannibalization, and document it in `DECISIONS.md`.

## 10. Vendor (1P) price matching protocol

1. List vendor ASINs that also sell on DTC or through retailers with public prices.
2. Before any DTC or retailer promotion, estimate the matching exposure: Amazon may lower its retail price to the lowest public price it finds; vendor margin agreements and retailer relations then absorb the gap.
3. Options: exclude 1P ASINs from DTC promotions, use DTC exclusive SKUs for promotions, use value-adds instead of price cuts, time-box promotions and note that matching may persist after the promotion ends.
4. Track net PPM and price changes on vendor ASINs weekly during and after promotions.
5. Never contact Amazon or retailers to demand price changes on behalf of the brand through an agent; humans manage commercial relationships.

## 11. US MAP policies (only with counsel)

- A unilateral MAP policy usually restricts advertised prices, not selling prices, and is enforced by the brand's own decision to stop supplying, not by agreements. State law differs.
- Marketplaces do not enforce a brand's MAP. Amazon decides featured offers on its own rules; listing below MAP is a reseller decision.
- Agent role: build the price monitoring data (with `market-intel`) and the channel price map; drafting, publishing or enforcing a MAP policy is a legal and commercial decision for humans and counsel via `compliance`.
- Never apply US MAP logic in the EU, UK or Turkey.

## 12. Channel conflict checklist (monthly)

- [ ] Channel price map refreshed for all hero SKUs.
- [ ] Featured offer and buybox history reviewed for drops linked to price events.
- [ ] Upcoming DTC, retail and marketplace events aligned on one calendar.
- [ ] Exclusive SKUs and packs performing; no leakage of DTC exclusives to marketplaces through resellers.
- [ ] Unauthorized sellers list updated; counterfeit cases filed with evidence.
- [ ] No price instructions or discount caps in any reseller communication.
- [ ] Cannibalization indicators (DTC brand search, DTC new customers) stable.
