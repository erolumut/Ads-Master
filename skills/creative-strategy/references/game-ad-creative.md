# Game Ad Creative

> Knowledge as of 2026-10 (research pass 2026-10-12). Most game creative facts below were readable only as search results or vendor posts, so they carry [Reported, 2026-10] or [Unverified]; regulator rulings were confirmed through two or more secondary reports, not on the regulator's own page. Run the Freshness protocol in SKILL.md and the `ads-verify` skill before a spend decision rests on any of them.

Purpose: decide what a game ad shows, how it opens, how it sounds, what it may claim, and how a small studio tests game creative cheaply without misleading anyone. Production of video, playables and trailers is `video-studio` ([Playable ads and game trailers](../../video-studio/references/playable-ads-and-game-trailers.md)). Networks, bidding and per install economics are `mobile-app-growth` (its `game-user-acquisition` module). Claims and policy verdicts are `compliance` ([Games and virtual currencies](../../compliance/references/games-and-virtual-currencies.md)).

Boundary: Ads Master owns how a game earns, is found, keeps players, is measured and passes review. The game's own repo owns how it plays (game design, level design, difficulty). This module never proposes changes to a level or a rule to make an ad work; it captures what the game already does.

## 1. The rule every game ad passes first

**Show the game a new player gets.** The mechanic in the ad is the core loop most play time is spent on, and a new player meets it early.

Why this is the first rule and not a style choice:

| Case | What happened | What it teaches | Evidence |
|------|---------------|-----------------|----------|
| Playrix, Homescapes and Gardenscapes (ASA, 2020-09-30) | Facebook ads showed pin pulling puzzles. The puzzles existed in the games as mini games that appeared rarely and only at later levels; the main game was match 3 and decorating. The ads carried "Not all images represent actual gameplay". The ASA ruled the ads misleading under the CAP Code rules on misleading advertising, qualification and exaggeration and said Facebook's length limits were long enough to show representative play | A mechanic that exists but is rare or late is not representative. The disclaimer did not cure it | [Reported, 2026-10] (pocketgamer.biz, fkks.com and others) |
| Top Games, Evony: The King's Return (ASA, 2024-04-03) | A paid X video showed shooting numbered barrels. The puzzles were real gameplay, but the core game was city building with puzzle and PvP or PvE elements, and the storyline could not progress without the other parts. The advertiser's argument that viewers of the ad retained above 80% was not accepted | Real footage is not enough. The ad must convey the core playing experience | [Reported, 2026-10] (mishcon.com, DWF round up) |
| Rivergame and AppQuantum (ASA, 2022) | Further rulings against mobile game ads that did not show the game | The pattern is settled in the UK, not a one-off | [Reported, 2026-10] |
| Platform policies | Meta, Google and TikTok misrepresentation policies reject ads that misrepresent the product | A ruling in one market is also a platform policy risk everywhere | [Reported, 2026-10]; check the current policy page per platform |

House rule derived from these cases (ours, not a regulator threshold): **the mechanic shown must be the core loop and must be reachable in the first session of a fresh install.** If the team cannot point to the level and minute where a new player meets it, the ad does not ship. Disclaimers such as "not all images represent gameplay" may not cure a misleading impression; never rely on them.

### Representativeness test (fill per concept, attach to the brief)

| Check | Pass condition | Evidence to attach |
|-------|----------------|--------------------|
| Same verb and rules | The player action and the rule in the ad are the game's core loop | Mechanic name from the game repo's own description |
| Reachable early | A new player meets this mechanic in the first session | Level id or mode and median minutes from install (level funnel from `measurement`) |
| Share of play | The mechanic is what most play time is spent on | Play time share by mode or mechanic (`measurement`); if unavailable, the game repo's statement |
| Captured, not drawn | Footage comes from a real build or the game's capture mode | Build version, capture date, level id or seed |
| Same look | Art, UI, effects and difficulty match the build | Side by side frame vs build screenshot |
| Honest fail | Any fail shown is one a real player can produce with real inputs | Recorded input log or a human play capture |
| Side modes labeled | A rare or late mode is not presented as the game | The ad names it ("bonus levels") and still shows the core loop |
| Claims | Every number or superlative is on `brand/CLAIMS.md` | Claim IDs |

A concept that fails any row goes back to the brief, not to compliance for a workaround.

## 2. Hooks that work for games

Ranked by how often they appear in top game creative reports. Prevalence data is vendor level [Unverified]; test in your own account.

