---
name: content
description: Content studio with brand consistency. Use this skill whenever the user wants to create content — blog posts, social media (X/Twitter, LinkedIn, Reddit, HN), presentations (Slidev/Reveal/Spectacle), infographics, image prompts, video scripts (Remotion), editorial calendars, or content audits. Also triggers on brand setup, voice profiling, content repurposing, and content strategy. Covers any request involving writing, publishing, visual content creation, or content planning. Even if the user doesn't say "content" explicitly — if they're asking to write a blog post, create slides, draft a thread, plan a content calendar, or check content quality — use this skill.
---

# Content Studio — Main Router

This is the orchestrator skill for the content-skills pack. It receives `/content <subcommand>` invocations and delegates to the correct sub-skill. It does not generate content itself — it routes, enforces brand consistency, and coordinates multi-step workflows.

The pack is organized around a shared brand system. Every sub-skill reads from the same brand configuration, so voice, tone, visual identity, and audience targeting stay consistent whether the user is writing a blog post, drafting a LinkedIn update, or building a slide deck.

---

## Skill Pack Structure

```
content-skills/
├── content/SKILL.md          ← you are here (main router)
├── brand/                     ← shared brand source of truth
│   ├── BRAND.md               ← core identity: name, tagline, audience, positioning
│   ├── VOICE.md               ← voice & tone rules, vocabulary, banned phrases
│   ├── VISUAL.md              ← colors, typography, logo usage, visual style
│   ├── assets/                ← brand asset files
│   ├── fonts/                 ← typeface files
│   ├── logo/                  ← logo variants
│   ├── palettes/              ← color palette definitions
│   └── voice-samples/         ← reference writing samples
├── skills/                    ← individual content sub-skills
│   ├── content-setup/         ← brand setup & voice profiling
│   ├── content-strategy/      ← strategy, planning, briefs
│   ├── content-blog/          ← long-form blog posts
│   ├── content-twitter/       ← X/Twitter threads & posts
│   ├── content-linkedin/      ← LinkedIn posts & articles
│   ├── content-reddit/        ← Reddit posts & comments
│   ├── content-hackernews/    ← Hacker News posts
│   ├── content-presentation/  ← Slidev/Reveal/Spectacle decks
│   ├── content-infographic/   ← data visualizations & infographics
│   ├── content-image/         ← image generation prompts
│   ├── content-video/         ← Remotion video scripts
│   ├── content-calendar/      ← editorial calendar management
│   ├── content-repurpose/     ← cross-platform content adaptation
│   └── content-audit/         ← content quality scoring & audits
├── agents/                    ← agent definitions for parallel workflows
├── scripts/                   ← utility scripts
├── styles/                    ← shared style assets
└── assets/                    ← shared asset files
```

---

## The Brand Directory

The `brand/` directory is the single source of truth for all content generation. Three files form the core:

- **brand/BRAND.md** — Who you are. Company/personal name, tagline, mission, target audience segments, positioning statement, competitors, key differentiators. Every sub-skill reads this to understand context.

- **brand/VOICE.md** — How you sound. Tone dimensions (e.g., formal vs. casual, technical vs. accessible), vocabulary preferences, banned words/phrases, sentence rhythm guidelines, humor policy, jargon stance. Includes per-platform overrides (LinkedIn might be more formal than Twitter).

- **brand/VISUAL.md** — How you look. Primary and secondary color palettes, typography scale, logo usage rules, image style preferences, layout principles. Used by presentation, infographic, and image sub-skills.

Sub-skills must never hard-code brand assumptions. Always read from `brand/` at generation time.

---

## Routing Table

When the user invokes `/content <subcommand>`, match the subcommand below and delegate to the corresponding sub-skill. Pass along all remaining arguments and context.

