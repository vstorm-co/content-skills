---
name: content-audit
description: Content quality audit with anti-slop detection and brand consistency scoring. Use when user wants to check content quality, audit a draft, score content, verify brand consistency, detect AI-generated patterns, or run a quality check before publishing.
---

# Content Quality Audit

## Overview

This skill audits content across three dimensions, each scored out of 100:

1. **Content Quality** -- Anti-slop score, readability, hook strength, structural variety
2. **Brand Voice Consistency** -- How well the content matches the voice profile in `brand/VOICE.md`
3. **Brand Visual Consistency** -- For visual content (presentations, videos, infographics), how well it matches `brand/VISUAL.md`

The composite score combines all applicable dimensions. For text-only content, the composite is based on dimensions 1 and 2. For visual content, all three dimensions contribute.

---

## Modes

### Quick Score (`/content score`)

Runs a fast assessment and returns:
- Composite score (out of 100)
- Top 3 issues to fix
- One-sentence summary

Use this for a quick pulse check on a draft.

### Full Audit (`/content audit`)

Runs a comprehensive review and returns:
- Detailed scores for each dimension with subscores
- Line-level feedback with specific callouts
- Forbidden phrase detection
- Readability metrics
- Concrete fix suggestions for every issue found
- Before/after examples for the most critical issues

Use this before publishing.

---

## Before You Start

1. **Load brand references**: Read `brand/VOICE.md` and `brand/VISUAL.md` if they exist. These define the scoring criteria for brand consistency. If they do not exist, score brand consistency against reasonable defaults and note that brand files should be created for more accurate scoring.

2. **Identify the content type**: Blog post, thread, LinkedIn post, newsletter, video script, slide deck, etc. Different content types have different quality expectations.

3. **Get the content**: The user should provide the draft text or a path to the file containing the content.

---

## Audit Flow

### Stage 1: Content Quality Audit

Run the content through these checks. Reference `slop-detector.md` for the full pattern list and `scoring.md` for the scoring rubric.

#### Anti-Slop Detection

Scan the content for AI-generated patterns grouped by severity:

**Critical** (major deductions):
- Opening cliches ("In today's fast-paced world," "Let's dive in," etc.)
- Closing cliches ("In conclusion," "To sum up," "At the end of the day")
- Buzzwords used as substance substitutes ("leverage," "unlock," "game-changer," "paradigm shift")
- Filler phrases that add no meaning ("It's worth noting that," "It goes without saying," "Needless to say")
- Em-dash abuse (more than 2 em-dashes per 500 words)

**Warning** (moderate deductions):
- Overused transitions ("Furthermore," "Moreover," "Additionally" appearing more than once)
- Generic metaphors ("Think of it as..." "It's like..." without a genuinely illuminating comparison)
- Vocabulary tells ("delve," "tapestry," "landscape," "myriad," "plethora")
- Structural tells (all paragraphs within 10% of the same length)

**Info** (minor deductions):
- Passive voice (acceptable at <15% of sentences, flagged above that)
- Predictable cadence (every sentence following the same rhythm)
- Missed opportunities for concrete examples

For each detection, report:
- The flagged text (exact quote with location)
- The severity level
- Why it is a problem
- A specific suggested fix

#### Readability Analysis

- **Sentence length variety**: Standard deviation of sentence lengths. Higher variety = better. Flag if >60% of sentences are within 5 words of the average.
- **Paragraph length variety**: Mix of short (1-2 sentences) and longer (3-5 sentences) paragraphs. Flag if all paragraphs are the same length.
- **Flesch-Kincaid Grade Level**: Report the grade level. For most content, aim for grades 8-12. Technical content can go higher, but flag anything above grade 16.
- **Average words per sentence**: Report the average. Flag if >25 (too dense) or <10 (too choppy).

#### Hook Strength

Evaluate the opening (first 2-3 sentences) on a 1-10 scale:

| Score | Criteria |
|---|---|
| 9-10 | Specific, surprising, creates genuine curiosity or tension. Reader must continue. |
| 7-8 | Good hook with a clear promise of value. Could be sharper but works. |
| 5-6 | Functional but generic. Gets to the topic but does not create urgency. |
| 3-4 | Weak. Generic opening, throat-clearing, or vague promise. |
| 1-2 | Cliche opener, "In this article we will explore...", or no hook at all. |

#### Structure Analysis

- Does the content have clear section headings (for long-form)?
- Is information logically ordered?
- Does the closing land with impact (CTA, insight, question, callback)?
- Are there concrete examples, data, or evidence for claims?

### Stage 2: Brand Voice Consistency

Reference `brand-consistency.md` for the full methodology.

Compare the content against `brand/VOICE.md` on these dimensions:

#### Voice Match

