# Tools, APIs and MCP Servers for CRO

> Prefer connectors that let Claude read data directly (MCP servers, APIs). Fall back to CSV exports in `ads-master/data/imports/`. Always state which data source and date range a finding uses. Use read-only scopes. Store tokens in environment variables, never in files under `ads-master/`.

## 1. Market state (as of 2026-10; verify before recommending a purchase)

| Event | Date | What it means |
|-------|------|---------------|
| Google Optimize sunset | 30 Sept 2023 | Teams moved to GA4-integrated third-party tools |
| Hotjar merged into Contentsquare Group | 1 July 2025 | Hotjar pricing now on Contentsquare plans (Experience Analytics, Voice of Customer, Product Analytics lines); Sense AI features by plan [secondary sources, 2026] |
| OpenAI acquired Statsig ($1.1B, stock) | Announced 2 Sept 2025 | Founder became OpenAI CTO of Applications [Study/press, 2025-09] |
| Amplitude took over Statsig brand, platform and customers | 5 May 2026 | Engineering team stayed at OpenAI; Amplitude frames it as a strategic partnership; check roadmap and renewal terms [press, 2026-05] |
| VWO and AB Tasty agreed to combine | 20 Jan 2026 | Everstone-backed; over $100M ARR, 4,000+ customers claimed [press, 2026-01] |
| Combined company rebranded Wingify | 16 Sept 2026 | AI engine "Wingz"; customers can keep using VWO or AB Tasty during transition [press, 2026-09] |
| Optimizely Opal renamed Optimizely Agent Platform | 1 Sept 2026 | Experimentation agents: Idea builder, Build agent, CRO Manager virtual teammate [Official, 2026] |
| Shopify Rollouts (native theme A/B testing) | Winter '26 Edition, expanded June 2026 | Server-side theme splits; limited stats [secondary sources, 2026] |
| Datadog acquired Eppo | 2025 | Warehouse-native experimentation now part of Datadog [Unverified] |

Consolidation is raising prices and pushing vendors upmarket, according to competitors' analyses [Contested, vendor commentary]. For new purchases, check contract terms, data export, and roadmap commitments.

## 2. Tool landscape by job

### 2.1 Experimentation platforms
| Tool | Type | Strength | Notes |
|------|------|----------|-------|
| Optimizely Web and Feature Experimentation | Client and server side | Enterprise programs, Stats Engine (sequential), Agent Platform AI agents, contextual bandits (April 2026) | Expensive; release notes at support.optimizely.com |
| Wingify (VWO, AB Tasty) | Client side plus server side, personalization | Mid-market and enterprise; Bayesian reporting (VWO SmartStats) [Unverified current] | Integration ongoing in 2026 |
| Kameleoon | Client and server side | Hybrid testing, personalization, strong in EU | Check AI features [Unverified] |
| Convert | Client side | Privacy focus, flat pricing, both stats approaches [Unverified] | |
| GrowthBook | Open source, warehouse native, feature flags | Bayesian default, frequentist and sequential, CUPED, self-host option [Unverified current defaults] | Good fit for Next.js and data teams |
| PostHog | Product analytics plus experiments, flags, replay, surveys | One tool for SaaS; generous free tier [Unverified current limits] | |
| Statsig (Amplitude) | Flags and experiments, CUPED, warehouse native | Strong stats; ownership changed May 2026 | Watch for consolidation with Amplitude Experiment |
| LaunchDarkly | Feature management plus experimentation | Engineering-led rollouts | |
| Shopify Rollouts | Native theme and configuration tests | Server-side split, free with Shopify | No targeting, no confidence intervals [secondary 2026] |
| Shopify apps (for example Intelligems, Shoplift) | Price, shipping, theme tests | Ecommerce-specific metrics | Verify app listing details |

Choosing:
```
Traffic under about 20k monthly sessions and no developer?  -> No platform yet. Research + fixes + before/after.
Shopify, theme-level tests only?                            -> Rollouts, compute stats yourself; app if targeting or pricing tests needed.
Developer access, React/Next.js, data warehouse?           -> GrowthBook or PostHog (server-side, no flicker).
Marketing-led team, many page tests, mid-market budget?    -> Wingify (VWO/AB Tasty), Convert, Kameleoon.
Enterprise program, many teams, governance?                -> Optimizely, Kameleoon, Wingify enterprise, Amplitude/Statsig.
```

