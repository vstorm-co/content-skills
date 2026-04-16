# Remotion Patterns Reference

Common patterns for building video compositions with Remotion. Use these as building blocks when generating Remotion code from storyboards.

---

## Project Setup

### Root Composition

```tsx
// src/Root.tsx
import { Composition } from "remotion";
import { SocialShort } from "./compositions/SocialShort";
import { Explainer } from "./compositions/Explainer";
import { DataStory } from "./compositions/DataStory";
import { TalkingHead } from "./compositions/TalkingHead";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="SocialShort"
        component={SocialShort}
        durationInFrames={30 * 30} // 30 seconds at 30fps
        fps={30}
        width={1080}
        height={1920} // 9:16 vertical
        defaultProps={{
          title: "Your Title Here",
          brandColor: "#6366F1",
        }}
      />
      <Composition
        id="Explainer"
        component={Explainer}
        durationInFrames={30 * 180} // 3 minutes
        fps={30}
        width={1920}
        height={1080} // 16:9 landscape
        defaultProps={{}}
      />
      {/* Add more compositions as needed */}
    </>
  );
};
```

---

## Core Hooks

### useCurrentFrame

Returns the current frame number. Use for all time-based animations.

```tsx
import { useCurrentFrame } from "remotion";

const MyComponent: React.FC = () => {
  const frame = useCurrentFrame();
  // frame starts at 0 within each <Sequence>
  const opacity = Math.min(1, frame / 15); // fade in over 15 frames
  return <div style={{ opacity }}>Hello</div>;
};
```

### useVideoConfig

Returns fps, width, height, and durationInFrames for the current composition.

```tsx
import { useVideoConfig } from "remotion";

const MyComponent: React.FC = () => {
  const { fps, width, height, durationInFrames } = useVideoConfig();
  const fontSize = width * 0.05; // responsive text
  return <h1 style={{ fontSize }}>Responsive Title</h1>;
};
```

---

## Animation Primitives

### interpolate

Maps a frame number to a value range. The workhorse of Remotion animation.

```tsx
import { interpolate, useCurrentFrame } from "remotion";

const frame = useCurrentFrame();

// Basic fade in over first 20 frames
const opacity = interpolate(frame, [0, 20], [0, 1], {
  extrapolateRight: "clamp",
});

// Slide in from bottom
const translateY = interpolate(frame, [0, 30], [100, 0], {
  extrapolateRight: "clamp",
});

// Scale with easing
const scale = interpolate(frame, [0, 25], [0.5, 1], {
  extrapolateRight: "clamp",
  easing: Easing.out(Easing.ease),
});
```

### spring

Creates natural, physics-based animations. Preferred over linear interpolation for UI elements.

```tsx
import { spring, useCurrentFrame, useVideoConfig } from "remotion";

const frame = useCurrentFrame();
const { fps } = useVideoConfig();

// Basic spring (returns 0 -> ~1)
const scale = spring({
  frame,
  fps,
  config: {
    damping: 12,
    stiffness: 200,
    mass: 0.5,
  },
});

// Delayed spring (starts at frame 15)
const delayedScale = spring({
  frame: frame - 15,
  fps,
  config: { damping: 10 },
});
```

### Spring Presets

Common spring configurations for different animation feels:

```tsx
// Snappy -- for UI elements, text reveals
const snappy = { damping: 12, stiffness: 200, mass: 0.5 };

// Bouncy -- for playful elements, logos
const bouncy = { damping: 8, stiffness: 150, mass: 0.8 };

// Gentle -- for backgrounds, slow reveals
const gentle = { damping: 20, stiffness: 80, mass: 1 };

// Heavy -- for large elements, dramatic reveals
const heavy = { damping: 15, stiffness: 100, mass: 2 };
```

---

## Composition Structure

### Sequence

Offsets a group of elements in time. Each child's `useCurrentFrame()` starts at 0.

```tsx
import { Sequence } from "remotion";

const MyVideo: React.FC = () => {
  return (
    <>
      {/* Scene 1: frames 0-89 (3 seconds at 30fps) */}
      <Sequence from={0} durationInFrames={90}>
        <Scene1 />
      </Sequence>

      {/* Scene 2: frames 90-209 */}
      <Sequence from={90} durationInFrames={120}>
        <Scene2 />
      </Sequence>

      {/* Overlapping element: appears during both scenes */}
      <Sequence from={60} durationInFrames={90}>
        <Watermark />
      </Sequence>
    </>
  );
};
```

### Series

Plays children back-to-back without manual frame math. Cleaner than chaining Sequences.

```tsx
import { Series } from "remotion";

const MyVideo: React.FC = () => {
  return (
    <Series>
      <Series.Sequence durationInFrames={90}>
        <Scene1 />
      </Series.Sequence>
      <Series.Sequence durationInFrames={120}>
        <Scene2 />
      </Series.Sequence>
      <Series.Sequence durationInFrames={60}>
        <Scene3 />
      </Series.Sequence>
    </Series>
  );
};
```

