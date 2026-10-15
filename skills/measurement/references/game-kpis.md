# Game KPIs: Definitions, Dashboards and Soft Launch Gates

> Knowledge as of 2026-10 (research pass 2026-10-12). The definitions in this module are ours and change only with a `DECISIONS.md` entry. The benchmarks were read from search summaries and vendor reports, not from the full studies, so their strongest label is [Reported, 2026-10]; every benchmark row carries a re-check date. Compare a game with its own history first and with benchmarks second.

## 0. The one owner rule

`measurement` owns every game number: its definition, its formula, its source of truth and its traps. Everyone else reads.

| Agent | Reads from this module | Never does |
|-------|------------------------|-----------|
| `game-monetization` | ARPDAU split, impressions per DAU, eCPM, payer conversion, ARPPU, offer conversion, payer tiers | Redefines ARPDAU, payer conversion or eCPM in its own outputs |
| `game-liveops` | D1, D7, D30, stickiness, event participation, season completion, churn by level | Reports a rolling D7 next to a classic D7, or a level funnel with its own churn rule |
| `mobile-app-growth` | Install cohorts, LTV and pLTV curves, ROAS D0, D7, D30, payback | Sets a D7 ROAS target from a blog instead of the game's own curve (section 5) |
| `app-store-optimization`, `store-submission` | Crash and vitals definitions for quality gates | |
| `growth-orchestrator` | Soft launch gate verdicts (section 9) | Calls a soft launch on a cohort under the minimum size |

A metric that is not here does not exist yet. Ask `measurement` (handoff), get a row in this module (global) or in the project's `ads-master/METRICS.md` (project specific), and log the decision. The project file wins where it differs, and every report says which definition it used.

Every game report states, in its header: product and game, timezone, active definition, install definition, retention type (classic), revenue basis (gross or net, IAP and ads), data source and date range, exclusions.

## 1. Eight decisions to fix before any number

| # | Decision | Options | Default | Why it matters |
|---|----------|---------|---------|----------------|
| 1 | Active | Any client event; only `session_start`; only a gameplay event | Any client event; server side events never count | A refund notification or an entitlement grant arrives from a server while the player is away; counting it inflates DAU and retention |
| 2 | Day boundary | UTC; the product's reset time; the player's local midnight | The product's reset boundary when the game has one (a daily puzzle resets at a fixed time), else UTC; one choice per product | A player at 23:30 and again at 00:20 is retained on day 1 in one timezone and not in another (section 3.2) |
| 3 | Install | Store first download; first open (MMP install); first event in analytics | Retention and level funnels: first activity day in analytics. UA tables: MMP install date. Never mixed in one table | Tools differ by a day or more [Reported, 2026-10]; redownloads look like installs in some tools |
| 4 | Retention type | Classic (active exactly on day N); rolling or return (day N or later); bracket (a range of days) | Classic | GameAnalytics publishes classic retention [Reported, 2026-10]; rolling is always higher and is not comparable |
| 5 | Window | Calendar day; 24 hour window from install | Calendar day in the day boundary of row 2 | Amplitude and Mixpanel default to rolling 24 hour windows [Reported, 2026-10]; confirm in each tool before comparing |
| 6 | Revenue basis | Gross (what the player paid); net of store fee; net of tax and refunds; ads estimated (impression level) or paid out | Two columns, gross and net; ARPDAU in `METRICS.md` uses IAP net plus ad revenue; refunds land on the day the store reports them | A 30% store fee and VAT make gross and net ARPDAU differ by more than most test effects |
| 7 | Exclusions | Test devices, QA, internal staff, bots, sandbox purchases, the store reviewer demo account | Flag at ingest and exclude from reports, never delete | A soft launch of 2,000 installs with 150 internal devices is a different game |
| 8 | Product or game | A product (one store listing or web app) may hold many games (Game Monetization Contract section 2) | Report per product and per game; per game install = the first play of that game | DAU of a platform and DAU of its third game answer different questions |

Write the answers into `ads-master/METRICS.md` (game rows) and `ads-master/MEASUREMENT.md` on day one.

## 2. KPI dictionary

Additivity follows the reporting rules in the `METRICS.md` template: counts and money add up, ratios are always recomputed from summed numerators and denominators, never averaged.

