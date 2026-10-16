# Daily Loops and Streaks

> Knowledge as of 2026-10. Apple and Android rules here were read at the official pages on 2026-10-12 [Official]. Facts about Wordle, LinkedIn games and Duolingo come from search summaries [Reported, 2026-10]. Patterns without a public source are labeled [Practitioner consensus] or [Practitioner heuristic]. This module specifies the daily layer around a game; the game repo owns the rules, the content and the implementation.

Gate: a daily loop spec, a streak rule draft and a reminder plan are G1. Changing a live streak rule, a tick time or a reminder schedule reaches players and is G3 (change request with rollback). Reminder sends belong to `lifecycle-crm`.

## 1. What the daily loop is

The daily loop is the smallest repeating unit of retention: one reason to open the game today and one reason to come back tomorrow.

| Step | Question it answers | Owner of the build | What liveops specifies |
|------|---------------------|--------------------|------------------------|
| 1. Trigger | Why open now? | Game repo, `lifecycle-crm` for messages | The daily moment (tick time), the reminder moment request, the store and in-game surfaces that show "today" |
| 2. Today's play | What is new today? | Game repo | That something is new every day and is the same for everyone who compares results |
| 3. Result | How did I do, compared to whom? | Game repo | The comparison set (self, group, everyone), the share artifact |
| 4. Social moment | Who sees it? | Game repo | Group board, share grid, friend notifications |
| 5. Closure | Am I done? What happens tomorrow? | Game repo | A calm "done for today" state with the next tick in local time and the streak status |

The loop works when steps 2 to 5 fit inside one short session and step 1 happens without a push for the engaged core. A loop that needs a push every day for most players is a loop that is not yet a habit.

Write the daily promise in one sentence before anything else, for example "one new puzzle, two tries, the best counts, your group sees it". If the sentence needs a second clause to explain a reward, the loop is too complex for a player who reads nothing.

## 2. The shared daily (Wordle style)

### 2.1 The pattern

One puzzle per day, the same for everyone who compares results, with a spoiler free share artifact. Evidence:

| Product | What it does | Label |
|---------|--------------|-------|
| Wordle (NYT) | One puzzle a day released at midnight in the player's time zone; statistics show Played, Win %, Current Streak and Max Streak; a puzzle finished after local midnight breaks the current streak and starts a new one | [Reported, 2026-10] (NYT Help Center via search) |
| Wordle share grid | Colored squares that show the path, never the letters | [Reported, 2026-10] |
| LinkedIn games | Daily puzzles reset at midnight Pacific Time; streaks; comparisons with connections; company or school boards reported by some guides and not by others | Reset and streaks [Reported, 2026-10]; boards [Unverified] |
| NYT Games | Puzzles as a subscription product; The New York Times Company reported 13.35 million subscribers across its products in Q2 2026 (not a games only figure) and said paywalling The Mini in Q3 2025 added single product subscribers | [Reported, 2026-10] (10-Q via search) |
| Puzzmo | Daily puzzles with an optional subscription (archives, leaderboards, no ads, about $40 a year); acquired by Hearst | [Reported, 2026-10] |
| Apple Game Center | Apple's own example of a challenge is a daily mini crossword: a recurring leaderboard that restarts daily, a game activity with a deep link to the crossword, and a challenge that is not repeatable | [Official, 2026-10] |

### 2.2 The day id and the tick

Every daily product needs one rule for when "today" starts. The day id must come from the server, never from the device clock, so a player cannot change the time zone to see tomorrow early or replay yesterday as today.

| Rule | How it works | Strength | Weakness | Seen in |
|------|--------------|----------|----------|---------|
| Local midnight | Day N starts at each player's local midnight | Natural ritual, "today" means today | A global board compares different windows; time zone changes need guarding; group members in two zones see two days | Wordle [Reported, 2026-10] |
| One global tick | Day N starts for everyone at one instant (00:00 UTC, or a home market time) | One shared day for every board; simple fairness and anti-cheat; a group plays the same puzzle at the same time | The tick lands at an odd local hour in far markets | LinkedIn games, midnight Pacific [Reported, 2026-10]; Play Games daily leaderboards reset at UTC-7 all year [Official, 2026-10] |
| Group home time | A group declares its zone and its day follows it | Fits friend groups in one city | A player in two groups lives two days; a board with scope `everyone` still needs one global rule | [Practitioner heuristic] |

Decision procedure (liveops proposes, the product owner decides, the game repo implements):
1. List the boards (contract section 3). If any ranked board has scope `everyone`, it needs one global day id. Local midnight is then a display choice, not the board's day.
2. Use the same day id for the streak, the group board and the global board. Two definitions of "today" produce disputes no support script can settle.
3. Pick the tick for the largest market's daily habit: a tick inside the evening play window in the home market means players see the day end while they still play [Practitioner heuristic].
4. Show the next tick in the player's local time on the closure screen and in the share text.
5. Write the rule into `ads-master/METRICS.md` through `measurement` (day boundary is a metric definition: D1 and DAU depend on it).

