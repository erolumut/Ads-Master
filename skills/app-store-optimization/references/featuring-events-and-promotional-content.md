# Featuring, In-App Events and Promotional Content

> Knowledge as of 2026-10. In-App Events rules are long standing [Official] and unchanged in 2026 per the 2026-10-12 pass. Featuring nomination fields and lead times come from Apple pages seen in search summaries [Reported, 2026-10]; the minimum lead time is [Contested] between two Apple pages. Google Play has no self nomination for featuring; promotional content is the lever.

Gate: a featuring nomination, an in-app event submission, a promotional content submission and a promotional text change are G3 (they commit the brand in public or to the platform). Drafts in `ads-master/outputs/` are G1; unsubmitted events in App Store Connect are G2.

## 1. Apple featuring nominations

| Item | Detail | Evidence |
|------|--------|----------|
| Who can submit | Account Holder, Admin, App Manager, Marketing roles | [Reported, 2026-10] |
| Nomination types | New Content, App Enhancements, App Launch | [Reported, 2026-10] |
| Fields | Name up to 60 characters, description up to 1,000, up to 10 related apps, up to 5 supporting URLs | [Reported, 2026-10] |
| Lead time | At least 2 weeks (Apple's getting featured page) vs at least 3 weeks (App Store Connect Help); up to 3 months ahead is ideal per Apple | [Contested]; plan for 3 weeks minimum |
| Practitioner lead time for launches and major updates | 6 to 8 weeks | [Practitioner consensus] |
| Games | Games can propose offers for the Apple Games app; event badges In-Game Offer, Now On Sale, Try Before You Buy (US first, summer 2026) | [Reported, 2026-10]; badges [Official, 2026-06] (moved) |

What editors look for is qualitative: craft and design quality, a clear story of what is new, accessibility, localization, use of new platform features, and complete Accessibility Nutrition Labels [Practitioner consensus]. A nomination does not guarantee featuring.

Nomination draft template:

```
# Featuring nomination: <app>, <type>, <target date>
Type: New Content | App Enhancements | App Launch
Name (60): <...>
Description (1,000): what is new, who it is for, why now, platform features used, accessibility and localization facts
Related apps (up to 10): <IDs>
Supporting URLs (up to 5): press kit, video, event page
Availability: storefronts, languages, release date, in-app event IDs
Assets ready: screenshots, previews, 2026 assets (Asset Library IDs)
Claims checked: compliance verdict reference
Submit by: <date> (at least 3 weeks before; 6 to 8 weeks for launches)
Approval: G3 line in the change request
```

## 2. Apple In-App Events

| Item | Detail | Evidence |
|------|--------|----------|
| Where they show | Product page, search results, Today, Games and Apps tabs, editorial, Apple Games app | [Official] |
| Capacity | Up to 10 approved events at a time; up to 5 published at once | [Official], verify current limits |
| Duration | Up to 31 days per event; promotion can start up to 14 days before the event | [Official], verify |
| Metadata | Event name 30 characters, short description 50, long description 120, event card media (16:9) and details page media (9:16), badge, deep link, purpose, audience priority | [Official], verify |
| Badges | Challenge, Competition, Live Event, Major Update, New Season, Premiere, Special Event; plus Apple Games app badges above | [Official] |
| Review | Can be submitted independently of an app version (since 2025-10-29) and bundled with IAPs, custom product pages and PPO tests | [Official] (moved) |
| Assets | Managed through the Asset Library; pre-approval possible | [Official, 2026-10] (moved) |
| Measurement | Event impressions, opens, downloads and redownloads in App Store Connect | [Official] |

Events can surface in search results for relevant queries [Official], so an event name with the job words of a high value term can earn extra search presence for its duration. Use the words users search with, never claims you cannot back.

Event setup choices:

| Setting | Options | How to choose |
|---------|---------|---------------|
| Purpose | Appropriate for all users, attract new users, keep active users informed, bring back lapsed users [Official], verify labels | Pick the audience the event is truly for; it shapes who sees it |
| Priority | Normal or high [Official], verify | High only for the one event per period that matters most |
| Badge | Section table above | The badge that describes the event honestly; "Major Update" only for real major updates |
| Deep link | URL that opens the event content | Required in practice: an event that opens the home screen wastes the tap |
| Media | Card (16:9) and details page (9:16), image or video | Same promise as the event name; no text heavy art |

Event strategy:
1. A 12 month calendar: seasonal moments, content drops, challenges, major updates, sales (games and subscriptions where allowed).
2. Each event has a deep link into the event content and a measurement plan.
3. Events reach lapsed users: pair with `lifecycle-crm` messages and, for paid re-engagement, `mobile-app-growth`.
4. Big events get a featuring nomination (section 1) and a seasonal custom product page.
5. Read events by type after 3 or more of each: which badges and purposes bring downloads and redownloads.

Worked event read (illustrative, three events of different types in one quarter):

| Event | Impressions | Opens | Downloads | Redownloads | Opens / impressions | (Downloads + redownloads) / opens |
|-------|------------:|------:|----------:|------------:|--------------------:|----------------------------------:|
| Spring challenge | 120,000 | 3,600 | 540 | 410 | 3.0% | 26.4% |
| Feature launch | 80,000 | 1,600 | 300 | 90 | 2.0% | 24.4% |
| Annual sale | 150,000 | 6,000 | 450 | 1,350 | 4.0% | 30.0% |

Reading: the sale drew the most opens and mostly brought lapsed users back (redownloads three times downloads), so pair the next sale with `lifecycle-crm` win-back messages; of the two content events, the challenge brought more new downloads (540 vs 300) while the feature launch turned a larger share of opens into new downloads (18.8% vs 15.0%), so test a feature launch with a wider audience setting next. Repeat each type at least 3 times before calling a pattern, then write it to memory.

## 3. Apple promotional text

- 170 characters at the top of the description, editable without a new version, not a search field [Official].
- Use it for the current event, offer or news. Keep the offer identical to the paywall and in-app event; price reduction claims follow the reference price rules (EU 30 days, Türkiye 10 days) via `compliance`.
- Update is G3 (public). Schedule changes in the event calendar so the text never shows an expired offer.

## 4. Google Play: featuring and promotional content

| Item | Detail | Evidence |
|------|--------|----------|
| Featuring | No self nomination | [Reported, 2026-10]; editorial picks favor high quality, well rated apps [Practitioner consensus] |
| Promotional content (formerly LiveOps) | Cards for events, offers and major updates across Play surfaces and on the listing | [Official] |
| Promotional content and featuring | Google's engagement page says promotional content increases the chance of featuring | [Unverified] (single page) |
| Promotional tagline | 80 characters | [Unverified] |
| Play Points | Promotions for Play Points members | [Unverified] current eligibility |
| Play Games Services achievements | Shown in search filters; 15 or more recommended | [Unverified] |
| Engage SDK | Collections and Entertainment Space surfaces; content on the listing for existing users | [Official, 2026-05] (moved) |

Eligibility, formats and lead times for promotional content change; read Play Console Help before each quarter's plan.

Play promotional content procedure:
1. Check eligibility and formats in Play Console Help for the quarter (they change).
2. Draft the card: event type, dates, title, description, image, deep link, audience; same offer as the iOS event and the in-app paywall.
3. `compliance` checks the offer and price claims; G3 approval to submit.
4. Read: card impressions, clicks, acquisitions and reactivations as Play Console reports them; compare with the iOS event of the same theme.

## 5. Featuring readiness checklist (both stores)

- [ ] Crash and ANR rates under thresholds; no open vitals or wake lock breach.
- [ ] Rating 4.0 or higher on core storefronts and no rising negative theme (`review_themes.py` exit 0).
- [ ] Localized metadata and screenshots for the storefronts in the nomination.
- [ ] Accessibility facts documented (Apple Accessibility Nutrition Labels where available).
- [ ] Current screenshots and previews show the new content; 2026 assets ready if used.
- [ ] Deep links tested for the new content.
- [ ] Press kit, video and support pages live (supporting URLs).
- [ ] Every claim approved by `compliance`.

## 6. Event calendar template

| Month | Event | Type and badge | Stores | Audience | Deep link | Assets due | Submit by | Nomination | Promo text or tagline | KPI |
|-------|-------|----------------|--------|----------|-----------|-----------|-----------|------------|-----------------------|-----|
| 2026-11 | Black Friday plan sale | Special Event; Now On Sale for games | iOS event, Play promotional content | All, lapsed priority | app://offers/bf | 2026-10-20 | 2026-10-27 | 2026-10-01 | "Annual plan sale, ends <date>" (compliance checked) | Event downloads and redownloads, paid conversions |
| 2027-01 | New year challenge | Challenge | iOS, Play | Lapsed users | app://challenge/ny | 2026-12-08 | 2026-12-15 | 2026-11-20 | "Start the 30 day challenge" | Opens, redownloads, D7 retention |

## 7. Featuring hits (KPI)

Definition: featuring placements per quarter, each confirmed by an ASO tool featuring tracker or by a browse traffic spike in App Store Connect or explore traffic in Play Console that matches the placement dates.

Log every hit in the journal with dates, storefronts, placement and the browse lift (views and downloads vs the prior 4 weeks), and add an `event` row to the metadata change log so rank reads in that window are discounted.

## 8. Mistakes to prevent

1. Nominating 1 week before launch.
2. An event that says "sale" while the paywall shows the regular price.
3. Events without deep links that drop users on the home screen.
4. Promotional text left on an expired offer.
5. Reading a rank change during a featuring week as the effect of metadata.
6. Treating Play promotional content as guaranteed featuring.
