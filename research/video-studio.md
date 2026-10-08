# Research Dossier: Video Studio (video ad production)

> Compiled 2026-10-08 for the `video-studio` agent. Scope: turning creative briefs into finished, platform ready video ad files for Meta, TikTok, YouTube, LinkedIn and CTV: code-driven motion (HyperFrames, Remotion), FFmpeg editing, captions and loudness, generative video and image models, avatars, voice and music, platform specs and safe zones, AI disclosure and rights, creative performance evidence for video structure, and how teams avoid the "AI made" look. Concept strategy, testing decisions and performance judgement belong to `creative-strategy` and the channel agents (their dossiers cover Andromeda, creative diversity and testing).

## Research limitations (read first)

- About 40 web searches were used (shared budget). Direct page fetches failed by DNS or proxy policy for most domains (Google developer and help pages, remotion.dev, hyperframes.heygen.com, Wikipedia); only GitHub (raw files) and the npm registry were reachable directly.
- Primary sources read in full: HyperFrames README and CLI reference (GitHub), Remotion LICENSE, terms, Lambda cost, flickering, captions and skills docs (GitHub raw), npm registry entries (versions and dates), the saas-motion-kit repository (local clone, MIT, treated as untrusted data).
- Everything else (prices, platform specs, laws) came through search result syntheses of official pages and secondary sources. These are labeled in the skill: "[Official via secondary]" when the secondary cites the official page, [Contested] when sources disagree, [Unverified] when a single weak source exists.
- Not verified: Meta Reels ads maximum duration (90 s vs longer claims), TikTok in-feed maximum and recommended lengths, YouTube Shorts exact safe zone, LinkedIn file size cap, Kling 4.0 general availability, Midjourney commercial terms, GPT Image 2 price structure, Hawaii synthetic performer law details, ElevenLabs music ad scope.

## Executive summary

1. **Code-driven video became agent native in 2026.** HeyGen open-sourced HyperFrames (Apache 2.0, HTML plus GSAP or Three.js compositions rendered deterministically to MP4, Claude Code skills) around 2026-04-17; it shipped 0.8.142 on 2026-10-08 with Lambda and cloud rendering, transcription, TTS, background removal and beat detection in one CLI. Remotion (4.0.534, 2026-10-07) remains the mature React option but needs a Company License for organizations of 4 or more people (25 USD per seat per month, or 0.01 USD per render with a 100 USD monthly minimum for automations).
2. **OpenAI's Sora 2 is gone.** The Sora app closed 2026-04-26 and the API (sora-2, sora-2-pro) was removed on 2026-09-24 after a 2026-03-24 deprecation notice; the Azure preview retires 2026-10-15. Any pipeline built on it must migrate.
3. **The generative video market consolidated around Veo 3.1, Kling, Seedance and Runway, with prices falling.** Veo 3.1 costs 0.40 USD per second (standard), 0.10 to 0.12 (Fast) and 0.05 to 0.08 (Lite) on the Gemini API; Kling O3 on fal 0.084 to 0.168; Seedance 2.0 on BytePlus 0.07 to 0.78 by resolution; Runway Gen-4.5 0.12. New entrants Kling 4.0 (early access 2026-09-28, 30 s clips) and Vidu Q4 preview (2026-10-07, from 0.014 USD per s) push length and price further.
4. **Real faces are now gated.** After a February 2026 Hollywood backlash, ByteDance blocked real-person face references in Seedance 2.0 unless identity is verified; HeyGen requires a recorded consent video for digital twins. Consent infrastructure is becoming a moat for avatar vendors.
5. **Disclosure law arrived for synthetic performers.** New York's synthetic performer ad law took effect 2026-06-09, Hawaii enacted a near copy in 2026-07, and California's SB 1050 (signed 2026-09-16) applies from 2027-01-01 with prescribed wording and private actions. EU AI Act Article 50 applies from 2026-08-02; the final Commission guidelines (2026-07-20) treat a photorealistic invented person and a potentially misleading AI product image as deep fakes, and give commercial ads the standard label.
6. **Platforms label AI by default.** Meta labels ads made with its tools and, from 2026-06, ads with detected third-party AI signals (C2PA); TikTok requires its AIGC label or a clear disclaimer on realistic AI ad content; Google added an AI label setting and in-creative labels in 2026-07. Stripping provenance is both detectable and a trust risk.
7. **Audiences still punish obvious AI ads.** NIQ (2024) found AI ads less engaging and less memorable; Ipsos with Syracuse (2026-05) found human-made 30 s ads 14 percent stronger short term and 17 percent stronger long term than Sora-made versions; IAB (2026-01) found 45 percent of young consumers positive vs 82 percent of executives believing they are. McDonald's Netherlands pulled an AI holiday ad within 3 days (2025-12). Vendor tests show AI presenters can match humans on CTR in some accounts, so the answer is "real proof, AI stage", not "no AI".
8. **Music is the biggest legal trap in brand video.** Labels sued Quince (2026-04), Kroger (2026-08-21, 392 uses) and others for music in social marketing posts, including paid influencer posts the brand directed; Crumbl and DSW settled in 2026. Platform UGC music licenses never cover brand ads.
9. **Specs are converging on vertical, captions and safe zones, but numbers conflict.** Meta unified the Reels and Stories safe zone (about 14 percent top, 35 percent bottom, 6 percent sides) around 2026-03; TikTok and Shorts overlays differ, and Shorts values conflict between Google's template and measured previews. A "universal" 9:16 safe box (union of all three) is the practical answer for cross-posted files. No platform publishes an ad loudness target; -14 LUFS and -1 dBTP is the working consensus.
10. **Top operators run a factory with taste gates.** They keep humans at a few decisions (message, treatment, storyboard, final), template everything repeatable, iterate winners by keeping the first 2 seconds, vary one family at a time, name every file for analysis, and feed retention data back weekly. Tooling for agents (MCP servers from fal, Runway, HeyGen, ElevenLabs, Replicate; skills from HyperFrames and Remotion) makes this executable from Claude Code in 2026.

## State of the channel in 2026

