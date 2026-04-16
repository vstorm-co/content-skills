#!/usr/bin/env python3
"""Analyze writing samples to extract a voice profile.

Reads text files from a directory, analyzes writing patterns, and
outputs a voice profile in VOICE.md format.

Usage:
    python scripts/voice_profile_learner.py brand/voice-samples/
    python scripts/voice_profile_learner.py samples/ --output brand/VOICE.md
"""

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path


def strip_markdown(text: str) -> str:
    """Remove markdown formatting for analysis."""
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"^---[\s\S]*?---\n", "", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", "", text)
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)
    text = re.sub(r"^\s*>\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
    return text.strip()


def read_samples(directory: str) -> list[dict]:
    """Read all text/markdown files from a directory."""
    dir_path = Path(directory)
    if not dir_path.exists():
        return []

    samples = []
    extensions = {".md", ".txt", ".markdown", ".rst", ".html"}

    for file in sorted(dir_path.iterdir()):
        if file.is_file() and file.suffix.lower() in extensions:
            try:
                text = file.read_text(encoding="utf-8")
                samples.append({"file": file.name, "text": text, "clean": strip_markdown(text)})
            except (UnicodeDecodeError, PermissionError):
                continue

    return samples


def analyze_sentence_patterns(texts: list[str]) -> dict:
    """Analyze sentence length and rhythm patterns."""
    all_sentence_lengths = []

    for text in texts:
        sentences = re.split(r"(?<=[.!?])\s+", text)
        for s in sentences:
            words = s.split()
            if len(words) >= 3:  # Skip fragments
                all_sentence_lengths.append(len(words))

    if not all_sentence_lengths:
        return {"avg_length": 0, "variation": "unknown", "rhythm": "unknown"}

    avg = sum(all_sentence_lengths) / len(all_sentence_lengths)
    variance = sum((l - avg) ** 2 for l in all_sentence_lengths) / len(all_sentence_lengths)
    std_dev = math.sqrt(variance)

    # Categorize rhythm
    if std_dev > 8:
        rhythm = "highly varied (punchy shorts mixed with flowing longs)"
    elif std_dev > 5:
        rhythm = "moderately varied (natural conversational rhythm)"
    elif std_dev > 3:
        rhythm = "somewhat uniform (steady but not monotonous)"
    else:
        rhythm = "very uniform (may feel robotic)"

    # Categorize length preference
    if avg > 20:
        length_pref = "long (academic/formal style)"
    elif avg > 15:
        length_pref = "medium-long (detailed, explanatory)"
    elif avg > 10:
        length_pref = "medium (conversational)"
    else:
        length_pref = "short (punchy, direct)"

    # Short sentence ratio (under 8 words)
    short_ratio = sum(1 for l in all_sentence_lengths if l < 8) / len(all_sentence_lengths)

    return {
        "avg_length": round(avg, 1),
        "std_dev": round(std_dev, 1),
        "min_length": min(all_sentence_lengths),
        "max_length": max(all_sentence_lengths),
        "rhythm": rhythm,
        "length_preference": length_pref,
        "short_sentence_ratio": round(short_ratio, 2),
        "total_sentences": len(all_sentence_lengths),
    }


def analyze_vocabulary(texts: list[str]) -> dict:
    """Analyze vocabulary frequency and complexity."""
    all_words = []
    for text in texts:
        words = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?\b", text.lower())
        all_words.extend(words)

    if not all_words:
        return {}

    freq = Counter(all_words)
    total = len(all_words)
    unique = len(set(all_words))
    ttr = unique / total

    # Vocabulary complexity: ratio of long words (>8 chars)
    long_words = sum(1 for w in all_words if len(w) > 8)
    complexity_ratio = long_words / total

    # Stop words for filtering
    stop_words = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "is", "are", "was", "were", "be", "been",
        "being", "have", "has", "had", "do", "does", "did", "will", "would",
        "could", "should", "may", "might", "can", "shall", "this", "that",
        "these", "those", "it", "its", "i", "you", "he", "she", "we", "they",
        "my", "your", "his", "her", "our", "their", "not", "no", "if", "then",
        "than", "so", "as", "up", "out", "about", "into", "through", "just",
        "also", "more", "most", "very", "too", "here", "there", "when", "where",
        "what", "how", "who", "which", "all", "each", "every", "some", "any",
    }

    # Signature words: frequent non-stop words
    content_freq = {w: c for w, c in freq.items() if w not in stop_words and len(w) > 3}
    signature_words = sorted(content_freq.items(), key=lambda x: x[1], reverse=True)[:30]

    return {
        "total_words": total,
        "unique_words": unique,
        "type_token_ratio": round(ttr, 3),
        "complexity_ratio": round(complexity_ratio, 3),
        "vocabulary_level": (
            "advanced" if complexity_ratio > 0.15
            else "intermediate" if complexity_ratio > 0.08
            else "accessible"
        ),
        "signature_words": [{"word": w, "count": c} for w, c in signature_words[:15]],
    }


