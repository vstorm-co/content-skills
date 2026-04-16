#!/usr/bin/env python3
"""Check text for AI slop patterns.

Scans a text file for common AI-generated writing patterns: generic openings,
buzzwords, filler phrases, passive voice overuse, and uniform paragraph structure.
Outputs a JSON report with total score, patterns found, and severity per pattern.

Usage:
    python scripts/anti_slop_checker.py <input_file>
    python scripts/anti_slop_checker.py content/draft.md --verbose
"""

import argparse
import json
import re
import sys
from pathlib import Path


# Pattern definitions: (pattern_name, regex, severity, description, penalty)
# Severity: "critical" (10 pts), "warning" (5 pts), "suggestion" (2 pts)
SLOP_PATTERNS = [
    # Opening cliches
    (
        "generic_opening_dive",
        r"(?i)^#*\s*.*\n\n.*?let'?s\s+dive\s+in",
        "critical",
        "Opens with 'Let's dive in'",
        10,
    ),
    (
        "generic_opening_fast_paced",
        r"(?i)in\s+today'?s\s+(fast[- ]paced|ever[- ]changing|digital|modern)\s+world",
        "critical",
        "Opens with 'In today's [adjective] world'",
        10,
    ),
    (
        "generic_opening_ever_evolving",
        r"(?i)in\s+the\s+ever[- ]evolving\s+(landscape|world|realm)",
        "critical",
        "Uses 'in the ever-evolving landscape'",
        10,
    ),
    (
        "generic_opening_no_secret",
        r"(?i)it'?s\s+no\s+secret\s+that",
        "warning",
        "Uses 'it's no secret that'",
        5,
    ),
    (
        "generic_opening_have_you_wondered",
        r"(?i)have\s+you\s+ever\s+wondered",
        "warning",
        "Opens with 'Have you ever wondered'",
        5,
    ),
    (
        "generic_opening_as_we_all_know",
        r"(?i)as\s+we\s+all\s+know",
        "warning",
        "Uses 'as we all know'",
        5,
    ),
    (
        "generic_opening_in_this_article",
        r"(?i)in\s+this\s+(article|post|blog\s+post|piece),?\s+we\s+will",
        "warning",
        "Uses 'In this article, we will...'",
        5,
    ),
    # Closing cliches
    (
        "generic_closing_in_conclusion",
        r"(?i)\bin\s+conclusion\b",
        "warning",
        "Uses 'In conclusion'",
        5,
    ),
    (
        "generic_closing_to_sum_up",
        r"(?i)\bto\s+sum\s+up\b",
        "warning",
        "Uses 'To sum up'",
        5,
    ),
    (
        "generic_closing_there_you_have_it",
        r"(?i)and\s+there\s+you\s+have\s+it",
        "warning",
        "Uses 'And there you have it'",
        5,
    ),
    (
        "generic_closing_happy_coding",
        r"(?i)happy\s+coding!?",
        "suggestion",
        "Uses 'Happy coding!'",
        2,
    ),
    (
        "generic_closing_hope_helpful",
        r"(?i)i\s+hope\s+this\s+(was|is)\s+helpful",
        "warning",
        "Uses 'I hope this was helpful'",
        5,
    ),
    # Buzzwords
    (
        "buzzword_game_changer",
        r"(?i)\bgame[- ]changer\b",
        "warning",
        "Uses 'game-changer' without specifics",
        5,
    ),
    (
        "buzzword_paradigm_shift",
        r"(?i)\bparadigm\s+shift\b",
        "warning",
        "Uses 'paradigm shift'",
        5,
    ),
    (
        "buzzword_leverage_verb",
        r"(?i)\bleverag(e|ing|ed)\b",
        "warning",
        "Uses 'leverage' as a verb (use 'use' instead)",
        5,
    ),
    (
        "buzzword_unlock_potential",
        r"(?i)\bunlock\s+(the\s+)?(full\s+)?potential\b",
        "warning",
        "Uses 'unlock potential'",
        5,
    ),
    (
        "buzzword_empower",
        r"(?i)\bempower(s|ing|ed|ment)?\b",
        "warning",
        "Uses 'empower' (describe what the person can now do instead)",
        5,
    ),
    (
        "buzzword_robust",
        r"(?i)\brobust\b",
        "suggestion",
        "Uses 'robust' (describe what makes it reliable instead)",
        2,
    ),
    (
        "buzzword_seamless",
        r"(?i)\bseamless(ly)?\b",
        "warning",
        "Uses 'seamless' (describe the actual UX instead)",
        5,
    ),
    (
        "buzzword_cutting_edge",
        r"(?i)\bcutting[- ]edge\b",
        "warning",
        "Uses 'cutting-edge' (name the specific technology instead)",
        5,
    ),
    (
        "buzzword_best_in_class",
        r"(?i)\bbest[- ]in[- ]class\b",
        "warning",
        "Uses 'best-in-class' (compared to what?)",
        5,
    ),
    (
        "buzzword_holistic",
        r"(?i)\bholistic(ally)?\b",
        "warning",
        "Uses 'holistic' (describe the specific scope instead)",
        5,
    ),
    (
        "buzzword_synergy",
        r"(?i)\bsynerg(y|ies|ize|istic)\b",
        "critical",
        "Uses 'synergy' (describe what the combination produces)",
        10,
    ),
    (
        "buzzword_deep_dive",
        r"(?i)\bdeep\s+dive\b",
        "suggestion",
        "Uses 'deep dive'",
        2,
    ),
    (
        "buzzword_unpack",
        r"(?i)\bunpack\b",
        "suggestion",
        "Uses 'unpack' (just explain it)",
        2,
    ),
    (
        "buzzword_delve",
        r"(?i)\bdelve\b",
        "critical",
        "Uses 'delve' (banned in all contexts)",
        10,
    ),
    (
        "buzzword_at_end_of_day",
        r"(?i)\bat\s+the\s+end\s+of\s+the\s+day\b",
        "warning",
        "Uses 'at the end of the day'",
        5,
    ),
    # Filler phrases
    (
        "filler_worth_noting",
        r"(?i)\bit'?s\s+worth\s+noting\s+that\b",
        "warning",
        "Uses filler 'It's worth noting that'",
        5,
    ),
    (
        "filler_goes_without_saying",
        r"(?i)\bit\s+goes\s+without\s+saying\b",
        "warning",
        "Uses filler 'It goes without saying'",
        5,
    ),
    (
        "filler_needless_to_say",
        r"(?i)\bneedless\s+to\s+say\b",
        "warning",
        "Uses filler 'Needless to say'",
        5,
    ),
    (
        "filler_as_a_matter_of_fact",
        r"(?i)\bas\s+a\s+matter\s+of\s+fact\b",
        "suggestion",
        "Uses filler 'As a matter of fact'",
        2,
    ),
    (
        "filler_in_order_to",
        r"(?i)\bin\s+order\s+to\b",
        "suggestion",
        "Uses 'in order to' (simplify to 'to')",
        2,
    ),
    (
        "filler_due_to_the_fact",
        r"(?i)\bdue\s+to\s+the\s+fact\s+that\b",
        "warning",
        "Uses 'due to the fact that' (simplify to 'because')",
        5,
    ),
    (
        "filler_important_to_note",
        r"(?i)\bit\s+is\s+important\s+to\s+note\s+that\b",
        "warning",
        "Uses filler 'It is important to note that'",
        5,
    ),
    (
        "filler_when_it_comes_to",
        r"(?i)\bwhen\s+it\s+comes\s+to\b",
        "suggestion",
        "Uses filler 'When it comes to'",
        2,
    ),
    (
        "filler_the_reality_is",
        r"(?i)\bthe\s+reality\s+is\s+that\b",
        "suggestion",
        "Uses filler 'The reality is that'",
        2,
    ),
    (
        "filler_furthermore",
        r"(?i)^\s*furthermore,?\s",
        "suggestion",
        "Uses filler transition 'Furthermore'",
        2,
    ),
    (
        "filler_moreover",
        r"(?i)^\s*moreover,?\s",
        "suggestion",
        "Uses filler transition 'Moreover'",
        2,
    ),
    # AI self-reference
    (
        "ai_self_reference",
        r"(?i)\bas\s+an?\s+ai\b",
        "critical",
        "Contains AI self-reference ('As an AI...')",
        10,
    ),
    (
        "ai_happy_to_help",
        r"(?i)\bi'?d\s+be\s+happy\s+to\b",
        "warning",
        "Contains AI hedging ('I'd be happy to...')",
        5,
    ),
]


