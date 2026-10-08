# UX Pattern Library

The core module. 62 storefront patterns, each with its job, evidence label, when to use it, anti patterns, implementation notes, accessible markup notes and the reference repos that show a good implementation. Pattern IDs (P01 to P62) are used in audits, change lists and the [Audit checklist](audit-checklist.md).

Evidence labels follow the spec: `[Official, YYYY-MM]`, `[Study, YYYY or YYYY-MM]`, `[Practitioner consensus]`, `[Contested]`, `[Unverified]`. Baymard figures are from public summaries of paywalled research; the month is given where the article states it. Repo paths are relative to the repo root and were read on 2026-10-08 (see [Reference repos](reference-repos.md)). Never copy repo code verbatim; the recipes in [Shopify implementation](platform-implementation-shopify.md) and [Headless implementation](platform-implementation-headless.md) are original minimal versions.

Lane key: **TS** = table stakes, implement directly as a diff after approval, measure before/after. **TF** = test first, hand to `cro` with a hypothesis. **TS/TF** = the defect fix is TS, the design variant is TF.

## A. Navigation and homepage
### P01 Category-first main navigation (TS)
- Job: let shoppers reach any product family in one or two steps using the words they use.
- Evidence: 58% of desktop and 67% of mobile leading sites are mediocre or worse on homepage and category navigation [Study, 2025]; 33% of mobile sites do not make product categories the top level items [Study, older Baymard article].
- Use when: always. Top level items are product categories (or needs), not "Shop", "Collections", "New" only.
- Avoid: brand-speak labels, more than about 8 top level items on desktop, burying categories under one "Shop" item.
- Build: derive labels from search logs and competitor nav; 1 to 3 levels; each level has a "Shop all <category>" link.
- A11y: `<nav aria-label="Main">`, lists of links, current page `aria-current="page"`.
- Repos: Horizon `blocks/_header-menu.liquid`, `assets/header-menu.js`; Dawn `sections/header.liquid`.

### P02 Desktop mega menu as disclosure (TS/TF)
- Job: show the full scope of deep catalogs so users skip levels.
- Evidence: NN/g reports mega menus work well when grouped and scannable; organize items in columns [Study, NN/g]; Horizon ships several mega menu layouts [Official, 2025-05].
- Use when: 3+ levels or 30+ subcategories. Small catalogs use a simple dropdown or no dropdown.
- Avoid: hover-only opening with no delay (accidental opens), ARIA `role="menu"` for site navigation, images that push links below the fold, menus that close when the pointer crosses a gap.
- Build: open on click and on hover with intent delay (about 150 to 250 ms), close on Escape and outside click, keep open while pointer travels diagonally.
- A11y: disclosure pattern: `<button aria-expanded aria-controls>` per top item, panel is a list of links. Do not trap focus. Escape returns focus to the trigger.
- Repos: Horizon `assets/header-menu.js`, Radix `packages/react/navigation-menu`, Base UI `packages/react/src/navigation-menu`.

### P03 Mobile menu drawer with drill-down (TS)
- Job: full category access on a phone without endless accordions.
- Evidence: hidden navigation is less discoverable and used later in tasks (179 participants) [Study, NN/g hamburger study]; NN/g 2025 update: icon is recognized but the risks remain [Study, 2025].
- Use when: always on mobile; pair with visible category chips or tiles on the homepage (P04).
- Avoid: nested accordions three deep, menu that scrolls the page behind it, no "Back" control, no "Shop all".
- Build: slide-in panels per level with a Back button and level title; search field at the top of the drawer; account and locale links at the bottom.
- A11y: modal drawer (native `<dialog>` or Base UI Drawer/Dialog), focus first heading, return focus to the menu button, `overscroll-behavior: contain` on the panel.
- Repos: Horizon `assets/header-drawer.js`; Next.js Commerce `components/layout/navbar/mobile-menu.tsx` (Headless UI Dialog).

### P04 Full scope links on mobile homepage (TS)
- Job: avoid users thinking a narrow promo selection is the whole category.
- Evidence: 59% of mobile homepages do not provide the full scope for links [Study, 2025]; 58% of apps miss it [Study, 2026].
- Use when: any homepage that features subsets ("Summer dresses") on mobile.
- Avoid: only promo tiles with no route to the full category tree.
- Build: a "Shop by category" block with every top level category, above the fold or directly below the hero.
- A11y: real links with visible text, not text baked into images.
- Repos: Horizon `sections/collection-list.liquid`, `sections/collection-links.liquid`.

### P05 Hero with one job, no auto-rotation (TS/TF)
- Job: state what the store sells and give one primary path.
- Evidence: auto-forwarding carousels reduce visibility and annoy users [Study, NN/g]; WCAG 2.2.2 requires pause for motion over 5 seconds [Official, W3C].
- Use when: every homepage. Test the message (TF), not whether a hero exists.
- Avoid: auto-rotating slideshows, text in images, video heroes that delay LCP, three competing CTAs.
- Build: one image or short muted loop with poster, headline, subline, one primary CTA, one secondary text link; hero image is the LCP element with `fetchpriority="high"` and no lazy loading.
- A11y: if any motion: visible pause control; `prefers-reduced-motion` stops it.
- Repos: Horizon `sections/hero.liquid`, `sections/slideshow.liquid` (has controls).

### P06 Homepage sections with explicit jobs (TS)
- Job: each section answers one question: what, why us, what is popular, what is new, proof, how to buy.
- Evidence: [Practitioner consensus]; Baymard flags homepage among the weakest areas [Study, 2025].
- Use when: always; order sections by the job sequence for cold traffic.
- Avoid: sections added by apps with no owner, duplicate product carousels, newsletter popups on first paint.
- Build: section inventory with job, owner, data source and KPI (see [Homepage and navigation](homepage-and-navigation.md)).
- A11y: one `h1`, logical heading order per section.
- Repos: Horizon `templates/index.json` (section stack).

