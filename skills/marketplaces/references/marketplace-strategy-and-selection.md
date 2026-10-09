# Marketplace Strategy and Selection

> Which marketplace, when, with which assortment and in which role. Knowledge as of 2026-10. Market sizes and fees move every year: verify with the Freshness Protocol in SKILL.md before using any number in a decision.

## 1. The role of a marketplace in the channel mix

Decide the role before the marketplace. Every marketplace plays one or more of five roles:

| Role | What it means | Typical KPI | Example |
|------|---------------|-------------|---------|
| Demand capture | Buyers already search the marketplace for the category; you need shelf presence | Organic share, featured offer %, TACoS | Amazon for consumables in the US, Germany, UK |
| Primary sales channel | Most revenue comes from the marketplace (private label, resellers) | Marketplace CM3, stock turns | Private label on Amazon; reseller on Trendyol |
| Market entry | Test a new country without local site, logistics or payments | Sell-through, CM3 at small scale, reviews | bol.com for NL and BE, Allegro for Poland, noon for UAE and KSA |
| Brand control | You list because others already sell your product badly | Content ownership, featured offer, MAP corridor (where lawful) | Brand owner taking back Amazon from unauthorized resellers |
| Clearance and long tail | Sell slow stock or SKUs not worth DTC traffic | Recovery rate vs liquidation | eBay, outlet programs, Amazon Outlet |

Rule: write the role into `STRATEGY.md` per marketplace. A demand capture marketplace is judged on share and TACoS; a market entry marketplace on learning and contribution at small scale; a brand control marketplace on content and price stability.

## 2. Marketplace landscape for the markets this system serves (2026)

| Market | Leading marketplaces | Notes | Label |
|--------|---------------------|-------|-------|
| US | Amazon, Walmart Marketplace, eBay, Etsy, TikTok Shop, Temu and Shein (cross-border), Amazon Haul for under USD 20 | Walmart New-Seller Savings runs 2026-02-02 to 2027-01-31 | [Official, 2026] for Walmart program |
| UK and DE, FR, IT, ES | Amazon (dominant), eBay, Zalando (fashion), Otto and Kaufland (DE), Cdiscount (FR), TikTok Shop | Amazon EU cut fees from 2026-01-05 | [Official, 2025-12] |
| Netherlands and Belgium (Flanders) | bol.com (dominant local), Amazon.nl and Amazon.com.be, Zalando, TikTok Shop (NL and BE live 2026-06-15) | bol strongest in books, toys, home, electronics, baby | [Official, 2026-06] for TikTok Shop |
| Poland, CZ, SK, HU | Allegro (dominant in PL; allegro.cz, .sk, .hu), Amazon.pl, Temu | Allegro reported 4.2 million customers on its international sites | [Secondary, 2025] |
| Turkey | Trendyol, Hepsiburada (Kaspi.kz owns about 66%), Amazon.com.tr, n11, Pazarama, Çiçeksepeti (gifts) | Hepsiburada FY2025 GMV TRY 257.5B (IAS 29 restated), marketplace 68.4% of GMV | [Official, 2026-02] |
| Gulf (UAE, KSA) and Egypt | Amazon.ae, Amazon.sa, Amazon.eg, noon (UAE, KSA, Egypt), Amazon Bazaar (low price, KSA and UAE), Namshi (fashion) | noon storage fee rises 2026-10-01 | [Official noon help, 2026] |

Market share numbers differ by source and definition (GMV vs orders, 1P plus 3P). Never quote a share without source and date. Use `market-intel` for current share of search and traffic estimates.

## 3. Selection scorecard

Score each candidate marketplace 1 to 5 on every criterion, multiply by the weight, and keep the evidence in the output file.

