# BNU Academic Report PPT Skill

Codex skill for generating Beijing Normal University / School of Systems Science style academic report slides from:

- a paper PDF plus related materials,
- a detailed Markdown analysis report,
- or a PPT-ready Markdown slide brief.

The skill is designed for Chinese academic presentations. It bundles BNU/SSS visual assets, style references, PPT-ready Markdown conventions, and a rendering wrapper that validates generated PPTX decks.

## What It Produces

- editable `.pptx` slide deck;
- slide outline `.json`;
- optional PDF/PNG previews;
- a normalized PPT-ready Markdown workflow for paper analysis reports.

## Main Style

- 16:9 BNU academic minimal layout;
- dark-blue cover/header bar with BNU and SSS wordmarks;
- two-level navigation header for content slides;
- gold active chapter and blue active subsection mask;
- clean figure insertion with preserved aspect ratio;
- simple centered `谢谢大家` ending page.

## Requirements

This skill expects the companion renderer skill to exist locally:

```bash
~/.codex/skills/general/academic-ppt-builder/scripts/render_academic_pptx.py
```

The wrapper also supports overrides:

```bash
ACADEMIC_PPT_BUILDER_SCRIPT=/path/to/render_academic_pptx.py
```

Optional preview export uses `libreoffice` and `pdftoppm` when available.

## Usage

Render a PPT-ready Markdown file:

```bash
python ~/.codex/skills/general/bnu-academic-report-ppt/scripts/render_bnu_academic_ppt.py \
  --input-md /abs/path/report__ppt_brief.md \
  --output-pptx /abs/path/report__bnu_academic.pptx \
  --outline-json /abs/path/report__slide_outline.json \
  --preview-dir /abs/path/preview
```

For a paper PDF, first create a detailed paper analysis report and visual asset manifest, then derive the PPT-ready Markdown brief before rendering.

## Repository Layout

- `SKILL.md`: Codex skill entry point and workflow.
- `references/`: input modes, style rules, and PPT-ready Markdown template.
- `scripts/`: rendering/validation wrapper.
- `assets/`: BNU/SSS logo and style assets.
- `templates/`: style examples and reference PPTX decks.

## Privacy Note

Template presenter fields use `XXX` placeholders. Replace them in generated reports/decks with the actual presenter information as needed.

