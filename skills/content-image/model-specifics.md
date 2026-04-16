# Model-Specific Prompt Guidance

How to optimize prompts for each major image generation model. The same concept requires different prompt strategies depending on the target model.

---

## DALL-E 3 (OpenAI)

### How It Works

DALL-E 3 uses a language model to expand your prompt before generating. It prefers natural language over keyword lists. Describe the image as you would to a skilled photographer or illustrator.

### Prompt Strategy

- **Write full sentences**: "A software developer reviewing code on a large monitor in a modern office with natural light streaming through floor-to-ceiling windows" works better than keyword dumps.
- **Be descriptive**: More detail generally produces better results. Specify colors, materials, lighting, mood, composition.
- **Describe what you want, not what you do not want**: DALL-E 3 has no negative prompt support. Instead of "no people," say "empty room."
- **Style references work**: "in the style of editorial photography" or "flat vector illustration style" are understood.
- **Specify aspect ratio in the API**: Use the `size` parameter: `1024x1024`, `1792x1024`, `1024x1792`.

### Example Prompt (DALL-E 3)

```
A mid-30s woman sitting at a minimalist white desk reviewing financial data on a
large curved monitor. The office has floor-to-ceiling windows with soft morning
light coming from the left. A small succulent plant and a ceramic coffee mug sit
on the desk. Editorial photography style, shallow depth of field, muted warm
tones, 50mm lens perspective. The mood is focused and productive.
```

### Settings

| Parameter | Value | Notes |
|---|---|---|
| Size | `1792x1024` | Landscape. Use `1024x1792` for portrait. |
| Quality | `hd` | Always use HD for final assets. `standard` for drafts. |
| Style | `natural` or `vivid` | `natural` for photography. `vivid` for illustrations and dramatic scenes. |

### Tips

- DALL-E 3 rewrites your prompt internally. If the output does not match your intent, add more specific constraints.
- It handles text in images better than previous versions, but text is still unreliable. Avoid prompts that require specific words in the image.
- For consistent series, repeat the core style description verbatim across prompts and only change the subject.

---

## Midjourney

### How It Works

Midjourney responds well to aesthetic keywords, artistic references, and technical photography terms. It is more "vibes-driven" than DALL-E -- fewer words can produce strong results if those words are well-chosen.

### Prompt Strategy

- **Lead with the subject, follow with style**: "portrait of a woman at a desk, editorial photography, natural light, muted tones"
- **Use aesthetic keywords**: Midjourney understands terms like "ethereal," "moody," "cinematic," "minimalist," "brutalist."
- **Reference artists or art movements** (for style, not to copy): "in the style of editorial photography" or "inspired by Bauhaus design."
- **Parameters matter**: Append `--ar`, `--s`, `--q`, and `--v` parameters.
- **Shorter prompts can work**: Unlike DALL-E, Midjourney sometimes produces better results with focused, shorter prompts.

### Example Prompt (Midjourney)

```
woman reviewing code on large monitor, modern minimal office, natural window light,
editorial photography, shallow depth of field, muted warm tones, 50mm lens --ar 16:9
--s 250 --q 2 --v 6.1
```

### Parameters

| Parameter | Values | Purpose |
|---|---|---|
| `--ar` | `16:9`, `1:1`, `4:5`, `2:3`, `3:2` | Aspect ratio |
| `--s` | 0-1000 (default 100) | Stylization. Higher = more artistic interpretation. Lower = more literal. |
| `--q` | 0.25, 0.5, 1, 2 | Quality/detail. 2 = maximum. |
| `--v` | `6`, `6.1` | Model version. Use latest for best results. |
| `--no` | keywords | Negative prompt. `--no text, watermark, blur` |
| `--c` | 0-100 (default 0) | Chaos. Higher = more variation between results. |
| `--w` | 0-1000 | Weird. Adds unusual elements. Use low values (50-100) for subtle creative variation. |

### Tips

- Use `/describe` on a reference image to get keywords Midjourney understands.
- `--s 0` gives you the most literal interpretation of your prompt. Good for specific requirements.
- `--s 750+` gives you Midjourney's artistic interpretation. Good for exploration.
- For photographic realism, include camera and lens references: "Canon EOS R5, 85mm f/1.4."
- For illustration styles, reference the medium: "digital illustration, vector art, gouache painting."

