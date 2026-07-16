# Main Theorem

Status: Proven

## Theorem

The regular side-$1$ hexagon $H$ cannot be covered by seven open unit
equilateral triangles.

Equivalently, for every $L>1$, the regular side-$L$ hexagon $H_L$ cannot be
covered by seven closed unit equilateral triangles.

The equivalence of these two formulations is proved in
[`../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

## 1. Role assignment and exhaustive classifications

Suppose for contradiction that seven open unit equilateral triangles cover
$H$. The seven distinguished points

$$
O,V_0,\dots,V_5
$$

are pairwise at distance at least $1$. Any two points in one open unit
equilateral triangle are at distance strictly below $1$. Consequently each
triangle contains at most one distinguished point. Since all seven points are
covered by seven triangles, the triangles have distinct roles

$$
T_C,T_0,\dots,T_5,
$$

where $O\in T_C$ and $V_i\in T_i$. This bookkeeping is recorded in
[`../1XXX_foundations/10XX_global_conventions/1000_problem_statement.md`](../1XXX_foundations/10XX_global_conventions/1000_problem_statement.md).

Apply the proved center and vertex-role classifications to the closed
triangles associated with the original open roles, retaining the same role
symbols. The center classification
[`../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md)
places $T_C$ in exactly one of CE0, CE1, and CE2. The proved vertex-role
classification
[`../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md)
places every original $T_i$ in exactly one of Vd0, Vd1, Vd2, and T3-like.

Let $(a_i,b_i)$ be the actual maximal incoming and outgoing boundary reaches
of $T_i$, as in
[`../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md`](../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md),
and put

$$
N_+
=
\left\lvert
\left\{
i:a_i+b_i>1
\right\}
\right\rvert.
$$

Exactly one of $N_+=0$, $N_+=1$, and $N_+\ge2$ holds. In every case where the
six vertex roles cover the whole boundary and a branch uses smaller strict
boundary-handoff demands, the proved selection theorem
[`../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
connects them to these actual reaches without silently changing the required
supercritical count.

We now eliminate every resulting case.

## 2. CE0

Assume first that $T_C$ is CE0.

### 2.1. No supercritical row

If $N_+=0$, the strict perimeter-overlap argument in
[`../3XXX_CE0/30XX_Nplus0/3010_CE0_perimeter_length_obstruction.md`](../3XXX_CE0/30XX_Nplus0/3010_CE0_perimeter_length_obstruction.md)
gives a contradiction.

### 2.2. Exactly one supercritical row

Suppose $N_+=1$. The exhaustive vertex classification gives exactly one of
the following three alternatives.

1. If all six vertex roles are Vd0, the residual-core and forced-disk theorem
   in
   [`../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31030_CE0_all_Vd0_residual_core_strategy.md`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31030_CE0_all_Vd0_residual_core_strategy.md)
   gives a contradiction.
2. If at least one vertex role is Vd1 or Vd2, the strict boundary-length
   obstruction in
   [`../3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](../3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md)
   gives a contradiction.
3. Otherwise at least one vertex role is T3-like and every other role is Vd0
   or T3-like. The direct T3-like area package
   [`../3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3171_T3_like_area_certificate_index.md`](../3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3171_T3_like_area_certificate_index.md)
   gives a contradiction.

### 2.3. At least two supercritical rows

If $N_+\ge2$, the unconditional local square-loss theorem and its strict
six-row assembly in
[`../3XXX_CE0/32XX_Nplus_ge2/3201_area_conjecture_index.md`](../3XXX_CE0/32XX_Nplus_ge2/3201_area_conjecture_index.md)
give a contradiction.

Thus CE0 is impossible.

## 3. CE1 and CE2

Assume now that $T_C$ is CE1 or CE2.

### 3.1. No supercritical row

Suppose $N_+=0$.

1. If all six vertex roles are Vd0, the exact boundary-loss theorem
   [`../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md)
   gives a contradiction.
2. If a Vd1 or Vd2 role occurs, the CE1 and CE2 boundary-length obstructions
   are respectively
   [`../4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](../4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md)
   and
   [`../4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md`](../4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md).
3. Otherwise at least one role is T3-like and no role is Vd1 or Vd2. The
   exact four-label reassembly
   [`../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md`](../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md)
   gives a contradiction.

### 3.2. Exactly one supercritical row

Suppose $N_+=1$.

If a Vd1 or Vd2 role occurs, then:

- in CE1, the obstruction is
  [`../4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md`](../4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md);
- in CE2 with at least two such roles, it is
  [`../4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md`](../4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4111_CE2_Nplus1_at_least_two_Vd1_Vd2_boundary_length_obstruction.md);
- in CE2 with exactly one such role, the exhaustive assembly is
  [`../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4140_CE2_Nplus1_exactly_one_Vd1_Vd2_index.md).

It remains to suppose that no Vd1 or Vd2 role occurs. Count the T3-like
roles.

- At least two are excluded by
  [`../4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md`](../4XXX_CE1CE2/41XX_Nplus1/412X_at_least_two_T3_like/4123_CE1_CE2_at_least_two_T3_like_diagonal_obstruction.md).
- Exactly one is excluded by
  [`../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md`](../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4130_CE1CE2_exactly_one_T3_like_index.md).
- If none occurs, all six vertex roles are Vd0. The exhaustive center-gap
  proof in
  [`../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4101_CE1CE2_Nplus1_all_Vd0_strategy.md)
  gives a contradiction. Its no-gap state is closed by the
  center-independent all-boundary residual-core theorem
  [`../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31035_center_independent_all_boundary_obstruction.md`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/31035_center_independent_all_boundary_obstruction.md).

### 3.3. At least two supercritical rows

If $N_+\ge2$, the shared skeleton-length obstruction
[`../4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](../4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md)
gives a contradiction.

Thus CE1 and CE2 are both impossible.

## 4. Conclusion

The exhaustive CE0, CE1, and CE2 alternatives all lead to contradictions.
Therefore seven open unit equilateral triangles cannot cover $H$.

Finally, the proved open/closed/scaled equivalence cited above gives the
equivalent statement that, for every $L>1$, seven closed unit equilateral
triangles cannot cover $H_L$.

$$
\Box
$$
