# Game Monetization Contract (v0.1)

> The reusable way every game product earns money without breaking fairness, store rules or consumer law. Ads Master owns this contract; each product's own repo implements it once and carries a conformance test. Contract version `0.1`, 2026-10. Drafted from a real integration (a daily social mini game product with two counted tries a day, group points, 21 day seasons and a practice level) and read against a second architecture (a board game platform whose games are pure reducer modules), then reviewed twice by a second model; both reviews are folded in.

## 1. Why a contract

Without one, every game reinvents offers, ad placements, price lists and event names, and each version gets a different bug: an ad that fires before consent, a SKU without a Play product id, a paid item that changes a leaderboard, a currency with no real money price, a group purchase that quietly lifts the buyer on a global board. With one, a product registers its moments and its policy file, and the checks, dashboards, store declarations and agents work on day one.

## 2. Three layers

| Layer | What | Where it lives | Who reads it |
|-------|------|----------------|--------------|
| 1. Policy file | `monetization-policy.json`, one per **product** (a store listing or a web app, which may hold many games), versioned with `contractVersion` and `policyRevision` | The product repo (and `ads-master/data/` in the workspace) | The product's code at runtime, `monetization_check.py`, `monetization_conformance.py`, the agents |
| 2. Types | Six interfaces, sketched below; each codebase writes them in its own language | The product repo | The product's code |
| 3. Runbook | Kill switch, remote config, consent order, grant rules, refunds | Section 8 | Engineers and agents |

The policy file is the only executable part, and it must be imported by the product's code, not copied into it. A contract that no code imports is a document, and documents drift. Constants that the policy governs (for example tries per day) are read from the policy or asserted equal to it in the conformance test.

## 3. Modes, boards and what each may sell

Every placement and offer declares the mode it runs in; mode ids may be namespaced per game (`kilim:daily`, `memory:practice`). Ranked modes declare the **boards** they write to, each with a scope: `group` (a friend group, a team, a league division) or `everyone` (a global board). The checker derives fairness from the boards and the typed grants; nothing is self declared.

| Mode | Meaning | May grant | Never |
|------|---------|-----------|-------|
| `ranked` | Results that rank people against each other. Declares `countedAttemptsPerDay` (a positive integer, or `"unlimited"` for a ladder of matches) and `boards` | `cosmetic`, `access` (practice, archive, stats), `pass` | Anything that changes play: `attempt`, `moves`, `time`, `booster`, `currency`, `lives`, `streak_protection` |
| `practice` | Uncounted play (replays, practice levels, archive) | Anything that does not write to a ranked board | Writing to a ranked board |
| `social` | Shared moments equal for everyone who receives them (encores, group themes) | A `round` granted to the group or everyone, written only to boards no wider than who receives it | A benefit only the buyer receives in a competitive context |
| `progression` | Single player level progress (Royal Match style levels, campaigns). Not the same as a platform's "progress" or stars slot | Boosters before a level, extra moves or extra time after a fail, currency, lives, passes | Escalating continue prices, hidden odds, countdown pressure aimed at minors, any write to a ranked board |

**The ranked rule (checked mechanically).** Every ranked board has a constant number of counted attempts per player per day (or is declared unlimited). No purchase, ad or reward changes it. Only a `round` may write to a ranked board, and only to boards whose scope is no wider than who receives the round: a round bought for the group writes to group boards, never to an `everyone` board. Everything else in a ranked mode is cosmetic, access or a pass.

**The progression rule.** Boosters and continues are legitimate in `progression` mode, the way Royal Match sells "+5 moves" and pre level boosters [Reported, 2026-10, teardowns]. Each moves, time or booster offer carries a limit per attempt (`maxPerAttempt`), a fixed price shown before purchase, no escalation inside one attempt (also not by sibling offers at the same moment), and never writes to a ranked board.

**Derived boards.** A board computed from other data (a streak board fed by daily play, a season table fed by daily points) counts as ranked when its inputs are ranked. A `streak_protection` grant (a streak freeze) is therefore play changing when the streak is shown competitively. A product that sells or rewards streak protection decides this explicitly and declares the streak board.

## 4. Typed grants

Every catalog item and every rewarded placement lists what it grants as typed objects:

```json
{ "kind": "round", "id": "encore_round", "writesTo": ["group_day", "group_season"] }
{ "kind": "moves", "amount": 5 }
{ "kind": "currency", "id": "coins", "amount": 1000 }
{ "kind": "access", "id": "archive" }
```

| Kind | Changes play | Typical mode |
|------|--------------|--------------|
| `cosmetic`, `access`, `pass` | No | Any |
| `round` | Writes to the boards it names | `social` |
| `attempt`, `moves`, `time`, `booster`, `lives` | Yes | `progression` or `practice` |
| `currency` | Yes (it buys play changing items) | `progression` |
| `streak_protection` | Yes when the streak is shown competitively | Decide per product |

