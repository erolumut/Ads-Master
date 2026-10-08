# Structured Data

> Scope: which rich result types Google supports in 2026 and which were removed, required and recommended properties for the types that matter, copy-paste JSON-LD templates, platform implementation, validation and monitoring at scale. Always check the search gallery before promising a rich result: https://developers.google.com/search/docs/appearance/structured-data/search-gallery

## 1. Principles [Official, Google structured data general guidelines]
1. Use JSON-LD (preferred by Google). Microdata and RDFa still work.
2. Markup must describe content visible on the page. Marking up invisible or misleading content is a structured data manual action risk.
3. Required properties are needed for eligibility; recommended properties improve eligibility and display.
4. Valid markup does not guarantee a rich result. Google decides per query, device and site quality.
5. Use the most specific type (`Product` not `Thing`, `NewsArticle` for news).
6. One entity, one description: avoid duplicate conflicting blocks from theme, plugin and app.
7. Connect entities with `@id` references inside a `@graph` so Organization, WebSite, WebPage and main entity form one graph.
8. Self-serving review snippets: reviews about a LocalBusiness or Organization published on its own site are not eligible for star rich results (since 2019).
9. Structured data is not required for AI Overviews or AI Mode, and there is no special schema for them; it helps systems understand entities and attributes [Official, 2025-05]. Other AI systems may use it too (ai-search-optimization handles that layer).

## 2. Support status in 2026
| Type | Status | Notes |
|------|--------|-------|
| Article (Article, NewsArticle, BlogPosting) | Supported | No required properties; helps title, image, date understanding |
| Breadcrumb (BreadcrumbList) | Supported | Mobile results show breadcrumbs in URL line variably |
| Carousel (ItemList) | Supported for specific types | Check gallery for current host types |
| Dataset | Dataset Search only (Google clarified in 2026 it powers Dataset Search results, not Google Search features) [Official, 2026] | |
| Discussion forum (DiscussionForumPosting) | Supported | For forum and UGC threads |
| Education Q&A (flashcards) | Supported | Education sites |
| Employer aggregate rating | Supported | |
| Event | Supported | Event experience in Search |
| FAQ (FAQPage) | Rich results no longer shown in Google Search for any site from 2026-05-07 (deprecation note added to docs 2026-05-08); Search Console FAQ reporting retired 2026-06; API support ended 2026-08 [Official, 2026-05]. Before that, restricted since 2023-08 to authoritative government and health sites | Valid schema.org markup; harmless, no display; do not build strategy on it. Bing and AI systems may still read it |
| HowTo | Removed (2023) | Remove or keep as harmless; no rich result |
| Image metadata | Supported | License, creator, credit |
| Job posting | Supported | Also Indexing API eligible |
| Local business | Supported | Knowledge panel signals; most local data comes from GBP |
| Practice problem | Deprecated: removed from Search Console rich result reports, the Rich Results Test and search appearance filters in 2026-01 [Official, 2026-01] | Harmless, no display |
| Math solver | Verify current status in the gallery | |
| Movie carousel | Supported | |
| Organization (logo, contact, return policy, loyalty program) | Supported | Organization level `hasMerchantReturnPolicy` and `hasMemberProgram` for merchants |
| Product: product snippets | Supported | Reviews, ratings, price in snippets |
| Product: merchant listings | Supported | Shopping knowledge panel, popular products, free listings eligibility signals |
| Product variants (ProductGroup) | Supported (since 2024) | Variants with `hasVariant`, `variesBy` |
| Loyalty program (MemberProgram) | Supported (added 2025-06) [Official, 2025-06] | Member prices in results |
| Profile page (ProfilePage) | Supported | Creators, authors, forum profiles |
| Q&A (QAPage) | Supported | Single question pages with user answers |
| Recipe | Supported | |
| Review snippet | Supported | Not for self-serving business reviews |
| Software app | Supported | Ratings and price |
| Speakable | Beta, limited | |
| Subscription and paywalled content | Supported | Required to avoid cloaking flags for paywalls |
| Vacation rental | Supported | Partner program |
| Video (VideoObject, Clip, SeekToAction, BroadcastEvent) | Supported | Key moments, LIVE badge |
| Site name (WebSite) | Supported | Homepage only |
| Book actions, Course info, Claim review (fact check in Search), Estimated salary, Learning video, Special announcement, Vehicle listing | Phased out from Search results (announced 2025-06); documentation for course info, estimated salary, learning video, special announcement and vehicle listing removed 2025-09; coverage conflicts on whether Book actions got a reprieve | [Official, 2025-06 and 2025-09]; markup harmless, no display |
| Sitelinks search box (WebSite SearchAction) | Removed 2024-11 | No effect |

