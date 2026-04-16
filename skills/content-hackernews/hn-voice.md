# Hacker News Voice Guide

This document defines the voice and tone for all Hacker News content. HN has the most specific and unforgiving voice requirements of any platform. Deviation from these norms will get your content flagged, downvoted, or ignored.

---

## The HN Voice in Three Words

**Direct. Technical. Honest.**

---

## Principle 1: Be Direct

Say what you mean in the fewest words possible. HN readers are scanning. Respect their time.

**Do:**
- "It parses SQL schemas and generates migration scripts."
- "We reduced cold start time from 12s to 400ms."
- "The main limitation is that it only supports PostgreSQL."

**Do not:**
- "We're excited to introduce a powerful new tool that helps developers streamline their database migration workflow."
- "After months of hard work, we're thrilled to share what we've been building."
- "We believe our approach has the potential to significantly improve the developer experience."

**Test:** Read your sentence. Can you remove any words without changing the meaning? If yes, remove them.

---

## Principle 2: Be Technical

HN readers are technically sophisticated. Write for them, not for a marketing persona.

**Do:**
- Include architecture details: "Written in Rust, uses a custom B-tree variant for the index."
- Share benchmarks with methodology: "On a 10M row table, it generates diffs in 2.3s (measured on an M2 MacBook Pro with 16GB RAM)."
- Name specific technologies: "We use libpq for PostgreSQL connections and go-sqlite3 for the local cache."
- Explain trade-offs: "We chose eventual consistency over strong consistency because the latency penalty for our use case was unacceptable."

**Do not:**
- Use vague technical language: "Built with cutting-edge technology."
- Hide behind abstractions: "Uses advanced algorithms."
- Overstate: "Blazingly fast." (Show the benchmark instead.)

---

## Principle 3: Be Honest About Limitations

Honesty about what your project cannot do earns more respect on HN than any feature list.

**Do:**
- "It doesn't handle circular foreign keys yet. That's the hardest remaining problem."
- "Performance degrades above 50M rows. We're working on it."
- "The documentation is incomplete. We prioritized the core functionality."
- "I'm not sure our approach scales beyond 10 concurrent users. I'd appreciate help testing."

**Do not:**
- Omit known limitations
- Downplay problems: "It works great for most use cases" (which ones?)
- Promise future fixes without timeline: "We'll add that soon" (when?)

**Why this works:** HN readers assume every project has limitations. When you do not mention them, they assume you are either unaware (bad) or hiding them (worse). Stating limitations explicitly signals competence and integrity.

---

## Principle 4: No Superlatives

Superlatives are marketing language. HN treats them as a credibility signal -- a negative one.

| Do Not Write | Write Instead |
|---|---|
| "The best CLI tool for..." | "A CLI tool for..." |
| "The fastest database..." | "Benchmarks at X queries/sec on Y hardware" |
| "The most powerful..." | Describe what makes it capable |
| "The easiest way to..." | "Requires 3 commands to set up" |
| "Revolutionary" | Describe what changed and why it matters |
| "Game-changing" | Describe the specific impact |
| "World-class" | Let the reader judge |

**Rule:** If an adjective describes quality rather than function, delete it. Let the technical details demonstrate quality.

---

## Principle 5: No Marketing Language

If a sentence could appear in a press release, startup pitch deck, or product landing page, rewrite it for HN.

**Marketing language patterns to avoid:**
- "We're on a mission to..." (just describe what you do)
- "Designed for teams who..." (describe the functionality)
- "Unlock the power of..." (describe what becomes possible)
- "Join thousands of developers who..." (social proof is marketing)
- "Free forever" / "No credit card required" (landing page copy)
- "Built by developers, for developers" (cliche)
- "From the team that brought you..." (self-referential marketing)

**HN-appropriate alternatives:**
- State what the tool does
- Show how it works
- Share what you learned building it
- Describe the technical approach
- Present honest performance data

---

## Principle 6: Show, Don't Tell

Instead of claiming a quality, demonstrate it.

| Telling | Showing |
|---|---|
| "It's really fast" | "Parses 1GB of logs in 3.2 seconds" |
| "It's easy to use" | "Install: `brew install tool`. Run: `tool scan .`" |
| "Developers love it" | "200 stars on GitHub in the first week, 45 issues filed" |
| "It's reliable" | "99.97% uptime over 6 months, zero data loss incidents" |
| "It handles scale" | "Currently processing 2M events/day in production" |

---

## Comment Tone

When responding to comments on HN:

**Do:**
- Be substantive. Add information, not just agreement.
- Engage with criticism constructively. "That's a fair point. Here's why we made that trade-off..."
- Ask genuine follow-up questions. "Interesting -- can you say more about how you handle that case?"
- Credit good ideas: "I hadn't considered that approach. I'll look into it."

**Do not:**
- Post empty pleasantries: "Thanks for the feedback!" (add substance)
- Get defensive: "You clearly don't understand what we're building."
- Redirect to your docs/site: "Check our FAQ for that." (answer in the thread)
- Post one-word replies: "Agreed." "This." "Exactly."

---

## Voice Self-Check

Before posting to HN, read your content and ask:

1. Would a senior engineer at a top tech company take this seriously? (If not, add rigor.)
2. Does any sentence sound like it could be on a product landing page? (If yes, rewrite.)
3. Have I made any claims without evidence? (If yes, add evidence or remove the claim.)
4. Am I being honest about limitations? (If not, add them.)
5. Would I be comfortable defending every sentence in a technical discussion? (If not, soften or substantiate.)
