# Listing Optimization

> Knowledge as of 2026-10. Applies to Amazon first, with adaptations for bol, Trendyol, Hepsiburada, Allegro and others. Every word on a listing is customer facing copy: facts from `ads-master/brand/PRODUCT_FACTS.md`, claims from `ads-master/brand/CLAIMS.md`, and a `compliance` pass before publishing.

## 1. What a listing must do

1. Be found: index for the terms customers use (title, bullets, attributes, backend terms, category).
2. Win the click: main image, title start, price, rating, delivery badge.
3. Convert: images, bullets, A+, reviews, Q&A answer the buying questions in order.
4. Be understood by AI shopping assistants: Alexa for Shopping (formerly Rufus) and marketplace assistants read listing text, A+, reviews and Q&A to answer questions and pick products.

## 2. Keyword research procedure

| Step | Source | Output |
|------|--------|--------|
| 1. Seed list | Product facts, customer language from reviews (own and competitors), DTC site search, Google Search Console | 30 to 80 seed terms |
| 2. Marketplace demand | Amazon Brand Analytics Top Search Terms and Search Query Performance (Brand Registry), search box suggestions, Product Opportunity Explorer; bol and Turkish panel search reports where available | Terms with relative volume |
| 3. Competitor terms | Reverse ASIN tools (Helium 10, Jungle Scout, DataHawk and similar), competitor titles | Terms competitors rank and advertise for |
| 4. Ads data | Sponsored Products search term report (60 to 90 days) | Terms that convert for you |
| 5. Prioritize | Relevance (0 to 3) x volume x conversion evidence | Tier 1 (title), Tier 2 (bullets and attributes), Tier 3 (backend) |
| 6. Localize | Native speaker per market: Dutch (NL vs Flemish), German, Turkish, Arabic | Market keyword map |

Rule: relevance beats volume. A high volume term that does not describe the product lowers conversion, and conversion feeds organic rank.

## 3. Amazon title

Rules since 2025-01: 200 characters maximum including spaces for most categories, no special characters (! $ ? _ { } ^ and similar) unless part of the brand name, no word repeated more than twice except articles, prepositions and conjunctions [Official, 2025-01, prior knowledge]. Category style guides can set shorter limits and specific orders.

Formula: `Brand + Product type + Key differentiator + Key attribute (size, material, count) + Variant (color, size)`

| Bad | Good |
|-----|------|
| "Best Premium Yoga Mat!!! Non Slip Yoga Mat Exercise Mat Fitness Mat Gift" | "Brandname Yoga Mat 6 mm, Non-Slip TPE, 183 x 61 cm, with Carry Strap, Sage Green" |

Front-load: the first 70 to 80 characters show on mobile search; put brand, product type and the main differentiator there [Practitioner consensus].

## 4. Bullets (Amazon "About this item")

- Use 5 bullets. Start each with a short benefit label in plain words, then the fact that proves it.
- Order by buying questions: (1) main outcome, (2) key spec or compatibility, (3) material or quality proof, (4) use cases and who it is for, (5) what is in the box, care, warranty or guarantee.
- Write answers to the questions shoppers ask the AI assistant: "Is it safe for X?", "Does it fit Y?", "How long does it last?". Use exact numbers from PRODUCT_FACTS.md.
- Keep each bullet readable (about 150 to 250 characters is common practice) [Practitioner consensus]. Check category limits.
- Banned in listings across Amazon policy: prices, promotions, shipping claims, competitor names, unverifiable superlatives ("best", "number one") without evidence, medical or pesticide claims without authorization [Official, prior knowledge].

## 5. Backend search terms (Amazon)

- Limit: under 250 bytes per field for most marketplaces (multibyte characters such as Turkish, German umlauts or Arabic use more bytes) [Official, prior knowledge].
- Include: synonyms, spelling variants, other languages customers use in that store (for example English terms on Amazon.de), use cases, abbreviations.
- Exclude: brand names (own or competitors), ASINs, words already in the title, repeated words, punctuation, "best", "cheap", temporary terms ("new", "sale"), offensive terms.
- Separate words with spaces; no commas needed. Singular or plural duplicates are generally not needed [Practitioner consensus].
- Check indexing: search the exact term with your ASIN, or use an indexing checker tool, 24 to 72 hours after the update.

## 6. Images and video

| Slot | Content | Specs and notes |
|------|---------|-----------------|
| 1 Main | Product only on pure white (RGB 255,255,255), fills about 85% of the frame | Required for most categories; no text, logos or badges [Official, prior knowledge] |
| 2 | Key benefit infographic | Large text, readable on mobile |
| 3 | Size and dimensions with a reference object | Reduces returns |
| 4 | In use, lifestyle | Show the target user |
| 5 | Features close-up, materials | Proof of quality |
| 6 | Comparison (vs older model or variants, never named competitors) | Comparison claims go to compliance |
| 7 | What is in the box, care | |
| Video | 30 to 60 seconds, demo first 5 seconds, captions | Sponsored Brands video can reuse it; production via `video-studio` |

