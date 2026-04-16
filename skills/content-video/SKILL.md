---
name: content-video
description: Video script generation and Remotion composition scaffolding. Use when user wants to create video content, storyboards, Remotion scripts, social media shorts, explainer videos, or video scripts.
---

# Video Script & Remotion Composition Generation

## Before You Start

1. **Check for brand identity**: Read `brand/VOICE.md` and `brand/VISUAL.md` if they exist. Video content requires both voice (for narration/script tone) and visual identity (for colors, fonts, logo animations). If these files do not exist, use sensible defaults and suggest the user run the content-setup skill.

2. **Determine what the user needs**: This skill produces two possible outputs:
   - **Storyboard / Script only** -- a scene-by-scene document with narration, visual direction, and timing. Suitable for handing off to an editor or recording team.
   - **Storyboard + Remotion code** -- all of the above, plus a TSX composition that can be rendered programmatically using Remotion. Use this when the user wants a code-driven video.

3. **Determine the template type**: Ask the user (or infer from their prompt) which format fits:
   - **Social Short** (15-60 seconds) -- punchy, hook-first, vertical or square format (`templates/social-short.tsx.template`)
   - **Explainer** (2-5 minutes) -- structured walkthrough with sections, diagrams, code animations (`templates/explainer.tsx.template`)
   - **Data Story** -- animated charts, number reveals, data transitions (`templates/data-story.tsx.template`)
   - **Talking Head** -- person on camera with lower thirds, name cards, topic overlays (`templates/talking-head.tsx.template`)

4. **Gather inputs**: Topic, target audience, key message, desired duration, platform (YouTube, TikTok, LinkedIn, X, Instagram Reels), and any existing assets (images, logos, data).

---

## Generation Flow

Follow these stages. Do not skip any.

### Stage 1: Brief

Confirm the following with the user (or extract from their prompt):

- Topic and core message (one sentence)
- Target audience and platform
- Template type (social-short, explainer, data-story, talking-head)
- Desired duration
- Whether Remotion code is needed
- Available assets: logo files, brand colors, fonts, footage, data
- Narration style: voiceover, on-screen text only, or talking head
- Music mood: upbeat, calm, dramatic, corporate, playful, none

### Stage 2: Storyboard

Produce a scene-by-scene storyboard using the format defined in `storyboard-template.md`:

- Scene number and timestamp range
- Visual description (what the viewer sees)
- Narration or dialogue (exact script or key talking points)
- Motion notes (camera movement, transitions, animations)
- Audio cues (music changes, sound effects, silence)
- Duration per scene

Present the storyboard to the user for approval before writing Remotion code.

### Stage 3: Script Polish

Refine the narration/dialogue:

- Apply brand voice from `brand/VOICE.md`
- Ensure pacing matches the target duration (roughly 150 words per minute for narration)
- Vary sentence length for natural rhythm
- Write for the ear, not the eye -- short sentences, active voice, conversational flow
- Add emphasis markers where the speaker should stress a word
- Include pause indicators [PAUSE] where beats are needed

### Stage 4: Remotion Composition (if requested)

Generate the TSX composition using patterns from `remotion-patterns.md` and the appropriate template:

- Set up the `Composition` with correct `durationInFrames`, `fps`, `width`, `height`
- Use `useCurrentFrame()` and `useVideoConfig()` for animation timing
- Apply brand colors and fonts from `brand/VISUAL.md`
- Implement scene transitions using `<Series>` and `<Sequence>` components
- Add spring animations for natural motion
- Include text overlays, lower thirds, or data visualizations as specified in the storyboard
- Export all compositions from a single `Root.tsx`

### Stage 5: Review

Review the complete package against these criteria:

- Does the hook capture attention in the first 3 seconds?
- Is the pacing appropriate for the platform and duration?
- Does every scene serve the core message?
- Are transitions smooth and purposeful (not just decorative)?
- Does the visual style match the brand identity?
- Is the narration script natural when read aloud?
- Are audio cues specific enough for a producer to act on?

---

## Storyboard Format

Use the format defined in `storyboard-template.md` for all storyboards. Each scene must include:

| Field | Description |
|---|---|
| Scene # | Sequential number |
| Timestamp | Start and end time (e.g., 0:00-0:05) |
| Visual | What appears on screen -- composition, colors, motion |
| Narration | Exact words spoken or displayed as text |
| Motion | Camera movement, element animations, transitions |
| Audio | Music, sound effects, ambient sound, silence |
| Duration | Length in seconds |

---

## Remotion Integration

When generating Remotion code, follow these principles:

1. **One composition per video type**: Each template maps to a Remotion composition with its own props interface.
2. **Brand tokens as constants**: Extract colors, fonts, and spacing from `brand/VISUAL.md` into a shared `theme.ts` file.
3. **Scene-based architecture**: Each scene in the storyboard becomes a React component rendered inside a `<Sequence>`.
4. **Animation patterns**: Use spring animations for elements entering/exiting. Use `interpolate()` for continuous motion. See `remotion-patterns.md`.
5. **Responsive text**: Scale text based on `useVideoConfig()` dimensions so compositions work at multiple resolutions.
6. **Asset management**: Reference images and fonts via Remotion's `staticFile()` helper.

---

## Template Reference

| Template | Duration | Best For |
|---|---|---|
| `social-short.tsx.template` | 15-60s | TikTok, Reels, X clips, LinkedIn shorts |
| `explainer.tsx.template` | 2-5 min | Product walkthroughs, tutorials, feature launches |
| `data-story.tsx.template` | 30s-3 min | Metrics presentations, quarterly updates, data journalism |
| `talking-head.tsx.template` | 1-10 min | Interviews, commentary, thought leadership |

---

## Brand Integration

Video content must reflect the brand across both auditory and visual channels:

**Visual consistency** (from `brand/VISUAL.md`):
- Primary and secondary brand colors for backgrounds, text, accents
- Brand fonts for titles, body text, and lower thirds
- Logo animation: intro placement, watermark positioning, outro treatment
- Consistent padding, margins, and layout grid

**Voice consistency** (from `brand/VOICE.md`):
- Narration tone matches the brand personality
- Vocabulary choices align with brand guidelines
- Humor, formality, and energy level are on-brand

**Audio guidance**:
- Music mood should match the brand personality (e.g., a playful brand uses upbeat tracks)
- Sound effects should be subtle and purposeful, not gimmicky
- Voiceover pacing: 130-160 words per minute depending on energy level

---

## Output Checklist

Before delivering the final package, verify:

- [ ] Storyboard is complete with all scenes documented
- [ ] Narration script reads naturally when spoken aloud
- [ ] Total duration matches the requested range
- [ ] Hook captures attention within the first 3 seconds
- [ ] Brand colors, fonts, and logo are correctly applied (if Remotion)
- [ ] Remotion code compiles and renders without errors (if applicable)
- [ ] All compositions are exported from Root.tsx (if Remotion)
- [ ] Scene transitions are smooth and motivated
- [ ] Audio cues are specific and actionable
- [ ] Voice matches brand profile throughout the script
