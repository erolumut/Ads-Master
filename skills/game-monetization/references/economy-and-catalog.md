# Economy and Catalog

> Knowledge as of 2026-10 (research pass 2026-10-12). Every number here came from search summaries or vendor material: the strongest label is [Reported, 2026-10] and most are [Unverified]. Prices in examples are placeholders, never pricing decisions. Price points and ladders are set with `pricing-strategy` (its `iap-price-points` reference); this module owns the structure they plug into.

## 1. What this module owns and what it does not

| Owns | Does not own |
|------|--------------|
| Which currencies exist, whether they can be bought, and what they buy | Level design, difficulty, drop rates inside levels (the game repo) |
| The sources and sinks sheet: what a typical player earns and spends per active day | Price levels per country (pricing-strategy) |
| The catalog: one canonical SKU per product with typed grants and store ids | Store console setup and submission (store-submission, the human) |
| The shape of the price ladder (how many rungs, what each rung is for) | Claims on the offer screen (compliance) |
| Keeping `GAME_ECONOMY.md` and `data/monetization-policy.json` in sync | KPI definitions (measurement, `game-kpis`) |

The policy file is the executable twin of the economy. If the sheet and the file disagree, the file is what the game runs, so fix the sheet or raise `policyRevision` with a change request ([Monetization contract](monetization-contract.md) section 8).

## 2. Economy primitives

| Primitive | Contract grant kind | Earns its place when | Main risk | Default |
|-----------|--------------------|----------------------|-----------|---------|
| Real money only (no virtual currency) | none | The product sells few items (a pass, a subscription, a group round, cosmetics) | None structural; simplest to explain | Default for daily social and ranked products |
| One soft currency (coins) | `currency` | Many small sinks (continues, boosters, cosmetics) in a progression game | Inflation when sources outgrow sinks; opacity if prices are shown only in coins | Default for level based progression games [Reported, 2026-10] |
| A second, premium currency | `currency` | Rarely; large live service economies | Opaque pricing (an EU CPC principle concern), double conversion | Avoid unless a written reason exists |
| Boosters and power ups | `booster` | Progression games where a booster solves a specific obstacle | Selling difficulty; tuning difficulty for sales is game design and stays in the game repo | Progression only |
| Moves, time | `moves`, `time` | A level failed by a small margin in progression | Escalating prices per retry | Progression only, `maxPerAttempt`, fixed price |
| Lives or energy | `lives` | Only when the game repo decides a session pacing rule exists | Gating play, pressure to pay to continue | Not a default; the contract has no lives primitive by design |
| Cosmetics | `cosmetic` | Any game with identity (frames, themes, avatars, group themes) | Low revenue alone | Safe in every mode |
| Access (archive, stats, practice, replay) | `access` | Daily or content games with a back catalog | None if the free game stays complete | Safe in every mode |
| Passes (season pass, plus subscription) | `pass` | A season or content cadence exists (`game-liveops`) | Selling a track whose rewards change ranked results | Safe when the track grants only cosmetic, access or progression items |
| Group rounds | `round` | A group plays together (the Encore pattern) | Writing to a board wider than who receives the round | Social mode, group boards only |

Source for the soft currency default and the single currency feeding all sinks: monetization design snippets from Naavik, Unity and Supersonic [Reported, 2026-10]. The two currency warning rests on the EU CPC key principles on in-game virtual currencies (2025-03-21) [Reported, 2026-10].

## 3. Currency rules (non-negotiable)

