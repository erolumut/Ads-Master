# Web Game Monetization

> Knowledge as of 2026-10 (research pass 2026-10-12). Apple's App Review Guidelines were read at the source ([Official, 2026-10]); portal terms, web ad programs and platform embeds came from search summaries and vendor pages ([Reported, 2026-10] or [Unverified]). Portal revenue splits and exclusivity terms conflict between sources and change by deal: read the live contract before relying on any of them. Signing a portal deal, publishing a game to a portal and turning on payments are G3 decisions for the human; `growth-orchestrator` owns the publishing deal question (`game-studio-lifecycle`).

## 1. Where a web game can earn

| Route | Fits | Earns through | Main constraint |
|-------|------|---------------|-----------------|
| Own URL and PWA | Daily games, group games, anything with streaks, accounts and a group graph | Stripe or a merchant of record (passes, subscriptions, group rounds, cosmetics); web ads | Traffic is yours to find; web ad supply is limited |
| Web portals (Poki, CrazyGames, GameDistribution) | Short session games that benefit from portal traffic | Portal ad revenue share | Exclusivity, little player data, ads only |
| Platform embeds (Discord Activities, Reddit Devvit, Telegram Mini Apps, YouTube Playables, TikTok Mini Games) | Group play inside an existing social graph | Platform IAP, platform ads, developer funds | Platform rules and fees, availability by region |
| Store wrappers (TWA on Google Play, Capacitor on iOS) | A web game that needs store discovery and store billing | Store IAP, native ad SDKs | Store fees, review rules (4.2, 4.7), billing rules |

For a daily social or group game the own URL and PWA route has the highest fit: it keeps the data, the streaks and the group graph [Reported, 2026-10]. Portals fit poorly for a daily group game, mainly because of exclusivity.

## 2. Web ads

### 2.1 Google H5 Games Ads (Ad Placement API)

Status: a closed beta that a publisher applies to [Reported, 2026-10]. Rules summarized in the notes:

| Rule | Detail |
|------|--------|
| Rewarded only after explicit opt in | The player chooses to watch |
| The reward has no value outside the game | No cash, no tradeable goods |
| No money for viewing, no "support us" copy | The ad is not a donation |
| Grant on the viewed callback | The reward is granted only when the API reports the ad was viewed (`adViewed`) |
| Full screen ads only at transitions | Through `adBreak()` at natural breaks |

Plan so that nothing depends on admission: a web first game builds its revenue on passes, subscriptions and group rounds, and treats H5 ads as an addition if and when it is admitted.

### 2.2 Web rewarded and display vendors

Vendors named in the notes: AppLixir, Playgama, AdinPlay (Venatus), Playwire, ayeT. Vendor material claims rewarded CPMs of $8 to $28 in the US [Unverified, vendor claim]. Before any integration: consent handling (TCF in the EEA and UK), ad quality controls, payout terms, script weight and whether the vendor's rules allow the planned reward.

### 2.3 Web specifics that change the economics

1. Ad blockers and browser privacy features reduce fill; access to play must never depend on an ad.
2. Native mediation SDKs do not apply in a PWA; web SDKs only [Unverified].
3. iOS Web Push works only for Home Screen web apps, after a user gesture, since iOS 16.4 [Reported, 2026-10]; push about offers goes through `lifecycle-crm` and its consent rules.

## 3. Portals

| Portal | Terms seen | Label | Watch |
|--------|-----------|-------|-------|
| Poki | 100% of ad revenue from traffic you bring, 50/50 on Poki's traffic; web exclusivity; selective admission | [Reported, 2026-10]; exclusivity length 5 or 7 years [Contested] | Exclusivity can block your own web distribution; read the contract |
| CrazyGames | Basic launch (about 2 weeks) then Full launch; EUR 100 payout minimum via Tipalti; revenue split not published | [Reported, 2026-10] | Split unknown until the deal |
| GameDistribution | Revenue share reported as 33% and as 45% | [Contested] | Read the live terms |
| YouTube Playables | Ads; a revenue share pilot | [Reported, 2026-10] | Eligibility and pilot status |
| Facebook Instant Games | Monetized through Audience Network; the notes also record "Meta Web Games ended 2026-09-30" after a 2025-07-31 Meta developer post on web and Instant Games changes | [Unverified] | Confirm the current program before planning |

Never sign a portal deal from this agent. The "what never to sign" list and the publish or self publish decision live in `growth-orchestrator` (`game-studio-lifecycle`).

## 4. Platform embeds

| Platform | Monetization seen | Label | Fit |
|----------|-------------------|-------|-----|
| Discord Activities | Embedded App SDK 2.5.0 (May 2026); SKUs for IAP and subscriptions on desktop in the US, UK and EU; fee reported differently by sources | [Reported, 2026-10]; fee [Contested] | High for group play |
| Reddit Devvit | Daily games encouraged; Developer Funds up to $167,500 per app (2025 to 2026) | [Reported, 2026-10] | Medium to high for daily games |
| Telegram Mini Apps | Telegram Stars for digital goods; Stars are bought through store IAP (about 30%) | [Reported, 2026-10] | Market dependent |
| TikTok Mini Games | Business verification; Growth Max testing reported 2026-05-13 | [Reported, 2026-10] | Test only |

Every embed is its own store id in the policy file (for example `discord`), with its own product ids, so `monetization_check.py` can confirm each catalog item is sold where it is offered.

## 5. Payments on the web

### 5.1 Stripe or a merchant of record

