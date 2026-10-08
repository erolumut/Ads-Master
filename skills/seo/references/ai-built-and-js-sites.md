# AI-built and JavaScript Sites (Lovable, Bolt, v0, Replit, Cursor, SPAs)

> Knowledge as of 2026-10. Scope: sites generated with AI app builders and vibe coding tools, and any client side rendered single page app (SPA): why they underperform in search and AI answers, how to diagnose them in 15 minutes, fixes per stack, an annotated version of the popular "vibe coded site SEO checklist", what that checklist misses, and how to run `scripts/seo_preflight.py`. Rendering theory and indexing statuses live in [Crawl, index, render](crawl-index-render.md); framework details in [Technical SEO](technical-seo.md); AI crawler policy belongs to `ai-search-optimization`.

## 1. Why these sites fail

AI builders optimize for "it works in the preview". Search engines, social preview bots and AI crawlers read the first HTML response. When that response is an empty shell, everything downstream (titles, links, structured data, content) depends on a renderer that most of them do not run.

| # | Failure | What happens | Who is hurt | Detect |
|---|---------|--------------|-------------|--------|
| 1 | Client side rendered (CSR) shell | Raw HTML is `<div id="root"></div>` plus a script bundle. Google renders later in a queue; Bing renders less predictably; OpenAI, Anthropic and Perplexity crawlers fetched JS files but did not execute them in a 2024 log study [Study, 2024-12, Vercel and MERJ] | Bing, AI search, social previews, slow Google indexing | Preflight `js_shell`; view-source shows no body copy |
| 2 | One title and description for every route | `index.html` ships one static `<title>`; per route titles are set later by JavaScript (or never) | All engines: duplicate titles, rewritten snippets, identical share cards | Preflight `title_duplicate` |
| 3 | No sitemap, or a sitemap with preview hosts | Builders rarely generate `sitemap.xml`; some list `*.lovable.app`, `*.vercel.app` or staging URLs | Discovery, Bing (leans on sitemaps) | Preflight `sitemap_missing`, `sitemap_bad_url` |
| 4 | Hash routing (`/#/pricing`) | Google ignores URL fragments, so every route is one URL [Official, JavaScript SEO basics] | All engines | Preflight `hash_routing` |
| 5 | Soft 404s | Hosting rewrites every path to `index.html` with status 200; unknown slugs render a "not found" view on a 200 | Index bloat, soft 404 reports, crawl waste | Preflight `soft404_risk` (random URL probe) |
| 6 | Per route metadata missing or JS only | Canonical, Open Graph, hreflang and JSON-LD injected client side (react-helmet style) appear only after render | Social bots and AI crawlers never see them; Google sees them late | Preflight `canonical_missing`, empty JSON-LD column |
| 7 | Navigation as buttons | `onClick={() => navigate('/x')}` or `<a>` without `href`: no crawlable links | Discovery and internal PageRank | Preflight `js_links`, `no_internal_links` |
| 8 | Data fetched in the browser | Even with server rendering, products and posts often load from Supabase or an API after hydration [Practitioner, 2026] | Same as CSR for the main content | Raw HTML has headings but no product or post text |
| 9 | Bots blocked at the edge | Cloudflare blocks AI training crawlers by default on new domains since 2025-07-01; from 2026-09-15 Training and Agent classes are blocked by default on ad-carrying pages for new and free zones; challenge pages stop bots that do not run JS [Official, Cloudflare 2025-07 and 2026-07]. See `ai-search-optimization` [technical access](../../ai-search-optimization/references/technical-access-and-crawlers.md) | AI search, sometimes Googlebot and Bingbot [Contested] | Logs by user agent; Cloudflare AI Crawl Control |
| 10 | Staging leftovers | `Disallow: /` copied from a template, `noindex` meta from staging, preview deployments indexed. Vercel adds `X-Robots-Tag: noindex` to preview deployments by default [Official, Vercel docs], so serving production from a preview URL deindexes it | Whole site | Preflight `bot_blocked`, `noindex` |
| 11 | Two hosts for one site | Builder subdomain and custom domain both resolve; no redirect or canonical | Duplicate content, split signals | `site:` search for the builder subdomain; preflight `canonical_offhost` |
| 12 | Heavy bundles | 1 to 3 MB of JS on a landing page, unoptimized PNGs from image generators | LCP and INP on mid-range phones (conversion first) | PSI or CrUX field data; preflight `img_legacy_format` |
| 13 | Generic generated copy | The same AI written hero and feature blocks as thousands of other sites; no first-hand detail | Rankings (no information gain), AI citations, conversion | Manual read; compare with top results |
| 14 | Content behind login | Useful content only inside the app | Invisible to search | Logged out crawl |

