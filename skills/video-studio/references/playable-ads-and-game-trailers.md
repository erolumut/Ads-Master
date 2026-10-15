# Playable Ads and Game Trailers

> Knowledge as of 2026-10 (research pass 2026-10-12). Network playable specs were read only through search summaries of the network docs; the Meta and several network limits come from vendor guides and are [Unverified]. Apple guideline text was read at the source (guidelines dated 2026-06-08). Verify every size limit and CTA function in the network's own spec page before a batch, and log the check date in the batch output.

Purpose: produce two things from a real game. (1) Playable ads: a 15 to 30 second slice of the core rule that runs inside an ad network as one HTML file. (2) Trailers and gameplay cuts rendered frame by frame from the game's own deterministic simulation, so every frame is the real game, at any resolution, ratio and language, with no screen recording. Concepts, hooks and test design come from `creative-strategy` ([Game ad creative](../../creative-strategy/references/game-ad-creative.md)). Network setup and reads belong to `mobile-app-growth`.

Boundary: Ads Master owns how a game earns, is found, keeps players, is measured and passes review; the game's own repo owns how it plays. The capture mode in section 6 is an interface the game repo implements once; this module never changes rules, levels or difficulty to make footage look better.

## 1. Truth rules for game footage and playables

| Rule | Why | Check |
|------|-----|-------|
| The playable or trailer shows the game's core loop, reachable early | UK ASA rulings (Playrix 2020-09-30, Evony 2024-04-03) found ads misleading when the gameplay shown was rare, late or not the core experience, even with real footage and a disclaimer [Reported, 2026-10] | The representativeness test in [Game ad creative](../../creative-strategy/references/game-ad-creative.md) section 1 is attached to the brief |
| Same rule, same art, same UI | A playable that plays differently from the game drives installs that churn and is a misrepresentation risk | Side by side with the store build |
| Fails and wins are achievable | A staged fail no player can produce is fake gameplay | Input log recorded from human play or a bot limited to human speed |
| Speed changes and camera moves are presentation | They are fine in ads when the action itself is real | Never speed up a timer or score to make play look easier |
| App Store previews are stricter | Apple 2.3.4: "previews may only use video screen captures of the app itself" [Official, 2026-06] | Store preview cuts use device resolution, the game's own camera and UI, no cinematic camera paths; `store-submission` confirms before upload |

## 2. Playable ad design (what the 15 to 30 seconds contain)

| Beat | Time | Content | Why |
|------|------|---------|-----|
| First frame | 0 s | The board or scene of a real early level, fully drawn, plus a tutorial prompt (hand or arrow on the first move) | Most top playables carry a tutorial prompt (FoxData reports 85.4% [Unverified, vendor]); a viewer must know where to touch without reading |
| First touch | Within 1 to 3 s | One gesture performs the core rule | AppLovin's guidance starts the playable's timer only after the first interaction [Reported, 2026-10] |
| Loop | 3 to 6 moves | The one rule, a short difficulty ramp, the game's own sound after the first touch | One rule only: a playable that teaches two mechanics teaches neither |
| Outcome | 15 to 30 s of interaction | A win, or a near fail that invites "finish it in the game" | Matches the 15 to 30 seconds of interaction guidance for networks in `mobile-app-growth` app creative |
| End card | After the outcome, or after an idle limit | App icon, name, one line promise, CTA ("Play", "Install") | The end card is where the install happens; test variants |
| Idle fallback | After about 5 to 8 s with no touch (house default) | Auto play one move, then show the end card | A viewer who never touches still sees the game and the CTA |

Variants worth testing (one variable family at a time, per [Variants and testing handoff](variants-and-testing-handoff.md)):

| Family | Variants |
|--------|----------|
| Outcome | Easy win vs near fail vs unsolved at the last move |
| Prompt | Hand pointer vs glowing target vs one word ("Swipe") |
| End card | At least 3: CTA text, reward shown, progression shown; vendor guidance is to test several end cards [Unverified, vendor] |
| Length | Short (about 15 s) vs long (about 30 s) |
| Entry | Video intro (2 to 5 s of the winning video concept) then playable vs playable from frame 0; video to playable hybrids are reported as the fastest growing format [Unverified, FoxData] |

