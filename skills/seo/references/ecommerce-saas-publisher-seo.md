# Ecommerce, Marketplace, SaaS and Publisher SEO

> Scope: vertical playbooks. Ecommerce (category pages, product pages, faceted navigation, product structured data, merchant listings, platform specifics), marketplaces, B2B SaaS (bottom of funnel pages, comparison and alternatives pages, integrations, templates, docs), publishers (Top Stories, Discover, preferred sources, paywalls, site reputation abuse risk). Lead gen and local services: see [local-seo.md](local-seo.md).

---

## Part A. Ecommerce

### A1. Where the revenue is
| Page type | Typical share of non-brand organic revenue | Primary queries |
|-----------|-------------------------------------------|-----------------|
| Category and subcategory (PLP) | Usually the largest [Practitioner consensus] | Head and mid tail product type queries ("women's trail running shoes") |
| Indexable facets (brand x type, type x attribute) | Material in large catalogs | "nike trail running shoes women", "waterproof hiking boots" |
| Product (PDP) | Long tail, model and SKU queries | "trail runner 2 review", model numbers |
| Buying guides and comparisons | Assist; commercial investigation | "best trail running shoes for beginners" |
| Brand pages | Navigational and brand plus type | "acme running shoes" |

Prioritize PLP and facet work first for most catalogs; PDPs scale through templates.

### A2. Category page (PLP) standard
- Unique H1 and title aligned to the head query.
- Short intro (1 to 3 sentences) above the grid; deeper buying guidance below the grid (150 to 400 words is a common working range; test for your catalog) [Practitioner consensus].
- Product grid rendered server side with crawlable links to PDPs (`<a href>`), images with alt text.
- Subcategory and popular facet links (crawlable) near the top.
- Pagination with crawlable links and self canonicals.
- Filters that change URLs follow the faceted navigation rules in [crawl-index-render.md](crawl-index-render.md).
- BreadcrumbList; optionally ItemList.
- FAQ content where real questions exist (no FAQ rich result expected).
- Merchandising rules that keep in-stock, relevant products on page 1.
- Thin category rule: categories with fewer than about 3 to 6 products or no demand should be merged or noindexed until inventory grows; empty categories return 404 or show alternatives with noindex.

### A3. Facet indexing matrix (decide per attribute)
| Attribute | Search demand | Inventory per value | Decision |
|-----------|---------------|---------------------|----------|
| Brand | High | Usually enough | Index brand x category pages |
| Gender, age group | High | Enough | Index |
| Use or activity | Medium to high | Varies | Index where inventory passes gate |
| Material, feature (waterproof, wide fit) | Medium | Varies | Index top values with demand |
| Color | Low for most categories, high for some (dresses, sofas) | Varies | Usually do not index; exceptions with demand |
| Size | Low except niche (petite, plus size, wide) | High | Index only demand backed sizes as named collections |
| Price range | Low | Any | Do not index |
| Rating, availability, sort, view | None | Any | Never index; disallow |

Gate example: index a facet URL only if (monthly searches for the combination at least 50 or GSC impressions exist) and (in-stock products at least 6) and (it has a unique title, H1 and intro). Generate these as static, linkable URLs and include them in a facet sitemap.

### A4. Product page (PDP) standard
- Unique title (`Brand Model Key attribute | Store`), unique description written from product knowledge, specs table, sizing and fit info, shipping and returns summary, FAQs from support tickets.
- Multiple high quality images (several aspect ratios), video where useful, alt text.
- Reviews and Q&A rendered in HTML (not only in an iframe or client side widget).
- Product and Offer structured data matching visible price, availability and ratings (see [structured-data.md](structured-data.md)).
- Related products, accessories, and the parent category link.
- Manufacturer descriptions copied across retailers add no value; at minimum add unique intro, specs context, use cases and reviews for top revenue SKUs.

Variants:
| Situation | Treatment |
|-----------|-----------|
| Variants differ only by size or color with no separate demand | One URL with variant selectors; variant parameter URLs canonical to the main URL; ProductGroup markup |
| Variants with distinct demand (color named products, different models) | Separate indexable URLs with unique content; ProductGroup ties them |

Out of stock and discontinued:
| Situation | Action |
|-----------|--------|
| Temporarily out of stock | Keep 200, show availability and restock date, offer alternatives, `availability: OutOfStock` (or BackOrder, PreOrder) |
| Discontinued with a direct successor | 301 to the successor |
| Discontinued, no successor, page has links or traffic | Keep a 200 page stating discontinued with alternatives for a period, or 301 to the closest category; avoid mass redirects to homepage |
| Discontinued, no value | 404 or 410 |
| Seasonal products | Keep URL year round; update content and availability |

