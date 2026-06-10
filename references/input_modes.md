# Input Modes

## Mode A: 文献 PDF + 相关资料

Use this when the user gives a paper PDF, DOI, paper URL, Zotero item, local supplementary files, or figure/data materials and asks for a BNU academic report PPT.

Workflow:

1. Run the paper deep-analysis workflow first.
   - Verify title, authors, venue, date, DOI/URL, PDF status.
   - Download legal/official figures when possible.
   - Build or update `figures/visual_assets_manifest.json`.
   - Produce the detailed Chinese Markdown report and DOCX.
2. Derive a PPT-ready brief from the detailed report.
   - Keep the same logical framework.
   - Use only claims and visuals supported by the report.
   - Add self-drawn schematics only when they clarify paper methods/results; label them as schematic/redrawn.
3. Render and validate the BNU deck.

Recommended output layout for one-paper reports:

- 标题页
- 绪论背景: 作者简介, 历史脉络, 痛点与创新
- 方法框架: 数据来源, 概念/模型/流程, 训练评估
- 主要结果: 2-5 slides based on actual paper figures/tables
- 总结展望: 方法贡献, 局限边界, 领域启发
- 细节补充: metrics, formulas, hyperparameters
- 谢谢大家

## Mode B: 详细 Markdown 报告

Use this when the input is a long report, literature review, project report, or deep-analysis document.

Workflow:

1. Identify section hierarchy and main storyline.
2. Make a new `ppt_brief.md` instead of rendering the long report directly.
3. For each slide, keep one topic sentence and 3-5 support bullets.
4. Reuse figures already cited in the report. If the report has no suitable figure for an important method/logic slide, draw a clean schematic and add it to the report/manifest when appropriate.
5. Place appendices after conclusion.

## Mode C: PPT-ready Markdown

Use this when the input already has `## Slide N. ...` headings.

Workflow:

1. Normalize slide titles to `章节>小节`.
2. Remove visible source-section lines from the slide body.
3. Ensure every image path exists relative to the Markdown file or is absolute.
4. Ensure captions are concise and match the image.
5. Render with the wrapper script.

## When To Ask The User

Ask only if:

- multiple PDFs/papers are ambiguous and no target paper is obvious;
- BNU/SSS branding is not desired despite the user naming this skill;
- the user needs a fixed slide count or strict time limit and the source is too long to infer safely.
