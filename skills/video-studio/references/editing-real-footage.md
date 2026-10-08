# Editing Real Footage

> Purpose: turn phone, creator, founder and studio footage into ad variants with FFmpeg and a few free tools: intake, transcription, paper edits, hook swaps, cut-downs, reframing, captions, audio cleanup, loudness and stills for statics. Every command below was tested with FFmpeg 6.1 on 2026-10-08 unless marked; FFmpeg 8.0 (2025-08) adds a native `whisper` filter.

## 1. Footage intake (P2)

| Step | Action | Pass condition |
|------|--------|----------------|
| Rights | Release or creator contract on file for every identifiable person; paid usage scope (channels, term, territories, whitelisting or Spark) | Release ID in the intake log |
| Inventory | Log each clip: file, duration, fps, resolution, who is on camera, what is shown, usable moments with timecodes | Intake log CSV |
| Normalize | Convert variable frame rate phone clips to constant frame rate before editing | `ffprobe` shows a fixed `r_frame_rate` |
| Proxy (optional) | 720p proxies for fast review | |
| Claims scan | Note every spoken claim with timecode; map to `brand/CLAIMS.md` IDs or mark "not approved" | Unapproved claims never reach an edit |

```bash
# probe
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,r_frame_rate,avg_frame_rate,sample_rate -show_entries format=duration -of json in.mov
# VFR phone clip to CFR 30, mezzanine quality
ffmpeg -i in.mov -vf fps=30 -c:v libx264 -preset slow -crf 16 -pix_fmt yuv420p -c:a aac -b:a 256k -ar 48000 clip_cfr.mp4
```

Intake log columns: `clip_id, file, duration_s, fps, res, people (release IDs), shows, best_moments (tc ranges), spoken_claims (tc and claim ID), notes`.

## 2. Phone footage plan for Starter tier (founder, staff, customers)

Give this to the person filming. It is often the highest-return production mode at Starter budgets [Practitioner consensus].

```
Camera: phone back camera, 4K 30 fps, vertical, lens cleaned, exposure and focus locked on the face (long press)
Light: face toward a window, no backlight, no overhead only light
Sound: lavalier or wired mic if possible; quiet room; record 10 s of room tone
Framing: eyes at upper third, phone at eye level, arm's length or tripod
Takes: each hook line 3 times with different energy; full script 2 times; talking points loosely
B-roll list (2 to 5 s each, steady, 3 versions each):
  product in hand, product in use, close-up macro of texture or detail, unboxing, the problem situation,
  the result (real), the person reacting, packaging, a hand pressing or tapping, environment wide shot
Do not: read from a screen with eyes moving, wear logos of other brands, film customers without a signed release,
  play music while filming, say claims that are not on the approved list
```

## 3. Transcription and word timestamps

| Option | Cost (source, date) | Notes |
|--------|---------------------|-------|
| `npx hyperframes transcribe video.mp4 --model medium.en --language en` | Free, local (whisper.cpp or Parakeet) | Word-level timestamps; `--to srt` exports a sidecar [Official docs, 2026] |
| FFmpeg 8.0 `whisper` filter | Free, local; needs a build with `--enable-whisper` and a whisper.cpp model | Example: `ffmpeg -i in.mp4 -vn -af "whisper=model=ggml-base.en.bin:language=en:queue=3:destination=out.srt:format=srt" -f null -` [FFmpeg docs, 2025-08]; confirm options with `ffmpeg -h filter=whisper` |
| WhisperX | Free (MIT), needs a GPU for speed | Forced alignment for accurate word times; numbers and symbols may lack timestamps (spell them out) |
| ElevenLabs Scribe v2 | 0.22 USD per audio hour batch [Official pricing page, 2026] | 90+ languages, diarization |
| AssemblyAI Universal-3 Pro or 3.5 Pro | 0.21 USD per hour [AssemblyAI, 2026-09] | Universal-3 Pro covers 6 languages; Universal-2 covers 99 |
| Deepgram Nova-3 | About 0.26 to 0.29 USD per hour batch [trackers, 2026-08] | Pricing varies by source |

Always correct the transcript by ear before captions: brand names, numbers, claims. Captions must match the audio verbatim (QA blocker).

## 4. Paper edit and EDL

Write the edit as data first. One row per segment; the variant slot says which family the row belongs to.

