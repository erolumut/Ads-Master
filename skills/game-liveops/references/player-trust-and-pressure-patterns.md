# Player Trust and Pressure Patterns

> Knowledge as of 2026-10. Apple rules were read at the App Review Guidelines (last updated 2026-06-08) on 2026-10-12 [Official, 2026-06]. Regulator and enforcement items come from search summaries of law firm notes, regulator papers and trade press [Reported, 2026-10]; they are not legal advice. `compliance` gives the verdict on every customer facing word and on market rules; this module tells liveops where pressure hides in its own work so it reaches `compliance` early.

Gate: a pressure audit is G0 and G1. Removing a pressure pattern from a live product is a G3 change request like any other.

## 1. Motivation or pressure

Liveops uses time, goals, streaks and other players to bring people back. The same tools become pressure when they threaten a loss, hide a cost or target someone who cannot judge them.

| Tool | Motivation form | Pressure form | Why it matters |
|------|-----------------|---------------|----------------|
| Event end | End date and time shown plainly | Ticking countdown on an offer; "last chance" copy | Countdowns and time pressure named by consumer groups [Reported, 2026-10]; contract offers carry `countdown: false` |
| Streak | Count of days with free rest days, best streak kept | Streak loss threats, paid repair, guilt messages | Absence penalties and daily play incentives criticized by vzbv in 2025 [Reported, 2026-10] |
| Login calendar | Cumulative: next reward whenever you return | Consecutive: miss a day, back to day 1 | Punishes absence |
| Offers | Shown at a natural moment, fixed price, real money price visible | Pop up offer on app start; escalating prices; offers stacked at the fail moment | vzbv objected to purchase offers popping up right after app start (Monopoly Go) [Reported, 2026-10]; contract forbids escalation |
| Currencies | One currency, real money price shown, purchased currency never expires | Opaque currencies, bundle sizes that force leftovers, purchased currency that expires with the event | EU CPC principles on virtual currencies [Reported, 2026-10]; Apple 3.1.1: purchased credits or in-game currencies may not expire [Official, 2026-06] |
| Social | Group counts ("4 of 5 played") | Naming who broke the group streak; team kicks for absence | Social pressure; minors |
| Rewards | Earned through play; random rewards only with odds and labels | Paid random items, loot box style event rewards | Apple 3.1.1 odds before purchase [Official, 2026-06]; minors bans in some markets (`compliance`) |
| Notifications | Opted in, at the player's habit time, capped | Rewards for enabling push; threat messages; marketing without opt in | Apple 5.1.2(i) and 4.5.4 [Official, 2026-06] |
| Ads | Optional rewarded ads for uncounted extras | Ads as the only way to keep a streak or finish a free track | Ties loss aversion to ad views; contract typed grants |
| Competition | Small matched cohorts, disclosed bots | Undisclosed bots, pay to win ranks | Trust; contract ranked rule |

## 2. The rules and cases behind it

| Source | What it says or did | Label |
|--------|---------------------|-------|
| Apple Guideline 3.1.1 | IAP for digital unlocks; purchased credits or in-game currencies may not expire; loot box odds disclosed before purchase; gifting of IAP eligible items allowed, refunds only to the original purchaser | [Official, 2026-06] |
| Apple Guideline 4.5.4 | Push not required to function; promotional push only after explicit opt in through in-app consent language, with an in-app opt out | [Official, 2026-06] |
| Apple Guideline 4.5.3 | No spam through Game Center, push or Live Activities | [Official, 2026-06] |
| Apple Guideline 5.1.2(i) | Apps may not require users to enable system functions such as push notifications to receive monetary or other compensation | [Official, 2026-06] |
| Apple Guideline 2.3.13 | In-app events happen at the dates set; metadata accurate and about the event | [Official, 2026-06] |
| vzbv review of online games (2025) | Found manipulative design in all five games and platforms reviewed, including Monopoly Go: countdowns, incentives to play daily, rewards for watching ads; objected to purchase offers popping up right after app start; Scopely reportedly signed a cease and desist declaration and promised changes | [Reported, 2026-10] |
| EU CPC key principles on in-game virtual currencies (2025-03-21) | Real money price shown; no hidden costs or forced currency purchases; withdrawal rights; protection of children; national fines cited up to EUR 800k or 6% | [Reported, 2026-10] |
| EU DSA Article 28 guidelines on minors (2025) | Keep minors away from paid random items, manipulative design and obscured currencies (non binding; micro and small platforms exempt unless very large) | [Reported, 2026-10] |
| Digital Fairness Act | Proposal expected Q4 2026 (dark patterns, addictive design, virtual currencies, minors); not law | [Reported, 2026-10] |
| FTC v Epic (2022) | USD 245m in refunds over dark patterns and USD 275m over COPPA | [Reported, 2026-10] |
| FTC v Cognosphere, Genshin Impact (2025-01) | USD 20m; no purchases under 16 without parental consent; real costs and odds | [Reported, 2026-10] |
| Turkey Law 7578 (2026) | Game platforms: age rating and parental controls including purchase approval; duties mostly start after secondary regulation (verify) | [Reported, 2026-10] |
| Deceptive Design pattern library | Lists paid streak repair (Duolingo example) as a deceptive pattern | [Reported, 2026-10] |

