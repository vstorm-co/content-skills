# Slide Patterns

Reusable slide layouts and content patterns. Each pattern describes what it is, when to use it, what content belongs, and what to avoid.

---

## Title Slide

**Purpose**: First impression. Establish the topic, speaker, and context.

**Content**:
- Presentation title (specific, not clever for its own sake)
- Speaker name and affiliation
- Date or event name
- Optional: subtitle or one-line description

**Design**: Centered. Large title. Minimal text. Brand logo either centered above the title or small in a corner. Background can be a solid brand color, a subtle gradient, or a brand image with text overlay.

**Avoid**: Bullet points, long descriptions, multiple logos, "Welcome to my presentation."

---

## Section Divider

**Purpose**: Signal a major topic shift. Give the audience a mental reset.

**Content**:
- Section title (2-5 words)
- Optional: section number ("Part 2")

**Design**: Full-bleed brand accent color or contrasting background. Large centered text. No body text. This slide should feel like a chapter heading in a book.

**Avoid**: Bullet points, descriptions of what the section covers (that is the next slide's job), busy backgrounds.

---

## Stat Card

**Purpose**: Make a single number the entire story.

**Content**:
- One big number (percentage, dollar amount, count)
- One line of context below the number
- Optional: source attribution in small text

**Design**: Number should be the largest element on the slide by a wide margin. Use brand accent color for the number. Context text is neutral gray. Centered layout.

**Avoid**: Multiple stats on one slide (if you have 3 stats, use 3 stat card slides in sequence). Charts or graphs -- this is about a single data point, not a trend.

**Example structure**:
```
         47%
  reduction in deploy time
  Source: Internal metrics, Q3 2025
```

---

## Comparison (2-Column)

**Purpose**: Show a before/after, pros/cons, old way/new way, or feature comparison.

**Content**:
- Left column: Option A with 3-5 points
- Right column: Option B with 3-5 points
- Optional: column headers

**Design**: Equal-width columns with a clear vertical divider (line or whitespace). Use color to signal which option you favor (brand accent on the preferred option, neutral gray on the other). Icons or simple graphics for each point.

**Avoid**: More than 5 points per column. Unequal number of points (pad with whitespace if needed). Feature comparison matrices with checkmarks -- those belong in documents, not slides.

---

## Code Walkthrough

**Purpose**: Explain code to the audience step by step.

**Content**:
- A descriptive title (what the code does, not the filename)
- Code block with syntax highlighting
- Line highlight stepping (show 2-4 lines at a time)

**Design**: Dark background for code slides works well (even in light-themed decks). Monospace font at readable size. Maximum 15 lines of code. If longer, split across multiple slides.

**Avoid**: Showing all code at once without highlights. Tiny font to fit more code. Code without a title explaining its purpose. Screenshots of code (use actual text with syntax highlighting).

---

## Image + Caption

**Purpose**: Show a screenshot, diagram, photo, or illustration with context.

**Content**:
- Image (takes up 60-70% of the slide)
- Caption or title (1-2 lines)
- Optional: annotations or callout arrows on the image

**Design**: Image should be high quality and relevant. If it is a screenshot, crop to show only the relevant portion. Caption below or to the side. Do not overlay text on busy images.

**Avoid**: Stock photos that add no information. Images used as decoration. Low-resolution or blurry images. Multiple images on one slide (use one per slide or create a grid for deliberate comparison).

---

## Quote

**Purpose**: Let someone else make your point for you. Social proof, expert authority, customer voice.

**Content**:
- The quote (2-3 sentences maximum)
- Attribution: name, title, company
- Optional: headshot or company logo

**Design**: Large quotation marks (typographic, not straight quotes). Quote text in a larger font than body text. Attribution in smaller text below. Centered or left-aligned with generous margins.

**Avoid**: Long quotes (if it is more than 3 sentences, edit it down). Unattributed quotes. Multiple quotes on one slide. Quotes from yourself.

---

## Chart / Data

**Purpose**: Show a trend, distribution, comparison, or relationship in data.

**Content**:
- One chart per slide
- A title that states the insight, not the chart type ("Deploy time dropped 47% after migration" not "Deploy Time Chart")
- Axis labels and a legend if needed
- Data source in small text

**Design**: Use brand color palette for chart colors. Primary color for the key data series, secondary/neutral for context series. Minimal gridlines. Clean axis labels.

**Chart selection**:
- **Bar chart**: Comparing categories
- **Line chart**: Showing change over time
- **Pie/donut chart**: Showing parts of a whole (use sparingly, max 5 segments)
- **Scatter plot**: Showing correlation between two variables

**Avoid**: 3D charts. Excessive gridlines. Dual y-axes (split into two slides). Excel screenshots. Chartjunk (unnecessary visual elements that do not encode data).

---

## Team Grid

**Purpose**: Introduce the team.

**Content per person**:
- Photo or avatar
- Name
- Title or role
- One-line credential (relevant to the presentation context)

**Design**: Grid layout (2x2 for 4 people, 3x2 for 6). Consistent photo treatment (all circular, all square, all same size). Name prominent, credential smaller.

**Avoid**: More than 6 people on one slide (split across slides). Long bios. Unrelated credentials. Mismatched photo styles.

---

## Timeline

**Purpose**: Show a sequence of events, milestones, or a project plan.

**Content**:
- 4-8 points on a horizontal or vertical line
- Each point: date/label and 1-line description
- Optional: current position indicator

**Design**: Horizontal timelines work best for few items (4-6). Vertical for more items. Use the brand accent color for the timeline line and dots. Alternate descriptions above and below the line for horizontal layouts.

**Avoid**: More than 8 items (summarize or split). Dense text at each point. Gantt chart complexity -- this is a high-level view.

---

## CTA / Close

**Purpose**: The final slide the audience sees. Drive action.

**Content**:
- One clear call to action (not three)
- Contact information or next-step URL
- Optional: your logo

**Design**: Bold, centered CTA text. Large enough to read from the back of the room. Contact info smaller below. Clean and uncluttered.

**Avoid**: "Thank you" as the primary content (gratitude is verbal, not a slide). "Questions?" as the final slide (handle Q&A verbally). Multiple CTAs. Dense contact information.

**Example structure**:
```
    Start your free trial today
        example.com/start

    [your-name] | [email] | [handle]
```
