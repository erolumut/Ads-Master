# Liveops Calendar and Store Events

> Knowledge as of 2026-10. Apple In-App Events rules, Game Center and the Games app were read in full at developer.apple.com on 2026-10-12 [Official, 2026-10]; App Review Guideline 2.3.13 at the guidelines page last updated 2026-06-08 [Official, 2026-06]. Google Play promotional content rules were readable only as search summaries of Play Console Help (the help pages were not reachable from this environment) [Reported, 2026-10]; verify them in the live Play Console before each quarter's plan. Play Games Services facts were read at developer.android.com [Official, 2026-10].

Gate: the calendar, event metadata drafts and store submissions drafts are G1. Creating an unsubmitted in-app event in App Store Connect or a Play promotional content draft is G2. Submitting either for review, publishing, changing a live event and sending a featuring nomination are G3. `app-store-optimization` writes store copy and nominations; `store-submission` reviews event metadata against store rules; `compliance` gives the verdict on every customer facing word.

## 1. One calendar for every live moment

Every live moment of a product lives in one file, `ads-master/LIVEOPS_CALENDAR.md`, so the people who build, sell, message and submit all read the same dates.

| Row kind | Drafted by | Read by |
|----------|------------|---------|
| Seasons, events, challenges, tournaments, content drops | `game-liveops` | Game repo, every agent below |
| Store events (Apple in-app events, Play promotional content) | `game-liveops` (dates, deep link), `app-store-optimization` (copy) | `store-submission`, `compliance` |
| Offers and pass windows | `game-monetization` | `game-liveops`, `compliance` |
| Reminder moments | `game-liveops` requests | `lifecycle-crm` (consent, caps, sends) |
| Community moments (Discord, Reddit, socials) | `game-liveops` | `creative-strategy`, `lifecycle-crm` |
| Holidays per market and freeze windows | `game-liveops` | Everyone |

Rules:
1. A moment that is not in the calendar does not go live.
2. The human approves the calendar each month; each row's go live is a G3 line in a change request.
3. `liveops_calendar_check.py` runs on every edit (section 8).
4. Dates are in the product's day id zone (the tick rule in [Daily loops and streaks](daily-loops-and-streaks.md) section 2.2), written in the file header.

## 2. Apple In-App Events

### 2.1 Rules (read at the source)

| Rule | Detail | Label |
|------|--------|-------|
| Approved at once | Up to 15 approved events in App Store Connect at a time | [Official, 2026-10] |
| Published at once | Up to 10 events published on the App Store at a time | [Official, 2026-10] |
| Duration | Up to 31 days per event | [Official, 2026-10] |
| Promotion | Promoted up to 14 days before the start date | [Official, 2026-10] |
| Event name | Up to 30 characters, title case, the actual name of the event (for example "June Leaderboard Climb"), not a call to action and not the event type | [Official, 2026-10] |
| Short description | Up to 50 characters, sentence case | [Official, 2026-10] |
| Long description | Up to 120 characters, sentence case | [Official, 2026-10] |
| Prices | Specific pricing in event metadata leads to rejection; prices vary by region and can change independently of the event | [Official, 2026-10] |
| Claims and words | Avoid unverifiable claims ("the best", "#1") and extra words such as "game event"; no all capitals, no repeated exclamation marks | [Official, 2026-10] |
| Media | Event card 16:9 (1920x1080 to 3840x2160), details page 9:16 (1080x1920 to 2160x3840), image or video at 30 or 60 fps; videos loop, so make the loop seamless; no borders or gradients (Apple applies its own); avoid text and logos in media | [Official, 2026-10] |
| Deep link | Universal link recommended, or a custom URL; no URL shorteners; test it; before the event starts, a landing page that reminds players when to return is acceptable; always a way back to the main app | [Official, 2026-10] |
| Review | Events can be submitted independently of a new app version | [Official, 2026-10] |
| Where events show | Product page, search results, editorial selections and personalized recommendations on the Today, Games and Apps tabs, and in the Apple Games app | [Official, 2026-10] |
| Notifications | Customers can opt in on the event card or details page to be notified when the event starts | [Official, 2026-10] |
| Roles | Account Holder, Admin, App Manager or Marketing | [Official, 2026-10] |
| Guideline 2.3.13 | The event must fit an App Store Connect event type; metadata must be accurate and about the event, not the app; events happen at the dates and times set, across storefronts; monetization follows Section 3; the deep link goes to the right place | [Official, 2026-06] |

