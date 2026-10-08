# Research Dossier: Creative Strategy (cross channel)

> Compiled 2026-10-08 for the `creative-strategy` agent. Scope: creative research, strategy frameworks, Meta Andromeda and creative diversity, formats and specs, hooks and scripts, testing, creative analytics and fatigue, AI creative production, creators and UGC, copywriting, briefs and operations, compliance and disclosure.

## Research limitations (read first)

- The build environment allowed 13 web searches before a shared search budget was exhausted, and blocked direct page fetches for every domain tried (Meta, Google, TikTok, FTC, EUR-Lex, trade press). The target of 35+ searches with primary source fetches was not met.
- What was verified live: Meta Andromeda and GEM framing, Meta creative diversity guidance as reported, Meta Creative Testing tool mechanics (practitioner reports), Meta fatigue labels, Meta Creative diversity rating (August 2026), Meta AI labeling (February 2025 and June 1, 2026), Advantage+ creative defaults (contested), Meta Advertising Week announcements (October 6, 2026), Meta Q2 2025 figures. All via search result synthesis of secondary and some official pages.
- Not verified live in this session: TikTok 2025 to 2026 creative and Symphony changes, Google Marketing Live 2026 creative features, LinkedIn 2026 formats, ChatGPT ads creative specs, current text of FTC and EU rules. These are covered from prior knowledge with [Unverified] or "not re-verified" labels and appear in the watch list.
- Verification pass 2026-10-08: a shared pass of targeted extended searches (sources 68 to 97) re-verified TikTok Symphony and the TikTok AIGC ad rule, Google Asset Studio and the July 2026 Google AI labeling update, ChatGPT ad formats, Meta's third-party AI labels, the Creative diversity rating, the EU AI Act Article 50 date after the Digital Omnibus, New York and California synthetic performer laws, YouTube ABCD figures and current safe zones. Labels below were upgraded or corrected accordingly; LinkedIn 2026 formats and FTC text were not re-verified.
- Every agent action that depends on these items must run the Freshness Protocol in `skills/creative-strategy/SKILL.md` first.

## Executive summary

1. Creative is the main targeting lever on Meta and TikTok in 2026. Meta's Andromeda retrieval system (announced December 2024, enhanced through 2025) picks a few thousand candidate ads per request from tens of millions, and Meta's guidance is to diversify concepts, messages, visuals and formats so the system has distinct options [Official, 2024-12; 2025].
2. Near-duplicate ads are widely believed to be grouped and to compete for the same retrieval chance. The "Entity ID" label and a "60% similarity" threshold are industry shorthand and vendor claims, not Meta documentation [Practitioner consensus; thresholds Unverified].
3. Meta started showing a Creative diversity rating (Low, Medium, High) per ad set in Ads Manager in late August 2026, based on visual similarity of images and video thumbnails and described as estimated and in development [Official, 2026-08, Business Help Center as quoted by trade press]. Separate fatigue, similarity and theme metrics are only in Insights API tests with a few agencies and resellers since June 2026 [Official statement, 2026-09].
4. Meta publishes no official number of ads per ad set. Practitioner ranges run from 3 to 5 genuinely different creatives for small advertisers to 10 to 20+ distinct concepts at scale; the right number is what the test budget can read [Practitioner consensus, contested].
5. Meta's Creative Testing tool (documented around October 2025) splits spend evenly across 2 to 5 ad variants inside a campaign, with a suggested budget of up to about 20% and up to 30 days, Highest volume bidding only [Practitioner reports of Meta docs].
6. Meta's Delivery column flags "Creative limited" (cost per result above past ads, under 2x) and "Creative fatigue" (2x or more); both lag leading indicators such as hook rate and CTR decay [Official per secondary summaries].
7. Generative AI in ad platforms went mainstream: Meta cited about 2 million advertisers using its genAI creative tools in mid 2025 and more than 4 million in October 2026, and made image to video generation in Advantage+ creative generally available on October 6, 2026 [Official per trade press].
8. Advantage+ creative enhancements are on by default for new Sales, Leads and App campaigns since the February 2026 unified creation flow (Meta for Developers "Automation Unification", 2026-02-13; the September date in some posts was not supported), and marketers reported AI features re-enabling and altering ads after opting out [Practitioner consensus, 2026-02; Marketing Brew 2026-04].
9. Disclosure tightened: Meta labels ads made with its genAI tools (since February 2025) and, from June 1, 2026, detects and labels third-party AI media using signals like C2PA; TikTok's ad policy requires the AIGC label or a clear disclaimer on AI-generated or significantly edited ad content; Google allowed in-creative AI labels and added an AI label setting in July 2026 (not a blanket mandate); EU AI Act Article 50 applies from August 2, 2026 and the Digital Omnibus (Regulation 2026/1744) did not delay it, apart from a marking grace period to December 2, 2026 for generative systems already on the market; New York's synthetic performer disclosure law applies from June 9, 2026 and California's from January 1, 2027; the FTC rule banning fake reviews and testimonials, including AI-generated ones, has applied since October 21, 2024 [Official, 2026].
10. Top operators win on process, not tools: VOC-driven concepts, a concept registry and naming convention, concept-level analysis, a funded testing lane with written kill and scale rules, modular production, and creator rosters chosen for diversity.

## State of the channel in 2026 (with numbers)

