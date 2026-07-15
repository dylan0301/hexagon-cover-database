# CE1/CE2, $N_+=1$, All Vd0: Exact Gap Strategy

Status: Strategy

This index gives the complete case split for `410X`.  Every state containing
a V-gap is proved impossible.  The only open terminal target is the
all-boundary six-point inequality `4104-F`; consequently this package does
not claim that `410X`, `310X`, or the main theorem is proved.

## Package ledger

| File | Status | Role |
|---|---|---|
| [`4101_CE1CE2_Nplus1_all_Vd0_strategy.md`](4101_CE1CE2_Nplus1_all_Vd0_strategy.md) | Strategy | Hypotheses, exhaustive gap split, and the one open target. |
| [`4102_CE2_two_gap_completion.md`](4102_CE2_two_gap_completion.md) | Proven | Excludes the CE2 state in which both center intervals contain V-gaps. |
| [`4104_all_boundary_transfer_to_310X.md`](4104_all_boundary_transfer_to_310X.md) | Reduction | Transfers the no-gap state to the strict six-point target `4104-F`. |
| [`4106_CE1_one_gap_five_map_completion.md`](4106_CE1_one_gap_five_map_completion.md) | Proven | Excludes the CE1 one-gap state by an exact five-map inequality and Bernstein certificate. |
| [`4107_CE2_one_gap_five_map_completion.md`](4107_CE2_one_gap_five_map_completion.md) | Proven | Excludes both reflected CE2 one-gap states. |
| [`4108_ce1_terminal_verifier.py`](4108_ce1_terminal_verifier.py) | Experiment | Reconstructs the exact rational Bernstein tensors used in `4106`. |

## 1. Hypotheses and the unique supercritical row

Assume that seven open unit equilateral triangles cover the full side-one
hexagon $H$.  Choose an open center role $T_C$ containing $O$ and six Vd0
vertex roles $T_0,\dots,T_5$.  Assume

$$
T_C\text{ is CE1 or CE2},
\qquad
N_+=1.
$$

Closing the triangles for compact local calculations is justified by the
strictness transfer in
[`../../../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md`](../../../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

The exactly-one-midpoint theorem
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
allows the normalization

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\}.
$$

For $i\ne0$, radial locality therefore puts $M_i$ in $T_i$.  The midpoint
self-cover theorem
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2005_midpoint_self_cover_lemma.md)
gives

$$
a_i+b_i\le1,
\qquad i\ne0.
$$

Since $N_+=1$, the unique supercritical row is $T_0$.

Let $d_i$ be the center role's radial exit toward $V_i$ and put

$$
c_i=1-d_i.
$$

Convexity of radial intersections shows that the actual radial reach of
$T_i$ is at least $c_i$.  Lowering the actual demand to $c_i$ enlarges the
feasible row set, so it is a valid relaxation.

For every nonsupercritical row $i\ne0$, define

$$
F_i(a)=\min\{B_{c_i}(a),1-a\},
\qquad
G_i(a)=1-F_i(a).
$$

The exact map $B_c$ is proved in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md),
and the capped relaxation and monotonicity of $G_i$ are proved in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md).

## 2. Boundary gaps

On $e_{i,i+1}$, measured from $V_i$, the adjacent vertex roles cover the
intervals

$$
[0,b_i]
\qquad\text{and}\qquad
[1-a_{i+1},1].
$$

Their uncovered open interval is a V-gap, and it exists exactly when

$$
b_i<1-a_{i+1}.
$$

If a center interval $[s,t]$ contains that gap, full boundary coverage forces

$$
b_i\ge s,
\qquad
a_{i+1}\ge1-t.
$$

The center formulas and all of their strict domains are proved in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md)
and
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md).

## 3. Exhaustive CE1 split

A CE1 role has one boundary interval, normalized to

$$
T_C\cap e_{0,1}=[s,t].
$$

- If the interval contains a V-gap, `4106` propagates the five
  nonsupercritical capped maps from $1-t$ and proves that the resulting lower
  bound for $a_0$ is strictly greater than the exact upper bound allowed by
  the same $T_0$ with $b_0\ge s$.  This is a contradiction.
- If it contains no V-gap, the vertex roles cover that interval.  Outside the
  center interval the original full cover and Vd0 boundary locality already
  force coverage by the vertex roles.  Hence the six vertex roles cover all
  of $\partial H$, and `4104` applies.

These two alternatives are exhaustive.

## 4. Exhaustive CE2 split

Normalize the two center intervals as

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v],
$$

with both coordinates measured from $V_0$.  Each interval either contains a
V-gap or does not, so exactly one of the following occurs.

1. Both contain gaps.  `4102` proves this impossible by the strict
   two-endpoint capped-loss inequality.
2. Exactly one contains a gap.  `4107` proves the right-gap five-map
   inequality on the full strict CE2 domain; reflection across the axis
   through $V_0$ gives the left-gap inequality.  Both orientations are
   impossible.
3. Neither contains a gap.  The six vertex roles cover both center intervals
   and, by the same locality argument as in CE1, all of $\partial H$.
   Therefore `4104` applies.

Thus every CE2 state containing a V-gap is closed.

## 5. The only open target

In the remaining no-gap state, the six vertex roles cover $\partial H$.
The strict handoff construction in `4104` produces one selected
supercritical row, five selected strictly nonsupercritical rows, and a finite
six-point set that must lie in $T_C$.  It reduces the state to

$$
\boxed{
\text{Target 4104-F:}\qquad F_6(a,b)\ge1
}
$$

on the strict selected domain

$$
a+b>1,
\qquad
a^2+ab+b^2<1.
$$

This inequality is not proved.  The stronger `3101X` target $F_6(a,b)>1$ is
also open.  Therefore `410X` remains `Strategy`, and `4104-F` is its sole
terminal obligation.