### 2.2 Behavior analytics and VOC
| Tool | Use | Notes |
|------|-----|-------|
| Microsoft Clarity | Free heatmaps, recordings, frustration signals, Copilot summaries, AI Visibility | Data Export API and official MCP server (see section 4) |
| Contentsquare (incl. Hotjar) | Heatmaps, replay, zoning, surveys, Sense AI | Free plan with session caps and partial replay capture [secondary 2026]; connectors for AI assistants with tool call limits [Official support 2026] |
| PostHog session replay | Replay tied to product analytics | SaaS |
| FullStory, Mouseflow, Lucky Orange | Replay and heatmaps | Compare cost and sampling |
| Fairing, KnoCommerce | Post-purchase surveys on Shopify | Attribution and "what almost stopped you" |
| Typeform, Tally, Google Forms | Customer surveys | |
| Zuko | Form analytics (field-level) | |

### 2.3 User testing
UserTesting, Lyssna (five-second, preference, first-click tests), Maze (prototype tests), moderated calls with Zoom or Lookback. Recruit from customer lists where possible.

### 2.4 Landing page builders
Unbounce, Instapage, Leadpages, Webflow, Framer, Shopify page builders (PageFly, GemPages, Shogun, Replo). Check each page's weight; builders often add JavaScript. Unbounce's 2024 benchmark (41,000 pages) is useful context for lead gen medians [Study, 2024].

### 2.5 Speed and accessibility
PageSpeed Insights (and API), CrUX API and CrUX History API, Search Console CWV report, Lighthouse and Lighthouse CI, WebPageTest, DebugBear, SpeedCurve, RUMvision; axe DevTools, WAVE, Pa11y, Lighthouse accessibility. Do not recommend accessibility overlays as a compliance fix: the US FTC took action against an overlay vendor (accessiBe) in 2025 over claims its tool made sites compliant [Unverified details, verify].

## 3. Data access matrix for Claude

| Need | Best source | Access method |
|------|-------------|---------------|
| Funnel by device, channel, landing page | GA4 | GA4 MCP server or Data API; BigQuery export; CSV from Explorations |
| Behavior signals, recordings | Clarity, Contentsquare | Clarity MCP or Data Export API; Contentsquare connector; manual review links |
| Test results | Testing platform | Platform API or MCP if available; CSV export |
| Orders, AOV, products | Shopify, WooCommerce | Shopify Admin GraphQL API (read scopes), CSV exports |
| Lead quality | CRM (HubSpot, Salesforce) | CRM connector or CSV export of leads with stage |
| Speed | CrUX API, PSI API, RUM | API calls below |
| Pages and code | Repository | Read files directly; run local build and Lighthouse |
| Screenshots and QA | Local browser automation | Playwright (CLI or MCP), Chrome DevTools MCP [Unverified availability] |

## 4. API and MCP recipes

### 4.1 Microsoft Clarity MCP server and Data Export API
Community directories list an official package `@microsoft/clarity-mcp-server`, run with npx and a `CLARITY_API_TOKEN` (or `--clarity_api_token`), exposing a `get-clarity-data` tool that queries the Data Export API for the last 1 to 3 days with up to 3 dimensions (for example Browser, Device, Country/Region) and metrics such as Scroll Depth, Engagement Time and Traffic [secondary sources; verify on Microsoft Learn and npm].
Example MCP client config (Claude Code `.mcp.json`):
```json
{
  "mcpServers": {
    "clarity": {
      "command": "npx",
      "args": ["-y", "@microsoft/clarity-mcp-server"],
      "env": { "CLARITY_API_TOKEN": "${CLARITY_API_TOKEN}" }
    }
  }
}
```
Direct API call (generate the token in Clarity Settings > Data Export) [Unverified endpoint details; the API has a low daily request limit per project, check docs]:
```bash
curl -s "https://www.clarity.ms/export-data/api/v1/project-live-insights?numOfDays=3&dimension1=Device&dimension2=Source" \
  -H "Authorization: Bearer $CLARITY_API_TOKEN" -H "Content-Type: application/json"
```
The export covers only recent days. Pull and save snapshots to `ads-master/data/imports/YYYY-MM-DD_clarity_<what>.json` to build history.

