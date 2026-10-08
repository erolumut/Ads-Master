# Release Process and Rollback

> How every site change moves from idea to production and back again if needed. Platform loops live in [Shopify](shopify-theme-engineering.md), [WordPress](wordpress-woocommerce.md) and [Next.js, headless and Webflow](nextjs-headless-and-webflow.md). Checks live in [Automated QA](automated-qa-and-tests.md). Knowledge as of 2026-10.

## 1. Principles

1. Production is never the workspace. Every change starts on a branch, a development theme, a staging site or a preview deployment.
2. Every release has a recorded rollback target before anything is published: the live theme ID, the production deployment ID, the database backup file name, the Webflow backup name.
3. Publishing is G3. The agent prepares, the human publishes or approves the publish line by line in a change request. Previews and unpublished themes are G2.
4. A release is not done at publish. It is done when post release checks pass at T+15 minutes, T+2 hours and T+24 hours.
5. Rollback is a decision rule, not a debate. If a rollback trigger fires, restore first and investigate second.
6. Small batches. One release carries one theme of change. Mixed releases (new section plus app install plus tracking change) make root cause analysis impossible.
7. Freeze windows are real. No non-emergency releases in the 72 hours before a sale start, a campaign launch, a price change or BFCM week unless the human approves an exception in `DECISIONS.md`.

## 2. Risk lanes

Classify every change before planning it. The lane decides the checks and the approver.

| Lane | Examples | Required checks | Approver | Typical window |
|------|----------|-----------------|----------|----------------|
| L0 Content | Copy, image swap inside an existing section, blog post | Visual check on preview, link check, compliance check for claims | Content owner | Any business hour |
| L1 Template | New section, layout change, new landing page template | Full smoke tests, visual diff, a11y, Lighthouse, mobile device check | Site publishing approver | Tue to Thu, morning, low traffic |
| L2 Commerce logic | Cart drawer, variant picker, pricing display, discounts display, shipping messages | L1 plus add to cart and checkout handoff tests, price parity check vs feed and ads | Site approver plus offer owner | Tue to Thu, never in a sale week |
| L3 Tracking | Pixel, GTM container, consent banner, checkout extensions, web pixels | L1 plus event firing tests, dedup check, consent states, test order | Site approver plus `measurement` sign off | Same as L2; never on a Friday |
| L4 Platform | Theme migration, framework major upgrade, plugin major update, app install or removal, CDN or DNS change | Everything plus staged rollout or full regression, backup restore test | Human owner, written plan | Planned, announced, with on call coverage |
| L5 Security patch | Framework CVE, plugin vulnerability under active exploitation | Build, smoke tests, quick visual check; skip non-essential checks | Human owner (fast track) | As soon as possible, inside 24 hours for critical |

Rules of thumb:
- Anything that touches price, discount, shipping, tax, checkout or tracking is at least L2.
- Anything that changes what loads on every page (layout files, `theme.liquid`, root layout, header scripts) is at least L1 and gets a performance check.
- An app install is L4 on Shopify and WordPress: apps inject code you do not review.

## 3. The release pipeline (12 steps)

| # | Step | Gate | Output |
|---|------|------|--------|
| 1 | Intake: what, why, who asked, success metric, lane, deadline | G0 | Release brief in the change request draft |
| 2 | Snapshot production: record live IDs, take backup, export current settings | G0 to G2 | Rollback target recorded |
| 3 | Branch: `release/YYYY-MM-DD-<topic>` from the default branch | G1 | Branch name |
| 4 | Build locally: platform dev loop (`shopify theme dev`, `next dev`, `wp-env start`) | G1 | Working change on local preview |
| 5 | Automated checks locally: lint, theme check or type check, unit, smoke tests | G1 | Check log |
| 6 | Preview: unpublished theme, preview deployment, staging push | G2 | Preview URL, theme or deployment ID |
| 7 | QA on preview: release QA checklist (section 5), device tests, worst case data where relevant | G0 | QA report with PASS or FAIL per item |
| 8 | Change request: one line per change with rollback, risk and evidence | G1 | `CHANGE_REQUEST.md` filled |
| 9 | Approval: human approves line by line | Human | Approval reference (name, date, channel) |
| 10 | Publish in the approved window, by the human or by the agent at stage 4 after explicit approval | G3 | Publish timestamp, new live ID |
| 11 | Post release checks at T+15 min, T+2 h, T+24 h | G0 | Post release log |
| 12 | Release notes, journal entry, close the change request | G1 | `ads-master/logs/releases/` file, journal entry |

