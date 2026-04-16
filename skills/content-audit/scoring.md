# Scoring Rubric

Detailed scoring methodology for content audits. All scores are out of 100.

---

## Dimension 1: Content Quality

### Anti-Slop Score (25% of Content Quality)

Measures how free the content is from AI-generated patterns.

**Calculation**:
```
Start at 100 points.

For each detected pattern:
  Critical severity: -8 points (first occurrence), -5 points (subsequent)
  Warning severity: -3 points (first occurrence), -2 points (subsequent)
  Info severity:    -1 point (first occurrence), -0.5 points (subsequent)

Minimum score: 0
```

**Interpretation**:
| Score | Meaning |
|---|---|
| 95-100 | Virtually no AI patterns detected. Reads as authentically human. |
| 85-94 | Minor AI patterns present but not distracting. Quick fixes needed. |
| 70-84 | Noticeable AI patterns. Several fixes required before publishing. |
| 50-69 | Significant AI patterns throughout. Major revision needed. |
| Below 50 | Reads as unedited AI output. Rewrite recommended. |

---

### Readability Score (25% of Content Quality)

Measures how easy and enjoyable the content is to read.

**Components**:

#### Sentence Length Variety (40% of Readability)
```
Calculate standard deviation of sentence word counts.

StdDev >= 8:  Score 100 (excellent variety)
StdDev 6-7:   Score 85
StdDev 4-5:   Score 70
StdDev 2-3:   Score 50
StdDev 0-1:   Score 30 (monotonous)
```

#### Paragraph Length Variety (25% of Readability)
```
Count paragraphs. Measure sentence counts per paragraph.

Has mix of 1-sentence and 3-5 sentence paragraphs: Score 100
Some variety but no 1-sentence paragraphs:          Score 75
All paragraphs within 1 sentence of each other:     Score 50
All paragraphs exactly the same length:              Score 25
```

#### Flesch-Kincaid Grade Level (20% of Readability)
```
Target depends on content type:

Blog/newsletter (target: grade 8-12):
  Grade 8-10:  Score 100
  Grade 11-12: Score 90
  Grade 6-7:   Score 80 (too simple for most audiences)
  Grade 13-14: Score 70 (getting dense)
  Grade 15+:   Score 50 (too academic)
  Grade 5-:    Score 60 (oversimplified)

Technical content (target: grade 10-14):
  Grade 10-12: Score 100
  Grade 13-14: Score 90
  Grade 8-9:   Score 85
  Grade 15-16: Score 70
  Grade 17+:   Score 50
```

#### Average Words Per Sentence (15% of Readability)
```
Ideal range: 14-20 words per sentence.

14-20: Score 100
12-13 or 21-22: Score 85
10-11 or 23-25: Score 70
8-9 or 26-28:   Score 55
<8 or >28:       Score 40
```

**Readability Score** = (Sentence variety * 0.40) + (Paragraph variety * 0.25) + (Flesch-Kincaid * 0.20) + (Avg words/sentence * 0.15)

---

### Hook Strength (25% of Content Quality)

Evaluates the first 2-3 sentences of the content.

**Scoring criteria**:

| Score | Criteria | Examples |
|---|---|---|
| 95-100 | Specific, surprising, creates genuine tension. Uses a concrete number, story, or bold claim. Reader cannot stop. | "We deleted 40% of our codebase last Tuesday. Revenue went up." |
| 85-94 | Strong hook with clear promise of value. Specific but could be sharper. | "There are three things every new engineering manager gets wrong. I know because I got all three wrong." |
| 70-84 | Good enough. Gets to the topic clearly but does not create urgency or surprise. | "Rate limiting is more nuanced than most tutorials suggest. Here is what they miss." |
| 55-69 | Functional but generic. Could be the opening to thousands of articles. | "Rate limiting is an important topic for API developers. Let's look at the best approaches." |
| 40-54 | Weak. Generic opening, throat-clearing, or vague promise. | "APIs are everywhere these days. As developers, we need to think about rate limiting." |
| 20-39 | Cliche opener or "In this article" framing. | "In today's digital world, APIs have become essential. In this article, we will explore rate limiting." |
| 0-19 | No hook at all. Starts with a definition or background that does not engage. | "Rate limiting is defined as the practice of controlling the rate of requests a user can make to an API." |

---

### Structure Score (25% of Content Quality)

Evaluates the overall organization and structure.

**Components**:

#### Section Headings (30% of Structure)
```
Long-form content (>800 words):
  Clear, descriptive headings every 200-400 words: Score 100
  Headings present but vague ("Part 1", "Next"):   Score 60
  No headings in long-form content:                  Score 30

Short-form content (<800 words):
  Headings helpful but not required:                 Score 80-100
```

