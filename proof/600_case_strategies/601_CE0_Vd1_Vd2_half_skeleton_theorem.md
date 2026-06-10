# CE0 + Vd1/Vd2 Half-Skeleton Theorem

Status: Proven

## Expanded closed-triangle theorem

For every $L>1$, let $H_L$ be the regular hexagon of side length $L$. There is no cover of $S_{1/2}(H_L)$ by seven closed unit equilateral triangles

$$
T_C,T_0,\dots,T_5
$$

under the assumptions:

$$
T_C\text{ is CE0},
$$

and at least one $V_i$-triangle is Vd1 or Vd2.

## Original open-triangle corollary

By the Lebesgue-number/scaling equivalence, the same obstruction applies to the original side-$1$ open unit formulation:

$$
\mathrm{CE0}+\mathrm{Vd1/Vd2}
$$

cannot occur in a seven-open-unit-triangle cover of $S_{1/2}(H)$.

## Proof components

The proof is assembled from:

1. `602_CE0_Vd1_Vd2_rhombus_geometry.md`.
2. `603_CE0_Vd1_Vd2_frontier_perturbation.md`.
3. `604_CE0_Vd1_Vd2_F_chain_inequalities.md`.
4. `605_CE0_Vd1_Vd2_midpoint_hole_subcases.md`.
5. `606_CE0_Vd1_Vd2_assembly.md`.

## Normalization

By $D_6$-symmetry, assume the Vd1/Vd2 triangle is $T_0$. Let $x$ be the largest distance from $O$ to the chosen adjacent-ray intersection of $T_0$.

The proof splits into

$$
x<\frac12 \qquad\text{and}\qquad x\ge\frac12.
$$

The small-$x$ case uses

$$
b+F^{\circ3}(a)<1.
$$

The large-$x$ case uses

$$
b+F^{\circ4}(a)<1.
$$
