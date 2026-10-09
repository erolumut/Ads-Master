# Ads Master

**Plug and play growth agents for Claude Code.** Twenty three specialist agents for paid media, SEO, AI search visibility, the storefront, conversion, offers, pricing, marketplaces, creative and video production, retention, apps, measurement and compliance. They are built on a deep market research sweep (October 2026) and designed to adapt to any project: ecommerce, lead gen, B2B SaaS, local services, apps and marketplaces, from a $500 test budget to enterprise scale.

Install once, drop into any project, and get a senior growth team that audits, plans, builds and reviews, while you keep the final say on every dollar spent and every word published. Safety is enforced twice: by the agents' rules and by deterministic hooks that block risky actions no matter what a model decides.

| At a glance | |
|---|---|
| Agents | 23 specialists plus 3 utility skills (`ads-setup`, `ads-review`, `ads-verify`) |
| Workflow Kit | A separate plugin for any project: model routing (haiku, sonnet, opus, fable), parallel sessions, sprint prompts, plan first sessions, handover, decision log, review guardians, git hooks and gate scripts |
| Playbook depth | 348 reference modules, about 72,000 lines of procedures, audits, settings, formulas, queries and scripts |
| Research | 24 dossiers with dated timelines of platform changes (January 2025 to October 2026) and about 3,900 unique cited URLs |
| Safety | Gates G0 to G4, automation stages 1 to 5, guard hooks with tests, claims registry, incident runbook |
| Tools | SEO preflight crawler, daily report builder, tracking plan checker, basket economics calculator, claims checker, approved copy lock, post release smoke check, verified facts check, FFmpeg delivery, variant planner, URL and injection checkers |
| Install | Claude Code plugin, project copy script, or open this repo directly |

---

## The team

| Group | Agent | What it masters |
|-------|-------|-----------------|
| Strategy and control | `growth-orchestrator` | The conductor. Diagnoses the business, picks channels, allocates budget on marginal returns, runs unit economics and forecasts, routes work, enforces publish gates, runs the daily, weekly and monthly reviews. |
| | `measurement` | GA4, GTM, server-side tagging, consent mode, conversion APIs, offline and CRM conversions, attribution, incrementality and MMM, the unified daily report. |
| | `compliance` | The claims and policy gate: product facts and claims registry, food, health, finance and other regulated claims, pricing and consumer law (EU, UK, US, Turkey), reviews and influencers, green claims, platform policies, AI disclosure, marketing consent. |
| | `market-intel` | Competitor ads, offers, pricing, SEO and AI visibility gaps, voice of customer, demand and market sizing. |
| Paid acquisition | `meta-ads` | Facebook, Instagram, Threads, WhatsApp. Andromeda era structure, Advantage+, bidding, creative diversity, CAPI, lead and messaging ads, scaling and recovery. |
| | `google-ads` | Search, AI Max, Performance Max, Demand Gen, YouTube, Shopping, ads in AI Overviews and AI Mode. Value based bidding, GAQL audit queries, scripts. |
| | `microsoft-ads` | Bing, Copilot placements, Microsoft Audience Network, PMax and Shopping, Google import done right. |
| | `chatgpt-ads` | Ads inside ChatGPT (OpenAI Ads Manager) plus strategy for every other AI assistant ad surface. |
| | `tiktok-ads` | Smart+, GMV Max and TikTok Shop, Spark Ads, creators, TikTok Ad Network. |
| | `linkedin-ads` | B2B paid social and ABM: Thought Leader Ads, lead gen forms, CRM sync, pipeline as the KPI. |
| | `mobile-app-growth` | ASO for both stores, Apple Ads, app campaigns on Google, Meta and TikTok, MMPs, SKAN and AdAttributionKit, paywalls, web to app. |
| Organic visibility | `seo` | Technical, content, local, ecommerce and international SEO for Google and Bing after AI Overviews. Fixes SEO in your codebase, ships a preflight crawler. |
| | `ai-search-optimization` | GEO, AEO, LLMO: being mentioned, recommended and cited by ChatGPT, AI Overviews, AI Mode, Gemini, Perplexity, Copilot and Claude. Evidence over folklore. |
| Conversion and storefront | `storefront-ux` | The store itself: navigation, homepage, on-site search, filters, product pages, cart drawer, checkout extensions, accessibility. A pattern library drawn from open source commerce repos, shipped as code. |
| | `cro` | Conversion research, landing pages, experiment statistics, in-app browser and mobile checkout details. |
| | `site-engineer` | Preview, QA, release and rollback for Shopify, WordPress, Next.js and Webflow; launch QA for every ad destination; worst case data tests; security review of changes. |
| Offer and commerce | `offer-strategy` | Incentive mechanics: bundles, launch offers, discount vs bonus vs free shipping economics, subscriptions, promo calendar, channel conflict. |
| | `pricing-strategy` | The commercial pricing consultant: price level vs competitors, cost to serve and margin waterfall, minimum basket and free delivery threshold, price architecture, willingness to pay, channel price corridors, price increases, the Commercial Pricing Report. |
| | `marketplaces` | Amazon, bol.com, Trendyol, Hepsiburada, Allegro, Zalando, Etsy, eBay, Walmart, noon: marketplace choice, listings, retail media ads, Featured Offer, fees and contribution, account health, price parity with DTC. |
| | `commerce-feeds` | Merchant Center, Meta and TikTok catalogs, ChatGPT and AI shopping feeds, agentic commerce readiness, custom labels for profit bidding. |
| Creative | `creative-strategy` | Customer research to angles, hooks, scripts and briefs; creative testing systems; creative analytics; localization. |
| | `video-studio` | Briefs to finished video ad files: code driven motion (HyperFrames, Remotion), generative video under a spend cap, avatars with disclosure, FFmpeg editing, captions, safe zones, variant batches. |
| Retention | `lifecycle-crm` | Email, SMS, WhatsApp and push flows, deliverability, consent, subscriptions, loyalty, cohort LTV, and retention data fed back to paid media. |

