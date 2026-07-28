# Private source ledger

This is an authoring and verification record, not a reader-facing proof.
Repository paths are relative to the repository root.  Only numbered sources
with a sufficient recorded status may support a manuscript theorem.

## Persistent manuscript artifacts

| Artifact | Role |
|---|---|
| `arrange/paper_draft/main.tex` | AMS preamble and body/appendix assembly. The universal transfer calculus now precedes the signed center calculus. |
| `arrange/paper_draft/01_introduction.tex` | Theorem, dictionary, unchanged routing table, active-gap-rank kernel, and the canonical decorated $g$-family overview. |
| `arrange/paper_draft/02_structural_reductions.tex` | Common geometry and exhaustive structural reduction. |
| `arrange/paper_draft/02a_universal_calculus.tex` | Enclosure gauge, universal radical, historical $g_c$, hatted cap, complement dual, center-assisted subscripts, free envelope $g_c^{\rm sc}$, composition, affine superscripts, threshold superscripts, and path budget. |
| `arrange/paper_draft/04a_signed_center_calculus.tex` | Signed CE1/CE2 normal form, center exits, boundary budget, actual-row $\widehat g_c^\vee$ interface, common five-row reduction, and CE2 threshold clause. |
| `arrange/paper_draft/03_strategy1_length.tex` | Complete trace-budget proof; unchanged by the Strategy 2 notation refactor. |
| `arrange/paper_draft/04b_common_CE1_CE2_budgets.tex` | Master perimeter deficit, short-role count, small CE2 slack, and three-short-role theorem. |
| `arrange/paper_draft/04_strategy2_reader.tex` | Master chain-relaxation table, all-Vd0 kernel, CE1/CE2 relaxations of one exact five-row chain, free-envelope rescuer chain, and Vd terminal transfers. |
| `arrange/paper_draft/05_strategy3_area.tex` | Complete area proof; its $\mathcal L$ notation is disjoint from the transfer family. |
| `arrange/paper_draft/06_strategy4_reader.tex` | Direct forcing, Newton inner reduction, cap chain, overlap proposition, and enclosure contradiction. |
| `arrange/paper_draft/07_exhaustive_assembly.tex` | Final routing-table assembly, citing the Strategy 2 chain table and preserving the Strategy 1 side of the hybrid row. |
| `arrange/paper_draft/04c_short_Vd_placements.tex` | Quarter radial envelope, T3-like and Vd1 profiles, adjacent rescuer, and exact Vd placements. It may retain $A_{\rm sc},B_{\rm sc}$ as explicitly documented technical aliases of $1-g_c^{\rm sc},g_c^{\rm sc}$. |
| `arrange/paper_draft/04_strategy2_exact_demand.tex` | Exact contact-cell catalogue, endpoint certificates, CE1 terminal algebra, and irreducible `407X` audit. It retains $B_c,F_c,G_c$ as technical aliases. |
| `arrange/paper_draft/06_strategy4_ab_core.tex` | Exact strict $AB$ frontier, forcing signs, Newton placement, ray order, and overlap proofs. |
| `arrange/paper_draft/appendix_symbols.tex` | Compact canonical symbol table, including $g_c$, $\widehat g_c$, $f^\vee$, $g_{c,J}^\vee$, $g_c^{\rm sc}$, and decorated lower relaxations. |
| `arrange/paper_draft/appendix_exact_mixed_overlap.tex` | Mixed-overlap proof, exact Bernstein identities, digest, and replay record. |
| `arrange/paper_draft/main.pdf` | Derived artifact. It is not replaced by this source-only notation refactor. |

The tracked PDF therefore remains the previous build.  Build from
`arrange/paper_draft/` with

```text
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex
```

No bibliography is required.  Figures are explanatory and are not proof
certificates.

## Canonical transfer dictionary

The authoritative source is
`proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md`.

For incoming defect $x=1-a$ and radial demand $c$,

$$
g_c(x)=\max\{y:(1-x,y,c)\in\mathcal A\},
\qquad
\widehat g_c(x)=\min\{g_c(x),x\}.
$$

For any map $f$,

$$
f^\vee(a)=1-f(1-a).
$$

Thus $\widehat g_c^\vee$ is the exact nonsupercritical reach transfer, and
$\widehat g_{c,J}^\vee$ is its center-assisted form.  The single free strict-
supercritical outgoing envelope is

$$
g_c^{\rm sc}
=
\sup_{\{x:g_c(x)>x\}}g_c(x).
$$

The old symbols remain only as technical aliases:

$$
B_c(a)=g_c(1-a),
\qquad
F_c(a)=\widehat g_c(1-a),
\qquad
G_c(a)=\widehat g_c^\vee(a),
$$

$$
B_{\rm sc}(c)=g_c^{\rm sc},
\qquad
A_{\rm sc}(c)=1-g_c^{\rm sc}.
$$

