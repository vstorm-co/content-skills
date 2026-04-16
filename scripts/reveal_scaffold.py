#!/usr/bin/env python3
"""Scaffold a Reveal.js presentation project.

Creates a directory with index.html, CSS, and brand integration
derived from brand/VISUAL.md if available.

Usage:
    python scripts/reveal_scaffold.py my-presentation
    python scripts/reveal_scaffold.py my-deck --brand-dir ./brand --title "Q4 Strategy"
"""

import argparse
import json
import re
import sys
from pathlib import Path


def read_brand_visual(brand_dir: str) -> dict:
    """Read brand/VISUAL.md and extract colors and typography."""
    visual_path = Path(brand_dir) / "VISUAL.md"
    brand = {
        "primary": "#1a1a2e",
        "secondary": "#16213e",
        "accent": "#0f3460",
        "text": "#e4e4e4",
        "background": "#0a0a0a",
        "font_display": "Space Grotesk",
        "font_body": "Inter",
        "font_mono": "JetBrains Mono",
    }

    if not visual_path.exists():
        return brand

    text = visual_path.read_text(encoding="utf-8")

    color_mappings = {
        "primary": r"(?i)primary[^\n]*?(#[0-9a-fA-F]{6})",
        "secondary": r"(?i)secondary[^\n]*?(#[0-9a-fA-F]{6})",
        "accent": r"(?i)accent[^\n]*?(#[0-9a-fA-F]{6})",
        "text": r"(?i)(?:text|foreground)[^\n]*?(#[0-9a-fA-F]{6})",
        "background": r"(?i)background[^\n]*?(#[0-9a-fA-F]{6})",
    }

    for key, pattern in color_mappings.items():
        match = re.search(pattern, text)
        if match:
            brand[key] = match.group(1)

    font_match = re.search(r"(?i)(?:display|heading)\s*(?:font|typeface)[^\n]*?:\s*([A-Z][A-Za-z\s]+)", text)
    if font_match:
        brand["font_display"] = font_match.group(1).strip()

    font_match = re.search(r"(?i)body\s*(?:font|typeface)[^\n]*?:\s*([A-Z][A-Za-z\s]+)", text)
    if font_match:
        brand["font_body"] = font_match.group(1).strip()

    return brand


def generate_index_html(title: str, brand: dict) -> str:
    """Generate the main index.html for Reveal.js."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reset.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/theme/black.css" id="theme">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/monokai.css">
    <link rel="stylesheet" href="css/brand.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">

            <!-- Title Slide -->
            <section>
                <h1>{title}</h1>
                <p class="subtitle">Subtitle goes here</p>
            </section>

            <!-- Agenda -->
            <section>
                <h2>Agenda</h2>
                <ul>
                    <li class="fragment">Point one</li>
                    <li class="fragment">Point two</li>
                    <li class="fragment">Point three</li>
                    <li class="fragment">Point four</li>
                </ul>
            </section>

            <!-- Section One -->
            <section>
                <h2>Section One</h2>
                <p>Content goes here. Replace with your actual content.</p>
                <ul>
                    <li>Key point with supporting detail</li>
                    <li>Another point backed by evidence</li>
                    <li>A third point that advances the argument</li>
                </ul>
            </section>

            <!-- Section Two -->
            <section>
                <h2>Section Two</h2>
                <p>More content here.</p>
                <pre><code data-trim data-noescape class="python">
# Code examples render with syntax highlighting
def example():
    return "Reveal.js supports code blocks natively"
                </code></pre>
            </section>

            <!-- Key Takeaway -->
            <section data-background="{brand['secondary']}">
                <h2>Key Takeaway</h2>
                <p>The single most important thing the audience should remember.</p>
            </section>

            <!-- Closing -->
            <section>
                <h2>Thank You</h2>
                <p><a href="https://example.com">Learn more</a></p>
            </section>

        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/notes/notes.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/markdown/markdown.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@5/plugin/highlight/highlight.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            transition: 'slide',
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
        }});
    </script>
</body>
</html>
"""


