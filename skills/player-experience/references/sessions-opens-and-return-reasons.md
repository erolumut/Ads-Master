# Sessions, Opens and Return Reasons

> Knowledge as of 2026-10 (research pass 2026-10-16, dossier `research/player-experience.md`). Facts about named games come from search summaries, trackers and vendor digests; treat every D1, D7 and D30 figure as a tracker estimate. The "player view" column is the dossier's reading of player and critic reaction, not a survey.

Gate: session designs, return reason lists and reminder requests are G1. A live change to lives, timers, streak rules or event timing reaches players and is G3. Sending a notification belongs to `lifecycle-crm`; designing an event calendar belongs to `game-liveops`.

## 1. The aim

More app opens and longer sessions, earned honestly: the player comes back because something real is waiting and stays because play is good, then leaves cleanly with a reason to return. A session that ends because the player chose to stop is a good session.

## 2. What top games use

From the dossier (section 4.3) and the retention notes.

| Mechanic | Games | Purpose | Player view | Label |
|----------|-------|---------|-------------|-------|
| Lives with refill timers (5 lives, about 30 minutes each) | Royal Match, Candy Crush, Color Block Jam | Return when full; refill revenue | Criticised as "wait to play" and "pay to skip" | [Reported, 2026-10] |
| Timed infinite lives as rewards | Royal Match | Longer sessions without churn at zero lives | Friendly | [Reported, 2026-10] |
| Layered event calendar (tournaments, win streaks, team events, album chase; weekend peaks) | Royal Match (Sensor Tower 2026), Monopoly Go (events every 1 to 3 days) | Opens and revenue | Neutral; pressure concerns for children | [Reported, 2026-10] |
| Win streak with escalating pre placed boosters, lost on fail | Royal Match | Longer sessions, stakes on the end of level offer | Mixed (loss aversion) | [Reported, 2026-10] |
| Team chest, team life requests | Royal Match | Opens through social obligation | Questionable for social pressure | [Reported, 2026-10] |
| Continue after fail (coins for 5 moves at rising price; rewarded revive) | Royal Match, Block Blast | Revenue | Criticised; rewarded revive seen as friendlier | [Reported, 2026-10] |
| New obstacle introduced alone; 200 new levels a month | Royal Match | Learnability; content runway | Friendly | [Reported, 2026-10] |
| Daily rewards, daily boosters, quick daily goals | Candy Crush, Monopoly Go | Opens | Mostly accepted | [Reported, 2026-10] |
| Streaks and badges, no purchase, no timer | NYT Games (11.2B solves in 2025) | Opens | Valued by players | [Reported, 2026-10] |
| Sticker albums with packs | Monopoly Go | Revenue and length | Criticised as gambling like | [Reported, 2026-10] |

Context numbers, all tracker or company estimates:

| Fact | Label |
|------|-------|
| Block Blast: about 70M DAU and 300M MAU (company press release, 2026-01) | [Reported, 2026-01] |
| Block Blast session about 12 minutes (Udonis, AppMagic) | [Reported, 2026-10] |
| Block Blast retention figures conflict between sources | [Contested] |
| Monopoly Go: 70% return daily (Sensor Tower) | [Reported, 2026-10] |
| Royal Match: Royal Pass +2% D30 (Naavik) | [Reported, 2026-10] |
| Color Block Jam: about 10% D90 called "healthy" by a Rollic VP | [Reported, 2026-10] |
| GameAnalytics: median D1 about 22% in 2025, declining | [Reported, 2026-10] |
| NYT Games: no streak freeze found; bonus puzzles do not affect streaks; the 2024 strike asked players to break streaks | [Reported, 2026-10] |

Read these as "what exists", never as targets.

## 3. Our allowed versions

| Market mechanic | Our version | Why |
|-----------------|-------------|-----|
| Lives with refill timers | Not a default. If the game repo uses lives, a refill is a neutral state ("lives full") the player may see; never a pressure message; never sold with a countdown aimed at minors | "Wait to play" and "pay to skip" are the criticised core |
| Timed infinite lives as a reward | Allowed as a reward for play (an event milestone), same for every player who reaches it | Friendly; extends sessions without a gate |
| Layered event calendar | Owned by `game-liveops`; this package asks only that events add content, not obligations, and that shared event boards never adapt | Opens from real content |
| Win streak with escalating boosters lost on fail | Use a gentle form: boosters earned by a streak are kept in part on a fail, or the streak counts wins without escalating stakes; never tied to an end of level offer | Loss aversion attached to an offer is a pressure pattern |
| Team chest and life requests | A team goal that fills from anyone's play; no per member blame; no request spam (cap requests) | Social without obligation |
| Continue after fail | Owned by `game-monetization` under the [monetization contract](../../game-monetization/references/monetization-contract.md): fixed price, no escalation, capped. The engine never makes a fail likelier to sell a continue | Fairness and consumer law |
| Mechanic introduced alone, steady content | Adopt fully | Learnability and runway |
| Daily rewards and quick goals | Cumulative calendars that never reset; a small daily goal from real content | Accepted, if no reset threat |
| Streaks and badges, no purchase, no timer | Adopt, with free automatic rest days and a permanent best streak | Valued; see [game-liveops streak rules](../../game-liveops/references/daily-loops-and-streaks.md) section 3 |
| Sticker albums with paid packs | Not proposed | Gambling like criticism; KIDS Act direction on variable rewards |

## 4. Session endings with a next goal

A session should end on a known next step, not on a trap.