### P07 Announcement bar with true information (TS)
- Job: surface one fact that removes a purchase blocker (shipping threshold, delivery cut-off, returns window).
- Evidence: unexpected extra costs are the top checkout abandonment reason in Baymard surveys (secondary sources disagree on the exact share) [Study, 2025] [Contested on the number].
- Use when: there is a real, stable fact. Rotation only if each message is visible long enough and pausable.
- Avoid: fake countdowns, discount codes that do not work in all markets, more than 3 rotating messages.
- Build: single line, market-aware text from settings or market metafields; links to the policy.
- A11y: rotating bars need pause; do not use `aria-live` for auto-rotation.
- Repos: Horizon `sections/header-announcements.liquid`, `assets/announcement-bar.js`.

### P08 Breadcrumbs and intermediary category pages (TS)
- Job: orientation and lateral movement in deep catalogs.
- Evidence: Baymard names taxonomy, main navigation and intermediary category pages as the areas with most room to improve [Study, 2025].
- Use when: 2+ category levels. Intermediary pages show subcategory tiles plus bestsellers, not a 3,000 item list.
- Avoid: breadcrumbs that reflect the browsing path only (inconsistent), breadcrumbs on mobile that wrap to 4 lines.
- Build: hierarchy-based breadcrumb; on mobile show only the parent link.
- A11y: `<nav aria-label="Breadcrumb">` with ordered list, last item `aria-current="page"`. Structured data: hand to `seo`.
- Repos: Saleor Paper storefront (`/{locale}/{channel}` routing), Medusa `src/modules/categories`.

### P09 Footer as utility hub (TS)
- Job: answer service questions (shipping, returns, contact, size help, payment methods, legal, locale).
- Evidence: WCAG 2.2 SC 3.2.6 Consistent Help requires help mechanisms in a consistent location [Official, W3C 2023-10].
- Use when: always.
- Avoid: 60 SEO links, missing contact route, policies only as PDF.
- Build: service links first, then categories, then company and legal; locale selector and payment icons.
- A11y: `<footer>` with headed link groups; accordions on mobile use `<details>` or disclosure buttons.
- Repos: Horizon `sections/footer.liquid`, `blocks/footer-policy-list.liquid`.

## B. On-site search
### P10 Visible search field (TS)
- Job: give high-intent users the fastest path; searchers convert higher in most stores [Practitioner consensus, vendor claims vary].
- Evidence: 46% of desktop, 58% of mobile and 64% of app sites are mediocre or worse on search [Study, 2026].
- Use when: catalogs above about 30 SKUs. Desktop: open field in header. Mobile: field visible on homepage and PLP, icon elsewhere.
- Avoid: icon only on desktop for large catalogs, search that opens a modal with no field focus.
- Build: `<form role="search" action="/search">` with `type="search"`, `enterkeyhint="search"`, 16px font on mobile.
- A11y: visible label or `aria-label`, clear button with name.
- Repos: Horizon `blocks/_search-input.liquid` (`role="search"`, reset button with label).

### P11 Predictive search (autocomplete) (TS)
- Job: suggest queries, categories and products while typing so users form better queries.
- Evidence: 80% of sites offer autocomplete but only 19% implement it fully; 69% of sites risk misleading users through poor misspelling support in autocomplete [Study, Baymard].
- Use when: catalogs above about 50 SKUs.
- Avoid: more than about 10 suggestions, suggestions that do not copy into the field when selected via keys, product-only results without query suggestions, flicker from out-of-order responses.
- Build: debounce about 150 to 250 ms, abort stale requests, show query suggestions plus scoped category suggestions plus 4 to 6 products with price and image, recent searches when empty.
- A11y: ARIA combobox: input `role="combobox" aria-expanded aria-controls aria-autocomplete="list"`, `aria-activedescendant` for the highlighted option, options in `role="listbox"`, Escape closes, result count announced politely.
- Repos: Horizon `assets/predictive-search.js` (200 ms debounce, AbortController, arrow keys, Escape) and `sections/predictive-search.liquid`; React Aria `Autocomplete.tsx`, `ComboBox.tsx`; Hydrogen skeleton `app/components/SearchFormPredictive.tsx`.

### P12 Typo tolerance, synonyms and stemming (TS)
- Job: return results for "jakcet", "sneakers" vs "trainers", plurals and abbreviations.
- Evidence: Baymard describes 12 query types (exact, product type, feature, thematic, symptom, compatibility, slang and others) [Study]; Spring '26 coverage reports Shopify search now tolerates typos [Unverified, 2026-06].
- Use when: always; synonym lists come from the zero result report and customer language.
- Avoid: one-way synonyms that pull irrelevant products, synonyms with spaces in Shopify Search & Discovery if the theme breaks on them [Unverified, third-party help 2026-05].
- Build: weekly synonym review from zero results and low CTR queries ([Search and merchandising](search-and-merchandising.md)).
- A11y: "Showing results for X" text announced, with a link to search the original query.
- Repos: Meilisearch and Typesense docs (typo tolerance settings) for headless; Shopify Search & Discovery app for Liquid.

### P13 Zero results recovery (TS)
- Job: never dead-end a searcher.
- Evidence: [Practitioner consensus]; Shopify Analytics provides a no-results search report [Official].
- Use when: always.
- Avoid: "No results" with nothing else, a 404-style page.
- Build: repeat the query, spelling suggestion, popular categories, bestsellers, contact or chat link; log the query.
- A11y: heading that states the outcome; suggestions as links.
- Repos: Horizon `sections/search-results.liquid`, `sections/predictive-search-empty.liquid`.

### P14 Search results page with scope and filters (TS)
- Job: narrow large result sets and keep the query.
- Evidence: 94% of sites do not let mobile shoppers search within the current category [Unverified, secondary summary of Baymard]; 37% of apps do not persist the query [Study, 2026].
- Use when: always for catalogs with filters.
- Avoid: query cleared from the field on the results page, different filters than the PLP, infinite scroll on search results (Baymard found it harmful on search) [Study, 2016].
- Build: keep the query in the field, show category scope chips and the same filter component as PLP, sort by relevance default.
- A11y: result count in a polite live region after filter changes.
- Repos: Horizon `sections/search-results.liquid`, `sections/search-header.liquid`; Next.js Commerce `app/search/page.tsx`.

