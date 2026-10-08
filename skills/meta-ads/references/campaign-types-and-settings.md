# Campaign Types and Settings

> Knowledge as of 2026-10. Meta renames settings often and rolls out changes account by account. Always confirm the label in the live Ads Manager before writing a change list. Where a setting name differs in the account, use the account's label and note the difference in the journal.

## 1. Objectives (Outcome-driven ad experiences)

| Objective | Typical performance goals | Conversion locations | Use for |
|-----------|---------------------------|----------------------|---------|
| Awareness | Maximize reach, impressions, ad recall lift, ThruPlay | n/a | Brand, launch, reach for retail; measured with brand lift or geo tests |
| Traffic | Landing page views, link clicks, conversations, calls | Website, app, messaging, calls | Rarely the right choice for performance; LPV only for content or seeding audiences |
| Engagement | Video views, post engagement, conversations, Page likes, event responses | On ad, messaging, website (engagement events) | Messaging-led businesses, video seeding, community |
| Leads | Leads, conversion leads, conversations, calls, quality calls | Instant forms, website, messaging (Messenger, Instagram, WhatsApp), calls, app | Lead gen, local services, B2B |
| App promotion | App installs, app events, value | App stores, MMP | Apps and games |
| Sales | Conversions, value, conversations, catalog sales | Website, app, website and app, messaging, calls, website and in-store | Ecommerce, subscriptions, any business with a purchase event |

Rule: choose the objective that matches the business event you will optimize to, then pick the deepest event with enough volume (see bidding module).

## 2. Advantage+ versus manual (the 2025 to 2026 unification)

Timeline:
| Date | Change | Label |
|------|--------|-------|
| 2022-08 | Advantage+ shopping campaigns (ASC) launched | [Official, 2022-08] |
| 2025-02 | Advantage+ shopping renamed Advantage+ sales campaigns; streamlined creation tested for Sales, App and Leads with Advantage+ on by default | [Official, 2025-02] (Jon Loomer coverage, Meta business page) |
| 2025-05 | Marketing API: unified Advantage+ structure; Advantage+ status determined by budget, audience and placement settings instead of a special campaign type | [Official, 2025-05] (PPC Land coverage) |
| 2025-10 to 2026-Q1 | API v24 then v25 phase out creation of legacy ASC and AAC through `smart_promotion_type`; campaigns created the new way | [Official, 2025 to 2026] verify in changelog |
| 2026-02 | "Automation Unification" (Meta for Developers, 2026-02-13): Sales, Leads and App campaigns default to an automation-first Advantage+ setup; manual and Advantage+ build paths merged in the UI; Advantage+ creative enhancements on by default for new campaigns, each can be switched off | [Official, 2026-02, developer notice via secondary]; UI details [Practitioner consensus]. February, not September, is the consensus date |
| 2026-08 | Ad set placement exclusions removed in many accounts from 2026-08-25 (in-product notice seen 2026-08-20); value rules offered as the alternative | [Practitioner consensus, 2026-08]; scope [Contested], see section 6 |
| 2026-10-06 | Customer Lifecycle Strategy (ad set setting in Sales campaigns: reach new and existing customers, or acquire new customers only) opened to all advertisers; Advantage+ creative image to video generally available | [Official, 2026-10] via Relevant Audience, Common Thread Collective |

How "Advantage+ on" is decided now: a Sales, App or Leads campaign shows Advantage+ on when three levers are on together:
1. Advantage campaign budget (campaign level budget; some accounts label it Advantage+ campaign budget).
2. Advantage+ audience (your inputs act as suggestions, with hard audience controls only for location, minimum age, language and excluded custom audiences).
3. Advantage+ placements (no placement exclusions at ad set level).

Turning any lever off (ad set budgets, original audience options, manual placements) turns the Advantage+ badge off for that part. The campaign still runs; it simply loses the automation for that lever.

Decision tree:
```
Is there a clean purchase or lead signal with >= 50 events per week at the campaign level?
  No  -> Use Advantage+ on, highest volume, optimize to the deepest event you can feed (consolidate first).
  Yes -> Is the main constraint efficiency (CPA or ROAS target hard)?
          Yes -> Advantage+ on + cost per result goal or ROAS goal, value rules if segments differ in value.
          No  -> Advantage+ on + highest volume or highest value, scale by budget.
Is there a legal or business reason the algorithm must not reach some people (age, geo, existing customers only, regulated claims)?
  Yes -> Use audience controls and account-level controls first. Use original audience options only if controls cannot express it.
```

