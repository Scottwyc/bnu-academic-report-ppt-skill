#!/usr/bin/env python3
"""Export representative BNU style screenshots from the bundled reference PPTX."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PPTX = ROOT / "templates" / "pptx" / "bnu_paper_deep_analysis_reference_v58.pptx"
DEFAULT_OUT = ROOT / "assets" / "style_examples"
DEFAULT_GALLERY = ROOT / "assets" / "模板风格.png"

SLIDE_SELECTION = [
    (1, "01_cover_layout.png", "Cover layout"),
    (5, "02_method_framework_layout.png", "Method framework"),
    (10, "03_method_figure_layout.png", "Method figure"),
    (15, "04_result_figure_layout.png", "Result figure"),
    (19, "05_table_layout.png", "Table layout"),
    (22, "06_summary_outlook_layout.png", "Summary outlook"),
]


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def find_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if path and Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def convert_pptx_to_pngs(pptx: Path, workdir: Path, dpi: int) -> Path:
    pdf_dir = workdir / "pdf"
    png_dir = workdir / "png"
    pdf_dir.mkdir()
    png_dir.mkdir()
    run(["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", str(pdf_dir), str(pptx)])
    pdf = pdf_dir / f"{pptx.stem}.pdf"
    if not pdf.exists():
        raise FileNotFoundError(f"LibreOffice did not produce expected PDF: {pdf}")
    run(["pdftoppm", "-png", "-r", str(dpi), str(pdf), str(png_dir / "slide")])
    return png_dir


def crop_to_16x9(path: Path) -> Image.Image:
    img = Image.open(path).convert("RGB")
    target_ratio = 16 / 9
    ratio = img.width / img.height
    if abs(ratio - target_ratio) < 0.01:
        return img
    if ratio > target_ratio:
        new_w = int(img.height * target_ratio)
        left = (img.width - new_w) // 2
        return img.crop((left, 0, left + new_w, img.height))
    new_h = int(img.width / target_ratio)
    top = (img.height - new_h) // 2
    return img.crop((0, top, img.width, top + new_h))


def export_selected(png_dir: Path, out_dir: Path) -> list[tuple[Path, str]]:
    out_dir.mkdir(parents=True, exist_ok=True)
    exported: list[tuple[Path, str]] = []
    for slide_no, name, label in SLIDE_SELECTION:
        src = png_dir / f"slide-{slide_no:02d}.png"
        if not src.exists():
            raise FileNotFoundError(src)
        img = crop_to_16x9(src)
        dest = out_dir / name
        img.save(dest, optimize=True)
        exported.append((dest, label))
    return exported


def make_gallery(exported: list[tuple[Path, str]], gallery_path: Path) -> None:
    thumb_w, thumb_h = 720, 405
    pad = 34
    label_h = 44
    cols = 2
    rows = (len(exported) + cols - 1) // cols
    width = cols * thumb_w + (cols + 1) * pad
    height = rows * (thumb_h + label_h) + (rows + 1) * pad
    bg = Image.new("RGB", (width, height), "#f4f7fb")
    draw = ImageDraw.Draw(bg)
    label_font = find_font(22, True)
    small_font = find_font(18)

    for idx, (path, label) in enumerate(exported):
        img = Image.open(path).convert("RGB")
        img = img.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        x = pad + (idx % cols) * (thumb_w + pad)
        y = pad + (idx // cols) * (thumb_h + label_h + pad)
        draw.rounded_rectangle((x - 4, y - 4, x + thumb_w + 4, y + thumb_h + 4), radius=10, fill="#d8e2ef")
        bg.paste(img, (x, y))
        draw.text((x, y + thumb_h + 10), f"{idx + 1}. {label}", font=label_font, fill="#173763")

    note = "Representative pages exported from the bundled anonymized reference deck"
    draw.text((pad, height - 28), note, font=small_font, fill="#5c6878")
    gallery_path.parent.mkdir(parents=True, exist_ok=True)
    bg.save(gallery_path, optimize=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Export representative style screenshots from the BNU reference PPTX.")
    parser.add_argument("--pptx", type=Path, default=DEFAULT_PPTX)
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--gallery", type=Path, default=DEFAULT_GALLERY)
    parser.add_argument("--dpi", type=int, default=150)
    args = parser.parse_args()

    if not shutil.which("libreoffice"):
        raise RuntimeError("libreoffice is required to export PPTX previews")
    if not shutil.which("pdftoppm"):
        raise RuntimeError("pdftoppm is required to export PPTX previews")

    with tempfile.TemporaryDirectory(prefix="bnu_style_examples_") as tmp:
        png_dir = convert_pptx_to_pngs(args.pptx.resolve(), Path(tmp), args.dpi)
        exported = export_selected(png_dir, args.out_dir.resolve())
        make_gallery(exported, args.gallery.resolve())

    print("Exported style examples:")
    for path, label in exported:
        print(f"- {label}: {path}")
    print(f"- Gallery: {args.gallery.resolve()}")


if __name__ == "__main__":
    main()
