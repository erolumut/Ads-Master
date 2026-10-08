# Tools, APIs and MCP Servers

> Knowledge as of 2026-10. Tool features and pricing change monthly; verify on the vendor's site before recommending. Do not quote prices from memory. The agent uses whatever connectors the user has installed and states which data source and date range it used.

## 1. Data access hierarchy (prefer the top)

1. First-party platform data: Google Search Console, Bing Webmaster Tools, GA4, server or CDN logs.
2. Prompt tracking tool exports or APIs (raw answers and cited URLs).
3. DIY collection via LLM APIs (a proxy for consumer products, label it as such).
4. Manual runs in consumer interfaces (screenshots plus text, small samples).

## 2. First-party tools

| Tool | What it gives for AI visibility | Access for Claude | Limits |
|------|--------------------------------|-------------------|--------|
| Google Search Console | Generative AI performance report (AIO and AI Mode impressions by page, country, device, date; since 2026-05-18); Search generative AI control; Web performance; URL Inspection | Search Console API covers Web performance; availability of the Generative AI report in the API is not confirmed [Unverified]. Community MCP servers for Search Console exist [Unverified quality] | No clicks or queries for AI; combined AIO and AI Mode |
| Bing Webmaster Tools | AI Performance: citations, cited pages, grounding queries, intents, topics, citation share, compare (preview) | Bing Webmaster API exists for classic data; AI Performance has no public API as of 2026-06 [Official] | Sampled; preview; Microsoft surfaces only |
| GA4 | AI channel group sessions, engagement, key events | GA4 Data API; Google released an official experimental Google Analytics MCP server in 2025 [Official, 2025; verify current status] | Dark AI traffic; AI Overviews inseparable from organic |
| Server and CDN logs | Bot access, status codes, user-fetch hits by URL | File export to `ads-master/data/imports/`; Cloudflare dashboard and API | Requires access; spoofed UAs |
| Cloudflare AI Crawl Control | Per-crawler requests, allow or block, robots.txt compliance, pay per crawl | Dashboard; Cloudflare API | Cloudflare sites only |

## 3. Prompt tracking and AI visibility platforms

Capabilities differ and change fast. Use the evaluation checklist in section 4. Listed alphabetically; inclusion is not endorsement.

| Tool | Positioning (as publicly described) | Notes |
|------|-----------------------------------|-------|
| Ahrefs Brand Radar | Brand mentions across AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini, Copilot plus web mentions | Large prompt database; good for competitor mention benchmarks. Ahrefs offers an official MCP server [Official, 2025] |
| AthenaHQ | AI visibility tracking and recommendations | Verify engines covered |
| BrightEdge (AI Catalyst and related) | Enterprise SEO suite with AI search tracking | Enterprise focus |
| Conductor | Enterprise SEO and AEO tracking | Enterprise focus |
| Evertune | Brand perception in LLMs at scale | Brand and marketing teams |
| Goodie | AI visibility platform | Publishes referral share research |
| Gumshoe | Persona-based AI visibility tracking | Co-authored the SparkToro variance study |
| LLMrefs, Rankscale, Trakkr and similar | Lower-cost trackers | Check collection method |
| Otterly.AI | Prompt monitoring across major engines | Publishes citation research; check runs per prompt |
| Peec AI | Prompt tracking with source analysis | Published the ChatGPT index analysis (2026) |
| Profound | Enterprise AI visibility, citation and conversation analytics, crawler analytics | Large citation datasets; enterprise pricing |
| Scrunch AI | AI visibility plus agent-facing site experience | Check current features |
| Semrush (AI Toolkit, AI visibility features, Enterprise AIO) | AI visibility tracking inside the Semrush suite | Semrush offers an official MCP server [Official, 2025]. Adobe announced an agreement to acquire Semrush in 2025-11 [Official, 2025-11; verify closing] |
| seoClarity | Enterprise SEO with AI tracking | Enterprise focus |
| Similarweb (AI traffic and brand visibility) | AI referral traffic benchmarks and brand visibility | Panel-based traffic estimates |
| Yext (Scout) | Local and brand visibility in AI | Strong for multi-location |
| Yoast AI Brand Insights | Brand visibility tracking; added Claude tracking 2026-05-28 [Official vendor, 2026-05] | WordPress ecosystem |

## 4. Tool evaluation checklist (ask every vendor, record answers)

| Question | Why it matters |
|----------|---------------|
| Which engines and modes (free, paid, AI Mode, AIO, shopping)? | Retrieval differs by mode |
| Interface scraping or API? Logged-in or logged-out? | API answers differ from consumer products |
| Runs per prompt and refresh frequency? | Variance requires repeated sampling |
| Geo method (proxy location, stated location)? | Local and market differences |
| Are raw answers and cited URLs exportable? | Enables source mapping and re-scoring |
| How are brand mentions detected (aliases, product names, misspellings)? | False negatives and positives |
| How is sentiment scored and can it be audited? | Model-scored sentiment drifts |
| Prompt volume method? | Usually modeled; directional only |
| API or MCP access? | Automation and Claude access |
| Data retention and history? | Trend analysis |
| Price per prompt per engine at your scale? | Budget fit |