| Hook | What the first 2 seconds show | Why it may work | Risk | Required proof |
|------|-------------------------------|-----------------|------|----------------|
| Unsolved level | A real level one move from the solution, then the cut: "Can you finish it?" | The urge to finish an interrupted task (the Zeigarnik and Ovsiankina effects; the memory effect replicates poorly, the urge to resume is the practical bet, so treat it as a hypothesis [Contested]) | Becomes bait if the level is not in the early game or the solution is impossible | Level id reachable early; the solution exists in the build |
| Near fail or fail | A player fails by one move on a real level; the viewer sees the better move | Viewers want to do better than the player | The regulator cases above; "fail bait" where the mechanic is not the game | Representativeness test, honest fail row |
| Satisfying loop (ASMR) | The core action with the game's own sound: blocks sliding into doors, tiles clearing, a board filling | Sound on placements reward tactile loops; Color Block Jam creatives used unsolved levels, ASMR in game sounds and "No Ads" messaging [Reported, 2026-10, Segwise 2025-04, vendor] | Adding sounds or effects the game does not have | Audio stems from the build (section 3) |
| Progression or transformation | A board, room or kingdom changing over a session | Shows reward beyond one level | Only if the meta exists and is reachable | Capture from a real save at a stated level |
| Group or social moment | Friends' scores on a group board, a shared result grid, a group bonus round | Daily social games sell the group, not the puzzle | Fake friends, fake counts | Real UI with demo names labeled as examples |
| Daily ritual | "Today's puzzle" with a streak count | Daily games behave like Wordle or BeReal, not like level games | A streak framed as a loss threat (pressure) | Streak shown as celebration, never as "you will lose" |
| Challenge to the viewer | "Only 1% solve this" | Ego and curiosity | An invented statistic is a misleading claim | A real share from `measurement` with date range, or no number |
| Real player reaction (UGC) | A creator playing the real build with face cam | Native on TikTok and Reels | Scripted reactions to features that do not exist | Creator plays the store build; usage rights in writing |
| Celebrity | A known face playing or reacting; Royal Match ran celebrity ads [Reported, 2026-10] | Reach and attention at scale | Cost; the celebrity implying they play when they do not | Endorsement reflects honest use; contract and disclosure (section 7) |

Decision rule: a game account with no winner starts with 3 to 5 concepts across at least three different hook types from this table, each passing the representativeness test.

## 3. Sound: ASMR and the game's own audio

| Rule | Why | How |
|------|-----|-----|
| Use the game's real sound effects for the core action | The sound is part of the product being represented; it is also the cheapest satisfying audio you own | Export SFX stems from the build, or capture audio from the capture mode run (`video-studio` module) |
| Music may be added, licensed | Music is presentation, not product | License per [Avatars, voice and music](../../video-studio/references/avatars-voice-and-music.md); no unlicensed trending audio in paid ads |
| Do not add impact sounds the game lacks | A satisfying crunch that the game does not make is a small misrepresentation | If a sound is wanted in the ad, add it to the game first (game repo decision) or leave it out |
| Design for sound on and sound off | TikTok and Reels are mostly sound on; Feed placements play muted | Captions and on screen text carry the hook; the ASMR cut is the sound on variant |
| Loudness per platform spec | Loud ads get skipped and some platforms normalize | Follow [Platform specs and safe zones](../../video-studio/references/platform-specs-and-safe-zones.md) |

## 4. Claims that game ads make, and when they are allowed

| Claim | Allowed when | Blocked when | Evidence |
|-------|--------------|--------------|----------|
| "No ads" or "ad free" | The product shows no ads to anyone at the time the ad runs, in every market the ad targets | Ads run for some players, or only a paid tier is ad free. Then say what is true: "Remove ads with a one-time purchase" | House rule from consumer law on misleading claims; the "No Ads" angle is common in hybrid casual creative [Reported, 2026-10] |
| "Free" or "free to play" | Download and core play cost nothing; in-app purchases are disclosed where the platform shows them | The game cannot be progressed in practice without paying. The 2014 EU CPC common position on in-app purchases says a game presented as free must not mislead about real costs [Reported, 2026-10] | Store listing shows in-app purchases |
| "Offline", "no wifi needed" | The core loop works fully offline | Only some modes work offline | Test on airplane mode, logged in the brief |
| Numbers ("10,000 levels", "1M players") | A dated source from the game repo or `measurement` | Rounded up, projected or from another product | Claim ID in `brand/CLAIMS.md` |
| "Best", "#1" | Rank source, store, country and date | No source | Store rank screenshot with date |
| Prizes, cash, rewards | Never for a game without a licensed real money component | Always for social casino or skill games without licences; route to `compliance` gambling pack | |

