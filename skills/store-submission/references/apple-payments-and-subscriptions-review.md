# Apple Payments and Subscriptions Review

> Knowledge as of 2026-10. Guideline text read at the source on 2026-10-15 (last updated 2026-06-08, [Official, 2026-06]); Apple's auto-renewable subscriptions page and the complete review help page read 2026-10-12 ([Official, 2026-10]); EU terms from the 2026-08-18 news item ([Official, 2026-08]) and the research pass. This module checks that what is sold passes review. It does not decide what to sell or at what price: paywall design, offers and store pricing belong to `mobile-app-growth`, price points to `pricing-strategy`, a game's economy and `monetization-policy.json` to `game-monetization`, consumer law verdicts to `compliance`.

## 1. What must use in-app purchase (3.1.1)

| Rule | Evidence |
|------|----------|
| Unlocking features or functionality inside the app (subscriptions, in-game currencies, game levels, premium content, full versions) uses in-app purchase; no license keys, QR codes or cryptocurrencies as unlock mechanisms | [Official, 2026-06] |
| Credits or in-game currencies bought through in-app purchase may not expire | [Official, 2026-06] |
| A restore mechanism exists for any restorable in-app purchase | [Official, 2026-06] |
| Apps offering loot boxes or other mechanisms that give randomized virtual items for purchase disclose the odds of each type of item before purchase | [Official, 2026-06] |
| Items acquired on other platforms or the website may be used in the app if they are also available as in-app purchases (3.1.3(b), multiplatform services, including consumables in multiplatform games) | [Official, 2026-06] |

Restorable means non consumables and auto-renewable subscriptions in StoreKit terms; consumables (continues, boosters, coins) are not restored [Practitioner consensus]. A season pass is restorable when it is sold as a non consumable or a subscription. With `--policy`, `submission_check.py` fails a dossier that marks restore n/a while the catalog sells a non consumable, subscription or season product in a store.

## 2. Links to other purchase methods

| Storefront | Rule | Evidence |
|------------|------|----------|
| United States | Entitlements are not required for buttons, external links or other calls to action to a website purchase | [Official, 2026-06] |
| Specific regions with StoreKit External Purchase Link Entitlements | The app may offer in-app purchase and also a link to the developer's website about other ways to buy, under the entitlement agreement | [Official, 2026-06] |
| All other storefronts | Apps and metadata may not include buttons, external links or other calls to action that direct customers to purchasing other than in-app purchase | [Official, 2026-06] |
| Communication outside the app | Developers may tell their user base about other purchase methods outside the app | [Official, 2026-06] |
| Abuse | Misleading marketing, scams or fraud in relation to an entitlement leads to removal and possible removal from the program | [Official, 2026-06] |

The fee on US link outs is in litigation (Epic v Apple): a 2025-04 order set zero commission; the Ninth Circuit (2025-12) kept the contempt finding, allowed a cost based fee and remanded; rehearing was denied in 2026-03; Supreme Court review was in motion around 2026-06-30; no rate was set as of 2026-08-16 [Reported, 2026-10]. Treat zero commission as temporary. Whether to link out, from which storefront and at what price is a `mobile-app-growth` and human decision; this agent checks only that the link appears on allowed storefronts and that the screen is described in the notes.

## 3. EU terms from 2026-10-01 (high level)

Apple's 2026-08-18 news item lists changes effective 2026-10-01: adjusted commission rates across the App Store, alternative payments and alternatively distributed apps; apps may offer alternative payment options alongside Apple in-app purchase; child safety protections for alternative payments on the App Store; broader qualifications to run alternative marketplaces and distribute from the web [Official, 2026-08]. The research pass recorded the rates on Apple's EU page as: in-app purchase 26% (15% for small business and for subscriptions after year one), alternative in-app payment 20% (10%), link out within 7 days 15% (10%), and a 5% Core Technology Commission for marketplace or web distributed apps [Official, 2026-10] (read in the research pass; re-read the live page before any decision rests on a number).

