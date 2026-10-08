# Technical SEO and Code Fixes

> Scope: the server, HTML and framework layer. Status codes, redirects, robots.txt, meta robots, sitemaps, HTTPS, mobile, Core Web Vitals, and copy-paste recipes for Next.js, Nuxt, SPAs, Shopify, WordPress, Webflow and custom servers. Rendering, indexing triage, canonical clusters, faceted navigation and logs are in [crawl-index-render.md](crawl-index-render.md).

## 1. The technical health model
Work top down. A failure at a higher stage makes everything below it irrelevant.

| Stage | Question | Fast check | Owner of fix |
|-------|----------|-----------|--------------|
| Discover | Can Google find the URL? | In sitemap? Linked with `<a href>` from an indexed page? | SEO plus dev |
| Crawl | Is fetching allowed and fast? | robots.txt test, status code, response time | Dev, hosting |
| Render | Does the rendered DOM contain content and links? | URL Inspection live test, headless render diff | Dev |
| Index | Is the URL indexable and chosen as canonical? | Meta robots, X-Robots-Tag, canonical, Page indexing report | SEO plus dev |
| Rank | Does it deserve to rank? | Intent match, quality, links, internal links | SEO, content |
| Click | Does the snippet win clicks? | Title link, snippet, rich result, SERP features | SEO, content |
| Convert | Does the visit produce value? | GA4 landing page conversion rate | cro (handoff) |

## 2. HTTP status codes: what Google does [Official, Google HTTP status and network errors doc]
| Code | Google behavior | Use it for |
|------|-----------------|-----------|
| 200 | Content considered for indexing. A 200 page that says "not found" or is empty may be classified soft 404 | Real pages only |
| 301, 308 | Permanent. Strong signal that the target becomes canonical | Moves, consolidation, protocol and host normalization |
| 302, 303, 307 | Temporary. Weak canonical signal; source usually stays indexed | Short term moves, geo or A/B routing for users (not for Googlebot only) |
| 304 | Not modified; fine for refresh crawls | Conditional requests (ETag, Last-Modified) save crawl |
| 404, 410 | Not indexed; indexed URLs drop out. 410 may be processed marginally faster [Practitioner consensus] | Removed content with no replacement |
| 401, 403 | Treated like other 4xx: not indexed. Never use to slow crawling | Auth areas |
| 429, 500, 503 | Google slows crawling. Persistent errors lead to URLs dropping from the index | Temporary overload or maintenance (503 with Retry-After) |
| Soft 404 | 200 with error or empty content; reported in Page indexing | Fix with real 404 or real content |

Redirect rules:
- Googlebot follows up to 10 hops, then reports a redirect error. Target: one hop. Every chain over 1 hop on a money page is a fix.
- Server side 301 or 308 beats meta refresh and JavaScript redirects. JS redirects work only after rendering and are the last resort.
- Redirect to the closest equivalent. Mass redirects of unrelated URLs to the homepage are treated as soft 404s.
- Keep redirects for at least one year after a move, ideally indefinitely [Official, site move guidance].
- Update internal links to the final URL. Do not rely on redirects for internal navigation.

Host and URL normalization (pick one of each, redirect the rest in one hop):
| Variant | Rule |
|---------|------|
| http vs https | 301 to https, HSTS header after verification |
| www vs non-www | 301 to the chosen host |
| Trailing slash | One form; 301 the other (Next.js `trailingSlash`, nginx rewrite) |
| Uppercase paths | 301 to lowercase if the server is case sensitive and duplicates exist |
| index.html, index.php | 301 to directory URL |
| Tracking parameters (utm_, gclid, fbclid) | Self canonical to clean URL; never link internally with UTMs |

