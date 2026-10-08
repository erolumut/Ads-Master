# Cart, Cart Drawer and Upsells

Cart drawer and cart page, free shipping progress, upsells that do not hurt checkout, line editing, discount codes, express checkout buttons, and cart state integrity. Patterns P35, P40 to P45 in the [Pattern library](ux-pattern-library.md).

## 1. Evidence snapshot

| Finding | Source | Label |
|---------|--------|-------|
| Average documented cart abandonment 70.22% | Baymard (50 studies, updated 2025-09) | [Study, 2025-09] |
| Extra costs are the top reason for checkout abandonment (shares differ by secondary source: 39% to 48%) | Baymard US survey 2025 via secondary | [Study, 2025] [Contested on the number] |
| 52% of desktop sites show irrelevant cart cross-sells; 66% of users frustrated by a separate cross-sell step | Baymard cart cross-sell research | [Study] |
| Cross-sell context guideline updated 2026-07 | Baymard guideline 578 | [Study, 2026-07] |
| Horizon: slide-out cart, cart notes, discount codes in cart via Ajax Cart API, stale cart after Back fixed in 4.2.0 | Horizon theme listing and release notes | [Official, 2026-09] |
| Nested cart lines (add-ons tied to a parent line) in Ajax Cart API and Storefront API 2025-10 | Shopify dev docs | [Official, 2025-10] |
| Standard storefront actions `Shopify.actions.openCart`, `updateCart`, `getCart` and events `shopify:cart:lines-update` | Shopify Spring '26 | [Official, 2026-06] |

## 2. Drawer, page or both

| Situation | Choose | Why |
|-----------|--------|-----|
| Browse-heavy DTC, AOV under about 150, 1 to 5 items per order | Drawer plus a full cart page link | Keeps the shopping context |
| Large carts (10+ lines), B2B, bulk | Cart page (drawer optional as a mini summary) | Editing space, tables |
| 1 to 10 SKU store with single-product orders | Drawer, or direct to checkout via "Buy now" test (TF) | Fewer steps |
| Headless | Drawer as a dialog route or state plus `/cart` page | Shareable cart URL (`/cart/<lines>` style routes in Hydrogen) |

## 3. Drawer specification

Structure (top to bottom):
1. Header: "Your cart (3)" as heading, close button.
2. Free shipping progress (if a threshold exists in the market).
3. Line items: image, title, variant, unit price, quantity stepper, line price, remove.
4. Nested add-ons under their parent line (warranty, gift wrap).
5. Cross-sells (max 3, labeled with reason), collapsed by default on small screens if they push the subtotal below the fold.
6. Order note and gift options (collapsed).
7. Footer (sticky inside the drawer): subtotal, "Taxes and shipping calculated at checkout" or the actual estimate, discount code disclosure, primary "Checkout" button, express checkout buttons below, link "View cart".

Behavior:
- Opens after add to cart (configurable), from the cart icon, and via `Shopify.actions.openCart` on Liquid storefronts.
- Width: full on mobile, 400 to 480 px on desktop; height `100dvh`; footer padded with `env(safe-area-inset-bottom)`.
- Background inert, body scroll locked, `overscroll-behavior: contain` inside.
- Escape and backdrop click close; focus returns to the trigger.
- Updates are optimistic with rollback; errors inline per line ("Only 2 left in stock, quantity set to 2").
- Cart state refreshes on `pageshow` when `event.persisted` is true (bfcache) so Back never shows stale lines (Horizon fixed this in 4.2.0).
- Close the drawer before opening another dialog (Horizon closes it when the installments modal opens).

Accessibility:
- Native `<dialog>` with `showModal()` or a primitive dialog; `aria-labelledby` to the heading; initial focus on the heading or close button.
- Quantity buttons named with product and variant; the quantity input labeled; totals update in a polite live region ("Subtotal EUR 128.00").
- Remove: button "Remove Linen Shirt, M"; after removal show inline "Removed. Undo" with focus moved to the undo button or to the next line.

Repos: Horizon `snippets/cart-drawer.liquid` (`<dialog>`, `aria-labelledby`), `assets/cart-drawer.js`, `assets/component-cart-items.js`, `assets/component-cart-quantity-selector.js`, `assets/cart-discount.js`, `assets/cart-note.js`; Next.js Commerce `components/cart/modal.tsx` (Headless UI Dialog), `cart-context.tsx` (`useOptimistic`); Hydrogen `CartMain.tsx` (`useOptimisticCart`), `CartLineItem.tsx`; WooCommerce `client/blocks/assets/js/blocks/mini-cart`.

