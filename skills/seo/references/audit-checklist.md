# SEO Audit Checklist (Scored)

> Use for full audits (quarterly) and scoped audits (pick sections). Mark each item Pass, Fail, Partial or N/A. Record evidence (URL, screenshot path, export file, date). Severity drives the score. Sections K to Q apply only when relevant to the business model. Detailed fixes live in the linked references.

Severity: Critical (blocks indexing or causes sitewide loss or policy risk), High (material loss on money pages), Medium (meaningful but contained), Low (hygiene).

## A. Access and measurement
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| A1 | Search Console Domain property verified; owners documented | Data and alerts | Search Console settings | Critical | Verify via DNS |
| A2 | Bing Webmaster Tools verified | Bing and Copilot data, IndexNow | BWT dashboard | Medium | Import from Search Console |
| A3 | GA4 Organic Search sessions and key events reconcile with backend within tolerance | Trustworthy outcomes | Compare 30 days | High | Hand to measurement |
| A4 | Bulk data export to BigQuery enabled (Growth tier and above) | Full query history | Search Console settings | Low | Enable |
| A5 | Annotations for updates, releases, num=100 boundary | Interpretation | Search Console annotations, dashboard | Low | Add |
| A6 | Rank tracking set for priority query set at useful depth | Visibility KPI | Tool config | Medium | Configure top 20 to 50 |

## B. Crawlability
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| B1 | robots.txt returns 200, no accidental `Disallow: /` or blocks on money sections | Crawl access | Fetch file; Search Console robots.txt report | Critical | Correct rules |
| B2 | CSS, JS and rendering APIs not blocked | Rendering | URL Inspection page resources | High | Allow |
| B3 | Infinite spaces controlled (internal search, sort, session IDs, calendars) | Crawl waste | Crawl and logs parameter share | Medium | Disallow patterns |
| B4 | No WAF or bot management blocking verified Googlebot or Bingbot | Crawl access | Crawl Stats 403 and 429, logs, CDN bot reports | Critical | Allowlist verified bots |
| B5 | Average response time stable; 5xx under 1% | Crawl capacity | Crawl Stats | High | Server and caching fixes |
| B6 | Important pages linked with crawlable `<a href>` | Discovery | Crawl with JS off and on | High | Real links |
| B7 | XML sitemaps exist, declared in robots.txt, submitted, split by type | Discovery and monitoring | Sitemaps report | Medium | Generate from source of truth |
| B8 | Sitemaps contain only 200, indexable, canonical URLs; accurate lastmod | Signal quality | Sampler script, crawler | Medium | Filter at generation |
| B9 | Orphan valuable pages count | Discovery and equity | Crawl vs sitemap, GSC, logs | Medium | Link or retire |

## C. Indexability
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| C1 | No noindex (meta or header) on money templates | Indexing | Crawl directives; curl | Critical | Remove; environment specific settings |
| C2 | Indexing ratio per priority sitemap over 90% | Coverage | Page indexing filtered by sitemap | High | Triage reasons |
| C3 | "Crawled, currently not indexed" and "Discovered, currently not indexed" trend not rising on valuable templates | Quality or capacity | Page indexing report | High | Quality, consolidation, crawl waste |
| C4 | Soft 404s fixed | Crawl and quality | Page indexing | Medium | Real 404 or content |
| C5 | Correct status codes (404 for missing, 301 or 308 for moved) | Index hygiene | Crawl, curl random URL | High | Server and framework config |
| C6 | Staging and dev environments not indexed | Duplicate content, leaks | `site:` search, header check | High | Auth plus noindex header |
| C7 | Thin or low value sections noindexed or improved | Site quality | Content audit | Medium | Prune or improve |

## D. Rendering
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| D1 | Primary content, title, canonical, robots, hreflang, JSON-LD in raw HTML | Reliable indexing across engines | curl vs rendered diff | High | SSR, SSG or ISR |
| D2 | No JS-only navigation or `#` routes for indexable views | Discovery | Crawl, code review | High | History API URLs and links |
| D3 | Client side 404 views return HTTP 404 | Soft 404s | curl unknown route | Medium | Server status handling |
| D4 | Lazy loaded content visible without interaction | Content discovery | Rendered HTML | Medium | Native lazy loading, render in HTML |
| D5 | HTML size and inline hydration payload reasonable (well under 2 MB; Googlebot stops at 2 MB of uncompressed HTML per Google docs, 2026-02) | Processing limits, speed | Page weight | Low | Trim payloads |

