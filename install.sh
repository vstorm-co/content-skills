#!/usr/bin/env bash
# install.sh — Install content-skills pack
#
# Installs to BOTH ~/.claude/ and ~/.agents/ so the same skills work with
# Claude Code, Codex, and any AGENTS.md-compatible agent CLI.
#
# One-command install:
#   curl -fsSL https://raw.githubusercontent.com/vstorm-co/content-skills/main/install.sh | bash
#
# Or from local clone:
#   git clone https://github.com/vstorm-co/content-skills.git
#   cd content-skills && ./install.sh

set -euo pipefail

# ── Colors ──────────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
DIM='\033[2m'
NC='\033[0m'

success() { echo -e "  ${GREEN}✓${NC} $1"; }
warn()    { echo -e "  ${YELLOW}⚠${NC} $1"; }
fail()    { echo -e "  ${RED}✗${NC} $1"; }
info()    { echo -e "  ${BLUE}→${NC} $1"; }

# ── Detect mode ─────────────────────────────────────────────────────────
INTERACTIVE=true
if [ ! -t 0 ]; then
    INTERACTIVE=false
fi

echo ""
echo -e "${BOLD}content-skills installer${NC}"
echo -e "${DIM}Content studio with YOUR brand baked in${NC}"
echo ""

# ── Prerequisites ───────────────────────────────────────────────────────
echo -e "${BOLD}Checking prerequisites...${NC}"

# Python 3.10+
PYTHON_CMD=""
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
fi

