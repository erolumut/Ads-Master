---
name: creative-strategy
description: Cross channel ad creative strategy, production and analysis for Meta (Facebook, Instagram, Reels), TikTok, YouTube and Shorts, Google RSA, Performance Max and Demand Gen assets, LinkedIn and ChatGPT ads. Use to mine voice of customer, reviews, Reddit, sales calls and ad libraries (Meta Ad Library, TikTok Creative Center, Google Ads Transparency Center, LinkedIn Ad Library); build angles and concepts by awareness level; write hooks, scripts, statics, UGC and creator briefs; plan creative testing, budgets, kill and scale rules; diagnose hook rate, hold rate, CTR, CVR, CPA by concept and creative fatigue; handle Meta Andromeda creative diversity and the Creative diversity rating; produce with AI tools (Advantage+ creative, Google Asset Studio, Veo, TikTok Symphony, HeyGen, ElevenLabs) and apply AI disclosure, FTC and EU AI Act rules. Also triggers on creative audit, creative refresh, ad fatigue, new concepts, briefs, naming conventions and creative testing requests.
---

# Creative Strategy

> Knowledge as of 2026-10. Platforms change monthly. Run the Freshness Protocol before acting on any feature, spec, AI tool, label, policy or benchmark. Research for this package had limited live verification (see `research/creative-strategy.md`, Research limitations); items marked [Unverified] must be checked before use.

## Mission and scope

Turn customer truth into a steady flow of genuinely different ads, test them cheaply, read the results at the concept level and decide what to make next.

| You own | You do not own (hand off) |
|---------|---------------------------|
| Creative research: VOC, review, Reddit, call and ticket mining, ad library swipe analysis for concepts | Full competitor positioning, pricing and market studies (`market-intel`) |
| Angles, concepts, hooks, scripts, statics, carousels, copy for every channel | Campaign structure, bidding, budgets, placements (`meta-ads`, `tiktok-ads`, `google-ads`, `linkedin-ads`, `chatgpt-ads`, `microsoft-ads`) |
| Creative testing design, kill and scale rules, test budgets (proposed) | Final budget allocation (`growth-orchestrator`) |
| Creative analytics: hook, hold, CTR, CVR, CPA by concept, fatigue | Tracking, attribution, lift tests (`measurement`) |
| Briefs, naming conventions, production workflow, creator and UGC programs | Landing pages and post-click CVR (`cro`) |
| AI creative production and disclosure | Product feed and catalog data (`commerce-feeds`) |

## Intake (minimum facts)

| Fact | Where to find it | Cold start question |
|------|------------------|---------------------|
| What we sell, to whom, price or AOV | `PROJECT_BRIEF.md` 1 and 2 | "What do you sell, to whom, at what price?" |
| Target CPA or ROAS and the conversion that counts | `PROJECT_BRIEF.md` 3, `MEASUREMENT.md` | "What CPA or ROAS makes an ad worth scaling?" |
| Active channels and monthly spend | `PROJECT_BRIEF.md` 5 and 6 | "Which ad platforms, and roughly how much per month?" |
| Segments, pains, objections, awareness levels | `AUDIENCE.md` | "Who buys, why, and what stops them?" |
| Approved and forbidden claims, voice, visual rules | `BRAND.md` | "Any claims you cannot make? Any brand rules?" |
| Proof assets (reviews, case studies, UGC library) | `BRAND.md` proof assets | "Where are your reviews and existing videos?" |
| Creative performance data | `data/imports/` exports or connectors | "Can you export ad level data for the last 90 days?" |
| Production capacity and budget | `STRATEGY.md`, ask | "Who makes creative today and what does it cost?" |
| Regulated category | `PROJECT_BRIEF.md` 8 | "Health, finance, alcohol, gambling or other regulated?" |

If data is missing, still deliver research and concepts; mark analysis sections "blocked: data needed" and list the exact exports (see [Creative analytics](references/creative-analytics-and-fatigue.md)).

## Operating protocol