---

## Stable Diffusion (SDXL / SD 1.5)

### How It Works

Stable Diffusion uses a CLIP text encoder that responds to weighted tokens. It is the most configurable model -- you control the checkpoint, sampler, steps, CFG scale, and can apply LoRAs for specific styles. Negative prompts are essential.

### Prompt Strategy

- **Use weighted tokens**: `(important detail:1.3)` increases emphasis. `(unwanted detail:0.5)` decreases. Scale from 0.5 to 1.5.
- **Keyword-driven**: Similar to Midjourney but with more control. Front-load the most important elements.
- **Quality boosters**: Include quality keywords like "masterpiece, best quality, highly detailed, 8k" at the start or end.
- **Negative prompts are critical**: Always include a negative prompt to avoid common artifacts.
- **Checkpoint matters**: Choose a checkpoint that matches your desired style (realistic, anime, illustration).

### Example Prompt (Stable Diffusion / SDXL)

**Positive**:
```
(editorial photography:1.3), woman reviewing code on large monitor, modern minimal office,
(natural window light:1.2), shallow depth of field, muted warm tones, 50mm lens,
focused expression, high quality, professional photograph, 8k
```

**Negative**:
```
(low quality:1.4), (blurry:1.3), deformed, distorted, disfigured, bad anatomy,
extra fingers, mutated hands, watermark, text, signature, logo, stock photo,
oversaturated, HDR, cartoon, anime, 3d render, painting
```

### Key Settings

| Setting | Recommended Values | Notes |
|---|---|---|
| Sampler | DPM++ 2M Karras, Euler a | DPM++ 2M Karras is reliable for most uses. |
| Steps | 25-40 | More steps = more detail but slower. 30 is a good default. |
| CFG Scale | 5-9 | How closely to follow the prompt. 7 is default. Higher = more literal but can look stiff. |
| Resolution | 1024x1024 (SDXL), 512x768 (SD 1.5) | Generate at native resolution, then upscale. |
| Seed | -1 (random) or fixed | Fix seed for reproducibility. Use random for exploration. |

### LoRA and Checkpoint Selection

- **Photorealistic**: Use a realistic checkpoint (Juggernaut XL, RealVisXL).
- **Illustration**: Use an illustration-focused checkpoint or LoRA.
- **Specific style**: Search CivitAI for LoRAs that match the desired aesthetic.

### Tips

- Always use a negative prompt. The difference in quality is dramatic.
- For SDXL, generate at 1024x1024 or 1024x768. Do not go below 768 on any dimension.
- Use img2img for refining a generation you like but want to adjust.
- ControlNet can guide composition (pose, depth, edge) -- useful for specific layouts.
- For consistent series, fix the seed and only change the subject in the prompt.

---

## Model Comparison

| Factor | DALL-E 3 | Midjourney | Stable Diffusion |
|---|---|---|---|
| Prompt style | Natural language | Keywords + parameters | Weighted tokens |
| Negative prompts | Not supported | `--no` parameter | Full negative prompt |
| Customization | Low (API params only) | Medium (params) | High (checkpoints, LoRAs, samplers) |
| Ease of use | Highest | High | Lowest (needs setup) |
| Text in images | Best (but still imperfect) | Poor | Poor |
| Photorealism | Very good | Excellent | Excellent (with right checkpoint) |
| Illustration | Good | Excellent | Good to excellent |
| Consistency | High | Medium | Medium (higher with fixed seeds) |
| Cost | Per-image API pricing | Subscription | Free (self-hosted) or per-image |
| Best for | Quick, high-quality results | Aesthetic exploration | Full control, specific styles |

---

## Recommendations by Use Case

| Use Case | Primary | Why |
|---|---|---|
| Blog hero images | DALL-E 3 | Fast, consistent, natural language prompts |
| Social media series | Midjourney | Strong aesthetics, good variation with upscaling |
| Brand-specific style | Stable Diffusion | Train a LoRA on brand imagery for consistency |
| Product mockups | Midjourney or DALL-E 3 | Both handle objects well |
| Abstract/conceptual | Midjourney | Best at interpreting abstract prompts artistically |
| Batch generation | Stable Diffusion | Self-hosted, no per-image cost |
| Quick iteration | DALL-E 3 | Fastest turnaround, API integration |
