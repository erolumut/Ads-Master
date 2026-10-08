# Site Architecture and Internal Linking

> Scope: how pages are organized, connected and prioritized. URL design, hub and spoke clusters, click depth, navigation, breadcrumbs, contextual links, anchor text, orphan pages, internal link audits and a prioritized link plan. Faceted navigation and pagination mechanics are in [crawl-index-render.md](crawl-index-render.md).

## 1. Why this is the highest leverage lever you control
- Internal links are how Google discovers URLs, understands topical relationships and distributes link equity (PageRank still exists as one of many signals) [Official, ranking systems guide lists link analysis systems and PageRank].
- They cost nothing but dev or editorial time, take effect on recrawl, and are fully reversible.
- Pages ranking 4 to 20 with few internal links are the most reliable quick wins in most audits [Practitioner consensus].

## 2. Architecture principles
1. Money pages within 3 clicks of the homepage. Click depth correlates with crawl frequency and perceived importance.
2. Hub and spoke: each topic has a hub (category, pillar, product line) that links to every spoke, and spokes link back to the hub and to closely related spokes.
3. URL paths reflect hierarchy only when the hierarchy is stable. Flat URLs (`/product-name`) are fine; deep folder paths make future restructures expensive.
4. One canonical path per page. Avoid the same page living under several folders.
5. Navigation is for users and for priority. Global navigation links appear on every page and concentrate equity; reserve them for revenue and hub pages.
6. Subfolders by default for new content types (blog, docs, locations). Subdomains are treated as separate sites in many respects and split authority in practice [Contested: Google says both work; practitioner tests often favor subfolders].

## 3. URL design rules
| Rule | Good | Bad |
|------|------|-----|
| Lowercase, hyphens, readable words | `/running-shoes/womens/` | `/Category.aspx?id=443&cat=2` |
| Stable: no dates or IDs unless meaningful | `/guides/seo-migration-checklist` | `/2023/04/12/post-1234` for evergreen content |
| No stop word bloat, no keyword stuffing | `/crm-for-real-estate` | `/best-crm-software-for-real-estate-agents-crm-tool` |
| No session IDs or tracking parameters in internal links | `/pricing` | `/pricing?utm_source=nav` |
| Language or market folder at root for international | `/de-de/` | `?lang=de` |
| Trailing slash policy consistent | Always or never | Mixed |

Changing URLs costs rankings temporarily even with redirects. Do it only when the gain is structural (consolidation, migration, international), never for cosmetic keywords.

## 4. Architecture templates by business model
| Model | Structure | Hubs | Cross links |
|-------|-----------|------|-------------|
| Ecommerce | Home > Department > Category > Subcategory or indexable facet > PDP | Category pages | PDP to siblings, accessories, parent category; buying guides to categories |
| B2B SaaS | Home > Product, Solutions (use case, industry, role), Integrations, Compare, Pricing, Resources (blog, templates, docs) | Product and solution pages; integration directory; comparison hub | Blog posts to the solution or feature they support; integration pages to use cases |
| Lead gen and local services | Home > Services > Service detail; Locations > City > City x Service (only where real presence) | Service pages, location hubs | Location pages to services offered there; service pages to locations served |
| Publisher | Home > Sections > Topic hubs > Articles; Author pages | Topic hubs (curated, updated) | Articles to hub and to related articles; hubs to evergreen explainers |
| Marketplace | Home > Category > Category x Location or Brand > Listing | Category and location hubs | Listing to related listings and parent hubs; seller profile to listings |
| Docs and help center | Product area > Topic > Article | Product area index | Article to prerequisites and next steps |

## 5. Link types and how to use them
| Link type | Role | Rules |
|-----------|------|-------|
| Global navigation | Signals site wide priority | Hubs and revenue pages only; mega menus with hundreds of links dilute and slow INP |
| Footer | Utility, trust, secondary hubs | Avoid keyword stuffed footer link blocks |
| Breadcrumbs | Hierarchy, crawl paths, rich result | Every page below home; mark up with BreadcrumbList |
| Contextual in-content links | Strongest relevance signal | Descriptive anchors, placed where useful, 3 to 10 per 1,000 words as a sanity range [Practitioner consensus] |
| Related modules (related products, posts) | Scalable equity flow | Generate by topic similarity or taxonomy, not randomly; limit to 4 to 12 links |
| HTML sitemap or index pages | Catch all for large sites | Useful for directories and marketplaces with deep inventory |
| Pagination links | Crawl paths to deep items | Crawlable `<a href>` |

Anchor text:
- Describe the target page's topic in natural language ("enterprise CRM pricing", "how to size running shoes").
- Vary anchors across sources; identical exact match anchors from hundreds of templated links look manipulative and add little.
- Avoid "click here" and "read more" as the only anchor; add context or an `aria-label` for accessibility.
- Internal `rel="nofollow"` does not "sculpt PageRank"; it only withholds discovery. Use it almost never internally.

## 6. Internal link audit procedure
Inputs: full crawl (Screaming Frog or Sitebulb, JavaScript rendering on if the site needs it), Search Console performance by page (last 3 months), sitemap list, business value per page (revenue, lead value, or a 1 to 5 priority).

