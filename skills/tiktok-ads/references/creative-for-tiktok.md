# Creative for TikTok

> Knowledge as of 2026-10. On TikTok, creative is the targeting, the bid lever and the main cause of both scale and decay. This module covers native production rules, hooks, sound, testing, fatigue and refresh, AI creative (Symphony) and labeling. Spark Ads and creator sourcing live in spark-ads-and-creators.md. Hand cross-channel concept work to the creative-strategy agent.

## 1. What "native" means on TikTok

| Rule | Detail | Why |
|------|--------|-----|
| Vertical 9:16, full screen | 1080x1920 recommended; never letterboxed 16:9 or 1:1 | Non-native framing signals "ad" and loses the thumb-stop |
| Sound on by design | Voiceover, dialogue or a sound that carries the story. TikTok's sound studies have long reported that most users consider sound essential to the experience [Unverified figure, TikTok Marketing Science 2021] | TikTok is a sound-on platform; silent ads underperform |
| Person on camera in the first second | Face, hands with product, or a creator talking to camera | Human presence is the most consistent stop signal [Practitioner consensus] |
| Lo-fi but clear | Phone-shot look, good light, clean audio, readable captions | Polished TV spots read as interruptions |
| Hook in the first 1 to 3 seconds | Lead with the problem, result, claim or pattern break | TikTok guidance has long stated that the top CTR ads show the key message or product in the first 3 seconds [Unverified figure, TikTok creative guidance 2021/2022] |
| Captions and on-screen text inside safe zones | Keep text away from the right rail (icons), bottom caption area and top bar | UI overlays cover text; use the Creative Center safe zone guide |
| Length | 9 to 34 seconds for most performance ads; TikTok has recommended 21 to 34 seconds for In-Feed conversions in older guidance [Unverified] | Long enough to show demo and proof, short enough to hold |
| One idea per ad | One problem, one product, one CTA | Multi-message ads lose hold rate |
| Music from the Commercial Music Library (CML) or original audio | Business accounts and ads must use licensed audio. Music Autofix detects music that cannot be used [Official, 2026-05] | Unlicensed music causes rejections or muting |

Specs to confirm in the Ads Manager upload screen: file types (MP4, MOV and others), size limit, minimum resolution, ad text length, and display name rules. These change and differ for Spark Ads.

## 2. Hook library (first 1 to 3 seconds)

| Hook type | Template | Works for |
|-----------|----------|-----------|
| Callout | "If you [specific situation], stop scrolling." | Niche audiences, B2B roles, local |
| Problem agitation | "My [problem] was so bad I [consequence]." | Health-adjacent (within policy), beauty, home |
| Result first | Show the end state, then "Here's how." | Cleaning, beauty, fitness gear, software dashboards |
| Contrarian | "Stop buying [category]. Do this instead." | Crowded categories |
| Social proof | "This has [N] reviews and here's why." (only true numbers) | Products with proof |
| Unboxing / ASMR | Satisfying open, pour, click, peel in silence then voice | Physical products |
| Comparison | Side by side vs the usual alternative | Products with visible difference |
| Question | "Why does nobody talk about [thing]?" | Education, finance (within policy) |
| Reply to comment | Green screen a real comment and answer it | Objection handling, Spark Ads on organic posts |
| Founder POV | "I started this company because..." | DTC brands with a story |
| "TikTok made me buy it" / haul | Creator lists items with honest reactions | TikTok Shop, affiliates |
| Stitch-style reaction | React to a trend or claim | Brands with personality |

Write 3 to 5 hooks per concept. Hooks are the cheapest variable to iterate and the most predictive of scale.

## 3. Body structures that convert

1. Problem -> agitation -> product as solution -> demo -> proof -> offer -> CTA.
2. Hook -> "3 reasons why" -> CTA.
3. Before/after process (not for weight loss or restricted categories; see policy-and-account-health.md) -> how it works -> CTA.
4. Day-in-the-life with natural product use -> reveal -> CTA.
5. Objection list: "You're probably thinking..." -> answer each -> CTA.
6. Expert or creator explainer -> demo -> CTA.
7. Live shopping clip: host demo with price and urgency (Shop sellers; Video-to-LIVE).

CTA rules: say it and show it ("Tap Shop now to get the bundle"). Match the CTA button to the destination. For TikTok Shop, point to the product card or LIVE.

## 4. Creative diagnostics metrics