Deprecations after June 2025 confirmed in the 2026-10-08 check: Practice problem (2026-01), FAQ rich results (2026-05). Google says unused structured data causes no harm and that these removals do not affect ranking. Verify every type in the gallery and on developers.google.com/search/updates before an implementation project [Freshness rule].

## 3. Required and recommended properties (key types)
Verify against current Google docs before implementation; properties change.

| Type | Required | Recommended (high value) |
|------|----------|--------------------------|
| Product (snippet) | `name`; and one of `review`, `aggregateRating`, `offers` | `offers.price`, `priceCurrency`, `availability`, `brand`, `sku`, `gtin`, `image`, `description`, `aggregateRating` |
| Product (merchant listing) | `name`, `image`, `offers` with `price` and `priceCurrency` | `availability`, `itemCondition`, `gtin` or `mpn`, `brand`, `shippingDetails`, `hasMerchantReturnPolicy` (or organization level policies), `color`, `size`, `material`, `aggregateRating`, `review` |
| ProductGroup (variants) | `name`, `hasVariant` (Products), `productGroupID`, `variesBy` | Each variant: `sku`, `gtin`, own `offers`, `inProductGroupWithID` |
| Organization | None strictly required | `name`, `url`, `logo`, `sameAs`, `address`, `contactPoint`, `telephone`, `email`, `legalName`, `foundingDate`, identifiers (`vatID`, `duns`, `iso6523Code`), `hasMerchantReturnPolicy`, `hasMemberProgram` |
| LocalBusiness (most specific subtype) | `name`, `address` | `geo`, `telephone`, `url`, `openingHoursSpecification`, `priceRange`, `image`, `department`, `menu`, `servesCuisine` |
| Article | None | `headline`, `image` (several aspect ratios), `datePublished`, `dateModified`, `author` (Person with `name` and `url`), `publisher` |
| BreadcrumbList | `itemListElement` of ListItem with `position`, `name`, `item` (item optional on last) | Mirror visible breadcrumb |
| Event | `name`, `startDate`, `location` (Place with address, or VirtualLocation) | `endDate`, `eventStatus`, `eventAttendanceMode`, `offers`, `organizer`, `performer`, `image`, `description` |
| JobPosting | `title`, `description`, `datePosted`, `hiringOrganization`, `jobLocation` (or remote: `jobLocationType` TELECOMMUTE plus `applicantLocationRequirements`) | `validThrough`, `baseSalary`, `employmentType`, `identifier`, `directApply` |
| VideoObject | `name`, `thumbnailUrl`, `uploadDate` | `description`, `contentUrl`, `embedUrl`, `duration`, `hasPart` (Clip) or SeekToAction, `expires` |
| Review snippet | `author`, `reviewRating.ratingValue`, `itemReviewed` (when not nested); AggregateRating: `ratingValue`, `ratingCount` or `reviewCount` | `bestRating`, `worstRating` when not 5 and 1 |
| SoftwareApplication | `name`, `offers.price` (with `priceCurrency` if over 0), `aggregateRating` or `review` | `applicationCategory`, `operatingSystem` |
| ProfilePage | `mainEntity` (Person or Organization) with `name` | `alternateName`, `identifier`, `image`, `sameAs`, `description`, `dateCreated`, `dateModified` |
| DiscussionForumPosting | `author`, `datePublished`, and one of `text`, `image`, `video` | `headline`, `url`, `comment`, `interactionStatistic` |
| Recipe | `name`, `image` | `recipeIngredient`, `recipeInstructions`, `totalTime`, `nutrition`, `aggregateRating`, `video` |
| Paywalled content | `isAccessibleForFree: false`, `hasPart` WebPageElement with `isAccessibleForFree: false` and `cssSelector` | Class names must exist on the page |

