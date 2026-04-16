# Slidev Framework Reference

## Overview

Slidev is a markdown-first, developer-oriented presentation framework built on Vue.js and Vite. Write slides in markdown, get a polished presentation with code highlighting, transitions, and hot-reload. Default choice for technical content.

---

## Setup

```bash
npm init slidev@latest
# or
npx slidev slides.md
```

Project structure:

```
project/
  slides.md          # Main slide content
  style.css          # Custom styles (optional)
  components/        # Vue components (optional)
  public/            # Static assets
  package.json
```

---

## Markdown Syntax

### Slide Separators

```markdown
# First Slide

Content here

---

# Second Slide

More content

---
```

Three dashes `---` separate slides. Each slide is an independent markdown section.

### Frontmatter (Per-Slide)

```markdown
---
layout: cover
background: /images/hero.jpg
class: text-center
---

# Presentation Title

Subtitle goes here
```

### Global Frontmatter (First Slide)

```markdown
---
theme: default
title: My Presentation
info: |
  Description of the presentation
class: text-center
highlighter: shiki
transition: slide-left
---
```

---

## Layouts

Built-in layouts:

| Layout | Use |
|---|---|
| `default` | Standard content slide |
| `cover` | Title/cover slide with centered content |
| `center` | Content centered vertically and horizontally |
| `intro` | Introduction slide |
| `two-cols` | Two-column layout |
| `image-right` | Content left, image right |
| `image-left` | Image left, content right |
| `image` | Full-screen image |
| `iframe-right` | Content left, iframe right |
| `fact` | Big statement/number |
| `statement` | Centered statement |
| `quote` | Blockquote styling |
| `section` | Section divider |
| `end` | Closing slide |
| `none` | No layout, raw content |

Usage:

```markdown
---
layout: two-cols
---

# Left Column

Content on the left side.

::right::

# Right Column

Content on the right side.
```

---

## Code Blocks

Slidev uses Shiki for syntax highlighting with line highlighting support:

````markdown
```typescript {2|4-5|all}
function process(data: Input): Output {
  const validated = validate(data);    // highlighted first
  
  const transformed = transform(validated);  // then these
  const result = format(transformed);        // two lines
  
  return result;
}
```
````

The `{2|4-5|all}` syntax steps through highlights: line 2 first, then lines 4-5, then all.

### Monaco Editor (Live Code)

```markdown
```ts {monaco}
// This becomes an interactive editor
const greeting = "Hello, world!";
console.log(greeting);
```
```

---

## Components

Use Vue components directly in markdown:

```markdown
<Counter :count="10" />

<Tweet id="1390115482657726468" />
```

Custom components go in the `components/` directory and are auto-imported.

---

## Transitions

Global (in frontmatter):

```markdown
---
transition: slide-left
---
```

Per-slide:

```markdown
---
transition: fade-out
---
```

Available transitions: `fade`, `fade-out`, `slide-left`, `slide-right`, `slide-up`, `slide-down`, `view-transition`.

---

## Speaker Notes

Add notes with HTML comments at the bottom of a slide:

```markdown
# My Slide Title

Visible content here.

<!--
Speaker notes go here.
These are only visible in presenter mode.
Press P to toggle presenter view.
-->
```

---

## Theming

### Built-in Themes

Install from npm:

```bash
npm install @slidev/theme-seriph
```

Use in frontmatter:

```markdown
---
theme: seriph
---
```

### Brand Integration via CSS

Create `style.css` in the project root:

```css
/* Import brand fonts */
@import url('https://fonts.googleapis.com/css2?family=YOUR_BRAND_FONT');

:root {
  /* Map brand colors */
  --slidev-theme-primary: #E94560;
  --slidev-theme-background: #FFFFFF;
  
  /* Typography */
  --slidev-font-family: 'Your Brand Font', sans-serif;
  --slidev-font-family-mono: 'JetBrains Mono', monospace;
}

/* Override heading styles */
.slidev-layout h1 {
  font-family: var(--slidev-font-family);
  color: var(--slidev-theme-primary);
  font-weight: 700;
}

.slidev-layout h2 {
  font-family: var(--slidev-font-family);
  color: #333333;
  font-weight: 600;
}

/* Brand logo in footer */
.slidev-layout::after {
  content: '';
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  width: 40px;
  height: 40px;
  background-image: url('/logo.svg');
  background-size: contain;
  background-repeat: no-repeat;
  opacity: 0.5;
}

/* Accent color for links and emphasis */
.slidev-layout a {
  color: var(--slidev-theme-primary);
}

.slidev-layout strong {
  color: var(--slidev-theme-primary);
}
```

Place logo file in `public/logo.svg`.

---

## Presenter Mode

Press `P` during the presentation to open presenter mode, which shows:
- Current slide
- Next slide preview
- Speaker notes
- Timer
- Slide navigation

---

## Exporting

```bash
# PDF
npx slidev export

# PDF with dark theme
npx slidev export --dark

# PNG (one per slide)
npx slidev export --format png

# SPA (deployable static site)
npx slidev build
```

---

## Key Commands

| Key | Action |
|---|---|
| `Space` / `Right` | Next slide/animation |
| `Left` | Previous slide |
| `P` | Presenter mode |
| `O` | Slide overview |
| `D` | Dark mode toggle |
| `F` | Fullscreen |
| `G` | Go to slide (type number) |
