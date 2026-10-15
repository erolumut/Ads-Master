# Events and Seasons

> Knowledge as of 2026-10. Teardown facts (Royal Match, Monopoly Go) come from search summaries of trade press and analyst teardowns [Reported, 2026-10] or a single source [Unverified]; they describe what a hit did, not what works for every game. Apple event badge definitions were read at the official page on 2026-10-12 [Official, 2026-10]. Fairness rules come from the Game Monetization Contract v0.1 ([contract](../../game-monetization/references/monetization-contract.md)).

Gate: event specs, reward ladders and season plans are G1. Scheduling an event live, changing an event that players can see, ending one early or changing season dates is G3. Prices and offers inside events belong to `game-monetization`.

## 1. Events in nested time scales

Hit puzzle games run several events at once, each on its own clock, so every session has a near goal, a mid goal and a long goal [Reported, 2026-10, teardowns].

| Scale | Length | Example | Label | Job in the retention stack |
|-------|--------|---------|-------|----------------------------|
| Burst | About 1 hour | Royal Match Lightning Rush | [Reported, 2026-10] | Makes this session special; rewards intensity |
| Short | 2 to 3 days | Royal Match King's Cup (about 2 days, about 50 players, unlocked around level 25); Sky Race (3 days) | [Reported, 2026-10] | Brings players back across days; mid week lift |
| Week | 7 days | Weekly race, team chest cycle, weekend event | [Practitioner consensus] | Weekly rhythm; team and group goals |
| Season | 21 to 31 days (3 months for rated play) | Royal Pass, about 30 steps per month, unlocked around level 37; a daily social game with 21 day seasons; a board platform with 3 month rating seasons | Royal Pass [Unverified, single teardown source]; the other two are product decisions | Long goal; the pass; standings reset |
| Annual | Holidays, anniversary, new game launch | Calendar | [Practitioner consensus] | Spikes, reactivation, featuring |

Rules for the stack:
1. At most one event per time scale live at once for a given player; two events on the same clock compete for the same session [Practitioner heuristic].
2. Every scale has a free path a non payer can finish (section 6).
3. The calendar shows the whole stack on one page (`LIVEOPS_CALENDAR.md`, [calendar module](liveops-calendar-and-store-events.md)).
4. Smaller games run fewer scales: a new game starts with the daily loop plus one weekly event and adds scales only when the previous one reads positive against a holdout.

## 2. Event formats

| Format | Mechanic | Moves | Fits | Risk | Contract note |
|--------|----------|-------|------|------|---------------|
| Milestone track | Normal play earns event points; a ladder of rewards | Sessions per DAU, D7 | Every type | Too long a ladder: completion collapses | Rewards are economy sources: send the ladder to `game-monetization` |
| Collection | Collect tokens during normal play | Sessions, playtime | Level games, hybrid casual | Collection with random packs drifts into loot box territory | Paid random items need odds and labels; never for minors in some markets (`compliance`) |
| Race (small cohort) | First to N wins among a small group | D1 to D3 returns, intensity | Level games, hybrid | Pay to win if fed by purchasable progress | A race ranks people: it is a ranked board (section 4) |
| Cohort leaderboard | Rank among about 50 matched players over 2 to 3 days | Returns across days | Level games | Same as race; whales dominate unmatched cohorts | Ranked board with scope `group` |
| Team chest | Team members fill one shared goal; everyone gets the reward | Social retention, team activity | Teams, groups | Free riders, dead teams | Collective, not ranked: progression grants may feed it |
| In team leaderboard | Top 3 inside a team get extra | Competition among friends | Teams | Paid progress decides ranks | Ranked board with scope `group` |
| Community goal | Everyone together reaches a global target | Belonging, news value | Daily social, web first, board platforms | Goal too far: shared failure | Not ranked |
| Challenge | One fixed hard puzzle or condition for the event window | Return of skilled players | Daily, board, puzzle | Frustration; difficulty is the game repo's call | Counted attempts declared if ranked |
| Theme week | New content skin or theme on the daily content | Novelty, share rate | Daily social, board | Thin novelty decays fast | Never changes counted attempts or scoring |
| Tournament | Bracket or Swiss rounds at scheduled times | Concentrated play, rated players | Board and multiplayer | Splits the matchmaking pool | Rated results are ranked boards; nothing sold changes them |
| Premiere or major update | New content or mode launch | Reactivation, featuring | All | Content not ready | Store event (Major Update, Premiere badges) |