Google's position in 2026: it renders JavaScript and removed an outdated "design for accessibility without JavaScript" section from its JavaScript SEO page on 2026-03-04 [Official, 2026-03]. The same page now says pages with a non-200 status may skip rendering (2025-12-18) and that JavaScript must not change the canonical declared in the raw HTML (2025-12-17) [Official, 2025-12]. "Google can render it" is not "every crawler can read it": Bing, AI crawlers and social bots still need server HTML.

## 2. Fifteen minute triage

1. Run the preflight on production (section 8): `python3 seo_preflight.py https://www.example.com/ --limit 50 --out preflight.md`.
2. View source (not DevTools Elements) of the home page, one money page and one deep page. Is the H1, body copy and navigation in the HTML?
3. `curl -sI https://www.example.com/this-page-does-not-exist` must return 404, not 200.
4. `curl -s https://www.example.com/robots.txt` and `/sitemap.xml`: both 200, sitemap lists the custom domain only.
5. Search Console: URL Inspection > Test live URL > View tested page > HTML and Screenshot for a money page. Page indexing report: "Crawled, currently not indexed", "Duplicate without user-selected canonical", "Soft 404".
6. `site:builder-subdomain.example-host.app` in Google: should return nothing once redirected.
7. If on Cloudflare: Security > Bots and AI Crawl Control settings; 30 days of logs by user agent for Googlebot, Bingbot, OAI-SearchBot, Claude-SearchBot, PerplexityBot.
8. Bing Webmaster Tools URL Inspection for the same money page.
9. Classify every route type with the decision table below and write the fix plan.

## 3. Rendering decision per route type

| Route type | Indexable? | Strategy | Notes |
|-----------|-----------|----------|-------|
| Home, landing, pricing, about, features, use cases | Yes | Static generation (SSG) or prerender at build | Cheapest and fastest; content changes ship with deploys |
| Blog, guides, docs, glossary | Yes | SSG with incremental rebuilds (ISR) or prerender | One URL per post; generated sitemap |
| Product and category pages | Yes | SSR or ISR with server data fetching | Prices and stock in HTML; Product JSON-LD server side |
| Search results, filters, sort orders | Usually no | CSR is fine; `noindex` or parameter rules | Keep out of sitemap |
| Logged in app, dashboards, settings | No | CSR | Disallow or noindex; never in sitemap |
| Programmatic pages (locations, integrations, templates) | Only above a content gate | SSG or ISR with per page data | Scaled content abuse risk; see [E-E-A-T and quality](eeat-and-quality-policies.md) |

Choose in this order: (1) framework native SSG or SSR (best), (2) build time prerender of routes (good), (3) prerender service or the builder's crawler prerender (dynamic rendering, which Google calls a workaround and not a long-term solution [Official]), (4) leave CSR only for non indexable routes.

## 4. Fixes per stack

### 4.1 Lovable

| Fact | Detail |
|------|--------|
| New projects | Lovable's FAQ says apps created from 2026-05-13 (2026-06-22 for Enterprise workspaces) run on TanStack Start, which renders pages on the server; each publish builds a server rendered app, prerenders routes that do not depend on request data and deploys as an edge Worker [Official, Lovable FAQ and blog, 2026-05]. Some third-party guides date the SSR launch to 2026-04-20 [Contested]; check the stack in the project, not the creation date |
| Older projects | React plus Vite, rendered in the browser. Lovable serves prerendered copies of published pages to verified search engines, social preview bots and AI crawlers via a headless browser [Official, 2026]. That is dynamic rendering: unverified agents (including this preflight) still get the shell |
| Upgrade | Eligible older projects can be upgraded to TanStack Start [Official, 2026] |
| Remaining gap | Generated code often reads Lovable Cloud (Supabase) from the browser, so lists and posts arrive after load even on TanStack Start [Practitioner, 2026] |

