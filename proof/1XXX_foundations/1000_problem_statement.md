# Problem Statement

Status: Definition

Let $H$ be the regular hexagon of side length $1$, centered at

$$
O=(0,0).
$$

Its vertices are

$$
V_i=\left(\cos \frac{i\pi}{3},\sin \frac{i\pi}{3}\right), \qquad i\in \mathbb Z/6\mathbb Z.
$$

## Final theorem target

$$
\boxed{\text{The regular hexagon }H\text{ cannot be covered by seven open unit equilateral triangles.}}
$$

## Equivalent expanded closed formulation

For $L>1$, let $H_L$ be the regular hexagon of side length $L$, centered at $O$, with vertices $L V_i$.

The equivalent formulation is:

$$
\boxed{\text{For every }L>1,\ H_L\text{ cannot be covered by seven closed unit equilateral triangles.}}
$$

The equivalence is proved in `103_open_unit_vs_shrunken_closed_equivalence.md`.

## Seven-triangle bookkeeping

A hypothetical cover is organized as

$$
T_C,T_0,T_1,\dots,T_5.
$$

Here:

- $T_C$ is a triangle containing the center $O$;
- $T_i$ is a triangle containing the vertex $V_i$.

This is bookkeeping: a genuine cover might have multiple triangles containing the same special point, but one representative is fixed for each required role.

## Target hierarchy

$$
H\supset S\supset S_{1/2}.
$$

Noncoverage of $S$ implies noncoverage of $H$. Noncoverage of $S_{1/2}$ gives a local or case-specific obstruction.

The converse direction is not available. In fact, the May 24, 2026 counterexample in `../9XXX_failed_ideas/908X_skeleton_cover_counterexample/9081_skeleton_cover_counterexample.md` numerically verifies seven closed equilateral triangles of side strictly less than $1$ covering $S$. Thus $S$ is too small as a standalone global target.