| KPI | Formula | Grain and roll up | Trap |
|-----|---------|-------------------|------|
| DAU | Distinct players with at least one qualifying event in the day | Day; never summed across days (sum of DAU is "player days") | "Active" defined differently in two tools; server events counted |
| WAU | Distinct players active in the 7 days ending on the day | Rolling 7 days | Calendar week and rolling 7 days differ; say which |
| MAU | Distinct players active in the 30 days ending on the day | Rolling 30 days (or calendar month, labeled) | A calendar month has 28 to 31 days |
| Stickiness | Average DAU over the 30 days / MAU of the same 30 days | Ratio | Drops during UA bursts (new players enter MAU before they form a habit); a single day's DAU over MAU is noise |
| New players | Players whose first activity day is the day | Day, additive | Reinstalls and new devices look new unless identity carries over |
| Classic DN retention | Players of an install cohort active exactly on day N / cohort size | Install cohort; pooled = sum retained / sum cohort sizes over mature cohorts | Averaging cohort rates; reading a cohort before day N is complete |
| Rolling (return) DN | Players active on day N or any later day / cohort size | Install cohort | Always higher than classic and still rising as data arrives; never mix with classic |
| Active days in first week | Mean days active in days 0 to 6 per install | Install cohort | Best habit signal for daily games; mature only after day 6 |
| Sessions per DAU | Sessions / DAU | Day, ratio | A session definition (timeout) changes the number; state it |
| Session length | Median session duration | Day | The last session of a day often lacks an end event; use the last event time, foreground only |
| Playtime per DAU | Foreground seconds / DAU | Day, ratio | Background time and idle screens |
| Level funnel | Per level: players who started, completed, failed, quit; attempts | Level, by build and by cohort | Players and attempts are different denominators; a fail (lost) and a quit (left) are different events |
| Win rate per level | Completions / attempts | Level | Boosters and continues change it; split by "used a booster" |
| Attempts per completion | Attempts / completions | Level | Survivorship: only players who stayed are counted on hard levels |
| Churn by level | Players inactive 7 or more days whose last level was N / players who reached N | Level, as of a date | Censoring: players still active are not churned yet; a recent build has too little time to show churn |
| ARPDAU (total) | (IAP revenue + ad revenue) / DAU | Day; over a period = total revenue / sum of DAU | Gross vs net; refunds; always shown split |
| ARPDAU IAP, ARPDAU ads | Each revenue type / DAU | Day or period | Ad revenue is estimated at impression level and restated when paid out |
| Ad share | Ad revenue / (IAP + ad revenue) | Period | Moves with country mix: growing markets lean on ads, US, CA, KR and JP lean on IAP [Reported, 2026-10] |
| Impressions per DAU | Ad impressions / DAU, per placement and format | Day, placement | High usage with low impressions per DAU means the entry point is hard to find [Reported, 2026-10, LevelPlay docs] |
| eCPM | Ad revenue / impressions x 1,000, per placement, format, network and country | Placement day | Mediation reported eCPM vs paid out; blended eCPM hides placement mix |
| Ad ARPDAU check | Impressions per DAU x eCPM / 1,000 | Placement day | 1.5 impressions per DAU at a $4 eCPM is $0.006 per DAU [Reported, 2026-10, worked example in the research notes] |
| Fill rate | Ads shown / ads requested (contract events `ad_shown` / `ad_requested`) | Placement day | Requests fired too early (before the ad is needed) lower fill with no revenue effect |
| Rewarded opt in rate | Rewarded ads started / rewarded offers shown, per placement | Placement day | Counting `ad_shown` without `ad_rewarded` overstates value delivered |
| Offer conversion | `offer_accepted` / `offer_shown`, per `offer_id`, `point` and `policy_revision` | Offer day | Different revisions of a policy pooled together |
| Payer conversion (daily) | Active players with net IAP above zero that day / DAU | Day | A refund only player is not a payer |
| Payer conversion (window) | Active players with net IAP above zero in the window / distinct active players in the window | 7 or 30 days | Not the same as the daily number; label the window |
| Payer conversion (cohort) | Players of an install cohort with net IAP above zero by day N / cohort size | Install cohort | Mature only after day N |
| ARPPU | Net IAP revenue of payers / payers, same period | Day or window | Period mismatch: monthly ARPPU against daily payer share |
| First purchase timing | Median days from install to first purchase, payers only | Install cohort | Early cohorts have not had time to buy late |
| Refund rate | Refunded transactions / purchase transactions, by store | Month | Refunds arrive weeks after the purchase |
| LTV (n) | Cumulative revenue per install by day N (IAP net + ad), cohort | Install cohort | Always say the horizon and gross or net |
| pLTV (n) | Predicted LTV at day N from early days (section 5) | Cohort | A fixed multiplier goes stale |
| ROAS Dn | Cumulative revenue by day N of the cohort / spend on that cohort | Campaign cohort | iOS revenue in SKAdNetwork and AdAttributionKit arrives late and coarse; label modeled numbers |
| CPI | Spend / attributed installs (paid CPI); spend / all installs (blended) | Campaign day | Comparing a paid CPI with a blended one |
| Payback day | First day cumulative net LTV per install is at least CPI | Cohort | Gross LTV makes payback look early |
| K-factor | Invites per active player x invite to join conversion, same window | Weekly cohort | Same definition as `mobile-app-growth` ([App growth model](../../mobile-app-growth/references/app-growth-model-and-unit-economics.md) section 10.1); count joins that reach the first game, not link taps |
| Event participation | Distinct players with at least one event action / distinct active players in the event window | Event | For a one day event this is participants / DAU; a holdout is needed to call it uplift |
| Season completion | Players who finished the season track / players active during the season | Season | Report also the share who started the track |
| Crash rate | Players with a crash / DAU (user perceived crash rate in Play vitals) | Day | Google Play's bad behavior thresholds are 1.09% user perceived crash rate and 0.47% ANR rate overall, 8% per phone model, over 28 days [Official, 2026-10] |