Never skip step 2. The most expensive incidents in this domain are rollbacks with no clean target (a theme edited in place, a database overwritten from staging, a deployment promoted with no record of the previous one).

## 4. Snapshot and rollback targets by platform

| Platform | Snapshot before release | Rollback action | Time to restore | Watch out |
|----------|------------------------|-----------------|-----------------|-----------|
| Shopify theme | `shopify theme list --role live --json` and record the ID; `shopify theme duplicate --theme <live id> --name "backup YYYY-MM-DD"`; `shopify theme pull --live` into a backup branch | Human publishes the previous theme (Online Store > Themes > Publish) or `shopify theme publish --theme <previous id>` with approval | 1 to 2 minutes | Theme library holds a limited number of themes (20 per store at the time of writing [Official, verify]); delete old backups only with approval (theme delete is G4 for agents) |
| Shopify settings outside the theme | Screenshot or export: checkout settings, shipping, markets, discounts, app embeds, navigation | Re-apply manually from the snapshot | 5 to 30 minutes | Not versioned by Shopify; your snapshot is the only record |
| WordPress or WooCommerce | `wp db export` with timestamp, `wp plugin list --format=json`, host snapshot of files and database | Restore files and database pair, or roll back one plugin with `wp plugin install <slug> --version=<old> --force` | 5 to 60 minutes | Never restore a database over a live store without exporting new orders first; orders placed after the backup would be lost |
| Next.js on Vercel | `vercel ls --prod` or the dashboard: record the current production deployment URL and ID | Instant Rollback to the recorded deployment (dashboard or `vercel rollback <url>`), human approved | Seconds | A rollback can stop production domains from auto-assigning on later deploys; promote explicitly afterwards [Official, 2023-12] |
| Netlify | Record the published deploy ID | Publish the previous deploy from the deploys list (or the API), human approved | Seconds | Locked publishing stops auto publishes until unlocked |
| Cloudflare Pages or Workers | Record the deployment ID | Roll back to the previous deployment in the dashboard or `wrangler rollback` (G3) | Seconds | Workers secrets and bindings are not rolled back with code |
| Webflow | Create a named manual backup (wait for "Changes saved" first) | Restore the backup, then publish (human) | Minutes | Restoring a historical backup can reset CMS, Ecommerce, Page and Asset IDs for older backups; CMS item deletions are not rolled back by publishing [Official and practitioner, 2026] |
| GTM container | Export the live container version number | Publish the previous container version | 1 minute | Owned with `measurement`; never publish a container from this agent |
| DNS or CDN | Export zone records, page rules, cache rules | Re-apply records; TTL decides speed | Up to TTL | L4 only; keep TTL low (300 s) for 24 hours before a planned change |

## 5. Release QA checklist (run on the preview, every L1 to L4 release)

Mark each item PASS, FAIL or N/A with evidence (screenshot, log line, test report).

