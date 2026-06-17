# Algorithm-2 Setup And Point Construction

Status: Strategy

After symmetry and reduction, take the unique supercritical row to be the $V_4$ row. The free data are organized as:

$$
a_4,b_4,a_1,b_1.
$$

The sketch treats $a_4,b_4$ as outer parameters and $a_1,b_1$ as the remaining free variables controlling the positions of two boundary points.

For Vd0 rows, the intended reduction uses the equalities

$$
a_3+b_3=1,\qquad a_5+b_5=1.
$$

The reduction justifying these normalizations from the full all-Vd0 branch is not proved here.

## Fixed $V_4$ Points

Two obstruction points are selected intersections involving the strict local $AB$-union frontier at $V_4$. The exact nondegenerate strict frontier formula for

$$
a+b>1,\qquad a^2+ab+b^2<1
$$

is recorded in [`../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009_ab_union_curve_a_plus_b_gt_1.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009_ab_union_curve_a_plus_b_gt_1.md).

The strict branch realization for the selected two fixed points is now recorded in [`3115_strict_branch_line_realization.md`](3115_strict_branch_line_realization.md): in the strict $\rho<1$ branch, the $C_2$ circle intersects the non-axis frontier exactly once on $\Gamma_A^{\mathrm{lin}}$, and the $C_5$ circle intersects it exactly once on $\Gamma_B^{\mathrm{lin}}$.

The limiting boundary $\rho=1$ is not covered by that proof because the nondegenerate strict curve formula degenerates there.

## Algorithm-2 Diagonal Points

Algorithm 2 chooses three diagonal points by forcing two of the three nonsupercritical rows among $V_0,V_1,V_2$ to lie on equality lines.

The three equality patterns are:

$$
a_1+b_1=1,\qquad a_2+b_2=1,
$$

$$
a_0+b_0=1,\qquad a_2+b_2=1,
$$

and

$$
a_0+b_0=1,\qquad a_1+b_1=1.
$$

The two-variable reduction is recorded in [`3116_algorithm2_two_variable_transition.md`](3116_algorithm2_two_variable_transition.md). Under the equality assumptions, all three diagonal choices use the same local pair

$$
(1-b_4,1-a_4).
$$

Thus algorithm 2 uses one common diagonal coordinate

$$
c_*=c_{\max}(1-b_4,1-a_4),
$$

and places

$$
D_j^{(2)}=(1-c_*)V_j,\qquad j=0,1,2.
$$

The intended property is that, regardless of how the free boundary points move, these diagonal points remain inside the relaxed obstruction region used for the finite five-point test.

The current status of that containment statement is still empirical/strategy. A proof must define the relaxed obstruction region exactly and prove the containment for all allowed parameters.