Loot boxes in ads: if the game sells paid random items, UK ads must disclose that (CAP guidance on advertising in-game purchases, 2021, reported; verify) and UK store listings must state it prominently, for example "Contains loot boxes" or "Includes random-item purchases"; a generic "offers in-app purchases" is not enough. The CAP enforcement notice was published 2026-02-26 with monitoring from 2026-05-26 [Reported, 2026-10]. A BBC investigation (2024-11) found that of 26 top grossing Google Play games labelled as containing loot boxes, only 2 disclosed them in ads, with Monopoly Go among those that did not; the ASA said it was monitoring the sector [Reported, 2026-10]. The ASA has since upheld loot box disclosure complaints against other publishers (Kabam and Hutch, 2025-11) [Reported, 2026-10]. Rule: a game with paid random items carries the disclosure in every UK ad and listing, and `compliance` confirms the wording per market.

Children: never write a direct exhortation to children to buy ("Get your gems now!") in an ad that may reach minors; it is on the EU unfair practices blacklist (UCPD Annex I point 28) [Reported, 2026-10]. Game ads that may appeal to children are reviewed against [Games and virtual currencies](../../compliance/references/games-and-virtual-currencies.md).

## 5. Creative testing stages for games

Games test creative in stages because cheap upstream signals filter concepts before the expensive revenue read. Stage metrics come from UA practitioners [Practitioner consensus]; thresholds are set from the account's own history.

| Stage | Question | Primary metric | Secondary | Where | Who reads |
|-------|----------|----------------|-----------|-------|-----------|
| 0. Concept screen | Does anyone stop for this hook? | 3 second view rate, hook rate, organic shares | Comments that quote the hook | Organic TikTok or Reels posts, or a low budget reach test | creative-strategy |
| 1. Install efficiency | Does it make people install? | IPM (installs per 1,000 impressions) or CTR where IPM is not reported | CPM | The network or channel that will scale it (AppLovin, Unity, Mintegral, Meta, TikTok, Google) | creative-strategy with the channel agent |
| 2. Cost and quality | Do installs cost what we can pay, and do they stay? | CPI at the target geo | D1 retention of the creative's install cohort vs the account median | Same channel, target geo | mobile-app-growth, measurement |
| 3. Value | Do these players pay or watch ads? | D7 ROAS (or D3 when payback is short) | D7 retention, payer share | Finalists only, on event or value bidding | mobile-app-growth, measurement |

Formulas: IPM = installs / impressions x 1,000. CTR = clicks / impressions. CPI = spend / installs. D1 retention by creative = installs from the creative active on day 1 / installs from the creative (classic day N, one definition across the account; `measurement` owns it). D7 ROAS = revenue by day 7 from the cohort / spend on the cohort.

### Sample size you need before reading a stage

Install counts behave like Poisson counts, so the 95% interval on IPM or CPI is about plus or minus 1.96 / sqrt(installs):

| Installs per creative | Approximate 95% interval on IPM or CPI |
|----------------------:|---------------------------------------:|
| 25 | plus or minus 39% |
| 50 | plus or minus 28% |
| 100 | plus or minus 20% |
| 200 | plus or minus 14% |
| 400 | plus or minus 10% |

Retention is a proportion. At a D1 of 35%, the 95% interval is about plus or minus 9 points at 100 installs, 5 points at 300 and 3 points at 1,000. Two creatives whose D1 differs by 4 points cannot be told apart below about 1,000 installs each. So D1 by creative is a red flag detector (a creative 10 or more points below the account median at 300 installs), not a ranking tool.

### Kill and graduate rules (defaults; tune to the account)

| Signal | Decision |
|--------|----------|
| IPM in the bottom quartile of the account's last 90 days after 50 installs or 20,000 impressions, whichever comes first | Kill the execution; re-hook once if the concept has evidence |
| IPM top half but CPI above target by more than 30% at 100 installs | Check geo and placement mix with the channel agent before judging the creative |
| D1 of the creative cohort 10 or more points below the account median at 300 installs | Stop and run the representativeness test: installs that churn fast are the signature of an ad that promised a different game. Treat as a compliance flag, not only a performance problem |
| D7 ROAS at or above the stage 3 target with enough installs for the finalist read | Graduate to scaling; start the iteration ladder |
| Playable or video holding spend but IPM falling week over week | Fatigue; vendor reports put playable fatigue at 7 to 10 days [Unverified, vendor]. Measure your own decay before rotating on a calendar |

