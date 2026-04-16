# Presentation Narrative Structure

How to build a compelling narrative arc for presentations. This is not about slide design -- it is about the story your deck tells.

---

## The Core Arc: Hook-Problem-Solution-Evidence-CTA

Every presentation, regardless of type, follows a tension-release pattern. The audience should feel uncomfortable before you offer relief.

### Hook

The first 30 seconds determine whether the audience pays attention. The hook creates a gap -- something unresolved that demands closure.

**Effective hooks**:
- **A surprising stat**: "73% of deploys that pass CI fail in production within a week."
- **A provocative question**: "What if everything you believe about customer retention is wrong?"
- **A relatable scenario**: "It is 2am. Your phone buzzes. The dashboard is red."
- **A bold claim**: "You can cut your infrastructure costs by half without reducing reliability."
- **A contradiction**: "The more features you ship, the fewer customers you keep."

**Ineffective hooks**:
- "Today I am going to talk about..." (This is a table of contents, not a hook.)
- "My name is X and I work at Y." (Save introductions for after you have earned attention.)
- "Let's dive in!" (Empty filler. Dive into what?)
- A joke unrelated to the topic. (Risks falling flat and wastes the opening.)

### Problem

After the hook, define the problem clearly. The audience should be nodding: "Yes, I have felt this."

**Keys**:
- Use the audience's language, not yours. If they call it "deployment pain," do not call it "release management challenges."
- Be specific. "It takes 3 weeks to ship a one-line change" beats "development velocity is slow."
- Quantify the cost. Time, money, opportunity, morale.
- Do not rush this. The audience needs to feel the weight of the problem before they will value your solution.

### Solution

Present your answer. This is where you pivot from tension to relief.

**Keys**:
- Lead with the outcome, not the mechanism. "You will deploy in minutes, not weeks" before "We use a blue-green deployment pipeline with automated canary analysis."
- Show, do not tell. A screenshot, demo, or walkthrough beats a description.
- Match the solution to the problem. Every problem point from the previous section should have a corresponding solution point.
- Do not oversell. Honest confidence is more persuasive than hype.

### Evidence

Back up your solution with proof. The audience is thinking "This sounds good, but does it actually work?"

**Types of evidence** (in order of persuasiveness):
1. **Live demo**: They see it work in real time.
2. **Customer results**: A specific company achieved a specific outcome.
3. **Data**: Aggregated metrics across users/deployments/experiments.
4. **Expert endorsement**: A respected voice vouches for the approach.
5. **Logical argument**: First principles reasoning (weakest, but necessary when other evidence is unavailable).

Use at least two types. A customer story plus data is a strong combination.

### CTA

End with one clear action. Not "here are five ways to get started." One.

**Effective CTAs**:
- "Open your laptop and run `npx create-thing` right now."
- "Email me at [address] and I will send you the template."
- "Go to [url] and start your free trial."
- "Talk to your team lead this week about trying [approach] on one project."

**Ineffective CTAs**:
- "Check out our website." (Too vague.)
- "Consider adopting this approach." (Too passive.)
- "Any questions?" (This is Q&A facilitation, not a CTA.)

---

## Tension and Release

Great presentations are not flat. They oscillate between tension (discomfort, curiosity, uncertainty) and release (answers, clarity, relief).

### Building Tension

- Present a problem without immediately solving it.
- Show data that challenges assumptions.
- Ask a question and pause before answering.
- Show a failure case before showing the fix.
- Use silence. A 3-second pause after a bold claim creates more tension than any animation.

### Releasing Tension

- Reveal the solution after the audience has sat with the problem.
- Show the "after" following a painful "before."
- Deliver the punchline of a story.
- Share the happy ending of a case study.

### The Rhythm

A 20-minute talk might have 3-4 tension-release cycles:

1. **Hook** (tension) -> Problem statement (more tension) -> Solution overview (release)
2. **Technical challenge 1** (tension) -> How we solved it (release)
3. **Technical challenge 2** (tension) -> How we solved it (release)
4. **The remaining risk** (tension) -> Evidence that it works anyway (release) -> CTA

Each cycle should escalate. The first tension is mild curiosity. By the third cycle, the audience is deeply invested.

---

## Pacing Guidance

### Time Allocation

| Deck Length | Hook/Problem | Solution | Evidence | CTA |
|---|---|---|---|---|
| 5 min (lightning talk) | 1 min | 2 min | 1.5 min | 30 sec |
| 20 min (conference talk) | 4 min | 8 min | 6 min | 2 min |
| 40 min (keynote) | 8 min | 16 min | 12 min | 4 min |

The solution section is always the largest. Spend proportionally more time on the problem as the talk gets shorter (in a lightning talk, if the audience does not feel the pain in 60 seconds, you have lost them).

### Slides Per Minute

- Dense slides (code, data, complex diagrams): 1 slide per 2-3 minutes
- Standard slides (title + key point): 1 slide per 1-2 minutes
- Impact slides (stat cards, big statements): 1 slide per 15-30 seconds
- Transition slides (section dividers): 1 slide per 5-10 seconds

A 20-minute talk with 30 slides is fine if many are impact or transition slides. A 20-minute talk with 30 dense slides means you are rushing.

---

## Adapting the Arc by Deck Type

### Pitch Deck
Compress the arc. Investors have seen 1000 pitches. Get to the point fast. Hook with the market opportunity, not a story. Evidence is traction data, not anecdotes.

### Sales Deck
Start with the buyer's world, not your product. The problem section should use their terminology. The solution is framed as a framework, not a feature list. Evidence is case studies with named customers.

### Conference Talk
You have permission to go deep. The teaching section (Solution) can include multiple technical concepts with code examples. Alternate between teaching and "why this matters" to maintain engagement.

### Workshop
The arc repeats for each exercise block: introduce concept (mini-hook), demonstrate (solution), hands-on exercise (evidence that they can do it), review. The overall workshop has a meta-arc from "you do not know this" to "you just built something real."

### Client Proposal
The problem section should quote the client's own words. The solution section is your methodology, not your company overview. Evidence is case studies from similar engagements. The CTA is "sign the SOW."

---

## Common Narrative Mistakes

1. **Starting with yourself**: "Let me tell you about our company..." Nobody cares about your company until they care about the problem you solve.

2. **Burying the lead**: Saving the key insight for slide 25 of 30. If the audience walks out at slide 15, they should still have the main idea.

3. **All tension, no release**: Problem after problem after problem, then a rushed solution at the end. Balance the weight.

4. **All release, no tension**: "Everything is great and here is why!" Without tension, the solution feels unnecessary.

5. **The data dump**: 15 slides of charts with no narrative thread. Data is evidence, not story. Wrap each data point in meaning.

6. **The feature parade**: Feature 1, Feature 2, Feature 3... Features are not narrative. They are evidence that supports a narrative about solving the problem.

7. **Ignoring the audience's internal monologue**: At every slide, the audience is thinking something. If Slide 5 shows a bold claim, the audience is thinking "prove it." If Slide 6 is another claim instead of proof, you have lost trust.
