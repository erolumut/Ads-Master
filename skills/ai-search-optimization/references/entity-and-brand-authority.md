# Entity and Brand Authority

> Knowledge as of 2026-10. AI engines answer about entities (brands, products, people, places). They recommend brands they can identify unambiguously and describe consistently across many independent sources. This module makes the brand a clean, consistent, well-corroborated entity.

## 1. Why entity work matters

| Mechanism | Evidence | Implication |
|-----------|----------|-------------|
| Off-site branded mentions correlate most strongly with AI Overview brand visibility (0.664) | [Study, 2025, Ahrefs 75k brands; correlational] | Mentions on independent sites are the main lever |
| ChatGPT leaned heavily on Wikipedia in 2024 to 2025 citation data | [Study, 2025, Profound] | Reference sources shape descriptions |
| Google features need a clear entity (Knowledge Graph) to show brand panels and attribute facts | [Official, general Search documentation] | Organization markup and consistent profiles help Google connect sources |
| Engines hedge or mix up brands with similar names | [Practitioner consensus] | Disambiguation is a real problem for generic or shared names |

## 2. The brand fact sheet (single source of truth)

Create and maintain `ads-master/outputs/ai-search-optimization/YYYY-MM-DD_ai-search-optimization_brand-fact-sheet.md` and publish an equivalent public page (About or Press facts).

| Field | Example | Where it must match |
|-------|---------|--------------------|
| Legal and brand name | Acme Payroll, Inc. / Acme | Site, schema, LinkedIn, Crunchbase, G2, Wikidata, GBP |
| One-sentence description | "Acme is payroll and HR software for US small businesses with 5 to 100 employees." | Meta description, About, all profiles |
| Category terms | payroll software, HR software | Profiles, schema, review platform categories |
| Founded, HQ, founders, leadership | 2017, Austin TX | About, LinkedIn, Crunchbase, Wikidata |
| Products and plans | Core, Plus | Site, review platforms |
| Pricing (public) | From $40 plus $6 per employee | Pricing page, G2, Capterra |
| Key numbers | 12,000 customers (2026-09) | Press page, PR, profiles |
| Differentiators with proof | "Multi-state tax filing included on every plan" | Site, comparisons, PR |
| Official URLs and handles | site, LinkedIn, X, YouTube, GitHub | sameAs list |
| NAP (local) | Name, address, phone | GBP, Bing Places, Apple Business Connect, Yelp, directories |
| Things the brand is NOT | "Not affiliated with Acme Corp (industrial)" | About, FAQ |

Rule: when a fact changes, update the site first, then every profile within 14 days, then log a journal entry.

## 3. Structured data for entities

Google says structured data is not required for AI features and must match visible content [Official]. Bing has said schema helps its systems understand content [Practitioner report, 2025-03]. Use it for disambiguation and rich results, not as a citation hack.

### 3.1 Organization (home page or About)

```json
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "https://www.example.com/#organization",
  "name": "Acme",
  "legalName": "Acme Payroll, Inc.",
  "url": "https://www.example.com/",
  "logo": "https://www.example.com/static/logo.png",
  "description": "Payroll and HR software for US small businesses with 5 to 100 employees.",
  "foundingDate": "2017",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Austin",
    "addressRegion": "TX",
    "addressCountry": "US"
  },
  "sameAs": [
    "https://www.linkedin.com/company/example",
    "https://www.youtube.com/@example",
    "https://x.com/example",
    "https://www.wikidata.org/wiki/Q00000000",
    "https://www.crunchbase.com/organization/example",
    "https://www.g2.com/products/example/reviews"
  ]
}
```

Rules:
1. Use one stable `@id` for the organization and reference it from Product, Article publisher and WebSite markup.
2. sameAs lists only profiles the brand controls or that are canonical about it (Wikidata, Wikipedia if it exists, review profile).
3. Never mark up facts that are not visible on the page.

### 3.2 Product (ecommerce and SaaS)

Include name, description, brand (reference to Organization), sku or gtin where applicable, offers (price, priceCurrency, availability), and aggregateRating only when ratings are visible on the page and collected per Google's review snippet guidelines (no self-serving reviews of your own business on Organization or LocalBusiness pages) [Official]. Product feed work belongs to `commerce-feeds`; on-page markup belongs here and to `seo`.

### 3.3 Other types

| Type | Use when | Notes |
|------|----------|-------|
| LocalBusiness (and subtypes) | Physical locations or service areas | Match NAP exactly with Google Business Profile |
| Person | Authors and executives quoted as experts | Link to their profiles via sameAs |
| Article or BlogPosting | Editorial content | author, datePublished, dateModified, publisher reference |
| SoftwareApplication | SaaS and apps | applicationCategory, operatingSystem, offers |
| FAQPage | Visible FAQ content | Rich results limited by Google since 2023; keep for clarity only |
| Review, AggregateRating | Product reviews shown on page | Follow review snippet policy |

Validate with the Schema Markup Validator and Google's Rich Results Test. Hand off sitewide implementation to `seo`.

## 4. Wikidata and Wikipedia

| Asset | Who qualifies | What to do | What not to do |
|-------|--------------|------------|----------------|
| Wikidata item | Entities with a clear identity and references (often lower bar than Wikipedia) | Create or correct the item with references to independent sources; add official website, logo, founding date, headquarters, social IDs, industry | Add promotional descriptions; add unsourced claims |
| Wikipedia article | Only if notable under Wikipedia's notability guidelines (significant coverage in independent reliable sources) | If an article exists: propose corrections on the Talk page with sources and disclose conflict of interest. If none exists and the brand is notable: wait for independent editors, or use the Articles for Creation process with full COI disclosure | Write or edit your own article directly; hire undisclosed paid editors (violates Wikipedia terms of use) |

