# Spectacle Framework Reference

## Overview

Spectacle is a React-based presentation framework from Formidable. It exposes presentations as React component trees, making it ideal for React teams who want custom interactive components, complex animations, and programmatic slide generation.

---

## Setup

```bash
npx create-spectacle
# or manually:
npm install spectacle react react-dom
```

Basic structure:

```
project/
  src/
    index.jsx        # Entry point
    slides.jsx       # Slide components
    theme.js         # Custom theme
    components/      # Reusable slide components
  public/
    index.html
  package.json
```

---

## Deck Structure

```jsx
import { Deck, Slide, Heading, Text, FlexBox } from 'spectacle';
import theme from './theme';

function Presentation() {
  return (
    <Deck theme={theme}>
      <Slide>
        <Heading>First Slide</Heading>
        <Text>Content here</Text>
      </Slide>
      <Slide>
        <Heading>Second Slide</Heading>
      </Slide>
    </Deck>
  );
}
```

---

## Core Components

### Layout

```jsx
import { FlexBox, Grid, Box } from 'spectacle';

// Centered content
<FlexBox alignItems="center" justifyContent="center" height="100%">
  <Heading>Centered</Heading>
</FlexBox>

// Two columns
<Grid gridTemplateColumns="1fr 1fr" gridGap={40}>
  <Box>Left column</Box>
  <Box>Right column</Box>
</Grid>
```

### Typography

```jsx
import { Heading, Text, Quote, Link, OrderedList, UnorderedList, ListItem } from 'spectacle';

<Heading fontSize="h1">Main Title</Heading>
<Heading fontSize="h2">Subtitle</Heading>
<Text>Body text</Text>
<Quote>A blockquote with attribution</Quote>
<Link href="https://example.com">Click here</Link>

<UnorderedList>
  <ListItem>First point</ListItem>
  <ListItem>Second point</ListItem>
</UnorderedList>
```

### Images

```jsx
import { Image } from 'spectacle';

<Image src="/diagram.png" width="80%" />
```

### Notes

```jsx
import { Slide, Notes } from 'spectacle';

<Slide>
  <Heading>Visible Content</Heading>
  <Notes>
    Speaker notes here. Only visible in presenter mode.
    Press Alt+P to open presenter view.
  </Notes>
</Slide>
```

---

## Themes

### Custom Theme Object

```javascript
// theme.js
const theme = {
  colors: {
    primary: '#1A1A2E',       // Heading text
    secondary: '#E94560',     // Accent/links
    tertiary: '#FFFFFF',      // Background
    quaternary: '#16213E',    // Code background
    quinary: '#333333',       // Body text
  },
  fonts: {
    header: '"Your Brand Font", Helvetica, sans-serif',
    text: '"Your Brand Body Font", Helvetica, sans-serif',
    monospace: '"JetBrains Mono", monospace',
  },
  fontSizes: {
    h1: '72px',
    h2: '56px',
    h3: '40px',
    text: '28px',
    monospace: '20px',
  },
};

export default theme;
```

### Brand Integration

Map brand/VISUAL.md values:

| Brand Token | Theme Property |
|---|---|
| Primary color | `colors.secondary` (accent) |
| Background | `colors.tertiary` |
| Heading color | `colors.primary` |
| Body text color | `colors.quinary` |
| Heading font | `fonts.header` |
| Body font | `fonts.text` |

---

## Animations

### Appear (Fragment Equivalent)

```jsx
import { Appear } from 'spectacle';

<Slide>
  <Heading>Progressive Reveal</Heading>
  <Appear>
    <Text>First point appears</Text>
  </Appear>
  <Appear>
    <Text>Then this one</Text>
  </Appear>
  <Appear>
    <Text>Then this one</Text>
  </Appear>
</Slide>
```

### Stepper (Step-Through Animation)

```jsx
import { Stepper } from 'spectacle';

<Stepper values={['Step 1', 'Step 2', 'Step 3']}>
  {(value, step) => (
    <Text>Current: {value} (step {step})</Text>
  )}
</Stepper>
```

### Slide Transitions

```jsx
import { Slide, SlideTransition } from 'spectacle';

<Slide transition={{
  from: { opacity: 0, transform: 'translateX(100%)' },
  enter: { opacity: 1, transform: 'translateX(0)' },
  leave: { opacity: 0, transform: 'translateX(-100%)' },
}}>
  <Heading>Animated Slide</Heading>
</Slide>
```

---

## Code Highlighting

```jsx
import { CodePane } from 'spectacle';

<CodePane language="javascript" highlightRanges={[1, [3, 5], 7]}>
{`function process(data) {
  const validated = validate(data);
  
  const transformed = transform(validated);
  const result = format(transformed);
  
  return result;
}`}
</CodePane>
```

`highlightRanges` steps through: line 1, then lines 3-5, then line 7.

---

## Custom Components

Build reusable slide components for consistency:

```jsx
// components/StatCard.jsx
import { FlexBox, Heading, Text } from 'spectacle';

function StatCard({ number, label, color }) {
  return (
    <FlexBox flexDirection="column" alignItems="center">
      <Heading fontSize="120px" color={color || 'secondary'}>
        {number}
      </Heading>
      <Text fontSize="24px">{label}</Text>
    </FlexBox>
  );
}

// Usage in slides:
<Slide>
  <StatCard number="47%" label="reduction in deploy time" />
</Slide>
```

---

## Presenter Mode

Press `Alt + P` to open the presenter view in a new window, which shows:
- Current slide
- Next slide
- Speaker notes
- Timer

---

## Export

Spectacle does not have built-in PDF export. Options:

1. **decktape**: `npx decktape spectacle http://localhost:3000 output.pdf`
2. **Browser print**: Navigate to `?exportMode=true`, then Cmd+P with landscape and no margins.
3. **Screenshot automation**: Use Puppeteer to capture each slide as PNG.

---

## Key Commands

| Key | Action |
|---|---|
| `Right` / `Space` | Next slide/step |
| `Left` | Previous slide |
| `Alt + P` | Presenter mode |
| `Alt + O` | Overview mode |
| `Alt + F` | Fullscreen |
