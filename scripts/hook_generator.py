#!/usr/bin/env python3
"""Generate hook variations for a given topic.

Produces 10 hook variations using different rhetorical patterns:
curiosity gap, bold claim, statistic, story, question, and contrarian.

Usage:
    python scripts/hook_generator.py "Why static types matter"
    python scripts/hook_generator.py "API rate limiting" --count 15
"""

import argparse
import json
import sys
import textwrap


# Hook pattern templates. Each pattern has a name, description, and
# template strings with {topic} placeholder.
HOOK_PATTERNS = [
    {
        "name": "curiosity_gap",
        "description": "Creates an information gap the reader wants to close",
        "templates": [
            "Most people get {topic} completely wrong. Here is what they miss.",
            "There is a counterintuitive truth about {topic} that changes how you approach it.",
            "The biggest misconception about {topic} is one you probably believe right now.",
        ],
    },
    {
        "name": "bold_claim",
        "description": "Opens with a strong, arguable assertion",
        "templates": [
            "{topic} is not what you think it is. It is [specific reframe].",
            "If you are still [common approach to topic], you are wasting your time.",
            "The conventional wisdom about {topic} is dead wrong.",
        ],
    },
    {
        "name": "statistic",
        "description": "Leads with a specific, surprising number",
        "templates": [
            "[X%] of teams get {topic} wrong on the first try. The fix takes [time].",
            "We spent [X hours/days] on {topic} before realizing [insight]. Here is the shortcut.",
        ],
    },
    {
        "name": "story",
        "description": "Opens with a brief narrative or anecdote",
        "templates": [
            "Last [time period], we [specific event related to topic]. What happened next changed our approach to {topic} entirely.",
            "Three months into [project], the team discovered that their approach to {topic} had been solving the wrong problem.",
        ],
    },
    {
        "name": "question",
        "description": "Poses a specific, non-rhetorical question",
        "templates": [
            "What happens when {topic} fails at the worst possible moment?",
            "Why do experienced teams still struggle with {topic}?",
        ],
    },
    {
        "name": "contrarian",
        "description": "Takes the opposite position from consensus",
        "templates": [
            "Everyone says you need {topic}. I am not so sure.",
            "Unpopular opinion: the way most people think about {topic} causes more problems than it solves.",
            "The best approach to {topic} might be to stop doing it altogether.",
        ],
    },
    {
        "name": "before_after",
        "description": "Contrasts the old way with the new way",
        "templates": [
            "Before we figured out {topic}, [pain]. After, [result].",
        ],
    },
    {
        "name": "direct_value",
        "description": "Leads with the concrete benefit to the reader",
        "templates": [
            "This approach to {topic} will save you [specific time/effort]. No caveats.",
            "Here is how to get {topic} right in [specific timeframe], even if you have tried and failed before.",
        ],
    },
]


def generate_hooks(topic: str, count: int = 10) -> list[dict]:
    """Generate hook variations for a topic.

    Cycles through patterns and templates to produce the requested number
    of hooks. Returns a list of dicts with pattern name, hook text, and
    editing guidance.
    """
    hooks = []
    template_index = 0

    # Flatten all templates with their pattern info
    all_templates = []
    for pattern in HOOK_PATTERNS:
        for template in pattern["templates"]:
            all_templates.append(
                {
                    "pattern": pattern["name"],
                    "description": pattern["description"],
                    "template": template,
                }
            )

    # Generate hooks cycling through templates
    for i in range(count):
        entry = all_templates[i % len(all_templates)]
        hook_text = entry["template"].replace("{topic}", topic)

        hooks.append(
            {
                "number": i + 1,
                "pattern": entry["pattern"],
                "pattern_description": entry["description"],
                "hook": hook_text,
                "editing_notes": _get_editing_notes(entry["pattern"], hook_text),
            }
        )

    return hooks


def _get_editing_notes(pattern: str, hook: str) -> str:
    """Provide editing guidance for a hook."""
    notes = {
        "curiosity_gap": "Replace the vague promise with a specific detail from your content. The gap must be worth closing.",
        "bold_claim": "Fill in the [specific reframe] with your actual argument. The claim must be defensible.",
        "statistic": "Replace [X%], [X hours/days], and [insight] with real numbers from your experience or research.",
        "story": "Replace [time period], [specific event], and [project] with your actual story. Real details make this pattern work.",
        "question": "Make sure this question has a non-obvious answer. If the reader can guess the answer, it is not a good hook.",
        "contrarian": "This only works if you have genuine evidence against the consensus. Do not be contrarian for shock value.",
        "before_after": "Replace [pain] and [result] with specific, measurable outcomes.",
        "direct_value": "Replace [specific time/effort] and [specific timeframe] with real numbers. Vague promises kill this pattern.",
    }
    return notes.get(pattern, "Customize the bracketed placeholders with specifics from your content.")


def main():
    parser = argparse.ArgumentParser(
        description="Generate hook variations for a given topic."
    )
    parser.add_argument("topic", help="The topic to generate hooks for")
    parser.add_argument(
        "--count",
        "-n",
        type=int,
        default=10,
        help="Number of hooks to generate (default: 10)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print formatted output to stderr"
    )

    args = parser.parse_args()
    hooks = generate_hooks(args.topic, args.count)

    output = {
        "topic": args.topic,
        "count": len(hooks),
        "hooks": hooks,
    }

    print(json.dumps(output, indent=2))

    if args.verbose:
        print(f"\n--- Hook Variations for: {args.topic} ---", file=sys.stderr)
        for hook in hooks:
            print(f"\n{hook['number']}. [{hook['pattern']}]", file=sys.stderr)
            wrapped = textwrap.fill(hook["hook"], width=72, initial_indent="   ", subsequent_indent="   ")
            print(wrapped, file=sys.stderr)
            note = textwrap.fill(
                f"Note: {hook['editing_notes']}",
                width=72,
                initial_indent="   ",
                subsequent_indent="   ",
            )
            print(note, file=sys.stderr)


if __name__ == "__main__":
    main()
