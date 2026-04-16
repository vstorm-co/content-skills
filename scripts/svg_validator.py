#!/usr/bin/env python3
"""Validate SVG files for quality and accessibility.

Checks: well-formed XML, no external references, reasonable file size,
embedded fonts detection, and accessibility elements (title/desc).

Usage:
    python scripts/svg_validator.py <svg_file>
    python scripts/svg_validator.py assets/infographic.svg --max-size 500
"""

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


# SVG namespace
SVG_NS = "http://www.w3.org/2000/svg"
XLINK_NS = "http://www.w3.org/1999/xlink"

# Default max file size in KB
DEFAULT_MAX_SIZE_KB = 500

# Patterns for external references
EXTERNAL_REF_PATTERNS = [
    re.compile(r'(?:href|src)\s*=\s*["\']https?://', re.IGNORECASE),
    re.compile(r'url\s*\(\s*["\']?https?://', re.IGNORECASE),
    re.compile(r'xlink:href\s*=\s*["\']https?://', re.IGNORECASE),
]

# Patterns for embedded JavaScript (potential security issue)
SCRIPT_PATTERNS = [
    re.compile(r"<script[\s>]", re.IGNORECASE),
    re.compile(r"\bon\w+\s*=", re.IGNORECASE),  # onclick, onload, etc.
]