## 3. Retention in detail

### 3.1 Classic vs rolling (illustrative numbers, not a benchmark)

| Day | Cohort players active that day | Classic DN | Players active on day N or later | Rolling DN |
|-----|-------------------------------:|-----------:|---------------------------------:|-----------:|
| 1 | 300 of 1,000 | 30.0% | 420 | 42.0% |
| 7 | 110 | 11.0% | 190 | 19.0% |
| 30 | 40 | 4.0% | 60 | 6.0% |

The same game looks almost twice as good on rolling D7. A vendor deck, a dashboard default and a publisher's term sheet can each use a different one. Ask, write it down, convert nothing silently.

### 3.2 Calendar days, 24 hour windows and timezones

- Calendar D1 counts a player who installs at 23:55 and plays again at 00:05 as retained after ten minutes. A 24 hour window counts activity between hour 24 and hour 48 after install. Late evening installs inflate calendar D1; markets in other timezones shift by hours.
- The golden fixture of `game_kpis.py` holds one such player: in UTC the pooled D1 is 7 of 11, in UTC+03:00 it is 6 of 11, because the player's two sessions fall on two UTC days and one Istanbul day. Same data, two answers, both correct for their definition.
- Pick one boundary per product (section 1, row 2), state it in every report, and never compare numbers built on different boundaries.

### 3.3 Maturity and timing

- A cohort enters DN only when day N is complete in the chosen timezone. Showing D7 for yesterday's installs as zero is the most common dashboard bug.
- D30 for a cohort needs 30 more days of data. A soft launch that installs players for 30 days needs about 60 days to read D30 on all its cohorts [Reported, 2026-10].
- Pool cohorts as a ratio of sums. In the fixture the mean of five D1 cohort rates is 65.0% while the pooled rate is 63.6%: small cohorts get the same weight as large ones in a mean.
- Classic retention is not monotonic per cohort (a cohort can show more players on day 7 than on day 1); rolling is. Odd shapes in small cohorts are noise until the cohort is large (section 10).

### 3.4 Censoring, mix and history

- An export that starts after launch makes older players look like installs on its first day. Exclude those cohorts (`--cohorts-from` in the script).
- Retention moves with traffic mix: organic, each network, each country and each creative bring different players [Reported, 2026-10]. Read retention by source before judging the game; a D1 drop in a week that added a new network is a mix question first.
- A new build changes the funnel. Annotate builds and `policy_revision` changes on every chart.

### 3.5 Daily games

A game with one capped session a day (a daily puzzle, a counted try) has a content supply of one play per day. Classic DN is still the definition, but add active days in the first week, active days per week among retained players, and streak continuation, because the habit is the product. Section 9.5 shows how gates change.

## 4. Monetization numbers

### 4.1 ARPDAU split and the identities

```
ARPDAU            = (IAP revenue + ad revenue) / DAU
ARPDAU IAP        = payer share x ARPPU            (same day and the same players only)
ARPDAU ads        = sum over placements of impressions per DAU x eCPM / 1,000
period ARPDAU     = period revenue / sum of daily DAU   (never the mean of daily ARPDAU)
```

The first identity breaks when payer share is a window number and ARPPU a monthly one: window payers / window actives x revenue / payers equals revenue per window active player, which is not revenue per daily active player. Use the window numbers as a set (window payer conversion, window ARPPU, window ARPDAU), never mixed with daily ones.

Worked from the golden fixture (7 day window): 11 player days, IAP 17.96, ads 0.11, so ARPDAU 1.6427 (IAP 1.6327, ads 0.0100); 4 payers among 8 active players, window payer conversion 50%, ARPPU 4.49. A refund of 4.99 arrived on the last day, so that day shows negative IAP revenue. That is correct: refunds land when the store reports them.

### 4.2 Gross, net, estimated, paid

