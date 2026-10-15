# Liveops Playbooks

> Knowledge as of 2026-10. Every play ends in a change request for human approval. Drafts in `ads-master/` are G1; unsubmitted store events, Play drafts, unpublished config and created but unstarted experiments are G2; anything players see (an event going live, a config change, a store submission, a reminder send, a season date change) is G3. Follow the project's automation stage in `ads-master/GUARDRAILS.md`.

Plays: 1 First live event, 2 Launch a season, 3 Rescue falling D7, 4 Holiday calendar, 5 Sunset, 6 Weekly liveops loop, 7 Difficulty flag, 8 Store event submission, 9 Live incident, 10 Change request.

## Play 1: First live event

Entry: a product with a working daily loop or level progression, KPI definitions in `METRICS.md`, remote config, and at least two weeks of stable D1 and D7.

| Step | When | Action | Owner | Gate |
|------|------|--------|-------|------|
| 1. Pick the job | T minus 6 weeks | Choose what the event should move (return across days, sessions, group activity) and the format that moves it ([Events and seasons](events-and-seasons.md) section 2); for a first event, a weekly milestone track or a community goal is the safest | game-liveops | G1 |
| 2. Spec | T minus 5 weeks | Event spec (section 3 of the events module): eligibility, qualifying action, ladder as typed grants, end rules, fairness, kill switch, telemetry | game-liveops | G1 |
| 3. Economy | T minus 5 weeks | Reward ladder into the sinks and sources sheet; any offer around the event | game-monetization | G1 |
| 4. Feasibility | T minus 4 weeks | Game repo confirms build cost and date; event config as data where possible | Game repo | |
| 5. Measurement | T minus 4 weeks | Events in the tracking plan; holdout (10% by player, or by group for group features); read date | measurement | G1 |
| 6. Calendar | T minus 4 weeks | Calendar row; `liveops_calendar_check.py` exit 0 | game-liveops | G1 |
| 7. Copy and store | T minus 3 weeks | Event copy intent to `compliance`; store event only if the event is a real limited moment with new content (Apple); otherwise in game surfaces only | app-store-optimization, compliance | G1 |
| 8. Reminders | T minus 2 weeks | Event start reminder moment request | lifecycle-crm | G1 |
| 9. QA | T minus 1 week | Event on a test build or test accounts; kill switch tested; deep links tested | Game repo | G2 |
| 10. Approve | T minus 3 days | Change request: go live, holdout, reminder, store event | Human | G3 |
| 11. Live check | T plus 1 hour and T plus 1 day | Participation curve, errors, complaints; kill switch ready | game-liveops | G0 |
| 12. Read | End plus 7 days | Event read template; decision: repeat, change, rest, retire | game-liveops | G1 |

Exit: a read with uplift vs holdout, a decision, and an EXPERIMENTS.md row closed.

## Play 2: Launch a season

Entry: a product with at least one event read and a daily or weekly rhythm; season length chosen ([Events and seasons](events-and-seasons.md) section 6.2).

1. **Season plan (T minus 6 weeks).** Dates in the day id zone, theme, free track and its completion target, premium track shape (with `game-monetization`), reset and persist table, catch up rule, weekly events inside the season, recap card.
2. **Fairness check.** Season tables are derived ranked boards: nothing purchasable feeds them; pass grants are `pass`, `cosmetic` or `access`; group rounds write only to group boards (contract).
3. **Economy and price (T minus 5 weeks).** `game-monetization` prices the pass and the `on_season_start` offer; `monetization_check.py` passes on the updated policy.
4. **Store (T minus 3 to 2 weeks).** Apple in-app event with the New Season badge, promoted up to 14 days ahead, submitted so approval lands before the promotion start; Play promotional content draft (major update type when the season adds real content; verify types in the console); featuring nomination by `app-store-optimization` for a big season.
5. **Reminders.** Season start, mid season checkpoint and final week moments requested from `lifecycle-crm`; no countdown copy; minors excluded from urgency.
6. **Measurement.** Season participation, progress distribution, completion, next season return; holdout by group when the season is new.
7. **Go live (G3).** At the tick; live check within the first hour.
8. **Middle.** Weekly read of progress against plan; if the median participant is behind the completion plan by week 2, propose a catch up adjustment (reward pacing, never ranked rules).
9. **Close.** Standings frozen at the tick, unclaimed free rewards granted, recap share card, the season read within 7 days.
10. **Next season.** Announce before the close so the gap is short.

