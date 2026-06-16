# CE0 May 25 Supremum-Endpoint Archive

Status: Failed

This folder archives the May 25 five-point obstruction target for the CE0,
$N_+=1$ setting. It is not recorded as a false inequality. It is archived
because the diagonal points are defined by actual-union supremum endpoints
before a clean all-Vd0 reduction is available, so the route is too complicated
to serve as the live CE0 all-Vd0 proof package.

The target was imported from:

| Source | Recorded status | Notes |
|---|---|---|
| [`dylan0301/hexagon-cover-visual/proof2/conj0525-reduction-prompt.md`](https://github.com/dylan0301/hexagon-cover-visual/blob/gulgu/proof2/conj0525-reduction-prompt.md) | External source | Imported May 25 source prompt. |

It concerns the reduced slice

$$
t_3=t_2,\qquad t_5=t_4,\qquad t_4>t_2,
$$

with

$$
t_0\le t_5,\qquad t_1\le t_0,\qquad t_2\le t_1.
$$

Equivalently, the unique strict local $AB$-union vertex is $V_4$:

$$
a_4+b_4>1,
$$

The exact nondegenerate strict $AB$-union frontier formula for this local
region, including the two unit-circle arcs and two line segments, is recorded
in:

| File | Recorded status | Notes |
|---|---|---|
| [../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009_ab_union_curve_a_plus_b_gt_1.md](../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009_ab_union_curve_a_plus_b_gt_1.md) | Reference | Strict $AB$-union frontier formula. |

while

$$
a_0+b_0\le1,\qquad a_1+b_1\le1,\qquad a_2+b_2\le1,
$$

and the May 21/22 equalities

$$
a_3+b_3=1,\qquad a_5+b_5=1
$$

are used as assumptions.

The five obstruction points are

$$
K_5=\{P_3,P_5,D_0,D_1,D_2\}.
$$

The conjecture is:

$$
\Lambda(K_5)>1
$$

whenever all five points are defined.  Equivalently, no closed unit
equilateral triangle contains the five points.

## Relation to the May 21/22 package

The points $P_3$ and $P_5$ are the same type of selected non-axis
intersections used in `../962X_may21_four_point_failure/`.  The May 25 target replaces
the four-point Pattern A radial pair with three diagonal endpoints

$$
D_0,\qquad D_1,\qquad D_2
$$

defined from the initial uncovered intervals along $[O,V_0]$, $[O,V_1]$, and
$[O,V_2]$.

This replacement is intentional.  The diagonal endpoints are not chosen from a
fixed local radial formula or from a preassigned Vd1/Vd2-type local pattern.
They are chosen from the actual uncovered set after removing all six regions
$R_i$.  Thus if a nonlocal region cuts a half-diagonal before the usual radial
point, the point $D_j$ moves to that first cut instead of forcing the old
radial choice.

This package does not prove the May 25 conjecture and does not record a
counterexample.  It records the precise target, branch choices, diagonal
endpoint issues, and proof obligations.
The June 3 one-critical neighbor-envelope strategy for simplifying the
diagonal endpoint functions is recorded in
[`9636_CE0_one_critical_neighbor_envelope_strategy.md`](9636_CE0_one_critical_neighbor_envelope_strategy.md)
(Status: Strategy).

## Skeleton-target caveat

The source prompt describes a historical global obstruction for the full
skeleton $S$.  In this repository, standalone noncoverage of $S$ is refuted by
the May 24 numerical counterexample in
[`../908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md`](../908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md)
(Status: Empirical).

Thus this folder should be read only as a focused conditional finite-point
target, not as a proof of full-skeleton noncoverage.

## Files

| File | Recorded status | Notes |
|---|---|---|
| [`9632_CE0_reduction_prompt_spec.md`](9632_CE0_reduction_prompt_spec.md) | Reference | Self-contained May 25 reduced-slice specification in repository notation. |
| [`9633_CE0_five_point_target_and_obligations.md`](9633_CE0_five_point_target_and_obligations.md) | Lemma target | The conjectural five-point inequality and proof obligations. |
| [`9634_CE0_branch_and_diagonal_case_notes.md`](9634_CE0_branch_and_diagonal_case_notes.md) | Strategy | Branch-selection and diagonal-cut notes for $P_3$, $P_5$, and $D_j$. |
| [`9635_CE0_current_status.md`](9635_CE0_current_status.md) | Reference | Short status table and exact unresolved gaps. |
| [`9636_CE0_one_critical_neighbor_envelope_strategy.md`](9636_CE0_one_critical_neighbor_envelope_strategy.md) | Strategy | Strategy note for replacing the local radial/neighbor maximum defining $D_j$ by a four-variable max-free envelope. |
