# Pattern: Slide Deck / Presentation to Blog Post

## When to Use

The source is a slide deck (10-50 slides) with or without speaker notes, and the target is a blog post (1500-3500 words).

---

## Transformation Steps

### Step 1: Understand the Presentation Structure

Slides are visual, compressed, and designed for a speaker to elaborate on. Map the structure:

- **Title slide**: Becomes the blog title and introduction
- **Agenda / overview slide**: Becomes the blog outline or section structure
- **Content slides**: Each slide or group of related slides becomes a blog section
- **Transition slides**: Usually become section headings or paragraph transitions
- **Summary / closing slide**: Becomes the blog conclusion
- **Speaker notes**: These are your primary source for the written content -- they contain what the speaker actually said, which is far more detailed than the slide bullets

### Step 2: Expand the Bullets

Slide bullets are compressed. Each bullet typically represents a paragraph of explanation. For each bullet point:

- What is the full explanation behind this point?
- What example or evidence supports it?
- Why does it matter?
- How does it connect to the next point?

If speaker notes exist, use them as the starting point and expand from there. If no speaker notes exist, you will need to infer the explanation from the bullet points and any context the user provides.

### Step 3: Add Written Transitions

Presentations rely on the speaker's voice and slide transitions to connect ideas. Blog posts need explicit written transitions:

| Presentation Transition | Blog Transition |
|---|---|
| New slide appears | New section heading with a transitional sentence |
| Speaker says "Now let's look at..." | "This raises a related question: [next section topic]." |
| Animated build (bullets appearing one by one) | Numbered list with explanatory text between items |
| Visual comparison (side-by-side) | Comparison table or "On the one hand... on the other hand..." structure |
| Demo slide | Step-by-step walkthrough with code blocks or screenshots |

### Step 4: Handle Visual Slides

For slides that are primarily visual (diagrams, charts, screenshots):

- **Diagrams**: Describe the diagram in text AND embed the image. Do not rely on the image alone -- blog readers may skim past images, and screen readers cannot read diagrams.
- **Charts/data**: Include the key numbers in text. "As the chart shows, conversion increased from 2.1% to 3.7% over 6 months" is better than just embedding the chart.
- **Screenshots**: Include as images with captions that explain what the reader should notice.
- **Key slides**: Consider embedding 3-5 of the most impactful slides as images to break up the text and give readers a visual anchor.

### Step 5: Write the Blog Post

Structure:

1. **Title**: Adapt the presentation title for SEO and click-worthiness. Presentation titles are often short and vague ("The Future of APIs"). Blog titles should be specific ("Why REST APIs Won't Survive the Next 5 Years").
2. **Introduction**: Do not start with "I recently gave a talk about..." unless the talk itself is the story. Start with the problem or insight the presentation addressed.
3. **Body sections**: One section per major slide group. Each section should:
   - Open with the key point (not the buildup)
   - Include the explanation that the speaker would have given
   - Add concrete examples, code, or data
   - Embed relevant slides as images where they add value
4. **Conclusion**: Expand the closing slide into a proper ending with a CTA or forward-looking insight.
5. **Link to the original**: If the slides are available online, link to them at the beginning or end for people who prefer the visual format.

---

## Example Transformation

**Slide** (bullet points):
```
Why We Moved to Event-Driven Architecture
- Synchronous calls between 12 services
- P99 latency: 4.2 seconds
- One service down = cascade failure
- Needed: loose coupling + resilience
```

**Speaker notes** (if available):
> "So when we started, we had 12 microservices all calling each other synchronously. You can imagine the problems. Our P99 latency had crept up to over 4 seconds, and the worst part was that if any single service went down, it would cascade and take down half the platform."

**Blog version**:

```markdown
## The Problem: Synchronous Spaghetti

Our platform had grown to 12 microservices, all communicating through
synchronous HTTP calls. On paper, microservices promised independence.
In practice, we had built a distributed monolith.

The symptoms were hard to ignore:

- **Latency**: P99 response time had crept up to 4.2 seconds. A single
  user request could trigger a chain of 6 synchronous calls, each
  waiting for the previous one to complete.
- **Fragility**: When any one service went down, the failure cascaded.
  A 30-second outage in our notification service would cause timeouts
  in the order service, which backed up the payment service, which
  eventually brought down the entire checkout flow.
- **Coupling**: Despite being separate services, they were deeply coupled
  through their synchronous APIs. Changing one service's contract
  required coordinated deploys across three others.

We needed loose coupling and resilience. That led us to event-driven
architecture.
```

---

## Common Mistakes

1. **Bullet-to-bullet translation**: Simply converting slide bullets into blog bullets misses the opportunity to add depth. Each bullet should become a paragraph or a well-explained list item.
2. **Ignoring visual slides**: If a slide had an architecture diagram, the blog needs either the image or a detailed textual description. Do not skip visual content.
3. **Keeping presentation rhetoric**: "Let's take a look at..." and "As we discussed in the previous slide..." do not work in blog format. Rewrite transitions for a reading experience.
4. **No context for embedded slides**: If you embed a slide image, add a caption and surrounding text that explains what the reader should take from it.
5. **Forgetting the speaker's value-add**: The slides alone are often not that informative. The speaker's commentary is where the real content lives. If you do not have speaker notes, you need the user's input on what each slide was about.
