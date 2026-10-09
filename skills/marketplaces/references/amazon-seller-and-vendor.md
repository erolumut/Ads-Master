# Amazon Seller Central and Vendor Central

> Knowledge as of 2026-10. Amazon announces most changes inside Seller Central (News, Seller Forums announcements) behind a login. Many 2026 details below come from secondary sources quoting those notices; items marked [Unverified] must be checked in the live account before a decision. Use the `ads-verify` skill when a decision depends on one.

## 1. Account types and programs

| Program | What it is | Who needs it | Notes |
|---------|-----------|--------------|-------|
| Seller Central Professional | 3P selling account with monthly subscription and API access | Every serious seller | Individual plan has per item fee and no API or ads |
| Unified account (EU, NA) | One account for several marketplaces in a region | Multi-country sellers | Separate VAT, EPR and listing languages per country |
| Vendor Central | 1P: Amazon buys wholesale via purchase orders | Invited brands | Payment terms, co-op, chargebacks; see section 9 |
| Brand Registry | Brand protection and brand tools for trademark owners | Brand owners and private label | Unlocks A+, Brand Store, Sponsored Brands, Brand Analytics, Vine, Attribution bonus, Transparency eligibility |
| Transparency, Project Zero | Unit level serialization (Transparency), self-service counterfeit removal (Project Zero) | Brands with counterfeit or reseller problems | Availability differs by marketplace |
| Amazon Business | B2B pricing, quantity discounts, business-only offers | Office, industrial, supplies | Separate price tiers can create parity questions |
| Subscribe and Save | Recurring orders with discount funded by the seller | Consumables | Model the discount in CM3 |
| Amazon Haul | Ultra-low price storefront (most items under USD 10 or 20 equivalents) | Invited sellers, mostly factories that hit price points | Amazon said Haul serves 25 locations with more planned in 2026 [Official, 2025-12]; invitation only [Secondary, 2026] |
| Amazon Bazaar | Low price app and storefront in several markets including KSA and UAE | Low price sellers | Status per market [Unverified] |

## 2. The Featured Offer (Buy Box)

The Featured Offer is the offer in the buy box on the product page. Most sales on a detail page go to it, and Sponsored Products ads only serve when the advertiser holds it [Official, prior knowledge].

### 2.1 What changed in 2026
- Amazon removed seller performance as a standalone eligibility gate for the Featured Offer. Announced in Seller Forums on 2026-07-06 (some sources say 2026-07-08); US rollout from early July, EU and UK from 2026-07-20, global completion expected by end of 2026. All offers now enter one ranking; performance signals still weigh inside it [Secondary, multiple, 2026-07].
- Practical effect: more offers compete, including sellers previously locked out (and some brand owners who could not win their own listing). Winning still depends on price, delivery speed and promise, stock and service quality.

### 2.2 Featured offer drivers (in practice)

