# bol (bol.com): Netherlands and Belgium

> Knowledge as of 2026-10. bol publishes partner rules, fees and changes in the Partner Platform (partnerplatform.bol.com), Seller Help (Verkopershulp, "Tarieven en vergoedingen") and developers.bol.com. Third-party blogs quote very different commission numbers; always read the live rate card in your seller account before modeling. Numbers below are labeled.

## 1. Why bol

- Largest local marketplace in the Netherlands and Flanders, with strong loyalty (bol Select membership) and a delivery promise culture ("before 23:59 ordered, tomorrow delivered") [Practitioner consensus].
- Categories where bol is strongest: books, toys, baby, home and garden, electronics accessories, personal care, sports, pet [Practitioner consensus].
- Belgium: bol serves Flanders natively; listings and customer service in Dutch. French language coverage for Wallonia should be checked before planning [Unverified].
- Competes with Amazon.nl and Amazon.com.be, Coolblue (retail, not an open marketplace for most categories), Zalando (fashion), and TikTok Shop (NL and BE live since 2026-06-15) [Official TikTok newsroom, 2026-06].

## 2. Account models

| Model | What it is | When |
|-------|-----------|------|
| Partner program (verkopen via bol) | You sell as a third-party partner on bol | Most brands and resellers |
| Supplier (leverancier) | bol buys from you as retailer (1P) | Larger brands invited by bol category teams; bol sets the retail price |
| Both | Partner offers alongside bol's own retail offer | Possible on the same product; compete for the buy block |

The buy block ("koopblok") is bol's featured offer. Only the offer in the buy block can show Sponsored Products ads [Official, bol supplier help]. Drivers are price, delivery promise, stock and partner performance [Practitioner consensus; bol does not publish weights].

## 3. Fees

| Fee | Structure | Source and label |
|-----|-----------|------------------|
| Commission | Fixed amount per item plus a percentage of the sales price (incl. VAT), by product category; published under "Tarieven en vergoedingen" and updated periodically | [Official structure; exact rates per account] |
| Reported commission ranges | Third-party sources disagree (for example fixed EUR 0.20 to 2.48 plus 4.1% to 20.7%; others quote 7% to 17%). The fixed fee is set by product type and by sale price incl. VAT | [Contested, 2026] Use the account rate card |
| Food and 2026 promotions | Food variable commission 4.0% to 6.0% (one 2026 source); a temporary 25% discount on variable commission for items newly added to selected categories from 2026-07-20 to 2026-12-31 (one snippet); bol may adjust category rates twice a year | [Unverified]; the binding rates are in the seller account and the partner platform commission page |
| Logistiek via bol (LVB) | Per order fulfillment fee by size class (3XS, XXS, XS, S and up) plus storage and inbound | New tariffs for 3XS and XXS from 2026-09-09 reported [Secondary, 2026-09]; amounts per rate card |
| Verzenden via bol (VVB) | bol shipping labels for self-fulfilled orders at contracted rates | Peak surcharge in November and December reported (about 40%) [Secondary, 2026] |
| Sponsored Products | CPC, auction | [Official] |
| Subscription | Monthly partner fee may apply depending on program and period | [Unverified] check account |

Model the full stack in [Unit economics](marketplace-unit-economics.md). Remember: bol commission is calculated on the price including VAT, so a VAT inclusive price change moves the commission too.

## 4. Fulfillment: LVB vs own fulfillment

| Factor | LVB | Own fulfillment (with or without VVB) |
|--------|-----|----------------------------------------|
| Delivery promise | bol controls; strong next-day promise | You must hit the promise you set; late delivery hurts score and buy block |
| Buy block | Often favored for speed and reliability [Practitioner consensus] | Competitive if promise and performance are strong |
| Returns | bol handles | You handle |
| Cost | Per unit fee plus storage; small items are cheap, bulky items expensive | Your warehouse plus carrier |
| Control | Less (stock in bol warehouse) | Full |
| Peak | Inbound deadlines before Sinterklaas and Black Friday | Carrier capacity and surcharges |

Rule: LVB for fast moving small and medium SKUs that compete for the buy block; own fulfillment for bulky, slow or fragile items and for brands with a strong NL warehouse.

## 5. Listings on bol

| Element | Rule of thumb | Note |
|---------|---------------|------|
| Product content | bol has one product page per EAN; content comes from bol's catalog and suppliers or brand content | Brands improve content via content upload; partners with low authority cannot override everything |
| EAN | Required; one EAN per product variant | Missing or wrong EAN creates duplicates and lost buy block |
| Title | Brand + product type + key attribute + size or variant, in Dutch | Follow bol category template |
| Description | Clear Dutch copy, specs in attributes | Attributes feed filters; fill every relevant attribute |
| Images | Main image on white, multiple angles, in-use images | Check bol image specs per category |
| Reviews | Customer reviews on product page; partner rating separate | See [Reviews](reviews-and-ratings.md) |
| Delivery promise | Set the promise you can meet; it shows on the offer | Promise misses damage performance metrics |

Translation: native Dutch copy written for NL and BE. Machine translation without review produces errors in product attributes and claims; route copy through `compliance` for claims.