Apple's own guidance lists challenges, competitions and special content launches as good in-app event candidates and repetitive daily tasks as poor ones [Official, 2026-10]. The badge mapping is in the [calendar module](liveops-calendar-and-store-events.md) section 2.4.

## 3. The event spec (what liveops hands to the game repo)

Liveops writes the spec; the game repo decides feasibility, implements and owns the rules inside the play. One spec per event type, one calendar row per occurrence.

```
# Event spec: <event type id>, v<n>
Format: milestone | collection | race | cohort_leaderboard | team_chest | in_team_leaderboard | community_goal | challenge | theme_week | tournament | premiere
Time scale: burst | short | week | season | annual; length <hours or days>
Eligibility: unlock rule (for example level reached, days since install), regions, age bracket rules
Entry: automatic | opt in (opt in preferred for competitive formats)
Qualifying action: <what earns progress, in plain words>; mode it reads from (contract mode id)
Progress and rewards: ladder shape (number of steps, where the free path ends), reward types as typed grants (cosmetic, access, pass, currency, booster, ...), with game-monetization sign off
Ranking: none | board id and scope (group or everyone); what feeds it; why no purchase can change it
Cohorts: size, matching rule (recent activity band, skill band), bots disclosed or none
End rules: end time in the day id rule, ties, late joiners, unclaimed rewards (auto granted at end)
Fairness: contract mode and grants checked; no counted attempt changes; minors rules
Copy intent: what the player must understand; end date and time shown plainly; no countdown on offers
Store: Apple in-app event badge and purpose, Play promotional content type, or none
Reminders: moments requested from lifecycle-crm
KPIs: participation, completion, uplift metric vs holdout, guardrails
Holdout: percent, unit (player or group), compensation after the read
Kill switch: remote config key
Telemetry: liveops_event_shown, liveops_event_joined, liveops_event_progressed, liveops_event_completed, liveops_reward_claimed (proposed to measurement)
```

## 4. Competitive events and the fairness rule

The contract defines a ranked mode as anything that ranks people against each other, and a board computed from other play counts as ranked when it ranks people (derived boards, contract section 3). So:

