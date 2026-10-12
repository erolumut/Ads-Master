# Game Monetization Contract (v0.1)

> The reusable way every game in the portfolio earns money without breaking fairness, store rules or consumer law. Ads Master owns this contract; each game's own repo implements it once and carries a conformance test. Contract version `0.1`, 2026-10. Drafted from a real integration (a daily social mini game app with two counted tries a day, group points, 21 day seasons and a practice level) and read against a second game architecture (a pure reducer board game module) before it was called standard.

## 1. Why a contract

Without one, every game reinvents offers, ad placements, price lists and event names, and each version gets a different bug: an ad that fires before consent, a SKU without a Play product id, a paid item that changes a leaderboard, a currency with no real money price. With one, a new game registers its moments and its policy file, and the checks, dashboards, store declarations and agents work on day one.

## 2. Three layers

| Layer | What | Where it lives | Who reads it |
|-------|------|----------------|--------------|
| 1. Policy file | `monetization-policy.json`, one per game, versioned with `contractVersion` | The game repo (and `ads-master/data/` in the workspace) | The game's code at runtime, `monetization_check.py`, `monetization_conformance.py`, the agents |
| 2. Types | Six interfaces, sketched below; each codebase writes them in its own language | The game repo | The game's code |
| 3. Runbook | Kill switch, remote config, consent order, grant rules | This file, section 7 | Engineers and agents |

The policy file is the only executable part, and it must be imported by the game's code, not copied into it. A contract that no code imports is a document, and documents drift.

## 3. Modes and what each may sell

Every placement and offer declares the mode it runs in. The mode decides what may be granted.

| Mode | Meaning | May grant | Never |
|------|---------|-----------|-------|
| `ranked` | Results that rank people against each other (daily boards, group points, global boards, leagues) | Cosmetics, practice access, archive access, a bonus round the whole group receives (scope `group`) | Anything that changes a ranked result: extra counted attempts, extra time, boosters, continues, score multipliers |
| `practice` | Uncounted play (replays, practice levels, archive) | Extra plays, hints, anything that does not touch a ranked result | Writing into a ranked board |
| `social` | Shared moments that are equal for everyone in the group (encores, group themes) | Rounds or items granted to every member equally; the buyer gets nothing the others do not | A benefit only the buyer receives in a competitive context |
| `progression` | Single player level progress (Royal Match style levels, campaigns) | Boosters before a level, extra moves or extra time after a fail (continues), lives refills, starter packs, passes | Escalating continue prices, hidden odds, countdown pressure aimed at minors, a continue that costs more than it says |

The ranked rule (checked mechanically): **every ranked board declares a constant number of counted attempts per player per day (`countedAttemptsPerDay`). No purchase, ad or reward changes it. A ranked mode placement or offer must declare `affectsRankedResult: false` and may grant only cosmetics, practice, archive or a group scoped round.**

The progression rule: boosters and continues are legitimate in `progression` mode, the way Royal Match sells "+5 moves" and pre level boosters [Practitioner consensus, teardowns 2025 to 2026]. They must carry a fixed real money or currency price shown before purchase, a limit per attempt (`maxPerAttempt`), no price escalation inside one attempt, and they never leak into a ranked board (a progression score never feeds a ranked leaderboard unless that board is declared `pay_to_progress` and labelled as such to players).

## 4. The six types (sketch)

Written in TypeScript for readability; implement in the game's own language. Vendor names appear only in adapters.

```ts
// 1. Where an offer or ad may appear. Open list: games add their own with the custom: prefix.
type OfferPoint =
  | "onSessionStart" | "onLevelStart" | "onLevelEnd" | "onFail"
  | "onAttemptsExhausted" | "onSeasonStart" | "onSeasonEnd" | "onMenu" | "onLoading"
  | `custom:${string}`;

// 2. What the game knows at that moment. The policy decides with this; nothing else.
interface OfferContext {
  mode: "ranked" | "practice" | "social" | "progression";
  point: OfferPoint;
  attemptsLeft: number | null;        // counted attempts left today in ranked modes
  payerTier: "none" | "low" | "mid" | "high";
  consent: { ads: boolean; personalizedAds: boolean; att: "authorized" | "denied" | "not_determined" | "n/a" };
  ageBracket: "under13" | "13to15" | "16to17" | "adult" | "unknown";
  region: string;                     // ISO 3166-1 alpha-2
  sessionCount: number;
  levelIndex: number | null;          // progression only
  secondsSinceLastInterstitial: number | null;
}

// 3. An ad placement, mirrored from the policy file.
interface Placement {
  id: string;
  format: "rewarded" | "interstitial" | "banner" | "app_open" | "native";
  point: OfferPoint;
  mode: OfferContext["mode"];
  affectsRankedResult: boolean;       // must be false in ranked mode
}

// 4. What a player owns. The server keeps a grant log; the client never grants.
interface Entitlement {
  id: string;                         // e.g. "season_pass:2026-s14", "aloo_plus", "encore:<group>:<day>"
  source: { provider: "stripe" | "apple" | "google" | "reward" | "admin"; transactionId: string };
  grantedAt: string;                  // ISO 8601
  expiresAt: string | null;
  revokedAt: string | null;           // set on refund or chargeback
}
// Grants are idempotent on (provider, transactionId). A refund revokes. Revocation is logged, never deleted.

// 5. One catalog for every platform.
interface CatalogItem {
  sku: string;                        // canonical, platform neutral
  kind: "consumable" | "non_consumable" | "subscription" | "season";
  grants: string[];                   // entitlement ids or currency amounts ("coins:500")
  prices: Record<string, number>;     // real money per ISO 4217 currency, shown before purchase
  platformIds: { stripe?: string; apple?: string; google?: string };
  random: boolean;                    // true = loot box style: odds and labels required
  odds?: Record<string, number>;
}

// 6. The only place a vendor appears.
interface MonetizationAdapter {
  showRewarded(placementId: string, ctx: OfferContext): Promise<"completed" | "skipped" | "unavailable">;
  showInterstitial(placementId: string, ctx: OfferContext): Promise<"shown" | "skipped" | "unavailable">;
  purchase(sku: string): Promise<{ status: "completed" | "cancelled" | "pending" | "failed"; transactionId?: string }>;
  restore(): Promise<string[]>;       // transaction ids, then the server re-grants
}
```

