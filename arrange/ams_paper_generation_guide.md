# AMS-Style Main-Theorem Paper Generation Guide

This file is an authoring specification for an LLM. It is not a proof source.
Its purpose is to generate a self-contained, rigorous AMS-style paper proving
the main theorem recorded in
[`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md).

The generated paper must be organized by four proof strategies rather than by
the repository's CE-first folder tree:

1. direct length-sum obstructions;
2. exact boundary--radial demand propagation;
3. area loss;
4. the center-independent direct nine-point obstruction.

The repository remains the authoritative source for mathematical content and
proof status. The generated paper must reorganize that content without
strengthening any statement, dropping any hypothesis, or treating navigation
files as proofs.

## 1. Nonnegotiable Source And Status Rules

Before writing, read completely:

- [`README.md`](../README.md);
- [`0000_main_theorem.md`](../proof/0XXX_main/0000_main_theorem.md);
- [`0001_proof_tree_index.md`](../proof/0XXX_main/0001_proof_tree_index.md);
- [`0002_status_and_dependencies.md`](../proof/0XXX_main/0002_status_and_dependencies.md);
- [`0910_notation_dictionary.md`](../proof/09XX_appendices/0910_notation_dictionary.md);
- [`1006_proof_status_conventions.md`](../proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md).

Apply these rules throughout generation:

1. Use a mathematical result as established only when its source says
   `Status: Proven` or when it is an exact definition from a source saying
   `Status: Definition`.
2. A `Reference` or index file supplies navigation only. Follow its links to
   the proved sources and read those sources before writing the corresponding
   proof.
3. A `Reduction` proves only its reduction. It cannot close a branch unless
   every terminal dependency is independently `Proven`.
4. Never promote `Practically proven`, `Lemma target`, `Strategy`,
   `Empirical`, `Experiment`, or `Failed` material into the proof.
5. Exact finite certificates and exact positive-basis identities must be
   presented as independently checkable arguments. A plot, floating-point
   run, or script invocation by itself is not a proof.
6. Repository identifiers and paths are provenance for the authoring process.
   The reader-facing paper must contain mathematical theorem names, statements,
   proofs, and ordinary cross-references rather than appeals to files such as
   “`4013`” or “the database.”
7. Preserve all hypotheses involving open versus closed triangles,
   distinguished points in interiors, strict inequalities, positive-length
   traces, midpoint coverage, CE type, vertex type, and $N_+$.

Maintain the private source ledger in
`arrange/paper_draft/source_ledger.md`. For every theorem, lemma, or
certificate in the paper, record its authoritative path, recorded status, and
the manuscript label where it is proved. The ledger does not replace proofs in
the paper.

## 2. Required Paper Deliverable

Generate one modular, compilable AMS-LaTeX manuscript. Every persistent
manuscript artifact must remain under the existing workspace
`arrange/paper_draft/`. Do not create or modify paper-generation artifacts in
`proof/`, at the repository root, or in any other proof package.

Use this required baseline source layout:

```text
arrange/paper_draft/
|-- main.tex
|-- 01_introduction.tex
|-- 02_structural_reductions.tex
|-- 03_strategy1_length.tex
|-- 04_strategy2_exact_demand.tex
|-- 05_strategy3_area.tex
|-- 06_strategy4_ab_core.tex
|-- 07_exhaustive_assembly.tex
|-- appendix_exact_formulas.tex
|-- appendix_certificates.tex
|-- appendix_exact_mixed_overlap.tex
|-- source_ledger.md
|-- fonts/
|   |-- README.md
|   |-- OFL.txt
|   |-- noto_sans_kr_subset_115.ttf
|   `-- noto_sans_kr_subset_118.ttf
|-- main.pdf
|-- references.bib                 # only when verified sources are cited
`-- figures/
```

If another persistent source or build-support file becomes necessary, place it
under `arrange/paper_draft/` and record its role in `source_ledger.md`. Visual
assets and their generation sources have the stricter location rule in
Section 13.

The preamble in `main.tex` must begin with the following minimum structure:

```latex
\documentclass{amsart}
\usepackage{amsmath,amssymb,amsthm,mathtools,graphicx}
\usepackage{fontspec}

\newfontfamily\hangulA[Path=fonts/]{noto_sans_kr_subset_115.ttf}
\newfontfamily\hangulB[Path=fonts/]{noto_sans_kr_subset_118.ttf}
\newcommand{\straddlinghangul}{{\hangulA 걸}{\hangulB 거치는}}

\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
```

`main.tex` owns the title metadata, abstract, document environment, component
assembly, optional bibliography, and `\end{document}`. The numbered component
files begin with their own `\section` command and contain no document preamble.
Use this assembly order:

```latex
\begin{document}
\begin{abstract}
% Exact theorem statement and proof-method summary.
\end{abstract}
\maketitle
\input{01_introduction}
\input{02_structural_reductions}
\input{03_strategy1_length}
\input{04_strategy2_exact_demand}
\input{05_strategy3_area}
\input{06_strategy4_ab_core}
\input{07_exhaustive_assembly}
\appendix
\input{appendix_exact_formulas}
\input{appendix_certificates}
\input{appendix_exact_mixed_overlap}
% Add \bibliographystyle{amsplain} and \bibliography{references} only if used.
\end{document}
```

Do not add an input for the deleted
`06_strategy4_nonbranching_completion.tex`; its exact material belongs in
`appendix_exact_mixed_overlap.tex`.

Add `\bibliography{references}` only when `references.bib` contains verified
external sources that are actually cited. Compile from
`arrange/paper_draft/` with XeLaTeX so `fontspec` can load the local Hangul
subsets. The tracked `main.pdf`, logs, and auxiliary files must remain inside
that workspace. Regenerate `main.pdf` after every accepted source change; a
stale PDF is not an acceptable deliverable. No `\input`, bibliography, font,
or graphics path may escape the workspace.

The manuscript must contain, in this order:

1. title, author placeholder, abstract, and keywords;
2. introduction and precise main theorem;
3. geometric setup and exhaustive structural reductions;
4. one major section for each of the four strategies in the order specified
   here;
5. an exhaustive final assembly;
6. technical appendices for long exact formulas and certificates;
7. a bibliography only when genuine, verified external references are actually
   cited.

Do not invent historical claims or bibliography entries. If external
literature has not been supplied or independently verified, omit the
bibliography from the delivered manuscript and record the missing literature
review only in the private drafting ledger.

Use `\label`, `\ref`, and `\eqref` consistently. Recommended label prefixes
are `sec:`, `thm:`, `lem:`, `prop:`, `cor:`, `def:`, `eq:`, and `app:`. Every
result used later must be stated before use or cited by a precise backward
cross-reference. Avoid duplicated proofs: prove a specialized lemma in the
strategy section that owns it, then cite it later.

The final paper must be self-contained at the level expected of a research
article. It may move lengthy algebra and certified finite checks to appendices,
but the body must state their exact inputs, outputs, hypotheses, and logical
role.

## 3. Staged Generation Workflow

Do not attempt the full manuscript in one pass. Use the following sequence.

### Stage 0: dependency and notation audit

1. Work from `arrange/paper_draft/` and use the fixed source layout from
   Section 2, omitting only the conditional bibliography when it is unused.
2. Initialize `source_ledger.md` and record every persistent file in the
   workspace, including the exact mixed-overlap appendix, embedded fonts,
   their license and provenance, and the tracked `main.pdf`.
3. Read every shared source in Section 5 below.
4. Read every source assigned to the strategy currently being drafted.
5. Confirm the recorded status in the source itself, not merely in an index.
6. Build a list of theorem statements, dependencies, normalization choices,
   and strictness conditions.
7. Fix one paper-wide notation convention before drafting prose.

Use uppercase $(A_i,B_i,C_i)$ for actual maximal reaches whenever actual
reaches and smaller selected demands occur together. Reserve lowercase
$(a_i,b_i,c_i)$ for selected or prescribed lower-bound demands. If a local
section uses lowercase letters for actual reaches, explicitly announce that
temporary convention and do not mix the two meanings.

### Stage 1: shared setup

Draft the introduction in `01_introduction.tex`. Draft the geometric model,
open/closed/scaled equivalence, role assignment, exhaustive classifications,
$N_+$ definition, and strict-handoff machinery in
`02_structural_reductions.tex`. Audit that the resulting case split is
exhaustive before drafting any strategy section.

### Stages 2--5: the four strategy sections

Write the strategies into these files, in order:

1. Strategy 1 in `03_strategy1_length.tex`;
2. Strategy 2 in `04_strategy2_exact_demand.tex`;
3. Strategy 3 in `05_strategy3_area.tex`;
4. Strategy 4 in `06_strategy4_ab_core.tex`.

For each strategy file:

1. prove its chapter-local reusable lemmas;
2. state and prove its terminal branch theorems;
3. record exactly which rows of the final routing table it closes;
4. check that all strict inequalities survive passage between open roles,
   their closures, actual reaches, and selected demands;
5. stop and repair any unresolved dependency before moving to the next
   strategy.

### Stage 6: final assembly

Write the main proof in `07_exhaustive_assembly.tex` from the routing table in
Section 10. The assembly must show explicitly that every CE class, every
$N_+$ range, and every exhaustive vertex-type refinement has been handled. Do
not replace this audit by the sentence “all remaining cases are similar.”

### Stage 7: certificates and final audit

Place long exact tables and formulas in `appendix_exact_formulas.tex`. Place
the finite caliper theorem and its reproduction details in
`appendix_certificates.tex`. Put the active rational-envelope and global
Bernstein mixed-overlap proof in `appendix_exact_mixed_overlap.tex`. Assemble
every component through `main.tex`, run the checks in Section 15, and compile
from `arrange/paper_draft/` with
`latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`. Inspect
every warning, undefined reference, missing citation, missing font, and
missing asset, and regenerate the tracked `main.pdf`. Only then produce the
final paper.

## 4. Reader-Facing Paper Architecture

Use the following major sections. In an `amsart` paper these are `\section`
units, even though this guide informally calls them chapters.

1. **Introduction and main result.** State the open-unit theorem, the expanded
   closed formulation, the four proof mechanisms, and the proof roadmap.
2. **Geometric setup and structural reductions.** Establish the common
   definitions, role assignment, classifications, rows, gaps, and handoffs.
3. **Strategy 1: Direct length-sum obstructions.** Develop coarse
   one-dimensional trace budgets on the boundary, diagonals, and conditional
   skeleton targets.
4. **Strategy 2: Exact boundary--radial demand propagation.** Develop the exact
   CE1/CE2 trace formulas, local maps, gap propagation, and exact placement
   arguments.
5. **Strategy 3: Area loss.** Develop the local loss inequalities and global
   six-row area certificates for CE0.
6. **Strategy 4: Center-independent direct nine-point obstruction.** Treat
   the unified $N_+=1$, all-Vd0, zero-boundary-gap branch by forcing six
   radial and three asymmetric witnesses into the center role, without
   splitting first by center class.
7. **Exhaustive assembly.** Route every terminal case and conclude the main
   theorem.

Appendices should contain the long piecewise formulas, exhaustive finite label
tables, exact finite certificates, global positive-basis identities,
reproduction details, and coordinate proofs that remain logical dependencies
and whose length would obscure the main argument. Do not reproduce a full
algebraic catalogue or a superseded interval audit when every active use has
been replaced by a shorter proved consequence.

## 5. Shared Setup And Structural Reductions

Only genuinely cross-strategy material belongs before the strategy sections.
Use the following sources.

| Source | Recorded status | Manuscript role |
|---|---|---|
| [`1000_problem_statement.md`](../proof/1XXX_foundations/10XX_global_conventions/1000_problem_statement.md) | Definition | Define the theorem target and seven role triangles. |
| [`1001_geometry_objects.md`](../proof/1XXX_foundations/10XX_global_conventions/1001_geometry_objects.md) | Definition | Define $H$, $H_L$, $O$, $V_i$, edges, radial arms, and midpoints. |
| [`1002_targets_skeleton_half_skeleton_lotus_benzene.md`](../proof/1XXX_foundations/10XX_global_conventions/1002_targets_skeleton_half_skeleton_lotus_benzene.md) | Definition | Define only $S$ and $S_{1/2}$ when later sections need them. Omit unused Lotus, Benzene, and experimental targets. |
| [`1003_open_unit_vs_shrunken_closed_equivalence.md`](../proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md) | Proven | Prove the open, shrunken-closed, and expanded-closed equivalence. |
| [`1005_symmetry_and_normalization.md`](../proof/1XXX_foundations/10XX_global_conventions/1005_symmetry_and_normalization.md) | Definition | Fix the $D_6$ normalization convention. |
| [`1101_CE_classification.md`](../proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md) | Proven | Prove the exhaustive CE0/CE1/CE2 classification. |
| [`1201_V_triangle_types.md`](../proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) | Proven | Prove the Vd0/Vd1/Vd2/T3-like classification and T3-like translation normalization. |
| [`1202_local_coordinates_abc.md`](../proof/1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md) | Definition | Define actual reaches and demand coordinates. |
| [`1208_boundary_degeneracies.md`](../proof/1XXX_foundations/12XX_V_triangle/1208_boundary_degeneracies.md) | Definition | Fix endpoint, tangency, and positive-length conventions. |
| [`1212_vertex_rows_and_Nplus.md`](../proof/1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md) | Definition | Define actual supercritical rows and $N_+$. |
| [`1214_strict_boundary_handoff_selection.md`](../proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) | Proven | Transfer exact-one and at-least-two actual supercritical patterns to selected strict handoffs. |
| [`1213_T3_like_nonsupercritical.md`](../proof/1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md) | Proven | Record that T3-like rows never contribute to $N_+$. |
| [`2005_midpoint_self_cover_lemma.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md) | Proven | Relate own-midpoint coverage to nonsupercriticality. |
| [`2100_CE1_CE2_exactly_one_midpoint_lemma.md`](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md) | Proven | Normalize CE1/CE2 center roles to the unique covered midpoint. |

