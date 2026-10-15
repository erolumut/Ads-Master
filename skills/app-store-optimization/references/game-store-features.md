# Game Store Features: Games App, Game Center, Play Games and Game Listings

> Knowledge as of 2026-10 (research pass 2026-10-12). Apple's Games app, Game Center, In-App Events, product page, getting featured and age rating pages were read at developer.apple.com, and Play Games Services, Play Games on PC and Play Points pages at developer.android.com [Official, 2026-10]. Play Console Help pages (promotional content, pricing, metadata) were readable only as search summaries [Reported, 2026-10]. PEGI, UK ASA and other regulator items come from law firm and press summaries [Reported, 2026-10]. Run the Freshness protocol in SKILL.md before acting.

## 0. Who owns what

| Work | Owner |
|------|-------|
| Listing text, store creative, CPPs and CSLs, featuring nominations, in-app event and promotional content copy, ratings and reviews; recommending Game Center and Play Games Services for discovery | `app-store-optimization` (this module) |
| The live ops calendar, event dates, deep links into event content | `game-liveops` ([LiveOps calendar and store events](../../game-liveops/references/liveops-calendar-and-store-events.md)) |
| Whether a build, its age rating answers and its metadata pass review; native value for wrappers (Guideline 4.2) | `store-submission` |
| What the stores are told about ads, purchases and loot boxes (`storeDeclarations` in the policy file) | `game-monetization` with `compliance` |
| Every customer facing word, loot box label wording, age rating interpretation | `compliance` ([Games and virtual currencies](../../compliance/references/games-and-virtual-currencies.md)) |
| Implementing GameKit, Play Games Services or the Input SDK | The game's own repo |

Gate: drafts are G1; unsubmitted events, listing edits and achievements configured but not published are G2; submitting, publishing, changing a live listing and sending a nomination are G3.

## 1. The Apple Games app

| Fact | Detail | Evidence |
|------|--------|----------|
| Availability | Pre-installed on iOS 26, iPadOS 26 and macOS 26 or later; "now available for all customers" | [Official, 2026-10] |
| Automatic presence | Every game on the App Store appears in Games app search, the Library tab and Continue Playing without any work | [Official, 2026-10] |
| Prominence | "Games that include Game Center features and In-App Events are prominently displayed across the Games app" | [Official, 2026-10] |
| Tabs | Home (recently played, top charts, in-app events, personalized recommendations, editorial selections, friend activity), Friends (what friends play, invites to challenges and multiplayer, compare scores and achievements), Arcade, Library, Search | [Official, 2026-10] |
| Game page | Uses the App Store product page metadata (description, screenshots, previews) plus in-app events and Game Center activity; players can tap to play and invite friends | [Official, 2026-10] |
| Top Played chart | Game Center initialization signs players in automatically, which lets the game appear in social recommendations on Home and Friends and in a Top Played chart shown in the Games app and on the App Store | [Official, 2026-10] |
| Re-engagement | Players are notified when a friend passes their score and can jump back in or redownload, even with the game no longer installed | [Official, 2026-10] |

Consequences:
1. The product page now has a second home: the game page in the Games app reuses its screenshots and previews, so gameplay first creative matters twice.
2. Game Center initialization is the price of entry to social recommendations and the Top Played chart. A game without it is listed but not recommended through friends.
3. In-app events show on the Games app Home tab, the game page, the player's library and search results [Official, 2026-10], so the event calendar is a discovery plan.

## 2. Game Center features

| Feature | What Apple says it does | Discovery effect | Evidence |
|---------|-------------------------|------------------|----------|
| Leaderboards | Submit scores through a simple API; Apple's UI; automatic notifications when a friend passes a score | Friend beat notifications re-engage lapsed players | [Official, 2026-10] |
| Challenges | Built from leaderboards: friends compete in score based competitions "to see who can win before time runs out" | Recommended in more places in the Games app | [Official, 2026-10]; duration options and player counts not stated on the pages read, check the GameKit documentation |
| Achievements | Collect and unlock; friends see them; achievement rarity shows how many players unlocked one | Progress visible in the Games app | [Official, 2026-10] |
| Multiplayer activities | Promote multiplayer experiences and invites across the Games app, "even across platforms"; configurable with Game Center infrastructure or your own multiplayer system | Recommended in more places | [Official, 2026-10] |
| Access point, identity | In game access to Game Center features; the player's nickname can be the default username, the avatar can appear in multiplayer | Faster onboarding | [Official, 2026-10] |
| Real time and turn based multiplayer, matchmaking rules, saved games | Invite friends, contacts, iMessage groups, nearby players; rules on skill or party codes; resume across devices | | [Official, 2026-10] |
| Widgets and App Store sections | Game Center Activity and Continue Playing widgets; Game Center and Friends Are Playing sections on the App Store | Discovery through friends outside the game | [Official, 2026-10] |
| Setup | Add the Game Center capability in Xcode, configure features in App Store Connect, implement with GameKit | | [Official, 2026-10] |
| Review | Game Center features can be submitted separately during review (2025-10) | | [Reported, 2026-10] |

