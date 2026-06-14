# Algorithm-2 Setup And Point Construction

Status: Empirical strategy

After symmetry and reduction, take the unique supercritical row to be the
$V_4$ row. The free data are organized as:

$$
a_4,b_4,a_1,b_1.
$$

The sketch treats $a_4,b_4$ as outer parameters and $a_1,b_1$ as the remaining
free variables controlling the positions of two boundary points.

For Vd0 rows, the intended reduction uses the equalities

$$
a_3+b_3=1,\qquad a_5+b_5=1.
$$

The reduction justifying these normalizations is not proved here.

## Fixed $V_4$ Points

Two obstruction points are selected intersections involving the strict local
$AB$-union frontier at $V_4$. The exact nondegenerate strict frontier formula
for

$$
a+b>1,\qquad a^2+ab+b^2<1
$$

is recorded in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009_ab_union_curve_a_plus_b_gt_1.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009_ab_union_curve_a_plus_b_gt_1.md).

The intended two fixed points are the selected intersections of that frontier
with radius-$1$ circles centered at the boundary points corresponding to the
$b_2a_3$ and $b_5a_0$ data. Branch selection, existence, endpoint, and
closest-valid-branch conditions are not proved in this file.

## Algorithm-2 Diagonal Points

Algorithm 2 chooses three diagonal points by forcing two of the three
nonsupercritical rows among $V_0,V_1,V_2$ to lie on equality lines.

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

The intended property is that, regardless of how the free boundary points move,
the corresponding diagonal points remain inside the relaxed obstruction region
used for the finite five-point test.

The current status is empirical/strategy. A proof must define the relaxed
region exactly and prove the containment for all allowed parameters.
