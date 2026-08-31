#!/usr/bin/env python3
"""Verify that the reader-oriented paper reuses, but does not alter, original sources."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'arrange' / 'readable_paper' / 'ORIGINAL_SOURCE_MANIFEST.json'


def main() -> None:
    data = json.loads(MANIFEST.read_text(encoding='utf-8'))
    failures: list[str] = []
    for rel, expected in data['files'].items():
        path = ROOT / rel
        if not path.is_file():
            failures.append(f'missing original source: {rel}')
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            failures.append(f'original source changed: {rel}\n  expected {expected}\n  actual   {actual}')
    if failures:
        raise SystemExit('\n'.join(failures))
    print(f"verified {len(data['files'])} reused original files against additive baseline {data['source_head']}")


if __name__ == '__main__':
    main()