Choose by archetype (recommendation for the game repo; ASO does not implement):

| Archetype | Start with | Then |
|-----------|-----------|------|
| Daily social game (one counted play a day, groups) | A recurring daily leaderboard fed only by counted results; friends visibility | Challenges built from that leaderboard; a streak achievement set |
| Level based puzzle | Achievements across the level track; a weekly event leaderboard | Challenges on event levels |
| Multiplayer or board game | Multiplayer activities with the game's own system and invites | Turn based notifications, achievements |

Fairness rule from the Game Monetization Contract (section 3): a Game Center leaderboard is a ranked board with scope `everyone` (Game Center shows it to all players and filtered to friends). Only results the policy lets write to such a board are submitted: never an encore round bought for a group, never a practice replay, never a score helped by a purchased booster in a ranked mode. Declare each Game Center leaderboard as a board (`{"id": ..., "scope": "everyone"}`) of its ranked mode in `monetization-policy.json` so the checker can see it.

Game Center is also native value for a web game wrapped for iOS, which matters for Guideline 4.2 ("elevate beyond a repackaged website") [Official, 2026-10]; `store-submission` owns that argument.

## 3. In-app events for games

Rules read at the source [Official, 2026-10]: up to 15 approved events in App Store Connect and up to 10 published per app at a time; each event lasts up to 31 days and can be promoted up to 14 days before its start; name up to 30 characters (title case), short description up to 50, long description up to 120 (sentence case); submitted for review independently of an app version; badges Challenge, Competition, Live Event, Major Update, New Season, Premiere, Special Event.

Note: [Featuring, events and promotional content](featuring-events-and-promotional-content.md) section 2 still lists 10 approved and 5 published; the official page read on 2026-10-12 says 15 and 10. Use 15 and 10 and re-check in App Store Connect.

What Apple calls good and poor candidates for games [Official, 2026-10]:

| Good | Poor |
|------|------|
| Challenges ("beating a certain number of levels"), competitions ("a tournament where players battle to win the most matches"), special content launches, new modes or levels (Major Update), a battle pass or themed season (New Season) | "Repetitive activities such as daily tasks or rewards" |

So the daily puzzle itself is never an in-app event; a season, a themed week of new content, a community challenge or a new mini game is. Dates, deep links and the shared calendar come from `game-liveops` ([LiveOps calendar and store events](../../game-liveops/references/liveops-calendar-and-store-events.md)); copy, media and purpose come from here, with the procedure in [Featuring, events and promotional content](featuring-events-and-promotional-content.md) section 2.

Event copy rules for games: the name carries the words players search with (events appear in search results [Official]); no prices in event metadata; no "free" unless the content is free; an event that sells a pass says what is free and what is paid on the event page; compliance approves every line.

## 4. In-app purchases on the product page

The product page can show in-app purchases in two sections, up to 20 items in total [Official, 2026-10]. For a game: the season pass, ad removal (state whether rewarded ads remain), a starter pack and a subscription if any. Names and images are store text and creative: real items, no countdown words, the same names as in the game and in the catalog (`sku` and the store product id in the policy file).

## 5. Google Play Games Services (v2)

| Fact | Detail | Evidence |
|------|--------|----------|
| What it is | A Gamer Profile with consistent player identification across phones, tablets and PCs; achievements and leaderboards; social graph and friends; events; Play Points; Play Games Sidekick overlay with Gemini tips; game stats on the profile | [Official, 2026-10] (page updated 2026-10-06) |
| What it is not | "Not ... a primary system for inventory management or game-state preservation"; use your own in game identity (Sign in with Google, a custom backend) for progress | [Official, 2026-10] |
| Level Up program | Leagues, quests, achievements and streaks mechanics are restricted to titles enrolled in Level Up; integrated titles gain "increased discoverability and visibility across multiple Play Games surfaces" | [Official, 2026-10]; the uplift claim on the page has no data [Unverified, platform claim] |
| Achievements baseline (Level Up guidelines) | At least 10 achievements across the game's life | [Official, 2026-10] |
| Achievements recommended | 40 or more, including surprise ones, milestones and progress | [Official, 2026-10] |
| Quests eligibility | At least 4 achievements reliably reachable within an hour of play by everyone | [Official, 2026-10] |
| Limits | Up to 400 achievements; 2,000 points in total, multiples of 5, at most 200 per achievement; incremental achievements need at least 10 sessions; name up to 100 characters, description up to 500 | [Official, 2026-10] |
| Discovery | "High-quality achievements ... increase discovery across Google Play" | [Official, 2026-10] |

