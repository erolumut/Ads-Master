# Measurement and Prompt Tracking

> Knowledge as of 2026-10. AI answers vary run to run, by engine, mode, location, account and memory. Measurement must be statistical, segmented and honest about what it cannot see. Never report a single run as "our ranking in ChatGPT".

## 1. The four-layer measurement stack

| Layer | Question | Sources | Cadence |
|-------|----------|---------|---------|
| 1. Visibility | Are we mentioned, recommended and cited for the prompts that matter? | Prompt tracking tool or DIY runs | Weekly collection, monthly reporting |
| 2. First-party platform data | What do engines that report tell us? | Google Search Console Generative AI performance report; Bing Webmaster Tools AI Performance | Monthly |
| 3. Traffic and engagement | Do AI surfaces send visits, and what do they do? | GA4 AI channel group; server logs for user-fetch bots | Weekly |
| 4. Business outcomes | Does it make money? | GA4 key events by AI channel; CRM self-reported attribution; branded search trend | Monthly and quarterly |

## 2. Prompt set design

### 2.1 Prompt classes

| Class | Purpose | Example | Share of set |
|-------|---------|---------|--------------|
| Category discovery | Unbranded "best" and "top" | "best accounting software for freelancers" | 25 to 35% |
| Problem and use case | Pain-led prompts | "how do I stop late invoice payments" | 15 to 25% |
| Comparison | Head-to-head | "Acme vs Globex for agencies" | 10 to 15% |
| Alternatives | Switching intent | "cheaper alternatives to Globex" | 5 to 10% |
| Brand facts | Accuracy and sentiment | "Acme pricing", "is Acme legit" | 10 to 15% |
| Local or segment | Geo or vertical | "payroll provider for restaurants in Texas" | As relevant |
| Shopping | Product discovery | "waterproof hiking boots under $150" | Ecommerce: 30%+ |
| Informational authority | Topics where you want to be the cited source | "average SaaS churn rate 2026" | 10 to 20% |

### 2.2 Where prompts come from (in priority order)

1. Sales call notes, chat transcripts, support tickets: the exact phrasing customers use.
2. Google Search Console queries (long, question-like queries are close to prompts) and Bing grounding queries.
3. Customer interviews and surveys ("what did you ask ChatGPT before buying?").
4. People Also Ask, Reddit and forum thread titles in the category.
5. Competitor positioning (their comparison pages).
6. Tool-provided prompt volume estimates. Treat as directional: no engine publishes prompt volumes [Unverified for all vendor volume data].

### 2.3 Prompt set size by tier

| Tier | Prompts | Engines | Runs per prompt per collection | Geos and languages |
|------|---------|---------|-------------------------------|---------------------|
| Starter | 25 to 50 | 2 to 3 (ChatGPT, Google AI Mode or AIO, one more by GA4 data) | 3 | Primary market |
| Growth | 50 to 150 | 4 to 5 | 3 to 5 | Primary plus one |
| Scale | 150 to 500 | All major | 5 | Top markets |
| Enterprise | 500 to 5,000 | All major plus regional | 5 to 10 | All markets, local languages |

### 2.4 Prompt record template

| ID | Prompt | Class | Persona | Funnel stage | Geo | Language | Priority (1 to 3) | Target page | Competitors expected | Notes |
|----|--------|-------|---------|-------------|-----|----------|-------------------|-------------|----------------------|-------|
| P001 | best payroll software for a 20 person restaurant | Category | Owner-operator | Consideration | US-TX | en | 1 | /payroll-for-restaurants | Gusto, ADP | |

Rules:
1. Freeze the prompt set for at least one quarter. Changing prompts breaks trend lines. Add new prompts as a new cohort.
2. Write prompts the way buyers type them (often long and conversational), not as keywords.
3. Include persona context in some prompts ("I run a 3 location bakery") because real users do.

## 3. Collection protocol

