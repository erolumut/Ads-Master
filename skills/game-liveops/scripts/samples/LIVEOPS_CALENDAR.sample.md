# Liveops Calendar

> Sample for liveops_calendar_check.py: a daily social mini game product with group boards, 21 day seasons and two counted tries a day. Dates, names and links are illustrative, not a plan.

Product: example-daily
Day id rule: one global tick at 00:00 UTC
Time zone for dates below: UTC
Calendar revision: 3
Last reviewed: 2026-10-15 by sample

## Calendar

| ID | Name | Format | Scale | Start | End | Audience | Ranked board | Store | Badge | Promo start | Submit by | Deep link | Reminders | Offer ref | Holdout | KPI | Owner | Status |
|----|------|--------|-------|-------|-----|----------|--------------|-------|-------|-------------|-----------|-----------|-----------|-----------|---------|-----|-------|--------|
| LO-101 | Autumn Season | season | season | 2026-11-02 | 2026-11-22 | all | group_season (group) | both | New Season | 2026-10-26 | 2026-10-16 | https://example.com/season/7 | season_start | none | 10% by group | Season completion, D7 of season starters | game-liveops | planned |
| LO-102 | Harvest Words week | theme_week | week | 2026-11-09 | 2026-11-15 | all | none | apple | Special Event | 2026-11-02 | 2026-10-23 | https://example.com/week/harvest | event_start | none | none | Share rate, day over day return | game-liveops | planned |
| LO-103 | Friday Duel | challenge | short | 2026-11-13 | 2026-11-15 | groups of 3 or more | group_day (group) | none | | | | https://example.com/duel | none | none | 10% by group | Group active members | game-liveops | idea |
| LO-104 | Million Words together | community_goal | week | 2026-11-16 | 2026-11-22 | all | none | none | | | | https://example.com/goal | event_start | none | 5% | Participation, sessions per DAU | game-liveops | idea |
| LO-105 | Season pass window | offer | none | 2026-11-02 | 2026-11-08 | all adults | none | none | | | | | none | season_pass_at_season_start | n/a | Pass conversion | game-monetization | planned |
| LO-106 | Thanksgiving (US) | holiday | none | 2026-11-26 | 2026-11-26 | US | none | none | | | | | none | none | n/a | | game-liveops | planned |
| LO-107 | New mini game premiere | premiere | short | 2026-12-07 | 2026-12-20 | all | none | both | Premiere | 2026-11-30 | 2026-11-20 | https://example.com/new | event_start | none | none | New game DAU share, D7 | game-liveops | idea |
| LO-108 | Year end freeze | freeze | none | 2026-12-21 | 2026-12-28 | all | none | none | | | | | none | none | n/a | | game-liveops | planned |

## Store event metadata

| ID | Event name | Short description | Long description | Purpose | Priority |
|----|------------|-------------------|------------------|---------|----------|
| LO-101 | Autumn Season | A new season with your group | Three weeks of daily rounds, a fresh group table and autumn themes for everyone. | active users | high |
| LO-102 | Harvest Words Week | Autumn words in every daily round | Seven days of harvest themed daily rounds. Play with your group and share your grid. | lapsed users | normal |
| LO-107 | Meet Tile Rush | A new mini game joins the daily set | Tile Rush joins the daily rounds for everyone. Two tries a day, the best counts. | all users | normal |

## Reads

| ID | Read date | Participation | Completion | Uplift vs holdout | Decision | Output file |
|----|-----------|---------------|------------|-------------------|----------|-------------|