## 3. robots.txt
Facts [Official, Google robots.txt spec]:
- One file per protocol, host and port: `https://shop.example.com/robots.txt` does not govern `https://www.example.com`.
- Google processes the first 500 KiB. Supported fields: `user-agent`, `allow`, `disallow`, `sitemap`. `crawl-delay` is ignored by Google (Bing honors it). `noindex` in robots.txt is not supported (since September 2019).
- Most specific (longest) matching rule wins; on a tie, `allow` wins. Paths are case sensitive. Wildcards: `*` and `$` (end of URL).
- Status handling: 4xx for robots.txt means "no restrictions". 5xx or unreachable: Google stops crawling for 12 hours, then uses the last good copy for up to 30 days, then treats the site as unrestricted if the site is otherwise available.
- Disallow blocks crawling, not indexing. A disallowed URL can still be indexed without content if linked. To deindex, allow crawling and serve noindex.

Template for a typical site:
```txt
User-agent: *
Disallow: /cart
Disallow: /checkout
Disallow: /account
Disallow: /search
Disallow: /*?*sort=
Disallow: /*?*sessionid=
Allow: /*.css$
Allow: /*.js$

Sitemap: https://www.example.com/sitemap.xml
```
Rules of thumb:
- Never block CSS, JS, images or API endpoints that rendering needs. Check with URL Inspection "Page resources".
- Block infinite spaces (internal search, calendars, sort orders, session IDs, low value facet combinations) only after checking they hold no indexed traffic.
- AI and other crawler tokens: `Googlebot` controls Search including AI Overviews and AI Mode. `Google-Extended` controls Gemini model training and grounding outside Search, not AI Overviews [Official, Google crawlers doc]. `Bingbot` feeds Bing and Copilot. Policy for GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot and others belongs to ai-search-optimization; never change those lines without that handoff.
- Staging: protect with HTTP authentication or IP allowlist. A `Disallow: /` on staging gets copied to production at launch more often than any other SEO bug.

## 4. Meta robots and X-Robots-Tag
| Directive | Effect | Notes |
|-----------|--------|-------|
| `noindex` | Removes from index once recrawled | Must be crawlable. Google may skip rendering a page whose raw HTML has noindex, so JS cannot remove it later |
| `nofollow` | Do not follow links on this page | Rarely right for whole pages |
| `nosnippet` | No text snippet or video preview; also excludes content from AI Overviews and AI Mode | Removes classic snippets too; costly |
| `max-snippet:[n]` | Limits snippet length; also limits use in AI features | `-1` means no limit |
| `max-image-preview:large` | Allows large image previews | Needed for strong Discover performance |
| `max-video-preview:[n]` | Video preview seconds | `-1` no limit |
| `data-nosnippet` (HTML attribute) | Excludes a section from snippets and AI features | Use on boilerplate, pricing disclaimers, paywalled teasers |
| `unavailable_after: [date]` | Drop after date | Events, expiring offers |
| `noimageindex` | Images on page not indexed | Rare |
| `indexifembedded` | Index content embedded via iframe despite noindex | Embeds, widgets |

`X-Robots-Tag` HTTP header applies the same directives to non-HTML files (PDF, images) and is the cleanest way to noindex staging at the server:
```nginx
# nginx: noindex all PDFs in a folder and protect staging
location ^~ /internal-docs/ { add_header X-Robots-Tag "noindex" always; }
# staging server block
add_header X-Robots-Tag "noindex, nofollow" always;
auth_basic "Staging";
auth_basic_user_file /etc/nginx/.htpasswd;
```
Conflicts: when meta robots and the header disagree, Google applies the most restrictive directive.

Google Search Console AI features setting (2026): Search Console added a property level "Search generative AI" setting that excludes a site from AI Overviews, AI Mode and AI features in Discover without removing classic snippets. Default is Include; Google says it is not a ranking signal [Official, 2026-06; rollout status Contested]. Decision process in [ai-overviews-and-serp-changes.md](ai-overviews-and-serp-changes.md). Never change it without written approval.

## 5. XML sitemaps
Facts [Official, Google sitemaps docs]:
- Max 50,000 URLs or 50 MB uncompressed per file. Sitemap index files list up to 50,000 sitemaps.
- Google ignores `priority` and `changefreq`. It uses `lastmod` when it is consistently accurate. Bing relies on `lastmod` heavily for recrawl decisions in AI powered search [Official, Bing Webmaster blog 2025].
- The Google sitemap ping endpoint was retired in 2023. Submit in Search Console and declare in robots.txt.
- Image sitemaps: only `image:loc` is used. Video sitemaps for video landing pages. News sitemaps: only articles published in the last 2 days, up to 1,000 URLs per file.

