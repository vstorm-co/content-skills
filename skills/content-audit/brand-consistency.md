# Brand Consistency Checking

How to evaluate content against brand guidelines for both voice and visual identity.

---

## Voice Consistency Check

### Source of Truth

The primary reference is `brand/VOICE.md`. If this file does not exist, evaluate against reasonable defaults (clear, direct, conversational-professional) and note in the audit that brand voice files should be created for more accurate scoring.

### Check 1: Formality Match

Compare the content's formality level against the brand's target:

| Level | Indicators |
|---|---|
| Casual | Contractions, slang, first person, humor, sentence fragments, exclamations |
| Conversational | Contractions, first/second person, accessible vocabulary, moderate sentence length |
| Professional | Fewer contractions, balanced first/third person, precise vocabulary, moderate formality |
| Formal | No contractions, third person, technical vocabulary, longer sentences, no humor |
| Academic | Third person, citations, passive voice acceptable, specialized terminology |

**Scoring**:
- If the brand targets "conversational" and the content reads as "formal," that is a significant miss (deduct 20-30 points from formality score).
- If the brand targets "professional" and the content reads as "conversational," that is a moderate miss (deduct 10-20 points).
- Minor formality shifts within adjacent levels are acceptable (deduct 0-5 points).

### Check 2: Vocabulary Alignment

Compare vocabulary usage against the brand's word lists:

**Preferred terms**: Words the brand actively uses. Check that the content uses these where appropriate.
- Score: Percentage of opportunities where the preferred term was used vs. a generic alternative.

**Banned terms**: Words the brand explicitly avoids. Check for any occurrences.
- Score: Start at 100, deduct 10 points for each banned term found.

**Jargon level**: Does the content match the brand's target jargon usage?
- Too much jargon for a brand targeting accessibility = deduction
- Too little jargon for a brand targeting experts = deduction

### Check 3: Sentence Rhythm

Analyze sentence patterns and compare to the brand profile:

- **Average sentence length**: Does it match the brand's typical range?
- **Sentence length variation**: Does it match the brand's pattern (consistently short? Deliberately varied? Long and flowing?)?
- **Rhetorical patterns**: Does the brand use questions? Lists? Fragments? Check for alignment.
- **Paragraph rhythm**: Does the paragraph length pattern match the brand?

**Scoring**:
- Calculate the delta between the content's sentence metrics and the brand's target metrics.
- Larger deltas = larger deductions.

### Check 4: Personality Consistency

Check for the brand's personality traits throughout the content:

| Trait | Positive Indicators | Negative Indicators |
|---|---|---|
| Witty | Clever observations, wordplay, unexpected comparisons | Forced jokes, cringe humor, sarcasm that does not land |
| Serious | Measured claims, evidence-based, authoritative tone | Dryness, monotone, reads like a textbook |
| Provocative | Bold claims, challenges assumptions, takes a stance | Alienating, offensive, contrarian for its own sake |
| Warm | Empathetic language, inclusive, encouraging | Saccharine, patronizing, toxic positivity |
| Direct | Short sentences, clear claims, no hedging | Blunt to the point of rudeness, missing context |
| Technical | Precise terminology, code examples, architectural detail | Inaccessible to the target audience, showing off |

**Scoring**:
- Check 3-5 random paragraphs for personality alignment.
- If the personality is consistent throughout: high score.
- If the personality shifts mid-piece (e.g., casual opening, formal middle): deduction.
- If the personality contradicts the brand profile: significant deduction.

### Check 5: Forbidden Phrase Scan

Run a literal string match for every phrase in the brand's banned list. For each match, report:

```
FORBIDDEN PHRASE DETECTED
Phrase: "[exact phrase]"
Location: [Paragraph X, sentence Y]
From banned list: [Yes -- listed in brand/VOICE.md under banned phrases]
Suggested replacement: [From the banned list's replacement suggestion, or generate one]
```

---

## Visual Consistency Check

### Source of Truth

The primary reference is `brand/VISUAL.md`. This check applies only to content with visual elements (presentations, video compositions, infographics, social media graphics).

### Check 1: Color Palette

For each color used in the content:

1. Extract the hex value (or RGB/HSL equivalent)
2. Compare against the approved palette in `brand/VISUAL.md`
3. Flag any color that is not in the palette

**Scoring**:
- All colors from the palette: 100
- One off-brand color: 80
- Two off-brand colors: 60
- Three or more off-brand colors: 40
- Completely off-brand color scheme: 20

Report each off-brand color with:
- The hex value found
- Where it appears (background, text, accent, etc.)
- The nearest approved color from the palette
- Suggested fix

### Check 2: Typography

Check all text elements against the brand's font specifications:

- **Heading font**: Is the correct font used for headings?
- **Body font**: Is the correct font used for body text?
- **Monospace font**: Is the correct font used for code?
- **Font sizes**: Do they follow the brand's type scale?
- **Font weights**: Are the correct weights used (bold for headings, regular for body, etc.)?
- **Line height**: Does it match the brand's specified line height?

**Scoring**:
- All typography matches: 100
- Wrong font family: -20 per instance
- Wrong font size: -10 per instance
- Wrong font weight: -5 per instance
- Wrong line height: -5 per instance

### Check 3: Logo Usage

If the content includes the brand logo:

- Is it the correct version (full color, monochrome, icon-only)?
- Is it positioned according to brand guidelines?
- Does it have sufficient clear space around it?
- Is it the correct minimum size?
- Is it distorted, stretched, or recolored?

**Scoring**:
- Logo correct and well-placed: 100
- Minor positioning issue: 80
- Wrong logo version: 60
- Logo distorted or incorrectly modified: 40
- Logo missing where expected: 20

### Check 4: Layout and Spacing

Check the overall layout against brand guidelines:

- Does the layout follow the brand's grid system?
- Is spacing consistent with the brand's spacing scale?
- Are margins and padding consistent?
- Is the visual hierarchy clear (headings larger than body, etc.)?
- Is there sufficient white space?

**Scoring**: Holistic assessment based on overall adherence to the layout system.

---

## Combining Scores

### Text-Only Content

```
Voice Consistency Score = (
  Formality match * 0.30 +
  Vocabulary alignment * 0.25 +
  Sentence rhythm * 0.20 +
  Personality consistency * 0.15 +
  Forbidden phrases * 0.10
)
```

### Visual Content

```
Visual Consistency Score = (
  Color palette * 0.35 +
  Typography * 0.30 +
  Logo usage * 0.20 +
  Layout/spacing * 0.15
)
```

### Composite

See `scoring.md` for the full composite calculation.
