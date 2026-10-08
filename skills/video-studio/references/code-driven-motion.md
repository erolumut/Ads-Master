# Code-driven Motion (HyperFrames and Remotion)

> Purpose: build ad videos as code (HTML or React compositions rendered frame by frame to video) so offers, product videos, UI demos, review cards, kinetic type and end cards can be versioned, localized and rendered in batches with exact, repeatable results. Versions checked on the npm registry on 2026-10-08: `hyperframes` 0.8.142 (published 2026-10-08), `remotion` 4.0.534 (2026-10-07).

## 1. When code-driven is the right mode

| Use code-driven for | Do not use it for |
|---------------------|-------------------|
| Offer videos, countdowns, price and end cards | Proof that needs a real person or real product use (film it) |
| Product hero with feature callouts (real product photos or footage inside) | Fake demonstrations of physical performance |
| Software UI walkthroughs (real UI rebuilt, or truthful imaginary UI) | Inventing UI capabilities that do not exist |
| Kinetic type hooks over real B-roll (hook packs) | Anything a phone video does better at Starter tier |
| Review cards, data stories, listicles | Charts with invented numbers |
| Catalog videos from a product feed | |
| Localization (text layers swap per language) | |
| End card libraries attached to footage edits | |

Rule: code renders the stage, the type and the UI. Real footage and real product photos carry the physical proof.

## 2. Tool choice

| Tool | Authoring | License (2026-10) | Distributed render | Fit |
|------|-----------|-------------------|-------------------|-----|
| HyperFrames (HeyGen) | Plain HTML, CSS, GSAP, Three.js, Lottie, CSS or WAAPI animation; `index.html` plays in a browser, no build step | Apache 2.0, no per-render fees, no commercial thresholds [Official, GitHub README] | Local, Docker (deterministic), HeyGen cloud render, self-deployed AWS Lambda | Agent first; default for new ad templates. Open sourced 2026-04-17 [secondary]; very active (daily releases) |
| Remotion | React components, `useCurrentFrame()` | Free for individuals, for-profit orgs up to 3 people, non-profits; otherwise Company License: Creators 25 USD per seat per month; Automators 0.01 USD per successful render with 100 USD monthly minimum (billed in blocks of 1,000 renders); Enterprise from 500 USD per month [Official, remotion terms on GitHub, 2026] | Remotion Lambda (mature), Cloud Run, Vercel | Teams already on React; large automated pipelines; the license note above changes with Remotion 5.0 [verify] |
| Motion Canvas | TypeScript generators, editor | MIT | No | Original project inactive (last npm release 3.17.2 on 2024-12-14); community fork Canvas Commons 0.4.0 (2026-09-24) [npm registry] |
| Revideo | Fork of Motion Canvas with render API | MIT | Self-hosted | 0.11.0 (2026-07-10) [npm registry]; smaller community |
| FFmpeg drawtext and overlays | Filter graphs | LGPL or GPL builds | Any | Simple text overlays and end cards on footage only |

Default: HyperFrames for new work in Claude Code (HTML is what agents write best, Apache 2.0, determinism built in). Use Remotion when the project already has Remotion code or a React design system, and check the license tier with the human (a company with 4 or more people needs a Company License; automation pipelines count as Automators).

## 3. HyperFrames recipes

Install and skills (Node.js 22 or later and FFmpeg required):

```bash
npx skills add heygen-com/hyperframes          # interactive picker; pick Core Skills
npx hyperframes skills update                  # agents and CI: installs exactly the core set from main
npx hyperframes init my-ad --resolution portrait-4k
npx hyperframes doctor                         # environment check
```

Creation workflows exposed as skills (router `/hyperframes`): `/product-launch-video` (from a URL, 30 to 90 s sweet spot), `/motion-graphics` (unnarrated under about 10 s: kinetic type, stat hit, logo sting, lower third; MP4 or transparent overlay), `/embedded-captions` (captions on talking-head footage), `/talking-head-recut` (overlays on interviews and podcasts), `/music-to-video` (beat-synced), `/faceless-explainer`, `/general-video`, `/remotion-to-hyperframes` [Official, GitHub README 2026-10].