## 4. JSON-LD templates
Homepage graph (Organization, WebSite with site name):
```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://www.example.com/#organization",
      "name": "Acme",
      "legalName": "Acme Inc.",
      "url": "https://www.example.com/",
      "logo": "https://www.example.com/static/logo-512.png",
      "sameAs": [
        "https://www.linkedin.com/company/acme",
        "https://www.youtube.com/@acme",
        "https://www.wikidata.org/wiki/Q000000"
      ],
      "contactPoint": [{ "@type": "ContactPoint", "contactType": "customer support", "telephone": "+1-555-555-0100", "email": "support@example.com" }]
    },
    {
      "@type": "WebSite",
      "@id": "https://www.example.com/#website",
      "url": "https://www.example.com/",
      "name": "Acme",
      "alternateName": ["Acme Store", "acme.com"],
      "publisher": { "@id": "https://www.example.com/#organization" }
    }
  ]
}
```
Product merchant listing with offer, shipping and returns:
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "@id": "https://www.example.com/products/trail-runner-2#product",
  "name": "Trail Runner 2 Women's Running Shoe",
  "image": ["https://www.example.com/img/tr2-1x1.jpg", "https://www.example.com/img/tr2-4x3.jpg", "https://www.example.com/img/tr2-16x9.jpg"],
  "description": "Lightweight trail running shoe with 6 mm drop and rock plate.",
  "sku": "TR2-W-BLU-38",
  "gtin13": "0000000000000",
  "brand": { "@type": "Brand", "name": "Acme" },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": 4.6, "reviewCount": 182 },
  "offers": {
    "@type": "Offer",
    "url": "https://www.example.com/products/trail-runner-2",
    "price": 129.00,
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "itemCondition": "https://schema.org/NewCondition",
    "shippingDetails": {
      "@type": "OfferShippingDetails",
      "shippingRate": { "@type": "MonetaryAmount", "value": 0, "currency": "USD" },
      "shippingDestination": { "@type": "DefinedRegion", "addressCountry": "US" },
      "deliveryTime": {
        "@type": "ShippingDeliveryTime",
        "handlingTime": { "@type": "QuantitativeValue", "minValue": 0, "maxValue": 1, "unitCode": "DAY" },
        "transitTime": { "@type": "QuantitativeValue", "minValue": 2, "maxValue": 5, "unitCode": "DAY" }
      }
    },
    "hasMerchantReturnPolicy": {
      "@type": "MerchantReturnPolicy",
      "applicableCountry": "US",
      "returnPolicyCategory": "https://schema.org/MerchantReturnFiniteReturnWindow",
      "merchantReturnDays": 30,
      "returnMethod": "https://schema.org/ReturnByMail",
      "returnFees": "https://schema.org/FreeReturn"
    }
  }
}
```
Prefer organization level return and shipping policies (on Organization, or configured in Merchant Center or Search Console where available) when they are uniform, instead of repeating them on every product.

Product variants:
```json
{
  "@context": "https://schema.org",
  "@type": "ProductGroup",
  "name": "Trail Runner 2",
  "productGroupID": "TR2",
  "variesBy": ["https://schema.org/size", "https://schema.org/color"],
  "brand": { "@type": "Brand", "name": "Acme" },
  "hasVariant": [
    { "@type": "Product", "sku": "TR2-W-BLU-38", "name": "Trail Runner 2 Blue 38", "size": "38", "color": "Blue",
      "image": "https://www.example.com/img/tr2-blue.jpg",
      "offers": { "@type": "Offer", "price": 129.00, "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": "https://www.example.com/products/trail-runner-2?variant=blue-38" } }
  ]
}
```
Breadcrumbs:
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Running", "item": "https://www.example.com/running/" },
    { "@type": "ListItem", "position": 2, "name": "Trail Running Shoes", "item": "https://www.example.com/running/trail-shoes/" },
    { "@type": "ListItem", "position": 3, "name": "Trail Runner 2" }
  ]
}
```
Article with author:
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Choose Trail Running Shoes: We Tested 14 Pairs",
  "image": ["https://www.example.com/img/guide-16x9.jpg"],
  "datePublished": "2026-03-02T08:00:00+00:00",
  "dateModified": "2026-09-18T10:30:00+00:00",
  "author": [{ "@type": "Person", "name": "Dana Lee", "url": "https://www.example.com/authors/dana-lee", "jobTitle": "Gear editor" }],
  "publisher": { "@id": "https://www.example.com/#organization" }
}
```
LocalBusiness (use the most specific subtype, for example `Plumber`, `Dentist`):
```json
{
  "@context": "https://schema.org",
  "@type": "Plumber",
  "@id": "https://www.example.com/locations/austin#business",
  "name": "Acme Plumbing Austin",
  "url": "https://www.example.com/locations/austin",
  "telephone": "+1-512-555-0100",
  "address": { "@type": "PostalAddress", "streetAddress": "100 Main St", "addressLocality": "Austin", "addressRegion": "TX", "postalCode": "78701", "addressCountry": "US" },
  "geo": { "@type": "GeoCoordinates", "latitude": 30.2672, "longitude": -97.7431 },
  "openingHoursSpecification": [{ "@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"], "opens": "07:00", "closes": "19:00" }],
  "areaServed": ["Austin", "Round Rock", "Cedar Park"],
  "parentOrganization": { "@id": "https://www.example.com/#organization" }
}
```
Video with key moments:
```json
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "How to lace trail running shoes for downhill",
  "description": "Three lacing methods tested on a 12 percent descent.",
  "thumbnailUrl": "https://www.example.com/img/lacing-thumb.jpg",
  "uploadDate": "2026-05-04T09:00:00+00:00",
  "duration": "PT4M12S",
  "contentUrl": "https://www.example.com/video/lacing.mp4",
  "hasPart": [
    { "@type": "Clip", "name": "Heel lock lacing", "startOffset": 35, "endOffset": 110, "url": "https://www.example.com/guides/lacing?t=35" }
  ]
}
```
SoftwareApplication (SaaS):
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Acme CRM",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web, iOS, Android",
  "offers": { "@type": "Offer", "price": 29, "priceCurrency": "USD" },
  "aggregateRating": { "@type": "AggregateRating", "ratingValue": 4.5, "ratingCount": 812 }
}
```
Only mark up ratings that are displayed on the page and collected by a method you can document.

