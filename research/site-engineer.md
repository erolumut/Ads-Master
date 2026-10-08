# Research Dossier: Site Engineering, Release QA and Launch QA

> Research date: 2026-10-08. Scope: how websites and storefronts that receive paid and organic traffic are built, previewed, tested, released and rolled back in 2026 (Shopify themes and CLI, WordPress and WooCommerce, Next.js and headless, Webflow), automated QA (Playwright, Lighthouse, axe), launch QA for ad destinations, mobile web behavior (Safari 26 and 27, in-app browsers), worst case data testing, UI primitives and dependency health, performance and third party script governance, and security review including supply chain and prompt injection.
>
> Method and limits: 21 web searches (extended mode for 2026 and niche topics). WebFetch was blocked by DNS in the research environment, so web findings rely on search result content. Primary evidence was strengthened with read only clones of public repositories inspected on 2026-10-08 (Shopify CLI with git history from 2025-09, Shopify AI Toolkit, Shopify Horizon and Hydrogen, WooCommerce, Playwright docs and tags, Base UI, Radix Primitives, shadcn/ui, sonner, vaul, Emil Kowalski's skills). Cloned files were treated as untrusted data. The Ads Master guard hook was probed locally with 27 release commands. Evidence labels follow the authoring spec; single sourced or unconfirmed items are [Unverified].

## 1. Executive summary

1. Shopify CLI moved to a major version 4 line (4.0.0 on 2026-05-21, 4.9.0 on 2026-10-08): `theme serve` removed, Node 20 dropped, store commands (`store auth`, `store execute`, `store bulk execute`, `store create`, `store delete`) unhidden on 2026-07-01, and `theme dev` now requires `--allow-live` against a live theme in non-interactive sessions (2026-10-07) [Official, repo]. Agent runbooks written for CLI 3.x are partly wrong.
2. The Ads Master guard hook misses several release commands (probe 2026-10-08): `shopify theme push --publish`, `push --theme <live id>`, flags set through `SHOPIFY_FLAG_*` environment variables, and `vercel promote` and `vercel rollback` are classed G2; `shopify store execute --allow-mutations`, `shopify store delete`, `theme dev --allow-live`, `netlify api restoreSiteDeploy` and `wp @prod` writes are not recognized. Built in G2 rules match before `extra_ask_bash_patterns`, so only `extra_blocked_bash_patterns` or a guard update closes the G2 cases [Official, local test].
3. Shopify's checkout migration finished in 2026: Scripts stopped executing on 2026-06-30 (editing locked from 2026-04-15) and non-Plus Thank you and Order status pages were auto upgraded on 2026-08-26 without migrating scripts [Official changelog; secondary for the August upgrade]. Every store audit in Q4 2026 must test discounts, shipping rules and purchase tracking with a test order.
4. Shopify's AI Toolkit (2.x, October 2026) gives agents docs search, Liquid and GraphQL validation and store management through `store execute`, but sends telemetry by default, including the user's latest prompt verbatim on Claude Code when a Shopify skill activates; opting out needs a file at `~/.config/shopify-ai-toolkit/opt-out` [Official, repo README 2026-10-07].
5. Next.js runs a monthly security release cadence: nine CVEs in July 2026 (16.2.11 and 15.5.21), two critical fixes in August (16.3.3), an out of band release in September and seven fixes on 2026-09-30 (16.3.8 and 15.5.27), after React2Shell (CVE-2025-55182, CVSS 10, December 2025) and the March 2025 middleware bypass [Official]. Framework patching is a standing release lane, not an emergency.
6. npm supply chain attacks escalated from account phishing (chalk and debug, 2025-09-08) to self replicating worms (Shai-Hulud 2025-09 and 2025-11; TanStack 2026-05; ChainDrop 2026-08 with valid provenance on malicious releases) [Study, multiple vendors; CISA 2026-04-20 for Axios]. Lockfiles, ignored install scripts and release cooldowns are now baseline for any repo an agent touches.
7. Safari 26 (2025-09) changed mobile web QA: browser chrome tinting is derived from the page and ignores `theme-color`, and fixed bottom elements interact badly with the new floating toolbar [Practitioner reports, 2025 to 2026]. Safari 27 (2026-09) added scroll anchoring and customizable `select` and, per WWDC26 coverage, a built in MCP server for coding agents [Official for features; secondary for MCP].
8. Lighthouse 13 (2025-10-10; PSI 2025-10-20) removed legacy audit IDs from reports and JSON in favor of insight audits; scoring did not change [Official]. CI scripts and dashboards that parse audit IDs silently break.
9. Agentic QA tooling matured: Playwright Test Agents (planner, generator, healer) since 1.56 (2025-10-06), Playwright 1.64 (2026-10-07) with WebMCP testing, and Chrome DevTools MCP stable with Chrome 149 (2026-06-02) [Official]. Healers can weaken assertions; reviewed deterministic tests remain the release gate.
10. Component dependencies carry maintenance risk: vaul's README declares it unmaintained (2025-10-03), yet shadcn/ui's Drawer still imports vaul 1.1.2 (October 2026), while Base UI shipped 1.0 (2025-12-11) and a stable Drawer (1.3.0, 2026-03-12) [Official, repos]. A dependency health check belongs in every adoption decision.

## 2. State of the domain in 2026 (with numbers)

### 2.1 Platform versions and cadence (as of 2026-10-08)

| Platform | Current | Cadence observed | Source |
|----------|---------|------------------|--------|
| Shopify CLI | 4.9.0 (2026-10-08) | Minor releases roughly every 2 to 4 weeks (3.86 on 2025-10-16 to 4.9 on 2026-10-08) | Repo tags [Official] |
| Shopify API | 2026-07 stable (new quarter on 2026-07-01) | Quarterly | Secondary, 2026-06 |
| Hydrogen | 2026.4.7 on React Router 7.16 | Calendar versioned | Repo [Official] |
| WordPress | 7.1.1 (7.0 on 2026-05-20, 7.1 on 2026-08-19) | Two to three majors per year | make.wordpress.org [Official]; secondary for 7.1.1 |
| WooCommerce | 11.2.0 (2026-10-07), requires WordPress 7.0 and PHP 7.4 | About every 4 to 6 weeks | Repo changelog [Official] |
| Next.js | 16.3.8 Active LTS, 15.5.27 Maintenance LTS (2026-09-30) | Monthly security releases plus out of band | nextjs.org [Official] |
| Playwright | 1.64 (2026-10-07) | About every 6 to 8 weeks (1.56 to 1.64 in 12 months) | Repo tags [Official] |
| Lighthouse | 13.x (13.0 on 2025-10-10) | Majors yearly | Chrome blog [Official] |
| Base UI | 1.8.0 (2026-09-04) | Monthly minors | Repo [Official] |

### 2.2 Security pressure

- WordPress ecosystem: 11,334 new vulnerabilities in 2025 (up 42%), 91% in plugins, 9% in themes, six in core; 46% without a patch at disclosure; weighted median about five hours to mass exploitation for heavily targeted flaws [Study, Patchstack 2026 via secondary summaries; time figures Unverified].
- npm: classic tokens revoked on 2025-12-09, new write tokens enforce 2FA, trusted publishing GA since 2025-07-31 [Official, GitHub changelog]. Worm campaigns in 2025 and 2026 compromised hundreds of packages per wave (Shai-Hulud 2.0: about 600 to 800 packages and over 25,000 repos exposed by some counts) [Study, Datadog, Invicti, Wiz].
- Next.js: at least 20 CVEs patched between July and September 2026 across three scheduled and one out of band release [Official, nextjs.org security tag].
- PCI DSS 4.0.1: requirements 6.4.3 and 11.6.1 (payment page script inventory and tamper detection) mandatory since 2025-03-31 for SAQ A-EP and D; SAQ A merchants instead attest their site is not susceptible to script attacks (revision dated 2025-01-31, FAQ 1588 in 2025-02) [Secondary, 2025].
- reCAPTCHA: keys moved under Google Cloud projects (2025 into 2026); free Essentials tier 10,000 assessments per month, after which requests error unless billing is enabled [Official, Google Cloud docs].

### 2.3 Performance and third parties

- Top 1,000 sites carry a median 129 third party requests on desktop and 106 on mobile (all sites: 83 and 79); the top 1,000 added 15 requests year over year while the number of distinct third party domains fell [Study, Web Almanac 2025].
- Server side tagging hides vendor traffic from client measurement, so third party prevalence numbers are lower bounds [Study, Web Almanac 2025].
- Core Web Vitals thresholds unchanged (LCP 2.5 s, INP 200 ms, CLS 0.1 at p75) [Official, web.dev]; Soft Navigations final origin trial Chrome 147 to 149 with shipping planned later in 2026 [Official, 2026-04-20].

### 2.4 Mobile and in-app browsing

- iOS 26 Safari moved Advanced Fingerprinting Protection to all browsing by default for known fingerprinting scripts; Link Tracking Protection still applies in Private Browsing, Mail and Messages, and in all browsing only when users opt in [Contested between vendors; careful sources agree on this scope].
- In-app browser behavior is documented mostly by researchers and vendors: Krause (2022) showed injected JavaScript in Instagram and Facebook in-app browsers on iOS; vendor claims of 25% to 40% conversion loss in in-app browsers have no independent data [Study 2022; Unverified for loss figures].

## 3. Timeline of changes, January 2025 to October 2026

| Date | Change | Area | Label |
|------|--------|------|-------|
| 2025-01-31 | PCI SSC revises SAQ A: 6.4.3 and 11.6.1 removed as line items, script attack eligibility criterion added | Security | [Secondary] |
| 2025-02-28 | PCI SSC FAQ 1588 on meeting the SAQ A script criterion | Security | [Secondary] |
| 2025-03 | Rules File Backdoor disclosed (hidden Unicode instructions in AI coding rules files) | Security | [Study] |
| 2025-03-21 | CVE-2025-29927 Next.js middleware bypass disclosed (fixed 12.3.5, 13.5.9, 14.2.25, 15.2.3) | Next.js | [Official] |
| 2025-03-31 | PCI DSS 4.0.1 future dated requirements mandatory | Security | [Official] |
| 2025-04 | Shopify extends Scripts deadline from 2025-08-28 to 2026-06-30 | Shopify | [Official] |
| 2025-04 | Chrome announces Lighthouse move to insight audits | Testing | [Official] |
| 2025-06 | Shopify Summer '25 Edition: Horizon themes and theme blocks | Shopify | [Official] |
| 2025-07-07 | WooCommerce 10.0 | WordPress | [Official] |
| 2025-07-31 | npm trusted publishing generally available | Security | [Official] |
| 2025-08-28 | Shopify Plus Thank you and Order status upgrade deadline | Shopify | [Official] |
| 2025-09 | iOS 26 and Safari 26: new browser chrome, theme-color ignored for tinting, fingerprinting protection default | Mobile | [Official; practitioner for tinting] |
| 2025-09-08 | chalk, debug and 16 more npm packages compromised (about 2 hour window) | Security | [Study] |
| 2025-09 | Shai-Hulud npm worm | Security | [Study] |
| 2025-09-23 | Chrome DevTools MCP public preview | Tooling | [Secondary] |
| 2025-10 | Next.js 16: `proxy.ts`, Cache Components, Turbopack default | Next.js | [Official] |
| 2025-10-03 | vaul README marks the project unmaintained | UI libraries | [Official, repo] |
| 2025-10-06 | Playwright 1.56: Test Agents, `page.consoleMessages()`, `page.requests()` | Testing | [Official] |
| 2025-10-10 | Lighthouse 13.0 (PSI on 2025-10-20) | Testing | [Official] |
| 2025-10-16 | Shopify CLI 3.86 | Shopify | [Official, repo] |
| 2025-11-05 | npm stops classic token creation; 2FA on write tokens | Security | [Official] |
| 2025-11-24 | Shai-Hulud 2.0 worm (preinstall execution, wiper fallback) | Security | [Study] |
| 2025-11-25 | Playwright 1.57 runs on Chrome for Testing builds | Testing | [Official] |
| 2025-12-02 | WordPress 6.9 with the Abilities API | WordPress | [Official] |
| 2025-12-03 | React2Shell CVE-2025-55182 (CVSS 10) disclosed; exploitation from 2025-12-05 | Next.js | [Official] |
| 2025-12-09 | npm classic tokens revoked | Security | [Official] |
| 2025-12-09 | OWASP Top 10 for Agentic Applications published | Security | [Secondary] |
| 2025-12-11 | Base UI 1.0.0 | UI libraries | [Official, repo] |
| 2026-01-23 | Playwright 1.58 (removed `_react` and `_vue` selectors) | Testing | [Official] |
| 2026-03-12 | Base UI 1.3.0: Drawer stable | UI libraries | [Official, repo] |
| 2026-03-17 | `shopify theme preview --overrides` added | Shopify | [Official, repo] |
| 2026-03-18 | Next.js 16.2 | Next.js | [Official] |
| 2026-03 to 2026-04 | Axios npm compromise; CISA alert 2026-04-20 | Security | [Official] |
| 2026-03-31 | WordPress 7.0 delayed | WordPress | [Official] |
| 2026-03 | Chrome DevTools MCP adds Lighthouse (v0.19) | Tooling | [Secondary] |
| 2026-04 | Webflow Data API single page publish | Webflow | [Official] |
| 2026-04-15 | Shopify Scripts editing and publishing locked | Shopify | [Official] |
| 2026-04-20 | Final Soft Navigations origin trial (Chrome 147 to 149) | Performance | [Official] |
| 2026-05-11 | TanStack npm compromise through CI trust | Security | [Study] |
| 2026-05-20 | WordPress 7.0 (PHP 7.4 minimum; real time collaboration pulled) | WordPress | [Official] |
| 2026-05-21 | Shopify CLI 4.0.0 (`theme serve` removed, Node 20 dropped) | Shopify | [Official, repo] |
| 2026-06-02 | Chrome 149: DevTools MCP server and CLI stable | Tooling | [Official] |
| 2026-06-15 | Playwright 1.61 (WebAuthn passkeys, Web Storage API) | Testing | [Official] |
| 2026-06-16 | Shopify CLI 4.2.0 (standard events inspector, DNS rebinding fix) | Shopify | [Official, repo] |
| 2026-06-17 | Shopify Summer '26 Edition | Shopify | [Secondary] |
| 2026-06 | WWDC26: Safari 27 beta | Mobile | [Official] |
| 2026-06-30 | Shopify Scripts stop executing | Shopify | [Official] |
| 2026-07-01 | Shopify CLI store commands unhidden | Shopify | [Official, repo] |
| 2026-07-08 | npm 12 reported to stop running dependency lifecycle scripts by default | Security | [Unverified] |
| 2026-07 (20 or 21) | Next.js July security release: nine CVEs | Next.js | [Official] |
| 2026-07-21 | Shopify Liquid July '26 developer preview (`{% block %}`, `{% partial %}`) | Shopify | [Secondary; Unverified details] |
| 2026-07-24 | Playwright 1.62 (component stories, AbortSignal) | Testing | [Official] |
| 2026-07-31 | Shopify CLI 4.6.0 (`--reconciliation-strategy`) | Shopify | [Official, repo] |
| 2026-08-04 | WooCommerce 11.0 (product block editor APIs removed with shims) | WordPress | [Official] |
| 2026-08-04 | ChainDrop npm worm | Security | [Study] |
| 2026-08-19 | WordPress 7.1 | WordPress | [Official; secondary] |
| 2026-08-22 | Vercel changelog on Instant Rollback from the production deployment tile | Hosting | [Secondary report of official changelog] |
| 2026-08-25 | Next.js August security release (16.3.3, 15.5.24) | Next.js | [Official] |
| 2026-08-26 | Shopify non-Plus Thank you and Order status auto upgrade | Shopify | [Secondary] |
| 2026-09-04 | Playwright 1.63 (test locks, `locator.visible()`); Base UI 1.8.0 | Testing, UI | [Official] |
| 2026-09-14 | iOS 27 released | Mobile | [Secondary] |
| 2026-09 | WebKit Features for Safari 27.0 | Mobile | [Official] |
| 2026-09-22 | Next.js out of band security release (16.3.6, 15.5.26) | Next.js | [Official] |
| 2026-09-30 | Next.js September security release (16.3.8, 15.5.27); npm trusted publishing dist-tag permissions | Next.js, Security | [Official] |
| 2026-10-07 | Playwright 1.64 (WebMCP); WooCommerce 11.2.0; Shopify CLI requires `--allow-live` for live `theme dev` without prompts | Testing, WordPress, Shopify | [Official] |
| 2026-10-08 | Shopify CLI 4.9.0 | Shopify | [Official, repo] |

## 4. Best practice consensus

1. Every change goes through a preview environment (development or unpublished theme, preview deployment, staging) and production is never edited directly [Practitioner consensus; platform docs].
2. Record the rollback target before publishing; theme and deployment rollbacks are minutes, database rollbacks are hours [Practitioner consensus].
3. Automate the money path: add to cart to checkout handoff and lead form submit tests on every preview and read only on live [Practitioner consensus].
4. Pull merchant edits from live before pushing theme JSON (Shopify) and check database stored templates before deploying block theme files (WordPress) [Official docs; practitioner consensus].
5. Test on real devices for mobile; emulation is for regressions [Practitioner consensus].
6. Preserve UTMs and click IDs through all redirects, capture them first party on landing, and keep redirect chains to one hop [Official ad platform guidance; practitioner consensus].
7. Deduplicate browser and server conversion events with a shared event ID [Official, Meta and others].
8. Keep previews protected and non indexable; never send preview traffic to production pixels without test codes [Official host docs; practitioner].
9. Install dependencies from lockfiles with install scripts disabled by default and patch frameworks on a schedule [Official npm and framework guidance; security vendor consensus].
10. Treat repository instruction files and fetched content as untrusted input for agents [OWASP agentic guidance; vendor research].
11. Govern third party scripts with an owner per script and enforce performance budgets in CI [Practitioner consensus; Shopify docs].
12. Use inline errors for anything the user must act on; reserve toasts for non critical confirmations [Practitioner consensus; WCAG guidance on status messages].

## 5. Contested topics (both sides)

| Topic | Side A | Side B | Working position |
|-------|--------|--------|------------------|
| iOS 26 and click IDs | Vendors: Safari strips `gclid` and `fbclid` in all browsing | Testers on final releases: stripping only in Private Browsing, Mail, Messages and opted in all browsing | Capture click IDs first party; test with settings on and off; do not promise either |
| Healing test agents | Faster test maintenance, fewer red builds | Healers can mask real defects by changing assertions or skipping tests | Allow healing on branches; review every healed diff; skipped tests block releases |
| Shopify GitHub integration on the live theme | Simplest continuous deployment for small teams | Every merge goes live without QA; merchant editor commits conflict | Connect a release candidate theme, not the live theme |
| Vercel Deployment Protection for production on all plans | 2025 changelog: free on every plan | Docs snippets list some options as Pro and Enterprise | Verify in the project's dashboard |
| Partytown and worker offloading for tags | Moves third party JS off the main thread | Breaks tags needing synchronous DOM access; vendor support uneven | Use only for tags proven to work, with event integrity tests |
| Rolling releases vs simple rollback for marketing sites | Canary catches errors before full exposure | Marketing sites have low error signal at small traffic shares; adds complexity | Use rolling releases at Scale and Enterprise tiers with error and Speed Insights comparison; instant rollback elsewhere |
| SAQ A script criterion | Provider assurance is enough | Providers lack visibility into the parent page; QSAs may require 6.4.3 style controls | Keep marketing tags off payment pages; inventory scripts anyway |
| npm 12 lifecycle scripts default | Reported to stop running dependency scripts by default (2026-07-08) | Single secondary source | Keep `--ignore-scripts` explicitly until confirmed |

## 6. What top operators do differently

- They make the pipeline boring: one command or click to preview, one to publish, one to roll back, all written down per platform.
- They run launch QA as a gate with a verdict, and re-run destination checks weekly on top spend URLs to catch drift from site changes.
- They own a device lab of two to four real phones and test inside the social apps that send traffic.
- They keep QA products, fixtures and market specific test data so edge states are always testable.
- They schedule framework and plugin patch windows aligned to vendor release cadences (Next.js monthly security releases, WooCommerce releases) instead of reacting.
- They keep a tag register and remove scripts every quarter.
- They separate read and write access for agents and tools, opt out of vendor telemetry on client work, and scan repos for instructions before letting agents work.
- They measure change failure rate and time to restore like an engineering team, even for marketing pages.

## 7. Common expensive mistakes

| Mistake | Cost | Prevention |
|---------|------|------------|
| Pushing a local theme over live JSON templates | Lost merchant content, broken homepage during campaigns | Pull before push; `--nodelete`; release candidate themes |
| Pushing a staging database over a live WooCommerce store | Lost orders and customers | Files only deploys; settings re-applied by script |
| Redirects that drop click IDs | Smart bidding loses conversions for weeks | Parameter survival tests; one hop rule |
| Sale price or discount left live after the sale | Margin loss, legal pricing issues | Sale end play with parity checks |
| Cached PDP showing old prices | Misrepresentation, disapprovals | Cache tags and revalidation tests |
| Missing tracking after the Shopify Thank you page upgrade | Wrong ROAS, broken bidding | Test order and event verification |
| Pixel plus CAPI without dedup | Double conversions, inflated ROAS | Event ID tests |
| Installing apps or plugins straight on production | Slow pages, errors, security holes | L4 lane, staging, tag register |
| Emulation only mobile QA | iPhone specific breakage in paid social traffic | Real device matrix |
| Running installs with scripts enabled during worm windows | Secret theft, CI compromise | `--ignore-scripts`, cooldowns |
| Agent following instructions found in a repo or page | Unauthorized changes, data exfiltration | Untrusted data rule, guard hook, scans |

## 8. Benchmarks (source, date, sample, caveat)

| Benchmark | Value | Source and date | Sample | Caveat |
|-----------|-------|-----------------|--------|--------|
| Third party requests, top 1,000 sites | Median 129 desktop, 106 mobile | Web Almanac 2025 | HTTP Archive crawl | Lower bound because of server side tagging; methodology threshold changed vs 2024 |
| Third party requests, all sites | Median 83 desktop, 79 mobile | Web Almanac 2025 | HTTP Archive crawl | Same |
| Median mobile TBT | 1,916 ms, up 58% vs 2024 | Secondary article citing Web Almanac 2025 | Not stated | [Unverified] |
| WordPress vulnerabilities | 11,334 in 2025, 91% plugins, 46% unpatched at disclosure | Patchstack 2026 report (secondary summaries) | Patchstack database | Vendor data |
| Time to mass exploitation (WordPress) | Weighted median about 5 hours | Patchstack (secondary) | Heavily targeted flaws | [Unverified] |
| chalk and debug compromise exposure window | About 2 hours | Wiz, 2025-09 | 18 packages | Single incident |
| Core Web Vitals thresholds | LCP 2.5 s, INP 200 ms, CLS 0.1 at p75 | web.dev, checked 2026-10 | Not a benchmark; Google thresholds | Thresholds, not targets per vertical |
| Mobile CWV pass shares | LCP about 62%, INP 77%, CLS 81% good | CrUX July 2025 via the cro dossier | Page level, all sites | Varies by vertical and platform |
| Webflow restore points | Automatic every 50th autosave | Webflow Help, 2026 | Product behavior | Not a performance benchmark |
| reCAPTCHA free tier | 10,000 assessments per month | Google Cloud docs, 2026 | Pricing | Check per project or organization scope |

Compare a project against its own history first. Benchmarks vary by vertical, platform, geography and season.

## 9. Tools, APIs and MCP servers

| Tool | Publisher | Use | Status (2026-10) |
|------|-----------|-----|------------------|
| Shopify CLI (`@shopify/cli`) | Shopify | Theme dev, check, push, preview, publish; store GraphQL | 4.9.0 [Official] |
| Shopify AI Toolkit | Shopify | Docs, schema validation, store management for agents | 2.1.x, telemetry default on [Official] |
| Shopify Dev MCP (`@shopify/dev-mcp`) | Shopify | Docs search, `validate_theme` | Open sourced 2026-04 per secondary [Secondary] |
| Storefront MCP | Shopify | Per store endpoint for shopping agents | Live on stores per secondary [Secondary] |
| WP-CLI | WordPress | Site operations | Stable [Official] |
| WordPress Abilities API and MCP adapter; WooCommerce abilities | WordPress, WooCommerce | Expose capabilities to agents | Core since 6.9; improved in 7.1 [Official] |
| Vercel CLI and API | Vercel | Previews, production deploys, rollbacks, rolling releases | Rolling Releases GA [Official] |
| Netlify CLI | Netlify | Deploy previews, production deploys | Stable [Official] |
| Webflow MCP server and Data API | Webflow | Designer and CMS edits, publishing | Official remote and local servers [Official] |
| Playwright, Playwright MCP, Test Agents | Microsoft | E2E, visual, a11y, exploratory QA | 1.64 [Official] |
| Chrome DevTools MCP | Google | Traces, network, console, Lighthouse | Stable since Chrome 149 [Official] |
| Safari MCP server | Apple | Agent access to Safari inspection | Safari 27 per WWDC26 coverage [Secondary] |
| Lighthouse, LHCI, PSI API, CrUX API | Google | Lab and field performance | Lighthouse 13 [Official] |
| axe-core, @axe-core/playwright | Deque | Accessibility checks | Active [Official] |
| gitleaks, trufflehog, osv-scanner, npm audit, Socket | Various | Secrets and dependency scanning | Active [Official] |
| `url_check.py`, `scan_injection.py` | Ads Master | Destination checks, injection scan | Shipped with this skill |

## 10. Official sources to monitor

| Area | Source |
|------|--------|
| Shopify | shopify.dev/changelog; github.com/Shopify/cli releases and theme changelog; Shopify Editions; help.shopify.com checkout pages; github.com/Shopify/shopify-ai-toolkit |
| WordPress | make.wordpress.org/core; wordpress.org/news; WooCommerce `changelog.txt` and developer blog |
| Next.js and React | nextjs.org/blog and nextjs.org/blog/tag/security; react.dev/blog; GitHub security advisories for vercel/next.js |
| Hosting | vercel.com/changelog; netlify.com/changelog; developers.cloudflare.com changelog |
| Webflow | developers.webflow.com changelog; webflow.com/updates; help.webflow.com |
| Testing | playwright.dev release notes; developer.chrome.com blog (Lighthouse, DevTools, CrUX); developers.google.com/speed/docs/insights/release_notes |
| Browsers | webkit.org/blog; Chrome release notes; Apple developer forums (Safari) |
| Security | cisa.gov alerts; github.blog/changelog (npm); genai.owasp.org; PCI SSC document library; Patchstack and Wordfence |
| Accessibility | W3C WCAG; EU EAA national authority sites |

## 11. Open questions and watch list

1. Shopify Liquid July '26 developer preview: final tag names, release date and Theme Check rules (single secondary source today).
2. Whether Shopify adds safer CLI defaults for agents beyond the 2026-10-07 `--allow-live` change (for example confirmation for `--publish` in non-interactive mode).
3. Ads Master guard update to cover the release command gaps found in this research (requires a change to `scripts/guard.py`).
4. Soft Navigations shipping in Chrome and how CrUX reports SPA route changes.
5. Safari 27 MCP server availability and whether it can inspect iOS Safari on devices.
6. npm 12 lifecycle script defaults (confirm on npm's changelog).
7. Next.js held back vulnerabilities (two pending upstream coordination after 2026-09-30).
8. Vercel Rolling Releases plan availability changes and Deployment Protection plan details.
9. Shopify theme library limits and any Rollouts changes affecting theme release workflows.
10. In-app browser behavior changes from Meta and TikTok (no official 2026 announcements found).
11. WordPress real time collaboration (deferred from 7.0 and 7.1) and its database impact when it ships.
12. reCAPTCHA free tier scope (per project or organization) and any further pricing change.

## 12. Sources

1. Shopify CLI repository, theme CHANGELOG and tags 3.86.0 to 4.9.0. Shopify (GitHub). https://github.com/Shopify/cli. 2025-10-16 to 2026-10-08.
2. Shopify CLI command reference (packages/cli/README.md). Shopify (GitHub). https://github.com/Shopify/cli/blob/main/packages/cli/README.md. 2026-10.
3. Require live theme confirmation when prompting is unavailable (commit 22f4455). Shopify (GitHub). https://github.com/Shopify/cli/commit/22f445572fdcc38730ad8cc898b9410f669c12e2. 2026-10-07.
4. Shopify AI Toolkit README and CHANGELOG. Shopify (GitHub). https://github.com/Shopify/shopify-ai-toolkit. 2026-10-07.
5. Shopify AI Toolkit documentation. Shopify. https://shopify.dev/docs/apps/build/ai-toolkit. 2026.
6. Shopify Dev MCP: What It Is and How to Use It (2026). Let's Talk Shop. https://www.letstalkshop.com/blog/shopify-dev-mcp. 2026.
7. Shopify MCP: Complete Guide (2026). MCP.Directory. https://mcp.directory/blog/shopify-mcp-complete-guide-2026. 2026-03.
8. Shopify Scripts will be deprecated on June 30, 2026. Shopify developer changelog. https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026. 2025-04.
9. Script Editor limitations. Shopify Help Center. https://help.shopify.com/en/manual/checkout-settings/script-editor/limitations. 2026.
10. Shopify Thank You Page Tracking: The August 26, 2026 Deadline. WeltPixel. https://weltpixel.com/blogs/news/shopify-thank-you-page-tracking-the-august-26-2026-deadline. 2026.
11. Shopify Thank You and Order Status upgrade August 2026. Consentmo. https://www.consentmo.com/blog-posts/shopify-thank-you-order-status-upgrade-august-2026. 2026.
12. Shopify Summer '26 Edition: what to adopt. li.solutions. https://li.solutions/blog/shopify-summer-2026-edition/. 2026-06.
13. Shopify's July 2026 Preview Every Theme Developer Should See. Medium. https://medium.com/@palakesfera12/shopifys-july-2026-preview-every-theme-developer-should-see-874cd38dc6c0. 2026-07.
14. Theme blocks. Shopify Partners blog. https://www.shopify.com/partners/blog/themeblocks. 2025.
15. Audit and remove third-party scripts. shopify.dev. https://shopify.dev/docs/storefronts/themes/best-practices/performance/audit-remove-third-party-scripts. 2026.
16. Horizon theme repository. Shopify (GitHub). https://github.com/Shopify/horizon. 2026-10.
17. Hydrogen CHANGELOG 2026.4.6 and 2026.4.7. Shopify (GitHub). https://github.com/Shopify/hydrogen. 2026-10-06.
18. WordPress 7.0 Release Party Updated Schedule. make.wordpress.org. https://make.wordpress.org/core/2026/04/22/wordpress-7-0-release-party-updated-schedule/. 2026-04-22.
19. WordPress Delays Release Of Version 7.0 To Focus On Stability. Search Engine Journal. https://www.searchenginejournal.com/wordpress-delays-release-of-version-7-0-to-focus-on-stability/570944/. 2026-04.
20. Abilities API in WordPress 6.9. make.wordpress.org. https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/. 2025-11-10.
21. Abilities API improvements in WordPress 7.1. make.wordpress.org. https://make.wordpress.org/core/2026/07/31/abilities-api-improvements-in-wordpress-7-1/. 2026-07-31.
22. WordPress 7.1: Release, new features and update guide. Raidboxes. https://raidboxes.io/en/blog/wordpress/wordpress-7-1/. 2026-08.
23. WooCommerce changelog.txt and readme.txt. WooCommerce (GitHub). https://github.com/woocommerce/woocommerce. 2026-10-07.
24. Security analysis and insights from 2025. Patchstack. https://patchstack.com. 2026.
25. WordPress hacking statistics. Colorlib. https://colorlib.com/wp/wordpress-hacking-statistics/. 2026.
26. Next.js 16. nextjs.org. https://nextjs.org/blog/next-16. 2025-10.
27. Next.js 16.2. nextjs.org. https://nextjs.org/blog/next-16-2. 2026-03-18.
28. July 2026 Security Release. nextjs.org. https://nextjs.org/blog/july-2026-security-release. 2026-07.
29. Next.js Security Advisories. nextjs.org. https://nextjs.org/blog/tag/security. 2026-09-30.
30. Update: August Next.js Security Release. nextjs.org. https://nextjs.org/blog/nextjs-security-release-august-2026-update. 2026-08.
31. Next.js security release (July 2026): what to know. Netlify changelog. https://www.netlify.com/changelog/2026-07-21-nextjs-security-vulnerabilities/. 2026-07-21.
32. CVE-2026-64642. Ionix. https://www.ionix.io/threat-center/cve-2026-64642/. 2026-07.
33. Critical Security Vulnerability in React Server Components. React. https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components. 2025-12-03.
34. Defending against the CVE-2025-55182 (React2Shell) vulnerability in React Server Components. Microsoft Security Blog. https://www.microsoft.com/en-us/security/blog/2025/12/15/defending-against-the-cve-2025-55182-react2shell-vulnerability-in-react-server-components/. 2025-12-15.
35. Understanding CVE-2025-29927: the Next.js middleware authorization bypass. Datadog Security Labs. https://securitylabs.datadoghq.com/articles/nextjs-middleware-auth-bypass/. 2025-03.
36. Rolling Releases are now generally available. Vercel changelog. https://vercel.com/changelog/rolling-releases-are-now-generally-available. 2025.
37. Rolling releases. Vercel docs. https://vercel.com/docs/rolling-releases. 2026.
38. Revert and pin deployments with Instant Rollback. Vercel changelog. https://vercel.com/changelog/revert-and-pin-deployments-with-instant-rollback. 2023-12-19.
39. Deployment Protection. Vercel docs. https://vercel.com/docs/security/deployment-protection. 2026.
40. Protect production deployments for free on every plan. Vercel changelog. https://vercel.com/changelog/protect-production-deployments-for-free-on-every-plan. 2025.
41. Publish site. Webflow Data API reference. https://developers.webflow.com/data/reference/sites/publish. 2026.
42. Webflow developer changelog, 2026-04-08. Webflow. https://developers.webflow.com/home/changelog/2026/4/8. 2026-04-08.
43. Page branching. Webflow Help Center. https://help.webflow.com/hc/en-us/articles/33961355506195. 2026.
44. Save and restore backups. Webflow Help Center. https://help.webflow.com/hc/en-us/articles/33961244069395. 2026.
45. Webflow MCP server. Webflow developers. https://developers.webflow.com/data/docs/ai-tools. 2026.
46. Playwright release notes (1.56 to 1.64). Microsoft. https://playwright.dev/docs/release-notes. 2025-10-06 to 2026-10-07.
47. Playwright Test Agents. Microsoft. https://playwright.dev/docs/test-agents. 2025-10.
48. Lighthouse 13.0. Chrome for Developers. https://developer.chrome.com/blog/lighthouse-13-0. 2025-10-10.
49. Lighthouse is moving to performance insight audits. Chrome for Developers. https://developer.chrome.com/blog/moving-lighthouse-to-insights. 2025-04.
50. PageSpeed Insights release notes. Google for Developers. https://developers.google.com/speed/docs/insights/release_notes. 2025-10-20.
51. What's new in DevTools (Chrome 149). Chrome for Developers. https://developer.chrome.com/blog/new-in-devtools-149. 2026-06-02.
52. Chrome DevTools MCP server public preview. gihyo.jp. https://gihyo.jp/article/2025/09/chrome-devtools-mcp-server. 2025-09-23.
53. Final Soft Navigations origin trial starting in Chrome 147. Chrome for Developers. https://developer.chrome.com/blog/final-soft-navigations-origin-trial. 2026-04-20.
54. How the Core Web Vitals metrics thresholds were defined. web.dev. https://web.dev/articles/defining-core-web-vitals-thresholds. Checked 2026-10.
55. Web Almanac 2025: Third Parties. HTTP Archive. https://almanac.httparchive.org/en/2025/third-parties. 2025.
56. Lighthouse CI. Google Chrome (GitHub). https://github.com/GoogleChrome/lighthouse-ci. 2026.
57. axe-core. Deque (GitHub). https://github.com/dequelabs/axe-core. 2026.
58. WebKit Features in Safari 26.0. WebKit. https://webkit.org/blog/17333/webkit-features-in-safari-26-0/. 2025-09.
59. WebKit Features for Safari 27.0. WebKit. https://webkit.org/blog/18325/webkit-features-for-safari-27-0/. 2026-09.
60. News from WWDC26: WebKit in Safari 27 beta. WebKit. https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/. 2026-06.
61. iOS26 Safari theme-color/tab-tinting with fixed position elements is a mess. Ben Frain. https://benfrain.com/ios26-safari-theme-color-tab-tinting-with-fixed-position-elements/. 2025.
62. Safari 26 Liquid Glass: toolbar tinting, white bars, viewport bugs. Pavel Larionov. https://1ar.io/updates/safari-26-liquid-glass-web/. 2025.
63. Define the Theme Color for Safari 26. grooovinger. https://grooovinger.com/notes/2026-02-27-safari-26-header-background. 2026-02-27.
64. Safari 26 tracking changes explained. Taggrs. https://taggrs.io/safari-26-tracking-changes/. 2025.
65. iOS 27 Link Tracking Protection: what gets stripped. Improvado. https://improvado.io/blog/ios-26-link-tracking-protection-attribution. 2026.
66. Safari 27 tightens the screws on client-side tracking. Littledata. https://www.littledata.io/blog/2026/07/23/safari-27-tracking-protection. 2026-07-23.
67. iOS Privacy: Instagram and Facebook can track anything you do on any website in their in-app browser. Felix Krause. https://krausefx.com/blog/ios-privacy-instagram-and-facebook-can-track-anything-you-do-on-any-website-in-their-in-app-browser. 2022-08.
68. Emil Kowalski skills (mobile-native, break-ui). Emil Kowalski (GitHub). https://github.com/emilkowalski/skills. 2026.
69. Big Changes for SAQ A: What You Need to Know About 2025 Updates for 11.6.1 and 6.4.3. SecurityMetrics. https://www.securitymetrics.com/blog/big-changes-for-saq-a. 2025.
70. PCI DSS 4.0.1 SAQ A and Client-Side Security: A Plain-English FAQ. Report URI. https://blog.report-uri.com/pci-dss-4-0-1-saq-a-and-client-side-security-a-plain-english-faq/. 2025.
71. SAQ A eligibility. Adyen docs. https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility. 2025.
72. Widespread npm supply chain attack: debug, chalk and beyond. Wiz. https://www.wiz.io/blog/widespread-npm-supply-chain-attack-breaking-down-impact-scope-across-debug-chalk. 2025-09.
73. Critical npm supply chain attack response (September 8, 2025). Vercel. https://vercel.com/blog/critical-npm-supply-chain-attack-response-september-8-2025. 2025-09-08.
74. The Shai-Hulud 2.0 npm worm: analysis, and what you need to know. Datadog Security Labs. https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/. 2025-11.
75. "Shai-Hulud" Worm Compromises npm Ecosystem in Supply Chain Attack. Palo Alto Networks Unit 42. https://unit42.paloaltonetworks.com/npm-supply-chain-attack/. 2025-11-26.
76. npm security update: classic token creation disabled and granular token changes. GitHub changelog. https://github.blog/changelog/2025-11-05-npm-security-update-classic-token-creation-disabled-and-granular-token-changes/. 2025-11-05.
77. Opt-in dist-tag permissions for npm trusted publishing. GitHub changelog. https://github.blog/changelog/2026-09-30-opt-in-dist-tag-permissions-for-npm-trusted-publishing/. 2026-09-30.
78. Supply Chain Compromise Impacts Axios Node Package Manager. CISA. https://www.cisa.gov/news-events/alerts/2026/04/20/supply-chain-compromise-impacts-axios-node-package-manager. 2026-04-20.
79. TanStack and 160+ npm/PyPI Packages Compromised in Supply Chain Worm Attack. Orca Security. https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/. 2026-05.
80. 'ChainDrop' worm compromises hundreds of popular npm packages. Datadog Security Labs. https://securitylabs.datadoghq.com/articles/npm-worm-compromises-popular-npm-packages/. 2026-08.
81. Massive ChainDrop npm supply-chain attack infects hundreds of packages. BleepingComputer. https://www.bleepingcomputer.com/news/security/massive-chaindrop-npm-supply-chain-attack-infects-hundreds-of-packages/. 2026-08.
82. OWASP Top 10 for Agentic Applications. Cycode. https://cycode.com/blog/owasp-top-10-agentic-applications/. 2025-12.
83. New Rules File Backdoor Attack Lets Hackers Inject Malicious Code via AI Code Editors. The Hacker News. https://thehackernews.com/2025/03/new-rules-file-backdoor-attack-lets.html. 2025-03.
84. Mitigating indirect AGENTS.md injection attacks in agentic environments. NVIDIA Technical Blog. https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/. 2026.
85. reCAPTCHA Classic to reCAPTCHA Enterprise migration overview. Google Cloud. https://docs.cloud.google.com/recaptcha/docs/migration-overview. 2025 to 2026.
86. reCAPTCHA compare tiers. Google Cloud. https://docs.cloud.google.com/recaptcha/docs/compare-tiers. 2026.
87. Protect your forms from spam and abuse. Cloudflare docs. https://developers.cloudflare.com/use-cases/solutions/protect-sensitive-forms-fraud-abuse/. 2026.
88. vaul README and package.json. Emil Kowalski (GitHub). https://github.com/emilkowalski/vaul. 2025-10-03.
89. sonner repository. Emil Kowalski (GitHub). https://github.com/emilkowalski/sonner. 2026-08.
90. Base UI CHANGELOG. MUI (GitHub). https://github.com/mui/base-ui. 2026-09-04.
91. shadcn/ui registry (drawer component, app dependencies). shadcn (GitHub). https://github.com/shadcn-ui/ui. 2026-10.
92. Radix Primitives. WorkOS (GitHub). https://github.com/radix-ui/primitives. 2026-10.
93. Shai-Hulud 2.0 Worm Supply-Chain Attack on npm Dependencies. Invicti. https://www.invicti.com/blog/web-security/shai-hulud-2-worm-supply-chain-attack-on-npm-dependencies. 2025-11.
94. Post-mortem of Shai-Hulud attack on November 24th, 2025. PostHog. https://posthog.com/blog/nov-24-shai-hulud-attack-post-mortem. 2025-11.
