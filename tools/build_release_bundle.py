#!/usr/bin/env python3
"""Build a deterministic archival bundle for the computer-assisted proof."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXED_TIME = (2000, 1, 1, 0, 0, 0)


def files() -> list[Path]:
    paths = [
        ROOT / "arrange/paper_draft/main.pdf",
        ROOT / "arrange/CURRENT_VERIFICATION_SUMMARY.txt",
        ROOT / "REPRODUCE.md",
        ROOT / "LICENSE",
        ROOT / "requirements-proof.txt",
        ROOT / ".github/workflows/paper-rebuild.yml",
        ROOT / ".github/workflows/proof-ci.yml",
        ROOT / "arrange/paper_draft/source_ledger.md",
        ROOT / "tools/generate_active_dependency_graph.py",
        ROOT / "tools/generate_proof_manifest.py",
        ROOT / "tools/proof_lint.py",
        ROOT / "tools/verify_strategy2_pure_algebra.py",
        ROOT / "tools/verify_strategy2_spec_sync.py",
        ROOT / "tools/verify_pdf_render.py",
        ROOT / "tools/compare_pdfs_semantically.py",
        ROOT / "tools/generate_verification_summary.py",
        ROOT / "tools/build_release_bundle.py",
        ROOT / "proof/ACTIVE_DEPENDENCY_GRAPH.json",
        ROOT / "proof/ACTIVE_DEPENDENCIES.txt",
        ROOT / "proof/MANIFEST.txt",
        ROOT / "proof/407X_PROVENANCE.json",
        ROOT / "proof/3105X_CERTIFICATE_PROVENANCE.json",
        ROOT / "formalization/strategy2_optimization/lakefile.lean",
        ROOT / "formalization/strategy2_optimization/lean-toolchain",
        ROOT / "formalization/strategy2_optimization/lake-manifest.json",
        ROOT / "formalization/strategy2_optimization/Strategy2Optimization.lean",
        ROOT / "formalization/strategy2_optimization/Strategy2Optimization/Problems.lean",
    ]
    computation = ROOT / (
        "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/"
        "3105X_self_contained_direct_Vd0_nine_point/3105X_computation"
    )
    paths.extend(sorted(computation.glob("mixed_overlap_core_data_*.py")))
    paths.extend(
        [
            computation / "mixed_overlap_core_polynomials.py",
            computation / "verify_mixed_overlap_core_derivation.py",
            computation / "verify_global_core_positivity.py",
        ]
    )
    return paths


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=ROOT / "release/hexagon-cover-proof-bundle.zip"
    )
    args = parser.parse_args()
    selected = files()
    missing = [path for path in selected if not path.is_file()]
    if missing:
        raise SystemExit("missing release inputs:\n" + "\n".join(map(str, missing)))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(set(selected), key=lambda p: p.relative_to(ROOT).as_posix()):
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            zf.writestr(info, path.read_bytes())
    print(args.output)


if __name__ == "__main__":
    main()
