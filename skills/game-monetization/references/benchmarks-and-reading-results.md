# Benchmarks and Reading Results

> Knowledge as of 2026-10 (research pass 2026-10-12). Every benchmark below came from search summaries, vendor reports or secondhand coverage: none is [Official] and most are [Unverified]. They vary by genre, country, platform, season and traffic mix. Compare a game with its own history first and benchmarks second. Metric definitions belong to `measurement` (`game-kpis` in the measurement skill); this module repeats the decomposition only to locate a change, and if anything here differs from `game-kpis`, `game-kpis` wins.

## 1. Rules for every number

1. Definitions come from `ads-master/METRICS.md` and measurement's `game-kpis`. Never redefine DAU, retention, ARPDAU, payer conversion or ARPPU in a monetization report.
2. Every figure names its source (export, connector, dashboard) and its date range, timezone and whether revenue is gross or net of store fees, tax and refunds.
3. Ratios roll up from summed numerators and denominators; never average ARPDAU across days or countries.
4. D1 and D7 are guard rails on every monetization change: a revenue win that breaks a guard rail stop rule is not a win.
5. Benchmarks are context in a footnote, never the target in a plan.

## 2. The decomposition tree

Use the tree to find which factor moved. The identities are measurement's (the `game-kpis` dictionary lists ARPDAU = IAP + ad, ARPDAU = payer share x ARPPU for the matching period, and ad ARPDAU = impressions per DAU x eCPM / 1000).

```
ARPDAU (net)
  = IAP ARPDAU + ad ARPDAU
IAP ARPDAU
  = daily payer share (payers today / DAU) x daily ARPPU (IAP net revenue today / payers today)
  daily payer share  <- offers shown per DAU x acceptance rate x purchase completion rate
  daily ARPPU         <- SKU mix x price x purchases per payer, minus refunds
ad ARPDAU
  = sum over placements of (impressions per DAU x eCPM / 1000)
  impressions per DAU <- sessions per DAU x eligible moments x show rate x opt in (rewarded) x fill
  eCPM                <- country mix x platform x format x demand (bidders) x seasonality
```

Read the tree top down, and stop at the first factor that moved more than its own normal weekly variation.

## 3. Per placement economics (one row per placement id)

| Placement | Format | Eligible DAU share | Show rate | Opt in (rewarded) | Fill | Impressions per DAU | eCPM | Ad revenue per DAU | D1 and D7 vs holdout |
|-----------|--------|--------------------|-----------|-------------------|------|---------------------|------|-------------------|----------------------|

Sources: mediation reports by ad unit (the ad unit name equals the policy placement id), `ad_requested`, `ad_shown`, `ad_rewarded`, `ad_failed` and `ad_revenue` events, measurement's DAU. Fill = shown / requested; show rate = requested / eligible moments.

## 4. Per offer economics (one row per offer id)

| Offer | Point | Mode | Shown per DAU | Acceptance (accepted / shown) | Completion (completed / started) | Revenue per shown | Refund rate | Complaints |
|-------|-------|------|---------------|-------------------------------|----------------------------------|-------------------|-------------|------------|

Sources: `offer_shown`, `offer_accepted`, `offer_declined`, `purchase_started`, `purchase_completed`, `purchase_refunded`. Revenue per shown is the number that compares offers at different points fairly.

## 5. Benchmarks (context only)

| Metric | Value | Source and date | Label | Caveat |
|--------|-------|-----------------|-------|--------|
| ARPDAU, hybrid casual | $0.15 to $0.50, IAP 40% to 60% of revenue | Vendor material in the 2026-10-12 notes | [Unverified, vendor claim] | Genre mix and tier 1 share unknown |
| ARPDAU, casual and puzzle | $0.03 to $0.10 | Vendor material | [Unverified, vendor claim] | Same |
| IAP share that works in hybrid casual | About 60% IAP (Supersonic); hybrids at 70/30 or 60/40 IAP to ads (Deconstructor of Fun, 2024-12) | Supersonic, Deconstructor of Fun | [Unverified] | Opinion pieces with examples |
| IAP share by market | Growing markets 55% to 70% ad revenue; US, CA, KR, JP 77% to 90% IAP | Secondhand | [Unverified] | Source chain unclear |
| Payer conversion | 2% to 5% | Unity | [Unverified, vendor claim] | Cohort vs daily not stated |
| Revenue concentration | 1% to 2% of players drive 50% to 70% of IAP | One source | [Unverified] | Single source |
| Rewarded eCPM (Q4 2024) | About $13.6 iOS, $9.0 Android | Appodeal Q4 2024 report | [Unverified, vendor report] | One mediator's traffic |
| Interstitial eCPM (Q4 2024) | About $10.4 iOS, $9.6 Android | Same | [Unverified, vendor report] | Same |
| Banner eCPM (Q4 2024) | About $0.4 iOS, $0.5 Android | Same | [Unverified, vendor report] | Same |
| US rewarded eCPM | $19.63 iOS, $16.49 Android | MonetizeMore, undated | [Unverified] | Undated |
| Regional eCPM ranges | Western Europe iOS $5 to $12; Brazil Android $1 to $3; India Android $0.30 to $1 | MWM, 2026 | [Unverified] | Format not always stated |
| Web rewarded CPM claims | $8 to $28 US | Web ad vendors | [Unverified, vendor claim] | Sales material |
| Mobile game ad revenue | About $12 billion in 2025; puzzle and arcade over 65% | Sensor Tower via gamedevreports | [Reported, 2026-10] | Market estimate |
| Market direction H1 2026 | Mobile IAP about minus 2% (about $40 billion); game ad spend about plus 8% | PocketGamer.biz | [Reported, 2026-10] | Half year |
| Ad revenue by platform Q2 2026 | 55% Android, 45% iOS | Tenjin, 2026-08 | [Unverified, vendor] | Tenjin customers only |
| Royal Match lifetime revenue per download | About $34 | Naavik | [Unverified] | An outlier at the top of the genre |
| Royal Match revenue 2024 | About $1.4 billion | Business of Apps | [Unverified] | Estimate |
| Season pass effect | Plus 31% revenue in the first 30 days after Royal Match added a pass (2021) | Naavik | [Unverified] | One game, one launch |
| Retention context (guard rails, owned by measurement) | Median D1 about 22% (top quartile 26% to 28%), median D7 3.4% to 3.9%, D30 about 0.7% | GameAnalytics 2025 benchmarks via gamedevreports | [Reported, 2026-10] | Mobile games broadly; a daily social game follows its own curve |
| Sessions | Median session 5 to 6 minutes, about 4 sessions a day | Same | [Reported, 2026-10] | Same |