Fatigue: vendor reports put playable fatigue at 7 to 10 days [Unverified, vendor]. Read your own IPM decay per playable before rotating on a calendar.

## 3. Network specs (verify before every batch)

| Network | Packaging | Size limit | CTA call | Other rules | Label |
|---------|-----------|-----------|----------|-------------|-------|
| AppLovin | Single HTML file, every asset inlined (base64), no external JS, CSS, fonts or images | 5 MB | MRAID `mraid.open(storeUrl)` | Works in portrait and landscape; timer starts after the first interaction | [Reported, 2026-10] (AppLovin docs via search) |
| Unity Ads | Single inlined `index.html` | Under 5 MB | `mraid.open(storeUrl)` | MRAID version differs between Unity pages (2.0 in the 3.5 docs, 3.0 in the current creative specs) | [Contested]: check the current Unity creative specs |
| Google App campaigns (HTML5 playables) | ZIP | 5 MB and at most 512 files on the current help page; an older Google page lists 1 MB and 40 files | Google ExitApi | Orientation set by a meta tag; no sound before the user interacts; validate with Google's HTML5 validator | [Contested] between two Google help pages; treat 5 MB and 512 files as current only after checking |
| Meta | Single HTML or ZIP | 2 MB single HTML, 5 MB ZIP | `FbPlayableAd.onCTAClick()`; `mraid.js` not supported | All assets inline, no external URLs | [Unverified] (vendor guides only) |
| Mintegral, TikTok, Moloco, Liftoff, ironSource, others | Check the network spec page | Unknown here | Usually MRAID or a network function | | [Unverified]: not researched |

Build to the strictest common target first: one HTML file under 2 MB, all assets inlined, no network requests, no local storage, sound only after a touch, both orientations. Then package per network through the CTA adapter (section 4). Base64 inflates binary assets by about one third (4 bytes per 3), so budget the raw assets at about 1.4 MB for a 2 MB file.

## 4. Building a playable

Choose the source of the rules first, because it decides how truthful the playable is.

| Approach | When | Size | Truth risk | Notes |
|----------|------|------|------------|-------|
| A. Reuse the game's own rules module | Web or JS games whose rules live in a pure module (state in, action in, state out) | Medium; strip networking, analytics and unused content | Lowest: the rules are the game's | Best fit for deterministic web games; the same module powers section 6 |
| B. Rebuild the slice in a light framework (Phaser, PixiJS, plain canvas) | Native games, or engines too heavy to bundle | Smallest | Medium: the rule is reimplemented; test it against the game's behaviour on the same level | Name the level and seed it reproduces |
| C. Engine export tooling for Unity games (for example Luna Playable) | Unity projects | Varies | Low | Licence and pricing [Unverified]; check before committing |
| D. Agency or freelancer | No in-house capacity | Varies | Depends on the brief | Give them the representativeness test and the level id; review the rule before paying |

CTA adapter (the only place a network name appears; the rest of the playable stays network neutral):

```html
<script>
  // One playable, many networks. Set NETWORK at packaging time.
  const NETWORK = "__NETWORK__";            // "mraid" | "google" | "meta" | "preview"
  const STORE_URL = "__STORE_URL__";       // store or MMP click URL supplied by mobile-app-growth
  function cta() {
    if (NETWORK === "mraid" && window.mraid) { mraid.open(STORE_URL); return; }
    if (NETWORK === "google" && window.ExitApi) { ExitApi.exit(); return; }
    if (NETWORK === "meta" && window.FbPlayableAd) { FbPlayableAd.onCTAClick(); return; }
    console.log("CTA", STORE_URL);          // preview only
  }
  function whenReady(start) {              // MRAID containers fire "ready"; others start on load
    if (NETWORK === "mraid" && window.mraid && mraid.getState() === "loading") {
      mraid.addEventListener("ready", start);
    } else { window.addEventListener("load", start); }
  }
  // Sound and the playable timer start only after the first touch.
  // startAudio and startTimer belong to the playable's own code.
  window.addEventListener("pointerdown", () => { startAudio(); startTimer(); }, { once: true });
</script>
```

