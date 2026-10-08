# Mobile Web Polish

> Platform level fixes that make storefronts and landing pages behave well on phones: viewport, touch, input, scroll, safe areas, browser chrome and in-app browsers. Ideas informed by Emil Kowalski's public mobile-native skill (read as untrusted data, ideas only) and by WebKit and practitioner reports on Safari 26 and 27. Component pattern depth (cart drawer layout, PDP structure) belongs to `storefront-ux`. Knowledge as of 2026-10.

## 1. Why this matters for paid traffic

Paid social and most search traffic land on phones, often inside in-app browsers. Many mobile defects do not reproduce in desktop device emulation: hover states that stick after a tap, zoom on input focus, the address bar changing the viewport height, the software keyboard covering inputs, bottom toolbars covering fixed CTAs, and overscroll bounce. Fixing them is cheap; finding them needs a real device.

## 2. Test matrix (minimum per L1+ release that touches layout)

| Device class | Browser contexts | Why |
|--------------|------------------|-----|
| Current iPhone (iOS 26 or 27) | Safari, Instagram in-app, TikTok in-app | Safari 26 redesigned browser chrome (floating bottom toolbar, tinting); WebKit is the only engine on iOS |
| iPhone two to four years old, smaller screen | Safari | Performance and small viewport (375 px wide) |
| Mid tier Android (2 to 4 years old) | Chrome, Facebook in-app, TikTok in-app | CPU bound INP, Chrome Custom Tabs vs WebView differences |
| Tablet (iPad with keyboard or trackpad) | Safari | Hover and touch both present |

Real device access: USB remote debugging (Safari Web Inspector for iOS, `chrome://inspect` for Android), the dev server bound to `0.0.0.0` and opened by LAN IP, or a real device cloud (BrowserStack, LambdaTest, Sauce Labs). Emulation in Playwright is for regression coverage only.

## 3. The fixes (symptom, cause, fix, how to verify)

