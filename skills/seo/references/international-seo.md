# International SEO

> Scope: choosing a structure for multiple countries and languages, hreflang rules and implementation, validation scripts, geotargeting signals, translation and localization quality, platform specifics, measurement per market, and a market launch playbook.

## 1. Structure options
| Option | Example | Pros | Cons | Choose when |
|--------|---------|------|------|-------------|
| ccTLD | `example.de`, `example.fr` | Strongest local signal; trust in some markets (Germany, Japan, Turkey) | Separate authority per domain; more cost; domain availability | Large local operations, separate legal entities, markets where local domains convert better |
| Subfolder | `example.com/de-de/` | Consolidated authority; one property; cheapest to run | Weaker local signal than ccTLD; one server location (irrelevant with a CDN) | Default for most businesses |
| Subdomain | `de.example.com` | Separate hosting or platform per market | Splits signals in practice; more management | Technical constraints (separate platforms) |
| Parameters | `example.com/?lang=de` | None | Hard to target, crawl and report | Never |
| Same URL, content by IP or Accept-Language | `example.com` | None for SEO | Googlebot mostly crawls from the US and sees one version | Never for indexable content |

Folder naming: language only (`/de/`) when one version serves all speakers; language and region (`/de-at/`, `/en-gb/`) when content differs by country (prices, currency, availability, legal). Keep naming consistent.

Search Console no longer has an International Targeting setting (removed 2022). Geotargeting comes from ccTLDs, hreflang, local content (currency, addresses, phone numbers), local links and mentions.

## 2. hreflang rules [Official, Google localized versions doc]
1. Every version lists every version in the cluster, including itself (self referencing).
2. Return links are mandatory: if A points to B, B must point to A. Missing return tags cause Google to ignore the pair.
3. Values: ISO 639-1 language (`en`, `de`, `pt`), optionally plus ISO 3166-1 alpha-2 region (`en-GB`, `pt-BR`). Region alone is invalid. Common errors: `en-UK` (must be `en-GB`) and `es-LA` (LA is Laos, not Latin America; use specific countries such as `es-MX` or language only `es`).
4. `x-default` for the fallback page (language selector or global English).
5. URLs must be absolute, canonical, indexable and return 200. Never point hreflang at redirected, noindexed or canonicalized-away URLs.
6. Canonical on each version points to itself, not to another language version.
7. Use one implementation method per page set: HTML `<link>` in head, HTTP `Link` header (for PDFs), or XML sitemap. Sitemaps are easiest at scale.
8. hreflang is a signal for which version to show, not a ranking boost and not a duplicate content fix for different content.

Note on `es-419`: Google's documentation supports language codes plus country codes; regional codes like `419` (Latin America) are not supported for hreflang by Google [Official; verify current doc]. Use country specific values or language only.

HTML example:
```html
<link rel="alternate" hreflang="en-us" href="https://www.example.com/en-us/pricing/" />
<link rel="alternate" hreflang="en-gb" href="https://www.example.com/en-gb/pricing/" />
<link rel="alternate" hreflang="de-de" href="https://www.example.com/de-de/preise/" />
<link rel="alternate" hreflang="x-default" href="https://www.example.com/pricing/" />
```
XML sitemap example:
```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
  <url>
    <loc>https://www.example.com/en-us/pricing/</loc>
    <xhtml:link rel="alternate" hreflang="en-us" href="https://www.example.com/en-us/pricing/"/>
    <xhtml:link rel="alternate" hreflang="en-gb" href="https://www.example.com/en-gb/pricing/"/>
    <xhtml:link rel="alternate" hreflang="de-de" href="https://www.example.com/de-de/preise/"/>
    <xhtml:link rel="alternate" hreflang="x-default" href="https://www.example.com/pricing/"/>
  </url>
  <!-- repeat a <url> entry for each version with the same full set of alternates -->
</urlset>
```
Next.js App Router:
```tsx
export async function generateMetadata({ params }: { params: Promise<{ locale: string }> }): Promise<Metadata> {
  const { locale } = await params
  return {
    alternates: {
      canonical: `/${locale}/pricing/`,
      languages: {
        'en-US': '/en-us/pricing/',
        'en-GB': '/en-gb/pricing/',
        'de-DE': '/de-de/preise/',
        'x-default': '/pricing/',
      },
    },
  }
}
```
Only list alternates that actually exist for that page; pages without a translation must not reference a missing URL.

Bing: uses hreflang and the `content-language` meta tag or HTTP header as signals; adding `<meta http-equiv="content-language" content="de-de">` is cheap insurance for Bing [Unverified weight; Practitioner consensus].

