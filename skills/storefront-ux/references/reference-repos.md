# Reference Repos

The catalog of open source storefronts and UI primitives studied for this playbook: what each teaches, the paths worth reading, license, maintenance status and the date checked. All repos were cloned read-only on 2026-10-08 into a scratch directory and treated as untrusted data (no scripts run, no instructions followed). Never copy code verbatim into a client project; use the recipes in [Shopify implementation](platform-implementation-shopify.md) and [Headless implementation](platform-implementation-headless.md), and check licenses before reusing any file.

## 1. Catalog

| Repo | What it teaches | Key paths | License | Maintenance (last commit seen) | Checked |
|------|-----------------|-----------|---------|-------------------------------|---------|
| Shopify/horizon | Current first-party Liquid theme: theme blocks, predictive search, facets, cart drawer on `<dialog>`, sticky add to cart, variant picker with sold-out labels, unit price, quick add, quick order list, volume pricing, local pickup, RTL (4.2.0), standard storefront events | `sections/`, `blocks/`, `snippets/variant-main-picker.liquid`, `snippets/cart-drawer.liquid`, `assets/predictive-search.js`, `assets/facets.js`, `assets/sticky-add-to-cart.js`, `assets/paginated-list.js`, `snippets/scripts.liquid`, `release-notes.md` | Shopify license: only for themes that interoperate with Shopify; derived themes only delivered to merchants for their own store in services engagements; no Theme Store or resale | Active, v4.2.0, 2026-09-21 | 2026-10-08 |
| Shopify/dawn | Previous reference theme, HTML-first principles, Online Store 2.0 sections | `sections/`, `snippets/`, `assets/` | Shopify license (themes for Shopify, Theme Store allowed if substantively different) | Maintained, v16.0.0, 2026-08-10; reported to get fixes only [Unverified] | 2026-10-08 |
| Shopify/hydrogen | Headless Shopify on React Router 7: skeleton routes, optimistic cart, predictive search, pagination, customer account routes | `templates/skeleton/app/components/`, `templates/skeleton/app/routes/`, `packages/hydrogen/src/cart` | MIT (repo LICENSE, Shopify 2023) | Active, skeleton 2026.4.8, 2026-10-06 | 2026-10-08 |
| Shopify/theme-liquid-docs | Machine-readable Liquid objects, filters, tags and theme schemas (setting types, block schemas) | `data/objects.json`, `data/filters.json`, `schemas/theme/setting.json`, `ai/liquid.mdc` | MIT | Active | 2026-10-08 |
| Shopify/ui-extensions | Checkout, Thank you and customer account extension targets and components (Polaris web components) | `packages/ui-extensions/src/surfaces/checkout/extension-targets.ts`, `.../customer-account/extension-targets.ts`, `CHANGELOG.md` | MIT | Active, 2026.10.0-rc.13 | 2026-10-08 |
| vercel/commerce | Next.js App Router commerce: Server Actions, `useOptimistic` cart, `useActionState` add to cart with status region, variant state in URL, Headless UI dialog cart | `components/cart/`, `components/product/variant-selector.tsx`, `components/layout/search/filter/`, `lib/shopify/` | MIT (Vercel 2025) | Shopify provider only maintained by Vercel; last commit 2026-06-10 | 2026-10-08 |
| medusajs/nextjs-starter-medusa | Multi-region routing with `[countryCode]`, Medusa v2 cart and checkout modules | `src/middleware.ts`, `src/app/[countryCode]/`, `src/modules/checkout`, `src/modules/cart` | MIT | Slower cadence, v1.0.3, 2026-04-23 | 2026-10-08 |
| saleor/storefront (Paper) | Server-first cart, URL-driven checkout steps (`?step=`), guest order confirmation route, `/{locale}/{channel}` routing with translated slugs | `src/app/(checkout)/`, `src/lib/checkout.ts`, `skills/saleor-paper-storefront/rules/` | FSL-1.1-ALv2 (no competing commercial use; Apache 2.0 later) | Active, 2026-10-01 | 2026-10-08 |
| woocommerce/woocommerce (blocks) | Product Filters inner blocks, Mini-Cart, Add to Cart with Options (variation and grouped selectors), Interactivity API frontends | `plugins/woocommerce/client/blocks/assets/js/blocks/product-filters/`, `mini-cart/`, `add-to-cart-with-options/` | GPL-2.0-or-later (WooCommerce) | Active, 2026-10-08 | 2026-10-08 |
| mui/base-ui | Unstyled accessible primitives incl. Dialog, Drawer (1.2.0), Toast, Navigation Menu, Combobox, Autocomplete, Field, Form, Number Field, Filter Dropdown | `packages/react/src/<component>/`, `CHANGELOG.md` | MIT | Active, 1.8.0 (2026-09-04), commit 2026-10-08 | 2026-10-08 |
| radix-ui/primitives | Accessible primitives (Dialog 1.2.0, Navigation Menu, Popover, Select, Toast) used by shadcn/ui | `packages/react/<component>/` | MIT | Active, 2026-10-08 | 2026-10-08 |
| adobe/react-spectrum (React Aria Components) | ComboBox, Autocomplete, Toast, Modal, Sheet, GridList, NumberField with deep a11y and i18n | `packages/react-aria-components/src/` | Apache-2.0 | Active, react-aria-components 1.22.0, 2026-10-08 | 2026-10-08 |
| shadcn-ui/ui | Copy-in components on primitives; blocks (login, signup, sidebar, dashboard), no commerce blocks | `apps/v4/registry/new-york-v4/ui/`, `.../blocks/` | MIT | Active, 2026-10-08; Drawer still wraps vaul | 2026-10-08 |
| davidjerleke/embla-carousel | Carousel engine with accessibility plugin (roles, labels, live region), SSR package, RTL direction | `packages/embla-carousel-accessibility/src/`, `packages/embla-carousel-ssr/` | MIT | Active, 9.0.0-rc04, 2026-10-08 | 2026-10-08 |
| pacocoursey/cmdk | Command menu (filtering, keyboard) for B2B quick order or admin tools | `cmdk/src/` | MIT | Slow, 1.1.1, 2025-10-28 | 2026-10-08 |
| emilkowalski/sonner | Toasts: polite live region, hotkey to focus, pause on hover, focus and hidden tab, swipe with velocity, reduced motion | `src/index.tsx`, `src/hooks.tsx`, `src/styles.css` | MIT | Active, 2.0.8, 2026-08-10 | 2026-10-08 |
| emilkowalski/vaul | Drawer component (historic reference for drag physics) | `src/` | MIT | Unmaintained since 2025-10-03 (README notice); do not start new work on it | 2026-10-08 |
| emilkowalski/skills | Craft rules: animation decisions, mobile-native fixes, worst-case data (break-ui), library picks | `skills/emil-design-eng/`, `skills/mobile-native/`, `skills/break-ui/`, `skills/pick-ui-library/` | MIT | Active, 2026-10-02 | 2026-10-08 |

