---
name: content-image
description: Image prompt engineering for AI image generation models. Use when user wants to generate images, create image prompts, or optimize prompts for DALL-E, Midjourney, Stable Diffusion, or other image generation tools.
---

# Content Image Skill

## Important: This Skill Generates Prompts, Not Images

Claude cannot generate images. This skill produces **ready-to-paste prompts** optimized for AI image generation models. The output is text that the user copies into DALL-E, Midjourney, Stable Diffusion, or another image generation tool.

Every output includes:
1. The prompt text (optimized for the target model)
2. Recommended model and settings
3. Negative prompt (where the model supports it)
4. Variations to try

---

## When This Skill Activates

- User asks for an image, illustration, or visual asset
- User wants to create image prompts or optimize existing prompts
- User mentions DALL-E, Midjourney, Stable Diffusion, Flux, or other image generation tools
- User says "generate an image of..." or "I need a visual for..."
- User wants a hero image, social media graphic, blog illustration, or product shot

---

## Prompt Structure

Every effective image prompt has four components:

### 1. Subject

What is in the image. Be specific and concrete.

- Bad: "a person working"
- Good: "a software developer sitting at a standing desk with dual monitors, writing code, coffee mug nearby"

The subject should be described in enough detail that two different artists would produce recognizably similar images.

### 2. Style

The visual treatment. Reference a specific style from the style library or describe it explicitly.

- Bad: "nice looking"
- Good: "editorial photography, shallow depth of field, natural window light, 35mm lens"

See `style-library/` for pre-built style descriptions:
- `style-library/editorial.md` -- Clean, professional photography
- `style-library/flat-illustration.md` -- Bold, geometric, vector-like
- `style-library/3d-render.md` -- Soft lighting, smooth surfaces, product-shot feel
- `style-library/film-still.md` -- Cinematic, dramatic, atmospheric

### 3. Mood / Atmosphere

The emotional tone of the image.

- Calm, focused, productive
- Energetic, vibrant, optimistic
- Dramatic, tense, high-stakes
- Warm, inviting, approachable
- Minimal, quiet, contemplative

### 4. Technical Specs

Resolution, aspect ratio, and model-specific parameters.

- Aspect ratio: 16:9 (hero banners), 1:1 (social), 4:5 (Instagram portrait), 3:2 (blog photos)
- Quality: high detail, photorealistic vs. stylized
- Lighting: natural, studio, dramatic, flat, backlighting
- Camera: wide angle, close-up, overhead, eye-level

---

## Generation Flow

### Step 1: Read Brand Context

If `brand/VISUAL.md` exists, read it for:
- Color palette (suggest prompts that align with brand colors)
- Visual style preference (photography vs. illustration, minimal vs. bold)
- Mood and tone (professional, playful, technical)

If the brand aesthetic is "clean, minimal, professional," do not suggest prompts for grungy textures or maximalist compositions.

### Step 2: Understand the Need

Ask:
- **What is the image for?** Blog header, social post, presentation slide, product page, email banner.
- **What should it show?** The subject matter.
- **What feeling should it evoke?** The mood.
- **Any existing visual references?** Links to images they like.
- **Target model?** DALL-E, Midjourney, Stable Diffusion, or no preference.

If the user provides a vague request ("I need an image for my blog post about AI"), ask for specifics before generating prompts.

### Step 3: Select Style

Based on the brand and use case, recommend a style:

| Use Case | Recommended Style | Why |
|---|---|---|
| Blog hero image (professional) | Editorial photography | Clean, credible, publication-quality |
| Social media graphic | Flat illustration | Eye-catching, scalable, shares well |
| Product landing page | 3D render | Modern, polished, product-focused |
| Thought leadership piece | Film still | Dramatic, memorable, shareable |
| Technical documentation | Flat illustration | Clear, diagrammatic, on-brand |
| Event promotion | Editorial or film still | Atmospheric, engaging |

### Step 4: Build Prompt

Assemble the prompt using the four components (subject + style + mood + technical specs). Structure varies by model -- see `model-specifics.md`.

### Step 5: Add Negative Prompt

For models that support negative prompts (Stable Diffusion, some Midjourney modes), specify what to avoid:

Common negative prompt elements:
- "blurry, low quality, distorted, deformed"
- "text, watermark, signature, logo" (unless text is desired)
- "stock photo, generic, clip art" (for editorial/premium look)
- "oversaturated, neon, garish" (for professional/muted aesthetics)

