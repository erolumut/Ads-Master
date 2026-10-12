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

## 2b. Copy-in registries and galleries (rung 5)

The shadcn CLI is the delivery mechanism for most of these: CLI 3.0 (2025-08-27) added namespaced registries (`@ns/name`) with auth headers and an MCP server, CLI 4.0 (2026-03-06) added `--preset`, `--dry-run`, `--diff` and `--view`, Base UI became the default base in CLI 4.13.0 (2026-07-03) and React Aria a first class base on 2026-07-17 (`--base aria`) [Opened, shadcn changelog]. The official directory (`apps/v4/registry/directory.json`) listed 443 registries on 2026-10-12; there is no central registrar, so a listing is not a review [Opened].

A project that wants its own identity publishes its own namespaced registry (`@yourbrand`) built on Base UI or React Aria and skinned with its tokens. Everything below is then a reference or a one off copy into that registry.

| Source | Licence | Price | Forces | Verdict |
|---|---|---|---|---|
| shadcn/ui | MIT, keep the notice in substantial copies [Opened] | Free | Tailwind 4, React 19, the chosen base | Foundation (delivery and starting code) |
| Ark UI | MIT [Opened]; 5.39.3 (2026-10-05) | Free | Zag state machines | Alternative foundation |
| Untitled UI React | MIT; Pro under a separate licence [Opened] | Pro reported $349 solo, $2,499 business [Reported] | React Aria, Tailwind 4, Motion | Well maintained, but a recognisable look of its own; not in the shadcn directory |
| Tailwind Plus | Commercial: unlimited end products, no redistribution, no publishing UI libraries or starter kits [Opened, licence] | Reported $299 personal, $979 team [Reported] | Tailwind, Headless UI | Internal tools and layout reference |
| coss (formerly Origin UI) | AGPLv3 by default; only `apps/ui` and `apps/origin` are MIT [Opened, README] | Free | Base UI, Tailwind 4 | Reference; copy only from the MIT folders after reading its licensing file |
| Kibo UI | MIT text, moved to `shadcnblocks/kibo` [Opened] | Free | Headless libs | Internal tools |
| ReUI (data grid, kanban) | not checked | not checked | | Worth a look for internal tools [Reported] |
| tweakcn | Apache-2.0 [Opened] | Free, Pro reported [Unverified] | shadcn token model | Theme exploration only |
| Magic UI | MIT [Opened]; Pro terms forbid redistribution and competing templates, with liquidated damages [Reported] | Free, Pro paid | Motion, Tailwind | Reference for marketing effects |
| Aceternity UI | Pro: no resale or redistribution [Reported]; free tier terms unclear [Unverified] | Pro reported $199 lifetime [Reported] | Motion, Tailwind | Reference only |
| Animate UI | LICENSE.md is MIT plus Commons Clause while the README badge says MIT [Opened] | Free | Motion, Radix, Base UI beta | Reference only; licence conflict |
| React Bits | MIT plus Commons Clause: no reselling or porting the components [Opened] | Free, Pro reported $99 to $299 [Reported] | GSAP, three, ogl, Motion | Reference only; heavy dependencies |
| motion-primitives | MIT per README, no LICENSE file found [Opened] | Free | Motion 11 | Reference for motion vocabulary |
| Kokonut UI, Cult UI | MIT [Opened]; Pro tiers paid | Cult Pro reported $199 lifetime [Reported] | Motion, Radix | Reference only |
| 21st.dev | Community items often show "License: unknown" [Reported]; CLI MIT | Free with limits, paid tiers | API key for installs | Avoid as a code source; unknown means no licence |

### The sites from the viral list (2026-10)

All six are young (2026), MIT for their free tier with a paid Pro tier, and have no independent reviews yet [Opened, repos; Reported, sites].

| Site | Licence | Price | Forces | Verdict |
|---|---|---|---|---|
| affectui.com | MIT, 2026 [Opened] | 39 free items, Pro price not found | Nothing: one `.tsx` per item with inline styles | Reference; inline styles must be rewritten to tokens |
| kobra.systems | Paid, terms not read [Unverified] | Reported $199 solo one time, $150 per seat, $19 per component, about 10 free [Reported] | Base UI [Reported] | Reference; read the terms before any copy |
| uiarc.dev | MIT, 2026 [Opened] | About 100 free, Pro paid [Reported] | CSS modules, Motion | Reference |
| beui.dev | MIT, 2026 [Opened] | Free | Motion, Tailwind 4 | Reference; not for CSS only motion projects |
| boardui.com | MIT free tier, Pro separate licence [Opened] | Pro one off, price not found | React Aria, Tailwind 4, Motion, Recharts | Internal tools; generated repo that takes no contributions |
| evilcharts.com | MIT, 2026 [Opened] | Free | Recharts 3 or ECharts 6, Base UI, Motion | Internal dashboards; see [Charts](charts.md) |
| transitions.dev | Recipes free for commercial use, no redistribution as a kit; tooling MIT [Opened] | Free, Pro tier | None (CSS) | Best fit for CSS first projects; see [Motion without libraries](motion-without-libraries.md) |

Licence traps in this space: Commons Clause (fine inside your product, bans reselling or porting), AGPL outside marked folders, paid kits that forbid templates or publishing derived libraries, and "unknown" on gallery mirrors.

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