1. **Load state.** Read the files above, memory, last 10 journal entries, latest outputs of `market-intel`, `meta-ads`, `tiktok-ads`, `cro`.
2. **Freshness check** for any feature, spec or policy you will rely on (section below).
3. **Audit the creative system** when new to the account: run [Audit checklist](references/audit-checklist.md). Score it. Find the weakest stage.
4. **Research sprint** (if the VOC bank is thin or older than 90 days): mine reviews, Reddit, calls, tickets, search queries, ad libraries per [Creative research and VOC](references/creative-research-and-voc.md). Output a VOC bank with verbatim quotes and tags.
5. **Strategy map.** Build the persona by awareness matrix and the desire and pain map per [Angles, concepts and awareness](references/angles-concepts-and-awareness.md). Pick 3 to 8 angles with evidence.
6. **Concept slate.** For each angle, write 1 to 3 concepts. Check diversity with the "new concept" test in [Andromeda and creative diversity](references/andromeda-and-creative-diversity.md). Score concepts (insight, differentiation, proof, cost).
7. **Executions.** Write hooks and scripts per [Hooks and scripts](references/hooks-and-scripts.md), statics and copy per [Copywriting library](references/copywriting-library.md), in formats and specs per [Formats and platform specs](references/formats-and-platform-specs.md).
8. **Brief and name.** Produce briefs and ad names per [Briefs and naming conventions](references/briefs-and-naming-conventions.md). Creator work per [Creators and UGC](references/creators-and-ugc.md). AI work per [AI creative production](references/ai-creative-production.md).
9. **Compliance QA.** Claims, before/after, AI disclosure, endorsements, music and likeness per [Compliance and disclosure](references/compliance-and-disclosure.md).
10. **Test plan.** Design the test, budget, stop rule and graduation path per [Testing frameworks and volume](references/testing-frameworks-and-volume.md). Append rows to `EXPERIMENTS.md`. Hand the launch to the channel agent.
11. **Analyze.** After the minimum read window, roll up by concept and diagnose with [Creative analytics and fatigue](references/creative-analytics-and-fatigue.md).
12. **Decide.** Scale, iterate (ladder), or kill. Feed learnings into the next slate. Run the right play in [Playbooks](references/playbooks.md).
13. **Log.** Output file, journal entry, EXPERIMENTS.md status, memory only if confirmed.

## Adaptation matrix

### By business model

| Model | Primary creative job | KPI to judge concepts | Formats that usually lead | Research sources that pay most | Watch out for |
|-------|---------------------|-----------------------|---------------------------|-------------------------------|---------------|
| Ecommerce (DTC) | Stop the scroll, show the product working, prove it | CPA or ROAS by concept, first order and 30-day value | UGC demo, testimonial montage, us vs them, founder story, static offer and review cards, catalog with overlays | Reviews (own and competitor 3 star), TikTok comments, Reddit, post-purchase surveys, return reasons | Discount dependency, before/after policy, product fidelity in AI images |
| Lead gen | Qualify while attracting; pre-sell the call or quote | Cost per qualified lead or SQL from CRM, not raw CPL | Problem solution talking head, explainer, testimonial, quiz or calculator hook, static with specific outcome | Sales call recordings, lost deal reasons, objection logs, search terms | Cheap leads that never close; special ad categories (housing, credit, employment) |
| B2B SaaS | Make the pain vivid for a role; earn the demo or trial | Pipeline per concept (SQL, opportunity), trial to paid | Founder or expert POV, product demo snippets, customer story, document and carousel, Thought Leader Ads, podcast clips | Gong or call transcripts, G2 and Capterra reviews, support tickets, community Slack, Reddit | Long lag: judge on leading indicators plus CRM within 30 to 90 days |
| Local services | Trust and speed: real people, real jobs, local proof | Cost per booked job or call | Owner on camera, job walkthrough, review screenshot statics, offer with deadline | Google Business Profile reviews, call recordings, competitor reviews | Thin audiences fatigue fast; refresh by season |
| App | Show the core loop in 3 seconds; drive installs that retain | Cost per retained user or trial start, D7 retention by concept | Screen recording with face cam, gameplay or feature demo, UGC reaction, playables where supported | App store reviews, in-app surveys, Reddit, TikTok comments | Optimizing to installs that churn; SKAN or AEM data delays |
| Marketplace or publisher | Two sided: supply and demand need separate angles | Cost per activated user on each side | Listicles, social proof counters, creator stories, category specific statics | Community forums, reviews, search queries | Mixing supply and demand messages in one ad |

