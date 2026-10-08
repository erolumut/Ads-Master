# Content Engineering for LLMs

> Knowledge as of 2026-10. Goal: make owned pages the easiest, most trustworthy passage for an engine to retrieve, quote and cite for the sub-questions buyers ask. Everything here also has to work for humans and for classic SEO. If a tactic only works for bots, do not ship it.

## 1. The five properties of a citable page

| Property | Test | Failure looks like |
|----------|------|-------------------|
| Retrievable | Bot allowed, 200 status, key text in raw HTML, indexed in Google and Bing | Pricing rendered by JavaScript; page behind a bot challenge |
| Matchable | A passage closely matches a real sub-query in wording and meaning | Page targets "solutions" language buyers never use |
| Extractable | The answer sits in one self-contained passage of 40 to 120 words that names the entity | Answer spread across tabs, sliders, images or pronouns |
| Citable | Specific, verifiable facts: numbers, dates, named sources, original data | Generic claims ("industry leading", "best in class") |
| Consistent | Facts match what third-party pages say about the brand | Old pricing on G2, new pricing on site; the engine hedges or picks the wrong one |

## 2. Proven vs speculative

| Tactic | Status | Evidence |
|--------|--------|----------|
| Add real statistics with sources to key passages | Supported | [Study, 2024, Princeton GEO: statistics addition among top methods] |
| Add attributed quotations from named experts | Supported | [Study, 2024, Princeton GEO: quotation addition among top methods] |
| Cite authoritative sources inline | Supported, strongest for lower-ranked pages | [Study, 2024, Princeton GEO] |
| Clear, fluent, simple language | Small positive effect | [Study, 2024] |
| Keyword stuffing | Does not work | [Study, 2024] |
| Server-rendered text | Required for most AI crawlers | [Study, 2024-12, Vercel logs] |
| Answer-first section openings | Strong practitioner consensus, consistent with passage retrieval | [Practitioner consensus] |
| Tables for comparisons and specs | Practitioner consensus; tables are extractable and often reproduced in answers | [Practitioner consensus] |
| Original data and research | Strong practitioner consensus; primary sources attract citations and mentions | [Practitioner consensus] |
| Freshness updates on decision pages | Supported by observational studies | [Study, 2025] |
| FAQ sections | Plausible for extraction; FAQ rich results limited by Google since 2023 to authoritative government and health sites | [Official for rich results; Unverified for AI lift] |
| Question-phrased headings | Plausible; matches conversational sub-queries | [Practitioner consensus] |
| Front-loading facts in title and first 200 characters | Plausible; reported ChatGPT index stores limited text | [Unverified] |
| Separate markdown copies of pages for bots | Not needed; Google calls it temporary and unnecessary; risk of inconsistency | [Practitioner report, 2026-05] |
| Hidden text or instructions aimed at LLMs | Prohibited. Treated as spam or prompt injection; can get pages filtered | [Official spam policies; Practitioner consensus] |
| Mass AI-generated pages | High risk under Google's scaled content abuse policy (2024-03) | [Official, 2024] |

## 3. Answer-first passage pattern

Use this for every section that targets a sub-query.

```
## <Question as the buyer asks it>

<Entity name> <direct answer in one sentence with the key fact, number or verdict>.
<One to two sentences of qualification: who it applies to, conditions, date>.
<Evidence: statistic with source, or quote with name and role, or link to data>.

<Optional: table or 3 to 6 bullet list with specifics>
```

Worked example (B2B SaaS pricing):

```
## How much does Acme Payroll cost for a 20 person company?

Acme Payroll costs $6 per employee per month plus a $40 monthly base fee,
so a 20 person company pays $160 per month on the Core plan (pricing as of
2026-09). Multi-state tax filing is included; HR add-ons cost $4 per employee.
Annual billing cuts the total by 15%.

| Plan | Base fee | Per employee | Multi-state | Time tracking |
|------|----------|--------------|-------------|---------------|
| Core | $40 | $6 | Included | Add-on |
| Plus | $80 | $9 | Included | Included |
```

Rules:
1. Name the entity in the first sentence of each section. Passages are retrieved out of context.
2. Put the number in the first sentence. Add the date for anything that changes.
3. One question per section. If you need "and", split it.
4. 40 to 120 words before any table or list [Practitioner consensus].
5. No marketing adjectives without proof.

## 4. Chunking and page structure

| Element | Rule |
|---------|------|
| Title tag and H1 | State the entity and the answer type ("Acme vs Globex: pricing, features and which to choose (2026)") |
| Intro (first 100 words) | Summarize the verdict or the key facts. No throat clearing |
| H2s | Phrase as the sub-queries from the fan-out map |
| Section length | 80 to 300 words per section is typical; long enough to answer, short enough to stay on one idea |
| Lists | Use for criteria, steps, pros and cons |
| Tables | Use for comparisons, specs, pricing, eligibility. HTML tables, never images |
| Tabs and accordions | Fine only if the content is in the initial HTML (not loaded on click) |
| Images and charts | Add the key number in the caption or adjacent text |
| PDFs | Publish an HTML version of any report you want cited |
| Dates | Visible "Updated YYYY-MM-DD" plus accurate dateModified in schema when content changes materially |
| Internal links | Link each facet page to the hub and to sibling comparisons |

## 5. Page types that earn citations (by prompt class)