| Area | State (2026-10) | Numbers and sources |
|------|-----------------|---------------------|
| Code-driven motion | HyperFrames (HTML, Apache 2.0, agent first) and Remotion (React, licensed) dominate; Motion Canvas inactive since 2024-12, community fork Canvas Commons and Revideo continue | HyperFrames 0.8.142 (2026-10-08), Remotion 4.0.534 (2026-10-07), Canvas Commons 0.4.0 (2026-09-24), Revideo 0.11.0 (2026-07-10) [npm registry]; HyperFrames reported 47.9k GitHub stars by 2026-09 [secondary] |
| Generative video | Veo 3.1 family, Kling 3.0 and O3, Seedance 2.0 and 2.5, Runway Gen-4.5 and Aleph 2.0, Luma Ray 3.2, Hailuo and H3, Pika 2.5, Wan 3.0, Vidu Q4 preview; Sora 2 discontinued | Per second prices from about 0.014 (Vidu Q4 launch) to 0.78 (Seedance 4K) USD [sources 15 to 35 below] |
| Generative images | Nano Banana 2 and Pro (Google), GPT Image 2 (OpenAI), FLUX.2 (BFL), Midjourney V8.x (no official API), Ideogram 3.0, Seedream | Nano Banana 2 0.045 to 0.151 USD per image; Pro 0.134 to 0.24; GPT Image 2 about 0.03 to 0.08 [Contested] |
| Platform native generation | Meta image to video GA 2026-10-06; TikTok Symphony with Seedance 2.0 (2026-05-13) and 2.5 (2026-08-03); Google Asset Studio with Veo, Nano Banana Pro, Gemini Omni (about 2026-08-26) | Meta cites more than 4 million advertisers using its generative ad tools (2026-10) [creative-strategy dossier] |
| Avatars | HeyGen (Avatar IV and V, API about 0.05 USD per s), Synthesia (Express-2), Arcads, Creatify, Captions or Mirage, TikTok Symphony avatars | HeyGen ended free API credits 2026-02 [secondary] |
| Voice and transcription | ElevenLabs (TTS, cloning with consent, Scribe v2 at 0.22 USD per audio hour), AssemblyAI Universal-3.5 Pro (2026-09-22, 0.21 USD per hour), Deepgram Nova-3, local whisper.cpp, Parakeet, WhisperX, FFmpeg 8.0 whisper filter (2025-08) | [sources 51, 59 to 62] |
| Music | Licensed libraries (Epidemic Sound Business covers paid ads under revenue caps; Artlist Pro covers paid ads and broadcast TV), platform commercial libraries, Eleven Music (self-serve excludes film, TV, radio) | Brand lawsuits 2024 to 2026 with statutory exposure up to tens of millions USD [sources 55 to 58] |
| Disclosure law | NY in force 2026-06-09; Hawaii 2026-07; California 2027-01-01; EU Article 50 from 2026-08-02 with final code (2026-06-10) and guidelines (2026-07-20); FTC fake testimonial rule since 2024-10-21 | Penalties: NY 1,000 to 5,000 USD per violation; EU up to 15M EUR or 3 percent of turnover; FTC up to 53,088 USD per violation |
| Consumer response | Skepticism of AI ads rising among young consumers; human-made ads outperform in the first controlled sales-validated comparison | IAB 2026-01; Ipsos and Syracuse 2026-05; NIQ 2024-12 |

## Timeline of changes, January 2025 to October 2026

