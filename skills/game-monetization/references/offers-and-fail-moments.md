# Offers and Fail Moments

> Knowledge as of 2026-10 (research pass 2026-10-12). Teardown facts about named games come from search summaries and vendor teardowns ([Reported, 2026-10] at best, often [Unverified]); they show what exists in the market, not what we copy. The fairness rules come from the [Monetization contract](monetization-contract.md) and are checked by `monetization_check.py`. Game design (what a level asks, how hard it is) belongs to the game repo; this module decides only what may be sold or shown, where, and on what terms.

## 1. The rule that decides everything

**Ranked results are never purchasable.** A ranked mode declares a constant number of counted attempts per player per day on every board it writes to; no purchase, ad or reward changes it. In a ranked mode only cosmetics, access (practice, archive, stats), passes, and a `round` received by the whole group (written only to boards no wider than that group) may be sold or earned.

**Progression mode may sell play.** In single player level progress, boosters before a level and extra moves or extra time after a fail are legitimate, the way Royal Match sells "+5 moves" and pre level boosters [Reported, 2026-10]. Each such offer has a fixed price shown before purchase, a limit per attempt, no escalation inside one attempt (not by the same offer and not by sibling offers at the same moment) and never writes to a ranked board.

The house default for daily ranked games: no paid and no earned counted tries. Level based progression games selling boosters, extra moves and extra time are welcome under the progression rule.

| Mode | Sell or reward | Never |
|------|----------------|-------|
| `ranked` | `cosmetic`, `access`, `pass` | `attempt`, `moves`, `time`, `booster`, `currency`, `lives`, `streak_protection`; any write to a ranked board except a group `round` |
| `practice` | Anything that does not write to a ranked board | A write to a ranked board |
| `social` | A `round` for the group or everyone, written to boards no wider than who receives it | A benefit only the buyer receives in a competitive context |
| `progression` | Boosters, moves, time, currency, lives, passes | Escalating continue prices, hidden odds, countdown pressure aimed at minors, any write to a ranked board |

Derived boards count: a streak board or a season table fed by ranked play is ranked. A streak freeze (`streak_protection`) is play changing when the streak is shown competitively, so the product decides and declares the streak board before selling or rewarding one.

## 2. Offer point map

Offer points come from the contract's `OfferPoint` list; products add `custom_*` points without a contract change.

| Point | Progression game | Daily ranked or social game | Never at this point |
|-------|------------------|-----------------------------|---------------------|
| `on_session_start` | At most one offer, only after the first sessions, never stacked | Season pass reminder in the first days of a season, at most once a day | A pop up chain; an offer before the player has played in a new install |
| `on_level_start` | Pre level booster (fixed price, `maxPerAttempt`) | Nothing that changes the counted attempt | A booster for a ranked or counted attempt |
| `on_level_end` | Reward multiplier (rewarded), level end interstitial with grace | Share, practice, archive | An interstitial inside a counted attempt |
| `on_fail` | Extra moves or time for a fixed price; rewarded continue as the free path, capped per day | Not applicable to counted tries (see `on_attempts_exhausted`) | A rising price for the same continue |
| `on_attempts_exhausted` | Lives refill only if the game repo uses lives (not a default) | Uncounted replay ("play again, does not count"), practice, archive, the group Encore, a subscription that includes unlimited uncounted replay | A paid or earned counted try |
| `on_season_start` | Season or event pass | Season pass (cosmetic track, access) | A pass track reward that changes ranked results |
| `on_season_end` | Results, next season preview | Results, next season pass preview | "Last chance" pressure copy, retroactive loss of earned rewards |
| `on_menu` | Shop, ad removal, banner (menus only) | Shop, subscription, cosmetics | Banners in play |
| `on_loading` | Banner where the game has a real loading screen | Same | Artificial loading screens added to carry ads |

## 3. The fail moment (progression)

Pattern shared across the 2026-10-12 sources: when a level is failed by a small margin, offer extra moves for soft currency (often with a booster), offer a rewarded revive as the free path, make the continue a choice and never a gate, and tie a booster offer to the obstacle that caused the fail [Reported, 2026-10] (Naavik, Unity, Supersonic summaries).

