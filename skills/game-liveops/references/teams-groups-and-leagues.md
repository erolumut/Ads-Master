# Teams, Groups and Leagues

> Knowledge as of 2026-10. Game Center facts were read at Apple's developer pages on 2026-10-12 [Official, 2026-10]; Play Games Services leaderboard facts at developer.android.com the same day [Official, 2026-10]. Teardown facts are [Reported, 2026-10] from search summaries. Ranked fairness follows the Game Monetization Contract v0.2 ([contract](../../game-monetization/references/monetization-contract.md)). Chat, moderation and safety rules are owned by `compliance` and the game repo; this module covers the retention layer.

Gate: social structure specs are G1. Changing team size limits, league rules, matching rules or group features that players see is G3. Moderation policy changes go through `compliance`.

## 1. Why social structures retain

Players who play with people they know come back for the people as much as for the game [Practitioner consensus]. The hits show the same parts again and again:

| Part | Example | Label |
|------|---------|-------|
| Team chest (collective goal) | Royal Match team chest | [Reported, 2026-10] |
| In team leaderboard | Royal Match top 3 inside the team | [Reported, 2026-10] |
| Partner events (pairs complete goals together) | Monopoly Go | [Reported, 2026-10] |
| Comparisons with real connections | LinkedIn games show how connections did | [Reported, 2026-10] |
| Friend notifications | Game Center notifies players when a friend passes their score, which can bring them back even when the game is not installed | [Official, 2026-10] |
| Friend challenges | Game Center challenges built on leaderboards, invite friends and contacts, scores in real time, up to 16 players | [Official, 2026-10] |
| Private groups | Daily social games where a friend group shares one daily board and season table (Aloo like) | Product pattern |

## 2. Structures

| Structure | Size | Who forms it | Comparison | Best for | Main risk |
|-----------|------|--------------|------------|----------|-----------|
| Friends | Any | Players (invites, contacts, platform friends) | Head to head, friends board | Every type | Empty for new players: cold start |
| Private group | Small (friends, family, office) | Players by invite link or code | Group day board, group season table | Daily social games | Dead groups when one or two members stop |
| Team or club | Medium | Players join open or invite only teams | Team chest, in team board, team vs team | Level games, board platforms | Free riders, inactive members, leader burnout |
| League | Fixed cohort per period | The system, by activity or skill | Promotion and relegation by rank | Weekly competitive rhythm | Demotion as punishment; pay to win if fed by purchasable progress |
| Global board | Everyone | The system | Rank or percentile | Daily puzzles, rated play | Top is unreachable: show percentile and nearby ranks instead |

Default for a small studio: friends and private groups first (they need no liquidity), teams later, leagues only when daily actives are high enough to fill cohorts with similar players [Practitioner heuristic].

## 3. Group and team health

A group with one active member is a solo player with an empty screen. Health is measured per group and acted on with gentle tools.

| Metric (proposed to `measurement`) | Definition | Read |
|------------------------------------|-----------|------|
| Active members per group | Members active in the last 7 days | Median and distribution; groups with 0 or 1 active are dying |
| Share of players in a healthy group | Players in a group with at least 3 members active in 7 days / DAU | The social retention base |
| Solo rate | DAU with no group or team / DAU | Cold start problem size |
| Group creation to second member | Groups that gain a second member within 48 hours / groups created | Invite flow health |
| Team contribution spread | Share of team chest progress from the top contributor | Free rider and burnout check |

Tools:
1. Invite flows that carry the group: one link that opens the group's today, on web and in the app (activities with party codes and a web fallback URL on Apple; invites open a web page when the API is unavailable [Official, 2026-10]).
2. Suggest active open teams to solo players and to members of dead teams; let a player leave a dead team without losing anything earned.
3. Team leaders can remove members inactive for a long period; the system never punishes the inactive member beyond leaving the team.
4. Merge or archive dead private groups only with member consent; never delete group history (history is part of what players earned).

## 4. Team events

| Format | How it works | Fairness note | Read |
|--------|--------------|---------------|------|
| Team chest | Members' play fills one goal; every member receives the reward | Collective, not ranked: progression grants may feed it | Completion rate by team size band |
| In team top 3 | Extra reward for the top contributors inside the team | A ranked board with scope `group`: fed only by play no purchase changes, or redesigned as a milestone | Contribution spread |
| Team vs team | Teams matched for a window, highest total wins | Ranked board; match by team activity; nothing sold changes totals | Share of matches decided by one player |
| Help requests and gifts | Members send each other help or gifts | Apple allows gifting of IAP eligible items; gifts refund only to the original purchaser and may not be exchanged [Official, 2026-06]; gifts that change play follow the contract's typed grants | Gift reciprocity, no pay to get help pressure |

Royal Match runs a team chest and an in team top 3 together [Reported, 2026-10]; under contract v0.2 the in team top 3 is only fair when its inputs cannot be bought (events module section 4).

## 5. Leagues

League rules are a meta layer the game repo implements; liveops proposes the shape and reads it.