| Number | What it is | Where it comes from | Reconcile |
|--------|------------|---------------------|-----------|
| IAP gross | Price paid including tax | Store or Stripe transaction | Monthly against store reports |
| IAP net | After store fee, tax and refunds | Store proceeds reports, Stripe balance | Monthly; fee route per market from [App growth model](../../mobile-app-growth/references/app-growth-model-and-unit-economics.md) section 3.1 |
| Ad revenue (impression level) | Estimated revenue per impression from mediation | `ad_revenue` events, precision `exact`, `publisher_defined` or `estimated` | Against the network's paid out amount each month |
| Ad revenue (paid) | What the networks pay | Network payment reports | Payout thresholds and terms delay cash: AppLovin $100 minimum, Net 15; Unity Ads Net 60, $100 [Reported, 2026-10] |

Report the gap between estimated and paid ad revenue as a ratio by network, the way platform and backend conversions are reported in the daily report.

### 4.3 Payer tiers (the contract's `payerTier`)

The contract's `OfferContext.payerTier` (none, low, mid, high) needs one definition per product. Default, until `METRICS.md` says otherwise:

| Tier | Rule |
|------|------|
| none | No net purchase ever |
| low | Payers below the 50th percentile of trailing 90 day net IAP spend among payers |
| mid | 50th to 90th percentile |
| high | Top 10% of payers by trailing 90 day net spend |

Percentile cut offs follow how devtodev segments payers [Reported, 2026-10]; fixed dollar thresholds break across currencies and price changes. One source says the top 1% to 2% of players drive 50% to 70% of IAP [Unverified, single source]; check the share in your own data before any decision rests on it. Tiers are for analysis and offer relevance. Showing a different price for the same item to different tiers is personalized pricing, which EU consumer law requires to be disclosed; route any such idea to `compliance` before a test.

## 5. LTV, pLTV, ROAS and payback

1. Build the curve from cohorts: cumulative revenue per install at D0, D1, D3, D7, D14, D30, D60, D90, D180, D365, by channel, OS and country, both gross and net.
2. Fit only after at least 3 cohorts reach the horizon. Until then use ratios from mature cohorts (LTV D180 / LTV D7).
3. A fixed multiplier goes stale: Liftoff reported a cohort with a higher D7 LTV and a lower D180 LTV than its neighbor [Reported, 2026-10]. Refit monthly, after every economy change and after a big traffic mix change; a power law fit on early days is a common alternative to a fixed ratio [Reported, 2026-10].
4. Validate every pLTV model on cohorts that matured: report the error at D30 and D90 (predicted vs actual), by channel. A model whose error exceeds the margin buffer cannot set bids.
5. Derive ROAS targets from the curve, not from a benchmark:

```
target D7 ROAS     = target D180 ROAS / (LTV D180 / LTV D7)
break even ROAS    = 1 / share of revenue kept        (gross ROAS basis)
payback day        = first day with cumulative net LTV >= CPI
```

Example: when D180 revenue is 6 times D7 revenue, a D7 ROAS of 20% reaches 120% by D180 [Reported, 2026-10, Liftoff worked example]. When ROAS is measured on gross revenue and the studio keeps 70% after fees, break even gross ROAS is 1 / 0.7 = 1.43 [Reported, 2026-10]. `mobile-app-growth` turns these into channel targets; this module owns the curve.

6. D0 ROAS is a creative and audience screen, not a profitability read.
7. iOS ROAS from SKAdNetwork and AdAttributionKit arrives late and in buckets ([Game tracking](game-tracking.md) section 6); label modeled iOS revenue as modeled.

## 6. K-factor and organic lift

- Same definition and read rules as [App growth model](../../mobile-app-growth/references/app-growth-model-and-unit-economics.md) section 10: k = invites per active player x invite to join conversion, with the join counted when the invitee reaches the first game within 14 days.
- One vendor guide calls 0.3 to 0.7 typical for games [Unverified, vendor claim]; the read thresholds in section 10.4 of that module apply.
- Group and social games count joins into a group separately from installs: an invitee who joins a group without installing (web play) is a join, not an install.
- Only a holdout of the invite feature proves the joins are incremental.

## 7. Live ops numbers

| Number | Definition | Read rule |
|--------|-----------|-----------|
| Event participation | Section 2 | Compare events of the same type; participation alone is not uplift |
| Event uplift | Difference in ARPDAU, sessions per DAU and D7 between players who could see the event and a holdout who could not, or between switchback periods | A holdout of 5% to 10% of players, or a geo split, decided before launch; read after the event ends plus 7 days |
| Season completion | Section 2 | Read with the share of payers who bought the pass |
| Streak continuation | Players active today who were on a streak yesterday / players on a streak yesterday | Daily games; protect against counting streak saves as play |
| Counted attempts per day | Constant per ranked board, from the policy file | Never a KPI to grow: the contract fixes it, so engagement cannot be bought |