| Element | Rule | Policy field |
|---------|------|--------------|
| Price | Fixed, shown in real money (or currency with its real money price) before the tap | `basePrice`, `priceInVirtual`, `showRealMoneyPrice` |
| Limit | Continues per attempt capped | `maxPerAttempt` (required for moves, time and booster offers) |
| Escalation | None. The second continue in the same attempt costs the same as the first | `priceEscalation: false`; sibling offers at the same point sell the same grants at one price |
| Free path | A rewarded continue, opt in, granted on completion, capped per day | Placement `format: rewarded`, `optIn`, `grantOn: completed`, `dailyCap` |
| Copy | States what the player gets; no countdown, no guilt | `countdown: false` for any audience with minors |
| Decline | One tap, equally visible, returns to the map without a second offer | `offer_declined` event |

What the market does that we refuse: a reported Royal Match pattern of a first continue around 900 coins rising above 2,000 after a second fail (single source, fungies.io) [Unverified]. Rising continue prices inside one attempt are a pressure pattern consumer regulators target, and the contract forbids them in two ways (`priceEscalation` and the sibling price check).

Who decides near miss difficulty: the game repo. Reported teardowns describe "fail by 1 to 2 moves" as core design in top match games [Reported, 2026-10]; whether a game does that is game design and never a monetization request. If the economy review shows continues concentrated on a few levels, `game-liveops` raises a difficulty flag to the game repo; no one tunes levels to sell continues.

## 4. Attempts exhausted (daily ranked)

The moment after the last counted try is the highest attention moment in a daily game and the easiest place to break fairness.