| Date | Change | Impact on video production | Source |
|------|--------|---------------------------|--------|
| 2025-02 | Meta expands "AI info" labeling for ads made with its generative tools | Expect labels on Meta-generated media | Meta newsroom [creative-strategy dossier] |
| 2025-03-10 | Google enables "shorter video" enhancements for Demand Gen by default | Supply your own short cuts or opt out | PPC News Feed |
| 2025-04 | Warner sues Crumbl over 159 songs in social posts | Music licensing risk for brand social | Bloomberg Law |
| 2025-05 | Veo 3 launches with native audio (Google I/O) | Generated clips with synced sound | TechCrunch 2025-05-20 |
| 2025-05 | Beastie Boys and UMG settle with Chili's over "Sabotage" ads | Precedent for music in ads | Rolling Stone and others |
| 2025-08 | FFmpeg 8.0 ships a native whisper filter | Local captions inside FFmpeg | heise |
| 2025-08 | ElevenLabs launches Eleven Music with commercial clearance on paid plans | AI music option with carve-outs | ElevenLabs |
| 2025-08 | Sony sues DSW over 122 recordings in social ads | Same | Music Business Worldwide |
| 2025-09-01 | China's AI content labeling measures take effect | Labels for China-facing content | Official [creative-strategy dossier] |
| 2025-09-08 | Veo 3 price cut to 0.40 USD per s; 9:16 and 1080p in the Gemini API | Vertical generation affordable | AlternativeTo, Google |
| 2025-10-15 | Veo 3.1 stable release | Better prompt fidelity, ingredients, frames | Wikipedia via search |
| 2025-11 | Coca-Cola's second AI holiday ad draws backlash | Brand risk of visibly AI films | Forbes 2025-11-04 |
| 2025-11-17 to 12-01 | Cloudflare announces and closes the Replicate acquisition (about 57.4M USD) | Replicate continues as a brand and API | SEC 10-Q |
| 2025-11-20 | Nano Banana Pro (Gemini 3 Pro Image) launches | Better text in images, multi-reference consistency | Google DeepMind via press |
| 2025-12 | McDonald's Netherlands pulls an AI Christmas ad after 3 days | Same | NBC News |
| 2025-12 | fal raises 140M USD Series D at 4.5B USD | Aggregator scale | Sacra and press |
| 2025-12-11 | New York signs the synthetic performer ad disclosure law | Disclosure duty from 2026-06-09 | Manatt, Cooley |
| 2025-12-22 | FTC sends warning letters under the consumer review and testimonial rule | Enforcement signal on fake testimonials | Venable, Benesch |
| 2026-01-13 | Veo 3.1 Ingredients to Video gets native 9:16 and 1080p or 4K upscaling | Vertical ad shots from references | TechCrunch, Google blog |
| 2026-01 | IAB "AI ad gap" study | Consumer skepticism data | IAB |
| 2026-01 to 02 | Kling O3 (about 2026-01-31) and Kling 3.0 (2026-02-04 or 05) launch | Start and end frames, multi-shot, up to 15 s | Hedra, Atlas Cloud, Morphic |
| 2026-02 | Seedance 2.0 launches; on 2026-02-15 ByteDance restricts realistic faces and IP after Hollywood objections | Real-face references need verification | NBC News, secondary |
| 2026-02 | HeyGen ends free API credits (pay as you go) | Budget for avatar tests | Secondary |
| 2026-02-26 | Nano Banana 2 (Gemini 3.1 Flash Image) launches | Cheap, consistent keyframes and cast cards | Google blog via press |
| 2026-03 | Meta unifies Reels and Stories safe zones (about 14/35/6 percent) | One 9:16 layout for Meta vertical | Billo and 2026 spec guides |
| 2026-03-24 | OpenAI notifies developers that the Videos API and Sora 2 models will be removed 2026-09-24 | Migration needed | OpenAI community, secondary |
| 2026-04-02 to 09 | fal opens Seedance 2.0 API access (enterprise then broad, with filters) | API access outside BytePlus | Secondary |
| 2026-04-17 | HeyGen open-sources HyperFrames | Agent-native HTML to video | ai-tldr, GitHub |
| 2026-04 | UMG, Capitol and Concord sue Quince over music in TikTok and Instagram posts | Influencer posts count | Music Business Worldwide |
| 2026-04 | Video action campaigns finish upgrading to Demand Gen | Demand Gen asset sets (16:9, 9:16, 1:1, 4:5) | Secondary |
| 2026-04-26 | Sora app shuts down | Consumer Sora workflows end | Secondary |
| 2026-05-13 | Seedance 2.0 in TikTok Symphony Creative Studio | Free or bundled AI video inside TikTok | TikTok business blog [creative-strategy dossier] |
| 2026-05-18 | Ipsos and Syracuse publish human vs AI ad study (14 and 17 percent gaps) | Evidence for real-proof production | Syracuse University |
| 2026-05 | Warner and Crumbl reach a settlement in principle | Music risk realized | Bloomberg Law, Digital Music News |
| 2026-05-27 | Runway opens a hosted MCP server (its models plus Seedance, Kling 3.0, Veo 3.1, GPT Image 2, Nano Banana Pro) | Generation from Claude via MCP | AI Weekly |
| 2026-06-01 | Meta begins labeling ads with detected third-party AI signals (C2PA) | Labels on externally generated media | Meta Help Center [some blogs say 2026-07, Contested] |
| 2026-06-09 | New York synthetic performer law in force | On-screen disclosure for AI performers | Manatt |
| 2026-06-10 | EU publishes the final code of practice on marking and labelling AI-generated content | Two-layer marking for providers, label icons for deployers | Legal 500, Commission |
| 2026-06-17 | Kling 3.0 Turbo and Omni upgrade | Faster, cheaper Kling | Atlas Cloud [secondary] |
| 2026-07 | Google "Updates to AI labeling requirements" and AI label setting | In-creative AI labels allowed; settings across Google ad tools | Google Ads policy 17257106 |
| 2026-07 | Hawaii enacts a synthetic performer law nearly identical to New York's | Another disclosure market | Kelley Drye, Bloomberg Law [Contested] |
| 2026-07-20 | Commission adopts final Article 50 guidelines (C(2026) 5054) | Ads get the standard deep fake label | Bird and Bird, Faegre Drinker |
| 2026-07-24 to 27 | Digital Omnibus published and in force; Article 50 dates kept; marking grace to 2026-12-02 for existing systems | Deployer duties start 2026-08-02 | White and Case |
| 2026-08-02 | EU Article 50 applies | Label realistic AI people, products, scenes in EU-facing ads | EUR-Lex |
| 2026-08-03 | Seedance 2.5 in TikTok Symphony (30 s, more references) | Longer native AI clips on TikTok | TikTok business blog |
| 2026-08-06 to 24 | Alibaba Wan 3.0 beta then GA on Alibaba Cloud | Another low-cost model | Secondary |
| 2026-08-21 | Sony sues Kroger over at least 392 uses of recordings in social ads | Music risk at retail scale | Digital Music News, PPC Land |
| 2026-08-26 | Gemini Omni in Google Ads Asset Studio | Brief-driven video inside Google Ads | Search Engine Land [creative-strategy dossier] |
| 2026-09-16 | California SB 1050 signed (effective 2027-01-01) | Prescribed disclosure wording, audio-only ads covered | DLA Piper, Manatt |
| 2026-09-22 | AssemblyAI Universal-3.5 Pro | Cheaper accurate transcription | AssemblyAI |
| 2026-09-24 | Sora 2 API removed | Same | Secondary |
| 2026-09-28 | Kling 4.0 Flash early access (30 s clips, 10 keyframes), full launch announced for 2026-10 | Longer generated shots | Bloomberg |
| 2026-10-06 | Meta image to video generally available (Advertising Week) | Platform-made motion from statics | [creative-strategy dossier] |
| 2026-10-07 | Vidu Q4 preview (from 0.014 USD per s) | Price pressure | GlobeNewswire |
| 2026-10-08 | Google opens SynthID verification to everyone; HyperFrames 0.8.142 published | Provenance checks; tool velocity | Dataconomy; npm |
| 2026-10-15 | Azure OpenAI sora-2 preview retires | Last Sora endpoint ends | Secondary |
| 2026-12-02 | EU marking grace period ends for generative systems on the market before 2026-08-02 | Vendor watermarking everywhere | White and Case |
| 2027-01-01 | California SB 1050 effective | Disclosure wording required | DLA Piper |

## Best practice consensus

1. **Hook in the first 1 to 2 seconds, product or problem visible immediately.** TikTok recommends stating the core proposition in the first 3 seconds; Google's ABCD puts the brand and an attention hook early; Meta's Reels research links visual plus sound openings to higher purchase intent rankings. [Official, multiple]
2. **One message per ad.** Variants test ways to land the message, not different messages. [Practitioner consensus; saas-motion-kit]
3. **Design for sound off and sound on.** Captions always; voice plus music for Reels, TikTok and Shorts (over 75 percent of Instagram Reels views are sound on per Meta, 2024). [Official]
4. **Native vertical and native look per platform.** Separate 9:16 and 4:5 files for Meta, native 9:16 for TikTok and Shorts, 16:9 plus vertical for YouTube Demand Gen; no letterboxed or watermarked reposts. [Official and practitioner]
5. **Safe zones decide layout.** Use the platform overlay previews and a conservative union zone for cross-posting. [Practitioner consensus, 2026]
6. **Render big, deliver small, deterministically.** 4K masters downscaled with Lanczos; seek-safe compositions; seeded randomness; local assets. [HyperFrames and Remotion docs; saas-motion-kit]
7. **Variants by family.** Hooks first on a fixed body, then bodies on the winning hook, then CTAs; ratios and languages are deliverables. [Practitioner consensus]
8. **Name for analysis.** Concept, hook, body, CTA, length, ratio and flags in the ad name; registry rows per file. [Practitioner consensus; creative-strategy]
9. **Real proof, AI stage.** Real products, real UI, real people for proof; AI for settings, b-roll, versions and localization; disclose synthetic people. [Practitioner consensus; FTC; EU AI Act]
10. **Licensed audio only.** Brand ads need commercial licenses; platform commercial libraries for platform-only use. [Official libraries; lawsuits]
11. **Loudness about -14 LUFS integrated with a -1 dBTP ceiling for social; broadcast specs for CTV.** [Practitioner consensus; ATSC A/85, EBU R128]
12. **Human taste at a few gates.** Message, treatment, storyboard, final cut; automate the rest. [saas-motion-kit; practitioner]

