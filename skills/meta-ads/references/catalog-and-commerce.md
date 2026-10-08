# Catalog and Commerce

> Knowledge as of 2026-10. Boundary: feed creation, feed rules, attribute optimization and multi-platform catalog hygiene belong to `commerce-feeds`. This module covers how Meta uses the catalog in ads, the settings, and the checks that matter for delivery.

## 1. Catalog foundations

| Item | Standard | Check |
|------|----------|-------|
| Catalog | One catalog per brand and market set, in the business portfolio, connected to the dataset | Commerce Manager > Catalog > Events: dataset connected |
| Data source | Scheduled feed (hourly or daily), platform integration (Shopify, WooCommerce, BigCommerce), or Catalog Batch API for large catalogs | Last update time, error count |
| ID matching | content_ids in Pixel and CAPI events equal catalog `id` (or `retailer_id`) | Events Manager / Commerce Manager match rate; target 90%+ [Practitioner consensus] |
| Required fields | id, title, description, availability, condition, price, link, image_link, brand | Diagnostics tab: no blocking errors |
| Strongly recommended | sale_price, sale_price_effective_date, google_product_category or fb_product_category, item_group_id for variants, additional_image_link, video (where supported), custom_label_0 to 4 | Feed audit by `commerce-feeds` |
| Availability sync | Out of stock items marked quickly | Stock changes reflected within hours |
| Country and language | Country and language feeds or overrides for each market | Localized titles and prices per market |

## 2. Advantage+ catalog ads

Advantage+ catalog ads (formerly dynamic product ads) personalize products shown per person using catalog and event signal [Official].

Setup in a Sales campaign:
1. Turn on the catalog option at campaign or ad set level (label varies, "Advantage+ catalog ads" or "Catalog").
2. Choose catalog and product set.
3. Audience: Advantage+ audience (broad: Meta finds people likely to buy any product), or retarget viewers and add to cart users (custom audience based on catalog events, no expansion) when separate retargeting is justified.
4. Ad format: carousel, collection, or single image or video with catalog. Options include showing catalog videos, dynamic media (product videos where in the feed), catalog frames and overlays (price, discount, free shipping), and AI-generated catalog imagery or backgrounds where available [Unverified availability].
5. Add a lifestyle intro card or video as the first carousel card for brand context.

Product set strategy:
| Product set | Rule | Use |
|-------------|------|-----|
| All in stock | availability = in stock | Default broad catalog |
| Best sellers | custom_label = bestseller (from backend sales last 30 days) | Highest efficiency |
| High margin | custom_label = margin_high | Profit-led scaling, ROAS goal |
| New arrivals | custom_label = new_30d | Launch visibility |
| Price bands | price ranges | Match creative and audience intent |
| Exclude | low margin, low stock, restricted items | Waste and policy control |
Custom labels are set by `commerce-feeds`; request them via journal with the logic.

## 3. Catalog in non-catalog ads

- Product extensions or "show products" under a regular ad: lets an image or video ad show catalog products below it [Official, availability varies].
- Shops ads and onsite checkout: Meta has moved away from Facebook and Instagram onsite checkout in most markets, sending buyers to the website checkout [Unverified current state by market]. Check whether Shops destination options still exist in the account before planning.
- Collaborative ads: brands selling through retailers can run catalog ads using the retailer's catalog segment and measure sales on the retailer site [Official]. Use when the brand does not own checkout.

## 4. Collection ads and Instant Experiences

Collection: a cover video or image with product tiles below, opening a full-screen Instant Experience.

Instant Experience templates [Official]:
| Template | Use |
|----------|-----|
| Instant storefront | Catalog grid, ecommerce browsing |
| Instant lookbook | Lifestyle images with tagged products |
| Instant customer acquisition | Landing-page-like flow driving to the site |
| Instant storytelling | Brand story, launches |

When to use: mobile-heavy audiences, slow websites (Instant Experience loads fast), product discovery. Measure on site purchases; Instant Experience engagement is not a conversion.

## 5. Diagnostics

| Symptom | Check | Fix |
|---------|-------|-----|
| Catalog ads not delivering | Catalog connected to dataset, product set size, items approved | Fix rejections, widen product set |
| Retargeting catalog audience tiny | Event match to catalog IDs | Align content_ids; fix variant IDs (item_group_id) |
| Showing out of stock items | Feed update frequency | Hourly feeds or API updates |
| Wrong prices in ads | Currency, sale_price dates, tax display rules | Feed fix; country overrides |
| Many items rejected | Commerce policy (prohibited products, image text, misleading claims) | Policy review, request review |
| Poor carousel CTR | Image quality, white backgrounds only | Lifestyle images, additional_image_link, frames |