Composition contract (from the HyperFrames core docs):
- Root element carries `data-composition-id`, `data-start`, `data-width`, `data-height`.
- Timed elements carry `class="clip"` plus `data-start`, `data-duration`, `data-track-index`.
- Animation runs on one paused GSAP timeline registered on `window.__timelines["main"]`.
- Every frame is a pure function of time: no `Date.now()`, no unseeded `Math.random()`, no network calls during render; load fonts, scripts and media from local files.
- Keep each `<video>` a direct child of the root; trim with `data-media-start` (saas-motion-kit lesson).
- Animate transforms and opacity; avoid tweening layout properties (top, left, letter-spacing).

Dev loop:

```bash
npx hyperframes lint                                   # composition errors
npx hyperframes check --json                           # lint, runtime, layout, motion, contrast, snapshots
npx hyperframes snapshot --at 0,1.5,6,13.5             # PNG stills at the hook, proof and end card
npx hyperframes preview                                # studio with live reload (human gate P5)
npx hyperframes render --quality delivery --resolution portrait-4k --output renders/C021_H01_4k.mp4
npx hyperframes render --docker --output renders/final.mp4        # deterministic output
npx hyperframes render --format webm --output overlays/endcard.webm  # transparent overlay for footage edits
```

Render flags that matter for ads [Official, CLI docs 2026-10]: `--format` (mp4, webm, mov, gif, png-sequence, hls; WebM and MOV carry transparency), `--fps` (default 30), `--quality` (draft, looks = CRF 16 default, delivery = high), `--resolution` (supersample to a preset: portrait-4k 2160 x 3840, landscape-4k, square-4k; aspect must match the composition), `--crf`, `--docker` (deterministic), `--workers` (1 to 24 Chrome workers, about 256 MB each), `--gpu` (hardware encode), `--video-frame-format png` for UI recordings.

Useful helpers in the same CLI: `npx hyperframes capture <url>` (tokens, fonts, logos, screenshots from a live site), `transcribe` (local whisper.cpp or Parakeet, word-level timestamps, SRT or VTT export), `tts` (local voice drafts), `remove-background` (VP9 alpha WebM or ProRes 4444 cutouts), `beats` (beat grid from the music track), `normalize-audio`, `add <block>` (catalog transitions, overlays, captions, charts).

Distributed and cloud rendering: `hyperframes lambda deploy|render|progress` deploys into your own AWS account; `hyperframes cloud render` uses HeyGen-hosted rendering (uploads the project: check the data policy first).