Build rules:
- Inline every asset: sprite atlas as one image, short mono audio loops, a subset font; no CDN, no web fonts by URL.
- Draw the first frame synchronously after load: the board and the prompt are visible before any animation starts.
- Large touch targets, one gesture type, no text the viewer must read to play.
- No analytics SDKs inside the playable; networks report impressions, interactions and installs.
- Packaging is a script, not a hand edit: one source folder, one build per network with `__NETWORK__` and `__STORE_URL__` replaced and the size checked against section 3.

Playable QA (add to the batch QA from the [QA checklist](qa-checklist.md)):
- [ ] File size under the network limit after inlining; size logged per network build.
- [ ] Zero network requests with the device offline (browser dev tools network panel).
- [ ] First frame shows the board and the prompt; no blank or loading frame.
- [ ] Sound starts only after the first touch; muted state works.
- [ ] Portrait and landscape both playable.
- [ ] CTA opens the store from the end card and from any in-play CTA, per network build.
- [ ] Win path, near fail path and idle fallback all reach the end card.
- [ ] Smooth on a low end Android phone in the network's preview or test tool (names and availability per network docs).
- [ ] Rule and art match the store build; level id and seed recorded.
- [ ] Compliance packet includes the playable file and the representativeness test.

## 5. Trailers from the game itself: why render, not record

| Screen recording | Frame by frame render from a capture mode |
|------------------|-------------------------------------------|
| Frame drops, notification bars, cursor, compression from the recorder | Every frame complete and clean |
| One resolution, one ratio per take | Any resolution (4K masters) and any ratio from the same run |
| Retake if a move goes wrong | The same seed and input log give the same run every time |
| Hard to localize UI text | Language switch per render; same timing |
| Hard to sync to music | Cuts land on beat because time is exact |
| Truth depends on the operator | Truth is structural: it is the real simulation stepping |

A practitioner post described a studio (Skyhold) rendering its trailer this way, stepping the real game frame by frame; the post could not be found again during research, so treat it as an illustration of the pattern, not a verified case [Unverified]. The method itself uses only standard tools (a browser automation library and FFmpeg).

## 6. The capture mode contract (implemented by the game repo)

The game repo adds a capture mode behind a flag (for example `?capture=1` or a build flag). Requirements:

| Requirement | Detail |
|-------------|--------|
| Deterministic simulation | Seeded random number generator; no wall clock reads (`Date.now()`, `performance.now()`) in the simulation; no unseeded `Math.random()`; no network during capture |
| Fixed timestep | The simulation advances in ticks of a fixed `dt` (for example 1/60 s); rendering reads the simulation state, it never advances it with frame time |
| Scripted input | Inputs come from an input log keyed by tick, recorded from a real play session or a bot limited to human speed |
| `render(t)` | Advances the simulation from the last tick to `floor(t / dt)`, applies logged inputs on their ticks, draws the frame, resolves when the frame is fully drawn |
| UI animations bound to time | CSS transitions, tweens and `requestAnimationFrame` loops are disabled or driven from `t` (Web Animations API: pause every animation and set `currentTime`) |
| Assets ready | `init` resolves only after `document.fonts.ready`, image decode and texture upload |
| Audio as events | Capture mode records sound events (`tick`, `soundId`, `volume`) so audio is rebuilt exactly (section 7); the browser does not capture audio in screenshots |
| Reset | `init(config)` restarts from the seed, so any shot can be re-rendered alone |

Interface sketch (the game implements it in its own code; names are a suggestion):

```js
// window.__capture, present only in capture mode
window.__capture = {
  async init({ seed, levelId, inputLog, width, height, lang, camera }) { /* reset sim, load assets, await fonts */ },
  async render(t) { /* step fixed ticks up to floor(t / dt), apply inputs, draw, await paint */ },
  duration() { /* seconds until the run ends */ },
  soundEvents() { /* [{ tick, soundId, volume }] collected so far */ },
};
```

Shot list for a trailer (one row per shot; kept in the batch folder as `shots.json`):

```json
[
  { "shot": "S01_hook", "levelId": "L004", "seed": 918273, "inputLog": "logs/L004_human_take3.json",
    "from": 12.0, "to": 15.5, "ratio": "916", "lang": "en", "camera": "default" },
  { "shot": "S02_loop", "levelId": "L004", "seed": 918273, "inputLog": "logs/L004_human_take3.json",
    "from": 0.0, "to": 9.0, "ratio": "916", "lang": "en", "camera": "default" }
]
```

