# Creative and Copy for Conversational Ads

> Knowledge as of 2026-10. Sources: OpenAI Help Center (Ads in ChatGPT: The Basics 20001207, Launch Campaigns 20001209, Create Ads 20001212, Troubleshooting 20001217), OpenAI announcements (2026-09-16, 2026-10-05), Ad Policies (v1.6), practitioner notes and panel studies. Re-verify live.

## 1. Anatomy of a chat card ad

| Element | Spec | Notes | Label |
|---------|------|-------|-------|
| Sponsored label | Added by OpenAI | Always present, visually separated from the answer | [Official, 2026-09] |
| Advertiser name | Account name or brand name from Settings | Must match the business identity | [Official, 2026-09] |
| Favicon or logo | JPEG, PNG or WebP, at least 256x256 | Missing favicon blocks serving | [Official, 2026-09] |
| Title (headline) | 16 to 24 characters recommended, 50 maximum | Some placements truncate; write to the recommended length | [Official, 2026-09] |
| Description (copy) | 32 to 48 characters recommended, 100 maximum | Adds information the title does not have | [Official, 2026-09] |
| Image | PNG or JPG, square, up to 1200x1200, public direct URL (or uploaded file) | Rendered small (about 64 px thumbnail reported); avoid text and logos as the main visual | [Official, 2026-09] and [Unverified] (thumbnail size) |
| Landing page | Valid, reachable, crawlable by OAI-AdsBot and OAI-SearchBot | Most relevant page, not a generic home page | [Official, 2026-09] |

Older guidance mentioned about 16 characters for titles and 32 for bodies; ads with 17 to 25 character titles and 33 to 39 character bodies passed review in practice [Unverified]. Use 16 to 24 and 32 to 48.

Accepted image hosts: public Google Drive links, AWS (S3, CloudFront) links, or your own domain or CDN; the link must open the file directly, not a preview page [Official, 2026-09]. Preview of an ad renders in an iframe of about 390x220 [Unverified].

## 2. How ChatGPT users differ from search users

| Search ad user | ChatGPT ad user |
|----------------|-----------------|
| Typed a short query, scanning 4 ads and 10 links | Mid conversation, already received a tailored answer, ad sits below it |
| Ad must match the keyword | Ad must add something the answer did not: a specific offer, price, availability, proof or next step |
| Often first touch | Often after 2+ prompts of refinement (66% of ads appear after the second prompt or later) [Study, 2026-07] |
| Competes with other ads | Usually the only sponsored offer in the answer [Study, 2026-08] |
| Leaves to a SERP | May open in an in-app view or browser; patience is low |

Writing principle: the answer already explained the category. Your ad is the concrete next step for someone who now knows what they want.

## 3. Copy rules

1. Title states the offering and its main value in plain words (product or service plus differentiator). OpenAI: informative details over broad marketing language [Official, 2026-09].
2. Description adds new information: benefit, feature, use case, price, availability, guarantee. Do not repeat the title [Official, 2026-09].
3. Be specific and verifiable: numbers, prices, delivery times, service areas. Every claim must be substantiated (policy) [Official, 2026-09].
4. No superlatives you cannot prove ("best", "#1"), no guarantees of outcomes, no false urgency, no all caps, no emoji, no repeated exclamation marks [Practitioner consensus] aligned with policy on misleading claims.
5. Never imitate ChatGPT's interface or voice, never imply OpenAI endorsement, never mention "ChatGPT" or "OpenAI" in copy [Official, 2026-09] (policy) and [Practitioner consensus].
6. Professional language; product and event names also must not be obscene or shocking [Official, 2026-09].
7. Write several distinct variations per offering, each with a different angle, so the system can match more situations [Official, 2026-09].
8. Match the landing page exactly: price, product, offer and wording. Mismatch is a rejection reason [Official, 2026-09].

### Angles to rotate (one per ad)
| Angle | Title pattern | Description pattern |
|-------|--------------|---------------------|
| Offer specificity | `<Product> for <use>` | `<Key spec>. From <price>.` |
| Price or value | `<Product> from <price>` | `<What is included>. <Delivery or trial>.` |
| Speed or convenience | `<Service> today in <area>` | `<Booking method>. <Time window>.` |
| Proof | `<Product> rated <score>` | `<Number> reviews. <Return policy>.` |
| Use case | `<Product> for <situation>` | `Built for <need>. <Feature>.` |
| Comparison (substantiated only) | `<Category> without <pain>` | `<Fact based difference>. <Proof>.` |
| Risk reversal | `Try <product> free` | `<Trial length>, cancel anytime.` |

### Examples (lengths inside recommended ranges)
| Business | Title | Description |
|----------|-------|-------------|
| Trail shoes | Wide toe trail shoes | Rock plate, 6 mm drop. Free returns 60 days. |
| Emergency plumber | 24/7 plumber in Austin | $89 call-out fee. Licensed, on site in 2 hours. |
| Bookkeeping SaaS | Retail bookkeeping app | Syncs Shopify and POS sales. 14-day free trial. |
| Language app | Spanish in 10 min a day | Speaking practice with feedback. Free to start. |
| Boutique hotel | Lisbon hotel in Alfama | River views, breakfast included. From EUR 140. |

## 4. Images

Rules [Official, 2026-09] and [Practitioner consensus]:
- Simple, relevant, matches title and copy; avoid abstract or cluttered visuals.
- Square crop that reads at thumbnail size: one product or one scene, high contrast, centered subject.
- Do not use the logo as the main visual (the favicon already identifies you).
- Avoid text in the image; if present, it must be legible and match the copy.
- Owned or licensed assets only; no sexual or violent content.
- One image can serve many ads (one file served 18 ads in a practitioner test) [Unverified].
- Product feed ads pull product images from the feed; keep feed images clean (white or neutral background, no watermarks).

