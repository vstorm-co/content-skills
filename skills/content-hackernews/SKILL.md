---
name: content-hackernews
description: Hacker News post generation for Show HN, Ask HN, and submissions. Use when user wants to post to Hacker News or write a Show HN/Ask HN post.
---

# Hacker News Content Generation

## Before You Start

1. **Understand HN culture**: Hacker News (news.ycombinator.com) is a community driven by intellectual curiosity and technical depth. It is run by Y Combinator and attracts founders, engineers, researchers, and technically sophisticated readers. The community is allergic to marketing, superlatives, and hype.

2. **Determine post type**:
   - **Show HN**: Sharing something you have built for community feedback
   - **Ask HN**: Asking the community a question
   - **Standard submission**: Sharing a link to content (your own or someone else's)

3. **Check for brand voice**: Read `brand/VOICE.md` if it exists, then heavily adapt it using `hn-voice.md`. HN has the strictest voice requirements of any platform. Marketing language of any kind will get the post flagged, downvoted, or ignored.

---

## HN Culture

### What HN Values
- Intellectual curiosity and genuine interest in ideas
- Technical depth and rigorous thinking
- Honesty, especially about limitations and trade-offs
- Novel insights and original thinking
- Clear, direct writing without embellishment
- Substance over polish

### What HN Rejects
- Marketing language of any kind ("revolutionary," "game-changing," "disruptive")
- Superlatives ("the best," "the fastest," "the most powerful")
- Emotional manipulation or engagement bait
- Clickbait titles
- Self-congratulation
- Hype without substance
- Excessive self-promotion without proportional community contribution

### The HN Audience
- Technically sophisticated: assume your reader can evaluate technical claims
- Detail-oriented: vague claims will be challenged in comments
- Skeptical of hype: extraordinary claims need extraordinary evidence
- Global: readers span every timezone and many industries
- Time-constrained: they scan titles and click selectively

---

## Show HN Format and Rules

Show HN is for sharing your own projects, products, or creations with the community.

### Title Format
```
Show HN: [Concise description of what it is]
```

**Good titles:**
- "Show HN: A terminal-based Markdown editor written in Rust"
- "Show HN: Open-source tool to visualize PostgreSQL query plans"
- "Show HN: I built a search engine for academic papers using semantic embeddings"

**Bad titles:**
- "Show HN: The revolutionary new way to manage your infrastructure" (marketing)
- "Show HN: Check out my awesome app!" (vague, hyped)
- "Show HN: [ProductName] -- Disrupting the observability space" (buzzwords)

### Title Rules
- Describe what it does, not how great it is
- Include the technology if relevant ("written in Rust," "using WASM")
- Keep it under 80 characters
- Do not use all caps or exclamation marks
- Do not include pricing or "free" in the title

### The Accompanying Comment

Every Show HN post should have a top-level comment from the creator. This comment is critical. Use `show-hn-template.md` for the structure.

The comment should cover:
1. **What it is**: One sentence. Clear, specific, no jargon.
2. **Why you built it**: The problem you faced or the motivation behind the project.
3. **How it works**: Brief technical overview for the curious. Architecture, key technologies, interesting design decisions.
4. **What's interesting technically**: What did you learn? What was hard? What's novel?
5. **Current state and limitations**: What works, what doesn't, what's next. Honesty here earns enormous respect.
6. **What you want**: Specific feedback you are looking for. "Feedback welcome" is vague. "I'd love feedback on the query optimizer approach" is actionable.

---

## Ask HN Format

Ask HN is for questions directed at the community.

### Title Format
```
Ask HN: [Your question]
```

**Good Ask HN posts:**
- Specific, well-defined questions
- Questions that invite diverse, experience-based answers
- Questions the community has not been asked recently
- Questions where the asker has context to share

**Bad Ask HN posts:**
- Questions easily answered by a search engine
- Surveys or market research disguised as questions
- "What do you think of [my product]?" (use Show HN instead)

### Body
- Provide context for why you are asking
- Share what you have already tried or considered
- Be specific about constraints or requirements
- Keep it concise. HN readers value brevity.

---

## Standard Submissions

When submitting a link (blog post, article, paper, tool):

### Title
- Use the original title of the content. HN prefers this.
- If the original title is clickbait, rewrite it to be descriptive and neutral
- Do not editorialize: "Great article about X" is editorializing. Just submit "X" with the link.
- Adding "(2023)" for older content or "(PDF)" for PDFs is acceptable

### Submission Timing
- HN is most active during US business hours (Pacific time)
- Posting during peak hours gives more initial visibility
- Weekends have less competition but also less traffic

---

## What Gets Flagged and Downvoted

Understanding HN's enforcement culture helps you avoid problems:

**Flagged (removed by community or moderators):**
- Obviously promotional submissions
- Clickbait titles
- Duplicate submissions of recent stories
- Low-quality content
- Submissions from domains that are heavily self-promoted

**Downvoted:**
- Comments with marketing language
- Defensive responses to criticism
- Comments that don't add to the discussion
- Self-promotional comments unrelated to the discussion
- "Thanks for the feedback!" without substance

**Invisible penalty: flame detection**
- HN has sophisticated flame-war detection
- Heated or uncharitable comments may be auto-deprioritized
- Assume good faith in your responses, even when others don't

---

## HN Voice

See `hn-voice.md` for detailed voice guidance. The essential rules:

1. **Be direct.** State things clearly. No throat-clearing.
2. **Be technical.** HN readers expect and appreciate technical depth.
3. **Be honest about limitations.** "We don't handle X well yet" earns more respect than "We handle everything."
4. **No superlatives.** Replace "the best" with specific comparisons.
5. **No marketing language.** If it could appear in a press release, rewrite it.
6. **Show, don't tell.** Instead of "It's fast," show the benchmark.

---

## Output Checklist

Before delivering HN content:

- [ ] Title is descriptive, not promotional (under 80 characters)
- [ ] Zero marketing language or superlatives
- [ ] Show HN posts include a substantive creator comment
- [ ] Ask HN posts include context and show prior research
- [ ] Technical details are included where relevant
- [ ] Limitations and current state are honestly described
- [ ] The content would survive scrutiny from a technically sophisticated, skeptical audience
- [ ] Voice follows `hn-voice.md` guidelines
- [ ] No clickbait, emotional manipulation, or engagement bait