### 2.3 Seeds and fairness

- The puzzle for day N is fixed once published and auditable afterwards (a deterministic seed derived from the day id). The game repo owns the generator; liveops asks only that the seed is server side and logged.
- Counted attempts per day are a constant declared in the monetization policy (`countedAttemptsPerDay`). No event, reward, purchase or admin action changes them (contract section 3). A compensation after an outage is an `admin` grant in the grant log, never a silent database edit (contract runbook rule 7).
- Past days live in `practice` mode (archive, replay). They never write to a ranked board.

### 2.4 The share artifact

The share grid is the cheapest acquisition channel a daily game has, and it is also a retention device (it closes the day with a social act).

Checklist for the share artifact:
- [ ] No spoiler: the artifact never reveals the answer or the solution path in a way that ruins the day for someone who has not played.
- [ ] Day number and product name in the first line, so a group chat can tell days apart.
- [ ] Plain text first (emoji grid or score line) so it pastes into every chat app; an image is optional.
- [ ] A short link back to the product with a referral parameter defined by `measurement` (UTM or own `ref`), landing on today's play, not on a marketing page.
- [ ] Readable without color (shape or symbol carries the meaning, color only reinforces it) for color blind players.
- [ ] Localized label words; numbers and symbols stay universal.
- [ ] One tap from the result screen; never behind a reward or an ad.
- [ ] No incentive to share (no coins for sharing): incentivized shares fill chats with spam and invite platform policy problems [Practitioner consensus].

Read it with: share rate (shares / players who completed today), share link opens, new players from share links (definitions owned by `measurement`).

## 3. Streaks without punishment

### 3.1 Why no punishment

A streak motivates by loss aversion. Used gently it builds a habit; used as a threat it produces guilt, then a broken streak, then a player who does not come back because the number they cared about is gone [Practitioner consensus]. It also draws regulators:

| Signal | What happened | Label |
|--------|---------------|-------|
| vzbv (German federation of consumer organisations), 2025 | Reviewed five games and platforms, including Monopoly Go, and found manipulative design in all of them, naming countdowns, incentives to play daily and rewards for watching ads; objected to purchase offers that pop up right after app start; Scopely reportedly signed a cease and desist declaration | [Reported, 2026-10] (vzbv paper and heise coverage via search; research notes add opaque currencies and absence penalties to the list) |
| EU CPC key principles on in-game virtual currencies, 2025-03-21 | Real money prices, no forced currency purchases, protection of children | [Reported, 2026-10] |
| EU DSA Article 28 guidelines on minors, 2025 | Keep minors away from manipulative design | [Reported, 2026-10] |
| Digital Fairness Act | Proposal expected in Q4 2026, covering dark patterns and addictive design; not law | [Reported, 2026-10] |
| Paid streak repair | Listed as a deceptive pattern by Deceptive Design (Duolingo example) | [Reported, 2026-10] |

Ads Master position: a streak counts what the player did; it never takes away what they earned, and protection is free by default.

### 3.2 The rules

1. **Earned stays earned.** When a streak breaks, the count restarts; nothing earned along the way (items, cosmetics, badges, titles) is removed.
2. **Best streak is permanent.** Show the best streak next to the current one, so a break never erases the achievement.
3. **Rest days are free and automatic.** A small allowance of rest days (a streak freeze) applies by itself when a day is missed and the screen says so ("rest day used"). The allowance size is a product decision; it is the same for every player.
4. **Streak protection is a `streak_protection` grant.** Under the contract it changes play whenever the streak is shown competitively (a streak board, group streak comparisons, a friends list sorted by streak). The product decides and declares whether its streak is competitive before it rewards or sells protection (contract sections 3 and 10).
5. **Never sold by default.** Ads Master does not propose selling streak protection or repair for real money. If a product owner wants to, it is a G3 decision with `game-monetization` and `compliance`, never for minors, and never while the streak is competitive.
6. **No ad gated rescue.** A rewarded ad to save a streak is a `streak_protection` grant too (the placement grants it); same rules as rule 4 and 5, and it ties loss aversion to ad views [Practitioner consensus].
7. **Welcome back, not you lost.** The first screen after a break greets the player and starts day 1; no loss animation, no "you lost X".
8. **No threat messages.** No push or in-game copy that says a streak will die or expire. One neutral reminder that today's play is ready, at the player's own habit time, for opted in adults only (section 5).
9. **Same day id as the boards.** The streak uses the server day id from section 2.2; time zone travel never breaks a streak by itself (grace for the travel day is a product choice; log it).
10. **Group streaks never blame.** A group streak shows how many played ("4 of 5 played today"), never who broke it.

