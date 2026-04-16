---
name: content-calendar
description: Editorial calendar planning and content scheduling. Use when user wants to plan a content calendar, create a publishing schedule, organize content across platforms, or plan a content series.
---

# Editorial Calendar Planning

## Before You Start

1. **Check for brand context**: Read `brand/VOICE.md` if it exists. Calendar planning should align content themes with brand pillars. If the user has already run the content-strategy skill, reference the content pillars and briefs from that output.

2. **Determine the calendar type**: Ask the user (or infer from their prompt) what kind of planning they need:
   - **Monthly Calendar** -- a full month of content planned across platforms (`templates/monthly-calendar.md.template`)
   - **Campaign Plan** -- a focused burst of content around a single theme, launch, or event (`templates/campaign-plan.md.template`)
   - **Content Series** -- a connected sequence of content pieces published over time (`templates/content-series.md.template`)

3. **Gather inputs**: Platforms the user publishes on, existing content pillars, any fixed dates (launches, events, holidays), production capacity (how much content per week is realistic), and current content pipeline.

---

## Planning Flow

### Stage 1: Context Gathering

Understand the constraints before scheduling anything:

- **Platforms**: Which platforms does the user publish on? Each has different cadence norms. See `cadence-guide.md`.
- **Capacity**: How many pieces per week can the team realistically produce? Be honest -- overplanning leads to burnout and abandoned calendars.
- **Pillars**: What content pillars exist? Reference `brand/BRAND.md` or the output of the content-strategy skill if available. If no pillars are defined, suggest 3-5 based on the user's context.
- **Fixed dates**: Product launches, conferences, holidays, seasonal events, industry milestones.
- **Existing pipeline**: Content already in progress, scheduled, or published recently. Avoid redundancy.

### Stage 2: Cadence Design

Set the publishing cadence for each platform based on:

1. **Platform norms**: See `cadence-guide.md` for recommended frequencies.
2. **Team capacity**: Never exceed what the team can sustain. A calendar that collapses after two weeks is worse than a modest calendar maintained for six months.
3. **Content quality threshold**: Reduce cadence before reducing quality. One great post per week beats five mediocre posts.
4. **Audience expectations**: If you have trained your audience to expect a weekly newsletter, do not suddenly go monthly.

Recommended starting cadences for a solo creator or small team:

| Platform | Minimum Viable Cadence | Ideal Cadence |
|---|---|---|
| Blog | 1/week | 2/week |
| X / Twitter | 3/week | 1-2/day |
| LinkedIn | 2/week | 4-5/week |
| Newsletter | 1/every two weeks | 1/week |
| YouTube | 1/every two weeks | 1/week |
| Reddit | 1/week | 2-3/week |

### Stage 3: Topic Mapping

Assign topics to calendar slots:

1. **Map pillars to weeks**: Rotate through content pillars so no single pillar dominates. A simple rotation (Pillar A, B, C, A, B, C...) works for three pillars.
2. **Assign formats per platform**: The same topic can appear on multiple platforms in different formats. A blog post might become a thread, a LinkedIn post, and a newsletter section.
3. **Anchor content first**: Schedule your highest-effort content first (blog posts, videos, newsletter features). Then fill in lighter formats (threads, LinkedIn posts) that can be derived from or complement the anchor content.
4. **Leave buffer slots**: Mark 10-20% of calendar slots as "flex" for reactive content (responding to news, trends, or community conversations).

### Stage 4: Calendar Assembly

Build the calendar using the appropriate template:

- **Monthly calendar**: Use `templates/monthly-calendar.md.template`. Week-by-week view with columns for date, platform, format, topic, pillar, status, and notes.
- **Campaign plan**: Use `templates/campaign-plan.md.template`. Timeline view with phases, content pieces per phase, and coordinated multi-platform execution.
- **Content series**: Use `templates/content-series.md.template`. Sequential view showing how individual pieces connect, with consistent cadence and a connecting thread.

### Stage 5: Review and Adjust

Review the assembled calendar for:

- **Pillar balance**: Is any pillar over- or under-represented?
- **Format variety**: Are you using the same format too often? Mix blog posts, threads, videos, images.
- **Pacing**: Is there a natural rhythm? Avoid publishing three heavy pieces in a row followed by nothing.
- **Dependencies**: If a LinkedIn post references a blog post, is the blog scheduled first?
- **Realistic workload**: Can the team actually produce this? Be ruthlessly honest.

---

## Multi-Platform Coordination

When the same theme appears across platforms, adapt it for each platform's norms:

| Platform | Adaptation |
|---|---|
| Blog | Full-depth treatment with structure, examples, and detail |
| X / Twitter | Extract the sharpest insight as a hook. Thread for more depth. |
| LinkedIn | Professional framing, personal perspective, lesson-oriented |
| Newsletter | Curated summary with personal commentary and links |
| YouTube | Visual treatment, demo or walkthrough format |
| Reddit | Community-first framing, practical value, avoid self-promotion tone |

The key principle: **Same theme, different treatment.** Never copy-paste the same text across platforms. Each platform's audience expects content that feels native.

---

## Calendar Statuses

Use these status labels for tracking:

| Status | Meaning |
|---|---|
| `idea` | Topic identified, no brief yet |
| `briefed` | Content brief is written |
| `in-progress` | Draft is being written |
| `review` | Draft is complete, being reviewed |
| `scheduled` | Final version ready, publication date set |
| `published` | Live |
| `flex` | Slot reserved for reactive/timely content |

---

## Integration with Other Skills

This skill coordinates with the broader content system:

| Need | Skill |
|---|---|
| Define content pillars | `/content strategy` |
| Write a blog post from the calendar | `/content blog` |
| Write a thread from the calendar | `/content twitter` |
| Write a LinkedIn post from the calendar | `/content linkedin` |
| Create a video from the calendar | `/content video` |
| Repurpose one piece into multiple formats | `/content repurpose` |
| Audit a piece before publishing | `/content audit` |

---

## Output Checklist

Before delivering the calendar, verify:

- [ ] Calendar format matches the user's need (monthly, campaign, or series)
- [ ] Publishing cadence is realistic for the team's capacity
- [ ] Content pillars are balanced across the calendar period
- [ ] Formats are varied (not all blog posts or all threads)
- [ ] Fixed dates (launches, events) are accounted for
- [ ] Multi-platform content is adapted per platform, not copy-pasted
- [ ] 10-20% of slots are reserved as flex for reactive content
- [ ] Dependencies between pieces are sequenced correctly
- [ ] Every slot has enough detail (topic, format, pillar, platform) for someone to write a brief
- [ ] Calendar is deliverable as a clean markdown table or structured document
