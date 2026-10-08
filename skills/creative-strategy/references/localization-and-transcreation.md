# Localization and Transcreation

> Knowledge as of 2026-10. Scope: adapting ads, landing pages and emails across languages and markets, with Turkish, English, Dutch, German and Arabic as worked examples: translation vs transcreation, the workflow with native review, glossary and claims consistency, typography and length, right to left layout and mirrored creative, local proof (reviews, payment and delivery signals, currency formats), cultural and seasonal hooks, platform language targeting rules and a scored QA checklist. Claims law sits with `compliance`; hreflang and URL structure with `seo` ([International SEO](../../seo/references/international-seo.md)); mobile rendering of long strings with `cro` ([Mobile and in-app browsers](../../cro/references/mobile-and-in-app-browsers.md)).

## 1. Translation, transcreation or original creation

| Approach | What it is | Use when | Output | Risk |
|----------|-----------|----------|--------|------|
| Translation | Same meaning, same structure | Specs, legal text, size charts, checkout, transactional email, help content | Faithful text; glossary terms fixed | Literal hooks fall flat; idioms break |
| Transcreation | Same intent and emotional effect, new words, sometimes new visuals | Headlines, hooks, video scripts, subject lines, offers, CTAs | A new line that does the same job, with a back translation for approval | Drifts from approved claims if unmanaged |
| Original creation | New concept for the market | Market specific angle (local pain, season, competitor, payment habit) | New concept in the creative registry | Costs more; needs local VOC |

Decision rule:
1. Is the text legally fixed or factual (price, spec, terms)? Translate.
2. Does it rely on wordplay, idiom, humor, cultural reference or rhythm (hooks, slogans, scripts)? Transcreate.
3. Does the winning angle depend on a local truth the source market lacks (installments in Turkey, cash on delivery in the Gulf, invoice payment in Germany)? Create original concepts and test them against the transcreated master.

## 2. Workflow

| Step | Owner | Output |
|------|-------|--------|
| 1. Source brief | creative-strategy | Master concept, awareness level, intent of each line, claim IDs from `ads-master/brand/CLAIMS.md`, mandatory elements, character limits per placement |
| 2. Market brief | creative-strategy with market-intel | Audience, local competitors and their ad library patterns, seasonal moments, payment and delivery habits, legal flags |
| 3. Glossary and style guide | Native linguist, approved by the human | Brand terms, do-not-translate list, product names, formality level, tone, banned words |
| 4. First draft | Native copywriter, or an AI draft fully edited by a native speaker | Draft per placement plus back translation of every headline and claim |
| 5. Claims check | compliance | Each claim mapped to an approved claim for that market, or routed for review |
| 6. Native review | Second native speaker living in the market | Review sheet with accept, change or reject per line |
| 7. Layout and typography QA | Designer or site-engineer | Screenshots of every placement and page in every language |
| 8. Platform setup | Channel agent | Language and location settings, naming with language code, UTMs with language |
| 9. Approval and launch | Human | Entities created PAUSED, approved, then launched |
| 10. Learn | creative-strategy | Results by language in the creative registry; winning local angles fed back to the master |

Formality is a brand decision per language, written in the style guide and applied consistently:

| Language | Informal | Formal | Typical DTC choice [Practitioner consensus] |
|----------|----------|--------|---------------------------------------------|
| Turkish | sen | siz | siz in most ads and all transactional text; sen for youth brands |
| German | du | Sie | du for lifestyle DTC, Sie for B2B, finance, health |
| Dutch | jij, je | u | jij for most consumer brands, u for finance, government, older audiences |
| Arabic | Gender and register vary by dialect | Modern Standard Arabic | MSA for broad Gulf campaigns; dialect (Gulf, Egyptian) for social video when natives write it |
| English | you | you | Market spelling (UK vs US) and vocabulary (trainers vs sneakers) |

## 3. Glossary and claims consistency

Glossary template (one row per term, kept in `ads-master/brand/` next to the claims register):

| Term (source) | Turkish | German | Dutch | Arabic | Do not translate | Notes |
|---------------|---------|--------|-------|--------|------------------|-------|
| Free shipping | Ücretsiz kargo | Kostenloser Versand | Gratis verzending | شحن مجاني | | Only where true for that market's threshold |
| Subscription | Abonelik | Abo | Abonnement | اشتراك | | |
| Brand name | | | | | Yes | Never translated or transliterated without approval |
| Product line names | | | | | Usually yes | Check trademark status per market |

