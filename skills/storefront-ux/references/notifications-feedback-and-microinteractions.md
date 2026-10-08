# Notifications, Feedback and Microinteractions

When to use inline messages, toasts, banners and dialogs; how to make feedback accessible; motion rules with restraint; mobile-native polish. Draws on sonner's implementation and Emil Kowalski's public craft rules (emilkowalski/skills, MIT, read 2026-10-08) translated into storefront rules in our own words. Patterns P56 to P58 in the [Pattern library](ux-pattern-library.md).

## 1. Evidence and sources

| Point | Source | Label |
|-------|--------|-------|
| Validations, notifications and indicators are different tools chosen by urgency and whether action is needed | NN/g "Indicators, Validations, and Notifications" | [Study, NN/g] |
| GitHub Primer considers toasts a significant accessibility concern and does not recommend them | Primer accessibility docs | [Official design system] |
| Adobe Spectrum: toasts stay at least 6,000 ms; Pearson: at least 5 seconds | Spectrum Web Components, Pearson guidelines | [Official design system] |
| Auto-dismissing toasts and WCAG 2.2.1 Timing Adjustable: debated on the W3C WAI list (2025) | w3c-wai-ig archives 2025 | [Contested] |
| sonner: default lifetime 4,000 ms, 3 visible, region `aria-live="polite"` labeled "Notifications alt+T", pauses while hovered, focused or tab hidden, honors reduced motion | sonner 2.0.8 source `src/index.tsx`, `src/hooks.tsx`, `src/styles.css` | [Official repo, 2026-08] |
| vaul (drawer) unmaintained since 2025-10-03; shadcn/ui drawer still wraps vaul | vaul README; shadcn `apps/v4/registry/new-york-v4/ui/drawer.tsx` | [Official repo, 2025-10] |
| Base UI added a Drawer component in 1.2.0 (2026-02-12) and a Toast component | Base UI CHANGELOG | [Official repo, 2026-02] |
| INP good threshold 200 ms | web.dev | [Official] |

## 2. Decision tree: which feedback channel

```
Is it an error or blocker the user must fix?
  yes -> Inline message next to the cause (field, line item, button). Persistent. Summary at top for forms.
  no  -> Is it the direct result of the action the user just took, in view?
           yes -> Change the control itself (button state, quantity, heart toggle) plus a status live region.
                  If the result lives elsewhere (cart), open or update that surface (cart drawer, count badge).
           no  -> Is it about something that happened outside the current view (saved in background,
                  item back in stock while browsing, network restored)?
                    yes -> Toast (non-critical, with a persistent place to find it later).
                    no  -> Is it page-wide and lasting (store closed for holidays, payment outage)?
                             yes -> Banner at the top, dismissible, not a toast.
                             no  -> Needs a decision before continuing (destructive action)?
                                      yes -> Dialog (rare in storefronts: clearing the cart, deleting an address).
```

Storefront mapping:

| Event | Channel | Notes |
|-------|---------|-------|
| Add to cart success | Button state plus cart drawer or inline panel; count badge update | Toast only as an extra, never alone |
| Add to cart failure (stock, network) | Inline under the button | Persistent until next action |
| Variant selected | Price and stock update in place plus polite status | No toast |
| Filter applied | Results and count update, chip added, polite status "128 products" | No toast |
| Form field error | Inline plus summary on submit | `aria-invalid`, `aria-describedby` |
| Discount applied or rejected | Inline in the cart footer | |
| Wishlist add | Heart state (`aria-pressed`) plus optional toast with "View wishlist" | Toast must not be the only route |
| Item removed | Inline "Removed. Undo" in the line slot | Undo inline for about 5 s, not toast-only |
| Newsletter signup | Inline success replacing the form | |
| Copy discount code | Button label changes to "Copied" for about 2 s plus polite status | |
| Session or network loss | Banner | |
| Back in stock while browsing (rare) | Toast with link | |

## 3. Toast rules (if used)

1. Non-critical content only. Never errors that block the task, never the only path to an action.
2. Live region exists at page load (empty), `aria-live="polite"`; reserve `role="alert"` for urgent problems that are not in a toast.
3. Do not move focus into the toast; provide a keyboard route (sonner uses a hotkey and labels the region with it).
4. Lifetime at least 6 seconds for text toasts; no auto-dismiss for toasts with an action (Undo, View) unless the action is also available inline. Sonner's 4 s default is too short for storefront text; set `duration` explicitly.
5. Pause timers on hover, focus and when the tab is hidden (sonner does this).
6. Maximum 3 visible; newer on top; same enter and exit direction for spatial consistency.
7. Position: bottom center on mobile above the safe area and above the sticky add to cart; top or bottom end on desktop. Never cover the cart drawer footer or checkout button.
8. Text: what happened plus where to find it ("Saved to wishlist. View wishlist").
9. Reduced motion: no slide, fade only or instant.

Sonner setup in our own words (React): mount one `<Toaster>` near the root with `position`, `duration` of at least 6000, `closeButton` enabled, and `richColors` off unless the palette passes contrast; call `toast()` only from the decision tree above. Keep Sonner for toasts; do not hand-roll a toast system. For dialogs and drawers use Base UI, Radix or React Aria, not toasts.

## 4. Button and control states