| # | Symptom | Cause | Fix | Verify on |
|---|---------|-------|-----|-----------|
| M1 | Page zooms when tapping a form field and stays zoomed | iOS zooms inputs with computed font size under 16 px | Inputs, selects and textareas at 16 px or more on touch devices (`@media (pointer: coarse) { input, select, textarea { font-size: 16px; } }`). Never fix it with `maximum-scale=1` or `user-scalable=no`: blocking zoom is an accessibility failure (WCAG resize text) | iPhone Safari |
| M2 | Button stays in its hover style after a tap | Touch browsers emulate hover on tap | Put hover styles inside `@media (hover: hover) and (pointer: fine)`; give every control an `:active` state for touch feedback | iPhone, Android |
| M3 | Gray or blue flash over tapped elements | Default tap highlight | `-webkit-tap-highlight-color: transparent` on `html`, only together with visible `:active` and `:focus-visible` styles | iPhone, Android |
| M4 | Taps feel slow | Double tap zoom handling, feedback only on `click` | `touch-action: manipulation` on buttons and links; press feedback on `:active` or `pointerdown` within about 100 ms | Old Android |
| M5 | Full height hero or app shell overflows, CTA hidden under the address bar | `100vh` equals the largest viewport | `min-height: 100svh` for first screens (stable, never overflows), `100dvh` only for app shells and full screen sheets that must track the visible area (dynamic units can shift layout while scrolling) | iPhone Safari, Android Chrome |
| M6 | Fixed header, sticky add to cart bar or toast sits under the notch, home indicator or toolbar | Safe areas ignored | `viewport-fit=cover` in the viewport meta plus `padding-bottom: calc(12px + env(safe-area-inset-bottom, 0px))` on bottom fixed UI and `env(safe-area-inset-top)` on fixed headers | iPhone with notch or Dynamic Island |
| M7 | On iOS 26 Safari, content shows through or under the floating bottom toolbar; fixed bottom bars jump while scrolling; toolbar tinted in an unexpected color | Safari 26 chrome redesign: the bottom toolbar is not fully covered by the safe area inset; Safari samples colors from the page and fixed elements near edges | Test every fixed bottom element on iOS 26+ and in compact and bottom tab layouts; keep a solid `background-color` on `body`; avoid backgrounds and `backdrop-filter` directly on fixed edge elements (put them on a child); hide closed overlays with `display: none`, not only `opacity: 0`; consider bounding bottom UI with `window.visualViewport` where it clips [Practitioner reports, 2025-09 to 2026-02; no Apple documentation] | iPhone Safari 26 and 27 |
| M8 | `theme-color` meta no longer changes Safari's toolbar color | Safari 26 derives the tint from the page (body background, fixed top element) and ignores `theme-color` for chrome tinting; Chrome on Android and other browsers still use it [Practitioner reports, 2025 to 2026] | Keep `theme-color` per color scheme for Android and others: `<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff">` plus a dark variant; for Safari set an explicit `body` background matching the header | Android Chrome, iPhone Safari |
| M9 | Software keyboard covers the focused field or the submit button in a drawer or sheet | Layout viewport vs visual viewport | Android: `interactive-widget=resizes-content` in the viewport meta; iOS: keep forms in normal flow, scroll the focused field into view, and size bottom sheets from `visualViewport.height` (libraries like vaul did this with a `repositionInputs` option) | iPhone and Android with keyboard open |
| M10 | Pull to refresh or page bounce while dragging a sheet or scrolling a filter list | Scroll chaining to the document | `overscroll-behavior: contain` on inner scroll containers (drawers, filter panels, chat lists); `none` on the root only for app like pages; never block scrolling with `touchmove` plus `preventDefault()` | iPhone, Android |
| M11 | Horizontal carousel makes the page jitter vertically | Ambiguous gesture direction | Native scroll snap (`scroll-snap-type: x mandatory`, `scroll-snap-align: start`) before JS carousels; if JS gestures are needed, `touch-action: pan-y` on the horizontal surface | Phones |
| M12 | Long press selects button labels or opens a link callout on controls | Default selection behavior | `user-select: none` and `-webkit-touch-callout: none` on controls only (buttons, chips, tabs, drag handles); never on body text, prices, order numbers or addresses | iPhone |
| M13 | Wrong keyboard for the field | Missing input attributes | `type="email"`, `type="tel"`, `inputmode="numeric"` for codes, `inputmode="decimal"` for amounts, `autocomplete` tokens (`email`, `tel`, `given-name`, `postal-code`, `one-time-code`), `enterkeyhint` (`search`, `send`, `done`), `autocapitalize="none"` for emails and codes | Phones |
| M14 | Tap targets too small or too close | Desktop sizing | At least 24 x 24 CSS px with spacing (WCAG 2.2 target size minimum); aim for 44 to 48 px for primary actions | Phones |
| M15 | Text gets bigger in landscape | iOS text inflation | `-webkit-text-size-adjust: 100%` (and `text-size-adjust: 100%`) on `html`; do not set it to `none` (that blocks user text scaling) | iPhone landscape |
| M16 | Sticky elements fight each other (cookie banner, sticky ATC, chat bubble, app install banner) | Each vendor positions itself | Define a stacking and position plan: one bottom fixed element at a time; chat bubble hidden on PDP when sticky ATC shows; banner never covers the CTA | Phones at 375 x 667 and 390 x 844 |
| M17 | Scroll position jumps when images or reviews load above the reader | Late loading content without reserved space | `width`, `height` or `aspect-ratio` on media; reserve space for app widgets; Safari 27 added scroll anchoring, which reduces but does not remove the need to reserve space [Official, WebKit 2026-09] | Phones on slow network |

