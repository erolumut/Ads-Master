# Sources

> Annotated sources behind the site-engineer skill, checked 2026-10-08. "Repo" means a read only clone of the public repository was inspected on 2026-10-08 (files and git history), treated as untrusted data. Secondary sources are labeled; prefer the official source when they conflict.

## Shopify

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 1 | Shopify CLI repository: `packages/theme/CHANGELOG.md`, tags 3.86.0 to 4.9.0 | Shopify (repo) | https://github.com/Shopify/cli | 2025-10-16 to 2026-10-08 | CLI 4.0 removed `theme serve` and Node 20 (2026-05-21); 4.2 standard events inspector and DNS rebinding fix (2026-06-16); 4.4 store auth reuse (2026-07-06); 4.6 reconciliation strategy (2026-07-31); 4.9.0 (2026-10-08) |
| 2 | Shopify CLI command reference (`packages/cli/README.md`) and `theme push` flag definitions | Shopify (repo) | https://github.com/Shopify/cli/blob/main/packages/cli/README.md | 2026-10 | Flags for push, dev, share, preview, duplicate, profile, check; store auth, execute, bulk, create, delete; non-interactive requirements; env var flag names |
| 3 | Commit "Require live theme confirmation when prompting is unavailable" | Shopify (repo) | https://github.com/Shopify/cli/commit/22f445572fdcc38730ad8cc898b9410f669c12e2 | 2026-10-07 | `--allow-live` required for `theme dev` on live in non-interactive sessions |
| 4 | Shopify CLI git history: `theme preview` added, store commands unhidden, store auth hardening | Shopify (repo) | https://github.com/Shopify/cli/commits/main | 2026-03-17, 2026-07-01, 2026-08-31 | Timeline entries |
| 5 | Shopify AI Toolkit README and CHANGELOG | Shopify (repo) | https://github.com/Shopify/shopify-ai-toolkit | 2026-10-07 | Plugin install, skills `shopify` and `ucp` (2.0), remote MCP for Cursor (2.1), telemetry payloads incl. verbatim prompt on Claude Code, opt out file |
| 6 | Shopify AI Toolkit docs | Shopify | https://shopify.dev/docs/apps/build/ai-toolkit | 2026 | Official entry point referenced by the README |
| 7 | Shopify Dev MCP: What It Is and How to Use It (2026) | Let's Talk Shop (secondary) | https://www.letstalkshop.com/blog/shopify-dev-mcp | 2026 | Dev MCP tools incl. `validate_theme`; never touches store data |
| 8 | Shopify MCP complete guide 2026 | MCP.Directory (secondary) | https://mcp.directory/blog/shopify-mcp-complete-guide-2026 | 2026-03 | Storefront MCP endpoint per store |
| 9 | Shopify Scripts will be deprecated on June 30, 2026 | Shopify developer changelog | https://shopify.dev/changelog/shopify-scripts-will-be-deprecated-on-june-30-2026 | 2025-04 | Scripts end date, editing lock 2026-04-15 |
| 10 | Script Editor limitations | Shopify Help Center | https://help.shopify.com/en/manual/checkout-settings/script-editor/limitations | 2026 | Scripts deprecated status |
| 11 | Shopify Thank You Page Tracking: The August 26, 2026 Deadline | WeltPixel (secondary) | https://weltpixel.com/blogs/news/shopify-thank-you-page-tracking-the-august-26-2026-deadline | 2026 | Non-Plus auto upgrade, customizations not migrated |
| 12 | Shopify Thank You and Order Status upgrade August 2026 | Consentmo (secondary) | https://www.consentmo.com/blog-posts/shopify-thank-you-order-status-upgrade-august-2026 | 2026 | Same; Plus deadline 2025-08-28 |
| 13 | Shopify Summer '26 Edition: what to adopt | li.solutions (secondary) | https://li.solutions/blog/shopify-summer-2026-edition/ | 2026-06 | Edition date 2026-06-17, scope |
| 14 | Shopify's July 2026 Preview Every Theme Developer Should See | Medium (secondary) | https://medium.com/@palakesfera12/shopifys-july-2026-preview-every-theme-developer-should-see-874cd38dc6c0 | 2026-07 | Liquid July '26 developer preview: Liquid templates, `{% block %}`, `{% partial %}`, Theme Check 3.28 [Unverified details] |
| 15 | Theme blocks | Shopify Partners blog | https://www.shopify.com/partners/blog/themeblocks | 2025 | Theme blocks, nesting up to 8 levels, `content_for blocks` |
| 16 | Audit and remove third-party scripts | shopify.dev | https://shopify.dev/docs/storefronts/themes/best-practices/performance/audit-remove-third-party-scripts | 2026 | Third party script audit procedure |
| 17 | Horizon theme repository | Shopify (repo) | https://github.com/Shopify/horizon | 2026-10 | Block based structure (95 blocks, 42 sections in the clone) |
| 18 | Hydrogen repository CHANGELOG (2026.4.6, 2026.4.7) | Shopify (repo) | https://github.com/Shopify/hydrogen | 2026-10-06 | Consent initialization and analytics changes; React Router 7.16 |

