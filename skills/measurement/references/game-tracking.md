# Game Tracking: Event Taxonomy, Revenue Truth, Consent and Attribution

> Knowledge as of 2026-10 (research pass 2026-10-12). Apple's AdAttributionKit session and Android's billing notification reference were read at the source [Official, 2026-10]; analytics vendor facts come from search summaries [Reported, 2026-10] or a single vendor [Unverified]. The event names and properties follow the Game Monetization Contract v0.1 ([contract](../../game-monetization/references/monetization-contract.md) section 6) and are checked by `monetization_conformance.py`. The KPI definitions these events feed live in [Game KPIs](game-kpis.md).

## 1. Principles

1. **One taxonomy for every game.** The same event names, properties and types across products, so the four dashboards and the checks work on day one ([Game KPIs](game-kpis.md) section 8).
2. **The contract names the money events.** Offers, purchases, entitlements, ads, ad revenue and consent use the contract's names and properties exactly. Gameplay events follow the same style: snake_case, past tense, closed value lists.
3. **The tracking plan is code.** Every event and property is declared in `ads-master/tracking-plan.json` (format in [Tracking plan as code](tracking-plan-as-code.md)); undeclared events fail the check. `monetization_conformance.py` proves every offer, placement and SKU in the policy is covered by value.
4. **The server is the truth for money.** The client reports what the player saw; the server reports what was paid, granted, refunded and revoked, after validation.
5. **Consent before any SDK that needs it.** Analytics in the consented mode only, ad SDKs only after the consent signal, the ATT prompt only after a value moment.
6. **No personal data in events.** User and group ids are pseudonymous and hashed where they leave the product; no names, emails, phone numbers or free text; contact books never uploaded.

## 2. The event taxonomy

The seven classic families (GameAnalytics uses progression, resource, business, ad, impression, design and error [Reported, 2026-10]) map to our names as follows.

| Family | Our events | Required properties | Fired from | Feeds |
|--------|-----------|---------------------|-----------|-------|
| Session | `session_started`, `session_ended` (optional, foreground end) | `product`, `game`, `build`, `platform` | Client | DAU, sessions, playtime |
| Progression | `level_started`, `level_completed`, `level_failed`, `level_quit` | `product`, `game`, `mode_id`, `level` (integer index), `attempt` (integer), `duration_s`, `boosters_used` (integer), `continues_used` (integer) | Client; ranked results also from the server | Level funnel, churn by level, win rate |
| Resource (economy) | `currency_earned`, `currency_spent` | `product`, `game`, `mode_id`, `currency_id`, `amount`, `flow` (`source` or `sink`), `reason` (closed list: `level_reward`, `purchase`, `ad_reward`, `booster`, `continue`, `event_reward`, `admin`) | Server when the balance lives on a server, else client | Sources and sinks per DAU, economy balance |
| Business (money) | `offer_shown`, `offer_accepted`, `offer_declined`, `purchase_started`, `purchase_completed`, `purchase_failed`, `purchase_refunded`, `entitlement_granted`, `entitlement_revoked` | Contract section 6: `product`, `game`, `mode_id`, `point`, `offer_id`, `sku`, `store`, `transaction_key`, `value`, `currency`, `owner_type`, `reason`, `contract_version`, `policy_revision` (as each event needs) | Offers and `purchase_started` from the client; completions, refunds and entitlements from the server | Offer conversion, payer conversion, ARPPU, refunds |
| Ad | `ad_requested`, `ad_shown`, `ad_rewarded`, `ad_failed` | `product`, `mode_id`, `point`, `placement_id`, `ad_format`, `error` (failed only), `contract_version`, `policy_revision` | Client (mediation callbacks); `ad_rewarded` only on completion | Fill rate, impressions per DAU, rewarded opt in |
| Impression | `ad_revenue` | `product`, `placement_id`, `ad_network`, `value`, `currency`, `precision` (`exact`, `publisher_defined`, `estimated`), `contract_version`, `policy_revision` | Client from the mediation impression callback, or server to server from mediation | ARPDAU ads, eCPM by placement, ROAS |
| Design (product moments) | `tutorial_step`, `share_sent`, `invite_sent`, `group_joined`, `streak_saved`, `event_action`, `season_step` | `product`, `game`, closed lists per event (`step`, `channel`, `event_id`, `season_id`) | Client | K-factor, group join rate, event participation, season completion |
| Error | `error_shown` (player facing errors), crash reports through the crash SDK | `product`, `build`, `error_code` (closed list), `severity` | Client | Daily dashboard; crash rate comes from the store vitals and the crash SDK |
| Consent | `consent_updated` | `ads`, `personalized_ads`, `att`, `product`, `contract_version`, `policy_revision` | Client | Consent rates, ad eligibility |