Fix list for a Lovable project:
1. Confirm the stack: TanStack Start files (`app/routes`, `createFileRoute`, server functions) vs `vite.config.ts` plus `react-router-dom` only.
2. Old stack: upgrade if eligible. If not, accept the crawler prerender for Google and Bing but verify with URL Inspection and Bing URL Inspection, and plan a migration for money pages.
3. Move content queries into route loaders or server functions so the HTML contains the data. Prompt the builder explicitly: "Load posts in the route loader on the server, not in useEffect."
4. Per route head: define title, description, canonical and Open Graph in each route's `head` option (TanStack Router `head: () => ({ meta: [...], links: [...] })`) [Official, TanStack docs; verify the API for your version].
5. Add a server route that returns `sitemap.xml` from the same data the pages use, and a `robots.txt` with the Sitemap line.
6. Make the custom domain primary. Redirect or canonicalize the builder subdomain to it [Unverified how each plan handles the subdomain; check project settings].
7. Return 404 for unknown slugs (`notFound()` in the loader) instead of rendering an empty page.

### 4.2 Bolt, Replit, Cursor and other Vite plus React SPAs

These tools usually scaffold Vite, React and React Router in SPA mode unless told otherwise [Practitioner consensus]. Options, best first:

| Option | Effort | Result |
|--------|--------|--------|
| A. React Router v7 framework mode with `prerender` (static hosting) or `ssr: true` | Low to medium | Real HTML per route, per route `meta`, works on static hosts |
| B. Move marketing routes to Astro or Next.js, keep the app as SPA under `/app` | Medium | Best performance for content; two codebases or a monorepo |
| C. `vite-react-ssg` style build time prerender | Low | Static HTML for listed routes; check library maintenance first |
| D. Prerender service at the edge | Low | Dynamic rendering workaround; extra cost, cache staleness, cloaking risk if content differs |

React Router v7 prerender (framework mode):

```ts
// react-router.config.ts
import type { Config } from "@react-router/dev/config";
import { getPostSlugs } from "./app/lib/content.server";

export default {
  ssr: false, // static hosting; set true when a Node or edge runtime is available
  async prerender() {
    const posts = await getPostSlugs();
    return ["/", "/pricing", "/about", ...posts.map((s) => `/blog/${s}`)];
  },
} satisfies Config;
```

```tsx
// app/routes/pricing.tsx: per route metadata in the HTML
export function meta() {
  return [
    { title: "Pricing | Example App" },
    { name: "description", content: "Plans from free to team, billed monthly or yearly." },
    { tagName: "link", rel: "canonical", href: "https://www.example.com/pricing" },
    { property: "og:title", content: "Pricing | Example App" },
  ];
}
```

Hosting rules that create soft 404s, and the fix:

| Host | SPA default | Fix |
|------|------------|-----|
| Netlify | `_redirects` rule `/* /index.html 200` | Serve prerendered files; end with `/* /404.html 404` |
| Cloudflare Pages | No top-level `404.html` means Pages assumes an SPA and serves index for unknown paths [Official, Cloudflare Pages docs] | Add a real `404.html` |
| Vercel | `rewrites` to `/index.html` in `vercel.json` | Remove the catch-all for content routes; framework not-found page |
| Nginx | `try_files $uri /index.html;` | `try_files $uri $uri/ =404;` for content paths |

### 4.3 v0 and Next.js projects

v0 generates Next.js App Router code, so server rendering is available, but generated pages often mark whole trees `"use client"`, fetch in `useEffect` and skip metadata [Practitioner consensus]. Fixes:

