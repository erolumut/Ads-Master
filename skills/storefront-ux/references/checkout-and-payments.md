# Checkout and Payments

Checkout UX within platform limits (Shopify checkout extensibility, WooCommerce Checkout block, Shopware, Adobe Commerce, headless), payment method visibility by market (iDEAL | Wero, TROY and installments, invoice, BNPL, mada, wallets), and the legal checks that touch checkout UI. Patterns P46 to P51 in the [Pattern library](ux-pattern-library.md). `cro` owns checkout experiments; `measurement` must verify tracking after every checkout change; `compliance` approves legal wording.

## 1. Evidence snapshot

| Finding | Source | Label |
|---------|--------|-------|
| 64% of 180+ sites mediocre or worse on checkout UX | Baymard checkout benchmark | [Study, 2025] |
| 62% do not make guest checkout the most prominent option | Baymard | [Study] |
| 72% do not auto-detect card type; average 11.3 form fields | Baymard | [Study] |
| 12% of US shoppers abandoned because the total was not visible up front | Baymard US survey | [Study] |
| Average large site can gain 35.26% conversion through better checkout design | Baymard | [Study, modeled] |
| Non-Plus Thank you and Order status pages auto-upgraded 2026-08-26; additional scripts stopped | Shopify Help Center and coverage | [Official, 2026-08] |
| Shopify Scripts stopped executing 2026-06-30; Functions replace them | Shopify Editions coverage | [Official, 2026-06] |
| Spring '26 checkout redesign: easier delivery options, prominent pay button, less mobile scrolling | Shopify Spring '26 Edition | [Official, 2026-06] |
| CCD2 applies 2026-11-20: BNPL in scope, cannot be preselected | Directive (EU) 2023/2225 | [Official] |
| iDEAL co-branded iDEAL \| Wero by 2026-03-31; Wero rollout Q4 2026; iDEAL decommission planned 2027-12-31 | ING, Stripe, EPI, MultiSafepay | [Official, 2026] |
| ACM: on most of about 100 large Dutch webshops, consumers with disabilities could not order (order buttons, CAPTCHA) | ACM 2026-03 | [Official, 2026-03] |

## 2. What you can change, by platform

| Platform | Checkout UI changes possible | Logic changes | Notes |
|----------|------------------------------|---------------|-------|
| Shopify Basic, Grow, Advanced | Checkout and accounts editor (branding, logo, colors, fonts), apps with UI extensions on Thank you and Order status pages only | Functions through public apps (payment customization, delivery customization, discounts, validation, cart transform) | No UI extensions in information, shipping, payment steps |
| Shopify Plus | Checkout UI extensions in all steps (targets below), branding API, custom apps with Functions | Custom Functions | Rollouts can test checkout configurations (Grow plan and up for experiments per Help Center) |
| WooCommerce | Checkout block (default for new stores since 8.3) with block extensibility (Store API, slot fills); classic shortcode checkout still exists | PHP hooks, payment gateway plugins | Mixing classic extensions with the block checkout is a common breakage source |
| Shopware 6 | Twig template overrides in the storefront theme, app system | Rule builder, payment apps | Checkout is part of the storefront; full control |
| Adobe Commerce (Magento) | Luma (Knockout) or Hyvä Checkout; Adobe Commerce Storefront drop-ins on Edge Delivery Services | Plugins | Heavy JS on Luma checkout hurts INP |
| Headless Shopify (Hydrogen, Next.js Commerce) | Hosted Shopify checkout via `checkoutUrl` (same limits as above) | Same as Shopify | Do not rebuild checkout; extend it |
| Medusa, Saleor, custom | Full control (Saleor Paper: URL-driven steps, guest confirmation route) | Your code | You own PCI scope boundaries, payment UX and accessibility |