| Driver | What to check | Action |
|--------|---------------|--------|
| Landed price (item plus shipping) | Your price vs other offers, vs external prices Amazon sees | Keep price competitive within the corridor; check external price (Amazon's price competitiveness policies can suppress the featured offer when a lower price is found elsewhere) |
| Delivery speed and promise | Prime badge, FBA vs FBM handling time, Seller Fulfilled Prime eligibility | FBA or SFP for hero SKUs; shorten handling time |
| Stock | In stock, enough units | Restock plan, safety stock |
| Seller performance | ODR, late shipment, cancellations, valid tracking, customer service response | Account health discipline (section 5) |
| Fulfillment channel | FBA offers often win ties | FBA for hero SKUs if economics allow |

### 2.3 Suppression and "No featured offer"
If no offer meets Amazon's pricing expectations (for example, price far above recent or external prices), the page can show "See All Buying Options" with no featured offer. Ads then do not serve. Check: Pricing Health page in Seller Central, Featured Offer eligibility per ASIN, recent price history. Fix with price, not with ads.

## 3. Fees (summary; full model in unit economics)

### 3.1 US 2026 [Secondary quoting Official notice, 2025-12 and 2026-01]
- Effective 2026-01-15. Referral fee percentages unchanged (reported unchanged since January 2024).
- FBA fulfillment fees rose on average about USD 0.08 per unit (Amazon framed it as under 0.5% of an average item price); Amazon said no new FBA fee types in 2026.
- Low-Price FBA rates apply automatically to items priced under USD 10.
- Amazon ended US FBA prep and labeling services from 2026-01-01: every unit must arrive prepped and labeled. Inbound defects now cost more.
- Low inventory level fee extended to Small Bulky and Large Bulky (per FNSKU; grocery exempt) [Secondary].
- A 3.5% fuel and logistics surcharge on US FBA fees from 2026-04-17 is reported by one third-party source only [Unverified].

### 3.2 Europe 2026 [Official, aboutamazon.eu, 2025-12]
- Average fee reduction of GBP 0.15 or EUR 0.17 per unit sold, described as Amazon's largest European fee cut.
- Referral cuts, for example: Home products up to EUR 20 or GBP 20 from 15% to 8%; Pet clothing and food up to EUR 10 from 15% to 5%; Grocery and vitamins up to EUR 10 from 8% to 5%.
- FBA parcel fulfillment fees reduced by an average of GBP 0.26; Low-Price FBA eligibility expanded; deal fee caps lowered.
- Effective 2026-01-05 (brought forward from 2026-02-01), with some FBA parcel and clothing changes from 2025-12-15 [Contested dates; check the dated notice per store].
- Offsetting increases on storage, return to seller and liquidation fees and some FBA changes in smaller stores (net about EUR 0.02 per FBA unit from those lines).
- Digital services fee surcharge passes local digital services tax rates through on some fees (for example France) [Unverified detail].

### 3.3 Gulf and Turkey
Amazon.ae, Amazon.sa and Amazon.com.tr publish their own fee schedules. No 2026 change was confirmed in research. Pull the live rate card per category before modeling [Unverified].

## 4. Inventory and capacity (FBA)

| Topic | 2026 state | Label |
|-------|-----------|-------|
| Capacity limits | Monthly capacity allocation in cubic feet, based on sales forecasts and performance | [Secondary, 2026] |
| Inventory Performance Index (IPI) | Below 400 triggers restrictions in several reports | [Unverified threshold] |
| Storage fees | Peak (October to December) rates are about 3 times off-peak for standard size | [Secondary, 2026] |
| Aged inventory surcharge | Steeper tiers in 2026 | [Secondary, 2026] |
| Low inventory level fee | Charged when historical days of supply is too low on standard and now bulky items | [Secondary, 2026] |
| Inbound placement service fee | Charged for minimal split shipments; lower or zero for Amazon optimized splits | [Official, 2024 onwards, prior knowledge] |

Target: 4 to 8 weeks of cover in FBA plus a buffer in a 3PL or Amazon Warehousing and Distribution (AWD) for replenishment. Detail in [Operations](operations-fulfillment-and-account-health.md).

## 5. Account health

| Metric | Target | Notes |
|--------|--------|-------|
| Account Health Rating (AHR) | Healthy band (200 or more on the 0 to 1,000 scale) | Below 200 at risk; 100 or less can lead to deactivation [Secondary, 2025-12] |
| Order Defect Rate (ODR) | Under 1% | Negative feedback, A-to-z claims, chargebacks |
| Late Shipment Rate (FBM) | Under 4% | 10 and 30 day windows |
| Pre-fulfillment Cancel Rate (FBM) | Under 2.5% | Stock sync is the usual cause |
| Valid Tracking Rate (FBM) | Over 95% | Per category rules |
| Policy compliance | Zero open violations | IP complaints, product authenticity, safety, restricted products, listing policy |

2026 operational changes reported for US FBM sellers (verify): SAFE-T claim window shortened to 30 days on 2026-01-21; refunds to be issued within 4 calendar days from 2026-01-26; Amazon sets minimum order handling capacity; custom return instructions field removed in August 2026 [Secondary, 2026; Unverified].

Appeals procedure: [Operations](operations-fulfillment-and-account-health.md) section 6.

## 6. Listings and catalog basics

- Catalog is shared: one detail page per product (ASIN), many offers. The brand owner with Brand Registry has strongest content authority, but other contributors can still influence attributes. Monitor detail page changes weekly.
- Variations (parent and child) group sizes and colors; reviews pool across variations. Never merge unrelated products (policy violation and review abuse).
- GTIN exemptions exist for private label and handmade where the brand is registered.
- Title rules since 2025-01: 200 characters maximum including spaces for most categories, no special characters such as ! $ ? _ { } ^ unless part of the brand, and no word repeated more than twice (except prepositions, articles and conjunctions) [Official, 2025-01, prior knowledge]. Category style guides can be stricter.
- Generative AI listing tools: Enhance My Listing (announced 2025-05) suggests titles, bullets, attributes and descriptions; Amazon reported over 900,000 sellers used its generative AI listing tools and that sellers accept AI content without edits over 90% of the time [Official via TechCrunch, 2025-05]. Treat every AI suggestion as a draft: check facts against PRODUCT_FACTS.md and claims against CLAIMS.md before accepting.

Full listing method: [Listing optimization](listing-optimization.md).

## 7. Brand tools (Brand Registry)

| Tool | Use | Key settings |
|------|-----|--------------|
| A+ Content (Basic, Premium A+ where eligible) | Visual product description modules; comparison charts | Comparison chart to cross-sell; keep alt text factual |
| Brand Story | Brand carousel above A+ | Link to Brand Store |
| Brand Store | Multi-page brand site on Amazon | Pages per category; Store insights (section-level insights added January 2026 [Secondary]) |
| Brand Analytics | Search Query Performance, Top Search Terms, Market Basket, Repeat Purchase, Demographics | Weekly pulls; see [Measurement](measurement-and-halo.md) |
| Amazon Attribution | Tags for off-Amazon traffic | Required for Brand Referral Bonus |
| Brand Referral Bonus | Credit on referral fees for sales driven by external traffic with Attribution tags, about 10% on average, 14 day window | Category rates differ [Secondary, 2026] |
| Vine | Reviews from invited reviewers | See [Reviews](reviews-and-ratings.md) |
| Manage Experiments | A/B tests of title, main image, bullets, description, A+ | Needs enough traffic; run 8 to 10 weeks |
| Customer Engagement (follow emails) | Email to brand followers | No discounts that violate policy; G3 because it reaches customers |
| Product Opportunity Explorer | Niche demand and search data | Use for launch research |

## 8. Events calendar (Amazon)

| Event | 2026 date | Notes | Label |
|-------|-----------|-------|-------|
| Prime Day | 2026-06-23 to 2026-06-26 (moved from July; Mexico ran 7 days) | Deal submissions close weeks earlier | [Official, 2026] |
| Prime Big Deal Days | 2026-10-06 to 2026-10-07 (Australia 2026-09-29 to 2026-10-05) | Second Prime event | [Official, 2026] |
| Black Friday and Cyber Monday | 2026-11-27 and 2026-11-30 | Peak storage fees apply October to December | [Calendar] |

Plan stock 8 to 12 weeks before any event because of capacity limits and inbound delays.

## 9. Vendor Central (1P) essentials

| Topic | What to manage | Check |
|-------|---------------|-------|
| Cost price and terms | Annual negotiation; allowances (co-op, damage allowance, freight) | Effective net margin after allowances |
| Purchase orders | Confirm, accept, ship per routing; fill rate | Fill rate, on-time |
| Chargebacks (operational) | Labeling, ASN, carton content errors | Monthly chargeback report; dispute within the window |
| Shortage claims | Units received less than invoiced | Dispute with proof of delivery |
| Retail price | Amazon decides; may match external prices | Watch for price matching against DTC or retail promotions |
| Reports | Retail Analytics (sales, traffic, inventory, net PPM) | Weekly |
| Ads | Same products; Sponsored Products click attribution 14 days for vendors | Compare windows correctly vs seller accounts |

1P risk: a DTC or retailer promotion can trigger Amazon to match the lower price, which then drags margin agreements and other retailers. Coordinate every visible DTC price change with `pricing-strategy`.

## 10. Weekly Seller Central routine

1. Account Health dashboard: any new warnings, policy violations, AHR change.
2. Featured offer percentage by child ASIN (Business Reports > Detail Page Sales and Traffic by Child Item).
3. Inventory: days of cover, stranded and suppressed listings, inbound status, capacity.
4. Pricing Health: suppressed featured offers, Fair Pricing alerts.
5. Voice of the Customer: CX health per ASIN, return reasons.
6. Ads: see [Retail media bidding](retail-media-bidding-and-structure.md) weekly review.
7. Detail page changes: title, images, bullets edited by others.
8. Reviews: new 1 to 3 star reviews; product issues to `market-intel` and the product team.