## Play 3: Rescue falling D7

Trigger: classic D7 of mature cohorts below the 8 week median for two consecutive weekly cohorts, confirmed by `measurement`.

| Step | Action | Detail |
|------|--------|--------|
| 1. Confirm | Same definition, mature cohorts only | No D7 read before day 7 is complete |
| 2. Mix | Split by source, market, platform, version, entry point | If every segment held, it is mix: report to `mobile-app-growth`, change nothing in the game |
| 3. Stage | D1 stable or falling too? | D1 falling too: first session problem (game repo); D1 stable: D1 to D7 problem (this play) |
| 4. Daily loop | Day over day return, daily completion, share rate | A bad daily round or a weak closure screen shows here |
| 5. Streaks | Break rate, recovery rate | Low recovery means punishment: streak rule change set |
| 6. Levels | `level_flags.py` on levels reached in days 1 to 7 | Churn spikes become difficulty flags |
| 7. First event and social | When does a new player meet the first event and the first group or team? | Too late: lower the unlock gate (test it) |
| 8. Reminders | Permission rate and reminder engagement for days 1 to 7 | Ask after value; habit time sends |
| 9. Pick 2 bets | Impact x confidence x ease | Each as an experiment with a holdout and a stop rule |
| 10. Read | After the outcome window | Roll out, iterate or kill; memory after confirmation |

Never: add counted tries, add pressure (countdowns, loss messages) or raise reminder volume as a D7 fix.

## Play 4: Holiday calendar

| When | Action |
|------|--------|
| 12 weeks before the quarter | List moments per market ([Calendar](liveops-calendar-and-store-events.md) section 6); look up moving dates for this year |
| 10 weeks | Pick the 2 or 3 moments that fit the product's audience; theme only for religious holidays; child themed moments flagged as child directed |
| 8 weeks | Event specs or theme specs; art brief to `creative-strategy` (16:9 and 9:16 store media) |
| 6 weeks | Offers with `game-monetization`; copy intents to `compliance`; featuring nomination plan with `app-store-optimization` |
| 4 weeks | Calendar rows; checker exit 0; freeze windows added for the store holiday period (check Apple Developer News each November) |
| 3 to 2 weeks | Apple in-app events submitted (Special Event badge for holiday events with new content); Play promotional content submitted 4 to 60 days ahead |
| During | Daily live check; reminders as approved |
| 2 weeks after | Reads vs last year's same moment (memory); retire moments that read flat twice |

## Play 5: Sunset (an event type, a mode or the game)

1. Decide with data: participation and uplift trend, cost to run, content runway, complaints.
2. Human decision for a mode or the game (G3); `game-liveops` decides retiring an event type with approval.
3. Notice: in game and calendar at least one full cycle ahead ([Player trust](player-trust-and-pressure-patterns.md) section 7).
4. Value: purchased items converted, refunded or kept usable (`game-monetization`, `compliance`); unclaimed free rewards granted automatically.
5. Surfaces: store events, reminders, promotional text and featuring plans tied to the content end on time.
6. History: results and badges stay visible where the product continues.
7. For a full game sunset: refunds, data export, account deletion paths and store removal are human actions with `compliance` and `store-submission`.
8. Read: what happened to players of the retired content (did they move to other content or leave?).

## Play 6: Weekly liveops loop

| Step | Time | Detail |
|------|------|--------|
| 1. Data | 10 min | Exports or connectors; date range; changes in the period (releases, incidents, events) |
| 2. KPIs | 15 min | D1, D7, D30 of mature cohorts, stickiness, daily loop metrics, participation, season progress ([Retention diagnostics](retention-diagnostics.md) section 8 memo) |
| 3. Flags | 10 min | `level_flags.py` on the funnel; daily round reads for daily games |
| 4. Events | 10 min | Live event health; reads due this week |
| 5. Calendar | 10 min | Next 6 weeks; `liveops_calendar_check.py --today <date>`; submissions and assets due |
| 6. Tests | 5 min | Running experiments: SRM, guardrails, read dates |
| 7. Handoffs and change requests | 10 min | Reminder requests, offers, store copy, flags to the game repo; journal |

