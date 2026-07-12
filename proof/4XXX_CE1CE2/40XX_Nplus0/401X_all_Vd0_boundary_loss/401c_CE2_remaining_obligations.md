# Exact CE2 Boundary-Loss Obligations Remaining After the CE1 Completion

Status: Strategy

This note records why the proved CE1 matrix in `401b` does not by itself close
the CE2 half of `401X`.

## Exact domain mismatch

The CE1 proof uses both

$$
t+R(1-s)\le S
$$

and

$$
t\ge S-\frac{R^2}{1-R}s.
$$

The second inequality excludes a positive-length overlap with the other edge
at $V_0$. Together they imply

$$
s\ge1-R
$$

and the strict loss inequality

$$
s>S-u.
$$

A CE2 center triangle has two coupled positive boundary intervals. Its exact
domain is instead the four-variable domain in
[`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md).
The CE1 no-second-interval inequality is unavailable. Therefore the CE1
branch matrix may not be copied to CE2 merely by selecting one of its two
intervals.

## Gap split

The CE2 branch has three logically different boundary states.

1. Neither center interval contains a V-gap. The exact open-perimeter lemma in
   `4014`, Section 6 proves this case impossible, including every row-sum
   equality case.
2. Exactly one center interval contains a V-gap. The adjacent radial demands
   are the coupled expressions in `2106`. The remaining target is an exact
   safe-map inequality over that one-gap CE2 domain, in both orientations.
   The CE1 inequality $s>S-u$ is not available there.
3. Both center intervals contain V-gaps. The replacement theorem in
   [`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2104_CE2_one_interval_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2104_CE2_one_interval_lemma.md)
   proves that such a skeleton system is not replacement-maximal. It does not
   by itself contradict the original full-hexagon cover: the replacement is
   proved to preserve the skeleton, and enlargement to a unit triangle can
   change the V-type or the value of $N_+$. A proof-tree use must either
   establish a maximal-role convention before classification or route every
   resulting branch exit.

## Exact remaining target

To promote the full `4013` package to `Proven`, it is still necessary to do
both of the following:

- prove the one-gap inequality using the coupled `2106` formulas; and
- justify the two-gap maximality convention at the full-cover proof-tree
  level or route every replacement exit.

The first two formerly open CE1 cells and both certificate-backed CE1 cells
are not on this list; they are proved analytically in `401b`.