| # | Check | How | Fail means |
|---|-------|-----|-----------|
| 1 | Build and static checks green | CI log; `shopify theme check --fail-level error`, `tsc --noEmit`, lint | Stop |
| 2 | Smoke tests green on desktop and mobile projects | Playwright report ([Automated QA](automated-qa-and-tests.md) templates) | Stop |
| 3 | Visual diff reviewed; every changed screenshot explained | Playwright `toHaveScreenshot` diff or visual service | Stop until explained |
| 4 | Accessibility: zero new serious or critical axe violations on changed templates | `@axe-core/playwright` | Stop for new critical |
| 5 | Performance: lab LCP and TBT within budget; no new render blocking resource; JS weight within budget | Lighthouse CI assertions ([Performance](performance-and-third-party-scripts.md)) | Stop or approved exception |
| 6 | Tracking: primary events fire once per action with correct value and currency | Network assertions; `measurement` sign off for L3 | Stop |
| 7 | Consent: banner shows, choices respected, no tags before consent where required | Test both accept and reject states | Stop |
| 8 | Prices, discounts, shipping messages match `PRODUCT_FACTS.md`, the feed and live ads | Parity check on top 10 SKUs | Stop |
| 9 | Mobile device check on one real iPhone and one real Android | [Mobile web polish](mobile-web-polish.md) checklist | Stop for Broken items |
| 10 | Worst case data for new or changed components | [Worst case data testing](worst-case-data-testing.md) | Stop for Broken items |
| 11 | Links: no new 404s or redirect chains on changed pages | Link checker | Fix before publish |
| 12 | Structured data still valid on PDP and key templates; price in JSON-LD equals visible price | Rich Results Test or schema extraction test | Stop for PDP regressions; hand off to `seo` |
| 13 | Security: no secrets in diff, no new public endpoints, dependencies audited | [Security review](security-review.md) quick checklist | Stop |
| 14 | SEO safety: no accidental `noindex`, canonical unchanged, robots unchanged | View source on preview vs live | Stop |
| 15 | Copy and claims passed `compliance` for customer facing text | Compliance approval reference | Stop |

## 6. Change request lines for releases

Use `ads-master/templates/CHANGE_REQUEST.md`. One line per publish action. Example:

| # | Level | Entity | Current | Proposed | Why (evidence) | Expected impact | Risk | Rollback | Approve |
|---|-------|--------|---------|----------|----------------|-----------------|------|----------|---------|
| 1 | Site | Shopify theme | Live theme 150000000001 "Horizon prod 2026-09-30" | Publish theme 150000000777 "release 2026-10-08 sticky ATC" | QA report 2026-10-08 all PASS; test plan E014 | RPV +2% to 4% expected (cro estimate) | Medium (L2) | Publish 150000000001 again; backup 150000000778 duplicated 2026-10-08 09:10 | Y/N |
| 2 | Site | Shopify app embed | Reviews app embed off on product template | On | Required for new review stars | Neutral | Low | Toggle off | Y/N |

Then add: release window, who publishes, who watches post release checks, rollback triggers (section 7) and the success metric with its read date.

## 7. Rollback triggers (decide in minutes, not hours)

Restore the snapshot without waiting for root cause when any of these appear after a publish:

| Trigger | Threshold | Source |
|---------|-----------|--------|
| Checkout handoff or add to cart broken | Any reproducible failure on a top template | Smoke test rerun on live, customer report |
| Purchase or lead events stop or double | Zero events for 30 minutes during normal traffic, or count ratio vs backend over 1.3 | `measurement` dashboards, platform event managers |
| JS error spike | New error type on more than 1% of sessions, or console errors on cart and checkout pages | RUM, error tracker, Playwright `page.pageErrors()` |
| Conversion rate drop | Below 70% of the same hours last week for 2 consecutive hours with normal traffic | Analytics, backend orders |
| Wrong price, discount or shipping live | Any | Parity check |
| Field or lab performance collapse | LCP or INP worse by more than 50% on key templates | Lighthouse on live, RUM |
| Layout broken on a major device class | Any Broken item on iPhone or Android | Device check |

After a rollback: write an `INCIDENTS.md` row, a journal entry, and keep the failed theme or deployment for investigation. Never delete it.

## 8. Post release checks

