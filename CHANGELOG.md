# Changelog

All notable changes to this skill are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions are tagged in git and published as GitHub Releases.

## [0.1.0] - 2026-09-29

Initial release.

- 9-step workflow: config setup → intake (topic + source) → gather raw material (video transcript / dev-journal / freeform) → confirm a digest → propose a structure that fits the material → draft in the user's voice → long-form de-slop pass → privacy/redaction pass → deliver and archive.
- Never publishes; taking the draft to Medium or elsewhere is always a human action.
- Structure is proposed per post from five templates, not fixed to one — `references/blog-structures.md` (problem/process/results/learnings, narrative arc, launch/update, lessons-learned, question-framed essay).
- `references/source-extraction.md` — video/presentation transcript extraction (via `yt-dlp`, with a browser-assisted fallback for Cloudflare-protected platforms like Vimeo, documented from a real extraction case on 2026-09-29), dev-journal reading, and freeform intake.
- `references/de-slop.md` — long-form AI-writing tells (editorializing closers, tricolon/em-dash pile-ups, generic transitions, humble-brag disclaimers, corporate jargon).
- `assets/config-template.md` — config scaffold (handle, audience, sources, always/never-write-about, redaction list, format prefs).
- `scripts/fetch_transcript.py` — fetches a video's caption track via `yt-dlp`, with a `--convert-only` mode for normalizing a manually-downloaded `.vtt`.

[0.1.0]: https://github.com/JK-Amanda-Goo/journal-writer-skill/releases/tag/v0.1.0
