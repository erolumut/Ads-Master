# Post-Purchase, Order Status and Accounts

Thank you page, order status and tracking, returns and the EU withdrawal function, customer accounts, reorder, loyalty and wishlists. Patterns P52 to P55 in the [Pattern library](ux-pattern-library.md). Messaging flows (emails, SMS, push) belong to `lifecycle-crm`; storefront-ux builds the on-site surfaces.

## 1. Evidence and platform facts

| Finding | Source | Label |
|---------|--------|-------|
| Non-Plus Shopify Thank you and Order status pages auto-upgraded on 2026-08-26; additional scripts removed; Plus deadline was 2025-08-28 with auto-upgrades from 2026-01 | Shopify Help Center and coverage | [Official, 2026-08] |
| Legacy customer accounts deprecated (2026-02-26): not available to new stores; no sunset date published as of 2026-10; a theme without legacy templates triggers automatic upgrade | Shopify developer changelog | [Official, 2026-02] |
| EU withdrawal function mandatory from 2026-06-19 (two-step, partial withdrawal, acknowledgment on durable medium); Germany § 356a BGB published 2026-02-05 | Directive (EU) 2023/2673, law firm summaries | [Official, 2026-06] |
| Loyalty is the 4th online account expectation; put balances on the main dashboard; return frequency declining over 3 years; frequency controls beat all-or-nothing unsubscribe | Baymard quantitative insights, 1,083 US shoppers | [Study, 2026-08] |
| Managed Markets supports EU buyer cancellation and return requests (14-day rule via Global-e as merchant of record) | Shopify changelog | [Official, 2026] |

## 2. Thank you page

Jobs, in order:
1. Confirm: "Thank you, your order #1043 is confirmed" as the heading; email address it was sent to.
2. Set expectations: delivery estimate, what happens next (packing, shipping email, tracking), pickup instructions if relevant.
3. Account: one-tap account creation or "Track this order in your account" (new customer accounts use email one-time codes).
4. One relevant next action: referral, app download, social follow, survey (one question, from `cro`), or a post-purchase offer. Pick one; five blocks dilute each other.
5. Support: contact and returns policy link; withdrawal function entry for EU orders.

Shopify: build with checkout UI extensions on `purchase.thank-you.*` targets (all plans) through apps or custom apps (Plus for custom). Tracking on this page uses web pixels or app pixels, not additional scripts; `measurement` verifies.

## 3. Order status and tracking

- Order status page and account order page show: items, status timeline (ordered, packed, shipped, out for delivery, delivered), carrier and tracking link, delivery estimate, address (editable until fulfillment where operations allow), invoice download (DE, TR), returns and withdrawal entry.
- Shopify targets: `customer-account.order-status.*` (block, announcement, cart line items, customer information, fulfillment details, payment details, return details, unfulfilled items), `customer-account.order.action.render`, `customer-account.order.action.menu-item.render`, `customer-account.order.page.render`, `customer-account.order-index.*`.
- Headless: Hydrogen skeleton `app/routes/account.orders._index.tsx` and `account.orders.$id.tsx` via the Customer Account API.

## 4. EU withdrawal function (from 2026-06-19)

Build spec (legal wording from `compliance`; check national law):
1. Entry point labeled "Withdraw from contract here" or equally unambiguous wording, prominently placed and available for the whole withdrawal period: on the order status page, in the account order view, and in the footer or a dedicated page reachable without forcing an app install.
2. Step 1 form: name, order identification (order number, email), the items to withdraw (partial withdrawal must be possible), electronic address for the acknowledgment.
3. Step 2: separate confirmation control ("Confirm withdrawal").
4. Acknowledgment sent without undue delay on a durable medium (email with content, date and time).
5. The withdrawal policy text states that the function exists and where it is.
6. Exclusions (bespoke goods, sealed hygiene items, perishables, some digital content) are handled by product data, not by hiding the function for everyone.
7. Accessibility: standard form semantics, no CAPTCHA wall, works with keyboard and screen readers.

Shopify: check the Help Center page "EU right of withdrawal" and available apps or customer account extensions; Managed Markets merchants have Global-e cancellation and return requests. Login-free access is debated [Unverified]; provide a guest route (order number plus email) to be safe.

Returns (beyond withdrawal): self-serve return request with reason codes (size too small, too large, not as described, damaged), label generation per carrier, refund timing stated. Return reasons feed PDP fixes (size guide, images) via the monthly audit.

## 5. Customer accounts

Shopify new customer accounts:
- Passwordless one-time code login by email; order history, addresses, returns; extensible with customer account UI extensions (profile, order index, order status, custom full pages via `customer-account.page.render`).
- Legacy Liquid templates (`customers/account.liquid`, `login.liquid`, `register.liquid`) will be locked then removed (no date yet). Plan migration: inventory custom fields, apps on account pages, pixels, B2B flows, Multipass or SSO needs; rebuild in UI extensions; tell customers about the code login.
- A theme change can trigger the upgrade if the new theme lacks legacy files: check before publishing any new theme (`site-engineer` release checklist).

Account dashboard content (priority order):
1. Recent orders with status and "Buy again" (adds the same variants to cart, skipping unavailable ones with a message).
2. Loyalty balance and next reward (if a program exists).
3. Subscriptions (next delivery, skip, pause, change frequency).
4. Addresses and payment methods (wallet managed by platform).
5. Returns and withdrawal.
6. Communication preferences with frequency controls (link to the preference center from `lifecycle-crm`).

Reorder patterns:
- Consumables: "Reorder" on the order card and a "Your usuals" list on the homepage for logged-in users (TF).
- B2B: quick order list, CSV upload, saved lists, volume pricing visible (Horizon quick order list; Shopify B2B catalogs and quantity rules).

## 6. Wishlists

- Heart toggle on cards and PDP: `<button aria-pressed="false" aria-label="Save Linen Shirt to wishlist">`.
- Guests: store locally (localStorage or cookie), show a count in the header, prompt to log in to sync across devices (never block saving).
- On login: merge local into account list; deduplicate.
- Wishlist page: items with current price and stock, add to cart, remove, share link.
- Back-in-stock and price-drop alerts only with explicit consent; sending is `lifecycle-crm`.
- 1 to 10 SKU stores: skip wishlists.

## 7. Post-purchase offers

- One offer, relevant to the order (refill, accessory, extended warranty), with a single accept action and no change to the original order total without clear confirmation.
- On Shopify, post-purchase offers run through apps on supported surfaces; confirm plan support and payment method compatibility before proposing [Unverified on current plan limits].
- Economics from `offer-strategy`; test with `cro`.

## 8. Measurement

Events: `purchase` (verified by `measurement`), `sign_up` after purchase, `reorder_click`, `withdrawal_start`, `withdrawal_confirm`, `return_request`, `wishlist_add`, `wishlist_to_cart`. KPIs: account creation rate after purchase, repeat purchase rate (owned by `lifecycle-crm`), reorder share, return rate by reason, withdrawal completion time, support tickets per 100 orders ("where is my order" should fall after tracking improvements).