Rules:
1. Include only canonical, indexable, 200 status URLs. Sitemap URLs that redirect, 404 or are noindexed waste trust in the file.
2. Split by page type (`/sitemaps/products-1.xml`, `/sitemaps/categories.xml`, `/sitemaps/articles-2026.xml`) so Page indexing can be filtered by sitemap and indexing ratio tracked per template.
3. `lastmod` changes only when main content changes (not on every build, not on price ticks unless that is what the page is about).
4. Regenerate automatically from the source of truth (database, CMS), not from a crawl.
5. Indexing ratio per sitemap = indexed URLs / submitted URLs. Investigate any template under 80% that should be fully indexed.

## 6. HTTPS, security, mobile
- HTTPS everywhere, valid certificates, no mixed content. HSTS once stable.
- Mobile-first indexing is complete for all sites (Google finished the move in July 2024; sites not accessible on mobile are not indexed) [Official, 2024]. Content, internal links, structured data, images and alt text must be equivalent on mobile. Hidden-on-mobile navigation that removes links removes them for Google.
- Intrusive interstitials on mobile entry (full screen popups before content) hurt users and page experience. Use banners for consent and app promos.
- Security issues and hacked content: check the Security issues report weekly. Common hacks: Japanese keyword hack, cloaked pharma pages, injected links. Fix, then request review.

## 7. Core Web Vitals and page performance
Thresholds at the 75th percentile of real user page loads, mobile and desktop separately [Official, web.dev]:

| Metric | Good | Needs improvement | Poor | Since |
|--------|------|-------------------|------|-------|
| LCP (Largest Contentful Paint) | 2.5 s or less | 2.5 to 4.0 s | over 4.0 s | 2020 |
| INP (Interaction to Next Paint) | 200 ms or less | 200 to 500 ms | over 500 ms | Replaced FID on 2024-03-12 |
| CLS (Cumulative Layout Shift) | 0.1 or less | 0.1 to 0.25 | over 0.25 | 2020 |

How Google uses them: Core Web Vitals are used by ranking systems, but relevance and quality dominate; treat CWV as a tie breaker for rankings and a direct lever for conversion and crawl efficiency [Official, page experience doc; Practitioner consensus]. Field data (CrUX, 28 day rolling) is what counts; Lighthouse lab scores are for debugging.

Diagnosis workflow:
1. Pull CrUX for origin and top templates (CrUX API or PageSpeed Insights API; script in [tools-api-mcp.md](tools-api-mcp.md)). Search Console Core Web Vitals report groups similar URLs.
2. Identify the failing metric per template and device.
3. Reproduce in Chrome DevTools Performance panel (or Chrome DevTools MCP traces) with CPU throttling 4x and slow 4G.
4. Fix at the template or component level; verify in lab; confirm in field after 28 days.

LCP fixes (by sub-part):
| Sub-part | Typical cause | Fix |
|----------|---------------|-----|
| TTFB | Slow server, no caching, redirects | CDN and full page cache, edge rendering, remove redirect hops, SSG or ISR for stable pages |
| Resource load delay | LCP image discovered late (CSS background, JS inserted, lazy loaded) | Put the LCP image in HTML `<img>`, `fetchpriority="high"`, preload when needed, never `loading="lazy"` on it |
| Resource load duration | Heavy images | AVIF or WebP, responsive `srcset` and `sizes`, correct dimensions, image CDN |
| Element render delay | Render blocking CSS and JS, client side rendering, fonts | Inline critical CSS, defer non critical JS, SSR, `font-display: swap` or optional |