---

## How it works

```
                          You
                           |
                  main Claude session  <-- loads the growth-orchestrator skill (conductor)
              /      |       |       |      \
         meta-ads storefront-ux video-studio ... measurement     <-- specialist subagents, in parallel
              \      |       |       |      /
   guard hooks (every tool call): G0 read | G1 draft | G2 prepare | G3 commit | G4 forbidden
                           |
                  ads-master/ (per project)
   PROJECT_BRIEF  MEASUREMENT  METRICS  STRATEGY  PRIORITIES  GUARDRAILS  DECISIONS  INCIDENTS
   brand/ (facts, claims)  creative-library/  memory/<agent>.md  journal/  outputs/<agent>/  logs/
```

- **Global brain, local state.** The playbooks (this repo) are reusable across every project. Each project keeps its own facts, learnings, journal, decisions and deliverables in `ads-master/`.
- **Publish gates.** Customer facing assets pass `compliance`, site changes pass `site-engineer`, scaling waits for `measurement`. The orchestrator enforces the order.
- **Deterministic safety.** Hooks inspect every tool call against `ads-master/guardrails.json`: reads pass, platform drafts need the right automation stage and a confirmation, anything that spends, goes live, changes prices or messages customers needs explicit approval, deletions and budgets above the cap are refused, secrets are kept out of files, and every write lands in an audit log.
- **Earned memory.** Each agent keeps `memory/<agent>.md` for patterns confirmed by that project's data.
- **Heartbeat.** `ads-review` produces the daily report (facts, interpretation, recommendation; platform reported next to backend observed), the weekly learning loop and the monthly reallocation.

---

## Install

### Option A: Claude Code plugin (recommended)

```text
/plugin marketplace add erolumut/Ads-Master
/plugin install ads-master@ads-master
```

