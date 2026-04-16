#!/usr/bin/env python3
"""Calculate readability metrics for a text file.

Computes Flesch-Kincaid grade level, average sentence length, paragraph
length variation, and vocabulary diversity. Outputs JSON.

Usage:
    python scripts/readability_score.py <input_file>
    python scripts/readability_score.py content/draft.md --verbose
"""

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path


def count_syllables(word: str) -> int:
    """Estimate syllable count for an English word.

    Uses a heuristic approach: count vowel groups, adjust for silent-e
    and common patterns.
    """
    word = word.lower().strip()
    if not word:
        return 0

    # Remove non-alpha
    word = re.sub(r"[^a-z]", "", word)
    if not word:
        return 0

    if len(word) <= 2:
        return 1

    # Count vowel groups
    vowel_groups = re.findall(r"[aeiouy]+", word)
    count = len(vowel_groups)

    # Adjust for silent e at end
    if word.endswith("e") and not word.endswith("le"):
        count -= 1

    # Adjust for common suffixes
    if word.endswith("ed") and len(word) > 3:
        if word[-3] not in "dt":
            count -= 1

    # Minimum 1 syllable
    return max(1, count)


def strip_markdown(text: str) -> str:
    """Remove markdown formatting to get plain text for analysis."""
    # Remove code blocks
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`]+`", "", text)

    # Remove frontmatter
    text = re.sub(r"^---[\s\S]*?---\n", "", text)

    # Remove headings markup (keep the text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)

    # Remove links but keep text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # Remove images
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", "", text)

    # Remove bold/italic markers
    text = re.sub(r"[*_]{1,3}([^*_]+)[*_]{1,3}", r"\1", text)

    # Remove blockquotes marker
    text = re.sub(r"^\s*>\s+", "", text, flags=re.MULTILINE)

    # Remove horizontal rules
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove list markers
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)

    return text.strip()


def extract_sentences(text: str) -> list[str]:
    """Split text into sentences."""
    # Split on sentence-ending punctuation followed by space or end
    sentences = re.split(r"(?<=[.!?])\s+", text)
    # Filter out empty strings and very short fragments
    return [s.strip() for s in sentences if len(s.strip()) > 5]


def extract_words(text: str) -> list[str]:
    """Extract words from text."""
    words = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?\b", text)
    return [w.lower() for w in words if len(w) > 0]


def extract_paragraphs(text: str) -> list[str]:
    """Split text into paragraphs."""
    paragraphs = text.split("\n\n")
    return [p.strip() for p in paragraphs if len(p.strip()) > 20]


def flesch_kincaid_grade(total_words: int, total_sentences: int, total_syllables: int) -> float:
    """Calculate Flesch-Kincaid Grade Level."""
    if total_sentences == 0 or total_words == 0:
        return 0.0

    grade = (
        0.39 * (total_words / total_sentences)
        + 11.8 * (total_syllables / total_words)
        - 15.59
    )
    return round(max(0, grade), 1)


def flesch_reading_ease(total_words: int, total_sentences: int, total_syllables: int) -> float:
    """Calculate Flesch Reading Ease score (0-100, higher = easier)."""
    if total_sentences == 0 or total_words == 0:
        return 0.0

    score = (
        206.835
        - 1.015 * (total_words / total_sentences)
        - 84.6 * (total_syllables / total_words)
    )
    return round(max(0, min(100, score)), 1)


def vocabulary_diversity(words: list[str]) -> dict:
    """Calculate vocabulary diversity metrics."""
    if not words:
        return {"unique_words": 0, "total_words": 0, "type_token_ratio": 0.0}

    total = len(words)
    unique = len(set(words))
    ttr = unique / total if total > 0 else 0.0

    # Hapax legomena: words that appear exactly once
    freq = Counter(words)
    hapax = sum(1 for count in freq.values() if count == 1)

    # Most frequent content words (exclude common stop words)
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
    content_words = {w: c for w, c in freq.items() if w not in stop_words}
    top_words = sorted(content_words.items(), key=lambda x: x[1], reverse=True)[:20]

    return {
        "unique_words": unique,
        "total_words": total,
        "type_token_ratio": round(ttr, 3),
        "hapax_legomena": hapax,
        "hapax_ratio": round(hapax / total, 3) if total > 0 else 0.0,
        "top_content_words": [{"word": w, "count": c} for w, c in top_words],
    }