INP fixes:
| Phase | Cause | Fix |
|-------|-------|-----|
| Input delay | Long tasks from third party scripts, hydration | Audit tags (chat, A/B testing, heatmaps, reviews widgets), load after interaction or idle, reduce hydration cost (server components, islands, partial hydration) |
| Processing | Heavy event handlers, synchronous state updates | Break up work with `await scheduler.yield()` (fallback `setTimeout`), debounce, move work off main thread (web workers), avoid layout thrash |
| Presentation delay | Large DOM, expensive style recalculation | Reduce DOM size, `content-visibility: auto` for off screen sections, virtualize long lists |

CLS fixes: width and height (or `aspect-ratio`) on images, video, iframes and ad slots; reserve space for consent banners and embeds; font fallback with `size-adjust`; never insert content above existing content after load except in response to user input; keep pages eligible for the back/forward cache (no `unload` handlers).

Third party script budget: every script on the money templates needs an owner and a reason. Tag managers often carry 20 or more tags no one uses; hand the tag list to measurement for cleanup.

## 8. Framework recipes
Always confirm the framework version first (`package.json`), because APIs change between major versions.

### 8.1 Next.js App Router (13.4 and later; params are async from 15)
Root layout with a safe default and no inherited canonical bug:
```tsx
// app/layout.tsx
import type { Metadata } from 'next'

export const metadata: Metadata = {
  metadataBase: new URL('https://www.example.com'),
  title: { default: 'Brand: what you sell', template: '%s | Brand' },
  description: 'One sentence value proposition with the main category term.',
  robots: {
    index: true,
    follow: true,
    googleBot: { 'max-image-preview': 'large', 'max-snippet': -1, 'max-video-preview': -1 },
  },
  // Do NOT set alternates.canonical here: child pages inherit it and every page canonicalizes to "/".
}
```
The most common Next.js SEO bug: `alternates: { canonical: '/' }` in the root layout. Every route that does not override it declares the homepage as canonical. Fix:
```diff
--- a/app/layout.tsx
+++ b/app/layout.tsx
@@ export const metadata: Metadata = {
   metadataBase: new URL('https://www.example.com'),
-  alternates: { canonical: '/' },
 }
--- a/app/page.tsx
+++ b/app/page.tsx
+export const metadata: Metadata = { alternates: { canonical: '/' } }
```
Dynamic routes:
```tsx
// app/products/[slug]/page.tsx
import type { Metadata } from 'next'
import { notFound } from 'next/navigation'

type Props = { params: Promise<{ slug: string }> }

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { slug } = await params
  const product = await getProduct(slug)
  if (!product) return { robots: { index: false, follow: true } }
  return {
    title: product.seoTitle ?? `${product.name} | ${product.brand}`,
    description: product.metaDescription,
    alternates: { canonical: `/products/${slug}` },
    openGraph: { images: [{ url: product.imageUrl, width: 1200, height: 630 }] },
  }
}

export default async function Page({ params }: Props) {
  const { slug } = await params
  const product = await getProduct(slug)
  if (!product) notFound() // call before any streamed UI so the status is a real 404
  return <ProductView product={product} />
}

export async function generateStaticParams() {
  return (await getTopProducts(1000)).map(p => ({ slug: p.slug })) // prebuild top pages; others render on demand
}
export const revalidate = 3600 // ISR: refresh hourly
```
Status code caveat: if `notFound()` runs after streaming has started (inside a Suspense boundary), the response can already be 200; Next.js then injects a noindex meta tag. Verify 404 templates with `curl -I` [Unverified for every version; test yours].

