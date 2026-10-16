# Games and Virtual Currencies

> Knowledge as of 2026-10 (research pass 2026-10-12). Rule pack for games that sell virtual currencies, items, passes or paid random items (loot boxes), show ads, or may reach minors. Almost every legal row below was readable only through law firm summaries and press coverage, so it carries [Reported, 2026-10] and a "Recheck by" date: verify at the source (the regulation, the regulator's notice, the court order) with the `ads-verify` skill before a verdict that blocks or approves a launch rests on it. Apple guideline text was read at the source (guidelines dated 2026-06-08) and is labeled [Official, 2026-06]. This pack is not legal advice; anything it cannot place under a documented rule is NEEDS HUMAN OR LEGAL REVIEW.

| This pack covers | It does not cover (route elsewhere) |
|------------------|-------------------------------------|
| Virtual currency and item sales, price display, bundles, odds, loot box labels, minors and spending controls, game ads (gameplay representation, loot box disclosure), store declarations and age ratings, the compliance review of a `monetization-policy.json` | Real money gambling and prizes ([Regulated categories](regulated-categories.md)); general price reduction and urgency rules ([Pricing, promotions and consumer law](pricing-promotions-and-consumer-law.md)); email, SMS and push consent ([Privacy in marketing and consent](privacy-in-marketing-and-consent.md)); economy design and offer tuning (`game-monetization`); store submission dossiers (`store-submission`) |

Boundary: Ads Master owns how a game earns, is found, keeps players, is measured and passes review; the game's own repo owns how it plays. Compliance judges what is sold, shown and said. It never proposes rule or level changes; when the law requires a product change (an age gate, a parental approval step), it states the requirement and hands it to `game-monetization` and the human.

## 1. Review order for a game

1. **Scope:** product id, policy revision, stores (web, Apple, Google), markets sold in, audience (minimum age, kids mode, unknown age handling), what is sold (currencies, items, passes, subscriptions, random items), ad formats.
2. **Mechanical screen:** run the contract checker on the policy file (section 7). Exit 1 means fix before review; exit 2 means the file could not be read or the contract version is unsupported.
3. **Rule pass by market:** sections 2 and 3, using the feature matrix in section 6.
4. **Screens and copy:** the purchase screen, odds screen, offer pop ups, store text and every ad (section 8).
5. **Verdict per market** in the standard vocabulary (APPROVED, APPROVED WITH EDITS, NEEDS HUMAN OR LEGAL REVIEW, BLOCKED) with rule IDs from this pack.

## 2. Rules by jurisdiction

| Rule ID | Market | Rule (as reported) | What it means for a game | Label | Recheck by |
|---------|--------|--------------------|--------------------------|-------|------------|
| GAME-EU-01 | EU | CPC network Key Principles on in-game virtual currencies (2025-03-21, led by the Netherlands ACM and the Norwegian Consumer Authority): show the price of virtual items in real money; no practices that hide the real cost; no forcing players to buy more currency than they need (bundle sizes that leave leftovers); clear information before purchase; respect withdrawal rights; protect children | Every item priced in currency also shows its real money equivalent at the point of purchase; pack sizes are checked with the bundle arithmetic in section 7.3 | [Reported, 2026-10] | 2027-03 |
| GAME-EU-02 | EU | CPC coordinated action (2026-09-30) against nine companies after a 2025 dialogue that did not satisfy the network: Crytek, InnoGames, King.com, Mojang, Plarium, PLR Worldwide Sales, Riot Games, Supercell, Ubisoft EMEA; a separate action concerns Activision Blizzard UK. An earlier CPC action (2025-03) addressed Star Stable (ads to children, time pressure, currency information) | The principles are being enforced against market leaders, not only published. National authorities may follow with enforcement | [Reported, 2026-10] | 2027-01 |
| GAME-EU-03 | EU | UCPD Annex I point 28: a direct exhortation to children to buy, or to persuade their parents to buy, is always unfair. The 2014 CPC common position on in-app purchases: a game presented as "free" must not mislead about real costs; no direct exhortation to children; clear payment information; no purchases by default without explicit consent | No "Buy now!" aimed at children in offers, push, ads or store text; "free to play" only with in-app purchases disclosed; purchase confirmation every time | [Reported, 2026-10] | 2027-06 |
| GAME-EU-04 | EU | DSA Article 28 guidelines on the protection of minors (2025-07): recommend keeping minors from paid random items, manipulative design and practices that obscure real money cost. Non binding; Article 28 applies to online platforms (services that disseminate user content to the public), and micro and small enterprises are exempt unless designated very large | Many games are not online platforms, but a game with public user content may be. Either way, the guidelines show where the Digital Fairness Act is heading; design for them now | [Reported, 2026-10] | 2027-01 |
| GAME-EU-05 | EU | Digital Fairness Act: not law. A proposal is expected in Q4 2026 covering dark patterns, addictive design, virtual currencies and minors | Watch item only; never cite it as a rule in a verdict until adopted | [Reported, 2026-10] | 2026-12 |
| GAME-EU-06 | EU | Consumer Rights Directive: for digital content not on a tangible medium, the 14 day withdrawal right ends only when supply begins with the consumer's prior express consent and acknowledgement that the right is lost, confirmed afterwards | Web checkout (Stripe or a merchant of record) collects that consent and acknowledgement and confirms it in the receipt; app stores run their own flows (check their terms) | [Reported, 2026-10] | 2027-06 |
| GAME-EU-07 | EU, UK | Consent before reading or storing identifiers for ads (ePrivacy Art 5(3), GDPR). CNIL fined a game publisher (Voodoo) EUR 3 million in 2023 over advertising use of an identifier without consent. The Italian competition authority fined Apple EUR 98.6 million (2025-12) over the double consent burden of ATT on developers; ATT itself is still required on iOS | No ad SDK initialises before CMP consent in the EEA and UK; no IDFA read before ATT; consent state flows into every ad request | [Reported, 2026-10] | 2027-03 |
| GAME-EU-08 | EU (PEGI) | PEGI: from 2026-06-01 new games with paid random items default to PEGI 16 (some 18); other new criteria reported: time limited offers PEGI 12, daily return rewards PEGI 7, NFTs PEGI 18. Whether existing games are reclassified from 2026-10-01 is [Contested]: some sources say existing titles keep their rating | Age rating answers and store rating texts change for games with paid random items; check the current PEGI criteria | [Reported, 2026-10] (single law firm source) | 2026-12 |
| GAME-TAX-01 | EU, Turkey | Selling digital goods to consumers on the web creates VAT duties per buyer country (EU OSS scheme; Turkey's VAT registration for foreign digital service providers). Stripe alone is not a merchant of record | Before the first web sale: register and remit, or sell through a merchant of record. Compliance and the human own the decision (with the accountant) and record it in `DECISIONS.md` | [Reported, 2026-10]; contract runbook | 2027-03 |
| GAME-BE-01 | Belgium | The Belgian Gaming Commission (2018) treats paid loot boxes as games of chance under gambling law; enforcement reported as weak | No paid random items sold in Belgium (the contract checker fails a random item when BE is in the regions) | [Reported, 2026-10] | 2027-06 |
| GAME-NL-01 | Netherlands | The Raad van State (2022, case 202005769) overturned the gambling authority's sanction against EA over FIFA packs; random prizes that can be traded for money remain a gambling law risk; no general loot box ban in force | Random items must not be tradeable or cash out; check for new legislation before launch | [Reported, 2026-10] | 2027-03 |
| GAME-DE-01 | Germany | USK ratings consider in-game purchases and random items as usage risks, with descriptors | Age rating answers include purchases and random items; the rating may rise | [Reported, 2026-10] | 2027-06 |
| GAME-UK-01 | UK | CAP enforcement notice (2026-02-26): app store listings for games with loot boxes (bought with real money or with currency that can only be bought) must disclose this prominently, for example "Contains loot boxes" or "Includes random-item purchases"; a generic "offers in-app purchases" is not enough; the publisher is responsible; active monitoring from 2026-05-26, then targeted enforcement | The UK listing text carries the label near the top; `app-store-optimization` places it, compliance approves the words | [Reported, 2026-10] | 2027-01 |
| GAME-UK-02 | UK | CAP guidance on advertising in-game purchases (2021): ads for games with loot boxes disclose them; costs not obscured; no direct exhortation to children. ASA rulings: Playrix (2020-09-30, rare and late mini games shown as the game, disclaimer did not cure), Top Games Evony (2024-04-03, real footage that did not convey the core experience), loot box disclosure rulings including Kabam and Hutch (2025-11) | Every UK ad passes the representativeness test in [Game ad creative](../../creative-strategy/references/game-ad-creative.md) and carries the loot box disclosure when the game sells random items | [Reported, 2026-10] | 2027-03 |
| GAME-UK-03 | UK | DCMS and Ukie industry principles on paid loot boxes (2023): technical controls so under 18s cannot buy without parental consent; odds disclosure; transparency | Spending controls for under 18s in the UK when random items are sold | [Reported, 2026-10] | 2027-06 |
| GAME-UK-04 | UK | DMCC Act 2024: CMA direct consumer enforcement since 2025-04-06 with fines up to 10% of global turnover; Schedule 20 banned practices include false urgency | Countdown offers must be real; see URG and PRICE rows in [Pricing, promotions and consumer law](pricing-promotions-and-consumer-law.md) | [Reported, 2026-10] | 2027-01 |
| GAME-US-01 | US | FTC v Epic (2022-12): USD 275 million COPPA penalty and USD 245 million in refunds over dark patterns (unwanted charges, confusing buttons, saved card charges without consent, locking accounts after chargebacks) | Confirmation before every charge; no account lock for disputing a charge (revoking the disputed entitlement is fine and logged); easy refunds path | [Reported, 2026-10] | 2027-06 |
| GAME-US-02 | US | FTC v Cognosphere (Genshin Impact, 2025-01): USD 20 million; no loot box sales to under 16s without parental consent; disclose odds and the real money cost (exchange rates) of virtual currency; COPPA violations | Under 16 purchase gate with parental consent for random items; real money price on currency items; odds in plain words | [Reported, 2026-10] | 2027-06 |
| GAME-US-03 | US | COPPA amended rule; compliance date for most provisions 2026-04-22 | If under 13s can play: neutral age screen, verifiable parental consent before personal data (including persistent identifiers used for ads), or no data and no personalized ads | [Reported, 2026-10]; see PRIV-KIDS-02 | 2026-12 |
| GAME-US-04 | US states | App store age laws: Texas SB 2420 enforceable after the Fifth Circuit stayed the injunction (2026-05 or 2026-06), Supreme Court review pending; Utah duties moved to 2027-05-06 | Read and honour the store's age category and parental consent signals where the law applies | [Reported, 2026-10] | 2026-12 |
| GAME-US-05 | US (New York) | New York Attorney General lawsuit (2026-02) against paid random items in Monopoly Go, described as a slot machine | Paid random items are a live litigation risk in the US, not only in Europe | [Reported, 2026-10] | 2027-01 |
| GAME-US-06 | US | Sweepstakes casino bans in several states (California from 2027-01); Google Ads requires social casino game certification (2025-04-14) | Social casino and sweepstakes mechanics go to the gambling pack and the human; never in a standard game review | [Reported, 2026-10] | 2027-01 |
| GAME-BR-01 | Brazil | Law 15.211/2025 (ECA Digital): paid loot boxes banned in games for children and adolescents; in force 2026-03 (16 or 17, sources differ); fines up to BRL 50 million or 10% of Brazil revenue. Apple's age rating table puts Brazil loot boxes at A18 | No paid random items for minors in Brazil; with an audience under 18, no paid random items in Brazil at all | [Reported, 2026-10]; Apple table [Official, 2026-10] | 2027-01 |
| GAME-AU-01 | Australia | Classification since 2024-09-22: games with paid chance based loot boxes rated at least M; simulated gambling R 18+. Apple: loot boxes plus social features rate 16+ in Australia | Age rating answers per storefront; simulated gambling is a different, stricter category | [Reported, 2026-10]; Apple [Official, 2026-10] | 2027-06 |
| GAME-CN-01 | China | Odds disclosure for random items required (since 2017) | Odds screen per item; publishing licences are out of scope for this pack | [Reported, 2026-10] | 2027-06 |
| GAME-TR-01 | Turkey | Law 7578 (Official Gazette 2026-05-01, the issue number differs between sources) amends Internet Law 5651: games must carry an age rating (unrated games default to the highest age class); game platforms must offer parental controls, including parental approval of monetary transactions; foreign platforms with more than 100,000 daily visits from Türkiye appoint a local representative; administrative fines (reported TRY 1 to 10 million, up to 30 million) and bandwidth throttling; under 15 social media restrictions; secondary regulation by BTK pending, most duties about 6 months after publication | For Turkish players under 18: an age rating and parental approval of purchases where the regulation requires; track the 100,000 daily visits threshold; recheck when BTK publishes rules | [Reported, 2026-10] | 2026-11 |
| GAME-TR-02 | Turkey | Commercial advertising regulation as amended (in force 2026-08-01): no profiling based targeted ads to children (Art 25/A); influencer labels; AI disclosure | No personalized ads to known or likely children in Turkey; see PRIV-TR-03 and [Country notes](country-notes.md) | [Reported, 2026-10] | 2027-03 |

## 3. Platform rules

| Rule ID | Platform | Rule | Label | Recheck by |
|---------|----------|------|-------|------------|
| GAME-APPLE-01 | Apple | 3.1.1: "Apps offering 'loot boxes' or other mechanisms that provide randomized virtual items for purchase must disclose the odds of receiving each type of item to customers prior to purchase." | [Official, 2026-06] | Each guideline update |
| GAME-APPLE-02 | Apple | 3.1.1: digital unlocks use In-App Purchase. 3.1.1(a): link entitlements "are not required for developers to include buttons, external links, or other calls to action in their United States storefront apps"; other storefronts allow links only under specific entitlements. 3.1.3(b): items bought on other platforms may be used in the app "provided those items are also available as in-app purchases within the app" | [Official, 2026-06]; the US link out commission is under litigation (Epic v Apple, Supreme Court review) [Reported, 2026-10] | 2026-12 |
| GAME-APPLE-03 | Apple | Age rating questionnaire covers loot boxes, simulated gambling and (required since 2026-09) social media capabilities; tiers 4+, 9+, 13+, 16+, 18+; loot boxes start at 9+ with storefront overrides (Australia 16+ with social features, Brazil A18) | [Official, 2026-10] (Apple age rating pages read in research) | 2027-01 |
| GAME-APPLE-04 | Apple | Kids Category: no third party analytics or advertising; parental gate before links out and purchases (1.3, 5.1.4) | [Official, 2026-10] (read in research) | 2027-01 |
| GAME-GP-01 | Google Play | Odds of randomized items disclosed before purchase, close to the purchase point | [Reported, 2026-10] | 2027-01 |
| GAME-GP-02 | Google Play | Families policy: when children are in the target audience, only self certified ad SDKs, child directed treatment, restricted ad content | [Official, 2026-10] (Play policy hub read in research) | 2027-01 |
| GAME-ADS-01 | Ad platforms | Misrepresentation policies (Meta, Google, TikTok) reject ads that do not show the product honestly; Google requires certification for social casino games | [Reported, 2026-10]; see [Platform ad policies](platform-ad-policies.md) | Each quarter |

## 4. Never do

| # | Never | Rule IDs |
|---|-------|----------|
| N1 | Sell a virtual item without its real money price visible at the point of purchase | GAME-EU-01, GAME-US-02 |
| N2 | Size currency packs so players must buy more than they need, or hide the total cost of an item behind several currencies | GAME-EU-01 |
| N3 | Countdown, scarcity or "only now" pressure in offers that can reach minors; any direct "buy" appeal to children | GAME-EU-03, GAME-EU-04, GAME-UK-02, GAME-UK-04 |
| N4 | Hidden, missing, vague or exaggerated odds on random items | GAME-APPLE-01, GAME-GP-01, GAME-CN-01, GAME-US-02 |
| N5 | Paid random items to minors in Brazil, in Belgium at all, or tradeable random prizes with cash value in the Netherlands | GAME-BR-01, GAME-BE-01, GAME-NL-01 |
| N6 | One tap charges, charges on a saved card without express consent, or locking an account because the player disputed a charge | GAME-US-01 |
| N7 | Ads that show gameplay other than the core loop a new player gets; disclaimers as the cure | GAME-UK-02, GAME-ADS-01 |
| N8 | Initialise an ad SDK or read the IDFA before consent and ATT | GAME-EU-07 |
| N9 | Collect personal data, including identifiers for ads, from under 13s without verifiable parental consent | GAME-US-03 |
| N10 | Prizes with real money value, or real money gambling imagery, without the gambling pack and a licence | GAME-US-06, [Regulated categories](regulated-categories.md) |
| N11 | "No ads" or "ad free" in any ad or listing while ads run for any player | GAME-UK-02 (misleading claim), [Game ad creative](../../creative-strategy/references/game-ad-creative.md) |
| N12 | Penalties for absence, guilt or loss framing ("your crops will die"), mid session pop up offers that block play, opaque currencies. The German consumer federation (VZBV) objected to Monopoly Go on these grounds (2025-06) [Reported, 2026-10] | GAME-EU-01, GAME-EU-04 |
| N13 | Sell or reward anything that changes a ranked or competitive result, including a streak freeze on a streak shown competitively | Contract fairness rule (not law); route to `game-monetization` |

## 5. Must have

| # | Must have | Rule IDs |
|---|-----------|----------|
| M1 | Real money price next to every virtual item and currency pack; real money equivalent shown where an item is priced in currency | GAME-EU-01, GAME-US-02 |
| M2 | Odds screen before purchase for every random item; UK listing label; UK ad disclosure | GAME-APPLE-01, GAME-GP-01, GAME-UK-01, GAME-UK-02 |
| M3 | Accurate age rating answers: Apple questionnaire (including social media), IARC on Play, PEGI or USK where they apply | GAME-APPLE-03, GAME-EU-08, GAME-DE-01, GAME-AU-01 |
| M4 | Spending controls for minors where law or precedent asks: parental consent for random items under 16 (US), under 18 controls (UK principles), parental purchase approval (Turkey) | GAME-US-02, GAME-UK-03, GAME-TR-01 |
| M5 | COPPA handling when under 13s may play | GAME-US-03 |
| M6 | Store age signals honoured where state laws apply | GAME-US-04 |
| M7 | A Brazil minor gate for paid random items, or no paid random items | GAME-BR-01 |
| M8 | Turkey: rating, parental approval flow, local representative threshold monitored | GAME-TR-01 |
| M9 | EU web checkout: withdrawal information, express consent and acknowledgement, confirmation | GAME-EU-06 |
| M10 | A refund and dispute path that does not punish the player; refunds revoke the entitlement and are logged | GAME-US-01; contract runbook |
| M11 | CMP before ad SDKs in the EEA and UK; ATT before IDFA on iOS | GAME-EU-07 |
| M12 | An SDK data map that matches App Privacy and Data safety answers | GAME-APPLE-03, `store-submission` |
| M13 | A representativeness test attached to every game ad | GAME-UK-02 |
| M14 | A recorded VAT and merchant of record decision before the first web sale | GAME-TAX-01 |

## 6. Feature by market matrix (summary; verdicts still cite the rows)

| Feature | EU general | Belgium | Netherlands | UK | US | Brazil | Australia | Turkey |
|---------|-----------|---------|-------------|----|----|--------|-----------|--------|
| Virtual currency sales | Real money price shown; no forced leftovers | Same | Same | Same plus DMCC | Real money cost shown (Genshin order as the model) | Same as EU as a baseline | Same as EU as a baseline | Parental approval for minors' purchases |
| Paid random items | Odds; under 18 caution (DSA guidelines); PEGI 16 default | No | Only if not tradeable for value | Odds, listing label, ad disclosure, under 18 controls | Odds; under 16 parental consent; litigation risk | Not for minors | Rated M or higher | Rating rises; parental approval |
| Countdown or scarcity offers | Only if true; never aimed at minors | Same | Same | True deadlines only (DMCC) | Truthful; FTC dark patterns lens | Same | Same | Same |
| Personalized ads | Consent first; none to minors on platforms | Same | Same | Consent first | Not to under 13s without parental consent | Minors protected | Consent rules vary | No profiling ads to children |
| Link out to web purchase from an iOS app | Only under Apple's EU terms and entitlements | Same | Same | Entitlement regions only | Allowed on the US storefront; fee under litigation | Entitlement rules | Entitlement rules | Entitlement rules |

## 7. Reviewing a monetization-policy.json

The Game Monetization Contract v0.2 (`skills/game-monetization/references/monetization-contract.md`) defines one policy file per product (a store listing or a web app that may hold several games; mode ids may be namespaced such as `wordgame:daily`). Offer points are snake_case (`on_fail`, `on_attempts_exhausted`, `custom_*`); grants are typed (`cosmetic`, `access`, `pass`, `round`, `attempt`, `moves`, `time`, `booster`, `currency`, `lives`, `streak_protection`, with `writesTo` boards); ranked modes declare boards with scope `group` or `everyone`; prices are integers in minor units; stores are declared in the file. Nothing about fairness is self declared: the checker derives it.

### 7.1 Procedure

1. Read the contract version the product implements and the policy revision under review. A new revision needs a new review; reviews cite the revision number.
2. Run the checker from the repo root (or `.claude/skills/...` in a project install):

```bash
python3 skills/game-monetization/scripts/monetization_check.py ads-master/data/monetization-policy.json
```

Exit 0 pass, 1 fail, 2 could not run (unreadable file or unsupported contract version). The last line states what the check cannot cover. When `monetization_conformance.py` is present in the same folder, run it too: it checks the policy against the tracking plan, the store product ids and the store declarations.
3. A FAIL goes back to `game-monetization` before any legal review: compliance does not approve a policy the checker fails.
4. On PASS, review what the checker cannot see (7.2), run the bundle arithmetic (7.3), the web sales checks (7.4) and the declarations cross check (7.5).
5. Write the verdict per market with the template in 7.6.

### 7.2 What the checker catches and what compliance must still judge

| Checker finding family | Rule IDs behind it | Fix owner |
|------------------------|--------------------|-----------|
| Purchasable virtual currency without the real money price shown | GAME-EU-01, GAME-US-02 | game-monetization |
| Random item without odds, odds not summing to 1, loot boxes not declared | GAME-APPLE-01, GAME-GP-01, GAME-UK-01 | game-monetization, app-store-optimization (label) |
| Random paid item with an audience under 18, or sold in Belgium | GAME-BR-01, GAME-EU-04, GAME-US-02, GAME-BE-01 | game-monetization, human |
| Price escalation, including escalation by sibling offers at the same moment | GAME-EU-01 (hidden cost), GAME-UK-04 (pressure) | game-monetization |
| Countdown copy with minors in the audience | GAME-EU-03, GAME-EU-04, GAME-UK-02 | game-monetization |
| Ads without consent required first | GAME-EU-07 | game-monetization, measurement |
| Store declarations disagree with the file (ads, purchases) | GAME-APPLE-03, Play ads declaration | store-submission |
| Interstitial or app open ads in kids mode | GAME-APPLE-04, GAME-GP-02 | game-monetization |
| Ranked mode grants that change play, rounds written to boards wider than the receivers | Contract fairness rule | game-monetization (compliance reviews only fairness claims in copy, such as "no pay to win") |

Compliance still judges by hand: the purchase and odds screens (wording, placement, prominence, language per market); the bundle sizes against item prices (7.3); age assurance and parental approval flows; the refund and dispute path; what the store consoles actually say compared with the file; every ad and store text; the reward wording on rewarded ads; tax and merchant of record (7.4); and any law that changed after the file was written.

### 7.3 Bundle arithmetic (the forced leftover check)

For each item priced in a virtual currency:
1. List the currency packs and their real money prices.
2. Find the cheapest combination of packs that covers the item for a player with zero balance.
3. Leftover = currency bought minus item price. Leftover share = leftover / item price.
4. Flag for review when the leftover share is above 50% or when the cheapest path needs more than one pack purchase (house thresholds; the CPC principles name the practice, not a number).
5. Real money equivalent of the item = item price x (pack price / pack size) of the cheapest pack the player can buy; this is the number shown next to the item under M1.

Worked example (placeholder prices): moves cost 900 coins; packs are 1,000 coins for 199 cents and 5,500 coins for 999 cents. Zero balance: one small pack covers it, leftover 100 coins (11%): no flag; real money equivalent 900 x 199 / 1,000 = 179 cents. If moves cost 1,100 coins, the player needs two small packs (2,000 coins for 398 cents), leftover 900 (82%) and two purchases: flag, and ask `game-monetization` to add a pack size or reprice.

### 7.4 Web sales checks

| Check | Rule | Pass condition |
|-------|------|----------------|
| VAT and merchant of record | GAME-TAX-01 | A written decision: registered for EU OSS and Turkish VAT where needed, or a merchant of record sells; the decision date and owner recorded in `DECISIONS.md` |
| Withdrawal | GAME-EU-06 | Checkout shows the withdrawal information, collects express consent and acknowledgement before access starts, and the receipt confirms it |
| Price display | GAME-EU-01 | Final price with taxes for consumers; currency of the buyer's market where sold |
| Minors | GAME-US-02, GAME-TR-01 | Same parental approval rules as in the store builds |
| Store parity | GAME-APPLE-02 | Items usable in the iOS app are also available as In-App Purchases (3.1.3(b)); US link outs only where allowed |

### 7.5 Declarations cross check

| Policy file says | Must match | Owner |
|------------------|-----------|-------|
| Ads present | Play "Contains ads" declaration; Apple App Privacy answers for ad SDK data; age rating answers | store-submission |
| Purchases present | Store in-app purchase setup; IARC and Apple questionnaire answers on purchases | store-submission |
| Random items present | Apple loot box answer; IARC random items answer; UK listing label; odds screens in every store build | store-submission, app-store-optimization |
| Audience minimum age, kids mode | Age rating tier; Families or Kids Category choice; ad SDK certification | store-submission, game-monetization |
| Regions | Storefront availability; Belgium excluded when random items exist; Brazil and Turkey minors flows | store-submission |

### 7.6 Verdict template for a policy revision

```
# Compliance review: <product> policy revision <n> (contract <version>), <date>
Checker: monetization_check.py exit <0|1|2>; conformance: <exit or not present>
Markets: <codes>. Audience: minimum age <n>, kids mode <yes|no>, unknown age handling <...>
| # | Element (sku, offer, placement, screen, text) | Market | Verdict | Rule ID | Source and date | Edit or action |
Bundle arithmetic: <items flagged, leftover shares>
Web sales: VAT and MoR decision <reference>; withdrawal flow <checked or not>
Declarations: <matches or gaps per store>
Needs human or legal review: <questions, owner, deadline>
Asset verdict per market: <...>
```

## 8. Game ads and store text

- Every ad: the representativeness test from [Game ad creative](../../creative-strategy/references/game-ad-creative.md), the loot box disclosure for UK ads when random items are sold, no "No ads" claim while ads run, no direct exhortation to children, no invented statistics. Verdict cites GAME-UK-02 or GAME-ADS-01.
- Playables: the same rules apply to the playable file; it must play the game's own rule ([Playable ads and game trailers](../../video-studio/references/playable-ads-and-game-trailers.md)).
- Store listings: UK loot box label (GAME-UK-01), "free" with in-app purchases disclosed (GAME-EU-03), age rating text consistent with the questionnaire.
- Push and in-app messages: no absence penalties, no countdowns to minors, no guilt framing (N3, N12); see the game notifications module in `lifecycle-crm`.

## 9. Minors and age assurance

| Situation | Minimum handling | Rule IDs |
|-----------|------------------|----------|
| Audience may include under 13s | Neutral age screen; no personalized ads; parental consent before personal data, or no data | GAME-US-03, GAME-GP-02, GAME-APPLE-04 |
| Under 16 with purchases of random items (US) | Parental consent before purchase | GAME-US-02 |
| Under 18 in the UK with random items | Spending controls with parental consent | GAME-UK-03 |
| Under 18 in Turkey | Parental approval of purchases where BTK rules require; age rating shown | GAME-TR-01 |
| Under 18 in Brazil | No paid random items | GAME-BR-01 |
| Age unknown | Treat as the youngest bracket the product allows in markets that require age handling; never default to adult for purchase gates | Contract runbook, minors |
| Store age signals available (Texas, later Utah) | Read and honour them; log the signal used | GAME-US-04 |

## 10. Escalation: always NEEDS HUMAN OR LEGAL REVIEW

1. Any paid random item, in any market.
2. Any audience that includes minors and has purchases or ads.
3. First sale in Belgium, the Netherlands, Brazil or Turkey.
4. Social casino, sweepstakes, prizes, tournaments with entry fees or cash rewards.
5. The first web sale (VAT and merchant of record decision).
6. Payment rails outside the main stores and Stripe (Discord, Telegram Stars, portal payments) until a rule row exists.
7. Any row in this pack whose "Recheck by" date has passed.
8. A regulator letter, a store rejection on monetization grounds, or a consumer group complaint.

## 11. Freshness watch list

| Item | Why it moves | Check |
|------|--------------|-------|
| Digital Fairness Act proposal | Expected Q4 2026 | Commission press corner; update GAME-EU-05 |
| CPC action outcomes | Commitments or national enforcement after 2026-09-30 | Commission consumer enforcement pages |
| UK ASA loot box enforcement after 2026-05-26 | First rulings under the notice | ASA rulings list |
| PEGI reclassification | Started 2026-10-01 | PEGI site |
| Turkey BTK secondary regulation | Duties start about 6 months after publication | Resmi Gazete, BTK |
| Texas and Utah app store acts | Supreme Court and effective dates | Court dockets, store developer notices |
| Epic v Apple link out commission | Supreme Court review agreed 2026-06-30 | Apple developer news, court docket |
| Apple guidelines | Updated several times a year (last read 2026-06-08 version) | developer.apple.com/app-store/review/guidelines |

## Sources for this pack

| Source | Date | Supports | Label |
|--------|------|----------|-------|
| Apple App Review Guidelines 3.1.1, 3.1.1(a), 3.1.3(b) (developer.apple.com) | 2026-06-08, read 2026-10-12 | GAME-APPLE-01, GAME-APPLE-02 | [Official, 2026-06] |
| Apple age ratings values and Kids Category pages (read in research note 05 and 09) | 2026-10 | GAME-APPLE-03, GAME-APPLE-04 | [Official, 2026-10] |
| Google Play policy hub, Families (read in research note 10) | 2026-10 | GAME-GP-02 | [Official, 2026-10] |
| Mondaq, Baker McKenzie, Reed Smith on the CPC key principles; PocketGamer.biz, Gaming.net, LexisNexis on the 2026-09-30 action | 2025-03 to 2026-10 | GAME-EU-01, GAME-EU-02 | [Reported, 2026-10] |
| Osborne Clarke on the DSA minors guidelines; digitalfairnessact.com; Lewis Silkin DFA consultation 2026-01-14 | 2025-07 to 2026-10 | GAME-EU-04, GAME-EU-05 | [Reported, 2026-10] |
| Lewis Silkin on PEGI changes | 2026-03-18 | GAME-EU-08 | [Reported, 2026-10] |
| Usercentrics on CNIL and Voodoo; AGCM on Apple ATT | 2023, 2025-12 | GAME-EU-07 | [Reported, 2026-10] |
| SBC News on EA and KSA; Raad van State ruling 202005769 | 2022 | GAME-NL-01 | [Reported, 2026-10] |
| Lewis Silkin, Mondaq and the ASA notice PDF on loot box disclosure in app stores | 2026-02-26 to 2026-02-27 | GAME-UK-01 | [Reported, 2026-10] |
| CMS on the loot box principles; Mishcon on Evony; PocketGamer.biz on Playrix | 2020 to 2024 | GAME-UK-02, GAME-UK-03 | [Reported, 2026-10] |
| Hunton on FTC v Epic; FTC blog on Genshin Impact (2025-01) | 2022-12, 2025-01 | GAME-US-01, GAME-US-02 | [Reported, 2026-10] |
| White and Case on COPPA; Pearl Cohen on Texas; FKKS on Utah; FPF on app store acts | 2025 to 2026 | GAME-US-03, GAME-US-04 | [Reported, 2026-10] |
| Demarest on ECA Digital (Law 15.211) | 2025 to 2026 | GAME-BR-01 | [Reported, 2026-10] |
| infrastructure.gov.au classification guidelines | 2024-09 | GAME-AU-01 | [Reported, 2026-10] |
| Mondaq, Gün + Partners, PILC on Law 7578 and Law 5651 amendments | 2026-05 to 2026-09 | GAME-TR-01 | [Reported, 2026-10] |
| Research note 06 (regulation), note 07 (teardowns: VZBV and Monopoly Go) | 2026-10-12 | Never and must lists, N12 | [Reported, 2026-10] |