All agents, skills and guard hooks are then available in every project. Skills appear as `/ads-master:<skill>` (for example `/ads-master:ads-setup`). The guard stays silent in projects without an `ads-master/` workspace. If the repository is private, make sure your git credentials can read it.

### Option B: copy into a project (team friendly, versioned with the project)

```bash
git clone https://github.com/erolumut/Ads-Master.git ~/ads-master
~/ads-master/scripts/install.sh /path/to/your/project
# or only what you need (orchestrator, measurement and utilities are always included):
~/ads-master/scripts/install.sh /path/to/your/project --only meta-ads,google-ads,storefront-ux,compliance
# later, to pull new playbook versions without touching your workspace:
~/ads-master/scripts/install.sh /path/to/your/project --update
```

This writes `.claude/agents/`, `.claude/skills/`, the guard hook (`.claude/hooks/ads-master-guard.py`, registered in `.claude/settings.json`) and an `ads-master/` workspace. Use `--no-hooks` only if you know why.

### Option C: use this repo as the workspace

Open the repo in Claude Code. The agents, skills and kits load from `.claude/` (per file symlinks rebuilt by `python3 scripts/link_dev.py`). Run `/ads-setup`. `ads-master/` is git ignored here by default.

### Pick only what you need

`install.sh <project> --pack ecommerce-dtc` (or `marketplace-seller`, `lead-gen-local`, `b2b-saas`, `mobile-app`, `ai-visibility`, `full`). Core (orchestrator, measurement, compliance and the utility skills) is always included. The full decision guide, the packs and the CLAUDE.md snippet are in [docs/HOW_TO_USE.md](docs/HOW_TO_USE.md), which regenerates itself from the repo.

### Workflow Kit (for any project, ads or not)

```text
/plugin install workflow-kit@ads-master
# or: scripts/install.sh /path/to/project --kit workflow --no-workspace --no-hooks
```

Model routing with cheap scouts and extractors, sonnet researchers and mechanics, opus verifiers and a fable advisor; a parallel sessions ledger; sprint, delegation and next session prompts; plan first sessions; handover; decision log with placeholder numbering; CLAUDE.md budget check; review guardians; validate only git hooks; workflow YAML lint and commit time invariants. Every script exits 0 pass, 1 fail, 2 could not run. The patterns and their origins: [docs/WORKFLOW_PATTERNS.md](docs/WORKFLOW_PATTERNS.md).

### Option D: other AI tools

Everything is plain Markdown plus small standard library Python scripts. Each `skills/<agent>/` folder can be added as project knowledge in other assistants or agent frameworks; the guard is Claude Code specific.

Requirements: Claude Code, Python 3 for the guard and scripts, FFmpeg for video-studio delivery.

---

## Quick start (first hour)

1. **Set up the workspace:** run `/ads-setup`. Claude scans the codebase (platform, tags, consent, schema, robots, AI crawler rules, app and ESP setup), asks up to eight business questions, sets the automation stage and money caps, seeds product facts and claims, and activates the right agents.
2. **Audit:** "Run a full growth audit." The orchestrator fans out to the active specialists, then returns one prioritized plan.
3. **Approve:** review `ads-master/PRIORITIES.md` and the change requests.
4. **Operate:** `/ads-review daily` for the daily report, `/ads-review weekly` every Monday (or schedule both). Raise the automation stage in `GUARDRAILS.md` only when the current one has run cleanly for weeks.

### Things to ask

- "Audit our Meta account using the exports in ads-master/data/imports."
- "Prepare our first launch: tracking, store, offer and claims checks, then a PAUSED campaign draft."
- "Audit the store page by page and ship the table stakes fixes as a branch."
- "Turn these three approved briefs into 9:16 and 4:5 videos with three hooks each."
- "Which is better for us: free shipping over 50 or four free bars in the 48 box? Show the economics."
- "Build the post purchase and replenishment flows in Klaviyo for the 24 and 48 packs."
- "Can we say 'high protein' and 'healthy' in our Dutch ads?"
- "Make our product and category pages more likely to be cited by ChatGPT and AI Overviews."
- "Run the SEO preflight on our staging site before we launch."
- "Write a commercial pricing report: our prices vs competitors per 100 g, cost to serve, minimum basket and free delivery threshold."
- "Should we sell on bol.com or Amazon first, and what does each leave us per order after fees and ads?"

