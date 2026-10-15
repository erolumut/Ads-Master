# Game Studio Lifecycle

> Knowledge as of 2026-10 (research pass 2026-10-12). Portal and platform terms below were readable mostly as search results, so they carry [Reported, 2026-10], [Unverified] or [Contested]; Poki's split and exclusivity come from Poki's own developer pages seen in search results. Deal terms change per game and per year: read the current terms in full before any decision, and treat every number here as a reason to ask, not as an answer. Soft launch gates are owned by `measurement` (its `game-kpis` module, section 9) and are never copied from a benchmark.

Purpose: run each game through the same stages (prototype, soft launch, scale, live ops, sunset) with written gates and kill rules, spread budget across a portfolio of games by stage, and decide how each game is distributed: self published, with a publisher, or on portals and platforms.

## 1. The boundary

**Ads Master owns how a game earns, is found, keeps players, is measured and passes review. The game's own repo owns how it plays (game design, level design, difficulty).** Ads Master reads level data and drafts change requests; it never designs the game. When a stage gate fails because of the game itself (the first session confuses, a level spike churns players), the finding goes to the human for the game repo with the evidence, not as a design proposal.

## 2. Stages at a glance

| Stage | Question | Exit gate | Lead agents | Spend (G3 change requests) | Output |
|-------|----------|-----------|-------------|-----------------------------|--------|
| 0. Prototype | Does the one rule make people want another go, and does it sell in an ad? | Playtest replay intent plus a marketability read (section 3) | creative-strategy, video-studio, measurement (minimal events), market-intel | Small fixed test budget per prototype | Prototype verdict: continue, rework, kill |
| 1. Soft launch | Do players stay and pay (or watch) enough in a few markets to justify scale? | Every primary gate in `METRICS.md` PASS with the threshold outside the 95% interval (`game_kpis.py --gates`) | measurement, game-monetization, game-liveops, mobile-app-growth, compliance, store-submission | Envelope sized to reach the gate cohorts (section 6) | Gate read per market, iteration log |
| 2. Scale | How much can we buy before marginal return falls below breakeven at the payback horizon? | Marginal D7 ROAS vs the curve target; payback inside the horizon | mobile-app-growth, creative-strategy, video-studio, app-store-optimization, measurement | Budget steps through change requests; steps above 30% go to `fable-advisor` first | Scale plan, budget steps, creative volume |
| 3. Live ops | How do we keep players and grow revenue per player without pressure patterns? | Retention and ARPDAU stable or rising; event participation; season completion | game-liveops, game-monetization, lifecycle-crm, app-store-optimization | Maintenance UA plus live ops cost | Live ops calendar, policy revisions, monthly economy review |
| 4. Sunset | Is the game still worth its servers, content and support? | Sunset rule (section 4) | growth-orchestrator, compliance, game-monetization, lifecycle-crm, store-submission | UA off | Sunset plan with player notice |

Every stage change is a decision row in `DECISIONS.md`, drafted here and approved by the human.

## 3. Stage detail

### 3.0 Prototype: one rule, tested twice

| Test | How | Read |
|------|-----|------|
| Play test | 10 to 20 people from the target audience play a build without help (house default); watch the first session | Do they understand the rule without reading? Do they ask for another go? Where do they stop? |
| Marketability | A real gameplay video of the one rule as an ad (stage 0 and stage 1 in [Game ad creative](../../creative-strategy/references/game-ad-creative.md)) before monetization or meta exists | IPM or CTR against your own earlier prototypes, not against a benchmark |
| Representativeness | The ad passes the representativeness test | A prototype that only sells with a fake ad is a kill |

Context: publishers screen at a scale a small studio cannot match (Rollic was reported to ideate 1,000 or more games a month; Color Block Jam was reported to start as a June 2024 prototype by three founders) [Reported, 2026-10]. The lesson for a small studio is speed and a written verdict per prototype, not volume.

### 3.1 Soft launch

