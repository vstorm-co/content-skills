#!/usr/bin/env python3
"""Check content against brand voice and visual guidelines.

Compares a content file against brand/VOICE.md and brand/VISUAL.md.
Checks vocabulary alignment, formality level, forbidden phrases, and
color hex codes in visual content.

Usage:
    python scripts/brand_consistency_checker.py <content_file>
    python scripts/brand_consistency_checker.py <content_file> --brand-dir ./brand
"""

import argparse
import json
import re
import sys
from pathlib import Path


def parse_voice_md(voice_path: Path) -> dict:
    """Extract voice rules from a VOICE.md file.

    Parses sections for: preferred vocabulary, forbidden phrases,
    formality level, and tone attributes.
    """
    if not voice_path.exists():
        return {}

    text = voice_path.read_text(encoding="utf-8")
    voice = {
        "preferred_words": [],
        "forbidden_phrases": [],
        "formality_level": None,
        "tone_attributes": [],
    }

    # Extract forbidden phrases (look for common section patterns)
    forbidden_section = re.search(
        r"(?i)(?:forbidden|banned|blacklist|avoid|don'?t\s+use|never\s+use)[^\n]*\n((?:[-*]\s+.*\n?)+)",
        text,
    )
    if forbidden_section:
        items = re.findall(r"[-*]\s+[\"']?([^\"'\n]+)[\"']?", forbidden_section.group(1))
        voice["forbidden_phrases"] = [item.strip().lower() for item in items]

    # Extract preferred vocabulary
    preferred_section = re.search(
        r"(?i)(?:preferred|use\s+these|vocabulary|words\s+we\s+(?:love|use))[^\n]*\n((?:[-*]\s+.*\n?)+)",
        text,
    )
    if preferred_section:
        items = re.findall(r"[-*]\s+[\"']?([^\"'\n]+)[\"']?", preferred_section.group(1))
        voice["preferred_words"] = [item.strip().lower() for item in items]

    # Extract formality level (look for a number 1-10)
    formality_match = re.search(
        r"(?i)formality[^\n]*?(\d{1,2})\s*(?:/\s*10|out\s+of\s+10)?", text
    )
    if formality_match:
        level = int(formality_match.group(1))
        if 1 <= level <= 10:
            voice["formality_level"] = level

    # Extract tone attributes (adjectives near "tone" or "voice")
    tone_section = re.search(
        r"(?i)(?:tone|voice)\s*(?:is|:)[^\n]*\n((?:[-*]\s+.*\n?)+)", text
    )
    if tone_section:
        items = re.findall(r"[-*]\s+(\w[\w\s-]*)", tone_section.group(1))
        voice["tone_attributes"] = [item.strip().lower() for item in items]

    return voice


