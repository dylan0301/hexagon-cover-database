#!/usr/bin/env python3
"""Generate the canonical theorem dependency graph.

The graph follows arrange/paper_draft/main.tex.  Its nodes are formal theorem-like
environments and its arrows are audited logical dependencies: explicit theorem
references in proofs, plus a small declared set of interface and routing edges.
"""
from __future__ import annotations

import argparse
import base64
import json
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import Any

try:
    import mistune
except ImportError:  # pragma: no cover - CI installs the repository requirements only
    mistune = None

ROOT = Path(__file__).resolve().parents[2]
PAPER = ROOT / "arrange" / "paper_draft"
MAIN = PAPER / "main.tex"
OUT_HTML = ROOT / "interactive" / "readable_proof_dependency_graph.html"
OUT_JSON = ROOT / "interactive" / "readable_proof_dependency_data.json"
REPORT = ROOT / "arrange" / "README.md"
BRANCH = "main"
REPOSITORY = "dylan0301/hexagon-cover-database"

ENV_RE = re.compile(
    r"\\begin\{(theorem|lemma|proposition|corollary)\}"
    r"(?:\[([^\]]*)\])?(.*?)\\end\{\1\}",
    re.S,
)
INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
REF_RE = re.compile(
    r"\\(?:ref|eqref|pageref|autoref|cref|Cref|zcref|zcpageref)"
    r"\*?(?:\[[^\]]*\])?\{([^}]+)\}"
)

GROUPS = [
    "Common geometry / Appendix A",
    "Method 1: trace length / Appendix B",
    "Method 2: area loss / Appendix C",
    "Method 3: local toolkit / Appendix D",
    "Method 3: universal terminals / Appendix D",
    "Method 3: nonzero-gap cases / Appendix D",
    "Method 3: zero-gap witnesses / Appendix E",
    "Appendix F: exact mixed-overlap certificate",
    "Method 3: zero-gap completion / Appendix E",
    "Final assembly",
]

COLORS = {
    "Common geometry / Appendix A": "#466b9f",
    "Method 1: trace length / Appendix B": "#277b67",
    "Method 2: area loss / Appendix C": "#9a6b2f",
    "Method 3: local toolkit / Appendix D": "#6c5aa5",
    "Method 3: universal terminals / Appendix D": "#785bb5",
    "Method 3: nonzero-gap cases / Appendix D": "#9b4f64",
    "Method 3: zero-gap witnesses / Appendix E": "#8a612e",
    "Appendix F: exact mixed-overlap certificate": "#714d8d",
    "Method 3: zero-gap completion / Appendix E": "#9a713a",
    "Final assembly": "#a24040",
}


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT.resolve()).as_posix()


def resolve_input(source: Path, raw: str) -> Path | None:
    target = Path(raw)
    if not target.suffix:
        target = target.with_suffix(".tex")
    for base in (source.parent, PAPER):
        candidate = (base / target).resolve()
        if candidate.is_file():
            return candidate
    return None


def active_sources() -> list[Path]:
    output: list[Path] = []

    def visit(path: Path) -> None:
        path = path.resolve()
        try:
            path.relative_to(PAPER.resolve())
        except ValueError as exc:
            raise RuntimeError(f"canonical paper input escapes {rel(PAPER)}: {path}") from exc
        if path in output:
            return
        output.append(path)
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in INPUT_RE.findall(text):
            child = resolve_input(path, raw)
            if child is None:
                raise RuntimeError(f"cannot resolve \\input{{{raw}}} from {rel(path)}")
            visit(child)

    visit(MAIN)
    return output


def strip_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        line = re.sub(r"(?<!\\)%.*$", "", line).rstrip()
        lines.append(line)
    return "\n".join(lines).strip()


def reference_labels(text: str) -> list[str]:
    labels: list[str] = []
    for raw in REF_RE.findall(text):
        labels.extend(label.strip() for label in raw.split(",") if label.strip())
    return labels


def parse_nodes(sources: list[Path]) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []
    for source in sources:
        text = source.read_text(encoding="utf-8", errors="replace")
        matches = list(ENV_RE.finditer(text))
        for index, match in enumerate(matches):
            body = match.group(3)
            labels = re.findall(r"\\label\{([^}]+)\}", body)
            if not labels:
                continue
            statement = strip_comments(re.sub(r"\\label\{[^}]+\}", "", body))
            next_start = matches[index + 1].start() if index + 1 < len(matches) else len(text)
            tail = text[match.end() : next_start]
            proof_match = re.search(
                r"\\begin\{proof\}(?:\[[^\]]*\])?(.*?)\\end\{proof\}",
                tail,
                re.S,
            )
            proof = proof_match.group(1) if proof_match else ""
            nodes.append(
                {
                    "id": labels[0],
                    "aliases": labels[1:],
                    "kind": match.group(1),
                    "title": (match.group(2) or match.group(1).title()).strip(),
                    "statementTex": statement,
                    "proofTex": proof,
                    "source": rel(source),
                    "sourceOrder": len(nodes),
                }
            )
    return nodes


def group_for(node: dict[str, Any]) -> str:
    node_id = node["id"]
    source = node["source"]
    if node_id in {"thm:main", "cor:expanded-closed"}:
        return "Final assembly"
    if source.endswith(
        (
            "02_structure_and_common_geometry.tex",
            "02_reader_framework.tex",
            "02_structural_reductions.tex",
            "02b_admissible_set_derivation.tex",
            "04a_signed_center_calculus.tex",
            "A_strict_handoff_optimization.tex",
            "appendix_certificates.tex",
            "A_structural_shared_signed_optimization.tex",
        )
    ):
        return "Common geometry / Appendix A"
    if source.endswith(
        (
            "03_trace_bounds.tex",
            "03_strategy1_reader.tex",
            "03_strategy1_length.tex",
            "04b_common_CE1_CE2_budgets.tex",
            "B_trace_length_optimization.tex",
        )
    ):
        return "Method 1: trace length / Appendix B"
    if source.endswith(
        (
            "05_area_loss_full.tex",
            "05_strategy3_reader.tex",
            "05_strategy3_area.tex",
            "C_area_loss_optimization.tex",
        )
    ):
        return "Method 2: area loss / Appendix C"
    if node_id in {
        "prop:app-disk-finite-caliper",
        "lem:app-disk-point-formula",
        "thm:new-complementary-gap",
        "thm:new-ce2-short-ray",
    }:
        return "Method 3: universal terminals / Appendix D"
    if node_id in {
        "prop:new-nplus-zero-gap-closures",
        "lem:readable-k410-forced",
        "prop:readable-k410-ce1",
        "prop:readable-k410-ce2",
        "prop:new-nplus-one-all-vd0",
        "prop:new-one-t3-terminal",
        "prop:new-one-vd-assembly",
        "prop:finite-enclosure-nonzero-gap-branches",
    }:
        return "Method 3: nonzero-gap cases / Appendix D"
    if source.endswith(
        (
            "06_finite_enclosure_full.tex",
            "06a_neighbor_ray_calculus.tex",
            "06i_simplified_finite_enclosure_interfaces.tex",
            "06b_ce1_direct_certificate.tex",
            "06d_detailed_direct_certificates.tex",
            "06_finite_enclosure_reader.tex",
            "D_local_output_calculus.tex",
            "D_nonzero_gap_finite_enclosure_optimization.tex",
            "D_two_chart_vd1_replacement.tex",
        )
    ):
        return "Method 3: local toolkit / Appendix D"
    if source.endswith("A_zero_gap_exact_certificate.tex"):
        return "Appendix F: exact mixed-overlap certificate"
    if node_id == "prop:technical-four-overlaps" or source.endswith(
        "06_zero_gap_completion.tex"
    ):
        return "Method 3: zero-gap completion / Appendix E"
    if source.endswith(
        (
            "06_zero_gap_ab_core.tex",
            "06_strategy4_reader.tex",
            "E_zero_gap_nine_point_optimization.tex",
        )
    ):
        return "Method 3: zero-gap witnesses / Appendix E"
    if source.endswith("07_exhaustive_assembly.tex"):
        return "Final assembly"
    raise RuntimeError(f"no architecture group declared for {node_id} in {source}")


ROUTING_NODES = {
    "prop:exhaustive-structural-reduction",
    "prop:length-branches",
    "cor:signed-budget-branches",
    "prop:area-branches",
    "prop:new-nplus-zero-gap-closures",
    "prop:new-one-t3-terminal",
    "prop:new-one-vd-assembly",
    "prop:finite-enclosure-nonzero-gap-branches",
    "prop:reader-ab-core-branches",
    "thm:main",
    "cor:expanded-closed",
}
CASE_TERMINALS = {
    "prop:ce2-vd2-midpoint-length",
    "prop:readable-k410-ce2",
    "prop:readable-k410-ce1",
    "prop:new-nplus-one-all-vd0",
    "thm:reader-witness-enclosure",
    "thm:reader-zero-gap-obstruction",
}
CERTIFICATE_NODES = {
    "thm:cert-caliper",
    "lem:paper-branchwise-cbar",
    "lem:paper-residual-to-overlap",
    "thm:paper-exact-mixed-certificate",
    "prop:technical-four-overlaps",
}


