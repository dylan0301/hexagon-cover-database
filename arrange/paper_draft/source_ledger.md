# Private source ledger

This is an authoring and verification record, not a reader-facing proof. Paths
are relative to the repository root. A grouped row applies to every listed
source and manuscript label. Within a table cell, a bare filename after a
fully qualified path is in the same directory as the preceding qualified
path.

## Persistent artifacts

| Artifact | Role |
|---|---|
| arrange/paper_draft/main.tex | AMS preamble, metadata, assembly, and XeLaTeX setup. |
| arrange/paper_draft/01_introduction.tex | First-chapter theorem, definitions, seventeen-row table, and four-strategy overview. |
| arrange/paper_draft/02_structural_reductions.tex | Common geometry, exhaustive reductions, and gap-count lemma. |
| arrange/paper_draft/03_strategy1_overview.tex | Reader-facing Strategy 1 mechanism and interface proposition. |
| arrange/paper_draft/04_strategy2_overview.tex | Reader-facing Strategy 2 map interface, actual-row induction, branch flows, and interface proposition. |
| arrange/paper_draft/05_strategy3_overview.tex | Reader-facing Strategy 3 global loss sums and interface proposition. |
| arrange/paper_draft/06_strategy4_overview.tex | Reader-facing Strategy 4 nine-point mechanism and interface proposition. |
| arrange/paper_draft/07_exhaustive_assembly.tex | Five-block audit of the Chapter 1 routing table and final proof. |
| arrange/paper_draft/03_strategy1_length.tex | Complete Strategy 1 formulas and proofs, included as a technical appendix. |
| arrange/paper_draft/04_strategy2_exact_demand.tex | Complete Strategy 2 formulas and proofs, included as a technical appendix. |
| arrange/paper_draft/04a_strategy2_half_edge_envelope.tex | Rational/monotonicity appendix with the half-edge envelope and its exact domain limitation. |
| arrange/paper_draft/05_strategy3_area.tex | Complete Strategy 3 local and global calculations, included as a technical appendix. |
| arrange/paper_draft/06_strategy4_ab_core.tex | Complete Strategy 4 witness and enclosure calculations, included as a technical appendix. |
| arrange/paper_draft/appendix_certificates.tex | Exact finite caliper certificate. |
| arrange/paper_draft/appendix_exact_mixed_overlap.tex | Active rational-envelope and global-Bernstein proof of the mixed overlaps. |
| arrange/paper_draft/source_ledger.md | This provenance/status ledger. |
| arrange/paper_draft/fonts/README.md | Embedded-font provenance and build note. |
| arrange/paper_draft/fonts/OFL.txt | SIL Open Font License. |
| arrange/paper_draft/fonts/noto_sans_kr_subset_115.ttf | Glyph subset containing 걸. |
| arrange/paper_draft/fonts/noto_sans_kr_subset_118.ttf | Glyph subset containing 거치는. |
| arrange/paper_draft/main.pdf | Derived compiled manuscript. |
| arrange/paper_draft/figures/ | TikZ sources, shared styles, and temporary PNG role examples for the reader-facing geometric figures. |

Build from arrange/paper_draft with:
latexmk -xelatex -interaction=nonstopmode -halt-on-error main.tex.
Auxiliary files are transient and are not committed. No external literature
was supplied or needed for the proof, so there is no bibliography.

## Figure ledger

Every figure is explanatory and no proof depends on visual inspection.

| Figure source | Status and coordinate source |
|---|---|
| figures/tikz_setup.tex | Shared print-safe styles; exact hexagon coordinates from `1001_geometry_objects.md`. |
| figures/geometry_roles.tex | Exact target geometry and role anchors in the paper normalization. |
| figures/role_examples/center_role_ce0_example.png; center_role_ce1_example.png; center_role_ce2_example.png | Temporary author-supplied illustrative center-role screenshots, not to scale; blank outer margins are cropped. |
| figures/role_examples/vertex_role_vd0_axis_aligned_example.png; vertex_role_vd0_nonsupercritical_example.png; vertex_role_vd0_supercritical_example.png; vertex_role_vd1_example.png; vertex_role_vd2_example.png; vertex_role_t3_like_example.png | Temporary author-supplied illustrative vertex-role screenshots, not to scale; blank outer margins are cropped. |
| figures/handoff_and_gap.tex | Exact one-dimensional trace/gap convention with schematic interval lengths; includes open endpoints and singleton gaps. |
| figures/strategy1_trace_targets.tex | Exact sets $\partial H,D,S$ and their lengths; colors are explanatory. |
| figures/strategy2_ce1_ce2_n0_all_vd0.png | Author-supplied common schematic for the CE1/CE2, $N_+=0$, all-Vd0 boundary package, not to scale; three representative Vd0 roles are shown, and the placement is not a candidate cover. |
| figures/strategy2_five_map_chain.tex | Schematic actual-row propagation graph, not a substitute for the five-link inequalities. |
| figures/strategy3_local_area_loss.png; figures/strategy3_global_area_loss.png | Author-supplied schematic local and cyclic area-retention views, not to scale; only the darker colored portions represent area retained inside $H$, and no proof depends on visual inspection. |
| figures/strategy4_nine_point_witness.tex | Symbolically exact radial-point pattern with schematic parameter-dependent asymmetric witnesses. |
| figures/strategy4_cap_chain.tex | Schematic support-direction cap chain, not to scale. |

