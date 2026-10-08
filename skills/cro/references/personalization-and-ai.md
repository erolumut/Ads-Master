# Personalization and AI in CRO

> Personalization is a test, not a feature. Every rule or model that changes content per segment must beat a non-personalized holdout. AI speeds up research, ideation and variant production; it does not replace evidence, compliance review or statistics.

## 1. Personalization ladder (climb only when the lower rung is done)

| Rung | What changes | Data needed | Typical tools | Measure against |
|------|-------------|-------------|---------------|-----------------|
| 0. One great page | Nothing per segment | Research | Any | Previous page |
| 1. Source-based message match | Hero by ad angle, keyword theme, campaign | UTM or allowlisted URL parameter | Server-side templates, CMS collections | Generic hero |
| 2. Context rules | Geo (currency, shipping, payment methods), device, new vs returning, time | Request headers, cookie | Platform features, edge middleware, testing tools | No-rule control |
| 3. Behavioral segments | Cart contents, browsing category, lifecycle stage | First-party events | Optimizely, Wingify (VWO, AB Tasty), Kameleoon, Dynamic Yield, Shopify apps | Holdout |
| 4. B2B account-based | Industry, company size, named accounts | Reverse IP, CRM, enrichment | Mutiny type tools, Optimizely, custom | Holdout |
| 5. Model-driven 1:1 | Product recommendations, ranking, offers per user | Large event history | Recommendation engines, contextual bandits | Holdout |

Optimizely's experiment data reported a primary metric win rate of 12.5% for personalized (targeted) experiments vs 10.7% for untargeted ones [Study, 2023]: a modest edge, not a magic jump.

## 2. Segment selection
Personalize for a segment only when:
1. The segment is large enough to measure (use the sample size table in [Experimentation statistics](experimentation-statistics.md)).
2. Research shows the segment has different needs or objections (not just a different conversion rate).
3. You can maintain the content (each segment variant is a page to keep current, legal and fast).

High-value segments that usually justify rungs 1 to 2:
- Paid traffic by angle or keyword theme (message match).
- Country: currency, shipping cost and time, local payment methods, local reviews.
- Returning visitors with items in cart: resume cart, show reassurance.
- B2B industry: logos, case study and use case for that industry.
- AI referral visitors: deep pages with specs and comparisons (they are pre-informed).

## 3. Implementation patterns

| Pattern | How | Pros | Cons |
|---------|-----|------|------|
| Separate URLs per segment | `/lp/flat-feet`, `/lp/wide-feet` | Simple, cacheable, clean analytics | More pages to maintain |
| Server-side rendering by parameter | Allowlisted `?angle=` read on the server | One template, no flicker | Cache key must include the parameter |
| Edge middleware | Assign or select variant at the CDN edge, rewrite to static variant | Fast, no flicker | Platform specific (Vercel, Netlify, Cloudflare) |
| Client-side tool | JS swaps content after load | No dev work per change | Flicker, slower LCP, blocked by some privacy tools |
| Platform native | Shopify Markets for geo pricing and currency, Rollouts for theme tests | Integrated | Limited targeting |

Rules:
- Never print raw URL text into the page. Map keys to approved copy.
- Personalized prices must be lawful and transparent. Do not use personal data or inferred vulnerability to set prices. EU and US regulators scrutinize "surveillance pricing" [Unverified, regulatory focus 2024 to 2026].
- Consent: personalization based on cookies or tracking identifiers needs consent where ePrivacy rules apply (EEA, UK). Context-based personalization (URL, geo from IP for currency) usually does not, but confirm with the human's legal advisor.

## 4. AI in the CRO workflow

| Step | Good use of AI | Human or data check required |
|------|----------------|------------------------------|
| Research | Summarize recordings (Clarity Copilot session insights, Contentsquare Sense), code survey and review verbatims, cluster themes | Spot-check 10% of summaries against raw data |
| Heuristic audit | First pass with a checklist on screenshots or HTML | Confirm each finding on a real device |
| Ideation | Generate hypotheses from research, generate 10 headline options from VOC | Each idea must cite evidence |
| Copy variants | Draft variants in brand voice from the copy deck | Claims, legal, brand voice review |
| Build | Generate code diffs for variants in the repo | Code review, QA, performance check |
| Analysis | Explain results, check SRM, draft readouts | Use the platform stats engine as source of truth |
| Personalization | Generate segment-specific copy sets | Holdout test, maintenance plan |

