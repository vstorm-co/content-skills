# Pattern: Blog Post to X Thread

## When to Use

The source is a blog post (800-3500 words) and the target is an X/Twitter thread (5-15 tweets).

---

## Transformation Steps

### Step 1: Identify the Hook

The thread hook is NOT the blog's introduction. Find the single most surprising, counterintuitive, or valuable insight in the post. That becomes tweet #1.

Good hooks:
- A surprising statistic or data point
- A contrarian claim
- A bold statement that challenges conventional wisdom
- A question that the audience will want answered
- A "most people think X, but actually Y" framing

Bad hooks:
- "I wrote a blog post about X" (no one cares about your blog post; they care about the insight)
- The blog's first paragraph copy-pasted
- A vague "here's what I learned" without specifics

### Step 2: Extract Key Points

From the blog post, extract 4-10 key points. Each will become 1-2 tweets. Criteria for a good thread point:

- It can stand alone as a useful insight
- It is specific (includes a number, example, or concrete detail)
- It builds on the previous point OR introduces a new facet of the topic
- It is not just filler connecting two better points

### Step 3: Structure the Thread

```
Tweet 1: HOOK -- the sharpest insight or most provocative claim
Tweet 2: Context -- why this matters or what prompted this
Tweet 3-N: Key points -- one per tweet, each building or adding a new dimension
Tweet N-1: The "so what" -- practical takeaway or implication
Tweet N: CTA -- link to the blog, ask a question, invite engagement
```

### Step 4: Write Each Tweet

For each tweet:
- Lead with the point, not the setup
- Use concrete numbers and examples
- One idea per tweet (two maximum)
- Vary tweet length: some short and punchy, some that use the full 280 characters
- Use line breaks for readability in longer tweets
- No hashtags mid-thread (one or two in the final tweet is fine)

### Step 5: Add Thread Mechanics

- Number tweets if the thread is longer than 7 tweets (e.g., "1/12")
- The final tweet should reference tweet 1 or the overall thread for retweet-ability
- Consider adding a "bookmark this" suggestion if the thread is reference material
- Include the blog link in the final tweet for people who want the full version

---

## Example Transformation

**Blog excerpt** (from a post about API rate limiting):
> "Most API rate limiting implementations use a simple counter that resets every minute. This works fine at low scale, but breaks down when you have bursty traffic patterns. The token bucket algorithm solves this by allowing short bursts while maintaining an average rate limit over time. We switched from fixed-window to token bucket and saw our 429 error rate drop by 73%."

**Thread version**:

Tweet 1:
"We reduced our API 429 errors by 73% with one change to our rate limiter.

Here's what most teams get wrong about rate limiting (and how to fix it):"

Tweet 2:
"The default approach: count requests per minute, reject when the count exceeds the limit, reset the counter.

This works fine... until your traffic gets bursty.

Then legitimate users start hitting 429s during normal usage spikes."

Tweet 3:
"The fix: token bucket algorithm.

Instead of a hard counter, you have a bucket that fills with tokens at a steady rate. Each request consumes a token.

Short bursts are fine (bucket has reserves). Sustained overuse gets limited.

Simple concept, dramatic improvement."

Tweet 4:
"Our results after switching:
- 429 errors: down 73%
- P99 latency: unchanged
- Implementation time: ~2 hours
- Lines of code: fewer than the fixed-window version

Full breakdown in the blog post: [link]"

---

## Common Mistakes

1. **Summarizing instead of extracting**: A thread is not a summary. It is a curated selection of the strongest points, restructured for the platform.
2. **Same hook as the blog**: The blog's opening was written for long-form readers. Thread readers need a faster, punchier hook.
3. **Too many tweets**: A 20-tweet thread loses most readers. 5-12 is the sweet spot.
4. **No standalone value**: If the thread only makes sense after reading the blog, it has failed. The thread must deliver value independently.
5. **Forgetting the link**: Always include the blog link in the final tweet for people who want more depth.