if [ -n "$PYTHON_CMD" ]; then
    PY_VERSION=$($PYTHON_CMD -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')" 2>/dev/null || echo "0.0")
    PY_MAJOR=$(echo "$PY_VERSION" | cut -d. -f1)
    PY_MINOR=$(echo "$PY_VERSION" | cut -d. -f2)
    if [ "$PY_MAJOR" -ge 3 ] && [ "$PY_MINOR" -ge 10 ]; then
        success "Python ${PY_VERSION}"
    else
        warn "Python ${PY_VERSION} found (3.10+ recommended). Scripts may not work."
    fi
else
    warn "Python not found. Scripts in scripts/ won't work without it."
fi

# Git
if command -v git &>/dev/null; then
    success "Git $(git --version | cut -d' ' -f3)"
else
    fail "Git not found. Required for remote install."
    if [ "$INTERACTIVE" = false ]; then
        echo -e "  ${RED}Install git and try again.${NC}"
        exit 1
    fi
fi

# Agent CLI detection (informational)
DETECTED_CLIS=()
if command -v claude &>/dev/null; then
    DETECTED_CLIS+=("Claude Code")
fi
if command -v codex &>/dev/null; then
    DETECTED_CLIS+=("Codex")
fi
if [ "${#DETECTED_CLIS[@]}" -gt 0 ]; then
    success "Detected agent CLI(s): ${DETECTED_CLIS[*]}"
else
    warn "No agent CLI detected. Skills will be ready when you install one (Claude Code, Codex, etc.)."
fi

echo ""

# ── Determine source ────────────────────────────────────────────────────
REPO_DIR=""
TEMP_DIR=""

if [ -n "${BASH_SOURCE[0]:-}" ] && [ -f "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/content/SKILL.md" ]; then
    REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    info "Installing from local directory: ${REPO_DIR}"
else
    info "Cloning content-skills from GitHub..."
    TEMP_DIR=$(mktemp -d)
    if git clone --depth 1 https://github.com/vstorm-co/content-skills.git "$TEMP_DIR" 2>/dev/null; then
        REPO_DIR="$TEMP_DIR"
        success "Repository cloned"
    else
        fail "Failed to clone repository"
        echo -e "  ${RED}Check your internet connection and try again.${NC}"
        exit 1
    fi
fi

# ── Install to each target (Claude Code + AGENTS.md spec) ──────────────
# Mirror the same install into both ~/.claude/ and ~/.agents/ so skills
# work with any agent CLI that follows either convention.
TARGET_BASES=("${HOME}/.claude" "${HOME}/.agents")

skill_count_total=0
agent_count_total=0
script_count_total=0

for BASE_DIR in "${TARGET_BASES[@]}"; do
    SKILLS_TARGET="${BASE_DIR}/skills"
    AGENTS_TARGET="${BASE_DIR}/agents"
    SCRIPTS_TARGET="${SKILLS_TARGET}/content-scripts"
    STYLES_TARGET="${SKILLS_TARGET}/content-styles"

    mkdir -p "$SKILLS_TARGET"
    mkdir -p "$AGENTS_TARGET"

    echo -e "${BOLD}Installing to ${BASE_DIR}...${NC}"

    skill_count=0
    agent_count=0
    script_count=0

    # Main router
    if [ -f "${REPO_DIR}/content/SKILL.md" ]; then
        cp "${REPO_DIR}/content/SKILL.md" "${SKILLS_TARGET}/content.md"
        success "content (main router)"
        skill_count=$((skill_count + 1))
    fi

    # Sub-skills
    if [ -d "${REPO_DIR}/skills" ]; then
        for skill_dir in "${REPO_DIR}/skills"/*/; do
            skill_name="$(basename "${skill_dir}")"
            skill_file="${skill_dir}SKILL.md"
            if [ -f "${skill_file}" ]; then
                mkdir -p "${SKILLS_TARGET}/${skill_name}"
                cp -r "${skill_dir}"* "${SKILLS_TARGET}/${skill_name}/"
                cp "${skill_file}" "${SKILLS_TARGET}/${skill_name}.md"
                success "${skill_name}"
                skill_count=$((skill_count + 1))
            fi
        done
    fi

    # Agents
    if [ -d "${REPO_DIR}/agents" ]; then
        for agent_file in "${REPO_DIR}/agents"/*.md; do
            if [ -f "${agent_file}" ]; then
                agent_name="$(basename "${agent_file}")"
                cp "${agent_file}" "${AGENTS_TARGET}/${agent_name}"
                agent_count=$((agent_count + 1))
            fi
        done
    fi
    if [ "$agent_count" -gt 0 ]; then
        success "${agent_count} agents"
    fi

    # Scripts
    if [ -d "${REPO_DIR}/scripts" ]; then
        mkdir -p "$SCRIPTS_TARGET"
        for script_file in "${REPO_DIR}/scripts"/*.py; do
            if [ -f "${script_file}" ]; then
                cp "${script_file}" "${SCRIPTS_TARGET}/"
                chmod +x "${SCRIPTS_TARGET}/$(basename "${script_file}")" 2>/dev/null || true
                script_count=$((script_count + 1))
            fi
        done
    fi
    if [ "$script_count" -gt 0 ]; then
        success "${script_count} Python scripts"
    fi

    # Styles
    if [ -d "${REPO_DIR}/styles" ]; then
        mkdir -p "$STYLES_TARGET"
        cp "${REPO_DIR}/styles"/*.json "$STYLES_TARGET/" 2>/dev/null || true
        success "Style tokens (typography, palettes, layouts)"
    fi

    skill_count_total=$((skill_count_total + skill_count))
    agent_count_total=$((agent_count_total + agent_count))
    script_count_total=$((script_count_total + script_count))

    echo ""
done

# ── Scaffold brand directory ────────────────────────────────────────────
echo -e "${BOLD}Setting up brand directory...${NC}"

BRAND_DIR="${REPO_DIR}/brand"
brand_new=false

if [ ! -d "${BRAND_DIR}" ]; then
    mkdir -p "${BRAND_DIR}"
    brand_new=true
fi

for subdir in assets fonts logo palettes voice-samples; do
    mkdir -p "${BRAND_DIR}/${subdir}"
done

if [ "$brand_new" = true ]; then
    success "Brand directory created at ${BRAND_DIR}"
else
    success "Brand directory verified at ${BRAND_DIR}"
fi

echo ""

# ── Python dependencies ─────────────────────────────────────────────────
if [ -n "$PYTHON_CMD" ] && [ -f "${REPO_DIR}/requirements.txt" ]; then
    echo -e "${BOLD}Installing Python dependencies...${NC}"
    if $PYTHON_CMD -m pip install --user -q -r "${REPO_DIR}/requirements.txt" 2>/dev/null; then
        success "Python dependencies installed"
    else
        warn "Could not install Python dependencies automatically"
        info "Run manually: pip install -r requirements.txt"
    fi
    echo ""
fi

# ── Cleanup temp dir ────────────────────────────────────────────────────
if [ -n "$TEMP_DIR" ] && [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi

# ── Summary ─────────────────────────────────────────────────────────────
echo -e "${GREEN}╔══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   ${BOLD}Installation Complete!${NC}${GREEN}                  ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════╝${NC}"
echo ""
echo -e "  Installed to:  ${BOLD}~/.claude/${NC} and ${BOLD}~/.agents/${NC}"
echo -e "  Works with:    ${BOLD}Claude Code, Codex, and any AGENTS.md-compatible CLI${NC}"
echo -e "  Skills:        ${BOLD}${skill_count_total}${NC} files (across both targets)"
echo -e "  Agents:        ${BOLD}${agent_count_total}${NC} subagents"
echo -e "  Scripts:       ${BOLD}${script_count_total}${NC} Python utilities"
echo ""
echo -e "  ${BOLD}Quick Start:${NC}"
echo -e "    Open your agent CLI and try:"
echo ""
echo -e "    ${DIM}/content setup${NC}                          Set up your brand"
echo -e "    ${DIM}/content blog \"your topic here\"${NC}         Write a blog post"
echo -e "    ${DIM}/content twitter \"your topic here\"${NC}      Create an X thread"
echo -e "    ${DIM}/content presentation \"your brief\"${NC}      Generate slides"
echo -e "    ${DIM}/content audit <draft>${NC}                  Check for AI slop"
echo ""
echo -e "  ${BOLD}All Commands:${NC}"
echo -e "    /content setup              Interactive brand onboarding"
echo -e "    /content blog <brief>       Long-form blog post"
echo -e "    /content twitter <topic>    X thread or single"
echo -e "    /content linkedin <topic>   LinkedIn post"
echo -e "    /content reddit <topic>     Subreddit-aware post"
echo -e "    /content hn <project>       Show HN post"
echo -e "    /content presentation       Slidev / Reveal.js / Spectacle"
echo -e "    /content infographic        SVG infographic"
echo -e "    /content image <prompt>     Image prompt engineering"
echo -e "    /content video <brief>      Remotion video + storyboard"
echo -e "    /content plan <topic>       30-day editorial calendar"
echo -e "    /content repurpose <src>    1 format → 5+ formats"
echo -e "    /content audit <draft>      Anti-slop + brand check"
echo -e "    /content series <theme>     10-post connected series"
echo -e "    /content score              Quick ship-readiness check"
echo ""
echo -e "  ${DIM}Documentation: https://github.com/vstorm-co/content-skills${NC}"
echo -e "  ${DIM}To uninstall:  bash uninstall.sh${NC}"
echo ""