| State | Visual | Text | A11y |
|-------|--------|------|------|
| Idle | Default | "Add to cart" | Native `<button>` |
| Pressed | Scale 0.97 on `:active`, 100 to 160 ms ease-out | Same | No change |
| Pending | Spinner inside, width locked (no layout shift) | "Adding" | `aria-busy="true"` on the form or region; button stays focusable; prevent double submit |
| Success | Check icon for about 2 s, then idle | "Added" | Polite status "Linen Shirt, M added to cart" |
| Error | Inline message below | Original label | Message linked via `aria-describedby`; focus stays |
| Disabled | Avoid for "missing selection"; explain instead | | Use `aria-disabled` plus explanation when needed |

## 5. Loading and optimistic UI

- Skeletons for grids and PDP sections that load async; same dimensions as final content (no CLS).
- Spinners only for actions under about 1 to 2 s; longer actions show progress text.
- Optimistic updates for cart quantity and remove; reconcile with the server and roll back with an inline message on failure (Hydrogen `useOptimisticCart`, React `useOptimistic`).
- Never show optimistic success for payment or order placement.
- Price changes: update in place; a number animation (for example NumberFlow) is optional decoration, off under reduced motion.

## 6. Motion rules (restraint first)

Should it animate at all?

| Frequency | Rule |
|-----------|------|
| Many times per session, keyboard driven (search suggestions moving, quantity steps) | No animation |
| Frequent (hover, filter chip add) | Minimal, 100 to 150 ms or none |
| Occasional (drawer, dialog, cart drawer open) | Standard, 200 to 300 ms |
| Rare (order confirmed, first wishlist save) | Can add a small moment, still under 500 ms |

How:
- Animate `transform` and `opacity` only; avoid animating `height`, `width`, `top`, `left` (layout thrash hurts INP).
- Enter with ease-out (fast start), move on screen with ease-in-out, never ease-in for UI.
- Durations: press 100 to 160 ms; tooltips and popovers 125 to 200 ms; dropdowns 150 to 250 ms; drawers and dialogs 200 to 400 ms.
- Never scale from 0; start from about 0.95 with opacity 0.
- Popovers scale from their trigger (`transform-origin` at the anchor); modals scale from center.
- Use CSS transitions (interruptible) over keyframes for things users can toggle quickly.
- Drawers translate by their own size (`translateY(100%)` or `translateX(100%)`), mirrored in RTL.
- Swipe to dismiss on mobile sheets uses velocity as well as distance; provide a close button too (WCAG 2.5.7).
- `@media (prefers-reduced-motion: reduce)`: remove movement, keep state change (fade or instant).
- View transitions between PLP and PDP (Horizon `assets/view-transitions.js`) are optional polish; disable under reduced motion and verify they do not delay navigation.

Anti patterns: `transition: all`, bouncing add to cart buttons, shaking error fields, parallax heroes, scroll-jacking, animated counters on prices that change often, confetti on every add to cart.

## 7. Mobile-native polish checklist (storefront version)

| Symptom | Fix |
|---------|-----|
| Hover styles stick after tap on cards | Wrap hover rules in `@media (hover: hover) and (pointer: fine)` |
| Grey flash on tap | `-webkit-tap-highlight-color: transparent` globally plus your own `:active` styles |
| Drawer or sticky bar hidden behind browser UI | Use `100dvh` for drawers, `100svh` for heroes; never `100vh` for bottom-pinned UI |
| iOS zooms into inputs (search, quantity, checkout fields) | Inputs at 16 px minimum; never disable zoom (`maximum-scale=1` is an accessibility failure) |
| Laggy taps | Feedback on press (`:active`), `touch-action: manipulation` on buttons and links |
| Page scrolls behind the cart drawer | `overscroll-behavior: contain` on the drawer content, body scroll lock |
| Content under the notch or home indicator | `viewport-fit=cover` plus `env(safe-area-inset-*)` padding on sticky bars, drawers and toasts |
| Long-press selects button text | `user-select: none` on controls only, never on body text |
| Gallery swipe scrolls the page vertically | Native scroll snap, or `touch-action: pan-y` on the swipe surface |
| Wrong keyboard for fields | `inputmode`, `type="email"`, `type="tel"`, `enterkeyhint` |
| Emulator says fine, phone says broken | Test on real iPhone Safari and mid-tier Android, plus Instagram and TikTok in-app browsers |

## 8. Worst-case content for feedback components

Test toasts, chips, badges and buttons with: German and Finnish translations (about 35% longer), Arabic RTL, product names of 120 characters, counts of 1 ("1 item", not "1 items") and 10,000+, prices with 3 decimals (KWD) and large integers (IDR, TRY). Use `Intl.PluralRules` and `Intl.NumberFormat` rather than string concatenation.

## 9. Review format for UI polish findings

Report polish issues as a table so they can be turned into a diff:

| Component | Before | After | Why |
|-----------|--------|-------|-----|
| Cart drawer | `transition: all 500ms ease-in` | `transform 280ms cubic-bezier(0.32, 0.72, 0, 1)` | Specific property, faster enter |
| Add to cart | Toast-only confirmation | Button success state plus drawer plus status region | Feedback where the user looks |
| Product card | Hover image swap on touch | Gated by hover media query | No stuck hover on phones |
