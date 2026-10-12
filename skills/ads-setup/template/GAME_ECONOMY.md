# Game Economy

> Game projects only. The human owns this file with `game-monetization`. Every price change is a change request (G3); this file records what is live and why. The machine readable twin is `data/monetization-policy.json` (checked by `monetization_check.py` in the game-monetization skill); keep both in sync.

## Currencies

| Currency | Real money or virtual | Purchasable | Real money price shown next to it | Sources (how players earn it) | Sinks (what it buys) |
|---|---|---|---|---|---|
| `<EUR, USD, TRY or coins>` | | | | | |

## Sources and sinks balance (per active day, for a typical non payer)

| Flow | Item | Amount per day | Notes |
|---|---|---|---|
| Source | | | |
| Sink | | | |

## Catalog

| SKU | Kind | Grants | Mode allowed | Prices per currency | Stripe id | Apple id | Play id | Random (odds) |
|---|---|---|---|---|---|---|---|---|
| `<sku>` | `<consumable, non_consumable, subscription, season>` | | `<ranked safe, practice, social, progression>` | | | | | `<no>` |

## Offer points

| Offer | Point | Mode | SKU | Grants to | Cap | Countdown (never for minors) |
|---|---|---|---|---|---|---|

## Ad placements

| Placement | Format | Point | Mode | Grace | Cooldown | Session cap | Daily cap |
|---|---|---|---|---|---|---|---|

## Fairness

- Ranked boards and their counted attempts per day:
- What may be sold or earned in ranked modes (cosmetics, practice, archive, passes, group rounds only):
- Progression items allowed (boosters, continues) and their limits per attempt:

## Change log

| Date | Change | Reason | Experiment row | Approved by |
|---|---|---|---|---|
