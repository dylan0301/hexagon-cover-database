#!/usr/bin/env python3
"""Render every PDF page and reject media-box clipping at the page border."""

from __future__ import annotations

import argparse
from pathlib import Path

import fitz


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--dpi", type=int, default=144)
    parser.add_argument("--edge-pixels", type=int, default=2)
    parser.add_argument("--threshold", type=int, default=245)
    args = parser.parse_args()

    if not args.pdf.is_file():
        raise SystemExit(f"missing PDF: {args.pdf}")
    document = fitz.open(args.pdf)
    if document.page_count == 0:
        raise SystemExit("PDF has no pages")

    bad: list[str] = []
    matrix = fitz.Matrix(args.dpi / 72, args.dpi / 72)
    for number, page in enumerate(document, start=1):
        rect = page.rect
        for block in page.get_text("blocks"):
            x0, y0, x1, y1 = block[:4]
            if x0 < -0.25 or y0 < -0.25 or x1 > rect.width + 0.25 or y1 > rect.height + 0.25:
                bad.append(
                    f"page {number}: text block outside media box "
                    f"({x0:.2f},{y0:.2f},{x1:.2f},{y1:.2f})"
                )

        pix = page.get_pixmap(matrix=matrix, alpha=False, colorspace=fitz.csRGB)
        width, height, stride = pix.width, pix.height, pix.stride
        samples = memoryview(pix.samples)
        edge = args.edge_pixels
        threshold = args.threshold

        def nonwhite_at(px: int, py: int) -> bool:
            offset = py * stride + 3 * px
            return min(samples[offset : offset + 3]) < threshold

        touched = False
        for py in range(height):
            for px in range(edge):
                if nonwhite_at(px, py) or nonwhite_at(width - 1 - px, py):
                    touched = True
                    break
            if touched:
                break
        if not touched:
            for px in range(width):
                for py in range(edge):
                    if nonwhite_at(px, py) or nonwhite_at(px, height - 1 - py):
                        touched = True
                        break
                if touched:
                    break
        if touched:
            bad.append(f"page {number}: rendered content touches the media-box border")

    if bad:
        print("verify_pdf_render: FAILED")
        for item in bad:
            print(f"- {item}")
        raise SystemExit(1)
    print(f"verify_pdf_render: PASS ({document.page_count} pages rendered and scanned)")


if __name__ == "__main__":
    main()