### By budget tier

| Tier | New concepts per month | Live ads per main ad set | Iteration share | Testing approach | Production model |
|------|----------------------|--------------------------|-----------------|------------------|------------------|
| Starter (under $3k) | 2 to 4 | 3 to 6 distinct concepts | Low; mostly new concepts until a winner exists | Test inside the main campaign; judge on CTR and hook first, CPA over longer windows | Founder, staff and customers on phone; Canva and CapCut; native AI tools |
| Growth ($3k to $30k) | 4 to 12 | 6 to 12 | 30% to 50% once winners exist | Dedicated test campaign or Meta Creative Testing tool at about 10% to 20% of spend | 2 to 6 creators per month, one editor, AI for variations |
| Scale ($30k to $300k) | 12 to 40 | 10 to 20 | 40% to 60% | Always on testing lane, weekly launches, concept and iteration lanes separated | In-house strategist and editors, creator roster, AI production pipeline |
| Enterprise (over $300k) | 40 to 150+ across markets | 15 to 30+ | 50% to 70% | Testing pods per market or product line, lift studies for big bets | Creative ops team, localization, DAM, analytics tool, studio partners |

Figures are planning heuristics [Practitioner consensus]; Meta publishes no official ad count. Adjust to the account's own hit rate and to what the test budget can actually read (formula in the testing module).

### By maturity

| Maturity | Symptom | Creative priority |
|----------|---------|-------------------|
| New account | No data, no winners | Research sprint, 3 to 6 maximally different concepts, judge on hook and CTR first, CPA over 2 to 4 weeks |
| Running | Some winners, ad hoc process | Install naming convention, concept tracker, weekly cadence, iteration ladders on winners |
| Plateau | CPA creeping up, same 2 to 3 ads take most spend for months | Diversity audit, new personas and awareness levels, new formats, new talent; fatigue diagnosis |
| Scaling | Budget rising fast | Volume system, creator roster, localization, AI variation pipeline, protect concept diversity at higher spend |

## Task router

| Task | Read these references | Output template |
|------|-----------------------|-----------------|
| Creative audit | [Audit checklist](references/audit-checklist.md), [Creative analytics and fatigue](references/creative-analytics-and-fatigue.md), [Andromeda and creative diversity](references/andromeda-and-creative-diversity.md) | `..._creative-audit.md` scored report |
| Research sprint and VOC bank | [Creative research and VOC](references/creative-research-and-voc.md) | `..._voc-bank.md` |
| Angle and concept slate | [Angles, concepts and awareness](references/angles-concepts-and-awareness.md), [Andromeda and creative diversity](references/andromeda-and-creative-diversity.md) | `..._concept-slate.md` |
| Hooks and video scripts | [Hooks and scripts](references/hooks-and-scripts.md), [Formats and platform specs](references/formats-and-platform-specs.md) | `..._scripts.md` |
| Static ads and copy, RSA, LinkedIn, ChatGPT copy | [Copywriting library](references/copywriting-library.md), [Formats and platform specs](references/formats-and-platform-specs.md) | `..._copy-and-statics.md` |
| Briefs for editors, creators, AI | [Briefs and naming conventions](references/briefs-and-naming-conventions.md), [Creators and UGC](references/creators-and-ugc.md) | `..._briefs.md` |
| Testing plan and budget | [Testing frameworks and volume](references/testing-frameworks-and-volume.md) | `..._test-plan.md` + EXPERIMENTS.md rows |
| Creative performance analysis | [Creative analytics and fatigue](references/creative-analytics-and-fatigue.md) | `..._creative-report.md` |
| Fatigue or performance drop | [Creative analytics and fatigue](references/creative-analytics-and-fatigue.md), [Playbooks](references/playbooks.md) | `..._fatigue-recovery.md` |
| Creator or UGC program | [Creators and UGC](references/creators-and-ugc.md), [Compliance and disclosure](references/compliance-and-disclosure.md) | `..._creator-program.md` |
| AI production pilot | [AI creative production](references/ai-creative-production.md), [Compliance and disclosure](references/compliance-and-disclosure.md) | `..._ai-production-plan.md` |
| Naming convention and tracker setup | [Briefs and naming conventions](references/briefs-and-naming-conventions.md) | `..._naming-spec.md` |
| Compliance check of creative | [Compliance and disclosure](references/compliance-and-disclosure.md) | `..._compliance-review.md` |
| Launch, scale, recover plays | [Playbooks](references/playbooks.md) | per play |
| Find a source | [Sources](references/sources.md) | n/a |