1. Every purchasable virtual currency shows its real money price next to every virtual price at the point of purchase (`showRealMoneyPrice: true`; `monetization_check.py` fails without it). Basis: EU CPC key principles 2025-03-21 [Reported, 2026-10].
2. No forced leftovers: currency packs and item prices are sized so a player can buy what they came for without being pushed to buy more currency than they need (the CPC principles name "awkward bundle sizes" and forced currency purchases) [Reported, 2026-10].
3. No currency in ranked modes: currency is play changing in the contract, so it never appears as a grant in a ranked mode offer or placement.
4. One conversion step at most: real money to currency to item. Never real money to premium currency to soft currency to item.
5. Earned and bought currency behave the same and are spent in a stated order; refunds claw back the bought part first (see [Segmentation and payment ops](segmentation-and-payment-ops.md) section 8).
6. Currency never expires silently. If a balance can expire (season currency), the date is shown from the moment it is earned.
7. Currency has no value outside the game and cannot be cashed out or traded for money (also a condition of Google's H5 Games Ads rewarded rules for web games [Reported, 2026-10]).

## 4. The sources and sinks sheet

The sheet answers one question: what does a typical non payer earn and spend in an active day, and how long until they can afford the things the game wants them to want? It lives in `ads-master/GAME_ECONOMY.md` (template from `ads-setup`).

### 4.1 Build it

1. List every source (level rewards, daily bonus, rewarded ad, event chests, pass track, gifts) with the amount per occurrence and occurrences per active day for three players: light (P25 of sessions), typical (median) and engaged (P75). Occurrences come from the game's own analytics export, read with measurement's definitions.
2. List every sink (continues, boosters, cosmetics, entries) with price and uses per active day for the same three players.
3. Compute per player type:

| Quantity | Formula |
|----------|---------|
| Daily net flow | sum of sources per day minus sum of sinks per day |
| Days to afford item X with free sources only | price of X / free daily source |
| Stockpile after N days | starting balance + N x daily net flow |
| Share of sinks covered by free sources | free sources / sinks |
| Rewarded share of sources | rewarded ad currency / all currency sources |

4. Read the stockpile distribution from data every month (P50, P90, P99 balances). A rising P50 balance with flat spend means sources outgrow sinks (inflation); offers lose value and the next price change gets harder.

### 4.2 Illustrative row set (placeholder numbers, not benchmarks)

| Flow | Item | Typical player per active day | Notes |
|------|------|-------------------------------|-------|
| Source | Level win reward | 6 wins x 50 coins = 300 | From the level funnel export |
| Source | Rewarded double coins | 2 x 50 = 100 | Capped at 5 per day in the policy |
| Source | Daily bonus | 100 | Same for everyone |
| Sink | Extra moves after a fail | 0.4 x 900 = 360 | Fixed price, max 2 per attempt |
| Sink | Booster before a level | 0.2 x 500 = 100 | Progression only |
| Net | | 300 + 100 + 100 minus 460 = +40 | Slow accumulation: a 2,000 coin item takes 50 active days for free |

The illustration uses the `progression-policy.json` sample shape (900 coins for 5 moves). Replace every value with the game's own data before any decision.

### 4.3 What the sheet must never be used for

It does not tune level difficulty. When the sheet shows that a level is the main sink driver (for example most continues are bought on one level), that is a finding for the game repo through `game-liveops` (difficulty flags), never a change Ads Master makes or requests as a revenue lever.

## 5. The catalog

### 5.1 One canonical SKU per product

Each catalog item in the policy file carries (contract section 5):

| Field | Rule |
|-------|------|
| `sku` | Store neutral, snake_case, stable for life. Never encode a price or a store in it (`coins_small`, not `coins_199_ios`). Never reuse a retired SKU id for different grants. |
| `kind` | `consumable`, `non_consumable`, `subscription` or `season` |
| `grants` | Typed grants only (section 2); a mixed bundle lists every grant |
| `basePrice` | `{currency, minor}` in integer minor units, never floats (`monetization_check.py` fails 2.99) |
| `platformPrices` | Per store, per currency, minor units, when a store price tier differs from the base |
| `storeProductIds` | One id per store id declared in `stores` (web Stripe price id, Apple product id, Play product id); `monetization_check.py` fails a missing one |
| `stores` | Optional: limit an item to some stores (for example a web only bundle) |
| `period`, `trialDays` | Subscriptions only (`P1M`, `P1Y`) |
| `random`, `odds` | Random items only; odds sum to 1 and are shown before purchase (section 7) |
| `priceInVirtual` | When the item can also be bought with currency |

### 5.2 Store product id conventions

| Store | Convention that survives migrations | Watch |
|-------|-------------------------------------|-------|
| Web (Stripe) | One Price object per SKU per currency; the policy stores the price id | A new price is a new id; update the policy and raise `policyRevision` |
| Apple | Reverse domain style (`<product>.<sku>`) | Product ids cannot be reused after deletion [Unverified]; never delete one to rename it; IAP must be attached to the version under review (Guideline 2.1(b)) [Official, 2026-10] |
| Google Play | snake_case equal to the SKU where possible | Billing Library 8 or later was required by 2026-08-31 (extension to 2026-11-01 possible) [Official, 2026-10] |

### 5.3 Catalog hygiene checks

1. Every item sold in a store has that store's product id (`monetization_check.py`).
2. Every item has `purchase_completed` and `purchase_refunded` coverage in the tracking plan (`monetization_conformance.py`).
3. Every item's grants are legal in every mode its offers use (`monetization_check.py`).
4. Items sold on several platforms are also sold as IAP inside iOS when they unlock content there (Guideline 3.1.3(b) multiplatform services) [Official, 2026-10]; route the details to `store-submission`.
5. Retired items stay in the catalog with no offers until every entitlement they granted has expired or been honored; deleting them breaks refund handling.

## 6. Price ladder shape

There is no public, sourced price ladder for games: the 2026-10-12 pass found none [Reported, 2026-10]. So the ladder is designed by role and tested, and `pricing-strategy` sets the numbers.

| Rung | Role | Typical content | Rules |
|------|------|-----------------|-------|
| Entry | First purchase, low risk | Starter pack, small currency pack, a group round | One time or capped; honest content value; never the only rung |
| Core | Repeat purchase | Mid currency pack, booster bundle, season pass | The rung most players who pay buy again |
| Value | Better unit price for committed players | Large pack, annual subscription | Unit price shown so the comparison is real; "best value" only when the math says so (compliance) |
| Remove ads | Permanent comfort | Ad removal, often bundled | Name exactly what is removed (see [Offers](offers-and-fail-moments.md) section 10) |

Rules for every ladder:
- Prices come from store price tiers per country; regional prices follow `pricing-strategy` and the store's own tier tables, never a manual currency conversion.
- The web shop and the stores sell the same SKU with the same grants; any web price difference is a decision with a reason (fees, tax) and a compliance check on how it is shown.
- A price change is a G3 change request, raises `policyRevision` and gets an `EXPERIMENTS.md` row.
- EU reference price rules apply to any "was" or "save" claim on an offer (30 day prior price; Turkey 10 days) through `compliance`.

## 7. Random items

Default: none. When a game repo wants a random paid item anyway:

| Requirement | Basis | Checked by |
|-------------|-------|------------|
| Odds shown before purchase | Apple Guideline 3.1.1 [Official, 2026-10]; Google Play policy [Reported, 2026-10] | `monetization_check.py` (odds present and sum to 1); the screen itself by `store-submission` |
| "Contains loot boxes" in UK store listings, prominently | ASA and CAP enforcement notice 2026-02-26, monitoring from 2026-05-26 [Reported, 2026-10] | `storeDeclarations.lootBoxes`, `monetization_conformance.py` against the store declarations file |
| No paid random items for minors | Brazil Law 15.211/2025 (in force 2026-03) [Reported, 2026-10]; EU DSA Art. 28 guidelines (non binding) [Reported, 2026-10] | `monetization_check.py` fails random items with an audience under 18 |
| Not sold in Belgium | Belgian gambling regulator position since 2018 [Reported, 2026-10] | `monetization_check.py` fails BE in regions |
| No tradeable prizes in the Netherlands | Raad van State 2022 ruling [Reported, 2026-10] | Human and compliance |
| Age rating impact | PEGI: new games with paid random items default to PEGI 16 from 2026-06-01 [Reported, 2026-10]; Apple lists loot boxes in its age rating values [Official, 2026-10] | `store-submission` |

## 8. Default stacks by game type

These are starting structures, not targets. Each becomes a policy file draft checked by both scripts before anyone discusses prices.

| Game type | Currencies | Catalog | Ads | Never |
|-----------|-----------|---------|-----|-------|
| Daily social or ranked (tries count toward boards) | None | Season pass, plus subscription (archive, stats, unlimited uncounted replay, no ads), group round (Encore), cosmetics, group themes | Optional rewarded for uncounted replay only | A paid or earned counted try |
| Level based progression puzzle | One soft currency with a free path | Coin ladder, starter pack, boosters, extra moves or time after a fail, piggy bank, ad removal, pass later | Rewarded continue and multiplier capped daily; interstitial at level end with grace, cooldown, session cap and reset after rewarded | Lives gating play, escalating continues |
| Hybrid casual | One soft currency | Boosters, no ads bundle, starter pack | Rewarded plus interstitials held back early | Interstitial after every level stacked with rewarded |
| Ads only casual | None or cosmetic only | Remove ads | Rewarded first, interstitials with strict caps, banners in menus only | Banners in play |
| Web portal game | None | Usually none (portal rules) | Portal SDK ads | Ads outside the portal SDK where exclusivity applies |

Sources for the progression and hybrid stacks: the default stack synthesis in the 2026-10-12 monetization notes (Naavik, Unity, Supersonic, Deconstructor of Fun, maf.ad) [Reported, 2026-10]; the refusals come from the teardown notes (section "Do not copy") [Reported, 2026-10].

## 9. Economy change protocol

1. Draft the change in a copy of the policy file; raise `policyRevision`.
2. Run `monetization_check.py` and `monetization_conformance.py`; both must pass.
3. Update `GAME_ECONOMY.md` (table rows and change log).
4. Write the `EXPERIMENTS.md` row: hypothesis, primary metric (usually ARPDAU or revenue per shown offer), guard rails (D1, D7, refund rate, complaint rate), stop rule, minimum 7 days.
5. Change request (G3) with the snapshot of the live config, the rollback (previous policy revision) and the read date.
6. After approval the human or the release pipeline ships it; read results by `policy_revision` ([Benchmarks and reading results](benchmarks-and-reading-results.md) section 7).

## 10. GAME_ECONOMY.md to policy file mapping

| GAME_ECONOMY.md table | Policy file key | Kept in sync by |
|-----------------------|-----------------|-----------------|
| Currencies | `currencies.virtual` | This agent, every change |
| Sources and sinks | Not in the policy (analysis) | Monthly economy review |
| Catalog | `catalog` | This agent; pricing-strategy for prices |
| Offer points | `offers` | This agent |
| Ad placements | `placements` | This agent |
| Fairness | `modes` (ranked boards, `countedAttemptsPerDay`) | The human decides; the checker enforces |
| Change log | `policyRevision` | Every change |

## 11. Quick checklist

- [ ] Every currency purchasable only in progression modes and shows its real money price.
- [ ] Sources and sinks sheet built from the game's own data for light, typical and engaged players.
- [ ] Monthly stockpile percentiles read; inflation flagged.
- [ ] Every SKU store neutral, typed grants, integer minor unit prices, every store id present.
- [ ] Ladder rungs have a role; prices from pricing-strategy; no "best value" without math.
- [ ] No random paid items, or every requirement in section 7 met.
- [ ] Policy file and GAME_ECONOMY.md agree; both scripts pass.
