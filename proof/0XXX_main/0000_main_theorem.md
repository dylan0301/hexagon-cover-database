# Main Theorem

Status: Proven

## Theorem

The regular side-$1$ hexagon $H$ cannot be covered by seven open unit
equilateral triangles. Equivalently, for every $L>1$, the regular side-$L$
hexagon $H_L$ cannot be covered by seven closed unit equilateral triangles.

The equivalence is proved in
[`1003`](../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

## Proof

Assume that seven open unit equilateral triangles cover $H$. Denote the
original open triangles by

$$
U_C,U_0,\dots,U_5,
$$

where $O\in U_C$ and $V_i\in U_i$, and put

$$
T_C=\overline{U_C},
\qquad
T_i=\overline{U_i}.
$$

The center $O$
and vertices $V_0,\dots,V_5$ are pairwise at distance at least $1$, whereas
two points in one open unit triangle are at distance strictly below $1$.
Each triangle therefore covers at most one distinguished point. Since seven
triangles cover all seven points, the displayed assignment gives their
distinct roles. Apply the exact-trace normalization in
[`1201`](../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md) to every
raw $(o,n)=(3,0)$ vertex role, and relabel the translated open role and its
closure as $U_i,T_i$. This preserves its intersection with $H$ exactly, keeps
$V_i$ in the open role, and leaves all actual reaches unchanged. Thus the
normalized roles still form a cover. Apply the proved classifications to the
closed triangles $T_C,T_i$, retaining $U_C,U_i$ whenever openness or open
membership is used.
By [`1101`](../1XXX_foundations/11XX_C_triangle/1101_CE_classification.md),
$T_C$ is exactly one of CE0, CE1, and CE2. By
the normalized classification in `1201`, every vertex role is exactly one of
Vd0, Vd1, Vd2, and T3-like.

Let $(A_i,B_i)$ be the actual maximal boundary reaches of $T_i$ and set

$$
N_+
=
\left\lvert
\left\lbrace i:A_i+B_i>1\right\rbrace
\right\rvert.
$$

For the vertex-type refinement, put

$$
d=
\left\lvert
\left\lbrace i:T_i\text{ is Vd1 or Vd2}\right\rbrace
\right\rvert,
\qquad
t=
\left\lvert
\left\lbrace i:T_i\text{ is T3-like}\right\rbrace
\right\rvert,
$$

so $N_{\rm sp}=d+t$. Let $N_{\rm gap}$ be the number of positive
C-triangle boundary traces containing a boundary set missed by the two
incident open V triangles; singleton missed sets count as gaps. Boundary
locality and openness give

$$
N_{\rm gap}=0
\quad\Longleftrightarrow\quad
U_0,\ldots,U_5\text{ cover }\partial H.
\tag{1}
$$

When a branch selects smaller strict handoffs,
[`1214`](../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
rigorously transfers the required supercritical pattern from the actual
reaches. It remains only to list the gap-first terminal cases.

### Zero boundary gaps

By (1), the six V roles alone cover the perimeter. The center type therefore
plays no part in this branch.

| $N_+$ | $(d,t)$ | Proven contradiction |
|---:|---|---|
| $0$ | any | V-only strict boundary overlap in [`2500`](../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md) |
| $1$ | $d\ge1$ | V-only boundary-length deficit in `2500` |
| $1$ | $d=0$, $t\ge1$ | Boundary-complete T3-like area certificate [`3174`](../3XXX_CE0/31XX_Nplus1/317X_T3_like_no_Vd1Vd2/3174_CE0_one_supercritical_T3_certificate.md) |
| $1$ | $(d,t)=(0,0)$ | Center-independent nine-point obstruction [`31058`](../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md) |
| $\ge2$ | any | Boundary-complete cyclic area certificate [`3208`](../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md) |

These rows are disjoint and exhaustive.  In the three-strategy numbering they
use Strategy 1 for trace length, Strategy 2 for area loss, and Strategy 3 for
finite enclosure.

### Nonzero boundary-gap count

A nonzero gap count forces the center to be CE1 or CE2. The common skeleton theorem
in
[`2530`](../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
states that $N_++N_{\rm sp}\ge3$ gives a strict deficit on the length-$12$
skeleton. If $N_+\ge2$, midpoint rescue forces a further positive-support
role, so $N_{\rm sp}\ge1$ and that theorem applies. Thus it remains to take
$N_+\in\{0,1\}$ and, after the same direct pruning,
$N_++d+t\le2$.

| $N_+$ | $(d,t)$ | Center | Proven contradiction |
|---:|---|---|---|
| $0$ | $(0,0)$ | CE1/CE2 | Finite residual-hull enclosure [`4013_new`](../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md) |
| $0$ | $d\ge1$ | CE1/CE2 | Boundary-length obstructions [`4040`](../4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4040_CE1_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md), [`4041`](../4XXX_CE1CE2/40XX_Nplus0/404X_exists_Vd1_Vd2_obstruction/4041_CE2_Nplus0_exists_Vd1_Vd2_boundary_length_obstruction.md) |
| $0$ | $(0,1)$ or $(0,2)$ | CE1/CE2 | Finite residual-hull enclosure [`4070_new`](../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md) |
| $1$ | $(0,0)$ | CE1/CE2 | Finite residual-hull enclosure [`4101_new`](../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4101_new_all_Vd0_finite_enclosure.md) |
| $1$ | $(0,1)$ | CE1/CE2 | Finite residual-hull enclosure [`4130_new`](../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md) |
| $1$ | $(1,0)$ | CE1 | Boundary obstruction [`4110`](../4XXX_CE1CE2/41XX_Nplus1/411X_Vd1_Vd2_obstruction/4110_CE1_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md) |
| $1$ | $(1,0)$ | CE2 | Finite residual-hull assembly [`4140_new`](../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md) |

The preceding high-count pruning and the displayed rows exhaust the
nonzero-gap branch.  The old reach calculations remain exact certificates
inside the new finite-enclosure packages, but they own no separate strategy.
Hence every gap rank leads to a contradiction, so seven open unit equilateral
triangles cannot cover $H$. The equivalence in `1003`
gives the closed expanded-hexagon formulation. $\square$