## 4. Free shipping progress indicator

Rules:
- Only in markets where a free shipping threshold exists; the threshold per market comes from `offer-strategy` and the platform shipping settings (single source of truth).
- Compute in presentment currency after discounts: `remaining = threshold_market - cart_subtotal_after_discounts`.
- Copy: "Add EUR 12.50 for free delivery" then "You get free delivery". No exclamation storms, no guilt copy.
- Text carries the meaning; the bar is decoration with `role="progressbar"` (or `<progress>`) and `aria-valuetext` equal to the text.
- Announce the crossing ("Free delivery unlocked") once in the polite region.
- Do not show it in the PDP header on every page; drawer and cart page are enough. Announcement bar can state the rule.
- Treat as TF on Scale stores (it can raise AOV and lower CVR); measure AOV, CVR and RPV together (`cro`).

Liquid note: `cart.total_price` is in presentment currency cents; a fixed shop-currency threshold must be converted per market or stored per market (market metafields) so the bar matches what checkout charges. See [Shopify implementation](platform-implementation-shopify.md).

## 5. Cart cross-sells that do not hurt checkout

| Do | Do not |
|----|--------|
| Up to 3 complements related to items in the cart | Generic bestsellers unrelated to the cart |
| Label the reason ("Goes with your Linen Shirt") | Unlabeled "You may also like" |
| Add in place, update totals | Navigate away to a PDP |
| Place below line items; collapse on small screens | Interstitial step or modal before checkout |
| Exclude items already in cart and sold-out items | Show the product the user just removed |
| Pick threshold fillers only when the threshold is close | Push items far above the remaining amount |

Measure attach rate, AOV, cart to checkout rate and RPV; ship variants through `cro`.

## 6. Line item editing

- Quantity stepper with min 1, max from inventory and quantity rules (`quantity_rule` min, max, increment for B2B).
- Variant change in the drawer (size swap) is TF; at minimum, link the line to the PDP with the variant preselected.
- Remove with undo for about 5 seconds inline, not in a toast only.
- Show line-level discounts and savings.
- Price changes since add (sale ended) shown inline with explanation.

## 7. Discount code

- Collapsed disclosure "Add discount code" in the drawer footer or cart page; checkout keeps its own field.
- Inline success: "SPRING10 applied, you save EUR 8.00"; inline error with reason (expired, minimum not reached, not valid in your market).
- Do not display a big empty code field that sends users away to coupon sites.

## 8. Express checkout buttons

- Cart and drawer: below the primary "Checkout" button, separated by "or".
- Show only wallets available in the market and device (platform-rendered buttons handle this on Shopify via `{{ content_for_additional_checkout_buttons }}` or the accelerated checkout block).
- PDP placement is TF (risk of skipping variant choice and upsells; benefit for single-variant products).
- Spring '26: accelerated checkouts support nested cart lines (add-ons survive express checkout) [Official, 2026-06].

## 9. Cart page extras

- Table layout on desktop, stacked cards on mobile.
- Shipping estimator (country and postal code) for markets with variable shipping.
- Order note, gift options, delivery date picker only if operations support them.
- "Continue shopping" returns to the last PLP, not the homepage.
- Save for later (logged in) is TF.

## 10. Cart integrity checks (run after every cart change)

| Check | How |
|-------|-----|
| Add, update, remove reflect on reload | Manual on mobile and desktop |
| Back and forward cache shows current cart | Add item, navigate, press Back |
| Currency and totals match checkout | Compare drawer subtotal vs checkout subtotal per market |
| Discount effects match checkout | Apply code in cart, verify at checkout |
| Nested add-on removed with parent | Remove parent line |
| Inventory limits enforced | Set quantity above stock |
| Events fire once | `add_to_cart`, `remove_from_cart`, `view_cart`, `begin_checkout` (with `measurement`) |
| Keyboard and screen reader | Open, edit, close, focus return |

## 11. KPIs

Cart to checkout rate, drawer open to checkout rate, attach rate of cross-sells and add-ons, AOV, items per order, cart edits per session, discount code error rate, RPV. AOV wins that lower CVR are judged on RPV and margin with `offer-strategy`.