## 6. Measurement for commerce

- Purchase events with value, currency, content_ids and contents (id, quantity, item_price).
- Product-level breakdowns in Ads Manager (product ID breakdown for catalog ads) to identify hero products and drains.
- Margin: send margin bands as custom labels, not raw cost data. If value optimization should chase profit, `measurement` decides whether to send profit as value.
- Retention: send repeat purchases with customer identifiers so audience segments classify existing customers correctly.

## 7. Threads and other placements for catalog

Advantage+ catalog ads can deliver on Threads with image and image carousel formats [Official, 2025 via secondary; formats limited]. Keep Advantage+ placements on and read placement breakdowns cautiously.

## 8. Commerce playbook by tier

| Tier | Catalog role |
|------|-------------|
| Starter | Optional; one catalog ad in the core campaign if the catalog is clean |
| Growth | Separate catalog campaign or catalog ads within the main sales campaign; bestseller product set |
| Scale | Catalog campaigns by margin tier with value optimization; seasonal product sets; collaborative ads if wholesale |
| Enterprise | Market-level catalogs with localized feeds via API, automated custom labels from BI, catalog video at scale |

## 9. Seasonal catalog checklist (BFCM, sales)

1. sale_price and sale_price_effective_date loaded for the event window (with `commerce-feeds`).
2. Catalog frames or overlays showing discount, approved by human.
3. Product sets for "on sale" and "gift ideas" prepared.
4. Stock buffers: exclude items with less than N units in stock.
5. Feed update frequency raised to hourly during the event.
6. Post-event: remove sale prices on time to avoid misleading price policy issues.

## 10. Vertical catalogs beyond retail

Meta supports catalog types beyond products for verticals where inventory changes constantly [Official, long-standing; availability varies by market]:
| Catalog type | Typical use | Key fields | Signal events |
|-------------|-------------|-----------|---------------|
| Hotels | Hotel and lodging | hotel_id, name, address, base_price, image | Search, ViewContent, InitiateCheckout, Purchase with check-in and check-out dates |
| Flights | Airlines and OTAs | origin_airport, destination_airport, price | Search and ViewContent with route parameters |
| Destinations | Travel inspiration | destination_id, name, types, price | ViewContent with destination IDs |
| Home listings | Real estate (special ad category Housing applies in many markets) | home_listing_id, address, price, availability | ViewContent, Lead |
| Vehicles / automotive inventory | Dealers and marketplaces | vehicle_id, make, model, year, mileage, price, VIN where required | ViewContent, Lead |
| Media titles | Streaming and entertainment | title_id, genre | ViewContent, Subscribe |
For housing, employment and financial offers in catalogs, special ad category rules still apply to targeting.

## 11. Catalog for marketplaces and multi-seller businesses

- Split catalogs or product sets by category and margin; marketplaces often have thin margins on some categories.
- Use custom labels for seller tier, commission rate, and return rate so product sets can exclude unprofitable inventory.
- For two-sided marketplaces, run catalog ads for the demand side only; acquire supply with Leads campaigns.
- Very large catalogs (millions of items): use the Catalog Batch API, keep IDs stable, and prioritize feed freshness for price and availability.

## 12. Worked example: catalog restructure (ecommerce, Scale tier)

Situation: 4,000 SKUs, one "All products" set, catalog ads spend 25k per month, ROAS falling, 30% of spend on 5% margin accessories.
1. Request custom labels from `commerce-feeds`: margin band (high, mid, low), bestseller (last 30 days units), stock depth.
2. Build product sets: High margin bestsellers, High margin other, Mid margin, exclude Low margin and stock under 5 units.
3. Campaign A: catalog ads on High margin sets with highest value bidding; Campaign B: Mid margin with cost per result goal at breakeven.
4. Add one lifestyle video intro card per set.
5. Read product ID breakdown after 14 days; move drains out of sets weekly.
6. Validate with backend gross profit per order, not platform ROAS alone.

## 13. Catalog API snippets (read only)

```
GET /{CATALOG_ID}?fields=name,product_count,vertical
GET /{CATALOG_ID}/product_sets?fields=id,name,filter,product_count
GET /{CATALOG_ID}/products?fields=retailer_id,name,availability,price,review_status&limit=100
GET /{CATALOG_ID}/diagnostics   (field availability varies by version)
```
Writes to catalogs (feeds, product updates) belong to `commerce-feeds` and require human approval.