## E. Canonicals and duplicates
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| E1 | Self referencing absolute canonicals on indexable pages | Consolidation | Crawl canonicals | High | Template fix |
| E2 | No inherited or global canonical to homepage (framework bug) | Deindexing | Crawl: canonical = homepage on non home pages | Critical | Remove global canonical |
| E3 | One canonical tag per page | Conflicts | Crawl "multiple canonicals" | Medium | Remove duplicates |
| E4 | Host, protocol, trailing slash, case normalized with single hop 301s | Duplicates | curl variants | Medium | Redirect rules |
| E5 | Google selected canonical matches declared for priority pages | Signal alignment | URL Inspection API sample | High | Align signals |
| E6 | Parameter and facet duplicates controlled | Index bloat | Crawl, Page indexing duplicates | High | Facet rules |

## F. Architecture and internal links
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| F1 | Money pages within 3 clicks | Priority signal | Crawl depth | High | Navigation and hub links |
| F2 | Pages ranking 4 to 20 for valuable queries have inlinks at or above template median | Quick wins | Crawl plus GSC join | Medium | Link plan |
| F3 | Breadcrumbs on all levels with markup | Hierarchy | Crawl, Rich Results Test | Low | Template |
| F4 | No internal links to redirects or 404s | Waste | Crawl | Low | Update links |
| F5 | No cannibalization on priority queries | Signal split | GSC query with multiple URLs | Medium | Consolidate |
| F6 | URL structure clean, stable, no tracking parameters in internal links | Duplicates | Crawl | Low | Fix templates |

## G. On-page
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| G1 | Unique, intent matched titles on money pages | Relevance and CTR | Crawl duplicates; review | Medium | Rewrite |
| G2 | One H1 aligned with title | Clarity | Crawl | Low | Template |
| G3 | Meta descriptions on money pages | CTR | Crawl | Low | Write |
| G4 | High impression, low CTR queries addressed | CTR | GSC queries vs own CTR curve | Medium | Titles, snippets, rich results |
| G5 | Images: alt text, dimensions, modern formats | Accessibility, CLS, image search | Crawl | Low | Template and CMS fields |
| G6 | WebSite site name markup on homepage | Site name in results | Rich Results Test | Low | Add |

## H. Content quality and E-E-A-T
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| H1 | Share of low quality pages per content type under 30% | Sitewide quality | Sample rating (eeat reference section 10) | High | Improve, merge, remove |
| H2 | Money and YMYL pages show first-hand experience and expertise | Quality | Review | High | SME input, evidence |
| H3 | Author bylines and author pages; reviewer for YMYL | Trust | Review | Medium | Add |
| H4 | About, contact, policies complete | Trust | Review | Medium | Add |
| H5 | Content decay list handled (top 20 decaying pages) | Traffic retention | Decay query | Medium | Refresh |
| H6 | No content outside the business's expertise produced for traffic | Quality and policy | Inventory | Medium | Noindex or remove |
| H7 | Dates honest (no fake freshness) | Trust | Diff content vs dateModified | Low | Fix process |

## I. Spam policy risk
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| I1 | No manual actions or security issues | Visibility | Search Console | Critical | Fix and reconsideration |
| I2 | No third party operated sections exploiting site signals (site reputation abuse) | Policy | Section inventory, operator check | Critical | Noindex or move |
| I3 | No scaled low value pages (AI, programmatic, translated) | Policy | Template inventory, indexing ratio | Critical | Gates, noindex, remove |
| I4 | No purchased or schemed links; no expired domain redirects | Policy | Backlink audit, history | High | Stop, remove, qualify |
| I5 | No doorway location or keyword variant pages | Policy | Inventory | High | Consolidate |
| I6 | No cloaking or bot specific content | Policy | Compare Googlebot and user fetch | Critical | Remove |
| I7 | UGC moderated, links `ugc`, spam profiles noindexed | Policy | Sample UGC | Medium | Moderation |

## J. Structured data
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| J1 | Organization (and LocalBusiness if relevant) markup with sameAs | Entity clarity | Validator | Low | Add |
| J2 | Product markup valid with price, availability, reviews where shown (ecommerce) | Rich results, merchant listings | Merchant listings report | High | Template fix |
| J3 | No markup for deprecated or ineligible types relied on for results | Wasted effort | Gallery check | Low | Remove or deprioritize |
| J4 | Markup matches visible content; no duplicate conflicting blocks | Policy and clarity | Extraction script | Medium | Consolidate |
| J5 | Enhancement reports free of errors on priority templates | Eligibility | Search Console | Medium | Fix |

## K. Core Web Vitals and mobile
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| K1 | Mobile CWV Good (LCP, INP, CLS at p75) on money templates | Ranking tie breaker, conversion | CrUX, CWV report | Medium | Template performance work |
| K2 | LCP image not lazy loaded, prioritized | LCP | Lighthouse, code | Medium | `fetchpriority`, preload |
| K3 | Third party scripts inventoried and justified | INP | Tag audit | Medium | Remove or defer |
| K4 | Mobile parity of content, links and markup | Mobile first indexing | Mobile render vs desktop | High | Responsive parity |
| K5 | No intrusive interstitials on mobile entry | UX | Manual check | Low | Banners |
| K6 | HTTPS everywhere, no mixed content | Security, trust | Crawl | High | Fix |