| Subcommand | Routes To | What It Does |
|---|---|---|
| `setup` | `skills/content-setup/SKILL.md` | Initialize brand identity. Walks the user through defining BRAND.md, VOICE.md, and VISUAL.md via an interactive questionnaire. |
| `brand show` | `skills/content-setup/SKILL.md` | Display the current brand configuration in a readable summary. |
| `brand update` | `skills/content-setup/SKILL.md` | Modify specific brand attributes without re-running full setup. |
| `voice` | `skills/content-setup/SKILL.md` | Analyze writing samples to extract and codify voice characteristics into VOICE.md. |
| `strategy` | `skills/content-strategy/SKILL.md` | Develop a content strategy: audience analysis, topic pillars, channel mix, publishing cadence. |
| `plan` | `skills/content-strategy/SKILL.md` | Create a content plan for a specific time period with topics, formats, and deadlines. |
| `brief` | `skills/content-strategy/SKILL.md` | Generate a detailed content brief for a single piece: angle, audience, key points, CTA, SEO targets. |
| `blog` | `skills/content-blog/SKILL.md` | Write a long-form blog post. Handles outlining, drafting, SEO metadata, and revision. |
| `twitter` | `skills/content-twitter/SKILL.md` | Create X/Twitter content: single tweets, threads, quote tweets, reply strategies. |
| `linkedin` | `skills/content-linkedin/SKILL.md` | Write LinkedIn posts, articles, and engagement content. Handles formatting for the platform's algorithm. |
| `reddit` | `skills/content-reddit/SKILL.md` | Draft Reddit posts and comments. Adapts tone per subreddit norms. |
| `hn` | `skills/content-hackernews/SKILL.md` | Write Hacker News submissions and comments. Emphasizes technical substance and avoids promotional tone. |
| `presentation` | `skills/content-presentation/SKILL.md` | Build slide decks in Slidev, Reveal.js, or Spectacle. Generates content, speaker notes, and styling. |
| `infographic` | `skills/content-infographic/SKILL.md` | Design data visualizations and infographic layouts with structured data and visual direction. |
| `image` | `skills/content-image/SKILL.md` | Generate detailed image prompts for AI image generators (DALL-E, Midjourney, Stable Diffusion). Brand-aligned style direction. |
| `video` | `skills/content-video/SKILL.md` | Write Remotion video scripts: scene structure, narration, motion graphics direction, timing. |
| `calendar` | `skills/content-calendar/SKILL.md` | Build and manage editorial calendars. Track content status, deadlines, and publishing schedules. |
| `repurpose` | `skills/content-repurpose/SKILL.md` | Adapt existing content across platforms. Takes one piece and produces variants for multiple channels. |
| `audit` | `skills/content-audit/SKILL.md` | Score content against quality criteria: brand alignment, readability, SEO, engagement potential. |
| `score` | `skills/content-audit/SKILL.md` | Alias for audit. Quick quality score on a piece of content. |
| `series` | *compound workflow* | Combines strategy + blog + repurpose. Plans a content series, writes the anchor post, then generates platform-specific variants. See "Compound Workflows" below. |

### Routing Rules

1. Match the first argument after `/content` against the subcommand column.
2. If the subcommand is unrecognized, list the available subcommands and ask the user to clarify.
3. If no subcommand is provided, show a brief help summary with all available subcommands.
4. Pass all remaining arguments, flags, and conversation context to the target sub-skill.
5. For compound workflows like `series`, execute sub-skills sequentially, passing output from each step as input to the next.

---

## Brand Integration Protocol

Before generating any content — in any sub-skill — execute this protocol:

### Step 1: Check for Brand Configuration

Look for `brand/BRAND.md` in the skill pack root.

### Step 2a: Brand Exists

If `brand/BRAND.md` exists:

1. Read `brand/BRAND.md` for core identity.
2. Read `brand/VOICE.md` if it exists. Apply voice rules to all text generation. If the sub-skill targets a specific platform, check for platform-specific overrides within VOICE.md.
3. Read `brand/VISUAL.md` if it exists and the sub-skill produces visual output (presentation, infographic, image).
4. Check `brand/voice-samples/` for reference material if doing voice-sensitive work.
5. Apply all brand constraints as hard requirements, not suggestions.

### Step 2b: No Brand Configuration

If `brand/BRAND.md` does not exist:

1. Use sensible defaults: professional tone, clear language, no jargon assumptions.
2. Proceed with content generation — do not block the user.
3. After delivering the content, add a note:

   > Your content pack doesn't have a brand profile yet. Run `/content setup` to define your brand identity, voice, and visual style. This makes all future content consistent and on-brand.

4. Do not repeat this suggestion if the user has already been told in the current session.

### Brand Override

If the user provides explicit instructions that conflict with the brand files (e.g., "make this more casual" when VOICE.md says formal), follow the user's instruction for that specific piece. Do not modify the brand files unless the user requests it via `/content brand update`.

---

## Anti-Slop Commitment

Every piece of content produced by this skill pack must meet these standards. These are non-negotiable.

### Banned Patterns

Do not produce content that:

- Opens with "In today's [fast-paced/ever-changing/digital] world..."
- Uses "leverage" as a verb when "use" works fine
- Strings together buzzwords without concrete meaning ("synergize cross-functional paradigms")
- Includes hollow calls to action ("Don't miss out!", "Act now!")
- Uses filler transitions ("Furthermore," "Moreover," "It's worth noting that")
- Pads sentences to sound more "professional" or "authoritative"
- Defaults to listicle format when the topic deserves depth
- Contains the phrase "game-changer," "deep dive," "unpack," or "at the end of the day" without irony
- Uses "delve" in any context
- Employs the passive voice to obscure who is doing what
- Includes self-referential hedging ("As an AI..." or "I'd be happy to...")

### Quality Principles

Every piece of content must:

