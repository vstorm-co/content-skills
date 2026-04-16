#!/usr/bin/env bash
# uninstall.sh — Remove content-skills pack
#
# Removes skills, agents, and scripts from BOTH ~/.claude/ and ~/.agents/.
# Does NOT delete your brand/ directory (that's your data).
#
# Usage:
#   bash uninstall.sh

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
info()    { echo -e "  ${BLUE}→${NC} $1"; }

TARGET_BASES=("${HOME}/.claude" "${HOME}/.agents")

echo ""
echo -e "${BOLD}content-skills uninstaller${NC}"
echo ""

# ── Confirmation ────────────────────────────────────────────────────────
if [ -t 0 ]; then
    echo -e "This will remove all content-skills from ${BOLD}~/.claude/${NC} and ${BOLD}~/.agents/${NC}"
    echo -e "Your ${BOLD}brand/${NC} directory will ${GREEN}NOT${NC} be deleted."
    echo ""
    read -rp "Continue? (y/n): " confirm
    if [[ "$confirm" != [yY]* ]]; then
        echo "Cancelled."
        exit 0
    fi
    echo ""
fi

removed_total=0
agent_removed_total=0

for BASE_DIR in "${TARGET_BASES[@]}"; do
    SKILLS_TARGET="${BASE_DIR}/skills"
    AGENTS_TARGET="${BASE_DIR}/agents"
    SCRIPTS_TARGET="${SKILLS_TARGET}/content-scripts"
    STYLES_TARGET="${SKILLS_TARGET}/content-styles"

    echo -e "${BOLD}Removing from ${BASE_DIR}...${NC}"

    removed=0
    agent_removed=0

    # Main router
    if [ -f "${SKILLS_TARGET}/content.md" ]; then
        rm -f "${SKILLS_TARGET}/content.md"
        success "content (main router)"
        removed=$((removed + 1))
    fi

    # Sub-skill files and directories
    for item in "${SKILLS_TARGET}"/content-*; do
        if [ -e "$item" ]; then
            name="$(basename "$item")"
            if [ "$name" = "content-scripts" ] || [ "$name" = "content-styles" ]; then
                continue
            fi
            rm -rf "$item"
            success "${name%.md}"
            removed=$((removed + 1))
        fi
    done

    # Agents
    for agent_file in "${AGENTS_TARGET}"/content-*.md; do
        if [ -f "${agent_file}" ]; then
            name="$(basename "${agent_file}" .md)"
            rm -f "${agent_file}"
            success "${name}"
            agent_removed=$((agent_removed + 1))
        fi
    done

    if [ "$agent_removed" -eq 0 ]; then
        info "No agent files found in ${AGENTS_TARGET}"
    fi

    # Scripts + styles
    if [ -d "$SCRIPTS_TARGET" ]; then
        rm -rf "$SCRIPTS_TARGET"
        success "Python scripts"
    fi

    if [ -d "$STYLES_TARGET" ]; then
        rm -rf "$STYLES_TARGET"
        success "Style tokens"
    fi

    removed_total=$((removed_total + removed))
    agent_removed_total=$((agent_removed_total + agent_removed))

    echo ""
done

# ── Summary ─────────────────────────────────────────────────────────────
echo -e "${GREEN}╔══════════════════════════════════════════╗${NC}"
echo -e "${GREEN}║   ${BOLD}Uninstall Complete${NC}${GREEN}                      ║${NC}"
echo -e "${GREEN}╚══════════════════════════════════════════╝${NC}"
echo ""
echo -e "  ${BOLD}Removed:${NC}"
echo -e "    ${removed_total} skill files"
echo -e "    ${agent_removed_total} agent files"
echo -e "    Scripts and style tokens"
echo ""
echo -e "  ${YELLOW}${BOLD}Your brand/ directory was NOT deleted.${NC}"
echo -e "  ${DIM}If you want to remove it, delete it manually:${NC}"
echo -e "  ${DIM}  rm -rf brand/${NC}"
echo ""
echo -e "  ${DIM}To remove Python dependencies:${NC}"
echo -e "  ${DIM}  pip uninstall -r requirements.txt${NC}"
echo ""
echo -e "  ${DIM}To reinstall: bash install.sh${NC}"
echo ""