Rules that make the numbers right:
- `level` is an integer index in progression order, even when the game shows "World 2, level 3". Keep the display label in the game's own data, not in the event; `game_kpis.py` needs integers for churn by level.
- `attempt` counts attempts at that level by that player (1, 2, 3); without it, players and attempts cannot be separated.
- A fail (`level_failed`, the player lost) and a quit (`level_quit`, the player left) are different events.
- `mode_id` may be namespaced per game (`kilim:daily`). Ranked results (counted attempts, board writes) are written by the server; the client event is a display event.
- Every monetization event carries `policy_revision`, so a revenue change can be read against the policy change that caused it.
- Mapping to other tools: GameAnalytics progression uses Start, Complete and Fail with up to three hierarchy levels and business events take the amount in minor units with an ISO 4217 currency [Reported, 2026-10]. GA4 for Firebase has recommended game events such as `level_start`, `level_end`, `earn_virtual_currency`, `spend_virtual_currency` and `ad_impression` [Unverified, names to confirm in the GA4 recommended events reference]. Map ours to theirs in the export layer, never by renaming our events per tool.

### 2.1 Tracking plan excerpt (measurement format)

```json
{
  "version": 1,
  "pii_policy": "no raw email, phone, name, address or free text in any parameter; user and group ids are hashed",
  "events": {
    "level_completed": {
      "owner": "measurement",
      "destinations": ["analytics"],
      "props": {
        "product": {"type": "enum", "values": ["puzzle_app"]},
        "game": {"type": "id"},
        "mode_id": {"type": "enum", "values": ["campaign", "weekly_race"]},
        "level": {"type": "num", "min": 1, "max": 20000},
        "attempt": {"type": "num", "min": 1, "max": 1000},
        "duration_s": {"type": "num", "min": 0, "max": 7200},
        "boosters_used": {"type": "num", "min": 0, "max": 20},
        "continues_used": {"type": "num", "min": 0, "max": 20}
      }
    },
    "ad_revenue": {
      "owner": "game-monetization",
      "destinations": ["analytics", "mmp"],
      "props": {
        "product": {"type": "enum", "values": ["puzzle_app"]},
        "placement_id": {"type": "enum", "values": ["rewarded_continue", "interstitial_level_end"]},
        "ad_network": {"type": "id"},
        "value": {"type": "num", "min": 0, "max": 10},
        "currency": {"type": "enum", "values": ["USD"]},
        "precision": {"type": "enum", "values": ["exact", "publisher_defined", "estimated"]},
        "contract_version": {"type": "enum", "values": ["0.1"]},
        "policy_revision": {"type": "num", "min": 1, "max": 10000}
      }
    }
  }
}
```

Two complete plans that pass the conformance check are in `skills/game-monetization/scripts/samples/` (`aloo-tracking-plan.json`, `progression-tracking-plan.json`). Run `tracking_plan_check.py --plan ... --code src/` for code parity and `monetization_conformance.py` for policy coverage before every release that touches events.

## 3. Ad revenue per impression into the analytics tool and the MMP

| Step | What | Owner | Evidence |
|------|------|-------|----------|
| 1 | Mediation (AppLovin MAX, Unity LevelPlay, AdMob) exposes impression level revenue in its impression callback: revenue, currency, network, format, placement, precision | Game client | [Reported, 2026-10] |
| 2 | The client emits `ad_revenue` with the contract properties and forwards the same impression to the MMP through the MMP's ad revenue integration (or the mediation's server to server feed to the MMP) | Game client, measurement | [Practitioner consensus]; confirm the integration in the MMP and mediation docs |
| 3 | The MMP attributes ad revenue to the install's campaign; ROAS includes ad revenue; SKAdNetwork and AdAttributionKit values include ad revenue buckets (section 6) | Measurement, mobile-app-growth | [Practitioner consensus] |
| 4 | Ad networks that optimize on value (tROAS, value bidding) receive ad revenue as an in-app value through the MMP postbacks | Mobile-app-growth | [Practitioner consensus] |
| 5 | Monthly: estimated impression revenue vs network paid out, as a ratio per network; restate when the gap is above 5% | Measurement | Our rule |

