# Product Detail Page (PDP)

Gallery and video, variant pickers and swatches, price and unit price, stock and delivery promise, size guides, description structure, reviews and UGC, Q and A, bundles and cross-sells, sticky add to cart, trust and returns info, back in stock, regulatory info. Patterns P26 to P39 in the [Pattern library](ux-pattern-library.md).

## 1. Evidence snapshot

| Finding | Source | Label |
|---------|--------|-------|
| Up to 62% of leading sites mediocre or worse on product page UX; 48% of desktop and 38% of mobile sites decent or good | Baymard Product Page UX 2026 | [Study, 2026] |
| 57% do not use button-style size selectors; 81% do not display price per unit; 67% do not provide a total order cost estimate near the buy section | Baymard 2026 | [Study, 2026] |
| 28% still use horizontal tabs for PDP layout; collapsed vertical sections led to content being overlooked far less (8%) | Baymard 2025 | [Study, 2025] |
| 55% of sites decent or better on product images; 91% do not provide in-scale images | Baymard 2025 | [Study, 2025] |
| 95% of test participants relied on reviews; 34% of sites do not allow review images; 80% do not respond to negative reviews | Baymard reviews research | [Study] |
| Delivery timing, total cost and financing details often unclear | Baymard Electronics and Office 2026 | [Study, 2026] |
| GPSR online listing duties (manufacturer, identifiers, warnings) apply since 2024-12-13 | Regulation (EU) 2023/988 | [Official, 2024-12] |
| Omnibus prior price rule for announced reductions | Directive (EU) 2019/2161 | [Official, 2022-05 in force] |
| Unit price display obligation for goods sold by quantity | Directive 98/6/EC; Germany PAngV | [Official] |

## 2. Above the fold order

Mobile (top to bottom): gallery (with counter), title, rating summary (stars, average, count, link to reviews), price block, variant pickers, quantity (only if commonly more than 1), primary button, express checkout (TF placement), delivery promise line, 2 to 3 trust lines (returns, shipping cost or threshold), then details.

Desktop: gallery left (about 55% to 60% width), buy box right and sticky while scrolling the gallery; the same order inside the buy box.

The buy box answers in this order: what is it, what does it cost, which option, when will it arrive, what if it does not fit or work.

## 3. Gallery specification

- Images: at least 5 for most products: main, alternate angles, detail or texture, in-scale (on a person or next to a known object), packaging or what is in the box; lifestyle as extra.
- Video: short muted loop or user-started video with captions; never autoplay with sound.
- Mobile: swipe with scroll snap, counter "2 of 7", dots optional; pinch zoom or tap to open a zoom dialog.
- Desktop: thumbnails visible; click to zoom (not hover only); keyboard arrows in the zoom dialog.
- Variant images: selecting a color moves the gallery to that color's images.
- Performance: first image is the LCP element (`fetchpriority="high"`, no lazy loading, responsive `srcset`), others lazy; fixed aspect ratio to avoid CLS.
- Accessibility: alt text per image view ("Linen shirt, back view, worn by model 183 cm in size M"); controls named; zoom dialog traps focus and closes with Escape; `prefers-reduced-motion` disables slide animations.

Repos: Horizon `blocks/_product-media-gallery.liquid`, `assets/media-gallery.js`, `assets/zoom-dialog.js`, `assets/drag-zoom-wrapper.js`; Embla with `embla-carousel-accessibility`; Next.js Commerce `components/product/gallery.tsx` (URL-driven image index, labeled prev and next).

## 4. Variant picker specification

| Option type | Control | Notes |
|-------------|---------|-------|
| Size (up to about 12 values) | Button radios | Show "Size: M" in the legend; sizes in logical order |
| Color | Swatch radios with names | Swatch from Shopify swatch data or metaobject; name visible on select and hover |
| Long lists (lengths, 40+ values) | Native select or listbox | Group values if possible |
| Material, style | Button radios | |
| Combined listings (separate products per color) | Swatches linking to sibling products | Preserve selected size across navigation where possible |