### P15 Search merchandising rules (TF)
- Job: route exact category queries, pin or boost products for business goals without hurting relevance.
- Evidence: [Practitioner consensus].
- Use when: queries that map to a category ("dresses") or brand; seasonal boosts.
- Avoid: boosting out-of-stock or low-margin items by default, redirects that strip filters.
- Build: redirects for exact category terms, pins for top 20 queries, boosts by margin label agreed with `offer-strategy`.
- A11y: redirected users see a note "Showing the Dresses category for 'dresses'".
- Repos: Shopify Search & Discovery (product boosts, synonyms); Algolia rules; Athos Commerce (Klevu, Searchspring) merchandising.

### P16 SKU, part number and quick order (TS for B2B)
- Job: let repeat and B2B buyers order by code.
- Evidence: Shopify predictive search does not search SKU by default per a vendor report [Unverified, 2026]; Horizon ships quick order lists for B2B [Official, 2025].
- Use when: B2B, spare parts, consumables, catalogs with codes on packaging.
- Avoid: SKU search that requires exact case, quick order without stock feedback.
- Build: include SKU and barcode in the search index; quick order list with quantity inputs and line errors.
- A11y: table with header cells, quantity inputs with labels naming the product.
- Repos: Horizon `sections/quick-order-list.liquid`, `assets/quick-order-list.js`.

## C. Collection and category pages (PLP)
### P17 Category-specific filters (TS)
- Job: let users narrow by the attributes that matter in that category.
- Evidence: 58% of desktop and 78% of mobile sites mediocre or worse on product lists and filtering (21,000+ scored parameters, 170+ sites) [Study, 2025-09]; 34% had poor filtering in an earlier benchmark [Study, older].
- Use when: categories with 20+ products.
- Avoid: one global filter set for all categories, filter values that return zero products, filters only in a hidden drawer on desktop.
- Build: desktop sidebar or horizontal bar with the top 4 to 6 filters visible; mobile full-height drawer with "See N items" button; counts per value; price range with typed inputs.
- A11y: each group is `<fieldset>` with `<legend>`; checkboxes are real inputs; the result count updates in `role="status"`; slider has numeric input alternative (WCAG 2.5.7 Dragging Movements).
- Repos: Horizon `blocks/filters.liquid`, `assets/facets.js`, `snippets/price-filter.liquid`; WooCommerce `client/blocks/assets/js/blocks/product-filters/inner-blocks/*`; Next.js Commerce `components/layout/search/filter/`.

### P18 Applied filters overview (TS)
- Job: show what is applied and allow one-tap removal.
- Evidence: 28% of sites lack an overview of applied filters [Study, 2025-09].
- Use when: any filtering.
- Avoid: applied state visible only inside collapsed groups.
- Build: chips above results with remove buttons and "Clear all"; URL holds the state.
- A11y: chip buttons named "Remove filter: Size M"; after removal move focus to the next chip or the results heading.
- Repos: Horizon `snippets/filter-remove-buttons.liquid`; WooCommerce `product-filters/inner-blocks/removable-chips`, `active-filters`.

### P19 Sort options that match intent (TS)
- Job: let users reorder by price, newness, rating, relevance.
- Evidence: users distrust perfect ratings from few reviews, which sort to the top under "User rating" [Study, Baymard].
- Use when: always.
- Avoid: "Featured" as the only meaningful option, rating sort that ignores review count.
- Build: default to best selling or curated; rating sort uses a count-weighted score; persist in URL.
- A11y: native `<select>` with label, or a listbox from a primitive library.
- Repos: Horizon `snippets/sorting.liquid`.

### P20 Product card with decision info (TS)
- Job: let users choose which PDP to open without pogo-sticking.
- Evidence: 81% of sites do not display price per unit on PDPs [Study, 2026]; EU law requires unit prices for many goods [Official, Directive 98/6/EC].
- Use when: always.
- Avoid: price hidden until hover, 4 badges per card, whole card as a link wrapping buttons (nested interactive).
- Build: image (second image on hover only for pointer devices), title, price and compare-at, unit price where required, swatches with count ("+4"), rating with count, at most one badge.
- A11y: one primary link (title) with the card made clickable via a pseudo-element; sale prices with visually hidden "Regular price" and "Sale price" text.
- Repos: Horizon `snippets/product-card.liquid`, `blocks/_product-card.liquid`, `snippets/unit-price.liquid`; Next.js Commerce `components/grid/tile.tsx`.

### P21 Combine variations into one list item (TS)
- Job: stop near-duplicate variants from flooding lists.
- Evidence: 42% of sites do not combine variations into one list item [Study, 2026].
- Use when: color or material variants shown as separate products.
- Avoid: separate cards per color with identical titles; or the opposite when colors are what users browse.
- Build: Shopify combined listings or a parent product with swatches; swatch click updates image and link.
- A11y: swatches are buttons or radios with color names, not color only.
- Repos: Horizon `snippets/variant-swatches.liquid`, `blocks/swatches.liquid`; Liquid `product_option_value.product_url` supports combined listings.

### P22 Quick add (TF)
- Job: add simple items from the list without a PDP visit.
- Evidence: [Contested]: speeds repeat purchases and consumables; can cause wrong-size purchases and returns in apparel.
- Use when: single-variant or 1-option products, consumables, B2B. Test for apparel.
- Avoid: quick add for products that need size guidance, quick view modals that duplicate the PDP poorly.
- Build: button opens a small variant panel only when options exist; feedback via cart drawer (P35).
- A11y: button name includes product ("Add Linen Shirt to cart"); panel is a dialog.
- Repos: Horizon `assets/quick-add.js` (loads JS only when enabled since 4.2.0).