Steps:
1. Crawl. Export for each URL: crawl depth, unique inlinks, unique outlinks, link score or internal PageRank, indexability, status.
2. Join with GSC page data (clicks, impressions, average position) and the priority list.
3. Find orphans: URLs in sitemaps, GSC or logs that the crawl did not reach. Classify: valuable (link them), obsolete (redirect or remove).
4. Find deep money pages: priority 4 or 5 pages with depth over 3.
5. Find under-linked opportunities: pages ranking 4 to 20 for valuable queries with fewer inlinks than the median of pages ranking 1 to 3 in the same template.
6. Find wasted equity: global links to low value pages (login variants, tag archives, filtered URLs), links to redirects and 404s.
7. Find cannibalization signals: two pages receiving internal links with the same anchor for the same query.
8. Build the link plan (template below), ranked by score.

Opportunity score per target page:
```
score = business_value (1 to 5)
      x position_factor (pos 4 to 10: 1.0, 11 to 20: 0.7, 21 to 50: 0.3, other: 0.1)
      x log10(impressions_3m + 10)
      / (1 + current_unique_inlinks / median_inlinks_of_template)
```
Rank by score; take the top 20 targets per sprint.

Source selection for each target:
- Pages topically closest to the target (same cluster, shared queries, site search `site:example.com "topic"`, or embeddings similarity from a crawler with AI integration).
- Pages with authority: many external referring domains, high crawl frequency, strong internal link score.
- Pages with traffic: users actually follow the link.

Link plan template (deliverable):
| # | Target URL | Target query set | Source URL | Placement (paragraph or module) | Anchor text | Rationale | Owner | Status |
|---|-----------|------------------|-----------|-------------------------------|------------|-----------|-------|--------|
| 1 | /crm-for-real-estate | crm for real estate agents | /blog/real-estate-lead-follow-up | Paragraph 3, after "follow up cadence" | CRM built for real estate agents | Same cluster, 41 referring domains | Editor | Draft |

Measurement: annotate the date in Search Console; compare target pages' clicks and average position 4 and 8 weeks after vs the 4 weeks before, against a control group of similar pages without new links. Log as an experiment in EXPERIMENTS.md when the batch is 20 or more pages.

## 7. Scalable internal linking in code
Related links module by shared taxonomy and recency (Next.js server component example):
```tsx
// app/blog/[slug]/Related.tsx (server component)
export default async function Related({ slug, tags }: { slug: string; tags: string[] }) {
  const related = await db.post.findMany({
    where: { slug: { not: slug }, tags: { hasSome: tags }, indexable: true },
    orderBy: [{ priority: 'desc' }, { updatedAt: 'desc' }],
    take: 6,
    select: { slug: true, title: true },
  })
  if (!related.length) return null
  return (
    <nav aria-label="Related guides">
      <h2>Related guides</h2>
      <ul>{related.map(p => <li key={p.slug}><a href={`/blog/${p.slug}`}>{p.title}</a></li>)}</ul>
    </nav>
  )
}
```
Rules for modules:
- Server rendered, plain `<a href>`.
- Exclude noindex, redirected and out of stock discontinued targets.
- Deterministic output per page (do not reshuffle on every request; it changes the link graph on every crawl).
- Cap the number of links; prefer relevance over volume.

Auto linking plugins that insert exact match anchors for keywords across thousands of posts produce unnatural patterns. Use them only with curated keyword to URL maps and a per page cap of 2 to 3 auto links.

## 8. Consolidation and cannibalization
Detect: one query with impressions on 2 or more URLs from the same site where the ranking URL flips week to week, or a lower quality URL ranks instead of the intended one. Query in [keyword-research-and-topical-maps.md](keyword-research-and-topical-maps.md).

Resolve:
| Situation | Action |
|-----------|--------|
| Two pages, same intent, one stronger | Merge best content into the stronger URL, 301 the weaker, update internal links |
| Two pages, different intents misread | Sharpen titles, H1 and copy to separate intents; adjust internal anchors |
| Blog post outranks the commercial page for a commercial query | Link the post to the commercial page with a descriptive anchor, strengthen the commercial page; consider merging |
| Category and subcategory compete | Differentiate scope and copy; link subcategory from category with specific anchor |

## 9. Breadcrumbs
- Visible on every page below the homepage, matching the hierarchy, with BreadcrumbList structured data (see [structured-data.md](structured-data.md)).
- On PDPs reachable from several categories, pick one primary category path for the breadcrumb.
- Mobile layouts often hide breadcrumbs; with mobile first indexing, hidden breadcrumbs lose their link value. Keep them in the mobile HTML.

## 10. Architecture changes: when to restructure
Restructure only when one of these holds:
- Important pages sit deeper than 4 clicks and cannot be surfaced with links alone.
- Two or more sections compete for the same intents.
- The business added a product line, market or language.
- A migration is happening anyway.
Every restructure follows the [migrations playbook](migrations-playbook.md), including a full redirect map.
