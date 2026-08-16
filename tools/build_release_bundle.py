#!/usr/bin/env python3
"""Build a deterministic archive containing every tracked repository file."""

from __future__ import annotations

import argparse
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXED_TIME = (2000, 1, 1, 0, 0, 0)


def files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
    )
    return [ROOT / p.decode("utf-8") for p in output.split(b"\0") if p]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=ROOT / "release/hexagon-cover-proof-bundle.zip"
    )
    args = parser.parse_args()
    selected = files()
    missing = [path for path in selected if not path.is_file()]
    if missing:
        raise SystemExit("missing tracked inputs:\n" + "\n".join(map(str, missing)))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(selected, key=lambda p: p.relative_to(ROOT).as_posix()):
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes())
    print(args.output)


if __name__ == "__main__":
    main()