Shopify checkout UI extension targets (from `Shopify/ui-extensions` 2026.10.0-rc.13, read 2026-10-08): `purchase.checkout.block.render`, `purchase.checkout.header.render-after`, `purchase.checkout.contact.render-after`, `purchase.checkout.delivery-address.render-before` and `render-after`, `purchase.checkout.shipping-option-list.render-before` and `render-after`, `purchase.checkout.shipping-option-item.render-after` and `.details.render`, `purchase.checkout.pickup-location-list.render-before` and `render-after`, `purchase.checkout.pickup-point-list.render-before` and `render-after`, `purchase.checkout.payment-method-list.render-before` and `render-after`, `purchase.checkout.reductions.render-before` and `render-after`, `purchase.checkout.cart-line-item.render-after`, `purchase.checkout.cart-line-list.render-after`, `purchase.checkout.actions.render-before`, `purchase.checkout.footer.render-after`, `purchase.checkout.gift-card.render`, `purchase.checkout.chat.render`, `purchase.address-autocomplete.suggest`, `purchase.address-autocomplete.format-suggestion`, and `purchase.thank-you.*` (block, announcement, header, footer, customer information, cart line list and items, chat). Extensions use Polaris web components (`s-` prefixed) since API 2025-10; check the current version before building.

## 3. Checkout UX laws (apply on any platform)

1. Guest checkout is the default path; account creation after purchase.
2. Email first, then delivery, then payment; never ask for a password before payment.
3. Total cost visible at every step, including shipping and taxes as soon as the address is known; no surprise fees (drip pricing is an unfair practice under EU UCPD guidance).
4. Delivery options named by speed and date ("DHL, Thu 9 to Fri 10 Oct, EUR 4.95"), pickup and pickup points where the market expects them (NL, DE, TR, FR).
5. The market's top payment method appears first; methods not offered are never shown as logos.
6. Form fields: only what fulfillment needs; correct `autocomplete` tokens; country first; address lookup where available; "Billing same as shipping" checked by default (WCAG 3.3.7 Redundant Entry).
7. Inline validation on blur and on submit, with an error summary and focus to the first error.
8. No CAPTCHA that blocks assistive tech users; use invisible risk scoring or accessible alternatives (WCAG 3.3.8 Accessible Authentication).
9. Order button wording that states the obligation to pay (Germany: "zahlungspflichtig bestellen" or an equally unambiguous label, § 312j BGB).
10. Required legal acceptance only where the law requires it (Turkey: pre-information form and distance sales contract acknowledgment; terms checkbox elsewhere only if legal advises).
11. No preselected paid add-ons, insurance or BNPL.
12. After any checkout change: test order in test mode and tracking verification with `measurement`.

## 4. Payment method visibility by market

| Market | Put first | Also expected | Watch outs | Label |
|--------|-----------|---------------|-----------|-------|
| Netherlands | iDEAL \| Wero (iDEAL \| Wero co-brand since 2026-Q1) | Cards, Apple Pay, PayPal, Klarna (pay later), Bancontact for Belgian buyers | Update logo and name to iDEAL \| Wero; plan the Wero contract switch from Q4 2026 and before iDEAL's planned end on 2027-12-31; A/B test Wero vs iDEAL per Stripe guidance (`cro`) | [Official, 2026] |
| Germany | PayPal | Invoice (Rechnung via Klarna, Ratepay, Unzer, Billie for B2B), SEPA direct debit, cards, Apple Pay, Google Pay, Klarna | EHI: PayPal 28.5%, invoice 25.8%, direct debit 17.3%, cards 12.3% of 2024 online purchases; giropay ended 2024-06-30; order button wording | [Study, EHI 2025] |
| Turkey | Credit card with installments (taksit) | TROY cards, debit cards, bank transfer (havale, EFT, FAST), BKM Express, cash on delivery for some categories | Installments around 55% of online transactions (2024); TROY 25.3% of card transaction value in 2025 with 90 million cards; domestic acquiring needed for TROY and installments; cards start disabled for ecommerce until the holder enables them; Shopify Payments not available, use local gateways (iyzico, PayTR, others) | [Study, Worldline 2024] [Official, BKM 2026-01] |
| Saudi Arabia | mada (debit) and Apple Pay | Cards, STC Pay, Tabby, Tamara, cash on delivery | Shopify Payments not available; mada through gateways such as Tap or Moyasar; COD rules by order value | [Unverified, vendor sources 2026] |
| UAE | Cards and Apple Pay | Tabby, Tamara, COD (reported 25% to 30% of orders outside Dubai) | Shopify Payments not available; gateways such as Checkout.com, Telr, PayTabs | [Unverified, vendor sources 2026] |
| US, UK | Wallets (Shop Pay, Apple Pay, Google Pay, PayPal) and cards | Klarna, Afterpay, Affirm | BNPL messaging rules differ by state and FCA | [Practitioner consensus] |