def role_for(node_id: str) -> str:
    if node_id in ROUTING_NODES:
        return "Routing / assembly"
    if node_id in CASE_TERMINALS:
        return "Case-closing terminal"
    if node_id in CERTIFICATE_NODES:
        return "Exact certificate"
    if node_id.startswith("prop:readable-") or node_id.startswith("lem:readable-"):
        return "Canonical interface"
    return "Reusable theorem / lemma"


CASE_META: dict[str, dict[str, Any]] = {
    "thm:main": {
        "cases": ["All routing rows R0-R13 (R6 split as R6a/R6b)"],
        "detail": "The final contradiction after Method 1, Method 2, and both Method 3 chapters dispatch every row.",
    },
    "cor:expanded-closed": {
        "cases": ["Every L>1 in the scaled closed formulation"],
        "detail": "Compactness and scaling transfer the main open-triangle theorem.",
    },
    "prop:ce-classification": {
        "cases": ["CE0", "CE1", "CE2"],
        "detail": "Classifies the C triangle by the number of positive boundary-edge traces.",
    },
    "prop:vertex-classification": {
        "cases": ["Vd0", "Vd1", "Vd2", "T3-like"],
        "detail": "The normalized exhaustive V-role classification.",
    },
    "lem:gap-exhaustion": {
        "cases": ["N_gap=0", "N_gap=1", "N_gap=2"],
        "detail": "Relates actual open boundary traces to the complete gap split, including singleton gaps.",
    },
    "prop:exhaustive-structural-reduction": {
        "cases": ["Every row R0-R13 (R6 split as R6a/R6b)"],
        "detail": "The unique routing assignment for a hypothetical cover.",
    },
    "prop:length-branches": {
        "cases": [
            "R0: N_gap=0, N_+=0",
            "R1: N_gap=0, N_+=1 with Vd1/Vd2",
            "R5/R6 high skeleton count",
            "R8 and R12 Vd length rows",
            "Vd2 neighboring-midpoint hybrid",
        ],
        "detail": "Collects every row closed by perimeter or skeleton length.",
    },
    "prop:area-branches": {
        "cases": ["R2: zero gap, unique supercritical and T3-like", "R4: zero gap, N_+>=2"],
        "detail": "The two center-independent cyclic area-loss rows.",
    },
    "prop:app-disk-finite-caliper": {
        "cases": ["A centered disk plus finitely many forced points"],
        "detail": "A minimizing side has a point--point contact, a point--disk tangent contact, or a disk-only support regime.",
    },
    "lem:app-one-third-radial-envelope": {
        "cases": ["Row E_1: adjacent Vd half-edge domain"],
        "detail": "Strengthens the general quarter envelope to c_max(M,m)<1-m/3 when M>=1/2.",
    },
    "lem:app-rescuer-tail-budget": {
        "cases": ["Rows D_1 and D_2: T3-like and Vd1 supported tails"],
        "detail": "Factors the common center-hiding and four-role path budget out of the T3-like and Vd1 proofs.",
    },
    "thm:new-complementary-gap": {
        "cases": ["Row A: one gap, N_+=0, Vd0/T3-like"],
        "detail": "The common radial disk plus the actual complementary gap has enclosure number at least one.",
    },
    "thm:new-ce2-short-ray": {
        "cases": ["Row B: two gaps, CE2, N_+ in {0,1}"],
        "detail": "The exact signed CE2 optimization places D_2 and D_4 in U_C but not both in T_C.",
    },
    "prop:new-nplus-zero-gap-closures": {
        "cases": [
            "Rows A and B",
            "R7/R9: N_+=0, no Vd1/Vd2, one or two gaps",
        ],
        "detail": "Assembly of the one-gap and two-gap universal terminals.",
    },
    "lem:readable-k410-forced": {
        "cases": ["Row C: one gap, N_+=1, all Vd0"],
        "detail": "Forces the seven-point set K_tr: O, M_0, both gap endpoints, and only P_2,P_3,P_4.",
    },
    "prop:readable-k410-ce1": {
        "cases": ["Row C, CE1"],
        "detail": "The reverse-path certificate contradicts the common terminal upper bound at T_0.",
    },
    "prop:readable-k410-ce2": {
        "cases": ["Row C, CE2"],
        "detail": "A T_4/T_2 high-radial threshold dichotomy contradicts the same upper bound.",
    },
    "prop:new-nplus-one-all-vd0": {
        "cases": ["Row C: one gap, N_+=1, all Vd0"],
        "detail": "The transverse seven-point witness K_tr has Lambda>=1; the former K_410 follows by inclusion.",
    },
    "prop:new-one-t3-terminal": {
        "cases": ["Row D_1 / the one-gap part of R11"],
        "detail": "The one-gap T3-like supported-tail terminal; the two-gap part of R11 instead closes by Row B.",
    },
    "prop:finite-vd1-supported-terminal": {
        "cases": ["Row D_2 / a supported-tail part of R13"],
        "detail": "The Vd1 supported-tail adapter feeds the common rescuer-tail budget.",
    },
    "prop:finite-vd-radial-separation": {
        "cases": ["Rows E_1 and E_2 / adjacent and nonadjacent parts of R13"],
        "detail": "A radial interval or the exact point D_tau remains outside every covering triangle.",
    },
    "prop:finite-two-chart-router": {
        "cases": ["R13 replacement router (not an additional A--F terminal row)"],
        "detail": "Replaces the distinguished pair, recomputes the output gap rank, and routes ranks 0, 1, and 2 to their established closers.",
    },
    "prop:new-one-vd-assembly": {
        "cases": ["R13 / Rows D_2, E_1, E_2, and the replacement router"],
        "detail": "Assembly of four separately named Vd placements plus the Vd2 Method 1 exit.",
    },
    "prop:finite-enclosure-nonzero-gap-branches": {
        "cases": ["Rows A--E: every nonzero-gap Method 3 row"],
        "detail": "Canonical nonzero-gap assembly after the exact finite-enclosure register.",
    },
    "lem:ab-extreme-jump": {
        "cases": ["Row F: zero gap, exactly one supercritical Vd0 role"],
        "detail": "Identifies the strict handoff minimum and maximum and the common boundary pair.",
    },
    "thm:strict-ab-union": {
        "cases": ["Row F: unique strict supercritical row"],
        "detail": "Exact disk/half-plane description of the strict AB-union frontier.",
    },
    "lem:symmetric-core-witness": {
        "cases": ["Row F"],
        "detail": "Six radial points force a centered disk into U_C.",
    },
    "lem:asymmetric-core-witness": {
        "cases": ["Row F"],
        "detail": "Forces the three parameter-dependent frontier witnesses Q_-,Q_0,Q_+ into U_C.",
    },
    "thm:paper-exact-mixed-certificate": {
        "cases": ["Row F, c_*>2/3, two mixed unequal-radius cap overlaps"],
        "detail": "Exact integer/Bernstein certificate; no floating-point or interval arithmetic.",
    },
    "prop:technical-four-overlaps": {
        "cases": ["Row F, c_*>2/3"],
        "detail": "Combines two analytic equal-radius overlaps with the two exact mixed overlaps.",
    },
    "thm:reader-witness-enclosure": {
        "cases": ["Row F: zero gap, N_+=1, all Vd0; any CE0/CE1/CE2"],
        "detail": "The exact nine-point witness set has enclosure number at least one.",
    },
    "thm:reader-zero-gap-obstruction": {
        "cases": ["Row F / routing row R3"],
        "detail": "The nine forced points cannot be contained in the open unit C triangle.",
    },
    "prop:reader-ab-core-branches": {
        "cases": ["R3: zero gap, N_+=1, all Vd0"],
        "detail": "Routes the unique remaining zero-gap row to the separate nine-point chapter.",
    },
}


