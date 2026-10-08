# Ads Master

**Plug and play growth agents for Claude Code.** Fourteen specialist agents for paid media, SEO, AI search visibility, measurement, conversion and creative, built on a deep market research sweep (October 2026) and designed to adapt to any project: ecommerce, lead gen, B2B SaaS, local services, apps and marketplaces, from a $1k test budget to enterprise scale.

Install once, drop into any project, and get a senior growth team that audits, plans, builds and reviews, while you keep the final say on every dollar spent and every word published.

| At a glance | |
|---|---|
| Agents | 14 specialists plus 2 utility skills |
| Playbook depth | 205 reference modules, about 45,000 lines of procedures, audits, settings, formulas, queries and scripts |
| Research | 15 dossiers with dated timelines of platform changes (January 2025 to October 2026) and about 2,600 cited URLs, every package verified in a second live research pass |
| Install | Claude Code plugin, project copy script, or open this repo directly |

---

## The team

| Agent | What it masters |
|-------|-----------------|
| `growth-orchestrator` | The conductor. Diagnoses the business, picks channels, allocates budget on marginal returns, runs unit economics and forecasts, routes work, runs the weekly and monthly reviews. |
| `meta-ads` | Facebook, Instagram, Threads, WhatsApp. Andromeda era structure, Advantage+ campaigns, bidding, creative diversity, CAPI, lead and messaging ads, scaling and recovery. |
| `google-ads` | Search, AI Max, Performance Max, Demand Gen, YouTube, Shopping, ads in AI Overviews and AI Mode. Value based bidding, GAQL audit queries, scripts. |
| `chatgpt-ads` | Ads inside ChatGPT (OpenAI Ads Manager) plus strategy for every other AI assistant ad surface. New channel test plans with honest measurement. |
| `microsoft-ads` | Bing, Copilot placements, Microsoft Audience Network, PMax and Shopping, Google import done right. |
| `tiktok-ads` | Smart+, GMV Max and TikTok Shop, Spark Ads, creators, native creative systems. |
| `linkedin-ads` | B2B paid social and ABM: Thought Leader Ads, lead gen forms, CRM sync, pipeline as the KPI. |
| `seo` | Technical, content, local, ecommerce and international SEO for Google and Bing after AI Overviews. Fixes SEO directly in your codebase. |
| `ai-search-optimization` | GEO, AEO, LLMO: being mentioned, recommended and cited by ChatGPT, AI Overviews, AI Mode, Gemini, Perplexity, Copilot and Claude. Evidence over folklore. |
| `measurement` | GA4, GTM, server-side tagging, consent mode, conversion APIs, offline and CRM conversions, attribution, incrementality and MMM. The foundation every other agent trusts. |
| `cro` | Landing pages, checkout and forms, experiment statistics, page speed for conversion. Builds pages and test variants in code. |
| `creative-strategy` | Customer research to angles, hooks, scripts and briefs; creative testing systems; AI creative production; creative analytics and fatigue. |
| `commerce-feeds` | Merchant Center, Meta and TikTok catalogs, ChatGPT and AI shopping feeds, agentic commerce readiness, custom labels for profit bidding. |
| `market-intel` | Competitor ads, offers, pricing, SEO and AI visibility gaps, voice of customer, demand and market sizing. |

Plus two utility skills: **`ads-setup`** (creates and fills the project workspace) and **`ads-review`** (the heartbeat: daily, weekly, monthly, quarterly).

---

## How it works

```
                        You
                         |
                 main Claude session  <-- loads the growth-orchestrator skill (conductor)
             /     |      |      |     \
        meta-ads google-ads seo  ...  measurement      <-- specialist subagents, run in parallel
             \     |      |      |     /
                 ads-master/ (per project)
     PROJECT_BRIEF  MEASUREMENT  STRATEGY  PRIORITIES  EXPERIMENTS
     memory/<agent>.md   journal/   data/imports/   outputs/<agent>/
```

- **Global brain, local state.** The playbooks (this repo) are reusable across every project. Each project keeps its own facts, learnings, journal and deliverables in `ads-master/`.
- **Shared memory through a journal.** Agents never talk directly. They write dated journal entries and read each other's.
- **Earned memory.** Each agent keeps `memory/<agent>.md` for patterns confirmed by that project's data, never assumptions.
- **Heartbeat.** `ads-review` runs the daily alert check, the weekly learning loop and the monthly reallocation, on demand or on a schedule.
- **Human in the loop.** Agents produce audits, plans and change requests. Nothing is spent, launched, paused or published without your approval.

---

## Install

### Option A: Claude Code plugin (recommended)

```text
/plugin marketplace add erolumut/Ads-Master
/plugin install ads-master@ads-master
```

All agents and skills are then available in every project. Skills appear as `/ads-master:<skill>` (for example `/ads-master:ads-setup`). If the repository is private, make sure your git credentials can read it.

### Option B: copy into a project (team friendly, versioned with the project)

