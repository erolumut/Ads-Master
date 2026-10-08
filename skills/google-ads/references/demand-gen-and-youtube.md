# Demand Gen, YouTube, Display and App

> Knowledge as of 2026-10. Demand Gen absorbed Video action campaigns (completed by 2026-04) and is absorbing Display campaigns (migration tool from 2026-06). Verify statuses in Google Ads Help.

## 1. The map of visual and video campaign types in 2026

| Campaign type | Job | Bidding | Status |
|---|---|---|---|
| Demand Gen | Demand creation and conversion from YouTube (in-stream, in-feed, Shorts), Discover, Gmail, Google Display Network, Maps | Maximize conversions, tCPA, Maximize conversion value, tROAS, Maximize clicks, target CPC | Core visual campaign [Official] |
| Video reach campaigns (VRC) | Reach and frequency (bumpers, skippable, non-skippable, Shorts in one campaign) | Target CPM, CPM | Awareness |
| Video views campaigns (VVC) | Views and engagement across in-stream, in-feed, Shorts | Maximum CPV | Consideration |
| Video action campaigns (VAC) | Retired, upgraded to Demand Gen | n/a | All remaining VAC were auto-upgraded by 2026-04 [Official, 2025 to 2026] |
| Display campaigns | Moving into Demand Gen as the GDN channel. Migration tool rolling out from 2026-06; later, new Display campaigns only inside Demand Gen | Same as Demand Gen | [Official, 2026] |
| App campaigns | Installs, in-app actions, pre-registration, engagement | tCPI, tCPA, tROAS | Separate system |
| Performance Max | Cross-channel conversion | See PMax module | |

## 2. Demand Gen essentials

Channels: YouTube (in-stream, in-feed, Shorts), Discover, Gmail, Google Display Network (added 2025), Maps (beta, 2026). Channel controls let you choose channels per ad group with separate reporting (launched 2025-03). Maps requires a location asset in the account, ads appear as promoted pins, and an advertiser can select Maps only in eligible accounts. [Official, 2025 to 2026; Maps beta status per Google Ads Liaison]

Formats: single image, carousel, video, product (feed-linked). One-tap image ads on Shorts and Gmail were added in a September 2026 update [Unverified, trade press 2026-09].

Settings and defaults to check:
| Setting | 2026 behavior | Action |
|---|---|---|
| View-through conversion optimization | On by default in new Demand Gen campaigns, open beta, video assets only; does not support offline conversions, store visits or OCI [Practitioner report, 2026-04] | Decide whether VTC counts in your goal. Report click-through and view-through separately. Validate with lift tests |
| Billing on Discover with VTC optimization | Switched from CPC to CPM billing from 2026-07-15 [Unverified, trade press] | Check billing and compare CPMs before and after |
| Lookalike segments | Moved from strict targeting to AI-powered audience signals from 2026-03-15 [Practitioner report, 2026] | Treat lookalikes as signals; tighten with exclusions and creative |
| New customer acquisition goal | Available | Use for growth with customer lists |
| Channel controls | Per ad group | Separate Shorts, in-stream and feeds when creative differs |
| Limited Ad Serving | Policy extended to all Google Ads surfaces in 2026, Demand Gen included from 2026-09-07 [Official policy update 2026-08, rollout gradual until 2028] | New advertisers may see limited delivery until trust is established |

Budget and learning [Practitioner consensus based on Google guidance]:
- Daily budget at least 15x target CPA (or a meaningful minimum, about 100 USD a day, if no target).
- Judge after about 50 conversions or 2 to 4 weeks, whichever is later.
- Do not change targets more than 15% at a time; do not edit creatives in the first 2 weeks.
- Google reported a 30% average conversion increase from H2 2025 Demand Gen improvements [Official claim via trade press, 2026-08; not independently verified].

Audience strategy:
1. Seed with Customer Match (purchasers, high value customers) and converters as lookalike seeds or signals.
2. Custom segments from converting search terms and competitor URLs.
3. Remarketing ad groups separate from new customer ad groups, with exclusions both ways.
4. Use optimized targeting for growth only when conversion tracking is clean.

Measurement:
- Demand Gen often shows low click-through conversions but real incremental effect. Do not cut it on last click alone. Use Conversion Lift (user or geo) or a geo holdout. See [experiments](experiments-and-testing.md).
- Report engaged-view conversions and view-through conversions separately from click conversions.
- Qualified Future Conversions, a predictive metric linking upper funnel views to later sales, was announced at GML 2026 [Official, 2026-05, availability unverified].

## 3. YouTube creative: ABCD and Shorts

Google's ABCD framework for effective video ads [Official, Think with Google]:
| Letter | Principle | Concrete rules |
|---|---|---|
| A | Attract | Hook in the first 5 seconds (before the skip button): fast pacing, a person or product on screen, tight framing, audio hook |
| B | Brand | Show the brand or product in the first 5 seconds, repeat it, say it out loud, show the logo naturally |
| C | Connect | One clear message, human emotion or humor, show the product in use, voiceover that explains |
| D | Direct | Clear call to action on screen and spoken, a reason to act now, end screen with offer |

