# Andromeda and Creative Diversity

> Purpose: understand what Meta's retrieval system means for creative, separate official statements from industry claims, and run a creative mix that gives the system genuinely different options. Campaign structure, budgets and Advantage+ settings belong to `meta-ads`; this module defines the creative inputs.

## 1. What is known, what is claimed, what is myth

| Statement | Status | Source and date |
|-----------|--------|-----------------|
| Andromeda is Meta's ads retrieval system: it selects a few thousand candidate ads from tens of millions for each request, before ranking | [Official, 2024-12] | Meta Engineering blog, Dec 2024; repeated on Meta's Q2 2025 earnings call (July 30, 2025) per secondary reports |
| Ranking of the shortlisted ads is done by other models; GEM (Generative Ads Recommendation Model) is a foundation model that improves downstream ranking models | [Official, 2025-11] | Meta Engineering blog, Nov 10, 2025 |
| Q2 2025: Andromeda enhancements selected more relevant, personalized candidates and expanded to Facebook Reels | [Official per secondary, 2025-07] | Meta Q2 2025 earnings call as quoted by trade press |
| Conversion lifts quoted for 2025 (about 5% Instagram, about 3% Facebook from the ads recommendation model; about 4% from Andromeda changes) | [Contested] attribution between models differs across secondary sources | MobileDevMemo, Marketing Dive and others, 2025 |
| Meta recommends diversifying creative by concept, message, visuals and format to give the system more options | [Official, 2024 to 2025] Meta guidance as summarized by trade press | Social Media Today, Meta Performance guidance; Meta resource "Maximize conversions with differentiated ad creative" (cited by Jon Loomer, 2025-10) |
| Meta publishes no official number of ads or concepts per ad set | [Practitioner consensus] | Multiple 2025 to 2026 guides |
| Ads Manager shows a Creative diversity rating (Low, Medium, High) per ad set based on how alike the images and video thumbnails are, described by Meta as estimated and in development | [Official per secondary, 2026-08] | Common Thread changelog (Aug 2026); third-party summaries of Meta Help Center; availability varies by account |
| Creative fatigue and similarity metrics were tested with select partners via the Insights API from about June 2026; Meta said they are not widely available | [Unverified] | Trade press summary, 2026 |
| "Entity ID": near-duplicate ads are clustered under one ID and get one "ticket" to the auction | [Practitioner consensus, mechanism unverified]. The term is industry shorthand, not a Meta term | AdsUploader guide (2026) states the term is not official |
| A "Creative Similarity Score" above 60% triggers retrieval suppression | [Unverified]. Threshold traced to a vendor's data, not Meta | Admetrics and repeats; no Meta confirmation found |
| "Andromeda killed targeting" | Myth. Targeting inputs still exist; Andromeda is retrieval infrastructure. Creative carries more of the matching work in broad setups | Jon Loomer (2025-11), Meta statements |
| 25 diverse creatives in one ad set produced 17% more conversions at 16% lower cost than five ad sets | [Contested] attributed to Meta internal testing by one source and to an agency test by another | Chatterbuzz, Confect, 2026 |

Operating stance: build for the documented direction (diverse, distinct creative inputs, simpler structures), treat specific thresholds as hypotheses, and validate with the account's own spend distribution and tests.

## 2. Why diversity matters (the practical model)

1. Retrieval picks candidates per person per request. If ten of your ads look and say the same thing, they are likely competing for the same people and the system has little reason to retrieve more than one of them. [Practitioner consensus]
2. Different concepts open different audience pockets. A runner identity ad and a parent humor ad reach different people even with identical targeting.
3. Ads that differ only cosmetically (color, crop, headline wording, music) are iterations. They are useful for optimizing a winner but add little reach.
4. Signals from concept level differences (persona, setting, talent, format, message) are what the creative understanding models can detect. Meta's diversity rating reportedly reads image and video thumbnail similarity [per secondary summaries], so visual sameness is directly measurable.

## 3. The "new concept" test (run before launching anything as a new concept)

Score each candidate against every live ad in the same ad set. It counts as a new concept only if it differs on at least 2 of these 8 dimensions, and at least 1 of the first 4:

| # | Dimension | Example of "different" |
|---|-----------|------------------------|
| 1 | Persona | Runner vs parent of teen athlete |
| 2 | Core desire or pain | Smell after washing vs fabric lifespan |
| 3 | Angle | Hidden cause vs failed solutions vs identity |
| 4 | Narrative structure | Testimonial vs demo vs listicle vs skit |
| 5 | Format | Video vs static vs carousel |
| 6 | Visual world | Outdoor trail vs laundry room vs lab |
| 7 | Talent | Different person, age, gender, style |
| 8 | Awareness level | Unaware vs product aware |

Quick human test: "Would a viewer describe these two ads as the same ad?" If yes, it is an iteration.

Thumbnail check: put first frames side by side. If they look alike at thumbnail size, the system may see them as alike.

## 4. How many concepts (planning heuristics)

No official numbers exist. Use these starting points, then size by what your test budget can read ([Testing frameworks and volume](testing-frameworks-and-volume.md)):

| Tier | Distinct concepts live in the main scaling ad set | New concepts per month | Executions per new concept |
|------|--------------------------------------------------|------------------------|---------------------------|
| Starter (under $3k) | 3 to 6 | 2 to 4 | 1 to 2 |
| Growth ($3k to $30k) | 6 to 12 | 4 to 12 | 2 to 3 |
| Scale ($30k to $300k) | 10 to 20 | 12 to 40 | 2 to 5 |
| Enterprise (over $300k) | 15 to 30+ per main ad set, per market | 40 to 150+ | 3 to 6 |

