# Landing Page Anatomy

> A landing page is any page where paid or organic traffic first lands. Its job is to continue the conversation the ad, query or AI answer started, then remove every reason not to take one action.

## 1. Choose the page by awareness level

Eugene Schwartz's five awareness levels (Breakthrough Advertising, 1966) decide how much the page must do before the ask. Read the segment's level in `ads-master/AUDIENCE.md`.

| Awareness | Visitor knows | Typical traffic | Page job | Length | Lead with |
|-----------|---------------|-----------------|----------|--------|-----------|
| Most aware | Your product and wants a deal | Brand search, retargeting, email | Close | Short | Offer, price, CTA |
| Product aware | Your product, not convinced | Brand plus competitor search, retargeting, comparison AI answers | Differentiate and de-risk | Short to medium | Proof, comparison, guarantee |
| Solution aware | Solutions exist, not yours | Non-brand search, Shopping, PMax, ChatGPT ads, AI referrals | Show why yours is the best solution | Medium | Specific outcome plus mechanism |
| Problem aware | The pain, not the solutions | Meta, TikTok, YouTube, Demand Gen cold audiences | Agitate problem, introduce category and product | Long | Problem in their words |
| Unaware | Nothing yet | Broad social, native, influencers | Story, curiosity, education | Long or pre-sell page | Story or hook |

Rule: page length matches the persuasion required, not a preference for short or long. Long pages win when the decision is expensive, complex or unfamiliar; short pages win when intent is high and the offer is known [Practitioner consensus]. Test length only after the first screen and the offer are right.

## 2. Page type decision tree

```
Is the traffic high intent for one specific product or SKU (Shopping, brand + product query, product carousel)?
  YES -> Product detail page (PDP). Make the PDP landing-page grade (section 7).
  NO  -> Is the offer one action (lead, booking, trial, signup) or one hero product?
        YES -> Dedicated landing page, navigation removed or reduced, one CTA.
        NO  -> Is the visitor comparing many items (category queries, "best X" queries, AI referrals)?
              YES -> Collection or comparison page with filters and clear "best for" labels.
              NO  -> Cold social traffic for a product needing education?
                    YES -> Pre-sell page (advertorial, listicle, quiz) that hands off to the PDP or offer page.
                    NO  -> Homepage only for brand traffic; never as the default for non-brand campaigns.
```

### Dedicated landing page vs product page
| Factor | Dedicated LP wins | PDP wins |
|--------|-------------------|----------|
| Catalog | 1 to 3 hero products, bundles, subscriptions | Large catalog, Shopping and PMax feed traffic |
| Traffic | Cold social, one angle per ad set | High intent search and Shopping |
| Offer | Special offer, bundle, quiz result, lead magnet | Standard price, standard offer |
| Measurement | Clean per-campaign testing | Shared page, more traffic for tests |
| Cost | Build and maintain per angle | Already exists |

Shopping, PMax and ChatGPT product carousel clicks land on the feed URL. The PDP is the landing page; improve it rather than redirecting. Price and availability on the page must match the feed or the item gets disapproved (hand feed issues to `commerce-feeds`).

## 3. Section by section anatomy (dedicated LP)

Order is a default. Move sections up when research says that objection kills conversion.

| # | Section | Job | Must contain | Common failure |
|---|---------|-----|--------------|----------------|
| 1 | Hero (first screen) | Match the ad, state the outcome, give one action | Headline matching ad promise, subhead with who and how, hero visual of product in use or result, primary CTA, proof strip (rating, count, logos) | Clever headline, stock image, CTA below the fold on mobile |
| 2 | Problem | Show you understand the visitor's situation | 2 to 4 pains in customer language from VOC | Generic pains, company language |
| 3 | Solution and mechanism | Why this works when others did not | Unique mechanism, how it works in 3 steps | Feature list without "so that" |
| 4 | Benefits | Outcomes, not features | 3 to 6 benefit blocks with specific numbers | Icons with one word each |
| 5 | Proof | Make the claim believable | Reviews with names and context, case results, ratings, media, certifications | Unattributed quotes, star widgets with 4 reviews |
| 6 | Offer | What exactly they get and pay | Price, what is included, bonus, payment options, shipping or onboarding | Price hidden or surprises later |
| 7 | Risk reversal | Remove downside | Guarantee, trial terms, cancel anytime, returns | Guarantee in the footer only |
| 8 | Objection handling (FAQ) | Answer the top 5 to 8 objections | Questions from surveys, chat and sales calls | FAQs about the company history |
| 9 | Final CTA | Second chance after persuasion | Restated outcome, CTA, risk reversal line | Different CTA than the hero |
| 10 | Footer | Trust and compliance | Contact, address, policies, legal | Full site navigation that leaks traffic |