Recommendation: integrate PGS v2 sign in and the baseline achievement set before soft launch on Android; keep a point reserve for future content (Google advises it [Official, 2026-10]); design the first four achievements so quests eligibility is met. Achievements describe play; they never reward a purchase.

## 6. Google Play Games on PC

| Level | Requirement | Evidence |
|-------|-------------|----------|
| Release (playability) | Playable with mouse and keyboard (compatibility mode is enough); gameplay not blocked by unsupported permissions, Google APIs or features; OpenGL ES 3.2 or below or Vulkan 1.1 or below | [Official, 2026-10] (page updated 2026-07-14) |
| Certification | Mouse and keyboard support, the Input SDK; stable 30 FPS on a lower tier PC and 60 FPS on a higher end PC; no crash over 20 minutes or more of continuous play; cross device progress sync including PC, Android and iOS | [Official, 2026-10] |
| Architecture | ARM or x86-64; ship x86-64 when possible; ARM games are certified if they meet performance and stability | [Official, 2026-10] |

For casual, puzzle and board games the playability level is often within reach; certification needs real engineering. ASO's part: once released on PC, add PC screenshots if the console offers a PC listing slot (verify in Play Console) and mention PC play only after it is live.

## 7. Play Points

"Participation in Play Points is available to select developers" through an interest form; members exchange points for discounted coupons and in-app products offered as promotions; setup covers in-app and one-time products [Official, 2026-10] (page updated 2026-10-06). A 2026-10-12 search summary said Play Points opened to all games in October 2025 [Reported, 2026-10]; the developer page read the same day says select developers [Contested]. Google's program page cites revenue uplift as high as 30% for participants [Unverified, platform claim]. Apply through the form (G3, it commits the brand) and plan Play Points promotions in the live ops calendar like any other offer.

## 8. Google Play promotional content (formerly LiveOps)

| Fact | Detail | Evidence |
|------|--------|----------|
| Content types | Offers (discounts, bonuses, rewards), time limited events (competitions, challenges, live events), major updates (new features, new content, pre-registration updates) | [Reported, 2026-10] (Play Console program page summary) |
| Eligibility | Apps that meet eligibility criteria for premium growth tools | [Reported, 2026-10] |
| Featuring | A submission can request further featuring across Google Play; Google's page claims more than twice as many explore acquisitions during a featuring window | [Reported, 2026-10]; the uplift is [Unverified, platform claim] |
| Audiences | Lapsed and churned player targeting reported since March 2025 | [Reported, 2026-10] |
| Lead times | Submission window reported as 4 to 60 days before the start | [Reported, 2026-10]; see the live ops calendar module |

Same offer, same dates and same promise as the iOS in-app event and the in-game screen. Copy procedure in [Featuring, events and promotional content](featuring-events-and-promotional-content.md) section 4.

## 9. Featuring criteria for games

Apple [Official, 2026-10]:
- Lead time: "a minimum of two weeks notice"; "up to three months in advance" for wider consideration. App Store Connect Help was summarized as 3 weeks ([Featuring, events and promotional content](featuring-events-and-promotional-content.md) section 1); plan 3 weeks minimum, 6 to 8 for a launch.
- "There's no checklist of requirements for getting featured." Additional considerations for games: gameplay design, art and animation, controls, story and characters (if applicable), replayability (if applicable), sound design and music, technical performance, overall value.
- General factors include accessibility ("well integrated features") and localization ("culturally relevant and appropriate content"); selections are localized and regionally curated, and Editors' Choice is curated per storefront.

Google Play: no self nomination; the levers are promotional content with a featuring request, Play Games Services and Level Up, vitals and rating quality [Reported, 2026-10].

Nomination draft for a game adds to the template in [Featuring, events and promotional content](featuring-events-and-promotional-content.md) section 1: the gameplay loop in one sentence, what is new for returning players, Game Center features used, accessibility features, languages, and the in-app event ids in the window.

## 10. Previews and screenshots for games

