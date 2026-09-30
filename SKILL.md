---
name: journal-writer
description: Turns a video/presentation transcript, a dev-journal, or just your own account of what happened into a long-form blog post — for Medium or a personal blog. Pulls raw material from whichever source fits (fetches a video's caption track, reads dev-journal entries, or asks you directly), builds a digest you confirm, proposes a structure that fits the material (problem/process/results/learnings, narrative arc, launch announcement, lessons-learned, or question-framed essay — not a fixed template), drafts in your voice, then runs a long-form de-slop pass before it reaches you. It never publishes anything. Use this skill whenever someone wants to write a Medium post, a blog entry, a long-form write-up of a project or talk, turn a presentation or demo transcript into an article, or write up "what I built and learned" as a proper post rather than a tweet. Trigger on requests like "write a blog post about X," "turn this transcript into an article," "can you write up this project," or pasting a video link/transcript and asking for a write-up. Not for short X/Twitter posts (see the daily-dev-journal skill), LinkedIn posts (different audience/format — see writer-linkedin), job-application answers or cover letters, release notes/changelogs alone, or docs/reports meant for internal collaboration rather than publishing.
---

# Journal Writer

Turn raw material — a talk you gave, a project you shipped, a day that actually had something in it — into a blog post that reads like you wrote it, not like it was generated about you.

Two hard rules:
- **This skill never publishes.** It hands you a finished draft as copy-paste-ready text (or a file). Posting to Medium or wherever it's going is always your move.
- **Nothing from a private or work context goes out without you saying yes.** See Step 7.

## The workspace

All user data lives outside this skill directory:

```
~/journal-writer/
├── config.md      # handle, voice, audience, sources, redaction list, format prefs
└── posts/         # archive of digests + drafts, one file per post
```

Create `posts/` on first use. Never commit anything from the workspace into this skill's repo — it can contain private project names, client names, and unpublished work.

## Step 0 — Config (first run only)

Check for `~/journal-writer/config.md`. If it's missing, copy `assets/config-template.md` there, then fill it in with the user — ask briefly for:

- **Name / handle** and **voice skill** — if a personal writing-voice skill exists (something like `yourname-voice`), record its name and use it in Step 5. Otherwise take cues from how the user writes in conversation.
- **Audience & angle** — who reads these, and where they usually go (Medium, a personal blog). This shapes length and tone defaults, not an actual publishing integration.
- **dev-journal location** — default `~/dev-journal/`, used when Step 2 pulls from project work.
- **Always/never write about** and a **redaction list** — same purpose as any personal-writing skill: know what's off-limits before a draft ever mentions it.
- **Format prefs** — default length, whether structure should always be proposed fresh (default) or usually follows one template, section-header style, closing style.

Tell the user they can edit `config.md` directly anytime. Re-read it at the start of every run.

## Step 1 — Intake

Establish two things before gathering anything:

1. **What's this post about?** A project, a talk, a launch, a reflection — get the one-line version first.
2. **What's the source?** Ask directly rather than assuming:
   - A video or presentation link → transcript extraction (Step 2).
   - A project already tracked in the dev-journal → journal read (Step 2).
   - Nothing written down yet → the user just tells you (Step 2, "Freeform").
   - More than one of the above at once is fine — note all of them.

## Step 2 — Gather the raw material

Extraction method depends entirely on the source type. Full detail, including the video-transcript extraction procedure (script + browser-assisted fallback) and the freeform prompts to use when nothing's written down, is in `references/source-extraction.md` — read it before this step on a video/transcript source, since the fallback path isn't obvious.

Short version:
- **Video/presentation:** `python3 scripts/fetch_transcript.py "<url>"`, then read the resulting `.vtt` and reconstruct it into flowing paragraphs (don't hand raw cue-by-cue text to the draft step). If the script fails, use the browser-assisted fallback documented in the reference file.
- **dev-journal:** read entries at the configured location for the relevant project.
- **Freeform:** ask the user to walk you through what happened — capture their actual words and specifics, not a paraphrase.
- **Multiple sources:** gather each separately, merge into one digest in Step 3.

## Step 3 — Build the digest and confirm it

From the gathered material, write a plain digest — no polish yet:

- **What actually happened** (the facts, in order or by theme, however they naturally group)
- **The specific details worth keeping** — numbers, tool names, exact phrasing, the moment something clicked or broke
- **Open questions** — anything unclear, missing, or that needs the user's own framing to make sense

Show it to the user. This is the editorial checkpoint: they confirm what's accurate, flag anything private, and often add the detail that makes the piece real. Don't move to structure until they've reacted to it.

## Step 4 — Propose a structure

Read `references/blog-structures.md`. Based on the confirmed digest's natural shape, propose the structure that fits best — problem/process/results/learnings, narrative arc, launch/update, lessons-learned, or question-framed essay — with one line of reasoning for why. If `config.md` names a default structure, propose that first but still check it actually fits this material rather than applying it blindly.

Let the user approve or redirect before drafting. This is a deliberate step, not a formality — the wrong structure forces the draft into a shape the material doesn't have, and it reads as generic no matter how well the prose is written after.

## Step 5 — Draft

Draft in the user's voice (use their `-voice` skill if `config.md` names one; otherwise match how they write in conversation). Follow the chosen structure from Step 4 and the section-header / closing-style prefs from `config.md`.

Keep the specific details from Step 3's digest in the draft — names, numbers, exact quotes. These are exactly what a generic rewrite erodes first, and they're what makes the piece read as written by someone who was actually there.

## Step 6 — De-slop pass

Read the draft back against `references/de-slop.md` — editorializing closers, tricolon/em-dash pile-ups, generic transitions, humble-brag disclaimers, corporate jargon, flowery abstraction standing in for a real detail. The test: could this paragraph have been written by someone who wasn't actually there? If yes, find the specific detail that's missing and put it back.

## Step 7 — Privacy pass

Before anything is handed over, check the draft against the `config.md` redaction list:

- **Employer / client work** — flag it if the post touches on a job or client engagement; ask before any of it goes out, even genericized.
- **Private repo names, internal URLs, unreleased product/feature names, teammates' names** — mask or cut per the redaction list.
- **Anything that reveals more than the user intended** — an offhand detail in the source material that wasn't meant for a public post.

When in doubt, show the user exactly what's identifying and let them decide, with a genericized alternative ready if they want it.

## Step 8 — Deliver and archive

Present the final draft as clean, copy-paste-ready text (or write it to a file if the user wants one). State the rough word count. **Do not publish, and don't offer to** — the user takes it to Medium (or wherever) themselves.

Archive to `~/journal-writer/posts/<slug>.md`:

```markdown
# <title>

## Source
<what this was built from — video link, dev-journal entry, or "freeform">

## Digest
<the confirmed digest from Step 3>

## Structure
<which structure was used and why>

## Draft
<the final draft>
```

## Reference files

- `references/source-extraction.md` — how to pull raw material from a video/presentation transcript (script + browser-assisted fallback), a dev-journal, or a freeform account.
- `references/blog-structures.md` — the five structure templates, what each fits, and how to pick.
- `references/de-slop.md` — long-form AI-writing tells and how to catch them.
- `assets/config-template.md` — the config scaffold copied to `~/journal-writer/config.md` on first run.
- `scripts/fetch_transcript.py` — fetches a video's caption track via `yt-dlp`; `--help` for options.