```tsx
// app/layout.tsx
import type { Metadata } from "next";
export const metadata: Metadata = {
  metadataBase: new URL("https://www.example.com"),
  title: { default: "Example App", template: "%s | Example App" },
  description: "One sentence on what the product does for whom.",
  alternates: { canonical: "/" },
};

// app/blog/[slug]/page.tsx: server component, data on the server
import { notFound } from "next/navigation";
export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }) {
  const post = await getPost((await params).slug);
  if (!post) return {};
  return {
    title: post.title,
    description: post.summary,
    alternates: { canonical: `/blog/${post.slug}`, languages: { "tr-TR": `/tr/blog/${post.slugTr}` } },
    openGraph: { title: post.title, images: [post.image] },
  };
}
export default async function Page({ params }: { params: Promise<{ slug: string }> }) {
  const post = await getPost((await params).slug);
  if (!post) notFound(); // real 404 status
  return <article><h1>{post.title}</h1>{/* server rendered body */}</article>;
}
```

```ts
// app/sitemap.ts
import type { MetadataRoute } from "next";
export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const posts = await getAllPosts();
  return [
    { url: "https://www.example.com/", lastModified: new Date() },
    ...posts.map((p) => ({ url: `https://www.example.com/blog/${p.slug}`, lastModified: p.updatedAt })),
  ];
}

