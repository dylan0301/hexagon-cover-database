# Original May 21/22 Prompt Context

Status: Strategy

This file records the additional prompt context from `hexagon-cover-visual/prompts/20260521conjecture.txt` and `hexagon-cover-visual/prompts/20260522quadTriangle.txt` in repository notation.  It is not itself a proof.

## 1. Starting assumption

Assume the global covering problem has been reduced to a case with exactly one $V$-triangle satisfying

$$
a_i+b_i>1.
$$

By rotation, take this strict vertex to be $V_4$.

The desired constrained reduction is

$$
a_4+b_4>1,
$$

$$
a_1+b_1=a_3+b_3=a_5+b_5=1,
$$

and

$$
a_0+b_0\le1,\qquad a_2+b_2\le1.
$$

Writing

$$
p=t_0=t_1,\qquad q=t_2=t_3,\qquad r=t_4=t_5,
$$

this becomes

$$
q<r, \qquad q\le p\le r.
$$

The equality reduction for $a_1+b_1=1$ was originally less certain than the equalities at $V_3,V_5$.  The five-point variant recorded in the alternate strategy adds the point $G_1$ to avoid assuming $a_1+b_1=1$.

## 2. Sector-enlarged idea for $V_3,V_5$

The original visualization prompt proposes replacing the ordinary AB-union set at $V_3$ and $V_5$ by slightly larger auxiliary sets.

For $V_3$, draw the radius-$1$ circle centered at $X_2$.  The intended auxiliary sector starts on the edge $V_3V_4$ and continues until the diagonal $OV_4$ in the visualization idea.

For $V_5$, draw the analogous radius-$1$ circle centered at $X_5$.

However, the later instruction says not to clip these circles by a hexagon diagonal for the four-point construction.  The points $P_3$ and $P_5$ should be defined as intersections of the non-axis curved boundary of the $V_4$ AB-union region with the full circles centered at $X_2$ and $X_5$.

Thus the mathematical version used in this package is:

$$
P_3\in \partial R_4\cap C_2, \qquad P_5\in \partial R_4\cap C_5,
$$

where $C_2$ and $C_5$ are full radius-$1$ circles, and the boundary is the non-axis curved boundary of $R_4$, not a hexagon edge and not a coordinate axis.

The nondegenerate strict $AB$-union frontier formula for this boundary is now
proved in
[../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md](../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).

## 3. Monotonicity intuition

The prompt intuition is:

- if $X_4$ moves toward $V_4$, the relevant $V_4$ AB-boundary curve moves closer to $V_4$;
- if $X_3$ moves toward $V_4$, the analogous effect occurs from the other side;
- the four-point enclosing equilateral triangle should be minimized when $X_3$ and $X_4$ are as close to $V_4$ as allowed;
- this leads to the equality conditions

$$
a_3+b_3=1, \qquad a_5+b_5=1.
$$

The current repository package does not prove this original global monotonicity claim.  It starts after the constrained slice has been imposed and studies the resulting Pattern A four-point problem.

## 4. Four-point obstruction

The four-point obstruction points are:

1. $P_3$, the selected non-axis $R_4$-boundary point on the circle centered at $X_2$;
2. $P_5$, the selected non-axis $R_4$-boundary point on the circle centered at $X_5$;
3. $G_0$, the radial max-$c$ point on $OV_0$ for the local admissible set at $V_0$;
4. $G_2$, the radial max-$c$ point on $OV_2$ for the local admissible set at $V_2$.

The Pattern A support case is the contact configuration

$$
(S_0,S_1,S_2)=\bigl(\{G_2\},\{P_3,P_5\},\{G_0\}\bigr).
$$

The scalar reduction for this case is recorded in `621_setup_and_patternA_reduction.md`.

## 5. Midpoint-window alternative

The May 22 prompt also suggests splitting into cases depending on whether every edge point lies near the midpoint, for example

$$
t_i\in[0.4,0.6]\qquad\text{for all }i.
$$

The proposed midpoint-window strategy is to use only the local admissible-set constraints at the six $V_i$-triangles to prove that the remaining skeleton cannot be covered.

A smaller proven window was found in exploratory work:

$$
t_i\in\left[\frac9{20},\frac{11}{20}\right]
$$

forces all radial residual points beyond radius $19/50$, so the six residual radial points cannot fit into a unit equilateral triangle.  This is not recorded here as part of the Pattern A proof.

## 6. Five-point variant

To avoid assuming

$$
a_1+b_1=1,
$$

the prompt proposes using five points

$$
P_3,\quad P_5,\quad G_0,\quad G_1,\quad G_2.
$$

This five-point target is recorded as a strategy direction, not as a completed proof.  It requires the nonemptiness condition

$$
r^2+r(1-q)+(1-q)^2\le1
$$

for $R_4$ and a separate support-pattern analysis for five points.

## 7. Relation to the quadrilateral lemma

The May 22 prompt states the minimal enclosing equilateral triangle lemma for convex quadrilaterals.  The repository version is recorded as

`proof/2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2607_minimal_enclosing_equilateral_quadrilateral_lemma.md`.

That lemma is used to justify reducing the four-point problem to finitely many support patterns.
