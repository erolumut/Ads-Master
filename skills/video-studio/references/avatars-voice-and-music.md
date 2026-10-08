# Avatars, Voice and Music

> Purpose: use AI avatars and synthetic voices where they help (explainers, localization, hook tests) without faking customers, and keep every second of audio licensed for paid ads. This is practical guidance, not legal advice; route edge cases to `compliance` and the human.

## 1. When an AI presenter is acceptable

```
Is the presenter presented as a customer, user, expert, employee or anyone with personal experience of the product?
  yes -> Do not use an AI presenter. Use the real person (with consent) or a labeled human actor.
  no  -> Is the presenter a digital twin of a real, identifiable person?
           yes -> Written consent (scope, channels, term, territories, revocation, pay) + platform consent flow
                  + disclosure in the ad ("AI-generated video of <name>; script approved by <name>").
           no  -> Synthetic performer. Disclose on screen near the performer (NY, Hawaii, California from 2027-01-01, EU).
                  Allowed jobs: explain, demonstrate the product UI, read the offer, localize.
```

Good jobs for AI presenters: B2B explainers and tutorials, app walkthroughs, localization of an approved human master, fast hook script tests where the presenter is clearly a presenter (not a customer), internal concept tests before paying creators.

Never: testimonials, "I tried this and..." scripts, before and after claims, doctors or other experts, children, impersonation of real people, sound-alike or look-alike of celebrities.

## 2. Avatar and AI UGC tools (2026-10)

| Tool | What it does | Price signal (source, date) | Consent and disclosure notes |
|------|--------------|-----------------------------|------------------------------|
| HeyGen | Stock avatars, Photo Avatars, Digital Twins (Avatar IV; "Avatar V" twin from about 15 s of footage), video translation and lip sync, API, MCP server, open-source LiveAvatar stack | API: Avatar IV about 0.1 credit per second at 0.50 USD per credit = about 0.05 USD per s (3 USD per minute); no free API credits since 2026-02; pay as you go wallet from 5 USD [Official developer docs via secondary, 2026] | Digital twins need a recorded consent video by the same person (hosted consent flow; upload or skip only for whitelisted Enterprise accounts with indemnity); photo and prompt avatars depict no identifiable person and need no consent [Official docs] |
| Synthesia | Studio avatars (Express-2: 1080p, 30 fps, hand and body movement), personal avatars, dubbing | Plans reported from about 29 USD to 89 USD per month; personal avatar add-on about 1,000 USD per year on monthly plans; API tier conflicts across sources [Contested, 2026] | Enterprise compliance focus; still disclose synthetic performers in ads |
| Arcads | AI "UGC actors" for ad scripts | No public price page in 2026-07; reported about 110 USD per month for 10 videos [secondary] | Actors look like customers: use only as clearly labeled presenters, never as testimonials; claims that actors are licensed real likenesses are unverified |
| Creatify | URL to video ads, avatars, batch variants | Free tier with watermark; paid from about 19 to 39 USD per month [Contested] | Same rules |
| Captions (Mirage) | AI editing, avatars, captions | From about 10 to 25 USD per month [secondary] | Same rules |
| TikTok Symphony | Stock and custom digital avatars, AI dubbing, Creative Studio | Inside TikTok for Business | Outputs carry AI labels, invisible watermark and C2PA |
| Runway Act-Two | Drives a character with a recorded performance | 0.05 USD per s [Runway API docs via secondary] | Consent of the driving performer |

Performance evidence is mixed and mostly vendor-reported: one agency reported AI characters winning 9 of 13 equal-budget tests with 17 to 29 percent lower CPA on its top winners; RevenueCat reported most synthetic avatars dropped early, one at 68 percent lower CTR than the human control because of a 0.2 s lip-sync lag, while a digital twin of a real employee reached 87 percent of the human conversion rate [Contested, 2026]. Test AI presenters against humans within the same concept before scaling, and watch comments for "AI" mentions.

## 3. Disclosure for synthetic performers