Claims rules:
1. A claim approved in one language is not approved in another. Each market has its own law, regulator and platform policy; the translation itself can change the claim ("helps" becomes "cures" in a careless translation).
2. Keep claims as IDs. Every localized line that carries a claim references the claim ID and the market status (approved, needs review, blocked) in CLAIMS.md.
3. Route through compliance: health and nutrition claims (EU Regulation 1924/2006 in the Netherlands and Germany), price reduction claims (EU Price Indication Directive Article 6a, prior lowest price in the last 30 days), comparative and superlative claims ("best", "number 1", "Testsieger" needs a licensed, current test source), environmental claims, and Turkish advertising rules enforced by the Ministry of Trade's Advertising Board. Labels: [Official] for the EU texts; country specifics are for compliance to verify.
4. Reviews and testimonials: never present a translated review as if the customer wrote it in that language. Show the original with a "translated from" note, or use reviews from that market.
5. Prices, thresholds and guarantees differ by market: rebuild offer lines from the market's facts, never translate a number.

## 4. Typography, length and layout

### 4.1 Length

Expect German and Dutch copy to run about 20% to 35% longer than English, and very short strings (buttons, badges) to grow by up to double; Turkish words get long through suffixes [Practitioner consensus, W3C text size guidance]. Design with this budget:

| Element | Rule |
|---------|------|
| Buttons and badges | Width from content with `min-width`, never a fixed width; test the longest language |
| Headlines on statics | Leave 30% spare width; prepare a shorter transcreation for tight placements |
| Platform limits | Character limits are the same in every language; write per language to the limit (RSA 30 and 90, Meta primary text visible lines), do not truncate a translation |
| Video subtitles | Max about 2 lines; re-time captions per language; reading speed drops with long compounds |

### 4.2 Turkish dotted and dotless i

Turkish has four letters: i and İ (dotted), ı and I (dotless). Generic casing gets them wrong.

| Operation | Wrong | Right | Fix |
|-----------|-------|-------|-----|
| Uppercase "indirim" | INDIRIM | İNDİRİM | `lang="tr"` on the page or element so CSS `text-transform: uppercase` applies Turkish case mapping [Official, MDN]; in JS `toLocaleUpperCase("tr-TR")` [Official, MDN] |
| Lowercase "İSTANBUL" | i̇stanbul (i plus a combining dot) | istanbul | `toLocaleLowerCase("tr-TR")` |
| Uppercase "ışık" | ISIK | IŞIK | Same; and the font must have the glyphs |
| Design tools | Text case set to uppercase in the design file | Type the correct capitals or set the language | Proof exported statics letter by letter |
| Search, coupon codes, form validation | Case-insensitive compare fails for İ and ı | Normalize with the locale, or compare codes as entered | site-engineer |

German: `text-transform: uppercase` turns ß into SS; long compounds ("Versandkostenfreigrenze") need `hyphens: auto` with `lang="de"`. Dutch: the digraph ij capitalizes as IJ ("IJsselmeer"), which CSS handles with `lang="nl"` [Official, MDN].

### 4.3 Fonts

- Turkish needs Latin Extended-A glyphs (ğ, ş, ı, İ): load the `latin-ext` subset or a font file with those glyphs; many display fonts lack İ and ı and the browser silently falls back to another font mid word.
- German and Dutch need ä, ö, ü, ß, ë, ï and the euro sign; check the display font, not only the body font.
- Arabic needs an Arabic script font with proper shaping (for example Noto Sans Arabic or IBM Plex Sans Arabic); never add letter spacing to Arabic (it breaks letter joining), avoid synthetic italics, increase line height.
- Test with real strings in the real font in the real placement; a glyph fallback is visible on statics and in video titles.

### 4.4 Right to left and mirrored creative

| Area | Rule |
|------|------|
| Page direction | `<html lang="ar" dir="rtl">`; CSS logical properties (`margin-inline-start`, `padding-inline-end`, `inset-inline`) instead of left and right [Official, W3C] |
| Mixed text | Wrap Latin brand names, numbers, prices, SKUs and URLs in `<bdi>` or set `dir="auto"` on user content |
| Icons | Mirror directional icons (arrows, chevrons, back and forward, progress); do not mirror logos, media play buttons, clocks, checkmarks or brand marks |
| Layout | Reading order flows right to left: carousels advance leftward, step indicators run right to left, primary CTA sits where the eye ends |
| Statics and video | Rebuild layouts, not just flip them: text block on the right, product facing into the text; check that flipping the image does not reverse text on packaging or show the product mirrored |
| Platform overlays | Re-check safe zones for each platform UI in RTL languages |
| Numbers | Decide Western digits or Arabic-Indic digits per market and set `numberingSystem` explicitly in Intl formatting; defaults differ by locale and engine |

