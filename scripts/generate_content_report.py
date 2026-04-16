#!/usr/bin/env python3
"""Generate a content report from a directory of content files.

Analyzes content pieces for: count by type, readability scores,
anti-slop compliance, and brand consistency over time.

Usage:
    python scripts/generate_content_report.py content/
    python scripts/generate_content_report.py content/ --brand-dir brand/ --verbose
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


# Reuse analysis functions from sibling scripts
# (Inline simplified versions to keep this script standalone)

SLOP_KEYWORDS = [
    "delve", "synergy", "leverage", "game-changer", "paradigm shift",
    "cutting-edge", "best-in-class", "holistic", "seamless", "robust",
    "empower", "unlock potential", "deep dive", "unpack",
]

FILLER_PHRASES = [
    "it's worth noting that", "at the end of the day", "in order to",
    "due to the fact that", "it goes without saying", "needless to say",
    "when it comes to", "the reality is that", "as a matter of fact",
    "it is important to note that",
]

OPENING_CLICHES = [
    r"(?i)in\s+today'?s\s+(fast[- ]paced|ever[- ]changing|digital)\s+world",
    r"(?i)let'?s\s+dive\s+in",
    r"(?i)in\s+the\s+ever[- ]evolving\s+(landscape|world)",
    r"(?i)have\s+you\s+ever\s+wondered",
]


def quick_slop_score(text: str) -> dict:
    """Quick anti-slop score (simplified version)."""
    penalty = 0
    issues = []

    text_lower = text.lower()

    for keyword in SLOP_KEYWORDS:
        count = text_lower.count(keyword.lower())
        if count > 0:
            penalty += count * 5
            issues.append(f"'{keyword}' x{count}")

    for phrase in FILLER_PHRASES:
        count = text_lower.count(phrase.lower())
        if count > 0:
            penalty += count * 3
            issues.append(f"filler: '{phrase}' x{count}")

    for pattern in OPENING_CLICHES:
        if re.search(pattern, text):
            penalty += 10
            issues.append("opening cliche detected")

    score = max(0, 100 - penalty)
    return {"score": score, "issues": issues}


def quick_readability(text: str) -> dict:
    """Quick readability metrics (simplified)."""
    # Strip markdown
    clean = re.sub(r"```[\s\S]*?```", "", text)
    clean = re.sub(r"^#{1,6}\s+", "", clean, flags=re.MULTILINE)
    clean = re.sub(r"[*_`\[\]()]", "", clean)

    words = clean.split()
    word_count = len(words)

    sentences = re.split(r"[.!?]+\s", clean)
    sentence_count = max(len([s for s in sentences if len(s.strip()) > 5]), 1)

    avg_sentence_length = word_count / sentence_count

    # Rough syllable count
    syllables = 0
    for word in words:
        word = word.lower().strip(".,;:!?\"'")
        vowel_groups = re.findall(r"[aeiouy]+", word)
        syllables += max(len(vowel_groups), 1)

    # Flesch-Kincaid Grade Level
    if word_count > 0 and sentence_count > 0:
        fk_grade = (
            0.39 * (word_count / sentence_count)
            + 11.8 * (syllables / word_count)
            - 15.59
        )
        fk_grade = round(max(0, fk_grade), 1)
    else:
        fk_grade = 0.0

    return {
        "word_count": word_count,
        "sentence_count": sentence_count,
        "avg_sentence_length": round(avg_sentence_length, 1),
        "flesch_kincaid_grade": fk_grade,
    }


def detect_content_type(filepath: Path, text: str) -> str:
    """Guess content type from filename and content."""
    name = filepath.stem.lower()
    suffix = filepath.suffix.lower()

    if suffix == ".svg":
        return "infographic"
    if suffix in (".html", ".htm"):
        if "reveal" in text.lower() or "slidev" in text.lower():
            return "presentation"
        return "web_content"
    if suffix in (".tsx", ".jsx"):
        return "video_script"

    # Check content patterns
    if re.search(r"^#{1,2}\s+", text, re.MULTILINE):
        if "thread" in name or "tweet" in name:
            return "twitter"
        if "linkedin" in name:
            return "linkedin"
        if "reddit" in name:
            return "reddit"
        return "blog_post"

    return "other"


def analyze_content_directory(content_dir: str, brand_dir: str = "brand") -> dict:
    """Analyze all content files in a directory."""
    dir_path = Path(content_dir)

    if not dir_path.exists():
        return {"error": f"Directory not found: {content_dir}"}

    content_extensions = {".md", ".txt", ".html", ".htm", ".svg", ".tsx", ".jsx", ".markdown"}
    files = []

    for file in sorted(dir_path.rglob("*")):
        if file.is_file() and file.suffix.lower() in content_extensions:
            files.append(file)

    if not files:
        return {"error": f"No content files found in {content_dir}"}

    # Analyze each file
    pieces = []
    type_counts = {}
    total_words = 0
    slop_scores = []
    readability_scores = []

    for file in files:
        try:
            text = file.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        content_type = detect_content_type(file, text)
        type_counts[content_type] = type_counts.get(content_type, 0) + 1

        readability = quick_readability(text)
        slop = quick_slop_score(text)

        total_words += readability["word_count"]
        slop_scores.append(slop["score"])
        readability_scores.append(readability["flesch_kincaid_grade"])

        # Get file modification time
        mtime = datetime.fromtimestamp(file.stat().st_mtime).isoformat()

        pieces.append({
            "file": str(file.relative_to(dir_path)),
            "type": content_type,
            "word_count": readability["word_count"],
            "readability": readability,
            "anti_slop_score": slop["score"],
            "slop_issues": slop["issues"],
            "last_modified": mtime,
        })

    # Summary stats
    avg_slop = sum(slop_scores) / len(slop_scores) if slop_scores else 0
    avg_readability = sum(readability_scores) / len(readability_scores) if readability_scores else 0

    # Pieces with issues
    flagged = [p for p in pieces if p["anti_slop_score"] < 70]

    report = {
        "directory": str(dir_path),
        "generated_at": datetime.now().isoformat(),
        "summary": {
            "total_pieces": len(pieces),
            "total_words": total_words,
            "content_types": type_counts,
            "avg_anti_slop_score": round(avg_slop, 1),
            "avg_readability_grade": round(avg_readability, 1),
            "pieces_flagged": len(flagged),
        },
        "pieces": pieces,
        "flagged_pieces": [
            {
                "file": p["file"],
                "anti_slop_score": p["anti_slop_score"],
                "issues": p["slop_issues"],
            }
            for p in flagged
        ],
    }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Generate a content report from a directory of content files."
    )
    parser.add_argument(
        "content_dir", help="Directory containing content files to analyze"
    )
    parser.add_argument(
        "--brand-dir",
        "-b",
        default="brand",
        help="Path to brand directory (default: brand/)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print summary to stderr"
    )

    args = parser.parse_args()
    report = analyze_content_directory(args.content_dir, args.brand_dir)

    if "error" in report:
        print(json.dumps(report, indent=2))
        sys.exit(1)

    print(json.dumps(report, indent=2))

    if args.verbose:
        s = report["summary"]
        print(f"\n--- Content Report ---", file=sys.stderr)
        print(f"Total pieces: {s['total_pieces']}", file=sys.stderr)
        print(f"Total words: {s['total_words']}", file=sys.stderr)
        print(f"Content types: {json.dumps(s['content_types'])}", file=sys.stderr)
        print(f"Avg anti-slop score: {s['avg_anti_slop_score']}/100", file=sys.stderr)
        print(f"Avg readability grade: {s['avg_readability_grade']}", file=sys.stderr)
        if s["pieces_flagged"] > 0:
            print(f"Flagged pieces: {s['pieces_flagged']}", file=sys.stderr)
            for fp in report["flagged_pieces"]:
                print(f"  - {fp['file']} (score: {fp['anti_slop_score']})", file=sys.stderr)

    sys.exit(0)


if __name__ == "__main__":
    main()