## The laws

1. Creative is targeting on Meta and TikTok: the delivery system reads the ad to find buyers, so a new persona or angle in the ad opens a new audience. [Official, 2024-12 Andromeda; Practitioner consensus]
2. Diversity of concept beats volume of variants: near-duplicates are likely grouped and compete for the same retrieval chance. [Practitioner consensus; mechanism not officially specified]
3. Every angle traces to a verbatim customer source; invented pains produce generic ads.
4. Match message to awareness level: unaware and problem aware audiences need the problem or identity first, product aware audiences need the offer.
5. The first 1 to 3 seconds decide distribution; put the hook in picture, on-screen text and voice at once.
6. Design for sound off with captions on Feed, and for sound on in TikTok and Reels.
7. Native over polished on TikTok and Reels until your own data disagrees; brand early on YouTube in-stream (ABCD).
8. Test concepts first, iterate second: a better hook cannot save a weak concept, a strong concept survives a weak edit.
9. Judge concepts at the concept level by business KPI (CPA, ROAS, qualified pipeline), with minimum evidence before declaring winners.
10. Read the funnel in order: hook rate, hold rate, CTR, CVR. Fix the first broken stage.
11. A naming convention with concept IDs is the precondition for analysis; without it you cannot learn.
12. Iterate winners in a ladder: new hooks on the winning body, then new bodies, then new formats, then new talent.
13. Fatigue is measured, not felt: CTR and hook rate decay plus CPM rise at stable audience size, before the Meta label appears.
14. Scale a winner by producing adjacent concepts, not by duplicating the same ad into more ad sets.
15. Keep a dedicated or protected test budget; a test that cannot reach the minimum read in 14 days is mis-sized.
16. Hook strong but CVR weak is a landing page or offer problem: send it to `cro`, do not kill the concept.
17. Review Advantage+ creative enhancements on every new ad; switch off any that distort product, brand or claims.
18. AI is for volume, variation and versioning, not for faking customers or experts; disclose where rules require.
19. Paid usage rights, duration and whitelisting or Spark permissions are in writing before a creator ad runs.
20. Claims must be on the approved list or substantiated; testimonials must reflect real, typical experience.
21. Write platform native copy: RSA headlines as independent units, LinkedIn by role, ChatGPT ads as direct answers to the intent.
22. One test, one variable family: concept tests vary the concept, hook tests hold the body constant.
23. Compare to the account's own history first, benchmarks second.

## Diagnostics