MANUAL_DEPS: dict[str, list[str]] = {
    "thm:main": [
        "prop:exhaustive-structural-reduction",
        "prop:length-branches",
        "prop:area-branches",
        "prop:finite-enclosure-nonzero-gap-branches",
        "prop:new-one-vd-assembly",
        "prop:reader-ab-core-branches",
    ],
    "cor:expanded-closed": ["thm:main", "prop:open-closed-scaled"],
    "prop:ce-classification": ["lem:distinct-roles"],
    "prop:vd0-exact-trace-normalization": ["lem:local-wedge"],
    "prop:vertex-classification": ["lem:local-wedge", "prop:vd0-exact-trace-normalization"],
    "lem:gap-exhaustion": ["lem:distinct-roles", "prop:ce-classification"],
    "lem:t3-nonsupercritical": ["prop:t3-translation"],
    "prop:strict-handoffs": ["lem:gap-exhaustion"],
    "prop:unique-center-midpoint": ["prop:app-signed-center-optimization"],
    "prop:exhaustive-structural-reduction": [
        "prop:ce-classification",
        "prop:vertex-classification",
        "lem:gap-exhaustion",
        "prop:unique-center-midpoint",
    ],
    "prop:app-signed-center-optimization": ["prop:ce-classification"],
    "lem:center-skeleton-cap": ["prop:unique-center-midpoint", "prop:app-signed-center-optimization"],
    "lem:positive-support-skeleton-cap": ["lem:center-skeleton-cap"],
    "lem:no-support-skeleton-cap": ["thm:boundary-trace-table"],
    "lem:supercritical-skeleton-cap": ["lem:app-local-admissible-set"],
    "lem:positive-support-rescuer": ["prop:unique-center-midpoint", "lem:self-midpoint"],
    "prop:vd-corner-normal-form": ["prop:vertex-classification"],
    "lem:vd2-neighbor-midpoint-cap": ["prop:vd-corner-normal-form"],
    "thm:boundary-trace-table": [
        "cor:signed-center-boundary",
        "prop:vd-corner-normal-form",
        "lem:t3-nonsupercritical",
    ],
    "lem:signed-perimeter-deficit": ["thm:boundary-trace-table"],
    "thm:common-skeleton-count": [
        "lem:center-skeleton-cap",
        "lem:positive-support-skeleton-cap",
        "lem:no-support-skeleton-cap",
        "lem:supercritical-skeleton-cap",
    ],
    "cor:signed-budget-branches": [
        "lem:signed-perimeter-deficit",
        "thm:common-skeleton-count",
        "lem:vd2-neighbor-midpoint-cap",
    ],
    "lem:area-wedge": ["lem:local-wedge"],
    "thm:local-square-loss": ["lem:area-wedge"],
    "thm:t3-direct-loss": ["lem:t3-nonsupercritical", "prop:t3-translation"],
    "lem:cyclic-area-loss": ["thm:local-square-loss", "thm:t3-direct-loss"],
    "prop:area-branches": ["prop:strict-handoffs", "lem:cyclic-area-loss"],
    "lem:new-compact-open-shrink": ["lem:app-open-closed-scaling"],
    "lem:app-shared-enclosure-gauge": [],
    "lem:app-local-admissible-set": ["lem:app-shared-enclosure-gauge"],
    "lem:app-direct-threshold": ["lem:app-local-admissible-set", "prop:app-four-direct-outputs"],
    "lem:app-selected-chords": ["lem:app-local-admissible-set", "prop:app-four-direct-outputs"],
    "prop:app-neighbor-ray-formula": ["lem:app-shared-enclosure-gauge"],
    "prop:app-four-direct-outputs": ["lem:app-local-admissible-set"],
    "lem:app-one-third-radial-envelope": ["lem:app-local-admissible-set"],
    "lem:new-type-aware-radial-forcing": [
        "lem:app-local-admissible-set",
        "prop:app-neighbor-ray-formula",
        "lem:reach-initial-segments",
    ],
    "lem:new-common-pair-domination": ["lem:app-local-admissible-set", "prop:app-neighbor-ray-formula"],
    "prop:app-disk-finite-caliper": ["lem:app-shared-enclosure-gauge"],
    "lem:app-disk-point-formula": ["prop:app-disk-finite-caliper"],
    "thm:new-complementary-gap": [
        "lem:app-disk-point-formula",
        "lem:new-common-pair-domination",
        "lem:app-local-admissible-set",
    ],
    "thm:new-ce2-short-ray": ["prop:app-signed-center-optimization", "lem:app-local-admissible-set"],
    "prop:new-nplus-zero-gap-closures": [
        "lem:gap-exhaustion",
        "lem:app-local-admissible-set",
        "prop:app-neighbor-ray-formula",
        "prop:app-signed-center-optimization",
        "lem:new-type-aware-radial-forcing",
        "lem:new-common-pair-domination",
        "thm:new-complementary-gap",
        "lem:new-compact-open-shrink",
        "thm:new-ce2-short-ray",
    ],
    "lem:readable-k410-forced": ["lem:reach-initial-segments", "lem:gap-exhaustion"],
    "lem:app-transverse-upper-squeeze": ["prop:app-signed-center-optimization", "lem:signed-diameter-transfer"],
    "prop:app-ce1-direct-certificate": [
        "prop:app-signed-center-optimization",
        "lem:app-selected-chords",
        "lem:app-direct-threshold",
    ],
    "prop:readable-k410-ce1": ["lem:app-transverse-upper-squeeze", "prop:app-ce1-direct-certificate"],
    "prop:readable-k410-ce2": [
        "lem:app-transverse-upper-squeeze",
        "lem:app-direct-threshold",
        "prop:app-signed-center-optimization",
    ],
    "prop:new-nplus-one-all-vd0": [
        "lem:readable-k410-forced",
        "prop:readable-k410-ce1",
        "prop:readable-k410-ce2",
        "lem:new-compact-open-shrink",
    ],
    "lem:app-rescuer-tail-budget": [
        "prop:app-signed-center-optimization",
        "lem:app-local-admissible-set",
    ],
    "prop:new-one-t3-terminal": [
        "prop:t3-translation",
        "lem:self-midpoint",
        "lem:reach-initial-segments",
        "lem:app-rescuer-tail-budget",
    ],
    "prop:new-one-vd-assembly": [
        "lem:signed-small-slack",
        "lem:app-one-third-radial-envelope",
        "prop:vd-corner-normal-form",
        "lem:signed-endpoints-dominate-slack",
        "lem:signed-diameter-transfer",
        "lem:app-rescuer-tail-budget",
        "thm:new-complementary-gap",
        "thm:new-ce2-short-ray",
        "prop:length-branches",
        "prop:ce2-vd2-midpoint-length",
    ],
    "prop:finite-enclosure-nonzero-gap-branches": [
        "prop:new-nplus-zero-gap-closures",
        "prop:new-nplus-one-all-vd0",
        "prop:new-one-t3-terminal",
        "prop:new-one-vd-assembly",
        "thm:new-ce2-short-ray",
    ],
    "lem:ab-extreme-jump": ["prop:strict-handoffs"],
    "thm:strict-ab-union": ["thm:cert-caliper", "lem:ab-extreme-jump"],
    "lem:symmetric-core-witness": ["lem:ab-extreme-jump", "lem:app-local-admissible-set"],
    "lem:fixed-line-signs": ["thm:strict-ab-union", "lem:ab-extreme-jump"],
    "lem:asymmetric-core-witness": ["thm:strict-ab-union", "lem:fixed-line-signs", "lem:reach-initial-segments"],
    "lem:technical-newton-reduction": ["lem:fixed-line-signs", "lem:asymmetric-core-witness"],
    "lem:paper-branchwise-cbar": ["lem:app-local-admissible-set", "lem:ab-extreme-jump"],
    "lem:paper-residual-to-overlap": ["lem:paper-branchwise-cbar", "lem:technical-newton-reduction"],
    "thm:paper-exact-mixed-certificate": ["lem:paper-branchwise-cbar", "lem:paper-residual-to-overlap"],
    "prop:technical-four-overlaps": ["lem:technical-newton-reduction", "thm:paper-exact-mixed-certificate"],
    "lem:reader-cap-chain": ["lem:app-shared-enclosure-gauge"],
    "thm:reader-witness-enclosure": [
        "lem:symmetric-core-witness",
        "lem:asymmetric-core-witness",
        "lem:technical-newton-reduction",
        "prop:technical-four-overlaps",
        "lem:reader-cap-chain",
    ],
    "thm:reader-zero-gap-obstruction": ["thm:reader-witness-enclosure", "lem:new-compact-open-shrink"],
    "prop:reader-ab-core-branches": ["thm:reader-zero-gap-obstruction", "lem:gap-exhaustion"],
}


ROUTING_ROWS = [
    ["R0", "0", "0", "all", "all", ["prop:length-branches"], "boundary overlap/length"],
    ["R1", "0", "1", "d>=1", "all", ["prop:length-branches"], "Vd boundary deficit"],
    ["R2", "0", "1", "d=0, t>=1", "all", ["prop:area-branches"], "cyclic area loss"],
    ["R3", "0", "1", "(d,t)=(0,0)", "CE0/CE1/CE2", ["prop:reader-ab-core-branches"], "separate nine-point chapter"],
    ["R4", "0", ">=2", "all", "all", ["prop:area-branches"], "cyclic area loss"],
    ["R5", ">=1", ">=2", "all", "CE1/CE2", ["prop:length-branches"], "positive-support rescuer"],
    ["R6a", ">=1", "0", "d+t>=3", "CE1/CE2", ["prop:length-branches"], "skeleton count"],
    ["R6b", ">=1", "1", "d+t>=2", "CE1/CE2", ["prop:length-branches"], "skeleton count"],
    ["R7", ">=1", "0", "(d,t)=(0,0)", "CE1/CE2", ["prop:new-nplus-zero-gap-closures"], "complementary-gap / CE2 short-ray terminals"],
    ["R8", ">=1", "0", "d>=1, d+t<=2", "CE1/CE2", ["prop:length-branches"], "Vd deficit"],
    ["R9", ">=1", "0", "d=0, t=1 or 2", "CE1/CE2", ["prop:new-nplus-zero-gap-closures"], "type-aware common pair"],
    ["R10", ">=1", "1", "(d,t)=(0,0)", "CE1/CE2", ["prop:new-nplus-one-all-vd0", "thm:new-ce2-short-ray"], "anisotropic/short ray"],
    ["R11", ">=1", "1", "(d,t)=(0,1)", "CE1/CE2", ["prop:new-one-t3-terminal", "thm:new-ce2-short-ray"], "one-gap supported tail / two-gap short ray"],
    ["R12", ">=1", "1", "(d,t)=(1,0)", "CE1", ["prop:length-branches"], "CE1 length exit"],
    ["R13", ">=1", "1", "(d,t)=(1,0)", "CE2", ["prop:new-one-vd-assembly"], "four named placements"],
]

