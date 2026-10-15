# Segmentation and Payment Operations

> Knowledge as of 2026-10 (research pass 2026-10-12). Segment shares come from single vendor sources ([Unverified]). Legal points are summaries for routing work, not legal advice: `compliance` gives the verdict per market and the human decides. Provider notification names in section 6 are from provider documentation known before this pass and were not re-read on 2026-10-12 ([Unverified]); confirm them in the current docs before building. Refund decisions, account actions and any change to live purchase flows are G3.

## Part A. Payer segmentation without manipulation

## 1. Why segment at all

Segmentation exists to show each player what is relevant to them and to protect them, never to find out how much more someone can be made to pay. Revenue in games is concentrated: one source says 1% to 2% of players ("whales") drive 50% to 70% of IAP revenue [Unverified]; payer conversion is commonly cited at 2% to 5% [Unverified, vendor claim]. Concentration is a fact to read, not a target to push.

## 2. Tiers (the contract's `payerTier`)

The contract's `OfferContext.payerTier` takes `none`, `low`, `mid` or `high`. Compute it on the server from the game's own data:

| Tier | Rule (set per game from its own distribution) | Typical use |
|------|-----------------------------------------------|-------------|
| `none` | No purchase in the trailing 90 days | Starter pack eligibility, rewarded first |
| `low` | Spend below the P50 of payers in the trailing 90 days | Core rung offers |
| `mid` | P50 to P90 of payers | Value rung, pass |
| `high` | Above P90 of payers | Fewer interruptions, support priority; never more pressure |

Percentile cutoffs per game rather than fixed money bands follow devtodev's segmentation approach [Unverified]. Store the cutoffs and the date computed in `memory/game-monetization.md`; recompute quarterly.

## 3. What segmentation may and may not change

| May change | May never change |
|------------|------------------|
| Which offer appears at a moment (relevance) | The price of the same item in the same market (no personalized prices) |
| Whether a starter pack is offered (non payers) | Odds of any random item |
| Ad load: fewer or no interstitials for payers and ad removal buyers | Difficulty or level content (game design, the game repo) |
| Support priority and refund handling speed | Pressure copy, countdowns or extra offers aimed at high spenders |
| Message frequency (fewer for heavy spenders) | Targeting by vulnerability signals: late night sessions, loss streaks, sudden spend velocity, stated age under 18 |
| Inclusion in tests | Inclusion of minors in any spend segment |

Personalized pricing based on automated decision making must be disclosed to EU consumers under the consumer rights rules added by the Omnibus Directive [Practitioner consensus; compliance confirms]. The house rule is simpler: no personalized prices at all.

## 4. Spend protections

| Protection | Basis | Implementation |
|------------|-------|----------------|
| Parental consent for purchases under 16 (US) | FTC v Cognosphere (Genshin Impact), January 2025, USD 20 million: no purchases under 16 without parental consent, real cost shown, odds disclosed [Reported, 2026-10] | Age signal plus parental approval flow; store family purchase controls where they exist |
| Parental purchase approval on game platforms (Turkey) | Law 7578, passed 2026-04-22; duties mostly start about 6 months after the implementing regulation (verify) [Reported, 2026-10] | Same flow, Turkish copy, compliance verdict |
| Protect children, no direct buy appeals to children | EU CPC key principles on in-game virtual currencies, 2025-03-21 [Reported, 2026-10] | Copy rules, no countdowns with minors (`monetization_check.py`) |
| No paid random items for minors | Brazil Law 15.211/2025 [Reported, 2026-10] | `monetization_check.py` fails random items with an audience under 18 |
| Optional spend limits | House rule | A player set monthly cap, honored on the server |
| High spend care | House rule | A spend velocity alert goes to support as a duty of care check, never to an offer engine |

## 5. Data rules