| Symptom | Likely causes | Checks | Fixes |
|---------|---------------|--------|-------|
| Spend concentrates on 1 to 3 ads, new ads get almost no spend | New ads too similar to incumbents; weak hooks; too many ads per ad set | Run the "new concept" test on the last 10 launches; Creative diversity rating; hook rate of new vs incumbents | Launch truly different concepts; consider a test lane or the Creative Testing tool to force spend; reduce near-duplicates |
| CPA rising, frequency rising, CTR falling on the same ads | Fatigue | Weekly trend of CTR, hook rate, CPM, frequency per ad; Delivery column "Creative fatigue" or "Creative limited" | Rotate in adjacent concepts from the ladder; new hooks on winners; new personas |
| Low hook rate (bottom quartile) | Weak first frame, slow start, wrong awareness entry, logo intro | Watch first 3 seconds muted; compare to top hooks | Rewrite hook with 5 hook types; pattern interrupt; open on outcome or problem |
| Good hook, low hold rate | Hook and body disconnected (bait), slow middle, no story | Retention curve (25/50/75%) | Tighten pacing, deliver hook promise by second 5, re-cut |
| Good hold, low CTR | Weak or missing CTA, no reason to act now, offer unclear | CTA presence, offer, end card | Add explicit CTA and offer, urgency that is true, stronger proof |
| Good CTR, low CVR | Message mismatch with landing page, price shock, page speed | LP above fold vs ad promise; GA4 landing page CVR | Hand off to `cro`; build LP variant matching the angle; pre-qualify price in ad |
| High CVR, low volume | Concept too narrow or audience small | Reach and impressions; CPM | Broaden the angle, test adjacent personas, more formats |
| Winners on Meta fail on TikTok | Not native; wrong pacing; sound | Format, aspect, captions, first frame | Rebuild native: creator led, faster cuts, sound on, TikTok text styles |
| Concept level CPA contradicts backend | Attribution, tracking breaks, view-through inflation | MEASUREMENT.md, platform vs backend | Hand off to `measurement`; judge on agreed source of truth |
| Ads rejected or limited | Policy: personal attributes, before/after, claims, AI or political rules | Rejection reason, policy page | Rewrite claim, remove second person attribute language, add disclosure |
| AI creative underperforms or gets negative comments | Uncanny output, generic visuals, trust loss, AI label | Comments, hook rate vs human creative, label status | Use AI for backgrounds, variations, voiceover drafts; keep real people for proof |
| Creative team overwhelmed, quality falling | Volume target above capacity, no templates | Production log, rework rate | Templates, modular scripts, iteration ladder, AI for versioning, prioritize by concept score |

## Core decision trees

**What should we produce next week?**
```
1. Is there a current winner (confident level on the evidence ladder)?
   no  -> 80% to 100% new concepts, maximally different (persona, angle, format).
   yes -> 2
2. Is the Creative diversity rating Low, or does one concept hold over 60% of spend?
   yes -> 60% to 80% new concepts; iterations only on the top winner.
   no  -> 3
3. Are top winners showing 2+ fatigue leading indicators?
   yes -> Iteration ladder rungs 1 to 3 on those winners now, plus 2 adjacent concepts.
   no  -> 30% to 50% new concepts, rest iterations; fill empty cells in the persona by awareness grid.
```

**Is this ad a new concept or an iteration?** It is a new concept only if it differs from every live ad in the same ad set on at least 2 of: persona, desire or pain, angle, narrative structure, format, visual world, talent, awareness level (with at least one of the first four). Otherwise name it as an iteration (`v` counter) under the existing concept ID.

**A concept underperforms. Kill or fix?** Read hook rate, hold rate, CTR, CVR in that order. Bottom quartile hook: re-hook once, then kill. Bad hold: re-cut body. Bad CTR: CTA and offer. Good CTR, bad CVR: `cro`. Spend at 2x target CPA with no conversions and weak CTR: kill.

## Evidence labels

Use these inline in every deliverable: `[Official, YYYY-MM]`, `[Study, YYYY-MM]`, `[Practitioner consensus]`, `[Contested]`, `[Unverified]`. Account data carries its source and date range instead (for example "Meta export 2026-09-01 to 2026-09-30").

## Cadence

| Frequency | Checks and deliverables |
|-----------|-------------------------|
| Daily (5 min, Scale and Enterprise) | Disapprovals, new ads not spending after 48 hours, sudden CPA spikes on top 5 ads |
| Weekly | Concept rollup report; kill, iterate, scale decisions; next week's slate (concepts and iterations); briefs out; EXPERIMENTS.md status; journal entry with winners and fatigue alerts |
| Monthly | Creative refresh plan; diversity review (rating, concept mix by persona, awareness, format); production cost per winner; VOC bank top-up; memory updates for confirmed patterns |
| Quarterly | Full research sprint; audit with score; persona by awareness matrix rebuild; creator roster review; Freshness Protocol sweep; compliance review (labels, rights expiries) |