FINITE_ROWS = [
    {"id": "A", "case": "N_gap=1, N_+=0, d=0, t in {0,1,2}", "forced": "the common radial disk and actual gap G_0 lie in U_C, with enclosure number at least one", "closer": "prop:new-nplus-zero-gap-closures", "figures": ["one_gap_n0"]},
    {"id": "B", "case": "N_gap=2, N_+ in {0,1}, d=0, N_E(T_C)=2", "forced": "D_2,D_4 lie in U_C but are not both in T_C", "closer": "thm:new-ce2-short-ray", "figures": ["two_gap_vd0", "two_gap_n1_t3"]},
    {"id": "C", "case": "N_gap=1, N_+=1, (d,t)=(0,0)", "forced": "K_tr, using the actual gap endpoints and P_2,P_3,P_4, lies in U_C and has enclosure number at least one", "closer": "prop:new-nplus-one-all-vd0", "figures": ["one_gap_n1_ce1", "one_gap_n1_ce2"]},
    {"id": "D_1", "case": "N_gap=1, N_+=1, (d,t)=(0,1)", "forced": "R_1(u)=epsilon V_1 lies in U_C and the four-role trace sum is greater than four", "closer": "prop:new-one-t3-terminal", "figures": ["one_gap_n1_t3"]},
    {"id": "D_2", "case": "N_gap in {1,2}, N_+=1, (d,t)=(1,0): supported-tail subcase", "forced": "R_1(u)=epsilon V_1 lies in U_C and the four-role trace sum is greater than four", "closer": "prop:finite-vd1-supported-terminal", "figures": ["vd1_rescuer"]},
    {"id": "E_1", "case": "N_gap in {1,2}, N_+=1, (d,t)=(1,0), tau in {1,5}", "forced": "c_loc<1-d_C leaves an uncovered interval on the routed radial arm", "closer": "prop:finite-vd-radial-separation", "figures": ["adjacent_vd"]},
    {"id": "E_2", "case": "N_gap in {1,2}, N_+=1, (d,t)=(1,0), tau in {2,3,4}", "forced": "d_tau^C<rho<1-C_tau and D_tau=rho V_tau is uncovered", "closer": "prop:finite-vd-radial-separation", "figures": ["nonadjacent_vd"]},
    {"id": "F", "case": "N_gap=0, N_+=1, (d,t)=(0,0)", "forced": "K_wit(a,b), formed from the six P_i^{rad} and Q_-,Q_0,Q_+, lies in U_C and has enclosure number at least one", "closer": "thm:reader-zero-gap-obstruction", "figures": ["zero_gap_original"]},
    {"id": "Router", "case": "R13 two-chart Vd1 replacement (not an additional A--F terminal row)", "forced": "a replacement cover with output gap rank 0, 1, or 2, routed to the established rank-specific closer", "closer": "prop:finite-two-chart-router", "figures": ["replacement"]},
]


def data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def figure_data() -> dict[str, dict[str, str]]:
    pfig = PAPER / "figures"
    assets = ROOT / "interactive" / "assets" / "readable_dependency"
    definitions = {
        "method3_spine": (assets / "method3_dependency_spine.png", "Canonical Method 3 dependency spine."),
        "zero_gap_original": (assets / "zero_gap_nine_point_witness.png", "Original repository nine-point witness schematic, restored from the historical TikZ source."),
        "one_gap_n0": (pfig / "trace_exact_ab" / "one_gap_n0_vd0.png", "One gap, N_+=0, all Vd0."),
        "two_gap_vd0": (pfig / "trace_exact_ab" / "two_gap_vd0.png", "Two-gap CE2 all-Vd0 branch."),
        "one_gap_n1_ce1": (pfig / "trace_exact_ab" / "one_gap_n1_vd0_ce1.png", "Anisotropic one-gap branch, CE1."),
        "one_gap_n1_ce2": (pfig / "trace_exact_ab" / "one_gap_n1_vd0_ce2.png", "Anisotropic one-gap branch, CE2."),
        "one_gap_n1_t3": (pfig / "trace_exact_ab" / "one_gap_n1_t3.png", "One-gap T3-like rescuer."),
        "two_gap_n1_t3": (pfig / "trace_exact_ab" / "two_gap_n1_t3.png", "Two-gap CE2 T3-like branch."),
        "adjacent_vd": (pfig / "trace_exact_ab" / "adjacent_vd.png", "Adjacent Vd radial-separation branch."),
        "nonadjacent_vd": (pfig / "trace_exact_ab" / "nonadjacent_vd.png", "Nonadjacent Vd radial-separation branch."),
        "vd1_rescuer": (pfig / "trace_exact_ab" / "vd1_rescuer.png", "Vd1 neighboring-midpoint rescuer."),
        "replacement": (pfig / "trace_exact_ab" / "replacement_output.png", "Two-chart replacement output."),
        "area_local": (pfig / "strategy3_local_area_loss.png", "Local Method 2 area-loss geometry."),
        "area_global": (pfig / "strategy3_global_area_loss.png", "Global cyclic Method 2 area-loss geometry."),
        "ce0": (pfig / "role_examples" / "center_role_ce0_example.png", "CE0 center role."),
        "ce1": (pfig / "role_examples" / "center_role_ce1_example.png", "CE1 center role."),
        "ce2": (pfig / "role_examples" / "center_role_ce2_example.png", "CE2 center role."),
        "vd0": (pfig / "role_examples" / "vertex_role_vd0_nonsupercritical_example.png", "Nonsupercritical Vd0 role."),
        "vd0plus": (pfig / "role_examples" / "vertex_role_vd0_supercritical_example.png", "Supercritical Vd0 role."),
        "vd1": (pfig / "role_examples" / "vertex_role_vd1_example.png", "Vd1 role."),
        "vd2": (pfig / "role_examples" / "vertex_role_vd2_example.png", "Vd2 role."),
        "t3": (pfig / "role_examples" / "vertex_role_t3_like_example.png", "T3-like role."),
    }
    result: dict[str, dict[str, str]] = {}
    for key, (path, caption) in definitions.items():
        if not path.is_file():
            continue
        result[key] = {
            "src": data_uri(path),
            "caption": caption,
            "repositoryPath": rel(path),
            "url": f"https://github.com/{REPOSITORY}/blob/{BRANCH}/{rel(path)}",
        }
    return result


FIGURE_ASSOC = {
    "prop:ce-classification": ["ce0", "ce1", "ce2"],
    "prop:vertex-classification": ["vd0", "vd0plus", "vd1", "vd2", "t3"],
    "prop:vd-corner-normal-form": ["vd1", "vd2"],
    "lem:vd2-neighbor-midpoint-cap": ["vd2"],
    "thm:local-square-loss": ["area_local"],
    "lem:cyclic-area-loss": ["area_global"],
    "prop:area-branches": ["area_local", "area_global"],
    "lem:new-type-aware-radial-forcing": ["one_gap_n0"],
    "thm:new-complementary-gap": ["one_gap_n0"],
    "thm:new-ce2-short-ray": ["two_gap_vd0", "two_gap_n1_t3"],
    "prop:new-nplus-zero-gap-closures": ["one_gap_n0", "two_gap_vd0"],
    "lem:readable-k410-forced": ["one_gap_n1_ce1", "one_gap_n1_ce2"],
    "prop:new-nplus-one-all-vd0": ["one_gap_n1_ce1", "one_gap_n1_ce2"],
    "lem:app-rescuer-tail-budget": ["one_gap_n1_t3", "vd1_rescuer"],
    "prop:new-one-t3-terminal": ["one_gap_n1_t3"],
    "prop:finite-vd1-supported-terminal": ["vd1_rescuer"],
    "prop:finite-vd-radial-separation": ["adjacent_vd", "nonadjacent_vd"],
    "prop:finite-two-chart-router": ["replacement"],
    "prop:new-one-vd-assembly": ["adjacent_vd", "nonadjacent_vd", "vd1_rescuer", "replacement"],
    "lem:ab-extreme-jump": ["zero_gap_original"],
    "thm:strict-ab-union": ["zero_gap_original"],
    "lem:symmetric-core-witness": ["zero_gap_original"],
    "lem:asymmetric-core-witness": ["zero_gap_original"],
    "thm:reader-witness-enclosure": ["zero_gap_original"],
    "thm:reader-zero-gap-obstruction": ["zero_gap_original"],
    "prop:reader-ab-core-branches": ["zero_gap_original"],
    "prop:finite-enclosure-nonzero-gap-branches": ["method3_spine"],
}


