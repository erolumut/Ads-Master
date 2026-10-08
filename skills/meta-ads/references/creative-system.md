# Creative System on Meta

> Knowledge as of 2026-10. Boundary: this module covers Meta-specific creative mechanics (how the delivery system treats creative, specs, Advantage+ creative settings, Meta testing tools, partnership ads, volume by tier, fatigue). General creative craft (research, angles, hooks, scripts, briefs, production, AI production workflows, cross-channel creative analytics) belongs to `creative-strategy`. Hand off briefs and concept generation there; take back finished assets and test plans.

## 1. Why creative is targeting on Meta

- Andromeda retrieval matches ads to people using learned representations of the ad itself [Official, 2024-12]. Your visual, copy, format and persona cues decide which users your ad is even considered for.
- Ranking models (Lattice with GEM knowledge) predict action rates per person per ad [Official, 2025-11]. Strong creative raises estimated action rate, which raises total value in the auction and lowers CPM paid per result.
- Near-duplicate ads are grouped (entity ID) and compete as one candidate [Practitioner consensus]. Variety in concept, not in micro-variations, opens new audience pockets.

The practical unit is the concept: a distinct combination of persona, motivator (problem, desire, fear, identity), angle, format and visual world. Executions (hook swaps, edits, aspect ratios) live inside a concept.

## 2. Creative diversity dimensions (use as a coverage grid)

| Dimension | Example values | Minimum spread per month (Growth tier) |
|-----------|---------------|------------------------------------------|
| Persona | New parent, gym regular, budget buyer, gift buyer, B2B ops manager | 3 |
| Motivator / angle | Problem-solution, social proof, us versus them, founder story, offer, education, objection handling, identity | 4 |
| Format | UGC talking head, demo, static image, carousel, catalog, meme or text post, motion graphic, creator partnership, podcast clip, before and after (where policy allows) | 4 |
| Messenger | Founder, customer, creator, expert, employee, no person | 3 |
| Visual world | Studio, home, outdoor, screen recording, illustrated, lo-fi phone | 3 |
| Length (video) | 6 to 15s, 15 to 30s, 30 to 60s, 60s+ | 2 |

Score coverage monthly: count live concepts per cell. Gaps are next month's briefs (pass to `creative-strategy`).

## 3. Creative volume by spend tier

| Tier | Live concepts | New concepts per week | Executions per concept | Refresh trigger |
|------|---------------|----------------------|------------------------|----------------|
| Starter (under $3k) | 3 to 6 | 1 to 2 | 1 to 2 | Frequency on top ad > 3 per 7 days or CPA +30% over 14 days |
| Growth ($3k to $30k) | 8 to 15 | 3 to 6 | 2 to 3 | Top 3 ads lose 20% of efficiency or 4+ weeks old |
| Scale ($30k to $300k) | 20 to 40 | 10 to 25 | 3 to 5 | Weekly pipeline regardless of fatigue |
| Enterprise (over $300k) | 40+ per market cluster | 25 to 60 | 3 to 8 including localization | Continuous; dedicated creative ops |
[Practitioner consensus, 2025 to 2026]. Scale volume to spend: a rough rule is one new concept per week per 1,000 to 2,000 of weekly spend for ecommerce; lead gen and B2B need fewer.

Ad set limit: 50 non-archived ads per ad set [Official, Marketing API reference]. Page-level ad limits also apply by the Page's highest monthly spend (250, 1,000, 5,000 or 20,000 ads) [Official, long-standing]; one account reported the Page limit no longer enforced in 2026-09 [Unverified, PPC Land]. Do not fill the ad set limit; 6 to 20 active ads per ad set is a workable range, with concepts distinct.

## 4. Specs and safe zones

| Placement group | Aspect ratio | Resolution | Notes |
|-----------------|-------------|-----------|-------|
| Feeds (FB, IG, Threads) | 4:5 (preferred), 1:1 | 1080 x 1350 or 1080 x 1080 | 4:5 takes more screen; Threads supports 1.91:1 to 9:16 video [Official, 2025-08 via secondary] |
| Stories, Reels, WhatsApp Status | 9:16 | 1080 x 1920 | Stories and Reels share one 9:16 safe zone since about 2026-03: keep key text and logos out of the top about 14% (270 px) and the bottom 20 to 35% (up to 670 px), with about 6% side margins; measured overlays differ (one tool reports 23% bottom on Reels), so use the conservative zone and check the Ads Manager safe zone overlay [Practitioner consensus, 2026-03] |
| Carousel | 1:1 or 4:5 | 1080 x 1080 or 1080 x 1350 | 2 to 10 cards; Threads carousels image only, 2 to 10 cards, headline 40 characters [Unverified, 2026] |
| Right column, Marketplace, search | 1:1 | 1080 x 1080 | Rendered from feed assets |
| Audience Network | 9:16, 1:1, 16:9 | as above | Lower quality traffic for leads; price with value rules |

