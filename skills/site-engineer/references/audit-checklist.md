# Site Engineering Audit Checklist (scored)

> Use for a full engineering and release readiness audit of a site or storefront, or a slice of it (only the sections that apply). Each item: check, why, how to verify, severity, fix. Score with the rubric at the end. Mark N/A when an item does not apply and say why. Knowledge as of 2026-10.

Severity weights: Critical 10, High 5, Medium 2, Low 1.

## A. Release process and rollback

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| A1 | Production is never edited directly; changes go through branch, preview, QA, approval | Direct edits cause untracked breakage and no rollback | Ask; review theme editor activity, git history vs live theme, WordPress plugin install dates | Critical | Adopt the pipeline in [Release process](release-process-and-rollback.md) |
| A2 | A rollback target is recorded before every release (theme ID, deployment ID, backup) | Rollback without a target takes hours | Last 5 release notes | Critical | Release notes template; snapshot step |
| A3 | Release notes exist for recent releases with approver and time | Incident analysis and accountability | `ads-master/logs/releases/` or team equivalent | High | Start release notes |
| A4 | Freeze windows defined for sales, launches and BFCM | Most expensive breakage happens during peaks | `DECISIONS.md`, team calendar | High | Define windows; record exceptions |
| A5 | Rollback triggers defined and known | Teams debate instead of restoring | Interview; incident history | High | Section 7 triggers |
| A6 | Post release checks run at T+15 min, T+2 h, T+24 h | Silent tracking and checkout breaks | Last releases | High | Post release checklist |
| A7 | Backups are restorable (tested in the last quarter) | Untested backups fail | Restore test record | High | Quarterly restore drill on staging |
| A8 | Release cadence fits the team setup | Too frequent without automation, or big bang releases | Release log | Medium | Section 12 cadence table |
| A9 | Guard coverage gaps for release commands mitigated (blocked or ask patterns in `guardrails.json`) | Some publish commands are not caught by the hook today | Read `guardrails.json` | High | Human adds the patterns in section 10 of the release reference |

## B. Environments and previews

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| B1 | A staging, development theme or preview deployment exists for every change | Needed for QA without customer impact | List themes or deployments | Critical | Set up per platform reference |
| B2 | Previews and staging are protected and not indexable | Duplicate content, leaked offers, data exposure | `curl -sI` without auth; `site:` search | High | Protection plus `noindex` |
| B3 | Preview environments do not send events to production pixels or datasets (or use test event codes) | QA traffic pollutes ad optimization | Network capture on preview | High | Environment scoped pixel config |
| B4 | Staging uses test payment, mail sink and no CRM writes | Real charges and emails to customers | Config review | Critical | Test modes, mail catcher |
| B5 | Environment variables scoped per environment; no secrets in `NEXT_PUBLIC_*` | Secret exposure | Host settings, bundle search | Critical | Re-scope and rotate |
| B6 | Merchant edits on live (Shopify JSON templates, block theme database templates) are pulled before pushes | Overwriting merchant content | Git history shows pre release pulls | High | Pull step in the loop |

## C. Automated QA

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| C1 | Smoke tests for the money path (add to cart to checkout handoff, or lead form submit in test mode) on desktop and mobile | Catches the breaks that cost revenue | Run the suite | Critical | [Automated QA](automated-qa-and-tests.md) templates 6 and 7 |
| C2 | Static checks in CI (Theme Check, lint, type check) | Cheap error catching | CI config | High | Add to CI |
| C3 | Tracking assertions for primary events (once, with value, dedup ID) | Double or missing conversions break bidding | Template 8 run | Critical | Add tracking tests with `measurement` |
| C4 | Parameter survival tests through redirects | Lost click IDs | Template 9 run | High | Add |
| C5 | Visual regression on key templates | Unexplained layout changes | Snapshot setup | Medium | Add with masks |
| C6 | Accessibility checks on key templates (no serious or critical axe violations) | Legal exposure (EAA since 2025-06-28 in the EU) and lost users | Template 11 | High | Fix; baseline known issues |
| C7 | Lighthouse CI budgets enforced | Performance regressions slip in | `lighthouserc.json` | Medium | Add budgets |
| C8 | Structured data and price parity test on PDP | Misrepresentation risk, rich result loss | Template 12 | High | Add |
| C9 | Tests run against the exact preview that gets promoted | Rebuilding after QA ships untested code | CI and deploy flow | Medium | Promote tested deployments |
| C10 | Flaky tests quarantined with owner and date | Ignored flakes hide real failures | CI history | Low | Flake policy |