Note for the main session: the `app-store-optimization` module on featuring and events still lists 10 approved and 5 published events; the official page read on 2026-10-12 says 15 approved and 10 published.

### 2.2 Good and poor candidates (Apple's own words, summarized)

| Good candidates | Poor candidates |
|-----------------|-----------------|
| Challenges, competitions, special content launches | Repetitive activities such as daily tasks or rewards |
| A limited time moment tied to new or permanent content | Price promotions that introduce no new content, features or goods |
| | General promotions that raise awareness of the app |

Consequence for daily games: the daily puzzle itself is not an in-app event. A season, a themed week with new content, a community challenge or a new mini game is.

### 2.3 Purpose and priority

| Setting | Options | Note | Label |
|---------|---------|------|-------|
| Purpose | Appropriate for all users; attract new users (never downloaded); keep active users informed (opened recently); bring back lapsed users (downloaded, not opened recently) | Not shown on the card; published events are discoverable by every customer whatever the purpose | [Official, 2026-10] |
| Priority | Normal or high | Events show chronologically by start time; high priority events appear ahead of normal ones | [Official, 2026-10] |

Use high priority for one event per period at most; two high priority events cancel each other out [Practitioner heuristic].

### 2.4 Badge mapping

| Liveops format | Apple badge (Apple's meaning) |
|----------------|-------------------------------|
| Challenge, milestone track with a goal before the end | Challenge (achieve a goal before the event ends) |
| Race, cohort leaderboard, tournament, league season | Competition (compete for the highest ranking or rewards) |
| Community goal, scheduled live tournament, theme week everyone plays at once | Live Event (real time, all users together, with new content, features or goods) |
| Content drop with significant new features or content | Major Update (beyond minor enhancements) |
| Season, league season with new content | New Season (new content or storylines building on established content) |
| New mini game, new game on a platform, new mode | Premiere (new content for the first time) |
| Holiday event spanning several activities | Special Event (limited time, not captured by another badge) |

### 2.5 Apple Games app and Game Center

| Feature | Liveops use | Label |
|---------|-------------|-------|
| In-app events in the Games app (Home tab, game page, library, search) | Every store event also reaches the Games app audience | [Official, 2026-10] |
| Challenges built on leaderboards (invite friends and contacts, real time scores, notifications until a winner, rematch; up to 16 players) | Daily challenge on a daily recurring board (Apple's own example: a daily mini crossword with a recurring leaderboard that restarts daily and a non repeatable challenge); weekly challenge for level games | [Official, 2026-10] |
| Score submission consumes a challenge attempt | Submit at the end of an attempt, after a revive is accepted or declined; never during play | [Official, 2026-10] |
| Activities with deep links and party codes, minimum version prompt | Entry points for events and challenges; invites that open a web page when the API is unavailable | [Official, 2026-10] |
| Friend notifications when a friend passes a score | Re-engagement without a push from us, even for players who uninstalled | [Official, 2026-10] |
| Games app pre-installed on iOS 26, iPadOS 26, macOS 26; games with Game Center and in-app events displayed more prominently | Reason to adopt Game Center before the first store event | [Official, 2026-10] |

Counted attempts for ranked play stay the product's own rule. A Game Center challenge on top of a ranked daily board uses the same scores; it never adds counted attempts.

## 3. Google Play promotional content

All rows below come from search summaries of Play Console Help pages and the Play Console program page [Reported, 2026-10], except where marked otherwise. Read the live console before relying on any of them.

| Rule | Detail | Label |
|------|--------|-------|
| Types | Offers (discounts, bonuses, rewards), time limited events, major updates (new features or content, pre-registration announcements) | [Reported, 2026-10] |
| Eligibility | Available to all games per the newer help page; apps need the premium growth tools criteria | [Reported, 2026-10] |
| Earliest submission | 60 days before the start date | [Reported, 2026-10] |
| Approval | Up to 4 days: submit at least 4 days before the start | [Reported, 2026-10] |
| Google Play Partner Program for Games | Participants asked to submit at least 14 days ahead for quality feedback | [Reported, 2026-10] |
| Preview | Events preview on Google Play up to 14 days ahead; offers cannot be previewed | [Reported, 2026-10] |
| Fixed durations | Major updates 28 days, pre-registration announcements 1 week, per one help page; a 2024 third party blog lists other durations | [Contested] |
| Audiences | Offers can be limited to new users; targeting of lapsed and churned users reported since March 2025 | [Reported, 2026-10] |
| Featuring | Content shows on the listing by default; content that meets quality guidelines may appear in more visible places; no limit on events per quarter | [Reported, 2026-10] |
| Effect claims | Google's program page claims more explore acquisitions for content users | [Unverified] (Google marketing claim) |
| Play Points | Open to all games since October 2025 | [Reported, 2026-10] |
| Play Games Services events | Analytics counters (currency sources and sinks), not live events | [Official, 2026-10] |
| Play Games Services leaderboards | Daily boards reset at UTC-7 all year; weekly at midnight between Saturday and Sunday (UTC-7) | [Official, 2026-10] |

Procedure: check eligibility and formats in the console for the quarter; draft the card (type, dates, title, description, image, deep link, audience) with the same offer as the iOS event and the in-game offer; `compliance` and `store-submission` review; G3 to submit; read impressions, clicks, acquisitions and reactivations as the console reports them.

## 4. Web and PWA first products

The web has no store calendar. The same calendar rows drive own surfaces instead:

| Surface | Use |
|---------|-----|
| The product's home and today screens | Event banner, season page, countdown free "ends <date> <time>" line |
| Share pages and share text | Season or event name in the share line |
| Web push (iOS only for Home Screen web apps, permission from a user gesture) and email | Reminder moments through `lifecycle-crm` [Official, 2026-10 for the Apple web push rules] |
| Discord Activities and Reddit (Devvit daily games) | Group play and community moments [Reported, 2026-10] |
| Search and AI answers | Season and event pages for `seo` and `ai-search-optimization` when the event is newsworthy |

When a store wrapper ships, the same rows gain store columns; nothing else changes.

## 5. Lead times (work backwards from the start)

| When | Action | Source |
|------|--------|--------|
| T minus 90 days | Holiday and season dates set for the quarter; content plan with the game repo | [Practitioner consensus] |
| T minus 60 days | Earliest Play promotional content submission | [Reported, 2026-10] |
| T minus 42 days | Art and media brief to `creative-strategy` and `video-studio` (16:9 and 9:16 assets) | [Practitioner heuristic] |
| T minus 21 days or more | Featuring nomination by `app-store-optimization` for big moments (Apple pages disagree on 2 vs 3 weeks; plan 3, and 6 to 8 weeks for launches) | [Contested] (see the ASO featuring module) |
| T minus 21 to 14 days | Apple in-app event submitted, so approval lands before the promotion start | [Practitioner heuristic] |
| T minus 14 days | Latest useful Apple promotion start (maximum promotion window); Play Partner Program submission | [Official, 2026-10]; [Reported, 2026-10] |
| T minus 7 days | Reminder moments confirmed with `lifecycle-crm`; holdout configured; kill switch tested | [Practitioner heuristic] |
| T minus 4 days | Latest Play promotional content submission | [Reported, 2026-10] |
| T | Start at the tick; live check within the first hour | |
| T plus 7 days after the end | Event read filed ([Events and seasons](events-and-seasons.md) section 8) | |

Apple's holiday period availability for App Store Connect submissions changes year to year [Unverified]; check Apple Developer News each November before planning late December submissions.

## 6. Holidays and moments by market

Fixed dates (verify local observance each year):

| Market | Moment | Date |
|--------|--------|------|
| Global | New Year | January 1 |
| Global | Valentine's Day | February 14 |
| Global | Halloween | October 31 |
| Global | Christmas | December 25 |
| United States | Independence Day; Thanksgiving; Black Friday | July 4; fourth Thursday of November; the day after |
| Netherlands | King's Day (Koningsdag); Sinterklaas evening | April 27 (April 26 when the 27th is a Sunday); December 5 |
| Turkey | National Sovereignty and Children's Day; Youth and Sports Day; Republic Day | April 23; May 19; October 29 |

Moving dates (look up every year; do not copy last year's date): Easter; Ramadan, Eid al-Fitr (Ramazan Bayramı) and Eid al-Adha (Kurban Bayramı), which move about 11 days earlier each year; Lunar New Year; Diwali; school holidays per country and region.

Rules:
- A moment aimed at children (for example April 23 in Turkey) makes the event child directed in practice: minors rules apply to its copy, offers and reminders ([Player trust](player-trust-and-pressure-patterns.md)).
- Religious holidays get respectful themes only; no offer pressure tied to them; `compliance` reviews.
- Holiday events usually carry the Special Event badge; a holiday that only discounts prices is a poor in-app event candidate.

## 7. Calendar governance

| Rhythm | Action |
|--------|--------|
| Every edit | Run `liveops_calendar_check.py`; fix every FAIL before saving the row as `planned` |
| Weekly loop | Review the next 6 weeks: deadlines due, assets, approvals, reads due; run the check with `--today` |
| Monthly | Human approves the next month; plan 3 months ahead; Freshness check on store rules |
| Quarterly | Holiday plan for the next two quarters; retire event types that read flat twice |

Freeze windows: add `freeze` rows for periods with no new live moments (a big binary release, a store holiday period, an incident). The checker warns when a row starts inside one.

## 8. liveops_calendar_check.py

`<skill>/scripts/liveops_calendar_check.py` reads `LIVEOPS_CALENDAR.md` (the template in section 9) or a CSV with the same columns, and checks:

| Check | Result |
|-------|--------|
| Required columns present; IDs unique; dates parse; end after start | Missing columns: exit 2; others FAIL |
| Apple rows: badge valid, deep link present, duration up to 31 days, promotion start no earlier than 14 days before the start and not after it, submission on or before the promotion start | FAIL |
| Apple published events above 10 on any day | FAIL |
| Apple approved events above 15 on any day (approximated from the submission date) | WARN |
| Apple metadata: name 30, short 50, long 120 characters; specific prices (currency symbols or codes with numbers, "% off") | FAIL |
| Apple metadata: "best", "#1", "game event", all capital words, repeated exclamation marks, purpose and priority values, more than one high priority event live at once | WARN |
| Apple rows for offers (price only promotions are poor candidates) | WARN |
| Play rows: submission later than 4 days before the start or earlier than 60 days before | WARN (rules [Reported]) |
| Two rows of the same scale overlapping | WARN (one event per scale) |
| Competitive formats without a declared ranked board | WARN (contract fairness) |
| Offer rows not owned by `game-monetization` | WARN |
| A measured format with no holdout anywhere in the calendar | WARN |
| Pressure words ("last chance", "hurry", "ends soon", "don't miss", "streak at risk") in names or metadata | WARN (route to `compliance`) |
| Rows starting inside a freeze window | WARN |
| With `--today`: submission date passed for an unsubmitted row | FAIL |

Exit codes: 0 no FAIL (warnings allowed), 1 at least one FAIL, 2 could not run.

```
python3 -I <skill>/scripts/liveops_calendar_check.py ads-master/LIVEOPS_CALENDAR.md --today 2026-10-15
```

The check cannot judge whether an event is a good idea, whether copy is truthful, whether assets meet Apple's visual guidance or whether Play's live console rules still match the reported ones.

## 9. LIVEOPS_CALENDAR template

Copy the block below to `ads-master/LIVEOPS_CALENDAR.md` (workspace template path: `skills/ads-setup/template/LIVEOPS_CALENDAR.md`). Keep the column names: the checker reads them. Values in angle brackets are placeholders; the two example rows show the format and should be replaced.

```markdown
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
```

## 10. Mistakes to prevent

1. Submitting the daily puzzle or a daily login reward as an in-app event (Apple calls them poor candidates).
2. A price or "50% off" in event metadata (rejection).
3. An event card promoted 20 days ahead (the maximum is 14).
4. An event that runs 35 days (the maximum is 31; split it or run two).
5. Eleven events published at once (the limit is 10).
6. A deep link that opens the home screen or breaks before the event starts.
7. A Play card submitted the day before the start.
8. Two short events on the same days fighting for the same session.
9. A store event whose dates differ from the in-game event (Guideline 2.3.13 says events happen at the dates set).
10. A holiday event for children with offer pressure in it.