Text guidance: primary text shows about 125 characters before truncation in feeds; headline about 40 characters; description often hidden. Put the hook in the first line. Captions burned in for video (most watch muted in feed; Reels and Stories are more sound-on).

Video guidance [Practitioner consensus]:
- Hook in the first 1 to 2 seconds: motion, face, problem statement, product in use.
- Design 9:16 masters, export 4:5 and 1:1 crops, or supply all three so placement asset customization uses native versions.
- Use licensed audio (Meta Sound Collection for ads); trending commercial songs in organic posts may be muted when boosted.

## 5. Advantage+ creative and generative features

See the enhancement table in [campaign-types-and-settings](campaign-types-and-settings.md) section 7. Operating rules:
1. Review every enhancement toggle at launch. Since 2026-02 enhancements are on by default for new Sales, Leads and App campaigns [Practitioner consensus, 2026-02]. Image to video in Advantage+ creative became generally available on 2026-10-06; product image to product video is in beta for eligible catalog advertisers; Ads Creative Studio (video concepts with editable hooks, audio, length, overlays and end scenes) widened access the same day [Official, 2026-10, via Relevant Audience].
2. Preview AI-modified versions (expanded images, generated backgrounds, text variations) for every ad in regulated or claims-sensitive accounts.
3. Test generative features as an A/B test (enhancements on vs off) when spend allows; otherwise use them for catalog and static-heavy accounts first.
4. Keep brand kit (logos, colors, fonts) uploaded where the account supports it so generated variants stay on brand.
5. Treat AI-generated people, voices and likenesses carefully. New York requires a conspicuous disclosure when an ad contains a synthetic performer (General Business Law 396-b, in force 2026-06-09, fines 1,000 USD then 5,000 USD) and California SB 1050 (signed 2026-09-16, effective 2027-01-01) requires a clear disclosure near the performer [Official law, via Manatt and DLA Piper]. Meta adds an "AI info" label (in the About this ad menu, sometimes next to Sponsored) to ads made with Meta's generative tools and, since 2026-06-01, to ads whose media carries C2PA or similar metadata from third-party AI tools [Official, 2026-06]. Coordinate with `creative-strategy` and legal.

## 6. Testing creative on Meta

Methods compared:
| Method | How | Pros | Cons | Use when |
|--------|-----|------|------|----------|
| In-flight (BAU) | Add new concepts to the scaling ad set | Real auction, no extra structure | Meta favors incumbents; new ads may get little spend | Default at Starter and for most iterations |
| Creative testing tool (Ads Manager, from 2025-10) | From an ad in an existing ad set, create 2 to 5 test ads; Meta splits spend evenly, each person sees one ad, with set duration, budget and comparison metric | Fair spend, clean read, no new campaign | Reported limits: highest volume bidding only (no cost per result goal, bid cap or ROAS goal); Meta recommends no more than 20% of budget for the test; default about 7 days, up to 30; test ads are duplicates and the original ad is not in the test; lifetime budgets were unsupported at launch but later observed working; a cap of 10 test ads appears in some accounts [Practitioner reports, 2025-10 to 2026-01, Jon Loomer and Search Engine Journal] | Growth tier and above for concept tests |
| ABO testing campaign ("sandbox") | Separate campaign, one ad set per concept, equal budgets | Controlled spend per concept | More learning resets, auction overlap with main campaign | When the testing tool cannot be used (bid strategy, format) |
| Experiments A/B test | Split audiences between 2 to 5 cells, choose key metric | Statistical read with confidence | Needs budget and time | Structural tests: enhancements on/off, format strategy, landing page |

Test design rules:
- Hypothesis written as "If we [change], then [metric] improves because [insight]". Log in ads-master/EXPERIMENTS.md.
- Primary metric: cost per result on the optimization event; secondary: hook rate, hold rate, CTR (link), CVR.
- Minimum read: each cell reaches at least 20 to 30 conversions, or spend of 2 to 3 x target CPA per cell for kill decisions [Practitioner consensus].
- Duration 7 days minimum (covers weekday effects), 14 days for lead gen with CRM lag.
- Winners graduate into the scaling ad set with the same post ID (preserves social proof) or as new ads if the test used separate creatives.

