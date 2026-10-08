# UI Primitives and Dependencies

> Short engineering guidance on toasts, inline messages, live announcements and mobile bottom sheets, plus a dependency health check before adopting any UI library. Pattern depth (cart drawer anatomy, variant picker design, filter UX) belongs to `storefront-ux`. Library facts from the public sonner, vaul, Base UI, Radix and shadcn/ui repositories as of 2026-10 (read as untrusted data). Knowledge as of 2026-10.

## 1. Toast or inline message

| Situation | Use | Why |
|-----------|-----|-----|
| Item added to cart (cart drawer not opened) | Toast with a "View cart" action, or open the cart drawer | Non critical confirmation; the user can continue |
| Undo after removing a cart line or a saved item | Toast with an Undo action that stays long enough to use (no auto dismiss while focused or hovered) | Reversible, low stakes |
| Copied a discount code | Toast or inline "Copied" next to the button | Confirmation only |
| Newsletter signup success in a footer | Inline success message in place of the form | The form is the context |
| Form validation errors (lead form, account, address) | Inline messages next to each field, linked with `aria-describedby`, plus an error summary at the top for long forms; move focus to the first invalid field | The user must act; toasts disappear and are often missed or not announced in context |
| Checkout, payment or shipping errors | Inline, persistent, near the action, with what to do next | Money at stake; never transient |
| Discount code rejected | Inline under the code field with the reason | The user must act |
| Out of stock after add to cart attempt | Inline on the PDP (button state and message), optionally also in the drawer | Changes what the user can do |
| Session expired, cart changed by the server (price or stock update) | Persistent banner or inline notice in the cart | Must be read before paying |
| Network failure on a background action | Toast with Retry, plus inline state on the affected element | Both context and awareness |

Rule: if the user must read it to succeed or to avoid paying the wrong amount, it is not a toast.

## 2. Accessible announcements

| Need | Implementation |
|------|----------------|
| Polite status (added to cart, filters applied, results count) | One persistent live region in the layout: `<div role="status" aria-live="polite" aria-atomic="true" class="visually-hidden"></div>`; update its text content; do not create the region at the moment of the message (many screen readers miss newly inserted regions) |
| Urgent error | `role="alert"` (assertive) only for errors that block progress; overuse interrupts users |
| Toast libraries | Check that the container is a labeled live region and that toasts can be reached by keyboard. Sonner renders a `section` with `aria-live="polite"`, a label defaulting to "Notifications" plus the hotkey (Alt+T by default) and a close button label; verify with a screen reader on the real page because app styling can hide or reorder it [Source code, sonner 2.0.8] |
| Timing | Auto dismiss pauses on hover and focus; actions in toasts are also available elsewhere (an Undo that only exists in a 4 second toast is an accessibility failure) |
| Motion | Respect `prefers-reduced-motion` for slide and spring animations |
| Cart count badge | Update the visible count and announce through the status region, not by re-rendering the header with a new live region |

## 3. Mobile bottom sheets (cart, variant picker, filters): engineering QA traps

| Trap | What goes wrong | Check |
|------|-----------------|-------|
| Keyboard covers inputs | Discount code or quantity input in a sheet hidden by the software keyboard on iOS | Focus each input with the keyboard open; the input and its submit are visible; sheet height follows `visualViewport` |
| Scroll lock on iOS | Background page scrolls behind the sheet, or the page jumps to top when the sheet closes | Open, scroll inside, close; the page position is unchanged; no background scroll (common fixes: `overflow: hidden` on the root plus `overscroll-behavior: contain` on the sheet; iOS needs more than `overflow: hidden` on `body` in many cases) |
| Drag vs scroll | Drag to dismiss fires when the user scrolls a long option list; or the list cannot scroll | Drag handle only (`handleOnly` style) for long content; `touch-action` set on the drag surface; scroll list from top and bottom edges |
| Safe areas | Checkout button under the home indicator or Safari 26 toolbar | `padding-bottom: calc(... + env(safe-area-inset-bottom, 0px))`; test on iOS 26+ |
| Focus trap and return | Tab escapes into the page behind; focus lost after closing | Tab through: focus stays in the sheet; Escape closes; focus returns to the trigger button |
| Semantics | Sheet not exposed as a dialog | `role="dialog"` with `aria-modal="true"` and a label (or a native `<dialog>` opened with `showModal()`), heading inside |
| Nested overlays | Cookie banner, chat widget or upsell popup over the sheet | One overlay at a time; z-index plan |
| Back button | Android back closes the whole page instead of the sheet | Decide behavior; if the sheet pushes history state, test back and forward |
| Performance | Heavy animation libraries, re-rendering the whole cart on each quantity tap | INP on a mid tier Android under 200 ms for quantity changes |