| Setting | Recommendation | Why |
|---------|---------------|-----|
| Runs | 3 to 10 per prompt per engine per collection | Answers vary; SparkToro found under 1% chance of identical brand lists [Study, 2026] |
| Session | Fresh session per run; memory and history off; logged-out baseline plus one logged-in persona panel if budget allows | Memory and history alter answers [Official for memory; effect size Unverified] |
| Mode | Record model and mode (free, paid, think, search on) | Retrieval paths differ by tier (ChatGPT free vs paid) [Study, 2026] |
| Location | Fixed geo per market (tool proxy or VPN) | Local results change by location |
| Timing | Same weekday window each week | Reduces drift noise |
| Interface vs API | Prefer interface-based collection for consumer engines. API answers with web search tools are a proxy, not the consumer product | Different models, tools and defaults [Practitioner consensus] |
| Storage | Keep full answer text and cited URLs, not only flags | Enables re-scoring and source mapping |

## 4. Metric definitions and formulas

| Metric | Formula | Notes |
|--------|---------|-------|
| Mention rate (visibility) | runs where brand is mentioned / total runs | Per engine, per prompt class; the primary KPI |
| Recommendation rate | runs where the brand is presented as a recommended option / total runs | Stricter than mention; for "best" prompts |
| Top-3 rate | runs where the brand is among the first 3 brands named / runs where any brand is named | Position is noisy; report as a rate, never as a rank |
| Citation rate | runs where at least one owned URL is cited / total runs | Owned domain only |
| Citation share | citations to owned domains / all citations in tracked answers | Compare to competitors' owned domains |
| Share of voice (mentions) | brand mentions / sum of mentions of all tracked brands | Define the competitor set and keep it fixed |
| Sentiment score | (positive mentions minus negative mentions) / total mentions | Use a rubric (section 6); spot-check model scoring |
| Accuracy rate | correct facts stated / facts stated about the brand | Against the brand fact sheet |
| Source presence | priority cited domains where the brand appears / priority cited domains | From the source map |
| AI referral sessions | GA4 sessions in the AI channel | Undercounted (app traffic, copy-paste) |
| AI-assisted conversions | key events with AI channel as session source; plus CRM self-reported | Report both |

## 5. Statistics: when is a change real?

AI answers are samples. Report intervals.

1. 95% interval for a rate p over n independent runs: p plus or minus 1.96 x sqrt(p x (1 minus p) / n).
2. Runs of the same prompt are correlated. Compute intervals by bootstrapping over prompts (resample prompts, not runs).
3. Rule of thumb for detectable change (two periods, 95%): with 200 runs per period at p around 0.3, the interval half-width is about 6 points, so changes under about 9 points are noise.
4. Minimum before claiming a win: at least 2 consecutive collections in the same direction and a change larger than the interval.

Bootstrap script for a tracking export (CSV with columns: period, prompt_id, engine, run_id, mentioned as 0 or 1):

```python
import csv, random, sys
from collections import defaultdict

def load(path):
    rows = list(csv.DictReader(open(path, newline="")))
    data = defaultdict(lambda: defaultdict(list))  # (period, engine) -> prompt -> [0/1]
    for r in rows:
        data[(r["period"], r["engine"])][r["prompt_id"]].append(int(r["mentioned"]))
    return data

def rate(prompts):
    runs = [x for v in prompts.values() for x in v]
    return sum(runs) / len(runs) if runs else 0.0

def bootstrap(prompts, iters=2000, seed=7):
    random.seed(seed)
    keys = list(prompts)
    stats = []
    for _ in range(iters):
        sample = [random.choice(keys) for _ in keys]
        runs = [x for k in sample for x in prompts[k]]
        stats.append(sum(runs) / len(runs))
    stats.sort()
    return stats[int(0.025 * iters)], stats[int(0.975 * iters)]

if __name__ == "__main__":
    data = load(sys.argv[1])
    for (period, engine), prompts in sorted(data.items()):
        lo, hi = bootstrap(prompts)
        print(f"{period}\t{engine}\tmention_rate={rate(prompts):.3f}\t95% CI=({lo:.3f}, {hi:.3f})\tprompts={len(prompts)}")
```

Run it with `python3 -I bootstrap_mentions.py ads-master/data/imports/<export>.csv`. Overlapping intervals between periods mean "no proven change".

## 6. Sentiment and accuracy rubric

