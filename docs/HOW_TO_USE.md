# How to use Ads Master

> A living document. The catalog sections between `AUTO` markers are generated from the agents, skills, packs and kits by `python3 scripts/build_docs.py`, and `scripts/validate.py` fails when they are stale. So when an agent, a pack or a kit is added, this guide updates itself. Text outside the markers is written by hand.

Ads Master is a set of growth agents for Claude Code: paid media, organic and AI visibility, the storefront, conversion, pricing and offers, creative and video, retention, apps, measurement and compliance, plus a conductor that routes the work and guard hooks that keep money and customers safe. You do not need all of it. Most projects start with one pack.

---

## 1. Decide in one minute

| Question | Answer |
|----------|--------|
| Use it in many projects, always up to date? | Install as a **plugin** (section 3, option A). |
| Version it with one project, share with a team, pick only some agents? | **Copy into the project** with a pack (option B). |
| Just trying it? | Open this repo in Claude Code and run `/ads-setup` here (option C). |
| Which agents do I need? | Pick the **pack** that matches the business (section 2). Core is always included. You can add or remove agents later. |

## 2. Packs: which agents for which project

Core (orchestrator, measurement, compliance and the three utility skills) is always installed: without measurement nobody can trust the numbers, and without compliance nothing should be published.

<!-- AUTO:packs:start -->
| Pack | For | Agents added on top of core | Install |
|------|-----|------------------------------|---------|
| Core (always installed) | Every project | `growth-orchestrator`, `measurement`, `compliance` | always |
| Ecommerce DTC | Brands selling on their own store (Shopify, WooCommerce, headless) | `meta-ads`, `google-ads`, `tiktok-ads`, `storefront-ux`, `cro`, `site-engineer`, `offer-strategy`, `pricing-strategy`, `commerce-feeds`, `creative-strategy`, `video-studio`, `lifecycle-crm`, `seo`, `ai-search-optimization`, `market-intel` | `install.sh <project> --pack ecommerce-dtc` |
| Marketplace seller | Brands or resellers selling on Amazon, bol.com, Trendyol, Hepsiburada and similar | `marketplaces`, `pricing-strategy`, `commerce-feeds`, `creative-strategy`, `market-intel`, `offer-strategy` | `install.sh <project> --pack marketplace-seller` |
| Lead gen and local services | Clinics, agencies, trades, real estate, education, local businesses | `google-ads`, `meta-ads`, `microsoft-ads`, `cro`, `site-engineer`, `seo`, `ai-search-optimization`, `creative-strategy`, `lifecycle-crm`, `market-intel` | `install.sh <project> --pack lead-gen-local` |
| B2B and SaaS | Software, B2B services and high consideration sales | `google-ads`, `linkedin-ads`, `microsoft-ads`, `chatgpt-ads`, `seo`, `ai-search-optimization`, `cro`, `site-engineer`, `pricing-strategy`, `offer-strategy`, `lifecycle-crm`, `creative-strategy`, `market-intel` | `install.sh <project> --pack b2b-saas` |
| Mobile app | iOS and Android apps, subscription and freemium | `mobile-app-growth`, `meta-ads`, `google-ads`, `tiktok-ads`, `creative-strategy`, `video-studio`, `lifecycle-crm`, `pricing-strategy`, `market-intel` | `install.sh <project> --pack mobile-app` |
| Organic and AI visibility | Any business that wants search and AI assistant visibility without paid media first | `seo`, `ai-search-optimization`, `chatgpt-ads`, `site-engineer`, `market-intel` | `install.sh <project> --pack ai-visibility` |
| Everything | Agencies and teams running many channels | all agents | `install.sh <project> --pack full` |
<!-- AUTO:packs:end -->

Rules of thumb:
- Start small: core plus the channels you actually spend on. Add `creative-strategy` and `video-studio` once you run video or paid social. Add `lifecycle-crm` once you have customers who consented to email or SMS.
- A starter budget (under about $3k per month) rarely needs more than two paid channels.
- Packs only decide what gets copied. The orchestrator still activates agents per project in `ads-master/HEARTBEAT.md`.

## 3. Install

**A. Plugin (all projects)**
```text
/plugin marketplace add erolumut/Ads-Master
/plugin install ads-master@ads-master
/plugin install workflow-kit@ads-master        # optional: model routing, parallel sessions, prompts
```