| Criterion | Weight | How to score | Evidence |
|-----------|--------|--------------|----------|
| Category demand on the marketplace | 20% | Search volume for top 20 category keywords on the marketplace; number of competing listings with over 100 ratings | Brand Analytics (if registered), keyword tools, panel search reports, `market-intel` |
| Contribution after all fees | 20% | Marketplace CM3 per unit for hero SKUs at expected price and ACoS | [Unit economics](marketplace-unit-economics.md) model |
| Competitive intensity | 10% | Price spread and review counts of top 10 results; presence of the marketplace's own label | Manual SERP check, Keepa or equivalent price history |
| Operational fit | 10% | Fulfillment options, delivery promise you can meet, returns handling, language | [Operations](operations-fulfillment-and-account-health.md) |
| Channel conflict risk | 15% | Overlap with DTC and retail customers; price corridor feasibility | [Channel conflict](channel-conflict-with-dtc.md) |
| Ads maturity and cost | 10% | Retail media products available, CPC levels, reporting depth, API | [Amazon Ads](amazon-ads.md), [bol](bol-com.md), [Turkey](trendyol-and-hepsiburada.md) |
| Regulatory and compliance load | 5% | EPR registrations (DE, FR packaging and WEEE), product safety (GPSR in the EU), Turkish e-commerce rules, Gulf registrations | `compliance` |
| Team and integration effort | 10% | Integration tool support (ChannelEngine, Channable, Sentos, Dopigo, ikas, Linnworks), API access, language | [Tools](tools-api-mcp.md) |

Decision rule: launch only on marketplaces scoring 3.5 or higher weighted, with positive CM3 on at least 3 hero SKUs at the expected price. Under 3.0, document why and revisit in 6 months.

## 4. Sequencing: which marketplace first

```
Is the brand already sold on the marketplace by others?
  Yes -> Brand control first: Brand Registry or equivalent, take content ownership, decide authorized seller policy (no price instructions)
  No  -> Is the home market served by one dominant marketplace?
           NL or BE -> bol.com first, Amazon.nl second
           TR       -> Trendyol and Hepsiburada together if operations allow; Trendyol first for fashion and fast moving consumer goods, Hepsiburada first for electronics and appliances [Practitioner consensus]
           PL       -> Allegro first
           DE, UK, US, FR, IT, ES -> Amazon first
           UAE, KSA -> Amazon.ae or Amazon.sa and noon; choose by category fit and fulfillment network
         Expand to the second marketplace only when the first runs at stable CM3, in-stock above 98% and healthy account metrics for 90 days.
```

Pan-EU expansion on Amazon (Pan-European FBA, Remote Fulfillment, Multi-Country Inventory) needs VAT registrations in storage countries, EPR registrations and translated listings. Model storage country VAT before enabling Pan-EU. [Official, prior knowledge]

## 5. Assortment split vs DTC

| Assortment type | Marketplace | DTC | Why |
|-----------------|-------------|-----|-----|
| Hero SKUs searched by name | Yes | Yes | Customers search the marketplace; absence hands the sale to competitors or resellers |
| Starter sizes and single units | Yes | Optional | Acquisition on marketplace, repeat on DTC through inserts is not allowed on most marketplaces; rely on brand recall instead |
| Bundles and kits exclusive to DTC | No | Yes | Avoids direct price comparison and gives DTC a reason to exist |
| Marketplace exclusive packs (multipacks with own GTIN) | Yes | No | Separate price point without undercutting DTC single unit |
| Subscriptions | Amazon Subscribe and Save where economics allow | DTC subscription with more value | Subscribe and Save discount is funded by the seller [Official, prior knowledge] |
| New launches | After DTC launch window (2 to 6 weeks) or at the same time if reviews are needed fast | First | Protects launch economics and early adopters on DTC |
| Low margin or bulky SKUs | Only if CM3 positive after fulfillment | Maybe | Bulky fees and storage often make them negative on FBA |
| Clearance | Outlet programs or secondary marketplaces | Not discounted publicly | Protects reference prices |

Rule: inserts or packaging that ask marketplace buyers to leave the marketplace, leave a review in exchange for something, or visit your site for a discount break policy on Amazon and most marketplaces. Brand recall comes from packaging, product quality and Brand Store follow programs, not from diverting buyers.