Duolingo's streak freeze, bought in advance with in-app gems and filling one missed day, with up to two equipped at a time [Reported, 2026-10], shows the mechanic works at scale; Ads Master keeps the mechanic and drops the paid part by default.

### 3.3 Streak forms

| Form | Counts | Best for | Risk | Note |
|------|--------|----------|------|------|
| Consecutive days | Days in a row with a completed daily | Shared daily puzzles | Harsh on one missed day | Pair with free rest days |
| Consecutive days with rest days | As above, with an automatic allowance | Default for daily games | Allowance too small feels like no allowance | Show the allowance on the streak screen |
| Weekly streak | Weeks with at least k play days | Level games, board games, weekend players | Less daily pull | Gentlest; fits players with irregular weeks |
| Group streak | Group days on which at least m members played | Daily social games with groups | Social pressure, blame | Show counts, never names; minors excluded from nudges |
| Cumulative counter | Days played this season or ever, never resets | Every game, especially for minors | Weak daily pull alone | Pair with the season (Events and seasons module) |

### 3.4 Login calendars

A login calendar (rewards for days 1 to 7) is a streak in disguise. Use the cumulative form: the next reward unlocks on the next day the player returns, whenever that is. Never reset the calendar to day 1 after a missed day [Practitioner consensus]. Rewards are economy sources: send the ladder to `game-monetization` for the sinks and sources sheet; in ranked modes they may be only `cosmetic`, `access` or `pass` grants (contract section 3).

### 3.5 Streak metrics (proposed to measurement)

| Metric | Definition (proposal; `measurement` owns the final one) | Read |
|--------|----------------------------------------------------------|------|
| Streak distribution | Share of DAU with current streak 1, 2 to 6, 7 to 29, 30 or more | Habit depth; rising long buckets mean habit forming |
| Break rate | Players whose streak ended yesterday / players with a streak of 2 or more the day before | Watch after tick or rule changes |
| Recovery rate | Players who return within 7 days after a break / players whose streak broke | The punishment test: a low rate means breaks end relationships |
| Rest day use | Rest days applied / streak players per week | Allowance sizing |
| Day over day return | Players active on day d and d+1 / players active on day d | The daily loop's own retention curve |

