# IAP Price Points, Regional Prices and Web Shop Parity for Games

> Knowledge as of 2026-10 (research pass 2026-10-12). Apple's In-App Purchase pricing help and its EU terms page were read at the source [Official, 2026-10]; Google Play pricing and fee facts were readable only as search summaries [Reported, 2026-10]; web shop numbers come from vendors [Unverified, vendor claim]. Fees and court cases move monthly: every fee row carries a confidence label and a re-check date. No price is published from here: every live price change is a G3 change request.

## 0. Scope and boundary

| Work | Owner |
|------|-------|
| Price points per SKU and currency, the price ladder, regional prices, web shop parity, currency display rules, the fee landscape used for price decisions | `pricing-strategy` (this module) |
| The economy: currencies, sources and sinks, which SKUs exist, what each grants (typed grants), offer points, caps | `game-monetization` |
| Promotions on top of list prices (launch discounts, bundles as incentives, promo calendar) | `offer-strategy` |
| Whether a price display, a discount claim, a bundle size or a minor's purchase flow is lawful | `compliance` ([Games and virtual currencies](../../compliance/references/games-and-virtual-currencies.md)) |
| Fee math inside payback and net revenue per install | `mobile-app-growth` ([App growth model](../../mobile-app-growth/references/app-growth-model-and-unit-economics.md) section 3) |
| IAP products attached to the build under review | `store-submission` |
| ARPDAU, payer conversion and ARPPU definitions used to read a price change | `measurement` ([Game KPIs](../../measurement/references/game-kpis.md)) |

## 1. The price model in the contract

The Game Monetization Contract ([contract](../../game-monetization/references/monetization-contract.md) section 5) fixes how prices are stored, so every game, store and script reads them the same way:

| Field | Rule |
|-------|------|
| `sku` | One canonical, store neutral id per product (`season_pass`, `coins_1200`) |
| `basePrice` | `{currency, minor}`: integer minor units (499 means 4.99), never floats |
| `platformPrices` | Per store id, per currency, in minor units, because stores set prices by price point and convert by their own rules |
| `storeProductIds` | Keyed by the policy's store ids (`web`, `apple`, `google`) |
| `random`, `odds` | A random item needs odds and the loot box declarations; the contract prefers fixed price items |
| Virtual currencies | `purchasable` and `showRealMoneyPrice` per currency |

A price decision from this module is a change to `basePrice` and `platformPrices` in the policy file plus the matching store console entries; `monetization_check.py` fails an item without a real money price in a listed currency.

## 2. Store price mechanics

### 2.1 Apple

| Fact | Detail | Evidence |
|------|--------|----------|
| Base storefront | Pick a base country or region; Apple generates comparable prices on the other 174 storefronts and 43 currencies, accounting for foreign exchange and certain taxes and following each region's most common price convention | [Official, 2026-10] |
| Automatic updates | Apple periodically updates prices on the other storefronts when taxes and exchange rates change, never in the base storefront, and notifies in advance | [Official, 2026-10] |
| Manual storefronts | You may manage some or all storefronts yourself; Apple then stops adjusting them, and you own tax and exchange rate changes | [Official, 2026-10] |
| Price points | Up to 800 price points by default; 100 higher price points on request, up to $10,000 | [Official, 2026-10] |
| Changing the base | Deletes scheduled price changes; new pricing takes effect immediately | [Official, 2026-10] |
| Türkiye | Apple applied a price equalization on 2025-11-17 | [Official, per the [Deep linking and web to app](../../mobile-app-growth/references/deep-linking-and-web-to-app.md) table] |

### 2.2 Google Play

| Fact | Detail | Evidence |
|------|--------|----------|
| Default price | The price you enter is the base for market prices; Play converts to local currency, adds tax in some countries, applies local pricing patterns and the exchange rate of the day you set it | [Reported, 2026-10] |
| Refresh | Local prices can be refreshed later to newer exchange rates | [Reported, 2026-10] |
| Per region | One-time products can carry different prices per region (edit per row or bulk edit) | [Reported, 2026-10] |
| Ranges | Allowed price ranges per country and currency are listed in Play Console Help | [Reported, 2026-10]; read the live list |
| Pricing templates | Described on a Google page; a third party reports they were removed | [Contested]; check the console |