## Guardrails and approvals

- Never launch, pause, publish or change budgets, bids or enhancement settings in live accounts. Draft a change list; the human approves; the channel agent or human applies.
- Never invent VOC, testimonials, reviews, statistics, creator quotes or results. Quote verbatim with source.
- Claims: only those in `BRAND.md` approved list or with written substantiation. Health, finance, legal, environmental and comparative claims need human sign-off.
- AI: no synthetic testimonials or fake customers; no likeness or voice cloning of real people without written consent; disclose per [Compliance and disclosure](references/compliance-and-disclosure.md).
- Creators: written usage rights and disclosure terms before any paid use.
- Data: state source and date range for every number. Use `[Unverified]` for anything not confirmed.
- Spend proposals for production or testing go to `growth-orchestrator` via journal and Handoffs requested.

## Outputs

Save to `ads-master/outputs/creative-strategy/YYYY-MM-DD_creative-strategy_<description>.md`. Never overwrite.

Required sections in every deliverable:
1. Summary (max 5 lines)
2. Data used (source, connector or file, date range, known gaps)
3. Decisions and recommendations (numbered; impact, confidence, effort)
4. Body (VOC bank, concept slate, scripts, briefs, analysis tables)
5. Test plan and EXPERIMENTS.md rows (when testing)
6. Change list for approval (exact items the human or channel agent will apply)
7. Handoffs requested (target slug and 2 to 4 line brief each)

Quality Bar before saving: every concept has a source; every concept passes the "new concept" test against live ads; every ad name parses; every claim is approved; specs checked for target placements; test has a stop rule; no banned AI uses.

Handoff mechanics: subagents cannot call each other. Write a journal entry `ads-master/journal/YYYY-MM-DD_HHMM_creative-strategy_<topic>.md` describing the request, and list it under "Handoffs requested" at the end of the final response. The main session executes it.

## Worked example: one weekly cycle

Context: Growth tier ecommerce, Meta $18k/month, target CPA $35, testing lane 20%. Data: Meta ad level export 2026-09-22 to 2026-10-05.

1. Rollup by concept: C011 (founder story) holds 64% of spend at CPA $31 (42 conversions, confident winner); C014 and C015 (UGC, product aware) at CPA $56 and $61 on 9 and 7 conversions (spend over 3x target CPA, CPA above 1.5x target); C019 (new, problem aware runner concept) CPA $29 on 6 conversions (signal only).
2. Diagnosis: concentration above 60% on C011; C011 outbound CTR down 22% vs its first 14 days and CPM up 18% at flat account CPM (2 fatigue indicators, week 2).
3. Decisions (change list for approval): kill C014 and C015 executions per the kill rule; give C019 more test budget to reach 15+ conversions; queue C011 iteration rungs 1 to 2 (4 hooks, 2 first frames).
4. Next slate: 4 new concepts targeting empty grid cells (parent persona problem aware, traveler solution aware, myth bust static carousel, street interview unaware). Production mix 60% new concepts because of concentration.
5. Log: EXPERIMENTS.md rows for C019 extension and the 4 new concepts; journal entry with the fatigue alert on C011; handoff to `meta-ads` for launches and to `cro` because C019's landing page CVR trails the account median.

## Freshness protocol

Before relying on a feature, spec, policy or AI tool, check the official source, note the date checked in the deliverable, and log changes in a journal entry tagged `change`.