### 4.5 Numbers, currency and dates

| Locale | Number | Currency display | Date | Notes |
|--------|--------|------------------|------|-------|
| en-US | 1,234.56 | $1,234.56 | 10/08/2026 | Month first |
| en-GB | 1,234.56 | £1,234.56 | 08/10/2026 | Day first |
| tr-TR | 1.234,56 | ₺1.234,56 (Intl default) or 1.234,56 TL (common in retail) | 08.10.2026 | Pick one style for the brand; prices include KDV (VAT) |
| nl-NL | 1.234,56 | € 1.234,56 | 08-10-2026 | Prices include BTW |
| de-DE | 1.234,56 | 1.234,56 € | 08.10.2026 | Prices include MwSt.; shipping cost shown near price |
| ar-AE, ar-SA | Locale dependent digits | Amount with AED or SAR; position follows locale data | Day first | Test both digit systems with the native reviewer |

```js
const price = (amount, locale, currency) =>
  new Intl.NumberFormat(locale, { style: "currency", currency }).format(amount);
price(1234.56, "tr-TR", "TRY"); // "₺1.234,56"
price(1234.56, "nl-NL", "EUR"); // "€ 1.234,56"
price(1234.56, "de-DE", "EUR"); // "1.234,56 €"
new Intl.NumberFormat("ar-SA", { style: "currency", currency: "SAR", numberingSystem: "latn" }).format(1234.56);
new Intl.PluralRules("ar").select(2); // "two": Arabic has six plural categories; never hard code "s"
```

Also localize units (cm vs inches), clothing and shoe sizes (EU, UK, US), address formats and phone formats in forms.

## 5. Local proof

Trust signals do not travel. A Trustpilot badge persuades in the UK; in the Netherlands and Germany buyers look for their own marks; in Turkey and the Gulf payment and delivery reassurance often matters more than review badges [Practitioner consensus].

| Market | Payment signals | Delivery signals | Review and trust signals |
|--------|-----------------|------------------|--------------------------|
| Turkey | Installments (taksit) on credit cards; troy (the domestic card scheme), Visa, Mastercard; bank transfer (havale or EFT); cash on delivery (kapıda ödeme) where offered | Same day dispatch, named carriers, free shipping threshold in TL | Marketplace ratings, complaint handling reputation (Şikayetvar), ETBİS e-commerce registration badge [verify display rules with compliance] |
| Netherlands | iDEAL, now co-branded "iDEAL \| Wero" (merchant co-branding window ended 2026-03-31; Wero offered to buyers from Q4 2026; iDEAL decommission planned for 2027-12-31 with some PSPs estimating 2027 to 2028) [Official, iDEAL and Stripe, 2026; end date Contested]; cards, PayPal, Klarna | "Voor 23:59 besteld, morgen in huis" style next day promises, PostNL or DHL, free returns | Thuiswinkel Waarborg, Kiyoh, Trustpilot |
| Germany | PayPal, Klarna (Kauf auf Rechnung, invoice), SEPA direct debit, cards | DHL, Packstation, delivery date, kostenloser Rückversand (free returns) | Trusted Shops, eKomi, test results with license and date |
| UK, US | Apple Pay, Google Pay, PayPal, Klarna, Clearpay (UK), Afterpay and Affirm (US), Shop Pay | Delivery date, free returns window | Trustpilot (UK), Google and on-site reviews |
| Gulf (UAE, Saudi Arabia) | Cash on delivery, Apple Pay, mada (Saudi debit scheme), Tabby and Tamara (installments), cards | Delivery by date, same day in major cities, easy returns | Google reviews, marketplace ratings, local phone and WhatsApp support |

Rules:
1. Show the payment logos the market recognizes near the price and in the ad when payment is a barrier (installments in Turkey, invoice in Germany, COD in the Gulf), but only methods the checkout really offers in that market (verify with commerce and payment provider).
2. Prices in local currency with local tax wording; no currency conversion in the ad.
3. Testimonials from customers in that market and language; disclose translations.
4. Local contact options: local phone format, WhatsApp in Turkey and the Gulf, local address or returns address in the EU.

## 6. Cultural and seasonal hooks

