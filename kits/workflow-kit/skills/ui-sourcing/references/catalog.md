# Catalog: sources by need (October 2026)

Dated, labelled picks for each rung of the ladder. Research date 2026-10-12. Labels: [Opened] read at the source (npm registry JSON, GitHub file, release notes), [Reported] search results only, [Unverified] one weak source. Versions and dates come from the npm registry unless noted. Re-check any row older than six months before relying on it, and always run the [Vetting checklist](vetting-checklist.md).

## 1. Headless primitives (rung 3)

| Source | Licence | State | Use |
|---|---|---|---|
| Base UI (`@base-ui/react`) | MIT | 1.0.0 on 2025-12-11, 1.9.0 on 2026-10-09 with Drawer swipe, velocity and iOS keyboard fixes [Opened]; Dialog, Drawer (snap points, swipe direction, virtual keyboard handling), Toast, Menu, Select, Combobox, Autocomplete, OTP field, Toggle Group, Tabs, Number Field | Default for new React work. Read the changelog before upgrading: breaking minors happened in 2026 |
| Radix Primitives | MIT | Active, not deprecated; shadcn reportedly defaulted new projects to Base UI on 2026-07-03 [Reported] | Keep existing Radix code; start new code on Base UI |
| React Aria Components | Apache-2.0 | Active (1.22.0, 2026-10) [Opened, Ads Master storefront research] | Deepest accessibility and internationalization; good for complex inputs and date handling |
| Platform: `<dialog>`, Popover API, `<details>`, anchor positioning | n/a | All engines; see [Motion without libraries](motion-without-libraries.md) for animation status | First choice before any library for simple overlays |
| Customizable `<select>` (`appearance: base-select`) | n/a | Chrome 135+, announced for Safari 27 at WWDC26 [Opened], Firefox not by default [Reported] | Progressive enhancement over the native select |
| `field-sizing: content` | n/a | Baseline newly available since June 2026 [Reported] | Auto growing textareas without JavaScript |
| `interestfor` | n/a | Chromium 142 only [Reported] | Enhancement only |

## 2. Focused packages (rung 4), mostly mobile first

| Need | Pick | Licence and state | Notes |
|---|---|---|---|
| Bottom sheet or drawer | Base UI Drawer | See above | vaul is unmaintained (README notice; last publish 2024-12-14) [Opened]: no new work on it, replace when touched. Silk (`@silk-hq/components` 0.10.1) has the most native feel but needs a paid licence for commercial use, price not found [Opened, README]. react-modal-sheet 5.6.0 (MIT, needs `motion`) ships no built in accessibility [Opened, README] |
| Toasts | Sonner 2.0.8 (2026-08-09) | MIT, slow but maintained [Opened] | Base UI Toast is the alternative when you already use Base UI. Errors the user must act on are inline, never a toast |
| One time code input | input-otp 1.5.0 (2026-08-18) | MIT, zero deps [Opened] | Or Base UI OTP field |
| Animated numbers | NumberFlow (`@number-flow/react` 0.6.2, 2026-07-18) | MIT, pre 1.0 [Opened] | Pin the version |
| Date picker | react-day-picker 10.0.2 (2026-09-30) | MIT; v10 removed deprecated v9 props [Opened] | Base UI has no calendar; check touch target sizes |
| Command palette | Base UI Combobox or Autocomplete | | cmdk 1.1.1 is stale (published 2025-03-14) and pulls in four Radix packages [Opened] |
| Carousel | Embla 8.6.0 | MIT; 9.0.0 still a release candidate (rc04, 2026-10-08) [Opened] | Pin 9 only after it goes stable |
| Sortable lists | `@dnd-kit/core` and `@dnd-kit/sortable` | MIT | `@dnd-kit/react` is still 0.x (0.5.0, 2026-06-11) [Opened]: pilot only |
| Long lists | react-virtuoso 4.18.16 (2026-09-29) | MIT, active [Opened] | |
| Tables and grids | TanStack Table | MIT | Headless; style with your tokens |
| Segmented control | Base UI Toggle Group or Tabs | | Compose; no library needed |
| Pull to refresh, swipe actions | Build in house | | No well maintained headless library found [Reported]; Pointer Events plus `overscroll-behavior` |
| Charts | See [Charts](charts.md) | | |
| Motion | See [Motion without libraries](motion-without-libraries.md) | | |

## 3. Mobile web and PWA facts that shape component choices

| Topic | State | Rule |
|---|---|---|
| Install on iOS 26 | Every site added to the Home Screen opens as a web app by default [Reported]; no `beforeinstallprompt` on iOS | Write your own "Share, then Add to Home Screen" hint |
| Web Push on iOS | Only for installed Home Screen apps, requested from a user gesture, since iOS 16.4 [Reported] | Ask after a meaningful action, never on first load |
| Safe areas | `viewport-fit=cover` plus `env(safe-area-inset-*)`; WebKit bugs 301108 and 306465 report iOS 26 problems [Reported] | Test on a real device in both orientations |
| Virtual keyboard | Virtual Keyboard API is Chromium only; iOS needs `visualViewport` [Reported] | Use a sheet that handles both (Base UI Drawer does) |
| Craft basics | `dvh` units, inputs at 16px or larger, never `user-scalable=no`, `touch-action: manipulation`, hover styles under `(hover: hover) and (pointer: fine)`, `overscroll-behavior`, `theme-color` per colour scheme, test the installed app separately [Opened, emilkowalski/skills mobile-native, MIT] | Treat as a checklist on every mobile surface |

## 4. Icons and fonts

| Source | Licence | Notes |
|---|---|---|
| Lucide | ISC; icons derived from Feather keep an MIT notice [Opened, LICENSE] | Keep the notice; one set per project |
| Heroicons | MIT [Opened] | |
| Phosphor | MIT [Opened] | Many weights; pick one weight per surface |
| Tabler Icons | MIT [Opened] | |
| Font Awesome Free | Icons CC BY 4.0, fonts OFL 1.1, code MIT [Reported] | Attribution required; brand icons are trademarks |
| Google Fonts | Mostly OFL | Self host (for example `next/font`); see the vetting checklist on EU consent |

## 5. Agent skills worth installing for taste

| Skill | What | Licence |
|---|---|---|
| emilkowalski/skills | Animation judgement (emil-design-eng, animate, review-animations, improve-animations), mobile-native, break-ui, pick-ui-library [Opened] | MIT |
| transitions.dev skill | CSS transition recipes and a tuning tool [Opened] | Recipes free for commercial use, no redistribution as a kit; tooling MIT |

Read a skill like any registry item before installing it: it becomes instructions for your agent.