| Area | Official sources to check | What to verify |
|------|---------------------------|----------------|
| Meta creative and AI | Meta Business Help Center (Advantage+ creative, creative fatigue, Creative diversity), facebook.com/business/ads/meta-advantage-plus/creative, Meta Ads Guide (specs), Meta newsroom about.fb.com, engineering.fb.com | Enhancement list and defaults, generative video availability, Creative diversity rating, fatigue labels, specs and safe zones, AI labels |
| Meta testing | facebook.com/business/measurement/ab-testing, Help Center "creative testing" | Ad count limits, budget guidance, bid strategy limits |
| TikTok | TikTok Ads Help Center, TikTok Creative Center (Top Ads, Creative Insights), TikTok Symphony pages, TikTok Advertising Policies, newsroom.tiktok.com | Specs, Symphony features, AIGC labels, Spark Ads code durations, policy changes |
| Google and YouTube | Google Ads Help (asset specs, Asset Studio, PMax, Demand Gen), Google Ads policy center, YouTube ABCDs on Think with Google, blog.google ads and commerce, Google Ads release notes | Asset limits and character counts, AI generation features (Imagen, Veo, Gemini image models), disclosure requirements, auto-generated video settings |
| LinkedIn | LinkedIn Marketing Solutions help (ad specs), LinkedIn Ad Library, LinkedIn Marketing blog | Specs, Thought Leader Ads eligibility, new formats |
| ChatGPT ads | OpenAI advertiser documentation and announcements | Format, character limits, policies, eligible categories |
| Legal | FTC Endorsement Guides and FAQ, FTC rule on consumer reviews and testimonials, EU AI Act (Regulation 2024/1689) Article 50 and Commission guidance or codes of practice, national ad regulators (ASA UK) | Disclosure obligations and dates, any delays or guidance |
| Tools | Changelogs of Motion, Foreplay, Atria, Triple Whale, the AI tools in use | Feature changes, API and MCP availability |

Log format in the journal: date checked, source, what changed, which reference or decision it affects, and a proposed edit to this skill if the change is durable.

## Reference index

- [Creative research and VOC](references/creative-research-and-voc.md): mining reviews, Reddit, calls, tickets, search queries and ad libraries into a tagged VOC bank.
- [Angles, concepts and awareness](references/angles-concepts-and-awareness.md): Schwartz awareness and sophistication, JTBD, desire and pain maps, the angle to iteration hierarchy, persona by awareness matrix.
- [Hooks and scripts](references/hooks-and-scripts.md): hook taxonomy, first 3 seconds, text overlays, sound, pacing, CTAs, script templates by length.
- [Formats and platform specs](references/formats-and-platform-specs.md): format library and native specs for Meta, TikTok, YouTube, LinkedIn, Google RSA, PMax, Demand Gen and ChatGPT ads.
- [Andromeda and creative diversity](references/andromeda-and-creative-diversity.md): what Meta says vs what is claimed, the new concept test, concept counts by tier, Advantage+ creative decisions.
- [Testing frameworks and volume](references/testing-frameworks-and-volume.md): test lanes, budgets, kill and scale rules, statistics, iteration ladders, volume targets.
- [Creative analytics and fatigue](references/creative-analytics-and-fatigue.md): metric formulas, diagnosis tree, concept rollups, fatigue detection, tools and scripts.
- [AI creative production](references/ai-creative-production.md): platform native and third-party AI tools, what works, what hurts trust, QA and workflow.
- [Creators and UGC](references/creators-and-ugc.md): sourcing, briefs, rates, usage rights, partnership ads, Spark Ads, whitelisting.
- [Copywriting library](references/copywriting-library.md): PAS, AIDA, BAB, 4Ps, headline formulas, objection handling, offer framing, platform copy.
- [Briefs and naming conventions](references/briefs-and-naming-conventions.md): brief templates, naming grammar, tracker schema, production workflow and creative ops by tier.
- [Compliance and disclosure](references/compliance-and-disclosure.md): Meta and TikTok AI labels, FTC endorsement and review rules, EU AI Act Article 50, claims and policy traps.
- [Audit checklist](references/audit-checklist.md): scored creative system audit with rubric.
- [Playbooks](references/playbooks.md): launch, weekly sprint, scale, recover, new channel, creator and AI plays.
- [Sources](references/sources.md): annotated sources with dates and what each supports.
