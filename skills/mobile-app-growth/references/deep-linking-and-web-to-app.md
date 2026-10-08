# Deep Linking and Web to App Funnels

> Knowledge as of 2026-10. Key changes: Firebase Dynamic Links shut down 2025-08-25; US App Store allows buttons and links to web purchases without an entitlement since 2025-05-01 with zero Apple commission while the fee is litigated (Apple proposed 15% / 10% / 5% on 2026-08-13; Supreme Court reviewing the contempt standard); Google Play US alternative billing and external content links programs live since 2025-12-09 with fees and reporting from 2026-10-01 per Google Help [Contested]; Google billing choice in the UK and EEA from 2026-06-30; Apple EU terms with link out at 15% from 2026-10-01; UK CMA steering rules proposed 2026-06-30; Google Play Instant ended 2025-12. Verify the regional matrix before any launch.

## 1. Deep link types

| Type | What it does | Platform mechanism | When to use |
|------|-------------|--------------------|-------------|
| Universal links (iOS) | HTTPS link opens the app if installed, the web page if not | apple-app-site-association (AASA) file + Associated Domains entitlement (`applinks:example.com`) | Default for every iOS link in ads, email, web |
| App Links (Android) | HTTPS link opens the app if installed and verified | `/.well-known/assetlinks.json` + intent filter with `android:autoVerify="true"` | Default for Android |
| URI schemes (`myapp://`) | Opens the app if installed, fails otherwise | Custom scheme | Internal routing only; never as the only link in ads |
| Deferred deep links | Routes a new user to specific content after install | Play Install Referrer (Android, deterministic); MMP or link provider logic on iOS; account login or redemption link | Ads to specific content, referrals, web to app |
| Custom product page deep links (iOS 18+) | A CPP can open matching in-app content for users who already have the app | App Store Connect CPP setting | Apple Ads and campaigns to existing users |
| Smart App Banner | Safari banner that opens or installs the app, passing `app-argument` | `<meta name="apple-itunes-app" content="app-id=123, app-argument=https://...">` | Website traffic on iOS |
| App Clips (iOS) | Lightweight part of the app without install | App Clip experiences | Physical world, quick tasks |

Google Play Instant apps ended in 2025-12; Google recommends deep links to the full app instead [Official, 2025-06].

## 2. Setup checklists

### 2.1 Universal links

- [ ] AASA served at `https://<domain>/.well-known/apple-app-site-association`, no file extension, `application/json`, HTTPS, no redirects.
- [ ] `applinks` details list the app ID (Team ID + bundle ID) and `components` with the paths that should open the app; exclude paths that must stay on the web (checkout, help).
- [ ] Associated Domains entitlement includes every domain and subdomain used in links (`applinks:example.com`, `applinks:go.example.com`).
- [ ] Apple fetches AASA through its CDN; changes propagate with a delay. Use the developer mode suffix on test devices while iterating [Official].
- [ ] The app handles the incoming URL (`NSUserActivity` or SwiftUI `onOpenURL`) and routes to content, with a fallback screen.
- Known limits: typed URLs in Safari do not open the app; links within the same domain in Safari stay on the web; many in-app browsers (Instagram, Facebook, TikTok) open the web page instead of the app [Practitioner consensus]. Plan an "Open in app" button on the landing page.

### 2.2 App Links

- [ ] `assetlinks.json` at `https://<domain>/.well-known/assetlinks.json` with the package name and SHA-256 certificate fingerprints.
- [ ] Include the Play App Signing key fingerprint from Play Console (App integrity), not only the upload key. This is the most common App Links failure [Practitioner consensus].
- [ ] Intent filters with `android:autoVerify="true"` for each host; on Android 12+ unverified links open in the browser by default [Official].
- [ ] Check status in Play Console > Deep links and with `adb shell pm get-app-links <package>`.

### 2.3 Deferred deep links

- Android: pass parameters through the Play Install Referrer (deterministic) via the MMP link.
- iOS: no deterministic path without ATT. Options in order of reliability: (1) the user logs in or redeems a link after install (web to app with account), (2) MMP link provider deferred deep linking (methods vary; ask which signals are used and avoid fingerprinting of ATT denied users [Contested]), (3) clipboard based approaches trigger a paste permission prompt and hurt conversion, avoid [Practitioner consensus].
- Pass only routing data (content ID, campaign, promo code), never personal data.

### 2.4 Replacing Firebase Dynamic Links

Firebase Dynamic Links stopped working on 2025-08-25 for page.link and custom domains; goo.gl links return errors [Official]. If any legacy link remains in emails, QR codes, printed material, app code or partner sites, it is broken now.

