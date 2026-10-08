# International Storefronts

Markets, languages, currencies, local formats, right-to-left layouts, local payments and legal display rules, with country modules for Turkey, the Netherlands, Germany and Arabic RTL markets (Saudi Arabia, UAE). Pattern P61 and P62 in the [Pattern library](ux-pattern-library.md); payments in [Checkout and payments](checkout-and-payments.md). hreflang, URL structure for search engines and international SEO decisions belong to `seo`; legal wording to `compliance`.

## 1. Platform facts (Shopify Markets and others)

| Fact | Source | Label |
|------|--------|-------|
| Markets drive currency, catalogs, price lists, languages, domains or subfolders; Markets and Catalogs moved to the main admin navigation | Shopify Help Center and coverage | [Official, 2026] |
| Catalog currency set in "Set prices in"; buyers still browse and pay in their market currency; no price list means converted base prices | Shopify Help Center and dev docs | [Official] |
| Managed Markets adaptive pricing (duties, taxes, FX, merchant of record fees; FX stabilized for a week) for merchants who joined before 2025-10-14 from 2026-03-26 | Shopify changelog | [Official, 2026-03] |
| Duties-inclusive pricing for Managed Markets, guaranteed at checkout (2026-07-10); DDU support ended 2026-08-24 with automatic conversion to DDP | Shopify changelog and coverage | [Official, 2026-07] [secondary on DDU details] |
| Automatic hreflang with an admin toggle (2026-07); Storefront API 2026-10 `@inContext` accepts `channelId` | Coverage of Shopify changelog | [Unverified, 2026-07] |
| Market-driven shipping model reported from 2026-10-01 with migration by 2027-07-01 | Single blog | [Unverified] |
| Horizon 4.2.0 renders `dir="{{ request.locale.direction }}"` and logical CSS for alignment; fixes for RTL prices, popovers and scroll hints | Horizon release notes | [Official, 2026-09] |
| Liquid `localization` object: `available_countries`, `available_languages`, `market`, `country`, `language`; `market` has `metafields` | Shopify theme-liquid-docs | [Official, 2026-10] |

Other platforms: WooCommerce needs multilingual and multicurrency plugins (WPML with WooCommerce Multilingual, Polylang, TranslatePress, or a currency switcher); Shopware has sales channels with languages, currencies and domains built in; Adobe Commerce uses websites, stores and store views; headless stacks route by locale and market (Saleor Paper `/{locale}/{channel}/...` with translated slugs; Medusa `[countryCode]` routes with a region map in middleware).

## 2. Market and locale UX rules

1. Country decides currency, taxes, shipping, payment methods and legal texts; language is a separate choice.
2. Suggest, never force: a dismissible banner "Shopping from Germany? Switch to EUR and German" with the choice remembered; no IP redirect without a way back; never redirect bots (coordinate with `seo`).
3. Selector shows country names (optionally in their own language) with currency ("Deutschland (EUR)"); languages listed by their own names ("Türkçe", "العربية"); no flags for languages.
4. Prices always in the market currency with the correct format and tax display; never show a converted price that checkout will not charge.
5. Content per market: delivery times, return windows, payment icons, size systems, holidays, legal pages.
6. Translations by humans for the top templates and checkout-adjacent text; machine translation reviewed for product data at scale; glossary for product terms.
7. Layout survives 35% text expansion (German, Finnish) and contraction (Chinese, Japanese).

## 3. Formatting reference

| Item | Rule | Example |
|------|------|---------|
| Currency format | `Intl.NumberFormat(locale, {style: 'currency', currency})` or Liquid money filters per market | de-DE: 1.299,90 €; nl-NL: € 1.299,90; tr-TR: ₺1.299,90; ar-SA: Arabic or Latin digits per locale settings |
| Decimals | Follow currency (JPY 0, KWD and BHD 3) | 12,500 IDR has no decimals in practice |
| Dates | Locale format; avoid ambiguous 03/04 | de: 9. Okt. 2026; tr: 9 Ekim 2026 |
| Units | Metric by default in EU, TR, GCC; size systems per market | EU shoe sizes, cm and kg |
| Phone | Country code selector; store E.164 | +90 5xx xxx xx xx |
| Pluralization | `Intl.PluralRules`, Shopify translation keys with plural forms | Arabic has six plural categories |
| Casing | Locale-aware lowercasing (Turkish dotted and dotless i) | "IŞIK".toLocaleLowerCase('tr') gives "ışık" |
| Sorting | `Intl.Collator(locale)` | Turkish ç, ğ, ı, ö, ş, ü ordering |
| Numbers in RTL | Wrap prices and codes in `<bdi>` or `dir="ltr"` spans | Order numbers, SKUs, discount codes |