| Decision | Rule | Source |
|----------|------|--------|
| Markets | 1 to 3 markets that look like the scale markets in behaviour but cost less; commonly cited choices are Canada, the Philippines, Australia, New Zealand and the Nordics [Reported, 2026-10]. Royal Match was reported to soft launch in the UK and Canada in 2021-07; Royal Kingdom was reported to soft launch in 2023-04 and be reset after about a year [Reported, 2026-10] | Research note 03 and 07 |
| Gates | Derived from the game's own beta curve by archetype (level puzzle, hybrid casual, midcore, daily social game) in `measurement`'s `game-kpis` module, section 9; written into `METRICS.md` before the soft launch starts, with the minimum cohort (default 1,000 installs per gate) and the read date | measurement |
| Traffic mix | Paid soft launch traffic does not look like global scale traffic; read gates by source and market, never blended across a UA burst | measurement |
| Monetization | The policy file passes `monetization_check.py` before the first build; ads held back early (interstitial grace) per the contract | game-monetization |
| Store builds | `store-submission` dossier before every store build; web games can soft launch on their own URL and, when a portal fits, on a portal's limited test (CrazyGames' Basic Launch is a temporary test of about 2 weeks with a limited audience and monetization off [Reported, 2026-10]) | store-submission, section 5 |
| Iterations | One change at a time, a new cohort, a new read | measurement |

### 3.2 Scale

- Budget steps only after every primary gate passes outside the interval; each step is a G3 change request with a read date.
- Bidding sequence and network choice are `mobile-app-growth` decisions (install, then in-app event, then ROAS bidding as volume allows).
- Creative volume grows with budget; concepts follow the stages in [Game ad creative](../../creative-strategy/references/game-ad-creative.md), produced from the game's capture mode by `video-studio`.
- Store presence is ready before scale: Game Center and Play Games Services features, in-app events, featuring nominations (`app-store-optimization`).
- Stop scaling when marginal D7 ROAS falls below the target derived from the game's own curve, or when CPI rises faster than early LTV for two consecutive reads.

### 3.3 Live ops

- `game-liveops` owns the loop, events, seasons and the calendar; `lifecycle-crm` the messages; `game-monetization` the policy revisions; `app-store-optimization` the store events.
- Every monetization change raises `policyRevision` and has an experiment row; the monthly economy review reads ARPDAU split, payer conversion and complaints with D1 and D7 as guard rails.
- Content runway is watched monthly; a runway below the next drop date is an incident for the game repo.

## 4. Kill and sunset rules (written before the data)

| Stage | Kill or stop rule (house defaults; the human decides) |
|-------|--------------------------------------------------------|
| Prototype | Players do not ask for another go in the play test, or the marketability IPM sits in the bottom third of your own prototypes after two hook types, or it sells only with an unrepresentative ad |
| Soft launch | Two to three iterations without moving a failing primary gate (the `game-kpis` decision rule): kill or re-concept |
| Scale | Marginal return below breakeven at the payback horizon for two consecutive budget steps: step back to the last profitable level and hold |
| Live ops | Contribution after store fees, ad network share, servers, content and support negative for 3 consecutive months with no content plan that changes the curve: open the sunset plan |

Sunset plan (all customer facing steps are G3 and pass `compliance`):
1. Announce in game, by message and in the store listing with a notice period (house default 60 to 90 days; `compliance` sets the minimum per market).
2. Stop selling currency, items and new subscriptions on the announcement date; stop UA.
3. Keep purchased items and currency usable until shutdown; refunds per store rules and consumer law (`compliance`).
4. Archive final boards and give players a way to keep what they can keep (results, stats export).
5. Delist from stores (`store-submission`); delete or anonymize player data per the privacy policy.
6. Write the post mortem with the numbers that drove the decision.

