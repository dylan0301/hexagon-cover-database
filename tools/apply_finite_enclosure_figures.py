#!/usr/bin/env python3
"""Apply the reviewer-approved finite-enclosure figure revision.

The script is deliberately surgical and idempotent.  It only inserts figure
inputs next to named statements, removes the superseded schematic floats, and
moves the complete sampled atlas from the canonical proof body to an appendix.
It does not alter theorem statements or proof text.
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def insert_after_statement(rel: str, label: str, input_rel: str) -> None:
    text = read(rel)
    snippet = f"\\input{{{input_rel}}}"
    if snippet in text:
        return

    marker = f"\\label{{{label}}}"
    label_pos = text.find(marker)
    if label_pos < 0:
        raise RuntimeError(f"label not found in {rel}: {label}")

    candidates: list[tuple[int, str]] = []
    for env in ("lemma", "theorem", "proposition", "corollary", "definition"):
        pos = text.rfind(f"\\begin{{{env}}}", 0, label_pos)
        if pos >= 0:
            candidates.append((pos, env))
    if not candidates:
        raise RuntimeError(f"statement start not found before {label} in {rel}")

    begin_pos, env = max(candidates)
    end_marker = f"\\end{{{env}}}"
    end_pos = text.find(end_marker, label_pos)
    if end_pos < 0:
        raise RuntimeError(f"statement end not found for {label} in {rel}")
    end_pos += len(end_marker)

    # The nearest begin environment must enclose the requested label.
    if begin_pos > label_pos:
        raise RuntimeError(f"malformed statement around {label} in {rel}")

    text = text[:end_pos] + "\n\n" + snippet + text[end_pos:]
    write(rel, text)


def insert_before(rel: str, anchor: str, snippet: str) -> None:
    text = read(rel)
    if snippet in text:
        return
    pos = text.find(anchor)
    if pos < 0:
        raise RuntimeError(f"anchor not found in {rel}: {anchor[:80]!r}")
    text = text[:pos] + snippet + "\n\n" + text[pos:]
    write(rel, text)


def replace_once(rel: str, old: str, new: str) -> None:
    text = read(rel)
    if new in text and old not in text:
        return
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"expected one occurrence in {rel}, found {count}: {old[:80]!r}")
    write(rel, text.replace(old, new, 1))


def remove_figure_by_label(rel: str, label: str) -> None:
    text = read(rel)
    marker = f"\\label{{{label}}}"
    pos = text.find(marker)
    if pos < 0:
        return
    start = text.rfind("\\begin{figure", 0, pos)
    end = text.find("\\end{figure}", pos)
    if start < 0 or end < 0:
        raise RuntimeError(f"figure bounds not found for {label} in {rel}")
    end += len("\\end{figure}")
    while start > 0 and text[start - 1] == "\n":
        start -= 1
    while end < len(text) and text[end] == "\n":
        end += 1
    write(rel, text[:start] + "\n\n" + text[end:])


def ensure_atlas_appendix() -> None:
    wrapper = r"""\section{Complete Trace-Exact Geometric Atlas}
\label{sec:trace-exact-geometric-atlas}

This appendix collects the complete sampled atlas for the finite-enclosure
case table.  Each shaded region is a dense numerical guide to a
source-conditioned trace-exact envelope; it is not used as a proof object.
The exact objects are the source-family unions defined in
Subsection~\ref{subsec:trace-exact-ab-envelopes}, and the proofs use only the
set inclusions and endpoint identities stated there.