## 4. RTL implementation checklist

- `<html lang="ar" dir="rtl">` from the locale (Shopify: `request.locale.direction`; headless: from the route locale).
- CSS logical properties everywhere: `margin-inline-start`, `padding-inline-end`, `inset-inline-start`, `text-align: start`, `border-inline-start`. Search for `left` and `right` in CSS and settings that store physical values (Horizon converted these to logical start and end in 4.2.0).
- Mirror directional icons (arrows, chevrons, back buttons, progress direction, drawer slide direction); do not mirror logos, media play icons, checkmarks, clocks, or product images.
- Carousels: set direction (Embla supports a `direction: 'rtl'` option); swipe semantics follow reading direction.
- Popovers and dropdowns anchor to the logical start (Horizon fixed popovers glued to the physical left in 4.2.0).
- Mixed content: Latin product names, SKUs, prices and URLs inside Arabic text need `<bdi>`; test discount codes and gift card codes.
- Fonts: Arabic-capable font stack with adequate line height (about 1.6 to 1.8 for body); avoid letter-spacing on Arabic text (it breaks joining).
- Forms: labels and inputs align to start; phone and email inputs stay LTR (`dir="ltr"` on the input) with RTL labels.
- Numerals: follow the locale; do not force Eastern Arabic digits unless the market expects them; keep consistency between storefront, checkout and emails.
- Test with real Arabic content (not reversed English) and with long names.

## 5. Country module: Turkey

| Area | Requirement or expectation | Label |
|------|----------------------------|-------|
| Payments | Credit cards with installments (taksit) via bank loyalty programs (Bonus, Maximum, World, Axess, CardFinans, Paraf, Advantage); TROY domestic scheme (25.3% of card transaction value in 2025, 90 million cards); domestic acquiring required for TROY and installments; foreign acquiring lowers approval rates | [Official, BKM 2026-01] [Study, Worldline 2024] |
| Gateways | Shopify Payments not available; local gateways such as iyzico and PayTR, or international PSPs with Turkish acquiring | [Practitioner consensus] |
| PDP | Installment table near the price ("Taksit seçenekleri") pulled from the gateway; state who pays the markup | [Practitioner consensus] |
| Checkout | Pre-information form (Ön Bilgilendirme Formu) and distance sales contract (Mesafeli Satış Sözleşmesi) shown and acknowledged before order; 14-day withdrawal right under the Distance Contracts Regulation | [Official, Turkish regulation] |
| Consent | KVKK privacy notice (aydınlatma metni) separate from explicit consent; commercial message consent through the İYS registry (with `lifecycle-crm` and `compliance`) | [Official] |
| Invoices | e-Arşiv or e-Fatura by email; invoice download in account | [Practitioner consensus] |
| Price display | Price reductions have their own reference price rules; ask `compliance` before showing compare-at prices | [Unverified] |
| Language | Turkish locale-aware casing and sorting; search must match "i/İ/ı/I" variants | [Official, Unicode] |
| Delivery | Couriers (Yurtiçi, Aras, MNG, PTT and others), phone required, same-day in large cities as a differentiator | [Practitioner consensus] |
| Trust | Show the registered company name, MERSİS or tax details in the footer as required; customer service phone | [Unverified on exact fields] |

## 6. Country module: Netherlands