| When | What |
|------|------|
| T+0 (right after publish) | Load home, top collection, top PDP, cart, top paid landing page on live; run the smoke suite against production in read only mode (no checkout submission) |
| T+15 min | Event counts flowing in platform event managers and analytics; error tracker quiet; no customer service flags |
| T+2 h | Conversion rate and add to cart rate vs same hours last week; JS errors; Core Web Vitals in RUM if available |
| T+24 h | Orders or leads vs backend; field data trend starts (CrUX needs 28 days for a full window); close the change request or open an incident |
| T+7 d | Success metric early read handed to `cro` or the requester; release marked done in the release log |

## 9. Release notes (save to `ads-master/logs/releases/YYYY-MM-DD_<topic>.md`)

```markdown
# Release YYYY-MM-DD <topic>
- Lane: L2 | Platform: Shopify | Requested by: <slug or person> | Approved by: <name>, <date>, <channel>
- Live before: <theme or deployment ID and name> | Live after: <ID and name> | Backup: <ID or file>
- Published at: <ISO time, timezone> by <person or agent at stage 4 with approval ref>
## What changed
- <one line per change, file paths or settings>
## QA evidence
- Report: ads-master/outputs/site-engineer/YYYY-MM-DD_site-engineer_release-qa-<topic>.md
## Post release checks
- T+15: <result> | T+2h: <result> | T+24h: <result>
## Rollback
- Trigger list: section 7 of release-process-and-rollback.md
- Command or click path: <exact steps>
## Follow ups
- <handoffs, experiments, known issues>
```

Also write a journal entry `ads-master/journal/YYYY-MM-DD_HHMM_site-engineer_release-<topic>.md` so channel agents know URLs, templates or tracking changed.

## 10. Guard hook coverage for release commands (updated in Ads Master v1.1)

The Ads Master guard (`scripts/guard.py`) classifies Bash commands with regular expressions. A probe on 2026-10-08 against Shopify CLI 4.9 flags found gaps; v1.1 of the guard closes them (tests in `scripts/test_guard.py`).

| Command | Gate in the guard (v1.1) | Why |
|---------|--------------------------|-----|
| `shopify theme push --unpublished` or `--development` | G2 | Creates or updates a non live theme |
| `shopify theme push --theme <id>` without `--unpublished` or `--development` | G3 | The target could be the live theme |
| `shopify theme push ... --publish`, `-p`, `--live`, `--allow-live` | G3 | Publishes or overwrites live files |
| `SHOPIFY_FLAG_LIVE=`, `SHOPIFY_FLAG_PUBLISH=`, `SHOPIFY_FLAG_ALLOW_LIVE=`, `SHOPIFY_FLAG_ALLOW_MUTATIONS=` prefixes | G3 | Flags set through environment variables |
| `shopify theme dev --allow-live` or `-a` | G3 | Live reload writes to the live theme |
| `shopify theme duplicate`, `shopify theme share` | G2 | Creates a theme in the library |
| `shopify store execute` or `store bulk execute` with `--allow-mutations` | G3 | Admin GraphQL writes (products, prices, inventory) |
| `shopify store delete`, `shopify theme delete` | G4 | Destructive |
| `vercel --prod`, `vercel promote`, `vercel rollback`, `vercel rolling-release` | G3 | Changes what production serves |
| `vercel deploy` (preview), `netlify deploy` without `--prod` | G2 | Preview deploy |
| `netlify deploy --prod`, `netlify api restoreSiteDeploy` | G3 | Changes the published deploy |
| `wp @prod ...` or `wp ... --ssh=<host>` with a write subcommand | G3 | WP-CLI writes against production |
| `wp ... db drop` or `db reset` | G4 | Destructive |

The human can still add project specific rules in `guardrails.json` (human owned): `extra_blocked_bash_patterns` are evaluated before every built in rule; `extra_ask_bash_patterns` are evaluated after the built in G4 and G3 rules and before the built in G2 rules. If a release command is not covered, apply the stricter gate by judgment, state it in the change request, and ask the main session for a guard update. Never edit `guardrails.json` or the guard yourself.