def analyze_file(filepath: str) -> dict:
    """Run all readability analyses on a file and return a report."""
    path = Path(filepath)
    if not path.exists():
        return {"error": f"File not found: {filepath}"}

    raw_text = path.read_text(encoding="utf-8")
    text = strip_markdown(raw_text)

    sentences = extract_sentences(text)
    words = extract_words(text)
    paragraphs = extract_paragraphs(text)

    total_words = len(words)
    total_sentences = len(sentences)
    total_syllables = sum(count_syllables(w) for w in words)

    # Sentence length stats
    sentence_lengths = [len(extract_words(s)) for s in sentences]
    avg_sentence_length = (
        sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0
    )
    min_sentence = min(sentence_lengths) if sentence_lengths else 0
    max_sentence = max(sentence_lengths) if sentence_lengths else 0

    sentence_length_std = 0.0
    if len(sentence_lengths) > 1:
        variance = sum(
            (l - avg_sentence_length) ** 2 for l in sentence_lengths
        ) / len(sentence_lengths)
        sentence_length_std = math.sqrt(variance)

    # Paragraph length stats
    paragraph_word_counts = [len(extract_words(p)) for p in paragraphs]
    avg_paragraph_length = (
        sum(paragraph_word_counts) / len(paragraph_word_counts)
        if paragraph_word_counts
        else 0
    )

    paragraph_length_std = 0.0
    if len(paragraph_word_counts) > 1:
        variance = sum(
            (l - avg_paragraph_length) ** 2 for l in paragraph_word_counts
        ) / len(paragraph_word_counts)
        paragraph_length_std = math.sqrt(variance)

    # Vocabulary
    vocab = vocabulary_diversity(words)

    # Grade level interpretation
    fk_grade = flesch_kincaid_grade(total_words, total_sentences, total_syllables)
    fre_score = flesch_reading_ease(total_words, total_sentences, total_syllables)

    if fre_score >= 80:
        reading_level = "easy (6th grade)"
    elif fre_score >= 60:
        reading_level = "standard (8th-9th grade)"
    elif fre_score >= 40:
        reading_level = "fairly difficult (10th-12th grade)"
    elif fre_score >= 20:
        reading_level = "difficult (college level)"
    else:
        reading_level = "very difficult (graduate level)"

    report = {
        "file": str(path),
        "word_count": total_words,
        "sentence_count": total_sentences,
        "paragraph_count": len(paragraphs),
        "readability": {
            "flesch_kincaid_grade_level": fk_grade,
            "flesch_reading_ease": fre_score,
            "reading_level": reading_level,
        },
        "sentence_metrics": {
            "average_length": round(avg_sentence_length, 1),
            "min_length": min_sentence,
            "max_length": max_sentence,
            "length_std_dev": round(sentence_length_std, 1),
            "length_variation": "good" if sentence_length_std > 5 else "low (monotonous rhythm)",
        },
        "paragraph_metrics": {
            "average_length_words": round(avg_paragraph_length, 1),
            "length_std_dev": round(paragraph_length_std, 1),
            "length_variation": "good" if paragraph_length_std > 15 else "low (uniform paragraphs)",
        },
        "vocabulary": vocab,
    }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Calculate readability metrics for a text file."
    )
    parser.add_argument("input_file", help="Path to the text file to analyze")
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print summary to stderr"
    )

    args = parser.parse_args()
    report = analyze_file(args.input_file)

    if "error" in report:
        print(json.dumps(report, indent=2))
        sys.exit(1)

    print(json.dumps(report, indent=2))

    if args.verbose:
        r = report["readability"]
        print(f"\n--- Readability Report ---", file=sys.stderr)
        print(f"Words: {report['word_count']}", file=sys.stderr)
        print(f"Sentences: {report['sentence_count']}", file=sys.stderr)
        print(f"Paragraphs: {report['paragraph_count']}", file=sys.stderr)
        print(
            f"Flesch-Kincaid Grade: {r['flesch_kincaid_grade_level']}", file=sys.stderr
        )
        print(f"Flesch Reading Ease: {r['flesch_reading_ease']}", file=sys.stderr)
        print(f"Level: {r['reading_level']}", file=sys.stderr)
        print(
            f"Avg sentence length: {report['sentence_metrics']['average_length']} words",
            file=sys.stderr,
        )
        print(
            f"Vocabulary diversity (TTR): {report['vocabulary']['type_token_ratio']}",
            file=sys.stderr,
        )

    sys.exit(0)


if __name__ == "__main__":
    main()