Use your own gateway data (method share and success rate by market, device and order value) before reordering. The tables above are starting hypotheses.

Shopify implementation: payment customization Function (hide, reorder or rename methods by market, cart total, product type) through a public app on any plan, or a custom app on Plus. Delivery customization Function for delivery option ordering and naming. Storefront payment icons via `shop.enabled_payment_types` filtered per market (or a manual setting per market).

## 5. BNPL and installments (CCD2 from 2026-11-20)

Rules for storefront and checkout UI (confirm national transposition with `compliance`):
- BNPL can be offered next to other methods but not preselected.
- Advertising of credit (banners, PDP lines, emails, social ads) must carry the mandatory risk warning where national law requires it.
- Provider pre-contract information (SECCI) must be readable on mobile; it is the provider's flow, but do not wrap it in a cramped iframe or modal stacked over the cart drawer.
- A merchant's own interest-free deferral is exempt only when paid within 50 days of delivery (14 days for large online sellers) and with limited late fees; third-party BNPL generally is in scope.
- Klarna is updating shopper agreements; recurring Pay Later charges without a new agreement route to Pay Now in EU markets [Unverified, Kustom help 2026].
- Turkey installments: show the installment table (bank programs such as Bonus, Maximum, World, Axess, CardFinans, Paraf, Advantage) on the PDP or in checkout from the gateway API; state who pays the installment markup.

## 6. Field and address patterns by market

| Market | Address pattern | Phone | Notes |
|--------|-----------------|-------|-------|
| Netherlands | Postcode plus house number lookup fills street and city | Optional unless carrier needs it | Pickup points (PostNL, DHL) common |
| Germany | Street plus house number, postal code, city; Packstation option | Optional | Company field for B2B; VAT ID for EU B2B |
| Turkey | Province (il), district (ilçe), neighborhood (mahalle), full address text | Required for couriers | T.C. identity number may be requested for invoices above legal thresholds; e-Arşiv invoice by email [Unverified on thresholds] |
| Saudi Arabia, UAE | City, district, street, building, national address (KSA) | Required, with country code | Arabic and Latin input both accepted; RTL forms |

Use `autocomplete` tokens (`given-name`, `family-name`, `email`, `tel`, `postal-code`, `address-line1`, `address-level2`, `country`), `inputmode="numeric"` for postal codes where numeric, 16 px inputs on mobile.

## 7. Checkout accessibility checks

- Every field has a visible label; errors linked with `aria-describedby`; `aria-invalid` on invalid fields.
- Payment method list is a radio group with names as text.
- Order button reachable and named; no CAPTCHA blocking keyboard or screen reader users.
- Timeouts warn and allow extension (WCAG 2.2.1).
- Platform checkouts (Shopify, Woo Checkout block) handle most semantics; your extensions and custom fields must match.

## 8. Checkout change protocol

1. Snapshot current settings (screenshots of checkout editor, payment method order per market, apps with extensions).
2. Draft the change request (`ads-master/templates/CHANGE_REQUEST.md`) with rollback steps.
3. Build in a development store or as an unpublished configuration; preview with `site-engineer`.
4. Human approves (G3); publish or schedule; for experiments use Rollouts or the testing tool with `cro`.
5. Place a test order (test mode or Bogus gateway on a dev store) per market and payment method; `measurement` verifies purchase events and values on every ad platform.
6. Monitor checkout completion by market and method for 7 days; roll back on a drop beyond the agreed guardrail.

## 9. KPIs

Checkout start to completion by step, device, market and payment method; payment failure rate by method; share of orders by method vs market expectation; express checkout share; error rate per field; time to complete; COD refusal rate (GCC, TR).