### P23 Load more with URL state (TS/TF)
- Job: progressive loading that keeps footer access and back-button position.
- Evidence: "Load more" with lazy loading performed best; infinite scroll harmful on search and mobile [Study, Baymard 2016, still referenced]; Horizon defaults to auto-loading with `history.pushState` [Official, 2026-09] [Contested].
- Use when: PLPs above 24 to 48 items. Pagination for very large B2B lists where position matters.
- Avoid: infinite scroll without URL updates, losing scroll position on Back, hiding the footer.
- Build: button "Show 24 more (of 312)"; update `?page=` with `pushState`; restore position on Back; crawlable paginated URLs (hand to `seo`).
- A11y: after loading, move focus to the first new item or announce "24 more products loaded".
- Repos: Horizon `assets/paginated-list.js`; Hydrogen `app/components/PaginatedResourceSection.tsx`.

### P24 Result count and scope header (TS)
- Job: tell users where they are and how much there is.
- Evidence: [Practitioner consensus].
- Use when: every PLP and search page.
- Avoid: long SEO text above products (move below the grid, hand to `seo`).
- Build: H1, product count, 1-line description, subcategory chips.
- A11y: count in the heading region; update politely after filtering.
- Repos: Horizon `blocks/_collection-info.liquid`.

### P25 Out-of-stock handling in lists (TS)
- Job: avoid dead ends while staying honest.
- Evidence: [Practitioner consensus].
- Use when: catalogs with frequent stockouts.
- Avoid: sold-out items ranked first, hiding all sold-out items when users need them for back-in-stock.
- Build: sort sold-out last; "In stock only" filter; card label "Sold out" with notify option on PDP.
- A11y: status in text, not greyed-out image only.
- Repos: Horizon `snippets/product-badges-styles.liquid` and badges logic in `snippets/product-card.liquid`.

## D. Product detail page (PDP)
### P26 Gallery with scale, zoom and video (TS)
- Job: let users judge appearance, size and quality.
- Evidence: only 55% of sites decent or better on product images; 91% do not provide in-scale images [Study, 2025].
- Use when: always; minimum about 5 images including in-scale and detail; video where motion explains.
- Avoid: lifestyle-only images, zoom that needs hover, carousels with dots only on mobile.
- Build: swipeable gallery on mobile with counter ("2 of 7"), thumbnails on desktop, pinch zoom, variant image switching.
- A11y: alt text that describes the view; buttons named "Next image"; zoom dialog with Escape; video captions and no autoplay with sound.
- Repos: Horizon `blocks/_product-media-gallery.liquid`, `assets/media-gallery.js`, `assets/zoom-dialog.js`, `assets/drag-zoom-wrapper.js`; Next.js Commerce `components/product/gallery.tsx`; Embla `packages/embla-carousel-accessibility`.

### P27 Variant picker as buttons and swatches (TS)
- Job: make options visible, comparable and quick to select.
- Evidence: 57% of sites do not use button-style size selectors [Study, 2026].
- Use when: options with up to about 12 values. Dropdown only for long lists (for example 40 lengths).
- Avoid: dropdowns for size and color, removing sold-out values (users cannot request back in stock), disabled inputs that cannot be focused.
- Build: radio group per option, selected value shown next to the option name, sold-out values styled and labeled but still focusable, variant in URL.
- A11y: `<fieldset><legend>Size: M</legend>` with radio inputs; sold-out: label suffix "sold out" and `aria-disabled="true"` rather than `disabled`.
- Repos: Horizon `snippets/variant-main-picker.liquid` (fieldset, legend, radios, sold-out label); Next.js Commerce `components/product/variant-selector.tsx` (URL state, but disables sold-out buttons).

### P28 Price block with legal clarity (TS)
- Job: one unambiguous price, sale context, unit price and tax note.
- Evidence: 81% do not show unit price [Study, 2026]; EU Omnibus rules require the prior lowest price in the last 30 days when announcing a reduction [Official, Directive 2019/2161].
- Use when: always.
- Avoid: compare-at prices that were never charged, unit price missing in the EU, price that changes after variant selection without announcement.
- Build: price, compare-at with prior-price note where required (wording from `compliance`), unit price, "incl. VAT" in EU, installment message only where compliant (P48).
- A11y: price updates on variant change announced in a polite region; strikethrough backed by visually hidden text; `<bdi>` around prices in RTL.
- Repos: Horizon `snippets/price.liquid`, `snippets/unit-price.liquid`, `assets/product-price.js`.

### P29 Stock and delivery promise (TS)
- Job: answer "when will it arrive" before the user leaves to find out.
- Evidence: Baymard 2026 electronics benchmark: checkouts often leave users unclear on delivery timing [Study, 2026]; 67% of sites do not show a total cost estimate near the buy section [Study, 2026].
- Use when: always; delivery date range by market and method.
- Avoid: fake low-stock counters, "ships in 24h" without a cut-off, promise that ignores the selected market.
- Build: "Order by 15:00 for delivery Thu 9 to Fri 10 Oct" from real carrier SLAs; stock status per variant from inventory; local pickup availability.
- A11y: plain text; time zone stated if relevant.
- Repos: Horizon `blocks/product-inventory.liquid`, `assets/product-inventory.js`, `assets/local-pickup.js`.

### P30 Size guide and fit information in context (TS)
- Job: reduce wrong-size orders and returns.
- Evidence: a fashion blog attributes to Baymard that 90% of apparel sites fail to let users assess size or fit [Unverified].
- Use when: apparel, footwear, furniture dimensions, rings.
- Avoid: size guide as a PDF or a separate page, charts in one unit system only.
- Build: link next to the size picker opening a dialog with the product-specific chart (metaobject), measuring how-to, cm and inches toggle, model height and size worn.
- A11y: data table with headers; dialog returns focus to the link.
- Repos: Horizon `blocks/popup-link.liquid` (dialog content), metaobject setting types in `theme-liquid-docs/schemas/theme/setting.json`.