## 6. Partner performance

bol measures partner performance on customer satisfaction and service: delivery on time per promise, cancellations, response time on customer questions, returns handling and customer ratings of the partner (shown as a score out of 10 on offers) [Practitioner consensus; exact norms and thresholds in the Partner Platform, Unverified]. Breaching performance norms can lead to warnings, offers going offline or account restrictions.

Weekly check: partner performance dashboard in the seller account, open customer questions (answer within 24 hours), cancellations, late deliveries, returns with reasons.

## 7. bol Retail Media (Sponsored Products and more)

### 7.1 Products [Official, retailmedia.bol.com and partnerplatform.bol.com]

| Product | What | Notes |
|---------|------|-------|
| Sponsored Products | CPC ads in search results and product pages for offers in the buy block | Conversions counted within 14 days of a click; since a 2026-08-27 update, 6 ad positions show in the bol app and mobile web instead of 4, same as desktop |
| Display onsite | Native banners on homepage, category and product pages | Mostly brand budgets via bol retail media team |
| Display offsite | Banners on premium sites and social (Facebook, Instagram, Pinterest) using bol shopper data | Creative must use the advertiser's look and feel, no bol logo or fonts, include "Available at bol" or "Exclusive at bol"; images at least 1080 x 1080 |
| Social advertising | Campaigns using bol shopper data on social | Consideration goals |

### 7.2 Sponsored Products structure on bol

```
Campaign per product group (margin band) and intent
  Automatic targeting campaign (discovery), lower bid
  Manual keyword campaign for top Dutch terms (brand, category)
  Product or category targeting where available
Daily budget per campaign; ACoS target per product group
```

Practice:
- Keywords are Dutch (and Flemish variants). Build the keyword list from bol search suggestions, Amazon.nl Brand Analytics (if available), Google Search Console Dutch queries and `market-intel`.
- Reported CPCs: EUR 0.10 on long tail to EUR 1.50 or more on competitive electronics terms; other sources estimate EUR 0.30 to 0.60 [Secondary, 2026; Unverified]. Use your own data after 2 weeks.
- Reported average ad spend of 5% to 15% of revenue for bol sellers comes from a blog without a method [Unverified]; set TACoS targets from your contribution model.
- Ads stop when the offer loses the buy block or goes out of stock: watch both daily in peak season.
- Because the 2026-08-27 change added mobile positions, compare mobile performance before and after that date separately.

### 7.3 Advertising API
bol's Advertising API manages Sponsored Products campaigns, budgets and performance reports. Its documentation sits in the Retailer API v11 tree (`advertising-api/aapi-overview`) and it uses the same client credentials (JWT) flow as the Retailer API. Reported versions: 11.0 (2023-12-20) and 11.1 (2025-09-03), with v9 and v10 removed [Unverified: official docs seen only in search summaries; read the release notes on api.bol.com before building].

## 8. Retailer API (v10)

- v10 is the live version; v8 and v9 were removed in December 2024; deprecated resources are removed after at least 12 months of support [Official, developers.bol.com].
- Several v10 offer endpoints are marked deprecated in the reference (create offer, offer export, unpublished offer report): plan migration to the replacement endpoints listed in the release notes [Official, 2026].
- The Commission Beta endpoint was not made generally available and was unsupported from 2026-03-01 [Official, 2026-01].
- Use: offers, prices, stock, orders, shipments, returns, inbound for LVB, insights (offer insights, performance), commission calculation via the supported endpoint.
- Detail and MCP options: [Tools, APIs and MCP](tools-api-mcp.md).

## 9. Calendar for NL and BE

| Event | Date | Prep |
|-------|------|------|
| Black Friday and Cyber Monday | Late November | LVB inbound deadlines; reference price rules (EU 30 day prior price) |
| Sinterklaas | 5 December (gift peak from mid November) | Toys, books, gifts: stock and LVB capacity |
| Christmas | December | Delivery cut-offs |
| Back to school | August | School supplies, electronics |
| King's Day | 27 April | Orange items, outdoor |
| Mother's Day and Father's Day | May and June (second Sunday of May; third Sunday of June in NL) | Gifts |

EU price indication rules apply to every "was" price on bol: the prior price is the lowest price in the 30 days before the discount (Omnibus). The Dutch regulator ACM actively fines misleading discounts. Coordinate discounts with `offer-strategy` and `compliance`.

## 10. bol audit quick list

| Check | Pass condition |
|-------|----------------|
| Buy block share on own EANs | Above 95% |
| Partner rating | 8.5 or higher out of 10 and stable [Practitioner consensus] |
| Customer questions answered | Within 24 hours |
| Delivery promise met | No late delivery warnings |
| Content completeness | All key attributes filled, at least 5 images on hero products |
| Sponsored Products structure | Split by product group and intent; negatives in place; ACoS targets from contribution |
| LVB stock cover | 4 to 8 weeks, peak stock planned 8 weeks ahead |
| Price vs DTC and Amazon.nl | Within corridor; no undercut by bol promotions you joined |
| API version | On v10, no deprecated endpoints without a migration plan |