## 4. First screen rules (mobile first)

Design at 360 to 430 CSS px width first. Most paid social traffic is mobile and lands inside in-app browsers.

- Headline: 6 to 12 words, states the outcome or the offer. Mirrors the ad.
- Subhead: 1 to 2 lines: who it is for, how it works, or the key differentiator.
- Visual: product in use, the result, or the interface. Real photos beat stock [Practitioner consensus]. The hero image is usually the LCP element; it must load fast (see [Speed](speed-and-core-web-vitals.md)).
- CTA visible without scrolling on a 390 x 844 viewport. Add a sticky bottom CTA on mobile after the first scroll.
- Proof strip directly under the CTA: rating with review count, customer count, or 3 to 5 recognizable logos.
- No carousel or auto-rotating slider in the hero. Each slide dilutes the message.
- No popup in the first 10 seconds for paid traffic. Google penalizes intrusive interstitials on mobile for organic, and paid visitors bounce [Practitioner consensus].

## 5. Attention ratio and exits

Attention ratio = number of clickable goals on the page : number of conversion goals. Target 1:1 on dedicated LPs (Unbounce concept) [Practitioner consensus].
- Remove main navigation on dedicated paid LPs. Keep logo (non-linked or linked to the same page), policies in footer.
- Keep navigation on SEO and AI referral landing pages, where visitors explore.
- Secondary CTA allowed for lower intent visitors ("See how it works", "Download the spec sheet") when it feeds the same funnel.

## 6. CTA rules

| Rule | Example |
|------|---------|
| Verb plus outcome, first person or imperative | "Get my quote", "Start free trial", "Shop the starter kit" |
| State the commitment level | "Book a 20-min demo", "No card required" under the button |
| One primary CTA style per page | Same color and copy in hero and final CTA |
| Contrast and size | Button contrast at least 3:1 against background (WCAG non-text contrast), text 4.5:1 |
| Microcopy under CTA | Risk reversal, time, price: "Free returns. Ships in 24 h." |
| Mobile target size | At least 44 x 44 px for comfortable tapping; WCAG 2.2 minimum is 24 x 24 CSS px |

## 7. PDP as a landing page (paid and Shopping traffic)

Minimum to make a PDP landing-page grade. Full PDP checklist is in [Ecommerce](ecommerce-pdp-cart-checkout.md).
- Title and first image match the ad or Shopping listing.
- Price, savings and stock visible above the fold on mobile; matches the feed.
- Rating and review count next to the title, linked to reviews.
- Add to cart visible on first screen; sticky add to cart on mobile.
- Delivery date estimate and shipping cost near add to cart.
- Returns and guarantee line near add to cart.
- Variant selection that cannot fail silently (clear error if no size chosen).

## 8. Page types and their anatomy

### 8.1 Lead gen LP (services, insurance, finance, education)
Hero with form or CTA to form > 3 benefits > how it works (3 steps) > proof > FAQ > form again. Form above the fold on desktop; on mobile, a CTA that scrolls to the form or opens a multi-step form. See [Forms](forms-and-lead-capture.md).

### 8.2 Local services LP
Click to call button in hero and sticky, service area named in the headline ("Emergency plumber in Leeds, 60-minute response"), real team photos, licenses and insurance, reviews from the area, price ranges or "from" prices, booking or quote form with 3 to 5 fields, hours. Track calls (handoff to `measurement`).

### 8.3 B2B demo or trial page
Headline with job outcome, logos of similar companies, product screenshot or 60 to 90 second video, 3 outcomes with numbers, integration logos, security and compliance badges (SOC 2, ISO 27001, GDPR), short form with instant scheduling. See [SaaS and pricing](saas-and-pricing-pages.md).

### 8.4 App install LP
Store badges, QR code for desktop visitors, ratings from the store, screenshots, deep link that preserves campaign parameters. Platform store pages are the real landing page for most app campaigns; test custom product pages (App Store) and custom store listings (Google Play).

