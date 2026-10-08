#!/usr/bin/env python3
"""ffmpeg_deliver.py: platform cut-downs, safe-zone QA frames and delivery checks for ad videos.

Standard library only. Needs ffmpeg and ffprobe on PATH (libass for caption burn-in).

Subcommands
  targets   List the delivery presets (size, safe zone, loudness target).
  plan      Print the ffmpeg commands that turn one master into platform files (dry run, default).
  render    Same as plan, but run the commands (two-pass loudness measured for real).
  overlay   Write a PNG of one frame with the unsafe areas of a preset shaded, for human QA.
  check     Probe a delivered file and report PASS or FAIL against a preset (size, fps, codecs,
            duration, loudness, true peak, black first frame, file name grammar).
  srt2ass   Convert an SRT file into an ASS file styled for a preset's safe zone (pixel units).

Examples
  python3 ffmpeg_deliver.py targets
  python3 ffmpeg_deliver.py plan --input master.mp4 --targets reels,feed45,yt169 \
      --stem C021_hcause_runner_prob_ugc_H03_cr07_30s --ver v2 --mode pad-blur --captions subs.srt
  python3 ffmpeg_deliver.py render --input master.mp4 --targets tiktok --stem ... --ver v1 --start 0 --end 15
  python3 ffmpeg_deliver.py overlay --input out.mp4 --target universal916 --at 1.0 --out qa.png
  python3 ffmpeg_deliver.py check --input out.mp4 --target reels

Safe-zone numbers are planning values from practitioner measurements and platform templates as of
2026-10 (see references/platform-specs-and-safe-zones.md). Verify against the live placement preview.
"""
import argparse
import json
import os
import re
import shlex
import subprocess
import sys

# name: (width, height, ratio_token, safe(top, bottom, left, right), lufs, true_peak, max_seconds, note)
TARGETS = {
    "reels":        (1080, 1920, "916", (269, 672, 65, 65), -14.0, -1.0, 90,  "Meta Reels and Stories, unified 9:16 zone (2026-03)"),
    "stories":      (1080, 1920, "916", (269, 672, 65, 65), -14.0, -1.0, 60,  "Meta Stories"),
    "tiktok":       (1080, 1920, "916", (160, 480, 60, 140), -14.0, -1.0, 60, "TikTok in-feed, right rail and caption area"),
    "shorts":       (1080, 1920, "916", (288, 672, 48, 192), -14.0, -1.0, 60, "YouTube Shorts, Google template values (contested)"),
    "universal916": (1080, 1920, "916", (288, 672, 65, 192), -14.0, -1.0, 60, "Union of Reels, TikTok and Shorts zones: one master for all 9:16"),
    "feed45":       (1080, 1350, "45",  (54, 54, 54, 54), -14.0, -1.0, 240, "Meta Feed 4:5, LinkedIn 4:5"),
    "square":       (1080, 1080, "11",  (54, 54, 54, 54), -14.0, -1.0, 240, "1:1 feeds, LinkedIn, Demand Gen"),
    "yt169":        (1920, 1080, "169", (100, 160, 96, 96), -14.0, -1.0, 180, "YouTube in-stream and Demand Gen 16:9; keep bottom right clear of skip button"),
    "linkedin169":  (1920, 1080, "169", (80, 120, 96, 96), -14.0, -1.0, 90, "LinkedIn desktop and mobile 16:9"),
    "ctv169":       (1920, 1080, "169", (108, 108, 192, 192), -24.0, -2.0, 30, "Connected TV, title safe 90 percent; ATSC A/85 -24 LKFS (use -23 for EBU R128 markets)"),
}

# Ad name grammar from creative-strategy (file stem = ad name without the launch date).
STEM_RE = re.compile(
    r"^(C\d{3})_([a-z]+)_([a-z0-9]+)_(unaw|prob|sol|prod|most)_"
    r"(ugc|cre|fdr|demo|test|uvt|list|ps|stat|car|meme|pod|str|gs|ai|cat)_"
    r"(H\d{2}|na)_(cr\d{2}|na)_(\d+s|na)_(916|45|11|169|na)_(v\d+)(_[a-zA-Z0-9-]+)?$"
)


