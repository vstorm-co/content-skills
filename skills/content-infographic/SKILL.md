---
name: content-infographic
description: Generate SVG and HTML infographics with brand-aware design. Use when user wants to create an infographic, data visualization, process flow, comparison chart, stat card, or visual data summary.
---

# Content Infographic Skill

## Purpose

Generate production-ready SVG and HTML infographics that are brand-aligned, accessible, and optimized for web, print, and social media embedding. This skill produces visual assets, not presentations or documents.

---

## When This Skill Activates

- User asks for an infographic, data visualization, process diagram, comparison chart, or stat card.
- User has data they want to visualize.
- User needs a visual summary for a blog post, social media, report, or presentation.
- User says "visualize this" or "make this visual" about any data or process.

---

## SVG-First Approach

Always default to SVG output unless the user requests otherwise. SVG advantages:

- **Scalable**: Looks sharp at any size, from social media thumbnail to conference poster.
- **Embeddable**: Inline in HTML, embed in markdown, include in presentations.
- **Print-ready**: No pixelation at any DPI.
- **Editable**: Users can modify colors, text, and layout after generation.
- **Accessible**: Supports `<title>`, `<desc>`, and `aria-label` attributes for screen readers.
- **Small file size**: Vector graphics compress well.

When to use HTML instead of SVG:
- Interactive infographics with hover states, tooltips, or animations.
- Infographics that need responsive reflow at different screen sizes.
- Dashboards with live data bindings.

---

## Generation Flow

### Step 1: Read Brand Context

Read these files if they exist:
- `brand/VISUAL.md` -- colors, fonts, logo rules
- `brand/BRAND.md` -- identity, audience (affects visual tone)

Extract:
- Primary, secondary, and accent colors
- Font family (or use a clean sans-serif default)
- Logo mark SVG path (for embedding in the infographic)
- Visual style preferences (minimal, bold, playful, corporate)

If `brand/` is missing, ask for 2-3 colors and proceed with a clean default style.

### Step 2: Understand the Data

Before designing anything, understand what needs to be communicated:

- **What is the data?** Numbers, categories, processes, comparisons, timelines.
- **What is the key insight?** Every infographic has one main takeaway. Identify it.
- **Who is the audience?** Technical vs. general, internal vs. external.
- **Where will it live?** Blog post, social media, email, print, presentation slide.

Ask clarifying questions if the user provides raw data without context.

### Step 3: Choose Layout

Based on the data type and key insight, select the appropriate template type:

| Data Type | Template | When to Use |
|---|---|---|
| Quantitative comparison | `data-viz` | Bar charts, line charts, pie charts, metrics |
| Sequential steps | `process-flow` | Workflows, how-it-works, timelines, pipelines |
| Side-by-side evaluation | `comparison` | Versus, pros/cons, feature matrix, before/after |
| Single key metric | `stat-card` | Hero numbers, KPI highlights, social sharing |

See `templates/` for each template type.

### Step 4: Generate SVG

Build the SVG following these principles:
- Set a viewBox appropriate for the output context (1200x800 for blog embeds, 1080x1080 for social, custom for others).
- Use CSS custom properties for colors so the user can retheme easily.
- Embed brand fonts via `<style>` inside the SVG or use web-safe fallbacks.
- Include the brand logo mark in a corner (default: bottom-right, small, 50% opacity).
- Add accessibility: `<title>` for the infographic name, `<desc>` for a plain-text summary.

### Step 5: Validate

Before delivering, check:
- [ ] Key insight is immediately visible (the most important information is the largest/most prominent element).
- [ ] Color contrast passes WCAG AA for all text.
- [ ] No more than 5-6 colors total.
- [ ] Text is readable at the intended display size.
- [ ] Brand colors and fonts are applied correctly.
- [ ] Logo is present but not distracting.
- [ ] SVG is valid and renders in all major browsers.

---

## Design Principles

See `design-principles.md` for the full reference. Key rules:

### Data-Ink Ratio