Review consequences for this agent:
1. An alternative payment option in the EU is a new business model change: describe it in the notes and confirm it is enabled only on the EU storefronts the terms cover.
2. Child safety protections apply to alternative payments: when the audience includes minors, `compliance` confirms the flow before submission.
3. Rates and the choice of payment route stay with `mobile-app-growth`, `pricing-strategy` and the human.

## 4. Subscriptions (3.1.2)

| Rule | Evidence |
|------|----------|
| Ongoing value; the period lasts at least 7 days; available across all of the user's devices; examples include new game levels, episodic content and multiplayer support | [Official, 2026-06] |
| Before asking a customer to subscribe, describe clearly what the user gets for the price (3.1.2(c)) and meet Schedule 2 of the Developer Program License Agreement | [Official, 2026-06] |
| The sign-up screen shows the subscription name and duration and the content or services provided; the full renewal price, clear, prominent and localized; a way for current subscribers to sign in or restore | [Official, 2026-10] |
| The app and the App Store metadata link to Terms of Use and the Privacy Policy | [Official, 2026-10] |
| The amount that will be billed is the most prominent pricing element; per month or savings breakdowns sit in a subordinate position and size | [Official, 2026-10] |
| A free trial screen states how long the trial lasts and the price billed after it | [Official, 2026-10] |
| Review needs a demo account with an expired subscription to see the whole purchase flow | [Official, 2026-10] |

### Paywall review checklist (one row per paywall and per storefront language)

| # | Check | Pass when |
|---|-------|-----------|
| 1 | Name and duration | "Plus, monthly" or equivalent visible before the buy button |
| 2 | What the user gets | Concrete content or features, not "premium" alone |
| 3 | Billed amount most prominent | The amount charged on confirmation is the largest price on screen; "per week" equivalents are smaller and below it |
| 4 | Renewal | Full renewal price and period visible; auto renewal stated |
| 5 | Trial | Trial length and the price after the trial, on the same screen |
| 6 | Restore or sign in | A visible Restore purchases control (or sign in for existing subscribers) |
| 7 | Terms and Privacy | Tappable links on the paywall; the same URLs in App Store Connect metadata |
| 8 | Close | The paywall can be dismissed when the app offers free use; no hidden close button [Practitioner consensus] |
| 9 | Localization | Prices come from StoreKit for the storefront, not hard coded |
| 10 | Copy verdict | `compliance` verdict on every claim and price line on the paywall |

### 2026 subscription changes worth checking before a submission

| Change | Evidence |
|--------|----------|
| Monthly subscriptions with a 12 month commitment are available (news 2026-04-27) | [Official, 2026-04] (title read; read the help page before configuring) |
| iOS 27: subscription Bundles and Suites; make sure the app uses StoreKit 2; multiseat purchasing on by default for subscriptions in App Store Connect from 2026-09-16; Volume Purchasing launches 2026-10-22 | [Official, 2026-09] |

A product left on default multiseat settings can appear in Apple Business or Apple School Manager purchase options: review the purchase option settings for consumer apps that should not be sold by the seat.

## 5. In-app purchases at review time (2.1(b))

| Step | Detail | Evidence |
|------|--------|----------|
| Complete | Every configured product is complete, up to date, visible to the reviewer and functional | [Official, 2026-06] |
| Explained | A product the reviewer cannot find (seasonal, region locked, unlocked late in a game) is explained in the notes with how to reach it | [Official, 2026-06] |
| Attached | Products are in Ready to Submit and attached to the version under review | [Official, 2026-10] (research pass) |
| Reachable | The demo account can reach the paywall without playing for an hour; give a shortcut or a seeded account state and say where | [Practitioner consensus] |
| Sandbox | Purchases tested with a sandbox account on the submitted build | [Practitioner consensus] |

## 6. Games: what is sold and how review reads it