- **Formality level**: Does the content match the brand's formality (casual, conversational, professional, academic)?
- **Sentence patterns**: Does the sentence rhythm match? (Short and punchy? Long and flowing? Mixed?)
- **Vocabulary alignment**: Does the content use the brand's preferred vocabulary? Avoid its banned terms?
- **Personality markers**: Does the content reflect the brand's personality traits (witty, serious, provocative, warm, etc.)?
- **Humor style**: If the brand uses humor, is it the right kind? If the brand is serious, is inappropriate humor present?

#### Forbidden Phrase Detection

Check the content against the banned phrase list in `brand/VOICE.md`. Report every match with:
- The exact phrase found
- Its location in the content
- The suggested replacement from the banned list

#### Voice Score Components

| Component | Weight | Description |
|---|---|---|
| Formality match | 30% | Alignment with target formality level |
| Vocabulary alignment | 25% | Use of preferred terms, avoidance of banned terms |
| Sentence rhythm | 20% | Match with brand's sentence pattern profile |
| Personality consistency | 15% | Brand personality reflected throughout |
| Forbidden phrases | 10% | Penalty for each banned phrase found |

### Stage 3: Brand Visual Consistency (Visual Content Only)

For presentations, video compositions, infographics, or any content with visual elements. Reference `brand-consistency.md`.

Check against `brand/VISUAL.md`:

- **Color palette**: Are all colors used from the approved palette? Flag any off-brand colors with their hex values.
- **Typography**: Are the correct fonts used for headings, body, and mono text? Are font sizes consistent with the brand scale?
- **Logo usage**: Is the logo present where expected? Is it the correct version (light/dark, full/icon)? Does it have sufficient clear space?
- **Spacing and layout**: Does the layout follow the brand's grid and spacing system?
- **Image style**: Do images match the brand's visual style (photography style, illustration style, icon style)?

---

## Scoring

Reference `scoring.md` for the detailed rubric.

### Score Breakdown

```
CONTENT QUALITY AUDIT
=====================

Composite Score: [XX]/100

Dimension 1: Content Quality          [XX]/100
  - Anti-slop score:                   [XX]/100
  - Readability:                       [XX]/100
  - Hook strength:                     [XX]/100
  - Structure:                         [XX]/100

Dimension 2: Brand Voice Consistency   [XX]/100
  - Formality match:                   [XX]/100
  - Vocabulary alignment:              [XX]/100
  - Sentence rhythm:                   [XX]/100
  - Personality consistency:           [XX]/100
  - Forbidden phrases:                 [XX]/100

Dimension 3: Visual Consistency        [XX]/100  (if applicable)
  - Color palette:                     [XX]/100
  - Typography:                        [XX]/100
  - Logo usage:                        [XX]/100
  - Layout/spacing:                    [XX]/100

TOP ISSUES (ranked by impact)
-----------------------------
1. [Issue description with specific example and fix]
2. [Issue description with specific example and fix]
3. [Issue description with specific example and fix]
...
```

### Composite Score Calculation

For text-only content:
```
Composite = (Content Quality * 0.60) + (Voice Consistency * 0.40)
```

For visual content:
```
Composite = (Content Quality * 0.40) + (Voice Consistency * 0.30) + (Visual Consistency * 0.30)
```

### Score Interpretation

| Score | Rating | Action |
|---|---|---|
| 90-100 | Excellent | Ready to publish. Minor polish optional. |
| 80-89 | Good | Fix the top 1-2 issues, then publish. |
| 70-79 | Acceptable | Several issues need attention. Revise and re-audit. |
| 60-69 | Needs Work | Significant issues. Major revision required. |
| Below 60 | Poor | Rewrite recommended. Fundamental issues present. |

---

## Feedback Format

For each issue found, provide:

```
[SEVERITY: critical/warning/info]
Location: [Paragraph number, sentence, or line reference]
Issue: [What the problem is]
Flagged text: "[exact text from the content]"
Why: [Why this is a problem -- what effect it has on the reader]
Fix: [Specific rewrite or action to take]
```

For the most critical issues, provide before/after examples:

```
BEFORE: "In today's rapidly evolving digital landscape, it's worth noting
that leveraging AI can be a real game-changer for content creation."

AFTER: "AI cut our content production time from 8 hours to 2. Here's
exactly how we set it up."
```

---

## Output Checklist

Before delivering the audit, verify:

- [ ] All three applicable dimensions are scored
- [ ] Anti-slop detection has been run against the full pattern list
- [ ] Every flagged issue includes the exact text, location, reason, and fix
- [ ] Forbidden phrase detection has been run against `brand/VOICE.md` banned list
- [ ] Hook strength is evaluated on the 1-10 scale with rationale
- [ ] Readability metrics are reported (sentence length variety, Flesch-Kincaid, etc.)
- [ ] Before/after examples are provided for the top 3 most critical issues
- [ ] Composite score is calculated using the correct formula
- [ ] Score interpretation is provided with clear next steps
- [ ] Feedback is specific and actionable (not "improve the writing")