def analyze_formality(texts: list[str]) -> dict:
    """Estimate formality level from writing patterns."""
    combined = " ".join(texts)
    words = combined.split()
    total_words = len(words)

    if total_words == 0:
        return {"level": 5, "indicators": []}

    indicators = []

    # Contractions
    contractions = len(re.findall(r"\b\w+'(?:t|s|re|ve|ll|d|m)\b", combined, re.IGNORECASE))
    contraction_ratio = contractions / total_words
    if contraction_ratio > 0.02:
        indicators.append(f"frequent contractions ({contractions} found) -> casual")
    elif contraction_ratio < 0.005:
        indicators.append("rare contractions -> formal")

    # First person
    first_person = len(re.findall(r"\b(I|my|me|we|our|us)\b", combined, re.IGNORECASE))
    first_person_ratio = first_person / total_words
    if first_person_ratio > 0.03:
        indicators.append(f"high first-person usage ({first_person}) -> personal/casual")

    # Exclamation marks
    exclamations = combined.count("!")
    if exclamations > 5:
        indicators.append(f"frequent exclamation marks ({exclamations}) -> enthusiastic/casual")
    elif exclamations == 0:
        indicators.append("no exclamation marks -> restrained/formal")

    # Questions
    questions = combined.count("?")
    if questions > 3:
        indicators.append(f"rhetorical questions used ({questions}) -> conversational")

    # Parenthetical asides
    parentheticals = len(re.findall(r"\([^)]+\)", combined))
    if parentheticals > 3:
        indicators.append(f"parenthetical asides ({parentheticals}) -> conversational/informal")

    # Em-dashes
    em_dashes = len(re.findall(r"[\u2014]|---?", combined))
    if em_dashes > 5:
        indicators.append(f"em-dash usage ({em_dashes}) -> stylistic, magazine-style")

    # Estimate level (1-10 scale)
    level = 5.0
    level -= contraction_ratio * 30
    level -= first_person_ratio * 20
    level -= (exclamations / max(total_words, 1)) * 500
    level += (len([w for w in words if len(w) > 10]) / total_words) * 20
    level = max(1, min(10, round(level)))

    descriptions = {
        1: "very casual (texting a friend)",
        2: "casual (blog comment)",
        3: "relaxed conversational (personal blog)",
        4: "conversational-professional (newsletter)",
        5: "professional (company blog)",
        6: "formal-professional (business communication)",
        7: "formal (industry publication)",
        8: "very formal (academic paper)",
        9: "highly formal (legal document)",
        10: "maximum formality (Supreme Court brief)",
    }

    return {
        "level": level,
        "description": descriptions.get(level, "professional"),
        "indicators": indicators,
    }


def analyze_punctuation(texts: list[str]) -> dict:
    """Analyze punctuation habits."""
    combined = " ".join(texts)

    patterns = {
        "em_dashes": len(re.findall(r"[\u2014]|---", combined)),
        "en_dashes": len(re.findall(r"[\u2013]|(?<!\-)--(?!\-)", combined)),
        "semicolons": combined.count(";"),
        "colons": combined.count(":"),
        "exclamations": combined.count("!"),
        "questions": combined.count("?"),
        "ellipses": len(re.findall(r"\.{3}|[\u2026]", combined)),
        "parentheticals": len(re.findall(r"\([^)]+\)", combined)),
    }

    # Identify signature punctuation habits
    habits = []
    if patterns["em_dashes"] > 5:
        habits.append("Heavy em-dash user (dramatic pauses, interjections)")
    if patterns["semicolons"] > 3:
        habits.append("Uses semicolons (balanced, complex sentences)")
    if patterns["ellipses"] > 2:
        habits.append("Uses ellipses (trailing thoughts, suspense)")
    if patterns["parentheticals"] > 5:
        habits.append("Frequent parenthetical asides (conversational tangents)")
    if patterns["exclamations"] > 5:
        habits.append("Generous with exclamation marks (enthusiastic tone)")
    if patterns["questions"] > 5:
        habits.append("Uses questions to engage the reader")

    return {
        "counts": patterns,
        "habits": habits,
    }