The stage 3 target comes from the game's own payback curve, not a benchmark. `mobile-app-growth` and `measurement` derive it (for example, if day 180 revenue is about 6 times day 7 revenue in your own cohorts and the payback goal is 120% at day 180, the D7 ROAS target is 20%; this worked logic was published by Liftoff in 2026-04 [Reported, 2026-10]).

## 6. Volume reality for a small studio

Large publishers and agencies screen many variants: practitioner reports describe 50 to 200 creative variants a week at agencies [Unverified], Rollic ideating 1,000 or more game prototypes a month [Reported, 2026-10], and Block Blast's studio running 50 or more product A/B tests a week with about 97% failing [Reported, 2026-10, vendor]. A small studio cannot match that and should not try.

| Lever | What a small studio does instead |
|-------|----------------------------------|
| Fewer, more different concepts | 2 to 4 new concepts a week at Starter, 4 to 8 at Growth, each a different hook type from section 2 ([Practitioner consensus]; size with the budget formula in [Testing frameworks and volume](testing-frameworks-and-volume.md)) |
| Cheap screening before paid tests | Post hook candidates organically first (stage 0); pay only for the top third |
| Production from the game itself | A capture mode in the game repo renders gameplay at any length, ratio and language without screen recording (`video-studio` playables and trailers module); one capture produces many cuts |
| One body, many hooks | Lock a winning body and swap the first 2 seconds (hook test, [Testing frameworks and volume](testing-frameworks-and-volume.md)) |
| Video first, playable second | Video is reported as about 80.9% of game creatives [Unverified, FoxData, vendor]; build a playable only for a concept that already won as video, since a playable costs days, not hours |
| Kill fast, keep the log | Every killed concept keeps its row in `creative-library/registry.csv` with the reason; patterns go to memory after two reads |

Budget check before planning volume: concepts readable per week = weekly test budget / (target CPI x installs needed per concept). Example: USD 1,000 a week, target CPI USD 1.00, 100 installs per stage 1 read gives 10 concept reads a week; at a CPI of USD 4.00 it gives 2 or 3. Plan the slate to the budget, not to a benchmark.

## 7. Celebrity, creators and UGC for games

| Topic | Rule |
|-------|------|
| Celebrity ads | The celebrity's statements reflect honest use; if they say they play, they played. Contract covers usage term, markets, platforms, paid social whitelisting and morality clause. Show real gameplay in the same ad, so the star sells the game the viewer will get |
| Creators playing the game | Creators play the public store build, not a debug build with unlocked content. Their reaction is genuine; scripted lines are labeled as the brand's ad |
| Disclosure | Paid creator posts carry the platform's paid partnership label and the market's disclosure ("ad", "reklam" in Turkey) per [Creators and UGC](creators-and-ugc.md) and `compliance` |
| Minors | No creators under 18 in ads for games with in-app purchases or paid random items; no content made to appeal mainly to children for such games |
| Rights | Written usage rights before paid use; gameplay footage recorded by a creator is still the studio's game, but the creator's face and voice need rights |
| AI presenters and voices | Allowed for narration with disclosure where required; never a synthetic "real player" testimonial ([AI creative production](ai-creative-production.md), [Compliance and disclosure](compliance-and-disclosure.md)) |

## 8. Game creative brief (template)

```
# Game creative brief: <concept ID> <working name>
Game and build: <game id, store build version, capture mode available yes or no>
Audience and placement: <channels, ratios, sound on or off>
Hook type (section 2): <unsolved level | near fail | ASMR loop | progression | group | daily | challenge | UGC | celebrity>
First 2 seconds: <what is on screen at t = 0>
Core loop shown: <mechanic>; reachable at <level or mode>, about <minutes> from install (source: <measurement export, date range>)
Representativeness test: <pass or fail per row in section 1>
Capture plan: <level id or seed, input log, length, ratios, languages>
Sound: <game SFX stems, licensed music id>
Claims: <claim IDs from brand/CLAIMS.md, or none>
Disclosures: <loot box line for UK, paid partnership, AI disclosure>
Variants: <hooks x bodies x end cards>
Test: <stage, budget, read point, kill rule>
Compliance verdict: <reference>
```

## 9. Pre-compliance QA for a game ad

