# Next.js, Headless Commerce and Webflow

> Preview deployments, environment variables, caching pitfalls, rollback, headless commerce basics, and the Webflow staging and publishing loop. Knowledge as of 2026-10.

## 1. Next.js state in 2026

| Date | Change | What it means for releases | Label |
|------|--------|---------------------------|-------|
| 2025-03-21 | CVE-2025-29927: the internal `x-middleware-subrequest` header let requests skip middleware (auth bypass); fixed in 12.3.5, 13.5.9, 14.2.25, 15.2.3. Vercel and Netlify hosted apps were not affected | Never rely on middleware alone for authorization; enforce auth in the route or data layer too | [Official and security research, 2025-03] |
| 2025-10 | Next.js 16: `proxy.ts` succeeds `middleware.ts` (Node.js runtime; `middleware.ts` deprecated but still works), Cache Components with the `"use cache"` directive (with `cacheComponents` enabled, rendering is dynamic unless explicitly cached), Turbopack by default | Upgrades change caching semantics: a page that was static may become dynamic or the reverse. Test caching behavior, not only rendering | [Official, 2025-10] |
| 2025-12-03 | React2Shell (CVE-2025-55182, CVSS 10.0): pre-auth remote code execution in React Server Components (React 19.0, 19.1.0, 19.1.1, 19.2.0; fixed 19.0.1, 19.1.2, 19.2.1); Next.js apps using RSC were exposed; exploitation seen from 2025-12-05 | Any App Router app must be patched; framework CVEs are L5 releases | [Official, React blog 2025-12-03; Microsoft 2025-12-15] |
| 2026-03-18 | Next.js 16.2: faster dev startup, new default error page, stable Adapter API | Adapter API matters for non-Vercel hosting | [Official, 2026-03] |
| 2026-07 (20 or 21) | July security release: nine CVEs fixed in 16.2.11 and 15.5.21, including Server Actions CPU exhaustion (affects most App Router apps), a proxy or middleware bypass with Turbopack and a single i18n locale, SSRF via dynamic rewrite destinations and on custom servers | Patch monthly; check for rewrites that interpolate user input into hostnames | [Official, 2026-07] |
| 2026-08-25 | August security release: 16.3.3 and 15.5.24 fix two critical vulnerabilities | 16.3 is the Active LTS line; 15.5 Maintenance LTS | [Official, 2026-08] |
| 2026-09-22 | Out of band release for a critical upstream dependency issue (16.3.6, 15.5.26) | Out of band patches happen; keep a fast lane | [Official, 2026-09] |
| 2026-09-30 | September release: 16.3.8 and 15.5.27 fix seven issues; two more held for upstream coordination | Minimum safe versions as of 2026-10-08: 16.3.8 or 15.5.27 [verify on nextjs.org/blog/tag/security] | [Official, 2026-09] |

Operating rule: Next.js now ships security releases on a monthly rhythm with pre-announcements. Put a standing L5 patch slot in the release calendar the week of each release and subscribe to the Next.js security advisories tag.

## 2. Preview deployments

| Host | Preview | Protection | Bypass for automated QA | Production promotion |
|------|---------|-----------|------------------------|----------------------|
| Vercel | Every push to a non production branch gets a preview URL; per PR comments | Deployment Protection (Vercel Authentication) is on by default for new projects; password protection is a paid option; protecting production with Vercel Authentication is free on every plan per a 2025 changelog (docs and changelog disagree on plan details; verify) | "Protection Bypass for Automation" secret sent as the `x-vercel-protection-bypass` header (store the secret in CI secrets, never in the repo) | Merge to the production branch or `vercel deploy --prod` (G3); `vercel promote` and `vercel rollback` change production (G3) |
| Netlify | Deploy Previews per PR, branch deploys, `netlify deploy --alias <name>` | Password or SSO protection on paid plans | Use the site password or team SSO session in tests; never disable protection for tests | Publish a deploy or `netlify deploy --prod` (G3); locked deploys stop auto publishing |
| Cloudflare Pages or Workers | Preview per branch | Cloudflare Access | Service tokens for Access (CI secret) | Production branch deploy (G3) |
| Self hosted | Staging host | Basic auth or VPN | Auth header in tests | Deploy pipeline (G3) |