### Ad composition skeleton (9:16, 15 s offer video)

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>
  @font-face { font-family: "Brand"; src: url("assets/fonts/brand-latin-ext-800.woff2") format("woff2"); font-weight: 800; }
  html, body { margin: 0; background: #101114; }
  #root { position: relative; width: 1080px; height: 1920px; overflow: hidden; font-family: "Brand", sans-serif; color: #f5f3ee; }
  /* universal 9:16 safe box: x 65 to 888, y 288 to 1248 */
  .safe { position: absolute; left: 65px; top: 288px; width: 823px; height: 960px; }
  .hook h1 { font-size: 104px; line-height: 1.02; margin: 0; }
  .offer .price { font-size: 180px; font-weight: 800; }
  .cta { position: absolute; left: 65px; top: 1120px; width: 823px; font-size: 64px; }
</style>
</head>
<body>
<div id="root" data-composition-id="C021-offer-916" data-start="0" data-width="1080" data-height="1920">
  <video class="clip" data-start="0" data-duration="15" data-track-index="0" data-media-start="2.4"
         src="assets/footage/product-in-use.mp4" muted></video>
  <div class="clip safe hook" data-start="0" data-duration="2.6" data-track-index="1"><h1>Knees sore after 5k?</h1></div>
  <div class="clip safe proof" data-start="2.6" data-duration="8.4" data-track-index="1"><!-- callouts from PRODUCT_FACTS.md --></div>
  <div class="clip safe offer" data-start="11" data-duration="4" data-track-index="1"><div class="price">-20%</div></div>
  <div class="clip cta" data-start="11.6" data-duration="3.4" data-track-index="2">Shop the first pair</div>
  <audio class="clip" data-start="0" data-duration="15" data-track-index="5" src="assets/audio/licensed-track.wav"></audio>
</div>
<script src="assets/js/gsap.min.js"></script>
<script>
  const tl = gsap.timeline({ paused: true });
  // Frame 0 must already show the hook: animate scale and position, never opacity from 0 at t = 0.
  tl.fromTo(".hook h1", { scale: 1.12, y: 30 }, { scale: 1, y: 0, duration: 0.45, ease: "expo.out" }, 0);
  tl.fromTo(".offer .price", { scale: 0.6, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.4, ease: "back.out(1.6)" }, 11);
  tl.fromTo(".cta", { x: -40, opacity: 0 }, { x: 0, opacity: 1, duration: 0.35, ease: "power3.out" }, 11.6);
  window.__timelines = window.__timelines || {};
  window.__timelines["main"] = tl;
</script>
</body>
</html>
```

Notes: bundle GSAP locally (no CDN at render). Check the license of every animation library you bundle; GSAP was made free for commercial use in 2025 [Practitioner report, verify current license]. HyperFrames also supports composition variables and sub-compositions (see the `/hyperframes-core` skill); prefer them for variants when available, otherwise use the template build in section 6.

## 4. Remotion recipes

```bash
npx create-video@latest            # or: bun create video
npx skills add remotion-dev/skills # agent skills: /remotion-best-practices, /remotion-create, /remotion-render, /remotion-captions
npx remotion studio
npx remotion render Offer916 renders/C021_H01_4k.mp4 --props=variants/C021_H01.json --codec=h264 --crf=16 --scale=2
```

Composition pattern (props drive the variant):

```tsx
import {AbsoluteFill, OffthreadVideo, Sequence, staticFile, useCurrentFrame, interpolate} from 'remotion';
type Props = {hook: string; price: string; cta: string; footage: string};
export const Offer: React.FC<Props> = ({hook, price, cta, footage}) => {
  const f = useCurrentFrame();
  const s = interpolate(f, [0, 13], [1.12, 1], {extrapolateRight: 'clamp'});
  return (
    <AbsoluteFill style={{backgroundColor: '#101114'}}>
      <OffthreadVideo src={staticFile(footage)} muted />
      <Sequence durationInFrames={78}><h1 style={{transform: `scale(${s})`}}>{hook}</h1></Sequence>
      <Sequence from={330}><div className="price">{price}</div><div className="cta">{cta}</div></Sequence>
    </AbsoluteFill>
  );
};
// Root: <Composition id="Offer916" component={Offer} durationInFrames={450} fps={30} width={1080} height={1920} defaultProps={{...}} />
```

Remotion determinism rules [Official, Remotion docs "Flickering"]: animate only from `useCurrentFrame()`; components must render the same frame the same way every time and not depend on render order; use `random(seed)` instead of `Math.random()`; use `<OffthreadVideo>`, `<Img>`, `<Audio>` and `delayRender()` so the renderer waits for assets; wait for fonts before measuring text. `--concurrency=1` hides flicker but is slow and blocks Lambda.

Captions: `@remotion/captions` provides `createTikTokStyleCaptions()` (available from v4.0.216) to group word timestamps into caption pages; a high `combineTokensWithinMilliseconds` gives phrase captions, a low value gives word by word [Official docs]. Feed it word timestamps from Whisper, WhisperX, `hyperframes transcribe` or a hosted STT.

Lambda cost reference: Remotion's own examples (2048 MB, us-east-1, v4.0.381) show about 0.001 USD for the Hello World render and about 0.017 to 0.021 USD for a 1 minute video, plus S3 and data transfer, and the Company License fee on top [Official, Remotion docs].

## 5. Determinism and quality checklist (both tools)

| Check | Pass |
|-------|------|
| Every animated value is a function of time or frame | No timers, no `requestAnimationFrame` loops, no wall clock |
| Randomness seeded | Particle and noise effects use a seed stored in the variant JSON |
| Assets local and preloaded | Fonts, images, video, audio and scripts in `assets/`; no network at render |
| Fonts subset correct | latin-ext (or the market's script) bundled; glyph check for ş, ğ, İ, ı, ä, ö, ü, ß, ñ, ç and currency symbols |
| Same input, same output | Render twice with `--docker` (HyperFrames) or the same Remotion version; compare checksums for template releases |
| Render big, deliver small | 4K master, Lanczos downscale; pixel art downscale with `flags=area` |
| Frame 0 | Hook visible at t = 0 (no fade from black) |
| Text sizes | Minimum 40 px body and 56 px captions on a 1080 wide vertical delivery (scale up for the 4K master) |
| Safe zones | Layout uses the universal box or the target preset; QA overlay frame checked |
| Contrast | `hyperframes check` contrast pass or manual check; no pure #000 on #fff bands after compression |

## 6. Variant builds from one template

Keep one template per style and ratio, and a JSON file per variant. Dependency-free build with Python's `string.Template`:

```python
# build_variants.py: python3 -I build_variants.py template.html variants/ out/
import json, pathlib, string, sys
tpl = string.Template(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
out = pathlib.Path(sys.argv[3]); out.mkdir(parents=True, exist_ok=True)
for vf in sorted(pathlib.Path(sys.argv[2]).glob("*.json")):
    v = json.loads(vf.read_text(encoding="utf-8"))
    d = out / vf.stem; d.mkdir(exist_ok=True)
    (d / "index.html").write_text(tpl.substitute(v), encoding="utf-8")   # template uses $hook, $price, $cta, $footage
    print(d)
```

Then render each folder at 4K and deliver with the delivery script:

```bash
for d in out/*/; do id=$(basename "$d"); (cd "$d" && npx hyperframes render --quality delivery --resolution portrait-4k --output "../../renders/${id}_4k.mp4"); done
python3 scripts/ffmpeg_deliver.py render --input renders/<id>_4k.mp4 --targets universal916 --mode fit --stem <stem> --ver v1
```

Variant JSON keys come from the variant matrix ([Variants and testing handoff](variants-and-testing-handoff.md)): `hook`, `hook_visual`, `body_ver`, `cta`, `price`, `deadline`, `lang`, `claims_ids`. Never put a claim string in a variant file unless it is copied from `brand/CLAIMS.md` with its ID.

## 7. Fonts, scripts and languages

- Ship font files locally with the subsets the market needs (latin-ext for Turkish, Polish, Czech, Romanian; Cyrillic; Greek; Arabic and Hebrew need shaping-capable fonts and `dir="rtl"`; CJK fonts are large, subset by used glyphs).
- Uppercase display text: write it in uppercase in the source. CSS `text-transform: uppercase` and naive upper functions turn Turkish i into I instead of İ, and break the dotless ı. Set `lang` on the element per language. [saas-motion-kit, 2026]
- Text expansion: German, Finnish and Turkish lines run 20 to 35 percent longer than English [Practitioner consensus]; test the longest language first in the layout.
- Numbers, currency and dates in local format; prices from the local feed or `offer-strategy`, never converted by the agent.

## 8. Real UI: clean or imaginary

Score each candidate screen 0 to 2 on: current (shipped, not about to change), calm (one focal point), on brand (tokens, type, icons), shows the proof moment directly. 7 to 8: use the real UI; 4 to 6: use it simplified; 0 to 3: design a truthful imaginary component (adapted from the saas-motion-kit components rule).

- Capture tokens and copy with `npx hyperframes capture <url>`; rebuild key components in HTML so they stay sharp at 4K and can animate. Do not paste screenshots for hero moments.
- Scale up for phones: body text 28 to 42 px on the 1080 canvas at minimum, labels 18 px or more, borders 2 to 4 px [saas-motion-kit]; for ads aim higher (40 px or more).
- Imaginary components show one true capability, in brand tokens, with demo scale data visibly labeled as an example. Never invent capabilities, customers, logos or statistics. See [Truth, disclosure and rights](truth-disclosure-and-rights.md).

## 9. Template library to build per brand (priority order)

| Template | Inputs | Variant slots | Style IDs |
|----------|--------|---------------|-----------|
| T1 Offer video | Product footage or photo, offer, deadline, CTA | Hook text, offer framing, CTA | S24, S21 |
| T2 Hook pack | One body edit (footage), 5 to 10 hook texts and first frames | Hook only | Any footage style |
| T3 End card library | Logo, offer, CTA, legal line | CTA family | All |
| T4 Product hero with callouts | Product turntable footage or photos, 3 to 5 facts from PRODUCT_FACTS.md | Callout set, order | S25 |
| T5 Review card stack | Verbatim reviews with source and date, star rating | Review selection | S23 |
| T6 UI walkthrough | Captured UI or imaginary components, 3 step flow | Flow, hook | S27, S19 |
| T7 Comparison split | Two states, 2 to 3 criteria with substantiation | Criteria order | S17 |
| T8 Data story | One sourced number, chart data | Number framing | S26 |
| T9 Catalog loop | Feed CSV (title, price, image), max 6 products | Product set | S29 |
| T10 Caption and lower-third overlays (transparent WebM) | SRT or word timestamps | Caption style | Any footage style |