## WordPress and WooCommerce

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 19 | WordPress 7.0 Release Party Updated Schedule | make.wordpress.org | https://make.wordpress.org/core/2026/04/22/wordpress-7-0-release-party-updated-schedule/ | 2026-04-22 | 7.0 date 2026-05-20 |
| 20 | WordPress Delays Release Of Version 7.0 To Focus On Stability | Search Engine Journal | https://www.searchenginejournal.com/wordpress-delays-release-of-version-7-0-to-focus-on-stability/570944/ | 2026-04 | Delay context |
| 21 | Abilities API in WordPress 6.9 | make.wordpress.org | https://make.wordpress.org/core/2025/11/10/abilities-api-in-wordpress-6-9/ | 2025-11-10 | Abilities API |
| 22 | Abilities API improvements in WordPress 7.1 | make.wordpress.org | https://make.wordpress.org/core/2026/07/31/abilities-api-improvements-in-wordpress-7-1/ | 2026-07-31 | Validation hooks, lifecycle action |
| 23 | WordPress 7.1 release coverage | Raidboxes (secondary) | https://raidboxes.io/en/blog/wordpress/wordpress-7-1/ | 2026-08 | 7.1 date 2026-08-19, deferred collaboration |
| 24 | WooCommerce `changelog.txt` and `readme.txt` | WooCommerce (repo) | https://github.com/woocommerce/woocommerce | 2026-10-07 | Release dates 9.6 to 11.2; 11.0 removals; 11.2 requirements (WP 7.0, PHP 7.4); MCP and abilities entries |
| 25 | Security analysis and insights from 2025 (State of WordPress Security) | Patchstack | https://patchstack.com | 2026 | 11,334 vulnerabilities in 2025, 91% plugins, 46% unpatched at disclosure |
| 26 | WordPress hacking statistics | Colorlib (secondary) | https://colorlib.com/wp/wordpress-hacking-statistics/ | 2026 | Patchstack time to exploitation figures [Unverified] |

