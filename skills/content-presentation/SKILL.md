---
name: content-presentation
description: Generate full HTML presentations using Slidev, Reveal.js, Spectacle, or raw HTML with brand integration. Use when user wants to create a presentation, slide deck, pitch deck, conference talk, workshop materials, keynote, sales deck, or client proposal slides. Even if user just says "slides" or "deck", use this skill.
---

# Content Presentation Skill

## Purpose

Generate complete, brand-aligned presentation decks in multiple frameworks. This skill handles everything from narrative structure to slide-by-slide code output with speaker notes.

---

## Framework Selection Guide

Choose the framework based on the use case. If the user has no preference, default based on context:

| Framework | Best For | Default When |
|---|---|---|
| **Slidev** | Developer talks, markdown-first workflows, Vue-based teams, heavy code content | The audience is technical, the content has code, or no preference stated |
| **Reveal.js** | Classic presentations, maximum browser compatibility, HTML/CSS/JS control | The user needs broad compatibility or prefers HTML-native authoring |
| **Spectacle** | React teams, custom interactive components, rich animations | The team uses React or needs interactive slide components |
| **Raw HTML** | Single portable file, no build step, email-embeddable, offline delivery | The user needs one file they can send or open anywhere |

See `frameworks/` for detailed guides on each:
- `frameworks/slidev.md` -- Markdown syntax, layouts, components, theming
- `frameworks/reveal-js.md` -- Setup, transitions, fragments, speaker notes, PDF export
- `frameworks/spectacle.md` -- React components, deck structure, themes, animations
- `frameworks/raw-html.md` -- Single-file structure, inline CSS, embedded fonts, responsive slides

---

## Generation Flow

Follow this sequence exactly. Do not skip steps.

### Step 1: Read Brand Context

Read these files if they exist:
- `brand/BRAND.md` -- identity, audience, differentiators
- `brand/VISUAL.md` -- colors, fonts, logo rules
- `brand/VOICE.md` -- tone, vocabulary, anti-patterns

If `brand/` is missing, ask the user for basic color, font, and tone preferences before proceeding. Do not generate a deck with default blue-and-white styling.

### Step 2: Clarifying Questions

Ask 3-5 targeted questions. Adapt based on what you already know:

1. **Length**: How many slides? (Offer a range based on type: pitch deck 10-15, conference talk 30-40, sales deck 12-18.)
2. **Audience**: Who is in the room? Technical depth, seniority, familiarity with the topic.
3. **Purpose**: What should the audience do after the last slide? (Buy, approve, learn, share, hire.)
4. **Data available**: Do you have specific stats, case studies, screenshots, or code to include?
5. **Delivery context**: Live talk, async read, recorded video, or print handout?

Do not ask all five if prior context answers some of them.

### Step 3: Recommend Framework

Based on answers, recommend a framework with a one-sentence rationale. Let the user override.

### Step 4: Generate Narrative Structure

Before writing any slide code, output a narrative outline:

```
Slide 1: [Title] -- Hook that establishes stakes
Slide 2: [The Problem] -- What the audience feels today
Slide 3: [Why It Matters] -- Cost of inaction
...
Slide N: [Close] -- Single clear CTA
```

Each entry: slide number, working title, one-line purpose. Include speaker note hints where the narrative arc shifts (tension, release, pivot).

### Step 5: User Approves Structure

Wait for explicit approval or revision requests. Do not proceed to code until the user says the structure is right.

### Step 6: Generate Slide-by-Slide Content

For each slide, output:
- The slide content (title, body, visuals, code blocks)
- Speaker notes (what to say, timing cues, transition phrases)
- Design notes where relevant (use the chart here, animate this list)

Apply brand CSS custom properties from VISUAL.md throughout. See `brand-integration.md` for mapping rules.

### Step 7: Deliver Output

Output depends on framework:
- **Slidev**: `slides.md` + `style.css` + `package.json` with setup instructions
- **Reveal.js**: `index.html` + `css/theme.css` or single HTML file
- **Spectacle**: React project files with component structure
- **Raw HTML**: Single `.html` file with everything inlined

---

## Narrative Arc

Every presentation follows this backbone. See `presentation-narrative.md` for deep guidance.

**Hook** -- Open with a statement, question, or stat that creates tension. Never open with "Hi, I'm..."

**Problem** -- Define the pain the audience already feels. Be specific. Use their language.

**Solution** -- Present your answer. Show, don't tell. Demo > description.

**Evidence** -- Back it up. Data, case studies, testimonials, live proof.