| Ending | What the player sees | What never appears |
|--------|----------------------|---------------------|
| After a win | The next level's goal or a progress bar toward a visible milestone | A countdown to "lose" a reward |
| After a fail | Retry, a hint offer (policy), a break offer after a long streak | A loss animation that frames the stop as failure; an offer stacked on an offer |
| After the daily | "Done for today", next tick in local time, the streak status (with rest days) | "Come back or lose your streak" |
| On a break accepted | "This level will wait for you" and the next goal | A purchase prompt |
| On out of content | "New levels on <date>" if the date is real | A fake date |

The `show_next_goal` action in the [policy](adaptive-policy-design.md) section 3.5 is the engine's hook; the content is the game's. Let the player stop cleanly: one tap to the home screen, no exit interstitial.

## 5. Return reasons

A return reason is why the game may tell a player to come back. It comes from real content or the player's own state, never from what the player is worth.

| Source (policy `source`) | Examples | Strict tier (minors) |
|--------------------------|----------|----------------------|
| `content` | A new daily, new levels, an event that started | Allowed, capped |
| `timer` (player's own state) | A timer the player started finished (a build, a refill the player asked about) | Allowed if the player set it; no pressure copy |
| `social` | A friend's move in a turn based game, a team goal filled | Allowed with care; no blame, no request spam |
| `streak` | Streak status reminders | Blocked by the checker in the strict tier |
| `loss` | Anything framed as a coming loss | Blocked by the checker in the strict tier; not proposed for adults either |

Source names other than `content` here are this module's working vocabulary; the checker blocks `streak` and `loss` in the strict tier ([policy format](policy-format.md) section 5). Agree new source names with the policy owner before using them.

### 5.1 Copy rules

1. Say what is waiting ("Today's puzzle is ready", "Level 120 to 140 just arrived"), not what the player will lose.
2. No guilt ("we miss you", "your team needs you"), no streak loss threats, no fake scarcity.
3. Never mention money, offers or ads in a return reason unless it is a declared marketing message handled by `lifecycle-crm` under its consent rules.
4. Same copy for every player with the same reason.

### 5.2 Caps and quiet hours

| Cap | Placeholder | Rule |
|-----|-------------|------|
| `maxPerDay` per reason | 1 | Required by the checker |
| `quietHours` | Sample uses 21:00 to 09:00 local | Required by the checker; set per market with `lifecycle-crm` |
| Total across reasons | One per day for most players | Decided with `lifecycle-crm` frequency rules |
| Silence after no response | Stop after several ignored reminders | [Practitioner consensus]; `lifecycle-crm` owns the rule |

### 5.3 Handoff to lifecycle-crm

The engine and this package produce the list of return reasons and the moments they become true. `lifecycle-crm` owns the channel (push, email, in-app), consent, opt in, frequency, timing and copy approval with `compliance` ([game notifications](../../lifecycle-crm/references/game-notifications-and-community.md)). Send:

```
Return reason: <id>
Source: content | timer | social
True when: <event, e.g. daily published for the player's day id>
Audience: opted in players; strict tier excluded from: <list>
Caps: maxPerDay <n>, quiet hours <local>, total cap shared with lifecycle-crm
Copy draft (for compliance): "<one line>"
Measure: opens within 24 hours of send vs holdout (see experiments)
```

## 6. Streaks with rest days

Follow the `game-liveops` streak rules: earned stays earned, best streak is permanent, rest days are free and automatic, no threat messages, no paid repair by default. The engine adds one point: a streak never changes difficulty. A player on a long streak gets the same levels and the same policy as anyone else; the streak is never a reason to ease, raise or offer.

## 7. Session length without pressure

| Lever | Honest version | Pressure version (out) |
|-------|----------------|-----------------------|
| Pacing | Rest levels after peaks; a quick win after a fail streak via a hint offer | Removing rest levels to stretch time |
| Goals | A visible milestone a few levels away | Endless near completion bars that never complete |
| Rewards | Timed infinite lives earned through play | Lives that run out to force a wait or a buy |
| Replay | Voluntary replay of a favorite level, practice mode | Forced repetition |
| Breaks | Offered after long fail streaks | Never offered |
| Stops | One tap exit, next goal shown | Exit interstitials, "are you sure?" chains |

Measure session length together with fun proxies (voluntary replay, one tap rating) and guardrails (quit after fail). A longer session with more quits after fails is a worse product ([experiments](experiments-and-measurement.md)).

## 8. Strict tier for minors

Follow the KIDS Act direction before it is law. The proposal COM(2026) 681 (2026-09-17) reportedly covers, for minors in online games: real money value for currency, no variable rewards, no streaks or daily return rewards, nothing that undermines a minor's decision to stop or pushes play at set times through penalties or lost benefits, profiling based recommendations off by default [Reported, 2026-09]. It is a proposal, not law, and sources conflict on scope.

| Item | Strict tier |
|------|-------------|
| Streaks | Cumulative counters only (never reset); no streak return reasons (the checker blocks `streak`) |
| Daily return rewards | None; daily content stays, without rewards for returning |
| Loss framed messages | None (the checker blocks `loss`) |
| Variable paid rewards | None |
| Timers | No timers that push play at set times |
| Profiling | Adaptation runs on in session play signals only; profiling based recommendations off by default; no ad SDK profiling |
| Breaks | Offered sooner (placeholder: lower fail streak threshold) |
| Notifications | Only `content` reasons, lowest caps, wider quiet hours, with `lifecycle-crm` and parental consent rules |

When age is unknown and the product can reach minors, apply the strict tier ([ethics](ethics-law-and-store-rules.md)).