| Rule | Detail | Evidence |
|------|--------|----------|
| Apple previews | Up to 3 per product page, up to 30 seconds each, footage captured on the device, autoplay muted, poster frame when they do not autoplay; localizable | [Official, 2026-10] |
| Apple screenshots | Up to 10; images captured from the app's UI | [Official, 2026-10] |
| Guideline 2.3.3 | More than half of the screenshots per device show the app in use | [Official, 2026-10] |
| Guideline 2.3.4 | Previews may use only screen captures of the app | [Official, 2026-10] |
| Guideline 2.3.8 | Metadata (icons, screenshots, previews) fit a 4+ audience even when the app is rated higher | [Official, 2026-10] |
| Guideline 2.3.10 and 2.3.7 | No other platform names or imagery; no competitor names or pricing terms in the name or keywords | [Official, 2026-10] (2.3.10 wording seen as a summary) |
| Promotional text | 170 characters, editable without a release, not a ranking field | [Official, 2026-10] |
| 2026 header and search result assets | New asset types and Asset Library from 2026-10-05 | [Official, 2026-10]; specs in [Store creative and conversion](store-creative-and-conversion.md) |
| Play title and short description | 30 and 80 characters; no emoji, "#1", "best" or "free" in the title | [Reported, 2026-10] |

Game specific rules (ours, from the ad rulings and the guidelines):
1. Gameplay first: frame 1 shows the core loop a new player meets in the first session, captured from a real build. The representativeness test in [Game ad creative](../../creative-strategy/references/game-ad-creative.md) section 1 applies to store creative too; the UK rulings against unrepresentative game ads are the reason [Reported, 2026-10].
2. Preview opens on play in the first 2 seconds (autoplay is muted, so sound is a bonus, not the hook).
3. No fake fails, no unreachable levels, no characters or modes the game does not have.
4. Show the social layer when it is the product (a group board, a share grid) with sample names, never real players' names.
5. A "No ads" claim appears only when no ads run, including rewarded; if ad removal keeps rewarded ads, say so.
6. Ratings, awards and "number one" claims only from `brand/CLAIMS.md`.
7. One capture session produces every size and language when the game has a capture mode (`video-studio`).

## 11. Age ratings

Apple (read at the source, values for iOS 26 and later) [Official, 2026-10]:

| Item | Rating effect |
|------|---------------|
| Tiers | 4+, 9+, 13+, 16+, 18+ (Unrated cannot be published on the App Store) |
| Loot boxes ("virtual containers that provide players with randomized virtual items for purchase") | 9+ globally |
| Simulated gambling | 13+ infrequent, 18+ frequent; real money gambling 18+ |
| User generated content, messaging and chat, advertising | Allowed at 4+ |
| Social media (redistribution or amplification of user content through a feed) | 13+; "social media disabled for users under 13" requires at least a Declared Age Range API check |
| Australia | 16+ for social media or loot boxes; R 18+ for infrequent simulated gambling |
| Brazil | Loot boxes A18; social media A16 |
| Korea | Frequent or intense simulated gambling needs a Rating Classification Number |
| Questionnaire | The social media capability question is required from 2026-09 [Official, 2026-10, research pass] |

Google Play: the IARC questionnaire in Play Console produces regional ratings, including PEGI in Europe [Reported, 2026-10]. Answers must match the policy file's `storeDeclarations` and the per store declarations file at `ads-master/data/store-declarations/<store>.json`, which holds the age rating answers (`monetization_conformance.py` checks both).

PEGI 2026 [Reported, 2026-10]: from June 2026 newly rated games with paid random items default to PEGI 16, some PEGI 18; time limited or quantity limited offers rate at least PEGI 12; reward for return mechanics such as daily quests at least PEGI 7; NFT or blockchain mechanics PEGI 18. Whether existing games are reclassified from 2026-10-01 or keep their current rating is [Contested] between sources (the compliance pack row GAME-EU-08 carries the same label). Check the PEGI criteria before answering.

Turkey Law 7578 adds age rating and parental controls duties for game platforms, including purchase approval [Reported, 2026-10]; route to `compliance`.

ASO consequences: a daily streak or a timed offer can move a European rating up; the rating shows on the listing and filters some players. `store-submission` fills the forms; this module keeps the listing text consistent with the rating.

## 12. Loot box labels and odds

| Rule | Detail | Evidence |
|------|--------|----------|
| Apple 3.1.1 | Apps offering loot boxes or other random paid items disclose the odds of each item type before purchase | [Official, 2026-10] |
| Google Play | Odds disclosed before purchase, close to the purchase | [Reported, 2026-10] |
| UK CAP enforcement notice (2026-02-26) | Store listings for games with loot boxes disclose them prominently, for example "Contains loot boxes" or "Includes random-item purchases"; a generic "offers in-app purchases" is not enough; monitoring from 2026-05-26 | [Reported, 2026-10] |
| Brazil | Paid loot boxes banned for minors from 2026-03 | [Reported, 2026-10] |
| Belgium | Paid loot boxes treated as gambling since 2018 | [Reported, 2026-10] |