Rule: Wikipedia is earned through independent press coverage. The upstream work is PR, not editing.

## 5. Knowledge Graph and brand SERP

1. Search the brand name in Google. Note whether a Knowledge Panel appears and whether facts are right.
2. If a panel exists, claim it through Google's verification flow and suggest edits with sources.
3. Align the brand SERP: home page, About, social profiles, review profiles and press should own page 1. Brand SERP results are what AI engines see when they research the brand.
4. Check Bing for the same brand query. Copilot and some ChatGPT paths draw from it.

## 6. Review platforms

| Business model | Platforms that typically appear in AI answers | Notes |
|----------------|---------------------------------------------|-------|
| B2B SaaS | G2, Capterra, TrustRadius, Gartner Peer Insights, Software Advice, GetApp | Category placement matters; keep profiles current |
| B2C ecommerce | Trustpilot, Google reviews (seller and product), Amazon reviews, Reddit threads, YouTube reviews | Product review volume and recency feed shopping answers |
| Local services | Google Business Profile, Yelp, Angi, BBB, Nextdoor, TripAdvisor (hospitality), Healthgrades (health) | Review count, rating, recency and responses |
| B2B services and agencies | Clutch, G2 services, UpCity, Google reviews | Case studies with numbers |
| Apps | App Store, Google Play | Ratings volume and recent reviews |

Verify which platforms are actually cited for your prompts. Do not assume.

Compliance rules:
1. The US FTC rule on fake reviews and testimonials (announced 2024-08, effective 2024-10) prohibits fake or AI-generated reviews, buying reviews, insider reviews without disclosure, and review suppression; civil penalties apply [Official, 2024].
2. Platform rules (Google, Amazon, Trustpilot, G2) ban incentives conditioned on positive sentiment and review gating. Ask every customer, not only happy ones.
3. Respond to negative reviews factually. Engines summarize sentiment, including unresolved complaints.

Review velocity plan:
1. Identify the two to three platforms cited most for your category prompts.
2. Add a review request step to the post-purchase or post-onboarding flow (all customers, no gating).
3. Target a steady monthly flow rather than bursts. Recency matters to buyers and plausibly to engines [Practitioner consensus].
4. Track count, average rating and recency monthly in the AI visibility report.

## 7. Digital PR for mentions

Objective: unlinked and linked mentions of the brand, with correct facts, on domains that AI engines cite for your priority prompts.

| Tactic | Fit | Notes |
|--------|-----|-------|
| Original data studies | All | Highest leverage; see content module |
| Expert commentary (journalist request platforms, newsletters, podcasts) | B2B, services, SaaS | Prepare quotable, specific answers |
| Inclusion in industry roundups and "best X" lists | All | Pitch with data and differentiation; affiliate programs where the publisher uses them, with disclosure |
| Awards and rankings with real criteria | B2B, local | Avoid pay-to-win awards with no editorial process |
| Partnerships and integrations directories | SaaS | Partner pages often rank for "X integrations" sub-queries |
| Customer case studies published by customers | B2B | Third-party domain mentions |
| Analyst relations | Enterprise B2B | Analyst reports feed buyer prompts |

Prioritization: list domains cited for your top prompts (from tracking), then pick PR targets from that list first.

## 8. Misinformation and inaccurate answers

Workflow when an engine states something wrong about the brand:
1. Capture: engine, mode, date, prompt, full answer, cited URLs (screenshot and text).
2. Reproduce: run the prompt at least 5 times across logged-out and logged-in sessions. Classify as systematic (appears in most runs) or sporadic.
3. Trace: open every cited URL. Find which source states the wrong fact. If no source is cited, it is likely parametric (training data) or a hallucination.
4. Fix at the source:
   1. Own site wrong or ambiguous: correct it, add a dated, explicit statement.
   2. Third-party page wrong: contact the publisher with evidence; update review platform profiles; suggest Wikidata or Wikipedia corrections via proper channels.
   3. Parametric or hallucinated: publish a clear, crawlable fact page; increase consistent mentions; use engine feedback buttons (thumbs down with explanation).
5. Re-test weekly for four weeks. Log outcome in the journal. Systematic errors on safety, pricing or legal facts go to the human immediately.
6. Do not threaten engines or publish attack content. Do not create fake pages to "overwrite" facts.

Severity scale:

| Severity | Example | Response time |
|----------|---------|---------------|
| Critical | Says product is unsafe, discontinued, a scam, or wrong legal or medical claim | Same day escalation to human |
| High | Wrong pricing, wrong availability, confuses with another company | Within 1 week |
| Medium | Outdated features, missing key differentiator | Within 1 month |
| Low | Tone, minor detail | Backlog |

## 9. Entity audit procedure

1. Run brand prompts across engines: "What is <brand>?", "Is <brand> legit?", "<brand> pricing", "<brand> vs <top competitor>", "Who owns <brand>?", "<brand> reviews". Five runs each, logged-out.
2. Score accuracy (0 to 2 per fact against the fact sheet), sentiment (negative, neutral, positive), and completeness (key differentiators mentioned).
3. List every cited domain and check its facts against the fact sheet.
4. Check schema, Wikidata, Knowledge Panel, review profiles, NAP consistency.
5. Output a correction list ranked by severity and reach.
