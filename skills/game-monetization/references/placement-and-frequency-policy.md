# Placement and Frequency Policy

> Knowledge as of 2026-10 (research pass 2026-10-12). Starting values below are vendor guidance and practitioner patterns seen in search summaries ([Reported, 2026-10]); none is a target. Each game reads its own tests with D1 and D7 as guard rails. Placements live in the policy file (`placements`) and are checked by `monetization_check.py`; event coverage is checked by `monetization_conformance.py`. A change to a live placement, cap or cooldown is G3.

## 1. Format rules (enforced by the checker)

| Format | Rules the policy must state | Checker result when missing |
|--------|-----------------------------|-----------------------------|
| Rewarded | `grants` (typed), `optIn: true`, `grantOn: "completed"`, a `dailyCap` | FAIL without grants, opt in or grant on completion; WARN without a daily cap |
| Interstitial | `graceLevels` or `graceSeconds`, `cooldownSeconds`, `sessionCap`; `resetAfterRewardedSeconds` recommended | FAIL without grace, cooldown or session cap; FAIL in kids mode |
| Banner | `point` is `on_menu` or `on_loading` | FAIL anywhere else (never in play) |
| App open | Allowed with a warning | WARN always (no public evidence for games yet); FAIL in kids mode |
| Native | Allowed | No format specific rule; treat like a banner for placement |

Grants in a rewarded placement follow the mode rules: in a ranked mode a rewarded ad may grant only cosmetics, access or a pass; it never grants an attempt, moves, time, boosters, currency, lives or streak protection, and never writes to a ranked board.

## 2. Starting values (to test, not to copy)

| Setting | Starting range seen | Source and label | The progression sample uses |
|---------|--------------------|------------------|----------------------------|
| First interstitial | After level 3 to 8, or 60 to 90 seconds; or skip the whole first session | Unity guidance and the 2026-10-12 placement template [Reported, 2026-10] | `graceLevels: 8` |
| Interstitial cooldown | 2 to 3 minutes; casual games often start at one per 60 to 90 seconds | Same [Reported, 2026-10] | `cooldownSeconds: 150` |
| Interstitials per session | 4 to 6 | Same [Reported, 2026-10] | `sessionCap: 5` |
| Pause after a rewarded view | Reset the interstitial timer; one template suppresses interstitials for 10 minutes after a rewarded view | Same [Reported, 2026-10] | `resetAfterRewardedSeconds: 600` |
| Rewarded per day | Capped and paced; no public number | [Reported, 2026-10] | `dailyCap: 5` |
| Test length | At least 7 days on ARPDAU with D1 and D7 as constraints | Unity guidance [Reported, 2026-10] | |

Color Block Jam was reported to keep early levels almost ad free and add interstitials after levels later (Mobidictum citing AppMagic, Q1 2025) [Unverified]; hybrid casual games broadly hold ads back early [Reported, 2026-10].

## 3. Rewarded placement catalog

| Placement | Mode | Grant | Fit | Notes |
|-----------|------|-------|-----|-------|
| Continue or revive after a fail | progression | `moves`, `time` | High | The free path next to the paid continue; capped per day |
| Reward multiplier at level end | progression | `currency` | High | Reported as the most popular rewarded placement in puzzle games (Unity and ironSource) [Unverified, vendor claim] |
| Boost before a level | progression | `booster` | Medium | Teach the booster first; one per attempt |
| Daily bonus doubler | progression | `currency`, `cosmetic` | Medium | Once a day |
| Uncounted replay after the counted tries | practice | `access` | High in daily ranked products | Never a counted try |
| Unlock an archive level for a day | practice | `access` | Medium | The subscription sells unlimited access |
| Cosmetic unlock | any | `cosmetic` | Low to medium | Safe in ranked products |

Value rule: a rewarded view grants a small, temporary benefit; IAP sells the larger or permanent one (Supersonic guidance) [Unverified, vendor guidance]. Payers watch rewarded ads too [Unverified], so ad removal usually keeps rewarded.

Visibility rule: low impressions per DAU with high usage among those who see the entry point means the entry point is hard to find (LevelPlay documentation) [Unverified, vendor guidance]. Fix the entry point before adding placements.

## 4. Interstitial placement rules

1. Only at natural breaks: level end, returning to the map, between rounds. Google Play's interstitial policy as summarized in the notes requires natural breaks, no ad before the splash screen and a closable ad (2023 era summary, recheck) [Unverified].
2. Never inside an attempt, never during a counted try, never between a fail and the continue offer (the player must be able to decide without an ad in the way).
3. Never right after a purchase or a rewarded view (reset timer).
4. Never on the first session of a new install unless a test proves no D1 cost.
5. Payers see fewer or no interstitials; an ad removal buyer sees none.
6. In web games, full screen ads appear only at transitions through the ad API's break call (Google H5 Games Ads `adBreak()`) [Reported, 2026-10].

## 5. Banners

