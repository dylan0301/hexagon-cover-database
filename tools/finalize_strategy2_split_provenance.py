#!/usr/bin/env python3
"""Finalize provenance for the split Strategy 2 verification tree."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "arrange" / "paper_draft"

FILES_407 = [
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4073_boundary_loss_framework.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4074_L_Full_branch.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4075_Tminus_low_lower_branch_obligations.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4078_left_L_family_completion.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4079_first_Full_branch.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407a_left_Thigh_branch_completion.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407c_rigor_completion_details.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407d_rigor_final_assembly.md",
]

BASE_3105 = (
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/"
    "3105X_self_contained_direct_Vd0_nine_point/3105X_computation/"
)
FILES_3105 = [
    BASE_3105 + f"mixed_overlap_core_data_{index:02d}.py" for index in range(6)
] + [
    BASE_3105 + "mixed_overlap_core_polynomials.py",
    BASE_3105 + "verify_mixed_overlap_core_derivation.py",
    BASE_3105 + "verify_global_core_positivity.py",
]


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def generated_block(text: str, begin: str, end: str, block: str) -> str:
    pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
    replacement = begin + "\n" + block.rstrip() + "\n" + end
    if pattern.search(text):
        return pattern.sub(replacement, text, count=1)
    return text.rstrip() + "\n\n" + replacement + "\n"


def generate_provenance() -> tuple[dict[str, str], dict[str, str]]:
    provenance_407 = {relative: blob_sha(ROOT / relative) for relative in FILES_407}
    provenance_3105 = {relative: blob_sha(ROOT / relative) for relative in FILES_3105}
    write(
        ROOT / "proof/407X_PROVENANCE.json",
        json.dumps(
            {"schema": 1, "generated_by": "Strategy 2 split finalizer", "files": provenance_407},
            indent=2,
            sort_keys=True,
        ),
    )
    write(
        ROOT / "proof/3105X_CERTIFICATE_PROVENANCE.json",
        json.dumps(
            {
                "schema": 1,
                "transcript_sha256": "dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485",
                "files": provenance_3105,
            },
            indent=2,
            sort_keys=True,
        ),
    )
    return provenance_407, provenance_3105


def write_strategy2_manifest(provenance: dict[str, str]) -> None:
    name = "04e_strategy2_verification_00_provenance_manifest"
    comments = "\n".join(f"% {relative} {sha}" for relative, sha in provenance.items())
    write(
        PAPER / f"{name}.tex",
        rf"""% Generated exact blob identities; checked by tools/proof_lint.py.
{comments}
\section{{Exact Strategy 2 Source Provenance}}
\label{{sec:strategy2-source-provenance}}
The complete four-label endpoint calculation is tied to exact proof-package
bytes by \texttt{{proof/407X\_PROVENANCE.json}}.  The full SHA-1 Git blob
identities are retained in this generated source and checked against every
referenced file before the paper is built.
""",
    )
    wrapper = PAPER / "04_strategy2_verification.tex"
    text = wrapper.read_text(encoding="utf-8")
    command = rf"\input{{{name}}}"
    if command not in text:
        first = text.find("\\input{")
        if first < 0:
            raise RuntimeError("split Strategy 2 wrapper has no inputs")
        text = text[:first] + command + "\n" + text[first:]
        write(wrapper, text)


def write_ledger_manifest(provenance: dict[str, str]) -> None:
    ledger = PAPER / "source_ledger.md"
    text = ledger.read_text(encoding="utf-8")
    rows = "\n".join(
        f"| `{Path(relative).name}` | `{sha[:12]}` |" for relative, sha in provenance.items()
    )
    block = (
        "## Generated 407X split-source provenance\n\n"
        "The split verification appendix retains the following exact proof-package objects.\n\n"
        "| File | Git blob prefix |\n|---|---|\n" + rows
    )
    text = generated_block(
        text,
        "<!-- BEGIN GENERATED 407X SPLIT PROVENANCE -->",
        "<!-- END GENERATED 407X SPLIT PROVENANCE -->",
        block,
    )
    write(ledger, text)


def write_strategy4_manifest(provenance: dict[str, str]) -> None:
    path = PAPER / "06a_strategy4_exact_certificate.tex"
    text = path.read_text(encoding="utf-8")
    comments = "\n".join(f"% {relative} {sha}" for relative, sha in provenance.items())
    text = generated_block(
        text,
        "% BEGIN GENERATED 3105X PROVENANCE",
        "% END GENERATED 3105X PROVENANCE",
        comments,
    )
    write(path, text)


def patch_lint_for_split_tree() -> None:
    path = ROOT / "tools/proof_lint.py"
    text = path.read_text(encoding="utf-8")
    old = '''strategy2_path = ROOT / "arrange/paper_draft/04_strategy2_verification.tex"\nstrategy2_text = strategy2_path.read_text(encoding="utf-8")'''
    new = '''strategy2_path = ROOT / "arrange/paper_draft/04_strategy2_verification.tex"\nstrategy2_paths = sorted(\n    path\n    for path in compiled\n    if path.name.startswith(("04_strategy2_", "04d_strategy2_", "04e_strategy2_"))\n)\nstrategy2_text = "\\n".join(path.read_text(encoding="utf-8") for path in strategy2_paths)'''
    if old in text:
        text = text.replace(old, new, 1)
    elif new not in text:
        raise RuntimeError("proof_lint Strategy 2 source assignment has an unknown form")
    write(path, text)


def remove_one_shot_workflows() -> None:
    for relative in [
        ".github/workflows/refresh-proof-provenance.yml",
        ".github/workflows/strategy2-optimization-branch.yml",
    ]:
        path = ROOT / relative
        if path.exists():
            path.unlink()


def main() -> None:
    provenance_407, provenance_3105 = generate_provenance()
    write_strategy2_manifest(provenance_407)
    write_ledger_manifest(provenance_407)
    write_strategy4_manifest(provenance_3105)
    patch_lint_for_split_tree()
    remove_one_shot_workflows()


if __name__ == "__main__":
    main()
