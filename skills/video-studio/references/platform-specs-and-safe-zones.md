# Platform Specs and Safe Zones

> Purpose: deliver files that every target placement accepts and that keep text, faces, offers and CTAs out of the interface overlays. Values are planning values as of 2026-10. Official spec pages could not be fetched directly during research; most numbers come from 2026 spec guides that cite the official pages, and conflicts are labeled. Before final export of a new batch, open the live preview in each ads manager (Meta Ads Manager placement preview and safe zone overlay, TikTok Ads Manager preview, Google Ads ad preview, LinkedIn Campaign Manager preview) and record the date checked.

## 1. Master and delivery settings (all platforms)

| Setting | Value | Why |
|---------|-------|-----|
| Master render | 2160 x 3840 (9:16), 2160 x 2700 (4:5), 2160 x 2160 (1:1), 3840 x 2160 (16:9) for code-driven work | Render at 4K, downscale with Lanczos: edges, text and 3D come out cleaner than a native 1080p render [saas-motion-kit, 2026] |
| Delivery size | 1080 x 1920, 1080 x 1350, 1080 x 1080, 1920 x 1080; optional 1440 x 2560 for Meta 9:16 | Some 2026 guides cite 1440 x 2560 for Reels and Stories in Meta's Ads Guide (2026-09) [Contested]; 1080 x 1920 is accepted everywhere |
| Container and codec | MP4, H.264 High profile, yuv420p 8-bit | Universal acceptance; HDR and 10-bit can look wrong in ad players |
| Frame rate | Constant 30 fps (or the source rate: 23.976, 25, 29.97); never variable frame rate | VFR phone footage causes audio drift and rejected uploads; convert to CFR first |
| Quality | CRF 16 to 20 at slow preset, or 10 to 20 Mbps for 1080 x 1920 | Platforms re-encode; give them clean input |
| GOP | 2 s (keyframe every 60 frames at 30 fps) | Cleaner re-encodes and trims |
| Faststart | `-movflags +faststart` (moov atom first) | Progressive playback and some uploaders require it |
| Audio | AAC-LC, 48 kHz, stereo, 192 to 320 kbps | Meta guides list 128 kbps or more |
| Color | Rec.709, full brand colors checked on a phone screen | Pure black and pure white bands look harsh after compression |

[ffmpeg_deliver.py](../scripts/ffmpeg_deliver.py) applies these settings and checks them (`check` subcommand).

## 2. Meta (Facebook, Instagram, Threads, Audience Network)

| Placement | Ratio and size | Length | Notes |
|-----------|---------------|--------|-------|
| Reels (FB, IG) | 9:16, 1080 x 1920 (1440 x 2560 cited in 2026 guides) | Common ceiling 90 s; some 2026 guides claim up to 15 min for IG Reels ads [Contested]; recommended 15 to 30 s | Sound on by default; Facebook Reels ads have no auto captioning: burn captions in; licensed music only |
| Stories (FB, IG, Messenger) | 9:16, 1080 x 1920 | Up to 60 s per card [verify]; 6 to 15 s segments perform as a sequence | Unified safe zone with Reels since about 2026-03 |
| Feed (FB, IG) | 4:5, 1080 x 1350 (1:1 accepted) | Long durations allowed; recommended 15 s or less to 30 s | Many viewers are muted; text carries more |
| In-stream and Audience Network | 16:9 or 1:1, 9:16 accepted in some | 5 to 120 s typical | Usually placement customized |
| Threads | 1:1 or 4:5 images; video 1.91:1 to 9:16 | Short | Text-led statics and short demos |
| File | MP4 or MOV, max 4 GB (under 1 GB uploads more reliably) | | H.264, AAC 128 kbps or more |

Supply a 9:16 and a 4:5 version of every key asset and use placement asset customization; do not let automatic cropping decide where the product sits. Advantage+ creative enhancements (including video expansion and generated variations) can alter the frame: the channel agent reviews them per ad.

## 3. TikTok

