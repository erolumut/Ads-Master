# Search and Merchandising

On-site search UI, autocomplete, typo tolerance, synonyms, zero results, search results pages, merchandising rules and search tool selection. Patterns P10 to P16 in the [Pattern library](ux-pattern-library.md).

## 1. Evidence snapshot

| Finding | Source | Label |
|---------|--------|-------|
| 46% of desktop, 58% of mobile and 64% of app sites mediocre or worse on search | Baymard search benchmark 2026 | [Study, 2026] |
| 80% of sites offer autocomplete, 19% get all details right | Baymard autocomplete research | [Study] |
| 69% of sites risk misleading users through poor misspelling support in autocomplete | Baymard | [Study] |
| 58% do not support users using autocomplete as a starting point for query building | Baymard | [Study] |
| 12 query types (exact, product type, feature, thematic, symptom, non-product, compatibility, relational, slang and abbreviations, and others) | Baymard query types research | [Study, 2026 article] |
| 37% of apps do not persist search queries | Baymard mobile app 2026 | [Study, 2026] |
| 94% of sites do not allow searching within the current category on mobile | Secondary summary | [Unverified] |
| Infinite scroll harmful on search results; load more performs best | Baymard via Smashing Magazine | [Study, 2016] |
| Reports of a new Shopify search engine rollout from June 2026, SKU search regressions, synonym groups dropped | Competitor vendor and App Store reviews | [Unverified, 2026-06] |
| Athos Commerce formed from Searchspring, Klevu and Intelligent Reach | Vendor sites | [Official vendor, 2025-01] |
| Algolia acquired Velou (catalog enrichment) | Algolia press release | [Official vendor, 2026-10] |

## 2. Search box specification

- Desktop: open input in the header for catalogs above about 30 SKUs, placeholder with examples ("Search dresses, shirts, gift cards"), width at least 27 characters visible.
- Mobile: visible field on home and PLP; icon in sticky header opens a full-screen search with the field focused and the keyboard up.
- Markup: `<form role="search" action="/search" method="get">`, `<input type="search" name="q" enterkeyhint="search" autocomplete="off">` (autocomplete off only for the browser list, the custom suggestions replace it), font size 16 px on mobile to avoid iOS zoom.
- Clear button named "Clear search"; submit button named "Search".

## 3. Autocomplete specification

Content blocks in order:
1. Query suggestions (up to 6 to 8), with the typed part de-emphasized and the completion emphasized.
2. Scope suggestions: "shirts in Men", "shirts in Women" (category scope).
3. Products (4 to 6) with image, title, price; "View all N results".
4. Empty state (focus without text): recent searches (local only), popular searches, top categories.

Behavior:
- Debounce 150 to 250 ms; cancel stale requests (AbortController); ignore responses older than the latest query.
- Keep total suggestions at or under about 10 on desktop and fewer on mobile [Study, Baymard].
- Up and Down move through options and copy the active query suggestion into the field [Study, Baymard: 58% do not copy]; Enter submits the highlighted item; Escape closes and keeps the text.
- Typo tolerance in suggestions; show corrected suggestion with the original query searchable.
- No layout shift: dropdown overlays content; reserve image dimensions.

ARIA combobox (W3C APG):
- Input: `role="combobox"`, `aria-expanded`, `aria-controls="<listbox id>"`, `aria-autocomplete="list"`, `aria-activedescendant="<option id>"` while an option is highlighted.
- Popup: `role="listbox"` with `role="option"` items and `aria-selected="true"` on the highlighted one. Products can live in a second listbox or as grouped options with `role="group"` and a label.
- Status: a polite live region announces "8 suggestions" after results settle (not on every keystroke).

Reference implementations: Horizon `assets/predictive-search.js` and `sections/predictive-search.liquid` (200 ms debounce, AbortController, listbox, Escape, arrow navigation, Shopify `/search/suggest` with `resources[limit_scope]=each`); React Aria `Autocomplete.tsx`, `ComboBox.tsx`; Base UI `autocomplete`, `combobox`; Hydrogen skeleton `SearchFormPredictive.tsx`, `SearchResultsPredictive.tsx`; cmdk for command-palette style search (best for B2B quick order, not consumer search).

## 4. Relevance basics checklist

| Capability | Check query | Expected |
|------------|-------------|----------|
| Typo tolerance | "jakcet", "tshrit" | Jacket, T-shirt results |
| Plural and stemming | "dress" vs "dresses" | Same set |
| Synonyms | "sneakers" vs "trainers", "sofa" vs "couch" | Same set |
| Units and formats | "32gb", "32 gb", "1,5 l" | Same set |
| Product type plus attribute | "black leather boots size 39" | Filters applied or ranked correctly |
| SKU and barcode | Exact SKU, partial SKU | The product |
| Brand | Brand name misspelled | Brand results |
| Non-product | "returns", "shipping", "size guide" | Policy or help page suggestion |
| Thematic | "wedding guest", "gift for dad" | Curated collection or tagged results |
| Compatibility | "case for iPhone 16" | Compatible products only |
| Language | Query in the market's other language (NL store with English query) | Results or suggestion |
| Turkish casing | "IŞIK", "ışık", "isik" | Same set (locale-aware lowercase) |

Run these 12 checks on every audit and after every search configuration change. Record pass, partial or fail.