```csv
seg_id,source,in_s,out_s,role,variant_slot,text_or_note,claim_ids
h01,clip_cfr_03.mp4,12.40,14.10,hook,H01,"If your knees hurt after every run",
h02,clip_cfr_05.mp4,3.00,4.60,hook,H02,"I almost quit running last spring",
b01,clip_cfr_03.mp4,14.10,22.80,body,v1,"tried insoles, braces, rest",
b02,broll_macro_01.mp4,0.00,3.20,body,v1,"macro of cushioning",CL-004
c01,endcard_cta1.webm,0.00,3.00,cta,cta1,"20% off first pair",OF-2026-10
```

Cut segments with identical encode settings so they concatenate without re-encoding:

```bash
# one segment (input-side seek is frame accurate when re-encoding)
ffmpeg -ss 12.40 -to 14.10 -i clip_cfr_03.mp4 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30" \
  -c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -ac 2 seg_h01.mp4
# concat hook H02 + body (list file, then stream copy)
printf "file 'seg_h02.mp4'\nfile 'seg_b01.mp4'\nfile 'seg_b02.mp4'\n" > list_H02.txt
ffmpeg -f concat -safe 0 -i list_H02.txt -c copy H02_v1_master.mp4
```

For code-driven end cards, render a transparent WebM (`npx hyperframes render --format webm`) and overlay it:

```bash
ffmpeg -i H02_v1_master.mp4 -c:v libvpx-vp9 -i endcard_cta1.webm \
  -filter_complex "[0:v][1:v]overlay=0:0:enable='between(t,12,15)'" -c:v libx264 -crf 17 -c:a copy H02_v1_cta1.mp4
```

(The `-c:v libvpx-vp9` before the second input forces the decoder that keeps the alpha channel.)

## 5. Hook swaps

Build the body once, then attach every hook. Rules:
- Each hook segment ends on an action or a breath, never mid-word; the body starts on the next action (J-cut audio if needed).
- Keep the hook 1.5 to 3.0 s. The promise of the hook must be paid off in the body by second 5 or 6.
- Hold the body, CTA, music and captions style constant across hook variants (one variable family).
- Name hook variants with H IDs on the same `ver` ([Variants and testing handoff](variants-and-testing-handoff.md)).

Hook sources ranked: a real moment from the footage (strongest), a re-shot line, a text-led hook over the strongest visual, a code-driven kinetic type pre-roll (1.5 s), a generated b-roll opener (only if it is not misleading and is labeled where required).

## 6. Cut-downs

| From | To | Keep | Drop |
|------|----|------|------|
| 60 s | 30 s | Hook, the strongest 2 proof beats, offer, CTA | Setup, third proof, repetition |
| 30 s | 15 s | Hook, one proof (the visual one), CTA | Problem setup, objection, second proof |
| 15 s | 6 s | Product in action (0 to 2), one benefit line (2 to 5), logo and CTA (5 to 6) | Everything else |
| Any | Winner iteration | Exactly the first 2 s (same file segment and audio) | Rebuild from the biggest retention drop |

Trim and hold the last frame for the end card with the delivery script:

```bash
python3 scripts/ffmpeg_deliver.py render --input master_30s.mp4 --start 0 --end 13.5 --hold-last 1.5 \
  --targets universal916 --stem C021_hcause_runner_prob_ugc_H02_cr07_15s --ver v1 --captions subs_15s.srt
```

## 7. Reframing between ratios

| Source to target | Method | Command (delivery script) |
|------------------|--------|---------------------------|
| 9:16 to 4:5 | Crop with focus on the subject | `--mode crop --focus-y 0.35` |
| 16:9 to 9:16 (talking head) | Crop on the face; split into segments if the subject moves | `--mode crop --focus-x 0.62` per segment |
| 16:9 to 9:16 (wide demo, UI) | Blurred background fill (pad-blur) keeps the whole frame | `--mode pad-blur` |
| Any to same aspect | Scale only | `--mode fit` |

Rules: never crop off the product, the face's eyes, on-screen text or the logo. When the subject moves across the frame, cut the clip into segments and give each its own focus. Prefer native vertical capture for TikTok and Reels: reframed 16:9 often looks repurposed.

## 8. Jump cuts and pace

Find pauses to remove (talking heads):

```bash
ffmpeg -i clip_cfr_03.mp4 -af silencedetect=noise=-35dB:d=0.4 -f null - 2>&1 | grep -E "silence_(start|end)"
```

