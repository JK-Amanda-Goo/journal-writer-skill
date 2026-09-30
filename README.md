# Journal Writer (Claude Code skill)

A [Claude Code](https://docs.claude.com/en/docs/claude-code) skill that turns raw material — a talk transcript, a dev-journal, or your own account of what happened — into a long-form blog post, for Medium or a personal blog.

It pulls source material from whatever fits (fetches a video's caption track, reads a dev-journal, or just asks you), builds a plain digest you confirm, proposes a structure that actually matches the material instead of forcing a fixed template, drafts in your voice, and runs a long-form de-slop pass before it reaches you.

**It never publishes anything.** You get a finished draft; taking it to Medium (or wherever) is always your move.

## Why the structure isn't fixed

A project retrospective, a personal reflection, and a launch announcement don't have the same shape, and forcing all three into one template is exactly what makes AI-assisted writing read as generic. This skill proposes from five structures — problem/process/results/learnings, narrative arc, launch/update, lessons-learned, question-framed essay — based on what the gathered material actually looks like, and asks before drafting.

## Install

```bash
git clone https://github.com/JK-Amanda-Goo/journal-writer-skill ~/Projects/journal-writer-skill
ln -s ~/Projects/journal-writer-skill ~/.claude/skills/journal-writer
```

On first run the skill creates `~/journal-writer/config.md` from a template and walks you through filling it in — handle, audience, sources, a redaction list, and format preferences.

## Use it

> "write a blog post about this project" · "turn this talk into an article" · "can you write up this launch" · paste a video link and ask for a write-up

It asks what the post is about and where the source material lives, then works through a confirmed digest and a proposed structure with you before drafting.

## Sources it can pull from

- **Video/presentation transcripts** — via `yt-dlp` where that works, with a browser-assisted fallback (documented in `references/source-extraction.md`) for platforms that block automated fetches.
- **A local dev-journal**, if you keep one.
- **Freeform** — you just tell it what happened.

A post can mix more than one source.

## Requirements

- Claude Code (or another agent that supports skills), with Python 3 and [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) on `PATH` for the transcript-fetch script.
- No API keys, no publishing integration. Everything else needs nothing external.

## Voice

If you have a personal writing-voice skill (something like `yourname-voice`), name it in `config.md` and this skill drafts through it. Without one, it matches how you write in the conversation.

## What this intentionally doesn't do

- **Publish.** It drafts; you post.
- **Force a template.** Structure is proposed from the material, not assumed.
- **Leak your work.** Employer, client, and private-repo material is flagged and held back until you say otherwise.
- **Replace short-form.** This is for a proper blog post, not a tweet (see [daily-dev-journal](https://github.com/JK-Amanda-Goo/daily-dev-journal-skill)) or a LinkedIn post (different audience/format).

## Files

- `SKILL.md` — the workflow
- `references/source-extraction.md` — pulling raw material from video transcripts, dev-journals, or freeform accounts
- `references/blog-structures.md` — the five structure templates and how to pick one
- `references/de-slop.md` — long-form AI-writing tells and how to catch them
- `assets/config-template.md` — the config scaffold
- `scripts/fetch_transcript.py` — fetches a video's caption track via `yt-dlp`

## Releasing

Every notable change gets a `CHANGELOG.md` entry (Keep a Changelog format), a matching git tag, and a GitHub Release whose notes are that changelog section:

```bash
# 1. Add a new version section to the top of CHANGELOG.md
# 2. git add -A && git commit -m "..."
git tag -a vX.Y.Z -m "vX.Y.Z - <one-line summary>"
git push origin main --tags
gh release create vX.Y.Z --title "vX.Y.Z" --notes "<paste the CHANGELOG section>"
```

## License

MIT — see `LICENSE`.