| Area | State | Numbers | Evidence |
|------|-------|---------|----------|
| Meta delivery | Retrieval (Andromeda) plus ranking models (GEM and downstream) do most of the targeting work in broad setups; creative supplies the signal | Andromeda: reported 10,000x increase in retrieval model complexity, +6% recall, +8% ads quality on selected segments (Meta engineering, Dec 2024, via secondary sources); Q2 2025 ads model improvements credited with about 5% more conversions on Instagram and about 3% on Facebook | [Official per secondary; attribution between Andromeda and GEM Contested] |
| Meta business scale | Ad revenue growth driven by AI ranking | Q2 2025 revenue $47.52B, +22% YoY | [Official per secondary, 2025-07] |
| Meta genAI adoption | Generative tools used broadly | About 2M advertisers (Q2 2025); more than 4M (October 2026) | [Official per trade press] |
| Meta video | Video dominates time spent | Meta cited video at about 60% of time on Facebook and Instagram (October 2026 coverage) | [Official per trade press, 2026-10] |
| Meta creative diagnostics | New native signals | Creative diversity rating (Low, Medium, High; 2026-08); fatigue labels; fatigue, similarity and top themes metrics tested with a small number of agencies and resellers via Insights API since 2026-06 | [Official, 2026-08 and 2026-09 statement] |
| Meta ad count | Documented limit | 50 non-archived ads per ad set; Page-level limits by spend tier | [Official, Marketing API reference] |
| Meta labels | AI media labeled | Meta tools since 2025-02; third-party detection since 2026-06-01 | [Official] |
| Meta creative testing | Native tool | 2 to 5 variants, up to about 20% budget, up to 30 days | [Practitioner reports, 2025-10] |
| TikTok | Creator native, sound on, Spark Ads, Smart+ automation, Symphony AI suite | Seedance 2.0 in Symphony Creative Studio GA 2026-05-13 (15 s, 2K, synced audio); Seedance 2.5 from 2026-08-03 (30 s; reference uploads 9 to 50 for paid advertisers in select markets); Symphony Agent 2026-06; AIGC label or clear disclaimer required on AI ad content | [Official, 2026-05 to 2026-08] |
| Google | Asset driven campaigns (PMax, Demand Gen, AI Max) consume text, image and video assets; Asset Studio is the creative home with Gemini, Veo and Nano Banana (Nano Banana Pro) models; Veo image to video in Asset Studio since 2026-03; GML 2026-05-20 announced Gemini Omni, Adobe and Canva imports and one-click creative testing for summer 2026 | ABCD adherence associated with about 30% short-term sales likelihood lift and 17% long-term brand contribution lift (Google with Kantar; modeled on about 11,000 ads) | [Study, re-confirmed 2026-10, modeled]; 2026 features [Official, 2026-05]; summer items not confirmed live |
| ChatGPT ads | Self-serve Ads Manager (ads.openai.com); sponsored chat card below the answer and product ad templates from feeds | Chat card title up to 50 characters (16 to 24 recommended), copy up to 100 (32 to 48 recommended), square image, favicon | [Official API reference for formats; limits Practitioner consensus, 2026] |
| Regulation | AI disclosure obligations in force | EU AI Act Article 50 from 2026-08-02 (not delayed by Regulation 2026/1744; 50(2) marking grace to 2026-12-02); New York synthetic performer law from 2026-06-09; California SB 1050 from 2027-01-01; FTC reviews rule since 2024-10-21; China AI labeling measures since 2025-09-01 | [Official, verified via law firm summaries 2026-10] |

## Channel by channel creative notes

### Meta (Facebook, Instagram, Threads)
- Delivery: Andromeda retrieval plus ranking models; broad targeting and Advantage+ campaigns rely on creative to find pockets of buyers [Official, 2024-12 to 2025-11].
- Diversity: Meta's guidance is to diversify by concept, message, visuals and format; Ads Manager added a Creative diversity rating in 2026-08 [Official].
- Creative inputs Meta can modify: Advantage+ creative enhancements, on by default since 2026-02, now including image to video (GA 2026-10-06); Muse Image announced 2026-07-07, not confirmed live [Official; availability Unverified].
- Diagnostics: Delivery column fatigue labels; similarity and fatigue metrics limited to Insights API tests with a few partners since 2026-06 [Official statement, 2026-09].
- Testing: Creative Testing tool and A/B tests in Experiments [Practitioner reports; Official A/B page].
- Labels: AI info labels for Meta tools (2025-02) and third-party AI media (2026-06-01) [Official].
- Creator: partnership ads; Creator Marketing Hub launched 2026-09-15 (discovery, permissions with expiry, one-click partnership ads, music and sticker removal); Instagram live video partnership ads from 2026-09-29; Threads ads without an Instagram account from 2026-09 [Official, 2026-09].

### TikTok
- Creative norms: creator-led, sound on, fast pacing, native text styles, trends; Spark Ads keep engagement on the original post [Practitioner consensus; Official product docs not re-fetched].
- AI: Symphony suite (Creative Studio, Symphony Agent, digital avatars, dubbing); Dreamina Seedance 2.0 GA in Symphony Creative Studio from 2026-05-13 and Seedance 2.5 (30-second video) from 2026-08-03 [Official, TikTok business blog].
- Labels: AIGC labeling for realistic AI content; C2PA-based auto labeling since 2024; ad policy allows AI-generated or significantly edited ad content only with the AIGC label or a clear disclaimer, otherwise rejection or restriction [Official, 2026 policy text via secondary]. The "effective 2026-07-21" date circulating in agency blogs is not in TikTok's changelog [Contested date].
- Research: Creative Center Top Ads and Creative Insights remain the main native research tools [Official, not re-fetched].

### Google (Search, PMax, Demand Gen, YouTube)
- Asset driven campaigns need complete, varied asset sets: RSA headlines and descriptions, PMax text, images, logos and video, Demand Gen images and video in multiple ratios [Official specs, not re-fetched].
- Generative assets: Asset Studio (Gemini, Veo, Nano Banana Pro) generates text, images and video from prompts, briefs or URLs inside Google Ads; Veo image to video since 2026-03; auto-generated video fills gaps when advertisers do not supply video [Official, 2026-03 and 2026-05].
- YouTube: ABCD (Attract, Brand, Connect, Direct) remains Google's core creative guidance [Official, not re-fetched].
- Disclosure: Google's July 2026 policy update permits text or visual AI labels inside AI-made image and video creatives, may auto-label assets from Google AI tools and adds an AI label setting across Google Ads, DV360, CM360, Merchant Center and Editor; mandatory synthetic content disclosure remains for election ads only [Official, 2026-07]. Reports of a universal "AI Generated" label mandate are incorrect.

### LinkedIn
- Formats: single image, video (including vertical), document ads, carousels, Thought Leader Ads, conversation and message ads [Official, not re-fetched].
- Creative norms: role-specific pain, numbers, real people, founder and expert POV; captions for muted autoplay [Practitioner consensus].
- Research: LinkedIn Ad Library [Official].

### ChatGPT and AI assistants
- OpenAI announced an ads test in ChatGPT in January 2026: US, Free and Go tiers, labeled, separate from answers, not near sensitive topics, advertisers do not receive chat content [Official, 2026-01].
- Formats by 2026-10: `chat_card` (advertiser name, favicon, title up to 50 characters, copy up to 100, square image, landing page) and `product_ad_template` from a product feed; no video in hands-on reviews; OpenAI asks for several title and copy variants with different angles [Official API reference; limits Practitioner consensus].
- Creative norms: direct, factual, intent matched copy; verify final specs with the `chatgpt-ads` agent.

### Microsoft Advertising
- RSA and asset formats mirror Google; Copilot and Audience Network placements reuse image assets [Official, not re-fetched].

## Timeline of changes, January 2025 to October 2026