def fail(msg):
    sys.exit("error: " + msg)


def q(s):
    return shlex.quote(str(s))


def run(cmd, capture=False):
    """Run a command list. Return (returncode, stdout+stderr text)."""
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return p.returncode, p.stdout


def esc_filter_path(path):
    """Escape a file path for use inside an ffmpeg filter argument."""
    return path.replace("\\", "/").replace(":", r"\:").replace("'", r"\'")


def video_chain(mode, w, h, fps, fx=0.5, fy=0.5, blur=40, pad_color="0x101010"):
    """Return (filter_complex_string, output_label). Input label is [0:v]."""
    common = f"setsar=1,fps={fps},format=yuv420p"
    if mode == "crop":
        chain = (f"[0:v]scale={w}:{h}:force_original_aspect_ratio=increase:flags=lanczos,"
                 f"crop={w}:{h}:(iw-{w})*{fx}:(ih-{h})*{fy},{common}[v]")
    elif mode == "pad":
        chain = (f"[0:v]scale={w}:{h}:force_original_aspect_ratio=decrease:flags=lanczos,"
                 f"pad={w}:{h}:({w}-iw)/2:({h}-ih)/2:color={pad_color},{common}[v]")
    elif mode == "pad-blur":
        chain = (f"[0:v]split=2[bgsrc][fgsrc];"
                 f"[bgsrc]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},gblur=sigma={blur},eq=brightness=-0.08[bg];"
                 f"[fgsrc]scale={w}:{h}:force_original_aspect_ratio=decrease:flags=lanczos[fg];"
                 f"[bg][fg]overlay=({w}-w)/2:({h}-h)/2,{common}[v]")
    elif mode == "fit":
        chain = f"[0:v]scale={w}:{h}:flags=lanczos,{common}[v]"
    else:
        fail(f"unknown mode {mode}")
    return chain, "[v]"


def tr_upper(text):
    """Uppercase that respects Turkish dotted and dotless i."""
    return text.replace("i", "\u0130").replace("\u0131", "I").upper()


def parse_srt(path):
    with open(path, encoding="utf-8-sig") as fh:
        blocks = re.split(r"\n\s*\n", fh.read().strip())
    cues = []
    for b in blocks:
        lines = [l for l in b.splitlines() if l.strip()]
        if len(lines) < 2:
            continue
        if "-->" in lines[0]:
            timing, text = lines[0], lines[1:]
        else:
            timing, text = lines[1], lines[2:]
        m = re.match(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)", timing)
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        start = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000.0
        end = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000.0
        cues.append((start, end, " ".join(text)))
    return cues


def ass_time(t):
    cs = int(round(t * 100))
    h, cs = divmod(cs, 360000)
    m, cs = divmod(cs, 6000)
    s, cs = divmod(cs, 100)
    return f"{h}:{m:02d}:{s:02d}.{cs:02d}"


def wrap(text, max_chars):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        if cur and len(cur) + 1 + len(wd) > max_chars:
            lines.append(cur)
            cur = wd
        else:
            cur = (cur + " " + wd).strip()
    if cur:
        lines.append(cur)
    return r"\N".join(lines[:2]) if len(lines) <= 2 else r"\N".join([lines[0], " ".join(lines[1:])])