### 2.3 Web (Stripe or a merchant of record)

You set each currency price yourself. Show consumers final prices with taxes in the EU, decide merchant of record before the first sale (`compliance` section 7.4 of the games pack), and keep the same `sku` and grant as the store item.

## 3. Regional pricing practice

| Approach | When it fits | Risk |
|----------|--------------|------|
| Store equalization from one base storefront | Default for a new game; the store tracks tax and exchange rates | Prices in low income markets stay high relative to local income |
| Manual prices for chosen storefronts | Markets with clear purchasing power gaps (for example Türkiye, India, Brazil) and enough volume to read a test | You own every exchange rate and tax change; inflation erodes the price (re-check monthly in TRY) |
| Round local price points | Every market: follow the local convention the store already uses (Apple follows "the most common pricing convention for each country or region") | Endings change perceived value; one rule per market ([Price architecture](price-architecture-and-pack-sizes.md) section 5) |
| Same price everywhere in USD terms | Rarely right | Ignores tax inclusive price display and local conventions |

Evidence is thin for games: no public study of regional IAP price elasticity in games was found in the 2026-10-12 pass. Treat purchasing power pricing as a hypothesis and test it:

1. Pick 1 to 3 markets with enough payers to read a change (at least about 100 payers per arm per read; size with [Elasticity and price tests](elasticity-and-price-tests.md)).
2. Change price points per market (a geo test), not per player. Same item, different prices for different players on one storefront is personalized pricing: `compliance` first.
3. Read 4 weeks before and after with a control market: net revenue per DAU (ARPDAU IAP, net), payer conversion, ARPPU, refund rate and D7 ([Game KPIs](../../measurement/references/game-kpis.md)).
4. Keep a fence: billing country is the store's storefront; on the web, the payment card country and VAT location.
5. Log the change in `EXPERIMENTS.md` with the policy revision.

## 4. Price ladders for games

Honest starting point: **no public price ladder for mobile games was found** in the 2026-10-12 research pass. The anchors below are single observations from reports, not ladders to copy.

| Observation | Value | Evidence |
|-------------|-------|----------|
| Piggy bank in Hexa Sort | Unlocks at level 7, price hidden until the goal, $4.99; third top IAP on US iOS | [Reported, 2026-10, Sensor Tower via maf.ad] |
| No Ads bundle in Color Block Jam | $11.99 US | [Reported, 2026-10] |
| Puzzmo Plus | About $40 a year (archives, leaderboards, no ads) | [Reported, 2026-10] |
| Royal Match continue | About 900 coins first, more than 2,000 after a second fail | [Reported, 2026-10]; an escalation pattern the contract forbids (`priceEscalation`), shown only as what not to copy |
| Royal Pass | From level 37, 30 steps a month | [Reported, 2026-10] |

### 4.1 Build the ladder from roles

| Role | Job | Rule |
|------|-----|------|
| Entry | The first purchase is easy to say yes to | The lowest price point that still clears the store's fixed costs on the web route (section 7) |
| Starter pack | One time, after the first levels, the best value the player will see | Clearly once per player; no countdown when minors may play |
| Core currency packs | Day to day purchases | Value per unit rises with pack size, honestly; the common item prices are reachable without leftovers |
| Value pack | The pack labeled "best value" | Only if its value per unit is really the best |
| Top pack | Payers who already spend | No pressure copy; the same rules as every pack |
| Pass and subscription | Recurring value | Monthly or season price; what is free and what is paid listed before purchase |
| Ad removal | Players who hate interstitials | Say whether rewarded ads remain |

### 4.2 Ladder checks (run on every draft)