1. Inventory: search the codebase for `page.link`, `FirebaseDynamicLinks`, `goo.gl`; export old links if still available.
2. Choose the replacement: platform native universal links and App Links on your own domain (cheapest), an MMP link product (AppsFlyer OneLink, Adjust links, Branch, Singular Links, Kochava, Airbridge) when attribution and deferred routing are needed, or a custom redirect service.
3. Re-issue QR codes and printed links on your own domain so the next vendor change does not break them.
4. Ship an app update with the new link handling; test every path (section 3).

## 3. Deep link QA matrix

Test each link type on real devices (iOS current and previous major version, Android current and an older device), app installed and not installed:

| Source | iOS installed | iOS not installed | Android installed | Android not installed |
|--------|---------------|-------------------|-------------------|-----------------------|
| Safari / Chrome | Opens content | Store, then content after install | Opens content | Store, then content |
| Gmail app | | | | |
| Messages / WhatsApp | | | | |
| Instagram and Facebook in-app browser | | | | |
| TikTok in-app browser | | | | |
| QR via camera | | | | |
| Push notification | | n/a | | n/a |
| Email (lifecycle-crm templates) | | | | |

Record pass or fail with app version and date in the journal. Rerun after every app release that touches routing and after any domain or CDN change.

## 4. Web to app: the regional rules (as of 2026-10)

| Market | Apple | Google Play |
|--------|-------|-------------|
| United States | Buttons, links and calls to action to web purchases allowed on the US storefront without an entitlement (Guidelines 3.1.1, 3.1.1(a), 3.1.3 updated 2025-05-01); Apple may show only a neutral message when users leave; in-app alternative payment processing still not allowed; zero commission today; Apple proposed 15% standard, 10% partner programs and renewals, 5% Small Business (2026-08-13); district court sets the fee, Supreme Court reviewing contempt (No. 25-1311, Apple brief 2026-09-14, Epic brief due 2026-11-13) [Official court record via coverage] [Contested outcome] | Alternative billing and external content links programs live since 2025-12-09 under the court order; Google Help says enrolled developers report transactions and pay service fees from 2026-10-01 and download reporting fees from 2026-12-01; from 2026-06-30 the service fee is 10% on the first $1M and on all auto-renewing subscriptions, 20% or 25% otherwise, with the 5% billing fee only on Play Billing [Official] [Contested enforcement] |
| EU (DMA) | From 2026-10-01: link out to web checkout 15% (10% programs); alternative in-app payments 20% (10%); IAP 26% (15% programs and subscriptions after year one); 5% Core Technology Commission for apps distributed outside the App Store; alternative marketplaces with looser eligibility [Official, 2026-08 via coverage, verify Attachment 14] | Billing choice in the EEA from 2026-06-30: alternative billing or links to your website alongside Play Billing, own choice screen per UX guidelines [Official, 2026-06] |
| United Kingdom | Steering currently banned by Apple; CMA proposed steering conduct requirements on 2026-06-30 (consultation closed 2026-07-28, decision expected late 2026) [Official, 2026-06] | Google changed UK Play terms in 2026-06 to allow redirects; billing choice in the UK from 2026-06-30 [Official, 2026-06] |
| Japan | Alternative marketplaces and payments under MSCA from iOS 26.2 (2025-12) [Official] | Fee split from 2026-12-31 [Official schedule via coverage] |
| South Korea | Alternative payment options under local law with reduced commission [Official, long standing]; trial and offer consent rules from 2025-02 [Official] | Fee split from 2026-12-31 [Official schedule via coverage] |
| Brazil | Alternative marketplaces and out of IAP payments from iOS 26.5 (2026-06), Core Technology Commission applies [Official] | Check local program [Unverified] |
| China | IAP commission 25% / 12% from 2026-03-15 [Official] | Google Play not available |
| Türkiye | No steering change; competition investigations into Apple (opened 2024-05-21) and Google Play billing (opened 2025-08-07) had no final decisions found as of 2026-10 [Official announcements]; Apple price equalization 2025-11-17 [Official] | Same investigation status |
| Rest of world | Reader app external link entitlement for qualifying reader apps; otherwise IAP [Official] | Rest of world fee changes phase in to 2027-09 [Official schedule via coverage] |

Rule: every web to app plan states the market, the route, the fee assumption with its evidence label and a re-check date. Hand claims and pricing disclosures to compliance.

## 5. Funnel architectures

### 5.1 Web first (paid social to web paywall)