The setup section must prove, not merely announce, that the seven points
$O,V_0,\ldots,V_5$ force distinct roles. It must distinguish the original open
roles from their closed associates. The T3-like translation theorem must be
described as closed-trace domination, not as a literal replacement that keeps
$V_i$ in the interior of an open role.

Define a boundary gap using the actual open traces on an edge. A singleton
uncovered endpoint between two open traces counts as a gap. This convention is
essential in Strategy 2 and Strategy 4.

## 6. Strategy 1: Direct Length-Sum Obstructions

### Chapter-local lemmas

Develop the following results inside this strategy section before their branch
applications.

| Source | Recorded status | Manuscript role |
|---|---|---|
| [`2008_neighbor_ray_max_c_formula.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md) | Proven | Supply the local adjacent-ray exclusion used in support and trace counting. |
| [`2014_Vd1_Vd2_corner_normal_form.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md) | Proven | Prove the corner normal form and strict half-unit boundary cap. |
| [`2015_Vd2_neighbor_midpoint_cap.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md) | Proven | Prove the one-third cap for a Vd2 neighboring-midpoint rescue. |
| [`2102_CE1_M0_e01_maximal_intervals.md`](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2102_CE1_M0_e01_maximal_intervals.md) | Proven | Supply the CE1 interval bound used in the center boundary cap. |
| [`2103_CE2_M0_e50_e01_maximal_interval_pairs.md`](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md) | Proven | Supply the CE2 interval-pair bound used in the center boundary cap. |
| [`2500_boundary_length_bounds.md`](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) | Proven | Prove the full boundary-trace table for center and vertex roles. |
| [`2510_skeleton_length_bounds.md`](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md) | Proven | Prove the conditional skeleton-trace caps. |
| [`2520_diagonal_length_bounds.md`](../proof/2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md) | Proven | Prove the full diagonal-trace caps. |

Define the diagonal target and state all target measures explicitly:

$$
D=\bigcup_{i=0}^5 r_i,
\qquad
\mathcal H^1(\partial H)=6,
\qquad
\mathcal H^1(D)=6,
\qquad
\mathcal H^1(S)=12.
$$

Every use of $S$ or $D$ must retain the hypotheses under which the corresponding
trace caps were proved. In particular, this section must not claim that seven
unit triangles can never cover $S$ without additional branch hypotheses.

### Terminal applications

| Source | Recorded status | Case closed in this strategy |
|---|---|---|
| [`3010_CE0_perimeter_length_obstruction.md`](../proof/3XXX_CE0/30XX_Nplus0/3010_CE0_perimeter_length_obstruction.md) | Proven | CE0, $N_+=0$. |
| [`3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](../proof/3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE0, $N_+=1$, with a Vd1/Vd2 role. |
| [`4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1, $N_+=0$, with a Vd1/Vd2 role. |
| [`4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2, $N_+=0$, with a Vd1/Vd2 role. |
| [`4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE1, $N_+=1$, with a Vd1/Vd2 role. |
| [`4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md) | Proven | CE2, $N_+=1$, with at least two Vd1/Vd2 roles. |
| [`4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md) | Proven | CE1/CE2, $N_+=1$, with at least two T3-like roles and no Vd1/Vd2 role. |
| [`4200_CE1_CE2_skeleton_length_route.md`](../proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md) | Proven | CE1/CE2, $N_+\ge2$. |
| [`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md) | Proven | The Vd2 neighboring-midpoint subcase of the CE2 exactly-one-Vd1/Vd2 package. |
| [`414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md) | Proven | The additional-positive-support subcase of that package. |

The last two rows are only part of the exceptional CE2 exactly-one-Vd1/Vd2
assembly. Strategy 2 proves its remaining placement subcases.

## 7. Strategy 2: Exact Boundary--Radial Demand Propagation

This section owns the difficult CE1/CE2 exact-value arguments. Its common
mechanism is:

1. exact center geometry turns a boundary gap, midpoint placement, or radial
   exit into endpoint and radial demands;
2. an exact local admissible-set or capped-demand map propagates those demands
   through neighboring nonsupercritical rows;
3. the returning demand is incompatible with the remaining boundary or radial
   capacity.

The entire CE1/CE2, $N_+=0$, all-Vd0 package belongs here, including its
elementary no-active-gap subcase. Keep that package together for conceptual
continuity.

### Chapter-local lemmas

| Source | Recorded status | Manuscript role |
|---|---|---|
| [`2004_admissible_set.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) | Proven | Prove the exact local admissible set and radial envelope. |
| [`2006_T3_like_midpoint_lemma.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md) | Proven | Exclude a T3-like role from its own midpoint. |
| [`2007_max_b_map.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md) | Proven | Supply the outgoing-fiber interval and universal diameter bound; retain the full contact catalogue only in the proof source. |
| [`2010_free_supercritical_max_b.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md) | Proven | Prove the free strict-supercritical outgoing supremum. |
| [`2011_capped_demand_map.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md) | Proven | Prove the exact capped nonsupercritical map, its four genuine labels, and duality. |
| [`2012_high_radial_low_root_bounds.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md) | Proven | Supply the high-radial low-root estimates. |
| [`2013_T3_like_side_tradeoff.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2013_T3_like_side_tradeoff.md) | Proven | Prove the T3-like side tradeoff and crossed-pair obstruction. |
| [`2105_CE1_exact_formulas.md`](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md) | Proven | Derive the exact CE1 domain, trace, radial exits, and demands. |
| [`2106_CE2_exact_formulas.md`](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md) | Proven | Derive the exact CE2 domain, coupled traces, radial exits, and demands. |
| [`2107_one_side_capped_loss.md`](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md) | Proven | Prove the one-side capped-output loss theorem. |
| [`2108_CE2_two_endpoint_capped_loss.md`](../proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md) | Proven | Prove the strict two-endpoint CE2 capped-output theorem. |

When this section needs a boundary or diagonal cap already proved in Strategy
1, cite that result rather than reproducing it.

### Terminal packages

| Source | Recorded status | Case closed in this strategy |
|---|---|---|
| [`4013_boundary_loss_index.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) | Proven | The entire CE1/CE2, $N_+=0$, all-Vd0 package, including no-, one-, and two-active-gap states. |
| [`4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md) | Proven | CE1/CE2, $N_+=0$, with a T3-like role and no Vd1/Vd2 role. |
| [`4102_CE2_two_gap_completion.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4102_CE2_two_gap_completion.md) | Proven | CE2, $N_+=1$, all Vd0, with two gaps. |
| [`4106_CE1_one_gap_five_map_completion.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md) | Proven | CE1, $N_+=1$, all Vd0, with one gap. |
| [`4107_CE2_one_gap_five_map_completion.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md) | Proven | CE2, $N_+=1$, all Vd0, with one gap in either orientation. |
| [`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) | Proven | Assemble the positive-gap cases here; defer its zero-gap case to Strategy 4. |
| [`4130_CE1CE2_exactly_one_T3_like_index.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md) | Proven | CE1/CE2, $N_+=1$, exactly one T3-like role and no Vd1/Vd2 role. |
| [`4131_midpoint_forcing_reduction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md) | Proven | Prove the exact midpoint and placement reduction for the preceding row. |
| [`4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md) | Proven | Prove its exact T3-like/supercritical propagation inequality and terminal boundary contradiction. |
| [`4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) | Proven | Navigate the exceptional CE2 exactly-one-Vd1/Vd2 package. |
| [`4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md) | Proven | Close the normalized Vd1 rescue placement. |
| [`4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md) | Proven | Close the adjacent placement. |
| [`4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md) | Proven | Close the nonadjacent placements. |
| [`4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md) | Proven | Replace the Vd1--supercritical pair and reduce to the proved all-Vd0 package. |
| [`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md) | Proven | Assemble these exact cases with Strategy 1's two exceptional subcases. |

### Required five-link one-gap chains

Do not compress a one-gap proof to the name of a fivefold composition. For
each orientation, display the starting endpoint demand, all five scalar
iterates, the capped-map bound for each actual row, the intervening boundary
handoff, the returning actual reach on row $0$, and its incompatible
supercritical-row upper bound. Use $(A_i,B_i)$ for actual boundary reaches and
reserve $c_i$ for the radial lower-bound demands.

For CE1, use the normalized variables of `4106`, including

$$
\begin{aligned}
c_0&=\eta+A+D,&
c_1&=1-\frac DR,&
c_2&=1-D,\\
c_3&=1-\frac AR,&
c_4&=1-A,&
c_5&=1-\frac Aw,
\end{aligned}
$$

and put $z_0=X=R-D$ and $z_j=G_{c_j}(z_{j-1})$ for
$1\le j\le5$. Write all five actual-row links:

$$
\begin{aligned}
A_1&\ge z_0,&
B_1&\le F_{c_1}(z_0),&
A_2&\ge1-B_1\ge z_1,\\
A_2&\ge z_1,&
B_2&\le F_{c_2}(z_1),&
A_3&\ge1-B_2\ge z_2,\\
A_3&\ge z_2,&
B_3&\le F_{c_3}(z_2),&
A_4&\ge1-B_3\ge z_3,\\
A_4&\ge z_3,&
B_4&\le F_{c_4}(z_3),&
A_5&\ge1-B_4\ge z_4,\\
A_5&\ge z_4,&
B_5&\le F_{c_5}(z_4),&
A_0&\ge1-B_5\ge z_5.
\end{aligned}
$$

End with the complete contradiction

$$
A_0\ge Z_{\mathrm{CE1}}:=z_5
>B_{c_0}(s)\ge A_0.
$$

For the CE2 right-gap orientation, use the exact demands

$$
\begin{aligned}
c_0&=k,&
c_1&=1-\frac{\delta}{R},&
c_2&=1-\delta,\\
c_3&=1-\min\left\{\frac{\delta}{w},\frac{\alpha}{R}\right\},&
c_4&=1-\alpha,&
c_5&=1-\frac{\alpha}{w}.
\end{aligned}
$$

Put $z_0=1-v=R-\delta$ and $z_j=G_{c_j}(z_{j-1})$. The
unique-gap hypothesis makes the other five handoffs strict, so write

$$
\begin{aligned}
A_1&\ge z_0,&
B_1&\le F_{c_1}(z_0),&
A_2&>1-B_1\ge z_1,\\
A_2&>z_1,&
B_2&\le F_{c_2}(z_1),&
A_3&>1-B_2\ge z_2,\\
A_3&>z_2,&
B_3&\le F_{c_3}(z_2),&
A_4&>1-B_3\ge z_3,\\
A_4&>z_3,&
B_4&\le F_{c_4}(z_3),&
A_5&>1-B_4\ge z_4,\\
A_5&>z_4,&
B_5&\le F_{c_5}(z_4),&
A_0&>1-B_5\ge z_5.
\end{aligned}
$$

The terminal comparison must be shown as

$$
A_0>Z_R:=z_5>B_{c_0}(y)\ge A_0.
$$

For the CE2 left-gap orientation, do not write only “by symmetry.” Record the
reflection

$$
x\longleftrightarrow y,
\quad u\longleftrightarrow v,
\quad R\longleftrightarrow w,
\quad \alpha\longleftrightarrow\delta,
$$

$$
A'_0=B_0,
\quad B'_0=A_0,
\quad A'_i=B_{6-i},
\quad B'_i=A_{6-i},
\quad c'_i=c_{6-i}
\quad(1\le i\le5).
$$

Put $\widetilde z_0=1-u=w-\alpha$ and
$\widetilde z_j=G_{c_{6-j}}(\widetilde z_{j-1})$. Then explicitly write the
reverse five-row chain

$$
\begin{aligned}
B_5&\ge\widetilde z_0,&
A_5&\le F_{c_5}(\widetilde z_0),&
B_4&>1-A_5\ge\widetilde z_1,\\
B_4&>\widetilde z_1,&
A_4&\le F_{c_4}(\widetilde z_1),&
B_3&>1-A_4\ge\widetilde z_2,\\
B_3&>\widetilde z_2,&
A_3&\le F_{c_3}(\widetilde z_2),&
B_2&>1-A_3\ge\widetilde z_3,\\
B_2&>\widetilde z_3,&
A_2&\le F_{c_2}(\widetilde z_3),&
B_1&>1-A_2\ge\widetilde z_4,\\
B_1&>\widetilde z_4,&
A_1&\le F_{c_1}(\widetilde z_4),&
B_0&>1-A_1\ge\widetilde z_5.
\end{aligned}
$$

Conclude with

$$
B_0>Z_L:=\widetilde z_5>B_{c_0}(x)\ge B_0.
$$

Use the simplified analytic proofs on the full strict CE1 and CE2 center
domains. Do not introduce an auxiliary survivor restriction or a classified
map for the unique supercritical row. In the CE1 estimate, retain the current
$p=-f_8$ derivative decomposition for the $Q(P)$ sign, the manifestly
positive expression for $-g_5'$, and monotonicity of $h$ together with
$h(3/4)<7/16$ for the low-$c$ row-$3$ chord. Retain the direct CE2
two-threshold argument, the analytic `407X` completion, the direct `2108`
two-gap loss, singleton-gap handling, and the universal diameter bound. The
optional `4104` reduction and historical `4108` verifier are not
dependencies, and the unused full `2007` contact catalogue should not be
reproduced.

For the `407X` package, incorporate the mathematical reduction proved in
[`4073_boundary_loss_framework.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4073_boundary_loss_framework.md)
but do not cite that `Reduction` file as a terminal proof. Read and integrate
the proved branch files listed by `4070`, including the exact final assembly in
[`407d_rigor_final_assembly.md`](../proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407d_rigor_final_assembly.md).

## 8. Strategy 3: Area Loss

This strategy contains only the final unconditional area route for CE0. Do not
include the failed tangent-envelope route or superseded structural hypotheses.

### Chapter-local lemmas and terminal assemblies

| Source | Recorded status | Manuscript role |
|---|---|---|
| [`3202_area_function_and_monotonicity.md`](../proof/3XXX_CE0/32XX_Nplus_ge2/3202_area_function_and_monotonicity.md) | Reference | Use only as a notation guide: define $f(a,b)$ and $G(a,b)=1-f(a,b)$ explicitly in the manuscript, and do not use its historical conjecture as a dependency. |
| [`3205_unconditional_local_square_loss.md`](../proof/3XXX_CE0/32XX_Nplus_ge2/3205_unconditional_local_square_loss.md) | Proven | Prove the ordinary and supercritical local square-loss inequalities. |
| [`3208_CE0_conditional_area_certificate.md`](../proof/3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md) | Proven | Prove the six-row strict area inequality from the local losses. |
| [`3175_direct_T3_like_area_loss.md`](../proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3175_direct_T3_like_area_loss.md) | Proven | Prove T3-like nonsupercriticality and the direct T3-like area-loss bound. |
| [`3174_CE0_one_supercritical_T3_certificate.md`](../proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3174_CE0_one_supercritical_T3_certificate.md) | Proven | Assemble the one-supercritical T3-like global loss. |
| [`3171_T3_like_area_certificate_index.md`](../proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3171_T3_like_area_certificate_index.md) | Proven | Close CE0, $N_+=1$, with a T3-like role and no Vd1/Vd2 role. |
| [`3201_area_conjecture_index.md`](../proof/3XXX_CE0/32XX_Nplus_ge2/3201_area_conjecture_index.md) | Proven | Close CE0, $N_+\ge2$, despite the historical filename. |

Normalize areas consistently. If one unit equilateral triangle has area
$\sqrt3/4$, then the side-one hexagon has normalized area $6$. Make every
strict inequality leading to a total below $6$ explicit.

## 9. Strategy 4: Center-Independent Direct Nine-Point Obstruction

State the strategy theorem without a CE hypothesis:

> There is no seven-role open cover in which all six vertex roles are Vd0,
> they cover the full boundary, and exactly one actual boundary row is
> supercritical.

For $N_+=1$, all Vd0, “zero boundary gaps” is equivalent to full coverage of
$\partial H$ by the six vertex roles. CE0 forces this zero-gap condition
automatically. CE1 and CE2 zero-gap cases satisfy the same center-independent
hypotheses and must be treated as applications of the same theorem, not as
separate reproofs.

### Chapter-local lemmas and terminal theorem

| Source | Recorded status | Manuscript role |
|---|---|---|
| [`2004_admissible_set.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md) | Proven | Reuse Strategy 2's exact radial envelope $c_{\max}$ for the common radial demand. |
| [`20090_ab_set_index.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20090_ab_set_index.md) | Reference | Use only for navigation; no index statement is a proof. |
| [`20095_exact_caliper_certificate.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20095_exact_caliper_certificate.md) | Proven | Supply the exact finite caliper theorem underlying the strict specialization. |
| [`20091_ab_union_curve_a_plus_b_gt_1.md`](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md) | Proven | Prove the four-piece frontier used only for the unique supercritical row. |
| [`31051_direct_radial_forcing.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31051_direct_radial_forcing.md) | Proven | Force the six common radial witnesses out of every actual vertex role by $c_{\max}$, openness, Vd0 locality, and diameter. |
| [`31052_fixed_line_circle_signs.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31052_fixed_line_circle_signs.md) | Proven | Prove all first-root, moving-circle, coordinate-sum, endpoint, and reflected signs locally. |
| [`31053_direct_asymmetric_witness_forcing.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31053_direct_asymmetric_witness_forcing.md) | Proven | Define $Q_-,Q_0,Q_+$ exactly and exclude them from all six actual vertex roles using the strict frontier, vertex distances, and $X_2,X_5$. |
| [`31054_four_cap_enclosure_reduction.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31054_four_cap_enclosure_reduction.md) | Proven | Supply the Newton inner witnesses, cap-chain reduction, ray order, and analytic adjacent-overlap proof. |
| [`31055_rational_radial_envelopes_and_mixed_reduction.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31055_rational_radial_envelopes_and_mixed_reduction.md) | Proven | Replace $c_*$ by branchwise rational upper envelopes and reduce the two mixed overlaps to eight integer-polynomial signs. |
| [`31056_global_analytic_mixed_positivity.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31056_global_analytic_mixed_positivity.md) | Proven | Prove those signs on three fixed charts by twenty global Bernstein identities, without interval arithmetic or subdivision. |
| [`31057_terminal_nine_point_enclosure.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31057_terminal_nine_point_enclosure.md) | Proven | Assemble the exact terminal inequality $\Lambda(K_{\mathrm{wit}})\ge1$. |
| [`31058_center_independent_direct_nine_point_obstruction.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) | Proven | Assemble the center-independent direct nine-point contradiction. |
| [`31059_CE0_Nplus1_all_Vd0_completion.md`](../proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31059_CE0_Nplus1_all_Vd0_completion.md) | Proven | Deduce the CE0 branch by proving that CE0 forces full vertex-role boundary coverage. |
| [`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](../proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) | Proven | Reuse `31058` for the CE1/CE2 zero-gap cases after Strategy 2 handles the positive-gap cases. |

The direct proof uses no $AB$-union for a nonsupercritical row, no symmetric
or asymmetric model residual core, no antitone comparison of six model
unions, no neighboring-ray theorem `2008`, and no optional six-point
inequality.  All direct and computational ingredients must come from the
self-contained `3105X` package; older packages are provenance only.

The section must explain the logical chain

$$
\text{zero gaps}
\Longrightarrow
\text{full Vd0 boundary cover}
\Longrightarrow
\text{strict exact-one handoffs}
\Longrightarrow
\text{six radial and three asymmetric witnesses forced into }T_C
\Longrightarrow
\Lambda(K_{\mathrm{wit}})\ge1
\Longrightarrow
\text{contradiction with containment in the open unit triangle }T_C.
$$

For the radial witnesses, explicitly exclude each $D_i$ from its matching
role by maximality of $c_{\max}$ and openness, from its adjacent roles by Vd0
locality, and from the three remaining roles by diameter. Their convex hull
forces the centered disk used in the enclosure theorem. For the asymmetric
witnesses, explicitly exclude row $4$ by the unique strict-row frontier,
rows $0,1,2$ by vertex distances, and rows $3,5$ by the actual handoffs
$X_2,X_5$. Then invoke `31054`--`31057` for the exact terminal enclosure
inequality. Keep the filename `06_strategy4_ab_core.tex` only for
assembly compatibility; reader-facing prose must call this the direct
nine-point obstruction.

## 10. Exhaustive Routing Table

The final assembly must route cases exactly as follows.

| Center and $N_+$ branch | Exhaustive refinement | Owning strategy |
|---|---|---:|
| CE0, $N_+=0$ | All vertex types | 1 |
| CE0, $N_+=1$ | All six roles Vd0; zero gaps are automatic | 4 |
| CE0, $N_+=1$ | At least one Vd1/Vd2 role | 1 |
| CE0, $N_+=1$ | No Vd1/Vd2 role and at least one T3-like role | 3 |
| CE0, $N_+\ge2$ | All vertex types | 3 |
| CE1/CE2, $N_+=0$ | All six roles Vd0, including the no-active-gap state | 2 |
| CE1/CE2, $N_+=0$ | At least one Vd1/Vd2 role | 1 |
| CE1/CE2, $N_+=0$ | No Vd1/Vd2 role and at least one T3-like role | 2 |
| CE1/CE2, $N_+=1$ | All six roles Vd0 and zero gaps | 4 |
| CE1/CE2, $N_+=1$ | All six roles Vd0 and exactly one gap | 2 |
| CE2, $N_+=1$ | All six roles Vd0 and two gaps | 2 |
| CE1, $N_+=1$ | At least one Vd1/Vd2 role | 1 |
| CE2, $N_+=1$ | At least two Vd1/Vd2 roles | 1 |
| CE2, $N_+=1$ | Exactly one Vd1/Vd2 role | Hybrid: Strategies 1 and 2 |
| CE1/CE2, $N_+=1$ | No Vd1/Vd2 role and exactly one T3-like role | 2 |
| CE1/CE2, $N_+=1$ | No Vd1/Vd2 role and at least two T3-like roles | 1 |
| CE1/CE2, $N_+\ge2$ | All vertex types | 1 |

For the hybrid CE2 row, Strategy 1 owns the additional-positive-support
skeleton sum and the Vd2 neighboring-midpoint cap. Strategy 2 owns the exact
adjacent/nonadjacent placements, Vd1 rescue, axis replacement, and reduction
to the $N_+=0$ all-Vd0 package.

The $N_+=1$, all-Vd0 gap split is center-independent at its first step:

- zero gaps go to Strategy 4 for CE0, CE1, and CE2;
- one gap goes to Strategy 2 and is possible for CE1 or CE2;
- two gaps go to Strategy 2 and are possible only for CE2.

The final proof must separately explain why these gap counts are exhaustive
and why CE0 cannot have a positive gap.

## 11. Mathematical Writing Requirements

The generated paper must follow these rules.

### Statements and dependencies

- State every lemma with all hypotheses needed at the point of application.
- Do not hide open/closed assumptions in prose preceding a theorem.
- Distinguish actual roles from normalized or dominating closed triangles.
- When a proof uses only a subset of a full trace, explicitly invoke
  monotonicity of $\mathcal H^1$.
- When replacing a role, prove which boundary, radial, midpoint, or interior
  coverage properties are preserved.
- When using symmetry, specify how every orientation-sensitive index and
  coordinate transforms.
- End each strategy section with a proposition listing precisely the terminal
  branches it closes.

### Notation and LaTeX

- Use `$...$` for inline mathematics and display environments for displayed
  mathematics in the generated LaTeX.
- Use `\left\lvert \left\lbrace ... \right\rbrace \right\rvert` for
  cardinalities.
- Use `\mathrm{...}` for named operators introduced by the paper.
- Put conditions for `\sup`, `\inf`, `\min`, and `\max` in subscripts.
- Do not use alignment markers inside operator arguments.
- Preserve the distinctions among $H$, $H_L$, $S$, and $S_{1/2}$.
- Preserve the labels CE0, CE1, CE2, Vd0, Vd1, Vd2, and T3-like.
- Preserve **걸거치는** when naming the recurring T3-like crossing or
  straddling phenomenon.

### Proof exposition

- Prefer short named lemmas over long unstructured calculations.
- Before a large case split, state why the cases are mutually exclusive and
  exhaustive.
- After the split, close every row explicitly.
- Give exact formulas before estimates derived from them.
- Mark strict inequalities and identify the hypothesis producing strictness.
- Do not use phrases such as “obvious,” “generic,” “by computation,” or
  “similarly” when they conceal an unproved branch.
- If a reflected case is omitted, write the exact reflection and explain why
  it preserves the hypotheses and conclusion.

## 12. Certificate Appendices

The paper must include independently checkable certificate statements for all
machine-assisted parts used in the proof.

At minimum, document:

1. the finite all-parameter caliper certificate in `20095`;
2. the branchwise rational $c_{\max}$ envelopes and exact mixed-overlap
   reduction in `31055`;
3. the three fixed charts and twenty global tensor-product Bernstein
   identities in `31056`;
4. every other machine-assisted certificate that remains a logical dependency
   after analytic simplification.

Optional historical cross-checks superseded by analytic proofs belong in the
source ledger and proof package, not in the manuscript certificate appendix.
In particular, the older outward-rounded adaptive subdivision and adaptive
mixed-overlap verifier are redundant legacy audits, not dependencies of the
active paper.

For each certificate, state:

- the exact parameter domain;
- the target inequality;
- the exact rational, integer-polynomial, or $\mathbb Q(\sqrt3)$
  representation;
- every positive denominator and equivalence used in clearing radicals;
- why the finite events or fixed analytic charts cover the full domain;
- the global positive-basis identity and exact coefficient-sign test;
- the strict margin or sign conclusion;
- the software command and expected output, as reproducibility information;
- why the mathematical verification does not depend on unrecorded
  floating-point assumptions.

For the mixed overlaps, record the $L$- and $T$-cell rational envelopes, the
reduction to the eight polynomials $A_{B,X},B_{B,X}$, the $T,L_0,L_1$ chart
coverage, and the exact sign check for the twenty global Bernstein
expansions. Record the canonical polynomial digest and the deterministic
`PASS` output with `adaptive_subdivision: false` and
`branch_and_bound: false`. The reproduction command is

```text
python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_mixed_overlap_core_derivation.py
python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_global_core_positivity.py
```

The first command derives the canonical polynomial transcript exactly from
the witness formulas using SymPy and checks byte-for-byte equality.  The
second uses only the Python standard library to verify the twenty global
Bernstein identities.

The required canonical digest is

```text
dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485
```

Do not describe interval boxes, pruning, adaptive depth, or directed rounding
as part of the active proof.

Scripts marked `Experiment` may be cited as reproduction aids only after the
paper has stated the exact certificate and verification theorem. Do not turn a
script's status into the status of a mathematical lemma.

## 13. Figure Policy And Asset Layout

Figures are optional. Generate one only when it materially clarifies the
geometric setup, a case structure, an exact local map, a trace budget, or the
direct nine-point witness construction. Do not add decorative images.

Every visual asset and every file used to generate it must live under
`arrange/paper_draft/figures/`. This includes:

- TikZ source fragments;
- coordinate or plotting scripts;
- source data created specifically for a figure;
- rendered PDF or PNG assets.

Use descriptive ASCII filenames with no spaces or shell-sensitive
punctuation. Reference figures only through paths of the form
`figures/descriptive_name.ext`. For a TikZ fragment, use
`\input{figures/descriptive_name.tex}`. For a rendered asset, use
`\includegraphics{figures/descriptive_name.pdf}` or the corresponding PNG
path. No graphics path may contain `..` or point outside the draft workspace.

Prefer exact vector figures:

1. derive coordinates from the definitions and formulas proved in the paper;
2. retain the TikZ or generation source beside the rendered PDF;
3. record the source formula, script, and rendered filename in
   `source_ledger.md`;
4. use PNG only when a vector representation is impractical.

When a figure uses TikZ source, add `\usepackage{tikz}` to `main.tex` and load
only the TikZ libraries actually used. Keep the TikZ fragment itself in
`figures/`; do not embed a long drawing directly in a strategy file.

If a raster image is generated by an illustration model rather than by exact
coordinates, label it clearly as schematic. Never use a generative image to
support a metric, incidence, extremal, coverage, or noncoverage claim.

Every figure must have a caption that says whether it is exact or schematic.
An exact caption must identify its coordinate normalization and relevant
hypotheses. A schematic caption must say that the drawing is not to scale.
The prose must prove every mathematical claim independently of the figure.
Figures, plots, and screenshots are explanatory aids, not proofs or
certificates.

If no figure materially improves the exposition, leave `figures/` empty and
omit figure packages beyond the minimum preamble.

## 14. Excluded And Historical Material

Do not use the following as proof dependencies:

- the empirical simplified Bands I--III catalog in `20092`--`20094`;
- the failed tangent-envelope conjecture `3172` and the unused conditional
  route `3173`;
- the superseded structural route `3204`;
- the algorithm-2 five-point packages and their empirical transition strips;
- the six-point strategy package;
- the older model residual-core assembly `31030`, `31032`, and `31035`, which
  remains an independent proved route but is not the paper's active route;
- the predecessor direct assembly `31041`--`31044`, which remains proved but
  is superseded as the active source by the self-contained `3105X` package;
- the outward-rounded mixed-overlap subsection of `31034`, its adaptive
  interval verifier, and the redundant adaptive verifier retained by `31037`;
- the proposed analytic finite-nine-point replacement `31045`, whose status
  remains `Strategy`;
- the optional reduction `4104`;
- the historical `4108` CE1 verifier;
- the empirical historical candidate `4141`;
- the May 21 and May 25 failed finite-point routes;
- the old `33XX` chain, which is not a dependency of the current main
  assembly.

The predecessor formulas and certificates are cited only in the `31050`
provenance index; the active direct route uses their complete local rewrites
in `31051`--`31057`. The neighbor-ray theorem `2008` remains a valid Strategy
1 dependency, but it is not a Strategy 4 dependency. Strategy 2 may use the
outgoing-fiber and diameter consequences of `2007` without importing its
unused full contact catalogue.

Do not assert global noncoverage of the full skeleton. The numerical
counterexample recorded in
[`9081_skeleton_cover_counterexample.md`](../proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md)
rules out that standalone route. Conditional skeleton and diagonal
obstructions remain valid only with their stated branch hypotheses.

## 15. Completion Checklist

The LLM must complete every item before presenting the manuscript.

### Source audit

- [ ] Every mathematical source used by the paper has been read completely.
- [ ] Every result used as established has `Status: Proven` or
      `Status: Definition` in its own file.
- [ ] Every `Reduction` has all terminal dependencies discharged by proved
      manuscript results.
- [ ] No empirical, failed, strategy, experiment, or optional route appears as
      a proof dependency.
- [ ] Strategy 4 is sourced entirely through the self-contained proven
      package `31051`--`31059`; earlier `310X` ingredients appear only in the
      `31050` provenance index.
- [ ] Every Markdown provenance link in this guide and `source_ledger.md`
      resolves to an existing file.

### Exhaustiveness audit

- [ ] Every row of the routing table in Section 10 appears exactly once in the
      final assembly, except the explicitly identified Strategy 1/2 hybrid.
- [ ] The CE0/CE1/CE2 split is proved exhaustive.
- [ ] The $N_+=0$, $N_+=1$, and $N_+\ge2$ split is exhaustive.
- [ ] Every vertex-role refinement follows from the proved exhaustive type
      classification.
- [ ] Zero, one, and two boundary gaps are handled with singleton gaps retained.
- [ ] The CE1, CE2 right-gap, and reflected CE2 left-gap proofs each display
      all five actual-row transitions and their terminal row-$0$ contradiction.

### Rigor audit

- [ ] Open roles and their closures are never silently identified.
- [ ] Actual reaches and selected demands are never conflated.
- [ ] Every midpoint-forcing argument lists all possible rescuing roles.
- [ ] Every length or area total specifies its normalization and strictness.
- [ ] Every exact certificate has a theorem statement and reproducible audit.
- [ ] The active mixed-overlap proof uses the fixed-chart global Bernstein
      certificate, not interval arithmetic, adaptive subdivision, or
      branch-and-bound.
- [ ] Strategy 4 directly excludes all nine witnesses from all six actual
      vertex roles before applying the enclosure theorem.
- [ ] No branch-specific skeleton result is stated globally.

### AMS manuscript audit

- [ ] `latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex`
      compiles without errors, undefined references, or undefined citations.
- [ ] Every theorem, lemma, equation, section, and appendix reference resolves.
- [ ] Every `\input`, bibliography, font, and graphics reference resolves
      inside `arrange/paper_draft/`.
- [ ] `main.tex` includes `appendix_exact_mixed_overlap.tex` and does not
      include `06_strategy4_nonbranching_completion.tex`.
- [ ] `fontspec` loads both local Noto Sans KR subsets under XeLaTeX, and
      **걸거치는** renders in the compiled paper.
- [ ] The abstract states the theorem and proof mechanisms without overstating
      what computation proves.
- [ ] The introduction's roadmap agrees with the final routing table.
- [ ] The final theorem invokes the open/closed/scaled equivalence correctly.
- [ ] The bibliography contains no invented or unverified entry.
- [ ] The tracked `main.pdf` was regenerated from the final accepted sources
      and is not stale.

### Workspace and figure audit

- [ ] All persistent paper sources, build-support files, compiled output, logs,
      and auxiliary files remain under `arrange/paper_draft/`.
- [ ] The embedded font subsets, their provenance README, and `OFL.txt` remain
      under `arrange/paper_draft/fonts/` and are recorded in the source ledger.
- [ ] No generated manuscript file modifies `proof/`, the repository root, or
      another package.
- [ ] Every visual asset, source drawing, data file, and generation script is
      under `arrange/paper_draft/figures/`.
- [ ] Every figure filename is descriptive ASCII without spaces or
      shell-sensitive punctuation.
- [ ] Every figure is identified as exact or schematic, and no proof depends
      on visual inspection.
- [ ] Every exact figure records its coordinate source; every schematic figure
      is declared not to scale.

Only after all five audits pass should the LLM call the paper complete.
