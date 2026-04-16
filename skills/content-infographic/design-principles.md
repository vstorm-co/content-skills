# Infographic Design Principles

Core principles for creating effective, accessible, and brand-aligned infographics.

---

## Data-Ink Ratio

Coined by Edward Tufte: maximize the share of ink used to present data, minimize everything else.

### Remove

- Decorative borders, shadows, and bevels
- 3D effects on charts (they distort data perception)
- Background textures and patterns (unless encoding information)
- Heavy gridlines (use light gray, or remove entirely if axis labels suffice)
- Redundant labels (if the bar shows "47%" above it, you do not also need it on the y-axis)
- Chart legends when direct labeling is possible (put the label next to the data, not in a separate box)

### Keep

- Axis labels (minimal, readable)
- Data point annotations (values displayed on or near the data)
- Source attribution (small, at the bottom)
- Title that states the insight

### Test

For every visual element, ask: "If I remove this, does the viewer lose information?" If the answer is no, remove it.

---

## Color Usage

### Color Encodes Information

Color should mean something. Common mappings:

| Color Role | Usage |
|---|---|
| Brand accent | The most important data point, the key insight, the hero number |
| Brand secondary | Supporting data, secondary series |
| Positive (green-ish) | Growth, success, improvement, above target |
| Negative (red-ish) | Decline, failure, risk, below target |
| Neutral (gray) | Context, baselines, non-emphasized data |

### Maximum Palette

Use no more than 5-6 distinct colors in a single infographic. If you need more categories, group smaller ones into "Other" or use a sequential palette (light-to-dark of one hue).

### Deriving Colors from Brand

When you need more colors than the brand palette provides:

1. Take the brand primary color.
2. Generate lighter variants (add white): 80%, 60%, 40%, 20% opacity.
3. Generate a complementary or analogous color using the brand secondary as a base.
4. Use gray for everything that does not need color emphasis.

### Never

- Use color as the only way to distinguish data series (accessibility failure).
- Use rainbow palettes (visually chaotic, no natural ordering).
- Use red and green as the only differentiators (red-green colorblindness affects ~8% of men).

---

## Colorblind-Safe Palettes

### Recommended Palettes