### P31 Description in collapsible vertical sections (TS)
- Job: scannable details without hiding content users need.
- Evidence: 28% of sites still use horizontal tabs; vertical collapsed sections caused users to overlook content far less (8%) [Study, 2025].
- Use when: descriptions with specs, care, materials, shipping and returns.
- Avoid: horizontal tabs, all sections collapsed including the key benefits, specs as prose.
- Build: short benefit summary visible; specs as a definition list or table; accordions for care, materials, shipping, returns, safety info (GPSR).
- A11y: `<details><summary>` or disclosure buttons with `aria-expanded`; headings inside.
- Repos: Horizon `blocks/accordion.liquid`, `blocks/_accordion-row.liquid`.

### P32 Reviews with distribution, filters and photos (TS/TF)
- Job: credible social proof that answers fit and quality questions.
- Evidence: 95% of test participants relied on reviews; 60% of sites ask too much to submit; 80% do not respond to negative reviews; 34% do not allow review images [Study, Baymard].
- Use when: once a product has reviews; show "No reviews yet" honestly otherwise.
- Avoid: hiding negative reviews, star average without count, fabricated or incentivized reviews without disclosure (illegal in EU and US).
- Build: summary near title (average plus count, links to section), distribution bars, filter by star and by "with photos", sort by recent, merchant responses.
- A11y: "4.6 out of 5 stars, 212 reviews" as text; bars with text values; review images with alt from reviewer or "Customer photo".
- Repos: Horizon `blocks/review.liquid` (rating display); review apps render their own app blocks.

### P33 Questions and answers, UGC (TF)
- Job: answer edge questions in public and capture missing PDP content.
- Evidence: [Practitioner consensus].
- Use when: complex products, catalogs with repeated support questions.
- Avoid: empty Q and A modules, unmoderated UGC.
- Build: seed from support tickets; move recurring answers into the description.
- A11y: headings per question or a definition list.
- Repos: app blocks; no reference implementation in the inspected repos.

### P34 Sticky add to cart on mobile (TF)
- Job: keep the buy action reachable after users scroll into details.
- Evidence: [Contested]: common and often positive in tests, but it can obscure content, chat and focus (WCAG 2.4.11).
- Use when: long mobile PDPs. Test it.
- Avoid: bar visible while the main button is visible, covering cookie banner or chat, adding to cart without a selected variant.
- Build: show when main buy buttons leave the viewport (IntersectionObserver), hide near the footer, include selected variant and price, open the variant picker if none selected.
- A11y: `scroll-padding-bottom` equal to bar height so focused elements are not hidden; bar is not a dialog.
- Repos: Horizon `assets/sticky-add-to-cart.js` (observer, hides near chat).

### P35 Add to cart feedback (TS)
- Job: confirm the add and offer the next step without losing the page.
- Evidence: [Practitioner consensus]; toasts alone are easy to miss and fail some users (see [Notifications](notifications-feedback-and-microinteractions.md)).
- Use when: always.
- Avoid: silent adds, toast-only confirmation, redirect to cart for browse-heavy stores.
- Build: button shows pending then success state; cart count updates; drawer opens (or inline confirmation panel on PDP) with item, subtotal, "Checkout" and "Continue shopping".
- A11y: status message in `role="status"`; when a drawer opens, focus moves to its heading.
- Repos: Next.js Commerce `components/cart/add-to-cart.tsx` (status live region, `useActionState`); Horizon `snippets/add-to-cart-button.liquid`, `assets/fly-to-cart.js`.

### P36 Bundles, add-ons and frequently bought together (TF)
- Job: raise AOV with items that complete the purchase.
- Evidence: cart cross-sells: 52% of desktop sites show irrelevant ones [Study, Baymard]; nested cart lines link add-ons (warranty) to a parent line [Official, 2025-10].
- Use when: real complements (case for a phone, refill for a device). Economics owned by `offer-strategy`.
- Avoid: random "You may also like" above the buy button, pre-checked add-ons (illegal in the EU for paid extras).
- Build: add-on checkboxes unchecked by default below buy buttons; bundles via Shopify Bundles or Cart Transform; nested cart lines via `parent_id` (Ajax) or `parent` (Storefront API).
- A11y: each add-on is a labeled checkbox with price.
- Repos: Horizon `blocks/product-recommendations.liquid`, `assets/product-recommendations.js`.

### P37 Trust and returns info at the buy button (TS)
- Job: remove last-mile doubt: returns, shipping cost, payment options, warranty.
- Evidence: Baymard 2026: users often unclear on total cost, financing and delivery [Study, 2026].
- Use when: always.
- Avoid: 12 payment logos, badges that claim certifications the store does not hold.
- Build: 2 to 4 short lines under the button (returns window, shipping cost or threshold, delivery estimate); payment icons limited to methods actually available in the market.
- A11y: icons have text equivalents or are decorative with adjacent text.
- Repos: Horizon `blocks/payment-icons.liquid`, `blocks/_product-details.liquid` (free shipping text default).

### P38 Back in stock and pre-order (TS)
- Job: capture demand when a variant is unavailable.
- Evidence: [Practitioner consensus].
- Use when: sold-out variants of active products.
- Avoid: email capture without consent text, pre-orders without a clear ship date and charge timing.
- Build: on sold-out variant, replace buy button with "Notify me when available" form (email or SMS per consent); pre-order label with date (selling plan or app); messages sent by `lifecycle-crm`.
- A11y: form with label; success state inline.
- Repos: Horizon supports pre-orders (theme listing) [Official]; implementation via selling plans (`selling_plan` objects in Liquid docs).

### P39 GPSR and regulatory product info (TS, EU)
- Job: meet EU General Product Safety Regulation duties for online listings.
- Evidence: since 2024-12-13 listings must show manufacturer name and contact, product identifiers and warnings or safety information [Official, Regulation (EU) 2023/988].
- Use when: selling consumer products into the EU.
- Avoid: safety info only on packaging.
- Build: metafields for manufacturer, EU responsible person, warnings; render in a "Product safety" section.
- A11y: plain text, not images.
- Repos: Horizon `blocks/product-custom-property.liquid` pattern for metafield-driven rows.

