# Collection Pages and Filters

Product list pages (PLP): filters and facets, sorting, product cards, quick add, load more vs pagination, back navigation and out-of-stock handling. Patterns P17 to P25 in the [Pattern library](ux-pattern-library.md).

## 1. Evidence snapshot

| Finding | Source | Label |
|---------|--------|-------|
| 58% of desktop and 78% of mobile leading sites mediocre or worse on product lists and filtering; 21,000+ manually scored parameters, 170+ US and EU sites | Baymard Product List UX 2025 (updated 2025-09-09) | [Study, 2025-09] |
| 28% of sites lack an at-a-glance overview of applied filters | Baymard 2025 | [Study, 2025-09] |
| 34% of sites with poor filtering; abandonment 67% to 90% on weak toolsets vs 17% to 33% on lightly optimized ones | Earlier Baymard benchmark | [Study, pre-2025] |
| 42% of sites do not combine variations into one list item | Baymard mobile 2026 | [Study, 2026] |
| Users distrust perfect ratings from few reviews, which top "User rating" sorts | Baymard | [Study] |
| Load more with lazy loading performed best; infinite scroll harmful on search and mobile | Baymard via Smashing Magazine | [Study, 2016] |
| Horizon defaults to auto-loading products with URL updates and filter state in history | Horizon 4.2.0 source | [Official, 2026-09] |

## 2. Filter design procedure

1. **Pick filters per category** from customer decision criteria: search refinements, support questions, review language, competitor filters. Apparel: size, color, fit, length, material, price. Electronics: compatibility, capacity, brand, price, rating. Furniture: dimensions, material, color, delivery time.
2. **Fix the data first**: filters are only as good as product attributes. Use metafields (Shopify), attributes (Woo), properties (Shopware), attributes (Magento). Normalize values ("Navy", "navy blue", "dark blue" become one value with a swatch). Hand catalog attribute gaps to `commerce-feeds` (same attributes power feeds).
3. **Order filters** by usage: the top 4 to 6 visible or expanded on desktop; the rest collapsed.
4. **Values**: show counts; hide or disable values that would return zero; sort sizes logically (XS to XXL, 36 to 46), colors with swatches and names, others by count.
5. **Price**: typed min and max inputs plus optional slider; respect market currency.
6. **Multi-select within a group is OR, across groups is AND**; state it implicitly by behavior and counts.

## 3. Filter UI specification

Desktop:
- Left sidebar (catalogs with many filter groups) or horizontal filter bar with dropdown panels (fewer groups, image-led grids). Do not hide all filters behind a "Filter" button on desktop.
- Apply on change with results updating in place (no full reload), URL updated, focus kept on the control.
- Applied filters chips above results with "Clear all" (P18).

Mobile:
- "Filter and sort" button sticky at the top of the grid with the active filter count ("Filter (3)").
- Full-height drawer (modal dialog) with groups as accordions, sizes and colors as tap targets of at least 44 px.
- Footer inside the drawer: "Clear" and "See 128 items" (count live). Apply on tap of "See items" or live-apply with the count updating; either way keep the count visible.
- Close returns focus to the "Filter and sort" button.

Accessibility:
- Each group `<fieldset><legend>Size</legend>` with checkbox inputs; swatches are checkboxes with visible or visually hidden color names.
- Result count in `role="status"` (Horizon `blocks/filters.liquid` uses `role="status"` spans).
- Price slider has numeric inputs (WCAG 2.5.7 Dragging Movements).
- Do not move focus to the results on each change; announce instead.

Performance:
- Filter interaction must stay under 200 ms INP: debounce price input, render results with section rendering (Liquid) or `startTransition` (React), keep the grid's image dimensions fixed.

URL and SEO:
- Filter state in query parameters (`filter.v.option.size=M`, `filter.p.m.custom.material=linen` on Shopify). Indexation of filtered URLs is an `seo` decision (canonical, noindex or curated landing pages); never change it without that handoff.

Reference implementations: Horizon `blocks/filters.liquid`, `snippets/list-filter.liquid`, `snippets/price-filter.liquid`, `snippets/filter-remove-buttons.liquid`, `assets/facets.js` (history push state, role status counts, 4.2.0 fix for price inputs wiped mid-edit); WooCommerce `client/blocks/assets/js/blocks/product-filters/inner-blocks/` (active-filters, attribute-filter, checkbox-list, chips, clear-button, price-filter, price-slider, rating-filter, removable-chips, status-filter, taxonomy-filter); Next.js Commerce `components/layout/search/filter/` (URL-driven sort and collections).

## 4. Sorting