### 4.2 GA4 Data API (landing page performance by device)
```bash
curl -s -X POST "https://analyticsdata.googleapis.com/v1beta/properties/$GA4_PROPERTY_ID:runReport" \
  -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
  -H "Content-Type: application/json" -d '{
  "dateRanges": [{"startDate": "90daysAgo", "endDate": "yesterday"}],
  "dimensions": [{"name": "landingPagePlusQueryString"}, {"name": "deviceCategory"}, {"name": "sessionDefaultChannelGroup"}],
  "metrics": [{"name": "sessions"}, {"name": "keyEvents"}, {"name": "sessionKeyEventRate"}, {"name": "purchaseRevenue"}],
  "orderBys": [{"metric": {"metricName": "sessions"}, "desc": true}],
  "limit": 200
}'
```
Funnel reports are available through `runFunnelReport` on the v1alpha endpoint [Official, alpha API, may change]. Google also publishes an open source Google Analytics MCP server [Unverified current status; check github.com/googleanalytics]. Coordinate property access with `measurement`.

### 4.3 CrUX API (field Core Web Vitals for a URL or origin)
```bash
curl -s -X POST "https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=$CRUX_API_KEY" \
  -H "Content-Type: application/json" -d '{
  "url": "https://www.example.com/lp/running",
  "formFactor": "PHONE",
  "metrics": ["largest_contentful_paint", "interaction_to_next_paint", "cumulative_layout_shift"]
}'
```
Use `"origin"` instead of `"url"` when the page has too little traffic. Use `records:queryHistoryRecord` for weekly trends.

### 4.4 PageSpeed Insights API (lab plus field)
```bash
curl -s "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https%3A%2F%2Fwww.example.com%2Flp%2Frunning&strategy=mobile&category=performance&category=accessibility&key=$PSI_API_KEY" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); a=d['lighthouseResult']['audits']; print('LCP', a['largest-contentful-paint']['displayValue'], '| CLS', a['cumulative-layout-shift']['displayValue'], '| TBT', a['total-blocking-time']['displayValue'])"
```

### 4.5 Lighthouse locally (no API key)
```bash
npx lighthouse https://www.example.com/lp/running --preset=perf --form-factor=mobile --screenEmulation.mobile \
  --output=json --output-path=./lh-running.json --quiet
```

### 4.6 Shopify Admin GraphQL (read-only order data for AOV and product mix)
Use a custom app with `read_orders` and `read_products` scopes, or a Shopify MCP connector if installed. Shopify also publishes a developer MCP server for docs and schema lookup [Unverified package name; check shopify.dev]. Never use write scopes for CRO analysis.

### 4.7 Other MCP servers to look for
| Server | Use | Status |
|--------|-----|--------|
| PostHog MCP | Query insights, flags, experiments | Official [Unverified, check posthog.com docs] |
| GrowthBook MCP | Read experiments and flags, create drafts | Official [Unverified] |
| Contentsquare connectors | Ask analytics questions from Claude or ChatGPT | Official support pages list availability on all plans with tool call limits [secondary 2026] |
| Playwright MCP | Drive a browser for screenshots and QA | Microsoft open source [Unverified] |
| Chrome DevTools MCP | Performance traces, network, console | Google open source [Unverified] |
| CRM MCP servers (HubSpot, Salesforce) | Lead quality by source and form | Check vendor |

If a connector is present in the session, use it. If not, ask for a CSV export (see `ads-master/data/imports/HOW_TO_EXPORT.md`, row `cro`) and continue.

## 5. CSV exports to request (when no connector)
| Export | Where | Columns needed | Range |
|--------|-------|----------------|-------|
| GA4 funnel exploration | Explore > Funnel, export | Step, device, users, completion rate, abandonment | Last 90 days |
| GA4 landing pages | Reports > Engagement > Landing page | Landing page, sessions, key events, revenue, device | Last 90 days |
| Shopify conversion funnel | Analytics > Reports | Sessions, added to cart, reached checkout, completed | Last 90 days, daily |
| Test results | Testing tool | Variant, visitors, conversions, revenue, by day | Test period |
| CRM leads | CRM | Lead ID, created date, source, form, landing page, stage, value | Last 180 days |
| Clarity | Dashboard export or API | Device, source, rage clicks, dead clicks, quick backs, scroll depth | Last 3 days via API; dashboard for longer |
| Reviews | Review app | Rating, text, date, product | All |

## 6. Security and approvals
- Read-only tokens for analytics and commerce. No write scopes without explicit human approval for a specific task.
- Do not paste tokens into chat outputs or files under `ads-master/`.
- Testing platforms: the agent may draft experiments only where the tool supports drafts and the human approved; starting, stopping or changing allocation of live tests requires explicit approval.
- Masking: confirm session recording tools mask personal data before analyzing recordings.