## E. Cart and cart drawer
### P40 Cart drawer vs cart page decision (TS)
- Job: confirm, edit and route to checkout with the fewest steps.
- Evidence: [Practitioner consensus]; Horizon offers a slide-out cart and a cart page [Official, 2025].
- Use when: drawer for browse-heavy stores; page or drawer plus page for large carts and B2B.
- Avoid: drawer without a link to a full cart page, drawers that lose items after Back (bfcache) [Official, Horizon fix 2026-09].
- Build: see [Cart drawer and upsells](cart-drawer-and-upsells.md) for the full spec.
- A11y: native `<dialog>` with `showModal()`, `aria-labelledby`, focus to heading, Escape, return focus to trigger.
- Repos: Horizon `snippets/cart-drawer.liquid`, `assets/cart-drawer.js`; Next.js Commerce `components/cart/modal.tsx`; Hydrogen `app/components/Aside.tsx` (missing focus trap, do not copy as is).

### P41 Free shipping progress indicator (TF)
- Job: make the threshold visible and actionable.
- Evidence: no public Baymard guideline found; vendor claims only [Unverified]; threshold economics belong to `offer-strategy`.
- Use when: a threshold exists in that market.
- Avoid: wrong currency, showing the bar in markets without free shipping, nagging copy, bars that ignore discounts.
- Build: compute remaining amount in presentment currency after discounts; text first ("Add EUR 12.50 for free delivery"), bar second; success state.
- A11y: text is the primary carrier; `<progress>` or `role="progressbar"` with `aria-valuetext`; polite announcement when the state crosses the threshold.
- Repos: no inspected repo ships it; recipes in the implementation references.

### P42 Relevant cart cross-sells (TF)
- Job: offer genuine complements without derailing checkout.
- Evidence: 52% of desktop sites show irrelevant cart cross-sells; 66% of users frustrated by a separate cross-sell step at Amazon [Study, Baymard]; guideline 578 updated 2026-07 [Study, 2026-07].
- Use when: complements exist and data supports relevance.
- Avoid: blocking interstitials, more than 3 items in a drawer, recommendations above the subtotal on mobile.
- Build: up to 3 items below line items, label the reason ("Goes with your Linen Shirt"), add in place.
- A11y: section heading; add buttons named with product.
- Repos: Horizon `sections/product-recommendations.liquid` (Shopify recommendations API).

### P43 Line item editing (TS)
- Job: change quantity, variant or remove items without fear.
- Evidence: [Practitioner consensus].
- Use when: always.
- Avoid: removal without undo, quantity inputs that accept values above stock and fail at checkout.
- Build: stepper with min, max from inventory and quantity rules; remove with inline "Undo" for about 5 seconds; errors next to the line.
- A11y: buttons named "Decrease quantity of Linen Shirt, M"; live region for total updates.
- Repos: Horizon `assets/component-cart-quantity-selector.js`, `assets/component-cart-items.js`; Hydrogen `app/components/CartLineItem.tsx` (labeled steppers).

### P44 Express checkout placement (TS/TF)
- Job: one-tap pay for users with wallets.
- Evidence: Shopify reports Shop Pay conversion benefits [Official claims, vendor]; Spring '26 extended accelerated checkouts to nested lines [Official, 2026-06].
- Use when: Shopify Payments or wallet support exists.
- Avoid: wallet buttons above the add to cart button on PDP for multi-variant products, five wallet buttons stacked on mobile.
- Build: cart and drawer: wallets below the main "Checkout" button; PDP: test placement (TF).
- A11y: platform-rendered buttons; ensure surrounding labels are clear.
- Repos: Horizon `blocks/accelerated-checkout.liquid`.

### P45 Discount code in cart (TS)
- Job: let users with a code apply it early and see the effect.
- Evidence: Horizon supports codes in cart via the Ajax Cart API [Official, 2025].
- Use when: the store issues codes.
- Avoid: a prominent empty code field that sends users to search for codes (collapse it).
- Build: collapsed "Discount code" disclosure; inline success or error; show savings in subtotal.
- A11y: input with label, error linked via `aria-describedby`.
- Repos: Horizon `assets/cart-discount.js`.

## F. Checkout and payments
### P46 Guest checkout most prominent (TS)
- Job: let first-time buyers pay without an account.
- Evidence: 62% of sites do not make guest checkout the most prominent option [Study, Baymard checkout benchmark].
- Use when: always for B2C.
- Avoid: forced account creation, password fields before payment.
- Build: email-first; account offer after purchase (P52).
- A11y: platform checkout; for custom checkouts, standard form semantics.
- Repos: Saleor Paper `src/app/(checkout)` (guest flow with `/order/{hmac}` confirmation).

### P47 Local payment methods first by market (TS)
- Job: show the method the market expects at the top.
- Evidence: NL: iDEAL rebranded iDEAL | Wero by 2026-03-31, Wero rollout from Q4 2026 [Official, EPI and banks 2026]; DE: PayPal 28.5% and invoice 25.8% of online purchases (2024 data) [Study, EHI 2025]; TR: installments around 55% of online transactions [Study, Worldline 2024], TROY 25.3% of card value in 2025 [Official, BKM 2026-01].
- Use when: every market with a distinct method mix.
- Avoid: one global order, logos of methods not offered at checkout.
- Build: payment customization Function (Shopify) or gateway config to order and hide methods per market; storefront icons per market. See [Checkout and payments](checkout-and-payments.md).
- A11y: method names as text, not logos only.
- Repos: `ui-extensions` checkout targets (`purchase.checkout.payment-method-list.render-before`).

### P48 Compliant BNPL and installment messaging (TS)
- Job: inform about installments without pressure.
- Evidence: CCD2 applies from 2026-11-20: BNPL in scope, cannot be preselected, risk warning in advertising [Official, Directive (EU) 2023/2225].
- Use when: BNPL or installments offered.
- Avoid: preselected BNPL, "0% interest" without the lender's required info, installment banners on every product card.
- Build: provider widgets with provider-approved copy; PDP line near price; checkout lists BNPL as one option, not default. `compliance` approves copy.
- A11y: widget text readable at 200% zoom; no autoplaying modals.
- Repos: Horizon `snippets/cart-drawer.liquid` closes the drawer when the installments CTA opens (avoids stacked dialogs).