Rules:
1. Every preview must be non indexable: protection on, or `X-Robots-Tag: noindex` on preview hosts. Leaked previews get indexed and duplicate the site.
2. Preview environments must never point to production payment, email or CRM write APIs. Use test keys and sandboxes.
3. Run the QA suite against the exact preview URL that will be promoted (promotion of a tested deployment beats rebuilding).

## 3. Environment variables

| Rule | Why |
|------|-----|
| Scope variables per environment (Development, Preview, Production) | A production secret in Preview means every PR can read it |
| `NEXT_PUBLIC_*` variables are shipped to the browser | Never put secrets in them; review every new `NEXT_PUBLIC_` variable in security review |
| Changing an environment variable requires a redeploy to take effect | QA the redeployed build, not the old one |
| Pull for local use with the host CLI (`vercel env pull .env.local`) | Keep `.env*` in `.gitignore`; `.env.example` holds placeholders only |
| Pixel IDs, GTM IDs, consent configuration per environment | Previews must not send events to production pixels and datasets (or must send them with a test event code), otherwise QA traffic pollutes ad optimization |

## 4. Caching pitfalls (where most Next.js marketing site bugs come from)

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Static or cached PDP after a price change | Old price on page, new price in feed and ads (misrepresentation risk) | Tag fetches (`cacheTag`, `revalidateTag`) and revalidate on product update webhooks; set short `cacheLife` for price and stock; verify from a clean session |
| Personalized content cached at the CDN | One visitor's cart count, geo price or login state shown to others | Do not cache responses that read cookies; vary correctly; move personalization client side or to dynamic segments |
| UTM or click ID query strings creating cache misses | Slow first loads from ads | Normalize cache keys to ignore marketing parameters where the host supports it, but keep them available to client code |
| Upgrade to Next 16 with `cacheComponents` | Pages switch between static and dynamic unexpectedly | Run a build report before and after; compare route rendering modes |
| Stale assets after deploy (version skew) | Errors when an old client calls a new server action or chunk | Enable Skew Protection on Vercel (recommended with Rolling Releases) or equivalent |
| ISR or revalidate on landing pages built for a campaign | Campaign offer changes do not show | On demand revalidation in the release steps; QA checks the live page after revalidation |
| Draft mode or preview mode left open | Drafts visible publicly | Protect draft endpoints with a secret; QA checks that `/api/draft` style routes reject requests without it |

## 5. Rollback

| Host | Mechanism | Notes |
|------|-----------|-------|
| Vercel | Instant Rollback to a previous production deployment (seconds); Rolling Releases (GA) send a fraction (for example 5%) of traffic to the new deployment with error rate and Speed Insights comparison before full promotion; available for one project on Pro and Enterprise, more on Enterprise | Record the current production deployment before every release. After an instant rollback, new deploys may not auto assign production domains until you promote one [Official, 2023 and 2025 changelogs] |
| Netlify | Publish a previous deploy from the Deploys list or API | Rollback does not revert environment variable or function config changes |
| Cloudflare | Roll back a Pages deployment or `wrangler rollback` for Workers (G3) | Bindings and secrets are separate |
| Any host | Git revert plus redeploy | Slowest; use when the bad change is data or config the host rollback does not cover |

Database and CMS changes are not rolled back by a code rollback. Pair code releases that depend on schema or CMS model changes with backward compatible changes (expand, migrate, contract).

## 6. Headless commerce basics