\input{06i_trace_exact_ab_atlas}
"""
    write("arrange/paper_draft/06h_trace_exact_ab_atlas_appendix.tex", wrapper)

    main = "arrange/paper_draft/main.tex"
    text = read(main)
    line = "\\input{06h_trace_exact_ab_atlas_appendix}"
    if line not in text:
        old = "\\input{06a_strategy4_exact_certificate}\n"
        if old not in text:
            raise RuntimeError("canonical appendix insertion point not found")
        text = text.replace(old, old + line + "\n", 1)
        write(main, text)


def patch_canonical_paper() -> None:
    chapter = "arrange/paper_draft/06_finite_enclosure_full.tex"

    old = "\\end{longtable}\n\\endgroup\n\n\n\\subsection{Trace-exact AB envelopes at an actual gap}"
    new = (
        "\\end{longtable}\n\\endgroup\n\n"
        "\\input{figures/finite_enclosure/fe00_case_roadmap}\n\n"
        "\\subsection{Trace-exact AB envelopes at an actual gap}"
    )
    replace_once(chapter, old, new)

    text = read(chapter)
    atlas_line = "\\input{06i_trace_exact_ab_atlas}\n\n"
    if atlas_line in text:
        text = text.replace(atlas_line, "", 1)
        write(chapter, text)

    insert_before(
        chapter,
        "\\input{06_direct_local_calculus}",
        "\\input{figures/finite_enclosure/fe01_trace_and_gauge}",
    )

    remove_figure_by_label(chapter, "fig:new-one-gap-radial-witness")
    remove_figure_by_label(chapter, "fig:new-two-gap-short-ray")
    remove_figure_by_label(chapter, "fig:new-anisotropic-witness")

    insert_after_statement(
        chapter,
        "lem:new-disk-point-formula",
        "figures/finite_enclosure/fe02_disk_plus_point",
    )
    insert_after_statement(
        chapter,
        "thm:new-complementary-gap",
        "figures/finite_enclosure/fe03_complementary_gap",
    )
    insert_after_statement(
        chapter,
        "thm:new-ce2-short-ray",
        "figures/finite_enclosure/fe04_ce2_short_ray",
    )
    insert_after_statement(
        chapter,
        "prop:new-nplus-one-all-vd0",
        "figures/finite_enclosure/fe05_k410_actual_reach",
    )

    insert_after_statement(
        "arrange/paper_draft/06a_neighbor_ray_calculus.tex",
        "prop:new-neighbor-ray-formula",
        "figures/finite_enclosure/fe06_neighbor_capacity",
    )
    insert_after_statement(
        "arrange/paper_draft/06b_ce1_direct_certificate.tex",
        "prop:new-ce1-direct-certificate",
        "figures/finite_enclosure/fe07_ce1_reverse_path",
    )
    insert_after_statement(
        "arrange/paper_draft/06c_exceptional_direct_terminals.tex",
        "prop:new-one-t3-terminal",
        "figures/finite_enclosure/fe08_t3_rescuer",
    )
    insert_after_statement(
        "arrange/paper_draft/06c_exceptional_direct_terminals.tex",
        "prop:new-one-vd-assembly",
        "figures/finite_enclosure/fe09_vd_placements",
    )
    insert_after_statement(
        "arrange/paper_draft/06_strategy4_ab_core.tex",
        "thm:strict-ab-union",
        "figures/finite_enclosure/fe10_ab_frontier",
    )
    insert_before(
        "arrange/paper_draft/06_strategy4_ab_core.tex",
        "\\subsection{Tangent reduction and exact mixed overlaps}",
        "\\input{figures/finite_enclosure/fe11_zero_gap_witness}",
    )
    insert_after_statement(
        "arrange/paper_draft/06_strategy4_completion.tex",
        "lem:reader-cap-chain",
        "figures/finite_enclosure/fe12_support_caps",
    )

    ensure_atlas_appendix()


def patch_readable_paper() -> None:
    toolkit = "arrange/readable_paper/05d_toolkit.tex"
    terminals = "arrange/readable_paper/05e_universal_terminals.tex"
    cases = "arrange/readable_paper/05g_nonzero_gap_cases.tex"

    insert_after_statement(
        toolkit,
        "prop:readable-trace-exact-ab-interface",
        "figures/finite_enclosure/fe01_trace_and_gauge",
    )
    insert_after_statement(
        "arrange/readable_paper/05b_neighbor_ray_calculus.tex",
        "prop:new-neighbor-ray-formula",
        "figures/finite_enclosure/fe06_neighbor_capacity",
    )

    remove_figure_by_label(terminals, "fig:new-one-gap-radial-witness")
    remove_figure_by_label(terminals, "fig:new-two-gap-short-ray")
    insert_after_statement(
        terminals,
        "lem:new-disk-point-formula",
        "figures/finite_enclosure/fe02_disk_plus_point",
    )
    insert_after_statement(
        terminals,
        "thm:new-complementary-gap",
        "figures/finite_enclosure/fe03_complementary_gap",
    )
    insert_after_statement(
        terminals,
        "thm:new-ce2-short-ray",
        "figures/finite_enclosure/fe04_ce2_short_ray",
    )

    remove_figure_by_label(cases, "fig:readable-anisotropic-witness")
    remove_figure_by_label(cases, "fig:readable-t3-cases")
    remove_figure_by_label(cases, "fig:readable-one-vd-cases")
    insert_after_statement(
        cases,
        "lem:readable-k410-forced",
        "figures/finite_enclosure/fe05_k410_actual_reach",
    )
    insert_after_statement(
        cases,
        "prop:readable-k410-ce1",
        "figures/finite_enclosure/fe07_ce1_reverse_path",
    )
    insert_after_statement(
        cases,
        "lem:readable-t3-o-side-endpoint",
        "figures/finite_enclosure/fe08_t3_rescuer",
    )
    insert_before(
        cases,
        "\\begin{corollary}[Direct one-Vd placement assembly]",
        "\\input{figures/finite_enclosure/fe09_vd_placements}",
    )

    insert_after_statement(
        "arrange/readable_paper/06a_zero_gap_nine_point_core.tex",
        "thm:strict-ab-union",
        "figures/finite_enclosure/fe10_ab_frontier",
    )
    insert_before(
        "arrange/readable_paper/06a_zero_gap_nine_point_core.tex",
        "\\subsection{Tangent reduction and exact mixed overlaps}",
        "\\input{figures/finite_enclosure/fe11_zero_gap_witness}",
    )
    insert_after_statement(
        "arrange/readable_paper/06b_zero_gap_nine_point_completion.tex",
        "lem:reader-cap-chain",
        "figures/finite_enclosure/fe12_support_caps",
    )


def main() -> None:
    patch_canonical_paper()
    patch_readable_paper()

    # A targeted audit: every requested figure must be referenced by at least
    # one paper source, and the obsolete three canonical floats must be gone.
    required = [
        f"figures/finite_enclosure/fe{i:02d}_"
        for i in range(13)
    ]
    corpus = "\n".join(
        p.read_text(encoding="utf-8")
        for base in (ROOT / "arrange/paper_draft", ROOT / "arrange/readable_paper")
        for p in base.glob("*.tex")
    )
    missing = [prefix for prefix in required if prefix not in corpus]
    if missing:
        raise RuntimeError(f"unreferenced figure prefixes: {missing}")

    for rel, label in (
        ("arrange/paper_draft/06_finite_enclosure_full.tex", "fig:new-one-gap-radial-witness"),
        ("arrange/paper_draft/06_finite_enclosure_full.tex", "fig:new-two-gap-short-ray"),
        ("arrange/paper_draft/06_finite_enclosure_full.tex", "fig:new-anisotropic-witness"),
    ):
        if f"\\label{{{label}}}" in read(rel):
            raise RuntimeError(f"obsolete figure label remains: {label}")

    print("Applied finite-enclosure figure revision.")


if __name__ == "__main__":
    main()