| Item | Value |
|------|-------|
| Ratio and size | 9:16 recommended, 1080 x 1920 (minimum 540 x 960); 1:1 (640 x 640 or more) and 16:9 (960 x 540 or more) accepted [Official via secondary] |
| Formats | MP4, MOV, MPEG, AVI; under 500 MB |
| Bitrate | At least 516 kbps cited by several guides (not confirmed on a TikTok page) [Unverified]; deliver 8 to 15 Mbps |
| Length | In-feed 5 to 60 s widely cited; some guides list up to 10 min [Contested]; recommended 9 to 15 s, 15 to 30 s or 21 to 34 s depending on the source [Contested]. Spark Ads inherit the organic post length |
| Sound | Sound on; Commercial Music Library or original audio; music in ads must be licensed |
| Ad text | Short caption; keep the hook in the video |
| AI | Realistic AI-generated or significantly edited ad content needs the AIGC label or a clear on-screen disclaimer [Official ad policy, 2026] |

## 4. YouTube and Google video

| Format | Length | Ratio | Notes |
|--------|--------|-------|-------|
| Skippable in-stream | No min or max; Google recommends under 3 min; skip button after 5 s [Official via secondary, 2026] | 16:9 primary; 9:16 and 1:1 accepted | Brand and hook in first 5 s |
| Non-skippable in-stream | 7 to 15 s standard; 16 to 30 s on Connected TV (horizontal only) [Official, Google Ads Help] | 16:9 | Sources conflict on longer limits by campaign subtype [Contested] |
| Bumper | Up to 6 s | 16:9, 9:16, 1:1 | One idea |
| Shorts ads | Google recommends under 60 s; 10 to 30 s for action campaigns [Official, Shorts ads guide] | 9:16, 1080 x 1920 | Native vertical; no letterboxed 16:9 |
| Demand Gen video | Minimum 5 s; videos under 10 s do not serve on in-stream [Official via secondary] | Supply 16:9, 9:16, 1:1 and 4:5 | Video action campaigns finished upgrading to Demand Gen in 2026-04; "shorter video" enhancements on by default since 2025-03-10 unless opted out |
| CTV | 15 or 30 s | 16:9 only for 30 s non-skippable | Broadcast loudness |
| Hosting | Ads run from YouTube videos (public or unlisted) on the advertiser's channel | | Channel agent uploads; custom thumbnails need a verified channel |

YouTube recommended upload bitrates (SDR): about 8 Mbps for 1080p at 24 to 30 fps, 12 Mbps at 48 to 60 fps; 35 to 45 Mbps for 2160p [Official, YouTube Help, long standing; verify].

## 5. LinkedIn

| Item | Value |
|------|-------|
| Ratios | 16:9, 1:1, 4:5, 9:16 (vertical serves on mobile only; for desktop plus mobile use 16:9) [Official via secondary] |
| Length | 3 s to 30 min; recommended 15 to 30 s |
| File | MP4, H.264 and AAC, max 200 MB in most guides (500 MB claim unverified) [Contested] |
| Resolution | 1080p recommended, 360p minimum |
| Captions | Upload SRT in Campaign Manager (English only supported per LinkedIn help) or burn in; most viewing is muted |
| CTV (BrandLink, CTV ads) | 16:9 landscape only |

## 6. Connected TV and broadcast style deliveries

| Item | Value |
|------|-------|
| Lengths | 15 s and 30 s (6 s on some) |
| Picture | 1920 x 1080 or 3840 x 2160, 23.976, 25 or 29.97 fps per market, often ProRes 422 HQ mezzanine per publisher spec |
| Safe areas | Title safe 90 percent, action safe 93 percent (SMPTE convention) |
| Loudness | US: ATSC A/85, -24 LKFS integrated, true peak -2 dBTP (CALM Act); EU: EBU R128, -23 LUFS, -1 dBTP |
| Slate and black | Follow the publisher spec; some require 2 s black at head and tail |

## 7. Safe zones in pixels

All values for a 1080 x 1920 canvas: top, bottom, left, right bands to keep free of text, logos, faces in key moments, prices and CTAs.

