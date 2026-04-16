# Voice & Tone Questions — Phase 2

These questions capture how the brand sounds when it writes. Voice is the personality; tone shifts by context but stays within the voice.

---

## Q1: Voices You Admire

**Ask:** "Name 2-3 brands, writers, or publications whose writing style you admire. They don't have to be in your industry."

**Probe:**
- "What specifically do you like about their writing? Is it the humor, the clarity, the authority, the warmth?"
- "If you could steal one thing from their style, what would it be?"
- "Is there a writer whose style you tried to imitate and it felt wrong? What didn't work?"

**Extract:** Named references with specific attributes admired. This gives Claude a calibration point.

---

## Q2: Formality Scale

**Ask:** "On a scale of 1 to 10, how formal should your writing be? Here's what each level sounds like:"

### The Formality Scale

| Level | Label | Example |
|---|---|---|
| 1 | Text to your best friend | "lol yeah just ship it, we'll fix it later" |
| 2 | Slack message to a coworker | "hey, can you take a look at this PR when you get a sec?" |
| 3 | Casual blog post | "So we broke production last week. Here's what happened and what we learned." |
| 4 | Friendly professional | "We recently shipped a major update. Here's what changed and why it matters for your workflow." |
| 5 | Standard business | "We're pleased to announce the release of version 3.0, which includes several significant improvements." |
| 6 | Polished professional | "Today we introduce version 3.0, representing a substantial advancement in our platform's capabilities." |
| 7 | Executive communication | "This quarter's release reflects our continued investment in platform reliability and developer experience." |
| 8 | Formal publication | "The latest iteration of the platform incorporates feedback from over 200 enterprise deployments." |
| 9 | Academic / legal | "The aforementioned release addresses compliance requirements pursuant to the updated regulatory framework." |
| 10 | Supreme Court brief | "Wherefore, the petitioner respectfully submits that the foregoing constitutes a material advancement." |

**Follow-ups:**
- "Does the level change depending on the platform? Maybe a 3 on Twitter and a 6 in whitepapers?"
- "Is there a level you never want to go below or above?"

**Extract:** A base formality level and any per-platform adjustments.

---

## Q3: Humor Style

**Ask:** "What role does humor play in your content?"

**Options to explore:**
- **None**: "We're serious. Our audience expects authority, not jokes."
- **Dry / deadpan**: Understated. The humor is in what you don't say.
- **Self-deprecating**: "We messed up, and here's the funny version of how."
- **Playful**: Light, energetic, uses wordplay and unexpected phrasing.
- **Absurdist**: Unexpected comparisons, surreal examples, breaks the fourth wall.
- **Situational**: Not trying to be funny, but acknowledges absurdity when it naturally arises.

**Probe:**
- "Can you think of a time humor in content worked well for you or a brand you follow?"
- "Is there a type of humor that would make your audience cringe?"
- "Would you ever use a meme in a blog post?"

**Extract:** Humor style label, boundaries, examples of humor that works and humor that does not.

---

## Q4: Favorite Phrases & Patterns

**Ask:** "Are there specific words or phrases your brand loves to use? Things that feel like 'you'?"

**Probe:**
- "Any signature sign-offs, greetings, or transitions?"
- "Words you use that your competitors don't?"
- "Is there a particular way you refer to your customers? (Users? Customers? Community? Builders? Makers?)"

**Extract:** Preferred vocabulary, signature phrases, customer terminology.

---

## Q5: Forbidden Words & Phrases

**Ask:** "Now the opposite. What words or phrases should never appear in your content?"

**Common triggers to explore:**
- Industry jargon they find pretentious ("leverage," "synergy," "disrupt")
- Competitor language they don't want to echo
- Overused marketing phrases ("game-changer," "revolutionary," "best-in-class")
- Words that misrepresent the brand ("cheap" vs. "affordable," "simple" vs. "easy")
- Gendered or exclusionary language

**Probe:**
- "If you saw one of these words in a draft, would you just change it or would you be actually upset?"
- "Are there words that are fine internally but should never face customers?"

**Extract:** Explicit ban list with context for why each word is banned. Severity level (mild preference vs. hard ban).

---

## Q6: Writing Samples (Optional)

**Ask:** "Do you have any existing writing that represents how you want to sound? Blog posts, emails, social posts, internal docs -- anything works."

**If yes:**
- Ask them to place 3-5 representative samples in `brand/voice-samples/`.
- The `/content voice` command will analyze these in detail.

**If no:**
- "That's fine. We'll build your voice from the answers you've given. You can always add samples later and run `/content voice` to refine."

**Extract:** Paths to sample files, or note that none exist yet.

---

## Synthesis: Voice Attributes

After this phase, Claude should be able to articulate the voice as 3-5 attributes, each on a spectrum:

**Format:** `[Attribute]: [Position on spectrum] — [Why]`

Examples:
- **Authority**: High -- this audience expects expertise, not hedging.
- **Warmth**: Medium -- friendly but not folksy. No "hey friend!" energy.
- **Directness**: Very high -- say what you mean in the fewest words.
- **Technical depth**: Moderate -- use terms the audience knows, define anything niche.
- **Playfulness**: Low-to-medium -- a well-placed joke is fine, forced humor is not.

These attributes become the backbone of `brand/VOICE.md`.
