# QA Checklist (P7)

> Purpose: no file leaves the studio with a broken spec, text under the interface, an unapproved claim, a missing disclosure, unlicensed audio or a name that analysis cannot parse. Run on every file of a new concept and on a sample of 1 in 5 files for iterations of an approved template (Scale and Enterprise), plus every file that changed text, claims or audio. Blockers stop delivery; warnings go in the batch report.

Automated checks: [ffmpeg_deliver.py](../scripts/ffmpeg_deliver.py) `check` (specs, loudness, true peak, black first frame, faststart, name grammar) and `overlay` (safe-zone frames). Name checks: [variant_matrix.py](../scripts/variant_matrix.py) `--validate`.

## A. File and encoding

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| A1 | Resolution matches the target (1080 x 1920, 1080 x 1350, 1080 x 1080, 1920 x 1080) | `check --target <preset>` | Blocker |
| A2 | H.264 High, yuv420p, constant frame rate 23.976 to 60 | `check` | Blocker |
| A3 | Duration equals the plan within 0.5 s and is within the placement limit | `check --expect-seconds N`; placement table in [Platform specs](platform-specs-and-safe-zones.md) | Blocker |
| A4 | AAC 48 kHz (or 44.1) stereo audio present when the plan has sound | `check --require-audio` | Blocker |
| A5 | Faststart (moov before mdat) | `check` | Warn |
| A6 | File size under the platform cap (TikTok 500 MB, LinkedIn 200 MB, Meta 4 GB) | `ls -l` | Blocker |
| A7 | No letterboxing or pillarboxing that wastes the frame (unless pad-blur by design) | Watch | Warn |
| A8 | No watermark from another app or platform (TikTok, CapCut, stock preview) | Watch | Blocker |

## B. Safe zones and layout

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| B1 | Hook text, captions, offer, price, logo and CTA inside the safe zone of every platform the file will run on | `overlay --target <preset or universal916>` at the hook, each caption position, offer and end card | Blocker |
| B2 | Faces and product not covered by the bottom UI during key lines | Overlay frames | Warn |
| B3 | 4:5 and 1:1 versions keep 5 percent margins | Overlay `feed45` or `square` | Blocker |
| B4 | 16:9 YouTube: nothing important under the skip button area (bottom right) | Overlay `yt169` | Warn |
| B5 | Phone check: watched on a phone at arm's length, brightness 50 percent | Human at P7 | Blocker for new concepts |

## C. First frame and hook

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| C1 | Frame 1 is not black, not a logo card, not a fade from zero | `check` black-first-frame test; watch | Blocker |
| C2 | Product or problem visible by 2.0 s | Watch with a timer | Blocker |
| C3 | Hook text readable without sound in under 1.5 s (max 6 words) | Watch muted | Warn |
| C4 | Hook promise paid off by second 5 or 6 | Watch | Warn |
| C5 | Cover or thumbnail frame chosen and exported | File present | Warn |
| C6 | Hook variants differ only in the hook rows (one variable family) | Compare EDL or storyboard rows | Blocker for test cells |

## D. Captions and on-screen text

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| D1 | Captions verbatim to the audio, no typos in brand or product names | Read along with audio | Blocker |
| D2 | Captions synced within about 0.1 s and on screen long enough to read | Watch; check SRT timings | Warn |
| D3 | Caption size at least 56 px on 1080 wide verticals, outline or box for contrast | Overlay frame | Warn |
| D4 | Correct language file per version; special characters render (ş, ğ, İ, ı, ä, ß, accents) | Watch the frames with those words | Blocker |
| D5 | Uppercase handled per language (Turkish i and ı) | Read | Blocker for TR and AZ |
| D6 | Text layers do not repeat what the captions already say on screen at the same time | Watch | Warn |
| D7 | SRT sidecar delivered where used (YouTube, LinkedIn) | File present | Warn |

## E. Claims and truth

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| E1 | Every claim (spoken, on screen, in end card) is in `brand/CLAIMS.md` with status approved, and the ID is in the registry row | Claims list in the compliance packet | Blocker |
| E2 | Every number has a source and date | Packet | Blocker |
| E3 | Product shown is the real product; shape, color, label, size and packaging accurate | Compare with `brand/PRODUCT_FACTS.md` and reference photos | Blocker |
| E4 | UI shown is real or a truthful imaginary component; demo data labeled | Clean or imaginary log | Blocker |
| E5 | Demonstrations real; speed changes or staging labeled | Shot notes | Blocker |
| E6 | Testimonials from real customers or paid creators with releases; typical or qualified | Release IDs | Blocker |
| E7 | Offer, price, discount, deadline match `offer-strategy` terms and the landing page | Manifest vs landing page | Blocker |
| E8 | No personal attribute phrasing, no prohibited before and after, no fake UI elements | Read and watch | Blocker |
| E9 | `compliance` sign-off recorded for new claims, regulated categories, comparative claims, AI performers | Batch report | Blocker |