| Placement | Top | Bottom | Left | Right | Source and label |
|-----------|-----|--------|------|-------|------------------|
| Meta Reels and Stories (unified, 9:16 Feed too) | 269 (14 percent) | 672 (35 percent) | 65 (6 percent) | 65 (6 percent) | 2026 guides after the 2026-03 unified update [Practitioner consensus, 2026-03] |
| Meta Stories (older guides) | 250 | 340 | | | Older guides [Superseded] |
| TikTok in-feed | 130 to 160 | 480 | about 60 | 140 | 2026 guides; check the TikTok preview overlay [Practitioner consensus, 2026] |
| YouTube Shorts (Google template values) | 288 | 672 | 48 | 192 | Attributed to Google Ads Help by third-party checkers [Contested] |
| YouTube Shorts (measured from previews) | 241 | 381 | 60 | 201 | adkit, measured 2026-03 [Practitioner measurement] |
| Universal 9:16 (one master for Reels, TikTok, Shorts) | 288 | 672 | 65 | 192 | Union of the strictest values above (this module) |

The universal 9:16 safe box is x 65 to 888 and y 288 to 1248 (823 x 960 px). Put the hook text, captions, offer and CTA inside it when one file goes to several platforms. Faces and the product can extend beyond it, but not into the bottom band during key lines.

4:5 and 1:1 feeds: keep a 5 percent margin (54 px on 1080 wide). When a 4:5 asset is auto placed into Reels or Stories, Meta letterboxes or crops: supply the 9:16 file instead.

16:9 YouTube: keep the bottom right clear for the skip button and the bottom band for the ad info bar and CTA overlay; keep logo bugs top right only if they do not collide with the info button. Planning margins top 100, bottom 160, left and right 96 [Practitioner consensus].

QA: render a frame with the unsafe areas shaded and look at it:

```bash
python3 scripts/ffmpeg_deliver.py overlay --input out_916.mp4 --target universal916 --at 1.0 --out qa_hook.png
python3 scripts/ffmpeg_deliver.py overlay --input out_916.mp4 --target tiktok --at 12.5 --out qa_cta.png
```

Check at minimum: the hook frame, every caption position change, the offer frame and the end card.

## 8. Loudness

No major social platform publishes an official loudness target for ads (none found in 2026 research). Working targets:

| Destination | Integrated | True peak | LRA | Label |
|-------------|-----------|-----------|-----|-------|
| Meta, TikTok, YouTube, LinkedIn (social default) | -14 LUFS | -1 dBTP | 11 LU or less | [Practitioner consensus]; YouTube normalizes near -14 but does not document it |
| Louder short-form option | -12 to -10 LUFS | -1 dBTP | | Some guides claim TikTok and Instagram prefer louder mixes [Contested]; test only if a quiet mix loses on hook rate |
| US broadcast and CTV | -24 LKFS | -2 dBTP | | ATSC A/85 |
| EU broadcast | -23 LUFS | -1 dBTP | | EBU R128 |
| Spotify audio ads (reference) | -16 LUFS +/- 1.5 | -2 dBTP | | Spotify ad specs |

Normalize with two-pass `loudnorm` (measure, then apply measured values with `linear=true`). The delivery script does this in `render`. Measure the result with `ebur128=peak=true` (the `check` subcommand).

## 9. Ratio and file plan per placement

| If the media plan includes | Deliver |
|----------------------------|---------|
| Meta Advantage+ with all placements | 9:16 and 4:5 (plus 1:1 only if Feed is a big share) |
| TikTok | 9:16 only (no letterboxed exports, no watermarks from other apps) |
| YouTube Demand Gen | 16:9, 9:16, 1:1 and 4:5 |
| YouTube in-stream only | 16:9 (plus 9:16 for Shorts inventory) |
| LinkedIn | 1:1 or 4:5 for feed, 16:9 for desktop heavy B2B, 9:16 for mobile |
| Pinterest, Snapchat (no agent) | 9:16 (Snapchat) and 2:3 or 9:16 (Pinterest); check their specs |

## 10. Thumbnails and covers

- Export the first frame and one chosen cover frame as PNG with every delivery.
- TikTok lets you pick a cover; Meta picks from frames or accepts an upload; YouTube custom thumbnails need a verified channel.
- The cover must not show text in unsafe zones and must not imply a feature or result that the video does not show.

## 11. Verification protocol before a new batch

1. Open each placement preview with one test file (channel agent or human, inside the account, no publishing).
2. Compare the overlay with the safe zone preset you used; update the preset in your batch output if the live overlay differs.
3. Confirm the length limit for the specific objective and placement in the ads manager form.
4. Record "Specs verified on YYYY-MM-DD in <tool>" in the delivery manifest.