Sitemap and robots:
```ts
// app/sitemap.ts
import type { MetadataRoute } from 'next'
export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const base = 'https://www.example.com'
  const [cats, products] = await Promise.all([getIndexableCategories(), getIndexableProducts()])
  return [
    { url: `${base}/`, lastModified: await getHomepageUpdatedAt() },
    ...cats.map(c => ({ url: `${base}/c/${c.slug}`, lastModified: c.contentUpdatedAt })),
    ...products.map(p => ({ url: `${base}/products/${p.slug}`, lastModified: p.contentUpdatedAt })),
  ]
}
// For more than 50,000 URLs export generateSitemaps() and split by id.
```
```ts
// app/robots.ts
import type { MetadataRoute } from 'next'
export default function robots(): MetadataRoute.Robots {
  const isProd = process.env.VERCEL_ENV === 'production' // adapt to your host
  if (!isProd) return { rules: [{ userAgent: '*', disallow: '/' }] } // plus auth on staging
  return {
    rules: [{ userAgent: '*', allow: '/', disallow: ['/api/', '/cart', '/account', '/search'] }],
    sitemap: 'https://www.example.com/sitemap.xml',
  }
}
```
JSON-LD (escape `<` as the Next.js docs recommend):
```tsx
export function JsonLd({ data }: { data: object }) {
  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, '\\u003c') }}
    />
  )
}
```
Other Next.js checks:
- Redirects in `next.config` with `permanent: true` return 308, which Google treats like 301. For thousands of redirects, check your host's limits and use middleware with a lookup map or the host's bulk redirect feature.
- `middleware.ts` geo or language redirects must not redirect Googlebot (crawls mostly from the US) away from content. Prefer a banner or `Vary` aware content negotiation with hreflang.
- Images: `next/image` with the LCP image marked as priority (the prop name changed in recent versions; check your version) and explicit `sizes`.
- Fonts: `next/font` self hosts and sets fallback metrics, reducing CLS.
- Streaming metadata (15.2 and later) can place metadata after initial HTML for some user agents; confirm titles and canonicals are in the raw HTML returned to Googlebot and Bingbot with curl [Unverified per version].
- Client components that fetch content after mount (`useEffect` fetch) hide content from the initial HTML. Move indexable content to server components.

### 8.2 Next.js Pages Router
- `next/head` per page; `getStaticProps` with `revalidate` for ISR, `getServerSideProps` for SSR; `return { notFound: true }` for 404.
- `next-sitemap` package for sitemaps; confirm it excludes noindex and redirected routes.

### 8.3 Nuxt, Astro, SvelteKit, Remix
| Framework | Head API | Sitemap and robots | Rendering control |
|-----------|----------|--------------------|-------------------|
| Nuxt 3 | `useSeoMeta({ title, description, ogImage })`, `useHead({ link: [{ rel: 'canonical', href }] })` | `@nuxtjs/sitemap`, `@nuxtjs/robots` (or the Nuxt SEO module) | `routeRules`: `prerender`, `isr`, `ssr: false` (avoid for indexable routes) |
| Astro | Layout `<head>` props | `@astrojs/sitemap` | Static by default; `output: 'server'` for SSR |
| SvelteKit | `<svelte:head>` | Custom endpoint `sitemap.xml/+server.ts` | `export const prerender = true` |
| Remix or React Router 7 | `meta` export per route | Resource route | SSR by default |

### 8.4 Client side SPA (React, Vue, Angular without SSR)
Risk: content and links exist only after JavaScript runs; other search engines and most AI crawlers do not render reliably. Options, best first:
1. Migrate indexable routes to an SSR or SSG framework (Next.js, Nuxt, Astro, Remix).
2. Prerender at build for static routes (static site generation of the SPA routes).
3. Dynamic rendering (serving bots a prerendered version) is a workaround Google no longer recommends; use only as a bridge [Official, Google dynamic rendering doc].
Minimum for any SPA: unique URLs per view (History API, no `#` routing), real `<a href>` links, server returns 404 for unknown routes (not 200 with a client side "not found"), title and canonical set per route.

### 8.5 Shopify
| Issue | Fix |
|-------|-----|
| Duplicate product paths `/collections/x/products/y` | Canonical already points to `/products/y`, but crawl is wasted. In product card snippets, link `{{ product.url }}` instead of `{{ product.url \| within: collection }}` |
| Tag filtered collections `/collections/x/tag` and filter params `?filter.p.m...` | Noindex via theme logic for tag pages; disallow low value filter params in `robots.txt.liquid` after checking traffic |
| Pages you want out of index and sitemap | Metafield `seo.hidden` = 1 (namespace `seo`, key `hidden`) adds noindex and removes from the sitemap |
| Sitemap | Auto generated at `/sitemap.xml`; cannot be edited directly |
| Forced URL prefixes `/products/`, `/collections/`, `/pages/`, `/blogs/<blog>/` | Accept; plan migrations around them |
| International | Shopify Markets subfolders or domains add hreflang automatically; verify reciprocity |
| App bloat | Each app may inject scripts; audit for INP and LCP; remove leftovers of uninstalled apps from theme code |
| Structured data | Many themes ship incomplete Product JSON-LD; check for duplicates from apps (reviews apps often add their own) |