PROOF_REFS: dict[str, list[dict[str, str]]] = defaultdict(list)


def add_proof_ref(ids: set[str], name: str, path: str) -> None:
    url = f"https://github.com/{REPOSITORY}/blob/{BRANCH}/{path}"
    for node_id in ids:
        PROOF_REFS[node_id].append({"name": name, "url": url})


add_proof_ref(
    {
        "lem:app-shared-enclosure-gauge",
        "lem:app-local-admissible-set",
        "prop:app-neighbor-ray-formula",
        "lem:new-type-aware-radial-forcing",
        "lem:new-common-pair-domination",
        "lem:app-disk-point-formula",
        "thm:new-complementary-gap",
        "thm:new-ce2-short-ray",
        "lem:reach-initial-segments",
        "lem:new-compact-open-shrink",
    },
    "2608 reusable finite-enclosure geometry",
    "proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md",
)
add_proof_ref(
    {
        "prop:app-disk-finite-caliper",
        "lem:app-one-third-radial-envelope",
        "lem:app-rescuer-tail-budget",
        "thm:new-ce2-short-ray",
    },
    "2609 simplified finite-enclosure lemmas",
    "proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md",
)
add_proof_ref(
    {
        "lem:readable-k410-forced",
        "lem:app-transverse-upper-squeeze",
        "prop:readable-k410-ce1",
        "prop:readable-k410-ce2",
        "prop:new-nplus-one-all-vd0",
    },
    "4103 transverse seven-point enclosure",
    "proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4103_transverse_seven_point_enclosure.md",
)

add_proof_ref(
    {"prop:new-nplus-zero-gap-closures"},
    "4013_new all-Vd0 finite enclosure",
    "proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md",
)
add_proof_ref(
    {"prop:new-nplus-zero-gap-closures"},
    "4070_new T3-like finite enclosure",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md",
)
add_proof_ref(
    {"lem:readable-k410-forced", "prop:readable-k410-ce2", "prop:new-nplus-one-all-vd0"},
    "4101_new all-Vd0 finite enclosure",
    "proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md",
)
add_proof_ref(
    {"prop:app-ce1-direct-certificate", "prop:readable-k410-ce1", "prop:new-nplus-one-all-vd0"},
    "4102_new CE1 direct radial certificate",
    "proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md",
)
add_proof_ref(
    {"prop:new-one-t3-terminal"},
    "4130_new T3-like finite enclosure",
    "proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md",
)
add_proof_ref(
    {"prop:new-one-vd-assembly"},
    "4140_new one-Vd finite-enclosure assembly",
    "proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md",
)
for zero_id in {
    "lem:ab-extreme-jump",
    "thm:strict-ab-union",
    "lem:symmetric-core-witness",
    "lem:fixed-line-signs",
    "lem:asymmetric-core-witness",
    "lem:technical-newton-reduction",
    "prop:technical-four-overlaps",
    "lem:reader-cap-chain",
    "thm:reader-witness-enclosure",
    "thm:reader-zero-gap-obstruction",
    "prop:reader-ab-core-branches",
    "lem:paper-branchwise-cbar",
    "lem:paper-residual-to-overlap",
    "thm:paper-exact-mixed-certificate",
}:
    PROOF_REFS[zero_id].append(
        {
            "name": "3105X direct nine-point proof package",
            "url": f"https://github.com/{REPOSITORY}/tree/{BRANCH}/proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point",
        }
    )


def build_data() -> dict[str, Any]:
    sources = active_sources()
    nodes = parse_nodes(sources)
    by_id = {node["id"]: node for node in nodes}
    if len(by_id) != len(nodes):
        duplicates = sorted(
            node_id
            for node_id in by_id
            if sum(node["id"] == node_id for node in nodes) > 1
        )
        raise RuntimeError(f"duplicate canonical statement labels: {duplicates}")

    declared_targets = set(MANUAL_DEPS)
    declared_prerequisites = {
        dependency for dependencies in MANUAL_DEPS.values() for dependency in dependencies
    }
    missing_declared = sorted((declared_targets | declared_prerequisites) - set(by_id))
    if missing_declared:
        raise RuntimeError(f"declared dependencies name missing canonical nodes: {missing_declared}")

    routing_closers = {closer for row in ROUTING_ROWS for closer in row[5]}
    card_closers = {row["closer"] for row in FINITE_ROWS}
    missing_closers = sorted((routing_closers | card_closers) - set(by_id))
    if missing_closers:
        raise RuntimeError(f"routing/card closers name missing canonical nodes: {missing_closers}")

    all_labels: dict[str, str] = {}
    for node in nodes:
        all_labels[node["id"]] = node["id"]
        for alias in node["aliases"]:
            all_labels[alias] = node["id"]

    for node in nodes:
        explicit = {
            all_labels[label]
            for label in reference_labels(node.pop("proofTex"))
            if label in all_labels and all_labels[label] != node["id"]
        }
        declared = set(MANUAL_DEPS.get(node["id"], []))
        node["deps"] = sorted(explicit | declared)
        node["group"] = group_for(node)
        node["groupIndex"] = GROUPS.index(node["group"])
        node["role"] = role_for(node["id"])
        meta = CASE_META.get(
            node["id"],
            {
                "cases": ["Reusable wherever its hypotheses occur"],
                "detail": "This is an interface theorem rather than a routing terminal.",
            },
        )
        node["cases"] = meta["cases"]
        node["caseDetail"] = meta["detail"]
        node["figureKeys"] = FIGURE_ASSOC.get(node["id"], [])
        node["sourceLinks"] = [
            {
                "name": node["source"],
                "url": f"https://github.com/{REPOSITORY}/blob/{BRANCH}/{node['source']}",
            }
        ]
        if node["id"] in {"thm:main", "cor:expanded-closed"}:
            node["sourceLinks"].append(
                {
                    "name": "arrange/paper_draft/07_exhaustive_assembly.tex",
                    "url": f"https://github.com/{REPOSITORY}/blob/{BRANCH}/arrange/paper_draft/07_exhaustive_assembly.tex",
                }
            )
        node["proofRefs"] = PROOF_REFS.get(node["id"], [])

    # Reverse edges and DAG audit.
    outgoing: dict[str, list[str]] = {node_id: [] for node_id in by_id}
    indegree: dict[str, int] = {node_id: 0 for node_id in by_id}
    for node in nodes:
        for dep in node["deps"]:
            outgoing[dep].append(node["id"])
            indegree[node["id"]] += 1
    queue: deque[str] = deque(sorted(node_id for node_id, degree in indegree.items() if degree == 0))
    visited: list[str] = []
    while queue:
        node_id = queue.popleft()
        visited.append(node_id)
        for target in outgoing[node_id]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    if len(visited) != len(nodes):
        cyclic = sorted(node_id for node_id, degree in indegree.items() if degree)
        raise RuntimeError(f"declared logical graph has a cycle: {cyclic}")
    for node in nodes:
        node["usedBy"] = sorted(outgoing[node["id"]])

    figures = figure_data()
    for node in nodes:
        node["figureKeys"] = [key for key in node["figureKeys"] if key in figures]

    report_markdown = REPORT.read_text(encoding="utf-8") if REPORT.is_file() else "# Implementation report\n\nPending final audit."
    report_html = (
        mistune.html(report_markdown)
        if mistune is not None
        else "<pre>" + report_markdown.replace("&", "&amp;").replace("<", "&lt;") + "</pre>"
    )
    return {
        "meta": {
            "repository": REPOSITORY,
            "branch": BRANCH,
            "nodeCount": len(nodes),
            "edgeCount": sum(len(node["deps"]) for node in nodes),
            "activeSourceCount": len(sources),
            "newArchitecture": [
                "exact body definitions and compact interfaces",
                "solved optimization Appendices A--E",
                "exact finite-enclosure register A--F",
                "separate zero-gap nine-point optimization",
                "exact mixed-overlap certificate in Appendix F",
                "final assembly",
            ],
            "graphSemantics": "Each arrow prerequisite -> result is an explicit theorem citation or a declared logical/routing interface. Historical untyped Markdown-reference cycles are not used.",
            "paperEntryPoint": "arrange/paper_draft/main.tex",
            "pdf": "arrange/paper_draft/main.pdf",
        },
        "groups": GROUPS,
        "colors": COLORS,
        "nodes": nodes,
        "figures": figures,
        "routingRows": [
            {
                "id": row[0],
                "gap": row[1],
                "nplus": row[2],
                "types": row[3],
                "center": row[4],
                "closers": row[5],
                "reason": row[6],
            }
            for row in ROUTING_ROWS
        ],
        "finiteRows": FINITE_ROWS,
        "reportMarkdown": report_markdown,
        "reportHtml": report_html,
    }