### P49 Address entry with autocomplete and validation (TS)
- Job: fewer fields, fewer delivery failures.
- Evidence: 54% of sites lack an address validator or lookup [Study, 2026]; average checkout has 11.3 form fields [Study, Baymard].
- Use when: custom checkouts and account address forms. Shopify checkout has its own; Plus can add address autocomplete targets [Official, ui-extensions].
- Avoid: two address lines required, phone required without reason, no `autocomplete` attributes.
- Build: correct `autocomplete` tokens, country first, postal lookup where available (NL postcode plus house number).
- A11y: labels visible, errors inline and summarized.
- Repos: `ui-extensions` targets `purchase.address-autocomplete.suggest` and `.format-suggestion`; Saleor Paper international address fields.

### P50 Inline validation and error recovery (TS)
- Job: users fix errors fast and keep their data.
- Evidence: WCAG 3.3.1, 3.3.3 and 3.3.7 Redundant Entry [Official, W3C].
- Use when: every form.
- Avoid: validation on each keystroke, clearing fields on error, errors only at the top.
- Build: validate on blur and on submit; summary at top with links to fields; focus the first invalid field.
- A11y: `aria-invalid`, `aria-describedby` to the message, error text not color only.
- Repos: Base UI `field`, `form`; React Aria `Form.tsx`, `FieldError.tsx`.

### P51 Persistent order summary and delivery dates in checkout (TS)
- Job: users see what they pay and when it arrives at every step.
- Evidence: 12% of US shoppers abandoned because the total was not visible up front [Study, Baymard]; Spring '26 checkout redesign made delivery options easier to scan [Official, 2026-06].
- Use when: custom checkouts; on Shopify configure delivery names and dates.
- Avoid: shipping cost revealed only at the last step.
- Build: delivery method names with date ranges; summary collapsible on mobile with total visible in the header.
- A11y: summary toggle is a disclosure button with the total in its name.
- Repos: Medusa starter `src/modules/checkout`; Saleor Paper URL steps `?step=contact|shipping|payment`.

## G. Post-purchase and accounts
### P52 Thank you page with next steps (TS)
- Job: confirm, set expectations, offer account creation and one relevant action.
- Evidence: non-Plus Shopify stores were auto-upgraded on 2026-08-26 and additional scripts stopped [Official, 2026-08].
- Use when: always.
- Avoid: five upsells, tracking scripts that no longer run (verify with `measurement`).
- Build: order number, delivery estimate, what happens next, account creation (one tap, prefilled), one offer or referral block, support link.
- A11y: heading that confirms the order; no auto-redirects.
- Repos: `ui-extensions` targets `purchase.thank-you.*`.

### P53 Order status, tracking and withdrawal function (TS)
- Job: self-serve status, returns and EU withdrawal.
- Evidence: EU withdrawal function mandatory from 2026-06-19 for online distance contracts with a withdrawal right (two-step, partial withdrawal, acknowledgment on a durable medium) [Official, Directive (EU) 2023/2673; DE § 356a BGB].
- Use when: all EU sales; tracking for all.
- Avoid: withdrawal only by email, withdrawal hidden behind login without an alternative [Unverified on the login point], forcing an app.
- Build: "Withdraw from contract here" entry on order status and in the footer or account, two-step flow, item selection, confirmation email. Legal wording from `compliance`.
- A11y: accessible form; confirmation page with heading.
- Repos: `ui-extensions` `customer-account.order-status.*`, `customer-account.order.action.render`.

### P54 Account dashboard with reorder and loyalty (TS)
- Job: fast repeat purchase and visible rewards.
- Evidence: loyalty ranks 4th in account expectations; put balances on the main dashboard [Study, Baymard 2026-08].
- Use when: repeat-purchase categories, B2B.
- Avoid: account pages that only list orders, legacy Liquid account templates on Shopify (deprecated 2026-02) [Official, 2026-02].
- Build: recent orders with "Buy again", saved addresses, loyalty balance, subscriptions, returns.
- A11y: tables with headers for orders; buttons named with order number.
- Repos: Hydrogen `app/routes/account.orders._index.tsx`, `account.orders.$id.tsx`; `ui-extensions` customer account targets.

### P55 Wishlist without forced login (TF)
- Job: save items for later and come back.
- Evidence: [Practitioner consensus].
- Use when: high consideration and fashion; skip for 1 to 10 SKU stores.
- Avoid: login wall on the heart icon, wishlists that vanish across devices without warning.
- Build: local wishlist for guests, merge into account on login, share link, back-in-stock and price-drop notifications via `lifecycle-crm` with consent.
- A11y: toggle button with `aria-pressed` and product name.
- Repos: Horizon `assets/recently-viewed-products.js` shows the local storage pattern for viewed items.

## H. Feedback, motion and notifications
### P56 Inline first, toast second (TS)
- Job: put feedback where the user is looking and keep errors persistent.
- Evidence: GitHub Primer does not recommend toasts; Adobe Spectrum requires at least 6 seconds; auto-dismissal conflicts with WCAG 2.2.1 debates [Official design systems; Contested].
- Use when: toasts only for non-critical confirmations with a persistent alternative.
- Avoid: errors in toasts, actions only reachable inside a disappearing toast.
- Build: decision tree in [Notifications](notifications-feedback-and-microinteractions.md).
- A11y: a live region present at page load; `role="status"` for success, `role="alert"` only for urgent errors.
- Repos: sonner `src/index.tsx` (polite region, hotkey to focus, pause on hover and hidden tab).