Conflicts kept visible: Color Block Jam was reported at $25 million IAP in Q1 2025 (AppMagic via Mobidictum) and at $12.1 million per 30 days (Insightrackr) [Contested].

## 6. Reading a monetization test

| Rule | Detail |
|------|--------|
| Length | At least 7 days, 2 to 4 weeks typical, full weeks, never stop early, judge after the novelty wears off; a D7 outcome needs 7 days after exposure [Reported, 2026-10] |
| Primary metric | Total ARPDAU (IAP plus ads, net), or revenue per shown offer for an offer test |
| Guard rails | D1, D7, sessions per DAU, refund rate, complaint rate, store rating trend |
| Unit | Users randomized once and kept in their cell; the read uses `policy_revision` per cell |
| Variance | Revenue per user is heavy tailed: a few large purchases move the mean. Report the median and the share of payers too, and ask `measurement` for the interval method (bootstrap or a trimmed mean decided before the test) |
| Decision | Ship only if the primary metric wins and no guard rail breaches its stop rule |

### 6.1 Sample size for a conversion metric (rule of thumb)

For a proportion p (for example daily payer share) and an absolute difference d to detect with 80% power at a 5% two sided level, users per cell are about 16 x p x (1 minus p) / d squared [Practitioner consensus].

| Baseline payer share | Change to detect | d | Users per cell |
|----------------------|------------------|---|----------------|
| 3% | 10% relative (3.0% to 3.3%) | 0.003 | about 51,700 |
| 3% | 30% relative (3.0% to 3.9%) | 0.009 | about 5,750 |
| 5% | 20% relative (5.0% to 6.0%) | 0.010 | about 7,600 |

Consequence: a game with 2,000 DAU cannot read a small IAP change in weeks. Test bigger changes, read ad metrics (many more events), or accept a directional read and label it as such.

## 7. Attributing revenue to policy changes

1. Every change raises `policyRevision`; every monetization event carries `policy_revision` (`monetization_conformance.py` fails when it is missing).
2. Roll out by remote config to a share of users first; keep a holdout on the previous revision.
3. Compare revenue per DAU and guard rails by revision, not by calendar date, so seasonality and UA bursts fall into both cells.
4. Log the revision, its start time and its cells in `EXPERIMENTS.md` and the journal.
5. A revision that ships to everyone without a holdout can only be read before and after; label such reads as weak.

## 8. Traps

| Trap | Why it misleads | Fix |
|------|-----------------|-----|
| Gross vs net mixed | Store fees and tax differ by platform and market | Net of fees, tax and refunds in every report; state it |
| Mediation eCPM vs paid out | Mediation reports estimates; payouts arrive later and can differ | Reconcile monthly; report paid out when it exists |
| ARPPU period mismatch | Daily payers with monthly revenue inflates ARPPU | Same period for numerator and denominator |
| Averaged ratios | Averages of daily ARPDAU weight small days like big ones | Sum revenue, sum DAU, divide |
| Refund lag | Refunds arrive days or weeks later | Re-read revenue after the refund window; read refunds by purchase cohort |
| Timezone and day boundary | Daily games reset at a fixed time; analytics may use UTC | Use the game's reset timezone for daily metrics, as measurement defines |
| UA mix shift | New paid cohorts monetize differently | Read by install cohort and channel with `mobile-app-growth` |
| Casual puzzle gates applied to a daily social game | A daily game behaves like a daily puzzle or social app, not like a level based puzzle game | Gates from the game's own curve (measurement and `growth-orchestrator`) |
| eCPM read without fill | A higher floor raises eCPM and loses impressions | Read revenue per DAU per placement |

## 9. Weekly read template

```
# Monetization weekly read: <game>, <week>, <timezone>
Data: <exports and connectors, date range>; revenue <gross or net>; definitions from METRICS.md
ARPDAU (IAP, ads, total) vs trailing 4 and 8 weeks
Guard rails: D1, D7 (latest mature cohorts), sessions per DAU, refund rate, complaint rate
Tree: which factor moved (payer share, ARPPU, impressions per DAU, eCPM, fill)
Per placement table (section 3); per offer table (section 4)
Tests running: revision, cells, days in, reads due
Incidents and refunds
Changes proposed (change requests), handoffs
```
