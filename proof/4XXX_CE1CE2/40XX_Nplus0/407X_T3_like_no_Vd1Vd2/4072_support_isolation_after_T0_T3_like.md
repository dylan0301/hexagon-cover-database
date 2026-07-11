# Support Isolation After the $T_0$ T3-Like Reduction

Status: Proven

This file records the support-isolation progress for the branch

$$
T_C\text{ is CE1 or CE2},\qquad N_+=0,
$$

with no Vd1/Vd2 rows and at least one T3-like vertex row.

It is used after the reduction in
[`4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md), which proves that, after normalizing

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
$$

one has

$$
T_0\text{ is T3-like}.
$$

We then reflect across the line through $O,V_0$ if necessary and assume

$$
T_0\text{ has positive-length support on }r_1=[O,V_1].
$$

This file deliberately does **not** assume $M_1\in T_0$ or $M_5\in T_0$.  The half-skeleton midpoint inventory in
[`../../../1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md`](../../../1XXX_foundations/12XX_V_triangle/1205_midpoint_subsets.md)
concerns maximal normalized triangles over $S_{1/2}$ only, not maximal triangles over the full skeleton $S$.

## 1. Dependencies

We use the following recorded dependencies.

1. The CE1/CE2 exact-one-midpoint dependency:
   [`../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md).
   Its hypothesis $O\in\mathrm{int}(T_C)$ is supplied by the original open
   center role before closure.

2. The T3-like midpoint exclusion:
   [`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2006_T3_like_midpoint_lemma.md):
   
   $$
   T_i\text{ T3-like}\quad\Longrightarrow\quad M_i\notin T_i.
   $$

3. The diagonal-length cap package:
   [`../../../2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md).
   This file records the reduced diagonal caps
   
   $$
   T_C\le {3\over2},\qquad \mathrm{Vd0}\le1,\qquad \mathrm{T3\text{-}like}\le {1\over2}.
   $$
   
   The T3-like cap is recorded there as practically proven, so the results in this file are conditional on that dependency.

4. T3-like rows are nonsupercritical:
   [`../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md`](../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md).

## 2. At most two T3-like rows

### Lemma 2.1

In the present branch, at most two vertex rows are T3-like.

### Proof

Let $k$ be the number of T3-like vertex rows.  Since $N_+=0$, every vertex row is nonsupercritical.  Since no row is Vd1 or Vd2, every non-T3-like vertex row is Vd0.

Let

$$
D=\bigcup_{i=0}^5 r_i
$$

be the diagonal target.  Its total length is

$$
\mathcal H^1(D)=6.
$$

By the reduced diagonal caps from `2520`, a CE1/CE2 center role contributes at most $3/2$, each T3-like row contributes at most $1/2$, and each nonsupercritical Vd0 row contributes at most $1$.  Therefore the total diagonal coverage is at most

$$
{3\over2}+k\cdot {1\over2}+(6-k)\cdot 1={15-k\over2}.
$$

If $k\ge3$, this is at most $6$.  The endpoint and active-interval degeneracies in the reduced open-cover accounting are strict, as recorded in `2520`, so the actual reduced diagonal contribution is strictly less than $6$.  This contradicts coverage of $D$.

Thus $k\le2$.

## 3. $T_2$ and $T_4$ are Vd0

### Lemma 3.1

After the $4071$ reduction and the reflection normalization above,

$$
T_2\text{ is Vd0}.
$$

### Proof

Assume for contradiction that $T_2$ is T3-like.  Since $T_0$ is already T3-like, Lemma 2.1 implies that no other row can be T3-like.

By the T3-like midpoint exclusion,

$$
M_2\notin T_2.
$$

Also $M_2\notin T_C$, since $T_C$ covers exactly $M_0$ among the six radial midpoints.  The only vertex rows that can cover $M_2$ are local to $M_2$, namely $T_1,T_2,T_3$.  The row $T_2$ is excluded.  The rows $T_1,T_3$ cannot be T3-like, because that would create a third T3-like row.  Since no row is Vd1 or Vd2, $T_1,T_3$ are Vd0.  Vd0 rows have no positive-length adjacent-ray support and cannot cover an adjacent midpoint in this branch.

Thus $M_2$ would be uncovered, contradiction.  Hence $T_2$ is not T3-like.  Since no Vd1/Vd2 row exists, $T_2$ is Vd0.

### Lemma 3.2

Similarly,

$$
T_4\text{ is Vd0}.
$$

### Proof

The proof is the reflection of Lemma 3.1.  If $T_4$ were T3-like, then $M_4\notin T_4$.  Its only local rescuers would be $T_3,T_5$, but neither can be T3-like because $T_0$ and $T_4$ would already be two T3-like rows.  With no Vd1/Vd2 rows, $T_3,T_5$ are Vd0 and cannot rescue the adjacent midpoint.  Thus $M_4$ would be uncovered.