## Main theorem and common reductions

| Authoritative source path(s) | Recorded status | Manuscript label(s) |
|---|---|---|
| proof/0XXX_main/0000_main_theorem.md | Proven | thm:main |
| proof/1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md | Proven | cor:expanded-closed; prop:open-closed-scaled |
| proof/1XXX_foundations/10XX_global_conventions/1000_problem_statement.md; 1001_geometry_objects.md | Definition | lem:distinct-roles, derived from the defined forcing points and proved in the manuscript |
| proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md | Proven | prop:ce-classification |
| proof/1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md | Proven | lem:local-wedge; prop:vertex-classification; prop:t3-translation |
| proof/1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md; proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3175_direct_T3_like_area_loss.md | Proven | lem:t3-nonsupercritical |
| proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md | Proven | prop:strict-handoffs; thm:strict-handoff |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md | Proven | lem:self-midpoint |
| proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md | Proven | prop:unique-center-midpoint |

Paper-wide definitions also use 1001_geometry_objects.md,
1002_targets_skeleton_half_skeleton_lotus_benzene.md,
1005_symmetry_and_normalization.md, 1202_local_coordinates_abc.md,
1208_boundary_degeneracies.md, and 1212_vertex_rows_and_Nplus.md, all recorded
as Definition. Only the objects explicitly defined again in the manuscript are
retained.

## Strategy 1: direct length sums

| Authoritative source path(s) | Recorded status | Manuscript label(s) |
|---|---|---|
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md | Proven | thm:neighbor-ray-capacity |
| proof/2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md | Proven | lem:center-skeleton-cap; lem:positive-support-skeleton-cap; lem:no-support-skeleton-cap; lem:supercritical-skeleton-cap; lem:positive-support-rescuer; thm:conditional-skeleton-obstruction |
| proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/414a_CE2_Nplus1_mixed_Vd1_Vd2_T3_like_skeleton_obstruction.md | Proven | prop:ce2-mixed-positive-support-length; prop:length-branches |
| proof/2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md | Proven | thm:diagonal-trace-table |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md | Proven | prop:vd-corner-normal-form |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2015_Vd2_neighbor_midpoint_cap.md | Proven | lem:vd2-neighbor-midpoint-cap |
| proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2102_CE1_M0_e01_maximal_intervals.md | Proven | lem:ce1-maximal-interval |
| proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2103_CE2_M0_e50_e01_maximal_interval_pairs.md | Proven | lem:ce2-interval-pairs |
| proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md | Proven | thm:boundary-trace-table |
| proof/3XXX_CE0/30XX_Nplus0/3010_CE0_perimeter_length_obstruction.md; proof/3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md; proof/4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md; 4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md; proof/4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md; 4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md | Proven | prop:boundary-length-branches; prop:length-branches |
| proof/4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md | Proven | thm:conditional-skeleton-obstruction; prop:length-branches |
| proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md | Proven | prop:ce2-vd2-midpoint-length; prop:length-branches |
| proof/4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md | Proven | prop:t3-diagonal-obstruction; prop:length-branches |
| All proved terminal sources in this Strategy 1 table | Proven | prop:length-interface, which cites prop:length-branches |

## Strategy 2: exact demand propagation