---

## Common Visual Patterns

### Text Reveal (Word by Word)

```tsx
const TextReveal: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const words = text.split(" ");

  return (
    <div style={{ display: "flex", flexWrap: "wrap", gap: 8 }}>
      {words.map((word, i) => {
        const delay = i * 5; // 5 frames between each word
        const s = spring({
          frame: frame - delay,
          fps,
          config: { damping: 12, stiffness: 200 },
        });
        return (
          <span
            key={i}
            style={{
              opacity: s,
              transform: `translateY(${(1 - s) * 20}px)`,
            }}
          >
            {word}
          </span>
        );
      })}
    </div>
  );
};
```

### Lower Third

```tsx
const LowerThird: React.FC<{
  name: string;
  title: string;
  brandColor: string;
}> = ({ name, title, brandColor }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const slideIn = spring({ frame, fps, config: { damping: 15 } });
  const barWidth = interpolate(slideIn, [0, 1], [0, 300]);

  return (
    <div style={{ position: "absolute", bottom: 80, left: 60 }}>
      <div
        style={{
          width: barWidth,
          height: 4,
          backgroundColor: brandColor,
          marginBottom: 8,
        }}
      />
      <div style={{ opacity: slideIn, transform: `translateX(${(1 - slideIn) * -30}px)` }}>
        <div style={{ fontSize: 32, fontWeight: 700, color: "#fff" }}>{name}</div>
        <div style={{ fontSize: 22, color: "#ccc" }}>{title}</div>
      </div>
    </div>
  );
};
```

### Number Counter

```tsx
const NumberCounter: React.FC<{
  from: number;
  to: number;
  duration: number;
}> = ({ from, to, duration }) => {
  const frame = useCurrentFrame();

  const progress = interpolate(frame, [0, duration], [0, 1], {
    extrapolateRight: "clamp",
    easing: Easing.out(Easing.cubic),
  });

  const value = Math.round(from + (to - from) * progress);

  return (
    <div style={{ fontSize: 80, fontWeight: 800, fontVariantNumeric: "tabular-nums" }}>
      {value.toLocaleString()}
    </div>
  );
};
```

### Crossfade Transition

```tsx
const Crossfade: React.FC<{
  children: [React.ReactNode, React.ReactNode];
  transitionStart: number;
  transitionDuration: number;
}> = ({ children, transitionStart, transitionDuration }) => {
  const frame = useCurrentFrame();

  const opacity = interpolate(
    frame,
    [transitionStart, transitionStart + transitionDuration],
    [0, 1],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
  );

  return (
    <>
      <div style={{ position: "absolute", inset: 0, opacity: 1 - opacity }}>
        {children[0]}
      </div>
      <div style={{ position: "absolute", inset: 0, opacity }}>
        {children[1]}
      </div>
    </>
  );
};
```

---

## Brand Theme Integration

Create a shared theme file that pulls from `brand/VISUAL.md`:

```tsx
// src/theme.ts
export const theme = {
  colors: {
    primary: "#6366F1",     // Replace with brand primary
    secondary: "#EC4899",   // Replace with brand secondary
    background: "#0A0A0A",
    surface: "#1A1A2E",
    text: "#FFFFFF",
    textMuted: "#A1A1AA",
  },
  fonts: {
    heading: "Inter",       // Replace with brand heading font
    body: "Inter",          // Replace with brand body font
    mono: "JetBrains Mono", // Replace with brand mono font
  },
  spacing: {
    xs: 8,
    sm: 16,
    md: 24,
    lg: 40,
    xl: 64,
  },
};
```

---

## Rendering Configuration

### CLI Rendering

```bash
# Preview in browser
npx remotion preview src/index.ts

# Render to MP4
npx remotion render src/index.ts SocialShort out/social-short.mp4

# Render specific frame range
npx remotion render src/index.ts SocialShort out/clip.mp4 --frames=0-90

# Render as GIF
npx remotion render src/index.ts SocialShort out/social.gif --codec=gif

# Render with custom props
npx remotion render src/index.ts SocialShort out/video.mp4 --props='{"title":"Custom Title"}'
```

### Render Settings

```tsx
// remotion.config.ts
import { Config } from "@remotion/cli/config";

Config.setVideoImageFormat("jpeg");
Config.setOverwriteOutput(true);
Config.setConcurrency(4);
```

---

## Performance Tips

1. **Avoid re-renders**: Memoize expensive components with `React.memo()`.
2. **Preload assets**: Use `prefetch()` for images and fonts that appear mid-video.
3. **Use `staticFile()`**: Reference assets in the `public/` folder via `staticFile("logo.png")`.
4. **Keep components pure**: Components should depend only on frame number and props. No side effects.
5. **Test at target resolution**: Preview at the actual output resolution to catch layout issues early.