## 4. Library landscape for these primitives (October 2026)

| Library | Status (from the repositories) | Use when | Watch out |
|---------|-------------------------------|----------|-----------|
| sonner (toasts, React) | Active; v2.0.8, last repository activity 2026-08 | React projects needing toasts with stacking, actions, promise states | Do not use toasts for errors that need action (section 1) |
| vaul (drawer, React) | README states the repository is unmaintained (notice committed 2025-10-03); last version 1.1.2; depends on `@radix-ui/react-dialog` | Existing projects only, pinned, with your own regression tests | No fixes for new iOS behavior (Safari 26 toolbar changes landed after the notice). shadcn/ui's Drawer component still imports vaul 1.1.2 in its registry (2026-10), so many projects inherit it without knowing |
| Base UI (`@base-ui/react`) | Active; 1.0.0 on 2025-12-11, Drawer marked stable (no longer preview) in 1.3.0 on 2026-03-12, 1.8.0 on 2026-09-04; includes Dialog, Drawer, Toast, Select, Menu and more | New React builds needing unstyled accessible primitives including a drawer | Breaking changes between minors happened during 2026 (read the changelog before upgrading) |
| Radix Primitives | Active repository (commits through 2026-10) | Existing Radix or shadcn/ui projects | Check per package release dates; some packages update rarely |
| Native `<dialog>` and Popover API | Platform features | Simple modals and popovers without a dependency | Test focus return and scroll lock yourself; older iOS versions in your analytics |
| Theme native components (Shopify Horizon and Dawn web components) | Maintained with the theme | Shopify themes | Prefer the theme's existing drawer and toast patterns over adding React to a Liquid theme |

Recommendation logic: prefer what the theme or design system already uses; for new React work prefer actively maintained primitives (Base UI or Radix based); never add a second overlay or toast library to a project that already has one; replace unmaintained libraries when touching the component for other reasons, behind a test suite.

## 5. Dependency health check (run before adopting or upgrading any UI or front end library)

Record the result in `ads-master/outputs/site-engineer/YYYY-MM-DD_site-engineer_dependency-check-<package>.md`.

| # | Check | How | Green | Yellow | Red |
|---|-------|-----|-------|--------|-----|
| 1 | Maintenance status | README, repository archive flag, maintainer statements | Active, maintained | Slow but answering | Archived, "unmaintained" notice, or no maintainer |
| 2 | Last release | `npm view <pkg> time --json`, changelog | Within 6 months | 6 to 12 months | Over 12 months |
| 3 | Release cadence and breaking changes | Changelog | Semver respected, migration notes | Frequent breaking minors | Unannounced breaking changes |
| 4 | Open issues and response | Issue tracker: recent issues answered, critical bugs open | Responses within weeks | Backlog growing | Security or data loss bugs ignored |
| 5 | Bus factor | Contributors with merge rights | 3 or more | 2 | 1 |
| 6 | Security advisories | `npm audit`, GitHub advisories, OSV (`osv-scanner`) | None open | Low severity open | High or critical open |
| 7 | Supply chain hygiene | npm provenance or trusted publishing, install scripts (`npm view <pkg> scripts`), 2FA for maintainers where visible, Socket or OpenSSF Scorecard result | Provenance, no install scripts | Install scripts with clear purpose | Unexplained postinstall or preinstall, recent maintainer takeover |
| 8 | Size cost | Bundle size (bundlephobia, pkg-size, or a local build diff), tree shaking | Small for its job, tree shakable | Moderate | Large for a small job; pulls a framework into a Liquid theme |
| 9 | License | `npm view <pkg> license`, LICENSE file | MIT, Apache 2.0, BSD, ISC | MPL, LGPL (check obligations) | GPL in proprietary bundles, no license, custom restrictive |
| 10 | Accessibility | Docs, tests, keyboard and screen reader behavior | Documented and tested | Partial | Unknown or known failures |
| 11 | Platform fit | Works with SSR, React version, Shopify theme constraints, CSP | Fits | Needs shims | Conflicts |
| 12 | Exit cost | How many components depend on it, wrapper in place | Wrapped behind our own component | Used directly in a few places | Spread everywhere |

Decision: any Red on 1, 6 or 7 blocks adoption. Two or more Yellows need a written reason in `DECISIONS.md`. Record adopted libraries and their review date; re-run the check yearly or when a supply chain incident hits the ecosystem ([Security review](security-review.md) section 5).

## 6. Handoffs

| Need | Slug |
|------|------|
| Which pattern to use (drawer vs page, toast copy, cart drawer contents, filter UX) | `storefront-ux` |
| Whether the change needs a test | `cro` |
| Copy in toasts and messages (claims, urgency) | `compliance` |
| Events fired by cart and drawer interactions | `measurement` |