**B. Copy into one project**
```bash
git clone https://github.com/erolumut/Ads-Master.git ~/ads-master
~/ads-master/scripts/install.sh /path/to/project --pack ecommerce-dtc          # a pack
~/ads-master/scripts/install.sh /path/to/project --only meta-ads,storefront-ux # or hand picked agents
~/ads-master/scripts/install.sh /path/to/project --pack b2b-saas --kit workflow # plus the Workflow Kit
~/ads-master/scripts/install.sh /path/to/project --update                      # later: refresh playbooks, workspace untouched
```

**C. This repo as the workspace:** open it in Claude Code and run `/ads-setup`.

## 4. What `/ads-setup` does

It creates the project's growth brain in `ads-master/` and fills it with what it can learn on its own, then asks you only for what it cannot. Nothing is spent, published or changed in any account.

1. **Creates the workspace** from the template (never overwrites existing files).
2. **Protects secrets and data:** proposes `.gitignore` lines for exports and `.env`, and a `.env.example` with placeholders.
3. **Scans the codebase:** site platform and rendering, analytics and pixels, server side events, consent tool, robots, sitemaps and AI crawler rules, structured data, feeds, CRM, email and SMS tools, mobile app setup, deploy and release setup, and product facts and claims already on the site.
4. **Asks up to eight questions:** business model, the goal and its hard limit, markets, budget, order or deal value and margin, what counts as a conversion and where the truth lives, which accounts and tools exist, and regulated claims.
5. **Does the math:** breakeven ROAS and target CPA from your margins.
6. **Sets the guardrails:** automation stage (starts at 1, read only) and money caps in `GUARDRAILS.md` and `guardrails.json`.
7. **Activates agents** in `HEARTBEAT.md` from rules (website, catalog, channels, B2B, app) and shows you the list.
8. **Links your CLAUDE.md** with a short block (with your approval).
9. **Checks the guard hooks** and the available connectors, recommending read only access first.
10. **Writes a setup report** and the first journal entry, and recommends the first step (usually a full growth audit, or a measurement audit if tracking looks broken).

The files it creates and why:

| File | Why it exists |
|------|---------------|
| `PROJECT_BRIEF.md` | The business facts every agent reads first |
| `MEASUREMENT.md`, `METRICS.md` | Where the truth lives and one definition per metric |
| `GUARDRAILS.md`, `guardrails.json` | Automation stage, money caps, approvers (the hooks enforce the JSON) |
| `STRATEGY.md`, `PRIORITIES.md`, `HEARTBEAT.md` | Quarter goals, this week's work, who runs when |
| `BRAND.md`, `AUDIENCE.md`, `COMPETITORS.md` | Voice, customers, rivals |
| `brand/PRODUCT_FACTS.md`, `brand/CLAIMS.md` | What is provably true and what may be said |
| `VERIFIED.md` | Claims verified for this project, with evidence and expiry |
| `EXPERIMENTS.md`, `DECISIONS.md`, `INCIDENTS.md` | Tests, decisions with reasons, stop conditions |
| `creative-library/registry.csv` | Every creative with its name, metadata and learning |
| `memory/`, `journal/`, `outputs/`, `logs/`, `data/imports/` | Earned learnings, shared log, deliverables, audit trail, your exports |

## 5. Wiring it into your CLAUDE.md

`/ads-setup` adds this block (between markers so a refresh can update it). Keep it short; the details live in the skills.

```markdown
<!-- ads-master:start -->
## Growth agents (Ads Master)
Project growth state lives in `ads-master/`. Before any marketing, ads, SEO, AI search, storefront, pricing, tracking or landing page task, read `ads-master/PROJECT_BRIEF.md` and `ads-master/MEASUREMENT.md`.
For multi channel work, load the `growth-orchestrator` skill and delegate to the specialist agents it names.
Safety policy: `ads-master/GUARDRAILS.md`, enforced by the Ads Master guard hooks. Agents never change live accounts, spend, message customers or publish without explicit approval.
<!-- ads-master:end -->
```