The zero-radial distinction is

$$
g_0(x)>x\quad(0<x<1),
\qquad
\widehat g_0(x)=x.
$$

## Universal structural and local sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/0XXX_main/0000_main_theorem.md` | Proven | `thm:main` and final assembly. |
| `proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md` | Proven | Open/closed/scaled equivalence. |
| `proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md` | Proven | CE0/CE1/CE2 classification. |
| `proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md` | Proven | Vd0/Vd1/Vd2/T3-like classification and translation normalization. |
| `proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md` | Proven | Strict handoffs and actual supercritical-pattern preservation. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md` | Proven | Exact local admissible set and enclosure gauge sublevel set. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md` | Proven | Exact outgoing envelope and interval fibers; technical alias $B_c$. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md` | Proven | Exact formula and nonattainment for $g_c^{\rm sc}$. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md` | Proven | Exact $\widehat g_c$, complement duality, and four labels; technical aliases $F_c,G_c$. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2016_universal_Tplus_normal_form.md` | Proven | Selected-$T_+$ normal form and affine lower relaxations. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2017_threshold_routing.md` | Proven | One-hit and two-threshold lower relaxations. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2018_diameter_transfer_and_adjacent_rescuer.md` | Proven | Diameter curve and common $1-g_c^{\rm sc}$--identity--$g_c^{\rm sc}$ rescuer chain. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md` | Proven | Residual operator, center-assisted $g$-transfers, radial component form, and path budget. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201a_equilateral_enclosure_and_radical_calculus.md` | Proven | Enclosure gauge, universal radical, and frontier atlas. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md` | Proven | Global quarter radial envelope. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md` | Proven | Vd own-radial and supported-arm margins. |
| `proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md` | Proven | Canonical transfer alphabet and relaxed composition. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md` | Proven | Signed center traces, sign class, and six exits. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2110_common_CE2_two_gap_application.md` | Proven | One application of the paired endpoint theorem to both two-gap cells. |

## Strategy 1 sources

The Strategy 1 routing and theorem statements are unchanged.  In particular,
`4040`, `4041`, `4110`, `4111`, `4123`, `4149`, `414a`, and `4200` retain
their perimeter or skeleton proofs.  The active common sources are `2500`,
`2510`, and `2530`.  The historical diagonal package `2520` remains proved but
is not an active manuscript dependency.

## Strategy 2 branch sources

| Source | Status | Principal manuscript use |
|---|---|---|
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md` | Proven | Exact hatted endpoint inequality for the one-gap $N_+=0$ chain. |
| `proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md` | Proven | Paired exact hatted endpoint inequality for both two-gap cells. |
| `proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md` | Proven | Strict identity cycle and exact-endpoint/$\mathrm I^3$ chains. |
| `proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md` | Proven | Residual exact endpoints with identity-relaxed interior and irreducible four-label audit. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4105_CE1_CE2_one_gap_five_row_interface.md` | Proven | Exact five-row $\widehat g_c^\vee$ induction and terminal capacity. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md` | Proven | CE1 affine/threshold relaxation; exact file may retain aliases. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md` | Proven | CE2 one-threshold-slot relaxation; exact file may retain aliases. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md` | Proven | All-Vd0 active-gap kernel and common chain table. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md` | Proven | T3-like verification against $1-g_c^{\rm sc}$. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md` | Proven | Vd1 verification against the same scalar threshold. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md` | Proven | Residuals, backward identity chain, quarter terminal transfer. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md` | Proven | Residual and identity propagation followed by a Vd-specific margin. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md` | Proven | Geometric preprocessing to ordinary Vd0 rows. |
| `proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md` | Proven | Exhaustive placement assembly with Strategy 1 complements retained. |

## Strategies 3 and 4

The active Strategy 3 sources remain `3205`, `3175`, `3174`, and `3208`.
The active Strategy 4 source remains the canonical `3105X` direct nine-point
package, with the strict supercritical $AB$ frontier in `20091`.  The body owns
the cap-chain and enclosure argument; the technical appendix owns the Newton
placement, overlap reductions, Gram factorization, integer-polynomial signs,
and Bernstein identities.

## Deliberate nondependencies

- The identity at zero radial demand belongs to $\widehat g_0$, not to raw
  $g_0$.
- The exact `407X` endpoint audit is not replaced by an unsupported envelope.
- The CE2 paired state is not split into independent one-gap calls.
- The CE1 scalar clause is not replaced by the CE2 threshold lemma.
- The `4146` terminal margin remains Vd-type-specific.
- Strategy 1 routes are not absorbed into Strategy 2.
- The historical half-edge $1/3$ envelope, optional `4104` reduction, optional
  disk-plus-point route, failed five-point route, and false full-skeleton route
  are not active dependencies.
- Numerical scripts are cross-checks unless a proved exact certificate is
  recorded in a source theorem.