def generate_voice_md(analysis: dict) -> str:
    """Generate VOICE.md content from analysis results."""
    sentences = analysis["sentences"]
    vocab = analysis["vocabulary"]
    formality = analysis["formality"]
    punctuation = analysis["punctuation"]

    # Build the VOICE.md
    lines = [
        "# Voice Profile",
        "",
        f"*Generated from {analysis['sample_count']} writing sample(s) ({analysis['total_words']} words total)*",
        "",
        "---",
        "",
        "## Formality",
        "",
        f"**Level:** {formality['level']}/10 ({formality['description']})",
        "",
    ]

    if formality["indicators"]:
        lines.append("**Indicators:**")
        for ind in formality["indicators"]:
            lines.append(f"- {ind}")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Sentence Rhythm",
        "",
        f"- **Average sentence length:** {sentences['avg_length']} words",
        f"- **Variation:** {sentences['rhythm']}",
        f"- **Short sentence ratio:** {sentences['short_sentence_ratio']} (percentage under 8 words)",
        f"- **Length preference:** {sentences['length_preference']}",
        "",
        "---",
        "",
        "## Vocabulary",
        "",
        f"- **Level:** {vocab.get('vocabulary_level', 'unknown')}",
        f"- **Type-token ratio:** {vocab.get('type_token_ratio', 0)} (higher = more diverse)",
        f"- **Complexity ratio:** {vocab.get('complexity_ratio', 0)} (ratio of 8+ character words)",
        "",
    ])

    if vocab.get("signature_words"):
        lines.append("**Signature words** (most frequent content words):")
        for entry in vocab["signature_words"][:10]:
            lines.append(f"- {entry['word']} ({entry['count']}x)")
        lines.append("")

    lines.extend([
        "---",
        "",
        "## Punctuation Style",
        "",
    ])

    if punctuation.get("habits"):
        for habit in punctuation["habits"]:
            lines.append(f"- {habit}")
    else:
        lines.append("- No strong punctuation habits detected")
    lines.append("")

    lines.extend([
        "---",
        "",
        "## Sounds Like Us / Does Not Sound Like Us",
        "",
        "*(Review and edit these based on the analysis above)*",
        "",
        "**Sounds like us:**",
        "- [Add 3-5 example sentences from your best writing]",
        "",
        "**Does not sound like us:**",
        "- [Add 3-5 examples of writing styles to avoid]",
        "",
        "---",
        "",
        "## Forbidden Phrases",
        "",
        "- [Add phrases that should never appear in your content]",
        "",
        "---",
        "",
        "## Preferred Vocabulary",
        "",
        "- [Add words and phrases you prefer to use]",
        "",
    ])

    return "\n".join(lines)


def analyze_samples(directory: str) -> dict:
    """Main analysis pipeline."""
    samples = read_samples(directory)

    if not samples:
        return {"error": f"No text files found in {directory}"}

    if sum(len(s["clean"]) for s in samples) < 200:
        return {
            "warning": "Total sample text is under 200 words. Voice analysis may be unreliable. Provide more writing samples for better results.",
            "sample_count": len(samples),
        }

    clean_texts = [s["clean"] for s in samples]
    combined_words = sum(len(t.split()) for t in clean_texts)

    analysis = {
        "sample_count": len(samples),
        "sample_files": [s["file"] for s in samples],
        "total_words": combined_words,
        "sentences": analyze_sentence_patterns(clean_texts),
        "vocabulary": analyze_vocabulary(clean_texts),
        "formality": analyze_formality(clean_texts),
        "punctuation": analyze_punctuation(clean_texts),
    }

    analysis["voice_md"] = generate_voice_md(analysis)

    return analysis


def main():
    parser = argparse.ArgumentParser(
        description="Analyze writing samples to extract a voice profile."
    )
    parser.add_argument(
        "samples_dir", help="Directory containing writing sample files (.md, .txt)"
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Write generated VOICE.md to this path (default: stdout)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output full analysis as JSON instead of VOICE.md",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print summary to stderr"
    )

    args = parser.parse_args()
    result = analyze_samples(args.samples_dir)

    if "error" in result:
        print(json.dumps(result, indent=2))
        sys.exit(1)

    if args.json:
        # Remove the voice_md from JSON output (it's large)
        json_result = {k: v for k, v in result.items() if k != "voice_md"}
        print(json.dumps(json_result, indent=2))
    else:
        voice_md = result.get("voice_md", "")
        if args.output:
            output_path = Path(args.output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(voice_md, encoding="utf-8")
            print(f"Voice profile written to: {args.output}", file=sys.stderr)
        else:
            print(voice_md)

    if args.verbose:
        print(f"\n--- Voice Analysis Summary ---", file=sys.stderr)
        print(f"Samples: {result['sample_count']}", file=sys.stderr)
        print(f"Total words: {result['total_words']}", file=sys.stderr)
        f = result["formality"]
        print(f"Formality: {f['level']}/10 ({f['description']})", file=sys.stderr)
        s = result["sentences"]
        print(f"Avg sentence: {s['avg_length']} words ({s['rhythm']})", file=sys.stderr)
        v = result["vocabulary"]
        print(f"Vocabulary: {v.get('vocabulary_level', '?')} (TTR: {v.get('type_token_ratio', '?')})", file=sys.stderr)

    sys.exit(0)


if __name__ == "__main__":
    main()