## 3. hreflang validation script
Checks reciprocity, self reference, status, canonical alignment for a list of URLs.
```python
import sys, requests
from lxml import html

UA = {"User-Agent": "Mozilla/5.0 (compatible; hreflang-audit)"}

def get_alts(url):
    r = requests.get(url, headers=UA, timeout=20, allow_redirects=False)
    if r.status_code != 200:
        return r.status_code, None, {}
    doc = html.fromstring(r.content)
    canon = (doc.xpath('//link[@rel="canonical"]/@href') or [None])[0]
    alts = {l.get("hreflang").lower(): l.get("href") for l in doc.xpath('//link[@rel="alternate"][@hreflang]')}
    return 200, canon, alts

def audit(urls):
    cache = {}
    for u in urls:
        cache[u] = get_alts(u)
    for u, (status, canon, alts) in cache.items():
        problems = []
        if status != 200:
            problems.append(f"status {status}")
        if canon and canon != u:
            problems.append(f"canonical points to {canon}")
        if u not in alts.values():
            problems.append("missing self reference")
        for lang, target in alts.items():
            if target not in cache:
                cache[target] = get_alts(target)
            t_status, _, t_alts = cache[target]
            if t_status != 200:
                problems.append(f"{lang} -> {target} returns {t_status}")
            elif u not in t_alts.values():
                problems.append(f"no return tag from {target}")
        print(u, "OK" if not problems else "; ".join(problems))

audit([line.strip() for line in sys.stdin if line.strip()])
```
At scale use a crawler's hreflang reports (Screaming Frog, Sitebulb) and Search Console data per market.

## 4. Redirects and language selection
- Never automatically redirect by IP or browser language for indexable pages; Googlebot crawls mostly from US IPs and without `Accept-Language`, so it would never see other versions.
- Show a dismissible banner suggesting the matching version; remember the user's choice in a cookie.
- If the root (`/`) must redirect, use a 302 to a default version and keep `x-default` on the root or a selector page.

## 5. Localization quality
- Machine translation without review risks low quality and scaled content issues; human review by native speakers is the standard for money pages [Practitioner consensus; Google's spam policies cover auto generated content without value].
- Localize, do not only translate: currency, prices, units, sizes, payment methods, shipping, legal pages, phone numbers, addresses, local proof (reviews, case studies, press), local keywords (research per market; direct translations of keywords often miss real search terms).
- Keyword research per market with local tools and native speakers; check SERPs from that country (rank tracker or SERP API with location settings).
- Same language, multiple countries (en-US, en-GB, en-AU): differentiate at least prices, currency, spelling, shipping and contact info. If pages are otherwise identical, hreflang still helps Google show the right one.

## 6. Platform notes
| Platform | International approach | Checks |
|----------|------------------------|--------|
| Shopify Markets | Subfolders per market or separate domains; automatic hreflang | Reciprocity, x-default, translated handles, currency switching without URL changes |
| Next.js | i18n routing via middleware and `[locale]` segments | No auto redirect for bots, `alternates.languages`, locale specific sitemaps |
| WordPress | WPML, Polylang, TranslatePress, or multisite | Plugin generated hreflang and sitemaps; avoid two plugins outputting hreflang |
| Webflow Localization | Subfolders with automatic hreflang | Untranslated pages, slugs |
| Headless CMS | Locale fields, slug per locale | Fallback behavior must not create duplicate untranslated pages |

## 7. Measurement per market
- Add each subfolder or ccTLD as its own Search Console property (URL prefix for folders) for clean reporting and access control, plus the Domain property for totals.
- Report per market: non-brand clicks, conversions, revenue, indexing ratio, hreflang errors, top competitors.
- Use Search Console country filter carefully: it reports searcher location, not the version shown.
- Rank tracking per country and language with local settings.
- Bing share is higher in some markets and on desktop; check Bing Webmaster Tools per market.

## 8. Market launch playbook
1. Business case: demand (keyword research in local language), competition, operations (shipping, support, payments).
2. Structure decision (section 1) documented with reasons.
3. Content plan: which pages launch localized (money pages first), which stay global.
4. Technical setup: folders or domains, hreflang (sitemap method), canonical rules, localized sitemaps, robots, CDN.
5. Localization: native review, local keyword mapping per page, local trust elements.
6. QA on staging: hreflang validation script, crawl, rendering, currency and price markup, structured data per market (`priceCurrency`, `addressCountry`).
7. Launch with approval; submit sitemaps; Search Console properties; Bing Webmaster Tools.
8. Local authority: PR and links from local media, partners, directories; local GBP if physical presence.
9. Monitor weekly for 12 weeks: indexing per market, wrong version ranking (hreflang errors), cannibalization between same language markets.

## 9. Common mistakes
- Using `en-UK`.
- hreflang pointing to the homepage for every page.
- Canonical on all language versions pointing to the English page.
- Untranslated pages published in many locales (duplicate content and poor UX).
- Auto redirects by IP.
- Mixed implementation methods (HTML on some pages, sitemap on others) with conflicting values.
- Forgetting hreflang updates after migrations or URL slug translations.
