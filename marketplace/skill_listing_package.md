# Skill Listing Package

Use this package to submit the skill to Agent Skills directories or marketplaces.

## Basic Fields

- **Skill name**: `bnu-academic-report-ppt`
- **Display name**: BNU Academic Report PPT
- **Repository**: `https://github.com/Scottwyc/bnu-academic-report-ppt-skill`
- **Category**: Productivity / Presentation / Academic Writing
- **Supported agents**: Codex CLI, Codex app, Claude Code-compatible skill runners that support `SKILL.md`
- **License**: MIT
- **Language**: Chinese first; English metadata included.

## Short Description

Generate Beijing Normal University / School of Systems Science style academic PPTX decks from a paper PDF, detailed Markdown report, or PPT-ready Markdown brief.

## Long Description

`bnu-academic-report-ppt` is an agent skill for producing editable academic report PowerPoint decks in a Beijing Normal University / School of Systems Science visual style. It is designed for Chinese academic presentations, especially paper deep-analysis and literature-review reports.

The skill defines a structured PPT-ready Markdown format, bundles BNU/SSS visual assets, provides style rules and reference templates, and includes a rendering wrapper that validates the generated PPTX for missing images, broken ZIP structure, and image aspect-ratio distortion. It works best together with a detailed paper-analysis workflow: first generate a figure-grounded Markdown report, then condense it into a slide brief and render the final deck.

## Key Features

- Converts PPT-ready Markdown into editable `.pptx`.
- Supports paper PDF, detailed Markdown report, or slide brief workflows.
- Uses BNU/SSS academic minimal styling with two-level navigation headers.
- Preserves figure aspect ratios and validates missing images.
- Produces optional PDF/PNG previews when `libreoffice` and `pdftoppm` are available.
- Bundles reference style assets, multi-page exported style screenshots, sample decks, and slide brief templates.

## Use Cases

- Literature-analysis seminar reports.
- Paper deep-reading presentations.
- Graduate course presentations.
- Research group meeting slides.
- Chinese academic decks that need consistent BNU/SSS branding.

## Install / Usage Snippet

```bash
git clone https://github.com/Scottwyc/bnu-academic-report-ppt-skill.git \
  ~/.codex/skills/general/bnu-academic-report-ppt
```

Render:

```bash
python ~/.codex/skills/general/bnu-academic-report-ppt/scripts/render_bnu_academic_ppt.py \
  --input-md /abs/path/report__ppt_brief.md \
  --output-pptx /abs/path/report__bnu_academic.pptx \
  --outline-json /abs/path/report__slide_outline.json \
  --preview-dir /abs/path/preview
```

## Dependencies

- Python with `python-pptx` and `Pillow`.
- Companion renderer: `academic-ppt-builder`.
- Optional preview export: `libreoffice` and `pdftoppm`.

## Tags

`codex-skill`, `agent-skill`, `pptx`, `academic-presentation`, `markdown-to-pptx`, `bnu`, `school-of-systems-science`, `chinese-academic-writing`, `paper-analysis`, `literature-review`

## Submission Notes

- The repository has been anonymized; template presenter fields use `XXX`.
- The skill includes BNU/SSS branding assets. Make sure the target platform allows institution-branded templates before listing publicly.
- Some marketplaces may prefer a plugin package rather than a raw skill folder. If required, package this skill into a Codex plugin while keeping `SKILL.md` unchanged.

## Suggested Platform-Specific Notes

### MCP Market

The public "Sell Skills" page currently says the seller workflow is "Coming Soon" and invites early access sign-up. Use this listing package when applying for early access or submitting after seller access opens.

### SkillsLLM

Use the repository URL and the short/long descriptions above in the "Submit a Skill" flow.

### AgentSkills

The submit page requires login. After signing in, use the fields above and classify it under presentation/productivity/academic workflows.