def check_well_formed(filepath: Path) -> dict:
    """Check if the SVG is well-formed XML."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()

        # Check root element is svg
        tag = root.tag
        is_svg = tag == "svg" or tag.endswith("}svg")

        return {
            "check": "well_formed_xml",
            "passed": True,
            "is_svg_root": is_svg,
            "root_tag": tag,
            "description": "Valid XML" + (" with SVG root element" if is_svg else " but root is not <svg>"),
        }
    except ET.ParseError as e:
        return {
            "check": "well_formed_xml",
            "passed": False,
            "error": str(e),
            "description": f"XML parse error: {e}",
        }


def check_external_references(text: str) -> dict:
    """Check for external URL references."""
    findings = []

    for pattern in EXTERNAL_REF_PATTERNS:
        for match in pattern.finditer(text):
            line_num = text[: match.start()].count("\n") + 1
            findings.append(
                {
                    "line": line_num,
                    "matched_text": match.group(0).strip()[:80],
                }
            )

    return {
        "check": "no_external_references",
        "passed": len(findings) == 0,
        "external_refs_found": len(findings),
        "findings": findings,
        "description": (
            "No external references found"
            if len(findings) == 0
            else f"{len(findings)} external reference(s) found"
        ),
    }


def check_file_size(filepath: Path, max_size_kb: int) -> dict:
    """Check that file size is reasonable."""
    size_bytes = filepath.stat().st_size
    size_kb = size_bytes / 1024

    return {
        "check": "file_size",
        "passed": size_kb <= max_size_kb,
        "size_bytes": size_bytes,
        "size_kb": round(size_kb, 1),
        "max_allowed_kb": max_size_kb,
        "description": (
            f"File size {size_kb:.1f} KB (within {max_size_kb} KB limit)"
            if size_kb <= max_size_kb
            else f"File size {size_kb:.1f} KB exceeds {max_size_kb} KB limit"
        ),
    }


def check_embedded_fonts(text: str) -> dict:
    """Check for embedded font definitions."""
    # Look for @font-face declarations
    font_face_matches = re.findall(r"@font-face\s*\{[^}]*\}", text, re.DOTALL)

    # Look for font-family declarations on text elements
    font_families = re.findall(r'font-family\s*[:=]\s*["\']?([^"\';\}]+)', text)
    unique_fonts = list(set(f.strip() for f in font_families))

    has_embedded = len(font_face_matches) > 0

    return {
        "check": "embedded_fonts",
        "has_embedded_fonts": has_embedded,
        "embedded_font_count": len(font_face_matches),
        "font_families_used": unique_fonts,
        "description": (
            f"{len(font_face_matches)} embedded @font-face declaration(s), "
            f"{len(unique_fonts)} font families used: {', '.join(unique_fonts) if unique_fonts else 'none'}"
        ),
        # Not a pass/fail -- informational
        "passed": True,
    }


def check_accessibility(filepath: Path) -> dict:
    """Check for accessibility elements: title and desc."""
    try:
        tree = ET.parse(filepath)
        root = tree.getroot()
    except ET.ParseError:
        return {
            "check": "accessibility",
            "passed": False,
            "description": "Cannot check accessibility: XML parse error",
        }

    # Check for <title> element
    title_elem = root.find(f"{{{SVG_NS}}}title") or root.find("title")
    has_title = title_elem is not None
    title_text = title_elem.text.strip() if title_elem is not None and title_elem.text else None

    # Check for <desc> element
    desc_elem = root.find(f"{{{SVG_NS}}}desc") or root.find("desc")
    has_desc = desc_elem is not None
    desc_text = desc_elem.text.strip() if desc_elem is not None and desc_elem.text else None

    # Check for role attribute on root
    has_role = root.get("role") is not None

    # Check for aria-label on root
    has_aria_label = root.get("aria-label") is not None or root.get("aria-labelledby") is not None

    passed = has_title and has_desc

    issues = []
    if not has_title:
        issues.append("Missing <title> element (required for screen readers)")
    elif not title_text:
        issues.append("<title> element is empty")
    if not has_desc:
        issues.append("Missing <desc> element (recommended for accessibility)")
    elif not desc_text:
        issues.append("<desc> element is empty")
    if not has_role and not has_aria_label:
        issues.append("Consider adding role='img' and aria-label to the <svg> element")

    return {
        "check": "accessibility",
        "passed": passed,
        "has_title": has_title,
        "title_text": title_text,
        "has_desc": has_desc,
        "desc_text": desc_text[:100] if desc_text else None,
        "has_role": has_role,
        "has_aria_label": has_aria_label,
        "issues": issues,
        "description": (
            "Accessibility checks passed"
            if passed
            else f"{len(issues)} accessibility issue(s) found"
        ),
    }


def check_scripts(text: str) -> dict:
    """Check for embedded JavaScript (potential security concern)."""
    findings = []

    for pattern in SCRIPT_PATTERNS:
        for match in pattern.finditer(text):
            line_num = text[: match.start()].count("\n") + 1
            findings.append(
                {
                    "line": line_num,
                    "matched_text": match.group(0).strip()[:80],
                }
            )

    return {
        "check": "no_scripts",
        "passed": len(findings) == 0,
        "scripts_found": len(findings),
        "findings": findings,
        "description": (
            "No embedded scripts found"
            if len(findings) == 0
            else f"{len(findings)} embedded script(s) or event handler(s) found"
        ),
    }


def validate_svg(filepath: str, max_size_kb: int = DEFAULT_MAX_SIZE_KB) -> dict:
    """Run all validation checks on an SVG file."""
    path = Path(filepath)

    if not path.exists():
        return {"error": f"File not found: {filepath}"}

    if path.suffix.lower() != ".svg":
        return {"error": f"Not an SVG file: {filepath}"}

    text = path.read_text(encoding="utf-8")

    checks = []
    checks.append(check_well_formed(path))
    checks.append(check_external_references(text))
    checks.append(check_file_size(path, max_size_kb))
    checks.append(check_embedded_fonts(text))
    checks.append(check_accessibility(path))
    checks.append(check_scripts(text))

    all_passed = all(c["passed"] for c in checks)
    failed_checks = [c["check"] for c in checks if not c["passed"]]

    report = {
        "file": str(path),
        "valid": all_passed,
        "checks_run": len(checks),
        "checks_passed": sum(1 for c in checks if c["passed"]),
        "checks_failed": failed_checks,
        "checks": checks,
    }

    return report


def main():
    parser = argparse.ArgumentParser(description="Validate SVG files.")
    parser.add_argument("svg_file", help="Path to the SVG file to validate")
    parser.add_argument(
        "--max-size",
        type=int,
        default=DEFAULT_MAX_SIZE_KB,
        help=f"Maximum file size in KB (default: {DEFAULT_MAX_SIZE_KB})",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print summary to stderr"
    )

    args = parser.parse_args()
    report = validate_svg(args.svg_file, args.max_size)

    if "error" in report:
        print(json.dumps(report, indent=2))
        sys.exit(1)

    print(json.dumps(report, indent=2))

    if args.verbose:
        print(f"\n--- SVG Validation Report ---", file=sys.stderr)
        print(f"File: {report['file']}", file=sys.stderr)
        print(
            f"Result: {'VALID' if report['valid'] else 'INVALID'}",
            file=sys.stderr,
        )
        print(
            f"Checks: {report['checks_passed']}/{report['checks_run']} passed",
            file=sys.stderr,
        )
        for check in report["checks"]:
            status = "PASS" if check["passed"] else "FAIL"
            print(f"  [{status}] {check['check']}: {check['description']}", file=sys.stderr)

    sys.exit(0 if report["valid"] else 1)


if __name__ == "__main__":
    main()