def find_line_number(text: str, match_start: int) -> int:
    """Return the 1-based line number for a character position."""
    return text[:match_start].count("\n") + 1


def check_em_dash_abuse(text: str) -> list[dict]:
    """Check for excessive em-dash usage."""
    findings = []
    paragraphs = text.split("\n\n")
    em_dash_pattern = re.compile(r"[\u2014]|---?")

    total_em_dashes = len(em_dash_pattern.findall(text))
    if total_em_dashes > 3:
        findings.append(
            {
                "pattern": "em_dash_overuse",
                "severity": "warning",
                "description": f"Excessive em-dash usage: {total_em_dashes} found (max 3 recommended)",
                "line": None,
                "penalty": 5,
            }
        )

    # Check for multiple em-dashes in same paragraph
    current_line = 1
    for para in paragraphs:
        count = len(em_dash_pattern.findall(para))
        if count >= 2:
            findings.append(
                {
                    "pattern": "em_dash_paragraph_cluster",
                    "severity": "suggestion",
                    "description": f"Multiple em-dashes ({count}) in single paragraph",
                    "line": current_line,
                    "penalty": 2,
                }
            )
        current_line += para.count("\n") + 2  # +2 for the blank line between paragraphs

    return findings


def check_paragraph_uniformity(text: str) -> list[dict]:
    """Check for monotonous paragraph lengths."""
    findings = []
    # Split on double newlines, ignore empty and heading-only paragraphs
    paragraphs = [
        p.strip()
        for p in text.split("\n\n")
        if p.strip() and not p.strip().startswith("#")
    ]

    if len(paragraphs) < 4:
        return findings

    # Count sentences per paragraph (rough: split on . ! ?)
    sentence_counts = []
    for para in paragraphs:
        sentences = re.split(r"[.!?]+\s", para)
        sentence_counts.append(len(sentences))

    if not sentence_counts:
        return findings

    # Check if all paragraphs have the same sentence count (within 1)
    avg = sum(sentence_counts) / len(sentence_counts)
    variance = sum((c - avg) ** 2 for c in sentence_counts) / len(sentence_counts)

    if variance < 0.5 and len(sentence_counts) > 3:
        findings.append(
            {
                "pattern": "uniform_paragraph_length",
                "severity": "warning",
                "description": f"Paragraphs have uniform length (avg {avg:.1f} sentences, variance {variance:.2f}). Vary paragraph lengths for better rhythm.",
                "line": None,
                "penalty": 5,
            }
        )

    return findings


