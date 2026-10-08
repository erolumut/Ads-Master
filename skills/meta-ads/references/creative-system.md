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

Ad set limit: 50 ads per ad set [Official]. Do not fill it; 6 to 20 active ads per ad set is a workable range, with concepts distinct.

## 4. Specs and safe zones

| Placement group | Aspect ratio | Resolution | Notes |
|-----------------|-------------|-----------|-------|
| Feeds (FB, IG, Threads) | 4:5 (preferred), 1:1 | 1080 x 1350 or 1080 x 1080 | 4:5 takes more screen; Threads supports 1.91:1 to 9:16 video [Official, 2025-08 via secondary] |
| Stories, Reels, WhatsApp Status | 9:16 | 1080 x 1920 | Keep key text and logos out of the top about 14% and bottom about 35% of Reels; about 6% side margins [Official guidance, verify current overlay] |
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
1. Review every enhancement toggle at launch. Since 2026-02 many are pre-selected on new Sales, Leads and App campaigns [Unverified].
2. Preview AI-modified versions (expanded images, generated backgrounds, text variations) for every ad in regulated or claims-sensitive accounts.
3. Test generative features as an A/B test (enhancements on vs off) when spend allows; otherwise use them for catalog and static-heavy accounts first.
4. Keep brand kit (logos, colors, fonts) uploaded where the account supports it so generated variants stay on brand.
5. Treat AI-generated people, voices and likenesses carefully: disclosure laws for synthetic performers are emerging (California, 2026-09) [Unverified details]; Meta labels some AI-generated ads. Coordinate with `creative-strategy` and legal.

## 6. Testing creative on Meta

Methods compared:
| Method | How | Pros | Cons | Use when |
|--------|-----|------|------|----------|
| In-flight (BAU) | Add new concepts to the scaling ad set | Real auction, no extra structure | Meta favors incumbents; new ads may get little spend | Default at Starter and for most iterations |
| Creative testing tool (Ads Manager, from 2025-10) | From an ad in an existing ad set, create 2 to 5 test ads; Meta splits spend evenly, each person sees one ad, with set duration, budget and comparison metric | Fair spend, clean read, no new campaign | Reported limits: no lifetime budgets, highest volume only, new ads only; original ad not in test [Unverified details] | Growth tier and above for concept tests |
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
- Creator Marketplace and the Partnership Ads Hub were reported merged into a Creator Marketing Hub on 2026-09-15 with AI creator discovery, one-click ad creation from creator posts and tools to remove copyrighted music from creator content [Unverified, 2026-09].
- Instagram live partnership ads reported generally available from 2026-09-29 [Unverified].

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