| Metric | Formula (from Ads Manager columns) | Diagnoses |
|--------|-----------------------------------|-----------|
| Hook rate (2s view rate) | 2-second video views / impressions | Opening seconds and thumbnail frame |
| 6s view rate (focused view rate) | 6-second video views / impressions | Whether the first beat earns attention; EVTA uses a 6s threshold [Official] |
| Hold rate | 6-second views / 2-second views | Whether the hook pays off |
| Average watch time and completion | Average play time, 100% views / impressions | Story pacing |
| CTR (destination) | Clicks / impressions | Offer and CTA clarity |
| CVR | Conversions / clicks | Landing page or Shop listing fit (hand to cro if low) |
| CPM | Cost / impressions x 1,000 | Auction pressure and creative quality signal |
| Cost per 1,000 reached and frequency | Reach columns | Fatigue |

Diagnostic grid:

| Hook rate | Hold rate | CTR | CVR | Read | Action |
|-----------|-----------|-----|-----|------|--------|
| Low | n/a | Low | n/a | Opening fails | New hooks on same body |
| High | Low | Low | n/a | Hook over-promises or body drags | Tighten body, show product earlier |
| High | High | Low | n/a | Entertaining but no reason to act | Stronger offer, clearer CTA, product earlier |
| High | High | High | Low | Click intent but page or listing fails | Landing page or listing check (cro, commerce-feeds) |
| High | High | High | High | Winner | Iterate hooks, scale, Spark it |

Use the account's own percentiles as thresholds (top quartile = good) rather than external averages. See benchmarks.md for how to build them.

## 5. Creative testing system

### 5.1 Definitions
- Concept: a distinct angle or idea (problem, audience, promise). New concepts find new pockets of buyers.
- Iteration: same concept, new hook, new creator, new format.
- Variation: same video, different first frame, text overlay, length or CTA.

Spend mix target at Growth tier and above: about 50% of new creative slots on new concepts, 35% on iterations of winners, 15% on variations [Practitioner consensus].

### 5.2 Testing structure options

| Option | Setup | Pros | Cons |
|--------|-------|------|------|
| Manual testing campaign | ABO, 1 ad group per batch of 3 to 5 creatives, broad, Maximum Delivery, same optimization event as scaling | Each batch gets spend; clean reads | Learning cost per batch |
| Smart+ asset groups | One asset group per concept, creative module manual | Matches how scaling campaigns behave | System concentrates spend on early leaders; losers get little spend |
| Split Test | Ads Manager split test for two creative strategies | Statistically clean | Needs budget and time; tests strategies, not 20 ads |

Graduation rule: an ad that hits the scaling threshold in testing (section 5.3) gets added to the Smart+ scaling campaign as a new ad, or via the Spark Ads code of its organic post, without pausing it in testing for 3 days.

### 5.3 Kill, keep, scale thresholds (Ads Master defaults, tune per account)

| Decision | Rule |
|----------|------|
| Kill early | Spend at least 1x target CPA, zero conversions, and hook rate in the bottom quartile of the account |
| Kill | Spend 2x to 3x target CPA with zero conversions, or CPA above 1.5x target after 3x target CPA spend |
| Keep | CPA within 1.2x target with at least 3 conversions |
| Scale | CPA at or below 0.8x target with at least 10 conversions in 7 days, or ROAS at or above 1.2x target with stable CVR |

These are house rules, not TikTok guidance. Calibrate with the project's own history and record changes in memory.

## 6. Creative fatigue and refresh cadence

TikTok audiences see far more content per session than on other platforms, and operators widely report that individual ads decay faster than on Meta [Practitioner consensus; no official decay curve found this cycle].

Fatigue signals (check weekly, daily at Scale tier):
1. CTR down 20% or more vs the ad's first 7 days at similar spend.
2. 6s view rate down 15% or more vs its first 7 days.
3. CPM up while CTR down (auction penalizes declining engagement).
4. Frequency above 3 per 7 days on a limited audience.
5. Comments turning negative or repetitive on a Spark Ad.

Refresh cadence (Ads Master defaults):

| Tier | New ads per week | New concepts per month | Notes |
|------|-----------------|-----------------------|-------|
| Starter (under $3k) | 2 to 3 | 2 to 4 | Iterate hooks on the best 1 or 2 concepts; Symphony for variations |
| Growth ($3k to $30k) | 5 to 10 | 6 to 10 | 2 to 4 creators on retainer, affiliate content for Shop |
| Scale ($30k to $300k) | 15 to 40 | 15 to 30 | Creator network via TikTok One, in-house editor, weekly creative review |
| Enterprise (over $300k) | 40+ | 30+ per market | Localization per market, Custom Creator Networks where available |