Noindex tag pages in `theme.liquid`:
```liquid
{%- if template contains 'collection' and current_tags -%}
  <meta name="robots" content="noindex, follow">
{%- endif -%}
```
Customize `robots.txt.liquid` while keeping Shopify defaults:
```liquid
{% for group in robots.default_groups %}
  {{- group.user_agent }}
  {%- for rule in group.rules -%}
    {{ rule }}
  {%- endfor -%}
  {%- if group.user_agent.value == '*' -%}
    {{ 'Disallow: /collections/*?*filter.v.price*' }}
  {%- endif -%}
  {%- if group.sitemap != blank -%}
    {{ group.sitemap }}
  {%- endif -%}
{% endfor %}
```

### 8.6 WordPress
| Check | Where | Fix |
|-------|-------|-----|
| "Discourage search engines from indexing this site" | Settings > Reading | Must be unchecked on production; it adds a noindex robots meta |
| One SEO plugin only | Plugins | Yoast, Rank Math or AIOSEO; theme or second plugin duplicating titles or schema is common |
| Permalinks | Settings > Permalinks | Post name structure; never change without a redirect map |
| Thin archives | Tag, date, author (single author), format archives | Noindex via SEO plugin; keep category archives if curated |
| Attachment pages | SEO plugin or WP 6.4+ default | Redirect to file or parent |
| Sitemaps | Core `wp-sitemap.xml` or plugin sitemap (plugin usually disables core) | One sitemap source; submit the index |
| Performance | Page cache, image optimization, remove unused plugins, defer scripts | Measure plugin cost with field data |
| Headless WordPress | WPGraphQL plus SEO plugin GraphQL extension | Render SEO fields server side in the frontend |

### 8.7 Webflow
- Per page and CMS template SEO fields (title, description, Open Graph), bound to CMS fields for collections.
- Site settings: auto generated sitemap toggle, robots.txt editor, global canonical URL, 301 redirects (supports pattern capture). Verify setting names in the current UI before instructing a user.
- JSON-LD: page or CMS template custom code in `<head>`, with CMS fields inserted into the JSON. Escape quotes in CMS values.
- Localization adds hreflang for localized locales; verify in source.

### 8.8 Wix, Squarespace and other hosted builders
Use built in SEO settings for titles, descriptions, canonicals, redirects and robots. Rendering is server side on both. Limits: little control over URL prefixes, scripts and server headers. Escalate platform limits to growth-orchestrator if they block a business critical fix.

## 9. Verification protocol for any code fix
1. Raw HTML check with Googlebot user agent (`curl -s -A "...Googlebot..."`): title, meta robots, canonical, hreflang, JSON-LD present and correct.
2. Rendered check: URL Inspection live test (Search Console) or headless browser; compare rendered vs raw for content, links and tags.
3. Status codes: `curl -sI` for 200, 301 or 308 single hop, 404 for unknown routes.
4. Structured data: Rich Results Test and Schema Markup Validator.
5. Crawl the changed template group (Screaming Frog list mode) to catch regressions across many URLs.
6. After deploy (with approval): monitor Page indexing, enhancements and clicks for the template for 2 to 4 weeks.

## 10. Prevent regressions (Scale and Enterprise)
- Add SEO checks to CI: a test that fetches key routes on the preview deployment and asserts status, `<title>` non empty, canonical equals expected, no `noindex` on production routes, JSON-LD parses.
- Monitor production daily with a scheduled crawl of 50 to 500 sample URLs per template and alert on changes in robots meta, canonical, status and title.
- Keep a "SEO surfaces" list in the repo README: files that control metadata, routing, redirects, robots, sitemaps, structured data.