When a manual (lever off) setup is still justified:
| Situation | Lever to turn off | Why |
|-----------|-------------------|-----|
| Regulated targeting limits beyond controls (e.g. age 21+ alcohol market rules, local licensing radius) | Audience | Legal requirement |
| Strict per-segment budgets required by finance or partners | Budget (ad set budgets) | Accountability |
| Placement must be blocked for brand safety and account-level control is too broad | Placements (if still available) | Brand safety |
| Retention or existing customer offers with no acquisition intent | Audience (custom audience, no expansion) | Prevent waste on non-customers |
| Clean structural experiment | Any | Test design |

## 3. Advantage+ audience in detail

| Input | Type in Advantage+ audience | Notes |
|-------|----------------------------|-------|
| Location | Control (hard) | Include and exclude countries, regions, cities, postal codes |
| Minimum age | Control (hard) | Set legal minimum; 18 default for many categories |
| Language | Control (hard) | Use only when creative is language-specific and geo is multilingual |
| Excluded custom audiences | Control (hard) | Purchasers, current customers, employees |
| Age range maximum, gender | Suggestion | The system may go beyond |
| Custom audiences, lookalikes | Suggestion | Seed the model early; low value once the campaign has conversion history |
| Detailed targeting (interests, behaviors) | Suggestion | Detailed targeting exclusions were removed for new ad sets from 2024-07-29, and existing ad sets using them stopped delivering from early 2025 (2025-01-31 per Meta's notice; one guide says 2025-03-31) [Official, 2024-07, via Jon Loomer and Social Media Today]; custom audience exclusions remain. AI audience discovery inside Detailed Targeting announced for the end of 2026 [Official, 2026-10, not yet live] |

Account-level audience controls (Advertising settings) apply to every campaign in the account. Use them for legal minimum age, excluded locations, and employee exclusions.

## 4. Budget settings

| Setting | Options | Recommendation |
|---------|---------|----------------|
| Budget level | Advantage campaign budget (campaign) or ad set budget | Campaign budget for scaling; ad set budget for tests and strict allocations |
| Budget type | Daily or lifetime | Daily for always-on; lifetime for flights, sales events and ad scheduling (dayparting) |
| Ad set spend limits (under campaign budget) | Minimum and maximum daily or lifetime spend | Use sparingly. Minimums force spend into weak ad sets; use only to guarantee new concept exposure |
| Budget scheduling | Increase budget by an amount or percentage for chosen time windows | Use for sales events and known high-intent windows (payday, BFCM, launch days) |
| Daily budget flexibility | Meta may spend more than the daily budget on high-opportunity days, while keeping weekly spend within 7 x daily budget | Daily flex raised from 25% to up to 75% above the daily budget in early 2025, shown first as an in-account message in some accounts [Official in-account notice via Jon Loomer and Meta support text, 2025-03]. Plan pacing with weekly totals, not daily totals |

Minimum budgets: Meta enforces minimum daily budgets that depend on currency and the billing or optimization event (historically about USD 1 per day for impression billing, about USD 5 per day for click or engagement optimization, and higher for low-frequency events) [Official, long-standing, verify in UI]. The practical minimum for conversion optimization is far higher: about 7 x target CPA per day per ad set to reach the learning threshold.

## 5. Optimization, conversion events and attribution settings

| Setting | Where | Options | Recommendation |
|---------|-------|---------|----------------|
| Conversion location | Ad set | Website, App, Website and app, Message destinations, Calls, Instant forms, Website and in-store | Match where the conversion happens; "Website and in-store" requires offline or store events via Conversions API |
| Performance goal | Ad set | Maximize number of conversions, Maximize value of conversions, Maximize number of landing page views, Maximize conversations, Conversion leads, Incremental conversions (where eligible) | Deepest goal with sufficient volume; value when values vary at least 2x between orders or leads |
| Conversion event | Ad set | Standard events, custom events, custom conversions | Purchase, Lead, CompleteRegistration, Subscribe, StartTrial; avoid custom conversions built on URL rules when CAPI events exist |
| Attribution model | Ad set | Standard or Incremental (where eligible) | Standard by default; incremental for mature accounts with stable tracking and >= 50 conversions per week (see measurement module) |
| Attribution setting (standard) | Ad set | 1-day click, 7-day click, 1-day view, engage-through (1 day) | 7-day click plus 1-day view as default for most; 1-day click for short cycles or when view credit inflates results; see measurement module for the 2026 changes |

## 6. Placements

Advantage+ placements is the default and recommended setting. Current placement families (labels vary by account): Facebook Feed, Facebook profile feed, Facebook Marketplace, Facebook video feeds, Facebook right column, Facebook Business Explore, Facebook Stories, Facebook Reels, ads on Facebook Reels, Facebook search results, Facebook in-stream video, Instagram Feed, Instagram profile feed, Instagram Explore home (Explore Feed removed in v26.0, 2026-07), Instagram Stories, Instagram Reels, Instagram search results, Messenger inbox, Messenger sponsored messages (Messenger Stories removed 2026-07 to 2026-08), Audience Network (native, banner, interstitial, rewarded video), Threads feed, WhatsApp Status (where available).

Changes to know:
| Date | Change | Label |
|------|--------|-------|
| 2025-04 | Threads ads opened to advertisers globally (delivery limited) | [Official, 2025-04] |
| 2025-08 | Threads video ads | [Official, 2025-08] via secondary |
| 2025-09 | Click to message ads in WhatsApp Status | [Official, 2025-09] via Social Media Today |
| 2025-10 | Threads image carousel ads | [Unverified, 2025-10] |
| 2026-01-21 | Threads ads rolling out to all users worldwide, gradual over months | [Official, 2026-01] (CNBC, TechCrunch) |
| 2026-02 | WhatsApp ads in Status and Promoted Channels announced as rolling out globally after 2025 tests | [Official, 2026-02] via trade press; EU later |
| 2026-07-29 | Graph API v26.0: Instagram Explore Feed placement no longer available (API calls naming it error; delivery shifts to other placements); Messenger Stories value silently stripped; applies to all API versions from 2026-10-27. Instagram Explore home is a separate placement and was not named | [Official, 2026-07] changelog via PPC Land and Unalsoft; Ads Manager UI timing varied by account |
| 2026-08-25 | Ad set level placement exclusions (placements, platforms, devices, operating systems) removed in a staged rollout; value rules allow per-placement bid changes from minus 90% to plus 1,000% but never a zero bid; account-level placement controls remain | [Practitioner consensus, 2026-08] (Jon Loomer, PPC Land, Common Thread Collective); no Meta newsroom or Help Center announcement found as of 2026-10-08, so scope and permanence stay [Contested] |
| 2026-09 | Threads ads can run from a native Threads profile with no Instagram account; Threads name may differ from the Instagram name; Threads-specific task-based access in the business portfolio; gradual rollout | [Official, 2026-09] via Social Media Today and MediaPost |

How to handle placements now:
1. Leave Advantage+ placements on unless a brand safety reason exists.
2. If a placement must not appear at all, use account-level placement controls (Advertising settings > Account controls > Placement controls), not ad set settings. Sort current exclusions into hard requirements (brand safety, contracts, regulation) and soft preferences (performance) before the ad set option disappears in the account.
3. If a placement is merely less valuable (for example Audience Network for lead quality), use a placement value rule to lower bids rather than block. Reported limits: value rules work with highest volume and cost per result goal, not bid cap or ROAS goal; rules act on individual placements, not whole platforms; rule and criteria counts differ across sources, so check the account [Practitioner reports, 2026-09].
4. Build creative that renders natively in 9:16, 4:5 and 1:1 so every placement gets a good asset (see creative module).
5. Read placement breakdowns with the breakdown effect in mind (see diagnostics module).

## 7. Creative settings at the ad level

| Setting | What it does | Default | Recommendation |
|---------|-------------|---------|----------------|
| Flexible ad format | Upload up to 10 images or videos per ad; Meta picks format and combination per person | Available on Sales, Leads, App, Traffic, Engagement | Use for concept bundles (one concept, several executions). Not a substitute for distinct concepts |
| Advantage+ creative enhancements | Automatic edits and additions (see table below) | On by default for new Sales, Leads and App campaigns since 2026-02 [Practitioner consensus, 2026-02] | Review every toggle; switch off any that risk brand, legal or claims issues |
| Multi-advertiser ads | Ad can appear alongside other advertisers' ads after engagement | On | Leave on unless brand policy forbids |
| Site links | Additional links under the ad | Off or suggested | Use for ecommerce with clear categories |
| Languages / translation | Auto-translate text and, for Reels, AI voice translation in some markets | Off | Use for multi-language markets after native speaker QA |
| Catalog / product extensions | Show products from catalog under a non-catalog ad | Optional | Useful for ecommerce with clean catalog |
| Call to action | Button label | Learn more / Shop now | Match intent; test "Get offer" vs "Shop now" only via clean test |
| Tracking | Website events dataset, app events, offline events, URL parameters | Dataset selected | Always set dataset and UTM parameters with {{campaign.id}}, {{adset.id}}, {{ad.id}} macros |

Advantage+ creative enhancement families (names vary by account and rollout):
| Enhancement | Typical effect | Brand risk | Default stance |
|------------|----------------|-----------|----------------|
| Visual touch-ups, adapt to placement, image expansion | Crops, expands or adjusts image to fit placements | Low to medium (AI-generated pixels at edges) | On, check previews |
| Text improvements / text variations | Swaps primary text with headline or generates variations | Medium to high for regulated claims | Off for regulated categories; on otherwise after review |
| Add overlays, enhance CTA | Adds text overlays or CTA styling | Medium | Test |
| Music | Adds background music to images and some videos | Low to medium | On for lifestyle, off for B2B and serious categories |
| Image animation, generate video from images (image to video GA 2026-10-06; product image to product video in beta for catalog advertisers) | Turns images into motion | Medium | Test on catalog and static-heavy accounts |
| Generate backgrounds | AI background generation for product images | Medium to high | Test, check product accuracy |
| Relevant comments | Shows a comment beneath the ad | Medium (shows negative comments) | On only with comment moderation |
| Image templates, catalog frames | Adds frames or templates | Low | On for catalog |
| Site links, product extensions | Adds destination options | Low | On for ecommerce |
| Translate text | Auto-translations | Medium | On only with QA |
| Virtual try-on, AI product imagery | Announced 2025 for apparel and accessories in some markets | Medium | Test where available [Unverified availability] |
| Muse Image generation (Meta Superintelligence Labs model) | Announced 2026-07-07 for Advantage+ creative "in the coming weeks" (backgrounds, expansion, touch-ups, variations) | Medium to high | Not confirmed live as of 2026-10-08 [Official announcement; availability Unverified] |

Rule: in regulated verticals (health, finance, legal, alcohol, gambling) switch off every generative text and overlay enhancement and document the decision in ads-master/BRAND.md via a journal proposal.

## 8. Other campaign types and formats

| Type | Use | Key settings |
|------|-----|-------------|
| Advantage+ catalog ads | Product-level dynamic ads in Sales campaigns | Catalog, product set, template; see catalog module |
| Collection with Instant Experience | Mobile storefront for catalogs or stories | Template (Instant storefront, lookbook, customer acquisition, storytelling) |
| Click to message (Messenger, Instagram, WhatsApp) | Conversations, leads or purchases via chat | Message template, ice breakers, automation; see lead gen module |
| Calls ads | Phone calls for local services | Call hours, call extension, quality calls optimization where available |
| Partnership ads | Ads from creator or partner handle | Partnership ad code or permissions; see creative module |
| Reach and frequency buying | Predictable reach for awareness | Frequency cap, schedule; needs minimum reach |
| Advantage+ app campaigns | App installs and events | MMP, SKAdNetwork, app events |
| Live video ads | Boost live broadcasts | Facebook live; Instagram live video partnership ads (a creator's active livestream run as a partnership ad in Stories, Reels and Feed) scheduled GA from 2026-09-29, with live commerce partners CommentSold, Firework, LiveMeUp, Sprii and TalkShopLive; the creator must grant ad access first [Official, 2026-09] via MediaPost; Meta's live shopping page still said beta for Instagram on 2026-10-01, so availability varies by account |
| Reels trending ads | Placement next to trending Reels and creators | Announced at IAB NewFronts (2025, expanded 2026) [Unverified details] |

## 9. Setup checklist before any launch

1. Dataset connected, Pixel plus Conversions API live, deduplicated, EMQ checked (measurement module).
2. Audience segments defined in ad account settings.
3. Account-level controls: minimum age, excluded employees, brand safety, placement controls.
4. Objective and conversion location match the business event.
5. Performance goal and bid strategy chosen with written rationale.
6. Budget meets the learning threshold or the plan explains why not.
7. Advantage+ creative enhancements reviewed one by one.
8. UTM parameters with ID macros set at ad level.
9. Special ad category declared if applicable.
10. Change list approved by the human before publishing.