## Contested topics

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| AI presenters vs human creators | Agency tests show AI characters winning 9 of 13 equal-budget tests with 17 to 29 percent lower CPA on winners; AI UGC CTR at 85 to 110 percent of human baselines (vendor aggregates, 2026) | Ipsos and Syracuse (2026-05) and NIQ (2024) show human-made ads stronger; RevenueCat saw most synthetic avatars dropped early, one with 68 percent lower CTR from lip-sync lag | Test within a concept; never as testimonials; disclose; keep real proof |
| Ideal TikTok length | Older TikTok guidance and some practitioners cite 21 to 34 s | 2026 guides recommend 9 to 15 s or 15 to 30 s | Test 15 s vs 30 s on the same hook |
| Meta Reels ads maximum length | Most guides: 90 s | Some 2026 guides claim up to 15 min for IG Reels ads; organic Reels up to 20 min for some accounts | Plan 15 to 30 s; treat 90 s as the safe ceiling; verify in Ads Manager |
| Shorts safe zone | Google-attributed template: 288 top, 672 bottom, 48 left, 192 right | Measured previews: 241, 381, 60, 201 | Use the stricter union for text |
| Social loudness | -14 LUFS works everywhere because platforms normalize near it | TikTok and Instagram reward louder mixes (-12 to -10 LUFS) | -14 default; test louder only if hook rate suffers |
| TikTok AIGC rule date | Agency blogs cite an effective date of 2026-07-21 | TikTok's 2026 ad policy changelog shows no AIGC change | Comply now regardless of the date |
| Meta third-party AI label date | Meta Help Center: 2026-06-01 | Some blogs: 2026-07 | Assume labels are live |
| Hawaii law | Kelley Drye and Bloomberg Law: enacted 2026-07 | A 2026-09 alert calls California the second state | Treat Hawaii like New York |
| Eleven Music for ads | Music terms permit online commercial use on self-serve plans | ElevenCreative page lists advertising as needing an additional license | Get written confirmation or use Enterprise or a library |
| Remotion vs HyperFrames for agents | Remotion is mature, has Lambda, React ecosystem | HyperFrames is HTML (easier for agents), Apache 2.0, no build step | HyperFrames default; Remotion when the project already uses it |
| GPT Image 2 pricing structure | Per resolution tiers (0.03 to 0.08 USD) | Per quality tiers at fixed size | Check OpenAI pricing before budgeting |

## What top operators do differently

1. **They separate taste from labor.** Two or three human decisions per batch (message, treatment, stills, final) and machine production for everything else, so output looks deliberate and volume stays high.
2. **They template the repeatable and film the proof.** Offer videos, end cards, review cards, UI walkthroughs and hook packs are templates; customer, founder and product proof is filmed once and reused across many hooks.
3. **They keep a footage bin and a hook bank.** Every shoot yields 10 or more hook takes and b-roll that feed months of iterations.
4. **They iterate from the retention curve, not from opinions.** "Keep the first 2 seconds, change the second half" for late cliffs; new hooks on the same body for early drop-offs.
5. **They make variety a checked rule.** A ledger of styles, opening shots, talent and visual worlds prevents the account from collapsing into one look (which delivery systems may treat as one ad).
6. **They use AI where it is invisible or honest.** Settings, b-roll, localization, scratch voices, cheap first-frame tests; disclosed presenters for explainers; never fake customers.
7. **They budget generation like media.** Caps, stills before video, draft tiers, reroll rates and logs per shot.
8. **They name everything for analysis.** Ad names that parse, registry rows with claims, licenses and releases, manifests with label settings and offer end dates.
9. **They treat music and likeness as legal assets.** License logs per file, release IDs per person, expiries tracked.
10. **They verify specs in live previews** each quarter and after platform UI changes, instead of trusting spec blogs.

## Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|-----------|
| AI "customers" giving testimonials | FTC penalties up to 53,088 USD per violation, platform rejections, trust loss | Actors are actors; real customers for testimonials |
| Unlicensed music in ads or directed influencer posts | Lawsuits with statutory exposure (Kroger case cites up to about 58.8M USD theoretical) | Library licenses, license log per file |
| Text and CTAs under the platform UI | Lower CTR, invisible offers | Safe zone overlays at hook, captions, offer, end card |
| One 16:9 master cropped automatically everywhere | Cut-off products and text, weak native fit | Ratio plan per placement; 9:16 and 4:5 siblings |
| Logo or slow intro in the first seconds | Low hook rate | Product or problem by 2 s |
| Testing many variables at once | No learning | One variable family per test |
| Unparseable names | No concept-level analysis | Grammar validation before delivery |
| Generated product shots that change the product | Returns, complaints, EU deep fake labels, misrepresentation | Composite real product photos |
| Building on a deprecated model (Sora 2) | Broken pipelines | Freshness checks; abstraction via aggregators |
| Uncapped generation rerolls | Budget overruns | Caps, stills first, logs |
| Countdown or scarcity that is not real | Consumer law and policy violations | Real deadlines, offer end date in the manifest |
| Stripping C2PA or watermarks to avoid labels | Detection, policy and trust risk | Keep provenance; disclose |

## Benchmarks

