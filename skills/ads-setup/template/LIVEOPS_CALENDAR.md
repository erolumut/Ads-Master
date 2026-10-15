# Liveops Calendar

> One calendar per product for every live moment: seasons, events, challenges, content drops, store events, offers, reminder moments, community moments, holidays and freeze windows. Drafted by game-liveops (offers by game-monetization), approved by the human each month; each go live is a G3 line in a change request. Run `liveops_calendar_check.py` after every edit.

Product: <product id>
Day id rule: <for example: one global tick at 00:00 UTC | local midnight with a global day id at 00:00 UTC>
Time zone for dates below: <IANA zone of the day id, for example UTC>
Calendar revision: <integer, raise on every approved change>
Last reviewed: <YYYY-MM-DD> by <name>

## Rules

- A moment that is not in this calendar does not go live.
- One event per time scale at a time (burst, short, week, season).
- Store rows: Apple events up to 31 days, promoted up to 14 days ahead, at most 10 published and 15 approved at once; no prices in event metadata. Play promotional content submitted 4 to 60 days before the start (verify in the console).
- Competitive formats declare their ranked board and scope (group or everyone); nothing sold changes them (Game Monetization Contract).
- Every measured format runs with a holdout at least once.
- Copy goes to compliance; reminders go to lifecycle-crm; offers come from game-monetization.

Field values:
- Format: milestone, collection, race, cohort_leaderboard, team_chest, in_team_leaderboard, community_goal, challenge, theme_week, tournament, premiere, season, league_season, content_drop, offer, community, holiday, freeze
- Scale: burst, short, week, season, annual, none
- Store: none, apple, play, both
- Badge (Apple): Challenge, Competition, Live Event, Major Update, New Season, Premiere, Special Event
- Status: idea, planned, approved, submitted, live, done, cancelled
- Dates: YYYY-MM-DD (start at 00:00, end at the end of that day) or YYYY-MM-DD HH:MM in the zone above

## Calendar

| ID | Name | Format | Scale | Start | End | Audience | Ranked board | Store | Badge | Promo start | Submit by | Deep link | Reminders | Offer ref | Holdout | KPI | Owner | Status |
|----|------|--------|-------|-------|-----|----------|--------------|-------|-------|-------------|-----------|-----------|-----------|-----------|---------|-----|-------|--------|
| LO-001 | <Season 1> | season | season | 2026-11-02 | 2026-11-22 | all | group_season (group) | both | New Season | 2026-10-26 | 2026-10-16 | <universal link to the season page> | season_start | <offer id from game-monetization or none> | 10% by group | Season completion, D7 of season starters | game-liveops | planned |
| LO-002 | <Community goal week> | community_goal | week | 2026-11-09 | 2026-11-15 | all | none | none | | | | <link> | event_start | none | none | Participation | game-liveops | idea |

## Store event metadata

| ID | Event name | Short description | Long description | Purpose | Priority |
|----|------------|-------------------|------------------|---------|----------|
| LO-001 | <Name, 30 characters> | <Short description, 50 characters> | <Long description, 120 characters> | all users | normal |

## Reads

| ID | Read date | Participation | Completion | Uplift vs holdout | Decision | Output file |
|----|-----------|---------------|------------|-------------------|----------|-------------|