| Score | Sentiment definition | Example |
|-------|---------------------|---------|
| +1 | Recommended, positive qualifiers, no caveats or minor ones | "Acme is a strong choice for small restaurants because..." |
| 0 | Neutral listing or mixed | "Acme and Globex both offer..." |
| minus 1 | Negative qualifiers, warnings, complaints cited | "Users report slow support..." |

Accuracy: list the facts stated about the brand in each sampled answer. Mark each correct, outdated or wrong against the fact sheet. Any wrong fact on pricing, safety, legal status or availability opens a correction ticket (see [Entity](entity-and-brand-authority.md) section 8).

## 7. Google Search Console: Generative AI performance report

Facts [Official, 2026-06 to 2026-08; re-checked 2026-10-08]:
1. Launched 2026-06-03 (UK subset first); beyond the UK from July; available to all sites worldwide as of 2026-08-31 (help page note).
2. Shows impressions from AI Overviews and AI Mode combined, by page (final URL after redirects), country and date; some guides also show a device split. There is no filter that separates AI Mode from AI Overviews as of 2026-10; a single blog's claim of a 2026-09-07 change could not be confirmed. Discover has its own generative AI report.
3. No clicks, no CTR, no position, no query text. Search Labs experiments excluded.
4. Data starts 2026-05-18. No backfill.
5. A search type selector covers Web: text-based and Web: multimodal (image-based) searches.
6. These impressions are already included in Web search type totals. Do not add them to Web totals.
7. Large sites hit the 1,000-row export limit; filter by country or URL path.
8. Not available in the Search Console API (no generative AI search type or search appearance value) or in the BigQuery bulk export as of 2026-10; UI and CSV export only [Official API docs; third-party checks 2026-08 and 2026-10].

How to use it:
1. Monthly: export page-level AI impressions. Rank pages by AI impressions and by AI share (AI impressions / Web impressions for the same page, both filtered to Web search type).
2. Pages with high AI impressions but falling clicks in the Web report: candidates for answer-first rewrites that earn the click (deeper data, tools, calculators, downloadable assets).
3. Pages with zero AI impressions in topics where AI features trigger: check snippet eligibility and content structure.
4. Annotate model and feature changes (Gemini updates, AI Overview expansions) in the report log.

## 8. Bing Webmaster Tools: AI Performance

Facts [Official, 2026-02, 2026-03 and 2026-06; re-checked 2026-10-08]:
1. Public preview since 2026-02-10 at bing.com/webmasters/aiperformance. Covers Copilot, Bing AI summaries and select partners.
2. Metrics: total citations, average cited pages (daily unique URLs cited), page-level citation activity, grounding queries (phrases the AI used to retrieve content).
3. 2026-03-23: grounding query to page mapping (select a query to see cited pages, or a page to see its grounding queries), worldwide for verified sites. 2026-06-16 additions in preview: Intents (for example Learn and Solve, Research, Comparison, Planning), Topics, Citation Share and Compare. No further features found between 2026-06-16 and 2026-10-08.
4. Sampled data, no clicks, no public API (Microsoft said API access would come during 2026; not shipped as of 2026-09), CSV export only, preview status. Does not cover ChatGPT, Claude or Perplexity.

How to use it:
1. Export grounding queries monthly. They are a real fan-out log. Map each to an owned passage; gaps become content briefs.
2. Track citation share by topic against competitors (Compare) where available.
3. Pages cited by Copilot but thin on facts are quick wins.

## 9. GA4 setup for AI referral traffic

Ownership: the GA4 configuration itself belongs to `measurement`. This agent specifies the requirement and checks it.

### 9.1 Custom channel group

1. Admin > Data display > Channel groups > Create new channel group (copy of Default).
2. Add channel "AI Assistants" with condition: Session source matches regex:

```
.*(chatgpt\.com|chat\.openai\.com|openai\.com|perplexity\.ai|gemini\.google\.com|bard\.google\.com|copilot\.microsoft\.com|copilot\.cloud\.microsoft|claude\.ai|meta\.ai|grok\.com|chat\.deepseek\.com|chat\.mistral\.ai|you\.com|poe\.com|phind\.com).*
```