## 6. Business model differences

| Business model | Main goals | Main risks | First moves |
|----------------|-----------|-----------|-------------|
| Brand owner (manufacturer with own brand) | Content control, featured offer, organic share, halo on retail and DTC | Unauthorized resellers, price erosion, counterfeit | Brand Registry, Transparency or Project Zero where available, A+ and Brand Store, authorized distribution, brand defense ads test |
| Reseller (sells other brands) | Featured offer share at margin, assortment breadth, operations efficiency | Thin margins, IP complaints, authenticity claims, repricer wars | Invoices from authorized sources, repricer with floor prices, account health discipline, category approvals |
| Private label | Rank on category keywords, reviews, ads efficiency | Copycats, review attacks, ad dependency, fee shocks | Differentiated product, Vine for first reviews, launch ad plan with TACoS glidepath |
| DTC brand adding marketplaces | Incremental reach without cannibalizing DTC | Price undercut, margin loss, customer data loss | Assortment split, price corridor, measure halo and cannibalization |
| Vendor (1P) | Retail relationship with Amazon or bol as buyer | Margin agreements, chargebacks, loss of price control | Negotiation calendar, chargeback audits, decide 1P vs 3P per SKU |

## 7. Amazon 1P vs 3P decision (also bol Retail vs Partner)

| Factor | 1P (Vendor Central, bol as retailer) | 3P (Seller Central, bol Partner Program) |
|--------|--------------------------------------|------------------------------------------|
| Price control | Retailer sets retail price | Seller sets price |
| Margin | Wholesale price minus allowances, co-op, chargebacks | Retail price minus fees |
| Data | Vendor reports (Retail Analytics) | Business Reports, Brand Analytics |
| Cash flow | Payment terms (often 60 to 90 days) | Payout every 2 weeks (Amazon), bol pays on schedule |
| Operational burden | Purchase orders and compliance with retailer logistics manuals | Listings, pricing, stock, customer service |
| Ads | Same ad products; Vendor click attribution 14 days on Sponsored Products | Seller click attribution 7 days on Sponsored Products [Secondary, 2026] |

Hybrid is common: 1P for high volume, low touch SKUs; 3P for new launches, long tail and controlled pricing. Document the per SKU decision in `DECISIONS.md`.

## 8. Launch plan template

```
# Marketplace launch plan: <marketplace> <country> | Date | Owner
## Role and goals (role, 90 day targets: sales, CM3, TACoS, ratings, in-stock)
## Scorecard result (weighted score, evidence links)
## Assortment (SKU list, GTINs, exclusive packs, excluded SKUs and why)
## Price plan (marketplace price per SKU, DTC price, corridor check, reference price history)
## Fee model per SKU (link to unit economics output)
## Fulfillment and logistics (FBA, LVB, Trendyol or Hepsiburada fulfillment, own warehouse; delivery promise; returns)
## Compliance (EPR, GPSR, labeling, certificates, category approvals, Turkish e-commerce rules)
## Listing pack status (titles, bullets, images, A+, backend terms, translations)
## Reviews plan (Vine or platform programs, Request a Review cadence)
## Ads launch (structure, budgets, ACoS targets by intent, TACoS glidepath)
## Measurement (Attribution tags, Brand Analytics, halo test design)
## Risks and stop conditions
## Approvals needed (G3 lines)
## Handoffs requested
```

## 9. Exit and pause rules

Pause or exit a marketplace when one of these is true for 2 consecutive quarters and the fix list has been tried:
- Marketplace CM3 negative after ads on more than 50% of revenue.
- Featured offer share on own brand below 80% because of authorized partners undercutting (then fix distribution, not prices).
- Account health incidents that the team cannot operationally prevent.
- Cannibalization test shows DTC loss larger than marketplace contribution gain.

Exiting is a G3 decision. Draft it in `DECISIONS.md` via `growth-orchestrator`, never close listings or delete ASINs (G4).
