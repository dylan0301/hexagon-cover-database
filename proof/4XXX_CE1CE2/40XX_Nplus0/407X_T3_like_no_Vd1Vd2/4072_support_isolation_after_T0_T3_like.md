# Support Isolation After the $T_0$ T3-Like Reduction

Status: Proven

Assume the branch of
[`4071`](4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md):

$$
T_C\text{ is CE1 or CE2},
\qquad
N_+=0,
$$

there are no Vd1/Vd2 roles,

$$
T_C\cap\left\{M_0,\ldots,M_5\right\}=\left\{M_0\right\},
$$

and $T_0$ is T3-like.  Reflect across $OV_0$ if necessary so that the unique
positive-length adjacent support of $T_0$ is on $r_1$.

## At most two T3-like roles

Let $k$ be the number of T3-like vertex roles.  The diagonal-trace theorem
[`2520`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2520_diagonal_length_bounds.md)
gives the following bounds for the role closures:

$$
L_D(T_C)<\frac{3}{2},
\qquad
L_D(T_i)<\frac{1}{2}\quad\text{for each T3-like role},
$$

and

$$
L_D(T_i)\le1\quad\text{for each nonsupercritical Vd0 role}.
$$

Every T3-like role is nonsupercritical by
[`1213`](../../../1XXX_foundations/12XX_V_triangle/1213_T3_like_nonsupercritical.md),
and $N_+=0$ makes every Vd0 role nonsupercritical.  Since the six radial arms
have total length $6$, coverage and subadditivity would imply

$$
6
\le
L_D(T_C)+\sum_{i=0}^5L_D(T_i)
<
\frac{3}{2}+\frac{k}{2}+(6-k)
=\frac{15-k}{2}.
$$

For $k\ge3$ the right side is at most $6$, a contradiction.  Hence

$$
\boxed{k\le2.}
$$

This citation removes the former duplication of the diagonal-cap proofs and
also removes the old circular dependency on the side model in `4073`.

## Forced Vd0 roles

### Lemma 1

The roles $T_2$ and $T_4$ are Vd0.

### Proof

Suppose $T_2$ were T3-like.  Then $T_0,T_2$ would be the two allowed
T3-like roles.  The midpoint exclusion gives $M_2\notin T_2$, while the
normalization gives $M_2\notin T_C$.  The only remaining local roles that
could cover $M_2$ in the original open cover are $T_1,T_3$.  They cannot be
T3-like by the bound $k\le2$, so exhaustiveness makes them Vd0.  An open Vd0
role cannot contain an adjacent midpoint, because that would give
positive-length adjacent support.  Thus $M_2$ would be uncovered.  Hence
$T_2$ is not T3-like and therefore is Vd0.

Reflection gives the same argument for $T_4$.

### Lemma 2

The role $T_5$ is Vd0.

### Proof

First note that the original open role $T_0$ cannot cover $M_5$.  If it did,
its intersection with $r_5$ would contain a relative neighborhood of $M_5$
and hence have positive length.  This contradicts the fact that the unique
adjacent support of the T3-like role $T_0$ is on $r_1$.

Suppose now that $T_5$ were T3-like.  Then $T_0,T_5$ would be the two allowed
T3-like roles.  The T3-like midpoint exclusion gives $M_5\notin T_5$, and
$M_5\notin T_C$ by normalization.  The other local roles are $T_4$ and
$T_0$.  Lemma 1 makes $T_4$ Vd0, so its original open triangle cannot cover
the adjacent midpoint; the preceding paragraph excludes $T_0$.  Thus $M_5$
would be uncovered.  Therefore $T_5$ is not T3-like and hence is Vd0.

## Radial support isolation

Only $T_0,T_1,T_2$ are local to $r_1$.  Lemma 1 makes $T_2$ Vd0, so

$$
\boxed{
r_1\text{ has positive-length support only from }T_C,T_0,T_1.
}
$$

Only $T_4,T_5,T_0$ are local to $r_5$.  Lemmas 1 and 2 make $T_4,T_5$ Vd0;
$T_5$ can support its own ray, whereas $T_4$ cannot support the adjacent ray.
The T3-like role $T_0$ selected $r_1$ and therefore has no positive-length
support on $r_5$.  Hence

$$
\boxed{
r_5\text{ has positive-length support only from }T_C,T_5.
}
$$

The argument does not force $T_1$ to be Vd0.  If $T_1$ is the possible
second T3-like role and supports $r_0$, that extra requirement only shrinks
its realizing set.  The universal nonsupercritical relaxation in `4073`
therefore remains valid without a separate constrained map.