### P57 Optimistic UI with rollback (TS)
- Job: instant response to cart actions with honest correction.
- Evidence: [Practitioner consensus]; INP threshold 200 ms [Official, web.dev].
- Use when: cart add, quantity, remove.
- Avoid: optimistic success when inventory may fail without a visible rollback message.
- Build: update UI immediately, reconcile with server response, show inline error and revert on failure.
- A11y: announce the final state, not the optimistic one twice.
- Repos: Hydrogen `useOptimisticCart` in `app/components/CartMain.tsx`; Next.js Commerce `components/cart/cart-context.tsx` (`useOptimistic`).

### P58 Motion with restraint (TS)
- Job: motion that explains state changes and never slows tasks.
- Evidence: [Practitioner consensus] (Emil Kowalski craft rules: ease-out for entering, under 300 ms, no animation on high-frequency keyboard actions); WCAG 2.3.3 and `prefers-reduced-motion` [Official].
- Use when: drawers, dialogs, add to cart, filter panels.
- Avoid: `transition: all`, scale from 0, bouncing UI, parallax heroes, animations on every product card scroll.
- Build: transform and opacity only, 150 to 250 ms for UI, 200 to 400 ms for drawers, reduced motion fallback.
- A11y: reduced motion removes movement but keeps state change visible.
- Repos: emilkowalski/skills `skills/emil-design-eng`, `skills/mobile-native`; Horizon `assets/view-transitions.js`.

## I. Accessibility, international and performance
### P59 Accessible overlays (dialogs and drawers) (TS)
- Job: overlays that keyboard and screen reader users can enter and leave.
- Evidence: ACM found consumers with disabilities could not order on most of about 100 large Dutch webshops (order buttons, CAPTCHA) [Official, 2026-03].
- Use when: every modal, drawer, quick view, size guide.
- Avoid: div overlays without focus management, `aria-modal` on a closed panel, unlabeled backdrop buttons.
- Build: native `<dialog>.showModal()` or Base UI, Radix, React Aria dialogs; Base UI Drawer replaces unmaintained vaul.
- A11y: name via `aria-labelledby`, initial focus, inert background, Escape, focus return.
- Repos: Horizon `assets/dialog.js`, `assets/theme-drawer.js`; Base UI `packages/react/src/drawer` (since 1.2.0, 2026-02); Radix `packages/react/dialog`.

### P60 Focus, targets and skip link (TS)
- Job: keyboard and touch users can reach and hit every control.
- Evidence: WCAG 2.2 adds 2.4.11 Focus Not Obscured, 2.5.8 Target Size Minimum (24 by 24 CSS px) [Official, W3C 2023-10]; EN 301 549 v4.1.1 (2026-09) incorporates WCAG 2.2 [Official, 2026-09].
- Use when: always.
- Avoid: `outline: none` without replacement, sticky bars covering focused fields, 16 px icon buttons.
- Build: skip link to main; `:focus-visible` ring with 3:1 contrast; `scroll-padding` for sticky header and sticky ATC; 44 px touch targets on mobile.
- A11y: test with keyboard only on every template.
- Repos: Horizon `assets/focus.js`; emilkowalski/skills `mobile-native` (touch fixes).

### P61 Country, currency and language selector (TS)
- Job: correct prices, taxes, delivery and language without forced redirects.
- Evidence: Shopify Markets drives currency, catalogs, domains and hreflang [Official, 2026].
- Use when: more than one market or language.
- Avoid: IP redirects with no way back, currency switch without country (wrong taxes and shipping), flags for languages.
- Build: suggest a market in a dismissible banner; selector in header or footer listing countries with currency; language separate; remember choice.
- A11y: native selects or listbox with labels; country names in their own language as an option.
- Repos: Horizon `assets/localization.js`; Medusa `src/middleware.ts` (`[countryCode]` routing); Saleor Paper `/{locale}/{channel}`.

### P62 Performance budget per template (TS)
- Job: keep LCP, INP and CLS in the good range on real mobile devices.
- Evidence: Rakuten 24 RPV +53.37% and CVR +33.13% after CWV work; Vodafone LCP 31% better, 8% more sales [Study, web.dev]; Ray-Ban doubled conversion with prerendering [Study, web.dev]; Shopify platform prefetch rules since 2025-06, up to 180 ms faster [Official, Shopify].
- Use when: always; budgets: LCP 2.5 s, INP 200 ms, CLS 0.1 at p75 mobile.
- Avoid: lazy loading the LCP image, 15 app scripts on PDP, hydration of static sections, carousels without dimensions.
- Build: LCP image `fetchpriority="high"`, responsive `srcset`, width and height; defer non-critical apps; speculation rules for PLP to PDP; JS budget per template (see [Audit method](storefront-audit-method.md)).
- A11y: performance work must not remove focus styles or labels.
- Repos: Horizon `assets/performance.js`, `assets/section-hydration.js`, `snippets/scripts.liquid` (import maps, module preloads); Shopify speculation rules docs.

## Pattern selection by catalog size

| Pattern group | 1 to 10 SKUs | 10 to 500 SKUs | 500+ SKUs |
|---------------|--------------|----------------|-----------|
| Navigation | P01 flat links, no mega menu | P01, P03, simple dropdown | P01 to P03 mega menu, P08 |
| Search | Optional, hide if under 30 SKUs | P10, P11, P13 | P10 to P16, third-party engine likely |
| PLP | Single collection or none | P17 to P20, P23 | All of C, filters per category |
| PDP | Long-form PDP, rich media, FAQ, comparison | P26 to P32, P35, P37 | Templated PDP from metafields, P27, P29 at scale |
| Cart | Drawer with one add-on | P40 to P45 | Cart page plus drawer, quick order (P16) |

## Pattern selection by AOV band

| AOV | Emphasize | De-emphasize |
|-----|-----------|--------------|
| Under 40 (USD or EUR) | P35 fast add, P41 threshold, P44 wallets, P22 quick add for consumables | Long comparison content |
| 40 to 150 | P27, P29, P32, P37 | Chat-heavy flows |
| 150 to 750 | P26 media depth, P30, P32 with photos, P48 installments, P29 delivery dates | Quick add |
| Over 750 | P29, P37, P48, consultation or chat, P53 service, P54 accounts | Free shipping bars (usually always free) |