`game-liveops` designs events and reads these; the definitions stay here.

## 8. The four standard dashboards

Every game gets the same four dashboards, built from the same events ([Game tracking](game-tracking.md)), so a new game plugs in on day one.

### 8.1 Daily (5 minutes, every day)

| Tile | Grain | Cut by | Alert |
|------|-------|--------|-------|
| New players, DAU, WAU, MAU, stickiness | Day | OS, country, source | DAU or new players outside the 7 day median by more than 30% |
| Revenue IAP and ads, ARPDAU split, payers | Day | Store, OS, country | Revenue zero on a day with DAU above zero; refunds above 2x their 28 day median |
| Latest mature D1 (cohort of two days ago) | Cohort | Source | D1 down 5 points vs the trailing 4 cohorts with each cohort above the minimum size |
| Crash rate and ANR rate | Day | Build, phone model | Above the store thresholds in section 2 |
| Ad fill rate, impressions per DAU | Day | Placement, network | Fill down 20% day over day |
| Tracking health | Day | Event | Events per DAU outside 3 standard deviations; any contract event missing for a day |
| Consent and ATT rates | Day | Region | A step change after a release |

The alert thresholds are starting values, not benchmarks; tune them in `MEASUREMENT.md` after 4 weeks.

### 8.2 UA (weekly, with `mobile-app-growth`)

Spend, installs, paid and blended CPI, D0, D1, D7 ROAS, D1 and D7 retention by campaign, country and creative, pLTV vs CPI, payback day by channel, SKAdNetwork null value share, MMP vs store install gap.

### 8.3 Monetization (weekly, with `game-monetization`)

IAP vs ads, ARPDAU split, payer conversion (daily and window), ARPPU, payer tiers, first purchase timing, offer conversion by `offer_id`, `point` and `policy_revision`, impressions per DAU and eCPM by placement, rewarded opt in rate, fill rate, top SKUs, refunds by store, currency sources and sinks per DAU (earned vs spent, from resource events), annotations for every policy revision.

### 8.4 Level design (weekly, with `game-liveops`, shared with the game repo)

Per level: starts, completes, fails, quits, win rate, attempts per completion, median time, booster and continue use, churn by last level. Spike flag (default heuristic, not a benchmark): churn by last level above 2 times the median of the 10 surrounding levels with at least 200 players reaching the level. Ads Master flags; the game repo decides what to change in the level ([Content cadence and difficulty signals](../../game-liveops/references/content-cadence-and-difficulty-signals.md)).

## 9. Soft launch gates derived from the game's own curve

### 9.1 Why copied gates fail

The common rules of thumb (D1 above 40% for casual) describe the top of the market. GameAnalytics medians are about 22% D1 and 3.4% to 3.9% D7 [Reported, 2026-10]. A gate copied from a blog kills most games, and a gate copied from the wrong genre kills the right game. A daily social game is not a level based puzzle game.

### 9.2 Procedure

1. **Archetype card.** Loop length, plays per day by design (unlimited levels or a capped daily play), monetization mix (IAP heavy, hybrid, ads first), social graph (solo, friends, groups), platforms (web, stores).
2. **Pick the gate metrics for the archetype.**

| Archetype | Primary gates | Secondary | Not a gate |
|-----------|---------------|-----------|------------|
| Casual level puzzle (Royal Match style) | D1, D7, D30 classic; ARPDAU; D7 ROAS vs curve target | Payer conversion, level churn spikes | Stickiness alone |
| Hybrid casual (ads plus IAP) | D1, D7; impressions per DAU; ad ARPDAU; D7 ROAS | D30 | IAP payer conversion alone |
| Midcore | D7, D30; payer conversion; ARPPU | D1 | D1 alone |
| Daily social game (one capped play a day, groups) | D7 and D30 classic; active days in the first week; group join rate in 3 days; stickiness | D1; invite to join conversion | Sessions per DAU, playtime (capped by design) |

3. **Derive the economic threshold.** If the game will buy traffic: expected CPI in the target markets (from `mobile-app-growth`) x (1 + margin buffer) = the LTV needed at the payback horizon. Divide by the curve ratio to get the D7 LTV needed, then split it into retention x ARPDAU. If the game grows by sharing (no paid UA), the threshold is retention plus k (section 6).
4. **Reality check** the derived threshold against the medians in section 9.4. A threshold far above top decile needs a reason; a threshold below the median needs a reason too.
5. **Size and timing.** Each gate needs a pooled mature cohort of at least the minimum size (default 1,000 installs, section 10) and the dates to mature. Write both into the gate row before the soft launch starts.
6. **Decision rule, written before the data.**

