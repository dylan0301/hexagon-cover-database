#!/usr/bin/env python3
"""Compare PDFs by stable semantics rather than unstable PDF object bytes.

XeTeX/xdvipdfmx can assign different document IDs, generated timestamps, or
compressed-object bytes to two consecutive builds even when the rendered
document is identical. This checker deliberately ignores those serialization
details and compares every stable, user-observable component:

* page count, media boxes, crop boxes, and rotations;
* document metadata excluding generated creation/modification timestamps and
  the timestamp suffix in XeTeX's generated creator field;
* table of contents and page labels;
* extracted words with coordinates;
* hyperlinks, annotations, widgets, and embedded-file names;
* exact RGB raster pixels at a fixed DPI.

The comparison is strict: there is no pixel tolerance.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

import fitz

IGNORED_METADATA_KEYS = {"creationDate", "modDate"}
XETEX_CREATOR_PATTERN = re.compile(r"\s*XeTeX output \d{4}\.\d{2}\.\d{2}:\d{4}\Z")


def rounded(value: float) -> float:
    return round(float(value), 4)


def rect_tuple(rect: fitz.Rect | None) -> tuple[float, float, float, float] | None:
    if rect is None:
        return None
    return tuple(rounded(value) for value in (rect.x0, rect.y0, rect.x1, rect.y1))


def point_tuple(point: Any) -> tuple[float, float] | str | None:
    if point is None:
        return None
    if hasattr(point, "x") and hasattr(point, "y"):
        return (rounded(point.x), rounded(point.y))
    if isinstance(point, (tuple, list)) and len(point) >= 2:
        return (rounded(point[0]), rounded(point[1]))
    return str(point)


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def normalize_metadata(document: fitz.Document) -> dict[str, str]:
    normalized: dict[str, str] = {}
    for key, raw_value in sorted((document.metadata or {}).items()):
        if key in IGNORED_METADATA_KEYS:
            continue
        value = raw_value or ""
        if key == "creator" and XETEX_CREATOR_PATTERN.fullmatch(value):
            value = "XeTeX output"
        normalized[key] = value
    return normalized


def normalize_toc(document: fitz.Document) -> list[list[Any]]:
    normalized: list[list[Any]] = []
    for level, title, page in document.get_toc(simple=True):
        normalized.append([int(level), str(title), int(page)])
    return normalized


def normalize_page_labels(document: fitz.Document) -> list[dict[str, Any]]:
    getter = getattr(document, "get_page_labels", None)
    if getter is None:
        return []
    labels = getter() or []
    return [
        {
            str(key): rounded(value) if isinstance(value, float) else value
            for key, value in sorted(label.items())
        }
        for label in labels
    ]


def normalize_words(page: fitz.Page) -> list[list[Any]]:
    words: list[list[Any]] = []
    for item in page.get_text("words", sort=True):
        x0, y0, x1, y1, text, block, line, word = item[:8]
        words.append(
            [
                rounded(x0),
                rounded(y0),
                rounded(x1),
                rounded(y1),
                str(text),
                int(block),
                int(line),
                int(word),
            ]
        )
    return words


def normalize_links(page: fitz.Page) -> list[dict[str, Any]]:
    links: list[dict[str, Any]] = []
    for link in page.get_links():
        normalized = {
            "kind": int(link.get("kind", 0)),
            "from": rect_tuple(link.get("from")),
            "page": int(link.get("page", -1)),
            "to": point_tuple(link.get("to")),
            "zoom": rounded(link.get("zoom", 0.0)),
            "uri": link.get("uri") or "",
            "file": link.get("file") or "",
            "name": link.get("name") or link.get("nameddest") or "",
        }
        links.append(normalized)
    return sorted(links, key=lambda item: canonical_json(item))


def iter_annotations(page: fitz.Page) -> Iterable[fitz.Annot]:
    annotations = page.annots()
    return [] if annotations is None else annotations


def normalize_annotations(page: fitz.Page) -> list[dict[str, Any]]:
    annotations: list[dict[str, Any]] = []
    for annotation in iter_annotations(page):
        info = {
            str(key): value if value is not None else ""
            for key, value in sorted((annotation.info or {}).items())
        }
        annotation_type = annotation.type
        annotations.append(
            {
                "type": [int(annotation_type[0]), str(annotation_type[1])],
                "rect": rect_tuple(annotation.rect),
                "info": info,
                "opacity": rounded(getattr(annotation, "opacity", 0.0)),
            }
        )
    return sorted(annotations, key=lambda item: canonical_json(item))


def normalize_widgets(page: fitz.Page) -> list[dict[str, Any]]:
    widgets = page.widgets()
    if widgets is None:
        return []
    normalized: list[dict[str, Any]] = []
    for widget in widgets:
        normalized.append(
            {
                "field_name": getattr(widget, "field_name", "") or "",
                "field_value": str(getattr(widget, "field_value", "") or ""),
                "field_type": int(getattr(widget, "field_type", 0) or 0),
                "field_flags": int(getattr(widget, "field_flags", 0) or 0),
                "rect": rect_tuple(getattr(widget, "rect", None)),
            }
        )
    return sorted(normalized, key=lambda item: canonical_json(item))


def embedded_file_names(document: fitz.Document) -> list[str]:
    getter = getattr(document, "embfile_names", None)
    return [] if getter is None else sorted(str(name) for name in (getter() or []))


def page_signature(page: fitz.Page, dpi: int) -> dict[str, Any]:
    pixmap = page.get_pixmap(
        matrix=fitz.Matrix(dpi / 72.0, dpi / 72.0),
        colorspace=fitz.csRGB,
        alpha=False,
        annots=True,
    )
    return {
        "rect": rect_tuple(page.rect),
        "cropbox": rect_tuple(page.cropbox),
        "rotation": int(page.rotation),
        "words": normalize_words(page),
        "links": normalize_links(page),
        "annotations": normalize_annotations(page),
        "widgets": normalize_widgets(page),
        "raster_width": int(pixmap.width),
        "raster_height": int(pixmap.height),
        "raster_sha256": hashlib.sha256(pixmap.samples).hexdigest(),
    }


def semantic_digest(path: Path, dpi: int = 144) -> str:
    digest = hashlib.sha256()
    with fitz.open(path) as document:
        header = {
            "page_count": int(document.page_count),
            "metadata": normalize_metadata(document),
            "toc": normalize_toc(document),
            "page_labels": normalize_page_labels(document),
            "embedded_files": embedded_file_names(document),
            "dpi": int(dpi),
        }
        digest.update(canonical_json(header))
        for page in document:
            digest.update(canonical_json(page_signature(page, dpi)))
    return digest.hexdigest()


def compare(left_path: Path, right_path: Path, dpi: int) -> tuple[str, str]:
    failures: list[str] = []
    left_digest = hashlib.sha256()
    right_digest = hashlib.sha256()

    with fitz.open(left_path) as left, fitz.open(right_path) as right:
        left_header = {
            "page_count": int(left.page_count),
            "metadata": normalize_metadata(left),
            "toc": normalize_toc(left),
            "page_labels": normalize_page_labels(left),
            "embedded_files": embedded_file_names(left),
            "dpi": int(dpi),
        }
        right_header = {
            "page_count": int(right.page_count),
            "metadata": normalize_metadata(right),
            "toc": normalize_toc(right),
            "page_labels": normalize_page_labels(right),
            "embedded_files": embedded_file_names(right),
            "dpi": int(dpi),
        }
        left_digest.update(canonical_json(left_header))
        right_digest.update(canonical_json(right_header))

        if left_header != right_header:
            failures.append("document metadata, outline, labels, or page count differs")

        for index in range(min(left.page_count, right.page_count)):
            left_signature = page_signature(left[index], dpi)
            right_signature = page_signature(right[index], dpi)
            left_digest.update(canonical_json(left_signature))
            right_digest.update(canonical_json(right_signature))
            if left_signature != right_signature:
                differing_fields = [
                    key
                    for key in sorted(left_signature)
                    if left_signature.get(key) != right_signature.get(key)
                ]
                failures.append(
                    f"page {index + 1} differs in: {', '.join(differing_fields)}"
                )

    if failures:
        print("compare_pdfs_semantically: FAILED")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    return left_digest.hexdigest(), right_digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("left", type=Path)
    parser.add_argument("right", type=Path)
    parser.add_argument("--dpi", type=int, default=144)
    args = parser.parse_args()

    for path in (args.left, args.right):
        if not path.is_file():
            raise SystemExit(f"missing PDF: {path}")
    if args.dpi <= 0:
        raise SystemExit("--dpi must be positive")

    left_digest, right_digest = compare(args.left, args.right, args.dpi)
    print(
        "compare_pdfs_semantically: PASS "
        f"(strict {args.dpi}-DPI raster, digest {left_digest})"
    )
    if left_digest != right_digest:
        raise AssertionError("internal semantic digest mismatch after successful comparison")


if __name__ == "__main__":
    main()