## D. Launch QA for ads

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| D1 | Every active ad's final URL returns 200 over HTTPS with at most one redirect | Wasted spend, disapprovals | `url_check.py` on an export of final URLs | Critical | Fix URLs or redirects |
| D2 | UTMs and click IDs survive to the final URL | Attribution and bidding signal | `url_check.py --add-click-ids` | Critical | Fix redirect rules |
| D3 | UTM convention followed (lowercase, no spaces, no PII) | Channel reporting accuracy | Export review | Medium | Governance doc with `measurement` |
| D4 | Offer, price and stock on landing pages match live ads | Misrepresentation, wasted spend | Top 20 ads by spend vs pages | Critical | Parity process |
| D5 | Launch QA ran before the last 3 launches | Process adoption | Outputs folder | High | Make launch QA a required gate |
| D6 | In-app browser tests done for social channels | Most social clicks land in-app | QA reports | High | Protocol in [Launch QA](launch-qa-for-ads.md) section 7 |
| D7 | Consent banner does not block the CTA on small phones | Bounce on paid traffic | Screenshot at 375 x 667 | High | Banner layout change |
| D8 | New entities were created PAUSED and budgets within caps | Spend control | Change requests and read backs | Critical | Enforce in channel agents |

## E. Mobile web

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| E1 | Zoom not disabled; inputs 16 px or more on touch | Accessibility and iOS zoom | View source, CSS | High | [Mobile web polish](mobile-web-polish.md) M1 |
| E2 | Bottom fixed UI clears safe areas and the Safari 26+ toolbar | Hidden CTAs on iPhone | Real iPhone | High | M6, M7 |
| E3 | Keyboard does not hide focused fields or submit buttons in forms and sheets | Abandoned forms | Real devices | High | M9 |
| E4 | No sticky hover; visible press feedback | Perceived quality | Real devices | Medium | M2 |
| E5 | No horizontal scroll at 320 px | Broken layout | Playwright at 320 px | High | Fix overflow |
| E6 | Correct input types and autocomplete on all forms | Form completion speed | Code review | Medium | M13 |
| E7 | Real device testing is part of release QA | Emulation misses mobile bugs | QA reports | High | Device matrix |

## F. Worst case data

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| F1 | Product cards, PDP and cart handle long names in every market language | Broken layouts in DE, NL, TR markets | QA products with catalog values | High | [Worst case data](worst-case-data-testing.md) |
| F2 | Prices formatted per market with locale aware formatting | Wrong price display | View each market | Critical | Money filters, `Intl.NumberFormat` |
| F3 | Zero and one review, sold out, many variants states render correctly | Common real states | QA products | High | Fix components |
| F4 | Forms accept long emails, plus addressing, international names and phone formats | Lost leads | Form tests | High | Validation fixes |
| F5 | Turkish casing and `lang` attributes correct per market | Wrong letters in headings | View TR pages with uppercase text | Medium | `lang`, locale aware casing |
| F6 | Worst case fixtures kept as regression tests | Breaks return | Fixture files or QA products exist | Low | Keep fixtures |

## G. Performance and third party scripts

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| G1 | Field Core Web Vitals good on top paid landing pages (p75 mobile) | Conversion and ad landing page experience | CrUX API, PSI | High | `cro` speed reference plus budgets |
| G2 | Tag register exists with owner and consent category for every script | Tag bloat and privacy risk | Register file | High | Build register |
| G3 | No duplicate pixels or analytics libraries | Double events, wasted main thread | Network capture | High | Remove duplicates with `measurement` |
| G4 | No leftover code from uninstalled apps or old testing tools | Errors and weight | Search theme and layout for vendor domains | Medium | Remove |
| G5 | LCP image not lazy loaded, discoverable, prioritized | LCP | Lighthouse insights | High | Image rules |
| G6 | Fonts limited, subset for market scripts, glyphs for ₺ and € present | CLS and tofu glyphs | Font files | Medium | Font rules |
| G7 | Performance budgets defined and enforced | Regressions | `lighthouserc.json` | Medium | Add |