| Topic | Rule |
|-------|------|
| Stack examples | Shopify Hydrogen on Oxygen (Hydrogen 2026.4.x on React Router 7.16 as of 2026-10), Next.js Commerce, Medusa storefronts, commercetools or BigCommerce front ends |
| Checkout | Hand off to the platform's hosted checkout (Shopify checkout URL from the cart). The handoff URL and cart attributes (UTMs, click IDs, consent) are release critical; test them in every release |
| Tokens | Storefront API public tokens are designed for the browser; private Storefront tokens and Admin tokens are server only. Review in security review |
| Analytics and consent | Hydrogen 2026.4.6 and 2026.4.7 changed consent initialization (asynchronous Customer Privacy API, consent required before analytics publish) and require the same origin Storefront API proxy in `createRequestHandler`. After upgrading Hydrogen, retest consent states and analytics events [Official, Hydrogen changelog 2026] |
| Caching | Product and collection data cached with tags and revalidated by webhooks; cart never cached |
| SEO parity | Server render product data and JSON-LD; hand off structured data to `seo` |
| Preview of content | CMS preview must use protected draft mode; QA checks drafts are not public |

## 7. Webflow loop

| Step | How | Gate |
|------|-----|------|
| Build | Designer on the main site, or a page branch (Enterprise only; merging overwrites the original page, and content edits made on the original while branched are discarded on merge) | G1 to G2 |
| Backup | Create a named backup in Site settings > Backups after "Changes saved" shows. Restore points are also created automatically every 50th autosave. Starter sites can restore only one of the two most recent backups unless on a paid workspace plan | G2 |
| Staging | Publish to the `webflow.io` staging subdomain only | G2 |
| QA | Run the suite against the staging URL (`BASE_URL=https://<site>.webflow.io`) | G0 |
| Publish | Publish to custom domains in the Designer, or the Data API `POST /v2/sites/{site_id}/publish` with `customDomains` or `publishToWebflowSubdomain` (rate limited to one successful publish queue per minute, `sites:write` scope). Since 2026-04 the API can publish a single page by page ID; staging to production promotion publishes all staged changes | G3 |
| Rollback | Restore the backup, then publish (human). Restoring an older historical backup can reset CMS, Ecommerce, Page and Asset IDs; CMS deletions are not restored by publishing | G3 |

Webflow specifics:
- Custom code (head, body, page level, embeds) is the main source of performance and security problems. Inventory it in every audit; it is not versioned separately.
- Webflow's official MCP server (remote at `developers.webflow.com/_mcp/server` with OAuth, or local with Node.js 22.3+) exposes elements, styles, variables, collections, custom code, assets and publishing. Authorize only for Site managers and above, and treat any publish tool call as G3.
- Page level publishing permissions exist on Enterprise and higher workspace plans [Secondary, 2026-05].

## 8. Other hosted builders (quick rules)

| Builder | Preview | Rollback | Note |
|---------|---------|----------|------|
| Framer | Staging domain and preview links | Version history restore | Custom code embeds need the same review as Webflow |
| Wix and Squarespace | Preview mode | Site history restore (limited) | Little code control; launch QA and tag governance are the main jobs |
| Landing page tools (Unbounce, Instapage, Leadpages, Replo, Shogun, GemPages) | Draft or preview URLs | Version history varies | Publish is G3; these tools often add their own scripts; include them in tag governance |

## 9. Next.js QA additions

| Check | How |
|-------|-----|
| `next build` passes with no type errors; route table compared before and after (static vs dynamic) | CI log diff |
| `npm ls next react react-dom` shows patched versions | Security review |
| Proxy or middleware protected routes reject requests with crafted headers (`x-middleware-subrequest`) and without auth | Playwright API request tests |
| Rewrites and redirects do not interpolate user input into hostnames | Code review of `next.config` and proxy |
| Server Actions require auth and validate input; rate limits on public actions (forms) | Code review, tests |
| Images: `next/image` with explicit sizes, priority on the LCP image only | Lighthouse LCP discovery insight |
| Previews protected and noindex | `curl -sI <preview-url>` shows auth or `x-robots-tag` |
