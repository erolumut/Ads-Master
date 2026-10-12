# Admin panels and internal dashboards

Most admin panels look alike because they start from the same blocks with the same default tokens. Starting from a template is fine; shipping its defaults is the problem. Research date 2026-10-12. Labels: [Opened] read at the source (package.json, LICENSE, npm registry), [Reported] search results only, [Unverified] one weak source. No commit dates were readable for these repositories, so check activity on GitHub before adopting.

## 1. Starting points

| Option | Licence and price | Stack | Tables and charts | Takes your tokens | Notes |
|---|---|---|---|---|---|
| shadcn blocks (dashboard, sidebar) | MIT, free [Opened] | Radix and Base UI variants; Base UI default since 2026-07 [Reported] | TanStack Table, Recharts 3 | Easy (copied code, CSS variables) | The common baseline, and the source of the common look |
| Kiranism next-shadcn-dashboard-starter | MIT, free [Opened] | Next 16, React 19, Tailwind 4, Base UI, Clerk auth [Opened] | TanStack Table with URL state (nuqs), Recharts 3, cmdk and kbar | Easy | Ships an auth provider; check it against your own account rules before keeping it |
| satnaing/shadcn-admin | MIT, free [Opened] | Vite and TanStack Router, not Next.js; Tailwind 4, React 19 [Opened] | TanStack Table, Recharts 3 | Easy | Port the routing if your app is Next.js |
| ReUI | Free components reported MIT; Pro and Ultimate tiers proprietary [Reported]; repository shows no licence field [Opened] | Next 16, Tailwind 4, Base UI and Radix flavours [Opened] | Data Grid (TanStack Table plus Virtual plus dnd-kit), Kanban [Reported] | Easy (shadcn registry) | Best for heavy tables; read the licence of each item |
| Kibo UI | Reported MIT; moved to shadcnblocks [Reported] | shadcn registry | Table, Kanban, Gantt [Reported] | Easy | |
| Refine (`@refinedev/core` 5.2.0) | MIT [Opened] | Headless admin framework; shadcn registry integration [Reported] | Your choice | Easy (headless) | Data providers, auth and CRUD with little code |
| React Admin (5.15.4) | MIT [Opened] | MUI by default; a shadcn admin kit exists on its core [Reported] | Own datagrid | Medium (MUI theme), easier with the shadcn kit | Mature CRUD framework |
| Cloudflare Kumo (2.14.0) | MIT [Opened] | Base UI, `motion`, optional ECharts 6, Phosphor icons [Opened] | ECharts time series, Sankey, maps [Reported] | Semantic tokens [Reported] | The free option with a different base and look; young and fast moving |
| HeroUI v3 | MIT; Pro paid [Reported] | React Aria, Tailwind 4 | Bring your own | Easy through CSS variables | Different look from shadcn; see the catalog |
| Mantine 9 | MIT [Opened] | React 19.2+, no Tailwind | Mantine datatable ecosystem | Strong theming | Good when the project does not use Tailwind |
| TailAdmin free (2.4.0) | MIT, Pro paid [Opened] | Next 16, Tailwind 4, no base library [Opened] | ApexCharts, FullCalendar | Hard (own CSS, no token layer) | Quick demo, costly to make your own |
| Tremor Blocks | Repository Apache-2.0 with MIT parts [Opened]; free since Vercel acquired Tremor in 2025-01 [Reported] | The blocks site requires Tailwind 3.4 [Reported] | Recharts 2 | Medium | Check each block's Tailwind version before using it in a Tailwind 4 app |
| Untitled UI React dashboards | Base MIT; the 250+ dashboards are Pro, reported $2,499 business one time [Reported] | React Aria, Tailwind 4 | Not confirmed | Medium (strong look) | Polished, opinionated |
| coss (formerly Origin UI) | AGPL by default, MIT only in marked folders [Reported, conflicting] | Base UI | Copy in patterns | Easy technically | AGPL may rule it out; read the licence |

## 2. Pick per situation

| Situation | Pick |
|---|---|
| Internal tool for a small team | Refine or React Admin for CRUD, on a shadcn blocks or Kiranism base; or a plain Next build with TanStack Table when you want full control of density |
| Customer facing admin | Kiranism or shadcn blocks as the base, ReUI or Kibo for heavy tables, then the project's own tokens, type scale and density before anything ships |
| Analytics dashboard | shadcn charts on Recharts 3; Kumo or ECharts when you need Sankey, heatmaps or maps; see [Charts](charts.md) |
| Small app with an owner dashboard (one screen of stats) | No kit: hand drawn SVG charts and the app's own components, shared between apps as one internal package |

## 3. Make it feel crafted, not generic

Practitioner opinion, mostly from public design writing about Linear, Vercel and Stripe [Reported]:

1. **Replace the defaults first:** radius, neutral palette, type scale and chart colours. The sameness of template dashboards comes from these four.
2. **Density on purpose:** a smaller base size (13 to 14 px) and tighter rows for tools people use all day; details on hover or in a side panel, not in extra columns.
3. **Tabular numbers** wherever figures are compared (`font-variant-numeric: tabular-nums`), right aligned, same unit and rounding per column.
4. **Keyboard first:** a command palette on Cmd+K for create, search and navigation; single letter shortcuts shown in hover hints; visible focus rings that sticky headers never cover.
5. **Designed states:** empty, sparse, loading, error and no permission states, each with a next step; an empty inbox is a success message, not a blank.
6. **Perceptual colour:** status and chart colours chosen in a perceptual space (LCH or OKLCH) so they have even weight and pass contrast.
7. **URL is state:** filters, sort, page and the open record live in the URL so views can be shared and the back button works.
8. **Collapsible, resizable sidebar** with the current location obvious and labels in plain words.

## 4. Before adopting a starter

Run the [Vetting checklist](vetting-checklist.md): licence per file (several starters mix MIT, Pro and AGPL), the auth provider it ships with, chart and table libraries against the project's budget, and a keyboard pass through one real flow. Record the starter in the Ledger as `copied` with its origin and commit.
