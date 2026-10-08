# Accessibility, WCAG 2.2 and the European Accessibility Act

Legal status, standards, enforcement so far, the storefront component checklist and the testing protocol. Accessibility is table stakes: defects go straight to the TS lane. Legal interpretation belongs to `compliance` and counsel; this module tells you what to build and test.

## 1. Legal and standards status (as of 2026-10-08)

| Item | Status | Label |
|------|--------|-------|
| European Accessibility Act (Directive (EU) 2019/882) | Applies since 2025-06-28 to ecommerce services offered to EU consumers; national laws set penalties | [Official, 2025-06] |
| Microenterprise exemption | Service providers with fewer than 10 employees and annual turnover or balance sheet of EUR 2 million or less are exempt for services | [Official] |
| Existing contracts and products | Transition rules for services under contracts concluded before 2025-06-28 (until 2030 at the latest) and some self-service terminals; not a reason to delay storefront fixes | [Official] |
| Harmonised standard currently cited | EN 301 549 v3.2.1 (based on WCAG 2.1 AA) is the cited version; one law firm argues no standard is cited under the EAA itself | [Contested, 2026-08] |
| EN 301 549 v4.1.1 | Adopted 2026-08-24, published by ETSI 2026-09-02; incorporates WCAG 2.2 AA (six new criteria, removes 4.1.1 Parsing), adds EAA mapping (Annex ZB, clause A.2); Official Journal citation expected late November to December 2026 | [Official, 2026-09] |
| Build target | WCAG 2.2 AA now; claims of conformance name the version tested (v3.2.1 until v4.1.1 is cited) | [Practitioner consensus] |
| US | ADA Title III lawsuits continue; no single federal web standard for private retailers; WCAG 2.1 or 2.2 AA used in settlements | [Practitioner consensus] |

Enforcement so far:

| Market | What happened | Label |
|--------|---------------|-------|
| France | Court in Caen ordered Carrefour (2026-06-04) to make its site and app accessible within 6 months, EUR 500 per day of delay; meeting about 71% of RGAA criteria was not enough; Lille dismissed the claim against Auchan's ecommerce arm (May 2026) citing a revenue threshold, appeal pending in Douai | [Official court reports via secondary, 2026] |
| Netherlands | ACM tested about 100 large webshops and providers (2026-03): about 61% not digitally accessible; ordering often blocked by inaccessible order buttons and CAPTCHA; ACM directs firms to improve, enforcement follows for laggards | [Official, 2026-03] |
| Sweden | PTS opened 28 supervision cases on ecommerce sites (from 2025-10) and received 124 complaints, most about webshops | [Official, 2026] |
| Germany | Early pressure through competition law (UWG) letters against web shops rather than BFSG authority fines | [Practitioner reports, 2026-04] |
| EU wide | No confirmed administrative EAA fine against an online shop found as of 2026-10; penalty ranges vary widely by country and sources conflict | [Unverified] |

The EAA also requires service information on how the service meets accessibility requirements (an accessibility statement in the terms or a dedicated page). Draft it with `compliance`.

Accessibility overlays (widget scripts) do not make a store conformant; the US FTC ordered accessiBe to pay USD 1 million over misleading claims (2025-01) [Official, 2025-01]. Do not recommend overlays.

## 2. WCAG 2.2 criteria that bite storefronts most

| SC | Level | Storefront risk |
|----|-------|-----------------|
| 1.1.1 Non-text content | A | Product images without useful alt, icon buttons without names, text in banner images |
| 1.3.1 Info and relationships | A | Filters without fieldsets, price lists as divs, tables without headers |
| 1.4.3 Contrast (minimum) | AA | Light grey prices, sale badges, placeholder text (low contrast on 83.9% of home pages, WebAIM 2026) |
| 1.4.10 Reflow | AA | Tables and filter bars that scroll horizontally at 320 px |
| 1.4.11 Non-text contrast | AA | Swatch borders, focus rings, input borders |
| 2.1.1 Keyboard | A | Mega menus, galleries, swatches, quick add, sliders |
| 2.2.1 Timing adjustable | A | Auto-dismissing toasts with actions, checkout timeouts |
| 2.2.2 Pause, stop, hide | A | Auto-rotating hero, marquees, announcement rotators |
| 2.4.3 Focus order | A | Drawers that open without focus moving; DOM order differing from visual order |
| 2.4.7 Focus visible | AA | `outline: none` |
| 2.4.11 Focus not obscured (minimum) (new in 2.2) | AA | Sticky header, sticky add to cart, cookie banner covering focused elements |
| 2.5.7 Dragging movements (new) | AA | Price sliders, swipe-only galleries, drag-to-dismiss sheets without buttons |
| 2.5.8 Target size (minimum) (new) | AA | Swatches, quantity steppers, close icons under 24 by 24 CSS px |
| 3.2.6 Consistent help (new) | A | Contact or chat placement changing between templates |
| 3.3.1 Error identification, 3.3.3 Error suggestion | A, AA | Checkout and account forms |
| 3.3.7 Redundant entry (new) | A | Re-entering billing address, re-entering email in multi-step flows |
| 3.3.8 Accessible authentication (minimum) (new) | AA | CAPTCHA puzzles at login, checkout or reviews; blocked paste in password or code fields |
| 4.1.2 Name, role, value | A | Custom selects, toggles (wishlist hearts), accordions without `aria-expanded` |
| 4.1.3 Status messages | AA | Cart updates, filter counts, add to cart results without live regions |