### 8.5 Pre-sell page for cold social (advertorial, listicle, quiz)
Used when cold Meta or TikTok traffic is not ready for a PDP. Must be labeled as advertising where required, contain no fake editorial branding, no fake news site styling, and no claims the brand cannot substantiate. Quiz funnels: 4 to 7 questions, show progress, capture email before the result only if the result is clearly worth it, map each result to a specific product or plan.

### 8.6 Webinar or event registration
Date, time with time zone, duration, speaker credentials, 3 learnings, seats or replay availability (true only), 2 to 3 fields.

### 8.7 AI referral and comparison landing pages (organic)
Visitors from ChatGPT, Perplexity, Copilot and Gemini arrive pre-informed and often on deep pages. Adobe reported AI-referred retail visits converting 42% better than non-AI traffic in March 2026 and 54% better in May 2026, after converting 38% worse in March 2025 [Study, 2026]. Make these pages: specs table, price, comparisons with named alternatives, "best for" statements, clear path to buy or book, consistent facts with what AI assistants say about you. Coordinate with `ai-search-optimization` and `seo`.

## 9. Proof placement rules

| Visitor doubt | Proof type | Place it |
|---------------|-----------|----------|
| "Does it work?" | Results, before and after (compliant), case studies with numbers | Next to the benefit it proves |
| "Is it for someone like me?" | Testimonials from the same segment, logos from the same industry | Hero proof strip and near CTA |
| "Is this company legit?" | Review platform rating, press, years in business, address, team | Hero strip, footer, near payment |
| "Will I regret it?" | Guarantee, return stats, cancel policy | Under CTA and in cart |
| "Is the price fair?" | Comparison table, cost per day, competitor price, ROI calculator | Next to price |

Review widgets with fewer than about 10 reviews can hurt more than help; show a qualitative quote instead until volume grows [Practitioner consensus]. All testimonials must be real and represent typical results or disclose otherwise (see [Offer and copy](offer-and-copy.md) on legal limits).

## 10. SEO and paid page coexistence
- Paid-only variants of an indexable page: add `<meta name="robots" content="noindex">` or canonical to the main page to avoid duplicate content.
- Never block paid LPs with robots.txt if Google Ads, Microsoft Ads or OpenAI ad review bots need to crawl them. OpenAI's ad review crawler (OAI-AdsBot) must reach the landing page or approval stalls [Unverified, secondary sources 2026].
- AI Max for Search and Performance Max can send traffic to any page on the domain when final URL expansion is on. Every indexable page must be ad-ready, or the channel agent must exclude URLs (hand to `google-ads`).

## 11. Wireframe templates

Cold social, ecommerce hero product (mobile):
```
[Logo]                              (no nav)
H1: <Outcome in customer words>
Sub: <For whom + mechanism>
[Hero image/video: product in use, 4:5]
[Primary CTA: Shop now, $49]  Free shipping over $60
*****  4.8 from 2,314 reviews
---
3 benefit blocks with photos
UGC strip (3 short videos or photos)
How it works (3 steps)
Comparison: us vs typical alternative
Reviews (filterable, most helpful first)
Offer box: bundles, savings, guarantee
FAQ (6 items)
Final CTA + guarantee
[Sticky CTA bar after first scroll]
```

Lead gen, non-brand search (desktop):
```
[Logo]                                   [Phone number, click to call]
H1: <Keyword-matched outcome>            | Form card: 3 to 5 fields
Sub: <Differentiator + proof number>     | CTA: Get my free quote
3 checkmark bullets                      | Privacy line, response time
Logos / ratings strip
How it works (3 steps) | Pricing guide or ranges | Reviews | FAQ | Form again
```

## 12. Pre-launch checklist (every LP)
1. Headline and offer match the top 3 ads pointing to it (screenshot pairs saved).
2. First screen shows headline, value, CTA and proof on a 390 x 844 viewport.
3. One primary CTA. Exits counted and justified.
4. Price, shipping, guarantee and key terms visible before the ask.
5. LCP under 2.5 s and CLS under 0.1 on a mid-range phone in field or lab test.
6. Form tested end to end; lead lands in CRM; conversion fires once (check with the `measurement` agent).
7. Tested inside the Meta, Instagram, TikTok and LinkedIn in-app browsers when those channels send traffic.
8. Accessibility: keyboard reachable CTA and form, labels, contrast, alt text.
9. Legal: claims substantiated, testimonials real, required disclosures present.
10. Analytics: page tagged with experiment and variant IDs if part of a test.
