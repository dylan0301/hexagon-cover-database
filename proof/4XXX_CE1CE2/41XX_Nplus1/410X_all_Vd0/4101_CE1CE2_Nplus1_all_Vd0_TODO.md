# CE1/CE2, $N_+=1$, All Vd0: Exact Gap Strategy

Status: Strategy

This note records the strongest current rigorous reduction for the `410X`
branch. It does not claim that the branch, `310X`, skeleton noncoverage, or
the main theorem is proved.

## Package progress

| File | Recorded status | Role |
|---|---|---|
| [`4101_CE1CE2_Nplus1_all_Vd0_TODO.md`](4101_CE1CE2_Nplus1_all_Vd0_TODO.md) | Strategy | Exact setup, case ledger, and remaining obligations. |
| [`4102_CE2_two_gap_completion.md`](4102_CE2_two_gap_completion.md) | Proven | Eliminates the CE2 two-gap state by importing the proved endpoint inequality from `401c` and `401e`. |
| [`4103_one_gap_five_map_reduction.md`](4103_one_gap_five_map_reduction.md) | Reduction | Reduces CE1 and CE2 exactly-one-gap states to three explicit five-map targets and records exact shortcut failures. |
| [`4104_all_boundary_transfer_to_310X.md`](4104_all_boundary_transfer_to_310X.md) | Reduction | Proves the all-boundary handoff and finite-point transfer to the strict six-point $F_6$ target. |
| [`4106_CE1_one_gap_five_map_completion.md`](4106_CE1_one_gap_five_map_completion.md) | Proven | Proves Target `4103-CE1` by a three-map dual reduction and an exact Bernstein terminal certificate. |
| [`4107_CE2_one_gap_five_map_completion.md`](4107_CE2_one_gap_five_map_completion.md) | Proven | Proves Targets `4103-CE2-R` and `4103-CE2-L`, including the complete reflected map order. |
| [`4108_ce1_terminal_verifier.py`](4108_ce1_terminal_verifier.py) | Experiment | Reconstructs the exact rational Bernstein tensors used in `4106`. |

## 1. Exact starting formulation

Begin with a hypothetical cover of the full side-one hexagon $H$ by seven
open unit equilateral triangles. This is not a skeleton-only hypothesis.

The equivalent expanded closed formulation is that, for every $L>1$, the
expanded hexagon $H_L$ is not covered by seven closed unit equilateral
triangles. The equivalence and strictness transfer are proved in
[`../../../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md`](../../../1XXX_foundations/10XX_global_conventions/1003_open_unit_vs_shrunken_closed_equivalence.md).

Choose one role $T_C$ that contains $O$ in its interior and six vertex roles
$T_0,\dots,T_5$. Close the open triangles for the local compact calculations;
do not discard the original interior condition at $O$.

Assume

$$
T_C\text{ is CE1 or CE2},
\qquad
N_+=1,
$$

and every $T_i$ is Vd0.

The corrected exactly-one-midpoint theorem
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md)
gives

$$
T_C\cap\left\{M_0,\dots,M_5\right\}=\left\{M_0\right\}
$$

after cyclic normalization. The hypothesis $O\in\mathrm{int}(T_C)$ is
essential; without it, $\mathrm{conv}\{O,V_0,V_1\}$ is a closed
two-midpoint counterexample.

## 2. Exact center data and radial relaxation

For CE1, use the exact domain, boundary interval, six radial exits, and six
demands in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2105_CE1_exact_formulas.md).

For CE2, use the coupled interval-pair domain and exact radial data in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md).

In either case, let $d_i$ be the exit distance of $T_C$ from $O$ toward
$V_i$, and set

$$
c_i=1-d_i.
$$

This inequality direction follows from convexity. If the actual radial reach
of $T_i$ from $V_i$ is $\widehat c_i$, full coverage of the radial arm gives

$$
\widehat c_i\ge1-d_i=c_i.
$$

If $c'\ge c$, a triangle containing the radial demand point at $c'$ also
contains the point at $c$, because the latter lies on the segment from $V_i$
to the former. Hence lowering $\widehat c_i$ to $c_i$ enlarges the feasible
row set. This is the precise monotonicity relaxation.

Since $M_i\notin T_C$ for $i\ne0$, all-Vd0 radial locality forces $M_i$ into
$T_i$ for those five indices. The proved midpoint self-cover lemma gives

$$
a_i+b_i\le1,
\qquad i\ne0.
$$

Therefore the unique supercritical row is

$$
\boxed{T_0.}
$$

Point-only contacts are handled by the usual finite closed-cover limit
argument; they do not replace a missing positive radial interval.

## 3. Proof-safe row maps

The exact unclassified demand map is the piecewise support-contact map

$$
B_c(a)=
\max_{\substack{0\le b\le1\\ {}(a,b,c)\in\mathcal A}}b
$$

from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md).
It is nonincreasing in $a,c$, and

$$
g_c(a)=1-B_c(a)
$$

is nondecreasing.

The old unselected list of algebraic candidates is not valid. In particular,
it accepted a fake high-$c$ component at

