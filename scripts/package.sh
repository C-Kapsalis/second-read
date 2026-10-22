#!/bin/sh
# Build the release assets into dist/ (attach them to a GitHub Release).
#
#   second-read-plugin.zip       Claude plugin: .claude-plugin/plugin.json,
#                                skills/, hooks/ at the zip root. Upload under
#                                Customize > Plugins in Claude (web or Desktop).
#   second-read-skill.zip        one skill folder (copy review), for
#   second-read-docs-skill.zip   Customize > Skills in Claude. Exactly one
#   second-read-editor-skill.zip top-level folder, one SKILL.md, no manifest.
#   second-read-chatgpt.zip      ChatGPT plugin: plugin.json + skills/ (no
#                                hooks), for the ChatGPT plugin upload.
#
# POSIX sh; needs only `zip`. Run from anywhere: sh scripts/package.sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
DIST="$ROOT/dist"
STAGE=$(mktemp -d)
trap 'rm -rf "$STAGE"' EXIT INT TERM

command -v zip >/dev/null 2>&1 || { echo "package.sh: zip not found" >&2; exit 1; }
rm -rf "$DIST"
mkdir -p "$DIST"

# Short descriptions for the standalone skill zips. Claude's skill upload
# documents a 200-character limit for a description; the plugin and the
# ChatGPT zip keep the long one from SKILL.md.
SHORT_COPY='Second read for marketing copy (email, social post, landing page, blog post). Use for "second read" or to review/proofread/rewrite copy before it goes out.'
SHORT_DOCS='Second read for technical docs (README, tutorial, how-to, reference, release notes). Use for "second read" or to review/proofread/rewrite docs before publishing.'
SHORT_EDITOR='Second Read editor: proposes source-anchored edits in reading order, asks where a reader may diverge, exports the author-approved draft. Use to edit or restructure a draft.'

# Copy one skill folder to $2, renaming the skill (folder and `name:`) to $3.
# With $4, replace the frontmatter description with that one line, in YAML
# single quotes (so $4 must not contain a single quote).
copy_skill() {
  mkdir -p "$2"
  cp -R "$ROOT/skills/$1/." "$2/"
  find "$2" -name '.DS_Store' -exec rm -f {} +
  sed "s/^name: .*/name: $3/" "$ROOT/skills/$1/SKILL.md" > "$2/SKILL.md"
  if [ $# -ge 4 ]; then
    [ ${#4} -lt 200 ] || { echo "package.sh: short description for $3 is ${#4} characters" >&2; exit 1; }
    awk -v d="$4" '
      NR == 1 && /^---$/ { fm = 1; print; next }
      fm && /^---$/ { fm = 0; print; next }
      fm && /^description:/ { print "description: \047" d "\047"; skip = 1; next }
      fm && skip && /^[ \t]/ { next }
      { skip = 0; print }
    ' "$2/SKILL.md" > "$2/SKILL.md.tmp" && mv "$2/SKILL.md.tmp" "$2/SKILL.md"
  fi
}

zip_dir() { # zip the contents of directory $1 into $2
  (cd "$1" && zip -qrX "$2" .)
}

# 1. Claude plugin
P="$STAGE/plugin"
mkdir -p "$P/.claude-plugin" "$P/hooks"
cp "$ROOT/.claude-plugin/plugin.json" "$ROOT/.claude-plugin/icon.png" "$P/.claude-plugin/"
cp -R "$ROOT/skills" "$P/"
cp "$ROOT/hooks/claude-hooks.json" "$ROOT/hooks/core.md" "$P/hooks/"
cp "$ROOT/LICENSE" "$ROOT/README.md" "$P/"
find "$P" -name '.DS_Store' -exec rm -f {} +
zip_dir "$P" "$DIST/second-read-plugin.zip"

# 2. Claude skills, one folder each (folder name = skill name)
copy_skill second-read "$STAGE/skill/second-read" second-read "$SHORT_COPY"
zip_dir "$STAGE/skill" "$DIST/second-read-skill.zip"
copy_skill docs "$STAGE/docs-skill/second-read-docs" second-read-docs "$SHORT_DOCS"
zip_dir "$STAGE/docs-skill" "$DIST/second-read-docs-skill.zip"
copy_skill editor "$STAGE/editor-skill/second-read-editor" second-read-editor "$SHORT_EDITOR"
zip_dir "$STAGE/editor-skill" "$DIST/second-read-editor-skill.zip"

# 3. ChatGPT plugin: skills only, no hooks
C="$STAGE/chatgpt"
mkdir -p "$C/skills"
cp "$ROOT/adapters/chatgpt/plugin.json" "$C/"
copy_skill second-read "$C/skills/second-read" second-read
copy_skill docs "$C/skills/second-read-docs" second-read-docs
copy_skill editor "$C/skills/second-read-editor" second-read-editor
cp "$ROOT/LICENSE" "$C/"
zip_dir "$C" "$DIST/second-read-chatgpt.zip"

ls -l "$DIST"
