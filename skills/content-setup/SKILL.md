---
name: content-setup
description: Interactive brand onboarding that creates the /brand/ directory with BRAND.md, VOICE.md, and VISUAL.md. Use when user runs /content setup, /content brand show, /content brand update, or /content voice. Also triggers when any content skill detects brand/ is missing.
---

# Content Setup Skill

## When This Skill Activates

This skill runs in three scenarios:

1. **Explicit invocation**: user runs `/content setup`, `/content brand show`, `/content brand update`, or `/content voice`.
2. **Missing brand detection**: any other content skill (e.g., `/content draft`, `/content social`) checks for the `brand/` directory and it does not exist. That skill should hand off here before proceeding.
3. **Voice recalibration**: user drops writing samples into `brand/voice-samples/` and runs `/content voice` to re-derive voice attributes.

---

## Command Routing

| Command | Behavior |
|---|---|
| `/content setup` | Full onboarding flow (all 5 phases) |
| `/content brand show` | Display current brand configuration from `brand/BRAND.md`, `brand/VOICE.md`, `brand/VISUAL.md` |
| `/content brand update` | Interactive modification of existing brand files |
| `/content voice` | Analyze writing samples in `brand/voice-samples/` and update `brand/VOICE.md` |

---

## The Onboarding Philosophy

This is a conversation, not a form. Claude should:

- Ask one question at a time (sometimes two if they are tightly related).
- Listen to the answer, then probe deeper when the response is vague or generic.
- Challenge cliches. If the user says "we empower people," ask what that looks like on a Tuesday afternoon.
- Reflect back what you heard before moving to the next phase, so the user can correct misunderstandings early.
- Keep a running internal summary; do not ask the user to repeat themselves.
- Be warm but direct. This process should feel like working with a sharp brand strategist, not filling out a government form.

**Never dump all questions at once.** The flow is adaptive -- skip questions whose answers are already obvious from prior responses. Add follow-ups when something interesting surfaces.

---

## Phase 1: Identity (5-7 questions)

Goal: Understand who this brand is at its core.

Key topics:
- Brand or company name
- What you actually do (product/service/mission)
- Who you serve (audience -- push for specifics)
- The elevator pitch (30 seconds or less)
- Competitors and how you differ from them
- The single biggest differentiator
- One-word brand essence

Probe hard on differentiators. "Better quality" is not a differentiator. "We hand-test every unit before shipping" is.

See `questions/brand-identity.md` for the full question script with follow-up probes.

See `questions/audience.md` for the detailed audience deep-dive.

---

## Phase 2: Voice (4-5 questions)

Goal: Capture how the brand sounds when it writes.

Key topics:
- Voices they admire (brands, writers, publications)
- Formality scale from 1 (SMS to a friend) to 10 (Supreme Court brief)
- Humor style (dry, playful, none, self-deprecating, absurdist)
- Favorite phrases and words they love to use
- Forbidden words and phrases (what should never appear)
- Writing samples (if available, analyze them)

If writing samples exist in `brand/voice-samples/`, analyze them for patterns: sentence length, vocabulary level, punctuation habits, rhetorical devices, tone shifts.

See `questions/voice-tone.md` for the full question script with the formality scale reference.

---

## Phase 3: Visual (4-5 questions)

Goal: Document the visual identity so content can reference it.

Key topics:
- Logo description and usage rules
- Primary and secondary color palette (hex values if known)
- Reference brands whose visual style they admire
- Typography preferences (serif vs sans-serif, specific fonts)
- Photography and illustration style (candid vs posed, illustrations vs photos, abstract vs literal)

Claude is not designing the brand -- just documenting what exists or what the user aspires to. If they have no visual identity yet, capture their preferences and inspirations.

See `questions/visual-style.md` for the full question script.

---

## Phase 4: Platforms (3-4 questions)

Goal: Know where the content lives and how often it ships.

Key topics:
- Current publishing platforms (blog, social, newsletter, podcast, etc.)
- Posting frequency goals per platform
- Content types per platform (long-form, short-form, threads, video scripts)
- Platforms they explicitly want to avoid and why

See `questions/platforms.md` for the full question script.

---

## Phase 5: Review

Goal: Confirm everything before generating files.

Process:
1. Present a structured summary of all captured information, organized by phase.
2. Ask: "What did I get wrong? What's missing?"
3. Iterate until the user confirms.
4. Generate the output files.

---

## Output Generation

After the user confirms the review, generate three files using the templates:

| File | Template | Purpose |
|---|---|---|
| `brand/BRAND.md` | `templates/BRAND.md.template` | Core identity, audience, platforms, content pillars |
| `brand/VOICE.md` | `templates/VOICE.md.template` | Voice attributes, example sentences, vocabulary, rhythm |
| `brand/VISUAL.md` | `templates/VISUAL.md.template` | Color palette, typography, logo rules, visual principles |

Create the `brand/` directory if it does not exist. If files already exist, confirm before overwriting.

See the `templates/` directory for the exact output format of each file.

---

## /content brand show

When the user runs `/content brand show`:

1. Check that `brand/BRAND.md`, `brand/VOICE.md`, and `brand/VISUAL.md` exist.
2. If any are missing, report which files are missing and offer to run setup.
3. If all exist, read each file and present a clean summary:
   - Brand identity in 2-3 sentences
   - Voice profile (key attributes, formality level)
   - Visual snapshot (primary colors, typography)
   - Active platforms and frequency
4. End with: "Run `/content brand update` to modify any of this."

---

## /content brand update

When the user runs `/content brand update`:

1. Read all existing brand files.
2. Ask: "What would you like to change?" Accept free-form input.
3. Map the requested changes to the relevant file(s).
4. Show a diff-style preview of what will change.
5. Confirm before writing.
6. Update only the affected sections, preserving everything else.

This is not a full re-onboarding. It is a surgical edit. If the user wants to start over, they should run `/content setup` again.

---

## /content voice

When the user runs `/content voice`:

1. Check for `brand/voice-samples/` directory.
2. If it does not exist, create it and ask the user to drop 3-5 writing samples there (blog posts, emails, social posts -- anything representative).
3. If samples exist, analyze them for:
   - Average sentence length and variation
   - Vocabulary complexity (Flesch-Kincaid or similar heuristic)
   - Punctuation patterns (em-dash heavy? Semicolons? Exclamation points?)
   - Rhetorical devices (questions, lists, metaphors, analogies)
   - Tone markers (formal/casual, confident/tentative, warm/distant)
   - Signature phrases or recurring patterns
4. Present findings to the user for confirmation.
5. Update `brand/VOICE.md` with the analysis, merging with any existing manual entries.

---

## Error Handling

- If the user abandons mid-flow, save progress to `brand/.setup-draft.json` so they can resume later.
- If brand files exist when `/content setup` is invoked, warn the user and ask whether to start fresh or update.
- If writing samples are too short (under 200 words total), warn that the voice analysis will be unreliable and ask for more material.

---

## Quality Bar

A completed brand setup must pass the validation checklist in `validation.md`. Key requirements:

- No placeholder text or "TBD" entries in final output
- Audience description includes at least: role, experience level, and primary pain point
- Voice section includes at least 3 "sounds like us" and 3 "doesn't sound like us" examples
- At least one publishing platform defined with a frequency goal
- Differentiator is specific and falsifiable (a competitor could not claim the same thing)
