# Diagonal Length Bounds

Status: Practically proven

Let

$$
D=\bigcup_{i=0}^5 r_i
$$

be the union of the six half-diagonals. Equivalently,

$$
D=[V_0,V_3]\cup[V_1,V_4]\cup[V_2,V_5].
$$

Then

$$
\mathcal H^1(D)=6.
$$

This file records the diagonal-length caps used by the CE1/CE2 T3-like
branches. The caps are measured in the reduced diagonal accounting for the
branch under consideration.

## Diagonal cap targets

| Role or local type | Hypothesis | Diagonal contribution cap |
|---|---|---:|
| CE1/CE2 center role | after reducing to the active $C$-only diagonal interval | $\frac32$ |
| Vd0 vertex role | $a+b\le1$ | $1$ |
| Vd0 vertex role | $a+b>1$ | $\frac12$ |
| T3-like vertex role | intended reduced T3-like diagonal branch | $\frac12$ |

The T3-like cap is recorded here as practically proven. Its complete proof is
not included in this file.

## Local support notes

The half-diagonal notation is defined in
[`../../1XXX_foundations/10XX_global_conventions/1001_geometry_objects.md`](../../1XXX_foundations/10XX_global_conventions/1001_geometry_objects.md).

The T3-like half-diagonal support convention is recorded in
[`../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md`](../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
After rotating indices to $i=0$, a T3-like $V_0$-triangle can have
positive-length half-diagonal intersection only with $OV_0$ and exactly one of
$OV_1$ and $OV_5$.

The T3-like nonsupercritical working dependency is recorded in
[`../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md`](../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md)
(Status: Proven).

## Use in the CE1/CE2 T3-like branch

Under the CE1/CE2, $N_+=1$, no-Vd1/Vd2, at-least-two-T3-like hypotheses, the
T3-like rows are nonsupercritical. Therefore the unique supercritical row is
Vd0. The worst diagonal-length accounting is then:

| Role count | Cap |
|---|---:|
| one CE1/CE2 center role | $\frac32$ |
| one supercritical Vd0 row | $\frac12$ |
| two T3-like rows | $2\cdot\frac12$ |
| three nonsupercritical Vd0 rows | $3\cdot1$ |

The total cap is

$$
\frac32+\frac12+2\cdot\frac12+3=6.
$$

In the reduced open-cover accounting, the endpoint and active-interval
degeneracies make the bound strict. Hence the seven role triangles cannot
cover the full diagonal target $D$ in this branch.