| Prompt class | Example prompt | Page type to own | Must contain |
|-------------|----------------|------------------|--------------|
| Category "best" | "best CRM for small law firms" | Category guide with honest criteria; plus earned inclusion on third-party lists | Criteria, who each option fits, pricing ranges, your product's honest position |
| Comparison | "Acme vs Globex" | X vs Y page | Side-by-side table, differences that matter, who should choose which, dated |
| Alternatives | "alternatives to Globex" | Alternatives page | Several real alternatives including yourself, reasons people switch, migration notes |
| Pricing | "how much does Acme cost" | Public pricing page | Numbers, plan limits, add-ons, billing terms, date |
| How-to | "how to run payroll in Texas" | Guide | Steps, requirements, numbers, sources, tool-agnostic first, product second |
| Definition | "what is employer of record" | Glossary entry | One-sentence definition, how it works, examples, related terms |
| Data | "average cost of X in 2026" | Original research or statistics page | Method, sample, date, downloadable data, quotable key findings |
| Trust | "is Acme legit", "Acme reviews" | About, security, reviews hub | Founding date, team, customers, certifications, review platform links |
| Local | "best emergency plumber near me" | Location pages plus Google Business Profile | NAP, service area, hours, prices or ranges, licenses, reviews |
| Product | "waterproof hiking boots under $150" | Product and collection pages | Specs in text, price, availability, materials, sizing, reviews |

## 6. "Best X" and listicle content: do it honestly

1. Owned "best X" pages that rank yourself first with no real criteria are a known manipulation pattern. Practitioners reported visibility losses for self-serving listicles in 2026 [Unverified]. Engines and users discount them.
2. Acceptable owned format: "How to choose X" with published criteria, a fair comparison table including competitors, and a clear statement of your bias ("We make Acme. Here is where Acme fits and where it does not.").
3. Third-party lists carry more weight. Earn them through product quality, review data, PR, analyst relations and affiliate programs with disclosure. See [Off-site](off-site-and-community-presence.md).

## 7. Statistics, quotations and sources (apply the GEO findings without fabricating)

| Method | Do | Never |
|--------|----|-------|
| Statistics | Use your own data (anonymized aggregates), public datasets, or cited studies with year | Invent numbers or round up to sound impressive |
| Quotations | Quote named people with role (customers with permission, internal experts, external experts) | Fabricate quotes or attribute to "experts" |
| Sources | Link to primary sources (official docs, studies, standards) | Cite low-quality aggregators that cite each other |
| Recency | State the date of every number | Present old numbers as current |

Original data playbook:
1. Find a question your buyers and journalists ask that nobody answers with data.
2. Use first-party data (product usage, transactions, support tickets) or run a survey with a stated method and sample.
3. Publish an HTML report with: method, sample, date, 5 to 10 quotable findings each in its own sentence, charts with text captions, downloadable table.
4. Pitch the findings to journalists and newsletters (digital PR). Mentions on cited domains are the payoff.
5. Refresh annually with the year in the title.

## 8. Freshness without faking

| Page type | Review cadence | What counts as a real update |
|-----------|---------------|------------------------------|
| Pricing, plans | On every change, at least quarterly check | New numbers, plan changes |
| Comparisons and alternatives | Quarterly | Competitor pricing, features, new entrants |
| Best-of and buyer guides | Quarterly to semiannually | New options, retested criteria |
| Statistics pages | Annually or when sources update | New data |
| Evergreen how-to | Annually | Regulation, UI or process changes |

Never change only the date. Engines and Google compare content changes, and users notice stale facts under a new date.

## 9. Fan-out coverage procedure (content gap analysis)

1. Take the top 20 to 50 priority prompts from the prompt set (see [Measurement](measurement-and-prompt-tracking.md)).
2. Build the fan-out map for each (see [Retrieval](how-ai-engines-retrieve-and-cite.md) section 4).
3. Create a coverage sheet:

| Prompt | Facet | Sub-query | Our URL | Passage exists? (Y/N) | Fact current? | Cited domains for this sub-query | Gap action |
|--------|-------|-----------|---------|----------------------|---------------|----------------------------------|-----------|

4. Prioritize gaps by: commercial intent of the prompt, how often competitors are mentioned, and whether the cited domains are reachable for you.
5. Write or rewrite passages using the pattern in section 3. One brief per page.

## 10. Content brief template (LLM-ready page)

```
# Content brief: <page>
Date: YYYY-MM-DD | Owner: ai-search-optimization | Hand off to: seo (on-page), human editor
Target prompts (from prompt set IDs): P012, P031, P044
Primary sub-queries (fan-out map): ...
Current state: URL, rendering check result, last updated, current citations (engines, dates)
Entities to name explicitly: brand, product, category, competitors, locations
Facts to state (with source and date): ...
Original data or quotes to include: ...
Sections (H2 as question -> one-line answer to lead with):
1. ...
Tables required: ...
Schema: Article or Product or FAQPage (if content is visible), Organization reference
Freshness: visible updated date, dateModified on material change
Do not: superlatives without proof, hidden text, competitor claims without a source
Success measure: mention rate and citation share for target prompts after 4 to 8 weeks (n runs)
```

## 11. Editorial QA checklist before publishing

1. Every section opens with a direct answer that names the entity.
2. Every number has a date and a source.
3. Key content is in the raw HTML (curl test passed).
4. Comparison claims about competitors are accurate, dated and sourced.
5. No hidden text, no bot-only content, no instructions to AI systems.
6. Title and first paragraph state the answer.
7. Facts match the brand fact sheet (see [Entity](entity-and-brand-authority.md)) and third-party profiles.
8. Schema matches visible content.
9. Internal links connect the page to its hub and siblings.
10. A human editor approved it. Publishing needs explicit approval.