// app/robots.ts
import type { MetadataRoute } from "next";
export default function robots(): MetadataRoute.Robots {
  return { rules: [{ userAgent: "*", allow: "/", disallow: ["/app/", "/api/"] }], sitemap: "https://www.example.com/sitemap.xml" };
}
```

Streaming metadata: on dynamically rendered routes, Next.js streams `generateMetadata` output after the first bytes for normal user agents; agents matched by the `htmlLimitedBots` config get blocking metadata in `<head>` [Official, Next.js docs, since 15.2]. Third-party testing says the default list covers Googlebot, Bingbot and major social bots [Unverified for AI crawlers]. If AI crawler visibility matters, prefer static routes for marketing pages, or extend the list (setting it replaces the default, so include the defaults you need):

```js
// next.config.js (Next.js 15.2 and later)
module.exports = {
  htmlLimitedBots: /Googlebot|Bingbot|OAI-SearchBot|ChatGPT-User|Claude-SearchBot|ClaudeBot|PerplexityBot|facebookexternalhit|Twitterbot|LinkedInBot|Slackbot|Discordbot/i,
};
```

Next.js 16 (current major since 2025-10) renamed `middleware.ts` to `proxy.ts` [Official, 2025-10; verify in the project's version]. Redirects belong in `next.config` `redirects()` (single hop, 308 by default for permanent).

### 4.4 Astro, Nuxt, SvelteKit and Vite SSG

| Stack | Render | Metadata | Sitemap and robots | 404 |
|-------|--------|----------|--------------------|-----|
| Astro | Static by default; islands hydrate only interactive parts | Layout `<head>` with props per page | `@astrojs/sitemap` (requires `site` in config); `public/robots.txt` | `src/pages/404.astro` |
| Nuxt | SSR by default; `routeRules` for prerender or ISR | `useSeoMeta`, `useHead` | `@nuxtjs/sitemap`, `@nuxtjs/robots` | `error.vue` with status from `createError` |
| SvelteKit | SSR by default; `export const prerender = true` per route | `<svelte:head>` | Server route `sitemap.xml/+server.ts` | `+error.svelte` with `error(404)` |
| Vite plus Vue | `vite-ssg` build time prerender | `@unhead/vue` | Plugin or build script | Static 404 file on host |

Astro is the lowest effort rebuild target for content sites made in an AI builder: copy components, keep interactive widgets as islands.

### 4.5 Sitemaps, robots and status codes via framework routes

| Need | Rule |
|------|------|
| Sitemap source | Generate from the same data that renders the pages, so deleted pages leave the sitemap automatically |
| Sitemap content | Only canonical, indexable, 200 URLs on the production host; accurate `lastmod` (Google uses it when it is consistently accurate and ignores `priority` and `changefreq`) [Official] |
| robots.txt | Allow content; disallow app, API and infinite parameter spaces; never block JS or CSS needed for rendering; add `Sitemap:` |
| Status codes | Unknown routes 404, removed content 404 or 410, moved content one 301 or 308 hop |
| Submission | Search Console and Bing Webmaster Tools sitemaps; IndexNow for Bing and others on publish |

## 5. Acceptance tests after a fix

- [ ] Preflight shows 0 Critical and 0 High on money templates.
- [ ] Raw HTML of every indexable template contains the H1, main copy, navigation links as `<a href>`, unique title, description, absolute self canonical and JSON-LD.
- [ ] Random URL returns 404; deleted product returns 404 or redirects to its closest replacement.
- [ ] Sitemap lists only production host URLs that return 200 and self canonicalize.
- [ ] URL Inspection rendered HTML matches raw HTML for content and links.
- [ ] Builder subdomain and preview deployments are not indexable.
- [ ] Logs show 200 responses for Googlebot, Bingbot and the AI search bots the policy allows.
- [ ] Field CWV at p75 (CrUX or RUM) within LCP 2.5 s, INP 200 ms, CLS 0.1 for mobile, or a plan exists.

## 6. The popular checklist, annotated

The human shared a widely circulated checklist for vibe coded sites. Verdicts: Correct (do it as stated), Partly correct (right direction, wrong rule or priority), Outdated (was true, no longer), Myth (not how search works).

| # | Checklist item | Verdict | The real rule | Evidence |
|---|---------------|---------|---------------|----------|
| 1 | Render server side | Correct, refined | Server HTML for every indexable route: SSR, SSG or build time prerender all qualify. Not every route needs it (app screens can stay CSR). Required for Bing reliability, AI crawlers and social previews | [Official, Google JS SEO basics 2025-12 to 2026-03]; [Study, 2024-12] |
| 2 | Sitemap | Correct, not sufficient | Generated, canonical 200 URLs only, accurate lastmod, declared in robots.txt. Helps discovery; does not make pages rank or get indexed by itself | [Official] |
| 3 | Submit to Search Console | Correct | Verify a Domain property, submit the sitemap, inspect key URLs. Do the same in Bing Webmaster Tools. "Request indexing" is for a few key URLs, not a fix for quality | [Official] |
| 4 | Unblock Googlebot | Correct | Check robots.txt, meta robots, X-Robots-Tag, WAF and CDN bot rules, and JS or CSS blocks. Verify in logs, not only in robots.txt | [Official] |
| 5 | Remove wrong noindex | Correct | Look in meta tags, HTTP headers and framework config; staging and preview leftovers are the usual cause | [Official] |
| 6 | Kill redirect chains | Correct | One hop. Googlebot follows up to 10 hops, but chains waste crawl and slow users; update internal links to the final URL | [Official, Google HTTP status docs] |
| 7 | Fix 404s | Partly correct | 404 for truly gone URLs is normal and does not harm the site. Fix broken internal links, 404s with links or traffic, and soft 404s (200 for missing pages), which is the real SPA problem | [Official] |
| 8 | Canonicals | Correct | One absolute self referencing canonical in raw HTML, consistent with sitemap and internal links. It is a hint; JS must not change it | [Official, 2025-12] |
| 9 | Meta description per page | Partly correct | Not a ranking factor; Google rewrites many snippets. Write unique descriptions for money pages and share cards; do not mass generate filler | [Official] |
| 10 | One H1 per page | Myth (as a Google rule) | Google has said multiple H1s are fine. Use one clear main heading for users and accessibility; the preflight reports it as Low | [Official, Google Search Central, 2019] |
| 11 | FAQ schema | Outdated | FAQ rich results stopped showing in Google Search for all sites from 2026-05-07 (limited to authoritative government and health sites since 2023-08); Search Console FAQ reporting retired 2026-06. Keep visible FAQs when users need them; markup is harmless but no lever | [Official, 2026-05] per [Structured data](structured-data.md) |
| 12 | Breadcrumbs | Correct, refined | Visible breadcrumbs plus BreadcrumbList markup help hierarchy and internal links. Google simplified mobile result URLs to the domain in 2025-01, so the SERP display gain is mostly desktop | [Official, 2025-01] |
| 13 | Link orphan pages | Correct | Every indexable page needs contextual internal links from relevant hubs; sitemap only discovery is weak | [Official]; preflight `sitemap_orphan` |
| 14 | Alt text | Correct | Descriptive alt for meaningful images (image search, accessibility, European Accessibility Act since 2025-06-28); empty alt for decorative images; no keyword stuffing | [Official] |
| 15 | WebP or AVIF | Partly correct | The goal is fewer bytes and a fast LCP image: modern formats via an image CDN, responsive `srcset`, correct dimensions, priority hint on the LCP image. A well compressed JPEG is not a ranking problem | [Official, web.dev] |
| 16 | Fix layout shifts | Correct | CLS at or under 0.1 at p75 field data: width and height on media, reserved space for embeds and banners, font loading strategy | [Official] |
| 17 | Load under 2 seconds | Myth (wrong metric) | There is no 2 second rule. Core Web Vitals at p75 of real user (field) data: LCP 2.5 s, INP 200 ms, CLS 0.1. Page experience is a tie breaker for ranking; speed matters more for conversion | [Official, web.dev] |
| 18 | Remove AI slop | Correct, refined | Google does not penalize AI assistance; the scaled content abuse policy (2024-03) targets mass produced low value pages however made, and the QRG (2025-01) rates them Lowest. Fix with first-hand detail, data and expert review, or prune | [Official] |
| 19 | Real author bio | Partly correct | Author pages help trust, but E-E-A-T is a quality framework, not a ranking factor: sourcing, accuracy, about and contact pages, reputation, reviews and site purpose matter more. Essential for YMYL | [Official, QRG] |
| 20 | Quality backlinks | Correct, slow | Earned links from relevant sites through useful assets, digital PR and partners. Paid links need `rel="sponsored"`; link schemes trigger spam systems | [Official] |
| 21 | Rank number 1 by Friday | Myth | New pages take days to weeks to be indexed and new sites usually 3 to 6 months to earn meaningful non-brand traffic. Track leading indicators (indexed pages, impressions, ranking spread) | [Practitioner consensus] |

## 7. What the checklist misses

| Missing item | Why it matters | Where |
|-------------|----------------|-------|
| Search intent and keyword targeting | A perfectly crawlable page that targets no demand gets no traffic | [Keyword research and topical maps](keyword-research-and-topical-maps.md) |
| Unique titles per route | The single most common AI builder defect (one title site wide) | Section 4; preflight `title_duplicate` |
| Internal linking architecture | Hubs, breadcrumbs, related links and money pages within 3 clicks decide importance | [Site architecture](site-architecture-and-internal-linking.md) |
| Content depth and information gain | Generated sites repeat the same claims; original data, experience and specifics win rankings and AI citations | [On-page and content](on-page-and-content.md) |
| Organization, WebSite and Product structured data | Entity understanding, merchant listings, product snippets | [Structured data](structured-data.md) |
| Real 404s and one canonical host | Soft 404s and duplicate builder hosts silently split signals | Sections 4.2 and 4.5 |
| Bing Webmaster Tools and IndexNow | Bing feeds Copilot and several AI answer engines; it relies more on sitemaps and server HTML | [Tools, APIs and MCP](tools-api-mcp.md) |
| AI crawler access | OAI-SearchBot, Claude-SearchBot, PerplexityBot need raw HTML and must not be blocked by robots.txt or the CDN | Hand off to `ai-search-optimization` |
| Measurement | Search Console, Bing Webmaster Tools and GA4 baselines before and after the fix; annotate the release | [Measurement and reporting](measurement-and-reporting.md) |
| Local SEO and Google Business Profile | For local businesses the map pack matters more than the site | [Local SEO](local-seo.md) |
| hreflang | Multi-language builder sites often translate in the browser with one URL; each language needs its own URL with reciprocal hreflang | [International SEO](international-seo.md) |
| Mobile parity and accessibility | Mobile first indexing; EAA obligations in the EU | [Technical SEO](technical-seo.md); `cro` |

## 8. Running seo_preflight.py

Location: `skills/seo/scripts/seo_preflight.py`. Python 3 standard library only; no install.

```bash
# production, polite defaults (1 request per second, 50 URLs)
python3 seo_preflight.py https://www.example.com/ --limit 50 --out preflight.md --json preflight.json