def generate_brand_css(brand: dict) -> str:
    """Generate brand-aligned CSS overrides for Reveal.js."""
    return f"""/* Brand-aligned Reveal.js styles
 * Generated by content-skills scaffold
 * Customize these values or replace with brand/VISUAL.md overrides
 */

:root {{
  --r-background-color: {brand['background']};
  --r-main-font: '{brand['font_body']}', ui-sans-serif, system-ui, sans-serif;
  --r-main-font-size: 38px;
  --r-main-color: {brand['text']};
  --r-heading-font: '{brand['font_display']}', ui-sans-serif, system-ui, sans-serif;
  --r-heading-color: {brand['primary']};
  --r-heading-text-transform: none;
  --r-heading-font-weight: 700;
  --r-code-font: '{brand['font_mono']}', ui-monospace, monospace;
  --r-link-color: {brand['accent']};
  --r-link-color-hover: {brand['primary']};
  --r-selection-background-color: {brand['accent']};
}}

/* Heading sizes */
.reveal h1 {{
  font-size: 2.5em;
}}

.reveal h2 {{
  font-size: 1.75em;
}}

.reveal h3 {{
  font-size: 1.25em;
}}

/* Subtitle styling */
.reveal .subtitle {{
  color: {brand['secondary']};
  font-size: 1.25em;
  margin-top: 0.5em;
}}

/* List styling */
.reveal ul,
.reveal ol {{
  text-align: left;
  margin-left: 1em;
}}

.reveal li {{
  margin-bottom: 0.5em;
  line-height: 1.4;
}}

/* Code blocks */
.reveal pre {{
  font-size: 0.7em;
  border-radius: 8px;
  box-shadow: none;
}}

.reveal code {{
  font-family: var(--r-code-font);
}}

/* Fragment animation */
.reveal .fragment {{
  transition: all 0.3s ease;
}}

/* Accent backgrounds */
.reveal section[data-background] h2 {{
  color: {brand['text']};
}}
"""


def scaffold(project_name: str, brand_dir: str = "brand", title: str | None = None):
    """Create the Reveal.js project directory structure."""
    project_path = Path(project_name)

    if project_path.exists():
        return {"error": f"Directory already exists: {project_name}"}

    display_title = title or project_name.replace("-", " ").replace("_", " ").title()
    brand = read_brand_visual(brand_dir)

    # Create directories
    project_path.mkdir(parents=True)
    (project_path / "css").mkdir()

    # Write files
    (project_path / "index.html").write_text(generate_index_html(display_title, brand))
    (project_path / "css" / "brand.css").write_text(generate_brand_css(brand))

    # Create .gitignore
    (project_path / ".gitignore").write_text("node_modules/\n")

    files_created = [
        str(project_path / "index.html"),
        str(project_path / "css" / "brand.css"),
        str(project_path / ".gitignore"),
    ]

    return {
        "project": project_name,
        "title": display_title,
        "path": str(project_path.resolve()),
        "files_created": files_created,
        "brand_source": str(Path(brand_dir) / "VISUAL.md") if (Path(brand_dir) / "VISUAL.md").exists() else "defaults",
        "next_steps": [
            f"cd {project_name}",
            "Open index.html in a browser",
            "Or use: npx serve .",
        ],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a Reveal.js presentation project."
    )
    parser.add_argument("project_name", help="Name of the project directory to create")
    parser.add_argument(
        "--brand-dir",
        "-b",
        default="brand",
        help="Path to brand directory (default: brand/)",
    )
    parser.add_argument(
        "--title",
        "-t",
        default=None,
        help="Presentation title (default: derived from project name)",
    )

    args = parser.parse_args()
    result = scaffold(args.project_name, args.brand_dir, args.title)

    if "error" in result:
        print(json.dumps(result, indent=2))
        sys.exit(1)

    print(json.dumps(result, indent=2))
    print(f"\nProject scaffolded at: {result['path']}", file=sys.stderr)
    print("Next steps:", file=sys.stderr)
    for step in result["next_steps"]:
        print(f"  {step}", file=sys.stderr)


if __name__ == "__main__":
    main()
