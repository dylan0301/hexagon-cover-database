# AMS-Style Self-Contained Paper Guide

This file specifies the active manuscript architecture. Numbered proof sources
remain authoritative for theorem status and hypotheses. The paper may
reorganize proved material, but it may not strengthen a claim, remove a
strictness condition, infer actual criticality from selected lower bounds, or
replace an exact certificate by numerical evidence.

## 1. Publication objective

The target is a self-contained paper of approximately ninety pages. The page
target is achieved by removing duplicated reader/appendix layers, not by
removing mathematical content. Every geometric reduction, case split, local
lemma, and exact certificate needed by the final theorem remains in the
published PDF.

The paper is strategy-oriented even though the numbered proof corpus remains
branch-oriented. `arrange/paper_proof_crosswalk.md` records the correspondence.

## 2. Active printed architecture

The manuscript uses the following top-level sections:

```text
01_introduction.tex
02_structure_and_common_geometry.tex
03_trace_bounds.tex
05_area_loss_full.tex
06_finite_enclosure_full.tex
07_exhaustive_assembly.tex
```

Their functions are:

1. theorem, canonical labeling, finite classifications, and routing table;
2. complete structural reduction and signed center geometry;
3. Strategy 1: complete trace-length proof;
4. Strategy 2: complete area-loss proof;
5. Strategy 3: residual-hull finite enclosure, exact local reach certificates,
   and the explicit nine-point theorem;
6. one final exhaustive assembly.

After the body-end label, the sole printed appendix is:

```text
06a_strategy4_exact_certificate.tex
```

It contains the exact unequal-radius support-arc certificate. Long local-reach certificate algebra is retained inside Strategy 3 so that each finite witness theorem and its exact noncontainment calculation remain together.

## 3. Source incorporation

The wrapper files temporarily demote sectioning commands while incorporating
established self-contained TeX modules. This changes presentation only;
labels, theorem statements, equations, and proof content are retained.

The active assembly is:

```latex
\input{01_introduction}
\input{02_structure_and_common_geometry}
\input{03_trace_bounds}
\input{05_area_loss_full}
\input{06_finite_enclosure_full}
\input{07_exhaustive_assembly}
\label{page:proof-body-end}

\clearpage
\appendix
\input{06a_strategy4_exact_certificate}
```

The exact legacy reach-certificate provenance manifest remains repository metadata and is
not typeset. Formalization-only optimization specifications and the Lean
statement-elaboration project remain repository verification objects; the
paper does not present them as a manuscript appendix or duplicate their
interface prose.

## 4. Content placement rule

Keep in the main mathematical narrative:

- open/closed/scaled equivalence;
- center and vertex classifications;
- maximal reaches, selected lower bounds, gaps, and handoffs;
- midpoint statements and signed center geometry;
- every local geometric reduction;
- all trace and area proofs;
- the admissible set and exact local reach calculus;
- all T3-like and Vd placement arguments;
- the two-chart replacement;
- nine-point forcing, Newton reduction, ray order, and support-arc argument;
- the final exhaustive case assembly.

Keep in the exact appendix:

- authenticated sparse polynomial data;
- rational-envelope and Gram reductions for the two mixed overlaps;
- denominator checks;
- exact Bernstein conversion and positivity conclusion.

Keep in repository navigation and verification files rather than the printed
article:

- Git blob tables and maintenance provenance prose;
- formalization registries and source-owner tables;
- run logs and release instructions;
- historical or failed approaches.

## 5. Paper-wide notation

Use the paper terminology:

- C triangle and V triangle;
- maximal reaches `(A_i,B_i,C_i)`;
- selected lower bounds `(a_i,b_i,c_i)`;
- `N_+` defined only from `A_i+B_i>1`;
- boundary gap, including singleton gaps;
- `N_gap` for the number of positive center traces containing a gap;
- CE0, CE1, CE2 and Vd0, Vd1, Vd2, T3-like.

The reader-facing transfer is branchwise. For a nonsupercritical triangle use
`B<=1-A` directly at radial lower bound at most `1/2`, and use the raw
high-radial admissible-set map above `1/2`. The raw zero-radial map is never
used as an identity handoff.

Provenance-bound legacy aliases may remain in the authenticated 407X files and
must be translated by the repository crosswalk. The printed paper uses only
`M`, `\overline M`, `\Phi`, and `M^{\rm sup}`; do not introduce a second
transfer family.

## 6. Non-negotiable distinctions

Every revision must preserve:

1. actual versus selected criticality;
2. open traces and singleton gaps;
3. CE1 point contact versus CE2 positive companion trace;
4. center-free hypotheses for propagated handoffs and path budgets;
5. endpoint external components in residuals;
6. connected-component selectors after squaring;
7. all branch-boundary equality assignments;
8. the inclusive CE2 threshold alternative;
9. the complete T3-like four-branch analysis;
10. adjacent and nonadjacent Vd-specific radial margins;
11. both charts and all strict margins in the Vd1 replacement;
12. the exact Strategy 4 arithmetic model and authenticated input.

## 7. Build and direct-main workflow

A source commit to `main` triggers
`.github/workflows/paper-rebuild.yml`. The workflow:

1. runs the proof-source, manuscript, and legacy reach-certificate semantic-interface checks;
2. elaborates the pinned Lean scalar-statement project;
3. replays the exact Strategy 4 certificate;
4. performs two clean builds with the pinned TeX Live 2025 image;
5. rejects undefined or duplicate references and overfull boxes;
6. compares the two PDFs by stable semantics and exact rendered pixels;
7. verifies rendering and an 84--104 page target interval;
8. regenerates `arrange/CURRENT_VERIFICATION_SUMMARY.txt`;
9. commits the canonical PDF and summary directly to `main`.

The write-enabled workflow runs the active proof-reference graph, legacy reach-certificate specifications,
exact certificates, Lean scalar-statement elaboration, and a two-build
semantic PDF audit before committing. GitHub does not recursively trigger the
ordinary read-only push workflow from the workflow-token commit; that
independent verifier runs on user pushes and pull requests and also builds the
archival bundle.

A manual dispatch may target a review branch; the workflow verifies that the
remote branch has not advanced and commits the pinned PDF and summary back to
that same branch. It then explicitly dispatches the read-only workflow on the
artifact commit; it does not rely on the workflow-token push to trigger it.

For local compilation:

```bash
cd arrange/paper_draft
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

Do not manually update the tracked PDF without also regenerating the current
verification summary.
