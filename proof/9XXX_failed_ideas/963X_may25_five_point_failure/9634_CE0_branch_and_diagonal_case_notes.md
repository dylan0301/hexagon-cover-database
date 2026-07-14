# Branch and Diagonal Case Notes

Status: Strategy

This file records the main branch-selection and diagonal-cut issues in the
May 25 five-point conjecture.

## $P_3$ and $P_5$ branch selection

The points $P_3$ and $P_5$ are selected from intersections of the non-axis
boundary of $R_4$ with radius-$1$ circles:

$$
C_2=\partial B(X_2,1),\qquad C_5=\partial B(X_5,1).
$$

The selected $P_3$ branch is the non-axis intersection between $\partial R_4$
and $C_2$ closest to $V_4$.  The selected $P_5$ branch is the analogous
intersection with $C_5$.

The nondegenerate strict $AB$-union frontier formula for $\partial R_4$ is
now proved in
[../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md](../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).

The local $R(a,b)$ predicate in `9632_CE0_reduction_prompt_spec.md` gives a
semialgebraic way to test candidate intersections.  A branch proof must show
more than the existence of an algebraic root: it must verify that the root lies
on the active non-axis boundary piece, satisfies the relevant inequalities, and
is the closest valid branch to $V_4$.

## Line-piece realization target

The May 30 working prompt proposes the following branch-realization target:
for the reduced May 25 slice, the selected intersections defining $P_3$ and
$P_5$ should occur on the line-segment pieces

$$
\Gamma_A^{\mathrm{lin}}\cup\Gamma_B^{\mathrm{lin}}
$$

of the strict $AB$-union frontier for $R_4$, not on the unit-circle arc
pieces.  This is a proof target, not a proved assertion in this package.

To certify this target, one must check the intersections of $C_2$ and $C_5$
with all four frontier pieces from
`../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md`.  For each
selected point the proof must show:

1. a valid intersection lies on one of the two closed line segments;
2. the point satisfies the active $R_4$ boundary conditions and segment
   parameter bounds;
3. every valid arc intersection is absent, farther from $V_4$, or belongs to a
   separated tangent or endpoint case;
4. the selected line-piece point is the closest valid non-axis branch to
   $V_4$.

Endpoint contacts at the junction points of the four-piece curve, circle
tangencies, and the limiting degeneration $\rho_4=a_4^2+a_4b_4+b_4^2=1$
should be treated as boundary cases before using a strict line-piece argument.

## Undefined branch cases

The five-point configuration is undefined if either selected intersection does
not exist.  Such cases should not be counted as counterexamples to the May 25
conjecture, because the conjecture is only stated for parameter choices where
all five points are defined.

Tangent intersections need separate handling.  They may belong to the defined
boundary case if the selected point is still well-defined, but they should not
be folded into a strict branch argument without checking the active
inequalities.

## Diagonal endpoints

Let

$$
U=H\setminus\bigcup_{i=0}^5 R_i.
$$

If $O\notin U$, then the five-point configuration is undefined.  Otherwise

$$
D_j=\rho_jV_j,\qquad j=0,1,2,
$$

where

$$
\rho_j=\sup\{\rho\in[0,1]: \lambda V_j\in U \text{ for every }0\le\lambda<\rho\}.
$$

Thus $D_j$ is determined by the first cut of the half-diagonal $[O,V_j]$ by
the union of all six $R_i$, not only by the local region adjacent to $V_j$.

This is the main change from the May 21/22 four-point radial construction.
The May 25 definition avoids committing to a fixed local radial point or a
preassigned Vd1/Vd2-type local pattern.  The point $D_j$ follows the actual
initial uncovered interval, so a nonlocal cut is part of the definition rather
than an exceptional failure mode.

Two common cases are:

1. No $R_i$ cuts $[O,V_j]$ before $V_j$.  Then $D_j=V_j$.
2. Some $R_i$ cuts $[O,V_j]$ before $V_j$.  Then $D_j$ is the first boundary
   point of $U$ along the ray from $O$ to $V_j$.

The source prompt emphasizes that a region such as $R_2$ may cut
$[O,V_1]$ before the usual radial point.  Such cross-cuts are part of the
definition and must be included in any proof.

## Proof strategy note

A useful implementation of the proof target should treat each $D_j$ as a
minimum over all valid cuts of the corresponding half-diagonal:

$$
\rho_j=\min\{1,\rho_{0j},\rho_{1j},\dots,\rho_{5j}\},
$$

where $\rho_{ij}$ denotes the first valid intersection of $R_i$ with
$[O,V_j]$, if it exists.  This formula is only a strategy notation here; each
$\rho_{ij}$ still requires a branch-realization proof from the exact local
predicate.

The May 30 working prompt suggests a one-dimensional shortcut for these
endpoint realizations.  For fixed $j$, compute the closest valid cut of
$[O,V_j]$ caused by each region that can meet this half-diagonal, with special
attention to the neighboring regions $R_{j-1}$ and $R_{j+1}$, and compare
those cut radii with the local maximal radial reach of $R_j$.  If this
comparison proves that no omitted region produces a smaller valid cut, then it
certifies the same value of $\rho_j$ without explicitly constructing the full
$a+b\le1$ $AB$-union frontier.

This shortcut is only a proof strategy.  A finished argument still has to
verify each candidate cut against the exact local predicate, prove the
candidate is the first cut from $O$, and separate the case in which no cut
occurs before $V_j$, giving $D_j=V_j$.

## Five-point enclosing-triangle contact roadmap

The remaining enclosing-triangle certificate should reduce the support-contact
regimes for

$$
K_5=\{P_3,P_5,D_0,D_1,D_2\}
$$

to a finite list of inequalities.  The May 30 working target is that, in the
generic contact regime, $P_3$ and $P_5$ lie on different supporting sides of a
minimal enclosing equilateral triangle, while $D_1$ lies on the remaining
supporting side.

The next split is whether $D_0$ or $D_2$ supplies an additional side contact.
When a symmetry or separate comparison justifies taking $D_0$ as the active
one, the remaining generic subcases are:

1. $D_0$ lies on the same supporting side as $D_1$;
2. $D_0$ lies on the same supporting side as $P_5$.

The reflected alternatives with $D_2$ active must be included unless they are
explicitly removed by a proved symmetry or monotonicity argument.  Cases in
which both $D_0$ and $D_2$ lie on supporting sides are boundary or tight-case
obligations, not generic cases to discard.  The prompt suggests that some such
cases may be perturbable unless the six boundary points are close to the
hexagon vertices, but that perturbation claim remains a proof obligation here.