| Jurisdiction or platform | Rule | Practical wording |
|--------------------------|------|-------------------|
| New York GBL 396-b (effective 2026-06-09) | Conspicuous disclosure when an ad includes a synthetic performer and the producer has actual knowledge; applies where the ad is seen; 1,000 USD first violation, 5,000 USD after; audio-only and translation-only uses exempt | On screen near the performer: "AI-generated presenter" for the whole time the performer is on screen |
| Hawaii (enacted 2026-07, nearly identical to New York) | Same duty and carve-outs per Kelley Drye and Bloomberg Law [Contested: some 2026-09 alerts call California the second state] | Same as New York |
| California SB 1050 (signed 2026-09-16, effective 2027-01-01) | Clear and conspicuous disclosure near the performer when a synthetic performer is prominently featured, shown long enough to understand, wording substantially similar to "this performance features a synthetic digital performer"; covers audio-only ads; private actions possible | "This performance features a synthetic digital performer." on screen; spoken in audio-only ads |
| EU AI Act Article 50(4) (applies from 2026-08-02; final Commission guidelines 2026-07-20; code of practice 2026-06-10) | Deployers disclose deep fakes; a photorealistic image or video of an invented person counts; label perceivable without tools, at first exposure at the latest; commercial ads get the standard label, not the lighter artistic regime | Visible label from the first frame the performer appears: "AI-generated presenter" or the EU icon set from the code of practice, in the ad's language |
| FTC (US) | Endorsements must reflect real experience; fake or AI testimonials banned under 16 CFR 465 (civil penalties up to 53,088 USD per violation); actors portraying customers need disclosure | "Actor portrayal" or "AI-generated presenter, not a customer" |
| Meta, TikTok, Google | Meta "AI info" labels (own tools and detected third-party signals from 2026-06); TikTok requires the AIGC label or clear disclaimer on realistic AI ad content; Google lets advertisers add in-creative AI labels and uses an AI label setting (2026-07) | Keep platform labels on; add the in-video text above anyway |

Build to the strictest standard once (on-screen text near the performer for the whole appearance, plus spoken line in audio-only ads) and reuse it in every market. Keep the disclosure inside the safe zone and at least the size of body captions.

## 4. Digital twins of real people (founder, staff, creators)

1. Written release covering: likeness and voice, AI generation, channels (paid social, CTV), term, territories, script approval, revocation, compensation, data storage and deletion.
2. Platform consent flow completed by the person (for example the HeyGen consent video). Store the release ID in the registry (`talent_release_ids`).
3. The person approves every script that their twin speaks. No claims beyond what the person would say themselves.
4. Disclose in the ad (EU deep fake rule applies to a realistic synthetic version of a real person). New York's law targets non-identifiable synthetic performers, but disclosure is still the safe default.
5. Deceased persons: New York requires heirs or executors to consent to commercial digital replicas (companion law, 2025-12).
6. On revocation: pull every live ad with the twin within the agreed window; the channel agent pauses after human approval.

## 5. Voice

| Option | Use | Notes |
|--------|-----|-------|
| Human VO talent | Brand voice, CTV, premium | Buyout terms: media (paid social, online video, broadcast), term, territory; union contracts may apply (SAG-AFTRA commercials in the US) |
| Founder or staff voice | Authentic B2B and DTC | Record in a quiet room; lavalier or USB mic; 48 kHz |
| ElevenLabs TTS and voice library | Drafts, localization, scale | Commercial use on paid plans; cloning only with consent and verification; voice cloning of public figures prohibited [Official terms via secondary, 2026] |
| Cloned voice of a real person | Localization of an approved master | Written consent, scope and disclosure; some guides say Professional Voice Cloning only allows your own voice on your account [Unverified] |
| Local TTS (`npx hyperframes tts`) | Scratch tracks for timing | Replace before delivery unless the voice license allows ads |
| Platform dubbing (TikTok Symphony, HeyGen translation) | Fast localization | Native speaker review of claims and pronunciation |

VO direction checklist: conversational read at about 150 to 190 words per minute for social (faster for hooks) [Practitioner consensus]; brand and product names with a pronunciation guide; the hook line recorded 3 ways; CTA recorded with 3 offers if a CTA test is planned; room tone recorded for edits.

## 6. Music for paid ads

| Source | Paid social ads | Broadcast or CTV | Notes (source, date) |
|--------|-----------------|------------------|----------------------|
| Epidemic Sound Business | Covered (paid ads, influencer campaigns, social posts) | Not addressed on the Business page; third-party guides point TV and broadcast to Enterprise | Eligibility caps: brands under 10M USD annual revenue, agencies, publishers and production companies under 5M USD [Official plan page, 2026] |
| Artlist (Pro license, Teams) | Covered (paid ads, client work) | Broadcast and TV covered; standalone audio such as radio ads not covered | Songs downloaded during a paid subscription stay covered after it ends [Official pricing and blog, 2026] |
| TikTok Commercial Music Library | Covered on TikTok | No | Only for TikTok |
| Meta Sound Collection | Covered on Meta | No | Only for Meta |
| Eleven Music (ElevenLabs) | Self-serve paid plans: online and offline commercial use except film, TV, radio and studio games; the ElevenCreative page lists advertising among uses needing an additional license [Contested]; Enterprise covers all media | Enterprise only | Free tier has no commercial rights; prompts may not name artists, songs or lyrics [Official terms, 2026] |
| Meta MusicGen local weights | No | No | Weights are CC-BY-NC 4.0 (non-commercial): drafts only |
| Commissioned composer | Yes, with a written work-for-hire or license covering ads | Yes if the contract says so | Keep stems for cut-downs |
| Commercial songs (label catalog) | Only with sync (publisher) and master (label) licenses | Same | Platform UGC licenses never cover brand ads |