| Benchmark | Value | Source and date | Sample and caveat |
|-----------|-------|-----------------|-------------------|
| Top CTR TikTok videos showing key message or product in first 3 s | 63 percent | TikTok internal research cited by Vericast, 2022 | Internal, correlational, old |
| Reels with visual plus sound opening, top 20 percent purchase intent | 1.5x likelihood | Meta with Toluna, reported 2025 | Exploratory ranking analysis |
| Product shown more than once in Reels | 2.7x purchase intent likelihood | Same | Same |
| Music or voiceover in Reels ads | Up to 13 percent higher incremental conversions | Meta hook guidance, 2025 | "Up to"; mix unknown |
| Instagram Reels views with sound on | Over 75 percent | Meta for Developers, 2024-11 | Organic |
| Reels ads vs image ads | About double Reels delivery, 34.5 percent lower cost per result (another source cites 15 percent) | Meta Reels ads page, 15 A/B tests 2022-05 to 2023-04 | Bundled creative changes [Contested figure] |
| Vertical assets on Shorts | 10 to 20 percent more conversions per dollar | Google, 2022 | Pre Demand Gen |
| Wolt brand at 4 s vs 9 s on Shorts | About 75 percent more unique users, 5.86 percent consideration lift; late arm 15 percent lower CPV | Google case study | One brand |
| ABCD adherence | About 30 percent higher short-term sales likelihood, 17 percent long-term brand contribution | Google with Kantar, about 2021 to 2022 | Modeled by Kantar AI on about 11,000 ads |
| Human vs AI 30 s ads | Human 14 percent stronger short term, 17 percent long term | Ipsos and Syracuse, 2026-05 | 20 ads, 3,000 US consumers; AI versions via Sora 2 |
| Executives vs young consumers positive on AI ads | 82 percent vs 45 percent | IAB, 2026-01 | 505 consumers, 104 executives, US |
| Ads made with generative AI in Kantar testing | 54th percentile vs 65th without | Kantar via secondary, 2026 | Database average |
| Avatar API cost | About 0.05 USD per second (HeyGen Avatar IV) | HeyGen docs via secondary, 2026 | Enterprise credit price basis |
| Remotion Lambda render | About 0.017 to 0.021 USD per 1 min video | Remotion docs, v4.0.381 | 2048 MB, us-east-1, plus S3 and license |
| Transcription | 0.21 to 0.29 USD per audio hour | AssemblyAI, ElevenLabs, Deepgram, 2026 | Batch rates |

Benchmarks vary by vertical, geo, season and account. Compare against the account's own history first.

## Tools, APIs and MCP servers

| Tool | Type | Status (2026-10) | Agent use |
|------|------|------------------|-----------|
| HyperFrames CLI and skills | Open source (Apache 2.0) | 0.8.142; skills via `npx skills add heygen-com/hyperframes`; Lambda and HeyGen cloud render | Code-driven ad templates, captions, transcription, background removal |
| Remotion and skills | Source-available, licensed | 4.0.534; `npx skills add remotion-dev/skills`; Lambda | React pipelines, Automators license for automation |
| FFmpeg 6 to 8 | Open source | 8.0 adds whisper filter | Editing, delivery, QA |
| fal | Aggregator API and hosted MCP | 1,000+ models; queue API | Veo, Kling, Seedance, Nano Banana, FLUX, Bria mattes |
| Replicate | Aggregator API, official MCP reported | Cloudflare owned since 2025-12-01 | Model runs |
| Gemini API and Vertex AI | Official API | Veo 3.1 family, Nano Banana 2 and Pro | Video and image generation |
| Runway API and MCP | Official API and hosted MCP (2026-05-27) | Gen-4.5, Aleph 2.0, Act-Two plus third-party models | Generation and video editing |
| HeyGen API and MCP | Official API; MCP repo in early development; remote OAuth MCP described | Avatar IV and V, consent API | Disclosed presenters, translation |
| ElevenLabs API and MCP | Official | TTS, cloning with consent, music, Scribe | Voice, music, transcription |
| AssemblyAI, Deepgram | APIs | Universal-3.5 Pro (2026-09-22), Nova-3 | Word timestamps |
| Platform native (Meta Advantage+ creative, TikTok Symphony, Google Asset Studio) | In-platform | Generally available features vary | Operated by channel agents |

## Official sources to monitor

| Source | What to watch |
|--------|---------------|
| github.com/heygen-com/hyperframes (README, docs, releases), npm `hyperframes` | CLI changes, skills, license |
| remotion.dev/docs/terms, Remotion LICENSE.md, npm `remotion` | Remotion 5.0 license changes, pricing |
| ai.google.dev pricing and model docs; Google blog (Veo, Flow, Nano Banana) | Prices, deprecations, new Veo versions |
| fal.ai model pages and pricing; Runway API docs; Kling and BytePlus pricing; Luma, MiniMax, Pika docs | Prices, durations, face policies, availability |
| OpenAI platform deprecations | Image model pricing and any new video API |
| developers.heygen.com (pricing, consent), Synthesia pricing, elevenlabs.io terms and pricing | Avatar and voice rates, consent flows, music scope |
| Epidemic Sound and Artlist plan pages | Paid ads and broadcast coverage, caps |
| Meta Ads Guide and Business Help Center (AI labels, safe zones), TikTok Ads Help (specs, creative best practices, ad policy), Google Ads Help (video formats, Shorts, Demand Gen, AI labeling 17257106), LinkedIn ad specs | Specs, overlays, label rules |
| digital-strategy.ec.europa.eu (Article 50 code, guidelines, FAQ), EUR-Lex | EU disclosure duties |
| New York GBL 396-b, Hawaii legislature, California SB 1050, FTC press releases and Federal Register | US disclosure and testimonial enforcement |
| ASA (UK) rulings, national ad regulators | Filtered beauty, AI imagery rulings |

## Open questions and watch list

1. Remotion 5.0 license changes: timing and terms for agents and automations.
2. Kling 4.0 general availability, pricing and API terms (announced for 2026-10).
3. Veo successor (no official Veo 4 as of 2026-10; several third-party pages claim one).
4. Meta Reels ads maximum duration and whether 1440 x 2560 becomes the recommended upload size.
5. Final YouTube Shorts ad safe zone values from Google's template.
6. Enforcement of New York's synthetic performer law (first complaints reported) and the federal executive order's effect on state AI laws.
7. EU national enforcement practice for Article 50 in advertising; adoption of the EU label icons.
8. ElevenLabs written position on Eleven Music for paid advertising on self-serve plans.
9. Whether Meta's Muse Image reaches Advantage+ creative and how its labels behave.
10. HyperFrames stability (very fast release cadence; pin versions per template).
11. Consumer sentiment trend toward AI ads in 2027 (IAB, Ipsos follow-ups).
12. FTC first civil penalty cases under 16 CFR 465 (unverified reports of 2026-04 settlements).

## Sources