Every visual element should encode data. Remove anything that does not:
- No decorative borders or shadows.
- No 3D effects on charts.
- No background textures or patterns unless they encode information.
- Gridlines should be light gray and minimal (or removed entirely if the axis labels are sufficient).

### Color with Meaning

- Use color to encode information, not for decoration.
- Primary brand color for the key data series or most important element.
- Secondary colors for supporting data.
- Neutral gray for context, labels, and axes.
- Never use color as the only differentiator -- pair with labels, patterns, or position for accessibility.

### Typography Hierarchy

Three levels maximum:
1. **Title**: Large, bold. States the key insight, not the chart type. "Revenue grew 47% in Q3" not "Revenue Chart."
2. **Labels**: Medium, regular weight. Axis labels, category names, data point annotations.
3. **Footnotes**: Small, light. Sources, methodology notes, date ranges.

### Whitespace

Whitespace is not empty space -- it is structure. Use it to:
- Separate sections of the infographic.
- Create visual breathing room around the key insight.
- Guide the eye from one element to the next.

### Grid Alignment

Align elements to an invisible grid. Misaligned elements create visual noise. In SVG, use consistent x/y coordinates and spacing values.

---

## Template Types

### Data Visualization (`templates/data-viz.svg.template`)

For quantitative data: bar charts, line charts, donut charts, area charts.

Key rules:
- Start bar chart y-axes at zero (truncated axes mislead).
- Use horizontal bar charts when category labels are long.
- Limit pie/donut charts to 5 segments. Use "Other" for the rest.
- Annotate data points directly on the chart when possible (reduces need for legends).

### Process Flow (`templates/process-flow.svg.template`)

For sequential information: workflows, how-it-works diagrams, timelines, pipelines.

Key rules:
- Flow left-to-right or top-to-bottom. Never right-to-left.
- Each step: icon or number + title + one-line description.
- Connect steps with arrows or lines.
- Use consistent spacing between steps.
- Highlight the current or most important step with the brand accent color.

### Comparison (`templates/comparison.svg.template`)

For side-by-side evaluation: versus layouts, feature matrices, pros/cons, before/after.

Key rules:
- Equal visual weight to both sides (unless the infographic is designed to favor one).
- Clear visual separator (vertical line, color difference, or whitespace).
- Consistent structure: same categories in the same order on both sides.
- Use icons or color coding to indicate positive/negative/neutral.

### Stat Card (`templates/stat-card.svg.template`)

For single key metrics: hero numbers, KPI highlights, social media sharing.

Key rules:
- The number is the largest element by far.
- Context below the number in smaller text.
- Optional: trend indicator (arrow up/down), comparison ("up from 32% last quarter").
- Keep the card focused: one stat, one context line, one optional trend indicator.

---

## Brand Logo Embedding

If `brand/logo/logo-mark.svg` exists, embed it in the infographic:

```svg
<g transform="translate(1120, 750)" opacity="0.5">
  <!-- Contents of logo-mark.svg pasted here -->
</g>
```

Placement: bottom-right corner by default. Adjust position based on layout.
Size: approximately 5-8% of the infographic width.
Opacity: 40-60% so it does not compete with the data.

---

## Output Formats

| Format | When to Use | How |
|---|---|---|
| `.svg` file | Web embed, presentation slide, further editing | Direct SVG output |
| Inline SVG in HTML | Blog post embed, email | SVG wrapped in `<div>` with responsive CSS |
| HTML + CSS | Interactive infographic | HTML structure with CSS styling and optional JS |

For social media, suggest the user render the SVG to PNG at 2x resolution using a tool like `svgexport` or a browser screenshot.

---

## Error Handling

- If the user provides no data, ask for it. Do not generate placeholder infographics with fake numbers.
- If the data has too many categories for the chosen format (e.g., 15 items in a pie chart), recommend a different format or suggest grouping.
- If brand/ is missing, proceed with a clean minimal style and note that running content-setup would improve consistency.
- If the data tells no clear story, push back: "What is the one thing you want the viewer to take away from this?"