## Next.js, hosting, Webflow

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 27 | Next.js 16 | Vercel (nextjs.org) | https://nextjs.org/blog/next-16 | 2025-10 | `proxy.ts`, Cache Components, `"use cache"` |
| 28 | Next.js 16.2 | Vercel (nextjs.org) | https://nextjs.org/blog/next-16-2 | 2026-03-18 | 16.2 features, Adapter API |
| 29 | July 2026 Security Release | Vercel (nextjs.org) | https://nextjs.org/blog/july-2026-security-release | 2026-07 | Nine CVEs fixed in 16.2.11 and 15.5.21 |
| 30 | Next.js Security Advisories tag | Vercel (nextjs.org) | https://nextjs.org/blog/tag/security | 2026-09-30 | August, September and out of band releases; 16.3.8 and 15.5.27 |
| 31 | Next.js security release (July 2026): what to know | Netlify changelog | https://www.netlify.com/changelog/2026-07-21-nextjs-security-vulnerabilities/ | 2026-07-21 | Host perspective on the July release |
| 32 | CVE-2026-64642 | Ionix threat center (secondary) | https://www.ionix.io/threat-center/cve-2026-64642/ | 2026-07 | Affected range 16.0.0 to 16.2.10 |
| 33 | Critical Security Vulnerability in React Server Components | React (react.dev) | https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components | 2025-12-03 | CVE-2025-55182 versions and fixes |
| 34 | Defending against the CVE-2025-55182 (React2Shell) vulnerability | Microsoft Security | https://www.microsoft.com/en-us/security/blog/2025/12/15/defending-against-the-cve-2025-55182-react2shell-vulnerability-in-react-server-components/ | 2025-12-15 | Exploitation from 2025-12-05; CVE merge |
| 35 | Understanding CVE-2025-29927: the Next.js middleware authorization bypass | Datadog Security Labs | https://securitylabs.datadoghq.com/articles/nextjs-middleware-auth-bypass/ | 2025-03 | Header based bypass, fixed versions |
| 36 | Rolling Releases are now generally available | Vercel changelog | https://vercel.com/changelog/rolling-releases-are-now-generally-available | 2025 | Rolling Releases mechanics and plans [GA date unverified] |
| 37 | Rolling releases docs | Vercel | https://vercel.com/docs/rolling-releases | 2026 | Skew protection recommendation, Instant Rollback during rollouts |
| 38 | Revert and pin deployments with Instant Rollback | Vercel changelog | https://vercel.com/changelog/revert-and-pin-deployments-with-instant-rollback | 2023-12-19 | Rollback stops auto assignment of domains |
| 39 | Deployment Protection | Vercel docs | https://vercel.com/docs/security/deployment-protection | 2026 | Protection methods; plan details [Contested with changelog] |
| 40 | Protect production deployments for free on every plan | Vercel changelog | https://vercel.com/changelog/protect-production-deployments-for-free-on-every-plan | 2025 | Free Vercel Authentication for production |
| 41 | Publish site (Data API) | Webflow developers | https://developers.webflow.com/data/reference/sites/publish | 2026 | Publish endpoint, rate limit, scope |
| 42 | Webflow developer changelog 2026-04-08 | Webflow developers | https://developers.webflow.com/home/changelog/2026/4/8 | 2026-04-08 | Single page publishing via API |
| 43 | Page branching | Webflow Help | https://help.webflow.com/hc/en-us/articles/33961355506195 | 2026 | Enterprise only, merge behavior |
| 44 | Save and restore backups | Webflow Help | https://help.webflow.com/hc/en-us/articles/33961244069395 | 2026 | Backup and restore rules |
| 45 | Webflow MCP server | Webflow developers | https://developers.webflow.com/data/docs/ai-tools | 2026 | Remote and local MCP, permissions |

## Testing and performance tooling

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 46 | Playwright release notes 1.56 to 1.64 (`docs/src/release-notes-js.md`) and tag dates | Microsoft (repo) | https://playwright.dev/docs/release-notes | 2025-10-06 to 2026-10-07 | Test Agents (1.56), Chrome for Testing (1.57), breaking removals (1.58), screencast (1.59), aria snapshot boxes (1.60), passkeys (1.61), component stories (1.62), test locks and `locator.visible()` (1.63), WebMCP (1.64) |
| 47 | Playwright Test Agents docs | Microsoft (repo) | https://playwright.dev/docs/test-agents | 2025-10 | `init-agents --loop=claude`, planner, generator, healer |
| 48 | Lighthouse 13.0 | Chrome for Developers | https://developer.chrome.com/blog/lighthouse-13-0 | 2025-10-10 | Insight audits replace legacy audits; scoring unchanged |
| 49 | Lighthouse is moving to performance insight audits | Chrome for Developers | https://developer.chrome.com/blog/moving-lighthouse-to-insights | 2025-04 | Migration plan, breaking changes for API users |
| 50 | PageSpeed Insights release notes | Google for Developers | https://developers.google.com/speed/docs/insights/release_notes | 2025-10-20 | PSI on Lighthouse 13 |
| 51 | What's new in DevTools (Chrome 149) | Chrome for Developers | https://developer.chrome.com/blog/new-in-devtools-149 | 2026-06-02 | Chrome DevTools MCP and CLI stable |
| 52 | Chrome DevTools MCP public preview coverage | gihyo.jp (secondary) | https://gihyo.jp/article/2025/09/chrome-devtools-mcp-server | 2025-09-23 | Preview launch date |
| 53 | Final Soft Navigations origin trial starting in Chrome 147 | Chrome for Developers | https://developer.chrome.com/blog/final-soft-navigations-origin-trial | 2026-04-20 | Soft navigations timeline |
| 54 | How the Core Web Vitals metrics thresholds were defined | web.dev | https://web.dev/articles/defining-core-web-vitals-thresholds | checked 2026-10 | Thresholds |
| 55 | Web Almanac 2025: Third Parties | HTTP Archive | https://almanac.httparchive.org/en/2025/third-parties | 2025 to 2026 | Third party request medians, methodology |
| 56 | Lighthouse CI | Google Chrome (repo) | https://github.com/GoogleChrome/lighthouse-ci | 2026 | Assertions, resource summary budgets |
| 57 | axe-core and @axe-core/playwright | Deque | https://github.com/dequelabs/axe-core | 2026 | Automated accessibility rules and tags |

