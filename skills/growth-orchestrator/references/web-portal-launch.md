# Web Portal Launch (portals as distribution and as a test market)

> Knowledge as of 2026-10 (research pass 2026-10-15). Every platform fact below comes from search summaries of the platforms' own developer pages, which could not be opened from this environment, so all are labeled [Reported, 2026-10] or weaker. Re-open the official page (sources at the end) before any submission or deal. Submitting a game, accepting terms and signing a deal are G3 or G4 human actions; this module plans and drafts.

AI made building a small game cheap. Players did not become cheaper: distribution is the business. Web portals already have millions of players looking for a new game, and they judge games on engagement, not on ad spend. For a small studio that makes them two things at once: a distribution channel for games that fit them, and a near free test market for a mechanic before any store build or paid soft launch.

## 1. When the portal route fits

| Fits | Does not fit |
|------|--------------|
| Short session, single player games: puzzle, casual, arcade, merge, physics, high score, light 3D racing or shooting | A daily social or group game whose home is its own URL, streaks and group graph: exclusivity and ads only conflict with it |
| A mechanic you want to test with real players before a store build | A game that needs accounts, purchases or your own analytics from day one |
| A studio that accepts ads as the only revenue on the portal | Multiplayer that needs your own servers and matchmaking (possible on some portals, rare) |
| Games you can strip of outside links, own ads and purchases | A brand or IP you cannot license to a portal |

A board game platform (rated play between people, bots for solo play) fits mainly through a single player mode against bots, as its own build. The platform itself stays on its own URL.

## 2. The portal first path

| Step | What happens | Gate to move on | Owner |
|------|--------------|-----------------|-------|
| 0. Scout | Read store charts and portal top lists; fill the idea sheet (section 3) | One idea with a clear core mechanic and our twist | market-intel, growth-orchestrator |
| 1. Prototype | One rule, playable in days; first session watched by 10 to 20 people (lifecycle 3.0) | Players ask for another go | the game repo |
| 2. Portal build | Portal SDK, size and load budget, mobile and desktop, ads at natural breaks only (section 4) | The submission checklist passes | site-engineer, game-monetization |
| 3. Portal test | CrazyGames Basic Launch or Poki's player fit test (section 5) | The portal's own benchmarks; our read of playtime, conversion to play and day 1 return | measurement |
| 4. Iterate | One change at a time, from the portal's feedback and our level funnel (`level_flags.py`) | The next test beats the last | game-liveops, measurement |
| 5. Decide | Keep on portals, move to stores, or kill (lifecycle section 4) | A written decision row in `DECISIONS.md` | growth-orchestrator, the human |
| 6. Store move | A winning mechanic gets a mobile build and the normal soft launch (lifecycle 3.1) | Store gates in `METRICS.md` | mobile-app-growth, store-submission |

Read the portal test as a signal about the mechanic, not as a forecast for the stores: portal players arrive browsing for a game, store players arrive from ads. Never move a game to the stores on portal plays alone; move it on playtime and return.

Exclusivity decides the order. A web exclusive deal (Poki) can block your own site and other web channels for years, so decide the game's home before signing (section 6).

## 3. Idea scouting sheet