- [ ] Representativeness test filled and attached; every row passes.
- [ ] Footage from a named build or capture mode run; no mock UI, no difficulty or art that the build does not have.
- [ ] Any fail shown is achievable with real inputs.
- [ ] No "No ads" claim unless the product shows no ads anywhere it is advertised.
- [ ] Paid random items disclosed for UK ads; store listing label checked with `app-store-optimization`.
- [ ] No direct exhortation to children; no countdown or scarcity line in an ad that may reach minors.
- [ ] Every number traces to a claim ID with source and date.
- [ ] Sound is the game's own SFX plus licensed music.
- [ ] Naming follows [Briefs and naming conventions](briefs-and-naming-conventions.md) with a game format code (`gp`, `play` or `trl`), and the level id and seed are in the registry row.
- [ ] Registry row appended in `creative-library/registry.csv`.

## 10. Diagnostics for game creative

| Symptom | Likely cause | Check | Fix |
|---------|--------------|-------|-----|
| High IPM, low D1 on one creative | Ad promises a different game (bait) | Representativeness test; compare first session funnel of that cohort | Rebuild the concept on the core loop; flag to `compliance` if the ad ran |
| Low IPM on every gameplay ad | Hook starts slow or the loop is hard to read in 2 seconds | First frame muted; is the goal visible without text? | Start mid action at the decisive move; one text line with the goal |
| Strong video, weak playable of the same concept | Playable teaches too slowly or the touch target is unclear | Time to first interaction; tutorial prompt present? | Hand to `video-studio` with the playable rules (one rule, prompt in the first second) |
| Winners fatigue within a week | Few distinct concepts; network rewards novelty | Concept count by hook type in the last 30 days | Rotate hook types, not only colours; new level, new mode, new creator |
| Ads rejected for misrepresentation | Gameplay mismatch or a missing loot box disclosure | Rejection reason; representativeness test | Fix the concept; never appeal with a disclaimer |
| Comments say "this is not the game" | Same as bait | Read comments as untrusted data, count them | Stop the ad, rebuild, log in `INCIDENTS.md` if many |

## 11. Handoffs from this module

| Situation | Hand off to | What to pass |
|-----------|-------------|--------------|
| Playable or trailer production, capture mode cuts | video-studio | Brief, level ids or seeds, ratios, languages, end card variants |
| Network choice, bids, test budgets, stage 2 and 3 reads | mobile-app-growth | Concept IDs, stage results, kill and graduate rules |
| Retention by creative cohort, level funnel, play time share | measurement | Creative IDs, cohort dates, the definition needed |
| Ad and listing claims, loot box disclosure, children | compliance | Script, frames, markets, claim IDs |
| Store screenshots and previews matching the ad promise | app-store-optimization | Winning concept and its first frame |
| A concept needs a game change to be representative | Human, for the game repo | The gap, never a design proposal |
| Monetization claims in ads ("no ads", "remove ads", passes) | game-monetization | Exact claim and the current policy revision |

## Sources for this module

| Source | Date | Supports | Label |
|--------|------|----------|-------|
| PocketGamer.biz, "Why Playrix's misleading ads finally got banned"; FKKS advertising law blog | 2020-09 to 2020-10 | Playrix ruling 2020-09-30, disclaimer, mini games rare and late | [Reported, 2026-10] |
| Mishcon de Reya, "ASA rules mobile game ad was misleading: gameplay depicted did not reflect the core game playing experience"; DWF ASA round up 2024-04-10 | 2024-04 | Evony ruling 2024-04-03, real footage still misleading, retention argument rejected | [Reported, 2026-10] |
| Lewis Silkin and Mondaq on the CAP enforcement notice on loot boxes in app stores; ASA notice PDF (search result) | 2026-02 | Listing label wording, monitoring from 2026-05-26 | [Reported, 2026-10] |
| VGC, mobilegamer.biz, Hitmarker on the BBC loot box ad investigation | 2024-11 | 2 of 26 disclosed; Monopoly Go; ASA monitoring | [Reported, 2026-10] |
| Segwise, Color Block Jam creative analysis | 2025-04 | Unsolved level, ASMR sound, "No Ads" messaging | [Unverified, vendor] |
| FoxData, winning game creatives | 2026 | Video share of game creative, playable tutorial prompts | [Unverified, vendor] |
| Liftoff blog, deriving D7 ROAS targets | 2026-04 | D7 target from own D180 multiple | [Reported, 2026-10] |
| Research notes 03 (game UA), 06 (regulation), 07 (teardowns: Royal Match, Color Block Jam, Block Blast, Monopoly Go) | 2026-10-12 | Stage metrics, volume reports, celebrity and fail ads | Mixed, as labeled inline |