## Mobile web and browsers

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 58 | WebKit Features in Safari 26.0 | WebKit | https://webkit.org/blog/17333/webkit-features-in-safari-26-0/ | 2025-09 | Safari 26 features, fingerprinting protection |
| 59 | WebKit Features for Safari 27.0 | WebKit | https://webkit.org/blog/18325/webkit-features-for-safari-27-0/ | 2026-09 | Scroll anchoring, customizable select, viewport unit fixes |
| 60 | News from WWDC26: WebKit in Safari 27 beta | WebKit | https://webkit.org/blog/17967/news-from-wwdc26-webkit-in-safari-27-beta/ | 2026-06 | Safari 27 beta features |
| 61 | iOS 26 Safari theme-color and tab tinting with fixed position elements | Ben Frain | https://benfrain.com/ios26-safari-theme-color-tab-tinting-with-fixed-position-elements/ | 2025 | Tinting derived from page, fixed element behavior [Practitioner] |
| 62 | Safari 26 Liquid Glass: toolbar tinting, white bars, viewport bugs | 1ar.io | https://1ar.io/updates/safari-26-liquid-glass-web/ | 2025 to 2026 | `theme-color` ignored for chrome tinting, workarounds [Practitioner] |
| 63 | Define the Theme Color for Safari 26 | grooovinger | https://grooovinger.com/notes/2026-02-27-safari-26-header-background | 2026-02-27 | Body background approach [Practitioner] |
| 64 | Safari 26 tracking changes explained | Taggrs (secondary) | https://taggrs.io/safari-26-tracking-changes/ | 2025 | Link Tracking Protection scope, AFP vs ATFP |
| 65 | iOS 27 Link Tracking Protection: what gets stripped | Improvado (secondary) | https://improvado.io/blog/ios-26-link-tracking-protection-attribution | 2026 | Contradicts "all browsing" stripping claims |
| 66 | Safari 27 tracking protection | Littledata (secondary) | https://www.littledata.io/blog/2026/07/23/safari-27-tracking-protection | 2026-07-23 | Safari 27 tracking context |
| 67 | iOS Privacy: Instagram and Facebook can track anything you do on any website in their in-app browser | Felix Krause | https://krausefx.com/blog/ios-privacy-instagram-and-facebook-can-track-anything-you-do-on-any-website-in-their-in-app-browser | 2022-08 | In-app browser script injection research |
| 68 | mobile-native and break-ui skills | Emil Kowalski (repo, ideas only) | https://github.com/emilkowalski/skills | 2026 | Inspiration for mobile polish and worst case data methods (no text copied) |