| Option | What it does | Tax position | Fits |
|--------|-------------|--------------|------|
| Stripe Checkout or Payment Element | Payment processing, subscriptions, webhooks | You are the seller: you register, collect and remit VAT or sales tax where the buyer lives | Teams ready to handle tax registrations |
| Merchant of record (Paddle, Lemon Squeezy) | The provider is the seller of record and handles consumer tax | The merchant of record collects and remits; higher fee | Small teams selling digital goods to many countries |

Tax note (contract section 5): selling digital goods on the web in the EU and Turkey creates VAT duties per buyer country, and Stripe alone is not a merchant of record. Either register and remit, or use a merchant of record. `compliance` and the human own this decision before the first web sale. Tax calculation tools compute the tax; they do not move the liability [Practitioner consensus].

### 5.2 What every web purchase flow needs

| Need | Detail | Owner |
|------|--------|-------|
| Server grant after a verified webhook | The client never grants; grants are idempotent on (store id, transaction key) | Product server, site-engineer |
| Refund and dispute webhooks wired | Revoke entitlements, claw back consumables ([Segmentation and payment ops](segmentation-and-payment-ops.md)) | Product server |
| Real money price including tax where required, before payment | Consumer law | compliance |
| EU withdrawal handling | Withdrawal information, the digital content consent step, and the withdrawal function for contracts that keep a right of withdrawal (from 2026-06-19, compliance rule SUB-EU-01) | compliance, site-engineer |
| Account binding | A purchase belongs to an account or group that survives a device change; guests can upgrade without losing purchases | Product |
| Restore | A web buyer who later installs the store app keeps what they bought | Product, store-submission |

## 6. Web shops for store apps

A store app may send players to a web shop where the rules allow it. The economics move monthly, so treat every fee here as a dated observation.

| Item | Status seen | Label |
|------|-------------|-------|
| Apple US storefront link outs | Allowed without an entitlement under Guideline 3.1.1(a) (guidelines dated 2026-06-08) | [Official, 2026-10] |
| Apple commission on US link outs | Litigated: Epic v Apple, Ninth Circuit December 2025 upheld contempt and allowed a cost based fee on remand; Supreme Court agreed to review on 2026-06-30; no rate set as of 2026-08-16 | [Reported, 2026-10]; treat 0% as temporary |
| Apple EU terms from 2026-10-01 | IAP 26% (15% small business and subscriptions after year 1); alternative in app payment 20% (10%); link out within 7 days 15% (10%); Core Technology Commission 5% for marketplace or web distributed apps | [Official, 2026-10] |
| Google Play fees from 2026-06-30 (US, EEA, UK) | 10% service fee on the first $1M plus 5% when Play Billing is used; above $1M disputed; Australia, Japan, Korea later; global 2027 | [Reported, 2026-10] |
| Google external content links | Install fees of $2.85 per app and $3.65 per game install within 24 hours | [Unverified] |
| Web shop vendors | Xsolla about 5%, Stash about 10% | [Unverified, vendor claim] |
| Web shop net and conversion | About $0.92 net per dollar vs $0.70 in store; conversion can drop up to 45% when players leave the app | [Unverified, vendor claim] |

Parity rules: the web shop sells the same SKUs with the same grants as the stores; the policy file holds every store's product id; price differences are decisions with a reason and a compliance check on how they are shown. Store fee modelling and price points belong to `pricing-strategy` (`iap-price-points`) and `mobile-app-growth` (`game-user-acquisition`).

## 7. Store wrappers for a web game

| Wrapper | Billing | Review rules that bite | Hand off |
|---------|---------|------------------------|----------|
| TWA on Google Play | Play Billing for digital goods; Billing Library 8 or later was required by 2026-08-31 (extension to 2026-11-01 possible) [Official, 2026-10] | Digital Asset Links must match the Play App Signing key, or the TWA shows browser UI [Official, 2026-10]; webview only apps risk minimum functionality findings [Reported, 2026-10]; new personal accounts need a 12 tester closed test for 14 days [Reported, 2026-10] | store-submission, site-engineer |
| Capacitor on iOS | In-App Purchase for digital unlocks (Guideline 3.1.1) [Official, 2026-10] | 4.2: elevate beyond a repackaged website [Official, 2026-10]; 4.7 if the app serves remote HTML5 mini games (IAP, report and block, age restriction, no native API exposure without permission) [Official, 2026-10]; privacy manifest for listed SDKs including Capacitor [Official, 2026-10] | store-submission, site-engineer |

## 8. Order of operations for a web first game

1. Web with Stripe (or a merchant of record) first: the season pass and the group consumable, no store fees, fastest learning. Tax decision made before the first sale.
2. Uncounted replay and practice free; a plus subscription when the archive is deep enough to be worth paying for.
3. Web ads only after consent is in place, and only as an addition (H5 Games Ads if admitted, or a vetted vendor).
4. The Google Play wrapper (TWA) with Play Billing for the same SKUs.
5. The iOS app with native value (Game Center, haptics, widgets or similar) so it clears 4.2, with IAP for the same SKUs.
6. Nothing in the plan depends on Google's H5 beta admitting the game.

Each step is a policy revision with new store ids, a passing `monetization_check.py` and `monetization_conformance.py` (with the new store's declarations file), and a G3 approval.

## 9. Quick checklist

- [ ] Route chosen per game (own URL, portal, embed, wrapper) with the reason in `DECISIONS.md`.
- [ ] Tax decision (register and remit, or merchant of record) made with compliance before the first web sale.
- [ ] Webhooks verified server side; grants idempotent; refunds and disputes revoke.
- [ ] Access to play never depends on an ad; web ads only after consent.
- [ ] No portal exclusivity signed without growth-orchestrator's review and the human's approval.
- [ ] Every store and embed is a store id in the policy with product ids for every item it sells.
- [ ] Web shop parity with the stores; fees dated and labeled.