---

## Why it adapts to any project

| Mechanism | What it does |
|-----------|-------------|
| Adaptation matrix in every skill | Changes structure, bidding, KPIs, creative volume and cadence by business model, budget tier and maturity |
| Project brief, metric dictionary, measurement file | Every decision is anchored to your margins, your definitions and your source of truth |
| Automation stages | The same agents run read only on day one and with controlled writes months later |
| Project memory and decision log | Learnings and decisions confirmed by your data override generic best practice |
| Freshness protocol | Before acting on settings, policies or benchmarks, agents check the official changelogs |
| Geo and country modules | Turkey, EU and UK, US, MENA built in; new countries generated on demand |
| Codebase awareness | When installed in a repo, agents read and fix the real site: tags, schema, robots, metadata, storefront components |

---

## Repository map

```
.claude-plugin/          plugin.json and marketplace.json
agents/                  23 subagent definitions
skills/<agent>/          SKILL.md + references/ (+ scripts/ where useful)
skills/ads-setup/        workspace installer + template/ (the per project workspace)
skills/ads-review/       heartbeat runner
skills/ads-verify/       evidence ladder for Unverified and Contested claims
kits/workflow-kit/       Workflow Kit plugin: routing agents, ritual skills, gate scripts, templates
hooks/hooks.json         guard hooks for plugin installs
scripts/guard.py         the deterministic guard (with scripts/test_guard.py)
scripts/install.sh       project installer
scripts/validate.py      structure, YAML, style, packs, links and docs freshness validator
scripts/build_docs.py    regenerates the AUTO sections of docs/HOW_TO_USE.md
scripts/link_dev.py      links agents, skills and kits into .claude/ for this repo
scripts/unverified_report.py  the verification queue of labeled claims
research/                market research dossiers behind every playbook
docs/                    HOW_TO_USE.md, AUTHORING_SPEC.md, GUARDRAILS_MODEL.md, WORKFLOW_PATTERNS.md, packs.json
AGENT_REGISTRY.md        roster, KPIs, cadences, handoffs
.claude/                 CLAUDE.md for working in this repo, symlinks that load agents and skills
```

## Research library

Every playbook is backed by a dossier in `research/` with a dated timeline of platform changes, best practice consensus, contested topics, benchmarks with caveats, tools and MCP servers, and numbered sources. Start with `research/00-market-overview-2026.md`.

## Keeping it current

Platforms change monthly. Each skill carries a "Knowledge as of" date and a Freshness Protocol. Every claim carries an evidence label: `[Official]`, `[Study]`, `[Practitioner consensus]`, `[Contested]` or `[Unverified]`. Agents treat `[Unverified]` and `[Contested]` items as hypotheses and confirm them in the live account or an official source before they drive spend. Recommended maintenance: every quarter, re-run the research for each agent, update references and dossiers, bump the version in `.claude-plugin/plugin.json`, and run `python3 scripts/validate.py` and `python3 scripts/test_guard.py`.

## Adding an agent

Copy the closest package, follow `docs/AUTHORING_SPEC.md`, register it in `AGENT_REGISTRY.md`, the growth-orchestrator routing table and the workspace template (HEARTBEAT and memory), then validate. Channels with quick start guides but no dedicated agent yet (Reddit, Pinterest, Snapchat, X, CTV, affiliate, influencer) are listed in the growth-orchestrator references.

## Disclaimer

Ads Master gives recommendations, drafts changes and enforces guardrails, but it is not legal advice. You remain responsible for ad spend, platform policy compliance, privacy law and claims in your ads. Benchmarks are directional; your own data wins.
