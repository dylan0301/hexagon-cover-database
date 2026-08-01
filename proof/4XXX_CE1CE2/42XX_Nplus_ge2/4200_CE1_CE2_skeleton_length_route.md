# CE1/CE2, $N_+\ge2$, Skeleton-Length Obstruction

Status: Proven

Assume the center role is CE1 or CE2, contains $O$ in its interior, and at
least two vertex V triangles are supercritical.

The midpoint-forcing lemma in
[`2510`](../../2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md)
shows that at least one further vertex role must rescue a missing midpoint and
therefore has positive-length support on an adjacent radial arm.  Thus the
configuration has at least three short vertex roles in the terminology of
[`2530`](../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md):

- two supercritical V triangles;
- one positive-support rescuer.

The three-short-role theorem in `2530` gives

$$
L_S(T_C)+\sum_{i=0}^5L_S(T_i)<12.
$$

The full hexagon skeleton has length $12$, so a cover would imply the opposite
weak inequality by subadditivity.  This contradiction eliminates every
CE1/CE2 branch with $N_+\ge2$.

$$
\Box
$$