1. saas-motion-kit (README, playbook, creative, components, templates, skill). tugrawork-creator. https://github.com/tugrawork-creator/saas-motion-kit . v1.4, 2026.
2. HyperFrames README. HeyGen. https://github.com/heygen-com/hyperframes . Accessed 2026-10-08.
3. HyperFrames CLI reference. HeyGen. https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx . Accessed 2026-10-08.
4. hyperframes (npm package). npm. https://www.npmjs.com/package/hyperframes . 0.8.142, 2026-10-08.
5. HeyGen HyperFrames release. ai-tldr.dev. https://ai-tldr.dev/releases/heygen-hyperframes/ . 2026.
6. HyperFrames: an open-source rendering framework for generating video with HTML. silenceper. https://silenceper.com/en/article/2026-05-02-hyperframes-html-video-rendering/ . 2026-05-02.
7. HyperFrames review. andrew.ooo. https://andrew.ooo/posts/hyperframes-heygen-html-video-agents-review/ . 2026.
8. Remotion License. Remotion. https://github.com/remotion-dev/remotion/blob/main/LICENSE.md . 2026.
9. Terms and Conditions of Remotion (v5.0). Remotion. https://www.remotion.dev/docs/terms . 2026.
10. How much does Remotion Lambda cost? Remotion. https://www.remotion.dev/docs/lambda/cost-example . 2026.
11. Flickering. Remotion. https://www.remotion.dev/docs/flickering . Current.
12. createTikTokStyleCaptions(). Remotion. https://www.remotion.dev/docs/captions/create-tiktok-style-captions . Current.
13. Agent Skills. Remotion. https://www.remotion.dev/docs/ai/skills . Current.
14. npm registry entries (remotion, @motion-canvas/core, @canvas-commons/core, @revideo/core). npm. https://registry.npmjs.org/ . Read 2026-10-08.
15. Gemini Developer API pricing. Google. https://ai.google.dev/gemini-api/docs/pricing . Via secondary 2026-09.
16. Veo 3.1 pricing. Magic Hour. https://magichour.ai/blog/veo-3-pricing . 2026.
17. Veo 3.1 Ingredients to Video. Google. https://blog.google/innovation-and-ai/technology/ai/veo-3-1-ingredients-to-video/ . 2026-01.
18. Google's update for Veo 3.1 lets users create vertical videos. TechCrunch. https://www.techcrunch.com/2026/01/13/googles-update-for-veo-3-1-lets-users-create-vertical-videos-through-reference-images/ . 2026-01-13.
19. Flow updates. Google. https://blog.google/innovation-and-ai/models-and-research/google-labs/flow-updates-february-2026/ . 2026-02.
20. Google opens SynthID AI media verification site to everyone. Dataconomy. https://dataconomy.com/2026/10/08/google-synthid-ai-media-verification-site/ . 2026-10-08.
21. Is the Sora2 API still working? OpenAI Developer Community. https://community.openai.com/t/is-the-sora2-api-still-working/1379946 . 2026.
22. Sora 2: what it was, why it ended. invideo. https://invideo.io/blog/sora-ai-video-generator/ . 2026-08.
23. Sora API shutdown alternatives. Spheron. https://www.spheron.network/blog/sora-2-api-shutdown-2026-self-hosted-video-alternatives/ . 2026.
24. Kling O3 image to video. fal. https://fal.ai/models/fal-ai/kling-video/o3/standard/image-to-video . 2026.
25. Kling AI pricing in 2026. CloudZero. https://www.cloudzero.com/blog/kling-ai-pricing/ . 2026.
26. Kling 3.0 review. Atlas Cloud. https://www.atlascloud.ai/blog/guides/kling-3.0-review-features-pricing-ai-alternatives . 2026.
27. Kling v3 vs O3. Picsart. https://picsart.com/blog/kling-v3-vs-o3/ . 2026.
28. Kuaishou's AI video spinoff unveils new model in ByteDance chase. Bloomberg. https://www.bloomberg.com/news/articles/2026-09-28/kuaishou-s-ai-video-spinoff-unveils-new-model-in-bytedance-chase . 2026-09-28.
29. Shengshu Technology launches Vidu Q4 Preview. GlobeNewswire. https://www.globenewswire.com/news-release/2026/10/07/3376813/0/en/shengshu-technology-launches-vidu-q4-preview-a-next-generation-ai-video-model-built-for-lifelike-performances.html . 2026-10-07.
30. Seedance 2.0 API guide. SeeGen. https://seegen.ai/blog/seedance-2-0-api . 2026.
31. Seedance 2.0 API pricing 2026. Anikuku. https://anikuku.com/blog/seedance-2-api-pricing-guide-2026 . 2026-09.
32. ByteDance responds to copyright infringement concerns with Seedance 2.0. NBC News. https://www.nbcnews.com/tech/tech-news/seedance-2-bytedance-copyright-infringement-concerns-hollywood-rcna259173 . 2026-02.
33. Transforming video creation with TikTok Symphony and Dreamina Seedance 2.5. TikTok for Business. https://ads.tiktok.com/business/en/blog/transforming-video-creation-tiktok-symphony-dreamina-seedance . 2026-08-03.
34. API pricing and costs. Runway. https://docs.dev.runwayml.com/guides/pricing/ . 2026.
35. Runway opens MCP server for ChatGPT, Claude, Cursor, Replit. AI Weekly. https://aiweekly.co/alerts/runway-opens-mcp-server-for-chatgpt-claude-cursor-replit . 2026-05.
36. Luma AI pricing 2026. WaveSpeed. https://wavespeed.ai/blog/cost-and-billing/luma-ai-pricing/ . 2026-10.
37. Hailuo 2.3. OpenRouter. https://openrouter.ai/minimax/hailuo-2.3 . 2026.
38. MiniMax H3. OpenRouter. https://openrouter.ai/minimax/hailuo-3 . 2026.
39. Pricing. Pika. https://dev.pika.art/pricing . 2026.
40. AI video model release tracker 2026. Magic Hour. https://magichour.ai/blog/ai-video-model-release-tracker-2026 . 2026.
41. Nano Banana pricing 2026. Virse. https://www.virse.ai/blog/nano-banana-pricing . 2026-09.
42. Gemini 3.1 Flash Image. Google AI for Developers. https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-image . 2026.
43. Nano Banana 2 makes edits easier and faster. DeepLearning.AI. https://charonhub.deeplearning.ai/nano-banana-2-aka-gemini-3-1-flash-image-makes-edits-easier-and-faster/ . 2026-02.
44. GPT Image 2 vs Nano Banana 2. Evolink. https://evolink.ai/blog/gpt-image-2-vs-nano-banana-2-2026 . 2026-08.
45. FLUX.2 Pro. OpenRouter. https://openrouter.ai/black-forest-labs/flux.2-pro . 2026.
46. Midjourney review 2026. Javis Review. https://javisreview.com/review/midjourney-review-2026/ . 2026.
47. Ideogram 3.0. Ideogram. https://ideogram.ai/models/3.0/ . Current.
48. Enterprise pricing. HeyGen. https://developers.heygen.com/docs/enterprise-pricing . 2026.
49. Avatar consent. HeyGen. https://developers.heygen.com/docs/avatar-consent . 2026.
50. HeyGen API pricing explained. Realtime Avatar Blog. https://realtimeavatar.ai/blog/heygen-api-pricing-explained . 2026.
51. API pricing. ElevenLabs. https://elevenlabs.io/pricing/api . 2026.
52. Eleven Music model-specific terms. ElevenLabs. https://elevenlabs.io/eleven-music-model-specific-terms . 2026.
53. Synthesia pricing. G2. https://www.g2.com/products/synthesia/pricing . 2026.
54. Arcads AI pricing. eesel. https://www.eesel.ai/blog/arcads-ai-pricing . 2026.
55. UMG sues Quince over unlicensed music in TikTok posts. Music Business Worldwide. https://www.musicbusinessworldwide.com/fashion-brand-quince-recently-valued-at-10b-sued-by-umg-over-unlicensed-use-of-music-from-sabrina-carpenter-justin-bieber-billie-eilish-and-more-in-tiktok-posts/ . 2026-04.
56. Sony Music sues Kroger. Digital Music News. https://www.digitalmusicnews.com/2026/08/24/sony-music-kroger-lawsuit/ . 2026-08-24.
57. Crumbl settles Warner Music copyright suit over social media ads. Bloomberg Law. https://news.bloomberglaw.com/ip-law/crumbl-settles-warner-music-copyright-suit-over-social-media-ads . 2026-05.
58. DSW reaches settlement in principle with Sony Music. Music Business Worldwide. https://www.musicbusinessworldwide.com/dsw-reaches-settlement-in-principle-with-sony-music-over-music-used-in-social-media-ads/ . 2026-08.
59. FFmpeg whisper filter source. FFmpeg. https://ffmpeg.org/doxygen/8.0/af__whisper_8c_source.html . 2025-08.
60. FFmpeg 8.0 integrates Whisper. heise. https://www.heise.de/en/news/FFmpeg-8-0-integrates-Whisper-Local-audio-transcription-without-the-cloud-10522091.html . 2025-08.
61. WhisperX: time-accurate speech transcription of long-form audio. arXiv. https://arxiv.org/abs/2303.00747 . 2023.
62. AssemblyAI pricing. AssemblyAI. https://www.assemblyai.com/pricing.md . 2026-09.
63. Business plan. Epidemic Sound. https://www.epidemicsound.com/our-plans/business-plan/ . 2026.
64. Pricing. Artlist. https://artlist.io/page/pricing . 2026.
65. Meta Reels ad specs 2026. Cinerads. https://www.cinerads.com/blog/meta-ads-video-creative-best-practices . 2026.
66. Meta ads safe zones: 2026 unified creative updates. Billo. https://billo.app/blog/meta-ads-safe-zones . 2026-03.
67. Meta video ad length requirements. Jon Loomer Digital. https://www.jonloomer.com/meta-video-ad-length-requirements/ . 2025 to 2026.
68. Instagram and Facebook Reels ads. Meta. https://www.facebook.com/business/ads/facebook-instagram-reels-ads . Current.
69. Unlock the power of Reels ads. Meta for Developers. https://developers.facebook.com/blog/post/2024/11/07/unlock-the-power-of-reel-ads/ . 2024-11.
70. Want Reels ads that actually work? Meta revealed the playbook. Best Media Info. https://bestmediainfo.com/insights/want-reels-ads-that-actually-work-meta-just-revealed-the-playbook-10866888 . 2025.
71. Meta shares tips on Reels hooks. Social Media Today. https://www.socialmediatoday.com/news/meta-shares-tips-on-reels-hooks-creative-diversification-in-ads-and-threa/808182/ . 2025.
72. Creative best practices for performance ads. TikTok Ads Help. https://ads.tiktok.com/help/article/creative-best-practices . Current.
73. Creative Codes. TikTok for Business. https://ads.tiktok.com/business/en/creative-codes . Current.
74. TikTok best practices. Vericast. https://vericast.com/wp-content/uploads/2022/09/Vericast-TikTok-Best-Practices-Vertical-CS0761-2022-09-8.5x11.pdf . 2022-09.
75. TikTok video ad specs 2026. Influencer Marketing Hub. https://influencermarketinghub.com/video-advertising/tiktok-video-ad-specs/ . 2026.
76. TikTok ad specs 2026: safe zones. TryMyPost. https://www.trymypost.com/blog/tiktok-ad-specs-2026-safe-zones . 2026.
77. Non-skippable in-stream ads. Google Ads Help. https://support.google.com/google-ads/answer/11462260 . Current.
78. Your guide to YouTube Shorts ads. Google Ads Help. https://support.google.com/google-ads/answer/16041697 . Current.
79. Demand Gen asset specifications. Google Ads Help. https://support.google.com/google-ads/answer/13704860 . Current.
80. Shorter video enhancements enabled for Demand Gen. PPC News Feed. https://ppcnewsfeed.com/ppc-news/2025-02/shorter-video-enhancements-automatically-enabled-for-demand-gen/ . 2025-02.
81. YouTube Shorts ad safe zones. adkit. https://adkit.so/tools/safe-zones/youtube . 2026-03.
82. ABCDs for Shorts one-sheet. Google. https://services.google.com/fh/files/misc/formarketingshortsabcdsonesheeters.pdf . 2023.
83. Wolt YouTube Shorts case study. Google. https://business.google.com/en-all/think/search-and-video/wolt-youtube-shorts/ . 2024.
84. Vertical video on YouTube. Google. https://blog.google/products/ads-commerce/vertical-video-youtube/ . 2022.
85. The ABCDs of effective video ads. YouTube. https://www.youtube.com/intl/en_ae/ads/abcds-of-effective-video-ads . Current.
86. Validating Google's ABCD framework with AI. Kantar. https://www.kantar.com/industries/technology-and-telecoms/validating-googles-abcd-framework-with-the-power-of-artificial-intelligence . n.d.
87. Create video ads for Classic ad sets. LinkedIn Help. https://www.linkedin.com/help/lms/answer/85304 . Current.
88. LinkedIn video ad specs. QuickFrame. https://quickframe.com/blog/linkedin-video-ad-specs . 2026.
89. Audio normalization: LUFS targets by platform. OpenClip. https://openclip.app/learn/audio-normalization . 2026.
90. Audio ads specs. Spotify Advertising. https://ads.spotify.com/en-NL/ad-experiences/audio-ads-specs . Current.
91. Recommended upload encoding settings. YouTube Help. https://support.google.com/youtube/answer/1722171 . Current.
92. EBU R128. EBU. https://tech.ebu.ch/publications/r128 . Current.
93. Loud commercials. FCC. https://www.fcc.gov/consumers/guides/loud-commercials . Current.
94. Regulation (EU) 2024/1689 (AI Act). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2024/1689/oj . 2024-07-12.
95. Code of Practice on transparency of AI-generated content. European Commission. https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content . 2026-06.
96. European Commission publishes final code of practice on marking and labelling AI-generated content. Legal 500. https://www.legal500.com/intelligence/european-union/technology/european-commission-publishes-final-code-of-practice-on-marking-and-labelling-ai-generated-content . 2026-06.
97. European Commission adopts final guidelines on Article 50. Bird and Bird. https://www.twobirds.com/en/insights/2026/european-commission-adopts-final-guidelines-on-ai-act-article-50-transparency-obligations-first-impr . 2026-07.
98. Commission confirms transparency code of practice as adequate and publishes final guidelines. Faegre Drinker. https://www.faegredrinker.com/en/insights/publications/2026/7/eu-ai-act-commission-confirms-transparency-code-of-practice-as-adequate-and-publishes-final-version-of-its-guidelines-on-transparency-obligations . 2026-07.
99. EU AI Act guidance expands AI disclosure rules for advertisers and PR teams. Davis+Gilbert. https://www.dglaw.com/eu-ai-act-guidance-expands-ai-disclosure-rules-for-advertisers-and-pr-teams/ . 2026.
100. Transparency obligations under Article 50 (FAQ). European Commission. https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act . 2026.
101. EU AI Omnibus enters into force. White and Case. https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act . 2026-07.
102. New York synthetic performer law: what advertisers need to know. Manatt. https://www.manatt.com/insights/newsletters/client-alert/new-york-synthetic-performer-law-what-advertisers-need-to-know . 2026.
103. New York enacts synthetic performer disclosure law. Cooley. https://www.cooley.com/news/insight/2026/2026-01-29-new-york-enacts-synthetic-performer-disclosure-law-for-advertisements-including-those-using-generative-ai . 2026-01-29.
104. California joins New York in requiring disclosure of synthetic performers. Manatt. https://www.manatt.com/insights/newsletters/client-alert/california-joins-new-york-in-requiring-disclosure-of-synthetic-performers-in-advertising . 2026-09.
105. California becomes the second state to enact a synthetic performer law. DLA Piper. https://www.dlapiper.com/en-us/insights/publications/2026/09/california-becomes-the-second-state-to-enact-a-synthetic-performer-law . 2026-09.
106. Hawaii enacts a synthetic performer law. Kelley Drye. https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/hawaii-enacts-a-synthetic-performer-law . 2026-07.
107. Two newly enacted New York laws will regulate certain AI-generated images. Skadden. https://www.skadden.com/insights/publications/2026/01/two-newly-enacted-new-york-laws-will-regulate . 2026-01.
108. FTC announces final rule banning fake reviews and testimonials. FTC. https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials . 2024-08-14.
109. FTC's Endorsement Guides: what people are asking. FTC. https://www.ftc.gov/business-guidance/resources/ftcs-endorsement-guides-what-people-are-asking . 2023.
110. FTC signals heightened enforcement of new consumer review rule. Venable. https://www.venable.com/insights/publications/2025/12/ftc-signals-heightened-enforcement-of-new . 2025-12.
111. FTC v. Colgate-Palmolive Co., 380 U.S. 374. Justia. https://supreme.justia.com/cases/federal/us/380/374/ . 1965.
112. Updates to AI labeling requirements. Google Advertising Policies Help. https://support.google.com/adspolicy/answer/17257106 . 2026-07.
113. How AI-generated images in ads are identified and labeled. Meta. https://www.meta.com/help/artificial-intelligence/355108217670024/ . Current.
114. Misleading and false content (ad policy). TikTok Ads Help. https://ads.tiktok.com/help/article/tiktok-ads-policy-misleading-and-false-content . 2026.
115. NIQ research uncovers hidden consumer attitudes toward AI-generated ads. NielsenIQ. https://nielseniq.com/global/en/news-center/2024/niq-research-uncovers-hidden-consumer-attitudes-toward-ai-generated-ads/ . 2024-12.
116. Newhouse research finds AI ads fall short on sales impact. Syracuse University. https://news.syr.edu/2026/05/18/newhouse-research-finds-ai-ads-fall-short-on-sales-impact/ . 2026-05-18.
117. The AI ad gap widens. IAB. https://www.iab.com/insights/the-ai-gap-widens/ . 2026-01.
118. Not lovin' it: McDonald's pulls AI-generated Christmas ad. NBC News. https://www.nbcnews.com/world/europe/mcdonalds-ai-generated-christmas-advert-social-media-backlash-rcna248590 . 2025-12.
119. Coca-Cola sparks backlash with AI-generated Christmas ad, again. Forbes. https://www.forbes.com/sites/danidiplacido/2025/11/04/coca-cola-sparks-backlash-with-ai-generated-christmas-ad-again/ . 2025-11-04.
120. Marketing AI report 2026. Canva. https://www.canva.com/newsroom/news/marketing-ai-report-2026/ . 2026.
121. AI characters vs UGC performance ads. Admiral Media. https://admiral.media/ai-characters-vs-ugc-performance-ads/ . 2026.
122. AI generated ads and UGC. RevenueCat. https://www.revenuecat.com/blog/growth/ad-generated-ads-ugc . 2026.
123. fal MCP server. fal. https://fal.ai/mcp . 2026.
124. HeyGen MCP server. HeyGen. https://docs.heygen.com/docs/heygen-mcp-server . 2026.
125. Introducing ElevenLabs MCP. ElevenLabs. https://elevenlabs.io/blog/introducing-elevenlabs-mcp . 2025.
126. Cloudflare Form 10-Q, Q1 2026. SEC. https://www.sec.gov/Archives/edgar/data/0001477333/000147733326000038/cloud-20260331.htm . 2026.
127. fal company profile. Sacra. https://sacra.com/c/fal-ai/ . 2026.
128. Three flashes or below threshold. W3C. https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html . Current.
