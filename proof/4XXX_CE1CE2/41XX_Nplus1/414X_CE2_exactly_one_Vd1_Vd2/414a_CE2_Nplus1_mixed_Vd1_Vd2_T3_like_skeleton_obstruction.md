# CE1/CE2, $N_+=1$, Mixed Vd1/Vd2--Positive-Support Obstruction

Status: Proven

Assume the closures of original open-cover roles satisfy:

- the center role is CE1 or CE2 with exact midpoint set $\{M_0\}$;
- $N_+=1$;
- exactly one vertex row is Vd1 or Vd2;
- at least one additional vertex row has positive-length support on an adjacent
  radial arm.

The unique supercritical row is distinct from every positive-support row:
[`2008`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md)
shows that a supercritical row has no positive adjacent-ray support.

In the terminology of the common skeleton theorem
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md),
there are at least three short vertex roles:

- the unique supercritical row;
- the Vd1/Vd2 row;
- one additional positive-support row.

The three-short-role theorem therefore gives

$$
L_S(T_C)+\sum_{i=0}^5L_S(T_i)<12.
$$

This estimate is applied to the closures of the original open roles, before
any optional T3-like translation, so the interior hypotheses of the skeleton
caps remain valid.  Since the full skeleton has length $12$, subadditivity for
a cover gives a contradiction.

Thus every mixed one-Vd1/Vd2 branch with an additional positive-support row,
including every Vd1/Vd2--T3-like mixture, is impossible.  The proof is
class-independent; the file remains in `414X` only because that assembly uses
it in the surviving CE2 branch.

$$
\Box
$$