Placement in the listing (UK storefront, and everywhere for simplicity): the label sits in the first lines of the description and in the promotional text when an event sells random items; the words come from `compliance`; the policy file's `storeDeclarations.lootBoxes` is true. The Game Monetization Contract prefers fixed price items without randomness; a game without random paid items needs no label and says nothing about loot boxes.

## 13. Game listing checklist

- [ ] Game Center initialized; at least one leaderboard and an achievement set; challenges or activities where they fit (section 2).
- [ ] Play Games Services v2 sign in; baseline 10 achievements, 4 reachable in the first hour (section 5).
- [ ] Gameplay first frame 1 and preview, passing the representativeness test (section 10).
- [ ] Metadata safe for 4+; no other platform names; no competitor names in keywords.
- [ ] A CPP per paid ad theme with the same gameplay, deep link where useful.
- [ ] In-app events and Play promotional content on the shared live ops calendar; no daily tasks as events (section 3).
- [ ] Promoted in-app purchases named as in the catalog (section 4).
- [ ] Age rating answers current on both stores, consistent with the policy file (section 11).
- [ ] Loot box odds before purchase and the UK label, or no random paid items (section 12).
- [ ] Featuring nomination 3 weeks to 3 months ahead with the game criteria answered (section 9).
- [ ] Web shop link only after the region policy review (`mobile-app-growth`, `compliance`).
- [ ] Every line approved by `compliance`; every submission a G3 change request.

## 14. Sources

| # | Source | Publisher | Date | Supports |
|---|--------|-----------|------|----------|
| 1 | Games app | Apple Developer, developer.apple.com/games-app | read 2026-10-12 | Section 1, Game Center recommendations, Top Played [Official, 2026-10] |
| 2 | Game Center | Apple Developer, developer.apple.com/game-center | read 2026-10-12 | Section 2 [Official, 2026-10] |
| 3 | Games | Apple Developer, developer.apple.com/games | read 2026-10-12 | Automatic Games app presence [Official, 2026-10] |
| 4 | In-App Events | Apple Developer, developer.apple.com/app-store/in-app-events | read 2026-10-12 | Section 3 limits, badges, candidates [Official, 2026-10] |
| 5 | Product page | Apple Developer, developer.apple.com/app-store/product-page | read 2026-10-12 | Previews, screenshots, promotional text, in-app purchases on the page [Official, 2026-10] |
| 6 | Getting featured | Apple Developer, developer.apple.com/app-store/getting-featured | read 2026-10-12 | Lead time, game criteria [Official, 2026-10] |
| 7 | Age ratings values and definitions | App Store Connect Help | read 2026-10-12 | Section 11 [Official, 2026-10] |
| 8 | App Review Guidelines (2026-06-08) | Apple Developer | read in the research pass | 2.3.3, 2.3.4, 2.3.7, 2.3.8, 3.1.1, 4.2 [Official, 2026-10] |
| 9 | Play Games Services overview; achievements | Android Developers, developer.android.com/games/pgs | read 2026-10-12 (updated 2026-10-06) | Section 5 [Official, 2026-10] |
| 10 | Get started with Google Play Games on PC | Android Developers, developer.android.com/games/playgames/start | read 2026-10-12 (updated 2026-07-14) | Section 6 [Official, 2026-10] |
| 11 | Play Points overview | Android Developers, developer.android.com/guide/playpoints | read 2026-10-12 (updated 2026-10-06) | Section 7 [Official, 2026-10] |
| 12 | Google Play Points program page; promotional content program page | Play Console (play.google.com/console/about/programs) | seen as search summaries 2026-10-12 | Uplift claims, content types, featuring request [Reported, 2026-10] |
| 13 | PEGI 2026 criteria coverage | RPC, Reed Smith, Lewis Silkin (2026-03-18), Pocketgamer.biz, VGC | 2026 | PEGI 16 for paid random items and other criteria [Reported, 2026-10]; reclassification [Contested] |
| 14 | CAP enforcement notice on loot boxes in app store listings | ASA and CAP via Lewis Silkin (2026-02-27) | 2026-02-26 | UK label [Reported, 2026-10] |
| 15 | Games and virtual currencies rule pack | Ads Master `compliance` | 2026-10 | Jurisdiction rows (BR, BE, UK, PEGI) |
