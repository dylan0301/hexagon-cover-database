# Main Theorem

Status: Proven

## Theorem

The regular side-$1$ hexagon $H$ cannot be covered by seven open unit
equilateral triangles. Equivalently, for every $L>1$, the regular side-$L$
hexagon $H_L$ cannot be covered by seven closed unit equilateral triangles.

The equivalence is proved in
[`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

## Proof

Assume that seven open unit equilateral triangles cover $H$. The center $O$
and vertices $V_0,\dots,V_5$ are pairwise at distance at least $1$, whereas
two points in one open unit triangle are at distance strictly below $1$.
Each triangle therefore covers at most one distinguished point. Since seven
triangles cover all seven points, they have distinct roles

$$
T_C,T_0,\dots,T_5,
$$

with $O\in T_C$ and $V_i\in T_i$.

Apply the proved classifications to the associated closed triangles, keeping
the same symbols. By [`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md),
$T_C$ is exactly one of CE0, CE1, and CE2. By
[`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md), every
vertex role is exactly one of Vd0, Vd1, Vd2, and T3-like.

Let $(a_i,b_i)$ be the actual maximal boundary reaches of $T_i$ and set

$$
N_+
=
\left\lvert
\left\lbrace i:a_i+b_i>1\right\rbrace
\right\rvert.
$$

Exactly one of $N_+=0$, $N_+=1$, and $N_+\ge2$ holds. When a branch selects
smaller strict cut rows, [`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
rigorously transfers the required supercritical pattern from these actual
reaches.

It remains only to list the exhaustive terminal cases.

### CE0

| Actual-row and vertex-type case | Proven contradiction |
|---|---|
| $N_+=0$ | Strict perimeter obstruction [`3010`](../3XXX_CE0/30XX_Nplus0/3010_CE0_perimeter_length_obstruction.md) |
| $N_+=1$, all six roles Vd0 | Self-contained direct all-Vd0 nine-point completion [`31059`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31059_CE0_Nplus1_all_Vd0_completion.md) |
| $N_+=1$, some role Vd1 or Vd2 | Boundary-length obstruction [`3141`](../3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) |
| $N_+=1$, no Vd1/Vd2 role and some T3-like role | Direct area obstruction [`3171`](../3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3171_T3_like_area_certificate_index.md) |
| $N_+\ge2$ | Six-row square-loss obstruction [`3201`](../3XXX_CE0/32XX_Nplus_ge2/3201_area_conjecture_index.md) |

For $N_+=1$, the last three rows are exhaustive: either all roles are Vd0;
otherwise a Vd1/Vd2 role occurs; otherwise the exhaustive vertex
classification forces a T3-like role. Hence CE0 is impossible.

### CE1 and CE2

| Actual-row and vertex-type case | Proven contradiction |
|---|---|
| $N_+=0$, all six roles Vd0 | Exact boundary-loss package [`4013`](../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) |
| $N_+=0$, some Vd1/Vd2 role, CE1 | Boundary-length obstruction [`4040`](../4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) |
| $N_+=0$, some Vd1/Vd2 role, CE2 | Boundary-length obstruction [`4041`](../4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) |
| $N_+=0$, no Vd1/Vd2 role and some T3-like role | Four-label obstruction [`4070`](../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md) |
| $N_+=1$, some Vd1/Vd2 role, CE1 | Boundary-length obstruction [`4110`](../4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) |
| $N_+=1$, at least two Vd1/Vd2 roles, CE2 | Boundary-length obstruction [`4111`](../4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md) |
| $N_+=1$, exactly one Vd1/Vd2 role, CE2 | Exhaustive mixed-type assembly [`4140`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md) |
| $N_+=1$, no Vd1/Vd2 role and at least two T3-like roles | Diagonal obstruction [`4123`](../4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md) |
| $N_+=1$, no Vd1/Vd2 role and exactly one T3-like role | Boundary obstruction [`4130`](../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md) |
| $N_+=1$, all six roles Vd0 | Exact gap closure [`4101`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md) |
| $N_+\ge2$ | Shared skeleton-length obstruction [`4200`](../4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md) |

For $N_+=0$, the first four rows are exhaustive by the vertex
classification. For $N_+=1$, first split according to whether a Vd1/Vd2 role
occurs; in CE2 split further into exactly one or at least two. If none occurs,
the number of T3-like roles is $0$, $1$, or at least $2$, giving the next
three rows. Thus CE1 and CE2 are impossible.

All three center classes lead to contradictions. Therefore seven open unit
equilateral triangles cannot cover $H$. The equivalence in `1003` gives the
closed expanded-hexagon formulation. $\square$