## 5. The six types (sketch)

Written in TypeScript for readability; implement in the product's own language. Store providers appear only in adapters and in the policy's `stores` list.

```ts
// 1. Where an offer or ad may appear. snake_case so strict event catalogs accept it; products add custom_ points.
type OfferPoint =
  | "on_session_start" | "on_level_start" | "on_level_end" | "on_fail"
  | "on_attempts_exhausted" | "on_season_start" | "on_season_end" | "on_menu" | "on_loading"
  | `custom_${string}`;

// 2. What the product knows at that moment. The policy decides with this; nothing else.
interface OfferContext {
  modeId: string;                         // may be namespaced, e.g. "kilim:daily"
  point: OfferPoint;
  attemptsLeft: number | "unlimited" | null;
  payerTier: "none" | "low" | "mid" | "high";
  consent: { ads: boolean; personalizedAds: boolean; att: "authorized" | "denied" | "not_determined" | "n/a" };
  ageBracket: "under13" | "13to15" | "16to17" | "adult" | "unknown";
  region: string;                         // ISO 3166-1 alpha-2
  sessionCount: number;
  levelIndex: number | null;              // progression only
  secondsSinceLastInterstitial: number | null;
}

// 3. An ad placement, mirrored from the policy file.
interface Placement {
  id: string;
  format: "rewarded" | "interstitial" | "banner" | "app_open" | "native";
  point: OfferPoint;
  modeId: string;
  grants: Grant[];                        // required for rewarded
}

// 4. What a player or a group owns. The server keeps a grant log; the client never grants.
interface Entitlement {
  id: string;                             // "season_pass:2026-s14", "plus", "encore:<group>:<day>"
  owner: { type: "user" | "group"; id: string };
  source: { storeId: string; transactionKey: string };  // subscriptions key on the original transaction id, not the renewal
  grantedAt: string;
  expiresAt: string | null;
  revokedAt: string | null;               // refund or chargeback; consumables also claw back through the ledger
}
// Grants are idempotent on (storeId, transactionKey). A refund revokes. Revocation is logged, never deleted.

// 5. One catalog for every store.
interface CatalogItem {
  sku: string;                            // canonical, store neutral
  kind: "consumable" | "non_consumable" | "subscription" | "season";
  grants: Grant[];
  basePrice: { currency: string; minor: number };          // integer minor units, never floats
  platformPrices?: Record<string, Record<string, number>>; // per store id, per currency, minor units (stores set prices by tier)
  storeProductIds: Record<string, string>;                 // keyed by the policy's store ids
  period?: string;                        // subscriptions: ISO 8601 duration such as P1M
  trialDays?: number;
  random: boolean;                        // loot box style: odds and labels required
  odds?: Record<string, number>;
}

// 6. The only place a vendor appears.
interface MonetizationAdapter {
  showRewarded(placementId: string, ctx: OfferContext): Promise<"completed" | "skipped" | "unavailable">;
  showInterstitial(placementId: string, ctx: OfferContext): Promise<"shown" | "skipped" | "unavailable">;
  purchase(sku: string): Promise<{ status: "completed" | "cancelled" | "pending" | "failed"; transactionKey?: string }>;
  restore(): Promise<string[]>;           // transaction keys, then the server re-grants
}
```

Adapters by store (examples, chosen per product):

| Store id (example) | Provider | Purchases | Ads |
|--------------------|----------|-----------|-----|
| `web` | Stripe or a merchant of record (Paddle, Lemon Squeezy) | Checkout or Payment Element | Google H5 Games Ads (closed beta, apply), a portal SDK, or a web rewarded vendor |
| `apple` | Apple | In-App Purchase (StoreKit), or a US link out where allowed | AdMob or AppLovin MAX through a native bridge |
| `google` | Google | Play Billing (Library 8 or later in 2026) | AdMob or AppLovin MAX |

Tax note: selling digital goods on the web in the EU and Turkey creates VAT duties per buyer country. Stripe alone is not a merchant of record; either register and remit, or use a merchant of record. `compliance` and the human own this decision before the first web sale.

## 6. Events (one taxonomy for every product)

Every offer and ad emits these events. Names and property values are snake_case so strict event catalogs accept them. Properties: `product`, `game` (the mini game or module when there is one), `mode_id`, `point`, `placement_id` or `sku`, `contract_version`, `policy_revision`. `monetization_conformance.py` fails when a placement or SKU has no event coverage in the tracking plan.

| Event | When |
|-------|------|
| `offer_shown`, `offer_accepted`, `offer_declined` | An offer appears and the player answers |
| `purchase_started`, `purchase_completed`, `purchase_failed`, `purchase_refunded` | The payment lifecycle (refunds from server notifications: Stripe webhooks, App Store Server Notifications, Play Real-time developer notifications) |
| `entitlement_granted`, `entitlement_revoked` | Server side, after validation |
| `ad_requested`, `ad_shown`, `ad_rewarded`, `ad_failed` | The ad lifecycle; `ad_rewarded` only on completion |
| `ad_revenue` | Impression level revenue from mediation where available |
| `consent_updated` | Any consent change |