Proposed event names (snake_case, matching the contract's event style): `daily_started`, `daily_completed`, `share_created`, `share_opened`, `streak_extended`, `streak_protected`, `streak_broken`, `streak_restarted`. `measurement` owns the tracking plan.

## 4. Daily loop by game type

| Game type | Daily unit | Comparison set | Streak form | Reminder moment | Watch |
|-----------|-----------|----------------|-------------|-----------------|-------|
| Daily social mini game (groups, 21 day seasons, two tries a day) | One shared seeded round per day, counted tries constant | Group day board, group season table, global day board | Consecutive with free rest days; group count view | Group activity ("3 of 5 played") and the daily tick, opted in | Daily completion rate, group active members, share rate, tries used |
| Level based puzzle (Royal Match, Color Block Jam) | Levels, plus a daily task or bonus | Self, team | Weekly or login calendar (cumulative) | Event start, lives refilled only if the game uses lives (never a pressure message) | Sessions per DAU, level progress per day, event participation |
| Hybrid casual | Short runs, daily challenge mode | Self, global daily board | Login calendar (cumulative) | Rarely; the loop must stand alone | D1, session count; ad pressure early |
| Board and multiplayer (rated play, a daily puzzle, tournaments, clubs) | A daily puzzle plus "your turn" in async games | Friends, club, rating ladder | Daily puzzle streak with rest days; never a streak on rated wins | Turn notifications are transactional; daily puzzle reminder is marketing | Match start time, daily puzzle completion, games per DAU |
| Web or PWA first | Same as the type above | Same | Same | Web push only after a user gesture; on iOS only for Home Screen web apps (section 5) | Share link to play conversion, Home Screen installs |
| Store native | Same | Plus Game Center and Play Games boards | Same | Native push with platform rules | Permission rate, friend notifications |

## 5. Reminder timing (with lifecycle-crm)

Liveops requests reminder moments; `lifecycle-crm` owns consent records, frequency caps, copy production, sends and holdouts. Every send is G3.

Platform rules to respect:

| Rule | Detail | Label |
|------|--------|-------|
| Apple 4.5.4 | Push must not be required for the app to work; push for promotions or direct marketing only after explicit opt in through consent language in the app UI, with an in-app way to opt out | [Official, 2026-06] |
| Apple 4.5.3 | No spam or unsolicited messages through Game Center, push or Live Activities | [Official, 2026-06] |
| Apple 5.1.2(i) | An app may not require users to enable push to receive monetary or other compensation: no coins, lives or rest days for turning notifications on | [Official, 2026-06] |
| Android 13+ | Notifications need the `POST_NOTIFICATIONS` runtime permission; after "Don't allow" the app cannot send non exempt notifications | [Official, 2026-10] |
| Web push on Apple | Home Screen web apps on iOS 16.4 or later and Safari on macOS; permission requested from a user gesture; every push must show a visible notification or Safari revokes the permission | [Official, 2026-10] |

Timing practice:

| Practice | Why | Label |
|----------|-----|-------|
| Ask for notification permission after the first completed daily, not at first launch | The player has seen the value; a first launch prompt gets fewer grants | [Practitioner consensus] |
| Send the daily reminder at the player's own habit time (the hour they usually play), local time | Fits the habit instead of interrupting | [Practitioner consensus] |
| At most one liveops reminder per player per day by default; `lifecycle-crm` sets the real caps | Fatigue and opt outs | [Practitioner heuristic] |
| Step down after ignored reminders (for example daily to weekly after several ignored days) | Silence is an answer; continued sends raise opt outs | [Practitioner heuristic] |
| Quiet hours and no reminders to players under 18 that use loss or urgency words | Minors rules, store rules | Contract runbook rule 6 |
| Turn notifications in async multiplayer are transactional, not marketing; still opt in and capped | Players asked for them by starting the game | [Practitioner consensus] |

Request format to `lifecycle-crm` (journal entry plus handoff):

```
Reminder moment request: <product>, <moment id>
Moment: daily tick | habit time | group activity | event start | season start | turn ready
Audience: opted in players, adults only for marketing reminders, segment rule
Timing rule: local time window, cap, step down rule
Message intent (no final copy): "today's puzzle is ready"
Deep link: <link into today's play>
Holdout: <percent, read metric, read date>
Calendar row: <LIVEOPS_CALENDAR id>
```

## 6. Web or PWA first vs store native

| Topic | Web or PWA first | Store native |
|-------|------------------|--------------|
| Daily surface | The URL is the habit; a bookmark or Home Screen icon; share links land on today | Home Screen icon, widgets, Game Center and Play Games surfaces |
| Reminders | Web push (iOS only for Home Screen web apps), email, community channels (Discord, Reddit) | Native push, Live Activities (no spam, Apple 4.5.3) |
| Social proof | Share grids in chats; Discord Activities for group play (Embedded App SDK, SKUs in some regions) [Reported, 2026-10]; Reddit Devvit encourages daily games [Reported, 2026-10] | Game Center friend notifications when a friend passes a score, even if the game is not installed [Official, 2026-10]; challenges up to 16 players [Official, 2026-10] |
| Day boundary | Server day id; the browser clock is untrusted | Same; Play Games daily boards reset at UTC-7 if used [Official, 2026-10] |
| Store events | None (the web has no store calendar) | Apple in-app events and Play promotional content (calendar module) |

A web first daily game reaches store surfaces later through a wrapper; plan the day id and the share link so they survive the move (the same link opens the web day or the installed app).

## 7. Daily loop audit questions

| # | Question | Pass when |
|---|----------|-----------|
| 1 | Is the daily promise one sentence a new player understands without reading? | Written and tested on 5 new players |
| 2 | Is the day id server side, with one rule shared by streaks and boards? | Rule written in METRICS.md |
| 3 | Is the next tick shown in local time at closure? | Visible on the closure screen |
| 4 | Is the share artifact spoiler free, plain text first, linked with a referral parameter? | Checklist 2.4 passes |
| 5 | Does a broken streak keep everything earned and show the best streak? | Verified in the build |
| 6 | Are rest days free, automatic and equal for all? | Verified; protection declared per contract |
| 7 | Is any copy or push a threat ("will die", "last chance")? | None found |
| 8 | Is notification permission asked after value, with no reward for granting it? | Verified on iOS and Android |
| 9 | Do past days live only in practice mode? | No archive play writes to a ranked board |
| 10 | Are the daily metrics in section 3.5 defined by `measurement`? | Present in METRICS.md |

## 8. Worked example (illustrative numbers)

A daily social game sees its recovery rate at 18%: of players whose streak broke, 18% came back within 7 days, against 41% day over day return for active players. Streak screens show "Streak lost" in red. Liveops reads it as punishment, not difficulty, and drafts a change set: free automatic rest days (allowance equal for all, declared non competitive streak), best streak shown permanently, a "welcome back" screen. `compliance` approves copy; `lifecycle-crm` removes the evening "your streak is at risk" reminder. Design: 50/50 split randomized by group (players in one group share streak views; section on clustering in [Experiments and remote config](experiments-and-remote-config.md)). Primary metric: recovery rate; guardrails: DAU, day over day return, share rate. Read after 3 full weeks. All numbers in this example are illustrative, not benchmarks.