Watch item: European campaigns on keeping purchased games playable after shutdown exist (a European Citizens' Initiative was reported in 2025) [Unverified in this pass]; check status with `compliance` before any sunset of a paid game.

## 5. Publishing and portal deals

### 5.1 Self publish or publisher

| | Self publish | Publisher |
|---|--------------|-----------|
| Gives | All revenue after store and network fees; control of pricing, monetization and data; the IP | UA money and scale, creative teams, soft launch infrastructure, live ops know how, network relationships |
| Takes | Your cash for UA and your time for everything else | A revenue share, often recoupment of UA from your share, exclusivity, rights in the IP or derivatives, control over monetization |
| Fits | A game whose home is its own URL and group graph; a studio that can fund a soft launch; a fairness rule you will not trade (no paid counted tries) | A level game that needs paid UA at scale and a studio that cannot fund it |

### 5.2 Portals and platforms

| Channel | What is known | Fit notes | Label |
|---------|---------------|-----------|-------|
| Poki | Poki's developer pages: developers keep 100% of earnings from players they bring themselves (search, bookmarks, own community) and split 50/50 on players Poki brings; Poki asks for web exclusivity (the game is on Poki only, for the open web; app stores and Steam stay open); non-exclusive licensing for a one-time flat fee is offered without the revenue share and marketing; developer tools in closed beta; term length reported as 5 or 7 years | Web exclusivity conflicts with a game whose home is its own URL; low fit for a daily group game; selective | Split and exclusivity [Reported, 2026-10] from Poki pages; term [Contested] |
| CrazyGames | Basic Launch: about 2 weeks, limited audience, monetization off; Full Launch chosen on playtime, conversion to gameplay and retention against other games, with full SDK integration and QA; revenue share starts at Full Launch | Split not published in the docs; third party figures conflict (60% of ads and 70% of IAP in jam terms; 50% to 70% elsewhere); EUR 100 minimum payout via Tipalti and no exclusivity are third party claims | Launch stages [Reported, 2026-10]; money terms [Unverified] |
| GameDistribution | Distributes HTML5 games to many sites; revenue share figures conflict (33% vs 45%) | Ask for the written split, payout terms and exclusivity; forum complaints about payouts exist and are unverified | [Contested] |
| YouTube Playables | Ads based (pre-roll, interstitial, rewarded) per Google's monetization page; revenue sharing piloted with a select number of creators; no in-app purchases as of 2026-09; beta in a few markets (reported: US, Canada, UK, Australia, India, Malaysia, Turkey) | Discovery inside YouTube; no IAP path today | [Reported, 2026-10] |
| Discord Activities | Games inside Discord through the Embedded App SDK; SKUs, entitlements and subscriptions; at launch (2024) IAP and subscriptions in the US, UK and EU on desktop; platform fee reported by a third party as 15% on the first USD 1 million then 30% | High fit for group play; check region and platform coverage and the fee in Discord's own terms | Mechanics [Reported, 2026-10]; fee [Unverified] |
| Reddit (Devvit) | Daily games are encouraged; Developer Funds paid by engagement tiers (the 2025 program reported up to USD 116,500 per app, tiered by daily qualified engagers and installs); a later cap of USD 167,500 per app appears only on an unverified mirror | Good fit for daily puzzles with a community; read the current program rules | 2025 program [Reported, 2026-10]; later cap [Unverified] |
| Telegram Mini Apps | Digital goods sold in Telegram Stars, which users buy through store in-app purchases | Store fees sit inside the Stars price | [Reported, 2026-10] |
| Facebook Instant Games | Meta changed web and Instant Games terms in 2025; the status after 2026-09-30 is unclear in research | Verify before any work | [Unverified] |
| TikTok Mini Games | Requires business verification; new growth formats in testing (2026-05) | Verify current availability by market | [Reported, 2026-10] |
| Google H5 Games Ads | Ad monetization for web games, closed beta | Never plan revenue that depends on admission | [Reported, 2026-10] |

### 5.3 Never sign without review

Signing a contract is never done by an agent (G4 class: it binds the business): the human signs after counsel reads it. Before that, `growth-orchestrator` writes the deal review below and flags any of these:

| Clause | Why it is dangerous |
|--------|---------------------|
| Exclusivity that covers your own URL, all of the web or all platforms | Ends the PWA first strategy and your own player relationship |
| A long term (multi year) with no performance based exit | You cannot leave a deal that does not deliver |
| IP assignment, a perpetual licence, or rights to sequels, derivatives or "similar games" | You lose the game or the next one |
| Right of first refusal or first negotiation on future games | Blocks other deals for years |
| Partner control over pricing, offers or ad placements | Can force paid counted tries or pressure patterns the contract forbids |
| Player data owned by the partner, or no access to your own analytics | You cannot measure or move players later |
| UA recoupment from your share without a cap, a report and an audit right | Your share can stay at zero |
| Unclear payout threshold, currency, timing or tax treatment | Cash never arrives |
| Termination for convenience on their side only | One sided risk |
| Mandatory SDKs that send data before consent | A consent breach you are liable for |
| Non-compete, most favoured nation or revenue share floors | Limits every other channel |
| Governing law and venue far from you | Disputes become unaffordable |

Deal review template:

```
# Deal review: <game> with <partner>, <date>
Channel and model: <portal, publisher, platform fund>
Money: <split per traffic source, recoupment, minimum guarantee, payout terms> (source: <document, page, date>)
Exclusivity: <scope, platforms, term, exit>
IP and future games: <assignment, licence, sequels, ROFR>
Control: <pricing, offers, ads, content changes>; conflicts with the monetization contract: <none or list>
Data: <ownership, access, consent order of SDKs>
Flags from section 5.3: <list>
Alternatives: <self publish plan, other portals>
Recommendation: <sign, negotiate these points, decline> for the human and counsel
```

## 6. Portfolio budget across games

Allocate by stage, not by enthusiasm. Each game's next budget step depends on its own gates.

| Bucket | How it is sized | Rule |
|--------|-----------------|------|
| Prototypes | A small fixed amount per prototype for the marketability read (enough installs for a stage 1 IPM read, section 5 of the game creative module) | Each prototype gets a verdict by a set date |
| Soft launches | Envelope = markets x minimum cohort per gate x expected CPI x planned iterations, plus creative production | No top up beyond the planned iterations without a decision row |
| Scale games | By marginal return at the payback horizon ([Budget allocation](budget-allocation.md)) | Budget steps only after gate passes; steps above 30% go to `fable-advisor` |
| Live ops games | Maintenance UA plus live ops cost, judged on contribution | Sunset rule in section 4 |
| Reserve | Held back for a winner moving from soft launch to scale | Released by the human |

Worked envelope (illustrative, not a benchmark): 2 soft launch markets x 1,000 installs per gate cohort x expected CPI USD 1.50 x 3 planned iterations = USD 9,000 of media before creative production. If the CPI read from `mobile-app-growth` is USD 3.00, the same plan needs USD 18,000: decide whether to cut to one market or one fewer iteration before starting, not halfway.

Comparing games: use contribution per install at the payback horizon after store fees, ad network share and refunds (`measurement` and `pricing-strategy`), never revenue alone. Shared engineering (the monetization contract, a capture mode, score integrity, the event taxonomy) is a portfolio asset; build it once and charge no single game for it.

Cross promotion between your own games is a channel: measure it with a holdout before counting it as growth, because it may move players rather than add them.

## 7. Which agents to activate per stage

| Agent | Prototype | Soft launch | Scale | Live ops | Sunset |
|-------|-----------|-------------|-------|----------|--------|
| measurement | Minimal events | Lead: gates, dashboards | Lead: ROAS and payback reads | Weekly dashboards | Final numbers |
| game-monetization | Not yet | Lead: policy file, economy | Offer and placement tuning | Lead: policy revisions | Stop sales plan |
| game-liveops | Not yet | Daily loop, first season | Calendar | Lead: calendar, events | Final event |
| compliance | Ad claims | Virtual currencies, minors, store text | Every new ad and offer | Every event and offer | Notice and refunds |
| store-submission | Not yet | Dossier per store build | Every build | Every build | Delisting |
| app-store-optimization | Not yet | Listing, game store features | Lead with featuring and events | Store events | Listing notice |
| mobile-app-growth | Marketability test | Soft launch UA | Lead: scale UA | Maintenance and re-engagement UA | UA off |
| creative-strategy | Lead: concept screens | Game creative stages | Volume | Event creative | None |
| video-studio | Capture cuts | Playables and gameplay cuts | Variant batches | Event and season trailers | None |
| site-engineer | Capture mode request, deterministic build | Score integrity, wrappers, release QA | Release QA | Release QA | Shutdown QA |
| lifecycle-crm | Not yet | Permission flow, drop and streak messages | Win back | Lead: event comms | Notice messages |
| pricing-strategy | Not yet | Price points per store and country | Regional pricing | Price reviews | None |
| market-intel | Genre and competitor scan | Competitor live ops | Competitor creative | Competitor events | None |

## 8. Game plan (output template)

```
# Game plan: <game>, stage <0 to 4>, <date>
Archetype card: loop length, plays per day by design, monetization mix, social graph, platforms
Stage question: <one sentence>
Gates (from METRICS.md, owned by measurement): <metric, threshold, derived from, minimum cohort, window, read date, decision if FAIL>
Kill rule for this stage: <written before the data>
Budget: <bucket, envelope with formula, change requests needed>
Distribution: <self publish, publisher, portals>; deal reviews: <links>
Policy file: <revision, monetization_check.py exit code>
Agents active and deliverables: <slug, deliverable, due>
Approvals needed: <G3 change requests; contracts for the human and counsel>
Next read date: <date>
```

## 9. Diagnostics across the lifecycle

| Symptom | Likely cause | First agent |
|---------|--------------|-------------|
| Cheap installs, poor D1 | Ad promises a different game | creative-strategy (representativeness test), then compliance |
| D1 fine, D7 fails | Early content or loop thins out after day 1; no reason to return | game-liveops, then the human for the game repo |
| Retention passes, D7 ROAS fails | Monetization timing, offer points or ad placements | game-monetization, measurement |
| Gates pass in one market only | Market fit or traffic mix | measurement, mobile-app-growth |
| Store build rejected | Review gap | store-submission |
| Revenue up, complaints and refunds up | Pressure patterns | compliance, game-monetization |
| Scale stalls at low spend | Creative volume or network fit | creative-strategy, mobile-app-growth |

## 10. Cadence

| When | What |
|------|------|
| Weekly per game | Stage read: gates or scale reads, creative stages, policy changes, incidents |
| Monthly portfolio | Budget by bucket, contribution per install per game, runway, sunset candidates, deal pipeline |
| Quarterly | Stage changes as decision rows; portfolio rebalance; Freshness pass on portal and store terms |

## Sources for this module

| Source | Date | Supports | Label |
|--------|------|----------|-------|
| Poki developer pages (sdk.poki.com, deals), via search | 2026 | 100% own traffic, 50/50 Poki traffic, web exclusivity, non-exclusive flat fee | [Reported, 2026-10] |
| CrazyGames developer docs (docs.crazygames.com), via search; third party guides (cinevva) | 2026 | Basic and Full Launch; split and payout claims | [Reported, 2026-10] and [Unverified] |
| Google YouTube Playables monetization page, via search; third party reports | 2026-09 | Ad formats, revenue share pilot, no IAP, markets | [Reported, 2026-10] |
| Discord developer docs on IAP for Activities, via search; third party guides | 2024 to 2026 | SKUs, entitlements, regions; fee claim | [Reported, 2026-10] and [Unverified] |
| r/Devvit community posts on Developer Funds | 2025 | 2025 program tiers and cap | [Reported, 2026-10] |
| Research note 02 (ad tech and portals), 03 (soft launch markets), 07 (teardowns), 08 (web first distribution) | 2026-10-12 | Portals, markets, prototype context | As labeled inline |
| `measurement` `game-kpis` module, section 9 | 2026-10 | Gate procedure, decision rule, minimum cohort | Internal module |
| Game Monetization Contract v0.1 | 2026-10 | Fairness rule that deals may not override | Internal contract |
