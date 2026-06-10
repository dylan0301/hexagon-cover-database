# Hexagon Covering Notes, 2026-05-08

Status: Navigation

These notes organize definitions, proof strategies, local lemmas, computations, and failed approaches for the problem of covering a regular hexagon by seven open unit equilateral triangles.

## Main theorem target

$$
\boxed{\text{The regular hexagon }H\text{ of side length }1\text{ cannot be covered by seven open unit equilateral triangles.}}
$$

The equivalent expanded closed-triangle formulation is:

$$
\boxed{\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}}
$$

The equivalence is proved in `100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`.

## Reading order

1. `proof/000_main_theorem.md`
2. `proof/001_proof_tree_index.md`
3. `100_foundations/100_problem_statement.md`
4. `100_foundations/103_open_unit_vs_shrunken_closed_equivalence.md`
5. `200_center_triangle/200_C_triangle_overview.md`
6. `300_vertex_triangle/300_V_triangle_overview.md`
7. `400_global_propagation/403_six_step_composition.md`
8. `500_half_skeleton_lemmas/500_half_skeleton_lemma_index.md`
9. `550_CE_Vd0_boundary_loss/550_index.md`
10. `600_case_strategies/600_case_strategy_index.md`
11. `620_may21_patternA/620_index.md`
12. `630_may25_five_point_conjecture/630_index.md`
13. `640_area_conjecture/640_index.md`
14. `900_failed_ideas/900_failed_idea_index.md`

## Proof-tree scaffold

The paper-style proof scaffold is recorded in:

- `proof/000_main_theorem.md`
- `proof/001_proof_tree_index.md`
- `proof/002_status_and_dependencies.md`

It organizes the current proof strategy by the supercritical row count

$$
N_+=\#\{i:a_i+b_i>1\}.
$$

This scaffold is a navigation layer. It does not move existing files or upgrade
any proof status beyond the cited source files.

## Most important current proof package

The case

$$
\mathrm{CE0}+\text{at least one Vd1 or Vd2}
$$

is recorded as proven for the half-skeleton target in:

- `600_case_strategies/601_CE0_Vd1_Vd2_half_skeleton_theorem.md`
- `600_case_strategies/602_CE0_Vd1_Vd2_rhombus_geometry.md`
- `600_case_strategies/603_CE0_Vd1_Vd2_frontier_perturbation.md`
- `600_case_strategies/604_CE0_Vd1_Vd2_F_chain_inequalities.md`
- `600_case_strategies/605_CE0_Vd1_Vd2_midpoint_hole_subcases.md`
- `600_case_strategies/606_CE0_Vd1_Vd2_assembly.md`

## Proven CE1/CE2 Vd0 boundary-loss package

The branch package for the CE1/CE2 all-Vd0 boundary-loss obstruction is recorded in:

- `550_CE_Vd0_boundary_loss/550_index.md`
- `550_CE_Vd0_boundary_loss/556_lower_sheet_completion_proofs.md`

It proves the boundary-loss lemma under the package assumptions.  For CE2, it still uses the CE2 one-interval reduction assumed in `550_CE_Vd0_boundary_loss/551_setup_and_reduction.md`.

## Active May 21/22 Pattern A package

The current four-point Pattern A reduction package is recorded in:

- `620_may21_patternA/620_index.md`

It proves the $p$-elimination theorem and the endpoint Taylor theorem for the lower outside-quarter Pattern A reduced inequalities.  The remaining non-endpoint Bernstein certificate is still incomplete and is recorded as empirical/certificate-prototype status.

## Active May 25 five-point conjecture package

The May 25 reduced five-point conjecture package is recorded in:

- `630_may25_five_point_conjecture/630_index.md`

It records the finite-point target $\Lambda(K_5)>1$ for $K_5=\{P_3,P_5,D_0,D_1,D_2\}$ under the reduced May 25 slice.  The target is open in this repository.

## Active area-conjecture package

The area-conjecture package is recorded in:

- `640_area_conjecture/640_index.md`

It records the target $\sum_i f(a_i,b_i)<5$ when at least two rows satisfy
$a_i+b_i>1$, using the CE0 six-point model and the separate CE1/reduced-CE2
seven-point extension.  The CE2 use assumes the CE2 one-interval lemma.

The package now includes a conditional CE0 analytic certificate:

- `640_area_conjecture/647_CE0_conditional_area_certificate.md`

This proves the CE0 six-point final inequality under the local square-loss
bounds for $f(a,b)$.  The local square-loss bounds themselves remain open proof
obligations, so the area package is not yet an unconditional proof of CE0, CE1,
or CE2.

## May 24 skeleton-cover counterexample

The full-skeleton noncoverage target is refuted by a numerical counterexample:

- `800_computation/811_skeleton_cover_counterexample.md`

The verifier records seven closed equilateral triangles of side strictly less than $1$ covering $S$.  This does not prove a cover of $H$ and does not change conditional half-skeleton results under their stated hypotheses.

## Proof-status labels

See `100_foundations/106_proof_status_conventions.md`.
