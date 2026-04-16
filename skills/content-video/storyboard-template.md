# Storyboard Template

Use this format for all video storyboards. Copy the scene block below for each scene in the video.

---

## Video Metadata

| Field | Value |
|---|---|
| **Title** | [Working title] |
| **Format** | [social-short / explainer / data-story / talking-head] |
| **Target Duration** | [e.g., 60 seconds] |
| **Platform** | [YouTube / TikTok / LinkedIn / X / Instagram / General] |
| **Aspect Ratio** | [16:9 / 9:16 / 1:1] |
| **Resolution** | [1920x1080 / 1080x1920 / 1080x1080] |
| **FPS** | [30 / 60] |
| **Narration Style** | [Voiceover / On-screen text / Talking head / Mixed] |
| **Music Mood** | [Upbeat / Calm / Dramatic / Corporate / Playful / None] |

---

## Scene Template

Copy this block for each scene:

```
### Scene [NUMBER]: [Scene Title]

**Timestamp**: [START] - [END]
**Duration**: [X seconds]

**Visual Description**:
[Describe exactly what the viewer sees. Include composition, layout, colors, elements on screen, background. Be specific enough that a designer or Remotion developer could recreate it.]

**Narration / Dialogue**:
[Exact words spoken by the narrator or displayed as on-screen text. Include emphasis markers in *asterisks* and pause indicators as [PAUSE]. If no narration, write "None -- visual only."]

**Motion Notes**:
- [Element]: [Animation type] (e.g., "Title text: fade in from bottom over 0.5s")
- [Element]: [Animation type]
- Transition to next scene: [cut / crossfade / slide / zoom / wipe]

**Audio Cues**:
- Music: [Description of music state -- starts, continues, fades, changes mood, stops]
- Sound effects: [Specific SFX with timing, e.g., "Whoosh on title reveal"]
- Ambient: [Background sounds if any]

**On-Screen Text** (if any):
- [Text content] | [Position: top/center/bottom] | [Style: title/subtitle/caption/lower-third]

**Assets Required**:
- [List images, icons, logos, footage, data visualizations needed for this scene]
```

---

## Example Scene

### Scene 1: Hook

**Timestamp**: 0:00 - 0:04
**Duration**: 4 seconds

**Visual Description**:
Dark background (#0A0A0A). A single line of white text appears center-screen in the brand heading font. Below it, a subtle gradient line in brand primary color pulses once.

**Narration / Dialogue**:
"What if your deploy pipeline could fix *itself*?"

**Motion Notes**:
- Title text: spring animation from scale 0.8 to 1.0, opacity 0 to 1 over 0.6s
- Gradient line: fade in at 0.8s, pulse animation at 1.2s
- Transition to next scene: crossfade over 0.5s

**Audio Cues**:
- Music: Low ambient synth begins, builds subtly
- Sound effects: Soft "ping" sound on text reveal
- Ambient: None

**On-Screen Text**:
- "What if your deploy pipeline could fix itself?" | center | title

**Assets Required**:
- Brand heading font
- Brand primary color value

---

## Storyboard Summary Table

After writing all scenes, include a summary table:

| Scene | Timestamp | Duration | Key Visual | Key Message |
|---|---|---|---|---|
| 1 | 0:00-0:04 | 4s | Hook text on dark bg | Pose the central question |
| 2 | 0:04-0:12 | 8s | Problem illustration | Show the pain point |
| ... | ... | ... | ... | ... |

**Total Duration**: [Sum of all scene durations]
**Word Count (Narration)**: [Total words in narration]
**Estimated VO Time**: [Word count / 150 words per minute]
