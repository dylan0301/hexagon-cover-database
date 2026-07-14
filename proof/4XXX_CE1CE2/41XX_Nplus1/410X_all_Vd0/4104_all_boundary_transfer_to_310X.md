# All-Boundary Six-Point Transfer to `310X`

Status: Reduction

This note proves that an all-boundary-covered `410X` configuration supplies
the exact one-supercritical anchored boundary data and finite interior
obstruction set used by the `3101X` six-point strategy. No CE0 property of
the center role is needed for this transfer.

## 1. Hypotheses

Begin with a cover of the full side-one hexagon $H$ by the open center role
$T_C$ and six open Vd0 vertex roles $T_0,\dots,T_5$. Assume exactly one
vertex row is supercritical and that the six vertex roles alone cover

$$
\partial H.
$$

For $T_i$, let $A_i$ be its actual maximal incoming reach on $e_{i-1,i}$,
and let $B_i$ be its actual maximal outgoing reach on $e_{i,i+1}$.

## 2. Strict boundary handoffs

On the relative interior of $e_{i,i+1}$, only the two endpoint V-roles have
positive-length local support. Since the roles are open and cover the whole
edge, their endpoint intervals overlap strictly:

$$
1-A_{i+1}<B_i.
$$

Choose

$$
x_i\in(1-A_{i+1},B_i)
$$

and let $X_i$ be the point of $e_{i,i+1}$ with coordinate $x_i$ measured
from $V_i$. Define the selected local demands at $V_i$ by

$$
a_i=1-x_{i-1},
\qquad
b_i=x_i.
$$

The points $V_i,X_{i-1},X_i$ all lie in the open triangle $T_i$.

If row $i$ is nonsupercritical, then

$$
A_i+B_i\le1.
$$

The strict handoff choices give

$$
x_i<B_i\le1-A_i<x_{i-1},
$$

and hence

$$
a_i+b_i=1-x_{i-1}+x_i<1.
$$

The selected row sums telescope:

$$
\sum_{i=0}^5(a_i+b_i)
=
\sum_{i=0}^5(1-x_{i-1}+x_i)
=6.
$$

Five selected rows are strictly below one, so the remaining selected row is
strictly above one. Thus the handoff data have exactly one supercritical row,
at the same normalized index as the original configuration.

Because the two anchors lie in the same open unit equilateral triangle, their
distance is strictly less than one. In the local $120$-degree coordinates,
this says

$$
a_i^2+a_ib_i+b_i^2<1.
$$

Therefore the selected data avoid the degenerate $\rho=1$ face of the strict
$AB$-union formulas.

## 3. Interior-uncovered points

For each $i$, let $R_i(a_i,b_i)$ be the exact local $AB$-union set: inside
the corner cone of $H$ at $V_i$, it is the union of all closed unit
equilateral triangles containing

$$
V_i,
\qquad
X_{i-1},
\qquad
X_i.
$$

The union sets are defined abstractly in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20090_ab_set_index.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20090_ab_set_index.md).
The strict supercritical frontier for the unique row with $a_i+b_i>1$ is
proved in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).
No formula for the general empirical catalog is used in the transfer below.
Replacing the abstract strict union by that four-piece frontier is therefore
rigorous; the separate optimization targets named below remain unchanged.

The closure of the actual $T_i$ is one of the unit triangles in the defining
union. If a point $P$ lies in both $\mathrm{int}(H)$ and the open triangle
$T_i$, a sufficiently small plane ball about $P$ lies in $T_i$ and in the
interior of the corner cone. Hence

$$
P\in\mathrm{int}(R_i).
$$

Define the plane-interior residual

$$
\mathcal U_6^\circ
=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5\mathrm{int}(R_i).
$$

No point of $\mathcal U_6^\circ$ lies in an open vertex role. The original
hypothesis is a cover of the full hexagon, not merely its boundary or
skeleton, so

$$
\boxed{
\mathcal U_6^\circ\subseteq T_C.
}
$$

This statement deliberately uses $\mathrm{int}(H)$. A boundary point of $H$
can lie on the boundary of a cone-clipped $R_i$ even when it lies in $T_i$,
so an unqualified plane-interior residual on all of $H$ would be too broad.

## 4. Transfer of the six-point reduction

Rotate the unique selected supercritical row to $V_4$ and put

$$
a=a_4,
\qquad
b=b_4.
$$

The handoff construction gives the strict domain

$$
a+b>1,
\qquad
a^2+ab+b^2<1.
$$

The point construction and fixed-line monotonicity proof in
[`../../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3101X_six_point/31012_core_graph_two_variable_relaxation.md`](../../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3101X_six_point/31012_core_graph_two_variable_relaxation.md)
use only the selected handoff data, the five nonsupercritical chain
inequalities, all-Vd0 locality, and the unique strict row. They construct an
actual finite six-point set $K_6^{\mathrm{act}}$ of row-$AB$-union
interior-uncovered points, all lying in $\mathrm{int}(H)$, and prove

$$
\mathrm{conv}\ K_6^{\mathrm{rel}}(a,b)
\subseteq
\mathrm{conv}\ K_6^{\mathrm{act}}.
$$

Every point of $K_6^{\mathrm{act}}$ belongs to $\mathcal U_6^\circ$, so the
full-cover argument above puts it in $T_C$. Convexity gives

$$
K_6^{\mathrm{rel}}(a,b)\subseteq T_C.
$$

The relaxed set is finite and $T_C$ is an open unit equilateral triangle.
Moving the three sides of $T_C$ inward by the minimum positive side margin of
the finite set gives a smaller containing equilateral triangle. Therefore its
minimum enclosing equilateral side length satisfies

$$
F_6(a,b)
:=
\Lambda\left(K_6^{\mathrm{rel}}(a,b)\right)
<1.
$$

The all-boundary-covered `410X` state is consequently reduced to

$$
\boxed{
\text{Target 4104-F:}
\qquad
F_6(a,b)\ge1
}
$$

throughout the strict selected domain. The current `3101X` program targets
the stronger inequality $F_6(a,b)>1$, which is sufficient but remains open.

## 5. Dependency audit

The transfer itself uses no CE0-specific hypothesis. In particular:

- redundant V-boundary coverage supplies the strict handoffs;
- the row-sum telescope supplies the exact one-supercritical pattern;
- the original full-$H$ cover forces every finite interior-uncovered point
  into $T_C$; and
- the strict anchor distances supply the nondegenerate $AB$-union domain.

The transfer does not prove Target `4104-F`. The constant-difference minimum
in `31019`, the transition-curve lower bound, and the global support
partition remain unproved or empirical. Unrestricted fixed-angle or ray
claims with recorded counterexamples cannot be used as substitutes. Thus the
six-point package remains `Strategy`, while the CE-independent transfer
proved here is a `Reduction`.