def check_passive_voice(text: str) -> list[dict]:
    """Rough check for passive voice overuse."""
    findings = []
    # Simple heuristic: "was/were/is/are/been/being + past participle"
    passive_pattern = re.compile(
        r"\b(was|were|is|are|been|being|be)\s+(\w+ed|written|taken|given|shown|known|made|done|seen|found|built|sent|told|held|run|set|put|cut|let|read)\b",
        re.IGNORECASE,
    )

    sentences = re.split(r"[.!?]+\s", text)
    total_sentences = len(sentences)
    passive_count = 0
    passive_lines = []

    for sentence in sentences:
        if passive_pattern.search(sentence):
            passive_count += 1
            # Find line number of this sentence in the original text
            match = re.search(re.escape(sentence[:50]), text)
            if match:
                passive_lines.append(find_line_number(text, match.start()))

    if total_sentences > 0:
        passive_ratio = passive_count / total_sentences
        if passive_ratio > 0.2:
            findings.append(
                {
                    "pattern": "passive_voice_overuse",
                    "severity": "warning",
                    "description": f"Passive voice in {passive_count}/{total_sentences} sentences ({passive_ratio:.0%}). Target is under 20%.",
                    "line": passive_lines[0] if passive_lines else None,
                    "penalty": 5,
                }
            )

    return findings