Remove pauses longer than about 0.3 s in hooks and 0.5 s in bodies; keep breaths that carry emotion. Scene changes in references or long clips:

```bash
ffmpeg -i ref.mp4 -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 | grep -o "pts_time:[0-9.]*"
```

Divide the count by the duration to get cuts per 10 s for reference breakdowns (borrow grammar, never assets).

## 9. Captions

1. Transcript corrected by ear, split into phrases of 2 to 6 words.
2. Convert SRT to an ASS file positioned for the target safe zone and burn in:

```bash
python3 scripts/ffmpeg_deliver.py srt2ass --srt subs.srt --target universal916 --out subs_916.ass --upper en
python3 scripts/ffmpeg_deliver.py render --input master.mp4 --targets universal916 --captions subs.srt --stem <stem> --ver v1
```

3. For kinetic word-by-word captions use HyperFrames `/embedded-captions` or Remotion `createTikTokStyleCaptions()` with word timestamps.
4. Burn captions for the strictest platform you will post the file to (universal916 for cross-posting); check with the overlay frame.
5. Upload SRT sidecars where the platform supports them (YouTube, LinkedIn English) in addition to burned captions when the ad must stay accessible.
6. Language versions get their own SRT and ASS files; never machine translate claims without native review.

## 10. Text overlays and labels with drawtext

```bash
ffmpeg -i in.mp4 -vf "drawtext=fontfile=/path/Brand-Bold.ttf:text='Sped up 2x':x=w-tw-80:y=320:fontsize=42:fontcolor=white:box=1:boxcolor=black@0.5:boxborderw=12" -c:a copy out.mp4
```

Use drawtext for short legal or disclosure labels ("Sped up 2x", "Actor portrayal", "AI-generated presenter", "Results vary"). Place inside the safe zone and keep on screen long enough to read (at least 2 s, or the whole time the AI performer is visible).

## 11. Speed, freeze and end card holds

```bash
# freeze the last frame 2.5 s and pad audio (end card hold)
ffmpeg -i in.mp4 -vf "tpad=stop_mode=clone:stop_duration=2.5" -af "apad=pad_dur=2.5" -c:v libx264 -crf 17 out.mp4
# speed up a demo 2x (label it on screen if speed matters to the claim)
ffmpeg -i demo.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" demo_2x.mp4
```

## 12. Audio cleanup, ducking and loudness

```bash
# voice cleanup: high-pass and FFT denoise
ffmpeg -i vo_raw.wav -af "highpass=f=90,afftdn=nf=-25" vo_clean.wav
# duck music under the voice (sidechain), then mix
ffmpeg -i music.wav -i vo_clean.wav -filter_complex \
 "[1:a]asplit=2[vo][sc];[0:a][sc]sidechaincompress=threshold=0.05:ratio=8:attack=20:release=300[duck];[duck][vo]amix=inputs=2:duration=longest:normalize=0[out]" \
 -map "[out]" mix.wav
# two-pass loudness to -14 LUFS / -1 dBTP is automatic in: ffmpeg_deliver.py render
```

## 13. Stills for statics from video frames

```bash
# a chosen frame at full quality
ffmpeg -ss 6.35 -i master_4k.mp4 -frames:v 1 -q:v 2 still_0635.png
# contact sheet, one frame per second, to pick candidates
ffmpeg -i master.mp4 -vf "fps=1,scale=320:-1,tile=4x2" -frames:v 1 sheet.png
```

Statics from video frames: crop to 1080 x 1350 (4:5) and 1080 x 1080, add headline text in code (HyperFrames still render or an image editor), keep claims from the approved list, and name them with `stat` format code and the parent concept ID. Hand static copy questions to `creative-strategy`.

## 14. Delivery and QA

```bash
python3 scripts/ffmpeg_deliver.py render --input H02_v1_master.mp4 --targets universal916,feed45 \
  --stem C021_hcause_runner_prob_ugc_H02_cr07_15s --ver v1 --captions subs.srt
for f in deliver/*.mp4; do python3 scripts/ffmpeg_deliver.py check --input "$f" --target universal916 --check-name || echo "FIX $f"; done
python3 scripts/ffmpeg_deliver.py overlay --input deliver/<file>_916_v1.mp4 --target universal916 --at 1.0 --out qa_hook.png
```

Then complete the [QA checklist](qa-checklist.md). Note: run `check` on 4:5 files with `--target feed45`.