WebAIM Million 2026 (home pages, automated): 95.9% with detectable failures, 56.1 errors per page; low contrast 83.9%, missing alt 53.1%, missing form labels about 51%, empty links 46.3%, empty buttons 30.6%, missing document language 13.5% [Study, 2026-02, via secondary coverage]. Fix these six first; they are most automated findings.

## 3. Component checklist (storefront)

| Component | Must have |
|-----------|-----------|
| Skip link | First focusable element, "Skip to content", visible on focus |
| Header nav | `<nav aria-label>`, disclosure buttons with `aria-expanded`, Escape closes, no focus trap |
| Mobile menu | Modal dialog semantics, focus to first item or heading, return focus, Escape |
| Search | Labeled input, combobox semantics for autocomplete, results count announced |
| Filters | Fieldsets and legends, real checkboxes, count in `role="status"`, slider with inputs |
| Product card | One link with the product name, price labels for sale and regular, alt text, rating as text |
| Gallery | Named controls, alt per image, zoom dialog accessible, no autoplay with sound, captions |
| Variant picker | Radio groups with legends, sold-out values focusable and labeled, changes announced |
| Quantity stepper | Labeled input, buttons named with product, min and max enforced with messages |
| Add to cart | Button with status feedback in a live region |
| Cart drawer | Dialog semantics, heading label, focus management, line actions named |
| Accordions | `<details>` or buttons with `aria-expanded` and `aria-controls` |
| Carousels | Pause control if auto, slide labels ("2 of 5"), buttons, no keyboard trap (Embla accessibility plugin sets roles and labels) |
| Toasts | Pre-existing polite region, long enough duration, not the only channel |
| Forms | Visible labels, `autocomplete`, inline errors, error summary, no CAPTCHA wall |
| Language | `<html lang>` per locale, `lang` on mixed-language snippets, `dir` for RTL |
| Media | Captions for product videos with speech, transcripts for long videos |
| Cookie banner | Keyboard reachable, does not trap focus forever, does not obscure focus (2.4.11) |
| Third-party widgets | Reviews, chat, BNPL, size tools tested like your own code; vendors asked for conformance reports |

## 4. Testing protocol

Per template, per release that touches UI:
1. Automated: axe DevTools or Lighthouse on mobile and desktop; zero critical and serious issues. Automated checks find only part of the issues.
2. Keyboard only: complete tasks T1, T3, T7 and T9 from the [Audit method](storefront-audit-method.md); check focus visibility and order, Escape behavior, no traps.
3. Screen readers: VoiceOver on iOS Safari (main mobile path), NVDA with Firefox or Chrome on Windows (desktop path); verify names, roles, live regions on add to cart, filters, cart updates.
4. Zoom and reflow: 200% text zoom, 400% zoom at 1280 px (equals 320 px reflow), no horizontal scroll except data tables.
5. Contrast: tokens checked (4.5:1 text, 3:1 large text and UI components and focus indicators).
6. Motion: reduced motion on; nothing essential lost.
7. Forced colors (Windows high contrast): focus and borders visible.
8. Third-party: run the same checks with apps enabled.

Record results in the audit checklist section K and log defects with severity:
- Critical: a group of users cannot complete purchase (keyboard trap in drawer, unlabeled pay button, CAPTCHA wall).
- High: key task much harder (filters unusable by keyboard, no live feedback on add to cart).
- Medium: degraded but possible.

## 5. Platform notes

- Shopify themes in the Theme Store must meet accessibility requirements (Lighthouse accessibility score of at least 90 on key pages among them) [Official]; custom themes and app code often regress after launch.
- Horizon: native `<dialog>` drawers, fieldset-based variant picker with sold-out labels, `role="status"` filter counts, `role="search"`, focus utilities, RTL support since 4.2.0. Still test after customization.
- Hydrogen skeleton: the `Aside` drawer lacks focus trapping and focus return; replace with an accessible dialog primitive.
- Next.js Commerce: Headless UI dialog for the cart, status live region for add to cart; disables sold-out variant buttons (blocks focus and back-in-stock).
- WooCommerce blocks and Checkout block: maintained with accessibility work upstream; classic extensions may inject inaccessible markup.
- Checkout on Shopify is platform-controlled; your checkout UI extensions must use the provided components correctly (labels, headings).

## 6. Accessibility in the change lanes

- Every accessibility defect is TS: fix, verify, log. No A/B test of accessibility fixes.
- Design changes that carry accessibility risk (sticky bars, auto-rotation, swipe-only UI) are TF and must pass this protocol in every variant.
- Accessibility statement and feedback mechanism: a contact route for accessibility issues on every page (footer), answered within a defined time.