### Step 6: Provide Variations

Always offer 2-3 prompt variations:
1. **Close-up variant**: Tighter framing, more detail on the subject.
2. **Wide variant**: Environmental context, more setting.
3. **Alternative style**: A different visual treatment for comparison.

---

## Brand Alignment

When generating prompts, align with the brand aesthetic from `brand/VISUAL.md`:

### Color Alignment

If the brand uses warm earth tones, suggest prompts with:
- "warm lighting, golden hour, earth tones, amber and terracotta palette"

If the brand uses cool blues and grays, suggest:
- "cool lighting, blue-gray tones, steel and slate palette, overcast sky"

Do not force brand colors into every image, but guide the aesthetic direction.

### Style Alignment

| Brand Aesthetic | Prompt Direction |
|---|---|
| Minimal, clean | "clean composition, negative space, simple background, uncluttered" |
| Bold, vibrant | "saturated colors, dynamic composition, high contrast, energetic" |
| Corporate, professional | "studio lighting, neutral background, polished, sharp focus" |
| Playful, creative | "whimsical elements, bright colors, unexpected angles, hand-drawn feel" |
| Technical, precise | "technical illustration, blueprint aesthetic, grid lines, precise geometry" |

### Consistency Across Assets

When generating multiple prompts for the same project (e.g., a series of blog post images), maintain consistency:
- Same style and mood across all prompts
- Same aspect ratio and quality settings
- Same color temperature and lighting direction
- Reference the same style library entry for all prompts in the series

---

## Model-Specific Optimization

See `model-specifics.md` for detailed guidance. Summary:

### DALL-E 3

- Uses natural language descriptions
- Longer, more descriptive prompts work well
- Specify style, mood, and technical details in full sentences
- No negative prompt support (describe what you want, not what you do not want)

### Midjourney

- Responds well to stylistic keywords and aesthetic references
- Use `--ar` for aspect ratio, `--s` for stylization, `--q` for quality
- Shorter, more keyword-driven prompts can be effective
- Version-specific parameters (v6, v6.1)

### Stable Diffusion

- Supports weighted tokens: `(important detail:1.3)` for emphasis
- Negative prompts are critical for quality
- Sampler and step count affect output
- LoRA and checkpoint selection matter

---

## Output Format

For each prompt request, deliver:

```
## Prompt

[The full prompt text, ready to paste]

## Model & Settings

- **Recommended model**: [DALL-E 3 / Midjourney v6.1 / SDXL]
- **Aspect ratio**: [16:9 / 1:1 / 4:5 / etc.]
- **Quality/Steps**: [model-specific settings]

## Negative Prompt (if applicable)

[Negative prompt text for SD/MJ]

## Variations

### Variation 1: [Description]
[Alternative prompt]

### Variation 2: [Description]
[Alternative prompt]

## Notes

[Any tips for getting the best result: regenerate if X, adjust Y for Z]
```

---

## Common Prompt Patterns

### The "Person Doing Thing" Pattern

`[demographic detail] [person description] [action] in [setting], [style], [lighting], [mood]`

Example: "A mid-30s Southeast Asian woman reviewing data on a tablet in a modern open office, editorial photography, natural window light from the left, focused and productive atmosphere"

### The "Product Shot" Pattern

`[product] on [surface/background], [camera angle], [lighting setup], [style]`

Example: "A matte black wireless keyboard on a minimal white desk, 45-degree angle, soft studio lighting with subtle shadow, 3D product render, clean and modern"

### The "Abstract Concept" Pattern

`[visual metaphor for concept], [style], [color palette], [mood]`

Example: "Interconnected glowing nodes forming a neural network pattern, dark background, blue and purple gradient, isometric 3D render, futuristic and clean"

### The "Environment" Pattern

`[place description], [time of day], [weather/atmosphere], [style], [camera position]`

Example: "A coworking space with floor-to-ceiling windows at golden hour, plants on desks, warm natural light, editorial photography, wide angle from the entrance"

---

## What This Skill Does Not Do

- Generate actual images (Claude is a text model)
- Create SVG graphics (use content-infographic for that)
- Design logos or brand marks (use a designer or specialized tool)
- Edit existing photos (use Photoshop, Lightroom, or similar)

If the user needs an SVG or infographic, redirect to the content-infographic skill. If they need a presentation visual, redirect to content-presentation.