Before a decision rests on any [Reported] row, `compliance` verifies it at the source (the `ads-verify` skill records the result).

## 3. Minors checklist for liveops

Use the contract's `ageBracket` (`under13`, `13to15`, `16to17`, `adult`, `unknown`) and the product's audience settings.

- [ ] No countdown or scarcity copy on any offer, event card or reminder shown to players under 18 or of unknown age where the market requires it (contract runbook rule 6).
- [ ] No streak threat or loss message, in game or by push, to minors.
- [ ] No marketing reminders to minors unless `compliance` approves the market rule and consent basis; turn reminders stay transactional.
- [ ] Event rewards for minors are reachable through normal play; no paid random rewards where the market forbids them.
- [ ] Purchases inside events follow parental approval rules where the law asks (Turkey Law 7578, the Genshin precedent in the US) [Reported, 2026-10].
- [ ] Child themed moments (for example April 23 in Turkey) are treated as child directed: copy and offers reviewed by `compliance`.
- [ ] No open chat with strangers by default; group invites among known people.
- [ ] Holdouts and experiments do not change what minors are offered (exclude them where possible).

## 4. Fairness rules liveops enforces

From the Game Monetization Contract v0.2 ([contract](../../game-monetization/references/monetization-contract.md)):

1. Every ranked board keeps a constant number of counted attempts per player per day; no event, reward, purchase, ad or admin action changes it.
2. In ranked modes, only `cosmetic`, `access` and `pass` grants; a `round` only from a social purchase and only to boards no wider than who receives it (a group round never writes to an `everyone` board).
3. A board that ranks people is ranked, including derived boards (streak boards, season tables, event leaderboards); nothing purchasable feeds it.
4. A `streak_protection` grant changes play when the streak is shown competitively; the product decides and declares it before rewarding or selling protection.
5. Compensation after an outage or a bug is an `admin` grant in the grant log, never a silent database edit.

Liveops checks each event spec and calendar row against these before it reaches the game repo, and asks `game-monetization` to run `monetization_check.py` when an event adds offers or grants.

## 5. Copy rules for live moments (drafts go to compliance)

| Avoid | Prefer |
|-------|--------|
| "Last chance! Season ends soon!" | "Season ends Sunday 22 November at 01:00" (local time) |
| "Your 40 day streak will die tonight" | "Today's round is ready" (opted in adults, at their habit time) |
| "You lost your streak" | "Welcome back. Your best is 40 days." |
| "Only 3 passes left" (when supply is not limited) | Nothing: fake scarcity is never written |
| "Don't let your team down" | "Your team is 80% to the chest" |
| "Get 100 coins for turning on notifications" | Ask after value, no reward (Apple 5.1.2(i)) |
| "Event ends in 02:59:41" next to an offer | End date and time as text; no timer on offers |

## 6. What not to copy from the hits

From the 2026-10-12 teardowns [Reported, 2026-10]:

| Pattern seen | Why we refuse it | Instead |
|--------------|------------------|---------|
| Lives that gate play; escalating continue prices (one blog's Royal Match example: a first continue near 900 coins rising above 2,000 after a second fail [Unverified, single source]) | Pressure at the fail moment; the contract forbids escalation inside one attempt | Fixed prices per attempt with `maxPerAttempt`; play never gated by a timer the player must pay to skip (`game-monetization` owns the economy) |
| Interstitial after every level stacked with rewarded ads | Ad pressure; early churn | `game-monetization` placement rules (grace, cooldown, caps) |
| Pop up offers at app start, opaque currencies, absence penalties (Monopoly Go per vzbv) | Regulator objections | Offers at natural moments, real money prices, no absence penalties |
| Loot box like dice or sticker packs bought with money | Gambling like design; minors bans; NY attorney general suit against Monopoly Go loot boxes reported in 2026-02 | Fixed contents, odds where random, `compliance` per market |
| Purchasable ranked races (levels beaten with paid boosters decide the rank) | Ranked result for sale | Milestone versions or dedicated no booster event levels ([Events and seasons](events-and-seasons.md) section 4) |
| "No Ads" messaging while ads still run | Misleading; ASA and store risk | Accurate entitlement copy |
| Fake gameplay in ads | UK ASA rulings on non representative game ads | Real gameplay (`creative-strategy`) |

## 7. Sunset fairness

When an event type, a mode or a whole game is retired:
1. Announce in game and in the calendar at least one full cycle ahead (a season for season content) [Practitioner heuristic].
2. Purchased items keep their value: convert, refund or keep them usable, per `game-monetization` and `compliance`; purchased currency never silently expires.
3. Grant unclaimed free rewards automatically before the end.
4. Keep history (results, best streaks, badges) visible where the product continues.
5. Stop reminders and store events tied to the retired content on time.
6. For a full game sunset, `compliance` and the human decide refunds, data export and store removal; store removal is a human action.

## 8. Pressure audit procedure

1. Collect every live surface: event cards, offer screens at each offer point, streak screens, closure screen, reminders, store event metadata, team and group screens.
2. Score each against section 1 (motivation or pressure) and section 3 (minors).
3. Check the calendar with `liveops_calendar_check.py` (pressure words, missing end dates).
4. List findings by severity: anything that reaches minors or contradicts the contract first.
5. Draft fixes as change requests; copy to `compliance`, offers to `game-monetization`, reminders to `lifecycle-crm`.
6. Re-audit after each season.

## 9. Pressure audit sheet

One row per surface; the audit output lists every row, not only the failures.

| Surface | Point or moment | Audience (age bracket, market) | Pattern seen | Motivation or pressure | Rule or case | Severity | Fix | Owner |
|---------|-----------------|--------------------------------|--------------|------------------------|--------------|----------|-----|-------|
| Streak screen after a break | `custom_streak_broken` | All, incl. 13to15 | "Streak lost" in red, repair offer | Pressure | Section 1 streak row; contract `streak_protection` | High | Welcome back screen; free rest day; remove the offer | game-liveops, game repo |
| Season end banner | on_menu, final week | Adults | "Ends in 02:59:41" timer next to the pass | Pressure | Contract `countdown: false`; consumer groups | High | End date as text; move the pass offer away from the timer | game-monetization |
| Event card in the store | Apple in-app event | All | "Best puzzle event ever" | Claim | Apple In-App Events metadata rules | Medium | Event name only; route copy to `compliance` | app-store-optimization |

Severity guide: Critical when it reaches minors with loss or urgency copy, or when a purchasable input feeds a ranked board; High for countdowns on offers, paid or ad gated streak rescue, rewards for notification opt in, pop up offers at session start beyond the policy; Medium for claims and wording; Low for presentation issues that inform rather than pressure.

## 10. Escalation

1. Critical findings are incidents: add a row to `ads-master/INCIDENTS.md`, tell the human, and draft the containment (kill switch or remote config) as a G3 change request the same day.
2. Findings that need a market rule (minors, loot boxes, consumer law) go to `compliance` with the surface, the copy and the markets; liveops does not interpret the law.
3. Findings in prices, offers or placements go to `game-monetization` with the offer point and the policy revision.
4. Findings in reminders go to `lifecycle-crm` with the moment id and the send volume.
5. Re-run the audit after the fixes ship and record the result in the journal.