def check_file(filepath: str, verbose: bool = False) -> dict:
    """Run all slop checks on a file and return a JSON-serializable report."""
    path = Path(filepath)
    if not path.exists():
        return {"error": f"File not found: {filepath}"}

    text = path.read_text(encoding="utf-8")
    patterns_found = []

    # Run regex pattern checks
    for name, pattern, severity, description, penalty in SLOP_PATTERNS:
        for match in re.finditer(pattern, text, re.MULTILINE):
            line_num = find_line_number(text, match.start())
            matched_text = match.group(0).strip()
            if len(matched_text) > 80:
                matched_text = matched_text[:77] + "..."
            patterns_found.append(
                {
                    "pattern": name,
                    "severity": severity,
                    "description": description,
                    "line": line_num,
                    "matched_text": matched_text,
                    "penalty": penalty,
                }
            )

    # Run structural checks
    patterns_found.extend(check_em_dash_abuse(text))
    patterns_found.extend(check_paragraph_uniformity(text))
    patterns_found.extend(check_passive_voice(text))

    # Calculate total score (start at 100, subtract penalties, floor at 0)
    total_penalty = sum(p["penalty"] for p in patterns_found)
    total_score = max(0, 100 - total_penalty)

    # Count by severity
    severity_counts = {"critical": 0, "warning": 0, "suggestion": 0}
    for p in patterns_found:
        severity_counts[p["severity"]] = severity_counts.get(p["severity"], 0) + 1

    report = {
        "file": str(path),
        "total_score": total_score,
        "total_patterns_found": len(patterns_found),
        "severity_counts": severity_counts,
        "passed": total_score >= 70 and severity_counts["critical"] == 0,
        "patterns_found": patterns_found,
    }

    return report


def main():
    parser = argparse.ArgumentParser(
        description="Check text files for AI slop patterns."
    )
    parser.add_argument("input_file", help="Path to the text file to check")
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Print detailed findings to stderr",
    )
    parser.add_argument(
        "--threshold",
        "-t",
        type=int,
        default=70,
        help="Minimum passing score (default: 70)",
    )

    args = parser.parse_args()
    report = check_file(args.input_file, verbose=args.verbose)

    if "error" in report:
        print(json.dumps(report, indent=2))
        sys.exit(1)

    print(json.dumps(report, indent=2))

    if args.verbose:
        score = report["total_score"]
        count = report["total_patterns_found"]
        print(f"\n--- Anti-Slop Report ---", file=sys.stderr)
        print(f"Score: {score}/100", file=sys.stderr)
        print(f"Patterns found: {count}", file=sys.stderr)
        for p in report["patterns_found"]:
            line_info = f"line {p['line']}" if p["line"] else "global"
            print(
                f"  [{p['severity'].upper()}] {p['description']} ({line_info})",
                file=sys.stderr,
            )
        if report["passed"]:
            print("Result: PASSED", file=sys.stderr)
        else:
            print("Result: FAILED", file=sys.stderr)

    sys.exit(0 if report["passed"] else 1)


if __name__ == "__main__":
    main()