Principles:
1. **Cohorts of similar players.** Place by recent activity and, where skill matters, by skill band; never by spend [Practitioner consensus].
2. **Soft demotion.** Protect the lowest band (no relegation out of it), protect new players for their first periods, and relegate only on ranks earned while active; a player who was away is paused, not demoted [Practitioner heuristic].
3. **Nothing sold changes a league result.** A league division is a ranked board with scope `group` (contract section 3).
4. **Visible rules.** Promotion and relegation zones shown from the first day of the period; the end time in local time.
5. **Season reset.** Placement resets softly at season end; rating math belongs to the game repo.
6. **Read.** Share of active players promoted, relegated and staying; churn after relegation vs after staying (relegation should not raise churn; if it does, demotion is punishment).

## 6. Groups in daily social games (Aloo like)

| Feature | Liveops role | Fairness |
|---------|--------------|----------|
| Group day board | Defines the comparison set and the day id rule; reads group activity | Ranked board with scope `group`; counted tries constant |
| Group season table | Season length, reset rules, recap card | Derived ranked board (fed by ranked daily points) |
| Group streak | Shows "4 of 5 played"; never names who missed | Derived board when shown competitively; `streak_protection` rules apply |
| Encore (a bonus round one member buys for the whole group) | Calendar slot (opens at the next tick, closes with the day), reminder moment for group members, read of group activity after encores | A `round` granted to the group writes only to group boards, never to the global board; buyer gets nothing the others do not (contract sections 3 and 10) |
| Group invite | Share link design, day carried in the link | Invite rewards never change play |

Group activity, not group count, is the retention signal: a product with many groups of one is a single player product with extra screens.

## 7. Multiplayer and board platforms (Avlu like)

| Topic | Practice | Label |
|-------|----------|-------|
| Liquidity first | An event that splits players across modes lengthens match waits; at low concurrency, concentrate play (one featured mode, scheduled tournaments) instead of adding modes | [Practitioner consensus] |
| Peak hour scheduling | Schedule live tournaments at each market's evening peak; one schedule per region when markets are far apart | [Practitioner consensus] |
| Rated seasons gated on liquidity | Start rated seasons when enough players are online to match similar ratings | Product pattern (a board platform plans 3 month seasons gated on a liquidity threshold) |
| Party codes | Game Center activities support party codes, with matchmaking that groups players with the same code; too many joiners on one code can split friends into different matches | [Official, 2026-10] |
| Async turn reminders | "Your turn" notices are transactional; opt in, capped, never used to carry marketing | [Practitioner consensus]; Apple 4.5.4 for marketing [Official, 2026-06] |
| Table rules are the game's | Events schedule and frame play; they never change time controls, timeout handling or scoring | Boundary rule |
| Daily puzzle on a board platform | Same seed for everyone, separate board, streak, spoiler free share grid | Product pattern; [daily loops module](daily-loops-and-streaks.md) |

## 8. Platform social features

| Feature | What it gives | Liveops use | Label |
|---------|---------------|-------------|-------|
| Game Center leaderboards | Friend passes your score: notification | Friend boards for weekly or daily competitions | [Official, 2026-10] |
| Recurring leaderboards | Boards that restart on a schedule (Apple's daily crossword example restarts daily) | Daily or weekly boards for challenges | [Official, 2026-10] |
| Game Center challenges | Score based competitions among friends before time runs out; built on an active leaderboard; up to 16 players; each submitted score consumes a challenge attempt; a revive mechanic submits after the player accepts or declines it | Friend challenges on the daily or weekly board; counted attempts stay the product's own rule | [Official, 2026-10] |
| Game Center activities | Deep links into content (Apple's example: send the player straight to the daily puzzle), party codes, minimum version prompts | Event and challenge entry points | [Official, 2026-10] |
| Apple Games app | Pre installed on iOS 26, iPadOS 26 and macOS 26; Home and Friends tabs; games with Game Center features and in-app events shown more prominently; a Top Played chart | Reason to adopt Game Center in store builds | [Official, 2026-10] |
| Play Games Services leaderboards | Daily, weekly and all time versions created automatically; daily resets at UTC-7 all year, weekly at midnight between Saturday and Sunday in the same zone; social and public boards | Daily and weekly boards on Android; align the product's day id or accept the offset | [Official, 2026-10] |

Note: Play Games Services "events" are analytics counters (for example currency sources and sinks), not live events [Official, 2026-10].

## 9. Safety and minors (route to compliance)

- User generated content and chat need a filter for objectionable material, a way to report content with timely responses, and the ability to block abusive users; random or anonymous chat experiences do not belong on the App Store (Apple Guideline 1.2) [Official, 2026-06].
- Minors: no open chat with strangers by default; group invites by link among known people; purchase approval rules per market (contract runbook rule 6).
- Leaderboards show nicknames, never real names or contact data by default.
- Every social feature with messaging goes to `compliance` before launch.

## 10. Anti patterns

| Anti pattern | Why it fails | Instead |
|--------------|--------------|---------|
| Team kicks or penalties for missing a day | Absence punishment; drives guilt churn | Leader removal after long inactivity only; no penalty |
| Global board as the only comparison | Top is unreachable for almost everyone | Friends, group, percentile, nearby ranks |
| Leagues before liquidity | Cohorts of mismatched or inactive players | Friends and groups first |
| Paid boosts to win team or league ranks | Ranked result for sale (contract) | Collective goals, cosmetic rewards |
| Shaming copy ("Ali broke the group streak") | Social pressure, harm to minors | Counts without names |
| Undisclosed bots in cohorts | Deception, trust loss | Disclose or do not use |
