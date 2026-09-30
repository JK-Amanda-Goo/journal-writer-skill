#!/usr/bin/env python3
"""Fetch a video/presentation's caption track as plain VTT.

Tries yt-dlp first (reliable for YouTube, and for Vimeo videos that don't
sit behind Cloudflare bot-protection). If that fails, prints the manual
browser-assisted fallback procedure instead of guessing further.

Usage:
    python3 fetch_transcript.py <url> [-o OUTPUT.vtt] [--lang en]
"""
import argparse
import glob
import os
import shutil
import subprocess
import sys
import tempfile


FALLBACK_MESSAGE = """
yt-dlp could not pull captions for this URL directly (common for Vimeo
videos behind Cloudflare bot-protection, or private/unlisted videos).

Fall back to the browser-assisted method — see
references/source-extraction.md, "Browser-assisted fallback" section:

  1. Open the video URL in a real browser session (Claude in Chrome).
  2. Play the video briefly and click the CC/subtitles control so the
     caption track actually loads.
  3. Read the tab's network requests filtered by ".vtt" — the caption
     file URL is signed and short-lived but needs no auth to fetch.
  4. curl that signed URL to a local .vtt file.
  5. Run: python3 fetch_transcript.py --convert-only <path-to.vtt>
     (or just hand the raw .vtt content to the agent — it reads cue text
     directly and reconstructs prose in the Gather step).
""".strip()


def run_ytdlp(url: str, lang: str, workdir: str) -> str | None:
    cmd = [
        "yt-dlp",
        "--skip-download",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", lang,
        "--sub-format", "vtt",
        "--no-warnings",
        "-o", os.path.join(workdir, "%(id)s.%(ext)s"),
        url,
    ]
    try:
        subprocess.run(cmd, check=True, capture_output=True, text=True, timeout=90)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError):
        return None

    matches = glob.glob(os.path.join(workdir, f"*.{lang}*.vtt"))
    if not matches:
        matches = glob.glob(os.path.join(workdir, "*.vtt"))
    return matches[0] if matches else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", nargs="?", help="Video URL (YouTube, Vimeo, etc.)")
    parser.add_argument("-o", "--out", default=None, help="Output .vtt path")
    parser.add_argument("--lang", default="en", help="Subtitle language (default: en)")
    parser.add_argument(
        "--convert-only",
        metavar="VTT_FILE",
        help="Skip fetching; just copy/normalize an already-downloaded .vtt to --out",
    )
    args = parser.parse_args()

    if args.convert_only:
        dest = args.out or os.path.basename(args.convert_only)
        shutil.copy(args.convert_only, dest)
        print(f"Wrote {dest}")
        return 0

    if not args.url:
        parser.error("a video URL is required unless --convert-only is used")

    with tempfile.TemporaryDirectory() as tmp:
        vtt_path = run_ytdlp(args.url, args.lang, tmp)
        if not vtt_path:
            print(FALLBACK_MESSAGE, file=sys.stderr)
            return 1

        dest = args.out or os.path.basename(vtt_path)
        shutil.copy(vtt_path, dest)
        print(f"Wrote {dest}")
        return 0


if __name__ == "__main__":
    sys.exit(main())
