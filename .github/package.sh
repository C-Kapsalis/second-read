#!/bin/sh
# Build the release zips into dist/ (the release workflow attaches them to the
# GitHub Release; run it by hand with: sh .github/package.sh).
#
#   second-read.zip         the skill: one second-read/ folder with SKILL.md,
#                           for Customize > Skills in Claude, the Skills tab in
#                           ChatGPT, or any agent's skills folder.
#   second-read-plugin.zip  the Claude plugin: .claude-plugin/ plus the skill
#                           at the zip root, for Customize > Plugins in Claude.
#
# POSIX sh; needs only `zip`.
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
DIST="$ROOT/dist"
STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT INT TERM

command -v zip >/dev/null 2>&1 || { echo "package.sh: zip not found" >&2; exit 1; }
rm -rf "$DIST"
mkdir -p "$DIST"

# The skill: exactly what the repo holds at its root, minus the repo's own files.
copy_skill() {
  mkdir -p "$1"
  cp "$ROOT/SKILL.md" "$ROOT/LICENSE" "$1/"
  cp -R "$ROOT/references" "$ROOT/scripts" "$ROOT/assets" "$ROOT/agents" "$1/"
  find "$1" \( -name '.DS_Store' -o -name '__pycache__' \) -exec rm -rf {} +
}

copy_skill "$STAGE/skill/second-read"
(cd "$STAGE/skill" && zip -qrX "$DIST/second-read.zip" .)

# Portable, skills-only package for the ChatGPT/Codex public plugin directory.
mkdir -p "$STAGE/openai/skills" "$STAGE/openai/assets"
cp "$ROOT/plugin.json" "$STAGE/openai/"
cp "$ROOT/LICENSE" "$ROOT/README.md" "$STAGE/openai/"
cp "$ROOT/.claude-plugin/icon.png" "$STAGE/openai/assets/icon.png"
copy_skill "$STAGE/openai/skills/second-read"
(cd "$STAGE/openai" && zip -qrX "$DIST/second-read-openai.zip" .)

copy_skill "$STAGE/plugin"
mkdir -p "$STAGE/plugin/.claude-plugin"
cp "$ROOT/.claude-plugin/plugin.json" "$ROOT/.claude-plugin/icon.png" "$STAGE/plugin/.claude-plugin/"
cp "$ROOT/README.md" "$STAGE/plugin/"
(cd "$STAGE/plugin" && zip -qrX "$DIST/second-read-plugin.zip" .)

ls -l "$DIST"