| Item | Type | Review checks |
|------|------|---------------|
| Continue after a fail, extra moves, boosters, lives refill, coins | Consumable | Fixed price shown before purchase; coins show real money price in the shop (contract rule); credits do not expire |
| Remove ads | Non consumable | Restore; no ads after purchase (a "No ads" product that still shows ads is a misleading feature and a consumer law risk) |
| Season pass for a fixed season | Non consumable or subscription | If auto-renewable: at least 7 days, ongoing value, 3.1.2 disclosures; restore |
| Monthly membership (archive, stats, no ads) | Auto-renewable subscription | Section 4 in full |
| Group bonus round bought by one player for the group (the Encore pattern in the monetization contract) | Consumable | Fixed price, no randomness; the review notes say who receives it and that it does not change ranked results |
| Paid random items (loot boxes, gacha, packs) | Consumable | Odds before purchase; age rating loot box answer (9+ minimum; Australia 16+, Brazil A18) [Official, 2026-10]; country rules in section 7 |

The fairness rule of the Game Monetization Contract (ranked results are never purchasable) is not an App Store rule, but store reviewers and regulators read pay to win in competitive modes as misleading when the listing promises fair play. The contract and `monetization_check.py` enforce it before this agent sees the build.

## 7. Loot boxes and random items across markets

| Market or rule | Requirement | Evidence |
|----------------|-------------|----------|
| Apple 3.1.1 | Odds of each item type disclosed before purchase | [Official, 2026-06] |
| Google Play | Odds disclosed before purchase, in close proximity to the purchase | [Reported, 2026-10] |
| Apple age rating | Loot boxes set at least 9+; Australia 16+; Brazil A18 | [Official, 2026-10] |
| UK | ASA and CAP enforcement notice (2026-02-26): "Contains loot boxes" shown prominently in store listings, monitoring from 2026-05-26 | [Reported, 2026-10] |
| Brazil | Law 15.211/2025 (ECA Digital): paid loot boxes banned for minors, in force from 2026-03 | [Reported, 2026-10] |
| PEGI | New games with paid random items default to PEGI 16 from 2026-06-01; reclassification of existing games from 2026-10-01 | [Reported, 2026-10] |
| Belgium | Paid loot boxes treated as gambling since 2018 | [Reported, 2026-10] |

Ads Master's position, from the proposal and the contract: do not ship paid random items in a new game. When a project already has them, `compliance` gives a per market verdict and this agent checks that the odds screen, the age rating answers, the UK listing label (with `app-store-optimization`) and `storeDeclarations.lootBoxes` agree.

## 8. Google Play counterpart (brief)

| Topic | Rule | Evidence |
|-------|------|----------|
| Billing | Digital goods through Google Play Billing, or the alternative billing and external link programs where enrolled (owned by `mobile-app-growth`) | [Official] (mobile-app-growth module) |
| Library version | Billing Library 8 or later for new apps and updates since 2026-08-31; extension to 2026-11-01 on request | [Official, 2026-09] |
| Subscription disclosure | Terms, price, billing frequency, auto renewal and trial conversion disclosed; how to manage and cancel; easy online cancellation | [Reported, 2026-10] |
| Cancellation and trials | Cancellation keeps access until the end of the paid period; a trial converts at full price at the end; people who already used a trial lose trial eligibility | [Official, 2026-10] |

Both stores' paywalls share one copy deck; differences in renewal and trial wording come from each store's rules, and both versions pass `compliance`.

## 9. Pre-submission payments checklist

- [ ] Every digital unlock goes through in-app purchase, except allowed US or entitlement links.
- [ ] Every product Ready to Submit, attached to the version, bought in the sandbox on the submitted build.
- [ ] Restore works on a fresh install with the demo account (non consumables and subscriptions).
- [ ] Paywall checklist (section 4) passed for every paywall and language.
- [ ] Demo account with an expired subscription exists and is in the notes.
- [ ] Virtual currency shows its real money price; no currency expires.
- [ ] Odds screen before every random purchase, or no random paid items.
- [ ] External purchase links only on allowed storefronts; EU alternative payments only where the terms apply.
- [ ] With a game policy file: `submission_check.py --policy` passes.
- [ ] `compliance` verdict on the paywall copy and prices.