## Security

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 69 | Big Changes for SAQ A: 2025 updates for 11.6.1 and 6.4.3 | SecurityMetrics (secondary) | https://www.securitymetrics.com/blog/big-changes-for-saq-a | 2025 | SAQ A eligibility change |
| 70 | PCI DSS 4.0.1 SAQ A and client-side security FAQ | Report URI (secondary) | https://blog.report-uri.com/pci-dss-4-0-1-saq-a-and-client-side-security-a-plain-english-faq/ | 2025 | FAQ 1588 interpretation |
| 71 | SAQ A eligibility | Adyen docs | https://docs.adyen.com/development-resources/pci-dss-compliance-guide/saq-a-eligibility | 2025 to 2026 | Provider view |
| 72 | Widespread npm supply chain attack: debug, chalk and beyond | Wiz | https://www.wiz.io/blog/widespread-npm-supply-chain-attack-breaking-down-impact-scope-across-debug-chalk | 2025-09 | 18 packages, exposure window |
| 73 | Critical npm supply chain attack response | Vercel | https://vercel.com/blog/critical-npm-supply-chain-attack-response-september-8-2025 | 2025-09-08 | Host response |
| 74 | The Shai-Hulud 2.0 npm worm: analysis | Datadog Security Labs | https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/ | 2025-11 | Preinstall execution, scale |
| 75 | Shai-Hulud worm compromises npm ecosystem | Palo Alto Networks Unit 42 | https://unit42.paloaltonetworks.com/npm-supply-chain-attack/ | 2025-09 to 2025-11 | Worm mechanics |
| 76 | npm security update: classic token creation disabled and granular token changes | GitHub changelog | https://github.blog/changelog/2025-11-05-npm-security-update-classic-token-creation-disabled-and-granular-token-changes/ | 2025-11-05 | Token changes |
| 77 | Opt-in dist-tag permissions for npm trusted publishing | GitHub changelog | https://github.blog/changelog/2026-09-30-opt-in-dist-tag-permissions-for-npm-trusted-publishing/ | 2026-09-30 | Trusted publishing change |
| 78 | Supply chain compromise impacts Axios Node Package Manager | CISA | https://www.cisa.gov/news-events/alerts/2026/04/20/supply-chain-compromise-impacts-axios-node-package-manager | 2026-04-20 | Axios compromise |
| 79 | TanStack and 160+ npm and PyPI packages compromised | Orca Security | https://orca.security/resources/blog/tanstack-npm-supply-chain-worm/ | 2026-05 | Pipeline trust compromise |
| 80 | ChainDrop worm compromises popular npm packages | Datadog Security Labs | https://securitylabs.datadoghq.com/articles/npm-worm-compromises-popular-npm-packages/ | 2026-08 | Valid provenance on malicious releases |
| 81 | OWASP Top 10 for Agentic Applications (summary) | Cycode (secondary; official at genai.owasp.org) | https://cycode.com/blog/owasp-top-10-agentic-applications/ | 2025-12 | ASI01 to ASI10 |
| 82 | New Rules File Backdoor attack | The Hacker News | https://thehackernews.com/2025/03/new-rules-file-backdoor-attack-lets.html | 2025-03 | Hidden Unicode in rules files |
| 83 | Mitigating indirect AGENTS.md injection attacks in agentic environments | NVIDIA Technical Blog | https://developer.nvidia.com/blog/mitigating-indirect-agents-md-injection-attacks-in-agentic-environments/ | 2026 | Build time generated instruction files |
| 84 | reCAPTCHA Classic to Enterprise migration overview | Google Cloud docs | https://docs.cloud.google.com/recaptcha/docs/migration-overview | 2025 to 2026 | Key migration |
| 85 | reCAPTCHA compare tiers | Google Cloud docs | https://docs.cloud.google.com/recaptcha/docs/compare-tiers | 2026 | 10,000 free assessments, Premium pricing |
| 86 | Protect your forms from spam and abuse | Cloudflare docs | https://developers.cloudflare.com/use-cases/solutions/protect-sensitive-forms-fraud-abuse/ | 2026 | Turnstile steps, rate limiting example |

## UI libraries

| # | Title | Publisher | URL | Date | Supports |
|---|-------|-----------|-----|------|----------|
| 87 | vaul README (unmaintained notice) and package.json | Emil Kowalski (repo) | https://github.com/emilkowalski/vaul | 2025-10-03 | Unmaintained status, v1.1.2, Radix dialog dependency, `repositionInputs` |
| 88 | sonner repository | Emil Kowalski (repo) | https://github.com/emilkowalski/sonner | 2026-08 | v2.0.8, live region and hotkey implementation |
| 89 | Base UI CHANGELOG | MUI (repo) | https://github.com/mui/base-ui | 2026-09-04 | 1.0.0 on 2025-12-11, Drawer stable in 1.3.0 on 2026-03-12, 1.8.0 |
| 90 | shadcn/ui registry drawer and app dependencies | shadcn (repo) | https://github.com/shadcn-ui/ui | 2026-10 | Drawer imports vaul 1.1.2 |
| 91 | Radix Primitives | WorkOS (repo) | https://github.com/radix-ui/primitives | 2026-10 | Active repository |

## Gaps and conflicts to recheck

- Liquid July '26 developer preview details (tags and Theme Check rule names) come from one secondary source.
- Vercel Rolling Releases GA date and Deployment Protection plan details (docs vs changelog).
- npm 12 default of not running dependency lifecycle scripts (single secondary source).
- Safari 27 built in MCP server availability and setup (secondary coverage of WWDC26).
- Patchstack time to exploitation percentages (secondary).
- Shopify theme library limit per store (stated as 20 from long standing documentation; recheck).