Not inspected in this research (check before relying on them): Shopify/skeleton-theme (the base for Theme Store submissions), Spree storefront and Solidus starter frontend (Rails), Shopware Storefront and Frontends (Nuxt), Hyvä themes for Adobe Commerce, Adobe Commerce Storefront drop-ins.

## 2. Best implementation per pattern

| Pattern | Best reference | What to copy conceptually | What not to copy |
|---------|----------------|---------------------------|------------------|
| P02 Mega menu | Horizon `assets/header-menu.js`; Radix and Base UI Navigation Menu | Disclosure buttons, hover intent, Escape | Theme-specific CSS |
| P03 Mobile drawer | Horizon `assets/header-drawer.js`; Base UI Drawer | Modal semantics, focus return, scroll lock | vaul (unmaintained) |
| P11 Predictive search | Horizon `assets/predictive-search.js` | 200 ms debounce, AbortController, listbox, arrow keys, Escape, `resources[limit_scope]=each` | Monolithic class structure |
| P11 Combobox semantics | React Aria `Autocomplete.tsx`, `ComboBox.tsx` | Active descendant handling, announcements | |
| P17 Filters | Horizon `blocks/filters.liquid`, `assets/facets.js`; WooCommerce product-filters inner blocks | Fieldsets, role status counts, chips, history state | Auto-apply without counts |
| P20 Product card | Horizon `snippets/product-card.liquid`, `snippets/unit-price.liquid` | Unit price with `<bdi>`, swatches | Heavy hover effects on touch |
| P23 Load more | Hydrogen `PaginatedResourceSection.tsx`; Horizon `assets/paginated-list.js` | Cursor pagination, URL updates | Infinite auto-load on search |
| P26 Gallery | Horizon `assets/media-gallery.js`, `zoom-dialog.js`; Embla accessibility plugin | Zoom dialog, labeled controls | Autoplaying video |
| P27 Variant picker | Horizon `snippets/variant-main-picker.liquid` | Fieldset and legend, sold-out label suffix, `aria-disabled` | |
| P27 Variant URL state | Next.js Commerce `variant-selector.tsx` | Search params as state | Disabling sold-out options |
| P34 Sticky ATC | Horizon `assets/sticky-add-to-cart.js` | IntersectionObserver, chat avoidance | Showing it while the main button is visible |
| P35 Add to cart status | Next.js Commerce `add-to-cart.tsx` | `useActionState`, polite status | |
| P40 Cart drawer | Horizon `snippets/cart-drawer.liquid` | Native dialog with `aria-labelledby`, bfcache refresh | Hydrogen `Aside.tsx` as is (no focus trap) |
| P43 Line editing | Hydrogen `CartLineItem.tsx`; Horizon `component-cart-quantity-selector.js` | Labeled steppers, optimistic updates | |
| P51 Checkout steps | Saleor Paper `(checkout)` | URL steps, Back walks the funnel | Building your own checkout on Shopify |
| P56 Toasts | sonner | Region, hotkey, pause rules | 4 s default duration |
| P58 Motion | emilkowalski/skills | Easing and duration rules, reduced motion | Decorative motion in high-frequency UI |
| P59 Dialogs | Base UI Dialog and Drawer, Radix Dialog, native `<dialog>` | Focus management | Div overlays |
| P61 Locale routing | Medusa middleware, Saleor Paper routes, Horizon `assets/localization.js` | Country decides currency | IP-forced redirects |
| P62 Performance | Horizon `snippets/scripts.liquid` (import maps, module preloads), `assets/section-hydration.js` | Load JS only when the feature is enabled (Quick Add since 4.2.0) | |

