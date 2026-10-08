# Creative for App Ads and Store Pages

> Knowledge as of 2026-10. New surfaces: App Store product page headers and search result assets (2026-10-05), Apple Ads use of those assets on the Today tab and in search (fall 2026), Google Play Shorts (2026-05), TikTok Auto-select creative for Smart+ App (2026-01), Meta Advantage+ creative enhancements on by default (2026-02). The creative-strategy agent owns cross channel concept research and testing systems; video-studio produces video files. This module defines what app campaigns need.

## 1. Creative is the targeting for app UA

On Meta, TikTok, Google App campaigns and the ML networks, the algorithm chooses who sees the ad based largely on creative and the optimization event. Most performance swings at Growth tier and above come from concepts, not bids [Practitioner consensus]. Budget creative production with media: at Scale tier, plan 10% to 20% of media spend for creative production and testing [Practitioner consensus].

## 2. Formats by channel

| Channel | Formats | Specs to supply |
|---------|---------|-----------------|
| Meta app campaigns | Video (9:16 Reels and Stories, 4:5 and 1:1 feed), static, carousel, playable ads, Flexible format | 9:16 video 15 to 30 s with captions; 1:1 and 4:5 static; HTML5 playable (optional) |
| TikTok | Native 9:16 video with sound, Spark Ads (creator posts), TikTok Ad Network inventory includes playables and rewarded | 9:16 video 9 to 34 s, safe zones, creator voiceover |
| Google App campaigns | Text, images, video (landscape, square, portrait), HTML5 | Up to 5 headlines, 5 descriptions, 20 images, 20 videos per ad group |
| AppLovin, Unity, Mintegral, Liftoff, Moloco | Rewarded and interstitial video, playables (MRAID HTML5), end cards, banners | Portrait and landscape video 15 to 30 s, playable 15 to 30 s of interaction, end card |
| Apple Ads | Default page or custom product page assets; new header and search result assets (fall 2026) | CPP screenshots, previews and creative assets |
| Store pages | Icon, screenshots, previews, headers, feature graphic, Play Shorts video | See ASO references |

## 3. Concept library for apps

| Concept | Works for | Structure |
|---------|-----------|-----------|
| Problem to outcome demo | Utilities, productivity, finance | Pain in 2 s, app solves it on screen, result |
| Screen recording with voiceover | Any app | Real UI, finger taps, creator or founder voice, captions |
| UGC testimonial | Subscription, health, education | Real user story; only with documented consent and truthful results |
| Before and after | Photo and video, fitness (careful with claims) | Clear disclosure; no fabricated results |
| Gameplay capture | Games | Real gameplay in the first 3 s; show the core loop and progression |
| Fail or puzzle hook (games) | Casual and hybrid casual | Must reflect actual gameplay (see policy, section 6) |
| Comparison | Switchers | Only verified, fair comparisons from brand/CLAIMS.md |
| Feature drop or event | Existing user re-engagement | Pair with in-app events and ACe |
| Price or offer | Ecommerce, marketplace, subscription trials | Exact terms on screen, consistent with the store page |
| Social proof at scale | Category leaders | Verified numbers only (ratings, users) |

Hook rules for app video:
- Show the app or the outcome in the first 2 seconds; the store page will show the app anyway, so do not hide it.
- One message per ad; the store page continues the same message (custom product page or custom store listing).
- Captions on: most placements autoplay muted except TikTok.
- End with the app icon, name and a clear call to action matching the platform button.

## 4. Playable ads (games and some apps)

- 15 to 30 seconds of real interaction, a tutorial hand in the first second, a satisfying win or near win, end card with install call to action.
- MRAID compliant HTML5, under each network's file size limit (commonly a few MB) [Practitioner consensus, verify per network].
- Test playables on the networks that weigh them most (AppLovin, Unity, Mintegral, Liftoff, Google, TikTok Ad Network).
- Measure IPM and D1 retention by playable; a playable that shows a different game than the real one drives installs and kills retention.

## 5. Testing and metrics

| Metric | Formula | Use |
|--------|---------|-----|
| IPM | Installs / impressions x 1,000 | Primary creative efficiency read on networks and TikTok |
| CTR | Clicks / impressions | Hook and message strength |
| Click to install rate | Installs / clicks | Store page match |
| CPI | Spend / installs | Cost read; always paired with quality |
| Cost per trial start or bid event | Spend / events | Deep funnel creative read |
| D7 ROAS or D7 revenue per install by creative | Revenue / spend | Quality; needs MMP creative level data |
| Hook rate (video) | 3 s views / impressions | Opening strength |

Test protocol:
1. Concepts first: test 3 to 5 new concepts per week at Growth tier, 10 to 30 at Scale [Practitioner consensus].
2. Each concept gets 2 to 3 variants (hook, length, voice).
3. Read after a minimum of 3,000 to 10,000 impressions or 50 installs per creative on networks; on Meta and TikTok follow the meta-ads and tiktok-ads kill and scale rules.
4. Kill on IPM or CTR below 70% of account median after the minimum; keep on cost per bid event at or below target.
5. Iterate winners: new hooks, new first 3 seconds, new formats (playable version of a video concept).
6. Register every creative in `ads-master/creative-library/registry.csv` with concept, hook, format, channel, launch date, metrics and status.

## 6. Policy and truthfulness

- Ads must reflect the actual app experience. Misleading gameplay ads (puzzles or mechanics that do not exist in the game) have drawn regulator rulings, for example UK ASA cases against mobile game ads [Official regulator history], and violate platform misrepresentation policies [Official].
- No fake system alerts, fake notifications or fake close buttons in ads [Official, Google and Meta policies].
- Health, finance, dating and gambling apps carry category rules on Meta, Google, TikTok and in the stores; route to compliance.
- AI generated people or testimonials need disclosure where required and must never imply a real user result that did not happen; EU AI Act transparency rules apply to synthetic content from 2026-08-02 [Official, verify scope with compliance].
- Store screenshots must show the app in use (Apple Guideline 2.3.3) and must not contain misleading claims [Official].
- Google Play listing experiments reportedly require an AI asset declaration (2026) [Unverified].

## 7. Store continuity

| Ad concept | Store landing |
|-----------|---------------|
| Feature specific ad | CPP or custom store listing with that feature first |
| Persona ad (students, runners, parents) | Persona CPP |
| Offer ad | Store page with the same offer in promotional text or an in-app event |
| Competitor switch ad (Apple Ads) | Competitor switch CPP |
| Gameplay hook | Screenshots and preview showing the same mode |

Mismatch shows up as a click to install rate below 30% to 40% of the account median for that channel [Practitioner consensus]; fix the page before the bid.

## 8. Creative brief template (app)

```
# Creative brief: <app>, <concept>, <date>
Channel and placements: <Meta Reels, TikTok, AppLovin rewarded, Google App campaigns>
Objective and bid event: <install, trial start, purchase, D7 ROAS>
Audience insight (from reviews and research): <quote, source, date>
Single message: <one sentence>
Proof allowed (from CLAIMS.md): <list>
Hook options (first 2 s): 1) 2) 3)
Structure: hook / problem / app demo / outcome / CTA
Assets: <screen recordings, gameplay capture, creator, voiceover>
Specs: <ratios, lengths, safe zones, playable requirements>
Store continuity: <CPP ID or custom store listing>
Success metric and kill rule: <IPM, cost per bid event, D7 ROAS thresholds>
Compliance notes: <category rules, disclosures>
Handoffs: video-studio (production), creative-strategy (concept system), compliance (claims)
```
