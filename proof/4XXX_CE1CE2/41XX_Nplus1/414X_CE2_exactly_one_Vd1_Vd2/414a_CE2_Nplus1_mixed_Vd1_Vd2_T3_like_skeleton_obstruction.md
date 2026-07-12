# CE2, $N_+=1$, Mixed Vd1/Vd2--Positive-Support Skeleton Obstruction

Status: Proven

This note closes the part of `414X` containing exactly one Vd1/Vd2 row and
one or more additional positive-adjacent-support rows. In particular, it
closes every requested mixture with one or more T3-like rows. It applies the skeleton caps from
[`../../../2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2510_skeleton_length_bounds.md)
to the closures of the original open-cover role triangles.

## Statement

Assume the closures of original open-cover roles satisfy

$$
T_C\text{ is CE2},
\qquad
T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
$$

$N_+=1$, exactly one vertex row is Vd1 or Vd2, and $k\ge1$ additional vertex
rows have positive-length intersection with an adjacent radial arm. Then the
seven role triangles cannot cover the full skeleton $S$.

## Distinct roles

The unique supercritical row is distinct from every positive-support row.
Indeed, the adjacent-ray formula in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md)
shows that a row with $a_i+b_i>1$ has no positive-length adjacent-ray
support. Every other row is nonsupercritical because $N_+=1$.

Consequently the six vertex roles consist of:

- one supercritical row;
- one Vd1/Vd2 row;
- $k$ additional positive-support rows; and
- $4-k$ remaining nonsupercritical rows with no adjacent-ray support.

Here $1\le k\le4$. No exhaustiveness assertion about the displayed
outside-vertex labels in `1201` is needed.

## Skeleton-length contradiction

For a role triangle $T$, write

$$
L_S(T)=\mathcal H^1(T\cap S).
$$

The bounds in `2510` give

$$
L_S(T_C)<\frac32,
$$

$$
L_S(T_{\mathrm{supercritical}})<\frac32,
$$

and, for the closures of the original open-cover roles,

$$
L_S(T_{\mathrm{Vd1/Vd2}})<\frac32,
\qquad
L_S(T_{\mathrm{positive},j})<\frac32.
$$

For a T3-like row, this application is made before the optional translation in
`1201`: every distinguished vertex lies in the interior of its original
open-cover role, which is the interior hypothesis required by `2510`,
Lemma 4. Each of the remaining $4-k$ nonsupercritical rows has no adjacent-ray
support, so `2510`, Lemma 5 gives

$$
L_S(T_j)\le2.
$$

Therefore

$$
\begin{aligned}
L_S(T_C)+\sum_{i=0}^5L_S(T_i)
&<\frac32(3+k)+2(4-k)\\
&=\frac{25-k}{2}\\
&\le12.
\end{aligned}
$$

When $k=1$, the displayed numerical bound equals $12$, but at least the
center and supercritical bounds are strict, so the total is still strictly
less than $12$.

If the seven triangles covered $S$, subadditivity would instead give

$$
12=\mathcal H^1(S)
\le L_S(T_C)+\sum_{i=0}^5L_S(T_i),
$$

a contradiction. Hence every stated mixed positive-support configuration,
including every Vd1/Vd2--T3-like mixture, is impossible.

$$
\Box
$$