| Date | Platform or body | Change | Creative implication | Evidence |
|------|------------------|--------|----------------------|----------|
| 2025-02 | Meta | Expanded genAI transparency: "AI info" labels on ads with images created or significantly edited by Meta genAI tools | Expect labels on AI-edited images | [Official, 2025-02] |
| 2025-03 | OpenAI | Native image generation in ChatGPT (GPT-4o image) | Cheap static concepting and mockups | [Vendor, not re-verified] |
| 2025-04 | Midjourney | V7 model | Better photoreal backgrounds and scenes | [Vendor, not re-verified] |
| 2025-05 | Google | Veo 3 (native audio) and Imagen 4 announced at I/O; Google Marketing Live: AI Max for Search, expanded generative asset tools | AI video with sound; more auto-generated assets in Google campaigns | [Vendor, not re-verified] |
| 2025-06 | Meta | Reported plan to fully automate ad creation and targeting by end of 2026 (press reports); new genAI ad tools showcased mid 2025 | Platform generated creative increases; strategist role shifts to inputs and guardrails | [Secondary, not re-verified] |
| 2025-07-30 | Meta | Q2 2025 earnings: Andromeda enhancements (more personalized candidates, Facebook Reels coverage), about 2M advertisers using genAI creative tools | Creative diversity matters more | [Official per secondary] |
| 2025-08 | Google | Gemini 2.5 Flash Image ("Nano Banana") | Fast consistent image editing for statics | [Vendor, not re-verified] |
| 2025-09-30 | OpenAI | Sora 2 video model | AI video quality jump; trust and disclosure questions | [Vendor, not re-verified] |
| 2025-10 | Meta | Creative Testing tool documented (2 to 5 variants, even spend split) | Native concept and hook tests inside campaigns | [Practitioner reports] |
| 2025-10 | Industry | Jon Loomer publishes creative diversification examples; "Andromeda" becomes dominant creative topic | Concept diversity becomes standard advice | [Practitioner, 2025-10] |
| 2025-11-10 | Meta | GEM (Generative Ads Recommendation Model) engineering post | Ranking models learn from richer signals; creative still the main input advertisers control | [Official, 2025-11] |
| 2025-11 | Industry | Clarifications that Andromeda did not "kill targeting" | Targeting inputs remain; creative does more matching | [Practitioner, 2025-11] |
| 2025-11 | EU | Commission digital omnibus proposals including AI Act timing changes | Final text left Article 50 dates unchanged (see 2026-07-24) | [Official] |
| 2025-12-11 | US (New York) | Synthetic performer ad disclosure law signed (GBL 396-b) | Disclose AI performers in ads seen in New York from 2026-06-09 | [Official law] |
| 2025-12 | Meta | Said it was testing creative analytics to diagnose fatigue and similarity | Native diversity tooling coming | [Secondary] |
| 2026-01 | OpenAI | Announced ads test in ChatGPT (US, Free and Go tiers) | New conversational ad copy surface | [Official, not re-verified] |
| 2026-02 | Meta | Advantage+ creative enhancements on by default for new Sales, Leads, App campaigns with the unified creation flow ("Automation Unification", 2026-02-13); September 2026 reports not supported | Review enhancements on every ad | [Practitioner consensus; developer notice via secondary] |
| 2026-03 | Google | Veo in Asset Studio: image to video for all campaigns and auto-generated Demand Gen | AI video from statics inside Google Ads | [Official, 2026-03] |
| 2026-04 | Meta | Trade press reports marketer pushback: AI features re-enabling, altering ads after opt-out; Meta says no penalty for opting out | Monthly enhancement audits | [Secondary, 2026-04] |
| 2026-05-13 | TikTok | Dreamina Seedance 2.0 in Symphony Creative Studio, GA for logged-in TikTok for Business users (15 s, 2K, synced audio, Reference to Video) | AI video variants inside Ads Manager, auto-labeled | [Official, 2026-05] |
| 2026-05-20 | Google | Google Marketing Live: Asset Studio as creative home (Gemini, Veo, Nano Banana), Gemini Omni, Adobe and Canva import, one-click creative testing announced for summer | More generated assets; test generated vs human assets | [Official, 2026-05] |
| 2026-06-01 | Meta | Automated detection and labeling of third-party AI-generated or edited ad media (C2PA and similar signals), including political ads | AI media from any tool may be labeled | [Official, Meta Help Center] |
| 2026-06 | Meta | Fatigue, similarity and top themes metrics tested with a few agencies and resellers via Insights API | Limited access | [Official statement to Marketing Brew, 2026-09] |
| 2026-06 | TikTok | Symphony Agent builds video campaigns from text prompts using trend analysis | Faster TikTok-native variants; review for sameness | [Official per trade press] |
| 2026-06-09 | US (New York) | Synthetic performer disclosure law in force (fines 1,000 then 5,000 USD) | Visible disclosure on AI performers in ads seen in New York | [Official law] |
| 2026-07 | Google | "Updates to AI labeling requirements": in-creative AI labels allowed, possible auto labels on Google AI assets, AI label setting rolled out through July | Label AI creative where markets require it | [Official, 2026-07] |
| 2026-07-07 | Meta | Muse Image announced; Advantage+ creative access "in the coming weeks" | Not confirmed live as of 2026-10-08 | [Official; availability Unverified] |
| 2026-07-21 (contested) | TikTok | Agency blogs report mandatory AI disclosure labels on realistic AI ad creative from this date; TikTok policy text requires AIGC label or disclaimer, changelog shows no AIGC change | Label every realistic AI asset regardless of date | [Contested date; rule Official] |
| 2026-07-24 | EU | Digital Omnibus on AI (Regulation 2026/1744) published, in force 2026-07-27: high-risk dates moved to 2027-12-02 and 2028-08-02; Article 50 untouched except 50(2) marking grace to 2026-12-02 for systems already on the market | EU deep fake disclosure still due from 2026-08-02 | [Official, 2026-07] |
| 2026-08-02 | EU | AI Act Article 50 transparency obligations apply | Disclose deep fakes and AI interactions in EU ads | [Official] |
| 2026-08-03 | TikTok | Seedance 2.5 in Symphony: up to 30 s video; 50 reference uploads for paid advertisers in select markets; AI labels, invisible watermark, C2PA | Longer AI video ads, still labeled | [Official, TikTok business blog] |
| 2026-08 | Meta | Creative diversity rating (Low, Medium, High) per ad set in Ads Manager | Native diversity signal; visual similarity only | [Official, Help Center as quoted] |
| 2026-09-08 | Meta | Muse personal AI agent with shopping and checkout | Agentic shopping context for ads | [per trade press] |
| 2026-09-15 | Meta | IAB Global Creator Week: Creator Marketing Hub launched globally; partnership ads available through Meta's ads connector for AI agents | Creator supply easier to source and run | [Official, 2026-09 via MediaPost, Marketing Dive] |
| 2026-09-16 | US (California) | SB 1050 synthetic performer disclosure law signed, effective 2027-01-01, model wording required | Build AI performer ads to the California standard now | [Official law] |
| 2026-09-21 to 09-26 | Meta | Threads ads available without an Instagram account | Another text-forward placement | [Official, 2026-09 via Social Media Today] |
| 2026-09-29 | Meta | Instagram live video partnership ads scheduled GA | Creator livestreams as ads | [Official, 2026-09] |
| 2026-10-06 | Meta | Advertising Week New York: image to video in Advantage+ creative generally available; Ads Creative Studio broader access; catalog video beta; agentic business assistant testing; 4M+ advertisers using genAI tools | Static libraries become video inputs; QA burden rises | [Official per trade press, 2026-10] |