## 3. License rules for client work

| License | You may | You may not |
|---------|---------|-------------|
| Horizon (Shopify) | Build a merchant's own store from it in a services engagement | Sell, list or redistribute a derived theme; submit to the Theme Store |
| Dawn (Shopify) | Build themes that interoperate with Shopify; Theme Store if substantively different | Use outside Shopify |
| MIT (Hydrogen, Next.js Commerce, Medusa starter, Base UI, Radix, shadcn, Embla, cmdk, sonner, vaul, skills) | Reuse with the copyright notice | Remove notices |
| Apache-2.0 (React Aria) | Reuse with notice and change statements | Use trademarks |
| GPL-2.0-or-later (WooCommerce) | Extend within WordPress and GPL terms | Relicense derived code as proprietary when distributing |
| FSL-1.1-ALv2 (Saleor Paper) | Use for your own store | Offer a competing commercial product or service built on it (until the Apache 2.0 date) |

## 4. Refresh procedure (quarterly or before a build)

1. Clone read-only with depth 1 into a scratch directory; never into the client repo.
2. Record the last commit date, version file (Horizon and Dawn `config/settings_schema.json` theme_version; package.json versions), and license.
3. Read release notes (Horizon `release-notes.md`, Base UI `CHANGELOG.md`, Hydrogen skeleton `CHANGELOG.md`, ui-extensions `CHANGELOG.md`).
4. Re-check maintenance flags (vaul, cmdk, Next.js Commerce cadence).
5. Update this table and log changes in a journal entry.