| Format | Ranked? | What may feed it | What may be sold or rewarded around it |
|--------|---------|------------------|----------------------------------------|
| Milestone track, team chest, community goal, collection | No: progress toward a goal, not a rank | Any play, including progression play where boosters and continues are sold | Per progression rules (fixed prices, `maxPerAttempt`, no escalation) |
| Race, cohort leaderboard, in team top 3, league, tournament, streak board | Yes: a ranked board with scope `group` (cohort, team, league division) or `everyone` | Only play that no purchase, ad or reward changes: a dedicated ranked mode with constant `countedAttemptsPerDay` (the contract's progression sample has a weekly race nobody can buy into) | Only `cosmetic`, `access` and `pass` grants; a `round` only from a social purchase to boards no wider than its recipients |

Consequence: a race in a level game that ranks players by levels beaten, while boosters and extra moves are sold for those levels, is a ranked board fed by purchasable play. Cohort races such as Royal Match's King's Cup are commonly described this way [Unverified mechanism: the notes give its length and cohort size, not its scoring], and Ads Master does not propose that shape under contract v0.1. Equivalent goals that keep fairness:
1. A milestone version (beat N levels in 2 days for a reward), with no rank among players.
2. A race on a dedicated event level set played without boosters or continues, with constant counted attempts.
3. A team chest (collective goal).

A product owner who wants a purchasable ranked race takes it to `game-monetization` as a contract change; liveops does not ship it under v0.1.

## 5. Cohorts for competitive formats

- Small cohorts make winning possible: the reported King's Cup cohort is about 50 players [Reported, 2026-10].
- Match cohorts by recent activity (sessions or days played in the last 7 days) and, for skill based ranks, by skill band, so a casual player is not placed against the most active players [Practitioner consensus].
- Bots or simulated opponents are disclosed or not used. An undisclosed bot in a competition is a deceptive pattern and a trust risk [Practitioner consensus]. On board platforms where bots are ordinary players of the engine, the seat shows it is a bot.
- Late joiners join a cohort of late joiners, not a cohort that is two days ahead.
- Read cohorts after each run: share of cohorts where the median participant finished in the reward zone.

## 6. Seasons and passes

### 6.1 What a season is

A season is the long arc: a theme, a free reward track, often a premium track (the pass), standings that reset, and a recap at the end.

| Owner | Owns |
|-------|------|
| `game-liveops` | Season length and dates, theme, free track shape and completion target, reset rules, catch up rules, calendar, store events, recap moment, reads |
| `game-monetization` | Pass price, premium track value, offers at `on_season_start` and `on_season_end`, economy balance of every reward |
| Game repo | Implementation, rules inside the play, content |
| `compliance` | Pass copy, minors, price display |

Reported pass evidence: Royal Pass unlocks around level 37 with about 30 steps per month [Unverified, single source]; Naavik reported a 31% revenue lift in the first 30 days after the pass launched in June 2021 [Unverified, single source]. Treat both as one game's history, not a forecast.

### 6.2 Season length

| Length | Calendar property | Fits | Note |
|--------|-------------------|------|------|
| 21 days | 3 weeks: every season starts on the same weekday; about 17.4 seasons a year (365 / 21) | Daily social games (group seasons) | Short enough to finish with friends; dates drift across months |
| Calendar month | Aligns with months and paydays; 28 to 31 days, weekday drifts | Level games with a monthly pass | Easy to communicate ("October season") |
| 4 or 5 weeks | Weekday aligned and longer | Games with weekly events inside the season | 13 or about 10 seasons a year |
| 3 months | Few resets, time for ratings to settle | Rated board and multiplayer play, gated on player liquidity | Needs mid season events to avoid a long flat middle |

Pick the length from the game's own rhythm: how many active days a typical engaged player has in a month, and how long a group keeps playing together. A length chosen because a hit used it is a borrowed number.

### 6.3 Season structure

| Phase | When | Liveops actions |
|-------|------|-----------------|
| Announce | 7 to 14 days before | Calendar row; Apple in-app event with the New Season badge, promoted up to 14 days ahead [Official, 2026-10]; Play promotional content draft; community post |
| Open | Day 1 | Free track starts; `on_season_start` offers only as the policy allows; reminder moment request |
| Middle | Each week | One weekly event inside the season; a checkpoint reward; read progress distribution |
| Final week | Last 7 days | Catch up rule live (section 6.5); end date and time shown plainly; no countdown copy on offers |
| Close | Last day at the tick | Standings frozen; unclaimed free rewards granted automatically; recap share card |
| Rest | 0 to 2 days, optional | A short gap lets standings settle; avoid long gaps that break habit |

### 6.4 Free track completion

- Declare a completion target before the season starts: the share of season participants who should reach the end of the free track, and the share of the most engaged players who should (product decision, written in the season plan).
- Size the track from data: the distribution of active days per season participant in the last seasons. A track that needs more active days than most participants have is a track most will not finish.
- Read after the season: final tier distribution, completion rate vs target, completion by join week.
- The free track never requires a purchase or an ad to finish; the premium track adds, it never gates the free track.

### 6.5 Catch up and late joiners

- A player who joins in the final week still earns something meaningful from the free track.
- Catch up mechanics (for example extra season points for players behind the median) are reward pacing, proposed by liveops and implemented by the game repo. They never write to a ranked board.
- In ranked seasons, catch up never changes standings; it changes rewards only.

### 6.6 What resets and what persists

| Resets at season end | Persists |
|----------------------|----------|
| Season points, season standings, season boards | Everything purchased |
| League or division placement (soft reset where ratings exist; rating math belongs to the game repo) | Cosmetics and titles earned |
| Premium track progress (by definition of a season) | Lifetime stats, best streak, history |
| Season currency earned in play, with clear notice before the end | Purchased currency never expires (Apple 3.1.1: purchased credits or in-game currencies may not expire) [Official, 2026-06] |

## 7. Monetization touchpoints (coordinate, do not own)

| Touchpoint | Liveops provides | `game-monetization` decides |
|------------|------------------|-----------------------------|
| Season pass | Season dates, free and premium track shape, completion targets | Price, premium value, `on_season_start` offer, refund rules |
| Event offers | The moment (event start, the obstacle the event introduces) | Whether an offer exists, price, caps, `countdown: false` |
| Event rewards | The reward ladder draft as typed grants | Economy balance in the sinks and sources sheet |
| Group purchases (an encore round for the group) | The calendar slot, the fairness check (writes only to group boards), reminder moments | Price, grant definition, refund handling |
| Event currency | Whether one is needed; expiry notice for earned currency | Currency rules; purchased currency never expires |

Never in an event: escalating prices inside one attempt, countdown copy on offers, paid random items for minors where the law forbids them, a buyer only benefit in a competitive context (contract sections 3 and 8).

## 8. Reading an event

Definitions are proposals to `measurement`; the project's `METRICS.md` wins.

| Metric | Definition | Read |
|--------|-----------|------|
| Participation | Participants (players who did the qualifying action at least once) / average DAU over the event window | Reach of the event |
| Completion | Players who reached the final free reward / participants | Ladder sizing |
| Uplift | Metric in the exposed group minus the holdout (sessions per DAU, D7 of players active at start, revenue per DAU with `game-monetization`) | Whether the event caused anything |
| Cannibalization | Change in other events' participation in the same window | Stack crowding |
| Repeat decay | Participation of run k / run 1 of the same event type | Fatigue |
| Sentiment | Review themes and community posts mentioning the event (`app-store-optimization` review themes) | Trust |

Participation is not success. An event that half of DAU joins and that changes nothing against the holdout spent content and attention for no gain. Read every new event type against a holdout ([Experiments and remote config](experiments-and-remote-config.md) section 5).

Event read template:

```
# Event read: <event id>, <dates>, <product>
Data: <source, date range, METRICS.md definitions used>
Participation: <x%> (participants / avg DAU)   Completion: <y%>
Uplift vs holdout (<holdout %>, unit <player|group>): <metric>: <+z, CI>   Guardrails: <...>
Repeat decay vs previous runs: <...>
Monetization read (from game-monetization): <...>
Sentiment: <themes>
Decision: repeat as is | change <what> | rest | retire
Memory candidate: <only if confirmed by two runs or one valid test>
```

## 9. Event fatigue

| Signal | Likely cause | Fix |
|--------|--------------|-----|
| Participation falls run after run | Same format, same rewards | Rotate formats; rest the format for a cycle |
| Completion falls while participation holds | Ladder too long, or the qualifying action got harder | Shorten the ladder; check difficulty flags for the event content |
| Sessions flat while events multiply | Stack crowding | One event per scale; remove the weakest |
| Reviews mention "too many events" or "pay to win" | Pressure or fairness leaks | Pressure audit ([Player trust](player-trust-and-pressure-patterns.md)); fairness check against the contract |

## 10. Events by game type

| Game type | Start with | Add when the first reads positive | Avoid |
|-----------|-----------|-----------------------------------|-------|
| Daily social mini game | Seasons with a group table; a theme week; a community goal | A group challenge on the daily (same counted tries); Game Center challenge on a daily recurring board | Bursts that pull players outside the daily ritual; anything that adds counted tries |
| Level based puzzle | Weekly milestone track; team chest | Short cohort event on a dedicated event level set; season pass | Purchasable ranked races; more than one event per scale |
| Hybrid casual | Daily challenge mode; weekly milestone | A collection event | Heavy event stacks (players come for a short loop; Color Block Jam reportedly grew with little live ops and heavy UA [Unverified, vendor source]) |
| Board and multiplayer | Weekly featured mode or tournament at peak hours; daily puzzle | Seasons of rated play when liquidity allows; club events | Events that split the matchmaking pool at low concurrency; events that change table rules (time controls, timeouts) |
| Web or PWA first | Same as the type; announce on the site, in share pages and communities | Discord or Reddit community events | Plans that depend on store surfaces |
| Store native | Same; Apple in-app events and Play promotional content for big moments | Game Center challenges | Store events for daily tasks (Apple calls them poor candidates [Official, 2026-10]) |