## 5. Landing page continuity

| Conversation intent | Best landing page | Avoid |
|--------------------|-------------------|-------|
| Specific product question | Product detail page of that product | Home page |
| Category comparison | Collection or comparison page with filters | Single product page that ignores alternatives |
| Local service need | Service page for that city with phone, hours, price cue | Generic services page |
| B2B problem | Use case page with proof and a short form or trial | Pricing page without context |
| Travel planning | Property or destination page with dates selector | Brand home page |

Checklist:
- [ ] Above the fold repeats the ad's offer and price.
- [ ] Loads fast on mobile (most ChatGPT usage is mobile app and mobile web); target LCP under 2.5 seconds.
- [ ] No interstitials, no login, no CAPTCHA, crawlable by OAI-AdsBot.
- [ ] `oppref` and UTMs survive redirects and client side routing.
- [ ] Clear single next step (add to cart, call, book, start trial).
- [ ] Consent banner does not block the page content (and pixel consent gating is wired).
- [ ] Do not send traffic directly to a checkout page [Practitioner consensus].

Hand landing page improvements to cro with the ad angles and session rate data.

## 6. AI assisted creative features

| Feature | What it does | How to use | Label |
|---------|-------------|-----------|-------|
| "Add new ad" prefill | Uses existing website metadata to prefill image, title, description; you review and assign | Treat as a draft; rewrite to recommended lengths | [Official, 2026-09] |
| AI suggested ad copy and imagery | Suggestions from landing page and objective | Use for volume; screen every claim | [Official, 2026-09] |
| AI text customization (opt-in) | Adapts existing headlines and descriptions to conversation context and translates to the user's language | Test as a separate ad group or campaign; check brand voice and claims in previews; keep claims in the base copy compliant because adapted versions inherit them | [Official, 2026-09] |

Test design for AI text customization: A/B at campaign level (same hints, same ads, customization on vs off), 2 weeks, compare CTR, post-click CVR and CPA. Watch for claim drift in previews.

## 7. Product feed ad templates
- One template per ad group; macros `{{brand}}`, `{{product.title}}`, `{{product.body}}`, `{{product.price}}` combined with text [Official, 2026-09].
- Feed titles should lead with brand, product type and key attribute (Google Shopping practice transfers).
- Keep prices and availability current (delta feed updates); price mismatches risk disapproval and bad user experience.
- Feed ads show images, titles, star ratings, prices and sale prices [Official, 2026-09]; populate ratings and sale price fields where allowed.

## 8. Preparing for new formats
| Format | Preparation now |
|--------|----------------|
| Visual ads during image generation (US test from late October 2026) [Official, 2026-10] | Build a library of square lifestyle images showing the product in use or the experience; inspiration first, not packshots only |
| Sponsored Agents (test, select US advertisers) [Official, 2026-09] | Draft a factual knowledge base (products, prices, policies, FAQs), escalation rules, lead capture flow; decide what the agent must never say |
| Carousels | Clean feed, consistent image style across products |
| Multi-language markets | Native copy per language; or test AI translation via text customization |

## 9. Policy pitfalls in creative (see policies reference)
- Health: no unsubstantiated wellness claims (diet pills, detox, health coaching are disallowed); supplements and devices only for approved US advertisers [Official, 2026-09].
- Finance: no guaranteed returns; restricted to approved US advertisers [Official, 2026-09].
- Comparisons and pricing claims must be substantiated [Official, 2026-09].
- Landing page must not lead to disallowed content (example: food delivery ad linking to alcohol delivery) [Official, 2026-09].
- Swimwear and lingerie only in standard retail context [Official, 2026-09].

## 10. What early advertisers report (all [Unverified] unless labeled)
- CTR varies widely by advertiser: panel averages 0.5% to 1.3%, top quartile around 1%, best brands about 1.6% with peaks near 5% [Study, 2026-05] (Similarweb relay) and [Study, 2026-08] (SE Ranking own test 1.30%).
- Delivery concentrates on one or two creatives per ad group [Study, 2026-08]; plan more variations rather than fewer.
- Specific, offer led copy and product feed ads are reported to outperform generic brand messages [Official, 2026-09] (feed ads among strongest performing) and [Practitioner consensus].
- Several small advertisers reported clicks without conversions (visa service, supplement brand, SaaS trials with no paid conversions) [Unverified] (Reddit self reports). Usually a mismatch between conversation intent and landing page, or low purchase intent of free tier users.
- Session loss: one advertiser saw click to session rate of 9.1% vs 29.8% on Google for the same page [Unverified]; check webview and redirect behavior.

## 11. Creative testing protocol
1. Start each ad group with 3 to 5 ads, each a single angle.
2. Run 7 days or 100 clicks per ad group before judging.
3. Judge ads on CTR and post-click CVR together (high CTR, low CVR usually means over promising copy).
4. Replace the bottom ad each cycle with a new angle; keep the winner.
5. Log angle results in the journal; promote patterns confirmed twice to memory.
6. Hand recurring winning angles to creative-strategy for cross channel use.

## 12. Ad copy sheet template
| Ad group | Ad name | Angle | Title (chars) | Description (chars) | Image file | Landing URL | UTM content | Claim source |
|----------|---------|-------|---------------|---------------------|-----------|-------------|-------------|--------------|
| | | | | | | | | |