1. Tiers are computed server side from aggregated purchase history; analytics receives the tier, not the spend.
2. No names, emails or payment details in analytics or in `ads-master/` (measurement's tracking plan rules: ids hashed, no free text).
3. Tier changes are not events sent to ad networks.

## Part B. Payment operations

## 6. The grant ledger and provider notifications

The server keeps one ledger of entitlements (contract section 5): grants are idempotent on (store id, transaction key), subscriptions key on the original transaction id so a renewal never grants twice, revocations are logged and never deleted, and admin grants (a try handed back after a crash, compensation) are ledger entries too, never silent database edits.

| Provider | Purchase truth | Refund and dispute signals (confirm names in current docs) | Contract events |
|----------|---------------|------------------------------------------------------------|-----------------|
| Stripe (web) | Verified webhook after payment | `charge.refunded`, `charge.dispute.created`, `charge.dispute.closed` [Unverified] | `purchase_completed`, `purchase_refunded`, `entitlement_granted`, `entitlement_revoked` |
| Apple | Server side transaction validation | App Store Server Notifications V2: `REFUND`, `REFUND_REVERSED`, and `CONSUMPTION_REQUEST` (Apple asks for consumption information before deciding a consumable refund) [Unverified] | Same |
| Google Play | Server side purchase verification | Real-time developer notifications and the Voided Purchases API for refunds and chargebacks [Unverified] | Same |

The contract names the channel for each (Stripe webhooks, App Store Server Notifications, Play Real-time developer notifications); `monetization_conformance.py` fails a catalog item that has no `purchase_refunded` coverage in the tracking plan.

## 7. Refund handling

1. Every refund notification revokes the entitlement in the ledger within minutes and emits `purchase_refunded` and `entitlement_revoked`.
2. Non consumables and subscriptions: access ends; earned progress that did not come from the refunded item stays.
3. Season passes: the pass and its unclaimed rewards end; claimed cosmetic rewards are removed only if the product's terms said so before purchase.
4. The player sees what changed and why, in plain words, in the game.
5. Answer Apple consumption requests truthfully from the ledger (what was delivered and used) [Unverified mechanism; confirm].
6. Weekly: refund rate by SKU, store and country against the game's own trailing 8 weeks.

## 8. Consumable clawback

| Situation | Rule |
|-----------|------|
| Refunded currency not yet spent | Remove it; bought currency is clawed back before earned currency |
| Refunded currency already spent | Record the shortfall in the ledger; do not remove earned currency or unrelated items to cover it; block new purchases only after repeated abuse |
| Refunded boosters or moves already used | Log it; the level result stands (single player progression) |
| Refunded group round already played | The round stays in every member's history; the buyer's refund is logged; repeated abuse blocks that buyer from buying rounds (contract runbook item 5) |
| Refund of an item that granted to a group | Never claw back from the other members |

Never punish a dispute beyond the refunded item (for example by locking the account and everything bought in it). The regulation notes list punishing disputes and one tap charges among the never do items, next to the FTC v Epic settlement (2022: USD 245 million in refunds over dark patterns and USD 275 million over COPPA) [Reported, 2026-10].

## 9. Chargebacks

| Step | Action |
|------|--------|
| Receive | Dispute webhook or store notification; revoke as for a refund |
| Evidence | Ledger extract (grant time, item, use), purchase confirmation shown, terms accepted; no personal data beyond what the provider requires |
| Respond | Within the provider's deadline; the human submits (G3) |
| Learn | Chargeback rate by SKU and country; a cluster on one SKU usually means unclear copy or an accidental purchase path |

## 10. Withdrawal rights and consumer law

| Topic | Rule | Basis | Owner |
|-------|------|-------|-------|
| EU digital content withdrawal | The 14 day withdrawal right falls away for digital content delivered at once only with the buyer's prior express consent and acknowledgment, confirmed on a durable medium | Consumer Rights Directive Art. 16(m) as amended by the Omnibus Directive [Practitioner consensus, not re-read in this pass] | compliance |
| EU withdrawal function | For distance contracts concluded online that keep a right of withdrawal, a "withdraw from contract here" function from 2026-06-19 | Directive (EU) 2023/2673; compliance rule SUB-EU-01 (label and source in the compliance skill) | compliance, site-engineer |
| Virtual currency and withdrawal | Withdrawal rights are named in the EU CPC key principles on in-game virtual currencies | [Reported, 2026-10] | compliance |
| Turkey distance contracts | Turkish consumer law has its own distance contract rules | Not researched in this pass; compliance confirms | compliance |
| Store purchases | Apple and Google run their own refund processes; the game honors their outcome | Store terms | Product |

## 11. Restore and cross platform entitlements

1. Subscriptions show Restore (or a sign in that restores) on the paywall (Apple Guideline 3.1.2) [Official, 2026-10]; `store-submission` checks restore for every restorable item.
2. Items bought on one platform unlock on another only through the account; items that unlock content inside the iOS app are also sold there as IAP (Guideline 3.1.3(b)) [Official, 2026-10].
3. Restore calls the adapter's `restore()`, then the server re-grants from the ledger; the client never grants.

## 12. Metrics this module reports

| Metric | Definition source | Healthy logic |
|--------|-------------------|---------------|
| Refund rate | measurement's `game-kpis` section 2 (value and count, by store and purchase month); report it once `METRICS.md` carries the project's definition | At or below the game's own trailing 8 weeks; any SKU above 2x its own median is a finding (house heuristic) |
| Chargeback rate | Same | Same |
| Complaint rate | measurement's `game-kpis` section 2: monetization complaints (tagged tickets, 1 and 2 star payment or ads reviews, chargebacks) per 1,000 DAU per week | Flat or falling after every monetization change |
| Grant reconciliation gap | Store and Stripe completed transactions without a ledger grant, and the reverse | Zero; any gap is an incident |

## 13. Operations runbook

| Cadence | Check | Stop condition |
|---------|-------|----------------|
| Daily | Refunds, chargebacks, failed grants, receipts without grants | Grants without a receipt, a receipt without a grant, duplicate grants: incident in `INCIDENTS.md`, kill switch on the affected offer |
| Weekly | Refund and chargeback rate by SKU, store, country; complaint themes | A rate above 2x its trailing median on a SKU (house heuristic): pause that offer (G3) and investigate copy and flow |
| Monthly | Reconcile store reports, Stripe payouts, mediation payouts and analytics revenue | An unexplained gap above the threshold set in `METRICS.md` |
| Quarterly | Recompute payer tier cutoffs; review spend protections per market | A new law in a market the product sells in |

## 14. Quick checklist

- [ ] Payer tiers computed server side from percentiles; no personalized prices.
- [ ] No targeting by vulnerability signals; minors never in spend segments.
- [ ] Parental approval where the law asks (US under 16 guidance from the Genshin settlement, Turkey Law 7578).
- [ ] Ledger idempotent; refunds and disputes revoke; clawback rules written and shown to players.
- [ ] Every catalog item has `purchase_completed` and `purchase_refunded` coverage (`monetization_conformance.py`).
- [ ] Withdrawal flow per market reviewed by compliance.
- [ ] Daily, weekly and monthly reconciliation running.
