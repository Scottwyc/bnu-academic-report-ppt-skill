# BNU Academic Report Style Rules

## Visual Identity

- Use 16:9 slides.
- Main colors:
  - dark navy `#1C345B`
  - BNU blue `#355D9D`
  - subsection active blue `#5785C7`
  - gold `#F0C95A`
  - text `#1C222B`
  - muted text `#636B74`
- Use Chinese-capable fonts:
  - PPTX East Asian: `Microsoft YaHei`
  - English/digits: `Arial`
  - Preview fallback: `Noto Sans CJK SC`, `Source Han Sans SC`, `WenQuanYi Micro Hei`

The bundled assets live in this skill's `assets/` directory.

Important assets:

- `bnu_wordmark_white.png` for dark header/cover bars.
- `bnu_wordmark_blue.png` for light backgrounds only.
- `sss_bnu_logo.png` or white SSS logo assets when the cover needs the School of Systems Science mark.
- `模板风格.png` as the quick 2x3 visual gallery exported from the reference PPTX.
- `style_examples/*.png` for individual representative slide screenshots: cover, method framework, method figure, result figure, table, and summary/outlook.

Use the full reference deck below as the concrete quality target for style and density:

`templates/pptx/bnu_paper_deep_analysis_reference_v58.pptx`

Match its main traits: dark-blue cover bar, white BNU wordmark, two-level content navigation, gold active chapter, blue active subsection mask, clean direct image insertion, centered close captions, no lower-left footer, and a simple `谢谢大家` ending slide.

When the reference deck changes, regenerate screenshots with:

```bash
python scripts/export_style_examples.py
```

## Header

Content slides:

- top dark-blue navigation bar with chapter tabs;
- active chapter highlighted in gold;
- lower blue subsection strip contains only numbered subsection labels such as `1.作者简介`;
- active subsection uses a blue/cyan mask;
- no separate arrow marker;
- keep header compact to preserve body space.

Cover and final thanks slides:

- use a single dark-blue top bar;
- BNU white horizontal wordmark at upper left;
- SSS white mark at upper right when available;
- no two-level internal navigation on cover/final slides.

## Body Typography

- Page topic sentence is larger than bullets and should fit one line when practical.
- Supporting bullets are indented one level.
- For `标签：说明` bullets, render the label before the first colon in bold.
- Convert ASCII `->` to `→`.
- Do not display the literal label `本页主题`.
- Use NOTE as a compact highlighted box after body content, only when there is space.

## Figure And Table Handling

- Preserve aspect ratio for all images.
- Default fit is contain, never stretch.
- Do not add shadows, cards, or opaque backgrounds behind transparent PNGs.
- Captions are centered, close to the figure, and the same width as the figure box.
- Table screenshots are often unreadable; redraw tables as clean PNGs with larger internal fonts.
- If a table image already contains a title/caption above it, omit the bottom PPT caption.
- Use `布局：right-large` only for a central overview/result figure that should dominate the right side.

## Density Rules

- Prefer 3-5 bullets per slide.
- Split dense methods/results across slides instead of shrinking text.
- Wide plots/tables: stacked text above and figure below.
- Normal/tall figures: two-column text-left / figure-right.
- Text-only slides should have generous whitespace.
- Appendix slides can be denser, but should still avoid overflow.

## Content Conventions

- Author slide: one page by default; portraits must match names; add short roles instead of biographies.
- Historical-context slide: list reference-like paper entries under each point when useful.
- Methods slides: explain inputs, outputs, model architecture, and training/evaluation separately when needed.
- Results slides: each key claim should tie to a concrete figure/table/panel/metric.
- Summary slides: separate method contribution, limitation/boundary, and outlook when useful.
- Final slide: centered `谢谢大家`; presenter line centered below.