| Authoritative source path(s) | Recorded status | Manuscript label(s) |
|---|---|---|
| proof/1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md | Definition | def:admissible-demands |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md | Proven | prop:exact-admissible-set; prop:local-admissible |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md; 2013_T3_like_side_tradeoff.md | Proven | lem:t3-midpoint-tradeoff |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md | Proven | outgoing-fiber interval and universal diameter bound used by the one-gap proofs; the unused full contact catalogue is deliberately not reproduced |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md | Proven | lem:free-supercritical-envelope |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md | Proven | prop:capped-demand-map |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md | Proven | eq:low-root-bounds; eq:high-demand-threshold; prop:ce1-one-gap; prop:ce2-one-gap; lem:407-four-label-loss |
| proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md; 2106_CE2_exact_formulas.md | Proven | prop:center-exact-formulas |
| proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2107_one_side_capped_loss.md | Proven | lem:one-side-capped-loss |
| proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2108_CE2_two_endpoint_capped_loss.md | Proven | lem:two-endpoint-capped-loss |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2012_high_radial_low_root_bounds.md; proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md | Proven | lem:half-edge-radial-envelope; lem:ce2-adjacent-outer-ratio; app:rational-monotonicity; exact domain restriction, counterexample, and adjacent outer-ratio calculation |
| proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md | Proven | prop:ce1-one-gap; explicit five-link actual-row chain $1\to2\to3\to4\to5\to0$, from $A_1\ge X$ through all five capped maps to $A_0\ge Z>B_{c_0}(s)$ |
| proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md | Proven | prop:ce2-one-gap; explicit right-gap chain $1\to2\to3\to4\to5\to0$ ending at $A_0>Z_R>B_{c_0}(y)$, and its fully reflected left-gap chain $5\to4\to3\to2\to1\to0$ ending at $B_0>Z_L>B_{c_0}(x)$ |
| proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md; 4102_CE2_two_gap_completion.md; 4106_CE1_one_gap_five_map_completion.md; 4107_CE2_one_gap_five_map_completion.md | Proven | prop:nplus-one-all-vd0 |
| proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md; 4131_midpoint_forcing_reduction.md; 4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md | Proven | prop:nplus-one-one-t3 |
| proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md | Proven | prop:nplus-zero-all-vd0 |
| proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md; 4072_support_isolation_after_T0_T3_like.md; 4074_L_Full_branch.md; 4075_Tminus_low_lower_branch_obligations.md; 4078_left_L_family_completion.md; 4079_first_Full_branch.md; 407a_left_Thigh_branch_completion.md; 407c_rigor_completion_details.md; 407d_rigor_final_assembly.md | Proven | lem:407-four-label-loss; prop:nplus-zero-t3 |
| proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md | Proven | package provenance for prop:nplus-zero-t3; terminal proof is supplied by the proved branch files in the preceding row |
| proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md | Proven | lem:vd1-adjacent-rescue |
| proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md | Proven | lem:vd-adjacent-placement |
| proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4146_CE2_Nplus1_T0_supercritical_nonadjacent_Vd1_Vd2_obstruction.md | Proven | lem:vd-nonadjacent-placement |
| proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md | Proven | lem:vd1-pair-replacement |
| proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md | Proven | package provenance for prop:ce2-one-vd-placement |
| proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md | Proven | prop:ce2-one-vd-placement; complementary exact-placement part of prop:demand-branches |
| All proved terminal sources in this Strategy 2 table | Proven | prop:demand-branches; prop:demand-interface |

The Reduction file 4073_boundary_loss_framework.md organizes notation only.
The script 407b_T_hi_Tminus_qright_threshold_certificate.py is retained as
an optional historical cross-check of the analytic threshold lemma, not as a
status source or manuscript dependency.  The superseded exact-rational script
4108_ce1_terminal_verifier.py is retained only as an independent cross-check
of the former Bernstein route and is not a manuscript dependency.

## Strategy 3: area loss

| Authoritative source path(s) | Recorded status | Manuscript label(s) |
|---|---|---|
| proof/3XXX_CE0/32XX_Nplus_ge2/3205_unconditional_local_square_loss.md | Proven | lem:area-wedge; thm:local-square-loss |
| proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3175_direct_T3_like_area_loss.md | Proven | thm:t3-direct-loss |
| proof/3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md; 3201_area_conjecture_index.md | Proven | lem:two-ascent-area |
| proof/3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3174_CE0_one_supercritical_T3_certificate.md; 3171_T3_like_area_certificate_index.md | Proven | lem:one-ascent-t3-area |
| All proved terminal sources in this Strategy 3 table | Proven | prop:area-branches; prop:area-interface |

The notation-only source 3202_area_function_and_monotonicity.md is Reference;
its historical conjecture is not used.

