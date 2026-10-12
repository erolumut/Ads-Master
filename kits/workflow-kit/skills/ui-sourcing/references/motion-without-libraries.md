# Motion without a JavaScript library

Most interface motion now ships in CSS in every major engine. Reach for a library only for what CSS cannot do. Research date 2026-10-12; labels: [Opened] read at the source, [Reported] search results only, [Unverified] one weak source. Browser support moves monthly: check caniuse before relying on a row.

## 1. Platform status

| Feature | What it gives | Support | Use it as |
|---------|---------------|---------|-----------|
| Same document View Transitions (`document.startViewTransition`, `view-transition-name`) | Animated state changes and shared element moves | Chrome and Edge 111, Safari 18, Firefox 144; Baseline since 2025-10 [Reported, web.dev] | Default for swaps that would otherwise cut |
| Cross document View Transitions (`@view-transition { navigation: auto }`) | Page to page transitions in multi page sites | Chromium and Safari 18.2; Firefox status conflicting in 2026 [Reported] | Progressive enhancement only |
| React `<ViewTransition>` | View Transitions from React state | Reported stable in React 19.3 (2026-09-09); Next.js docs conflict on whether a flag is still needed [Reported] | Read the installed framework docs (`node_modules/next/dist/docs`) before use |
| `@starting-style` and `transition-behavior: allow-discrete` | Enter and exit animations for elements that toggle `display`, popovers and dialogs | Chrome 117, Firefox 129, Safari 17.4 and 17.5; Baseline since 2024-08 [Reported, web.dev] | Default for overlays |
| `linear()` easing | Springs, bounce and elastic curves as pure CSS | Chrome 113, Firefox 112, Safari 17.2 [Reported] | Store generated curves as tokens (`--ease-spring`) |
| Scroll driven animations (`animation-timeline: scroll()`, `view()`) | Scroll progress and reveal without JavaScript | Chrome 115, Safari 26.0 [Opened, Safari 26 release notes]; Firefox behind a flag in 2026 [Reported] | Inside `@supports (animation-timeline: scroll())` with a static fallback |
| Anchor positioning | Tooltips and menus placed next to their trigger without JavaScript | Chrome 125, Safari 26.0 [Opened, Safari 26 release notes], Firefox 147 [Reported] | Default for new tooltips and menus; test edge cases |
| `interpolate-size` and `calc-size()` | Animate to `height: auto` | Chromium only in 2026 [Reported, caniuse] | Enhancement; use `grid-template-rows: 0fr` to `1fr` as the cross browser way |
| Popover API and `<dialog>` | Light dismiss, top layer, focus handling | All engines; the `overlay` property for smooth exits is Chromium first [Unverified] | Default overlay base; exits may snap where `overlay` is missing |

## 2. Recipes worth copying

1. **Overlay enter and exit:** `transition: opacity, scale, display allow-discrete, overlay allow-discrete;` with the closed state as the start in `@starting-style`; style `::backdrop` separately.
2. **Spring feel without a library:** generate a `linear()` curve (linear-easing-generator by Jake Archibald and Adam Argyle, Apache-2.0 [Opened]) and keep it as a token with a `cubic-bezier` fallback.
3. **No cuts:** wrap a state change in `document.startViewTransition` behind an `if` guard; name the shared element with `view-transition-name`.
4. **Accordion height:** animate `grid-template-rows` from `0fr` to `1fr`.
5. **Scroll reveal and progress:** `animation-timeline: view()` inside `@supports`, with the no motion state as the default.
6. **Reduced motion tier:** keep opacity and colour changes, drop movement and scale; use `0.01ms` instead of `0s` so `transitionend` handlers still fire; anything moving longer than 5 seconds gets a pause control.
7. **Anchored menus:** `position-anchor` plus a popover; no JavaScript positioning code.

## 3. Sources of good motion (taste and recipes)

| Source | What | Licence and price | Verdict |
|--------|------|-------------------|---------|
| transitions.dev (Jakub Antalik) | Copy ready CSS transitions with a reduced motion guard, a CLI (`npx transitions-dev add <name>`), an agent skill (`npx skills add Jakubantalik/transitions.dev`) and a tuning tool | Recipes usable in unlimited personal and commercial projects, no redistribution as a competing kit; CLI and tooling MIT [Opened, GitHub README]. A Pro tier exists; price not found | Best free CSS motion reference; adapt timings to your own tokens |
| emilkowalski/skills | Agent skills for animation judgement: emil-design-eng, animate, review-animations, improve-animations, animation-vocabulary, mobile-native, pick-ui-library and more | MIT [Opened, GitHub] | Strongest agent ready motion review; note its library picks lean on Motion, which a CSS only project skips |
| animations.dev (Emil Kowalski) | Paid course on interface animation | Paid, windowed enrolment; price not found [Reported] | Optional, for the person who owns motion |
| Open Props | CSS custom property tokens including easings | Licence not verified here [Unverified] | Check open-props.style before relying on it |

## 4. When a library is genuinely worth it

Motion (formerly Framer Motion) or a similar library earns its place for: layout animations across arbitrary DOM changes (shared layout), drag and gesture physics with velocity hand off, interruptible springs that keep velocity, and long orchestrated sequences. Motion's own docs state a mini `animate()` of about 2.5 kB and a hybrid of about 17 kB [Reported]; measure on your route. State changes, enter and exit, scroll linked effects and page transitions do not need it. A project whose rules say "CSS and Web Animations API only" records any exception as a decision first.

## 5. Haptics and sound on mobile web

| Topic | State | Rule |
|-------|-------|------|
| Vibration | Android Chrome supports `navigator.vibrate`; Safari does not | Never the only feedback |
| iOS haptic trick | A hidden `<input type="checkbox" switch>` with a label clicked from script fires the Taptic Engine on some iOS versions; one tester page and one library README report it stopped working in iOS 26.5 [Reported, unconfirmed by Apple] | Best effort only; test on a real device on the current iOS |
| Web Audio on iOS | Muted by the silent switch while `<audio>` plays; the audio context must be resumed from a `click` or `touchend`, not `touchstart` [Reported, WebKit bug 237322] | Resume from a click handler; offer an in app mute; never rely on sound alone |