def parse_visual_md(visual_path: Path) -> dict:
    """Extract visual rules from a VISUAL.md file.

    Parses sections for: color hex codes, font families, and visual rules.
    """
    if not visual_path.exists():
        return {}

    text = visual_path.read_text(encoding="utf-8")
    visual = {
        "hex_colors": [],
        "font_families": [],
    }

    # Extract all hex color codes defined in the brand
    hex_matches = re.findall(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", text)
    visual["hex_colors"] = [c.lower() for c in hex_matches]

    # Extract font family names (look for common font specification patterns)
    font_matches = re.findall(
        r"(?i)(?:font|typeface|family)[^\n]*?[:\-]\s*[\"']?([A-Z][A-Za-z\s]+?)(?:[\"',\n]|$)",
        text,
    )
    visual["font_families"] = [f.strip() for f in font_matches if len(f.strip()) > 1]

    return visual


def check_forbidden_phrases(text: str, forbidden: list[str]) -> list[dict]:
    """Check content for forbidden phrases."""
    findings = []
    text_lower = text.lower()

    for phrase in forbidden:
        pattern = re.compile(re.escape(phrase), re.IGNORECASE)
        for match in pattern.finditer(text):
            line_num = text[:match.start()].count("\n") + 1
            findings.append(
                {
                    "check": "forbidden_phrase",
                    "severity": "critical",
                    "description": f"Forbidden phrase found: '{phrase}'",
                    "line": line_num,
                    "matched_text": match.group(0),
                }
            )

    return findings


def check_vocabulary_alignment(text: str, preferred: list[str]) -> dict:
    """Check how many preferred vocabulary terms appear in the content."""
    text_lower = text.lower()
    found = []
    missing = []

    for word in preferred:
        if word.lower() in text_lower:
            found.append(word)
        else:
            missing.append(word)

    total = len(preferred)
    alignment = len(found) / total if total > 0 else 1.0

    return {
        "check": "vocabulary_alignment",
        "alignment_ratio": round(alignment, 2),
        "preferred_found": found,
        "preferred_missing": missing,
        "description": f"{len(found)}/{total} preferred terms used",
    }


def check_formality_level(text: str, target_level: int | None) -> dict:
    """Estimate content formality and compare to target.

    Uses heuristics: contraction usage, sentence length, vocabulary complexity.
    Scale: 1 (very casual) to 10 (very formal).
    """
    if target_level is None:
        return {
            "check": "formality_level",
            "target": None,
            "estimated": None,
            "description": "No target formality level defined in VOICE.md",
        }

    # Heuristic signals
    words = text.split()
    word_count = len(words)
    if word_count == 0:
        return {
            "check": "formality_level",
            "target": target_level,
            "estimated": 5,
            "deviation": 0,
            "description": "Empty content",
        }

    # Contractions lower formality
    contractions = len(re.findall(r"\b\w+'(?:t|s|re|ve|ll|d|m)\b", text, re.IGNORECASE))
    contraction_ratio = contractions / word_count

    # Long words raise formality
    long_words = sum(1 for w in words if len(w) > 8)
    long_word_ratio = long_words / word_count

    # Sentence length (longer = more formal)
    sentences = re.split(r"[.!?]+\s", text)
    avg_sentence_length = word_count / max(len(sentences), 1)

    # Estimate formality (1-10)
    estimated = 5.0
    estimated -= contraction_ratio * 15  # Contractions = casual
    estimated += long_word_ratio * 10  # Long words = formal
    estimated += (avg_sentence_length - 15) * 0.1  # Long sentences = formal
    estimated = max(1, min(10, round(estimated)))

    deviation = abs(estimated - target_level)

    return {
        "check": "formality_level",
        "target": target_level,
        "estimated": estimated,
        "deviation": deviation,
        "description": f"Estimated formality: {estimated}/10, target: {target_level}/10, deviation: {deviation}",
    }


def check_visual_colors(text: str, brand_colors: list[str]) -> list[dict]:
    """Check that hex colors in content match brand palette."""
    findings = []

    if not brand_colors:
        return findings

    # Find all hex colors in the content
    content_colors = re.findall(r"#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", text)

    for color in content_colors:
        color_lower = color.lower()
        if color_lower not in brand_colors:
            line_num = text[: text.lower().index(color_lower)].count("\n") + 1
            findings.append(
                {
                    "check": "off_brand_color",
                    "severity": "warning",
                    "description": f"Color {color} is not in the brand palette",
                    "line": line_num,
                    "matched_text": color,
                    "brand_colors": brand_colors,
                }
            )

    return findings


def check_content(content_path: str, brand_dir: str = "brand") -> dict:
    """Run all brand consistency checks and return a JSON-serializable report."""
    content_file = Path(content_path)
    brand_path = Path(brand_dir)

    if not content_file.exists():
        return {"error": f"Content file not found: {content_path}"}

    text = content_file.read_text(encoding="utf-8")

    voice_path = brand_path / "VOICE.md"
    visual_path = brand_path / "VISUAL.md"

    voice = parse_voice_md(voice_path)
    visual = parse_visual_md(visual_path)

    findings = []
    checks = {}

    # Check forbidden phrases
    if voice.get("forbidden_phrases"):
        forbidden_results = check_forbidden_phrases(text, voice["forbidden_phrases"])
        findings.extend(forbidden_results)
        checks["forbidden_phrases"] = {
            "violations": len(forbidden_results),
            "status": "pass" if len(forbidden_results) == 0 else "fail",
        }
    else:
        checks["forbidden_phrases"] = {
            "violations": 0,
            "status": "skipped",
            "reason": "No forbidden phrases defined in VOICE.md",
        }

    # Check vocabulary alignment
    if voice.get("preferred_words"):
        vocab_result = check_vocabulary_alignment(text, voice["preferred_words"])
        checks["vocabulary_alignment"] = vocab_result
    else:
        checks["vocabulary_alignment"] = {
            "status": "skipped",
            "reason": "No preferred vocabulary defined in VOICE.md",
        }

    # Check formality level
    formality_result = check_formality_level(text, voice.get("formality_level"))
    checks["formality_level"] = formality_result

    # Check visual colors (for visual content: SVG, HTML, CSS, etc.)
    visual_extensions = {".svg", ".html", ".htm", ".css", ".jsx", ".tsx"}
    if content_file.suffix.lower() in visual_extensions and visual.get("hex_colors"):
        color_results = check_visual_colors(text, visual["hex_colors"])
        findings.extend(color_results)
        checks["visual_colors"] = {
            "off_brand_colors": len(color_results),
            "brand_palette": visual["hex_colors"],
            "status": "pass" if len(color_results) == 0 else "fail",
        }
    else:
        checks["visual_colors"] = {
            "status": "skipped",
            "reason": "Not a visual content file or no brand colors defined",
        }

    # Calculate overall score
    score = 100
    for finding in findings:
        if finding.get("severity") == "critical":
            score -= 15
        elif finding.get("severity") == "warning":
            score -= 5

    # Penalize formality deviation
    if formality_result.get("deviation") and formality_result["deviation"] > 0:
        score -= formality_result["deviation"] * 5

    # Bonus for vocabulary alignment
    if checks.get("vocabulary_alignment", {}).get("alignment_ratio") is not None:
        alignment = checks["vocabulary_alignment"]["alignment_ratio"]
        if alignment < 0.3:
            score -= 10

    score = max(0, min(100, score))

    report = {
        "file": str(content_file),
        "brand_dir": str(brand_path),
        "brand_files_found": {
            "VOICE.md": voice_path.exists(),
            "VISUAL.md": visual_path.exists(),
        },
        "overall_score": score,
        "passed": score >= 70 and all(
            f.get("severity") != "critical" for f in findings
        ),
        "checks": checks,
        "findings": findings,
    }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Check content against brand voice and visual guidelines."
    )
    parser.add_argument("content_file", help="Path to the content file to check")
    parser.add_argument(
        "--brand-dir",
        "-b",
        default="brand",
        help="Path to the brand directory (default: brand/)",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print summary to stderr"
    )

    args = parser.parse_args()
    report = check_content(args.content_file, args.brand_dir)

    if "error" in report:
        print(json.dumps(report, indent=2))
        sys.exit(1)

    print(json.dumps(report, indent=2))

    if args.verbose:
        print(f"\n--- Brand Consistency Report ---", file=sys.stderr)
        print(f"Score: {report['overall_score']}/100", file=sys.stderr)
        print(
            f"Brand files: VOICE.md={'found' if report['brand_files_found']['VOICE.md'] else 'missing'}, "
            f"VISUAL.md={'found' if report['brand_files_found']['VISUAL.md'] else 'missing'}",
            file=sys.stderr,
        )
        for name, check in report["checks"].items():
            status = check.get("status", "done")
            print(f"  {name}: {status}", file=sys.stderr)
        if report["passed"]:
            print("Result: PASSED", file=sys.stderr)
        else:
            print("Result: FAILED", file=sys.stderr)

    sys.exit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