### A5. Merchant listings and free listings
- Two paths to product rich features: product structured data on your pages, and a Merchant Center product feed (free listings). Use both and keep them consistent; mismatches in price or availability cause disapprovals and lost visibility. Feed work belongs to commerce-feeds.
- Search Console shows Merchant listings and Product snippets enhancement reports; when Merchant Center is linked, product issues appear there too.
- Organization level shipping and return policies (in Merchant Center, Search Console where available, or Organization markup) reduce per product markup work.
- Loyalty program pricing can show via MemberProgram markup or Merchant Center [Unverified rollout by market].
- AI generated product images need IPTC `DigitalSourceType` metadata in Merchant Center.

### A6. Internal search and other crawl traps
- Internal site search results: disallow in robots.txt (Google recommends against letting search result pages be crawled) and noindex. Exception: curated search landing pages built as categories.
- Cart, checkout, account, wishlist, compare: disallow.
- Session or currency parameters: never in links.

### A7. Platform notes
| Platform | Key SEO constraints |
|----------|---------------------|
| Shopify | Forced URL prefixes; duplicate collection product paths; tag pages; filter params; Markets for international; apps add scripts; sitemap not editable; `seo.hidden` metafield (details in technical reference) |
| WooCommerce | Product category and tag archives; attribute archives; pagination; plugin bloat; use one SEO plugin |
| Adobe Commerce (Magento) | Layered navigation parameter explosion; category path URLs for products (set canonical and use top level product URLs); full page cache |
| BigCommerce | Faceted search URLs; default canonicals; Stencil theme JSON-LD |
| Salesforce Commerce Cloud | URL rules, pipeline URLs, locale folders, heavy JS; requires dev sprints |
| Headless (Next.js, Hydrogen) | Rendering choices; must recreate canonicals, sitemaps, redirects and structured data the platform used to provide |

### A8. Ecommerce KPIs
Non-brand organic revenue by page type; indexable categories ranking top 3 for head terms; indexing ratio for PDP and category sitemaps; share of crawl on non indexable URLs (logs); merchant listing errors; CWV on PLP and PDP (INP often fails due to filters and third party scripts).

---

## Part B. Marketplaces and directories
- Architecture: category hubs x location or brand matrices, listing pages, profile pages.
- Index gating is mandatory: only index combinations with inventory over a threshold (for example 5 or more active listings) and demand; otherwise noindex and keep out of sitemaps; return 404 for empty.
- Listing pages: unique UGC (descriptions, photos, reviews) moderated for quality and spam; expired listings handled like discontinued products (keep with "no longer available" and similar listings if they have links, else 404 or 410).
- Avoid doorway patterns: location pages must show real local inventory and data (counts, price ranges, maps, local insights).
- Profile pages: ProfilePage markup, noindex empty or spam profiles.
- UGC links: `rel="ugc"` on user submitted links.

---

## Part C. B2B SaaS

### C1. Page types in priority order
| Priority | Page type | Example query | Notes |
|----------|-----------|---------------|-------|
| 1 | Product and feature pages | "crm with email sequences" | Specific benefits, screenshots, proof, pricing link |
| 1 | Use case, industry, role pages | "crm for real estate agents" | One page per real ICP segment with tailored proof |
| 1 | Alternatives pages | "hubspot alternatives" | High intent; honest, specific, migration help |
| 1 | Comparison pages (us vs competitor, competitor vs competitor) | "hubspot vs pipedrive" | Fair, sourced, updated; show where competitor fits better |
| 1 | Pricing page | "acme pricing" | Indexable, clear plans; captures branded and comparison traffic |
| 2 | Integration pages (programmatic) | "salesforce slack integration" | Real setup steps, use cases, limits, screenshots |
| 2 | Templates and free tools | "sales pipeline template" | Link earning and lead capture |
| 2 | "Best X software" lists | "best crm for small business" | Include yourself transparently; first-hand testing; third party lists often matter more (earn placements) |
| 3 | Problem and how to content near the product | "how to automate lead follow up" | Show the product as the method |
| 4 | Broad top of funnel and glossary | "what is a crm" | Most exposed to AI Overviews; only if supports funnel |

### C2. Comparison and alternatives page standard
- Title: `<Competitor> Alternatives: <N> Options for <ICP> (<Year>)` only if you maintain it yearly; `<A> vs <B>: <key difference>`.
- Opening: who should choose which, in 2 to 3 sentences.
- Comparison table with sourced facts (pricing pages, docs) and the date checked.
- Sections by decision criteria the ICP cares about (pricing model, integrations, onboarding, support, compliance).
- Fair treatment: state where the competitor is stronger; unsupported negative claims create legal and trust risk. Legal review for comparative claims in your markets.
- Migration path: import tools, services, timelines.
- Proof: customer quotes from switchers, review site ratings with dates.
- Update quarterly; competitors change pricing often.

