# CE1/CE2, $N_+=1$, At Least Two T3-Like Rows

Status: Proven

Assume the center role is CE1 or CE2, $N_+=1$, no vertex role is Vd1 or Vd2,
and at least two vertex roles are T3-like.

T3-like rows are nonsupercritical, so the unique supercritical row is distinct
from them.  A supercritical row is a short role in the terminology of
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md),
and every T3-like row is short because it has positive-length support on an
adjacent radial arm.  Hence there are at least three short vertex roles.

The three-short-role skeleton theorem in `2530` gives

$$
L_S(T_C)+\sum_{i=0}^5L_S(T_i)<12.
$$

But the full hexagon skeleton has length $12$, so a cover would imply the
opposite weak inequality by subadditivity.  This contradiction eliminates the
CE1/CE2, $N_+=1$, at-least-two-T3-like branch.

$$
\Box
$$