Size: at least 1000 px on the longest side to enable zoom; 2000 px or more recommended [Official, prior knowledge]. Design for mobile first: test each image at phone size.

## 7. A+ content and Brand Store

| Module | Use |
|--------|-----|
| Brand Story carousel | Brand credibility, links to Brand Store and other products |
| Hero image with text | Main promise |
| Image and text pairs | Features to benefits |
| Comparison chart | Cross-sell own range; reduces wrong purchases |
| Q&A or FAQ style modules (where available) | Answer AI assistant style questions |
| Premium A+ (eligibility by account) | Video, larger modules, interactive hotspots |

Rules: A+ text is indexed differently than title and bullets (do not rely on A+ for keyword indexing) [Contested]; alt text must describe the image factually; no prices, promotions or guarantees outside policy. Test A+ variants with Manage Experiments.

Brand Store: one page per category and a bestsellers page; use Store insights (section-level insights introduced 2026-01 [Secondary]) to remove low engagement sections; link Sponsored Brands to Store pages that match the keyword intent.

## 8. AI shopping assistant readiness (Alexa for Shopping and others)

Alexa for Shopping (formerly Rufus, renamed in the US on 2026-05-13 [Secondary, multiple]) answers questions using listing content, reviews, Q&A and other signals, and shows Sponsored Prompts since 2026-03-25.

Checklist:
- Every common question answered in listing text with a fact: dimensions, compatibility, materials, certifications, age range, care, use cases, who it is not for.
- Consistent facts across title, bullets, attributes, A+, Brand Store and images (contradictions reduce trust and cause wrong answers).
- Structured attributes complete in the catalog (assistants and filters use them).
- Review themes: fix product issues that appear in negative review summaries; the assistant surfaces them.
- Ask the assistant 10 to 20 shopper questions about your product and competitors monthly; log answers in `outputs/marketplaces/` and fix gaps. Treat answers as observations, not ground truth.

## 9. Testing listings

| Tool | Where | How |
|------|-------|-----|
| Manage Experiments | Amazon, Brand Registry, eligible ASINs with enough traffic | A/B test title, main image, bullets, description, A+; run 4 to 10 weeks until Amazon reports a winner probability |
| Before and after | bol, Trendyol, Hepsiburada, others | Change one element, hold 2 to 4 weeks, compare conversion vs control SKUs and prior period; log in EXPERIMENTS.md |
| Main image click tests | Sponsored ads CTR | Use ad CTR by image as a directional signal |

## 10. Marketplace adaptations

| Marketplace | Differences |
|-------------|------------|
| bol | One page per EAN; content from catalog and brand uploads; attributes drive filters; Dutch copy; images per category specs; see [bol](bol-com.md) |
| Trendyol, Hepsiburada | Category attributes critical; Turkish copy; Q&A responsiveness; seller store page; see [Turkey](trendyol-and-hepsiburada.md) |
| Allegro | Parameters (attributes) define filters and search; Polish copy; description with image and text sections |
| Zalando | Brand content standards; size and fit data |
| Etsy | 13 tags, title for Etsy search, personalization fields |
| Walmart | Item content quality score; attributes; images |
| noon, Amazon Gulf | Arabic and English content |

## 11. Listing pack template

```
# Listing pack: <SKU> <marketplace> <language> | Date | Version
Sources: PRODUCT_FACTS.md version, CLAIMS.md version, keyword map file and date
Tier 1 keywords | Tier 2 | Tier 3 (backend)
Title (chars: n / limit)
Bullets 1 to 5 (chars each)
Description or A+ text (module by module)
Backend search terms (bytes: n / 250)
Attributes to fill (list with values)
Image brief (slots 1 to 7, video)
Claims used (each with CLAIMS.md reference)
Compliance status: pending | approved (date, reviewer)
Change request link (G3)
```

## 12. Listing QA checklist

- [ ] Title within limit, formula followed, no banned characters or repeated words.
- [ ] Every fact traceable to PRODUCT_FACTS.md; every claim approved in CLAIMS.md.
- [ ] Bullets answer the top 10 shopper questions.
- [ ] Backend terms under byte limit, no brands or ASINs.
- [ ] Main image compliant; 6 or more additional images; video if possible.
- [ ] A+ published with comparison chart; Brand Story linked.
- [ ] All key attributes filled; variations correct.
- [ ] Localized by a native speaker per market.
- [ ] Indexed for Tier 1 terms (checked 72 hours after publishing).
- [ ] Detail page change monitoring active.