| Result | Decision |
|--------|----------|
| Every primary gate PASS with the threshold outside the 95% interval | Scale step (budget change through a G3 change request) |
| A gate PASS with the threshold inside the interval | Hold spend; grow the cohort; re-read |
| A gate FAIL | Iterate: one change at a time, new cohort, new read |
| Two to three iterations without moving the failing gate | Kill or re-concept, decided by the human with `growth-orchestrator` |
| A gate CANNOT JUDGE (cohort too small) | No decision; more installs or a longer window |

`game_kpis.py --gates` gives PASS, FAIL or CANNOT JUDGE and flags a threshold that sits inside the 95% interval.

### 9.3 Rules of thumb (casual and midcore, top of market)

| Metric | Casual | Midcore | Hybrid casual | Evidence |
|--------|--------|---------|---------------|----------|
| D1 | Above 40% | Above 35% | | [Reported, 2026-10] |
| D7 | Above 20% | Above 15% | 15% to 22%; tier 1 paid UA works around 18% | [Reported, 2026-10] |
| D30 | 5% to 15% | | Strong at 9% to 15% | [Reported, 2026-10] |
| LTV model | Validated on 30 days of data | | | [Reported, 2026-10] |
| D7 ROAS | IAP heavy 15% to 40%; ad monetized about 7% to 8% | | | [Reported, 2026-10] |
| Markets | Canada, Philippines, Australia, New Zealand, Nordics; 1 to 3 at a time | | | [Reported, 2026-10] |
| Volume | About 15,000 users for stable data | | | [Reported, 2026-10] |

These come from soft launch guides and vendor blogs (sources 3 to 6). They are hypotheses for a level based game, never targets for another archetype.

### 9.4 Reality check: medians

| Metric | Median | Top quartile | Top 10% | Source and caveat |
|--------|-------:|-------------:|--------:|-------------------|
| D1 | About 22% | 26% to 28% | About 40% | GameAnalytics 2025 report on data to end 2024, via a summary [Reported, 2026-10]; all genres and sizes, classic |
| D7 | 3.4% to 3.9% | 7% to 8% | About 12% | Same |
| D30 | About 0.7% | | About 4% | Same |
| D1, all genres, 2025 | 27% | | | Adjust 2026 gaming report [Reported, 2026-10]; Adjust's install definition and panel differ from GameAnalytics |
| Session length, sessions per day | 5 to 6 minutes median; about 4 sessions per day | | | GameAnalytics via summary [Reported, 2026-10] |

Re-check by 2027-04.

### 9.5 A daily social game (Aloo type)

A daily social game behaves like Wordle, LinkedIn's games or BeReal, not like Royal Match: one shared play per day, a reason to return tomorrow (the new puzzle, the group board), and a capped session supply. What the 2026-10-12 pass found:

- Wordle: one puzzle per day, a share grid that hides the answer, no ads [Reported, 2026-10].
- LinkedIn games: streaks, connection leaderboards, company and school boards, reset at midnight Pacific time [Reported, 2026-10].
- The New York Times had 13.35 million subscribers in Q2 2026 (10-Q filing) and paywalling The Mini in Q3 2025 added single product subscribers [Reported, 2026-10].
- No public retention curve for Wordle, BeReal or LinkedIn games was found. Do not quote one.

So the gates come from the game's own beta cohorts:

| Gate | How to set the threshold | Why |
|------|--------------------------|-----|
| D7 classic | The higher of the economic need (step 3, when the game buys traffic) and the lower bound of the beta's 95% interval; colder soft launch traffic usually retains less than a friends and family beta, so holding that bound is a strong signal | Habit forms in week 1; the day after install matters less when there is one play per day |
| D30 classic | Read only when cohorts mature; set from beta D30 | The long tail is the business for a daily game |
| Active days in the first week | Beta mean; gate on not falling below it | The direct habit measure |
| Group join within 3 days | Share of new players who join or create a group; set from beta | Groups carry the return trigger |
| Stickiness | Trend, not a gate: rising after the first 30 days | UA bursts dilute it |
| D1 | Report; gate only against a floor that signals a broken first session | The first session is short by design; D1 is weaker evidence here |