```bash
git clone https://github.com/erolumut/Ads-Master.git ~/ads-master
~/ads-master/scripts/install.sh /path/to/your/project
# or only what you need (orchestrator, measurement and utilities are always included):
~/ads-master/scripts/install.sh /path/to/your/project --only meta-ads,google-ads,seo,ai-search-optimization
# later, to pull new playbook versions without touching your workspace:
~/ads-master/scripts/install.sh /path/to/your/project --update
```

This writes `.claude/agents/`, `.claude/skills/` and an `ads-master/` workspace into the project.

### Option C: use this repo as the workspace

Open the repo in Claude Code. The agents load from `.claude/` (symlinked). Run `/ads-setup`. Good for a single business or for trying the system out. `ads-master/` is git ignored here by default.

### Option D: other AI tools

Everything is plain Markdown. Each `skills/<agent>/` folder (SKILL.md plus references) can be added as project knowledge in other assistants or agent frameworks.

---

## Quick start (first hour)

1. **Set up the workspace:** run `/ads-setup`. Claude scans the codebase (platform, tags, consent, schema, robots, AI crawler rules), asks you up to eight questions and fills `ads-master/PROJECT_BRIEF.md` and `MEASUREMENT.md`.
2. **Audit:** "Run a full growth audit." The orchestrator fans out to the active specialists, then returns one prioritized plan.
3. **Approve:** review `ads-master/PRIORITIES.md` and the change requests.
4. **Operate:** run `/ads-review weekly` every Monday (or schedule it). Monthly and quarterly modes add reallocation, platform change checks and full audits.

### Things to ask

- "Audit our Meta account using the exports in ads-master/data/imports."
- "Our Google Ads CPA jumped 40 percent this week. Find out why."
- "Plan a ChatGPT Ads test for a $5k budget with a proper holdout."
- "Make our product and category pages more likely to be cited by ChatGPT and AI Overviews."
- "Implement Meta CAPI and Google enhanced conversions in this Next.js app with deduplication."
- "Build a landing page for the spring campaign and an A/B variant for the headline."
- "Show me what our top three competitors are running on Meta and TikTok and the angles we are missing."
- "Allocate next month's $40k across channels and show the marginal return math."

---

## Why it adapts to any project

| Mechanism | What it does |
|-----------|-------------|
| Adaptation matrix in every skill | Changes structure, bidding, KPIs, creative volume and cadence by business model, budget tier (Starter, Growth, Scale, Enterprise) and maturity |
| Project brief and measurement file | Every decision is anchored to your margins, your conversion definitions and your source of truth |
| Project memory | Learnings confirmed by your data override generic best practice |
| Freshness protocol | Before acting on settings, policies or benchmarks, agents check the official changelogs and log changes |
| Geo modules | Market notes for Turkey, EU and UK, US, MENA (privacy, taxes on ad spend, platforms, payments) |
| Codebase awareness | When installed in a repo, agents read and fix the real site: tags, schema, robots, metadata, landing pages |

---

## Repository map

```
.claude-plugin/          plugin.json and marketplace.json
agents/                  14 subagent definitions
skills/<agent>/          SKILL.md + references/ (deep modules, audits, sources)
skills/ads-setup/        workspace installer + template/
skills/ads-review/       heartbeat runner
research/                market research dossiers behind every playbook
docs/AUTHORING_SPEC.md   the contract for adding or editing agents
scripts/install.sh       project installer
scripts/validate.py      structure and style validator
AGENT_REGISTRY.md        roster, KPIs, cadences, handoffs
.claude/                 CLAUDE.md for working in this repo, symlinks that load agents and skills
```

## Research library

Every playbook is backed by a dossier in `research/` with a dated timeline of platform changes (January 2025 to October 2026), best practice consensus, contested topics, benchmarks with caveats, tools and MCP servers, and numbered sources. Start with `research/00-market-overview-2026.md`.

## Keeping it current

Platforms change monthly. Each skill carries a "Knowledge as of" date and a Freshness Protocol. Every claim carries an evidence label: `[Official]`, `[Study]`, `[Practitioner consensus]`, `[Contested]` or `[Unverified]`. Agents treat `[Unverified]` and `[Contested]` items as hypotheses and confirm them in the live account or an official source before they drive spend. Recommended maintenance: every quarter, re-run the research for each agent, update the references and research dossiers, bump the version in `.claude-plugin/plugin.json`, and run `python3 scripts/validate.py`.

## Adding an agent

Copy the closest package, follow `docs/AUTHORING_SPEC.md`, register it in `AGENT_REGISTRY.md` and in the growth-orchestrator routing table, then validate. Channels with quick start guides but no dedicated agent yet (Reddit, Pinterest, Snapchat, Amazon Ads, Apple Search Ads, CTV, affiliate, lifecycle email) are listed in the growth-orchestrator references.

## Disclaimer

Ads Master gives recommendations and drafts changes. You remain responsible for ad spend, platform policy compliance, privacy law and claims in your ads. Benchmarks are directional; your own data wins.
