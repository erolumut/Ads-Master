# Ad Monetization and Mediation

> Knowledge as of 2026-10 (research pass 2026-10-12). The ad tech findings came from search summaries and vendor pages only: market shares, payout terms and eCPMs are [Reported, 2026-10] at best and often single vendor claims [Unverified]. Mediation platforms change adapters, bidding partners and terms every quarter, so run the Freshness protocol in the skill before choosing a stack or quoting a term. Changing ad units, floors, networks or frequency in a live mediation account is G3.

## 1. Do ads fit this game?

Ad revenue per DAU is the sum over placements of impressions per DAU times eCPM divided by 1,000 (measurement's `game-kpis` dictionary; for example 1.5 impressions per DAU at a $4 eCPM gives $0.006 per DAU). That makes three questions decide fit:

| Question | Ads fit | Ads fit poorly |
|----------|---------|----------------|
| Are there natural breaks? | Level ends, retries, menus, between rounds | One short daily session, a continuous match, ranked play where an interruption changes a result |
| Where are the players? | Growing markets, where reported ad shares of game revenue run 55% to 70% [Unverified, secondhand] | US, Canada, Korea and Japan, where IAP is reported at 77% to 90% of revenue [Unverified, secondhand] |
| Does an ad view have something fair to grant? | Continues, multipliers, boosts in progression; uncounted replays in ranked products | Only a counted try (never allowed) |

Market context (search level): mobile game ad revenue about $12 billion in 2025 with puzzle and arcade over 65% (Sensor Tower via gamedevreports) [Reported, 2026-10]; game ad spend up about 8% in H1 2026 while mobile IAP fell about 2% (PocketGamer.biz) [Reported, 2026-10]; game ad revenue in Q2 2026 split 55% Android, 45% iOS in one vendor's data (Tenjin) [Unverified]. IAP first hybrids were reported to out earn ads first hybrids about 4x (secondhand from Deconstructor of Fun, 2024-12) [Unverified].

## 2. Choose one mediator

Run one mediation platform per app. Two mediators split demand and double SDK weight.

| | AppLovin MAX | Google AdMob | Unity LevelPlay |
|---|--------------|--------------|-----------------|
| Position | Reported market leader with over 50% mediation share in 2025 (PocketGamer.biz, PPC Land) [Reported, 2026-10] | Easiest start; Open Bidding results are net of Google's share [Reported, 2026-10] | Common in Unity built games [Reported, 2026-10] |
| Strength | Reported yield on rewarded and interstitial in tier 1 markets; built in A/B testing; Ad Review for creative quality [Reported, 2026-10] | Simple setup, Google demand, InMobi, ironSource and Unity bidding added 2025-07-07 [Reported, 2026-10] | Integrated with Unity tooling |
| Payout terms seen | AppLovin earnings: $100 minimum, Net 15 [Reported, 2026-10] | Not captured in the 2026-10-12 notes | Unity Ads: Net 60, $100 [Reported, 2026-10] |
| Watch | Litigation: AppLovin sued Unity on 2026-09-29 over the Ad Quality SDK in LevelPlay (ongoing) [Reported, 2026-10] | Net of share reporting makes eCPMs look lower than gross | Same litigation; check adapter support after any ruling |

Decision rules:
1. A small team with a first ad placement: AdMob, unless a vendor comparison on the game's own traffic says otherwise.
2. A game where ad revenue is a large share of ARPDAU in tier 1 markets: test MAX against the current stack with the platform's own A/B tool, reading ARPDAU and D1, D7, not eCPM alone.
3. A Unity built game with an existing LevelPlay integration: keep it unless a test shows a gap worth the migration.
4. Never switch mediators during a soft launch read, a season launch or a store featuring window.

## 3. Bidding first

1. Bidding (in app header bidding) first: every bidding network competes on each impression.
2. Waterfall line items only to fill gaps where bidding demand is thin (a country, a format).
3. No duplicate demand: a network should not appear both as a bidder and as a waterfall line for the same unit without a reason recorded in the journal.
4. Floors are tested, never set from an article; a floor change is G3 and gets an experiment row.

## 4. Networks and fit

Networks commonly named for games in 2025 to 2026 [Reported, 2026-10]: Google, Meta Audience Network, Unity, AppLovin, Mintegral (strong in playables and APAC), Moloco, Liftoff (Net 60 reported), Pangle (check region availability), with InMobi and DT Exchange as optional additions.

| Step | Networks to add | Why |
|------|-----------------|-----|
| Start | The mediator's own demand plus Google and one or two bidders | Fewer SDKs, faster review, cleaner reads |
| Growth | Add bidders that matter for the game's top 5 countries | Competition per impression |
| Scale | Fill specialists for weak countries or formats | Fill gaps without slowing the app |

Add one network at a time and read for at least 7 days: ARPDAU, fill rate, latency, crash rate, D1.

## 5. Payout terms and cash flow

| Source | Term seen | Label |
|--------|-----------|-------|
| AppLovin | $100 minimum, Net 15 | [Reported, 2026-10] |
| Unity Ads | $100 minimum, Net 60 | [Reported, 2026-10] |
| Liftoff | Net 60 | [Reported, 2026-10] |
| CrazyGames (web portal) | EUR 100 minimum via Tipalti | [Reported, 2026-10] |

Payout thresholds delay revenue for tiny apps: at a few dollars a day an account can wait months to clear a $100 minimum. Plan cash on payment dates, not on mediation dashboards, and record each network's term in `memory/game-monetization.md` after reading it in the live account.

## 6. SDK size and performance

| Rule | Detail |
|------|--------|
| Measure per adapter | Build with and without each adapter; record download size, install size, cold start time and crash rate |
| Budget | Set an app size budget with the app team before adding networks; anecdotes in the notes mention a 13 MB bundle and about 3.8 MB per network [Unverified] |
| Initialization | Lazy init after consent and after the first screen is usable; never block the first frame on ad SDKs |
| Vitals | A crash or ANR rise after an SDK update is an incident (Google Play bad behavior thresholds: 1.09% user perceived crash rate and 0.47% ANR rate overall [Official, 2026-10]) |

## 7. Consent order

Consent comes before any ad SDK call. This is the order the product implements (contract runbook item 1) and the order `store-submission` checks:

1. App start: no ad SDK initialized, no advertising identifier read.
2. Region known (from the store country or a privacy safe lookup).
3. EEA and UK: show a Google certified CMP using the IAB TCF. Google required certified CMPs for its ad products in these regions, and TCF v2.3 had a deadline around 2026-03-01 after which non compliant strings get Limited Ads [Reported, 2026-10].
4. US states with privacy laws: honor opt out signals in the CMP or the mediator's privacy settings (`measurement` and `compliance` own the state by state detail).
5. iOS: show the ATT prompt only after the player has seen value, never with incentives; no IDFA read before ATT. Reported gaming opt in rates disagree widely by method: 51% (AppsFlyer, Q1 2024), 35% (Adjust, Q2 2025), 13.85% (Singular, Q2 2024) [Contested].
6. Pass consent state to the mediator, then initialize it; the mediator passes it to networks.
7. Under 13 or unknown age where required: child directed treatment, no personalized ads, and in Google Play's Families program only self certified ads SDKs, with ad content rated no higher than G [Reported, 2026-10].
8. Record every change as `consent_updated`.

Why it matters: CNIL fined a game publisher EUR 3 million in 2023 over advertising use of an identifier without consent [Reported, 2026-10]; Italy's AGCM fined Apple EUR 98.6 million in December 2025 in a case about double consent prompts [Reported, 2026-10].

## 8. Ad quality and safety

| Control | Rule |
|---------|------|
| Category blocks | Block gambling, adult, dating and alcohol categories for any audience with minors; block real money gambling everywhere unless the human decides otherwise with compliance |
| Max ad content rating | Match the game's audience (G for child directed traffic) |
| Creative review | Use the mediator's ad quality tool where it exists (AppLovin Ad Review [Reported, 2026-10]); keep a player report path |
| Competitor ads | Decide once whether direct competitors may advertise; record it in `DECISIONS.md` |
| Redirects and auto store opens | Report and block; they drive complaints and store reviews |

## 9. Impression level revenue

Revenue per impression from the mediator (impression level revenue data) goes to analytics and the MMP as `ad_revenue` with `placement_id`, network, value, currency and precision (contract section 6). `measurement` owns the pipeline (`game-tracking`); this agent owns the placement ids and checks coverage with `monetization_conformance.py`. Mediation reported eCPM and paid out revenue differ; reconcile monthly ([Benchmarks and reading results](benchmarks-and-reading-results.md) section 8).

## 10. Native apps, web and PWAs

Native mediation SDKs do not run inside a PWA or a plain web game; web games use web ad products (Google's H5 Games Ads, portal SDKs, web rewarded vendors) [Unverified]. A Capacitor or TWA wrapper can bridge native SDKs, which brings the native consent, ATT and Data safety duties with it. See [Web game monetization](web-game-monetization.md).

## 11. Kids and families

| Situation | Rule |
|-----------|------|
| Kids mode in the policy (`audience.kidsMode: true`) | No interstitials and no app open ads (`monetization_check.py` fails them); no personalized ads; certified SDKs only |
| Apple Kids Category | No third party analytics or advertising, a parental gate for links and purchases (Guidelines 1.3 and 5.1.4) [Official, 2026-10] |
| Google Play target audience includes children | Families policy: self certified ads SDKs, child directed treatment [Reported, 2026-10]; since 2026-08-26 anonymous chat apps may not target children [Official, 2026-10] |
| Age unknown | Treat as the youngest bracket the product allows until an age signal exists |

## 12. Mediation setup checklist

- [ ] One mediator; choice and reason in `DECISIONS.md`.
- [ ] Bidding networks first; any waterfall line has a recorded reason.
- [ ] Ad unit per placement id (the policy file's ids), so revenue reads per placement.
- [ ] Consent order implemented and tested with consent denied (no ad request leaves the device).
- [ ] Category blocks and max content rating set for the audience.
- [ ] `ad_requested`, `ad_shown`, `ad_rewarded`, `ad_failed`, `ad_revenue` and `consent_updated` in the tracking plan; `monetization_conformance.py` passes.
- [ ] Rewarded reward granted by the server after the network's completion callback where the network offers one, never by the client alone (contract runbook item 2).
- [ ] Payout terms and thresholds read in each live account and recorded in memory.
- [ ] SDK size and cold start measured per adapter.
- [ ] Kill switch turns every placement off without a release.

## 13. Change request lines for ad settings

Example rows; the values are illustrative, not findings.

| # | Platform | Entity | Change | From | To | Reason with data | Expected effect | Risk | Rollback | Gate |
|---|----------|--------|--------|------|----|------------------|-----------------|------|----------|------|
| 1 | Mediator (live account) | Rewarded unit `double_coins` | Add a bidding network | not present | present | Fill below own 8 week median in the top 2 countries, 2026-09-14 to 2026-10-11 export | Fill up, ARPDAU up on that placement | Crash rate, size | Disable the network | G3 |
| 2 | Policy file | `level_end_interstitial.cooldownSeconds` | Raise cooldown | 150 | 180 | D7 down 0.4 points in test cell, same revenue | D7 back to control | Lower ad ARPDAU | Previous `policyRevision` | G3 |

Every line names the policy revision it creates and the experiment row that reads it.