Adapters by platform (examples, chosen per game):

| Platform | Purchases | Ads |
|----------|-----------|-----|
| Web, PWA | Stripe Checkout or Payment Element | Google H5 Games Ads (closed beta, apply), a portal SDK when published on a portal, or a web rewarded vendor |
| iOS wrapper or native | Apple In-App Purchase (StoreKit), or a US link out where allowed | AdMob or AppLovin MAX through a native bridge |
| Android wrapper or native | Google Play Billing (Library 8 or later in 2026) | AdMob or AppLovin MAX |

## 5. Events (one taxonomy for every game)

Every offer and ad emits these events with `game`, `mode`, `point`, `placement_id` or `sku`, `contract_version`. The tracking plan lists them, and `monetization_conformance.py` fails when a placement or SKU has no event coverage.

| Event | When |
|-------|------|
| `offer_shown`, `offer_accepted`, `offer_declined` | An offer appears and the player answers |
| `purchase_started`, `purchase_completed`, `purchase_failed`, `purchase_refunded` | The payment lifecycle (refunds from server notifications: Stripe webhooks, App Store Server Notifications, Play Real-time developer notifications) |
| `entitlement_granted`, `entitlement_revoked` | Server side, after validation |
| `ad_requested`, `ad_shown`, `ad_rewarded`, `ad_failed` | The ad lifecycle; `ad_rewarded` only on completion |
| `ad_revenue` | Impression level revenue from mediation where available |
| `consent_updated` | Any consent change |

## 6. The policy file

Schema: `scripts/monetization-policy.schema.json`. Example: `scripts/samples/aloo-policy.json` (a daily social game with ranked days, a practice level and a group encore). Minimum content:

| Key | Holds |
|-----|-------|
| `contractVersion` | `"0.1"` |
| `game` | id, platforms, audience (minimum age, kids mode), regions where it sells |
| `currencies` | Real money currencies used for prices; virtual currencies with `showRealMoneyPrice` |
| `modes` | Each mode with its kind; ranked modes with `countedAttemptsPerDay` |
| `catalog` | Catalog items (section 4) |
| `offers` | Offer point, mode, sku, `affectsRankedResult`, `grantsTo` (`buyer` or `group`), caps, `countdown`, `priceEscalation` |
| `placements` | Ad placements with format rules: interstitial grace (levels or seconds), cooldown, session cap, reset after rewarded; rewarded opt in and grant on completion; banners only on menu or loading points |
| `consent` | Ads require consent first; CMP standard (IAB TCF in the EEA and UK); ATT on iOS |
| `storeDeclarations` | What the stores are told: contains ads, in-app purchases, loot box label, age rating inputs |
| `killSwitch` | Remote config key that turns every offer and placement off |

## 7. Runbook

1. **Consent first.** No ad SDK initialises before consent in the EEA and UK, and no IDFA read before ATT on iOS (CNIL fined a game publisher EUR 3m in 2023 for advertising use of an identifier without consent [Unverified, secondary report]).
2. **Client shows, server grants.** The client asks the policy whether to show; only the server grants value, after validating the receipt or the ad reward callback.
3. **Kill switch.** Every offer and placement can be turned off by remote config within minutes, without a release.
4. **Remote config for tuning.** Frequencies, caps and prices change by config, never by hard coded numbers, and every change is an experiment row in `EXPERIMENTS.md`.
5. **Refunds revoke.** Server notifications revoke entitlements; the player sees what changed and why.
6. **Minors.** When `ageBracket` is under 18 or unknown in a region that requires it, purchases go through parental approval where the law asks (Turkey Law 7578, Genshin precedent in the US), personalized ads are off for under 13s, and no countdown or scarcity copy appears.
7. **Versioning.** A change that breaks a field bumps the minor version (`0.1` to `0.2`); each game declares the version it implements; the checks read the version and refuse unknown majors.

## 8. Conformance test (each game repo)

A game conforms when its own test suite proves:
1. The policy file loads and passes `monetization_check.py`.
2. A ranked board never accepts an attempt beyond `countedAttemptsPerDay` after any purchase, reward or encore.
3. Granting is idempotent on (provider, transaction id), and a refund revokes.
4. No ad call happens before consent (test with consent denied).
5. The kill switch stops every offer and placement.
6. Every placement and SKU emits the events in section 5.

## 9. What is deliberately not in the contract

- **No runtime library.** Games live on different stacks; the contract is a schema, types and tests, not a package.
- **No lives or energy primitive.** A game that wants lives models them in `progression` mode with its own rules; the contract does not push gating mechanics.
- **No vendor names in core types.** Vendors appear only in adapters and `platformIds`.
- **No game design.** Level design, difficulty and rules belong to the game repo; the contract only governs what may be sold or shown, and where.
