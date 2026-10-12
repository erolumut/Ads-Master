# UI Sources

<!-- Workflow Kit template. Copy to docs/UI-SOURCES.md and fill it once per project (ui-sourcing skill). The Profile tells every session what may come from outside; the Ledger records what did. Check it with: python3 <kit>/scripts/ui_sources_check.py docs/UI-SOURCES.md -->

> Owner: `<name>` · Last full review: `<YYYY-MM-DD>` · Stack profile: `<A to G from the skill's stack-profiles reference>`

## Profile

| Question | Answer for this project |
|---|---|
| Identity level | `<signature (looks like nobody else) / product (own tokens, standard patterns) / internal (speed over identity)>` |
| Direction doc | `<path to the design language or design rules this project reads first>` |
| Tokens live in | `<for example app/globals.css @theme, packages/design-tokens>` |
| Motion policy | `<CSS and Web Animations API only / motion allowed for springs and layout / none>` |
| Primitives | `<own components / Base UI / Radix / React Aria / platform dialog and popover>` |
| Icons | `<one set, for example lucide-react>` |
| Charts | `<none / hand drawn SVG / one named library>` |
| Budget | `<first load JS per route, or a perf budget file>` |
| Accessibility target | `<WCAG 2.2 AA, plus project rules>` |
| Reviewer | `<guardian or reviewer that checks a new source>` |

## Banned

Packages and sources this project never uses. The check fails if one appears in a package.json. Glob patterns work (`@mui/*`).

| Package | Why |
|---|---|
| `<package or pattern>` | `<reason, decision number>` |

## Watch

Extra package patterns that count as UI for this project, on top of the built in list (primitives, motion, charts, icons, overlays, carousels, maps, 3D, sound).

| Pattern | Why |
|---|---|
| `<package or pattern>` | `<reason>` |

## Ledger

One row per outside source that shaped shipped UI: an installed package, copied code, a paid kit, or a reference you adapted closely. Kind is `package`, `copied`, `paid kit`, `mcp` (a library served to the agent through an MCP server) or `reference`. Copied code needs an Origin URL, the files it landed in, and an origin comment in each file.

| Source | Kind | Version | Licence | Origin | Used in | Reviewed on | Reviewer | Notes |
|---|---|---|---|---|---|---|---|---|
| `<package or component name>` | `<kind>` | `<version or commit>` | `<MIT, ISC, Apache-2.0, paid: seats and terms>` | `<URL>` | `<paths, comma separated>` | `<YYYY-MM-DD>` | `<who>` | `<vetting result, adaptations made>` |