| Option | Default for | Notes |
|--------|-------------|-------|
| Featured or best selling | Category PLPs | Curated plus sales velocity; sold-out last |
| Relevance | Search results | Never "Featured" on search |
| Newest | Fashion, drops | |
| Price low to high, high to low | All | Use the market price after discounts |
| Customer rating | All with reviews | Weighted by count (Bayesian average), show count on cards |

Sort control: native `<select>` with label "Sort by" or a primitive listbox; mobile inside the filter drawer or as a separate sheet.

## 5. Product card anatomy

Order (top to bottom): image (aspect ratio fixed across the grid), swatches (up to 5 plus "+N"), title (2 lines max, then ellipsis with full title in the link), price block (price, compare-at, unit price where required), rating (stars plus count, only if 1+ review), one badge (Sale, New, Sold out, Low stock only if real), optional quick add.

Rules:
- Grid: 2 columns on mobile for most catalogs (1 column for large-image fashion is TF), 3 to 4 on desktop.
- Second image on hover only for `(hover: hover) and (pointer: fine)`.
- One link target (the title link) with the whole card clickable via an overlay; buttons inside the card (swatches, quick add) sit above the overlay.
- Price text: compare-at in `<s>` with visually hidden "Regular price" label; sale price labeled "Sale price".
- Unit price on cards for grocery, cosmetics, beverages and other unit-priced goods in the EU (Directive 98/6/EC; Germany PAngV).
- No 4-badge stacks; no "Only 2 left" unless inventory says so.

Reference implementations: Horizon `snippets/product-card.liquid`, `blocks/_product-card.liquid`, `blocks/_product-card-gallery.liquid`, `snippets/price.liquid`, `snippets/unit-price.liquid` (uses `unit_price_with_measurement` and `<bdi>`), `snippets/swatch.liquid`; 4.2.0 serves smaller card images in 2-column mobile grids.

## 6. Variant grouping

- Group color or material variants under one card with swatches when users shop by style (apparel, furniture). Show separate cards when users browse by color (paint, yarn) and test it.
- Shopify: combined listings (parent product, child products per color) or single product with variants; `product_option_value.product_url` lets swatches link to the right child.
- Swatch click on a card updates the image and the card link to that variant (no navigation).

## 7. Quick add rules

| Product type | Quick add? | Why |
|--------------|-----------|-----|
| Single variant, consumable, accessory | Yes | Repeat purchases, low risk |
| Apparel and footwear with sizes | Test (TF) | Speed vs wrong size and returns |
| Configurable or high-AOV | No | Needs PDP information |
| B2B catalogs | Quick order list instead | Bulk entry |

Implementation: quick add opens a small dialog only when options exist, shows option buttons and price, adds and opens the cart drawer. Horizon `assets/quick-add.js` (since 4.2.0 loads only when enabled).

## 8. Loading more products

Recommendation: "Load more" button with lazy loading and URL updates for consumer PLPs and search [Study, 2016]. Infinite auto-loading (Horizon default) is acceptable on category PLPs only if the URL updates, Back restores position and the footer stays reachable; treat switching between them as TF on high-traffic stores [Contested].

Specification:
- Initial page 24 to 48 items; button text "Show 24 more (48 of 312)".
- `history.pushState` or `replaceState` with `?page=N` so Back and shared links restore the position; on return, scroll to the last viewed product.
- Crawlable paginated URLs remain available for bots (`seo` decides rel and canonical).
- After loading, focus stays on the button (which moves below new items) or moves to the first new product; announce "24 more products loaded".
- Prefer pagination (numbered) for B2B and very large catalogs where users return to a position.

Reference implementations: Horizon `assets/paginated-list.js` (IntersectionObserver auto-load, push state per page); Hydrogen `PaginatedResourceSection.tsx` (cursor pagination with Load more and Load previous).

## 9. Collection header and content

- H1 (category name), product count, one-line description; subcategory chips under it.
- Long SEO copy below the grid, collapsed (`seo` owns content).
- Banners in the grid at most 1 per 12 products, never pushing the first row below the fold on mobile.

## 10. Out-of-stock policy

- Default: sold-out products sorted last; "In stock" filter available; sold-out cards labeled.
- Remove from lists only when discontinued (then redirect PDPs per `seo`).
- Variant-level stock: if the filtered size is sold out for a product, either hide that product under the size filter or label "Size M sold out" (Shopify filters by variant availability when the availability filter is on).

## 11. Measurement

Events (spec to `measurement`): `view_item_list` with list name, `select_item` with index, `filter_apply` (group, value), `filter_remove`, `sort_change`, `load_more` (page), `quick_add`. KPIs: PLP to PDP rate, filter usage and filter exit rate, products viewed per PLP session, ATC from PLP (quick add), RPV.
