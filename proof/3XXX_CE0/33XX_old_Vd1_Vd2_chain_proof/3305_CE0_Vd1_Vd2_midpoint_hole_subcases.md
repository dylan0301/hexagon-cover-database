# CE0 + Vd1/Vd2 Midpoint-Hole Subcases

Status: Proven case split

Assume

$$
T_C\text{ is CE0},
$$

and normalize so that

$$
T_0\text{ is Vd1 or Vd2}.
$$

Let $x$ be the largest distance from $O$ to the chosen adjacent-ray intersection of $T_0$.

## Subcase A: two holes are covered by two different triangles

This is the ordinary chain case.

For $x<1/2$, the obstruction is

$$
b+F^{\circ3}(a)<1.
$$

For $x\ge1/2$, the obstruction is

$$
b+F^{\circ4}(a)<1.
$$

The interpretation is that the remaining zero-diagonal chain cannot close.

## Subcase B: one triangle covers two holes

This is the frontier-compression case.

The triangle covering two holes has stronger $(a,b)$-constraints. Apply the frontier perturbation lemma to replace the actual $(a,b)$-data by a dominating feasible frontier point.

After this replacement, the same $F$-chain contradiction applies.

## Vd2 reduction

A Vd2 triangle has positive-length intersections with both adjacent rays. Choose either adjacent ray. The same Vd1-type local argument applies; the other adjacent-ray intersection is an extra constraint, not extra freedom.