## Best practice consensus

1. Research before ideation: mine reviews (especially 3 star and competitor 1 to 2 star), Reddit and forums, sales calls, support tickets and search queries; keep verbatim quotes. [Practitioner consensus]
2. Plan with a persona by awareness matrix (Schwartz) and cover several awareness levels, because broad delivery reaches all of them. [Practitioner consensus]
3. Distinguish angle, concept, execution and iteration; count only concepts as diversity. [Practitioner consensus, consistent with Meta guidance]
4. Hook in the first 1 to 3 seconds with visual, text and verbal layers aligned. [Official guidance from TikTok and Google ABCD; Practitioner consensus]
5. Design for sound off with captions on Feed, sound on for TikTok and Reels. [Practitioner consensus]
6. Native, creator-led formats on TikTok and Reels; brand early and clear CTAs on YouTube (ABCD). [Official Google; Practitioner consensus]
7. Supply placement-specific assets (9:16 plus 4:5 or 1:1, 16:9 for YouTube). [Official guidance]
8. Use a naming convention with concept IDs and analyze at the concept level. [Practitioner consensus]
9. Read funnel metrics in order (hook rate, hold rate, CTR, CVR) and fix the first broken stage. [Practitioner consensus]
10. Keep a funded testing lane with written kill and scale rules. [Practitioner consensus]
11. Scale winners through iteration ladders and adjacent concepts rather than duplicating ads. [Practitioner consensus]
12. Use AI for variation, versioning and localization; keep real people for proof; disclose as required. [Official rules plus Practitioner consensus]
13. Contract usage rights, whitelisting and Spark permissions before running creator ads. [Practitioner consensus; FTC requires disclosure]

## Contested topics (both sides)

| Topic | Side A | Side B | Working stance |
|-------|--------|--------|----------------|
| How many ads per ad set | Many (15 to 50) to feed Andromeda | Few but different (3 to 10), because budget must read them | Size by test budget; maximize distinctness, not count |
| Similarity thresholds and "Entity IDs" | Concrete thresholds (60%) and clustering rules | No Meta documentation; vendor numbers | Use the "new concept" test and spend distribution; treat thresholds as hypotheses |
| Advantage+ creative enhancements | Turn on: more variations, Meta optimizes | Turn off: brand damage, product misrepresentation, test noise | Enable selectively, review previews, test as separate ads, audit monthly |
| Dedicated testing campaigns | Force spend, clean reads | Results do not transfer to scaling campaigns, fragmentation | Use when in-situ starves new ads; validate graduation for 7 days; Creative Testing tool as a middle path |
| AI UGC and avatars | Cheap volume, fast localization, some advertisers report fine CPAs | Trust loss, labels, deception risk, FTC rule on fake testimonials | AI for explainers and variations with disclosure; never as fake customers |
| Polished vs lo-fi | Lo-fi UGC is native and trusted | Polished brand creative builds memory and works on YouTube and CTV | Placement dependent; test both within a concept |
| Statics in a video-first era | Statics are cheap, fast and often win on Meta Feed | Video gets more inventory (Reels) | Keep both; statics for offers and proof, video for cold audiences |
| Hook rate benchmarks | Fixed benchmarks (25% to 30%) are useful targets | Vary by vertical, placement and definitions | Use account percentiles |
| Creative diversity rating | Useful native signal | Visual-only, estimated, can mislead | Use as a hint alongside concept tagging |
| Creative replaces targeting | Creative is the targeting now | Targeting inputs, exclusions and structure still matter | Creative carries matching in broad setups; channel agents still own structure |

## What top operators do differently

1. They run creative as a research discipline: a VOC bank refreshed quarterly and a post-purchase survey that never stops.
2. They maintain a concept registry and naming grammar, so every report rolls up to concepts, angles, personas and creators.
3. They separate the creative strategist role from the media buyer role and meet weekly with a fixed agenda.
4. They track hit rate and production cost per winner, not just ad count.
5. They produce modularly: separate hook takes, raw footage, multiple lengths and ratios from one shoot.
6. They fund a testing lane and size volume to what the lane can read.
7. They iterate winners in ladders and plan the successor before the half-life ends.
8. They recruit creators for diversity (persona, age, setting, style), test them on proven scripts, and put the best on retainer.
9. They send high CTR, low CVR concepts to landing page work instead of killing them.
10. They use AI to multiply real assets (backgrounds, versions, localization), not to fake proof.
11. They audit platform AI settings and labels monthly and after duplications.
12. They keep a claims log and creator rights registry with expiry dates.

## Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|-----------|
| Launching dozens of near-duplicate variations as if they were new concepts | Starved ads, wasted production, fatigue of the one concept that spends | New concept test; production mix rules |
| Judging ads individually instead of concepts | Killing good concepts, scaling noise | Concept rollups |
| Declaring winners on a handful of conversions | False winners, scale failures | Evidence ladder |
| All creative aimed at product aware buyers (offers, features) | New customer acquisition stalls | Persona by awareness matrix |
| Repurposing Meta ads on TikTok without native edits | Poor TikTok results blamed on the channel | Native rebuild |
| No naming convention | No learning, repeated mistakes | Naming grammar and validation |
| AI-generated testimonials or synthetic customers | Legal exposure (FTC rule), platform action, trust loss | Compliance checklist |
| Leaving Advantage+ enhancements unchecked | Product misrepresentation, off-brand ads, claim risk | Per ad review, monthly audit |
| Running creator ads after usage rights expire | Legal claims, takedowns | Rights registry |
| Killing high CTR, low CVR ads | Losing strong concepts with a page problem | Handoff to `cro` |
| Testing more ads than the budget can read | No decisions | Budget formula |
| Editing ads mid-test | Learning resets, unreadable tests | Duplicate after the read |

## Benchmarks (source, date, sample, caveat)