## 5. Synonym and zero result workflow (weekly for Growth and up, monthly for Starter)

1. Export zero result queries and low click-through queries (Shopify Analytics or search vendor).
2. Classify each: misspelling (fix with typo tolerance or a synonym), vocabulary gap (synonym), catalog gap (product not sold: log for `offer-strategy` and `market-intel`), content gap (help page), noise.
3. Add synonyms as two-way groups only when meanings are equal; one-way for broader to narrower ("shoes" includes "boots", not the reverse).
4. Re-run the queries; log changes in the output file with date.
5. Feed recurring non-product queries into navigation or footer links.

Shopify Search & Discovery app: synonyms, product boosts, filters, recommendations. A third-party help center reported theme conflicts when synonym terms contain spaces [Unverified, 2026-05]; test after adding. Native filtering is reported to cap at 25 filters [Unverified, vendor claim].

## 6. Zero results page specification

- Heading: "No results for 'xyz'".
- Spelling suggestion as a link if available.
- Tips only if short ("Check spelling or try a broader term").
- Top categories, bestsellers, and recently viewed items.
- Contact or chat link for complex catalogs.
- Log the query (event `search_zero_results`, spec to `measurement`).

## 7. Search results page specification

- Query stays in the field; heading "Results for 'xyz' (128)".
- Category scope chips at the top (counts per category).
- Same filter and sort component as PLP (P17 to P19) with filters relevant to the result set.
- Product cards identical to PLP cards (P20).
- Load more button, not infinite scroll [Study, 2016].
- Non-product results (articles, pages) in a separate small section or tab.
- Redirect exact category queries to the category page with a note, keeping any typed attributes as filters.

## 8. Merchandising rules

| Rule type | Use | Guardrail |
|-----------|-----|-----------|
| Redirect | Exact category or brand query, policy queries | Never redirect queries with extra attributes without applying them as filters |
| Pin | Top 20 queries, seasonal heroes | Review monthly; never pin out-of-stock items |
| Boost | Margin, new arrivals, in-stock, bestseller labels from `offer-strategy` or `commerce-feeds` custom labels | Relevance first; boost factor small; measure search CVR |
| Bury | Sold out, discontinued, low rated | Keep visible for exact title queries |
| Personalization | Returning users, market | Must beat a holdout (`cro`) |

Merchandising changes are live changes (G3) when made in a production search tool. Draft them in a change request with before/after query screenshots.

## 9. Search tool selection

| Option | Fits | Strengths | Watch outs | Label |
|--------|------|-----------|-----------|-------|
| Shopify native search plus Search & Discovery app | Shopify stores up to a few thousand SKUs | Free, native filters, synonyms, boosts, recommendations | Limited rules; 2026 reports of SKU and synonym issues; verify on your store | [Official] plus [Unverified] issues |
| Algolia | Mid to enterprise, headless or Shopify | Speed, rules, analytics, AI features, Agent Studio | Cost scales with records and requests | [Official vendor] |
| Athos Commerce (Klevu, Searchspring) | Shopify, BigCommerce, Magento mid-market | Merchandising UI, Shopify apps | Post-merger roadmap and pricing still settling | [Practitioner consensus] |
| Searchanise | Shopify, BigCommerce SMB | Price, quick setup | Theme widget styling and speed | [Practitioner consensus] |
| Doofinder | EU SMB, WooCommerce, PrestaShop, Shopify | Multilingual, plans restructured in 2026 | Reports of price increases (2026-03) | [Unverified] |
| Constructor | Enterprise | Ranking with behavioral data; Gartner MQ 2026 leader (vendor claim) | Enterprise pricing | [Official vendor] |
| Boost Commerce | Shopify | Filters plus search for Shopify | App script weight | [Practitioner consensus] |
| Meilisearch | Headless, self-hosted or cloud | Open source, typo tolerance by default, fast | You build the UI and analytics | [Official docs] |
| Typesense | Headless, self-hosted or cloud | Open source (GPL-3.0), typo tolerance, faceting | GPL license implications for modifications | [Official docs] |
| Platform engines | WooCommerce (core search is weak; ElasticPress, FiboSearch), Shopware (built-in, OpenSearch for large catalogs), Adobe Commerce (OpenSearch required) | Native | Relevance tuning needs expertise | [Practitioner consensus] |

Decision by catalog size:
- 1 to 30 SKUs: no prominent search; navigation and a single collection suffice.
- 30 to 500: native search plus synonyms; fix zero results weekly.
- 500 to 5,000: native if checks in section 4 pass; otherwise a third-party engine.
- 5,000+ or multi-language or B2B part numbers: third-party engine with merchandising and analytics.

Switching engines is a TF item (`cro` measures search CVR, search exit rate, RPV of searchers) and a `site-engineer` release (script weight, fallbacks).

## 10. KPIs

| KPI | Definition | Direction |
|-----|-----------|-----------|
| Search usage | Sessions with a search / sessions | Context only |
| Search CVR | Orders from searching sessions / searching sessions | Up |
| Search exit rate | Searches with exit or no result click / searches | Down |
| Zero result rate | Zero result searches / searches | Down (target under 5% of searches, all top-50 queries with results) |
| Refinement rate | Searches followed by a new query / searches | Context (high means weak relevance) |
| Search revenue share | Revenue from searching sessions / revenue | Context |