1. Ad on Meta, TikTok or Google sends users to a mobile web landing or quiz.
2. Web paywall with plans and trial terms.
3. Checkout (Stripe, Paddle, RevenueCat Web Billing, Superwall or Adapty web paywalls, FunnelFox), Apple Pay and Google Pay on the web.
4. Account creation (email or Sign in with Apple on the web).
5. Success page: App Store or Play link (with App Store `ct` campaign token or MMP link) plus a redemption link or login instructions.
6. App install, login or redemption link opens the app and grants the entitlement (RevenueCat Web Billing sends a unique redemption link that deep links into the app; purchase works without login) [Official vendor docs].
7. Onboarding continues from where the web funnel stopped.

Measurement: Pixel plus Conversions API with event_id deduplication for StartTrial and Purchase (hand to measurement), Google Web to App Connect for Google traffic, MMP web to app attribution, and backend truth. No SKAN thresholds apply to web events.

### 5.2 App first with link out (US storefront)

1. Paywall shows IAP and a "Pay on web" or "Save X% on web" option, or only the web option where IAP is not offered (common for reader and multi platform apps; Spotify and Kindle added purchase links and buttons in 2025-05 [Official app updates via coverage]).
2. Tap opens the system browser; Apple may show a neutral message.
3. Prefilled checkout (signed token in the URL), Apple Pay.
4. Return to the app through a universal link; entitlement refresh.

Evidence: RevenueCat's controlled test on one app (Dipsea, 2025) found trial start 27.0% in-app vs 18.1% on web, trial to paid 25.0% vs 26.3%, and $0.93 web take home per $1.00 IAP [Study, 2025-05]. FunnelFox reports web LTV ahead of in-app in its cohorts; Adapty's 2026 benchmark (via Airbridge) found web LTV about $4 lower on average after fee savings [Contested]. Test per app; judge on net revenue per paywall view, not conversion rate.

### 5.3 Decision table

| Situation | Recommended route |
|-----------|-------------------|
| Starter, under $10k per month revenue, Small Business Program at 15% | Stay on IAP; test link out only on annual plans |
| Paid social is the main channel and iOS signal is weak | Web first funnel |
| US heavy, annual plans, strong brand | Link out test vs IAP on the paywall (A/B), then decide |
| EU heavy | Model 26% IAP vs 15% link out vs alternative payments 20% plus processor; often IAP still wins on conversion |
| Games with consumable IAP | Web shop for top spenders where allowed (US), keep IAP in game |
| Kids or Families category | Avoid link outs; policy and parental control risk |

## 6. Web funnel quality: the mobile web layer

Most web to app traffic arrives on phones inside in-app browsers. Apply these platform level fixes (adapted from design engineering practice; hand implementation to site-engineer and cro):

- Inputs at 16px or larger so iOS Safari does not zoom on focus; never disable zoom with `user-scalable=no` or `maximum-scale=1`.
- Correct keyboards: `type="email"`, `autocomplete="email"`, `inputmode="numeric"` for codes, `enterkeyhint` labels.
- Viewport units: `100svh` for the first screen (no overflow under the URL bar), `100dvh` for app style shells; sticky CTA bars padded with `env(safe-area-inset-bottom)` and `viewport-fit=cover`.
- Taps respond on press (`:active` styles, `touch-action: manipulation`); hover styles only inside `@media (hover: hover) and (pointer: fine)`; remove the tap highlight flash.
- `theme-color` per color scheme so the browser chrome matches the page.
- `overscroll-behavior` on multi step quizzes so pull to refresh does not reset progress.
- Test on real hardware and inside Instagram, Facebook and TikTok in-app browsers; emulation misses keyboard, safe area and in-app browser behavior.
- Speed: LCP under 2.5 seconds on a mid range Android over 4G; every second matters more than design polish on paid traffic.

## 7. Compliance checkpoints (hand to compliance)

- Auto renewal disclosures: price, period, trial end date, how to cancel, before payment; easy online cancellation. Several US states require it; the FTC click to cancel rule was vacated by a federal appeals court in 2025 [Practitioner consensus, verify current status with compliance].
- EU and UK consumer law: withdrawal rights for digital content and the waiver flow; VAT handling (a merchant of record handles it for you).
- Store rules: no misleading price comparisons between web and IAP; Apple rejected or removed apps that processed digital purchases in-app outside IAP (one vendor reports an app pulled in 2026-04) [Unverified case].
- Refunds and chargebacks are yours on web; budget 1% to 3% and monitor dispute rates with the processor [Practitioner consensus].
- Sign in with Apple: if the app offers third party login, Guideline 4.8 requires an equivalent privacy focused option [Official].