| Benchmark | Value | Source and date | Sample | Caveat |
|-----------|-------|-----------------|--------|--------|
| Andromeda retrieval improvements | +6% recall, +8% ads quality on selected segments, 10,000x model complexity | Meta Engineering via secondary sources, 2024-12 | Meta internal | Platform level, not per advertiser |
| Meta ranking model conversion lifts | About 5% Instagram, about 3% Facebook | Meta Q2 2025 call via secondary sources, 2025-07 | Meta platform | Attribution between models contested |
| Andromeda Q2 2025 enhancements | Nearly 4% more conversions on Facebook mobile Feed and Reels | Secondary timeline citing Meta, 2025 | Meta platform | Single secondary source |
| Advertisers using Meta genAI tools | About 2M (2025-07); more than 4M (2026-10) | Meta via trade press | Platform | Adoption, not performance |
| Diverse creative test | 25 diverse creatives in one ad set: 17% more conversions at 16% lower cost vs five ad sets | Chatterbuzz (attributes to Meta) and Confect (attributes to an agency), 2026 | Unknown | Contested attribution; treat as anecdote |
| Diversification lift | 9% incremental reach, 32% conversion efficiency attributed to a Meta study | Adsights blog, 2026 | Unknown | Could not find the underlying study [Unverified] |
| Meta fatigue labels | Creative limited: cost per result above past ads, under 2x; Creative fatigue: 2x or more | Meta Help Center via secondary summaries, 2025 to 2026 | Account history | Lagging indicators |
| Creative Testing tool | 2 to 5 variants; up to about 20% budget; up to 30 days | Practitioner reports of Meta documentation, 2025-10 | n/a | Limits change |
| Frequency thresholds | 2.5 early warning, 3.5 refresh (practitioner); Meta: no universal number | Practitioner blogs, 2026 | Varies | Depends on audience size and budget |
| YouTube ABCD | About 30% short-term sales likelihood lift; 17% long-term brand contribution lift for ads following ABCDs | Google with Kantar (YouTube ABCDs page, Kantar validation page; study about 2021 to 2022) | About 11,000 ads scored with Kantar Link AI across 180 features | Modeled predictions from a Google-commissioned study, not measured sales |
| TikTok first 3 seconds | Most highest CTR videos highlight key message or product in the first 3 seconds | TikTok Creative Center insight (date not re-verified) | TikTok internal | Older guidance |
| TikTok in-feed length | About 21 to 34 seconds recommended in older TikTok guidance | TikTok (date not re-verified) | TikTok internal | May have changed |
| Hook rate and hold rate | Hook 25% to 35%+ "good", hold 20% to 40%+ (practitioner quotes) | Various practitioner blogs | Unknown | Definitions differ; use account percentiles |
| Ad count per ad set | 3 to 5 (small business), 6+, 8 to 15, 10 to 15, 15 to 20, 20 to 30 | Excite Media, Jetfuel, Wonderful, AdsUploader, Tentenco, 2025 to 2026 | Agency experience | No Meta number exists |
| Meta ad limit per ad set | 50 non-archived ads (the 150 figure from a 2026 podcast is not supported) | Meta Marketing API reference | n/a | [Official] |
| Meta creative diagnostics (Q2 2026) | +8.3% ad clicks, +15.7% conversions on Facebook from new user understanding models with GEM and sequence learning | Meta Q2 2026 earnings call, 2026-07-29 | Meta platform | Several changes combined; platform level |

Benchmarks vary by vertical, geography, season, placement and attribution settings. Compare a project against its own history first.

## Tools, APIs and MCP servers

| Tool | Use for creative | Access for Claude | Notes |
|------|------------------|-------------------|-------|
| Meta Marketing API (Insights) | Ad level metrics including video plays, ThruPlays | Via MCP connectors or exports | Requires user authorization; read-only for analysis |
| Meta Ad Library and Ad Library API (`ads_archive`) | Competitor ads; API covers political and EU-delivered ads | Web and API | Commercial ads outside the EU not in API [Practitioner consensus, verify] |
| TikTok Creative Center | Top Ads, Creative Insights, trends | Web (login for some features) | No public API for Top Ads known [Unverified] |
| TikTok Commercial Content API and Library | EU ads transparency | API for researchers | EU scope |
| Google Ads Transparency Center | Competitor ads on Google | Web | No performance data |
| LinkedIn Ad Library | Competitor LinkedIn ads | Web | Limited filters |
| Google Ads API and Google Ads MCP server (open source from Google) | Asset reports, RSA performance | MCP (read-oriented) | Verify repository status and scope |
| Google Analytics MCP server | Landing page CVR by ad | MCP | Verify |
| Official Meta Ads MCP server (mcp.facebook.com/ads) and Ads CLI | Ad-level creative performance for agents; partnership ads | MCP (Meta Business OAuth, read or write scope) | [Official, open beta since 2026-04-29]; route writes through `meta-ads` |
| TikTok for Business MCP Server | TikTok ad and creative reporting for agents | MCP (about 400 API for Business endpoints as tools) | [Official, 2026-05]; route through `tiktok-ads` |
| Community Meta Ads MCP servers (for example Pipeboard) | Meta insights for agents | MCP | Community; review permissions and security |
| Motion | Creative analytics and tagging | Exports; API or MCP availability unverified | Popular with DTC |
| Atria | Ad library plus analytics and AI briefs | Web | Combined research and analysis |
| Foreplay | Swipe file, discovery, competitor tracking, briefs | Web and API [verify] | Research and briefing |
| Triple Whale, Northbeam | Creative views inside attribution platforms | Exports | Own attribution models |
| Superads, Segwise | Creative analytics, AI tagging | Exports | Segwise strong in apps |
| AdsUploader, Revealbot, Madgicx | Bulk launching, automation, reporting | Web | Naming discipline at scale |
| AI production | Meta Advantage+ creative and Ads Creative Studio, Google Asset Studio (Imagen, Veo, Gemini image), TikTok Symphony, Midjourney, Runway, Kling, Veo, Sora, HeyGen, Synthesia, Arcads, Creatify, ElevenLabs, CapCut, Descript | Web tools | Verify commercial terms and labeling behavior |
| VOC | Gong, Chorus, Fireflies; Zendesk, Intercom; Okendo, Yotpo, Judge.me, Trustpilot; G2, Capterra; KnoCommerce, Fairing; Reddit | Exports | Strip personal data |

## Official sources to monitor

| Source | Why |
|--------|-----|
| Meta Business Help Center: Advantage+ creative, creative fatigue, Creative diversity, partnership ads, creative testing | Feature definitions and defaults |
| Meta for Business news and about.fb.com newsroom | Launches (Advertising Week, Cannes, earnings) |
| engineering.fb.com | Delivery system changes (Andromeda, GEM) |
| Meta Ads Guide | Specs and safe zones |
| Meta investor relations (quarterly earnings calls) | Adoption numbers, delivery improvements |
| TikTok Ads Help Center, TikTok Creative Center, TikTok newsroom, TikTok Advertising Policies | Specs, Symphony, Spark Ads, AIGC labels |
| Google Ads Help, Google Ads policy center, Google Ads and Commerce blog, Think with Google | Asset specs, generative features, AI disclosure, ABCD |
| Google Marketing Live (annual, May) | Major Google ad product launches |
| LinkedIn Marketing Solutions help and blog | Specs, Thought Leader Ads, new formats |
| OpenAI announcements and advertiser documentation | ChatGPT ads formats and policies |
| FTC business guidance (endorsements, reviews) | US disclosure rules |
| EUR-Lex and European Commission AI Office | AI Act Article 50, codes of practice, omnibus status |
| UK ASA and CMA | UK rules on influencer disclosure and fake reviews |
| C2PA | Provenance standard used for AI labels |