Shorts rules [Practitioner consensus]:
- Vertical 9:16, native look (creator style, phone shot), captions on, sound on design, 10 to 35 seconds.
- Hook in the first 1 to 2 seconds. Text overlay that states the benefit.
- Use creator content: GML 2026 announced pulling organic YouTube creator videos into paid campaigns [Official, 2026-05].

Video format specs [Official, verify]:
| Format | Length | Notes |
|---|---|---|
| Skippable in-stream | Any, 15 to 60 seconds recommended for action | Skip after 5 seconds |
| Non-skippable in-stream | 15 seconds (up to 30 seconds on connected TV) | Reach and awareness |
| Bumper | 6 seconds | Frequency and recall |
| In-feed | Any | Thumbnail and title matter |
| Shorts | Vertical, up to 60 seconds | Native feel |
| Demand Gen video | At least 10 seconds recommended | Supply horizontal, vertical and square |

Creative volume by tier:
| Tier | Videos per month | Image sets per month |
|---|---|---|
| Starter | Do not run YouTube unless creative exists; 1 to 2 | 2 to 3 |
| Growth | 3 to 5 (horizontal and vertical) | 5 |
| Scale | 8 to 15 with hook variants | 10 |
| Enterprise | 20+ with structured testing | 20+ |

Hand off creative briefs to creative-strategy with the ABCD rules, format specs and the audience.

Asset Studio and generation:
- Multimodal Video Creation in Asset Studio is generally available (horizontal and vertical from one storyboard) [Practitioner report, 2026-08].
- Asset Studio with Gemini Omni (text, image, video from one brief) announced at GML 2026 with a staged rollout from summer 2026 [Official, 2026-05].
- Review every generated asset for brand and claims compliance before approval.

## 4. YouTube for reach and consideration

- Use VRC for efficient reach with frequency caps, mixing bumpers, non-skippable and Shorts. Measure with Brand Lift (ad recall, awareness, consideration) where eligible.
- Use VVC for consideration and remarketing pools.
- Connected TV: a large share of YouTube watch time is on TV screens; use 15 to 30 second creatives with clear branding. For CTV, QR codes or a memorable URL help direct response.
- Alcohol ads on YouTube inventory are allowed where locally permitted from 2026-10-30 under a personalized advertising policy update; targeting based on alcohol-related health information stays prohibited [Official policy notice, 2026-09].
- Business Agent (conversational agent in ads) entering a US beta on YouTube ads [Unverified, trade press 2026-09].

## 5. Display (inside Demand Gen from 2026)

- Display Network inventory remains available inside Demand Gen campaigns as the GDN channel. [Official, 2026]
- Use the migration tool when offered; it carries over learnings. Avoid migrating campaigns that are part of a running lift study.
- Placement hygiene: account-level placement exclusion list (mobile apps categories, kids content, low quality sites), content exclusions (sensitive categories), and brand suitability settings.
- Remarketing on Display: frequency caps, recency windows (1 to 7 days for high intent, 8 to 30 days for others), exclusions for converters.

## 6. App campaigns

| Subtype | Goal | Bidding ladder | Data rules |
|---|---|---|---|
| App installs (ACi) | Installs from new users | tCPI first, then tCPA on a key in-app event when 10+ events a day | Daily budget at least 50x tCPI; at least 10x tCPA for in-app actions [Official guidance, verify] |
| App engagement (ACe) | Re-engage existing users | tCPA or tROAS on in-app actions | Deep links required, audience lists of existing users |
| App pre-registration | Android pre-launch | Pre-registrations | Launch day boost |

Rules:
- Separate iOS and Android campaigns. iOS measurement relies on SKAdNetwork and on-device measurement; Android on Firebase or an MMP (AppsFlyer, Adjust, Branch, Singular).
- Assets: up to 5 headlines (30 characters), 5 descriptions (90 characters), up to 20 images, 20 videos, HTML5. Provide all orientations of video.
- Change targets by at most 20% at a time and wait for 100 conversions or 2 weeks between changes [Practitioner consensus].
- Keep the conversion event definition stable; changing the optimization event resets learning.
- For app brand protection, run a Search campaign on the app name if competitors bid on it.

## 7. Diagnostics

| Symptom | Likely causes | Fix |
|---|---|---|
| Demand Gen cost per conversion 2x Search | Expected for demand creation; or wrong conversion goal | Judge with lift test and blended results; check goal is the real outcome |
| Conversions mainly view-through | VTC optimization default | Report VTC separately; test VTC off vs on |
| Spend concentrated on Shorts with weak results | Creative not native to Shorts | Separate Shorts ad group with native vertical creative, or exclude Shorts via channel controls |
| Low delivery for a new account | Limited Ad Serving, low budget, narrow audiences | Broaden signals, raise budget to 15x CPA, build account history |
| App installs cheap but no retention | tCPI optimization on low value users | Move to tCPA on a retention or purchase event |