At Starter tier, run it every 2 weeks and keep the daily morning check for daily games.

## Play 7: Difficulty flag

Trigger: `level_flags.py` exit 1 (a churn spike), a daily round with a broken completion rate, or a complaint theme naming a level.

1. Re-run on mature cohorts; split payers and non payers if continue pressure is flagged.
2. Check what else changed: release, incident, event, UA mix.
3. Write the flag ([Content cadence and difficulty signals](content-cadence-and-difficulty-signals.md) section 6): evidence and a question, no parameter change.
4. Journal entry; the human routes it to the game repo's tracker.
5. When the game repo ships its decision, re-read on new mature cohorts and close the flag with the result.

## Play 8: Store event submission

1. Calendar row exists, checker exit 0, the event is a good candidate (not a daily task, not a price only promotion).
2. `app-store-optimization` drafts the event name (30), short (50) and long (120) descriptions, purpose and priority; no prices, no "best" or "#1".
3. Media: 16:9 card and 9:16 details page, image or seamless loop video, no borders, minimal text ([Calendar](liveops-calendar-and-store-events.md) section 2.1).
4. Deep link tested on a fresh install and an existing install; pre start landing page if promotion starts before the event.
5. `compliance` verdict; `store-submission` review of metadata against store rules.
6. G2: create the event unsubmitted in App Store Connect (or the Play draft).
7. G3: submit; read back the status; log the submission in the journal.
8. After the event: impressions, opens, downloads and redownloads (App Store Connect) and Play console metrics into the event read.

## Play 9: Live incident during an event or a daily round

Trigger: a broken daily round, a crash or outage during an event, a wrong reward, an event live with wrong dates, or a store event pointing to a broken link.

| Step | Time | Action | Gate |
|------|------|--------|------|
| 1. Detect and declare | Hour 0 | Incident row in `INCIDENTS.md`; tell the human; stop proposing unrelated writes | G1 |
| 2. Contain | Hour 0 to 1 | Kill switch for the event or offer (remote config); pause reminders for it (`lifecycle-crm`) | G3 |
| 3. Protect fairness | Hour 1 | For ranked boards: the product owner decides whether the day stands, is voided or replayed; counted attempts never change for some players only | G3 |
| 4. Compensate | After the fix | Compensation as an `admin` grant in the grant log for every affected player, equal for all affected, never a silent database edit (contract runbook rule 7) | G3 |
| 5. Communicate | Day 0 to 1 | Plain in game notice; store event or promotional text adjusted if they point to the broken content (`app-store-optimization`) | G3 |
| 6. Learn | After recovery | Post incident note; QA gap to the game repo; checker or flag rule if a new class of problem | G1 |

## Play 10: Change request (all live liveops changes)

Use `ads-master/templates/CHANGE_REQUEST.md`. One line per change (example rows with illustrative numbers and ids):

| # | Surface | Entity | Change | From | To | Reason with data (source, range) | Expected effect | Risk | Rollback | Gate | Approval |
|---|---------|--------|--------|------|----|----------------------------------|-----------------|------|----------|------|----------|
| 1 | Remote config | `liveops.streak.rest_days` | Free rest days for 50% of groups (E041) | 0 | 1 per week | Recovery rate 18% vs 41% day over day return, 2026-09-14 to 2026-10-11 (measurement export) | Recovery rate up 5 points | Streak inflation; mitigated by the weekly allowance | Set to 0 for the treatment arm | G3 | |
| 2 | App Store Connect | In-app event LO-101 | Submit for review | draft | submitted | Calendar LO-101, checker exit 0, compliance verdict C-212 | Season starters from the event card | Rejection | Withdraw or edit metadata | G3 | |
| 3 | Calendar | LO-104 | Move community goal one week later | 2026-11-16 | 2026-11-23 | Overlaps the theme week audience (checker warning) | Higher participation in both | None | Restore dates | G3 | |

Read back every executed change and log it with a timestamp in the journal.