## Open questions and watch list

1. Is Meta's Creative diversity rating (ad set level, visual similarity of images and thumbnails) exposed in the API or the official MCP server, and do its thresholds change? Watch Meta Help Center and API changelog.
2. Will Meta publish similarity or fatigue metrics broadly (beyond select partners)?
3. Advantage+ creative defaults by objective and region; whether account-level opt-outs persist after duplication.
4. Muse Image and Ads Creative Studio availability; quality of image to video for product categories.
5. TikTok: Symphony Agent output quality and sameness risk; free vs paid Seedance access; whether TikTok adds a dedicated AIGC toggle in Ads Manager.
6. Google: whether Gemini Omni and one-click creative testing in Asset Studio went live after summer 2026; how the AI label setting interacts with EU and New York rules.
7. ChatGPT ads: video or carousel formats, measurement, policy categories beyond the current restricted list.
8. EU AI Act: final Commission code of practice on marking and labeling AI-generated content; national enforcement of Article 50 from 2026-08-02.
9. US state laws: further synthetic performer laws after New York (2026-06-09) and California (2027-01-01); effect of the December 2025 federal executive order.
10. Whether Meta's fully automated ad creation ambitions (reported for end of 2026) shift the strategist role further toward inputs (VOC, brand memory, guardrails) and evaluation.
11. Measurement of creative incrementality: platform lift tests for creative strategies (founder vs UGC, AI vs human) at Scale tier.

## Implications for the creative-strategy agent

1. Default to concept diversity: every slate must pass the new concept test against live ads; iterations are a second lane.
2. Treat Meta's native diversity and fatigue signals as hints; run concept rollups from ad names as the primary analysis.
3. Size creative volume to the test budget with the concepts-per-week formula; recommend budget changes through `growth-orchestrator`.
4. Review platform AI enhancements per ad and monthly; recommend switching off those that distort product, brand or claims.
5. Plan for AI labels on any AI media and add explicit disclosure for realistic synthetic people in EU ads.
6. Never produce AI testimonials or synthetic customers.
7. Run the Freshness Protocol for TikTok, Google, LinkedIn and ChatGPT creative specs before final delivery; TikTok, Google and ChatGPT 2026 details were re-verified on 2026-10-08, LinkedIn was not.
8. Write learnings to memory only after two concepts or one valid test agree.

## Sources

