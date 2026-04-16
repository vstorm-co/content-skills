# Reveal.js Framework Reference

## Overview

Reveal.js is a mature, feature-rich HTML presentation framework. It works in any modern browser with no build step required. Best for classic presentations where you want full HTML/CSS/JS control and maximum compatibility.

---

## Setup

### CDN (no install)

```html
<!doctype html>
<html>
<head>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/white.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">
      <section>Slide 1</section>
      <section>Slide 2</section>
    </div>
  </div>
  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
  <script>Reveal.initialize();</script>
</body>
</html>
```

### npm install

```bash
npm init -y
npm install reveal.js
```

Then reference from `node_modules/reveal.js/dist/`.

---

## Configuration

```javascript
Reveal.initialize({
  hash: true,               // Enable slide-specific URLs
  slideNumber: true,         // Show slide numbers
  transition: 'slide',       // none | fade | slide | convex | concave | zoom
  transitionSpeed: 'default', // default | fast | slow
  backgroundTransition: 'fade',
  center: true,              // Vertically center content
  controls: true,            // Navigation arrows
  progress: true,            // Progress bar
  autoSlide: 0,              // 0 = disabled, or ms between slides
  width: 1920,               // Presentation width
  height: 1080,              // Presentation height
  margin: 0.04,
});
```

---

## Transitions

Per-slide transitions override global setting:

```html
<section data-transition="zoom">
  <h2>This slide zooms in</h2>
</section>

<section data-transition="fade-in slide-out">
  <h2>Fade in, slide out</h2>
</section>
```

Available: `none`, `fade`, `slide`, `convex`, `concave`, `zoom`.

---

## Fragments

Animate elements within a slide:

```html
<section>
  <p class="fragment">Appears first</p>
  <p class="fragment">Appears second</p>
  <p class="fragment highlight-red">Turns red</p>
  <p class="fragment fade-out">Fades away</p>
</section>
```

Fragment styles: `fade-in`, `fade-out`, `fade-up`, `fade-down`, `fade-left`, `fade-right`, `highlight-red`, `highlight-green`, `highlight-blue`, `highlight-current-blue`, `grow`, `shrink`, `strike`, `semi-fade-out`.

Order control with `data-fragment-index`:

```html
<p class="fragment" data-fragment-index="2">Second</p>
<p class="fragment" data-fragment-index="1">First</p>
```

---

## Speaker Notes

```html
<section>
  <h2>Slide Title</h2>
  <p>Visible content</p>
  <aside class="notes">
    Speaker notes go here. Only visible in speaker view.
    Press S to open the speaker view window.
  </aside>
</section>
```

Open speaker view: press `S` during presentation.

---

## Code Highlighting

Requires the highlight plugin:

```html
<script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
<script>
Reveal.initialize({
  plugins: [RevealHighlight]
});
</script>
```

Usage:

```html
<section>
  <pre><code data-trim data-noescape data-line-numbers="1|3-4|6">
function greet(name) {
  // This is highlighted on step 1
  const message = `Hello, ${name}`;
  console.log(message);
  // Then these lines on step 2
  return message;
}
  </code></pre>
</section>
```

`data-line-numbers="1|3-4|6"` steps through highlighting: first line 1, then lines 3-4, then line 6.

---

## Theming

### Built-in themes

`black`, `white`, `league`, `beige`, `sky`, `night`, `serif`, `simple`, `solarized`, `blood`, `moon`, `dracula`.

### Custom theme (brand integration)

Create a custom CSS file that overrides Reveal variables:

```css
/* brand-theme.css */
@import url('https://fonts.googleapis.com/css2?family=YOUR_BRAND_FONT');

:root {
  --r-background-color: #FFFFFF;
  --r-main-font: 'Your Brand Font', sans-serif;
  --r-main-font-size: 42px;
  --r-main-color: #333333;
  --r-heading-font: 'Your Brand Heading Font', sans-serif;
  --r-heading-color: #1A1A2E;
  --r-heading-letter-spacing: -0.02em;
  --r-heading-text-transform: none;
  --r-link-color: #E94560;
  --r-link-color-hover: #C73E54;
  --r-selection-background-color: #E94560;
  --r-selection-color: #FFFFFF;
}

/* Brand accent for emphasis */
.reveal .accent { color: var(--r-link-color); }

/* Logo in footer */
.reveal .slide-footer {
  position: absolute;
  bottom: 1em;
  right: 1em;
  font-size: 0.5em;
  opacity: 0.6;
}
```

Load after the base theme:

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/white.css">
<link rel="stylesheet" href="brand-theme.css">
```

---

## Brand CSS Integration

Map brand/VISUAL.md values to Reveal.js CSS variables:

| Brand Token | Reveal Variable |
|---|---|
| Primary color | `--r-link-color`, `--r-selection-background-color` |
| Text color | `--r-main-color` |
| Background color | `--r-background-color` |
| Heading color | `--r-heading-color` |
| Heading font | `--r-heading-font` |
| Body font | `--r-main-font` |

---

## Backgrounds

```html
<section data-background-color="#1A1A2E">
  <h2 style="color: white;">Dark background slide</h2>
</section>

<section data-background-image="path/to/image.jpg" data-background-size="cover">
  <h2>Image background</h2>
</section>

<section data-background-gradient="linear-gradient(to bottom, #283048, #859398)">
  <h2>Gradient background</h2>
</section>
```

---

## Vertical Slides (Nested)

```html
<section>
  <section>Vertical slide 1 (top)</section>
  <section>Vertical slide 2 (scroll down)</section>
</section>
```

Use sparingly. Vertical slides confuse audiences who expect left-right navigation.

---

## Export to PDF

1. Open the presentation in Chrome.
2. Append `?print-pdf` to the URL: `http://localhost:8000/?print-pdf`
3. Open Chrome's print dialog (Cmd+P / Ctrl+P).
4. Set destination to "Save as PDF".
5. Set layout to "Landscape".
6. Set margins to "None".
7. Enable "Background graphics".
8. Save.

For automated export, use `decktape`:

```bash
npx decktape reveal http://localhost:8000 output.pdf
```

---

## Useful Keyboard Shortcuts

| Key | Action |
|---|---|
| `S` | Speaker view |
| `F` | Fullscreen |
| `O` / `Esc` | Slide overview |
| `B` / `.` | Black screen (pause) |
| `Alt + Click` | Zoom into element |
| `?` | Show keyboard shortcuts |
