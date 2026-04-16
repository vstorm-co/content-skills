# content-skills

A skill pack for Claude Code that provides a complete content creation studio with brand consistency enforcement.

## What This Is

content-skills is a modular skill pack that handles the full content lifecycle: brand setup, strategy, writing, visual design, video scripting, cross-platform repurposing, and quality auditing. Every piece of content produced through this pack stays consistent with the user's defined brand identity.

## Repository Structure

```
content-skills/
├── CLAUDE.md              ← you are here
├── content/SKILL.md       ← main router skill (orchestrates all subcommands)
├── brand/                 ← shared brand source of truth
│   ├── BRAND.md           ← core identity, audience, positioning
│   ├── VOICE.md           ← voice & tone rules, vocabulary, banned phrases
│   ├── VISUAL.md          ← colors, typography, logo usage, visual style
│   ├── assets/            ← brand asset files
│   ├── fonts/             ← typeface files
│   ├── logo/              ← logo variants
│   ├── palettes/          ← color palette definitions
│   └── voice-samples/     ← reference writing samples for voice extraction
├── skills/                ← individual content sub-skills
│   ├── content-setup/     ← brand onboarding & voice profiling
│   ├── content-blog/      ← long-form blog post generation
│   └── ...                ← additional sub-skills per content type
├── agents/                ← agent definitions for parallel workflows
├── scripts/               ← Python utility scripts (anti-slop checker, readability, etc.)
├── styles/                ← default style tokens (typography, palettes, layouts)
└── assets/                ← shared asset files
```

## The Brand System

The `brand/` directory is the single source of truth for all content generation. Three files form the core:

- **brand/BRAND.md** -- Who you are. Name, mission, audience, positioning, differentiators.
- **brand/VOICE.md** -- How you sound. Tone, formality, vocabulary, banned phrases, per-platform overrides.
- **brand/VISUAL.md** -- How you look. Colors, typography, logo rules, image style.

All skills read from `brand/` at generation time. Sub-skills never hard-code brand assumptions.

If `brand/` is not configured, skills use sensible defaults and suggest running `/content setup`.

## Key Conventions

1. **All skills read from brand/.** No skill stores its own brand data. The brand directory is the shared contract.

2. **Anti-slop is always enforced.** Every piece of content is checked against the anti-slop rules before delivery. No generic openings, no buzzword padding, no filler phrases, no uniform paragraph lengths. See `skills/content-blog/anti-slop.md` for the full list.

3. **Voice consistency is always checked.** If `brand/VOICE.md` exists, every text-producing skill matches its tone, vocabulary, and rhythm. The brand guardian agent runs as a quality gate before finalization.

4. **Agents run in parallel when tasks are independent.** Repurposing spawns one agent per platform. Series creation can parallelize individual posts. Audits across multiple pieces run concurrently.

5. **Scripts are standalone utilities.** Each Python script in `scripts/` can be run independently with `python scripts/<name>.py`. They use argparse and output JSON where applicable.

6. **Styles provide defaults.** The `styles/` directory contains default tokens (typography, palettes, layouts) that are overridden by `brand/VISUAL.md` when it exists.