Selection rule: the cheapest tool that covers the project's top engines with exportable raw data and enough runs beats a feature-rich tool that hides its method.

## 5. MCP servers and connectors

| Server | Use | Status |
|--------|-----|--------|
| Ahrefs MCP | Keyword, backlink, Brand Radar style data inside Claude | Official [Official, 2025; verify endpoints] |
| Semrush MCP | Keyword, domain and AI visibility data | Official [Official, 2025; verify] |
| DataForSEO MCP | SERP data including AI Overview elements, LLM response and mention APIs | Official [Official, 2025; verify product names] |
| Google Analytics MCP | GA4 reporting queries | Official experimental [Official, 2025; verify] |
| Search Console MCP | GSC performance queries | Community projects [Unverified quality; review code before use] |
| Bing Webmaster Tools MCP | Classic Bing data | Community [Unverified] |
| Cloudflare MCP servers | Account and analytics access | Official Cloudflare MCP servers exist [Official, 2025; verify scope] |
| Profound, Peec AI, other trackers | Tracking data | Some vendors offer APIs or MCP; check [Unverified] |

Security rules for MCP use:
1. Prefer official servers. Review community server code before installing.
2. Use read-only scopes for analysis. Any write action (robots.txt, CDN, CMS) requires human approval and is never automated by this agent.
3. Never paste API keys into deliverables or journal entries.

## 6. DIY collection with LLM APIs (proxy measurement)

Use when no tracking tool is available. Label results "API proxy" in every report.

| API | Search grounding feature | Caveat |
|-----|------------------------|--------|
| OpenAI Responses API | Web search tool | Not identical to ChatGPT consumer search; model and index path may differ |
| Google Gemini API | Grounding with Google Search | Not identical to AI Mode or AI Overviews |
| Perplexity Sonar API | Built-in search with citations | Close to Perplexity product but not identical |
| Anthropic Messages API | Web search tool | Not identical to Claude apps |
| Azure AI Agents | Grounding with Bing Search (replaced Bing Search APIs in 2025-08) | Proxy for Copilot-like grounding |
| DataForSEO and similar | Scraped AI Overview and AI Mode results; LLM response APIs | Third-party collection |

Skeleton (pseudocode, adapt to current SDKs and model names from vendor docs):

```python
# For each prompt, engine and run: call the API with search enabled,
# store answer text and cited URLs, then detect brand mentions.
import csv, datetime, re

BRANDS = {"Acme": [r"\bacme\b"], "Globex": [r"\bglobex\b"]}

def detect(text):
    return {b: int(any(re.search(p, text, re.I) for p in pats)) for b, pats in BRANDS.items()}

def run_engine(engine, prompt):
    # Call the vendor SDK here with its web search tool enabled.
    # Return (answer_text, [cited_urls]). Record model id and settings.
    raise NotImplementedError

rows = []
for prompt_id, prompt in [("P001", "best payroll software for a 20 person restaurant")]:
    for engine in ["openai_web_search", "gemini_grounding", "perplexity_sonar"]:
        for run in range(5):
            text, urls = run_engine(engine, prompt)
            hits = detect(text)
            rows.append({"date": datetime.date.today().isoformat(), "prompt_id": prompt_id,
                         "engine": engine, "run_id": run, "mentioned": hits["Acme"],
                         "citations": "|".join(urls)})

with open("ai_tracking_export.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
```

Feed the CSV (with a `period` column added) to the bootstrap script in [Measurement](measurement-and-prompt-tracking.md).

Cost control: estimate calls = prompts x engines x runs per collection x collections per month. Start with the Starter tier sizes.

## 7. Technical tools

| Tool | Use |
|------|-----|
| curl, wget | Raw HTML and status checks with custom user agents |
| Screaming Frog SEO Spider | Crawl with custom user agents; compare text-only vs JavaScript rendering; extract schema |
| Google Rich Results Test, Schema Markup Validator | Structured data validation |
| GSC URL Inspection, Bing URL Inspection | Rendered HTML as Google and Bing see it |
| Log analyzers (GoAccess, Screaming Frog Log File Analyser, Botify, Oncrawl, Lumar) | Bot hits and status codes at scale |
| Cloudflare Radar bot directory | Bot classification and verification details |
| robots.txt testers | Validate group matching per token |

## 8. Manual collection protocol (when nothing else exists)

1. Use a clean browser profile, logged out, location fixed.
2. For logged-in checks, use a dedicated account with memory off and no history.
3. Paste the prompt exactly; record date, time, engine, mode, model shown.
4. Save the full answer text and every cited URL into a CSV row.
5. Repeat 3 times per prompt in separate sessions.
6. Never use the client's personal or employee accounts (personalized answers).