Why it matters: labels are suing brands over music in social marketing posts, including posts by paid influencers the brand directed. Examples: UMG, Capitol and Concord v. Quince (filed 2026-04, 67 recordings and 71 compositions listed); Sony v. Kroger (filed 2026-08-21, at least 392 uses, theoretical exposure about 58.8M USD); Sony v. DSW (2025-08, settlement in principle 2026-08); Warner v. Crumbl (2025-04, settled in principle 2026-05); Sony v. Marriott (settled 2024-10); Beastie Boys and UMG v. Chili's (settled 2025-05) [press and court filings via secondary, 2024 to 2026].

Music license log (one row per delivered file, stored in the batch output and the registry `music_license` column):

| Track | Source and license ID | Plan or contract | Covers paid ads | Covers territories | Covers broadcast | Downloaded on | Expiry or conditions |
|-------|----------------------|------------------|-----------------|-------------------|------------------|---------------|----------------------|

## 7. Sound design and mixing

- Pick or generate the music first for music-led edits, extract a beat grid (`npx hyperframes beats` or librosa), and cut on bars; put the reveal on the drop.
- SFX on product actions (click, pour, zip, tap) increase perceived quality; use licensed SFX libraries or record foley. Warm tuned sounds beat pure sine beeps (saas-motion-kit lesson).
- Voice first: music ducked 12 to 18 dB under voice; no music under legal lines.
- Final loudness per [Platform specs and safe zones](platform-specs-and-safe-zones.md) section 8; true peak at or below -1 dBTP for social.
- A cut to silence before the reveal is a strong pattern break; once per ad.
- Silent edits are valid for Feed and LinkedIn-first concepts, but still deliver a sound version for Reels and TikTok.

## 8. Avatar production workflow (disclosed presenter)

1. Confirm the job is allowed (section 1 decision tree) and log the decision in the brief card (`aiP` flag).
2. Script for a presenter, not a customer: "Here is how <product> does X", never "I used it and...". Run the claims through `brand/CLAIMS.md`.
3. Pick the avatar: stock or prompt avatar (no identifiable person) or a consented digital twin. Match age, register and setting to the persona without stereotyping.
4. Keep shots short (3 to 8 s per presenter shot) and cut away to real product or UI footage for every proof beat; lip-sync flaws show most on long close-ups.
5. Generate at 1080p or higher; check lip-sync on plosives and brand names; regenerate lines with lag (a 0.2 s lag cost one test 68 percent of CTR [vendor report, 2026]).
6. Add the disclosure text as a code-driven layer (stays sharp, survives re-edits) for the whole time the presenter is visible.
7. QA items F1, F2, F6 and F7 in the [QA checklist](qa-checklist.md); compliance packet lists the tool, the avatar type and the disclosure text per market.
8. Test against a human-presented version of the same concept before scaling.

## 9. Localization and dubbing workflow

| Step | Action | Owner |
|------|--------|-------|
| 1 | Freeze the master (picture lock) with text on separate layers and an approved SRT | video-studio |
| 2 | Native copywriter adapts hooks and on-screen text (adaptation, not translation); claims re-approved per market | creative-strategy, compliance |
| 3 | Voice: native human VO, or AI dubbing of the original speaker only with written consent covering dubbing and markets | video-studio, human |
| 4 | Lip-sync translation (HeyGen, Symphony) only for presenters or consented speakers; never on testimonials without the customer's consent to be dubbed | video-studio |
| 5 | Re-layout for text expansion; re-check safe zones per language | video-studio |
| 6 | Native reviewer watches every language version on a phone | human or market reviewer |
| 7 | Name with `Lxx` flag; registry rows per language | video-studio |

## 10. Voice casting and recording brief (template)

```
Voice brief: C0xx | <market>, <language>
Role: presenter | narrator | character (never "customer")
Voice: age range, energy (1 to 5), pace (words per minute), accent, warmth vs authority
Reference reads: links to approved brand videos (not other brands' ads)
Script: final, with pronunciation guide for brand, product and competitor-free terms
Deliverables: WAV 48 kHz 24-bit, 3 reads of each hook line, 2 full reads, 3 CTA variants, 10 s room tone
Usage: paid social and online video, <territories>, <term>, broadcast yes or no
Consent for AI use: none | dubbing only | voice clone (separate signed consent)
```

## 11. Music brief (template)

```
Music brief: C0xx
Mood and arc: <e.g. tense 0 to 4 s, lift on reveal at 4.5 s, warm resolve for CTA>
Tempo: <BPM range>; cut points on bars; drop at <time>
Instrumentation: <acoustic, electronic, percussion only>; avoid: <vocals, trending sound-alikes>
Length: 15 s and 30 s edits (stems preferred)
License needed: paid social in <territories>; broadcast <yes or no>; term <months>
Library search terms: <3 to 5 terms>
Fallback: silent edit with SFX only for Feed and LinkedIn
```
