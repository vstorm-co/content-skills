---
name: content-strategy
description: Content strategy, ideation, positioning, and editorial direction. Use when user wants to plan content strategy, generate content ideas, define content pillars, create a content brief, or develop editorial positioning.
---

# Content Strategy & Ideation

## Before You Start

1. **Check for existing brand context**: Read `brand/VOICE.md` and `brand/VISUAL.md` if they exist. Strategy work must align with the established brand identity. If no brand files exist, the strategy phase is a good time to define them -- suggest the user run content-setup first, or build foundational voice/visual decisions into the strategy output.

2. **Understand the distinction between strategy and tactics**:
   - **Strategy** answers: Who are we talking to? What do we want them to think/feel/do? What is our unique position? What themes define our content?
   - **Tactics** answer: What specific pieces do we publish? When? Where? In what format?
   - This skill handles strategy first, then translates it into tactical briefs that other skills (content-blog, content-twitter, content-video, etc.) can execute.

3. **Gather context**: Before strategizing, you need to understand the user's situation. Use the questions in `questions.md` as a starting framework. Not every question applies to every situation -- use judgment about which to ask and which to infer.

---

## Ideation Flow

Follow these four stages in order. Each stage builds on the previous one.

### Stage 1: Audience Analysis

Define who the content is for. Use the audience persona framework from `frameworks/audience-persona.md`.

For each target audience segment, document:

- **Demographics**: Role, seniority, company size, industry
- **Psychographics**: Values, beliefs, worldview, identity markers
- **Information diet**: Where do they currently get information? Who do they follow? What formats do they prefer?
- **Pain points**: What problems keep them up at night? What frustrates them about existing solutions or content?
- **Aspirations**: What do they want to become or achieve? What does success look like for them?
- **Current beliefs**: What do they already believe about your topic? What misconceptions exist?
- **Desired beliefs**: What should they believe after consuming your content?

The gap between current beliefs and desired beliefs is where your content strategy lives.

### Stage 2: Pillar Definition

Define 3-5 content pillars using the framework in `frameworks/content-pillar-model.md`. Each pillar is a core theme that:

- Aligns with the brand's expertise and authority
- Addresses a real audience need or interest
- Is broad enough to sustain dozens of content pieces
- Is specific enough to differentiate from competitors
- Connects to the brand's product, service, or mission

For each pillar, document:

- **Pillar name**: A clear, memorable label
- **Why it matters**: To the audience and to the brand
- **Core thesis**: The central argument or perspective the brand brings to this theme
- **Example topics**: 5-10 specific content ideas that fall under this pillar
- **Interconnections**: How this pillar relates to the other pillars

### Stage 3: Idea Generation

Generate specific content ideas organized by pillar. For each idea, capture:

- **Working title**: A specific, compelling title (not generic)
- **Pillar**: Which content pillar it belongs to
- **Format**: Blog, thread, video, newsletter, LinkedIn post, etc.
- **Angle**: What makes this take unique or interesting
- **JTBD**: What job does the audience hire this content to do? (See `frameworks/jobs-to-be-done.md`)
- **Key points**: 3-5 main arguments or sections
- **Effort**: Low / Medium / High
- **Priority**: Must-have / Nice-to-have / Backlog

Aim for 3-5 ideas per pillar in the initial brainstorm. Prioritize ideas that:

- Address the belief gap identified in Stage 1
- Can be executed with available resources
- Have clear distribution channels
- Can be repurposed across multiple formats

### Stage 4: Brief Creation

For each prioritized idea, create a structured content brief that can be handed off to an execution skill. The brief format:

```
## Content Brief: [Working Title]

**Pillar**: [Content pillar]
**Format**: [Blog / Thread / Video / Newsletter / etc.]
**Target audience**: [Specific segment from Stage 1]
**Goal**: [What should the reader think, feel, or do after consuming this?]

**Angle / Hook**:
[One paragraph describing the unique angle and why someone would click/read/watch]

**Key Points**:
1. [First key argument or section]
2. [Second key argument or section]
3. [Third key argument or section]

**Evidence / Examples**:
- [Data point, case study, or example to include]
- [Another supporting element]

**CTA**:
[What action should the audience take after consuming this content?]

**Distribution Plan**:
- Primary: [Main platform/channel]
- Repurpose: [Secondary formats -- e.g., "Extract 3 tweets, 1 LinkedIn post"]

**Success Metrics**:
- [How will you know this content worked?]

**Notes for Writer**:
- [Voice/tone guidance specific to this piece]
- [Things to avoid]
- [References or inspiration]
```

---

## Frameworks Reference

This skill includes three strategic frameworks in the `frameworks/` directory:

| Framework | When to Use | File |
|---|---|---|
| Jobs to Be Done | Understanding why audiences consume content | `frameworks/jobs-to-be-done.md` |
| Audience Persona | Defining target audience segments | `frameworks/audience-persona.md` |
| Content Pillar Model | Organizing content into strategic themes | `frameworks/content-pillar-model.md` |

Use one or more frameworks depending on the user's needs. Not every engagement requires all three.

---

## Strategy vs. Execution

This skill produces strategy and briefs. It does not produce finished content. The output of this skill feeds into execution skills:

| Output | Feeds Into |
|---|---|
| Blog brief | `/content blog` |
| Thread brief | `/content twitter` |
| Video brief | `/content video` |
| LinkedIn brief | `/content linkedin` |
| Presentation brief | `/content presentation` |
| Calendar plan | `/content calendar` |

When handing off a brief, include enough context that the execution skill can work independently -- the brief should be self-contained.

---

## Anti-Patterns to Avoid

When developing strategy, watch for these common failures:

1. **Strategy without specificity**: "We should create thought leadership content" is not a strategy. Name the audience, the angle, and the differentiation.
2. **Pillar sprawl**: More than 5 pillars means you have not made hard choices. Three focused pillars beat seven vague ones.
3. **Audience of everyone**: If your target audience is "developers," narrow it. Which developers? What experience level? What domain?
4. **Ideas without angles**: "Write a blog about Kubernetes" is a topic, not an idea. "Why your Kubernetes cluster is wasting 40% of your compute budget" is an idea.
5. **Ignoring distribution**: A content strategy without a distribution plan is a content graveyard. Every piece needs a specific path to its audience.
6. **Copying competitors**: Strategy should find the gap, not fill the same space. Ask: "What is nobody else saying about this topic?"

---

## Output Checklist

Before delivering the strategy, verify:

- [ ] At least one audience segment is defined with specifics (not generic)
- [ ] Belief gap is identified (current beliefs vs. desired beliefs)
- [ ] 3-5 content pillars are defined with clear theses
- [ ] Each pillar has 3-5 specific content ideas
- [ ] Priority ideas have full content briefs
- [ ] Distribution plan exists for each brief
- [ ] Strategy clearly differentiates from what competitors are publishing
- [ ] All frameworks used are referenced with specific findings
- [ ] Output is actionable -- another skill or human can execute it immediately