Practitioner ranges published in 2025 to 2026 vary widely (for example "at least 6 meaningfully different ads per ad set", "8 to 20 different concepts", "10 to 15 diverse concepts") and none come from Meta [Practitioner consensus, contested numbers]. More ads than the budget can feed spreads spend thin: at low budgets, fewer and more different beats more and similar.

Meta's ad count limits per ad set have changed over time (reports in 2026 cite 150 ads per ad set) [Unverified]. Check the current limit in Ads Manager.

## 5. Concept mix targets (per main ad set)

| Dimension | Target mix |
|-----------|-----------|
| Personas | At least 2 to 3 active personas represented |
| Awareness | At least 3 of 5 levels; at least 40% of concepts unaware or problem aware for new customer acquisition |
| Formats | At least 2 video styles plus statics or carousels |
| Talent | At least 3 different on-camera people at Growth and above |
| Angles | No single angle above 40% of live concepts |
| Age of creative | At least 20% of spend on concepts launched in the last 30 days at Growth and above |

## 6. Using the Creative diversity rating

If the rating appears in your Ads Manager (ad set level, Low, Medium, High):

| Rating | Action |
|--------|--------|
| Low | Stop launching iterations into this ad set. Next 2 sprints: new concepts only, chosen for maximum distance (persona and visual world first). Remove near-duplicates with weak results. |
| Medium | Balance: about half new concepts, half iterations on winners. Check which visual worlds dominate. |
| High | Keep cadence; focus iterations on top concepts; still add at least 2 new concepts per month. |

Treat the rating as a hint, not a KPI: it reportedly reads visual similarity only, not message or persona. An ad set can rate High with all ads using the same hook. [Per secondary sources; Meta describes it as estimated and in development]

## 7. Advantage+ creative and AI enhancements (creative decisions)

Meta's Advantage+ creative includes standard enhancements (adjusting brightness and contrast, aspect ratio, templates, music, text variations, image animation, 3D animation, image expansion, backgrounds, product overlays, comments and site links, among others; the list changes often). Reports in 2026 say enhancements are on by default for new Sales, Leads and App campaigns, with disputed start dates (February vs September 2026) [Contested]. Meta's help text says some enhancements may be on by default and can be turned off, and recommends checking previews. Meta made image to video generation in Advantage+ creative generally available on October 6, 2026 [Official per trade press, 2026-10].

Creative strategist's rules (the channel agent applies settings after approval):

| Enhancement type | Default stance | Switch off when |
|------------------|---------------|-----------------|
| Visual touch ups, aspect ratio expansion | Allow, check previews | Product color or shape fidelity matters (fashion, cosmetics, food) |
| Text variations and generated headlines | Allow only with brand and claim review | Regulated claims, strict voice, legal approved copy |
| Music | Allow for statics; review for video with voice | Voice-led videos, brand audio identity |
| Background generation, image expansion | Test | Product must appear in real context; luxury and fashion brands reporting brand damage |
| Image animation and image to video | Test in a separate ad, label in name | Product motion would misrepresent the product |
| Overlays (prices, reviews, site links) | Allow if data is accurate | Feeds with stale prices |

Name ads that use generative enhancements with the `aiE` token (see naming conventions) so you can compare performance. Marketers in 2026 reported AI features re-enabling after duplication and altering ads they had opted out of (Marketing Brew, April 2026) [Practitioner reports]: re-check enhancement settings after every duplicate and on a monthly audit.

## 8. Structure implications (inputs for `meta-ads`)

- Fewer, broader ad sets with more distinct concepts each, rather than many ad sets with a few similar ads. [Practitioner consensus, consistent with Meta's simplification guidance]
- Separate concept testing from scaling only if the scaling ad set starves new ads (common). Options: Meta's Creative Testing tool, a dedicated testing campaign, or periodic launches into the scaling ad set with enough budget headroom. See the testing module.
- Do not duplicate a winning ad into many ad sets; produce adjacent concepts.
- Keep a concept registry: every concept ID appears in ad names so spend distribution by concept is visible.

## 9. Diagnostic: is similarity hurting us?

1. Export ad level spend for the last 30 days (see analytics module).
2. Roll up by concept ID. Compute share of spend per concept.
3. If one concept takes more than 60% of spend and new concepts get under 5% each after 7 days, run the new concept test on the starved ads.
4. If starved ads are iterations of the dominant concept: expected. Stop producing those; produce new concepts.
5. If starved ads are genuinely different but have bottom quartile hook rates: hook problem, not similarity.
6. If genuinely different with fine hooks but no spend: test them with forced spend (testing tool or test campaign) before concluding.

## 10. Worked example

Scale tier skincare brand, $120k/month Meta. One Advantage+ sales campaign, 42 ads. Spend distribution: 3 ads take 78%. Thirty of the 42 ads are the same founder video with different hooks and captions; 9 are product statics on the same pink background; 3 are UGC.

Diagnosis: about 3 visual worlds, 2 personas, 1 awareness level (product aware). Diversity rating Low.

Plan:
1. Pause (proposal for approval) 20 weakest founder iterations with no meaningful spend in 14 days.
2. Next 30 days: 12 new concepts across 4 personas (new mothers, men 35+, acne prone teens' parents, dermatology skeptics), 3 awareness levels, formats (street interview, dermatologist explainer with a real consented expert, comparison carousel, meme static, routine POV).
3. Launch through the testing lane, graduate winners into the scaling ad set.
4. Success metric: concept count with at least 5% of spend rises from 3 to 8; blended CPA stable or better within 6 weeks.
