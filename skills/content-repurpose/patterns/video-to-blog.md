# Pattern: Video Script / Transcript to Blog Post

## When to Use

The source is a video script, video transcript, or recording notes, and the target is a blog post (1000-3000 words).

---

## Transformation Steps

### Step 1: Analyze the Video Structure

Videos and blog posts have different structures. Map the video's flow:

- **Visual beats**: What was shown on screen? These become sections, diagrams, or screenshots in the blog.
- **Narration flow**: What was said? This becomes the blog's written content, but it needs restructuring because spoken language is more repetitive and informal than written language.
- **Demonstrations**: Live demos or screen recordings become step-by-step instructions with screenshots.
- **Transitions**: "As you can see here..." becomes explicit section headings and written transitions.
- **Timestamps**: Use timestamps to identify the major sections and their relative importance.

### Step 2: Restructure for Reading

Spoken content follows a different logic than written content:

| Video Pattern | Blog Adaptation |
|---|---|
| Long verbal setup before the point | Lead with the point, then provide context |
| "As I mentioned earlier..." callbacks | Remove -- blog readers can scroll back |
| Visual demonstrations | Screenshots, code blocks, or diagrams with captions |
| Filler and repetition for emphasis | Cut ruthlessly -- written repetition feels lazy |
| Conversational tangents | Cut or move to a footnote/aside |
| "Let me show you..." transitions | Replace with section headings |
| Real-time debugging or exploration | Summarize the result; link to the video for the full walkthrough |

### Step 3: Add What Video Cannot Provide

Blog posts can offer things video cannot:

- **Scannable structure**: Headers, subheaders, bullet lists, code blocks
- **Copyable code**: Actual code blocks that readers can copy (vs. code on a screen recording)
- **Links**: Reference documentation, related posts, tools mentioned
- **Searchability**: SEO-optimized headings and content for people searching for the topic
- **Quick reference**: Summary tables, checklists, or TL;DR sections

### Step 4: Write the Blog Post

1. **Opening**: Write a new hook for blog readers. Do not use the video's "Hey everyone, welcome to..." opening. Start with the problem or insight.
2. **Body**: Convert each major video section into a blog section. Expand where the video was surface-level (spoken words convey less detail per minute than written words). Compress where the video was repetitive.
3. **Visuals**: Add screenshots or diagrams where the video showed something on screen. Describe visual elements in text for accessibility and searchability.
4. **Code**: If the video showed code, include it as properly formatted code blocks with syntax highlighting.
5. **Closing**: Write a blog-appropriate ending (not "Thanks for watching, don't forget to subscribe").

### Step 5: Cross-Link

- Link to the original video for people who prefer watching
- Embed the video at the top of the post if the platform supports it
- Note key timestamps in the video that correspond to blog sections

---

## Example Transformation

**Video transcript excerpt**:
> "Okay so let me show you what happens when we deploy this. As you can see on my screen, I'm going to go ahead and open up the terminal here. And what I'm going to do is run our deploy command. So let me type that in... npm run deploy. And you can see it's building now. Okay so while that's running, let me explain what's happening behind the scenes. The deploy script is actually doing three things..."

**Blog version**:

```markdown
## How the Deploy Works

Running `npm run deploy` triggers a three-stage pipeline:

1. **Build** -- Compiles TypeScript, bundles assets, and generates the static output
2. **Test** -- Runs the integration test suite against the build output
3. **Push** -- Deploys the build artifact to the CDN with cache invalidation

\`\`\`bash
npm run deploy
# Output:
# [1/3] Building... done (14s)
# [2/3] Testing... 42 passed, 0 failed (8s)
# [3/3] Deploying... done (3s)
# Deployed to https://example.com
\`\`\`

The entire process takes roughly 25 seconds for a typical build.
```

Notice what changed:
- Removed the verbal setup and screen-navigation narration
- Added a numbered list summarizing the stages
- Included a code block with the command and expected output
- Added specific timing information
- Made it scannable and reference-friendly

---

## Common Mistakes

1. **Transcribing instead of transforming**: A transcript is not a blog post. Spoken language needs substantial restructuring for reading.
2. **Losing the visual information**: If the video showed a diagram, architecture, or UI, the blog needs a screenshot or a written description of what was shown.
3. **Keeping verbal tics**: "So," "basically," "you know," "let me show you" -- remove all verbal filler.
4. **Missing the opportunity to add depth**: Spoken content is often shallower than written content because of time constraints. The blog version should add the detail that the video glossed over.
5. **Forgetting SEO**: Video titles and descriptions are often informal. Blog posts should have keyword-optimized headings and meta descriptions.
