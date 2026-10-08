# Conversion Research Methods

> Purpose: find the real reasons visitors do not convert before proposing any change. A test built on research wins more often than a test built on opinion. Optimizely reports that well designed experiments win far more often than poorly designed ones in its 2026 analysis of 173k experiments [Study, 2026] (definitions vary, see [Experimentation statistics](experimentation-statistics.md)).

## 1. The research stack (ResearchXL, adapted)

ResearchXL is the CXL research model (Peep Laja). Six streams, each answering a different question. Use at least three streams before any test, and require two independent streams to agree before calling something an insight.

| Stream | Question it answers | Primary tools | Minimum effort |
|--------|--------------------|---------------|----------------|
| Technical analysis | Is something broken for some devices or browsers? | GA4 Tech reports, BrowserStack or real devices, Clarity JS errors | 2 hours |
| Heuristic analysis | Where does the page violate known persuasion and usability principles? | LIFT model, [Audit checklist](audit-checklist.md) | 3 hours per template |
| Digital analytics | Where do people leave and which segments underperform? | GA4 funnel exploration, Shopify funnel, BigQuery | 4 hours |
| Behavior analytics | What do people do on the page? | Microsoft Clarity, Contentsquare (Hotjar), PostHog replay | 3 hours (50 to 100 recordings) |
| Qualitative surveys | Why do people hesitate, and in whose words? | On-site polls, post-purchase survey, customer survey | 1 to 2 weeks of collection |
| User testing | Can a first-time visitor understand and complete the task? | UserTesting, Lyssna, Maze, moderated calls | 5 users per round per segment |

Add two streams that matter for paid traffic:
- Ad to page scent review: see [Message match by channel](message-match-by-channel.md).
- Voice of customer mining from reviews, tickets, sales calls and communities (section 7).

## 2. Research sprint by traffic tier

| Tier | Monthly sessions to the funnel | Sprint length | Streams to run |
|------|-------------------------------|---------------|----------------|
| Starter | under 10k | 5 working days | Technical, heuristic, analytics, 30 recordings, post-purchase or post-signup survey, 5 user tests |
| Growth | 10k to 100k | 10 working days | All six streams, 100 recordings, on-site poll plus customer survey |
| Scale | 100k to 1M | 10 working days, then continuous | All six plus segment deep dives (device, source, new vs returning), monthly survey refresh |
| Enterprise | over 1M | Continuous research ops | All six, quarterly interviews per segment, research repository, dedicated analyst |

## 3. Digital analytics: find the leak

### 3.1 GA4 funnel exploration (UI path)
1. Explore > Funnel exploration > new.
2. Steps (ecommerce): `session_start` > `view_item` > `add_to_cart` > `begin_checkout` > `add_shipping_info` > `add_payment_info` > `purchase`.
3. Steps (lead gen): landing page view (page_location contains the LP path) > `form_start` > `form_submit` or `generate_lead`.
4. Toggle "Make open funnel" off for a closed funnel first (users must enter at step 1).
5. Breakdown: Device category. Then Session default channel group. Then Landing page + query string.
6. Turn on "Show elapsed time" to see where people stall.
7. Right click a step > "View users" or create a segment of drop-offs for remarketing analysis.

`form_start` and `form_submit` are GA4 enhanced measurement events. They miss multi-step, iframe and JavaScript-rendered forms often. Verify in DebugView before trusting them [Official, Google Analytics Help].

### 3.2 Segment table to build every time

| Segment | Why | Red flag |
|---------|-----|----------|
| Device (mobile, desktop, tablet) | Mobile usually converts lower; a gap over 3x needs investigation | Mobile CVR under one third of desktop on same traffic source |
| Browser and OS | Finds broken flows | One browser converts under 50% of the median browser |
| Channel and campaign | Message match problems | Paid social CVR far below paid search is normal; a drop vs its own history is not |
| Landing page | Template problems | High traffic page with bounce over 70% and CVR under half the site average |
| New vs returning | Trust and clarity problems hit new users | New user CVR under 25% of returning |
| Country or language | Localization, payment methods, shipping | Country with traffic but near zero orders |
| AI referral (chatgpt.com, perplexity.ai, copilot, gemini, claude.ai) | New, high intent segment | Lands on pages with no clear path to buy |