1. **Per unit value**: real money per currency unit falls (or stays) as packs grow; a "best value" label sits on the true best.
2. **No forced leftovers**: for every item priced in currency, run the bundle arithmetic in the compliance pack (section 7.3): cheapest path from a zero balance, leftover share above 50% or more than one pack needed is a flag [house thresholds; the CPC principles name the practice, not a number].
3. **Real money equivalent**: every currency price has a real money equivalent shown at the point of purchase (section 6).
4. **No escalation**: no item gets more expensive within an attempt or with each retry.
5. **Store reachability**: every price exists as a price point on each store and in each listed currency.
6. **Minor units**: every price in the policy is an integer in minor units; JPY and other zero decimal currencies have no minor digits.

Illustrative ladder (placeholder prices to show the arithmetic, not a recommendation):

| Pack | Price (USD) | Coins | Coins per USD | Real money per 100 coins |
|------|------------:|------:|--------------:|-------------------------:|
| Small | 1.99 | 1,000 | 502.5 | 0.199 |
| Medium | 4.99 | 2,750 | 551.1 | 0.181 |
| Large | 9.99 | 6,000 | 600.6 | 0.167 |
| Best value | 19.99 | 13,000 | 650.3 | 0.154 |

Check against items: a continue at 900 coins is covered by the small pack with 100 coins left (11%), no flag. A booster bundle at 1,100 coins needs two small packs ($3.98, 2,000 coins, 900 left, an 82% leftover share and two purchases) or one medium pack ($4.99, 1,650 left, 150%): the cheapest path is two small packs, which is a flag either way; reprice the item or add a pack size (the decision goes to `game-monetization`).

### 4.3 A daily social game

A game like Aloo sells few things: a season pass, a group encore (a fixed price consumable with no randomness that every group member receives) and a Plus subscription. The ladder is short: one price per SKU per currency, the same everywhere a player can buy it, and the encore's buyer shown to the group. The fairness rule decides what may be sold at all (contract section 3); this module only prices what passes it.

## 5. Web shop parity

| Question | Options | Consequences |
|----------|---------|--------------|
| Same SKU and grant | Always: one `sku`, one grant, both routes | Players and support see one catalog; the grant log stays idempotent per store |
| Same price | Equal price on web and in store; lower web price; same price with a web only bonus | A lower price or a bonus is a reason to leave the app, which store rules govern per storefront; equal prices give the cleanest parity but keep the fee gap |
| Apple multiplatform rule | Items usable in the iOS app are also offered as In-App Purchases (3.1.3(b)) | The web cannot be the only way to buy something used in the iOS app [Official, 2026-10] |
| Telling players about web prices | US storefront: buttons and links to web purchases allowed without an entitlement (3.1.1(a)); EU: link out terms with a 7 day commission window; Android: external offers programs | Wording about price differences goes to `compliance` and `store-submission` per storefront |
| Discounts on the web shop | The EU prior price rule (lowest price in the last 30 days) and Türkiye's 10 day rule apply to announced reductions | `compliance` checks every "save" or "was" claim |
| Taxes | The store is the merchant of record for IAP; on the web you are, unless a merchant of record sells | A written VAT decision before the first web sale |

Economics: web shop savings depend on the fee route (section 7) and on conversion leaving the app; one vendor reports conversion drops of up to 45% when the purchase leaves the app [Unverified, vendor claim]. Use the break even conversion formula in [App growth model](../../mobile-app-growth/references/app-growth-model-and-unit-economics.md) section 3.2 per market and per price point, and model a non zero US link out fee.

## 6. Currency display rules

1. **Real money price next to the virtual price** at the point of purchase for every item bought with a purchasable currency (EU CPC key principles on in-game virtual currencies, 2025-03-21) [Reported, 2026-10]. The policy file's `showRealMoneyPrice` must be true for purchasable currencies.
2. **How to compute it**: item price in currency x (pack price / pack size) of the cheapest pack a player can buy (compliance pack section 7.3, step 5); round to the currency's minor unit and show the currency.
3. **Final price to consumers**: tax inclusive in the EU and Türkiye, in the buyer's currency where the store sells in it.
4. **No hidden costs**: no second currency that hides the total; an item needing two currencies shows the combined real money price.
5. **Odds next to random items** before purchase (Apple 3.1.1 [Official, 2026-10]); the contract prefers no random paid items.
6. **No pressure**: no countdown or scarcity copy where minors may play; no "buy now" aimed at children (UCPD Annex I point 28) [Reported, 2026-10].
7. **Withdrawal and refunds**: the information before purchase and the receipt follow the store or, on the web, the EU withdrawal rules (`compliance`).
8. **Minors**: parental approval of purchases where the law asks (Turkey Law 7578, the FTC Genshin order for under 16s and random items) [Reported, 2026-10].