3. Move "AI Assistants" above "Referral" (channel rules evaluate top to bottom).
4. Verify the actual source values in Reports > Acquisition > Traffic acquisition with Session source filtered by a broad regex (gpt|openai|perplexity|gemini|copilot|claude|grok|deepseek|mistral) and update the regex with any new values.
5. Custom channel groups are applied to historical data as well, so trend comparisons work immediately [Official, GA4 help; verify current behavior]. Optionally set the new group as the primary channel group so standard reports use it.

### 9.2 Known attribution gaps

| Source | How it appears | Notes |
|--------|---------------|-------|
| ChatGPT web | chatgpt.com referral; ChatGPT appends utm_source=chatgpt.com to referral links [Official] (OpenAI Publishers and Developers FAQ). Since 2026-05-07 more prominent inline brand links send about 60% of ChatGPT referrals to homepages [Study, 2026-05] | Mobile and desktop apps may strip referrers (Direct); citation links with the UTM but no medium can land in Unassigned |
| Google AI Overviews and AI Mode | google / organic, inseparable from classic organic | Use the Search Console Generative AI report for impressions |
| Gemini app | gemini.google.com when a referrer passes | App traffic often direct |
| Copilot | copilot.microsoft.com or bing.com variants | Check actual values |
| Perplexity | perplexity.ai | Comet browser traffic may differ [Unverified] |
| Claude | claude.ai | Desktop app traffic may be direct |
| Agent browsers (Atlas, Comet) | May appear as normal browser sessions | [Unverified] |
| Copy-paste of brand name into Google | Branded organic or direct | Invisible AI influence: track branded search trend |

### 9.3 Complementary signals

1. Self-reported attribution: add "ChatGPT or another AI assistant" as an option in "How did you hear about us?" on forms and checkout, plus a free-text field. Hand off to `cro` and `measurement`.
2. Branded search volume trend (Search Console brand queries, Google Trends) as a downstream indicator.
3. User-fetch bot hits from logs (ChatGPT-User, Claude-User, Perplexity-User) by URL as a demand proxy.
4. Landing page mix: since 2026-05-07 more ChatGPT referrals land on homepages [Study, 2026-05]. Check homepage conversion paths for AI visitors.

## 10. Tools (summary; details in [Tools](tools-api-mcp.md))

Ask every vendor: engines and modes covered, interface vs API collection, logged-in or logged-out, runs per prompt, geo method, refresh frequency, how mentions and sentiment are parsed, data export and API, prompt volume methodology. Prefer tools that export raw answers and cited URLs.

## 11. Monthly AI visibility report template

Save as `ads-master/outputs/ai-search-optimization/YYYY-MM-DD_ai-search-optimization_monthly-report.md`.

```
# AI Visibility Report: <Month YYYY>
Data used: <tool export file, date range>, GSC Generative AI report (<range>), Bing AI Performance (<range>), GA4 (<range>)

## Headline (3 bullets, each with number, interval and source)

## Visibility by engine
| Engine | Mention rate (95% CI) | Prev month | Citation share | SoV | Sentiment | Runs |

## By prompt class
| Class | Mention rate | Change | Top competitor | Notes |

## Accuracy
| Issue | Engine | Severity | Source traced | Status |

## First-party data
GSC AI impressions by top pages; Bing citations, cited pages, top grounding queries

## Traffic and outcomes
AI channel sessions, engaged sessions, key events, conversion rate vs organic; self-reported AI mentions

## What we did last month and observed effect (with lag caveats)

## Next month: top 5 actions (impact x confidence x ease), approvals needed

## Handoffs requested
```

## 12. Common measurement mistakes

1. Reporting one run or a screenshot as a ranking.
2. Changing the prompt set every month.
3. Mixing logged-in personal accounts with tracking runs.
4. Comparing vendor A's "visibility score" with vendor B's.
5. Treating vendor prompt volumes as search volumes.
6. Adding Generative AI impressions on top of Web impressions.
7. Ignoring dark AI traffic and concluding "AI sends nothing".
8. Claiming causation from a content change when a model update happened the same week.