## L. International (if multiple locales)
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| L1 | hreflang reciprocal, self referencing, valid codes, x-default | Correct version shown | Validator script | High | Fix generation |
| L2 | hreflang targets 200, indexable, canonical | Signals accepted | Script | High | Fix |
| L3 | No IP or language auto redirects for bots | Crawl of all versions | Fetch from different locales | High | Banner instead |
| L4 | Localized content (currency, prices, legal, contact) | Relevance | Review | Medium | Localize |

## M. Local (if local presence)
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| M1 | GBP verified, primary category optimal, all fields complete | Local pack | GBP | High | Optimize |
| M2 | Business name compliant | Suspension risk | GBP vs signage | High | Correct |
| M3 | Review program with steady velocity and responses | Prominence, conversion | Review history | Medium | Program |
| M4 | Location pages with unique local proof linked from GBP | Relevance | Site review | Medium | Build |
| M5 | NAP consistent on top citations; Bing Places and Apple Business Connect claimed | Consistency | Citation audit | Low | Fix |
| M6 | Geo grid baseline tracked | Measurement | Tool | Low | Set up |

## N. Ecommerce, marketplace (if applicable)
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| N1 | Facet indexing rules implemented per matrix | Crawl and index control | Crawl, logs | High | Rules |
| N2 | Category pages with unique copy and crawlable product links | Rankings | Review | Medium | Template |
| N3 | Out of stock and discontinued handling per policy | Equity retention | Sample | Medium | Process |
| N4 | Duplicate product paths avoided (Shopify collection paths) | Crawl waste | Crawl | Low | Link canonical product URL |
| N5 | Merchant listings report clean; feed and markup consistent | Shopping surfaces | Search Console, Merchant Center | Medium | Fix; hand feed to commerce-feeds |
| N6 | Marketplace combinations gated by inventory | Thin pages | Index rules | High | Gates |

## O. Off-page
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| O1 | Referring domain growth from relevant editorial sources | Authority | Backlink tool trend | Medium | Link earning plan |
| O2 | Lost high value links reclaimed (404 targets redirected) | Equity | Backlinks to 404 | Medium | Redirects |
| O3 | Anchor text profile natural | Risk | Anchor distribution | Medium | Stop manipulation |
| O4 | Brand SERP and reviews healthy | Trust | Manual review | Medium | Reputation work |

## P. AI features and SERP
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| P1 | Query portfolio classified by AI Overview presence and intent | Realistic strategy | Rank tracker SERP features | Medium | Build classification |
| P2 | Generative AI report and Bing AI Performance reviewed monthly | Visibility trend | Reports | Low | Add to cadence |
| P3 | No unintended `nosnippet` or AI features opt-out | Lost visibility | Crawl directives; Search Console setting | High | Revert with approval |
| P4 | Key facts and entities consistent across site and profiles | AI answers and knowledge panel | Review | Low | Align; hand to ai-search-optimization |

## Q. Bing
| ID | Check | Why | How to verify | Severity | Fix |
|----|-------|-----|---------------|----------|-----|
| Q1 | Sitemaps processed in Bing Webmaster Tools | Coverage | BWT | Medium | Submit |
| Q2 | IndexNow firing on publish, update, delete | Freshness | Logs, plugin settings | Low | Configure |
| Q3 | Bingbot not blocked or crawl-delayed unnecessarily | Coverage | robots.txt, BWT crawl info | Medium | Fix |

## Scoring rubric
Weights: Critical 10, High 5, Medium 2, Low 1. Pass = full weight earned, Partial = half, Fail = 0, N/A excluded.

```
score = 100 x (sum of earned weights) / (sum of applicable weights)
```
Grade bands:
| Score | Grade | Meaning |
|-------|-------|---------|
| 90 to 100 | A | Strong foundation; focus on growth plays |
| 75 to 89 | B | Solid; fix High items this quarter |
| 60 to 74 | C | Material leaks; prioritize fixes before new content |
| Under 60 | D | Foundation broken; stop scaling content until fixed |

Blocker rule: any failed Critical item caps the grade at C regardless of score, and the report must list it first with an owner and a fix date.

Section sub-scores (same formula per section) show where to focus. Report the top 10 fixes ranked by (severity weight x affected revenue share x ease), each with owner, effort (S, M, L), approval needed, and verification method.

Audit deliverable outline:
```markdown
# SEO audit: <site> <date>
Data: <crawl date and tool, GSC property and range, GA4, backlinks source, CrUX>
## Score: <n>/100 (<grade>), blockers: <n>
## Section scores
| Section | Score | Critical fails | High fails |
## Critical blockers
## Top 10 fixes
| # | Item | Evidence | Impact | Effort | Owner | Approval | Verify by |
## Full results (by section, with evidence links)
## Change list for approval
## Re-audit date
```