Pitfalls: counting `ad_revenue` twice (client and server feed both forwarded); currency conversion done twice; `precision: estimated` rows treated as paid; ad revenue sent to a network for users who did not consent to ad measurement.

## 4. Server side purchase validation and refund notifications

| Store id | Validate | Refund and revocation signal | Idempotency key |
|----------|----------|------------------------------|-----------------|
| `apple` | App Store Server API transaction lookup on the server, signed transaction verified | App Store Server Notifications V2 (types such as `REFUND`, `REFUND_REVERSED`, `CONSUMPTION_REQUEST`) [Practitioner consensus; confirm names in Apple's reference] | Transaction id; subscriptions on the original transaction id |
| `google` | Google Play Developer API purchase lookup after every notification ("You must call the Google Play Developer API after receiving Real-time developer notifications") [Official, 2026-10] | Real-time developer notifications: `voidedPurchaseNotification` for refunds of one time products and subscriptions (full or quantity based partial refund); `PendingRefundReviewNotification` for chargebacks that need developer review within 24 hours; the Voided Purchases API as a pull backup [Official, 2026-10] | Purchase token and order id; check `messageId` to drop duplicate notifications [Official, 2026-10] |
| `web` (Stripe or a merchant of record) | Webhook signature verified; Checkout session or payment intent status read from the API | Refund and dispute webhooks | Payment intent or charge id |

Flow (contract section 8, runbook items 2 and 5):
1. Client calls `purchase(sku)`; on success it sends the receipt or token to the server and emits `purchase_started` only (never `purchase_completed`).
2. The server validates with the store, writes the entitlement to the grant log (idempotent on store id plus transaction key; owner `user` or `group`), then emits `purchase_completed` and `entitlement_granted` with `transaction_key`, `value` and `currency`.
3. A refund notification revokes: `purchase_refunded` (positive `value`, `reason` `refund`, `chargeback` or `store_revocation`) and `entitlement_revoked`; consumables already used are clawed back through the ledger and logged, never silently.
4. Revenue reports book refunds on the day the notification arrives ([Game KPIs](game-kpis.md) section 4); `game_kpis.py` expects the refund as negative revenue in its CSV.
5. Server events never count as player activity (a refund arrives while the player is away).
6. Sandbox and TestFlight purchases carry an environment flag and are excluded from reports.

Revenue truth order: store and Stripe payouts, then the server grant log, then the MMP, then client events. Reconcile monthly; a gap above 5% between the grant log and store reports is an incident.

## 5. Consent before SDKs

Initialization order (EEA, UK and Switzerland; also the default elsewhere):

| Step | What | Rule |
|------|------|------|
| 1 | Consent platform (CMP) shows or reads consent; IAB TCF for ad serving through Google in the EEA and UK requires a Google certified CMP | [Reported, 2026-10]; see [Consent and privacy](consent-and-privacy.md) section 4 for TCF v2.3 |
| 2 | Analytics SDK starts in the mode the consent allows (no advertising identifiers without consent) | [Consent and privacy](consent-and-privacy.md) |
| 3 | Mediation and ad SDKs initialize only after the consent signal exists and receive it (TCF string, US privacy signals) | Contract runbook item 1 |
| 4 | ATT prompt on iOS after the first value moment, never at first launch by reflex, no incentive | [Mobile measurement](../../mobile-app-growth/references/mobile-measurement-skan-aak-mmp.md) section 6 |
| 5 | MMP SDK with consent state; no IDFA read before ATT authorization | Apple 5.1.2(i) [Official, 2026-10] |
| 6 | `consent_updated` on every change; ad eligibility recomputed | Contract section 6 |

Children and families: a game that may be played by children uses only self certified family ad SDKs on Google Play, child directed treatment in ad requests and no personalized ads for under 13s; Apple's Kids Category forbids third party analytics and ads [Reported, 2026-10]. CNIL fined a game publisher EUR 3 million in 2023 over an identifier used for advertising without consent [Reported, 2026-10]. The SDK data map (what each SDK collects) feeds the App Privacy answers and the Play Data safety form; `store-submission` checks that they match.

Test: the conformance test in each game repo runs with consent denied and proves no ad request leaves the device (contract section 9, item 5).

## 6. SKAdNetwork and AdAttributionKit schema for games

Facts from Apple's WWDC25 AdAttributionKit session [Official, 2026-10]:
- Attribution windows are configurable in the app's Info.plist per ad network and per interaction type (click or view); without a configuration the defaults apply (clicks under 30 days, views under 1 day). Windows apply to install ads, not re-engagement.
- Attribution cooldown is configurable per conversion type (the session's example: 6 hours for install, 1 hour for re-engagement).
- Postbacks carry a country code when there is enough volume for similar conversions in that country.
- From iOS 18.4 an app can have overlapping re-engagement conversion windows and receive conversion tags (opt in with the `EligibleForAdAttributionKitOverlappingConversions` key).
- Development postbacks can be created in iOS Settings for testing.

SKAdNetwork 4 (still widely used): three postbacks, a fine value 0 to 63 only in the first window, coarse values after, crowd anonymity tiers [Official, see [Mobile measurement](../../mobile-app-growth/references/mobile-measurement-skan-aak-mmp.md) sections 3 and 4].

The game schema (template owned with `mobile-app-growth`; its section 5.2 is the same shape):

| Window | Value | Meaning |
|--------|-------|---------|
| 1 fine 0 to 7 | Retention and progression | Returned on day 1, tutorial complete, level thresholds reached (bit flags) |
| 1 fine 8 to 63 | Revenue | Combined IAP and ad revenue in log scaled buckets, crossed with the day 1 return flag; ad revenue from `ad_revenue` events counts |
| 1 coarse | low, medium, high | Returned on day 1; ad revenue above a threshold or level X; any IAP |
| 2 and 3 coarse | low, medium, high | Active; cumulative revenue above a threshold; payer above a high threshold |

Rules:
1. Encode what predicts D30 revenue inside 48 hours; validate monthly against Android and consented iOS cohorts (correlation of window 1 value with D30 revenue per user).
2. An ad impression tier is part of the revenue bucket, not a separate flag (64 states go fast).
3. Too many values early and too many campaigns push postbacks below crowd anonymity thresholds and null the fine value [Reported, 2026-10]; consolidate campaigns.
4. A daily game with one play a day encodes "returned on day 1" and "joined a group" before revenue; revenue arrives later.
5. Keep the schema stable for at least 4 weeks and tell every network before a change.
6. Web games have no SKAdNetwork; attribution is UTMs and click ids on the web ([UTM and channel governance](utm-and-channel-governance.md)).

## 7. Tool choice for small studios

| Tool | Fit | Watch out | Evidence |
|------|-----|-----------|----------|
| GameAnalytics | Game event model built in (progression, resource, business, ads), free tier, benchmarks, A/B tests | Its definitions (classic retention) must match ours; raw export plan for the warehouse | [Reported, 2026-10] |
| Firebase Analytics with BigQuery export | Free, Remote Config and A/B testing in the same console, raw events in BigQuery | 500 distinct event names and 25 parameters per event; events over the limits are dropped without an error [Reported, 2026-10] | [Reported, 2026-10] |
| Unity Gaming Services analytics | Unity built games, LevelPlay mediation in the same stack | Lock in to Unity services | [Reported, 2026-10] |
| devtodev | Game specific reports, payer segmentation | Free tier limits reported as up to 10,000 MAU in one source and differently in others | [Contested] |
| Amplitude, Mixpanel | Strong product analytics and funnels | Default retention uses 24 hour windows; event volume pricing | [Reported, 2026-10] |
| PostHog | Web games and PWAs, product analytics plus flags and experiments; 1 million free events a month reported | Self hosting is heavy work | [Reported, 2026-10] |
| Countly | Self hosted option | SSPL license terms | [Reported, 2026-10] |
| Snowplow | Warehouse first event pipelines at scale | Engineering effort | [Reported, 2026-10] |
| MMP: AppsFlyer, Adjust, Singular, Tenjin | Paid UA attribution, SKAdNetwork and AdAttributionKit decoding, ad revenue attribution | Free tier claims conflict (AppsFlyer Zero with 12,000 free conversions in year one; Adjust and Singular free tiers disputed; Tenjin free tier) | [Contested] |

Default stack by stage:

| Stage | Stack |
|-------|-------|
| Prototype and closed beta | GameAnalytics or Firebase free, Remote Config for the policy kill switch and tuning, crash SDK; no MMP until paid UA |
| Soft launch with paid tests | Add an MMP with ad revenue integration, SKAdNetwork and AdAttributionKit schema; BigQuery export or the analytics raw export for `game_kpis.py` |
| Scale | Warehouse as truth (BigQuery or Snowflake), the four dashboards on it, MMP cost ingestion, monthly ad revenue reconciliation |
| Web first game | PostHog or a similar first party tool, Stripe webhooks into the server, UTMs and click ids, no MMP until a store wrapper ships |

## 8. Web games

- First party collection on the game's own domain; the same event names as the apps, so a later store wrapper shares dashboards.
- Consent banner (CMP) before analytics cookies or ad scripts in the EEA and UK; Google H5 Games Ads (closed beta) and portal SDKs only after consent [Reported, 2026-10].
- Ad events: map the H5 Games Ads callbacks to the contract events (`adBreak` request to `ad_requested`, a viewed reward to `ad_rewarded`; grant only when the ad was viewed) [Reported, 2026-10].
- Purchases: Stripe or a merchant of record; the webhook is the truth; `purchase_completed` from the server.
- Identity: guest players are real records with a pseudonymous id; linking an account keeps the history (no new install in the data).
- Install: for a web game, "install" is the first play in analytics; a PWA home screen install is a separate event (`pwa_installed`) and a strong retention signal.
- Timezone: daily web games usually reset at a fixed time; use that boundary in every report ([Game KPIs](game-kpis.md) section 1).
- Bots and scrapers hit web games; filter them at ingest (user agent lists, impossible session rates) before DAU.

## 9. Release gate for game tracking

| # | Check | How |
|---|-------|-----|
| 1 | Every event in the build is in the tracking plan and every plan event is emitted | `tracking_plan_check.py --code` |
| 2 | Every offer, placement and SKU has its contract events by value, with `contract_version` and `policy_revision` | `monetization_conformance.py` |
| 3 | Captured payloads match types; no personal data | `tracking_plan_check.py --payloads` on a staging capture |
| 4 | Sandbox purchase, refund and restore tested on each store; the grant log is idempotent | Store sandbox, Stripe test mode |
| 5 | Consent denied path sends no ad request and no advertising identifier | Device proxy capture |
| 6 | `game_kpis.py` on a staging export gives the expected DAU and D1 for a scripted test cohort | Script output |
| 7 | Offline play: queued events keep their original timestamps and the server dedupes on resend | Airplane mode test |
| 8 | Test devices and reviewer demo accounts are flagged | Device list in `MEASUREMENT.md` |

A failure blocks the release through `site-engineer` (web) or `store-submission` (stores).

## 10. Sources

| # | Source | Publisher | Date | Supports |
|---|--------|-----------|------|----------|
| 1 | What's new in AdAttributionKit (WWDC25 session 221) | Apple, developer.apple.com/videos/play/wwdc2025/221 | 2025-06, read 2026-10-12 | Configurable windows, cooldown, country code, overlapping re-engagement and conversion tags, development postbacks [Official, 2026-10] |
| 2 | Real-time developer notifications reference | Android Developers, developer.android.com/google/play/billing/rtdn-reference | read 2026-10-12 | Notification types, voided purchases, chargeback review within 24 hours, must call the Developer API, `messageId` dedup [Official, 2026-10] |
| 3 | Event types | docs.gameanalytics.com | ongoing | Seven event families, progression hierarchy, business event fields [Reported, 2026-10] |
| 4 | Firebase limits and A/B testing concepts | Firebase documentation | ongoing | 500 event names, 25 parameters, silent drops [Reported, 2026-10] |
| 5 | Game analytics tool comparisons | devtodev, PostHog and vendor pages | 2025 to 2026 | Free tiers and fit [Reported, 2026-10]; [Contested] where they disagree |
| 6 | MMP pricing comparison | Airbridge | 2026 | Free tier claims [Contested] |
| 7 | Google H5 Games Ads (Ad Placement API) beta documentation | Google | 2026 | adBreak, opt in rewarded, grant on view [Reported, 2026-10] |
| 8 | CNIL decision on a game publisher | CNIL, via usercentrics summary | 2023 | Identifier without consent fine [Reported, 2026-10] |
| 9 | Google Play Families policy, self certified ads SDKs | Play Console Help | ongoing | Family ad SDK rule [Reported, 2026-10] |
| 10 | App Review Guidelines 1.3, 5.1.2 | Apple | 2026-06-08 version, read in the research pass | Kids Category, ATT and IDFA [Official, 2026-10] |
| 11 | Game Monetization Contract v0.1 | Ads Master | 2026-10 | Event names, properties, grant log, runbook |
