# Tools, APIs and MCP Servers

> What Claude can use to build, preview, test and release sites, with the gate each operation falls under. Prefer narrow tools over generic ones (`docs/GUARDRAILS_MODEL.md`). Versions and availability as of 2026-10; check each tool's changelog before relying on flags.

## 1. Tool inventory by job

| Job | Tool | What Claude can do | Gate | Notes |
|-----|------|--------------------|------|-------|
| Shopify theme dev and release | Shopify CLI 4.x (`@shopify/cli`, 4.9.0 on 2026-10-08) | `theme dev`, `check`, `pull`, `push --unpublished`, `share`, `preview --overrides`, `duplicate`, `profile`, `list`, `info` | G0 to G2; `publish`, `push --live`, `push --publish`, `dev --allow-live` are G3; `theme delete`, `store delete` G4 | Non-interactive use needs explicit target flags; JSON output with `--json` |
| Shopify store data | `shopify store auth` and `shopify store execute` (public since 2026-07) | Admin GraphQL reads; mutations with `--allow-mutations` | Reads G0; mutations G3 | Request minimal scopes in `store auth --scopes` |
| Shopify docs and validation | Shopify AI Toolkit plugin (skills `shopify`, `ucp`), Shopify Dev MCP (`@shopify/dev-mcp`) | Search docs and schemas, validate GraphQL, Liquid and UI extension code | G0 | Telemetry on by default, including the latest user prompt on Claude Code when a Shopify skill activates; opt out with `~/.config/shopify-ai-toolkit/opt-out` before client work |
| Shopify storefront as AI agents see it | Storefront MCP endpoint `https://<shop>.myshopify.com/api/mcp` | Query catalog and cart as a shopping agent would | G0 | QA for `ai-search-optimization` and `commerce-feeds`; never place orders |
| Hydrogen | Shopify CLI `hydrogen` commands, Oxygen deployments | Dev, build, preview deployments | Preview G2; production G3 | Hydrogen 2026.4.x on React Router 7.16 |
| WordPress | WP-CLI with aliases (`@staging`, `@prod`) | Inventory, backups, updates on staging, search replace dry runs | Reads G0; staging writes G2; production writes G3; deletes G4 | Guard does not yet recognize `wp @prod` writes; state the gate |
| WordPress and WooCommerce for agents | Abilities API (core since 6.9), MCP adapter, WooCommerce domain abilities | Expose site capabilities to MCP clients | Configuration is L4; reads G0; writes G3 | Security review for exposed abilities and roles |
| Vercel | Vercel CLI and REST API | `vercel deploy` (preview), `vercel ls`, `vercel inspect`, `vercel env pull`, `vercel logs`; `--prod`, `promote`, `rollback`, `rolling-release` | Preview G2; production changes G3 | Guard maps `promote` and `rollback` to G2 today; treat as G3 |
| Netlify | Netlify CLI and API | `netlify deploy --alias` (preview), `netlify status`; `--prod` and restore deploy | Preview G2; production G3 | |
| Cloudflare | Wrangler | Preview deployments; `deploy`, `rollback` | G3 for production | |
| Webflow | Webflow MCP server (remote at `developers.webflow.com/_mcp/server`, OAuth; or local, Node 22.3+), Data API v2 | Read and edit elements, styles, CMS, custom code; publish | Reads G0; Designer edits on staging G2; publish G3 | Site managers and above authorize; single page publish via API since 2026-04 |
| Browser automation | Playwright 1.64 (2026-10-07), Playwright MCP, `playwright-cli`, Playwright Test Agents (`npx playwright init-agents --loop=claude`) | Smoke, visual, a11y, tracking and redirect tests; exploratory QA | G0 against previews and read only live checks | Never submit checkout on a live store |
| Browser diagnostics | Chrome DevTools MCP (stable with Chrome 149, 2026-06-02) | Performance traces with named insights, network and console inspection, emulation (CPU, network, device), Lighthouse audits (since v0.19, 2026-03) | G0 | Requires Chrome stable and Node 20.19+; tool names change between versions |
| Safari diagnostics | Safari Web Inspector (USB), Safari 27 built in MCP server for coding agents | iOS specific debugging | G0 | MCP availability from WWDC26 coverage [Secondary; verify] |
| Performance | Lighthouse 13, Lighthouse CI (`@lhci/cli`), PageSpeed Insights API, CrUX API, `web-vitals` library | Lab and field metrics, CI budgets | G0 | Lighthouse 13 changed audit IDs; update parsers |
| Accessibility | axe-core with `@axe-core/playwright`, Lighthouse accessibility category | Automated WCAG checks | G0 | Automated checks catch a minority of issues; add keyboard tests |
| Links | lychee, linkinator, the Playwright link template | Broken links, redirect chains | G0 | |
| Structured data | Rich Results Test, Schema Markup Validator, JSON-LD extraction test | Validate markup | G0 | Strategy belongs to `seo` |
| Visual regression | Playwright screenshots, Percy, Chromatic, Argos, Applitools | Diffs on previews | G0 | Same rendering environment for baselines |
| Real devices | BrowserStack, LambdaTest, Sauce Labs, physical devices | iOS and Android, in-app browser approximations | G0 | In-app browsers need real apps on real devices |
| Security | gitleaks, trufflehog, `npm audit`, `osv-scanner`, Socket, Dependabot, `scan_injection.py` | Secret, dependency and injection scans | G0 | Never print secrets found; report location only |
| Launch QA | `url_check.py` (this skill's scripts folder) | Redirects, parameter survival, UTM hygiene, macros, noindex | G0 | Standard library only |
| CI | GitHub Actions, GitLab CI | Run suites on previews | Adding or changing CI that deploys is L4 and needs human approval | Pin actions; secrets in CI secret stores |

## 2. Data access matrix (what to ask the human for)

| Need | Preferred access | Fallback |
|------|------------------|----------|
| Shopify theme files | Theme Access app password (themes only) in `SHOPIFY_CLI_THEME_TOKEN` | Theme export zip from the admin |
| Shopify product and order data for QA | `store auth` with read only scopes (`read_products`, `read_inventory`); aggregated order data only | CSV export into `ads-master/data/imports/` |
| WordPress | SSH plus WP-CLI to staging; read only on production | Host backups, admin access to staging |
| Vercel or Netlify | A project scoped token with read access; preview protection bypass secret for CI | Dashboard screenshots of deployments |
| Webflow | MCP OAuth for one site; Data API token with `sites:read` | Staging URL and a backup name |
| Field performance | CrUX API key and PSI API key in env vars | PageSpeed Insights web UI screenshots |
| Ads entities for launch QA | Channel agent's change request and read back | Exports from ad platforms |
| Analytics for post release checks | GA4 or platform analytics via the measurement agent's connectors | Exports |

Never request owner or admin roles when a narrower role does the job. Record which access exists in `memory/site-engineer.md` under setup facts (no secrets).

## 3. Command cheat sheet with gates

```bash
# Shopify (G0 to G2)
shopify theme list --role live --json
shopify theme duplicate --theme "$LIVE_ID" --name "backup $(date +%F)" --force --json   # G2
shopify theme push --unpublished --theme "rc $(date +%F) <topic>" --strict --json      # G2
shopify theme push --development --development-context "pr-123" --json                # G2
shopify theme preview --theme "$RC_ID" --overrides qa/overrides.json --json           # G2
shopify theme check --fail-level error --output json                                  # G1
shopify theme profile --url /products/<handle> --json                                 # G0
# Shopify (G3, human approval): shopify theme publish --theme "$RC_ID"

# Vercel (G2 preview, G3 production)
vercel deploy --yes                       # preview
vercel ls --prod                          # record current production deployment
# G3: vercel deploy --prod | vercel promote <url> | vercel rollback <url>

# Netlify
netlify deploy --alias "rc-$(date +%Y%m%d)" --json      # preview
# G3: netlify deploy --prod

# WordPress
wp @staging plugin list --format=json
wp @staging db export "backups/$(date +%F_%H%M).sql"   # G2
wp @staging plugin update woocommerce --dry-run
# G3: wp @prod plugin update <slug>

# QA (G0)
npx playwright test -c qa/playwright.config.ts
npx @lhci/cli autorun
python3 -I skills/site-engineer/scripts/url_check.py qa/final-urls.txt --mobile --add-click-ids
python3 -I skills/site-engineer/scripts/scan_injection.py .
gitleaks detect --no-git -s . --redact
osv-scanner --lockfile=package-lock.json
```

Paths to this skill's scripts depend on the install (`.claude/skills/site-engineer/scripts/` in project installs).

## 4. MCP server hygiene

| Rule | Why |
|------|-----|
| List installed MCP servers and their scopes at the start of a task that will use them | Know what can write |
| Prefer read only tokens for audits and QA | Limits blast radius of a prompt injection or a wrong call |
| Treat any MCP publish, deploy, mutation or delete tool as G3 or G4 regardless of how the tool is named | The guard cannot always see inside MCP calls |
| Check vendor telemetry and data retention before using on client work | Prompts and code can leave the machine |
| Never paste credentials into MCP tool arguments when an OAuth or env based flow exists | Arguments can be logged |
| Record which servers were used in the output's "data used" section | Audit trail |

## 5. Evaluating a new tool (quick)

1. Official or community? Check the publisher, repository activity and maintenance status (same health check as [UI primitives and dependencies](ui-primitives-and-dependencies.md) section 5).
2. What scopes does it request, and can it run read only?
3. Does it send data to the vendor (telemetry, prompts, code)? Can it be disabled?
4. Does it fit the gate model (separate read and write tools, explicit publish)?
5. Record the decision in `DECISIONS.md` if adopted for a project.
