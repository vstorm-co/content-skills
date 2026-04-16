# Anti-Slop Guide for Blog Posts

Slop is generic, filler-laden writing that sounds like it was produced on autopilot. Every draft must be checked against this list before delivery. If a pattern appears, rewrite it.

---

## Opening Cliches

**Avoid these openers:**

| Slop Pattern | Why It Fails |
|---|---|
| "Let's dive in" | Overused, adds nothing, delays the actual content |
| "In today's fast-paced world" | Vague, cliched, could introduce any topic |
| "Have you ever wondered..." | Rhetorical question that nobody actually wonders |
| "In the ever-evolving landscape of..." | Corporate throat-clearing |
| "It's no secret that..." | If it's no secret, skip the preamble |
| "Whether you're a beginner or expert..." | Tries to address everyone, resonates with no one |
| "In this article, we will..." | Tells instead of shows; readers can see the headings |
| "As we all know..." | Presumptuous and adds zero value |

**Do this instead:**
- Start with a specific observation: "Last Tuesday, our deploy script deleted the production database."
- Start with a surprising fact: "The average blog post takes 4 hours to write. The average reader spends 37 seconds on it."
- Start with a bold claim: "Most API rate-limiting strategies are wrong."
- Start with a micro-story: "Three months into the migration, the team realized they'd been solving the wrong problem."

---

## Closing Cliches

**Avoid:**
- "In conclusion..."
- "To sum up..."
- "And there you have it!"
- "So what are you waiting for?"
- "Happy coding!"
- "I hope this was helpful"

**Do this instead:**
- End with a forward-looking insight: what comes next, what this means for the future
- Callback to the opening story or claim
- A specific, actionable CTA: "Clone the repo and run the benchmark yourself"
- A provocative question that extends the reader's thinking

---

## Em-Dash Abuse

One or two em-dashes per post is fine. More than that signals autopilot writing.

**Signs of abuse:**
- Multiple em-dashes in the same paragraph
- Using em-dashes where a period or comma works better
- Every aside wrapped in em-dashes instead of using parentheses or separate sentences

**Fix:** Replace most em-dashes with periods (for strong breaks) or commas (for light pauses). Reserve em-dashes for moments that genuinely need a dramatic pause.

---

## Uniform Paragraph Length

If every paragraph is 3-4 sentences long, the post reads like a textbook. Monotonous rhythm loses readers.

**Fix:**
- Mix 1-sentence paragraphs (for emphasis) with longer explanatory paragraphs
- Use a short paragraph after a complex one to let the reader breathe
- Occasionally use a 2-word or single-phrase paragraph for impact

---

## Generic Metaphors and Buzzwords

**Avoid:**

| Buzzword | What to Write Instead |
|---|---|
| "game-changer" | Describe the specific change and its magnitude |
| "paradigm shift" | Name the old way and the new way concretely |
| "unlock" (as in "unlock potential") | Describe what becomes possible and how |
| "leverage" (as a verb) | "use," "apply," "build on" |
| "empower" | Describe what the person can now do |
| "robust" | Describe what makes it reliable (test coverage, failure handling, etc.) |
| "seamless" | Describe the actual user experience |
| "cutting-edge" | Name the specific technology or technique |
| "best-in-class" | Compared to what? Show the comparison. |
| "holistic" | Describe the specific scope |
| "synergy" | Describe what the combination produces |
| "ecosystem" (when vague) | Name the specific tools, services, or components |
| "at scale" (without numbers) | Give the actual numbers |

**Rule of thumb:** If you can swap the buzzword into a different article about a different topic and it still makes sense, it's too vague. Replace it with specifics.

---

## Filler Phrases

These phrases add words without adding meaning. Delete them.

| Filler | Fix |
|---|---|
| "It's worth noting that..." | Just state the thing. |
| "At the end of the day..." | Delete it entirely. |
| "It goes without saying..." | Then don't say it. |
| "Needless to say..." | Same. |
| "As a matter of fact..." | Just state the fact. |
| "In order to..." | "To..." |
| "Due to the fact that..." | "Because..." |
| "It is important to note that..." | Delete and state the important thing directly. |
| "When it comes to..." | Name the thing directly. |
| "The reality is that..." | State the reality. |
| "For all intents and purposes..." | Delete. |
| "At this point in time..." | "Now..." or delete. |

---

## Passive Voice Overuse

Passive voice is not always wrong, but overuse makes writing feel evasive and dull.

**Signs of overuse:**
- More than 20% of sentences use passive construction
- The reader cannot tell who is doing the action
- Sentences feel unnecessarily long

**Common passive patterns to rewrite:**
- "The function was called by the server" --> "The server called the function"
- "It was decided that..." --> "The team decided..." or "We decided..."
- "Improvements were made" --> "We improved X by doing Y"

**When passive is fine:**
- The actor is genuinely unknown: "The server was compromised at 3am"
- The object is more important than the actor: "The vulnerability was patched within two hours"

---

## Missing Specifics

Vague claims without evidence are the hallmark of low-quality content.

**Avoid:**
- "Many companies are adopting..." (How many? Which ones?)
- "This approach is faster..." (By how much? Measured how?)
- "Developers love this tool..." (Which developers? What did they say?)
- "It significantly reduces..." (By what percentage?)
- "Studies show..." (Which studies? Link them.)

**Fix:** Every claim needs at least one of:
- A number or measurement
- A named example
- A citation or link
- A personal experience with specific details

---

## The Self-Check Process

After writing a draft, scan for these in order:

1. Read the first paragraph. Does it earn attention or waste it?
2. Search for every em-dash. Are there more than two? Rewrite.
3. Check paragraph lengths. Do they vary?
4. Ctrl+F for every buzzword in the list above. Replace with specifics.
5. Ctrl+F for every filler phrase. Delete.
6. Count passive-voice sentences. If over 20%, rewrite the worst offenders.
7. For every claim, ask: "What's the evidence?" If there is none, add it or cut the claim.
8. Read the closing. Does it land or fizzle?
