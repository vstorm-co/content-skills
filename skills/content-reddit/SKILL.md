---
name: content-reddit
description: Subreddit-aware post generation that matches community norms. Use when user wants to create a Reddit post or comment for any subreddit.
---

# Reddit Post Generation

## Before You Start

1. **Identify the target subreddit**: Different subreddits have radically different cultures, rules, and expectations. You must tailor content to the specific community.

2. **Check for subreddit profile**: Look in `subreddit-profiles/` for a profile of the target subreddit. If one exists, follow its guidance. If not, research the subreddit's rules and culture before writing.

3. **Check for brand voice**: Read `brand/VOICE.md` if it exists. Reddit requires the most aggressive voice adaptation of any platform -- brand voice must be subordinated to subreddit culture. If the brand voice conflicts with subreddit norms, subreddit norms win.

4. **Gather inputs**: Topic, target subreddit, post type (discussion, resource share, question, Show-style), any links or projects to share.

---

## Reddit's Anti-Marketing Culture

Reddit's users are among the most marketing-averse audiences on the internet. Understanding this is non-negotiable.

**Core principles:**
- Reddit communities exist for their members, not for brands
- Redditors can detect promotional content instantly and will punish it
- Value must come first; any mention of a product, service, or project must be secondary to the value the post provides
- Authenticity is the only currency that works on Reddit
- Being upfront about affiliations earns respect; hiding them destroys credibility

**Consequence of getting it wrong:**
- Post gets downvoted to zero
- Comments call out the promotional intent
- Account gets flagged or banned from the subreddit
- Brand reputation takes a hit with the most vocal tech community on the internet

---

## Subreddit Research Protocol

Before writing for any subreddit, understand:

### 1. Rules
- Read the sidebar rules completely
- Check for required post formats (flair, title format, content requirements)
- Note any banned content types (self-promotion, link posts, memes)

### 2. Culture
- What tone do top posts use? (Technical? Casual? Meme-heavy? Serious?)
- How long are successful posts? (One paragraph? Multi-section?)
- What kind of content gets upvoted vs. downvoted?
- How do community members talk to each other?

### 3. Self-Promotion Rules
- Most subreddits follow the "10% rule": no more than 10% of your activity should be self-promotional
- Some subreddits have specific self-promotion threads or days
- Some ban self-promotion entirely
- "Show" posts (sharing your own project) are usually acceptable if they follow the community's norms for transparency

### 4. Existing Conversations
- Has this topic been discussed recently? If so, consider commenting on the existing thread instead of creating a new one
- What questions or complaints come up repeatedly? Address those proactively in your post

---

## Post Types

### Discussion Post
- Opens with an observation, question, or thesis
- Invites genuine debate (not "Agree?")
- Shows the poster has thought about the topic before posting
- Includes the poster's own perspective as a starting point

### Resource Share / Link Post
- The title should describe what the resource is and why it's valuable
- If sharing your own work, say so explicitly
- Add a comment explaining context: what it is, why you built/wrote it, what feedback you are looking for

### Question Post
- Show you have already done basic research (Reddit hates "let me Google that for you" situations)
- Be specific about your setup, what you have tried, and where you are stuck
- Format code or technical details clearly

### Show-Style Post (Sharing Your Own Work)
- Be transparent: "I built this" not "Check out this cool tool" (which hides your affiliation)
- Lead with what the project does and why it exists
- Include technical details the community cares about
- Acknowledge limitations and what is not finished
- Ask for specific feedback, not just "thoughts?"
- See `anti-shill.md` for the full anti-promotional playbook

---

## Anti-Shill Rules

Read `anti-shill.md` before writing any post that mentions a product, project, or service. The core rules:

1. **Lead with value.** The post must be genuinely useful even if the reader never clicks a link or tries the product.
2. **Be transparent.** If you built it, say you built it. If you work for the company, say so.
3. **Engage genuinely.** Respond to criticism honestly. Do not get defensive. Do not astroturf.
4. **Never fake grassroots enthusiasm.** No "I just discovered this amazing tool" when you are the founder.
5. **Respect the subreddit's self-promotion rules.** If the subreddit says no self-promotion, do not self-promote.

---

## Subreddit Profiles

Pre-built culture guides for common subreddits are available in `subreddit-profiles/`:

| Profile | Subreddit |
|---|---|
| `r-programming.md` | r/programming |
| `r-python.md` | r/python |
| `r-devops.md` | r/devops |
| `r-selfhosted.md` | r/selfhosted |

For subreddits without a profile, follow the subreddit research protocol above.

---

## Reddit Voice Adaptation

Regardless of brand voice, Reddit content must:

- Sound like a real person, not a brand
- Use the subreddit's vocabulary and tone
- Match the community's level of formality (r/programming is different from r/ProgrammerHumor)
- Never use marketing language, superlatives, or corporate framing
- Be direct. Reddit rewards brevity and clarity.
- Admit what you do not know. Reddit respects intellectual honesty.

---

## Formatting for Reddit

Reddit uses Markdown. Key formatting tips:

- Use headers sparingly (one or two per post, not a header for every paragraph)
- Use bullet lists for technical specs, features, or comparisons
- Use code blocks for code (triple backticks or 4-space indent)
- Bold key terms if the post is long, to aid scanning
- Keep paragraphs short -- Reddit is often read on mobile
- TL;DR at the top or bottom for longer posts

---

## Output Checklist

Before delivering a Reddit post:

- [ ] Target subreddit is identified and its rules are followed
- [ ] Post type matches the content and the subreddit's norms
- [ ] Tone matches the subreddit's culture (not generic internet voice)
- [ ] Zero marketing language or promotional framing
- [ ] If self-promotional: transparency is explicit and anti-shill rules are followed
- [ ] Post adds genuine value to the community
- [ ] Formatting uses Reddit Markdown correctly
- [ ] Title is descriptive (not clickbait, not vague)
- [ ] If the post is long, a TL;DR is included
- [ ] The poster sounds like a community member, not a brand ambassador