## H. Security

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| H1 | No secrets in repo, theme or client bundles | Account takeover | gitleaks or trufflehog | Critical | Remove and rotate |
| H2 | Frameworks and plugins on patched versions (Next.js 16.3.8 or 15.5.27 or later as of 2026-09-30; React patched for CVE-2025-55182; WordPress and plugins current) | Known exploited vulnerabilities | `npm ls`, `wp plugin list` | Critical | Security patch play |
| H3 | Dependency installs use lockfiles and ignore install scripts by default | Supply chain worms | CI config | High | `npm ci --ignore-scripts` |
| H4 | Forms protected (challenge validated server side, rate limits, honeypot) and the challenge service within plan limits | Spam leads pollute ads and CRM | Code and Google Cloud reCAPTCHA usage | High | Turnstile or reCAPTCHA setup |
| H5 | No PII in URLs, analytics or pixels | Privacy law and platform policy | Template 7, network capture | Critical | Fix forms and redirects |
| H6 | Admin, login, preview and debug endpoints protected | Compromise | `curl` checks | High | Protect or remove |
| H7 | Payment page script inventory where an embedded payment form exists (PCI DSS 4.0.1) | Card skimming | Script list on payment pages | High (Critical if SAQ A-EP or D) | Inventory, integrity, monitoring |
| H8 | Agent instruction files and hidden Unicode reviewed | Prompt injection | `scan_injection.py` | High | Human review; remove |
| H9 | MCP servers and AI plugins use least privilege and telemetry is reviewed | Data leaving the project | Installed servers list | Medium | Narrow scopes, opt out |

## I. Platform specifics

| # | Check | Why | How to verify | Severity | Fix |
|---|-------|-----|---------------|----------|-----|
| I1 | Shopify: no logic still depending on Shopify Scripts (stopped 2026-06-30) | Discounts, shipping or payment rules silently gone | Scripts customizations report, checkout tests | Critical | Functions or apps (with `offer-strategy`) |
| I2 | Shopify: Thank you and Order status pages upgraded and tracking verified with a test order after 2025-08-28 (Plus) or 2026-08-26 (other plans) | Lost purchase tracking | Test order, pixel events | Critical | Web pixels, apps (with `measurement`) |
| I3 | Shopify: CLI 4.x in CI with Node 22 or later; no `theme serve` | CI breaks | CI config | Medium | Update |
| I4 | Shopify: AI Toolkit telemetry opt out set on client machines if installed | Prompts leave the machine | Opt out file exists | Medium | Create the file |
| I5 | WordPress: WooCommerce 11.x compatible extensions; HPOS status known | Fatals after upgrade | Staging upgrade test | High | Replace or patch extensions |
| I6 | WordPress: no database pushes from staging to a live store | Lost orders | Host settings, process | Critical | Files only deploys |
| I7 | Next.js: caching of price and stock data revalidates on updates | Wrong prices | Change a price on staging and watch | Critical | Tags and revalidation |
| I8 | Next.js: authorization not only in proxy or middleware | Bypass CVEs | Code review | High | Enforce in routes |
| I9 | Webflow: backup before publish; custom code inventoried | No rollback; risky embeds | Backups list; site settings | High | Process |
| I10 | Headless: checkout handoff carries cart attributes (UTMs, click IDs, consent) | Attribution | Test | High | Fix handoff |

## Scoring rubric

1. For each applicable item, award its weight if it passes, 0 if it fails. Partial passes get 0 (write what is missing).
2. Score = awarded weight / applicable weight x 100, overall and per section.
3. Grade:

| Score | Grade | Meaning |
|-------|-------|---------|
| 90 to 100 | A | Release ready; keep cadence |
| 75 to 89 | B | Solid; fix Highs within 30 days |
| 60 to 74 | C | Risky; fix Criticals now, Highs within 2 weeks; no L4 work until fixed |
| Below 60 | D | Unsafe for paid scaling; fix plan before more spend goes to the site |

4. Cap rule: any failed Critical caps the grade at C regardless of score. Any failed Critical in sections D or H, or items I1, I2, I6, I7, is also a stop condition candidate: check `ads-master/INCIDENTS.md` and raise it at the top of the report.
5. Report: score summary per section, failed Criticals and Highs with evidence, fix plan (owner, effort, date), handoffs requested. Save to `ads-master/outputs/site-engineer/YYYY-MM-DD_site-engineer_audit-<scope>.md`.
6. Re-audit: quarterly, after a platform migration, or after an incident.