## 7. Rendering pipeline: Playwright screenshots piped to FFmpeg

```js
// render_shot.mjs: node render_shot.mjs <url> <out.mp4> <seconds> <fps> <width> <height>
import { chromium } from "playwright";
import { spawn } from "node:child_process";
const [url, out, seconds, fps = "30", w = "1080", h = "1920"] = process.argv.slice(2);
if (Number(w) % 2 || Number(h) % 2) throw new Error("x264 with yuv420p needs even width and height");
const browser = await chromium.launch({ args: ["--use-angle=swiftshader", "--enable-unsafe-swiftshader"] });
const page = await (await browser.newContext({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 })).newPage();
await page.goto(url);
await page.waitForFunction(() => window.__capture !== undefined);
await page.evaluate((cfg) => window.__capture.init(cfg), JSON.parse(process.env.SHOT || "{}"));
const ff = spawn("ffmpeg", ["-y", "-f", "image2pipe", "-framerate", fps, "-c:v", "png", "-i", "-",
  "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", "-preset", "slow", "-movflags", "+faststart", out],
  { stdio: ["pipe", "inherit", "inherit"] });
const frames = Math.round(Number(seconds) * Number(fps));
for (let i = 0; i < frames; i++) {
  await page.evaluate((t) => window.__capture.render(t), i / Number(fps));
  const png = await page.screenshot({ type: "png" });
  if (!ff.stdin.write(png)) await new Promise((r) => ff.stdin.once("drain", r));
}
ff.stdin.end();
await new Promise((r) => ff.on("close", r));
await browser.close();
```

Then:
1. Rebuild audio from `soundEvents()`: mix the game's own sound files at each event time with FFmpeg (`adelay` per event into `amix`; `amix` lowers each input's level by default, so check the normalize option in your FFmpeg version) or render the game's audio graph in an `OfflineAudioContext`. Add licensed music per [Avatars, voice and music](avatars-voice-and-music.md).
2. Compose the ad in HyperFrames: the rendered gameplay MP4 becomes a `<video class="clip">` layer under the hook text, captions and end card, using the composition skeleton and determinism checklist in [Code-driven motion](code-driven-motion.md) sections 3 and 5. Variants (hooks, languages, end cards) come from the template build in section 6 of that module.
3. Deliver platform files and QA overlays with [ffmpeg_deliver.py](../scripts/ffmpeg_deliver.py) and the presets in [Platform specs and safe zones](platform-specs-and-safe-zones.md).
4. Name files with the creative-strategy grammar. Use the game format codes: `gp` for gameplay cuts, `play` for playable builds, `trl` for trailers. Record the level id and seed in the registry row.

Speed: one screenshot per frame is slow on long shots. Split a shot into frame ranges and render ranges in parallel browser instances; each instance calls `init` with the same seed and fast forwards the simulation without drawing to its first frame (this needs simulation and drawing to be separable in the game code). Concatenate the parts with FFmpeg's concat demuxer.

## 8. Traps and fixes

| Trap | Symptom | Fix |
|------|---------|-----|
| Lost WebGL context in headless Chromium | Black or frozen frames after a while, `webglcontextlost` in the console | Software GL flags (`--use-angle=swiftshader`, `--enable-unsafe-swiftshader`; flag names change between Chromium versions [Unverified], check yours) or run headed on a GPU machine; listen for `webglcontextlost` and `webglcontextrestored`, rebuild textures, re-render the frame; fewer parallel instances per machine |
| Blank canvas when reading pixels directly | `toDataURL` or `readPixels` returns an empty image | Use page screenshots, or create the context with `preserveDrawingBuffer: true`, or read inside the same frame as the draw |
| Odd frame size | x264 error that width or height is not divisible by 2 | Even viewport sizes, or `-vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"` |
| Device pixel ratio | Output twice the expected size | `deviceScaleFactor: 1` and set the size in the viewport; render 4K by viewport size, not by DPR, unless the game's UI scales correctly |
| Fonts swap mid shot | Text jumps on early frames | Await `document.fonts.ready` in `init`; bundle fonts locally |
| UI animated by wall clock | Menus and score counters out of sync with gameplay | Drive UI animations from `t`; disable `requestAnimationFrame` loops in capture mode |
| Hidden nondeterminism | Two renders of the same shot differ | Hash sample frames (SHA-256 of the PNG) across two renders on the same machine; any difference is a bug: unseeded random, iteration over unordered collections, time reads, floating point that depends on frame rate |
| Variable timestep leaks in | Physics differs between 30 and 60 fps renders | Simulation ticks at a fixed `dt` regardless of output fps; output frames sample the state (interpolate between ticks for smoothness if needed) |
| Audio drift | Sound slightly early or late at the end | Build audio from tick times, not from wall clock logs; check sync at the last event |
| Colour shift | Washed out colours after encode | Encode with `-pix_fmt yuv420p` and check the colour range on a phone, not only on a desktop player |