`policy_revision` on every event lets revenue be attributed to a policy change (a new cap, a new offer) in the same way an experiment is read.

## 7. The policy file

Schema: `scripts/monetization-policy.schema.json`. Examples: `scripts/samples/aloo-policy.json` (daily social product: ranked days, practice, a group encore that writes only to group boards) and `scripts/samples/progression-policy.json` (level based puzzle: boosters and extra moves in progression, a weekly race nobody can buy into).

| Key | Holds |
|-----|-------|
| `contractVersion`, `policyRevision` | `"0.1"`; an integer that goes up with every change |
| `product` | id, platforms, audience (minimum age, kids mode), regions where it sells |
| `stores` | Each store id with its provider and platforms (`web`: stripe, `apple`, `google`) |
| `currencies` | Virtual currencies with `purchasable` and `showRealMoneyPrice` |
| `modes` | Each mode with kind; ranked modes with `countedAttemptsPerDay` and `boards` |
| `catalog` | Catalog items (section 5) with typed grants |
| `offers` | Point, mode, sku, `grantsTo` (`buyer`, `group`, `everyone`), caps (`maxPerDay`, `maxPerAttempt`), `countdown`, `priceEscalation` |
| `placements` | Format, point, mode, typed grants for rewarded, and the format rules: interstitial grace (levels or seconds), cooldown, session cap, reset after rewarded; rewarded opt in and grant on completion; banners only on `on_menu` or `on_loading` |
| `consent` | Ads require consent first; CMP standard (IAB TCF in the EEA and UK); ATT on iOS |
| `storeDeclarations` | Contains ads, in-app purchases, loot boxes (what the stores and age rating forms are told) |
| `killSwitch` | Remote config key that turns every offer and placement off |

## 8. Runbook

1. **Consent first.** No ad SDK initialises before consent in the EEA and UK, and no IDFA read before ATT on iOS (CNIL fined a game publisher EUR 3m in 2023 over advertising use of an identifier without consent [Reported, 2026-10]).
2. **Client shows, server grants.** The client asks the policy whether to show; only the server grants value, after validating the receipt or the ad reward callback.
3. **Kill switch.** Every offer and placement can be turned off by remote config within minutes, without a release.
4. **Remote config for tuning.** Frequencies, caps and prices change by config, never by hard coded numbers, and every change raises `policyRevision` and gets an experiment row in `EXPERIMENTS.md`.
5. **Refunds revoke.** Server notifications revoke entitlements; consumables are clawed back through the ledger (a refunded encore that was already played is logged, and repeated abuse blocks the buyer); the player sees what changed.
6. **Minors.** When the age bracket is under 18 or unknown in a region that requires it, purchases go through parental approval where the law asks (Turkey Law 7578, the Genshin precedent in the US), personalized ads are off for under 13s, and no countdown or scarcity copy appears.
7. **Admin grants are entitlements too.** Any manual reset or compensation (for example handing back a try after a crash) is an `admin` grant in the same log, never a silent database edit.
8. **Versioning.** A breaking change bumps the minor version (`0.1` to `0.2`); each product declares the version it implements; the checker refuses versions it does not support (exit 2).

## 9. Conformance test (each product repo)

A product conforms when its own test suite proves:
1. The policy file loads and passes `monetization_check.py`; constants it governs equal the policy (for example tries per day).
2. No board accepts an attempt beyond `countedAttemptsPerDay` after any purchase, reward, admin grant or encore.
3. A group round writes only to the group boards the policy names; the global board query excludes encore plays.
4. Granting is idempotent on (store id, transaction key); a refund revokes; a subscription renewal does not grant twice.
5. No ad call happens before consent (test with consent denied).
6. The kill switch stops every offer and placement.
7. Every placement and SKU emits the events in section 6 with `policy_revision`.

## 10. Known decisions per product (examples from the two reference integrations)

| Product | Decision the contract surfaced | Owner |
|---------|-------------------------------|-------|
| Daily social mini games | The encore must be stored so the global board query excludes it (today every non refunded play counts toward the global board); tries per day must come from the policy | Product repo, before the encore ships |
| Board game platform with a streak | Streak freeze tokens are `streak_protection`; decide whether the streak is competitive before selling or rewarding them | The founder, before the platform reads a policy |

## 11. What is deliberately not in the contract

- **No runtime library.** Products live on different stacks; the contract is a schema, types and tests, not a package.
- **No lives or energy primitive as a default.** A product that wants lives models them in `progression` mode with its own rules; the contract does not push gating mechanics.
- **No vendor names in core types.** Vendors appear only in adapters and the `stores` list.
- **No game design.** Level design, difficulty and rules belong to the product repo; the contract governs only what may be sold or shown, and where.