## F. Disclosure and AI

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| F1 | Synthetic performer label on screen near the performer for the whole appearance (NY, Hawaii, California wording, EU) | Watch | Blocker when `aiP` |
| F2 | EU deep fake label from first exposure for realistic generated or manipulated people, products, places, events | Watch | Blocker for EU markets |
| F3 | Paid partnership or "#ad" in the first seconds for creator content | Watch | Blocker |
| F4 | Platform label settings listed in the manifest (TikTok AIGC, Google AI label, Meta default) | Manifest | Blocker |
| F5 | C2PA or watermarks not stripped from generated media | `ffprobe` metadata or tool records | Warn |
| F6 | No AI artifacts at phone size (hands, faces, text, product edges, flicker) | Frame-by-frame scrub of generated shots | Blocker |
| F7 | Digital twin consent and script approval on file | Release IDs | Blocker |

## G. Audio

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| G1 | Integrated loudness at target within 1 LU (-14 LUFS social, -24 LKFS US CTV, -23 LUFS EU broadcast) | `check` | Blocker |
| G2 | True peak at or below the ceiling (-1 dBTP social, -2 dBTP CTV) | `check` | Blocker |
| G3 | Voice intelligible over music on a phone speaker | Listen on a phone | Blocker |
| G4 | Music license covers paid ads, territories and channels; log row present | Music license log | Blocker |
| G5 | No clipped or distorted audio, no sudden level jumps at hook swaps | Listen at cuts | Warn |
| G6 | Captions present for every spoken line (sound off viewers) | Watch muted | Blocker on Feed and LinkedIn |

## H. Naming, registry and manifest

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| H1 | File stem parses with the creative-strategy grammar | `check --check-name` or `variant_matrix.py --validate` | Blocker |
| H2 | Registry row appended with claims, music, releases, flags, status `qa_pass` | Open the CSV | Blocker |
| H3 | Upload manifest row per file with platform, placement, copy, URL, label settings, offer end date | Manifest | Blocker |
| H4 | Ratio siblings paired for placement customization | Manifest notes | Warn |
| H5 | No secrets, tokens or personal data in file names, manifests, logs or journal | Read | Blocker |

## I. Accessibility and safety

| ID | Check | How to verify | Level |
|----|-------|---------------|-------|
| I1 | No more than 3 flashes per second (photosensitive seizure guidance, WCAG 2.3.1) | Watch strobing sections; avoid full-frame flashes | Blocker |
| I2 | Text contrast readable (white on light backgrounds fails) | Overlay frames | Warn |
| I3 | Captions for all speech | Watch muted | Blocker |

## J. Platform specific

| ID | Check | Level |
|----|-------|-------|
| J1 | TikTok: native 9:16, sound on mix, no other-app watermark, AIGC label plan for realistic AI | Blocker |
| J2 | Meta Reels: captions burned in (no auto captions on Facebook Reels ads), licensed music only | Blocker |
| J3 | YouTube in-stream: brand or product in first 5 s; 16:9 file; SRT uploaded if long | Warn |
| J4 | YouTube Shorts: native vertical, not letterboxed 16:9 | Blocker |
| J5 | LinkedIn: captions or SRT (English only per help center), under 200 MB, 16:9 if desktop matters | Warn |
| J6 | CTV: 16:9, broadcast loudness, publisher slate and black requirements | Blocker |

## QA report template (append to the batch output)

```
## QA summary: batch <id>, <date>
Files checked: N of M (sampling rule: all new concepts, 1 in 5 template iterations)
Automated: ffmpeg_deliver.py check -> N pass, K fail (list)
Safe zone frames reviewed: <files and timestamps>
Blockers found and fixed: <list>
Open warnings: <list with reason accepted>
Compliance: sent <date>, result <approved / changes>, by <who>
Disclosure: files flagged aiG <n>, aiP <n>; labels verified on screen: yes/no
Specs verified in platform previews on: <date and tool>
```