Availability states:
- Sold out: visually marked (strike or dashed), label suffix "sold out", still focusable and selectable so the user can choose "Notify me" (Horizon uses `aria-disabled="true"` and the label suffix).
- Unavailable combination (does not exist): marked "unavailable".
- Never remove sold-out values or use the `disabled` attribute that blocks focus and hides the state from screen readers.

Behavior:
- Selecting a value updates price, unit price, image, stock and delivery line, SKU, the URL (`?variant=` on Shopify or option params in headless) and the buy button state.
- Announce changes in a polite live region: "Size M selected. EUR 49.00. In stock."
- If no value is preselected (recommended for size), the buy button stays enabled and pressing it scrolls to and highlights the missing option with an inline message.

Repos: Horizon `snippets/variant-main-picker.liquid`, `assets/variant-picker.js`, `assets/variant-resolution.js`; Next.js Commerce `components/product/variant-selector.tsx` (URL state; note it disables sold-out options, which blocks back-in-stock flows).

## 5. Price block specification

- Current price (largest), compare-at price struck through only if it is a genuine prior price; for EU price reductions show the lowest price of the prior 30 days as required (wording from `compliance`).
- Unit price where legally required or useful ("EUR 12.90 / 100 ml"), near the price (Germany requires unit price in close proximity to the total price).
- Tax and shipping note per market: "incl. VAT, plus shipping" (DE: "inkl. MwSt., zzgl. Versandkosten" linked to shipping info).
- Volume or tier pricing (B2B): table of quantity breaks (Horizon `assets/volume-pricing.js`, `quantity_price_break` objects).
- Installments: provider widget line under the price only where compliant (CCD2 from 2026-11-20 in the EU; see [Checkout and payments](checkout-and-payments.md)).
- Subscriptions: selling plan options as radios ("One-time" vs "Subscribe and save 10%") with the per-delivery price.
- Accessibility: visually hidden labels for regular and sale price; price updates announced; `<bdi>` around price strings in RTL.

## 6. Stock and delivery promise

- Stock status per variant: In stock, Low stock (only when inventory is genuinely under a threshold you define and the number is real), Out of stock with notify, Pre-order with date.
- Delivery line: "Order within 3 h 20 min for delivery Thu 9 Oct" only from real carrier cut-offs and SLAs for the visitor's market; otherwise a range "Delivery 2 to 4 business days".
- Pickup: "Available for pickup at Amsterdam Centrum, usually ready in 2 hours" (Horizon `assets/local-pickup.js`).
- Total cost estimate: shipping cost or free threshold for the market shown near the button (67% of sites miss it).
- Never fake scarcity (fake "12 people viewing" counters, resetting timers). These are unfair commercial practices under the EU UCPD and FTC rules; the DFA proposal (expected Q4 2026) targets them further.

## 7. Size guide and fit

- Link "Size guide" right next to the size legend, opening a dialog with the product-specific chart (stored in a metaobject linked from a product metafield).
- Contents: measurements table (cm and inches toggle by market), how to measure, fit notes ("Runs small, consider one size up" from review data), model height and size worn.
- Optional fit tools (apps) are TF; measure returns rate by reason with `lifecycle-crm` or ops.

## 8. Description structure

- 2 to 4 benefit bullets visible under the buy box or right after it.
- Collapsible vertical sections (not horizontal tabs): Details and specs (definition list or table), Materials and care, Size and fit, Shipping and returns, Product safety (GPSR: manufacturer name and contact, EU responsible person, warnings), Warranty.
- Key content expanded by default on desktop when space allows; first section expanded on mobile.
- Every fact comes from `ads-master/brand/PRODUCT_FACTS.md` or the product data; claims only from `CLAIMS.md`.

## 9. Reviews and UGC

