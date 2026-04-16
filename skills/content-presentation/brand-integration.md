# Brand Integration for Presentations

How to map `brand/VISUAL.md`, `brand/VOICE.md`, and `brand/BRAND.md` into presentation styles.

---

## CSS Custom Properties Mapping

Read `brand/VISUAL.md` and extract the following values. Map them to CSS custom properties that all frameworks can consume.

### Color Mapping

| Brand Token | CSS Variable | Usage |
|---|---|---|
| Primary color | `--slide-accent` | Headings, links, emphasis, CTA buttons |
| Secondary color | `--slide-secondary` | Section dividers, chart secondary series, subtle accents |
| Background color | `--slide-bg` | Slide background |
| Text color | `--slide-text` | Body text |
| Heading color | `--slide-heading` | Heading text (often same as primary or a darker variant) |
| Neutral/gray | `--slide-muted` | Captions, footnotes, secondary text |

### Typography Mapping

| Brand Token | CSS Variable | Usage |
|---|---|---|
| Heading font | `--slide-heading-font` | All heading elements (h1-h3) |
| Body font | `--slide-body-font` | Paragraphs, lists, speaker notes |
| Monospace font | `--slide-mono-font` | Code blocks (default to JetBrains Mono or Fira Code if brand does not specify) |

### Example CSS Block

```css
:root {
  /* Colors from brand/VISUAL.md */
  --slide-accent: #E94560;
  --slide-secondary: #16213E;
  --slide-bg: #FFFFFF;
  --slide-text: #333333;
  --slide-heading: #1A1A2E;
  --slide-muted: #888888;

  /* Typography from brand/VISUAL.md */
  --slide-heading-font: 'Inter', -apple-system, sans-serif;
  --slide-body-font: 'Inter', -apple-system, sans-serif;
  --slide-mono-font: 'JetBrains Mono', 'Fira Code', monospace;
}
```

---

## Font Import

### Web Fonts (Google Fonts)

If the brand font is available on Google Fonts, import it at the top of the CSS:

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
```

### Local/Custom Fonts

If the brand provides font files in `brand/fonts/`, embed them:

```css
@font-face {
  font-family: 'BrandFont';
  src: url('./fonts/BrandFont-Regular.woff2') format('woff2');
  font-weight: 400;
}
@font-face {
  font-family: 'BrandFont';
  src: url('./fonts/BrandFont-Bold.woff2') format('woff2');
  font-weight: 700;
}
```

For raw HTML single-file presentations, base64-encode the font files.

### Fallback Stack

Always include a fallback stack in case the brand font fails to load:

```css
--slide-heading-font: 'BrandFont', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

---

## Logo Placement

### Title Slide

The logo appears prominently on the title slide. Placement options (choose based on layout):

- **Centered above title**: Works for cover layouts. Logo at 120-200px width.
- **Top-left corner**: Works for any layout. Logo at 80-120px width.

### Footer (All Other Slides)

The logo appears small in the footer of every slide after the title. Standard placement:

- **Position**: Bottom-right corner
- **Size**: 30-50px height
- **Opacity**: 50-70% (visible but not distracting)

### Implementation by Framework

**Slidev** (in `style.css`):
```css
.slidev-layout::after {
  content: '';
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  width: 40px;
  height: 40px;
  background: url('/logo.svg') no-repeat center / contain;
  opacity: 0.5;
}
```

**Reveal.js** (in HTML):
```html
<div class="slide-footer">
  <img src="logo.svg" alt="" height="30" />
</div>
```
With CSS:
```css
.slide-footer {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  opacity: 0.5;
  z-index: 10;
}
```

**Spectacle** (as a component):
```jsx
function SlideFooter() {
  return (
    <Box position="fixed" bottom="1rem" right="1rem" opacity={0.5}>
      <Image src="/logo.svg" height="30px" />
    </Box>
  );
}
```

**Raw HTML** (inline on each slide):
```html
<div class="logo-footer">
  <svg><!-- inline logo SVG --></svg>
</div>
```

---

## Color Usage in Slides

### Do

- Use the **primary/accent color** for: headings, links, key data in charts, CTA buttons, emphasis text.
- Use the **secondary color** for: section divider backgrounds, chart secondary series, borders.
- Use the **neutral/muted color** for: captions, footnotes, axis labels, non-essential text.
- Use **white or near-white** for: slide backgrounds in light mode, text on dark backgrounds.

### Do Not

- Use more than 3 colors on a single slide (accent + text + background is enough).
- Use the accent color for large background fills on most slides (reserve it for section dividers and special moments).
- Mix brand colors with unrelated colors. If you need more colors (for charts), derive them from the brand palette by adjusting lightness/saturation.

### Dark vs Light Mode

Read `brand/VISUAL.md` for a preferred mode. If not specified:

- **Default to light mode** for business presentations (pitch decks, proposals, sales decks).
- **Default to dark mode** for technical presentations (conference talks, workshops with code).

In dark mode, invert the mapping:
- `--slide-bg` becomes a dark color (brand secondary or #1A1A2E)
- `--slide-text` becomes white or light gray
- `--slide-accent` stays the same (accent colors should work on both backgrounds)

---

## Voice Integration

Read `brand/VOICE.md` to align slide copy with brand voice:

- **Formality level**: Adjust headline style. Formal brands: "Quarterly Performance Review." Casual brands: "How Q3 Actually Went."
- **Vocabulary**: Use brand-approved terms. Avoid forbidden words listed in VOICE.md.
- **Tone**: Match the energy. If the brand is "confident and direct," headlines should be assertive. If "warm and approachable," headlines can be more conversational.
- **Humor**: Only use humor if VOICE.md explicitly includes it. When in doubt, be clear over clever.

---

## Checklist Before Generating

Before outputting any slide code, verify:

- [ ] Brand primary color is mapped to `--slide-accent`
- [ ] Brand fonts are imported and applied to headings and body
- [ ] Logo is placed on title slide and in footer
- [ ] Slide copy matches VOICE.md formality and tone
- [ ] Color contrast passes WCAG AA (4.5:1 for body text, 3:1 for large text)
- [ ] Dark/light mode matches brand preference or context
- [ ] No off-brand colors are used without derivation from the brand palette