#### Logical Flow (30% of Structure)
```
Ideas build on each other naturally:                 Score 100
Mostly logical with 1-2 awkward transitions:         Score 75
Some sections feel out of order:                     Score 50
Disjointed, random ordering:                         Score 25
```

#### Evidence Density (20% of Structure)
```
Every claim has a specific example, number, or citation: Score 100
Most claims supported, 1-2 unsupported:                  Score 80
Mix of supported and unsupported claims:                  Score 60
Mostly unsupported assertions:                            Score 35
Pure opinion with no evidence:                            Score 20
```

#### Closing Strength (20% of Structure)
```
Strong close: CTA, callback, insight, or provocative question: Score 100
Adequate close: summarizes or states a clear takeaway:         Score 75
Weak close: trails off, generic conclusion:                     Score 45
Cliche close: "In conclusion...", "To sum up...":              Score 20
No close: content just stops:                                   Score 10
```

**Structure Score** = (Headings * 0.30) + (Flow * 0.30) + (Evidence * 0.20) + (Closing * 0.20)

---

### Content Quality Composite

```
Content Quality = (
  Anti-slop * 0.25 +
  Readability * 0.25 +
  Hook strength * 0.25 +
  Structure * 0.25
)
```

---

## Dimension 2: Brand Voice Consistency

See `brand-consistency.md` for detailed checking methodology.

```
Voice Consistency = (
  Formality match * 0.30 +
  Vocabulary alignment * 0.25 +
  Sentence rhythm * 0.20 +
  Personality consistency * 0.15 +
  Forbidden phrases * 0.10
)
```

If no `brand/VOICE.md` exists, evaluate against sensible defaults and cap the voice consistency score at 70 with a note that brand files would enable more accurate scoring.

---

## Dimension 3: Brand Visual Consistency

See `brand-consistency.md` for detailed checking methodology. Only applies to visual content.

```
Visual Consistency = (
  Color palette * 0.35 +
  Typography * 0.30 +
  Logo usage * 0.20 +
  Layout/spacing * 0.15
)
```

If no `brand/VISUAL.md` exists, skip this dimension and note that brand files would enable visual scoring.

---

## Overall Composite Score

### For Text-Only Content

```
Composite = (Content Quality * 0.60) + (Voice Consistency * 0.40)
```

### For Visual Content

```
Composite = (Content Quality * 0.40) + (Voice Consistency * 0.30) + (Visual Consistency * 0.30)
```

---

## Score Report Format

```
====================================
CONTENT AUDIT REPORT
====================================

Content: [Title or filename]
Type: [Blog post / Thread / LinkedIn post / etc.]
Word count: [N words]
Audit mode: [Quick score / Full audit]
Date: [YYYY-MM-DD]

------------------------------------
COMPOSITE SCORE: [XX]/100 -- [Rating]
------------------------------------

DIMENSION 1: Content Quality [XX]/100
  Anti-slop:     [XX]/100  ([N] issues found)
  Readability:   [XX]/100  (Grade level: [N], Avg sentence: [N] words)
  Hook strength: [XX]/100  ([1-10] / 10 rating)
  Structure:     [XX]/100

DIMENSION 2: Voice Consistency [XX]/100
  Formality:     [XX]/100
  Vocabulary:    [XX]/100  ([N] banned terms found)
  Rhythm:        [XX]/100
  Personality:   [XX]/100
  Forbidden:     [XX]/100  ([N] phrases found)

DIMENSION 3: Visual Consistency [XX]/100  (if applicable)
  Colors:        [XX]/100  ([N] off-brand colors)
  Typography:    [XX]/100
  Logo:          [XX]/100
  Layout:        [XX]/100

====================================
ISSUES ([N] total)
====================================

[Sorted by severity, then by position in the content]

1. [CRITICAL] [Location] -- [Issue description]
   Flagged: "[exact text]"
   Fix: [Specific suggestion]

2. [WARNING] [Location] -- [Issue description]
   Flagged: "[exact text]"
   Fix: [Specific suggestion]

...

====================================
TOP 3 FIXES (highest impact)
====================================

1. BEFORE: "[original text]"
   AFTER:  "[improved text]"
   Impact: +[N] points to [dimension]

2. BEFORE: "[original text]"
   AFTER:  "[improved text]"
   Impact: +[N] points to [dimension]

3. BEFORE: "[original text]"
   AFTER:  "[improved text]"
   Impact: +[N] points to [dimension]
```
