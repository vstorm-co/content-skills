---
name: content-repurpose
description: Transform content from one format into multiple formats while maintaining brand consistency. Use when user wants to repurpose content, convert a blog post to tweets, turn a presentation into a blog, create multiple formats from one piece, or cross-post content.
---

# Content Repurposing

## Core Principle: 1-to-Many

One strong piece of content should become 5+ pieces across different platforms and formats. This is not about copying and pasting -- each transformation adapts the content for the target platform's norms, audience expectations, and native format.

A single blog post can become:
- An X thread extracting the key insights
- A LinkedIn post with a professional angle
- A newsletter section with personal commentary
- A short-form video script
- A slide deck for presentations
- A Reddit post framed for community value
- An infographic summarizing the data

The source material provides the substance. Each transformation reshapes it.

---

## Before You Start

1. **Check for brand voice**: Read `brand/VOICE.md` if it exists. All transformations must maintain the same brand voice, even though tone and format vary by platform. If no brand voice is defined, maintain consistency across all outputs by inferring voice from the source material.

2. **Identify the source material**: What is the input? It can be any content piece:
   - Blog post or article
   - X thread
   - Video script or transcript
   - Podcast transcript
   - Slide deck or presentation
   - Newsletter issue
   - LinkedIn post
   - Any other written or spoken content

3. **Determine target formats**: Ask the user which formats they want, or recommend based on the format matrix in `format-matrix.md`. Not every source transforms well into every target -- the matrix shows which transformations are natural and which require significant rework.

4. **Understand platform norms**: Each platform has its own culture, format constraints, and audience expectations. Transformations that ignore these norms feel off.

---

## Repurposing Flow

### Stage 1: Source Analysis

Read the source material and extract:

- **Core message**: The single most important idea (one sentence)
- **Key insights**: 3-7 individual points or arguments
- **Best quotes**: Punchy, shareable lines from the source
- **Data points**: Numbers, statistics, or concrete examples
- **Narrative arc**: The story structure (if any)
- **Audience**: Who was the original piece written for?
- **Strongest section**: Which part of the source has the most standalone value?
- **Weakest section**: Which part depends heavily on context from the rest of the piece?

### Stage 2: Transformation Planning

For each target format, plan the transformation:

- What subset of the source material works for this format?
- What needs to be added (platform-specific framing, context, CTA)?
- What needs to be removed (detail that does not fit the format)?
- What structural changes are needed (reordering, splitting, combining)?
- What is the hook for this specific platform?

Reference the specific pattern file in `patterns/` for each transformation.

### Stage 3: Execution

Generate each transformation following the appropriate pattern. For each output:

1. Open with a platform-native hook (not the same hook used in the source or other outputs)
2. Adapt the content structure for the target format
3. Apply brand voice consistently
4. Add platform-specific elements (hashtags, formatting, CTA style)
5. Ensure the piece works standalone -- a reader should not need to have seen the source

### Stage 4: Review

Review all transformations together:

- Does each piece stand alone? (Someone encountering just the LinkedIn post should get value)
- Is the brand voice consistent across all outputs?
- Are the hooks different enough that someone who follows you on multiple platforms does not see the same opening five times?
- Does each piece feel native to its platform?
- Are there any contradictions between pieces?

---

## Transformation Patterns

Detailed guides for specific transformations are in the `patterns/` directory:

| Pattern | File | Description |
|---|---|---|
| Blog to Thread | `patterns/blog-to-thread.md` | Extract key insights into a tweetstorm |
| Thread to LinkedIn | `patterns/thread-to-linkedin.md` | Consolidate and professionalize |
| Video to Blog | `patterns/video-to-blog.md` | Structure written content from visual beats |
| Slides to Blog | `patterns/slides-to-blog.md` | Expand slide bullets into full narrative |
| Podcast to Social | `patterns/podcast-to-social.md` | Extract quotable moments and companion posts |

For transformations not covered by a specific pattern, follow the general principles in the flow above and adapt.

---

## Platform-Specific Adaptation Rules

Each platform has specific norms that transformations must respect:

### X / Twitter
- Maximum 280 characters per tweet (threads can be longer)
- Hook must be in the first tweet -- it determines whether anyone reads the rest
- Use line breaks for readability
- Numbers, lists, and surprising facts perform well
- End threads with a CTA or a callback to the first tweet

### LinkedIn
- Professional tone, but personal stories perform best
- First 2-3 lines must hook (they appear before the "see more" fold)
- Longer posts (800-1200 characters) tend to outperform short ones
- Lessons, frameworks, and personal reflections resonate
- Avoid jargon that would not make sense outside your niche

### Newsletter
- Readers have opted in -- they expect more depth and personality
- Personal commentary and opinion are expected, not just information
- Link back to the source material for those who want the full version
- Curate and contextualize, do not just summarize

### Reddit
- Community-first framing -- what value does this provide to the subreddit?
- No self-promotion tone. Frame everything as a contribution.
- Include enough context that the post is self-contained
- Engage with comments -- Reddit audiences expect two-way conversation

### YouTube / Video
- Visual storytelling -- what can you show, not just tell?
- Open with the hook in the first 3 seconds
- Structure content with clear sections and transitions
- Add visual elements that do not exist in the written version

---

## Parallel Execution

For large repurposing jobs (e.g., a blog post into 5+ formats), transformations can be executed in parallel since they are independent of each other. Each transformation:

- Takes the same source analysis as input
- Follows its own pattern
- Produces a standalone output

The only dependency is that the source analysis (Stage 1) must be complete before any transformation begins.

---

## Brand Consistency Across Transformations

When the same content appears on multiple platforms:

1. **Same core message**: The central insight should be consistent everywhere
2. **Same voice**: The brand personality should be recognizable across all outputs
3. **Different hooks**: Each platform gets a unique opening -- do not reuse hooks
4. **Different structure**: Each output should feel native to its platform
5. **Different CTAs**: Vary what you ask the audience to do (follow, read more, comment, share)
6. **Consistent facts**: If you cite a number in one place, use the same number everywhere

---

## Output Checklist

Before delivering the transformations, verify:

- [ ] Source material has been analyzed for core message, key insights, and best quotes
- [ ] Each transformation follows the appropriate pattern from `patterns/`
- [ ] Each output stands alone (does not require reading the source to make sense)
- [ ] Hooks are unique per platform (not the same opening repeated)
- [ ] Brand voice is consistent across all outputs
- [ ] Each output feels native to its target platform
- [ ] CTAs are appropriate for each platform
- [ ] No contradictions between outputs
- [ ] Format matrix confirms the transformation is well-suited (see `format-matrix.md`)
