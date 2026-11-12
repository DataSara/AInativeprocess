#!/usr/bin/env bash
# Builds the distributable files from prompt/ and knowledge/.
#   dist/reprocess-full.md         single file for any AI chat (attach it, or paste it)
#   dist/claude-skill/SKILL.md     Claude skill (zip the folder to upload)
# Fails if prompt/reprocess.md exceeds the 8,000-character limit of Custom GPT / Copilot agent instructions.
set -euo pipefail
cd "$(dirname "$0")/.."

limit=8000

if grep -q '```' knowledge/report-template.html; then
  echo "knowledge/report-template.html must not contain triple backticks (it is fenced in the bundle)" >&2
  exit 1
fi
chars=$(python3 -c 'import sys; print(len(open(sys.argv[1], encoding="utf-8").read()))' prompt/reprocess.md)
if (( chars > limit )); then
  echo "prompt/reprocess.md is $chars characters (limit $limit)" >&2
  exit 1
fi
echo "prompt/reprocess.md: $chars / $limit characters"

pv=$(sed -n 's/^# Reprocess \(v[0-9.]*\).*/\1/p' prompt/reprocess.md | head -1)
tv=$(sed -n 's/.*Prepared with Reprocess \(v[0-9.]*\).*/\1/p' knowledge/report-template.html | head -1)
if [ "$pv" != "$tv" ]; then
  echo "version mismatch: prompt $pv, template $tv" >&2
  exit 1
fi

rm -rf dist
mkdir -p dist/claude-skill/knowledge

{
  cat prompt/reprocess.md
  printf '\n\n---\n# Knowledge file: risk checklist\n\n'
  cat knowledge/risk-checklist.md
  printf '\n\n---\n# Knowledge file: redesign patterns\n\n'
  cat knowledge/redesign-patterns.md
  printf '\n\n---\n# Knowledge file: question bank\n\n'
  cat knowledge/question-bank.md
  printf '\n\n---\n# Knowledge file: tool catalog\n\n'
  cat knowledge/tool-catalog.md
  printf '\n\n---\n# Knowledge file: tool assessment kit\n\n'
  cat knowledge/tool-assessment-kit.md
  printf '\n\n---\n# Knowledge file: report template\n\n```html\n'
  cat knowledge/report-template.html
  printf '```\n'
} > dist/reprocess-full.md

{
  cat <<'EOF'
---
name: reprocess
description: Redesign an existing workflow or SOP to be AI-native. Classifies each step (automate, AI-assist, AI-autonomous, human, eliminate), places human gates, flags risk, compliance and security issues to check, recommends open-source build options with alternatives, states limitations, and produces a downloadable HTML report with diagrams. Use when someone wants to automate, streamline, or apply AI to a business process.
---

Knowledge files for this skill are in `knowledge/`: `question-bank.md`, `redesign-patterns.md`, `tool-catalog.md`, `risk-checklist.md`, `tool-assessment-kit.md`, `report-template.html`.

EOF
  cat prompt/reprocess.md
} > dist/claude-skill/SKILL.md
cp knowledge/redesign-patterns.md knowledge/question-bank.md knowledge/tool-catalog.md knowledge/risk-checklist.md knowledge/tool-assessment-kit.md knowledge/report-template.html dist/claude-skill/knowledge/

echo "Built: $(find dist -type f | sort | tr '\n' ' ')"