$$
a=\frac5{12},
\qquad
c=\frac{27}{28},
$$

where its candidate was $9/20$ although the exact formula gives

$$
B_{27/28}\left(\frac5{12}\right)
=
\frac{27(14-\sqrt{141})}{784}
<\frac9{20}.
$$

For the $N_+=1$ classification, demands and actual row reaches must not be
identified. Let

$$
B_i^0(x)=B_{c_i}^{\mathcal R_0}(x),
\qquad i\ne0,
$$

where $\mathcal R_0$ is the class of actually nonsupercritical Vd0 triangles,
and let

$$
B_0^+(x)=B_{c_0}^{\mathcal R_+}(x)
$$

for the actually supercritical Vd0 class. Define

$$
g_i(x)=1-B_i^0(x)
\quad(i\ne0),
\qquad
g_0(x)=1-B_0^+(x).
$$

Every $g_i$ is nondecreasing by feasible-set inclusion. If a classified map
is undefined, that row requirement is impossible. The unrestricted map is a
safe relaxation because

$$
B_i^0(x)\le B_{c_i}(x),
\qquad
B_0^+(x)\le B_{c_0}(x),
$$

but it does not encode the one-supercritical-row condition.

Two proved upper relaxations now encode the row classes safely. For
$i\ne0$, the capped-map theorem in
[`2011_capped_demand_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2011_capped_demand_map.md)
gives

$$
B_i^0(x)
\le
\min\left\{B_{c_i}(x),1-x\right\}.
$$

Write

$$
\widehat B_c(x)=\min\left\{B_c(x),1-x\right\}.
$$

For the strict-supercritical row, the free envelope in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2010_free_supercritical_max_b.md)
gives, for $c_0<1/2$,

$$
B_0^+(x)
\le
\min\left\{
B_{c_0}(x),
\frac{c_0+\sqrt{c_0^2-8c_0+4}}2
\right\}.
$$

The strict-supercritical feasible set is empty for $c_0\ge1/2$. These bounds
are sufficient for the exact reductions in `4103`; they are not asserted to
be exact classified maps.

## 4. Boundary recurrence and V-gaps

On $e_{i,i+1}$, parameterized from $V_i$, the adjacent vertex roles cover

$$
[0,b_i]
\qquad\text{and}\qquad
[1-a_{i+1},1].
$$

A V-gap exists exactly when

$$
b_i<1-a_{i+1}.
$$

If a center interval on this edge is

$$
I=[s,t]
$$

and contains the gap, full boundary coverage gives

$$
s\le b_i<1-a_{i+1}\le t.
$$

Therefore

$$
b_i\ge s,
\qquad
a_{i+1}\ge1-t.
$$

Now suppose a row has incoming lower bound $x$. Its outgoing reach is at most
$B_i(x)$, so boundary coverage forces the next incoming lower bound to be at
least

$$
1-B_i(x)=g_i(x).
$$

This proves the recurrence. Replacing the actual gap by all of $I$ changes
the start only from its true value to the weaker value $1-t$, and changes the
target only to the weaker value $1-s$. Because every $g_i$ is nondecreasing,
the replacement is a valid relaxation.

No nonlocal Vd0 row invalidates the recurrence: a Vd0 role has no
positive-length intersection with either adjacent radial arm, and on a
boundary edge only its two endpoint roles have positive-length local support.

## 5. CE1 split

Normalize

$$
T_C\cap e_{0,1}=[s,t].
$$

### CE1 with no V-gap

If the adjacent vertex reaches already cover $[s,t]$, the six V-triangles
cover all of $\partial H$. This is an all-boundary-covered case. It is not a
$g$-chain contradiction by itself and is sent to the proved reduction in
Section 8.

### CE1 with a V-gap

Starting at $T_1$ and propagating counterclockwise gives the necessary
condition

$$
\boxed{
(g_0\circ g_5\circ g_4\circ g_3\circ g_2\circ g_1)(1-t)
\le1-s.
}
$$

The reflected clockwise propagation gives

$$
\boxed{
(g_1\circ g_2\circ g_3\circ g_4\circ g_5\circ g_0)(s)
\le t.
}
$$

Both are necessary. The stronger common-realization reduction and the exact
five-map target are proved in
[`4103_one_gap_five_map_reduction.md`](4103_one_gap_five_map_reduction.md),
and the terminal target is proved in
[`4106_CE1_one_gap_five_map_completion.md`](4106_CE1_one_gap_five_map_completion.md).

## 6. CE2 exhaustive split

Write

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v],
$$

with both parameters measured from $V_0$. The canonical counterclockwise
interval on $e_{5,0}$ is

$$
[1-u,1-x].
$$

### Neither interval has a V-gap

The V-triangles cover all of $\partial H$. Use Section 8.

### Exactly one interval has a V-gap

If the active interval is $[y,v]\subset e_{0,1}$, the necessary conditions
are

$$
(g_0\circ g_5\circ g_4\circ g_3\circ g_2\circ g_1)(1-v)
\le1-y,
$$

and

$$
(g_1\circ g_2\circ g_3\circ g_4\circ g_5\circ g_0)(y)
\le v.
$$

If the active interval is $[1-u,1-x]\subset e_{5,0}$, they are

$$
(g_5\circ g_4\circ g_3\circ g_2\circ g_1\circ g_0)(x)
\le u,
$$

and

$$
(g_0\circ g_1\circ g_2\circ g_3\circ g_4\circ g_5)(1-u)
\le1-x.
$$

The exact survivor splits and the two reflected five-map targets are recorded
in `4103`, and both targets are proved in
[`4107_CE2_one_gap_five_map_completion.md`](4107_CE2_one_gap_five_map_completion.md).
The two-adjacent-row shortcut from `401X` is not globally valid; `4103` gives
exact CE1 and CE2 witnesses.

### Both intervals have V-gaps

This state is proved impossible in
[`4102_CE2_two_gap_completion.md`](4102_CE2_two_gap_completion.md). The two
far-end inputs involve only $T_1$ and $T_5$, and the exact endpoint theorem
from proved `401c` and `401e` gives

$$
\widehat B_{c_5}(1-u)
+
\widehat B_{c_1}(1-v)
<1.
$$

The resulting four-edge boundary remainder has length greater than three,
contradicting the row caps for $T_2,T_3,T_4$. The supercritical row $T_0$
does not occur in this argument.

## 7. Independent CE2 two-gap skeleton replacement

The proved replacement theorem
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2104_CE2_one_interval_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2104_CE2_one_interval_lemma.md)
shows that a two-gap all-Vd0 CE2 skeleton system is not replacement-maximal.

The one-sided complementary corner triangles

$$
\Delta(u,b_0)
\qquad\text{and}\qquad
\Delta(a_0,v)
$$

have side at most one, cover the radial demand $xy/(x+y)$, preserve the old
boundary reaches, and fill the left or right CE2 interval respectively.

The strengthened theorem also gives the single simultaneous replacement

$$
\Delta(u,v).
$$

After homothetic unit enlargement, its actual boundary reaches are

$$
\frac uL,
\qquad
\frac vL,
\qquad
L=\sqrt{u^2+uv+v^2}\le1.
$$

It is Vd0 and strictly supercritical because

$$
\frac{u+v}{L}>1.
$$

Thus the simultaneous replacement fills both gaps and lands exactly in the
all-boundary-covered CE2, $N_+=1$, all-Vd0 skeleton state. There are no
unclassified V-type or $N_+$ exits.

It still does not follow from bare supercriticality that the original $T_0$
binds an endpoint. More importantly, the replacement is proved to preserve
the skeleton, not the full interior cover of $H$. Therefore it does not by
itself complete a full-cover branch. It is no longer needed for the CE2
two-gap `410X` subcase, which is proved directly in `4102` without replacing
the original roles.

## 8. Proven all-boundary-covered reduction

If no center interval contains a V-gap, the six vertex roles cover every
boundary edge. Select a boundary handoff point $X_i$ on each edge and write

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

The strict handoff construction and full-cover transfer are proved in
[`4104_all_boundary_transfer_to_310X.md`](4104_all_boundary_transfer_to_310X.md).
It supplies exactly one selected supercritical row, five strictly
nonsupercritical rows, strict nondegenerate anchor distances, and the
inclusion of the finite six-point interior obstruction set in $T_C$. No CE0
property of the center role is needed.

This is a proved reduction, not a completed obstruction. Its terminal
inequality

$$
F_6(a,b)\ge1
$$

remains open. The `3101X` six-point package targets the stronger sufficient
inequality $F_6(a,b)>1$.

## 9. Counterexample and numerical warnings

The `908X` numerical skeleton cover is not a `410X` counterexample. Direct
floating-point classification of its recorded coordinates gives

$$
T_C\text{ of type CE0},
\qquad
N_+=1,
$$

with all six vertex roles Vd0. Its center role contains two midpoints and has
no boundary interval. This classification is empirical because the source
coordinates are floating point.

The old visual `maps.ts` predicate used the raw Cell-2 polynomial and accepted
the fake high-$c$ component exposed by `2007`. Numerical scans based on that
predicate are not proof-valid. Adding the selector

$$
c\le2\max(a,b)
$$

removes that particular sheet error, but still does not prove candidate
attainment or branch completeness inside the old visual code. A proof-level
scan must evaluate the exact piecewise map in `2007`, evaluate the equivalent
support minimum, or use a certified upper relaxation.

The exact local example in `2104` also shows that supercriticality does not
force the original $T_0$ to fill either CE2 interval. This is a counterexample
to that proposed inference, not to the replacement theorem and not to the full
`410X` obstruction.

## 10. Remaining proof obligation

The CE1 and CE2 exactly-one-gap targets are proved in `4106` and `4107`.
Together with the CE2 two-gap proof in `4102`, this closes every state in
which a center interval contains a V-gap.

The full `410X` branch remains open only at Target `4104-F`: prove

$$
F_6(a,b)\ge1
$$

on the strict selected domain, or prove the stronger existing `3101X`
target. The overall package remains `Strategy` because `4104-F` is a named
open terminal target.