## 5. Platform implementation notes
| Platform | How | Pitfalls |
|----------|-----|----------|
| Next.js and React SSR | Server render a JSON-LD component (escape `<`; see technical reference) | Client only injection is fine for Google after rendering, but other crawlers may miss it; render server side |
| Shopify | Theme snippet in `product.liquid` or JSON template section using Liquid objects and the `json` filter (`{{ product.title \| json }}`) | Theme plus reviews app plus SEO app producing three Product blocks; remove duplicates, merge rating into one block |
| WordPress | SEO plugin schema graph (Yoast, Rank Math) plus filters for custom types | Theme schema duplicates; plugin defaults (for example, marking every page as Article) |
| Webflow | Custom code in page or CMS template head with CMS fields | Unescaped quotes from CMS fields break JSON |
| Headless CMS | Model structured fields (price, ratings, author) and render JSON-LD from them | Free text fields cause inconsistency |

Shopify Liquid sketch:
```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": {{ product.title | json }},
  "image": {{ product.featured_image | image_url: width: 1200 | prepend: 'https:' | json }},
  "description": {{ product.description | strip_html | truncate: 500 | json }},
  "sku": {{ product.selected_or_first_available_variant.sku | json }},
  "brand": { "@type": "Brand", "name": {{ product.vendor | json }} },
  "offers": {
    "@type": "Offer",
    "url": {{ shop.url | append: product.url | json }},
    "price": {{ product.selected_or_first_available_variant.price | divided_by: 100.0 | json }},
    "priceCurrency": {{ cart.currency.iso_code | json }},
    "availability": "{% if product.selected_or_first_available_variant.available %}https://schema.org/InStock{% else %}https://schema.org/OutOfStock{% endif %}"
  }
}
</script>
```
Check whether `image_url` already returns a protocol relative or absolute URL in your theme version and adjust the `prepend`.

## 6. Validation and monitoring
| Tool | Use |
|------|-----|
| Rich Results Test (search.google.com/test/rich-results) | Google supported types only; renders the page; shows eligibility |
| Schema Markup Validator (validator.schema.org) | Any schema.org type; syntax and vocabulary |
| Search Console enhancement reports (Products, Merchant listings, Breadcrumbs, Videos, Events, etc.) | Errors and warnings at scale over time |
| URL Inspection > Enhancements | Per URL detected items |
| Crawler extraction (Screaming Frog structured data tab, Sitebulb) | Coverage across all templates |

Extraction and required field check at scale (Python, `extruct`):
```python
import json, sys, requests, extruct
from w3lib.html import get_base_url

REQUIRED = {"Product": ["name"], "Offer": ["price", "priceCurrency"], "BreadcrumbList": ["itemListElement"]}

def check(url: str):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (compatible; SEO-audit)"}, timeout=20)
    data = extruct.extract(r.text, base_url=get_base_url(r.text, r.url), syntaxes=["json-ld"])["json-ld"]
    issues = []
    def walk(node):
        if isinstance(node, dict):
            t = node.get("@type")
            for typ in (t if isinstance(t, list) else [t]):
                for prop in REQUIRED.get(typ, []):
                    if prop not in node:
                        issues.append(f"{typ} missing {prop}")
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(data)
    return {"url": url, "blocks": len(data), "issues": issues}

for line in sys.stdin:
    print(json.dumps(check(line.strip())))
```
Monitoring cadence: weekly enhancement report review; validate after every template release; quarterly support status check in the gallery.

## 7. Common mistakes
- Marking up reviews or ratings that are not visible or that come from a third party widget without the data on the page.
- `availability` and price in markup disagreeing with the page (or with the Merchant Center feed); hand mismatches to commerce-feeds.
- FAQ markup everywhere expecting rich results (restricted since 2023).
- Organization markup on every page with different data.
- Event markup for ongoing promotions (not events).
- Using `Article` for product or category pages.
- Hardcoded `dateModified` set to build time on every deploy.