## Strategy 4: center-independent direct nine-point obstruction

| Authoritative source path(s) | Recorded status | Manuscript label(s) |
|---|---|---|
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md | Proven | thm:strict-ab-union; the only $AB$-union used is the unique supercritical-row frontier |
| proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md; proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md | Proven | lem:ab-extreme-jump; exact-one handoff chain and common demands |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md; proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31051_direct_radial_forcing.md | Proven | lem:symmetric-core-witness; direct forcing of all six radial witnesses by $c_{\max}$, openness, Vd0 locality, and diameter |
| proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31052_fixed_line_circle_signs.md | Proven | lem:fixed-line-signs; complete fixed-line circle signs for the actual moving handoffs |
| proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31053_direct_asymmetric_witness_forcing.md | Proven | lem:asymmetric-core-witness; exact formulas, direct distances, and exclusion using $X_2,X_5$ |
| proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31054_four_cap_enclosure_reduction.md; 31057_terminal_nine_point_enclosure.md | Proven | thm:witness-enclosure; terminal cap reduction, analytic adjacent overlaps, and enclosure assembly |
| proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31055_rational_radial_envelopes_and_mixed_reduction.md; 31056_global_analytic_mixed_positivity.md | Proven | thm:witness-enclosure; app:exact-mixed-overlap; rational radial envelopes, exact mixed-overlap reduction, and global Bernstein positivity |
| proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md | Proven | thm:zero-gap-obstruction; center-independent direct nine-point contradiction |
| proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31059_CE0_Nplus1_all_Vd0_completion.md; proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md | Proven | prop:ab-core-branches; prop:nine-point-interface; CE0 completion and CE1/CE2 zero-gap reuse of 31058 |

The direct route uses no nonsupercritical $AB$-union, model-core inclusion,
neighboring-ray comparison, or optional six-point inequality.  All active
direct construction and exact certificate ingredients are now recorded
inside the self-contained `3105X` package.  The older `3103X` residual-core
route and `3104X` direct route remain independently Proven predecessors but
are not active manuscript dependencies.  The AB index 20090 is Reference
only, and the empirical files 20092--20094 and the false complementary
comparison are not dependencies.

The proposed file
proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3104X_direct_Vd0_nine_point/31045_analytic_nine_point_caliper_strategy.md
is recorded as `Strategy` and is excluded from the manuscript dependency
chain.

## Final assembly and certificates

| Authoritative source path(s) | Recorded status | Manuscript label(s) |
|---|---|---|
| proof/1XXX_foundations/11XX_C_triangle/1101_CE_classification.md; proof/2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md; proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md | Proven | lem:gap-exhaustion |
| proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20095_exact_caliper_certificate.md | Proven | thm:cert-caliper |
| proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31055_rational_radial_envelopes_and_mixed_reduction.md; 31056_global_analytic_mixed_positivity.md | Proven | app:exact-mixed-overlap; exact mixed-overlap dependency of thm:witness-enclosure |

The manuscript-dependent reproduction scripts have no independent proof
status. Their role is only to replay the exact integer, rational, and
$\mathbb Q(\sqrt3)$ identities stated and justified in the appendix.  The
optional historical 407b and 4108 cross-checks are described separately
above.

## Deliberate exclusions

No theorem depends on a source recorded as Practically proven, Lemma target,
Strategy, Empirical, Experiment, or Failed. In particular, the paper excludes
the empirical AB catalogs 20092--20094; the false global skeleton claim; the
failed 3172 tangent-envelope conjecture and unused 3173 route; superseded 3204;
the algorithm-2/five-point and unverified six-point packages; optional
Reduction 4104; Strategy 31045; the outward-rounded and adaptive
mixed-overlap audits; and the false \(N_+\ge2\) AB comparison.  The older
Proven `3103X` model-core and `3104X` direct assemblies are retained only as
unused independent predecessors. Reference and navigation files only locate
the proved sources itemized above.

The repository-level audit also read README.md,
proof/0XXX_main/0001_proof_tree_index.md,
proof/0XXX_main/0002_status_and_dependencies.md,
proof/09XX_appendices/0910_notation_dictionary.md, and
proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md.
They govern navigation, notation, and status interpretation, not theorem
proofs.  The Reference index
proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20090_ab_set_index.md
is used only for navigation.  The false global-skeleton route is excluded in
accord with
proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md,
recorded as Empirical; the paper uses only branch-conditional skeleton results.
