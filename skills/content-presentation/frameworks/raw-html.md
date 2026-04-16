# Raw HTML Presentation Reference

## Overview

A single self-contained HTML file with no dependencies, no build step, and no framework. Open it in any browser, email it as an attachment, or embed it in a CMS. Best when portability is the top priority.

---

## Single-File Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Presentation Title</title>
  <style>
    /* All CSS goes here -- nothing external */
  </style>
</head>
<body>

  <div class="deck">
    <section class="slide" id="slide-1">
      <h1>Title Slide</h1>
      <p>Subtitle or tagline</p>
    </section>

    <section class="slide" id="slide-2">
      <h2>Second Slide</h2>
      <p>Content here</p>
    </section>
  </div>

  <nav class="controls">
    <button onclick="prev()" aria-label="Previous slide">&larr;</button>
    <span class="slide-counter">1 / 2</span>
    <button onclick="next()" aria-label="Next slide">&rarr;</button>
  </nav>

  <script>
    /* All JavaScript goes here -- nothing external */
  </script>
</body>
</html>
```

Everything inlined. Zero external requests (except fonts if needed -- see below).

---

## Inline CSS

### Base Slide Styles

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --bg: #FFFFFF;
  --text: #1A1A2E;
  --accent: #E94560;
  --heading-font: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --body-font: 'Helvetica Neue', Helvetica, Arial, sans-serif;
  --slide-width: 1920px;
  --slide-height: 1080px;
}

html, body {
  height: 100%;
  background: #000;
  overflow: hidden;
}

.deck {
  position: relative;
  width: 100vw;
  height: 100vh;
}

.slide {
  position: absolute;
  top: 0; left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 5% 10%;
  background: var(--bg);
  color: var(--text);
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.4s ease;
}

.slide.active {
  opacity: 1;
  pointer-events: auto;
}

/* Typography */
h1 {
  font-family: var(--heading-font);
  font-size: clamp(36px, 5vw, 72px);
  font-weight: 700;
  margin-bottom: 0.5em;
  text-align: center;
}

h2 {
  font-family: var(--heading-font);
  font-size: clamp(28px, 3.5vw, 56px);
  font-weight: 600;
  margin-bottom: 0.5em;
}

p, li {
  font-family: var(--body-font);
  font-size: clamp(18px, 2vw, 32px);
  line-height: 1.5;
}

.accent { color: var(--accent); }

/* Controls */
.controls {
  position: fixed;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  align-items: center;
  gap: 1rem;
  z-index: 100;
}

.controls button {
  background: rgba(0,0,0,0.1);
  border: none;
  padding: 0.5rem 1rem;
  font-size: 1.5rem;
  cursor: pointer;
  border-radius: 4px;
}

.slide-counter {
  font-family: var(--body-font);
  font-size: 0.9rem;
  color: #666;
}
```

---

## Embedded Fonts

### Option 1: System Font Stack (No External Requests)

```css
--heading-font: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```

### Option 2: Base64-Encoded Font

Convert the font file to base64 and embed it:

```css
@font-face {
  font-family: 'BrandFont';
  src: url(data:font/woff2;base64,d09GMgABAAAAAA...) format('woff2');
  font-weight: 400;
  font-style: normal;
}
```

Generate base64 with: `base64 -i font.woff2 | tr -d '\n'`

### Option 3: Google Fonts Import (Requires Internet)

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
```

Only use this if the presentation will always be viewed online.

---

## Responsive Slides

The `clamp()` approach in the CSS above handles most cases. For full responsive scaling:

```css
.slide {
  /* Scale entire slide content proportionally */
  font-size: min(2vw, 2vh);
}