GA4 custom channel group for AI assistants (Admin > Data display > Channel groups > Create new). Condition: Source matches regex:

```
^(chatgpt\.com|chat\.openai\.com|perplexity\.ai|www\.perplexity\.ai|copilot\.microsoft\.com|gemini\.google\.com|claude\.ai|chat\.mistral\.ai|meta\.ai)$|utm_source=chatgpt\.com
```
Place it above "Referral" in the channel order. Coordinate with the `measurement` agent before changing channel groups.

### 3.3 Revenue impact of a leak (use to rank problems)
```
Monthly value of fixing a step = sessions reaching step x (target step rate - current step rate) x downstream conversion to purchase x AOV
```
Worked example: 40,000 monthly sessions reach the cart. Cart to checkout is 38%; the store's own mobile best month was 45%. Checkout to purchase is 55%, AOV $82.
Value = 40,000 x 0.07 x 0.55 x 82 = $126,280 per month at full recovery. Use 30% of that (winner's curse and partial recovery) for planning: about $38k per month.

### 3.4 BigQuery funnel by device (GA4 export)
```sql
-- Replace project.dataset and dates. Counts users reaching each step by device.
WITH ev AS (
  SELECT user_pseudo_id, device.category AS device, event_name
  FROM `project.analytics_123456.events_*`
  WHERE _TABLE_SUFFIX BETWEEN '20260701' AND '20260930'
    AND event_name IN ('view_item','add_to_cart','begin_checkout','add_payment_info','purchase')
)
SELECT device,
  COUNT(DISTINCT IF(event_name='view_item', user_pseudo_id, NULL)) AS view_item,
  COUNT(DISTINCT IF(event_name='add_to_cart', user_pseudo_id, NULL)) AS add_to_cart,
  COUNT(DISTINCT IF(event_name='begin_checkout', user_pseudo_id, NULL)) AS begin_checkout,
  COUNT(DISTINCT IF(event_name='add_payment_info', user_pseudo_id, NULL)) AS add_payment_info,
  COUNT(DISTINCT IF(event_name='purchase', user_pseudo_id, NULL)) AS purchase
FROM ev GROUP BY device ORDER BY view_item DESC;
```
This is an open funnel (users counted at each step regardless of order). Use it to compare devices, not to report a precise step rate.

### 3.5 Shopify
Analytics > Reports > "Conversion rate breakdown" or the Conversion funnel on the Analytics dashboard: sessions > added to cart > reached checkout > completed checkout. Compare against the store's own prior 90 days, then against benchmarks.

## 4. Behavior analytics (recordings and heatmaps)

### 4.1 Microsoft Clarity setup checks
- Free. Install via script, GTM or native integrations (Shopify, WordPress). Connect to GA4 in Settings > Setup to pass Clarity session links into GA4 [Official, Microsoft Learn].
- Masking: confirm that form inputs with personal data are masked (Settings > Masking). Strict mode for health, finance and any regulated category.
- Consent: in the EEA, UK and Switzerland, load Clarity only after consent through your CMP, or use its consent signal API. Coordinate with the `measurement` agent.

### 4.2 Clarity signals to filter on
| Signal | Meaning | First check |
|--------|---------|-------------|
| Rage clicks | Repeated clicks in one spot | Unresponsive element, slow INP, element that looks clickable but is not |
| Dead clicks | Clicks with no effect | Images, headings, icons that look like links; disabled buttons with no message |
| Excessive scrolling | Scanning without finding | Missing information, poor scannability |
| Quick backs | Left and returned fast | Mismatched link, wrong page from nav or ad |
| JavaScript errors | Script errors during session | Checkout or form broken for a browser |

### 4.3 Clarity Copilot (AI) features
| Feature | What it does | Use it for | Caveat |
|---------|-------------|-----------|--------|
| Copilot chat | Answers questions about dashboard data in natural language | Quick segment questions | Verify numbers in the dashboard |
| Session insights | Summarizes a set of recordings into takeaways | Triage 100 recordings fast, then watch the 10 it flags | Can miss rare but critical bugs |
| Heatmap insights | Summarizes heatmaps across devices | First pass on a template | Does not know your business goal |
| Ad Campaign Insights | Combines campaign metrics with behavior data | Spot campaign landing pages with poor engagement | Depends on UTM hygiene |
| AI Visibility (Citations, Topic Insights, Bot Activity) | Shows AI assistant citations and AI crawler activity | Hand to `ai-search-optimization`; for CRO, find pages that receive AI referrals | Citations count references, not rank or prominence; bot activity does not prove citation |

Clarity AI Visibility citations became generally available around May 2026 and content recommendations were added in June 2026 [Unverified exact dates, secondary sources]. Microsoft warns that generative AI output can be wrong [Official].

### 4.4 Contentsquare (Hotjar)
Hotjar merged into Contentsquare on 1 July 2025; Hotjar pricing now lives on Contentsquare pricing with separate Experience Analytics, Voice of Customer and Product Analytics lines [Study/secondary, 2026]. Sense AI: Sense Chat and replay and zoning summaries on Growth, Pro and Enterprise; Sense Analyst (agent) introduced March 2026 [Official, Contentsquare support 2026]. Confirm plan limits before relying on replay sampling.

### 4.5 Recording review protocol
1. Define the question first ("Why do mobile users abandon at shipping?").
2. Filter: device, entry page, exit page, frustration signal, converted vs not converted.
3. Watch 30 non-converters and 10 converters per question. Converters show the happy path; the gap is the insight.
4. Tag each session in a sheet: `session_url | device | source | step reached | issue tag | timestamp | severity 1 to 3`.
5. Count issue tags. An issue in 3 or more of 30 sessions is worth a hypothesis.
6. Never present a single recording as evidence. Present a count and two example links.

### 4.6 Heatmap rules
- Scroll maps: if under 50% of mobile users reach the section with the offer or proof, move it up or shorten the page above it.
- Click maps: clicks on non-links signal expected affordances (make them links or remove the look).
- Do not compare heatmaps across pages with different traffic mixes.
- Minimum 2,000 pageviews per device for a stable heatmap [Practitioner consensus].

## 5. Surveys

### 5.1 On-site polls (one question, contextual)
| Page | Trigger | Question |
|------|---------|----------|
| PDP or pricing | 30 s on page or 50% scroll | "Is there anything stopping you from buying today?" (open) |
| Cart | Exit intent (desktop) or back button pattern (mobile) | "What made you hesitate to check out?" |
| Lead form page | Exit intent | "What information is missing for you to request a quote?" |
| Any LP from paid | 15 s | "What brought you here today?" (tests ad scent) |
| Checkout | Avoid on-page polls. Use post-purchase survey instead. | |

### 5.2 Post-purchase or post-signup survey (thank you page or email within 24 h)
1. "What almost stopped you from buying from us today?" (the most valuable CRO question)
2. "Which other options did you consider before choosing us?"
3. "How did you first hear about us?" (attribution input, share with `measurement`)
4. "What is the main problem you hoped this would solve?"
5. "How would you describe us to a friend?" (copy language)

On Shopify, post-purchase surveys run as Thank you page app blocks after the 2025 to 2026 checkout extensibility migration (see [Ecommerce](ecommerce-pdp-cart-checkout.md)).

### 5.3 Sample and coding
- Target 100 to 200 open responses per question before coding themes [Practitioner consensus].
- Code each response into one primary theme. Report theme frequency and 3 verbatim quotes per theme.
- Re-run the post-purchase survey every quarter; compare theme shares over time.

## 6. User testing

- Five users per round per segment finds most usability problems for a single task (Nielsen, 2000) [Study, 2000]. Run more rounds, not bigger rounds.
- Recruit people who match AUDIENCE.md, never staff or friends.
- Tasks are scenarios, not instructions: "You need X for Y. Find the right option and get to the point of paying." Never say button names.
- Add a five-second test for the hero: show the first screen for 5 seconds, ask "What does this company offer, and who is it for?" Pass if 4 of 5 answer correctly.
- Moderated sessions for B2B and complex offers; unmoderated for ecommerce flows.

## 7. Voice of customer mining

| Source | What to extract | How |
|--------|-----------------|-----|
| Own reviews (1 to 3 star and 5 star) | Objections, outcomes, exact phrases | Export reviews; tag pain, outcome, objection, feature |
| Competitor reviews | Unmet needs, switching triggers | Amazon, Trustpilot, G2, Capterra, app stores |
| Support tickets and live chat | Pre-purchase questions | Filter tickets before first order |
| Sales calls (Gong, Fathom, notes) | Objections, decision criteria | Search for "price", "worried", "competitor", "how long" |
| Reddit and communities | Unfiltered language, alternatives | Search "<category> recommendations", "<brand> vs" |
| AI assistants | How assistants describe you and competitors | Ask the same buyer question in ChatGPT, Perplexity, Gemini; record claims |

VOC sheet columns: `source | date | segment | quote (verbatim) | theme | type (pain, outcome, objection, trigger, alternative) | strength 1 to 3`.

Claude prompt for coding VOC (paste batches of 50):
```
You are coding customer verbatims for conversion research. For each quote output:
quote_id | type (pain, desired outcome, objection, trigger, alternative, feature) | theme (2 to 4 words) | exact phrase worth reusing in copy (verbatim, max 12 words).
Do not paraphrase phrases. Do not invent quotes. Then list the top 8 themes with counts.
```

## 8. Customer interviews (jobs to be done)

- 5 to 8 interviews per segment, recent buyers (last 60 days) and recent churners or lost deals.
- Timeline structure: first thought > passive looking > active looking > deciding > first use.
- Questions: "What was going on in your life or business when you started looking?", "What else did you try?", "What almost made you not buy?", "What did you expect to happen after buying?"
- Record, transcribe, and code with the VOC prompt above.

## 9. Heuristic frameworks

### 9.1 LIFT model (WiderFunnel, Chris Goward)
Value proposition is the engine. Five factors move it: Relevance (+), Clarity (+), Urgency (+), Anxiety (-), Distraction (-). Score each 1 to 5 per page and write one sentence of evidence per factor.

### 9.2 MECLABS conversion heuristic [Practitioner]
`C = 4m + 3v + 2(i - f) - 2a`: motivation of the user, clarity of the value proposition, incentive, friction, anxiety. The coefficients are relative weights, not math. Use it to remind stakeholders that motivation (traffic quality) and value clarity beat button colors.

### 9.3 Fast heuristic pass (per page, 15 minutes)
1. Relevance: does the first screen match the ad or query that sent the traffic?
2. Clarity: can you state what it is, who it is for and why it is better in 5 seconds?
3. Value: is there a concrete, specific benefit and proof?
4. Friction: count fields, steps, required decisions, surprises.
5. Anxiety: are price, delivery, returns, contract terms and security answered before the ask?
6. Distraction: count exits and competing CTAs on the page.

## 10. From evidence to hypothesis

Insight grid (one row per finding):

| ID | Observation | Evidence (min 2 streams) | Segment | Root cause hypothesis | Proposed change | Metric | Priority score |
|----|------------|--------------------------|---------|----------------------|-----------------|--------|----------------|

Hypothesis format (matches EXPERIMENTS.md): "If we [change], then [primary metric] will [direction and size] for [segment], because [evidence]."

Triage each finding:
- Bug or clear usability defect with no downside: fix now ("just do it"), measure before and after.
- Uncertain or risky change with enough traffic: A/B test.
- Uncertain change without enough traffic: research more or ship with guardrails (see [Experimentation statistics](experimentation-statistics.md) section on low traffic).

## 11. Research report template
Save as `ads-master/outputs/cro/YYYY-MM-DD_cro_research-report.md`.
```
# Conversion research report: <site or funnel>
Date range of data: | Data sources used (with export dates):
## Executive summary (5 bullets, each with revenue at stake)
## Funnel and segment findings (tables)
## Behavior findings (counts, example recordings)
## Survey and VOC findings (themes, counts, verbatims)
## User testing findings (task success, quotes)
## Insight grid
## Recommended actions: just do it | test backlog | research next
## Open questions and data gaps
```
