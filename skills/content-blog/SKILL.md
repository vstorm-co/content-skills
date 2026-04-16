---
name: content-blog
description: Long-form blog post generation with brand voice integration and anti-slop enforcement. Use when user wants to write a blog post, article, tutorial, case study, opinion piece, deep dive, or listicle.
---

# Blog Post Generation

## Before You Start

1. **Check for brand voice**: Read `brand/VOICE.md` if it exists. This file defines the brand's tone, vocabulary, formality level, and signature patterns. If it does not exist, use sensible defaults (clear, direct, conversational-professional) and suggest the user run the content-setup skill to configure their voice.

2. **Determine the post type**: Ask the user (or infer from their prompt) which format fits best:
   - **Tutorial** -- step-by-step how-to content (`templates/tutorial.md.template`)
   - **Opinion** -- thought-leadership or contrarian takes (`templates/opinion.md.template`)
   - **Case Study** -- results-driven narrative (`templates/case-study.md.template`)
   - **Listicle** -- list-format posts with substance (`templates/listicle.md.template`)
   - **Deep Dive** -- long-form technical analysis (`templates/deep-dive.md.template`)

3. **Gather inputs**: Title or topic, target audience, key points the user wants covered, desired word count range, any links or data to reference.

---

## Generation Flow

Follow these five stages. Do not skip any.

### Stage 1: Brief

Confirm the following with the user (or extract from their prompt):

- Topic and angle
- Target audience and their existing knowledge level
- Post type (tutorial, opinion, case-study, listicle, deep-dive)
- Key points or arguments to include
- Desired length (short: 800-1200 words, medium: 1200-2000 words, long: 2000-3500 words)
- CTA or desired reader action

### Stage 2: Outline

Produce a structured outline with:

- Working title (can be refined later)
- Hook concept (one sentence describing how the post opens)
- Section headings with 2-3 bullet points each describing what goes in that section
- Closing approach (CTA, insight, question, callback to opening)

Present the outline to the user for approval before drafting.

### Stage 3: Draft

Write the full post following the approved outline. Apply:

- The appropriate template from `templates/`
- Brand voice from `brand/VOICE.md` (see `voice-integration.md`)
- Anti-slop rules from `anti-slop.md`
- Concrete examples, data, and specifics over abstract claims

### Stage 4: Revision

Review the draft against these criteria:

- Does the hook earn the reader's attention in the first two sentences?
- Does every section deliver on what the outline promised?
- Are there specific examples, numbers, or evidence for every claim?
- Is the voice consistent with the brand profile?
- Run the anti-slop checklist -- flag and fix any violations
- Is the reading flow natural? (Vary paragraph length. Vary sentence length.)
- Does the close land with impact?

### Stage 5: Polish

Final pass:

- Tighten sentences. Cut filler words.
- Verify all links, code snippets, or data references are accurate
- Write the meta description (under 160 characters)
- Suggest 3-5 title alternatives ranked by clarity and click-worthiness
- Format for the target platform (headings, code blocks, images, etc.)

---

## Post Structure Principles

**Opening / Hook**
- Never open with "Let's dive in," "In today's fast-paced world," or any throat-clearing phrase.
- Start with a specific observation, a surprising fact, a short story, or a bold claim.
- The first paragraph must give the reader a reason to keep reading.

**Body**
- Use clear section headings that tell the reader what they will learn in each section.
- Lead with the most valuable content. Do not bury the insight.
- Alternate between explanation and example. Never go more than two paragraphs without a concrete illustration.
- Use code snippets, screenshots, data, or quotes where they add clarity.
- Vary paragraph length: mix 1-sentence paragraphs with 3-4 sentence paragraphs.

**Closing**
- Do not trail off. End with a strong final thought: a CTA, a provocative question, a callback to the opening, or a forward-looking insight.
- Never end with "In conclusion" or "To sum up."

---

## Anti-Slop Enforcement

Before delivering any draft, run it through the anti-slop checklist defined in `anti-slop.md`. Every violation must be fixed. The most common blog-post slop patterns:

- Generic openings and closings
- Every paragraph the same length (the "wall of text" problem)
- Vague claims with no supporting evidence
- Buzzwords used as substance substitutes ("leverage," "game-changer," "unlock")
- Filler phrases that add no meaning
- Passive voice where active voice would be stronger

See `anti-slop.md` for the full list and positive alternatives.

---

## Voice Integration

Apply the brand voice consistently throughout the post. See `voice-integration.md` for the full protocol. Key steps:

1. Read `brand/VOICE.md` and internalize the voice attributes
2. Match formality level, humor type, and sentence rhythm
3. Use the brand's preferred vocabulary and avoid its blacklisted terms
4. After drafting, read the post aloud mentally -- does it sound like the brand?
5. Check three random paragraphs against the voice profile

---

## Template Reference

Each template in `templates/` provides the structural skeleton for its post type. Use the template as a starting framework, not a rigid fill-in-the-blank form. Adapt section order and depth to fit the specific topic.

| Template | Best For |
|---|---|
| `tutorial.md.template` | How-to guides, walkthroughs, getting-started posts |
| `opinion.md.template` | Thought leadership, hot takes, industry commentary |
| `case-study.md.template` | Customer stories, project retrospectives, results showcases |
| `listicle.md.template` | "N things about X" posts, resource roundups, comparison lists |
| `deep-dive.md.template` | Technical explorations, architecture breakdowns, research summaries |

---

## Output Checklist

Before delivering the final post, verify:

- [ ] Hook is specific and compelling (not a cliche)
- [ ] Every claim has a concrete example, number, or citation
- [ ] Anti-slop checklist passes with zero violations
- [ ] Voice matches brand profile (or sensible defaults)
- [ ] Sections have clear headings
- [ ] Paragraph and sentence length vary naturally
- [ ] Closing is strong (CTA, insight, or callback)
- [ ] Meta description is under 160 characters
- [ ] Title alternatives are provided
- [ ] Word count is within the requested range