Smart+ Auto-add can introduce fresh creative after launch to reduce fatigue [Official, 2026]. Use it only with an approved asset library so nothing off-brand ships.

## 7. Creative research sources

| Source | Use |
|--------|-----|
| TikTok Creative Center: Top Ads | Filter by region, industry, objective and period to see top ads and their CTR-style performance signals [Official] |
| Creative Center: Keyword Insights | Phrases and keywords that appear in high-performing ads; feeds hooks and Search Ads keywords |
| Creative Center: Trend Discovery (hashtags, songs, creators, videos) | Trending sounds and formats by region |
| Commercial Music Library | Licensed tracks for ads |
| Symphony Assistant | Research and script generation inside Creative Center; separate from Symphony Agent [Official] |
| TikTok Ads Library / Commercial Content Library (EU DSA) | Competitor ads served in the EU, with targeting and reach details [Official] |
| TikTok search bar and comments | Voice of customer and objections in users' own words |
| Your own top organic posts | The best Spark Ads candidates |

## 8. Symphony and AI creative (2025 to 2026)

| Tool | What it does | Date | Label |
|------|-------------|------|-------|
| Symphony Creative Studio | Generates videos from product info or URL, AI dubbing, digital avatars; rebuilt on ByteDance Dreamina Seedance 2.0 with text-to-video, image-to-video (up to 4 reference images) and reference-to-video modes | Rebuild 2026-05-13 | [Official, 2026-05] |
| Voiceover Avatars | Stock, licensed real-actor avatars speaking 30+ languages; non-exclusive (a competitor can use the same face) | 2026 | [Unverified, third-party guide] |
| Product Avatars | Avatar holds or shows an uploaded product or app screen image; some apparel accessories unsupported | 2026 | [Unverified] |
| Custom Avatars | Only sanctioned route for a real person's likeness; the person verifies identity on camera and records consent | 2026 | [Unverified] |
| Symphony Agent | Agentic ad creation across Creative Studio, Content Suite and TikTok One; analyzes trends, drafts videos from prompts, images or example videos | Cannes, 2026-06-22 | [Official, 2026-06] |
| Seedance 2.5 in Symphony | Newer video model | Reported 2026-08 | [Unverified] |
| Smart+ creative generation | Generates TikTok-ready videos from a product URL inside Smart+; Catalog Image and Video Auto-Crawl | 2025-10 to 2026-07 | [Official] |

How to use AI creative without hurting performance or trust:
1. Use AI for variations (new hooks, dubbing into new languages, resizing, caption removal), not as a replacement for real people demonstrating real products.
2. Never use an avatar to fake a customer testimonial or an expert endorsement. That is deceptive and violates ad policy.
3. Test AI variants against the human original in the same ad group; keep only those within 10% of the original's CPA.
4. Keep the AI-generated label. Symphony output carries AI labels and invisible watermarks [Official, 2026-06]. Disclose AI-generated realistic content you produce outside Symphony using the AI-generated content disclosure in the ad or post flow [Unverified for exact toggle name].
5. Users and creators can decline Dreamina-generated videos in some contexts [Unverified]; never use a creator's likeness or voice without a written license.

## 9. Brief template (send to creators or the creative-strategy agent)

```
Product / offer:
Audience segment and awareness level (from AUDIENCE.md):
Concept ID and angle:
Hook options (write 3 to 5, the first 3 seconds):
Must show: product in hand by second 3, the key demo, the proof point
Must say: claim wording approved in BRAND.md (exact text)
Must not say or show: forbidden claims, before/after, competitor names, unlicensed music
Format: 9:16, 15 to 35 s, sound on, captions burned in, safe zones respected
CTA (spoken and on screen):
Deliverables: 1 hero video + 3 hook variations + raw footage
Usage: Spark Ads code duration (30/60/365 days), paid usage term, whitelisting rights
Deadline and review steps:
```

## 10. Pre-flight QA checklist (every ad)
- [ ] 9:16, sound on, readable captions inside safe zones
- [ ] Hook in the first 3 seconds; product visible by second 3
- [ ] Claims match BRAND.md approved claims; no prohibited claims for the category
- [ ] Music from CML or original; licensed voice and likeness
- [ ] AI-generated content disclosed where required
- [ ] Destination URL loads under 3 seconds on mobile, matches the ad's offer and price
- [ ] UTM parameters present (utm_source=tiktok, utm_medium=paid_social, utm_campaign={campaign}, utm_content={ad})
- [ ] Spark code valid for the full planned flight
- [ ] Ad text free of all-caps spam, excessive punctuation and prohibited terms