## 7. The fee landscape in 2026, by confidence

| Route | Fee | Confidence | Re-check by |
|-------|-----|------------|-------------|
| Apple IAP, standard | 30%; 15% Small Business Program and subscriptions after year one | [Official, long standing] | 2027-01 |
| Apple EU from 2026-10-01, IAP | 26%; 15% for Small Business, Mini Apps and Video Partner programs and subscriptions after year one; "App Store commission rates apply to the price paid by the customer" | [Official, 2026-10] (Apple's EU page, superseded by Attachment 14 of the agreement) | 2027-01 |
| Apple EU, alternative in-app payment processing | 20%; 10% for program participants and subscriptions after year one | [Official, 2026-10] | 2027-01 |
| Apple EU, link out to web purchases | 15%; 10% for program participants and subscriptions after year one; only on sales within 7 days of the link tap | [Official, 2026-10] | 2027-01 |
| Apple EU, Core Technology Commission | 5% on digital sales in apps distributed outside the App Store (alternative marketplaces, web distribution), on the price less transaction taxes; Core Technology Fee, Initial Acquisition Fee and Store Services Fee removed | [Official, 2026-10] | 2027-01 |
| Apple US storefront, link out | 0% today while litigated; Apple proposed 15%, 10% and 5% tiers (2026-08-13); the Supreme Court agreed to review (2026-06-30); no rate set | [Contested]; plan with a non zero scenario | 2026-12 |
| Google Play US, UK, EEA from 2026-06-30 | Service fee 10% on the first $1M of annual earnings and on auto-renewing subscriptions; plus a 5% billing fee only when Play Billing is used | [Reported, 2026-10]; the `mobile-app-growth` fee table labels it official | 2027-01 |
| Google Play above $1M (one-time products, most game IAP) | 20% on new installs, 25% on existing installs reported; Games Level Up program rate of 15% on new installs from 2026-09-30 reported | [Contested]; research notes call the above $1M terms disputed | 2026-12 |
| Google Play, other regions | Australia from 2026-09-30, Japan and Korea from 2026-12-31, the rest by 2027-09 | [Reported, 2026-10] | 2027-01 |
| Google Play US external content links | A per install fee of $3.65 for games ($2.85 for apps) within 24 hours of the link is reported | [Contested] | 2026-12 |
| Web shop providers | Xsolla about 5%, Stash about 10% | [Unverified, vendor claim] | 2027-04 |
| Card processing on the web | Stripe standard 2.9% + $0.30 in the US | [Official vendor pricing, per the `mobile-app-growth` fee table] | 2027-04 |

The fee table used for payback math is [App growth model](../../mobile-app-growth/references/app-growth-model-and-unit-economics.md) section 3.1; when a row here changes, that table changes in the same session (and the reverse).

### 7.1 Net per sale, worked (US, $4.99, before sales tax, fee assumptions from the table)

| Route | Fee | Net to the studio |
|-------|-----|------------------:|
| Apple IAP, standard 30% | 1.497 | 3.49 |
| Apple IAP, Small Business 15% | 0.7485 | 4.24 |
| Google Play, first $1M, 10% + 5% billing | 0.7485 | 4.24 |
| Web via Stripe (2.9% + $0.30), US link out at today's 0% | 0.4447 | 4.55 |
| Web via Stripe with a hypothetical 15% Apple link out fee | 1.1932 | 3.80 |

Fixed processing fees punish small prices: $0.30 is 30% of a $0.99 sale but 1.5% of a $19.99 sale. Price entry items for the store route and test web shops on mid and top packs first. In the EU, confirm in Attachment 14 how VAT enters the commission base before modeling: Apple's page says commission applies "to the price paid by the customer" while the Core Technology Commission applies to the price "less any transaction taxes" [Official, 2026-10].

## 8. Price changes and tests

1. A price change is a G3 change request per store and storefront, with the policy file diff (`basePrice`, `platformPrices`, `policyRevision` raised) and a rollback.
2. Apple: changing the base storefront deletes scheduled changes and applies immediately [Official, 2026-10]; schedule changes for manual storefronts in the live ops calendar so no event shows an old price.
3. Consumables and passes: a new price applies to future purchases; subscription price increases follow each store's notice and consent rules (`compliance`, `mobile-app-growth`).
4. Read every change on net ARPDAU IAP, payer conversion, ARPPU, refund rate and D7 against a control market for 4 weeks; judge on net revenue per DAU, never on conversion alone.
5. Price tests between players on one storefront are personalized pricing in the EU: disclosure and `compliance` review first; prefer geo or time based tests.
6. `game-monetization` runs offer tests (where and when an offer appears); this module owns the price points those offers use.

## 9. Checklist

- [ ] Every SKU has one `sku`, store product ids for every store it sells on, and an integer minor unit price in every listed currency.
- [ ] Each price exists as a store price point; manual storefronts are listed with their next review date.
- [ ] Ladder checks in section 4.2 pass (per unit value, leftovers, real money equivalents, no escalation).
- [ ] Web shop: same grants, a parity decision with its consequences, tax decision recorded.
- [ ] Every fee assumption names its route, label and re-check date.
- [ ] Display rules in section 6 confirmed on screen by `compliance`.
- [ ] The change request carries the policy diff, store entries, read plan and rollback.

## 10. Sources

| # | Source | Publisher | Date | Supports |
|---|--------|-----------|------|----------|
| 1 | Set a price for an In-App Purchase | App Store Connect Help, developer.apple.com/help/app-store-connect | read 2026-10-12 | Base storefront, 174 storefronts, 43 currencies, 800 + 100 price points, automatic updates [Official, 2026-10] |
| 2 | DMA and apps in the EU | Apple Developer support | terms effective 2026-10-01, read 2026-10-12 | EU commission rates, 7 day window, CTC, removed fees [Official, 2026-10] |
| 3 | App Review Guidelines 3.1.1, 3.1.1(a), 3.1.3(b) | Apple | 2026-06-08 version | Odds, US link outs, multiplatform items [Official, 2026-10] |
| 4 | Play Console Help on default prices and one-time products | Google | seen as search summaries 2026-10-12 | Conversion, pricing patterns, per region prices [Reported, 2026-10] |
| 5 | Play billing and fee changes (Android Developers Blog 2026-06; Pocketgamer.biz; Android Headlines) | Google and press | 2026-06 | US, UK and EEA fees from 2026-06-30, Level Up rate [Reported, 2026-10] |
| 6 | Epic v Apple coverage | Fenwick, The Next Web, Courthouse News | 2025-12 to 2026-08 | US link out status [Reported, 2026-10] |
| 7 | CPC key principles on in-game virtual currencies | European Commission CPC network via law firm summaries | 2025-03-21 | Real money display, leftovers, withdrawal [Reported, 2026-10] |
| 8 | Piggy banks in top games | maf.ad (Sensor Tower data) | 2025 | Hexa Sort piggy bank [Reported, 2026-10] |
| 9 | Color Block Jam teardown | Segwise | 2025-04 | No Ads bundle price [Reported, 2026-10] |
| 10 | Royal Match teardowns | fungies.io, FoxData, Naavik | 2024 to 2025 | Continue escalation, Royal Pass [Reported, 2026-10] |
| 11 | Web shop business case and provider pricing | Unity, Xsolla, Stash | 2025 to 2026 | Web shop economics [Unverified, vendor claim] |
| 12 | Games and virtual currencies rule pack | Ads Master `compliance` | 2026-10 | Bundle arithmetic, web sales checks, minors |
| 13 | Game Monetization Contract v0.1 | Ads Master `game-monetization` | 2026-10 | Price fields, fairness rule |