1. Menus and real loading screens only (`on_menu`, `on_loading`); never in play, where they cause accidental taps and complaints.
2. Never overlapping controls or the safe area; the app team checks with the smallest supported phone.
3. Low revenue: Appodeal's Q4 2024 report put banners around $0.4 iOS and $0.5 Android eCPM, against about $13.6 and $9.0 for rewarded [Unverified, vendor report]. Decide whether a banner's revenue is worth its clutter with the game's own numbers.

## 6. What we never ship

| Pattern | Why |
|---------|-----|
| An interstitial after every level stacked with rewarded prompts | Listed as a pattern not to copy in the teardown notes, even though Segwise reported Screwdom earning over $75M in IAP in 2025 with an interstitial after every level [Unverified]; it trades D7 and reviews for short term ARPDAU |
| Ads that interrupt a counted attempt | Changes a ranked result |
| A rewarded ad for a counted try | Unequal access (fill, ATT, consent, ad blockers) and money adjacent advantage |
| Ad SDK calls before consent | Consent order (see [Ad monetization](ad-monetization-and-mediation.md) section 7) |
| Banners in play | Accidental taps |
| Fake close buttons, delayed close beyond the network default, auto redirects | Store policy and complaints |
| "Watch to support us" copy on the web | Not allowed in Google's H5 Games Ads rules for rewarded [Reported, 2026-10] |

## 7. Expected impressions per DAU (planning arithmetic)

Use the decomposition to set expectations before a test; then measure.

```
impressions per DAU (placement) = sessions per DAU
                                 x eligible moments per session
                                 x show rate (eligible moments that pass grace, cooldown and caps)
                                 x opt in rate (rewarded only)
                                 x fill rate
ad revenue per DAU (placement)  = impressions per DAU x eCPM / 1000
```

Illustration with placeholder values (not benchmarks): 4 sessions per DAU x 3 level ends per session x 0.35 show rate after grace and cooldown x 0.9 fill = 3.8 interstitial impressions per DAU; at a $5 eCPM that is $0.019 per DAU. The same game with a session cap of 5 cannot exceed 20 per DAU, so the cap is rarely the binding constraint in short session games; the cooldown is.

Session context: GameAnalytics data summarized in the notes put the median session at 5 to 6 minutes with about 4 sessions a day [Reported, 2026-10]; read the game's own numbers from measurement.

## 8. Testing a placement change

| Step | Rule |
|------|------|
| Hypothesis | One change per test: a cooldown, a grace, a cap, a new placement, a grant amount |
| Design | Random split by user, holdout kept; staged rollout by remote config; the new value raises `policyRevision` |
| Primary metric | ARPDAU (total, not ad only), read by `policy_revision` |
| Guard rails | D1 and D7 (measurement's definitions), session length, sessions per DAU, refund and complaint rate, store rating trend |
| Length | At least 7 days; D7 needs 7 days after exposure; full weeks; never stop early on a good day |
| Decision | Ship only when ARPDAU rises and no guard rail breaches its stop rule |
| Record | EXPERIMENTS.md row, journal entry, memory only when confirmed by a second read |

## 9. Placement spec template

```json
{ "id": "level_end_interstitial", "format": "interstitial", "point": "on_level_end", "mode": "levels",
  "graceLevels": 8, "cooldownSeconds": 150, "sessionCap": 5, "resetAfterRewardedSeconds": 600 }
```

| Field | Value |
|-------|-------|
| Placement id (also the mediation ad unit name) | |
| Format, point, mode | |
| Grants (rewarded) and daily cap | |
| Grace, cooldown, session cap, reset after rewarded (interstitial) | |
| Audience exclusions (payers, ad removal buyers, kids mode, first session) | |
| Consent dependency | No request before consent |
| Events covered (`monetization_conformance.py`) | `ad_requested`, `ad_shown`, `ad_rewarded` for rewarded; `ad_shown` for the rest |
| Expected impressions per DAU (section 7) | |
| Remote config keys and kill switch | |
| Test plan and stop rule | |

## 10. Remote config and the kill switch

1. Every frequency value (grace, cooldown, caps, reset) is a remote config value read through the policy, never a constant in code (contract runbook item 4).
2. The policy's `killSwitch` key turns every offer and placement off within minutes, without a release (contract runbook item 3). Test it before launch and after every SDK update.
3. A remote config change in production is a G3 change; the same approval rules apply as for a release.
4. Rollback means restoring the previous `policyRevision`, not editing values by hand.

## 11. Quick checklist

- [ ] Every placement in the policy has an ad unit with the same id in the mediator.
- [ ] Rewarded: typed grants legal for the mode, opt in, granted on completion by the server, daily cap.
- [ ] Interstitial: grace, cooldown, session cap, reset after rewarded; natural breaks only; none in kids mode.
- [ ] Banners on menus and loading screens only.
- [ ] No ad inside a counted attempt or between a fail and its continue offer.
- [ ] Payers and ad removal buyers excluded from interstitials.
- [ ] Events covered; conformance passes; kill switch tested.
- [ ] Every change tested 7 days or more with D1 and D7 guard rails.