| Area | Requirement or expectation | Label |
|------|----------------------------|-------|
| Payments | iDEAL first, shown as iDEAL \| Wero since 2026-Q1 (co-branding deadline 2026-03-31); Wero contract and integration from Q4 2026; iDEAL planned to end 2027-12-31; then cards, Apple Pay, PayPal, Klarna | [Official, 2026] |
| Address | Postcode plus house number lookup; pickup points (PostNL, DHL) | [Practitioner consensus] |
| Language | Dutch primary; English accepted for some segments, but checkout and legal texts in Dutch | [Practitioner consensus] |
| Trust | Thuiswinkel Waarborg membership badge only if a member; clear returns and KvK number in footer | [Practitioner consensus] |
| Accessibility | ACM actively testing large webshops (2026-03 report), complaints via ConsuWijzer | [Official, 2026-03] |
| Delivery promise | Next-day delivery is the norm for many categories; show cut-off times | [Practitioner consensus] |

## 7. Country module: Germany

| Area | Requirement or expectation | Label |
|------|----------------------------|-------|
| Payments | PayPal (28.5%) and invoice (25.8%) lead, then direct debit (17.3%) and cards (12.3%) of 2024 online purchases; Klarna and wallets common; giropay ended 2024-06-30 | [Study, EHI 2025] |
| Order button | Final button states the payment obligation ("zahlungspflichtig bestellen" or equally unambiguous, § 312j BGB) | [Official] |
| Withdrawal | Widerrufsbutton under § 356a BGB from 2026-06-19 (published 2026-02-05) | [Official, 2026-02] |
| Prices | "inkl. MwSt." and "zzgl. Versandkosten" with link near prices; unit price (Grundpreis) per kg, l, m or 100 g, 100 ml close to the total price (PAngV); 30-day prior lowest price for reductions | [Official] |
| Legal pages | Impressum, Datenschutz, AGB, Widerrufsbelehrung reachable from every page; accessibility statement under BFSG | [Official] |
| Accessibility | BFSG implements the EAA; early enforcement via UWG competitor letters | [Practitioner reports, 2026-04] |
| Trust | Trusted Shops or similar badges only with active membership; reviews with verification info | [Practitioner consensus] |
| Delivery | DHL Packstation and Postfiliale options, delivery to neighbor preferences | [Practitioner consensus] |
| Text length | German strings about 30% to 35% longer; test buttons, chips and navigation | [Practitioner consensus] |

## 8. Country module: Arabic RTL markets (Saudi Arabia, UAE)

| Area | Requirement or expectation | Label |
|------|----------------------------|-------|
| Direction | Full RTL layout for Arabic; English version LTR; switching keeps the same page | [Official W3C i18n practice] |
| Payments | KSA: mada debit and Apple Pay prominent, STC Pay, Tabby and Tamara BNPL, COD; UAE: cards, Apple Pay, Tabby, Tamara, COD (reported 25% to 30% of orders, higher outside Dubai and for first-time buyers) | [Unverified, vendor sources 2026] |
| Gateways | Shopify Payments not available in UAE or KSA; use gateways such as Tap, Moyasar, Checkout.com, Telr, PayTabs | [Unverified, vendor sources 2026] |
| COD rules | Offer COD for first orders and lower order values; limit for high-value, fragile or perishable items; confirm orders by phone or WhatsApp to cut refusals | [Practitioner consensus] |
| Taxes | VAT 15% (KSA), 5% (UAE); prices shown VAT-inclusive for consumers | [Official] |
| Currency | SAR, AED formatting per locale; avoid mixing Arabic-Indic and Latin digits inconsistently | [Practitioner consensus] |
| Addresses | KSA national address fields; phone required with country code | [Practitioner consensus] |
| Content | Modest imagery norms for some categories; Ramadan, Eid, White Friday and national day calendars (with `offer-strategy`) | [Practitioner consensus] |

## 9. International QA matrix

For each market: locale banner and selector; prices in PLP, PDP, cart and checkout match; taxes and duty display; shipping threshold text and progress bar per market; payment icons equal methods available; delivery estimates per market; legal links per market; translations complete on templates, notifications and checkout; RTL checks where relevant; search in the local language (stemming, synonyms, casing); test order per market in test mode with `measurement` verification.

## 10. Measurement

Segment every storefront KPI by market and language. Watch: CVR by market vs domestic, payment method share vs expectation, checkout completion by method, locale banner acceptance rate, selector usage, returns by market.