HTML_TEMPLATE = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Canonical hexagon-cover proof dependency graph</title>
<style>
:root{--bg:#0a1020;--panel:#111a2e;--panel2:#18243e;--ink:#eef3ff;--muted:#aebbd5;--line:#354666;--accent:#91b9ff;--shadow:0 15px 38px rgba(0,0,0,.28)}
*{box-sizing:border-box}html,body{height:100%;margin:0;background:var(--bg);color:var(--ink);font:15px/1.48 Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif}button,input,select{font:inherit}a{color:#a9c9ff}.small{font-size:12px;color:var(--muted)}
header{padding:19px 23px 13px;background:linear-gradient(135deg,#111a31,#1b2a4a);border-bottom:1px solid #33415f}.header-row{display:flex;justify-content:space-between;gap:18px;flex-wrap:wrap}h1{font-size:25px;margin:0 0 5px}.subtitle{max-width:980px;color:var(--muted)}.stats,.actions,.chips{display:flex;gap:7px;flex-wrap:wrap;margin-top:9px}.chip,.pill{display:inline-flex;align-items:center;border:1px solid #425374;border-radius:999px;padding:4px 9px;background:#17233d;font-size:12px}.btn{display:inline-flex;border:1px solid #50668e;background:#1a2948;color:#eef3ff;padding:8px 11px;border-radius:9px;cursor:pointer;text-decoration:none}.btn:hover{background:#273b63}
.tabs{display:flex;gap:3px;padding:9px 19px 0;background:#0e1729;border-bottom:1px solid #2d3b59;overflow:auto}.tab-btn{border:0;background:transparent;color:#aebbd7;padding:10px 13px;border-radius:9px 9px 0 0;cursor:pointer;white-space:nowrap}.tab-btn.active{background:#18233d;color:white}.tab{display:none}.tab.active{display:block}
.toolbar{display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:11px 15px;background:#111a2e;border-bottom:1px solid #2e3d5b}.toolbar input,.toolbar select{background:#0c1426;color:#edf2ff;border:1px solid #425273;border-radius:8px;padding:8px 10px}.toolbar input{min-width:260px;flex:1}.legend{display:flex;gap:11px;flex-wrap:wrap;color:#b9c6df;font-size:11px}.swatch{width:13px;height:10px;border-radius:3px;display:inline-block}
.graph-shell{display:grid;grid-template-columns:minmax(0,1fr) 400px;height:calc(100vh - 205px);min-height:640px}#graphViewport{overflow:hidden;position:relative;background:radial-gradient(circle at 1px 1px,rgba(145,167,210,.18) 1px,transparent 0) 0 0/24px 24px,linear-gradient(180deg,#0b1121,#090f1c)}#graphSvg{width:100%;height:100%;touch-action:none;user-select:none}#detail{overflow:auto;border-left:1px solid #33415d;background:#10182b;padding:16px}.empty{padding:36px 12px;text-align:center;color:var(--muted)}
.band{fill:#121c32;opacity:.52}.band-label{font-size:14px;font-weight:800;fill:#dbe7ff}.edge{fill:none;stroke:#5d6e8e;stroke-width:1.35;opacity:.53}.edge.routing{stroke:#efc76a;stroke-width:2;stroke-dasharray:7 5}.edge.certificate{stroke:#d6a6ff;stroke-dasharray:3 4}.edge.dim{opacity:.06}.node{cursor:pointer}.node rect{stroke:#9db3d9;stroke-width:1.45;filter:drop-shadow(0 4px 7px rgba(0,0,0,.28))}.node.case rect{stroke-width:3}.node.dim{opacity:.1}.node.selected rect{stroke:#fff2a8;stroke-width:4}.node .kind{font-size:9.5px;fill:#dbe4f7;text-transform:uppercase;letter-spacing:.07em}.node .title{font-size:12px;font-weight:700;fill:white}.node .dot{fill:#ffe28b}
.detail-title{font-size:21px;line-height:1.25;margin:8px 0 2px}.label{font:12px/1.4 ui-monospace,SFMono-Regular,Consolas,monospace;color:#9fb4dc;word-break:break-all}.detail-section{margin:17px 0}.detail-section h3{font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:#9fb4dc;margin:0 0 7px}.statement{white-space:pre-wrap;background:#09101f;border:1px solid #33415d;border-radius:10px;padding:12px;color:#f5f1e8;font:13px/1.48 ui-monospace,SFMono-Regular,Consolas,monospace;overflow:auto}.link-list{display:flex;flex-direction:column;gap:6px}.node-link{border:0;background:#192642;color:#dce8ff;border-radius:7px;padding:7px 9px;text-align:left;cursor:pointer}.node-link:hover{background:#263a61}.gallery{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}.figure{margin:0;border:1px solid #34425f;border-radius:9px;background:#0a1120;overflow:hidden}.figure img{width:100%;display:block;background:white}.figure figcaption{font-size:11px;color:#c7d3eb;padding:7px}
.content{max-width:1540px;margin:0 auto;padding:22px}.card{background:#121a2e;border:1px solid #31405e;border-radius:13px;padding:18px;box-shadow:var(--shadow);margin-bottom:16px}.card h2,.card h3{margin-top:0}.spine-image{max-width:100%;background:white;border-radius:9px;border:1px solid #46536a;padding:4px}.flow{display:grid;grid-template-columns:repeat(5,minmax(170px,1fr));gap:10px}.flow-step{background:#17243e;border:1px solid #3b4d70;border-radius:11px;padding:13px;position:relative}.flow-step:not(:last-child)::after{content:"→";position:absolute;right:-14px;top:42%;font-size:24px;color:#8fb7ff;z-index:2}
table{width:100%;border-collapse:collapse;background:#10182a}th,td{padding:9px 10px;border:1px solid #33415e;vertical-align:top;text-align:left}th{background:#1a2743;position:sticky;top:0;z-index:1}tbody tr:hover{background:#17233d}.table-wrap{overflow:auto;max-height:72vh;border:1px solid #33415e;border-radius:10px}.case-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:12px}.case-card{background:#111b31;border:1px solid #374867;border-radius:12px;padding:14px}.case-card img{width:100%;border-radius:8px;background:white;margin-top:8px}.report{background:white;color:#172033;padding:29px;border-radius:12px;box-shadow:var(--shadow)}.report h1,.report h2,.report h3{color:#111b2e}.report a{color:#174ea6}.report code,.report pre{background:#f1f4f9;color:#172033}.report table{background:white}.report th{background:#e8eef8;color:#172033;position:static}.report td,.report th{border-color:#b7c2d5}.report blockquote{border-left:4px solid #6688c5;margin-left:0;padding:8px 16px;background:#f2f6fc}
@media(max-width:1080px){.graph-shell{grid-template-columns:1fr;height:auto}#graphViewport{height:68vh}#detail{border-left:0;border-top:1px solid #33415d}.flow{grid-template-columns:1fr}.flow-step:not(:last-child)::after{content:"↓";right:auto;left:49%;top:auto;bottom:-24px}}
</style>
</head>
<body>
<header><div class="header-row"><div><h1>Canonical hexagon-cover proof graph</h1><div class="subtitle">The graph follows <code>arrange/paper_draft/main.tex</code>: exact body interfaces, solved optimization Appendices A--E, the exact mixed-overlap certificate in Appendix F, and final assembly. Click a node for its exact TeX statement and case scope.</div><div class="stats" id="stats"></div></div><div class="actions"><button class="btn" id="downloadJson">Download JSON</button><button class="btn" id="downloadReport">Download report</button><a class="btn" id="branchLink" target="_blank" rel="noreferrer">Open branch</a></div></div></header>
<div class="tabs"><button class="tab-btn active" data-tab="graph">Dependency graph</button><button class="tab-btn" data-tab="spine">Method 3 spine</button><button class="tab-btn" data-tab="routing">Routing R0-R13 (R6a/R6b)</button><button class="tab-btn" data-tab="cases">Finite register A--F</button><button class="tab-btn" data-tab="report">Implementation report</button><button class="tab-btn" data-tab="index">Statement index</button></div>
<section class="tab active" id="tab-graph"><div class="toolbar"><input id="search" placeholder="Search title, label, statement, or case..."><select id="groupFilter"><option value="">All architecture groups</option></select><select id="kindFilter"><option value="">All statement types</option><option>theorem</option><option>proposition</option><option>lemma</option><option>corollary</option></select><label class="chip"><input type="checkbox" id="caseOnly"> terminals/assemblies only</label><button class="btn" id="method3Only">Method 3 only</button><button class="btn" id="showAll">Show all</button><button class="btn" id="fit">Fit</button><button class="btn" id="clearFocus">Clear focus</button><div class="legend" id="legend"></div></div><div class="graph-shell"><div id="graphViewport"><svg id="graphSvg"></svg></div><aside id="detail"><div class="empty">Select a theorem, proposition, lemma, or corollary.</div></aside></div></section>
<section class="tab" id="tab-spine"><div class="content"><div class="card"><h2>Public Method 3 spine</h2><img class="spine-image" id="spineImage" alt="Method 3 dependency spine"><p>The body presents the exact mechanism and compact case terminals. Appendices D and E supply the nonzero-gap and zero-gap optimizations, and Appendix F supplies the exact mixed-overlap arithmetic.</p></div><div class="card"><div class="flow"><div class="flow-step"><b>1. Normalize</b><br><span class="small">N_gap, N_+, (d,t), actual reaches.</span></div><div class="flow-step"><b>2. Bound local capacity</b><br><span class="small">c_max, C_±, high-radial outputs.</span></div><div class="flow-step"><b>3. Force a witness</b><br><span class="small">Radial endpoints, exact gaps, or frontier points.</span></div><div class="flow-step"><b>4. Invoke one terminal</b><br><span class="small">Complementary gap, CE2 short ray, K_tr, supported tail, radial separation, or K_wit.</span></div><div class="flow-step"><b>5. Close the register</b><br><span class="small">Rows A--F or the replacement router, then R0-R13 with R6a/R6b.</span></div></div></div></div></section>
<section class="tab" id="tab-routing"><div class="content"><div class="card"><h2>Exhaustive routing ownership</h2><div class="table-wrap"><table id="routingTable"></table></div></div></div></section>
<section class="tab" id="tab-cases"><div class="content"><div class="card"><h2>Exact finite-enclosure register</h2><p>Cards A--F match the manuscript register; the replacement router is shown separately because it recomputes the output gap rank rather than adding a terminal row. Row F uses the restored original repository nine-point figure, not the trace-envelope screenshot with misleading fixed Q positions.</p><div class="case-grid" id="caseCards"></div></div></div></section>
<section class="tab" id="tab-report"><div class="content"><article class="report" id="reportBody"></article></div></section>
<section class="tab" id="tab-index"><div class="content"><div class="card"><h2>All formal statements</h2><input id="indexSearch" placeholder="Filter the statement index..." style="width:100%;margin-bottom:10px;background:#0d1426;color:white;border:1px solid #425273;border-radius:8px;padding:9px"><div class="table-wrap"><table id="indexTable"></table></div></div></div></section>
<script>
const DATA=__DATA__;
const nodeById=new Map(DATA.nodes.map(n=>[n.id,n]));
const reverse=new Map(DATA.nodes.map(n=>[n.id,[]]));for(const n of DATA.nodes)for(const d of n.deps)reverse.get(d)?.push(n.id);
const terminalRoles=new Set(["Case-closing terminal","Routing / assembly"]);let state={query:"",group:"",kind:"",caseOnly:false,method3Only:false,focus:null,selected:null};let view={x:30,y:28,scale:.68};
const svg=document.getElementById("graphSvg"),viewport=document.getElementById("graphViewport"),detail=document.getElementById("detail");
function esc(s){return String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
function svgEl(tag,attrs={}){const x=document.createElementNS("http://www.w3.org/2000/svg",tag);for(const[k,v]of Object.entries(attrs))x.setAttribute(k,v);return x;}
function download(name,text,type){const b=new Blob([text],{type}),a=document.createElement("a");a.href=URL.createObjectURL(b);a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}
document.getElementById("downloadJson").onclick=()=>download("canonical_proof_dependency_data.json",JSON.stringify({...DATA,reportHtml:undefined,reportMarkdown:undefined},null,2),"application/json");document.getElementById("downloadReport").onclick=()=>download("IMPLEMENTATION_REPORT.md",DATA.reportMarkdown,"text/markdown");document.getElementById("branchLink").href=`https://github.com/${DATA.meta.repository}/tree/${DATA.meta.branch}`;
document.getElementById("stats").innerHTML=[`${DATA.meta.nodeCount} formal statements`,`${DATA.meta.edgeCount} logical edges`,`${DATA.meta.activeSourceCount} active TeX sources`,`self-contained publication graph`].map(x=>`<span class="pill">${esc(x)}</span>`).join("");
for(const g of DATA.groups){const o=document.createElement("option");o.value=g;o.textContent=g;document.getElementById("groupFilter").append(o)}document.getElementById("legend").innerHTML=DATA.groups.map(g=>`<span><i class="swatch" style="background:${DATA.colors[g]}"></i>${esc(g)}</span>`).join("");
function match(n){const q=state.query.trim().toLowerCase();if(state.group&&n.group!==state.group)return false;if(state.kind&&n.kind!==state.kind)return false;if(state.caseOnly&&!terminalRoles.has(n.role))return false;if(state.method3Only&&!n.group.startsWith("Method 3")&&!n.group.startsWith("Appendix F"))return false;if(q&&!([n.id,n.title,n.statementTex,n.group,n.role,n.cases.join(" "),n.caseDetail].join(" ").toLowerCase().includes(q)))return false;return true}
function neighborhood(id){const k=new Set([id]),q=[id];while(q.length){const x=q.shift();for(const d of nodeById.get(x).deps)if(!k.has(d)){k.add(d);q.push(d)}}const q2=[id];while(q2.length){const x=q2.shift();for(const y of reverse.get(x)||[])if(!k.has(y)){k.add(y);q2.push(y)}}return k}
function wrap(s,max=27){const words=s.replace(/\\[A-Za-z]+/g,"").split(/\s+/),lines=[""];for(const w of words){const i=lines.length-1;if((lines[i]+" "+w).trim().length>max&&lines.length<2)lines.push(w);else lines[i]=(lines[i]+" "+w).trim()}return lines}
function edgeClass(target){if(nodeById.get(target).role==="Routing / assembly")return"routing";if(nodeById.get(target).role==="Exact certificate")return"certificate";return""}
function renderGraph(){const visible=DATA.nodes.filter(match),visibleSet=new Set(visible.map(n=>n.id)),groups=DATA.groups.filter(g=>visible.some(n=>n.group===g));const positions=new Map;let maxY=0;groups.forEach((g,gi)=>{const arr=visible.filter(n=>n.group===g).sort((a,b)=>a.sourceOrder-b.sourceOrder);arr.forEach((n,i)=>{const y=62+i*78;positions.set(n.id,{x:36+gi*275,y});maxY=Math.max(maxY,y+65)})});const W=Math.max(900,90+groups.length*275),H=Math.max(720,maxY+60);svg.replaceChildren();svg.setAttribute("viewBox",`0 0 ${W} ${H}`);const defs=svgEl("defs"),marker=svgEl("marker",{id:"arrow",viewBox:"0 0 10 10",refX:"9",refY:"5",markerWidth:"7",markerHeight:"7",orient:"auto-start-reverse"});marker.append(svgEl("path",{d:"M0 0 L10 5 L0 10 z",fill:"#7484a2"}));defs.append(marker);svg.append(defs);const scene=svgEl("g",{id:"scene"});svg.append(scene);groups.forEach((g,gi)=>{const x=18+gi*275;scene.append(svgEl("rect",{x,y:8,width:260,height:H-25,rx:12,class:"band"}));const t=svgEl("text",{x:x+12,y:30,class:"band-label"});t.textContent=g;scene.append(t)});const focus=state.focus?neighborhood(state.focus):null;for(const n of visible){const p2=positions.get(n.id);for(const d of n.deps){if(!visibleSet.has(d))continue;const p1=positions.get(d),x1=p1.x+225,y1=p1.y+29,x2=p2.x,y2=p2.y+29,mx=(x1+x2)/2;const path=svgEl("path",{d:`M${x1},${y1} C${mx},${y1} ${mx},${y2} ${x2},${y2}`,class:`edge ${edgeClass(n.id)}`,"marker-end":"url(#arrow)"});if(focus&&!(focus.has(d)&&focus.has(n.id)))path.classList.add("dim");scene.append(path)}}for(const n of visible){const p=positions.get(n.id),g=svgEl("g",{transform:`translate(${p.x},${p.y})`,class:`node ${terminalRoles.has(n.role)?"case":""}`});if(focus&&!focus.has(n.id))g.classList.add("dim");if(state.selected===n.id)g.classList.add("selected");g.append(svgEl("rect",{width:225,height:59,rx:9,fill:DATA.colors[n.group]}));const k=svgEl("text",{x:10,y:14,class:"kind"});k.textContent=n.kind+" · "+n.role;g.append(k);wrap(n.title).forEach((line,i)=>{const t=svgEl("text",{x:10,y:34+i*14,class:"title"});t.textContent=line;g.append(t)});if(terminalRoles.has(n.role))g.append(svgEl("circle",{cx:214,cy:11,r:4,class:"dot"}));g.onclick=e=>{e.stopPropagation();selectNode(n.id,true)};scene.append(g)}applyTransform()}
function applyTransform(){document.getElementById("scene")?.setAttribute("transform",`translate(${view.x} ${view.y}) scale(${view.scale})`)}function fit(){const vb=svg.viewBox.baseVal,r=viewport.getBoundingClientRect();view.scale=Math.min((r.width-35)/vb.width,(r.height-35)/vb.height);view.x=18;view.y=18;applyTransform()}
let dragging=false,last={x:0,y:0};svg.onpointerdown=e=>{if(e.target.closest?.(".node"))return;dragging=true;last={x:e.clientX,y:e.clientY};svg.setPointerCapture(e.pointerId)};svg.onpointermove=e=>{if(!dragging)return;view.x+=e.clientX-last.x;view.y+=e.clientY-last.y;last={x:e.clientX,y:e.clientY};applyTransform()};svg.onpointerup=()=>dragging=false;svg.addEventListener("wheel",e=>{e.preventDefault();const r=svg.getBoundingClientRect(),mx=e.clientX-r.left,my=e.clientY-r.top,old=view.scale,next=Math.max(.12,Math.min(2.8,old*(e.deltaY<0?1.12:.89)));view.x=mx-(mx-view.x)*(next/old);view.y=my-(my-view.y)*(next/old);view.scale=next;applyTransform()},{passive:false});
function nodeButtons(ids){return ids.length?`<div class="link-list">${ids.map(id=>{const n=nodeById.get(id);return`<button class="node-link" data-node="${esc(id)}"><b>${esc(n.title)}</b><br><span class="small">${esc(id)}</span></button>`}).join("")}</div>`:`<div class="small">None.</div>`}
function figures(keys){return keys.length?`<div class="gallery">${keys.map(k=>{const f=DATA.figures[k];return`<figure class="figure"><a href="${f.url}" target="_blank" rel="noreferrer"><img src="${f.src}" alt="${esc(f.caption)}"></a><figcaption>${esc(f.caption)}</figcaption></figure>`}).join("")}</div>`:""}
function selectNode(id,focusIt=false){const n=nodeById.get(id);if(!n)return;state.selected=id;if(focusIt)state.focus=id;detail.innerHTML=`<div class="chips"><span class="chip">${esc(n.kind)}</span><span class="chip">${esc(n.group)}</span><span class="chip">${esc(n.role)}</span></div><h2 class="detail-title">${esc(n.title)}</h2><div class="label">${esc(n.id)}${n.aliases.length?" · aliases: "+esc(n.aliases.join(", ")):""}</div><div class="detail-section"><h3>Case scope</h3><div class="chips">${n.cases.map(x=>`<span class="chip">${esc(x)}</span>`).join("")}</div><p>${esc(n.caseDetail)}</p></div><div class="detail-section"><h3>Exact TeX statement</h3><pre class="statement" id="statement"></pre></div>${n.figureKeys.length?`<div class="detail-section"><h3>Relevant figure(s)</h3>${figures(n.figureKeys)}</div>`:""}<div class="detail-section"><h3>Uses</h3>${nodeButtons(n.deps)}</div><div class="detail-section"><h3>Used by</h3>${nodeButtons(n.usedBy)}</div><div class="detail-section"><h3>Active manuscript source</h3><div class="link-list">${n.sourceLinks.map(x=>`<a href="${x.url}" target="_blank" rel="noreferrer">${esc(x.name)}</a>`).join("")}</div></div><div class="detail-section"><h3>Numbered proof authority</h3>${n.proofRefs.length?`<div class="link-list">${n.proofRefs.map(x=>`<a href="${x.url}" target="_blank" rel="noreferrer">${esc(x.name)}</a>`).join("")}</div>`:`<div class="small">Consult the canonical paper and numbered proof sources for this theorem family.</div>`}</div><button class="btn" id="focusThis">Focus complete ancestry and descendants</button>`;document.getElementById("statement").textContent=n.statementTex;detail.querySelectorAll("[data-node]").forEach(b=>b.onclick=()=>openNode(b.dataset.node));document.getElementById("focusThis").onclick=()=>{state.focus=id;renderGraph()};renderGraph()}
function openNode(id){document.querySelector('[data-tab="graph"]').click();state={query:"",group:"",kind:"",caseOnly:false,method3Only:false,focus:id,selected:id};document.getElementById("search").value="";document.getElementById("groupFilter").value="";document.getElementById("kindFilter").value="";document.getElementById("caseOnly").checked=false;renderGraph();selectNode(id,true);setTimeout(fit,25)}document.body.addEventListener("click",e=>{const b=e.target.closest("[data-node]");if(b?.dataset.node)openNode(b.dataset.node)});
document.getElementById("search").oninput=e=>{state.query=e.target.value;state.focus=null;renderGraph()};document.getElementById("groupFilter").onchange=e=>{state.group=e.target.value;state.focus=null;renderGraph()};document.getElementById("kindFilter").onchange=e=>{state.kind=e.target.value;state.focus=null;renderGraph()};document.getElementById("caseOnly").onchange=e=>{state.caseOnly=e.target.checked;state.focus=null;renderGraph()};document.getElementById("method3Only").onclick=()=>{state.method3Only=true;state.group="";document.getElementById("groupFilter").value="";renderGraph()};document.getElementById("showAll").onclick=()=>{state={query:"",group:"",kind:"",caseOnly:false,method3Only:false,focus:null,selected:null};document.getElementById("search").value="";document.getElementById("groupFilter").value="";document.getElementById("kindFilter").value="";document.getElementById("caseOnly").checked=false;renderGraph();setTimeout(fit,20)};document.getElementById("fit").onclick=fit;document.getElementById("clearFocus").onclick=()=>{state.focus=null;renderGraph()};
document.querySelectorAll(".tab-btn").forEach(btn=>btn.onclick=()=>{document.querySelectorAll(".tab-btn").forEach(x=>x.classList.toggle("active",x===btn));document.querySelectorAll(".tab").forEach(x=>x.classList.toggle("active",x.id===`tab-${btn.dataset.tab}`));if(btn.dataset.tab==="graph")setTimeout(()=>{renderGraph();fit()},20)});
const spine=DATA.figures.method3_spine;if(spine)document.getElementById("spineImage").src=spine.src;
function closers(ids){return ids.map(id=>`<button class="node-link" data-node="${id}">${esc(nodeById.get(id).title)}</button>`).join("")}
document.getElementById("routingTable").innerHTML=`<thead><tr><th>ID</th><th>N_gap</th><th>N_+</th><th>V-type refinement</th><th>C type</th><th>Closer(s)</th><th>Mechanism</th></tr></thead><tbody>${DATA.routingRows.map(r=>`<tr><td>${r.id}</td><td>${esc(r.gap)}</td><td>${esc(r.nplus)}</td><td>${esc(r.types)}</td><td>${esc(r.center)}</td><td>${closers(r.closers)}</td><td>${esc(r.reason)}</td></tr>`).join("")}</tbody>`;
document.getElementById("caseCards").innerHTML=DATA.finiteRows.map(r=>`<article class="case-card"><span class="chip">${r.id}</span><h3>${esc(r.case)}</h3><p><b>Forced object:</b> ${esc(r.forced)}</p><p><b>Terminal:</b> <button class="node-link" data-node="${r.closer}">${esc(nodeById.get(r.closer).title)}</button></p>${figures(r.figures)}</article>`).join("");document.getElementById("reportBody").innerHTML=DATA.reportHtml;
function renderIndex(){const q=document.getElementById("indexSearch").value.trim().toLowerCase(),rows=DATA.nodes.filter(n=>!q||[n.id,n.title,n.group,n.cases.join(" ")].join(" ").toLowerCase().includes(q));document.getElementById("indexTable").innerHTML=`<thead><tr><th>#</th><th>Type</th><th>Statement</th><th>Architecture group</th><th>Case scope</th><th>Uses</th></tr></thead><tbody>${rows.map((n,i)=>`<tr><td>${i+1}</td><td>${esc(n.kind)}</td><td><button class="node-link" data-node="${n.id}"><b>${esc(n.title)}</b><br><span class="small">${esc(n.id)}</span></button></td><td>${esc(n.group)}</td><td>${esc(n.cases.join("; "))}</td><td>${n.deps.length}</td></tr>`).join("")}</tbody>`}document.getElementById("indexSearch").oninput=renderIndex;renderIndex();renderGraph();setTimeout(fit,60);
</script></body></html>'''


def render() -> tuple[str, str]:
    data = build_data()
    json_text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    embedded = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html_text = HTML_TEMPLATE.replace("__DATA__", embedded)
    return html_text, json_text


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    html_text, json_text = render()
    if args.check:
        stale: list[str] = []
        if not OUT_HTML.is_file() or OUT_HTML.read_text(encoding="utf-8") != html_text:
            stale.append(rel(OUT_HTML))
        if not OUT_JSON.is_file() or OUT_JSON.read_text(encoding="utf-8") != json_text:
            stale.append(rel(OUT_JSON))
        if stale:
            raise SystemExit("canonical dependency artifacts are stale: " + ", ".join(stale))
        return
    OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
    OUT_HTML.write_text(html_text, encoding="utf-8")
    OUT_JSON.write_text(json_text, encoding="utf-8")
    print(f"wrote {rel(OUT_HTML)}")
    print(f"wrote {rel(OUT_JSON)}")


if __name__ == "__main__":
    main()
