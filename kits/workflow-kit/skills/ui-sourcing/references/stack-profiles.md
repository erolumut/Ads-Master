# Stack profiles: what may come from outside

Pick one profile per project (or per app in a monorepo) and write it into the Profile of `docs/UI-SOURCES.md`. The profile decides which rungs of the sourcing ladder are open. A project's own rules (direction doc, design language, motion rules) always win over this table.

## The sourcing ladder

Climb only as far as the need forces you:

1. **Reuse** what the project already has (its own component, token or pattern).
2. **Platform**: HTML and CSS features (`<dialog>`, Popover API, `<details>`, View Transitions, `@starting-style`, anchor positioning, `linear()` easing, `field-sizing`).
3. **Headless primitives**: unstyled, accessible behaviour (Base UI, React Aria Components, Radix) under your own styling.
4. **Focused package**: one small library for one hard job (toasts, OTP input, number animation, drag and drop, virtualization, date picker, charts).
5. **Copied component** from a registry or gallery, re-skinned with your tokens, with an origin comment and a ledger row.
6. **Paid kit or page builder**: only with terms read, a decision record, and a before and after measurement.

A viral list of "best UI components" is a list of rung 5 and 6 sources. Read them for ideas (rung 0: reference), then build on the lowest rung that works.

## Profiles

| Profile | Typical project | Open rungs | Defaults | Never |
|---------|-----------------|------------|----------|-------|
| **A. Signature product** (looks like nobody else) | Consumer app or game platform with its own design language and craft gate | 1 to 4; 5 as reference only | Own components on platform features or headless primitives; motion from the project's own tokens, CSS first; one icon set | Styled kits on signature surfaces (board, landing, lobby, reveal); a second motion or icon system; demo colours, radii or easing surviving a copy |
| **B. Mobile first PWA** (small team, in house UI) | Family, health, scheduling or social apps that live on the home screen | 1 to 4; 5 for non signature pieces after re-skin | Platform dialog and popover, own bottom sheet on a maintained primitive, one toast solution, safe areas and keyboard handling, budgeted first load JS | Unmaintained drawers; heavy animation libraries for simple fades; haptics or sound as the only feedback |
| **C. Internal tool or dashboard** (speed over identity) | Back office, admin, finance or operations consoles | 1 to 5; 6 after terms are read | shadcn style components on Base UI or Radix with the project's tokens; one chart library; TanStack Table for grids; calm defaults | Several chart libraries; copying unknown licence components; dashboards of dashboards on the home screen |
| **D. No framework, no build** | Plain ES modules apps, local tools, confidential data apps | 1 and 2; 4 only as a vendored, pinned file with a ledger row and if the project allows any library | Platform features, hand drawn SVG or Canvas for charts, CSS motion | Anything that needs a bundler, a CDN at runtime, or network calls the project forbids |
| **E. Static marketing or content site** | Brochure, booking enquiry, editorial, multilingual SSG sites | 1, 2, 4 (sparingly) | CSS motion and scroll driven effects with fallbacks, optimized images, self hosted fonts, zero client JS where possible | Animation libraries for reveal effects; third party font CDNs without consent in the EU |
| **F. Shopify theme** | Liquid Online Store 2.0 store (Horizon, Dawn or a premium theme) | Native blocks and alternate templates first, then reviewed theme blocks, section packs, theme app extensions; page builders last | Theme's own web components for drawers and toasts; apps as theme app extensions | React inside a Liquid theme; apps that edit `theme.liquid`; script tags |
| **G. Ad landing page** (any stack) | Campaign pages for paid traffic | The site's own components; per stack rules above | One page or template per message angle, the ad's promise in the headline, one call to action, proof above the fold, fast on a mid range phone | Page builder bloat; components that delay the main image; claims that skipped review |

## Choosing between neighbours

- A project can hold two profiles: an admin area is C inside an A product. Write both into the Profile and say which paths each covers.
- When unsure between A and B, ask whether a person would recognize the product from one screenshot without the logo. If yes, it is A.
- Moving a project up the ladder (for example allowing paid kits) is a decision, recorded in the project's decision log.