Specification:
- Summary under the title: stars, average to one decimal, count, link to the reviews section.
- Reviews section: distribution bars (5 to 1 star with counts), filter by rating and "with photos", sort by most recent and most helpful, review photos gallery, fit or attribute ratings for apparel, merchant responses to negative reviews.
- Submission: no account required, 3 to 4 fields, photo upload.
- Legal: no fake, bought or suppressed reviews; disclose incentivized reviews; state how reviews are collected and checked (EU Omnibus requirement on review verification information).
- Performance: reviews widget loads after the buy box is interactive; the summary stars can be rendered server-side from metafields (most review apps write rating metafields).
- Accessibility: text equivalents for stars and bars; review images with alt; pagination or load more for reviews with focus management.

Q and A: seed from support tickets, moderate, and move recurring answers into the description.

## 10. Cross-sell, bundles and add-ons on the PDP

- Placement: below the buy box or after the description; never between the variant picker and the buy button, except unchecked add-on checkboxes (warranty, gift wrap).
- Types: "Complete the look" or "Works with" (complements), "Frequently bought together" (data-driven), bundles (fixed or mix and match), add-ons (nested cart lines on Shopify, `parent_id` in the Ajax Cart API).
- Pre-checked paid add-ons are not allowed in the EU (Consumer Rights Directive Art. 22).
- Pricing and bundle economics come from `offer-strategy`.
- Shopify: Bundles app or Cart Transform Function (expand and merge operations; up to 150 components; add-ons cannot nest under bundles yet) [Official].

## 11. Sticky add to cart (mobile)

Test it (TF) on long PDPs. Specification if shipped:
- Appears when the main buy button leaves the viewport (IntersectionObserver), hides when it returns and near the footer.
- Shows thumbnail, price, selected variant and the button; if no variant chosen, the button scrolls to the picker.
- Does not overlap chat widgets, cookie bars or the iOS home indicator (`env(safe-area-inset-bottom)`).
- Set `scroll-padding-bottom` so focused fields are not hidden (WCAG 2.4.11).

Repos: Horizon `assets/sticky-add-to-cart.js` (observes buy buttons and the main section bottom; gated on chat state).

## 12. Add to cart feedback

- Button: idle, pending (spinner and "Adding"), success ("Added" for about 2 seconds), error (inline message under the button).
- Then: open cart drawer (most stores) or show an inline confirmation panel with item, subtotal, "View cart" and "Checkout".
- Toast-only confirmation is not enough (see [Notifications](notifications-feedback-and-microinteractions.md)).
- Fly-to-cart animation optional; respect reduced motion (Horizon `assets/fly-to-cart.js`).

## 13. Back in stock and pre-order

- Sold-out variant selected: replace the buy button with "Notify me when available" (email or SMS with explicit consent text), keep other variants purchasable.
- Pre-order: label "Pre-order, ships from 14 Nov", state when payment is taken; use selling plans or a pre-order app.
- The messages themselves are owned by `lifecycle-crm`.

## 14. PDP by catalog size and AOV

| Context | PDP approach |
|---------|--------------|
| 1 to 10 SKUs | Long-form PDP: benefits, how it works, comparison vs alternatives, proof, FAQ, guarantee, repeated buy button; often doubles as the paid landing page with `cro` |
| 10 to 500 SKUs | Template with metafield-driven sections; rich content for top 20% of products by revenue |
| 500+ SKUs | Strict template from structured attributes; automated specs table; reviews and Q and A at scale; content QA by data checks |
| AOV over 750 | Consultation or chat entry, financing info, detailed specs and warranty, delivery and installation options |
| Consumables | Subscription option, quantity breaks, reorder in account |

## 15. Measurement

Events: `view_item`, `select_variant` (custom), `add_to_cart`, `size_guide_open`, `review_filter`, `notify_me_submit`, `sticky_atc_click`, `gallery_interaction`. KPIs: PDP add to cart rate by device and product type, variant error rate (add pressed without selection), return rate by reason (size, not as described), notify-me signups and conversion.