1. Meta Andromeda: Advantage+ automation's next-gen personalized ads retrieval engine. Meta Engineering. https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/ . 2024-12-02 (not re-fetched; corroborated by secondary sources).
2. Meta's Generative Ads Model (GEM): the central brain accelerating ads recommendation AI innovation. Meta Engineering. https://engineering.fb.com/2025/11/10/ml-applications/metas-generative-ads-model-gem-the-central-brain-accelerating-ads-recommendation-ai-innovation/ . 2025-11-10.
3. Expanding GenAI Transparency for Meta's Ads Products. Meta Newsroom. https://about.fb.com/news/2025/02/gen-ai-transparency-metas-ads-products/ . 2025-02.
4. How AI-generated images in ads are identified and labeled on Meta. Meta Help. https://www.meta.com/help/artificial-intelligence/355108217670024/ . Current (accessed via search 2026-10-08).
5. Meta Advantage+ creative. Meta for Business. https://www.facebook.com/business/ads/meta-advantage-plus/creative . Current.
6. A/B testing ads on Facebook and Instagram. Meta for Business. https://www.facebook.com/business/measurement/ab-testing . Current.
7. Ads about social issues, elections or politics. Meta Transparency Center. https://transparency.meta.com/policies/ad-standards/SIEP-advertising/SIEP/ . Current.
8. Meta Ad Library. Meta. https://www.facebook.com/ads/library/ . Current (not re-fetched).
9. Every Meta Ads Change in 2026 (Updated Weekly). Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026 . 2026 (updated through 2026-10).
10. Meta's New Creative Diversity Score Is Live in Ads Manager. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/metas-new-creative-diversity-score-is-live-in-ads-manager-what-ecommerce-brands-must-act-on-now . 2026-08.
11. Meta Launches Generative Video Ads and In-Conversation Checkout at Advertising Week NY. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/meta-launches-generative-video-ads-and-in-conversation-checkout-at-advertising-week-ny-what-ecommerce-brands-must-do-now . 2026-10.
12. Meta introduces new AI-powered tools at Advertising Week. Social Media Today. https://www.socialmediatoday.com/news/meta-introduces-new-ai-powered-tools-at-ad-week-2026/832288/ . 2026-10.
13. Meta Unveils Enhanced AI Business Assistant, Automated Ad Tools. MediaPost. https://www.mediapost.com/publications/article/418580/meta-unveils-enhanced-ai-business-assistant-autom.html . 2026-10-08.
14. Meta Advertising Week 2026 Ad Tools: Live vs Testing. Relevant Audience. https://www.relevantaudience.com/meta/meta-advertising-week-new-york-2026-ad-tools/ . 2026-10.
15. Meta creative diversification: what counts as a new ad. Relevant Audience. https://www.relevantaudience.com/meta/meta-ad-creative-diversification-same-hook-same-ad/ . 2026.
16. How Meta's AI push is changing ad creation. Marketing Brew. https://www.marketingbrew.com/stories/2026/04/07/meta-ai-ad-creation . 2026-04-07.
17. Meta's AI push has made its way into ad creative. Not all marketers are happy about it. Marketing Brew. https://www.marketingbrew.com/stories/2026/04/21/meta-ai-creative-tools-marketer-response . 2026-04-21.
18. Meta adds updated disclosure tags for AI-generated ads. Social Media Today. https://www.socialmediatoday.com/news/meta-adds-updated-disclosure-tags-for-ai-generated-ads/824658/ . 2026.
19. Sociable: Meta adds updated disclosure tags for AI-generated ads. Marketing Dive. https://www.marketingdive.com/news/sociable-meta-adds-updated-disclosure-tags-for-ai-generated-ads/824833/ . 2026.
20. Meta Andromeda and Creative Diversification: 7 Examples Explained. Jon Loomer Digital. https://www.jonloomer.com/meta-andromeda-creative-diversification/ . 2025-10.
21. Meta Andromeda: What It Means for Your Ad Strategy. Jon Loomer Digital. https://www.jonloomer.com/meta-andromeda/ . 2025-11.
22. Meta's Creative Testing Tool: Setup, Strategy, and Results. Jon Loomer Digital. https://www.jonloomer.com/meta-creative-testing/ . 2025.
23. Meta Andromeda Explained: Entity IDs vs Creative Volume. AdsUploader. https://adsuploader.com/blog/meta-andromeda . 2026.
24. Advantage+ Creative Enhancements: The Complete 2026 Guide. AdsUploader. https://adsuploader.com/blog/advantage-plus-creative-enhancements . 2026.
25. Meta Ads Updates (September 2026). AdsUploader. https://adsuploader.com/blog/meta-ads-updates . 2026-09.
26. Meta Creative Fatigue and Similarity Score: Complete Guide. Admetrics. https://www.admetrics.io/en/post/meta-creative-fatigue-and-similarity-score-complete-guide . 2026.
27. Meta Creative Fatigue: How to Diagnose and Fix It Fast in 2026. Atria. https://www.tryatria.com/blog/meta-creative-fatigue-diagnose-and-fix-2026 . 2026.
28. Andromeda Meta Ads: The Creative Strategy Guide for 2026. Atria. https://www.tryatria.com/blog/andromeda-meta-ads . 2026.
29. Meta Andromeda: The ultimate guide to Meta Ads in 2026. Confect. https://confect.io/tactics/meta-andromeda-2026 . 2026.
30. Meta Andromeda: AI Creative Targeting Guide (2026). Chatterbuzz Media. https://www.chatterbuzzmedia.com/blog/meta-andromeda-creative-targeting/ . 2026.
31. Meta Algorithm Changes 2026: Andromeda Update Explained. Jetfuel. https://jetfuel.agency/metas-2026-algorithm-update-what-andromeda-changed-and-how-to-adapt-your-ads/ . 2026.
32. Meta Ads Strategy 2026: Why Andromeda, GEM, and iOS 26 Broke the Old Playbook. Tentenco on Medium. https://medium.com/@tentenco/meta-ads-strategy-2026-why-andromeda-gem-and-ios-26-broke-the-old-playbook-78cba1ad4820 . 2026.
33. Meta Q2 2025 earnings: 21% ad revenue growth, AI infrastructure improvements. Mobile Dev Memo. https://mobiledevmemo.com/meta-q2-2025-earnings-2mm-advertisers-using-genai-creative-ai-infrastructure-improvements/ . 2025-07.
34. 3 stats from Meta's Q2 as Zuckerberg shares superintelligence vision. Marketing Dive. https://marketingdive.com/news/3-stats-from-metas-q2-as-zuckerberg-shares-superintelligence-vision/756376 . 2025-07.
35. Understanding Meta's Andromeda. EasyInsights. https://easyinsights.ai/blog/understanding-meta-andromeda/ . 2025.
36. Meta's Update: A New Way to Test Creatives. EasyInsights. https://easyinsights.ai/blog/metas-update-a-new-way-to-test-creatives-from-a-b-to-ai-led-optimization/ . 2025.
37. How Meta Built a New AI-Powered Ads Model for 5% Better Conversions. ByteByteGo. https://blog.bytebytego.com/p/how-meta-built-a-new-ai-powered-ads . 2025.
38. Metas Advantage+ Enhancements is now the default. Fyr.ai. https://fyr.ai/metas-advantage-enhancements-is-now-the-default/ . 2026.
39. Meta default-on generative creative. EdgeFix Automation. https://edgefixautomation.com/reports/meta-default-on-generative-creative . 2026.
40. Meta is auto-generating AI ads for its advertisers, causing headaches for image-conscious fashion brands. Glossy. https://www.glossy.co/fashion/meta-is-auto-generating-ai-ads-for-its-advertisers-causing-headaches-for-image-conscious-fashion-brands/ . 2025 to 2026.
41. Creative Diversification vs. Iteration for Meta Ads. New Engen. https://newengen.com/insights/meta-creative-diversification/ . 2025 to 2026.
42. What does Meta mean by creative diversification? Excite Media. https://www.excitemedia.com.au/meta-creative-diversification/ . 2025 to 2026.
43. Meta Shares New Tips to Maximize Ad Campaign Performance. Social Media Today. https://www.socialmediatoday.com/news/meta-new-tips-maximize-ad-campaign-performance/652231/ . 2024.
44. How To Evaluate Creative Performance in Meta Ads. Search Engine Journal. https://www.searchenginejournal.com/how-to-evaluate-creative-performance-in-meta-ads/558741/ . 2025.
45. 7 Meta ad testing frameworks for subscription apps. RevenueCat. https://www.revenuecat.com/blog/growth/7-meta-ad-testing-frameworks-for-subscription-apps . 2025 to 2026.
46. Creative testing software for Meta and TikTok. Motion. https://motionapp.com/blog/creative-testing-software-meta-tiktok . 2025 to 2026.
47. Why Creative Diversity in Ads is the #1 Performance Lever in 2026. Superads. https://www.superads.ai/blog/creative-diversity-in-ads . 2026.
48. The Creative Era: How Meta's Andromeda Rewrites Ad Strategy. Dentsu. https://www.dentsu.com/ae/en/our-latest-thinking/meta-andromeda-strategy . 2025 to 2026.
49. Meta tests agentic ad assistant that can create campaigns, change targeting and budgets. Best Media Info. https://bestmediainfo.com/mediainfo/mediainfo-digital/meta-tests-agentic-ad-assistant-that-can-create-campaigns-change-targeting-and-budgets-12631550 . 2026-10.
50. Google Ads Now Requires Disclosure Labels On AI-Generated Content. Search Engine Journal. https://www.searchenginejournal.com/google-ads-requires-disclosure-for-ai-generated-content/581925/ . 2026 (headline overstates the rule; see source 76 for Google's text).
51. AI in Advertising: A Regulatory Lookahead for 2026. Charles Russell Speechlys. https://www.charlesrussellspeechlys.com/en/insights/expert-insights/commercial/2026/ai-in-advertising-a-regulatory-lookahead-for-2026/ . 2026.
52. AI Content Labels: Platform Rules for Advertisers 2026. Digital Applied. https://www.digitalapplied.com/blog/ai-content-labeling-rules-advertisers-2026-reference . 2026.
53. AI Ad Disclosure Requirements in 2026: Meta, TikTok, YouTube, and the EU Compared. Cinerads. https://www.cinerads.com/blog/ai-ad-disclosure-requirements . 2026.
54. Regulation (EU) 2024/1689 (Artificial Intelligence Act). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2024/1689/oj . 2024-07-12 (not re-fetched).
55. FTC's Endorsement Guides: What People Are Asking. US Federal Trade Commission. https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking . 2023 revision (not re-fetched).
56. Federal Trade Commission Announces Final Rule Banning Fake Reviews and Testimonials. US Federal Trade Commission. https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials . 2024-08-14 (not re-fetched).
57. Google Ads Transparency Center. Google. https://adstransparency.google.com/ . Current (not re-fetched).
58. TikTok Creative Center. TikTok. https://ads.tiktok.com/business/creativecenter/ . Current (not re-fetched).
59. TikTok Commercial Content Library. TikTok. https://library.tiktok.com/ . Current (not re-fetched).
60. LinkedIn Ad Library. LinkedIn. https://www.linkedin.com/ad-library/ . Current (not re-fetched).
61. C2PA Content Credentials. Coalition for Content Provenance and Authenticity. https://c2pa.org/ . Current (not re-fetched).
62. Meta Marketing API Insights. Meta for Developers. https://developers.facebook.com/docs/marketing-api/insights/ . Current (not re-fetched).
63. Meta Debuts Generative AI Features for Advertisers. TechCrunch. https://techcrunch.com/2023/10/04/meta-debuts-generative-ai-features-for-advertisers . 2023-10-04.
64. Meta is using private AI chats for ads. Proton. https://proton.me/blog/meta-ai-ads . 2025.
65. Breakthrough Advertising. Eugene Schwartz. Book, 1966.
66. $100M Offers. Alex Hormozi. Book, 2021.
67. Demand-Side Sales 101. Bob Moesta. Book, 2020.
68. Transforming Video Creation With TikTok Symphony And Dreamina Seedance 2.5. TikTok for Business blog. https://ads.tiktok.com/business/en/blog/transforming-video-creation-tiktok-symphony-dreamina-seedance . 2026-08-03.
69. TikTok Symphony gains 30-second AI video with Seedance 2.5 upgrade. PPC Land. https://ppc.land/tiktok-symphony-gains-30-second-ai-video-with-seedance-2-5-upgrade/ . 2026-08.
70. TikTok Symphony gets Dreamina Seedance 2.0: what changes for advertisers. PPC Land. https://ppc.land/tiktok-symphony-gets-dreamina-seedance-2-0-what-changes-for-advertisers/ . 2026-05.
71. TikTok adds new AI creation tools for marketers. Social Media Today. https://www.socialmediatoday.com/news/tiktok-adds-new-ai-creation-tools-for-marketers/823463/ . 2026-06.
72. Misleading and false content (advertising policy). TikTok Ads Help Center. https://ads.tiktok.com/help/article/tiktok-ads-policy-misleading-and-false-content . 2026 (section list only seen; text via secondary).
73. Integrity and Authenticity. TikTok Community Guidelines. https://www.tiktok.com/community-guidelines/en/integrity-authenticity . Current.
74. TikTok AI Content Disclosure Rules for Advertisers (2026). UGCVids. https://ugcvids.ai/blog/tiktok-ai-content-disclosure-rules-2026 . 2026-08 (cites policy text and changelog).
75. TikTok's New AI Ad Disclosure Rules. Common Thread Collective. https://commonthreadco.com/blogs/coachs-corner/tiktok-ai-ad-disclosure-rules-ecommerce-2026 . 2026-07 (source of the 2026-07-21 date, Contested).
76. Updates to AI labeling requirements (July 2026). Google Advertising Policies Help. https://support.google.com/adspolicy/answer/17257106?hl=en . 2026-07.
77. Google Ads Has New Setting For Altered Or Synthetic Content. Search Engine Roundtable. https://www.seroundtable.com/google-ads-altered-or-synthetic-content-37656.html . 2024-07.
78. Multimodal Video Creation in Asset Studio. Google Ads announcements. https://business.google.com/us/accelerate/announcements/multimodal-video-creation-in-asset-studio/ . 2026.
79. Veo in Google Ads (announcement page). Google Ads announcements. https://business.google.com/en-all/accelerate/announcements/veo-google-ads/ . 2026-03.
80. Asset Studio: your creative home in Google Ads (GML 2026 post). Google Ads on X. https://x.com/GoogleAds/status/2057148459497746590 . 2026-05-20.
81. Google Marketing Live 2026: 11 Biggest Announcements. WordStream. https://www.wordstream.com/blog/google-marketing-live-2026 . 2026-05.
82. Ads API reference: Ads. OpenAI Developers. https://developers.openai.com/ads/api-reference/ads . 2026.
83. Hands-On With ChatGPT Ads: Initial Impressions. Jon Loomer Digital. https://www.jonloomer.com/chatgpt-ads-initial-impressions/ . 2026.
84. ChatGPT Ads Specs 2026: Every Character Limit, Reconciled. MakeLocalAds. https://makelocalads.com/blog/chatgpt-ads-specs . 2026.
85. EU AI Omnibus enters into force, amending the AI Act. White and Case. https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act . 2026-07.
86. EU AI Act Omnibus Agreement: Postponed High-Risk Deadlines and Other Key Changes. Gibson Dunn. https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/ . 2026-05.
87. Yes, August 2 Still Matters: most transparency obligations remain. Jones Walker. https://www.joneswalker.com/en/insights/blogs/ai-law-blog/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-trans.html?id=102nbon . 2026.
88. New York Synthetic Performer Law: What Advertisers Need to Know. Manatt. https://www.manatt.com/insights/newsletters/client-alert/new-york-synthetic-performer-law-what-advertisers-need-to-know . 2026.
89. California becomes the second state to enact a synthetic performer law. DLA Piper. https://www.dlapiper.com/en-us/insights/publications/2026/09/california-becomes-the-second-state-to-enact-a-synthetic-performer-law . 2026-09.
90. Validating Google's ABCD framework with the power of artificial intelligence. Kantar. https://www.kantar.com/industries/technology-and-telecoms/validating-googles-abcd-framework-with-the-power-of-artificial-intelligence . n.d.
91. The ABCDs of effective video ads. YouTube. https://www.youtube.com/intl/en_ae/ads/abcds-of-effective-video-ads . Current.
92. How advertisers are adjusting to Meta's ad creative diversification best practices. Marketing Brew. https://www.marketingbrew.com/stories/meta-ad-creative-diversification-best-practices-advertiser-approach . 2026-09.
93. Meta Ads Safe Zones: A Guide to the 2026 Unified Creative Updates. Billo. https://billo.app/blog/meta-ads-safe-zones . 2026-03.
94. TikTok Ad Specs 2026: Safe Zones and Best Practices. TryMyPost. https://www.trymypost.com/blog/tiktok-ad-specs-2026-safe-zones . 2026.
95. Introducing Muse Image: Image Generation Built for Your World. Meta Newsroom. https://about.fb.com/news/2026/07/introducing-muse-image-meta-ai/ . 2026-07-07.
96. Meta Launches Creator Marketing Hub, Live Video Ads. MediaPost. https://www.mediapost.com/publications/article/418022/meta-launches-creator-marketing-hub-live-video-ad.html . 2026-09-16.
97. Ad campaign (ad set) reference: limits. Meta for Developers. https://developers.facebook.com/documentation/ads-commerce/marketing-api/reference/ad-campaign . Living.