h1 { font-size: 3em; }
h2 { font-size: 2.2em; }
p  { font-size: 1.2em; }
```

This ensures the presentation looks correct at any window size.

---

## JavaScript Navigation

```javascript
(function() {
  const slides = document.querySelectorAll('.slide');
  const counter = document.querySelector('.slide-counter');
  let current = 0;

  function show(index) {
    slides.forEach(s => s.classList.remove('active'));
    current = Math.max(0, Math.min(index, slides.length - 1));
    slides[current].classList.add('active');
    if (counter) counter.textContent = `${current + 1} / ${slides.length}`;
  }

  window.next = () => show(current + 1);
  window.prev = () => show(current - 1);

  document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); next(); }
    if (e.key === 'ArrowLeft') { e.preventDefault(); prev(); }
    if (e.key === 'f') {
      document.documentElement.requestFullscreen?.();
    }
  });

  // Touch support
  let touchStartX = 0;
  document.addEventListener('touchstart', (e) => { touchStartX = e.touches[0].clientX; });
  document.addEventListener('touchend', (e) => {
    const diff = touchStartX - e.changedTouches[0].clientX;
    if (Math.abs(diff) > 50) { diff > 0 ? next() : prev(); }
  });

  // Hash navigation
  const hash = parseInt(location.hash.replace('#', ''));
  show(isNaN(hash) ? 0 : hash - 1);
  window.addEventListener('hashchange', () => {
    const h = parseInt(location.hash.replace('#', ''));
    if (!isNaN(h)) show(h - 1);
  });

  // Initialize
  show(0);
})();
```

---

## Print CSS

Add print styles so the file prints as a slide-per-page document:

```css
@media print {
  html, body { background: white; overflow: visible; }

  .deck { position: static; }

  .slide {
    position: relative;
    opacity: 1;
    pointer-events: auto;
    page-break-after: always;
    page-break-inside: avoid;
    width: 100%;
    height: 100vh;
    break-after: page;
  }

  .controls { display: none; }
}
```

Print to PDF: Cmd+P / Ctrl+P, select "Save as PDF", set to Landscape, margins None.

---

## Embedding Everything in One File

Checklist for a truly self-contained file:

1. **CSS**: All styles in `<style>` tags, no external stylesheets.
2. **JavaScript**: All scripts in `<script>` tags, no external scripts.
3. **Fonts**: Either use system fonts or base64-encode brand fonts.
4. **Images**: Base64-encode and use inline:
   ```html
   <img src="data:image/png;base64,iVBORw0KGgo..." alt="Description" />
   ```
5. **SVGs**: Inline directly in the HTML:
   ```html
   <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
     <circle cx="50" cy="50" r="40" fill="var(--accent)" />
   </svg>
   ```
6. **Logo**: Inline SVG in a footer element on each slide.

Convert images to base64: `base64 -i image.png | tr -d '\n'`

---

## Slide Patterns in Raw HTML

### Title Slide

```html
<section class="slide title-slide">
  <div class="logo"><!-- inline SVG logo --></div>
  <h1>Presentation Title</h1>
  <p class="subtitle">Subtitle or Tagline</p>
  <p class="meta">Author Name | Date</p>
</section>
```

### Stat Card

```html
<section class="slide">
  <div class="stat-card">
    <span class="stat-number">47%</span>
    <span class="stat-label">reduction in deploy time</span>
  </div>
</section>
```

### Two-Column

```html
<section class="slide">
  <h2>Comparison</h2>
  <div class="two-col">
    <div class="col">
      <h3>Before</h3>
      <p>Description of the old way</p>
    </div>
    <div class="col">
      <h3>After</h3>
      <p>Description of the new way</p>
    </div>
  </div>
</section>
```

With supporting CSS:

```css
.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; width: 100%; }
.stat-card { text-align: center; }
.stat-number { font-size: clamp(48px, 10vw, 120px); font-weight: 700; color: var(--accent); display: block; }
.stat-label { font-size: clamp(16px, 2vw, 28px); color: #666; }
```

---

## Key Shortcuts

| Key | Action |
|---|---|
| `Right` / `Space` | Next slide |
| `Left` | Previous slide |
| `F` | Fullscreen |
| `#N` in URL | Jump to slide N |