## 9. Uses of the same render

| Output | Spec owner | Notes |
|--------|------------|-------|
| Paid video ads (6, 15, 30 s, 9:16, 4:5, 1:1, 16:9) | This skill | Hook first frame per [Ad video grammar](ad-video-grammar.md) |
| Playable intro (2 to 5 s of video before the playable) | This skill with `mobile-app-growth` | Export as frames or a short clip to embed only if the network size budget allows |
| App Store preview (up to 3 previews of up to 30 s, per the store research) | `app-store-optimization` writes, `store-submission` checks | Screen capture rule 2.3.4: device resolution, real UI, the game's own camera |
| Google Play promo video | `app-store-optimization` | Published on YouTube; same truth rule |
| Organic social cuts (TikTok, Shorts, Reels) | `creative-strategy` plans | Stage 0 concept screens in the game creative module |
| Press and portal trailers | `growth-orchestrator` (portal deals) | Same render, longer cut |

## 10. Handoffs from this module

| Situation | Hand off to | What to pass |
|-----------|-------------|--------------|
| Concept, hook and end card choices; test reads | creative-strategy | Batch with variant families and the level ids used |
| Upload playables and videos (PAUSED) to networks; network spec questions | mobile-app-growth | Network builds with sizes, CTA adapter per network, upload manifest |
| The game lacks a capture mode or is not deterministic | Human, for the game repo | The capture mode contract in section 6 as a request, never a design change |
| Store previews and promo videos | app-store-optimization, store-submission | Device resolution renders, shot list, the 2.3.4 check |
| Claims, loot box disclosure, children | compliance | Compliance packet with the playable file and the representativeness test |
| Retention by playable cohort | measurement | Creative IDs, dates |

## Sources for this module

| Source | Date | Supports | Label |
|--------|------|----------|-------|
| Apple App Review Guidelines 2.3.4 (previews are screen captures of the app) | 2026-06-08, read 2026-10-12 | Store preview rule | [Official, 2026-06] |
| AppLovin creative best practices and guidelines (support.applovin.com, axon.ai), via search | 2026 | 5 MB single HTML, inline assets, orientation, timer after first interaction | [Reported, 2026-10] |
| Unity Ads creative specifications and Unity Ads 3.5 creative asset specs, via search | 2026 and older | Under 5 MB single index.html, MRAID version conflict, `mraid.open` | [Contested] |
| Google Ads Help "About HTML5/Playable ads for App campaigns" and "About HTML5 for App campaigns", via search | Undated pages | 5 MB and 512 files vs 1 MB and 40 files, ExitApi, sound after interaction | [Contested] |
| Segwise "Playable ad specs: every major network compared"; Luna Labs Meta notes; other vendor guides | 2026-09 | Meta 2 MB single HTML and 5 MB ZIP, `FbPlayableAd.onCTAClick` | [Unverified, vendor] |
| FoxData winning game creatives | 2026 | Tutorial prompts in top playables, video to playable hybrids | [Unverified, vendor] |
| Research note 03 (game UA) | 2026-10-12 | Playable fatigue 7 to 10 days, several end cards | [Unverified, vendor] |
| Research note 08 (web distribution): Skyhold not found | 2026-10-12 | The frame by frame trailer example | [Unverified] |