# local build before a release (start the production build, not the dev server)
npm run build && npm run preview   # or: npx serve dist, next start, astro preview
python3 seo_preflight.py http://localhost:4173/ --limit 200 --delay 0.05 --fail-on high

# CI gate: exit code 2 when any High or Critical issue exists
python3 seo_preflight.py "$PREVIEW_URL" --limit 100 --fail-on high --quiet --out preflight.md
```

| Option | Default | Meaning |
|--------|---------|---------|
| `--limit` | 50 | Max URLs fetched (pages, redirects and errors) |
| `--delay` | 1.0 | Seconds between requests; a larger robots.txt Crawl-delay wins; under 0.1 only for local hosts |
| `--thin-words` | 150 | Raw HTML word count below which a page is thin; with a mount div (`root`, `app`, `__next`, `__nuxt`) it is a JS-only shell |
| `--no-sitemap-crawl` | off | Skip sitemap URLs that links did not reach |
| `--fail-on` | none | `critical`, `high` or `medium`: exit 2 for CI |
| `--json` | none | Machine readable output for other agents |

What it checks: HTTP status, redirect chains and loops, robots.txt per bot (Googlebot, Bingbot, OAI-SearchBot, GPTBot, ChatGPT-User, PerplexityBot, ClaudeBot, Claude-SearchBot, Google-Extended) with RFC 9309 longest match, JS and CSS blocked for Googlebot, sitemaps (index files, gzip), orphans and sitemap hygiene, meta robots and X-Robots-Tag noindex, canonical (missing, multiple, relative, other, other host, bad target), title and description (missing, duplicate, length), H1 count, raw HTML word count and JS-only shells, HTML over 2 MB, images (missing alt, legacy formats, missing dimensions), JSON-LD types and parse errors (flags FAQPage and HowTo as no rich result), hreflang (codes, self reference, reciprocity, x-default, bad targets), html lang, viewport (missing, zoom disabled), internal link counts, non-crawlable links, hash routing, click depth, broken internal links and a random URL soft 404 probe.

How to read it: fix Critical and High first. Bot blocks for AI crawlers are reported for a policy decision, not as defects. A clean preflight does not prove Google indexes the page (quality still decides); a failing preflight proves a non-rendering crawler cannot read it.

Limits: no JavaScript (by design), no login or basic auth, same host only (subdomains are other hosts), robots.txt rules only (CDN and WAF blocks show up as 403 or challenge pages, and verified-bot prerender services may serve Googlebot different HTML than this crawler sees: confirm with URL Inspection). Builder prerender for verified bots means the preflight may report a shell that Google does not see; record both views.

Tested on a local fixture with deliberate defects (2026-10-08): it flagged the JS shell (Critical), hash routing, soft 404 probe, 404 and 500 internal links, a 2 hop redirect chain and the link pointing to it, a noindex page in the sitemap, an X-Robots-Tag noindex, invalid JSON-LD and FAQPage markup, `en-UK` and a non-reciprocal hreflang, duplicate titles across 3 routes, missing and relative canonicals, two H1s, images without alt and dimensions, zoom disabled, missing lang, a `javascript:` link, an orphan sitemap URL, a 404 in the sitemap, `/assets/` blocked for Googlebot, GPTBot and PerplexityBot disallowed, and skipped the robots disallowed `/private/` path.

## 9. Outputs and handoffs

- Save as `ads-master/outputs/seo/YYYY-MM-DD_seo_js-site-fix-plan.md`: preflight summary, route classification table, chosen strategy per route type, diffs or builder prompts, acceptance tests, rollback.
- Hand off: `ai-search-optimization` (AI crawler policy and CDN settings), `site-engineer` (framework migration, hosting rules, release QA), `cro` (mobile speed and conversion on the rebuilt templates), `measurement` (tracking after a framework change, SPA page views).

## 10. Sources

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | Understand JavaScript SEO basics | Google Search Central | https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics | updated 2025-12 to 2026-03 | Rendering queue, History API over fragments, canonical in raw HTML, non-200 pages may skip rendering |
| 2 | Latest Google Search documentation updates | Google Search Central | https://developers.google.com/search/updates | 2025-12-17, 2025-12-18, 2026-03-04 | Dates of the JavaScript doc changes |
| 3 | Google JavaScript SEO docs now say non-200 status codes might not be rendered | Search Engine Roundtable | https://www.seroundtable.com/google-render-non-200-code-40627.html | 2025-12 | Non-200 rendering change |
| 4 | Google removes JavaScript SEO warning, says it is outdated | Search Engine Journal | https://www.searchenginejournal.com/google-removes-javascript-seo-warning-says-its-outdated/568829/ | 2026-03 | Accessibility section removal |
| 5 | Dynamic rendering as a workaround | Google Search Central | https://developers.google.com/search/docs/crawling-indexing/javascript/dynamic-rendering | n.d. | Dynamic rendering is not a long-term solution |
| 6 | HTTP status codes, network and DNS errors | Google Search Central | https://developers.google.com/search/docs/crawling-indexing/http-network-errors | n.d. | Up to 10 redirect hops, 404 handling |
| 7 | The rise of the AI crawler | Vercel | https://vercel.com/blog/the-rise-of-the-ai-crawler | 2024-12 | AI crawlers fetch but do not execute JavaScript |
| 8 | FAQ: SSR and prerendering | Lovable | https://lovable.dev/faq/deployment/rendering/ssr-prerendering-when-needed | 2026 | TanStack Start from 2026-05-13, crawler prerender for older apps |
| 9 | Building apps using TanStack Start | Lovable blog | https://lovable.dev/blog/building-apps-using-tanstack-start | 2026 | Server rendered builds as edge Workers, automatic route prerender |
| 10 | Lovable SEO in 2026: TanStack Start, prerendering, or Next.js migration? | nextlovable (third party) | https://nextlovable.com/lovable-seo | 2026 | Client side data fetching gap, contested launch dates |
| 11 | Metadata and OG images | Next.js docs | https://nextjs.org/docs/app/getting-started/metadata-and-og-images | 16.x | Metadata API, streaming metadata, htmlLimitedBots |
| 12 | Server-side streaming SEO in 2026: a cross-framework study | Unhead | https://unhead.unjs.io/learn/research/streaming-head-performance | 2026 | Default htmlLimitedBots coverage (third party) |
| 13 | Content Independence Day: no AI crawl without compensation | Cloudflare | https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/ | 2025-07-01 | Default AI crawler blocking on new domains |
| 14 | FAQPage structured data | Google Search Central | https://developers.google.com/search/docs/appearance/structured-data/faqpage | 2026-05 | FAQ rich results retired (see structured-data reference) |
| 15 | Core Web Vitals | web.dev | https://web.dev/articles/vitals | n.d. | LCP 2.5 s, INP 200 ms, CLS 0.1 at p75 |
| 16 | Spam policies for Google web search | Google Search Central | https://developers.google.com/search/docs/essentials/spam-policies | n.d. | Scaled content abuse |
| 17 | Cloudflare Pages: serving pages (SPA rendering) | Cloudflare docs | https://developers.cloudflare.com/pages/configuration/serving-pages/ | n.d. | SPA fallback when no 404.html exists |
| 18 | Search Central blog (mobile breadcrumb simplification, 2025-01) | Google | https://developers.google.com/search/blog | 2025-01 | Mobile result URLs show the domain |
| 19 | Vercel documentation (preview deployments carry X-Robots-Tag noindex) | Vercel | https://vercel.com/docs | n.d. | Preview deployments are not indexable by default |