- **Say something specific.** If you can swap in any company name and the text still works, it's too generic. Ground claims in the user's actual context.
- **Earn its length.** Every paragraph must carry weight. If a section can be cut without losing meaning, cut it.
- **Sound like a person wrote it.** Vary sentence length. Use contractions where natural. Allow personality. Avoid the flat, even cadence that signals machine generation.
- **Respect the reader's time.** Front-load the value. Don't bury the point under three paragraphs of setup.
- **Match platform norms.** A Twitter thread reads differently from a blog post reads differently from a HN comment. Each sub-skill knows its platform. Trust the routing.
- **Prefer concrete over abstract.** Numbers over adjectives. Examples over assertions. Evidence over claims.

### Self-Check

Before delivering any content, verify:

1. Could a reader identify whose brand this is without seeing a byline? (Brand alignment)
2. Would you actually read this if it showed up in your feed? (Interest test)
3. Does every sentence pull its weight? (Density test)
4. Is there a single clear takeaway? (Focus test)

---

## Compound Workflows

Some subcommands trigger multi-step workflows that chain sub-skills together.

### `/content series`

This is the most complex compound workflow. It executes in three phases:

1. **Strategy phase** — Invoke `skills/content-strategy/SKILL.md` to define the series: theme, number of installments, angle per installment, target audience, success metrics.

2. **Creation phase** — Invoke `skills/content-blog/SKILL.md` for each installment. Pass the series plan as context so each post maintains narrative continuity.

3. **Repurpose phase** — Invoke `skills/content-repurpose/SKILL.md` for each completed post. Generate platform variants based on the user's channel preferences.

Between phases, present the output to the user for review. Do not auto-proceed to the next phase without confirmation.

### Custom Compound Workflows

Users can chain subcommands manually:

```
/content brief "Why static types matter"
/content blog          # uses the brief from the previous step
/content repurpose     # adapts the blog post for other platforms
```

Maintain context between sequential invocations within the same session. Each sub-skill should check for recent output from related sub-skills and use it as input when relevant.

---

## Parallel Workflows with Agents

The `agents/` directory holds agent definitions for workflows that benefit from parallel execution. Use agents when a task naturally splits into independent work streams.

### When to Use Agents

- **Repurposing** — `/content repurpose` can spawn one agent per target platform. A blog post gets adapted to Twitter, LinkedIn, Reddit, and HN simultaneously rather than sequentially.
- **Series creation** — After the strategy phase of `/content series`, individual installments can be drafted in parallel if they don't depend on each other.
- **Audit** — `/content audit` across multiple pieces can score each piece in its own agent.
- **Calendar generation** — When populating a calendar with content for multiple channels, each channel's content plan can be developed in parallel.

### How to Use Agents

1. Define the task clearly before spawning. Each agent gets a specific brief: what to produce, what brand context to apply, what platform constraints to follow.
2. Pass brand context to every agent. Each agent must independently read from `brand/` — do not assume shared state between agents.
3. Collect and reconcile output. After agents complete, review their output for consistency. Flag any conflicts in tone, messaging, or facts.
4. Present unified results. The user should see a cohesive set of deliverables, not disconnected fragments.

### Agent Constraints

- Never spawn more agents than there are genuinely independent work streams.
- Each agent must apply the full Brand Integration Protocol independently.
- Each agent must apply the Anti-Slop Commitment independently.
- If an agent's output conflicts with another agent's output, flag the discrepancy for the user rather than silently picking one.

---

## Error Handling

### Unknown Subcommand

If the subcommand does not match any entry in the routing table:

```
Unknown subcommand: "<input>"

Available subcommands:
  setup, brand show, brand update, voice, strategy, plan, brief,
  blog, twitter, linkedin, reddit, hn, presentation, infographic,
  image, video, calendar, repurpose, audit, score, series

Run /content <subcommand> to get started.
```

### Missing Sub-Skill File

If a routing target file does not exist:

```
The sub-skill file at <path> is missing.
This sub-skill may not be installed yet. Check the skill pack structure.
```

### Empty Subcommand

If the user runs `/content` with no arguments, display:

```
Content Studio — available commands:

  Brand & Setup
    setup          Initialize your brand profile
    brand show     View current brand config
    brand update   Modify brand attributes
    voice          Profile your writing voice from samples

  Strategy & Planning
    strategy       Develop a content strategy
    plan           Create a time-bound content plan
    brief          Write a content brief for one piece

  Content Creation
    blog           Write a blog post
    twitter        Create X/Twitter content
    linkedin       Write LinkedIn posts
    reddit         Draft Reddit content
    hn             Write for Hacker News
    presentation   Build a slide deck
    infographic    Design an infographic
    image          Generate image prompts
    video          Write a video script

  Management
    calendar       Manage editorial calendar
    repurpose      Adapt content across platforms
    audit / score  Score content quality
    series         Plan + write + repurpose a content series
```