### 4.1 Vendor AI features (status as of 2026-10, verify before relying)
| Vendor | AI features | Date and status |
|--------|-------------|-----------------|
| Optimizely | Opal renamed Optimizely Agent Platform (1 Sept 2026); Idea builder for Web (April 2026) and Feature Experimentation (22 June 2026); Build agent turns an idea into a draft A/B test with variation, metric and audience (Sept 2026); CRO Manager virtual teammate stages experiments (25 Aug 2026); contextual multi-armed bandits (28 April 2026) | [Official, Optimizely release notes 2026; exact dates vary by note] |
| Wingify (VWO and AB Tasty) | Combined in January 2026, rebranded Wingify on 16 Sept 2026; embedded AI engine "Wingz" across experimentation and personalization; rollout to features still in progress | [Official/press, 2026] |
| Microsoft Clarity | Copilot chat, session insights, heatmap insights, Ad Campaign Insights; AI Visibility (citations, topic insights, bot activity) | [Official, 2025 to 2026] |
| Contentsquare (Hotjar) | Sense Chat, replay and zoning summaries (Growth and above), Sense Analyst agent (introduced March 2026), connectors to ChatGPT, Claude, Copilot and IDEs with tool call limits | [Official support pages, 2026] |
| Shopify | Rollouts native theme testing; Sidekick assistant in admin | [Unverified details, 2026] |
| Kameleoon, Convert, GrowthBook, PostHog | AI-assisted test ideation, variant generation or analysis features vary | [Unverified, check vendor docs] |
| AI landing page and variant tools (for example Coframe, Unbounce Smart Traffic, Webflow Optimize) | Generate or allocate variants automatically | [Unverified, check vendor docs] |

### 4.2 Risks of AI-generated variants
- Generic copy that loses specificity (AI defaults to adjectives). Enforce the specificity test in [Offer and copy](offer-and-copy.md).
- Invented claims, numbers or testimonials. Never allowed; every claim maps to BRAND.md or data.
- Many variants inflate false positives. Use multiple comparison corrections or bandits only for short-term allocation.
- Auto-allocation (bandits, "smart traffic") optimizes short-term conversion; it may hurt AOV, lead quality or retention. Keep guardrails and a holdout.
- Brand voice drift across many pages. Use BRAND.md voice rules as a checklist.
- Accessibility regressions in generated code. Run the accessibility checklist on every diff.

### 4.3 Claude workflow for AI-assisted variants (inside a codebase)
1. Read research outputs and the copy deck. Pick one hypothesis from the backlog.
2. Write 2 to 3 variant copy sets, each tied to a VOC theme and a hypothesis.
3. Implement as a code diff behind a flag or test assignment ([Build recipes](landing-page-build-recipes.md)). Do not merge or deploy.
4. Self-QA: build passes, no layout shift, LCP not worse, accessibility checklist, tracking events present.
5. Write the test plan with sample size and duration. Append the EXPERIMENTS.md row with status "proposed".
6. Present the diff, plan and screenshots to the human for approval.

## 5. AI agents as visitors

AI agents (assistant browsing modes, agentic browsers, shopping agents) now visit, compare and sometimes buy. Adobe reported AI-referred traffic to US retail sites up 393% year over year in Q1 2026 and up 127% in August 2026 [Study, 2026]; Clarity and other tools track AI crawler activity.

CRO implications:
| Area | Action |
|------|--------|
| Content | Prices, availability, shipping, returns and specs in HTML text, not only images or scripts |
| Structure | Semantic HTML, labeled form fields, buttons as `<button>`, clear headings; this also serves accessibility |
| Consistency | Same facts on page, feed, structured data and policies (agents and assistants cross-check) |
| Experiments | Exclude bots and agents from test populations; check for SRM caused by bot filtering differences |
| Analytics | Separate AI referral and agent traffic in reporting (custom channel group) |
| Checkout | Agentic checkout protocols (for example OpenAI and Stripe's Agentic Commerce Protocol, 2025) let purchases happen off-site; coordinate with `commerce-feeds` [Unverified current scope] |

## 6. Common personalization plays (with what to measure)

| Play | Segment signal | Content change | Primary metric | Guardrail |
|------|---------------|----------------|----------------|-----------|
| Local commerce | Country or region (IP geo, Shopify Markets) | Currency, local shipping cost and delivery dates, local payment methods, local reviews | RPV by country | Margin, return rate |
| Ad angle continuity | Allowlisted URL parameter or ad naming map | Hero headline, image, proof aligned to the ad | CVR by angle | Bounce, LCP |
| Returning cart holder | First-party cookie with cart contents | Resume cart banner, reassurance on shipping and returns | Checkout starts | AOV |
| New vs returning visitor | Cookie | New: more proof and explanation; returning: shortcuts to category or account | RPV | Engagement |
| B2B industry | Reverse IP enrichment or CRM match | Industry logos, case study, use case copy | Demo requests per visitor | SQL rate |
| Named account (ABM) | Target account list match | Account-specific headline, relevant integration, AE photo | Held demos from target accounts | Page speed |
| AI referral | Referrer or utm_source from assistants | Show specs, comparisons and buy path prominently | RPV for AI segment | Bounce |

## 7. Measuring cumulative impact
- Global holdout: keep 5% to 10% of eligible visitors on the non-personalized experience for a quarter; compare RPV or qualified conversions per visitor. This is the only clean read on what the personalization program is worth.
- Per-rule holdouts: each rule keeps a 10% to 20% holdout until it has proven itself, then a smaller one.
- Retire rules that do not beat holdout after a full test period; each rule has a maintenance cost.
- Report personalization impact separately from A/B test wins to avoid double counting.

## 8. Personalization test plan template
```
Segment definition and size (weekly eligible visitors):
Evidence the segment differs (needs, objections):
Personalized experience (content per segment):
Control: generic experience | Holdout share:
Primary metric: | Guardrails:
Consent basis:
Maintenance owner and review date:
Kill criteria:
```