Tips: if your CLAUDE.md is long, move area specific rules into path scoped files under `.claude/rules/` (the Workflow Kit's `instructions-budget` skill explains how). Do not paste playbook content into CLAUDE.md.

## 6. Day to day

- **Ask in plain language.** "Audit our Meta account", "Prepare our first launch", "Audit the store and fix the basics", "Make three hook variants of the winning video", "What price and minimum basket should we use?", "Can we say high protein in our Dutch ads?". The orchestrator routes multi agent work; single domain asks go straight to the specialist.
- **Approvals.** Agents produce audits, plans and change requests. You approve line by line. The hooks enforce what the automation stage allows.
- **Rhythm.** `/ads-review daily` (the daily report), `/ads-review weekly` (learning loop and priorities), monthly (reallocation, platform changes, verification pass), quarterly (strategy reset and full audits). Schedule them with `/loop`, a Routine or CI.

## 7. Recommended additions to your own flow (suggestions only; your project decides)

| Suggestion | Why | Effort |
|-----------|-----|--------|
| Run `/ads-review daily` at the start of the working day | Numbers every day, decisions on 3 and 7 day windows | 5 minutes |
| Make "launch readiness" a gate before any campaign goes live (orchestrator workflow) | Tracking, store, offer and claims green before spend | Built in |
| Route every customer facing text through `compliance` | Claims and price display mistakes are expensive | Built in |
| Put `site-engineer` release QA in your release checklist | Preview, smoke tests and rollback for every site change | Low |
| Keep `automation_stage` at 1 or 2 for the first month | Trust is earned with clean change requests | None |
| Add the monthly verification pass (`ads-verify`) | Turns Unverified claims into checked facts for your accounts | 30 minutes per month |
| Adopt the Workflow Kit's model routing | Opus for judgment, Sonnet for research and bounded edits, Haiku for lookups, Fable for second opinions: lower cost, same quality | Low |
| Adopt the parallel session ledger if you run several Claude sessions | Prevents sessions from overwriting each other | Low |
| Write sprint or phase prompts with the 7 block template | New sessions understand intent, scope and done | Medium |
| Log decisions in `ads-master/DECISIONS.md` | Future agents do not undo a deliberate choice | Low |

## 8. Agent catalog

<!-- AUTO:agents:start -->
| Agent | What it does | Packs | Model |
|-------|--------------|-------|-------|
| `ai-search-optimization` | AI search visibility (GEO, AEO, LLMO) specialist for ChatGPT search and shopping, Google AI Overviews and AI Mode, Gemini, Perplexity, Copilot, Claude, Meta AI and Grok. | ecommerce-dtc, lead-gen-local, b2b-saas, ai-visibility | inherit |
| `chatgpt-ads` | ChatGPT Ads (OpenAI Ads Manager, ads.openai.com) and cross surface strategy for AI assistant ads (Google AI Overviews and AI Mode, Microsoft Copilot, Amazon Alexa for Shopping prompts,... | b2b-saas, ai-visibility | inherit |
| `commerce-feeds` | Product feed and catalog specialist for Google Merchant Center, Meta and TikTok catalogs, Microsoft Merchant Center, Pinterest and Snapchat, plus AI shopping and agentic commerce (ChatGPT... | ecommerce-dtc, marketplace-seller | inherit |
| `compliance` | Claims and policy gate for all customer facing material. | core | inherit |
| `creative-strategy` | Cross channel creative strategist for Meta, TikTok, YouTube, Google assets, LinkedIn and ChatGPT ads. | ecommerce-dtc, marketplace-seller, lead-gen-local, b2b-saas, mobile-app | inherit |
| `cro` | Conversion rate optimization and landing page specialist for paid and organic traffic. | ecommerce-dtc, lead-gen-local, b2b-saas | inherit |
| `google-ads` | Google Ads operator for Search, AI Max, Performance Max, Demand Gen, YouTube, Shopping, Display, App, Local and ads in AI Overviews and AI Mode. | ecommerce-dtc, lead-gen-local, b2b-saas, mobile-app | inherit |
| `growth-orchestrator` | Growth strategist for the Ads Master system. | core | inherit |
| `lifecycle-crm` | Retention and lifecycle specialist for email, SMS, RCS, WhatsApp, push and in-app (Klaviyo, Braze, Customer.io, Iterable, Omnisend, Mailchimp, Attentive, Postscript, HubSpot). | ecommerce-dtc, lead-gen-local, b2b-saas, mobile-app | inherit |
| `linkedin-ads` | LinkedIn Ads specialist for B2B paid social in Campaign Manager. | b2b-saas | inherit |
| `market-intel` | Competitor and market intelligence for paid media, SEO and AI search. | ecommerce-dtc, marketplace-seller, lead-gen-local, b2b-saas, mobile-app, ai-visibility | inherit |
| `marketplaces` | Marketplace channel operator for Amazon (Seller Central, Vendor Central, Amazon Ads, DSP basics), bol.com, Trendyol, Hepsiburada, Allegro, Zalando, Etsy, eBay, Walmart, noon and Amazon in... | marketplace-seller | inherit |
| `measurement` | Measurement and tracking engineer for paid media. | core | inherit |
| `meta-ads` | Meta advertising specialist for Facebook, Instagram, Threads, WhatsApp, Messenger and Audience Network. | ecommerce-dtc, lead-gen-local, mobile-app | inherit |
| `microsoft-ads` | Microsoft Advertising specialist for Bing, Yahoo, AOL, DuckDuckGo, Edge, Microsoft Copilot and the Microsoft Audience Network. | lead-gen-local, b2b-saas | inherit |
| `mobile-app-growth` | Mobile app growth specialist for iOS and Android. | mobile-app | inherit |
| `offer-strategy` | Offer, pricing and merchandising strategist. | ecommerce-dtc, marketplace-seller, b2b-saas | inherit |
| `pricing-strategy` | Commercial pricing consultant. | ecommerce-dtc, marketplace-seller, b2b-saas, mobile-app | inherit |
| `seo` | SEO specialist for Google and Bing in the AI Overviews and AI Mode era. | ecommerce-dtc, lead-gen-local, b2b-saas, ai-visibility | inherit |
| `site-engineer` | Website engineering and release QA for Shopify themes, WordPress and WooCommerce, Next.js and headless storefronts and Webflow. | ecommerce-dtc, lead-gen-local, b2b-saas, ai-visibility | inherit |
| `storefront-ux` | Ecommerce storefront UX and implementation specialist. | ecommerce-dtc | inherit |
| `tiktok-ads` | TikTok advertising specialist for TikTok Ads Manager, Smart+, GMV Max and TikTok Shop ads, Spark Ads, TikTok One creators, Search Ads, lead gen and app campaigns. | ecommerce-dtc, mobile-app | inherit |
| `video-studio` | Video ad production agent for Meta Reels, Stories and Feed, TikTok, YouTube Shorts, in-stream and Demand Gen, LinkedIn and CTV. | ecommerce-dtc, mobile-app | inherit |
<!-- AUTO:agents:end -->

## 9. Skill catalog

<!-- AUTO:skills:start -->
| Skill | Use it for |
|-------|-----------|
| `ads-review` | Run the Ads Master operating rhythm (the heartbeat) for the current project. |
| `ads-setup` | Install or refresh the Ads Master project workspace (the ads-master/ folder) in the current project. |
| `ads-verify` | Turn uncertain claims into certain ones. |
| `ai-search-optimization` | AI search visibility (GEO, AEO, LLMO, AI SEO) playbook for getting a brand, its products and content mentioned, recommended and cited by ChatGPT search and shopping, Google AI Overviews and... |
| `chatgpt-ads` | Run ChatGPT Ads (OpenAI Ads Manager at ads.openai.com, Advertiser API) and plan AI assistant ad surfaces (Google ads in AI Overviews and AI Mode, Microsoft Copilot ads, Amazon Alexa for... |
| `commerce-feeds` | Product feeds and catalogs as a growth lever. |
| `compliance` | Claims and policy gate for every customer facing word, image and offer (ads, landing and product pages, emails, SMS, feeds, videos, creator posts, app store listings). |
| `creative-strategy` | Cross channel ad creative strategy, production and analysis for Meta (Facebook, Instagram, Reels), TikTok, YouTube and Shorts, Google RSA, Performance Max and Demand Gen assets, LinkedIn... |
| `cro` | Conversion rate optimization (CRO) and landing pages for paid and organic traffic. |
| `google-ads` | Google Ads playbook for auditing, launching, optimizing, scaling and recovering accounts across Search, AI Max for Search, Performance Max, Demand Gen, YouTube, Shopping, Display, App,... |
| `growth-orchestrator` | Conductor playbook and default entry point for the Ads Master growth system. |
| `lifecycle-crm` | Retention and lifecycle marketing (CRM) for email, SMS, RCS, WhatsApp, push and in-app. |
| `linkedin-ads` | LinkedIn Ads playbook for B2B paid social in Campaign Manager. |
| `market-intel` | Competitor and market intelligence playbook for paid media, SEO and AI search. |
| `marketplaces` | Marketplace channel playbook for selling and advertising on Amazon (Seller Central, Vendor Central, Brand Registry, A+, Brand Store, Featured Offer or Buy Box, FBA vs FBM, Vine, Amazon Ads... |
| `measurement` | Measurement, tracking and attribution playbook for paid media and growth. |
| `meta-ads` | Meta advertising playbook for Facebook, Instagram, Threads, WhatsApp, Messenger and Audience Network via Ads Manager and the Marketing API. |
| `microsoft-ads` | Microsoft Advertising (Bing Ads) playbook for Bing, Yahoo, AOL, DuckDuckGo, Edge, Microsoft Copilot ad placements and the Microsoft Audience Network. |
| `mobile-app-growth` | Mobile app growth playbook for iOS and Android. |
| `offer-strategy` | Offer strategy, pricing and merchandising economics. |
| `pricing-strategy` | Commercial pricing consultant playbook. |
| `seo` | Search engine optimization playbook for Google and Bing in the AI Overviews and AI Mode era. |
| `site-engineer` | Website engineering, release QA and rollback for the sites and storefronts growth work touches. |
| `storefront-ux` | Ecommerce storefront UX and implementation playbook. |
| `tiktok-ads` | TikTok advertising playbook for TikTok Ads Manager and TikTok Shop. |
| `video-studio` | Video ad production studio that turns creative briefs into finished, platform ready ad files for Meta Reels, Stories and Feed, TikTok, YouTube Shorts, in-stream and Demand Gen, LinkedIn and... |
<!-- AUTO:skills:end -->

## 10. Kits (plug and play add ons)

<!-- AUTO:kits:start -->
| Kit | Version | What it is | Agents | Skills | Path |
|-----|---------|-----------|-------:|-------:|------|
| `workflow-kit` | 1.0.0 | Plug and play working rituals for Claude Code projects: model routing and delegation, parallel sessions with a ledger, sprint and delegation prompts, plan first sessions, session start and handover, decision logs with... | 9 | 9 | `kits/workflow-kit` |
<!-- AUTO:kits:end -->

Install the Workflow Kit on its own in any project, Ads Master or not:

- As a plugin: `/plugin marketplace add erolumut/Ads-Master`, then `/plugin install workflow-kit@ads-master`. Agents are namespaced (`workflow-kit:scout`).
- By copy: `scripts/install.sh <project> --kit workflow --no-workspace --no-hooks`. Agents and skills land in `.claude/agents` and `.claude/skills`, scripts and templates in `.claude/workflow-kit/`.
- Then paste `templates/CLAUDE-snippet.md` into the project CLAUDE.md, merge `templates/settings-snippet.json` into `.claude/settings.json` by hand, and, if you want git hooks, copy `templates/githooks/` to `.githooks/` and run `git config core.hooksPath .githooks`.

What it gives you: model routing (scout, data-extractor and log-triage on `haiku`; researcher and mechanic on `sonnet`; verifier and reviewer on `opus`; fable-advisor on `fable`), a parallel sessions ledger, sprint and delegation prompts, a plan first session, session start and handover rituals, a decision log with placeholder numbering, a CLAUDE.md budget check, review guardians, validate only git hooks, a workflow YAML linter and a commit time invariants check. Every script exits 0 pass, 1 fail, 2 could not run, and names what it cannot cover.

In this repo, `python3 scripts/link_dev.py` links the Ads Master agents and skills plus every kit into `.claude/`, so all of them load here too. `validate.py` checks the links.

The patterns behind the kit and where each one came from: [docs/WORKFLOW_PATTERNS.md](WORKFLOW_PATTERNS.md).

## 11. Making uncertain claims certain

Every playbook claim carries an evidence label. `[Unverified]` and `[Contested]` claims are hypotheses. The `ads-verify` skill climbs an evidence ladder (live account read, official source, two independent dated sources, controlled test) and records the result in `ads-master/VERIFIED.md`, which every agent trusts over the playbook for that project. In this repo, `python3 scripts/unverified_report.py` lists the global queue by package.

Three habits make numbers certain, not just claims:
- Measure before quote: every figure in a report is recomputed from its source for that date range, never copied from notes or an earlier report.
- Ratios (ROAS, CAC, MER, POAS) are recomputed from summed numerators and denominators, never averaged (`METRICS.md` marks each metric's additivity).
- A check that could not run is reported as "could not run", never as green. Each script names what it cannot cover.

## 12. Updating and extending

- New playbook versions: `/plugin update` or `install.sh <project> --update`.
- Adding an agent: follow `docs/AUTHORING_SPEC.md`, add it to a pack in `docs/packs.json`, then run `python3 scripts/build_docs.py` and `python3 scripts/validate.py`. This guide updates itself.

## 13. Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| "Ads Master guard: ... automation stage 1" | The project is read only | Draft the change request, or raise the stage in `guardrails.json` (a human edit) |
| Guard never fires | No `ads-master/` workspace, or Python 3 missing | Run `/ads-setup`; install Python 3 |
| Plugin install fails | Private repo or no git credentials | Make sure your git credentials can read the repo |
| Agents cite outdated features | Platforms changed | Run the skill's Freshness Protocol or `ads-verify` |