def srt_to_ass(srt_path, ass_path, target, font="DejaVu Sans", size=None, upper=None,
               max_chars=28, position="lower"):
    w, h, _, (top, bottom, left, right), *_ = TARGETS[target]
    size = size or max(36, round(w * 0.058))
    if position == "center":
        align, margin_v = 5, 0
    else:
        align, margin_v = 2, bottom + round(h * 0.02)
    header = (
        "[Script Info]\nScriptType: v4.00+\nWrapStyle: 2\nScaledBorderAndShadow: yes\n"
        f"PlayResX: {w}\nPlayResY: {h}\n\n"
        "[V4+ Styles]\n"
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, "
        "Alignment, MarginL, MarginR, MarginV, Encoding\n"
        f"Style: Ad,{font},{size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,"
        f"{max(3, size // 12)},0,{align},{left + 20},{right + 20},{margin_v},1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    )
    out = [header]
    for start, end, text in parse_srt(srt_path):
        if upper == "tr":
            text = tr_upper(text)
        elif upper == "en":
            text = text.upper()
        text = wrap(text.replace("{", "(").replace("}", ")"), max_chars)
        out.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Ad,,0,0,0,,{text}\n")
    with open(ass_path, "w", encoding="utf-8") as fh:
        fh.write("".join(out))
    return ass_path


def loudnorm_args(lufs, tp, lra=11, measured=None):
    base = f"loudnorm=I={lufs}:TP={tp}:LRA={lra}"
    if not measured:
        return base
    return (base + f":measured_I={measured['input_i']}:measured_TP={measured['input_tp']}"
            f":measured_LRA={measured['input_lra']}:measured_thresh={measured['input_thresh']}"
            f":offset={measured['target_offset']}:linear=true:print_format=summary")


def measure_loudness(path, lufs, tp, start=None, end=None):
    cmd = ["ffmpeg", "-hide_banner", "-nostats", "-i", path]
    if start is not None:
        cmd += ["-ss", str(start)]
    if end is not None:
        cmd += ["-to", str(end)]
    cmd += ["-af", loudnorm_args(lufs, tp) + ":print_format=json", "-f", "null", "-"]
    code, out = run(cmd)
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", out, re.S)
    if code != 0 or not m:
        return None
    return json.loads(m.group(0))


def has_audio(path):
    code, out = run(["ffprobe", "-v", "error", "-select_streams", "a", "-show_entries",
                     "stream=index", "-of", "csv=p=0", path])
    return code == 0 and out.strip() != ""


def build_command(args, target, out_path, ass_path=None, measured=None, audio=True):
    w, h, ratio, safe, lufs, tp, max_s, _ = TARGETS[target]
    fc, label = video_chain(args.mode, w, h, args.fps, args.focus_x, args.focus_y)
    if ass_path:
        fc = fc[:-3] + f",ass='{esc_filter_path(ass_path)}'[v]"
    if args.hold_last:
        fc = fc[:-3] + f",tpad=stop_mode=clone:stop_duration={args.hold_last}[v]"
    cmd = ["ffmpeg", "-hide_banner", "-y", "-i", args.input]
    if args.start is not None:
        cmd += ["-ss", str(args.start)]
    if args.end is not None:
        cmd += ["-to", str(args.end)]
    cmd += ["-filter_complex", fc, "-map", label]
    if audio:
        af = loudnorm_args(lufs, tp, measured=measured)
        if args.hold_last:
            af = f"apad=pad_dur={args.hold_last}," + af
        cmd += ["-map", "0:a:0?", "-af", af, "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]
    else:
        cmd += ["-an"]
    cmd += ["-c:v", "libx264", "-preset", args.preset, "-crf", str(args.crf), "-profile:v", "high",
            "-pix_fmt", "yuv420p", "-g", str(int(args.fps) * 2), "-movflags", "+faststart", out_path]
    return cmd


def out_name(args, target):
    ratio = TARGETS[target][2]
    stem = args.stem or os.path.splitext(os.path.basename(args.input))[0]
    parts = [stem, ratio, args.ver] if args.ver else [stem, ratio]
    if args.flags:
        parts.append(args.flags)
    name = "_".join(parts)
    return os.path.join(args.out_dir, name + ".mp4"), name


def cmd_targets(_args):
    print(f"{'target':13} {'size':10} {'ratio':5} {'safe t/b/l/r':18} {'LUFS':6} {'TP':5} {'max s':5}  note")
    for k, (w, h, r, s, l, tp, mx, note) in TARGETS.items():
        print(f"{k:13} {w}x{h:<5} {r:5} {'/'.join(map(str, s)):18} {l:<6} {tp:<5} {mx:<5}  {note}")


def cmd_plan(args, execute=False):
    if not os.path.isfile(args.input) and execute:
        fail(f"input not found: {args.input}")
    targets = [t.strip() for t in args.targets.split(",") if t.strip()]
    for t in targets:
        if t not in TARGETS:
            fail(f"unknown target '{t}'. Run: targets")
    os.makedirs(args.out_dir, exist_ok=True) if execute else None
    audio = has_audio(args.input) if execute else (not args.no_audio)
    for t in targets:
        out_path, name = out_name(args, t)
        stem_check = name
        if args.stem and not STEM_RE.match(stem_check):
            print(f"# WARNING: '{stem_check}' does not parse with the creative-strategy name grammar", file=sys.stderr)
        ass_path = None
        if args.captions:
            ass_path = os.path.join(args.out_dir, name + ".ass")
            if execute:
                srt_to_ass(args.captions, ass_path, t, font=args.font, upper=args.upper,
                           max_chars=args.max_chars, position=args.caption_position)
            else:
                print(f"# captions: python3 ffmpeg_deliver.py srt2ass --srt {q(args.captions)} --target {t} --out {q(ass_path)}")
        lufs, tp = TARGETS[t][4], TARGETS[t][5]
        if audio:
            pass1 = ["ffmpeg", "-hide_banner", "-nostats", "-i", args.input]
            if args.start is not None:
                pass1 += ["-ss", str(args.start)]
            if args.end is not None:
                pass1 += ["-to", str(args.end)]
            pass1 += ["-af", loudnorm_args(lufs, tp) + ":print_format=json", "-f", "null", "-"]
        measured = None
        if execute and audio:
            measured = measure_loudness(args.input, lufs, tp, args.start, args.end)
            if measured is None:
                print(f"# {t}: loudness measurement failed, falling back to one-pass loudnorm", file=sys.stderr)
        cmd = build_command(args, t, out_path, ass_path, measured, audio)
        if not execute:
            print(f"# {t}: {TARGETS[t][7]}")
            if audio:
                print("# pass 1 (measure):  " + " ".join(q(c) for c in pass1))
                print("# pass 2 (render): copy measured_* values from pass 1 into loudnorm, or use `render`")
            print(" ".join(q(c) for c in cmd))
            print()
        else:
            code, out = run(cmd)
            status = "ok" if code == 0 else "FAILED"
            print(f"{t}: {status} -> {out_path}")
            if code != 0:
                print(out[-2000:], file=sys.stderr)
                sys.exit(1)


def cmd_overlay(args):
    w, h, _, (top, bottom, left, right), *_ = TARGETS[args.target]
    fc, _ = video_chain(args.mode, w, h, 30, args.focus_x, args.focus_y)
    shade = "red@0.35"
    boxes = [
        f"drawbox=x=0:y=0:w={w}:h={top}:color={shade}:t=fill",
        f"drawbox=x=0:y={h - bottom}:w={w}:h={bottom}:color={shade}:t=fill",
        f"drawbox=x=0:y={top}:w={left}:h={h - top - bottom}:color={shade}:t=fill",
        f"drawbox=x={w - right}:y={top}:w={right}:h={h - top - bottom}:color={shade}:t=fill",
        f"drawbox=x={left}:y={top}:w={w - left - right}:h={h - top - bottom}:color=lime@0.9:t=4",
    ]
    fc = fc[:-3] + "," + ",".join(boxes) + "[v]"
    cmd = ["ffmpeg", "-hide_banner", "-y", "-ss", str(args.at), "-i", args.input,
           "-filter_complex", fc, "-map", "[v]", "-frames:v", "1", args.out]
    if args.dry_run:
        print(" ".join(q(c) for c in cmd))
        return
    code, out = run(cmd)
    if code != 0:
        print(out[-2000:], file=sys.stderr)
        sys.exit(1)
    print(f"wrote {args.out} (shaded = unsafe for {args.target}; green box = safe area)")


def probe(path):
    code, out = run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", path])
    if code != 0:
        fail("ffprobe failed: " + out[-500:])
    return json.loads(out)


def cmd_check(args):
    w, h, ratio, _, lufs, tp, max_s, note = TARGETS[args.target]
    info = probe(args.input)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    dur = float(info["format"].get("duration", 0))
    results = []

    def res(name, ok, detail, blocker=True):
        results.append((name, ok, detail, blocker))

    if not v:
        fail("no video stream")
    num, den = (v.get("avg_frame_rate", "0/1").split("/") + ["1"])[:2]
    fps = float(num) / float(den) if float(den) else 0.0
    res("resolution", (v["width"], v["height"]) == (w, h), f"{v['width']}x{v['height']} (want {w}x{h})")
    res("video codec", v.get("codec_name") == "h264", v.get("codec_name"))
    res("pixel format", v.get("pix_fmt") == "yuv420p", v.get("pix_fmt"))
    res("frame rate", 23.0 <= fps <= 60.01, f"{fps:.3f} fps")
    res("duration", 0 < dur <= max_s, f"{dur:.2f}s (preset max {max_s}s; platform max may differ)", blocker=False)
    if args.expect_seconds:
        res("duration vs plan", abs(dur - args.expect_seconds) <= 0.5, f"{dur:.2f}s vs {args.expect_seconds}s")
    res("faststart", True, "check moov atom with: ffprobe -v trace (manual)", blocker=False)
    if a:
        res("audio codec", a.get("codec_name") == "aac", a.get("codec_name"))
        res("sample rate", a.get("sample_rate") in ("48000", "44100"), a.get("sample_rate"))
        code, out = run(["ffmpeg", "-hide_banner", "-nostats", "-i", args.input, "-af", "ebur128=peak=true",
                         "-f", "null", "-"])
        m_i = re.findall(r"I:\s+(-?[\d.]+|-inf)\s+LUFS", out)
        m_p = re.findall(r"Peak:\s+(-?[\d.]+|-inf)\s+dBFS", out)
        if m_i:
            ival = m_i[-1]
            if ival == "-inf":
                res("integrated loudness", False, "silent audio track")
            else:
                ival = float(ival)
                res("integrated loudness", abs(ival - lufs) <= args.lufs_tol, f"{ival} LUFS (target {lufs} +/- {args.lufs_tol})")
        if m_p and m_p[-1] != "-inf":
            pval = float(m_p[-1])
            res("true peak", pval <= tp + 0.2, f"{pval} dBTP (ceiling {tp})")
    else:
        res("audio", not args.require_audio, "no audio stream", blocker=args.require_audio)
    code, out = run(["ffmpeg", "-hide_banner", "-nostats", "-t", "1.0", "-i", args.input, "-vf",
                     "blackdetect=d=0.05:pix_th=0.10", "-an", "-f", "null", "-"])
    m = re.search(r"black_start:(\d+(?:\.\d+)?)", out)
    res("first frame not black", not (m and float(m.group(1)) < 0.05), "black at 0s" if m else "ok")
    stem = os.path.splitext(os.path.basename(args.input))[0]
    stem_core = re.sub(r"_(916|45|11|169)_(v\d+)(_[a-zA-Z0-9-]+)?$", "", stem)
    if args.check_name:
        res("name grammar", bool(STEM_RE.match(stem)), stem)
    failed = [r for r in results if not r[1] and r[3]]
    for name, ok, detail, blocker in results:
        tag = "PASS" if ok else ("FAIL" if blocker else "WARN")
        print(f"{tag:4}  {name:24} {detail}")
    print(f"\n{args.input}: {'PASS' if not failed else 'FAIL'} against {args.target} ({note})")
    sys.exit(1 if failed else 0)


def cmd_srt2ass(args):
    out = srt_to_ass(args.srt, args.out, args.target, font=args.font, size=args.size, upper=args.upper,
                     max_chars=args.max_chars, position=args.caption_position)
    print(f"wrote {out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("targets", help="list presets")

    def deliver_args(p):
        p.add_argument("--input", required=True)
        p.add_argument("--targets", required=True, help="comma list, e.g. reels,feed45,yt169")
        p.add_argument("--out-dir", default="deliver")
        p.add_argument("--stem", help="file stem without ratio and ver, e.g. C021_hcause_runner_prob_ugc_H03_cr07_30s")
        p.add_argument("--ver", default="", help="iteration token, e.g. v2")
        p.add_argument("--flags", default="", help="optional flags token, e.g. aiG-cta2-Ltr")
        p.add_argument("--mode", default="pad-blur", choices=["crop", "pad", "pad-blur", "fit"])
        p.add_argument("--focus-x", type=float, default=0.5, help="crop focus 0..1 (0 = left)")
        p.add_argument("--focus-y", type=float, default=0.5, help="crop focus 0..1 (0 = top)")
        p.add_argument("--fps", type=float, default=30)
        p.add_argument("--crf", type=int, default=18)
        p.add_argument("--preset", default="slow")
        p.add_argument("--start", type=float)
        p.add_argument("--end", type=float)
        p.add_argument("--hold-last", type=float, default=0.0, help="freeze the last frame N seconds (end card hold)")
        p.add_argument("--captions", help="SRT file to burn in (converted to ASS per target)")
        p.add_argument("--font", default="DejaVu Sans")
        p.add_argument("--upper", choices=["en", "tr"], help="uppercase captions; tr keeps dotted and dotless i correct")
        p.add_argument("--max-chars", type=int, default=28)
        p.add_argument("--caption-position", default="lower", choices=["lower", "center"])
        p.add_argument("--no-audio", action="store_true", help="plan only: assume no audio track")

    deliver_args(sub.add_parser("plan", help="print commands (dry run)"))
    deliver_args(sub.add_parser("render", help="run commands"))

    p = sub.add_parser("overlay", help="safe-zone QA frame")
    p.add_argument("--input", required=True)
    p.add_argument("--target", required=True, choices=list(TARGETS))
    p.add_argument("--at", type=float, default=1.0)
    p.add_argument("--out", default="safezone.png")
    p.add_argument("--mode", default="fit", choices=["crop", "pad", "pad-blur", "fit"])
    p.add_argument("--focus-x", type=float, default=0.5)
    p.add_argument("--focus-y", type=float, default=0.5)
    p.add_argument("--dry-run", action="store_true")

    p = sub.add_parser("check", help="QA a delivered file")
    p.add_argument("--input", required=True)
    p.add_argument("--target", required=True, choices=list(TARGETS))
    p.add_argument("--lufs-tol", type=float, default=1.0)
    p.add_argument("--expect-seconds", type=float)
    p.add_argument("--require-audio", action="store_true")
    p.add_argument("--check-name", action="store_true", help="validate the full stem against the name grammar")

    p = sub.add_parser("srt2ass", help="SRT to safe-zone ASS")
    p.add_argument("--srt", required=True)
    p.add_argument("--target", required=True, choices=list(TARGETS))
    p.add_argument("--out", required=True)
    p.add_argument("--font", default="DejaVu Sans")
    p.add_argument("--size", type=int)
    p.add_argument("--upper", choices=["en", "tr"])
    p.add_argument("--max-chars", type=int, default=28)
    p.add_argument("--caption-position", default="lower", choices=["lower", "center"])

    args = ap.parse_args()
    if args.cmd == "targets":
        cmd_targets(args)
    elif args.cmd == "plan":
        cmd_plan(args, execute=False)
    elif args.cmd == "render":
        cmd_plan(args, execute=True)
    elif args.cmd == "overlay":
        cmd_overlay(args)
    elif args.cmd == "check":
        cmd_check(args)
    elif args.cmd == "srt2ass":
        cmd_srt2ass(args)


if __name__ == "__main__":
    main()