## 11. Plays

### Play 1: Standard release (L1 or L2)
1. Intake and lane. 2. Snapshot (section 4). 3. Branch and build. 4. Push to an unpublished theme or preview deployment (G2). 5. Run section 5 QA on the preview URL. 6. Write the change request with rollback lines. 7. Human approves and publishes in the window. 8. Post release checks. 9. Release notes and journal.

### Play 2: Hotfix (live bug, not an incident)
1. Reproduce on live and on the last good theme or deployment. 2. If the last good version does not have the bug, propose rollback first (fastest fix). 3. Otherwise branch from the live state (pull the live theme first on Shopify), fix the smallest thing, run smoke tests and the failing check only. 4. Change request with "hotfix" label. 5. Publish with approval. 6. Add the missing test to the suite so it cannot regress.

### Play 3: Rollback
1. Confirm a trigger from section 7 with evidence. 2. Tell the human: trigger, evidence, rollback target, expected restore time. 3. Human approves (or performs) the restore. 4. Verify on live with the smoke suite. 5. Recommend pausing affected paid traffic if the destination was broken (the channel agent drafts the pause; the human approves). 6. Incident row, journal, keep the failed version.

### Play 4: Campaign launch day (site side)
1. T-5 days: landing pages built and on preview; launch QA dry run ([Launch QA for ads](launch-qa-for-ads.md)). 2. T-3 days: freeze begins for affected templates. 3. T-1 day: publish landing pages with approval; launch QA on live URLs with UTMs. 4. T-0: channel agents set entities live after human approval; run launch QA again within 30 minutes of first impressions. 5. T+1 day: event and order reconciliation with `measurement`.

### Play 5: Sale event (price and discount changes at a set time)
1. Prepare the sale theme or content as an unpublished theme or scheduled content. 2. Prepare discount and price changes as drafts (owned by `offer-strategy`, human approves). 3. Test the sale state on preview with the discount codes in a test checkout (no payment). 4. At start time the human publishes; the agent runs price parity checks on the top 20 SKUs within 10 minutes. 5. At end time revert, and run parity checks again (the expensive mistake is the sale price staying live).

### Play 6: Incident (checkout or destination broken)
Follow `ads-master/INCIDENTS.md`. Site specific order: stop writes, alert, rollback if a recent release is the likely cause, verify, preserve evidence (screenshots, HAR via Playwright trace, deployment logs), recommend pausing paid traffic to the broken URL, write the prevention rule (a new smoke test, a new guard pattern, a new checklist item).

### Play 7: Framework or plugin security patch (L5)
1. Read the advisory: affected versions, exploitation status, whether the hosting provider mitigates it. 2. Upgrade on a branch to the fixed version only (no unrelated upgrades). 3. Build, smoke tests, quick visual check. 4. Fast track approval. 5. Publish. 6. Confirm the deployed version (`next --version` in build logs, `wp plugin list`). Next.js runs a monthly security release program in 2026 with out of band releases for critical issues, so plan a recurring patch slot [Official, 2026-07 to 2026-09].

## 12. Release cadence by team setup

| Setup | Cadence | Who publishes | Minimum automation |
|-------|---------|---------------|--------------------|
| Solo founder | Batched weekly release, emergency fixes ad hoc | Founder in the admin | Theme check or build, 3 smoke tests, manual phone check |
| Small team (2 to 10) | Twice weekly windows | Named site owner | CI with smoke tests, Lighthouse CI, visual diff on 5 templates |
| Agency | Per client windows written in the SOW; client approves in writing | Client or agency lead with written approval | Shared test templates per platform, per client env files, release notes to client |
| In-house engineering | Continuous delivery with feature flags; marketing changes through the same pipeline | Engineering on call; marketing approves content | Full CI, preview per PR, rolling releases or canary, error budgets |