| Market | Moments (dates vary; verify each year) | Hooks that tend to work | Cautions |
|--------|----------------------------------------|------------------------|----------|
| Turkey | Ramazan Bayramı and Kurban Bayramı (Islamic calendar, about 11 days earlier each year), Mother's Day (second Sunday of May), Father's Day (third Sunday of June), November sales season, New Year gifts (Yılbaşı), back to school (September) | Gifting, family, installments, fast delivery before the holiday | Religious holidays are family time; avoid trivializing them; delivery cutoffs before Bayram |
| Netherlands | Koningsdag (27 April, or 26 April when the 27th is a Sunday), Sinterklaas (pakjesavond 5 December), Black Friday, summer holidays | Directness, value, sustainability backed by facts, humor | Overclaiming reads as untrustworthy; Sinterklaas and Christmas are separate moments |
| Germany | Advent and Christmas, Black Week, Mother's Day (second Sunday of May), Father's Day (Ascension Day), summer sales | Specs, proof, test results, data protection, quality | Superlatives need proof; privacy sensitivity; Christmas delivery cutoffs |
| UK, US | Black Friday and Cyber Monday, Boxing Day (UK), Mother's Day (UK: Mothering Sunday in March or April; US: second Sunday of May), Prime Day, back to school | Benefit led, social proof, urgency only when true | Mother's Day dates differ between the UK and US |
| Gulf | Ramadan (2027 expected to start around 2027-02-08, moon sighting decides), Eid al-Fitr, Eid al-Adha, White Friday (the Black Friday name used by some Gulf retailers), Saudi Founding Day (22 February), Saudi National Day (23 September), UAE National Day (2 December) | Generosity, family, evening and late night timing during Ramadan, premium gifting | Modest imagery; respectful use of religious and national symbols; shift ad schedules to evening and late night during Ramadan; national day creative must use symbols correctly |

## 7. Platform language targeting rules