Keep one row per candidate in `ads-master/data/game_ideas.csv` (or the game studio's own sheet):

| Field | What to write |
|-------|---------------|
| Reference games | Two or three games with many ratings or plays, where seen (store chart, portal list), date |
| Core mechanic | One sentence: what the player does every few seconds |
| Why it satisfies | The feeling (sorting, merging, clearing, near miss, combo) |
| Time to understand | Seconds until a new player gets it without text |
| What keeps them playing | Levels, high score, collection, daily reason |
| Our twist | Theme, added or removed mechanic, feel; never assets, names or look from the reference |
| Portal fit | Which portals and why |
| Store potential | Could it carry a level game economy later |
| Risk | Too close to a known game, IP, technical size |
| Verdict | Prototype, park, drop |

Taking a mechanic is normal; copying assets, names, characters or visual identity is not, and portals decline clones and games resembling known IP [Reported, 2026-10].

## 4. Submission and QA checklist (all portals)

| Area | Check | Why |
|------|-------|-----|
| Size | Initial download small: CrazyGames up to 50 MB and 20 MB for mobile homepage eligibility; Poki target under 8 MB (another page says 5 MB) [Contested]; YouTube Playables under 30 MiB until gameReady, ideally under 15 MiB | Portals measure until the first gameplay event; big games lose players while loading |
| Load | First play well under 10 seconds on a mid phone; Playables asks for interactive in under 5 seconds | Players leave during loading |
| Frame rate | 30 FPS minimum, 60 target on mainstream devices (Poki) | Feel and retention |
| Devices | Desktop Chrome and Edge; mobile web in the orientations you support; touch forced on tablets; Safari tested (CrazyGames disables games that break there) | Portals test both |
| Layout | Legible in a 16:9 iframe and small sizes (800x450 listed by CrazyGames); Playables must not lock orientation | Embeds vary |
| Self contained | All assets, fonts and libraries in the bundle; no external requests (Poki blocks them; Playables allows none) | Blocked calls break the game |
| Storage | Wrap `localStorage` in try and catch; Playables saves through its own SDK, under 3 MiB | Incognito and embeds |
| Links | Remove outside links, splash screens, cross promotion and app store links unless the portal's rules allow a specific case | Common rejection cause |
| Ads | Only the portal's SDK ads; midgame ads only at natural breaks; rewarded opt in with the reward on the finished callback; playable with an ad blocker | Portal ad rules; our monetization contract |
| Purchases | None unless the portal invites them (CrazyGames via its own account, invited games only; Poki none; Playables none) | Portal rules |
| SDK events | Loading finished, gameplay start on first input, gameplay stop on pause, death or level end; no repeated start or stop | Portals measure and serve ads from these events |
| Content | Rating fits the portal (CrazyGames Basic Launch asks PEGI 12 compliance; Coolmath: no violence or foul language) | Admission |
| Analytics | Our own minimal events allowed by the portal, plus the portal's dashboard; level funnel for `level_flags.py` | Iteration needs data |
| Assets | Thumbnails and covers in each portal's sizes; a short gameplay clip from the real game | Click through on category pages decides traffic |

`site-engineer` owns the build and the QA pass, `game-monetization` the ad placement rules, `compliance` the content and any claim in the listing.

## 5. Portal by portal

| Portal | Access | Test stage | Ads and purchases | Money and exclusivity | Label |
|--------|--------|------------|-------------------|------------------------|-------|
| CrazyGames | Open upload in the Developer Portal with a QA tool | Basic Launch: limited audience, monetization off, ends after at least 7 days and 500 plays (or after 21 days); judged on playtime, conversion to gameplay and retention against other games; then Full Launch with full SDK and QA | Only SDK ads: midgame at most every 3 minutes, rewarded, up to 2 banners per screen; purchases for invited games only | Split not published; payouts monthly via Tipalti (EUR 10 and EUR 100 thresholds both appear) [Contested]; other platforms such as mobile and Steam do not affect eligibility; an older T&C paid more for 2 months of browser exclusivity | [Reported, 2026-10] |
| Poki | Closed beta, submission form, replies only to good fits | Playtest recordings; player fit test with about 500 players (healthy: 3+ minutes average playtime, 25%+ of plays over 3 minutes); web fit test with about 10,000 players on category pages; final review 1 to 2 weeks; 2 to 3 months to global release | Only Poki ads; no purchases | 100% of earnings from players you bring, 50% from Poki's; web exclusive by default, and Discord and YouTube Playables count as web; term 5 or 7 years [Contested]; a non-exclusive flat licence fee exists; figures indicative until signed | [Reported, 2026-10] |
| YouTube Playables | Private preview, by invitation, interest form; certification before launch, release through a Partner Manager | Certification against MUST requirements | YouTube provided ads (pre-roll, interstitial, rewarded) only; no outside ads or purchases; revenue share piloted with a few creators; wording on ads conflicts between pages [Contested] | Exclusivity not addressed; Poki's terms treat it as web | [Reported, 2026-10] |
| GameDistribution | Dashboard checklist, then activation request; review up to 1 to 3 weeks [Contested] | Review then activation | Mandatory SDK with pre-roll and mid-roll; no own ads, purchases or tracking | 33% of net revenue in the 2025 developer agreement; payout within 60 days above EUR 100; non-exclusive licence; the build must match the latest version published elsewhere | [Reported, 2026-10]; older terms [Contested] |
| Coolmath Games | Submission form | Review | No ads of any kind, no outside links, no stats reporting to the developer | Buys a non-exclusive licence; fee negotiated; needs a "thinking" element | [Reported, 2026-10] |

What the portals judge, in their own words as summarized: is it fun, does it fit the audience, is it different, do people play long enough, does it work on desktop and mobile, do ads fit naturally [Reported, 2026-10, practitioner account consistent with the portals' test stages].

## 6. Exclusivity and the game's home

Decide where each game lives before any submission:

| Game type | Home | Portal stance |
|-----------|------|---------------|
| Daily social or group game | Own URL and PWA | No exclusive portal deal; non-exclusive channels only, if any |
| Single player portal game | Portals | Choose between one exclusive deal (Poki) and several non-exclusive portals (CrazyGames, GameDistribution); the choice is a decision row |
| Single player mode of a platform game | Platform URL, mode on portals as its own build | Non-exclusive only; the build links nowhere (portal rules), so its value is reach and testing, not funnel |
| Mechanic test | Whichever portal gives the fastest real player read (CrazyGames Basic Launch is open) | No exclusivity for a test |

Every deal goes through the review in [Game studio lifecycle](game-studio-lifecycle.md) section 5.3; Poki's exclusivity covering Discord and YouTube Playables is exactly the clause that review flags.

## 7. Relationship log

Portals see far more player data than a single studio. After a few shipped games, ask before building. Keep `ads-master/data/portal_contacts.csv`:

| Field | Content |
|-------|---------|
| Portal and contact | Team or person, channel (developer portal, email) |
| Games shipped with them | Name, date, result |
| What they asked for | Genres, mechanics, themes they say are working, with the date |
| Feedback on our builds | Requested changes and what we did |
| Next ask | The idea we want early feedback on |

Contact only through the portal's developer channels or public professional profiles; no scraping, no bulk messages (compliance PRIV-B2B-01 applies to any person's data).

## 8. After launch

1. Read the portal dashboard daily for the first week, then weekly: players, playtime, conversion to gameplay, retention, revenue.
2. Our own level funnel shows where players quit; a spike becomes one change and one new read (`game-liveops` `level_flags.py`).
3. Seasonal skins and small content drops can give an older game another push; they follow `game-liveops` event rules.
4. Each game's lessons go into the idea sheet's verdict column, so the next scout starts smarter.
5. Kill rules from the lifecycle (section 4) apply to portal games too: written before the data.

## 9. Myths

| Claim | Reality |
|-------|---------|
| "Build with AI and earn passively" | Practitioners report most early prototypes earn almost nothing; results came after dozens of games and distribution work [Reported, 2026-10] |
| "1 million plays means a hit" | Plays count tries; daily active players and playtime decide revenue and portal promotion |
| "Put ads everywhere at the end" | Portals cap and control ads; engagement drives both revenue and promotion, so monetization is designed in |
| "A clone with new art is fine" | Portals decline clones and look alikes; take the mechanic, never the identity |
| "Exclusive deals are free money" | They can lock the open web, including Discord and YouTube Playables, for years |

## Sources for this module

| Source | Date read | Supports | Label |
|--------|-----------|----------|-------|
| CrazyGames developer docs: requirements (intro, technical, ads, gameplay), basic launch metrics, payouts, SDK pages, FAQ (docs.crazygames.com) | 2026-10-15 via search summaries | Section 4 and 5 CrazyGames rows | [Reported, 2026-10] |
| CrazyGames developer terms PDFs 2021 and 2023 (files.crazygames.com) | 2026-10-15 via search summary | Browser exclusivity bonus | [Reported, 2026-10] |
| Poki for Developers guide: working with Poki, revenue deal types, quality requirements, SDK overview, testing, payouts, web engine; sdk.poki.com deals and bonus pages | 2026-10-15 via search summaries | Section 4 and 5 Poki rows, exclusivity scope | [Reported, 2026-10]; term [Contested] |
| YouTube Playables developer pages: overview, developer portal, certification requirements, monetization reference, FAQ (developers.google.com/youtube/gaming/playables) | 2026-10-15 via search summaries | Section 4 and 5 Playables rows | [Reported, 2026-10] |
| GameDistribution developer agreement (updated 2025-06-19), developer guidelines, partnership page, submission FAQ | 2026-10-15 via search summaries | GameDistribution row | [Reported, 2026-10]; older terms [Contested] |
| Coolmath Games submit a game page | 2026-10-15 via search summary | Coolmath row | [Reported, 2026-10] |
| A practitioner account of 120+ web game prototypes and portal distribution (public post, 2026-10) | 2026-10-15 | Sections 2, 7 and 9 framing | [Reported, 2026-10], one practitioner |