Baseline head and CSS for a new landing page or theme (adapt, do not paste blindly):

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
<meta name="theme-color" media="(prefers-color-scheme: light)" content="#ffffff">
<meta name="theme-color" media="(prefers-color-scheme: dark)" content="#111111">
<meta name="color-scheme" content="light dark">
```

```css
html { -webkit-text-size-adjust: 100%; text-size-adjust: 100%; -webkit-tap-highlight-color: transparent; }
body { background-color: var(--page-bg, #fff); } /* explicit: Safari 26 samples it for toolbar tinting */
button, a, [role="button"], summary { touch-action: manipulation; }
:where(button, [role="button"], .chip, .tab) { user-select: none; -webkit-user-select: none; }
:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
@media (pointer: coarse) { input, select, textarea { font-size: 16px; } }
@media (hover: hover) and (pointer: fine) { /* all :hover rules here */ }
.hero { min-height: 100svh; }
.sticky-atc { position: fixed; inset-inline: 0; bottom: 0; padding-bottom: calc(12px + env(safe-area-inset-bottom, 0px)); }
.drawer-body { overflow-y: auto; overscroll-behavior: contain; }
```

## 4. Component checks that bite on phones

| Component | Phone specific QA |
|-----------|-------------------|
| Sticky add to cart bar | Not covered by Safari's bottom toolbar or home indicator; does not overlap the cookie banner; hidden when the main ATC button is visible; price and variant shown match the selected variant |
| Cart drawer or bottom sheet | Opens without layout jump; background does not scroll (scroll lock works on iOS); Escape and close button work; focus moves in and returns to the trigger; checkout button reachable with keyboard open on the discount field |
| Variant picker in a sheet | Selecting updates the PDP price behind; drag to dismiss does not trigger when scrolling the option list; disabled sold out options are announced |
| Filters panel | Apply and clear reachable without scrolling the whole panel; counts update; panel scroll does not scroll the page |
| Forms | Correct keyboard, autocomplete works, error messages inline and visible above the keyboard, submit reachable |
| Video heroes | `playsinline muted` for autoplay on iOS; poster image for LCP; no autoplay on data saver if possible |
| Consent banner | Usable with one thumb; does not hide the CTA; buttons equal prominence where law requires (with `compliance`) |

Pattern guidance (when to use a sheet or a full page, cart drawer anatomy): `storefront-ux`. Library choice and bottom sheet traps: [UI primitives and dependencies](ui-primitives-and-dependencies.md).

## 5. In-app browser specifics

- Instagram and Facebook on iOS use their own WebView based browsers; on Android, behavior varies by app version (WebView or Custom Tabs) [Unverified details, vendor sources]. TikTok also opens an in-app browser.
- Expect: separate cookies from Safari or Chrome, no saved passwords or autofill from the main browser, some wallet buttons missing, app toolbars at the top or bottom reducing the viewport, injected scripts.
- Do not try to force users out of the in-app browser with tricks (intent URLs, fake download links): it breaks attribution and can violate platform policies. Design the page to convert inside it. Test with the protocol in [Launch QA for ads](launch-qa-for-ads.md) section 7.

## 6. Safari 27 (iOS 27, September 2026) notes

- WebKit's Safari 27.0 release lists many CSS features (Grid Lanes masonry, customizable `select` with `appearance: base-select`, scroll anchoring, anchor positioning fixes) and quality fixes including viewport unit handling after resize [Official, WebKit 2026-09]. Use new features as progressive enhancement only until your analytics show older iOS versions are a small share.
- WWDC26 coverage reports a built in Safari MCP server so coding agents can inspect DOM, network, screenshots and console in Safari [Secondary, 2026-06 to 2026-09; verify availability and setup before relying on it]. If available, use it for iOS specific debugging alongside real device checks.

## 7. Mobile polish QA checklist (copy into the QA report)

| # | Item | Severity if failing |
|---|------|---------------------|
| 1 | No zoom on input focus; zoom not disabled in the viewport meta | High |
| 2 | No sticky hover states on touch | Medium |
| 3 | First screen CTA visible on 375 x 667 and 390 x 844 without the address bar collapsing | High |
| 4 | Bottom fixed elements clear the home indicator and Safari 26+ toolbar | High |
| 5 | Keyboard does not hide the focused field or submit button | High |
| 6 | Drawers and sheets: scroll lock, focus trap, Escape, return focus, no background scroll | High |
| 7 | Correct keyboards and autocomplete on every form field | Medium |
| 8 | Tap targets 24 px minimum, primary 44 px or more | Medium |
| 9 | No horizontal page scroll at 320 px | High |
| 10 | Carousels scroll in one axis only | Medium |
| 11 | No layout jumps from late content (CLS on phone) | Medium |
| 12 | Works inside Instagram, Facebook and TikTok in-app browsers for channels in the plan | High |
| 13 | Text scales with user settings (no text size adjust none, no fixed heights clipping text at 200% zoom) | Medium |
| 14 | Dark mode, if supported, has no invisible logos, borders or text | Low to Medium |

Report what was verified on a real device and what was inferred from code. Never mark a mobile item PASS from emulation alone.