| Platform | Control | Rule (2026-10) | Setup |
|----------|---------|----------------|-------|
| Google Ads | Manual language targeting removed from Search campaigns and from Performance Max on the Search Network in late 2026-09 (announced 2026-08-14); matching uses the language of the ad and landing page, the query and user settings; PMax language settings still apply to YouTube, Display, Discover and Gmail [Official, 2026-08 to 2026-09] | Language is now a property of the ads and the page | One language per campaign or ad group, landing page in the same language; see [Google Ads search campaigns](../../google-ads/references/search-campaigns.md) |
| Meta | Language is a hard control in audience settings; Meta advises leaving it blank unless the language is uncommon in the chosen location [Official, Meta Help; verify wording]. Multi-language ads let you add translations to one ad, delivered by the viewer's language; auto-translate exists [Official] | Use creative language plus location; use the language control for bilingual or expat targeting | Separate ad sets per language only when budgets allow learning; native QA before enabling auto-translate |
| TikTok | Language targeting optional; creative language is the real filter | Do not narrow by language unless the market is multilingual | Native creators per language |
| LinkedIn | Profile language (the member's interface language) is a required campaign setting [Official, LinkedIn Help; verify] | Many professionals use English interfaces in non-English markets | Run English and local language versions as separate campaigns in markets like the Netherlands, Germany, Turkey and the Gulf |
| Microsoft Ads | Language set per campaign or ad group; ad text should match [Official, verify after the Google change since imports may differ] | Check imported campaigns | Keep one language per ad group |
| Email and SMS | Language from the stored customer preference or the storefront language at signup, not from IP | One template per language; RTL email templates need `dir="rtl"` in the HTML | lifecycle-crm owns sending |

Bilingual and multilingual markets to plan explicitly: Belgium (Dutch and French), Switzerland (German, French, Italian), the UAE (Arabic and English), Turkey (Turkish plus English for expats and tourists). Name campaigns and ads with a language code (`_tr`, `_de`, `_nl`, `_ar`, `_en`) and carry it in `utm_content` so results split by language.

## 8. Landing pages and email

1. One URL per language (subfolder or ccTLD), reciprocal hreflang, no automatic redirects by IP; a visible language switcher (seo).
2. Ad language = landing page language = checkout language. A Turkish ad that lands on an English page loses the click.
3. Currency follows market, not language (English speakers in the Netherlands still pay in euros with Dutch payment methods).
4. Emails: localized subject and preheader written to the language's length, sender name localized where the brand allows, legal footer per market, unsubscribe in the same language.
5. Check machine translated widgets: browser or app auto-translation of the page can garble prices and legal text; mark brand names and prices `translate="no"`.

## 9. QA checklist (score before launch)

| ID | Check | Severity |
|----|-------|----------|
| L1 | Native reviewer living in the market signed off every line | Critical |
| L2 | Every claim mapped to an approved claim for that market (CLAIMS.md) | Critical |
| L3 | Prices, thresholds, guarantees and offers rebuilt from that market's facts | Critical |
| L4 | Ad, landing page and checkout in the same language | High |
| L5 | Glossary terms and brand names consistent; do-not-translate list respected | High |
| L6 | Formality (sen or siz, du or Sie, jij or u) consistent across ad, page and email | High |
| L7 | No truncation or overflow in any placement (screenshots attached) | High |
| L8 | Turkish İ, ı, ş, ğ correct in uppercase text, statics and video titles | High |
| L9 | Fonts contain every glyph; no fallback mid word | High |
| L10 | RTL layout rebuilt and directional icons mirrored (Arabic) | High |
| L11 | Number, currency, date and plural formats per locale | Medium |
| L12 | Payment and delivery signals match what checkout offers in that market | Medium |
| L13 | Reviews from the market or translations disclosed | Medium |
| L14 | Seasonal hook dates verified for this year | Medium |
| L15 | Platform language settings per section 7; naming and UTMs carry the language code | Medium |
| L16 | Subtitles and voiceover by native speakers; AI voice or translation disclosed where required (see [Compliance and disclosure](compliance-and-disclosure.md)) | Medium |
| L17 | Units, sizes, address and phone formats localized | Low |
| L18 | Back translations stored with the approval | Low |

Score: Critical 10, High 5, Medium 2, Low 1 per passed item. Do not launch with a failed Critical item.

## 10. AI in localization

- Machine translation and LLM drafts are acceptable as first drafts; a native editor owns the final text, and claims always go through compliance.
- Give the model the glossary, style guide, claim IDs and character limits; ask for three transcreation options per headline with back translations.
- Platform auto-translate and AI voice translation (Meta and others) only after native review of a sample; keep them off for regulated categories.
- Log which assets used AI translation or voice in the creative registry for disclosure and learning.

## 11. Measurement

- Report CTR, CVR, CPA and ROAS by language and market, not blended across languages.
- Compare markets on contribution and nCAC in local economics; currency and purchasing power make raw CPA comparisons misleading.
- Test transcreated vs translated versions of the same concept in the same market at least once per market; record the result in EXPERIMENTS.md.

## 12. Sources

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | Text size in translation | W3C Internationalization | https://www.w3.org/International/articles/article-text-size.en | n.d. | Expansion of short and long strings |
| 2 | text-transform (language specific case mapping) | MDN | https://developer.mozilla.org/en-US/docs/Web/CSS/text-transform | n.d. | Turkish i, German ß, Dutch IJ |
| 3 | String.prototype.toLocaleUpperCase | MDN | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLocaleUpperCase | n.d. | Locale aware casing in JS |
| 4 | Intl.NumberFormat | MDN | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/NumberFormat | n.d. | Currency and number formats |
| 5 | Structural markup and right-to-left text in HTML | W3C Internationalization | https://www.w3.org/International/questions/qa-html-dir | n.d. | dir attribute, bidi isolation |
| 6 | iDEAL \| Wero branding | iDEAL | https://ideal.nl/en/ideal-wero-branding | 2026 | Co-branding dates |
| 7 | iDEAL to phase into Wero starting in 2026 | ABN AMRO | https://www.abnamro.com/en/news/ideal-to-phase-into-wero-starting-in-2026 | 2025 to 2026 | Migration phases |
| 8 | iDEAL to Wero migration | Stripe Support | https://support.stripe.com/questions/ideal-to-wero-migration | 2026 | PSP view of the end date (2027 to 2028) |
| 9 | Google Ads is retiring language targeting in Search campaigns | Search Engine Journal | https://www.searchenginejournal.com/google-is-removing-language-targeting-from-search-campaigns/585592/ | 2026-08 | Language setting removal |
| 10 | About language targeting | Google Ads Help | https://support.google.com/google-ads/answer/1722078 | n.d. | Current language matching rules |
| 11 | Directive (EU) 2019/2161 (Omnibus, price reduction rules) | EUR-Lex | https://eur-lex.europa.eu/eli/dir/2019/2161/oj | 2019 | Prior lowest price rule |
| 12 | Regulation (EC) No 1924/2006 on nutrition and health claims | EUR-Lex | https://eur-lex.europa.eu/eli/reg/2006/1924/oj | 2006 | Health claims in EU markets |
