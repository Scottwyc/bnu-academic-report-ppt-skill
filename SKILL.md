---
name: bnu-academic-report-ppt
description: Generate or refine Beijing Normal University academic report style PPTX decks from a paper PDF plus related materials, a detailed Markdown report, or a PPT-ready Markdown brief. Use for Chinese academic presentations that need BNU/School of Systems Science branding, two-level BNU navigation headers, literature/paper analysis slides, image-rich scientific figures, editable PPTX output, preview PDFs, and strict layout validation.
---

# BNU Academic Report PPT

Use this skill to create a **BNU academic report style** editable PowerPoint deck. It is a focused workflow built on top of `academic-ppt-builder`; use that renderer for the actual `.pptx` generation, but use this skill's bundled BNU/SSS assets and reference templates by default.

Default output language is Chinese. Default style is BNU/School of Systems Science academic minimal.

## Supported Inputs

1. **文献 PDF + 相关资料**
   - Use `paper-deep-analysis` first when the user wants a paper/literature analysis PPT.
   - Produce or update a detailed Chinese Markdown report, collect verified figures/assets, then derive a PPT-ready Markdown brief.
2. **详细 Markdown 报告**
   - Condense into a PPT-ready Markdown brief before rendering.
   - Preserve the source report structure and claims; do not invent unsupported content.
3. **PPT-ready Markdown**
   - Normalize headings, bullets, image paths, captions, and layout hints, then render directly.

Read `references/input_modes.md` when choosing the path.

## Required Deliverables

- `*_ppt_brief_*.md` when the input is PDF or detailed Markdown.
- `*.pptx` editable deck.
- `*_slide_outline_*.json` machine-readable outline.
- `preview/` PDF and PNG slide previews when LibreOffice / `pdftoppm` are available.
- Updated DOCX exports for Markdown sources when working downstream of `paper-deep-analysis`.

## Core Workflow

1. **Classify input**
   - PDF/materials: make or update the detailed report and visual asset manifest first.
   - Detailed report: produce a concise PPT-ready brief.
   - PPT-ready brief: validate and render.

2. **Prepare PPT-ready Markdown**
   - Use structured slide headings: `绪论背景>作者简介`, `方法框架>数据来源`, `主要结果>预测性能`, `总结展望>局限边界`.
   - Put the page claim as `- 本页主题：...`; the rendered slide should show only the sentence after the colon.
   - Use `**NOTE**：...` only when it fits; omit dense-slide notes.
   - Use `图片：...` and `图注：...` for every visual. Multiple images are allowed only when they support the same slide point.
   - Do not render visible `来源小节` / `证据图表` lines on slides; keep them as audit metadata only.
   - Start from `references/ppt_brief_template.md` for new briefs.

3. **Apply BNU style rules**
   - Read `references/bnu_style_rules.md` for layout refinements.
   - Use `templates/pptx/bnu_paper_deep_analysis_reference_v58.pptx` as the concrete visual target when judging style quality. It is the refined BNU paper deep-analysis deck from the LLM concept-graph paper.
   - Internal slides use the two-level BNU navigation header:
     - top strip: chapter tabs, active chapter in gold;
     - lower strip: numbered subsection labels only, active subsection in blue/cyan mask;
     - no arrow marker when the lower active mask is present.
   - Cover and final thanks pages use only the dark-blue top bar with BNU/SSS white wordmarks.

4. **Render**
   - Prefer the wrapper:

```bash
python ~/.codex/skills/general/bnu-academic-report-ppt/scripts/render_bnu_academic_ppt.py \
  --input-md /abs/path/ppt_brief.md \
  --output-pptx /abs/path/output.pptx \
  --outline-json /abs/path/slide_outline.json \
  --preview-dir /abs/path/preview
```

   - The wrapper calls an adjacent `academic-ppt-builder` skill renderer by default:
     `$CODEX_HOME/skills/general/academic-ppt-builder/scripts/render_academic_pptx.py`.
   - Override the renderer with `--builder-script` or `ACADEMIC_PPT_BUILDER_SCRIPT` when needed.
   - The wrapper passes this skill's bundled `assets/` directory to the renderer, so BNU/SSS logos and wordmarks are available even when `academic-ppt-builder` assets change.

5. **Verify**
   - Confirm `.pptx` opens with `python-pptx`.
   - Confirm all outline image paths exist.
   - Confirm every scientific image/table/logo keeps aspect ratio.
   - Export PDF/PNG previews when possible and inspect dense or newly changed slides.
   - For paper-analysis decks, verify every slide image matches the section content and comes from the report/manifest.

## Layout Lessons From The BNU Paper Deck

- Keep author/team slides to one page unless the user asks otherwise; add short identity/role bullets and pair portraits with names.
- Split dense methods or result logic into multiple slides instead of shrinking text.
- Put `细节补充` after `总结展望` like an appendix unless the user explicitly wants technical details earlier.
- Tables often need redrawn PPT-specific PNGs with larger internal type and tight captions.
- Figure captions should be close to and centered under the figure.
- Directly insert transparent PNGs; avoid shadows and picture-card backgrounds.
- For key overview figures, use `布局：right-large` only when the figure is central and readable.
- The final slide should contain only `谢谢大家` centered and `汇报人：...` below it.

## Bundled Assets And Templates

- `assets/bnu_wordmark_white.png`: transparent white BNU horizontal wordmark for dark headers and cover bars.
- `assets/bnu_wordmark_blue.png`: blue BNU wordmark for light backgrounds.
- `assets/sss_bnu_logo.png`: School of Systems Science / BNU logo asset.
- `assets/模板风格.png`: BNU navigation-style reference image.
- `templates/style/bnu_sss_academic_minimal_style.yaml`: style tokens.
- `templates/pptx/bnu_sss_academic_minimal_sample.pptx`: compact sample deck.
- `templates/pptx/bnu_paper_deep_analysis_reference_v58.pptx`: full refined reference deck for the target effect.

## Related Skills

- Use `paper-deep-analysis` for PDF-to-detailed-report and figure/asset collection.
- Use `academic-ppt-builder` as the rendering engine and low-level style reference.