Illustrative example only (not a benchmark): beta cohorts of 1,400 installs show D7 18% (interval 16% to 20%), 3.1 active days in the first week and 41% joining a group in 3 days; the soft launch gates become D7 at least 16% (the interval's lower bound; no paid UA planned yet), active days at least 3.0 and group join at least 40%, each read on at least 1,000 installs per market.

### 9.6 Gate table template (`METRICS.md`)

| Gate | Threshold | Derived from | Minimum cohort | Window | Read date | Decision if FAIL |
|------|-----------|--------------|----------------|--------|-----------|------------------|
| D7 classic | | Beta cohorts 2026-09-01 to 2026-09-28 | 1,000 | Cohorts of weeks 1 to 3 | Week 5 | Iterate onboarding |

## 10. Sample size cautions

Wilson 95% intervals (computed, z = 1.96):

| Installs in the pooled cohort | D1 near 35% | D7 near 10% |
|------------------------------:|-------------|-------------|
| 100 | 26.4% to 44.7% | 5.5% to 17.4% |
| 300 | 29.8% to 40.6% | 7.1% to 13.9% |
| 1,000 | 32.1% to 38.0% | 8.3% to 12.0% |
| 3,000 | 33.3% to 36.7% | 9.0% to 11.1% |
| 15,000 | 34.2% to 35.8% | 9.5% to 10.5% |

The research notes put 100 users at roughly 26% to 44% for D1 [Reported, 2026-10], which the table reproduces.

Smallest difference an A/B test can detect (80% power, 5% two sided, two equal arms, computed):

| Players per arm | Baseline 35% | Baseline 10% |
|----------------:|-------------:|-------------:|
| 1,000 | 6.0 points | 3.8 points |
| 5,000 | 2.7 points | 1.7 points |
| 15,000 | 1.5 points | 1.0 point |

Rules:
1. Default minimum cohort for a gate: 1,000 installs (an interval of about plus or minus 3 points at D1 near 35%). Under it, a gate is CANNOT JUDGE.
2. Never read D1 from under 1,000 installs as a decision [Reported, 2026-10, common pitfall].
3. A/B tests run at least 1 week, typically 2 to 4, are never stopped early, are judged after the novelty effect, and D7 outcomes need 7 days after the last exposure [Reported, 2026-10].
4. Read by source before pooling: a mix change can move the pooled rate more than the test did.
5. Holidays, featuring and a new network are confounders; annotate them.

## 11. Benchmarks (directional only)

| Metric | Value | Source | Label | Caveat | Re-check by |
|--------|-------|--------|-------|--------|-------------|
| Payer conversion | 2% to 5% of players | Unity guide; repeated widely | [Unverified] | Definition (daily, monthly, lifetime) rarely stated | 2027-04 |
| ARPDAU, hybrid casual | $0.15 to $0.50, IAP share 40% to 60% | Vendor blog | [Unverified, vendor claim] | Mix and country dependent | 2027-04 |
| ARPDAU, casual and puzzle | $0.03 to $0.10 | Vendor blog | [Unverified, vendor claim] | Same | 2027-04 |
| eCPM, Q4 2024 | Rewarded about $13.6 iOS, $9.0 Android; interstitial $10.4 and $9.6; banner $0.4 and $0.5 | Appodeal report | [Reported, 2026-10] | Q4 is seasonally high; one mediation platform | 2027-04 |
| eCPM ranges 2026 | Western Europe iOS $5 to $12; Brazil Android $1 to $3; India Android $0.30 to $1 | Vendor blog | [Unverified, vendor claim] | Format not always stated | 2027-04 |
| Game ad revenue split | 55% Android, 45% iOS, Q2 2026 | Tenjin (2026-08) | [Reported, 2026-10] | Tenjin's panel | 2027-02 |
| Mobile game revenue 2025 | $82B, +1% | Sensor Tower State of Gaming 2026 | [Reported, 2026-10] | Store IAP only | 2027-03 |
| Mobile game ad revenue 2025 | $12B; puzzle and arcade above 65% | Sensor Tower via a summary | [Reported, 2026-10] | Estimate | 2027-03 |
| CPI, global blended gaming | $0.56, +30% year over year | Adjust 2026 via FoxData | [Reported, 2026-10] | Blended across genres and countries | 2027-02 |
| CPI, casual 2025 | iOS $1.41, Android $0.14 | Liftoff casual report | [Reported, 2026-10] | Liftoff network data | 2027-02 |
| D30 ROAS, casual, 2024 | 47% iOS, 15% Android | Liftoff and Singular via a summary | [Reported, 2026-10] | Network panel | 2027-02 |
| ATT opt in, gaming | 51% (AppsFlyer, Q1 2024), 35% (Adjust, Q2 2025), 13.85% (Singular, Q2 2024) | Vendor reports | [Contested] | Denominators differ (shown the prompt vs all users) | 2027-04 |
| K-factor | 0.3 to 0.7 typical | Tenjin guide | [Unverified, vendor claim] | Definition varies | 2027-04 |

Mobile app growth keeps app wide (non game) retention and fee benchmarks in [App growth model](../../mobile-app-growth/references/app-growth-model-and-unit-economics.md) section 8.

## 12. The script: `game_kpis.py`

`<skill>/scripts/game_kpis.py` (standard library only; run with `python3 -I`).

| Input | Detail |
|-------|--------|
| CSV | `user_id`, `ts` (ISO 8601 with offset), `event`; optional `revenue` (major units, one currency, refunds negative), `revenue_type` (`iap` or `ad`), `level` (integer), `currency`, `transaction_id`, `game` |
| `--timezone` | IANA name or `+HH:MM`; default UTC (section 1, row 2) |
| `--as-of` | Last complete day; default the day before the latest event date (usually partial) |
| `--min-cohort` | Smallest pooled cohort a gate may judge; default 1,000 |
| `--gates` | JSON such as `{"d1": 0.30, "d7": 0.10, "d30": 0.03}` (fractions) |
| `--window`, `--churn-days`, `--cohorts-from`, `--game`, `--non-activity-events` | Monetization window (7), churn rule (7 days), left censoring cut, game filter, server events that never count as play |
| `--json`, `--out` | Machine readable results; Markdown report to a file |
| Short history | Days before the first event in the file are not counted in average DAU and stickiness; the report says how many of the 30 days it observed |

Exit codes: 0 report (every gate PASS), 1 a gate FAIL, 2 could not run or a gate could not be judged. A FAIL outranks a CANNOT JUDGE. The last line says what the check cannot cover.

The golden fixture `scripts/samples/game_events.csv` (12 players, 6 install cohorts) has hand computed answers in `scripts/samples/game_events_expected.json`, including a midnight install, a refund that must not count as play, a duplicate purchase row and a player exactly at the 7 day churn boundary. `test_game_kpis.py` checks the output against it exactly. Change a definition: change the golden first, by hand, then the code.

Export recipe: one row per contract event and gameplay event from the warehouse (BigQuery for Firebase, the GameAnalytics raw export, PostHog), `value` turned negative for `purchase_refunded`, minor units divided to major units, test devices removed.

## 13. Sources

| # | Source | Publisher | Date | Supports |
|---|--------|-----------|------|----------|
| 1 | GameAnalytics mobile gaming benchmarks 2025 (via gamedevreports summary and investgame PDF) | GameAnalytics | 2025, data to end 2024 | Retention medians and top quartile and decile, session length; classic retention [Reported, 2026-10] |
| 2 | Adjust gaming app insights 2026 | Adjust | 2026 | D1 27% across genres in 2025; CPI trend via FoxData [Reported, 2026-10] |
| 3 | Soft launch guide | gamegrowthadvisor.com | 2025-12-16 | Gates, markets, volumes [Reported, 2026-10] |
| 4 | Soft launch gate article | getbruin | 2025 to 2026 | Gate rules of thumb [Reported, 2026-10] |
| 5 | D7 ROAS article | playio | 2026 | D7 ROAS ranges by monetization [Reported, 2026-10] |
| 6 | Liftoff blog (post ?p=35616) and casual gaming report 2025 | Liftoff | 2025 to 2026-04 | Curve derived D7 targets, stale multipliers, casual CPI and ROAS [Reported, 2026-10] |
| 7 | Retention documentation | Amplitude, Mixpanel | ongoing | 24 hour window defaults [Reported, 2026-10] |
| 8 | Event types documentation | docs.gameanalytics.com | ongoing | Classic retention, event taxonomy [Reported, 2026-10] |
| 9 | Payer segmentation | devtodev | ongoing | Percentile payer tiers [Reported, 2026-10] |
| 10 | Unity IAP guide, LevelPlay documentation | Unity | ongoing | Payer share 2% to 5%, impressions per DAU reading [Reported, 2026-10] |
| 11 | Appodeal Q4 2024 eCPM report (PDF) | Appodeal | 2025 | eCPM anchors [Reported, 2026-10] |
| 12 | Tenjin ad revenue report; Tenjin k-factor guide | Tenjin | 2026-08; undated | Android and iOS split; k range [Reported, 2026-10]; [Unverified] |
| 13 | State of Mobile Gaming 2026 | Sensor Tower | 2026 | Revenue totals [Reported, 2026-10] |
| 14 | Android vitals | developer.android.com/topic/performance/vitals | page read 2026-10-12 | Crash and ANR thresholds [Official, 2026-10] |
| 15 | NYT 10-Q Q2 2026 | sec.gov | 2026 | Subscriber count [Reported, 2026-10] |
| 16 | LinkedIn games help | LinkedIn | 2026 | Streaks, boards, reset time [Reported, 2026-10] |
| 17 | AppLovin and Unity payment terms | support.applovin.com, docs.unity.com | ongoing | Payout minimums and terms [Reported, 2026-10] |
| 18 | Game Monetization Contract v0.1 | Ads Master, [contract](../../game-monetization/references/monetization-contract.md) | 2026-10 | Event names, payer tier field, modes and counted attempts |
