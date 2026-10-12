# Charts: pick by situation, not by demo

Most small products need fewer chart libraries than they think. A sparkline or a progress ring is ten lines of SVG; a real dashboard needs one library, chosen once. Research date 2026-10-12. Sizes are min+gz for one line chart, React external, CSS excluded, measured with esbuild on 2026-10-12 [Opened, own measurement]; your route will differ, so measure with your own build. Licences, versions and dates from the npm registry [Opened].

## 1. Libraries

| Library (version, npm date) | Licence | Size | Accessibility | Notes |
|---|---|---|---|---|
| Recharts 3.10.1 (2026-07-25) | MIT | 107 KB | Keyboard layer on by default in 3.x [Reported, release notes]; animations and tooltip honour reduced motion [Opened, source] | Active; the base of shadcn charts and EvilCharts |
| shadcn charts | MIT [Unverified] | Recharts plus a thin wrapper | Examples set `accessibilityLayer` [Reported] | Copied into your repo, so you own the code and the re-skin |
| EvilCharts (evilcharts.com) | MIT on the GitHub page [Opened] | Recharts, some on ECharts [Reported] | Unknown | Registry reported at 49 components, mirrors list 5 or 6; read each component before copying |
| visx 4.0.0 (2026-06-11) | MIT | 15 KB for a line path and a scale | Nothing built in; you add ARIA | Low level SVG pieces; React 19 support in v4 [Opened, releases] |
| d3-shape | ISC | about 1.5 KB for `line()` [Opened] | You add it | Curves for hand drawn SVG |
| Apache ECharts 6.1.0 (2026-05-19) | Apache-2.0 | 168 KB tree shaken line, 383 KB full | `aria` module with auto description and decal patterns [Opened, source]; no reduced motion hook found | Heatmaps, Sankey, geo; import from `echarts/core` |
| uPlot 1.6.32 (2025-03-14) | MIT | 23 KB plus about 2 KB CSS | None (canvas) | Dense time series and zoom; single file; last release over 18 months ago |
| Chart.js 4.5.1 (2025-10-13) | MIT | 49 KB registered line, 70 KB `auto` | None (canvas): add `role="img"`, a label and a table | Familiar, no reduced motion handling |
| Observable Plot 0.6.17 (2025-02-14) | ISC | 90 KB | Emits ARIA labels and descriptions [Opened, source] | Good for exploratory and static charts |
| Unovis 1.7.1 (2026-09-29) | Apache-2.0 | 60 KB | No ARIA or reduced motion hooks found in core | Active, React 19 peer |
| Liveline 0.0.7 (2026-03-12) | MIT | 22 KB | Honours reduced motion, no ARIA [Opened, source] | Only for live, streaming charts; very young |
| Tremor `@tremor/react` 3.18.7 (2025-01-13) | Apache-2.0 | 239 KB | None found | Avoid for new work: React 18 peer, Recharts 2, no release since Vercel acquired Tremor (2025-01-22) and made Tremor Blocks free under MIT [Reported] |
| Nivo 0.99.0, Victory 37.3.6 | MIT | 106 KB, 81 KB | Focus options exist | Last releases in 2025; prefer active options |
| ApexCharts 8.1.0 (2026-10-11) | "SEE LICENSE IN LICENSE.md" | not measured | not checked | Read the licence before considering it |

## 2. Pick per situation

| Situation | Pick |
|---|---|
| Sparklines, progress rings, small personal stats in a mobile app | Hand drawn SVG: one `<polyline>` or `<path>` (d3-shape if you want curves); a ring is two `<circle>` elements with `stroke-dasharray` and `stroke-dashoffset`, rotated -90 degrees. No library earns its size here |
| One or two simple charts in a budgeted Next.js app | Hand drawn SVG or visx primitives |
| A real dashboard (reports, ads and growth numbers, admin) | shadcn charts on Recharts 3 (or EvilCharts after reading the component), loaded per route; one library for the whole app |
| Heatmaps, Sankey, geo | ECharts with `echarts/core` tree shaking |
| No framework, no build step | Hand drawn SVG templates or `createElementNS`; a pinned, vendored uPlot file only for thousands of points, zoom or live series, and only if the project allows a library |
| Live streaming values | Liveline or uPlot, with a text alternative |

## 3. Accessibility must haves for every chart

1. A text alternative: `role="img"` with an `aria-label`, or a visible one line summary of the trend ("Up 12% since May").
2. The same data as a real `<table>` (visible, behind a toggle, or linked with `aria-describedby`), required for canvas charts.
3. Keyboard reach: one tab stop, then arrow keys through points; no hover only tooltips.
4. Never colour alone: shape, pattern or direct labels, and 3:1 contrast against the background.
5. Reduced motion: no draw in or live tick animation under `prefers-reduced-motion`.

## 4. Numbers on charts

A chart is a number surface. The axis, rounding and totals follow the same source and date range rules as any figure the project shows; a chart that disagrees with the table beside it is a bug, not a styling issue.
