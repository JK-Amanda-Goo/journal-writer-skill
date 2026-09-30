# Pulling raw material out of a source

The Gather step (SKILL.md Step 2) has to turn whatever the user points at into text the drafting step can work with. Three source types, three different extraction paths.

## Video / presentation transcripts

Most video platforms carry a caption track even when nobody's watching it — auto-generated or uploaded. That track is the fastest way to get exact spoken content without asking the user to re-type a talk.

**First, try the script:**

```bash
python3 scripts/fetch_transcript.py "<video url>"
```

This shells out to `yt-dlp`, which handles YouTube reliably and plenty of Vimeo videos too. If it writes a `.vtt` file, move to "Reading a .vtt file" below.

**If it fails** — commonly on Vimeo videos sitting behind Cloudflare bot-protection (confirmed 2026-09-29: `yt-dlp` got a 401 trying to fetch an OAuth token for a Cloudflare-Turnstile-protected Vimeo page) — use the browser-assisted fallback:

### Browser-assisted fallback

1. Open the video's page in a real browser session (Claude in Chrome tools: `tabs_context_mcp` → `navigate`).
2. Take a screenshot to confirm the player loaded, then click into the video area to start playback briefly.
3. Click the CC/subtitles control in the player controls — this is often what actually triggers the caption track to load over the network; it may not fire just from the page loading.
4. Read the tab's network requests filtered by the string `.vtt` (or `texttrack` / `captions` for other platforms). Vimeo serves signed URLs like `https://captions.vimeo.com/captions/<id>.vtt?expires=...&sig=...` — the signature makes the URL itself sufficient, no auth headers needed.
5. `curl` that URL directly to a local `.vtt` file. This works from a plain shell even though the player page itself is Cloudflare-gated — the signed caption URL isn't behind the same check.
6. Close the browser tab when done (`tabs_close_mcp`).

If no `.vtt` request ever shows up, the video has no caption track at all — ask the user whether they want to paste a transcript themselves, or narrate the content directly (see "Freeform" below).

### Reading a .vtt file

Don't hand the raw cue-by-cue VTT to the draft step. WebVTT auto-captions break sentences across cues arbitrarily — a cue often ends mid-clause. Read the whole file, then reconstruct it into flowing paragraphs:

- Drop cue numbers and timestamps.
- Merge cues into full sentences and group sentences into paragraphs at natural topic or pause boundaries — not one paragraph per cue.
- Watch for auto-caption artifacts at cue boundaries (two words fused with no space, a stray capital mid-sentence) and fix them by ear against the surrounding text.
- Keep the speaker's actual words. This step is formatting, not rewriting — the drafting step is where voice and shaping happen.

## Dev-journal entries

If the config names a `dev-journal location` (default `~/dev-journal/`), look for entries relevant to the project or date range the user names:

```bash
ls ~/dev-journal/<project>/*.md 2>/dev/null
```

Read what's there. A dev-journal entry is already curated and reflective — treat it as stronger signal than a raw transcript, but it may only cover part of the story (the technical decisions, not the "why" the user would tell a reader). Ask the user to fill gaps rather than inferring them.

## Freeform (the user just tells you)

Sometimes there's no artifact — the user wants to write about something they haven't recorded anywhere. Don't try to extract from nothing: ask directly. Useful prompts:

- "Walk me through what happened, in whatever order it comes to mind."
- "What was the moment this became a story worth telling?"
- "What did you actually try that didn't work, before what did?"

Capture their own words and specifics (numbers, names of tools, the actual line someone said) as the raw material — these are exactly what a later de-slop pass (`references/de-slop.md`) has to protect, because they're what a generic AI rewrite would sand off first.

## Multiple sources at once

A post can pull from more than one source — e.g. a talk transcript plus a dev-journal entry that covers the technical side the talk skipped. Gather each separately, then merge into one digest for Step 3 rather than drafting from either source alone.