## 4. A point-contact lemma for $M_5$

### Lemma 4.1

If $T_0$ is T3-like and has positive-length adjacent support on $r_1$, then

$$
M_5\notin T_0.
$$

### Proof

Use normalized $V_0$-local coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0).
$$

Thus

$$
V_0=(0,0),\qquad V_5=(1,0),\qquad V_1=(0,1),\qquad O=(1,1).
$$

For a T3-like $T_0$ with the side-through-$V_0$ normalization and adjacent support on $r_1$, write

$$
r=-R,\qquad s>0,\qquad D=s+R,
$$

with

$$
R^2-DR+D^2=1.
$$

Let $\tau\in[0,1]$ be the position of $V_0$ on the chosen side.  The triangle inequalities may be written as

$$
sx+Ry\ge0,
$$

$$
\tau+sy-Dx\ge0,
$$

and

$$
\tau-Rx+Dy\le1.
$$

On $r_5$, points have the form $(1,y)$, $0\le y\le1$.  The last two inequalities give

$$
y\ge {D-\tau\over s},\qquad y\le {1-\tau+R\over D}.
$$

Suppose $M_5\in T_0$.  In these coordinates, $M_5=(1,1/2)$.  Since $T_0$ has positive adjacent support on $r_1$, it has no positive-length support on $r_5$.  Hence the intersection with $r_5$ at $y=1/2$ must be a single point, and therefore

$$
{D-\tau\over s}={1\over2},\qquad {1-\tau+R\over D}={1\over2}.
$$

Using $s=D-R$, the first equality gives

$$
\tau={D+R\over2},
$$

while the second gives

$$
\tau=1+R-{D\over2}.
$$

Equating them yields

$$
R=2D-2.
$$

Substitution into

$$
R^2-DR+D^2=1
$$

gives

$$
3(D-1)^2=0.
$$

So $D=1$ and $R=0$, which degenerates the positive $r_1$ support.  This contradicts the T3-like support hypothesis.  Thus $M_5\notin T_0$.

## 5. $T_5$ is Vd0

### Lemma 5.1

In the present branch,

$$
T_5\text{ is Vd0}.
$$

### Proof

Assume for contradiction that $T_5$ is T3-like.  Then $T_0$ and $T_5$ are the two allowed T3-like rows, so no other row is T3-like.

By the T3-like midpoint exclusion,

$$
M_5\notin T_5.
$$

Also $M_5\notin T_C$, since $T_C$ covers exactly $M_0$ among the radial midpoints.  The only remaining local rescuers for $M_5$ are $T_4$ and $T_0$.  By Lemma 3.2, $T_4$ is Vd0 and cannot cover the adjacent midpoint $M_5$.  By Lemma 4.1, $M_5\notin T_0$.

Thus $M_5$ would be uncovered, contradiction.  Hence $T_5$ is not T3-like.  Since no row is Vd1 or Vd2, $T_5$ is Vd0.

## 6. Radial support isolation

### Theorem 6.1

After the $4071$ reduction and the reflection normalization,

$$
r_1\text{ has positive-length support only from }T_C,T_0,T_1,
$$

and

$$
r_5\text{ has positive-length support only from }T_C,T_5.
$$

### Proof

The only vertex roles that can have positive-length support on $r_1$ are local to that ray: $T_0,T_1,T_2$.  By Lemma 3.1, $T_2$ is Vd0, so it has no positive-length adjacent support on $r_1$.  Hence only $T_C,T_0,T_1$ can support $r_1$.

Similarly, the only vertex roles that can have positive-length support on $r_5$ are $T_4,T_5,T_0$.  By Lemmas 3.2 and 5.1, $T_4$ and $T_5$ are Vd0 except that $T_5$ supports its own radial $r_5$.  The row $T_0$ is T3-like but has selected positive adjacent support on $r_1$, so it has no positive-length support on $r_5$.  Therefore only $T_C,T_5$ can support $r_5$.

## 7. Consequence for the $r_0$ tail

The preceding lemmas do not remove all possible support on $r_0$.  The only possible additional supporter besides $T_C$ and $T_0$ is $T_1$ if $T_1$ is T3-like and chooses $r_0$ as its adjacent radial support.

Therefore the correct downstream split is:

1. If $T_1$ does not support $r_0$, then $T_0$ must cover the remaining $r_0$ tail after $T_C$.
2. If $T_1$ supports $r_0$, then the $T_1$ contribution must be bounded by a stricter neighboring-ray constrained $B$-map using the neighbor-ray formula in
   [`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md).

No assertion that all rows other than $T_0$ are Vd0 is made here; $T_1$ remains the exceptional possible T3-like row.
