# V-Triangle Overview

Status: Definition

A $V_i$-triangle $T_i$ is a unit equilateral triangle containing vertex $V_i$.

It interacts locally with:

- edge $e_{i-1,i}$;
- edge $e_{i,i+1}$;
- radial segment $[V_i,O]$;
- adjacent rays $r_{i-1}$ and $r_{i+1}$ for type classification.

## Type classification

For original vertex roles, the Vd0, Vd1, Vd2, and T3-like types are proved
exhaustive in
[`1201_V_triangle_types.md`](1201_V_triangle_types.md). That file also proves
the same-orientation translation normalization used in T3-like arguments.

## Local $AB$-union frontier

For prescribed adjacent edge points $A$ and $B$ with local edge lengths $a$
and $b$, the candidate local $AB$-union curve in the strict branch

$$
a+b>1, \qquad a^2+ab+b^2<1
$$

is recorded as a lemma target in
[`../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md`](../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).

The target formula gives two unit-circle arcs and two line segments, but its
support-pattern exhaustion is not yet proved.

## Neighbor-ray maximum

For prescribed adjacent edge points $A$ and $B$ with local edge lengths $a$ and $b$, the maximum parameter $c$ for which a $V_i$-triangle can also contain the neighboring radial point $(1-c)V_{i+1}$ is recorded in
[`../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md`](../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md).

The reflected lower-neighbor function for $(1-c)V_{i-1}$ is obtained by swapping $a$ and $b$.