### C3. Programmatic SaaS pages
- Integrations: one page per real integration with unique details; aggregate directory page; link from product pages.
- Templates: usable templates (download, duplicate in app), categories, internal links.
- Glossary: only when terms connect to product pages; avoid thin definitions (AI Overview exposed).
- Gate with the programmatic safeguards in [on-page-and-content.md](on-page-and-content.md).

### C4. Docs, help center, changelog, community
- Docs in a subfolder (`/docs/`) consolidate authority; subdomains work but split signals in practice [Contested].
- Docs rank for long tail feature and troubleshooting queries and feed AI answers; keep them crawlable (no client only rendering), versioned with canonicals to the latest version.
- Community forums: moderate, noindex empty threads, DiscussionForumPosting markup.

### C5. SaaS measurement
Organic signups, demo requests and pipeline by landing page group (product, comparison, integration, content), non-brand vs brand, and assisted conversions; CRM is the source of truth (MEASUREMENT.md). Many SaaS buyers research in AI assistants; hand off assistant visibility to ai-search-optimization.

---

## Part D. Publishers

### D1. Surfaces
| Surface | How you get in | Key levers |
|---------|----------------|-----------|
| Top Stories (news carousels) | Any indexed news content can appear; no AMP requirement since 2021 | Freshness, topical authority, original reporting, page experience, clear dates, Article markup, news sitemap |
| Google News | Automatic eligibility based on content and policies [Unverified current Publisher Center process] | Transparency (bylines, about, contact), policies |
| Discover | Indexed content meeting Discover policies; no markup needed | Large images (1200 px wide plus `max-image-preview:large`), compelling but honest titles, expertise, timeliness, local relevance |
| Preferred sources | Users choose favored sources for Top Stories (launched 2025-08 in US and India, expanding) [Official, 2025-08; expansion Unverified] | Ask loyal readers to add you via a button or link; verify the current link format in Google's help |
| Web search evergreen | Classic SEO | Topic hubs, explainers, updates |
| AI Overviews and AI Mode, Discover AI features | Same index | Original reporting is cited; generic rewrites are substituted |

### D2. Discover after the February 2026 update
Google's stated goals: more locally relevant content from sites based in the reader's country, less sensational and clickbait content, more in-depth, original and timely content from sites with demonstrated expertise in the topic [Official, 2026-02].
Actions:
1. Audit headlines in the Discover performance report: remove curiosity gaps, exaggeration, and withholding key information.
2. Concentrate on beats where you have expertise; reduce scattershot trend chasing.
3. Strengthen author pages and topical archives.
4. For international publishers: invest in coverage relevant to each country's audience rather than covering foreign markets remotely.
5. Image standards: unique, high resolution, relevant; no logos as lead images.
6. Track Discover clicks per article and share of articles getting any Discover traffic.

### D3. News technical standards
- `NewsArticle` markup with `datePublished`, `dateModified`, author with URL, images in several aspect ratios.
- News sitemap (articles from last 2 days, up to 1,000 URLs per file).
- Visible dates and bylines; correction notes.
- Live blogs: `LiveBlogPosting` markup and frequent updates; keep one URL per event.
- Paywalls: paywalled content markup (`isAccessibleForFree`, `hasPart` with `cssSelector`) so Google does not treat it as cloaking; flexible sampling choices are a business decision.
- Fast article templates; ad density that does not push content below the fold (CLS and INP from ad stacks are the most common failure).
- `max-image-preview:large` site wide.

### D4. Publisher risks
- Site reputation abuse: commerce, coupon, casino, or partner content sections operated by third parties. Audit every section's operator; noindex or move third party run sections (see [eeat-and-quality-policies.md](eeat-and-quality-policies.md)).
- Republishing old articles with new dates to appear fresh.
- Mass syndication without canonicals.
- AI written rewrites of other outlets' reporting (scaled content and scraping risk; low information gain).

### D5. Publisher KPIs
Search and Discover clicks per article, share of articles earning Discover traffic, Top Stories appearances for priority beats (rank tracker), returning users from search, subscriptions or registrations from search landings, RPM by entry source, Generative AI report impressions for Search and Discover.

---

## Part E. Apps
- Content only inside a native app is invisible to Search. Build indexable web pages for each use case and for shareable app content (profiles, listings, recipes).
- App deep links (Android App Links, iOS Universal Links) from web pages.
- App store optimization is separate; brand and feature web pages capture "best app for X" queries.
- Track installs from organic web via store attribution tools (hand to measurement).