Allowed, in order of fit:
1. **Play again, does not count**: an uncounted replay of today's level, clearly marked, never written to a ranked board. Free once or a few times a day, or unlimited inside a subscription.
2. **Practice or archive**: earlier levels or a practice level (`practice` mode).
3. **The Encore** for the group (section 5).
4. **Season pass or subscription**, shown at most once a day at this point.
5. **Rewarded ad for an uncounted replay** (the `rewarded_replay` placement in `aloo-policy.json`): never for a counted try. Rewarded access is not equal access: fill varies by country, ad blockers, ATT and consent, and web rewarded supply may not be available at all (Google's H5 Games Ads is a closed beta) [Reported, 2026-10].

Never: a paid counted try, an earned counted try (ad, streak, referral), a try that counts "only for a personal best" on a shared board, or copy that implies the player can still win today by paying.

## 5. The Encore pattern (group bonus round)

A group product sells one thing that is fair by construction: a bonus round that one member buys for everyone in the group.

| Constraint | Why | How it is enforced |
|------------|-----|--------------------|
| The whole group receives it; the buyer gets nothing the others do not | No money advantage among friends | `grantsTo: group` in a `social` mode offer; `monetization_check.py` fails `buyer` |
| It writes only to group boards (day and season), never to an `everyone` board | A group purchase must not lift anyone on a global board | Grant `{kind: round, writesTo: [group boards]}`; the checker fails a write to a wider board |
| The global board query excludes encore plays | Today's global board must stay "counted tries only" | The product repo's conformance test (contract section 9, item 3) |
| One try each on a new seed, the same points ladder, no speed or first bonus | Equal conditions for every member | Game repo implementation (these are the fairness constraints, the round's content is the game's) |
| Opens for everyone at the next tick, closes with the day | Nobody gets an early start | Game repo implementation |
| The group sees who gifted it | Social credit replaces advantage | Product UI |
| Fixed price consumable, no randomness | No loot box mechanics, no escalation | `kind: consumable`, `random: false`, `priceEscalation: false` |
| No countdown copy | Minors may be in groups | `countdown: false` |
| An IAP inside store wrappers | Digital content in an iOS or Android app uses store billing unless a link out is allowed | `storeProductIds` for every store (Guideline 3.1.1 [Official, 2026-10]) |
| Parental approval for buyers under 18 where the law asks | Turkey Law 7578 requires purchase approval on game platforms [Reported, 2026-10]; FTC Genshin settlement bars purchases under 16 without parental consent in the US [Reported, 2026-10] | Product flow; compliance per market |

Refunds: a refunded encore that was already played stays in the log; the round is not removed from other members' history; repeated refund abuse blocks that buyer from buying again ([Segmentation and payment ops](segmentation-and-payment-ops.md) section 8).

Policy encoding (from `aloo-policy.json`): mode `encore` of kind `social`; SKU `encore` with grant `{ "kind": "round", "id": "encore_round", "writesTo": ["group_day", "group_season"] }`; offer `encore_at_game_over` at `on_attempts_exhausted` with `grantsTo: group`, `maxPerDay: 1`.

## 6. Level start boosters (progression)

| Rule | Detail |
|------|--------|
| Teach before selling | Reported teardowns show boosters taught around level 7 with 3 free of each [Unverified]; free samples before the first paid offer |
| Fixed price, per attempt cap | `maxPerAttempt`, no escalation |
| Tied to the level, not to a timer | Offer the booster that helps with what this level asks, chosen by the game repo's level data, never by pressure |
| Visible inventory | The player sees owned boosters before buying more |
| Never in ranked | A booster in a weekly race or any ranked board is play changing; the checker fails it |

## 7. Season start pass

| Element | Ranked or social product | Progression product |
|---------|--------------------------|---------------------|
| Track rewards | Cosmetics, access, group themes, profile frames | Cosmetics, currency, boosters, access |
| Price | Fixed per season, shown before purchase | Same |
| Duration | Stated on the offer (the `aloo-policy.json` sample assumes 21 day seasons) | Monthly is common: Royal Pass reported at 30 steps per month from level 37 [Unverified] |
| Late buyers | Get every reward already earned on the track | Same |
| Expiry | No retroactive loss of earned rewards at season end | Same |
| Evidence of effect | Naavik reported +31% revenue in the first 30 days after Royal Match added its pass (June 2021) [Unverified] | Same |

The calendar of seasons and the content cadence belong to `game-liveops`; this module owns the pass as a product (price, track rules, policy entry, events).

## 8. Subscriptions (plus style: archive and replay)

A plus subscription sells comfort and depth, never results: the archive, stats, unlimited uncounted replay of today's level, cosmetic perks and, when true, no ads.

Evidence that daily puzzle players pay for this shape: The New York Times reported 13.35 million subscribers in Q2 2026 and added single product subscribers after paywalling The Mini in Q3 2025 [Reported, 2026-10]; Puzzmo Plus (about $40 a year) sells archives, leaderboards and no ads [Unverified]. These are bundles of many games or a publisher brand; they do not predict a single small game's conversion.

| Requirement | Basis | Owner |
|-------------|-------|-------|
| Name, duration, content, full renewal price as the most prominent price, trial length and price after, Restore, Terms and Privacy links in the app and metadata | Apple Guideline 3.1.2 [Official, 2026-10] | store-submission, compliance |
| Period at least 7 days, ongoing value, available on all the user's devices | Apple Guideline 3.1.2(a) [Official, 2026-10] | This agent (catalog), store-submission |
| Terms, price, frequency, auto renewal and trial conversion disclosed; easy online cancellation; cancellation keeps access to the period end; trials charge the full price at the end | Google Play billing docs [Official, 2026-10] and Play Console Help [Reported, 2026-10] | store-submission |
| EU withdrawal function on contracts with a right of withdrawal (from 2026-06-19) | Compliance rule SUB-EU-01 in the compliance skill | compliance, site-engineer |
| "No ads" means no ads | If optional rewarded ads stay, say "no interstitials or banners" instead | compliance |
| Entitlement keyed on the original transaction id | A renewal never grants twice (contract section 5) | Product server |

## 9. Starter packs

| Rule | Detail |
|------|--------|
| When | After the first levels or sessions, once the player knows what the items do [Reported, 2026-10] |
| What | One time, fixed price, content listed with honest quantities |
| Anchors | No invented "was" price; any reference price follows the EU 30 day and Turkey 10 day rules through compliance |
| Urgency | No countdown for audiences with minors; for adults only a real deadline, and `monetization_check.py` still warns |
| Eligibility | Shown to non payers; this is relevance, not price discrimination (the price is the same for everyone who sees it) |

## 10. Piggy bank and ad removal

**Piggy bank.** A bank fills as the player plays and can be bought at a fixed price. Reported examples: Hexa Sort unlocks it at level 7 and charges $4.99, reported as its third top IAP on US iOS by Sensor Tower via maf.ad; about 40 of the top 100 games have one; it is rarely a first purchase [Unverified]. House rules: the price and the fill rule are visible from the start (some games hide the price until the bank is full; we do not), the bank never empties without notice, and it grants currency, so it lives in progression modes only.

**Ad removal.** "Remove ads" usually keeps rewarded ads, which the player chooses [Reported, 2026-10]. Name exactly what goes: "Removes interstitials and banners. Optional rewarded videos stay." Color Block Jam's No Ads bundle was reported at $11.99 in the US [Unverified]. Never claim "No ads" in ads, store text or the offer while any ad format still runs; the teardown notes list "No Ads" claims while ads exist among the patterns to refuse [Reported, 2026-10].

## 11. Frequency and caps for offers

| Rule | Policy field or check |
|------|------------------------|
| Every offer has `maxPerDay` or `maxPerAttempt` | `monetization_check.py` warns when both are missing |
| One offer per moment; no stacked pop ups | Product logic; mid session pop ups were among the VZBV objections to Monopoly Go (2025-06) [Reported, 2026-10] |
| A declined offer stays declined for the session | Product logic, `offer_declined` event |
| No offer before the first completed session of a new install | Product logic |
| Payers see fewer interruptive ads, never higher prices | [Segmentation and payment ops](segmentation-and-payment-ops.md) section 3 |
| Every offer has `offer_shown`, `offer_accepted` and `offer_declined` coverage | `monetization_conformance.py` |

## 12. Offer copy rules (all go through compliance)

1. The real money price is on the button or right beside it.
2. What the player gets is stated in plain quantities.
3. No countdown or scarcity copy for audiences with minors; none at all unless the deadline is real.
4. No guilt or social pressure ("your team is counting on you", "don't let your friends down").
5. No "free" for anything that costs money or data later.
6. No implied advantage in ranked modes ("climb the leaderboard with Plus").
7. Gift and group offers name who receives what.

## 13. Offer spec template

Every new offer is drafted as a policy entry plus a sheet row plus tracking coverage:

```json
{ "id": "moves_on_fail", "point": "on_fail", "mode": "levels", "sku": "extra_moves",
  "grantsTo": "buyer", "maxPerAttempt": 2, "countdown": false, "priceEscalation": false }
```

| Field | Value |
|-------|-------|
| Offer id, point, mode | |
| SKU and grants | |
| Grants to | buyer, group, everyone |
| Caps | maxPerDay, maxPerAttempt |
| Price (pricing-strategy) | |
| Copy (compliance verdict id) | |
| Events covered (`monetization_conformance.py` result) | |
| Hypothesis and primary metric | |
| Guard rails | D1, D7, refund rate, complaint rate |
| Read date and stop rule | |

## 14. Quick decision table

| Question | Answer |
|----------|--------|
| Can we sell an extra counted try in the daily mode? | No. Offer an uncounted replay, practice, archive, the Encore, the pass or the subscription |
| Can a rewarded ad grant a counted try? | No. It may grant an uncounted replay |
| Can we sell +5 moves after a fail in level mode? | Yes, at a fixed price with `maxPerAttempt` |
| Can the second continue cost more? | No |
| Can a season pass include boosters? | In progression products yes; in ranked products only if the boosters cannot be used in any ranked mode |
| Can a group purchase write to the global board? | No |
| Can we sell a streak freeze? | Only after the product declares whether the streak is competitive; if it is, no |
| Can the Plus subscription show "no ads" while rewarded stays? | Only as "no interstitials or banners" |
| Can we show a starter pack countdown? | Not with minors in the audience; for adults only with a real deadline |