Leading indicators (video):
```
Hook rate   = 3-second video plays / impressions
Hold rate   = ThruPlays / 3-second video plays     (or 15s plays / 3s plays)
CTR (link)  = link clicks / impressions
CVR         = conversions / link clicks (or landing page views)
CPA         = CPM / (1000 x CTR x CVR)
```
Use leading indicators to diagnose and kill early losers; judge winners on CPA or value.

Kill and keep rules (per ad, after it has had a fair chance):
| Signal | Action |
|--------|--------|
| Spend 2 x target CPA, 0 conversions, hook rate and CTR below account median | Turn off |
| Spend 3 x target CPA, CPA > 1.5 x target | Turn off unless it drives cheap upper funnel events and the account is signal-starved |
| CPA within 20% of target, rising spend share | Keep, iterate (new hooks, formats) |
| CPA better than target with spend share growing | Protect; build 2 to 3 executions of the concept in new formats |

## 7. Partnership ads and creators

Mechanics:
- Partnership ads run with both the brand and creator (or partner brand) handles in the header. Created from an existing creator post (with permission) or with a partnership ad code, or built in Ads Manager with creator permission.
- Creator Marketing Hub (launched globally 2026-09-15 at IAB Global Creator Week; merger first signaled at Cannes in 2026-06) combines Creator Marketplace and the Partnership Ads Hub: creator and organic content discovery (including a "predicted affiliate content" filter), content-level permissions with expiration dates, a draft partnership ad from the hub in one click with a suggested objective, editing tools that remove copyrighted music and stickers that block ad use, and partnership messaging with creators [Official, 2026-09, via MediaPost, Marketing Dive, Social Media Today]. The Creator Marketplace API now covers Facebook creators, a Messaging API was added, and partnership ads can be created through Meta's ads connector for AI agents. Not included: affiliate commissions, order-level creator attribution or performance payments. Rollout continues through the end of 2026.
- Instagram live video partnership ads: a creator's active livestream can run as a partnership ad in Instagram Stories, Reels and Feed, scheduled generally available from 2026-09-29 (previously Facebook only); the creator must grant ad access in advance [Official, 2026-09]; availability varies by account.

Operating rules:
1. Secure paid usage rights in the creator contract: duration (90 days minimum, 12 months preferred), placements, edit rights, whitelisting or partnership ad permissions, exclusivity, and disclosure obligations.
2. Run partnership ads inside the main scaling ad set alongside brand ads; they are just different concepts.
3. Disclose paid partnerships per local rules (FTC in US, ASA in UK, Reklam Kurulu influencer guidance in Turkey requires clear advertising labels) [Unverified local details, verify with counsel].
4. Measure creators by concept performance, not by follower count.

## 8. Reels, Stories, Threads and WhatsApp Status best practices

| Surface | Do | Avoid |
|---------|-----|-------|
| Reels | Native vertical, creator-style, fast hook, captions, sound designed for sound-on | Landscape videos with bars, TV ads without edits |
| Stories | Sequential frames, clear CTA in middle third, polls are organic only | Text at edges, overcrowded frames |
| Threads feed | Conversational copy, images or short video, text-led statics | Hashtags and URLs in copy (unsupported in some formats) |
| WhatsApp Status | Vertical, simple, clear CTA to chat or site | Assuming Status reach in EU markets (rollout lags) |
| Facebook Feed | 4:5, readable statics, longer copy for considered purchases | Tiny text in images |
| Audience Network | Rely on automatic rendering; check lead quality | Judging it on CTR (accidental clicks) |

## 9. Fatigue

Signals that a concept is fatiguing (look at 7-day rolling vs prior 7 days):
- Frequency rising (cold campaigns above about 2.5 to 3.5 per 7 days is a common warning zone) [Practitioner consensus].
- CTR (link) down 20%+ with stable CPM.
- CPM rising while delivery shifts to fewer placements.
- CPA up 25%+ for 7 days with no tracking or site change.
Response: add new concepts first (not just new hooks), then reduce spend on the fatigued ad. Do not edit the fatigued ad (it resets learning on that ad set).

## 10. Creative registry template (copy into an output file)

```
| ConceptID | Persona | Motivator | Angle | Format | Messenger | Launch | Status | Spend | Results | CPA | Hook | Hold | CTR | Notes |
|-----------|---------|-----------|-------|--------|-----------|--------|--------|-------|---------|-----|------|------|-----|-------|
| C042 | Busy parent | Time saving | Demo | Reel UGC | Customer | 2026-10-01 | Live | | | | | | | |
```
Keep it in ads-master/outputs/meta-ads/ as a dated file and update with a new dated version each month.