**Categorical (distinct items)**:
- Blue (#4E79A7), Orange (#F28E2B), Red (#E15759), Teal (#76B7B2), Green (#59A14F), Yellow (#EDC948)
- Source: Tableau 10, optimized for colorblind accessibility.

**Sequential (low to high)**:
- Light to dark of one hue: #EFF3FF, #BDD7E7, #6BAED6, #3182BD, #08519C
- Works for heat maps, choropleth maps, and intensity scales.

**Diverging (below/above center)**:
- Orange to Blue: #B2182B, #EF8A62, #FDDBC7, #F7F7F7, #D1E5F0, #67A9CF, #2166AC
- Works for sentiment, deviation from average, temperature.

### Always Pair Color with Another Channel

- Color + pattern (hatching, dots)
- Color + shape (circle vs. square data points)
- Color + label (direct annotation)
- Color + position (already encoded in bar height/line position)

---

## Typography Hierarchy

### Three Levels Only

| Level | Size | Weight | Color | Use |
|---|---|---|---|---|
| Title | 24-32px | Bold (700) | Brand secondary or dark | States the key insight |
| Label | 14-18px | Regular (400) or Semi-bold (600) | Dark gray | Axis labels, category names, data annotations |
| Caption | 10-13px | Regular (400) | Medium gray | Source, footnotes, methodology notes |

### Rules

- One font family for the entire infographic (use the brand font).
- Never use more than two font weights (regular + bold).
- Left-align text by default. Center-align only for titles and single-line labels.
- Minimum font size: 10px for web, 8pt for print. Below this, text becomes unreadable.
- Line length: maximum 50-60 characters for descriptive text. Infographics should not have paragraphs.

---

## Whitespace

Whitespace (negative space) serves three functions:

### 1. Separation

Space between sections creates visual grouping. Items close together appear related (Gestalt proximity). Use consistent spacing:
- Between major sections: 40-60px
- Between related items: 15-25px
- Between a label and its data point: 5-10px

### 2. Emphasis

Surrounding a key element with generous whitespace makes it stand out. A big number with padding commands attention.

### 3. Breathing Room

Dense infographics feel overwhelming. If the infographic feels "busy," add whitespace before adding more content.

### Margin Guide

For a 1200x800 SVG:
- Top margin (above title): 30-50px
- Side margins: 50-80px
- Bottom margin (below source): 30-50px
- Internal padding: 20-40px around content blocks

---

## Grid Alignment

### Invisible Grid

Establish a grid before placing elements. Common grids for a 1200x800 infographic:

- **12-column grid**: Each column ~83px wide. Use for complex layouts with multiple columns.
- **4-column grid**: Each column ~250px wide (accounting for margins and gutters). Use for simple layouts.

### Alignment Rules

- All left edges of text and elements should snap to grid lines.
- All elements at the same hierarchy level should be the same size.
- Spacing between repeated elements (e.g., stat cards in a row) should be uniform.
- Center the overall composition in the viewBox.

### Test

Squint at the infographic. If elements look slightly off, they probably are. Align them.

---

## Accessibility

### Text Alternatives

Every SVG infographic needs:
- `<title>` element: short name of the infographic.
- `<desc>` element: plain-text summary of the data and key insight. A screen reader user should get the same information from the description that a sighted user gets from the visual.
- `role="img"` on the root `<svg>` element.

### Contrast

- Body text: minimum 4.5:1 contrast ratio against background (WCAG AA).
- Large text (24px+ or 18px bold): minimum 3:1 contrast ratio.
- Chart elements: minimum 3:1 against adjacent elements and background.

Tools: use a contrast checker to verify. Common failures: light gray text on white, light accent colors on white.

### Do Not Rely on Color Alone

Every data distinction communicated through color must also be communicated through another channel (shape, pattern, position, or direct label).

### Text in SVG

- Use actual `<text>` elements, not rasterized text in images.
- Embed fonts or use web-safe fallbacks so text renders correctly everywhere.
- Set `lang` attribute on the SVG root for screen reader language detection.

---

## Chart-Specific Principles

### Bar Charts

- Y-axis starts at zero. Truncated axes exaggerate differences and mislead.
- Horizontal bars when labels are long (> 3 words).
- Sort bars by value (largest to smallest) unless the categories have a natural order (months, age groups).
- Space between bars: 40-60% of bar width.

### Line Charts

- Use lines for continuous data (time series, temperature). Not for categorical data.
- Limit to 3-4 lines per chart. More lines become spaghetti.
- Annotate key points directly on the line rather than relying on a legend.
- Use area fill (low opacity) to emphasize a single primary series.

### Pie / Donut Charts

- Maximum 5 segments. Group the rest into "Other."
- Start the largest segment at 12 o'clock, proceeding clockwise by size.
- Use a donut (hollow center) for a cleaner look and to display a total in the center.
- Label segments directly; avoid external legends connected by thin lines (they create visual clutter).

### Scatter Plots

- Label axes clearly with units.
- Use consistent point sizes unless size encodes a third variable.
- Add a trend line only if the relationship is meaningful and you explain it.

---

## Common Mistakes

1. **Chartjunk**: decorative elements that do not encode data. Remove them.
2. **Misleading scales**: truncated axes, inconsistent intervals, dual y-axes with different scales.
3. **Too many categories**: 15-bar charts and 10-segment pies are unreadable. Simplify.
4. **No clear takeaway**: the viewer finishes looking and does not know what they learned. The title should state the insight.
5. **Inconsistent style**: mixing rounded and sharp corners, different font sizes for same-level elements, inconsistent color usage.
6. **Poor mobile experience**: an infographic designed for desktop that becomes illegible on a phone. Test at 400px width.