**CTA** -- One clear action. Not three. One.

The arc is not rigid. Conference talks may loop Problem-Solution-Evidence multiple times. Sales decks front-load the CTA as a preview. Workshop decks interleave teaching and exercises. Adapt the arc to the format.

---

## One Idea Per Slide

This is non-negotiable. If a slide has two ideas, split it into two slides. Slides are cheap. Audience confusion is expensive.

Test: can you describe the slide's purpose in one sentence without using "and"? If not, split it.

---

## Speaker Notes as First-Class Content

Speaker notes are not an afterthought. For every slide, write notes that include:
- What to say (key talking points, not a script)
- Timing guidance ("spend 60 seconds here", "this is your 10-minute mark")
- Transition phrase to the next slide
- Audience interaction cues ("pause for questions", "ask for a show of hands")

---

## Anti-Slop Rules for Slides

These patterns are banned. If you catch yourself generating them, stop and redesign.

| Banned Pattern | Why | Replace With |
|---|---|---|
| "Let's dive in!" as a title | Filler. Says nothing. | A specific hook: a stat, a question, a bold claim. |
| "Agenda" slide | Audiences do not care about your outline. | Jump straight to the hook. If you must orient, use a single visual timeline. |
| Bullet-pocalypse (5+ bullets) | Slides are not documents. Reading bullets kills engagement. | Split into multiple slides, use visuals, or restructure as a comparison. |
| Stock photo defaults | Generic handshake photos destroy credibility. | Use diagrams, data, screenshots, or no image at all. |
| "Questions?" as the last slide | Weak ending. The CTA should be last. | End with CTA. Add "Q&A" as a verbal transition, not a slide. |
| "Thank you" slide | Wastes the final impression. | Repeat the CTA or leave your contact info integrated into the close. |
| Wall of text | If they wanted to read, they would read a document. | Reduce to key phrase + speaker notes carry the detail. |
| Orphan slides | A slide with no clear connection to the one before or after it. | Add transitions in speaker notes; restructure the narrative. |

---

## Design Principles

- **Typography hierarchy**: Title (large, bold), subtitle (medium, regular weight), body (readable size). Never more than two font sizes on one slide.
- **Dark vs light**: Pick one mode per deck. Do not mix. Use brand VISUAL.md preference if specified.
- **Consistent rhythm**: Similar slide types should have similar layouts. A "stat card" slide should look the same every time it appears.
- **Charts over screenshots**: Never screenshot an Excel chart. Generate the chart in SVG or use the framework's charting tools.
- **Whitespace is a feature**: Empty space directs attention. Resist the urge to fill every pixel.
- **Color with purpose**: Use accent color for emphasis, not decoration. One accent per slide maximum.

---

## Slide Patterns

See `slide-patterns.md` for reusable patterns:
- Title slide
- Section divider
- Stat card
- Comparison (2-column)
- Code walkthrough
- Image + caption
- Quote
- Chart/data
- Team grid
- Timeline
- CTA/close

Each pattern includes layout guidance, what content belongs, and what does not.

---

## Brand Integration

See `brand-integration.md` for the full mapping from `brand/VISUAL.md` to presentation CSS.

Summary:
- Map brand primary color to `--slide-accent`
- Map brand fonts to `--slide-heading-font` and `--slide-body-font`
- Place logo on the title slide (centered or top-left) and in the footer of every subsequent slide (small, bottom-right)
- Use brand secondary colors for chart palettes and section dividers

---

## Templates

Pre-built narrative structures for common deck types. See `templates/`:

| Template | Framework | Slides | Use Case |
|---|---|---|---|
| `pitch-deck.slidev.template` | Slidev | 10-15 | Investor pitch |
| `conference-talk.reveal.template` | Reveal.js | 30-40 | Technical conference talk |
| `client-proposal.html.template` | Raw HTML | 15-25 | Consulting proposal |
| `sales-deck.slidev.template` | Slidev | 12-18 | B2B sales |
| `workshop.spectacle.template` | Spectacle | Varies | Interactive workshop |

Templates are starting points, not constraints. Adapt slide count, order, and content to the specific need.

---

## Error Handling

- If the user provides no content (just "make me a deck"), push back. Ask what the deck is about, who it is for, and what it should achieve.
- If the brand/ directory is missing, offer to proceed with user-specified colors/fonts or to run content-setup first.
- If the user asks for a format the framework does not support (e.g., PDF from Slidev), explain the export path and provide instructions.
