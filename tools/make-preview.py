"""Render the portfolio's cover slide into preview.jpg, the image shown in link previews.

Run again whenever the cover slide changes:
    pip install pymupdf
    python3 tools/make-preview.py
"""
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent.parent
WIDTH, HEIGHT = 1200, 630  # Open Graph recommended size

page = pymupdf.open(ROOT / "portfolio.pdf")[0]
scale = WIDTH / page.rect.width

# Crop the slide's centre to the preview's aspect ratio
clip_height = HEIGHT / scale
top = round((page.rect.height - clip_height) / 2 * scale) / scale  # whole output pixels
clip = pymupdf.Rect(0, top, page.rect.width, top + clip_height)

pixmap = page.get_pixmap(matrix=pymupdf.Matrix(scale, scale), clip=clip)
pixmap.save(ROOT / "preview.jpg", jpg_quality=85)
print(f"Wrote {ROOT / 'preview.jpg'} ({pixmap.width}x{pixmap.height})")
