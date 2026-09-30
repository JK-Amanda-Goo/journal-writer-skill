# journal-writer config

Edit this file freely. The skill reads it at the start of every run.

## Identity

- **Name / handle:** <how you sign, or leave blank>
- **Voice skill:** <name of your personal writing-voice skill, e.g. `yourname-voice`, or "none">

## Audience & angle

- **Who I'm writing for:** <e.g. other builders / a hiring audience / people in my creative field>
- **Where these usually go:** <e.g. Medium, a personal blog, a newsletter — informs length and tone defaults, not a hard platform integration>

## Sources

- **dev-journal location:** ~/dev-journal/
  <the skill looks here when a post draws on project work. If you don't keep one, leave the default — it just won't find anything and will ask you directly instead.>

## What's fair game

- **Always OK to write about:** <projects / topics with no restrictions>
- **Never write about:** <off-limits — a client engagement, an employer's internal work, a stealth project>

## Redaction list

Names and strings to strip or mask before anything goes out:

- Current employer: <name, or blank>
- Past employers: <names — note which ones you *do* want named with a credential parenthetical, e.g. "Sendbird (YC W16)", vs. ones to omit entirely>
- Clients: <names>
- Private repos / unreleased product names: <names>
- Teammates' names: <names, or "mask all">

## Format preferences

- **Default length:** 800-1500 words   <long-form default; adjust per platform if it differs>
- **Structure:** flexible — proposed per post   <or name a structure you default to, e.g. "PPRL" — see references/blog-structures.md>
- **Section headers:** bracketed (`[Like this]`)   <or "## Markdown headers" / "none — flowing prose">
- **Closing style:** forward-looking   <what you want the last paragraph to do — reflect, ask a question, state what's next>
