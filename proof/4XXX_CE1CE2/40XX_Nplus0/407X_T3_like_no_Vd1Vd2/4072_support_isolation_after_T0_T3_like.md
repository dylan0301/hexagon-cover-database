# Support Isolation After the $T_0$ T3-Like Reduction

Status: Proven

Retain the notation $U_C,U_i$ for original open roles and
$T_C=\overline{U_C},T_i=\overline{U_i}$ from the branch of
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

Let $k=N_{\rm sp}$ be the number of T3-like V triangles; there are no Vd1 or
Vd2 roles in this branch. The common budget theorem
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
gives the direct obstruction

$$
N_++N_{\rm sp}\ge3.
$$

Here $N_+=0$ and $N_{\rm sp}=k$. Hence the obstruction excludes $k\ge3$,
and

$$
\boxed{k\le2.}
$$

## Forced Vd0 roles

### Lemma 1

The roles $T_2$ and $T_4$ are Vd0.

### Proof

Suppose $T_2$ were T3-like.  Then $T_0,T_2$ would be the two allowed
T3-like roles.  The midpoint exclusion gives $M_2\notin T_2$, while the
normalization gives $M_2\notin T_C$. The only remaining local open roles that
could cover $M_2$ are $U_1,U_3$. Their closures cannot be
T3-like by the bound $k\le2$, so exhaustiveness makes them Vd0. An open role
whose closure is Vd0 cannot contain an adjacent midpoint, because that would give
positive-length adjacent support.  Thus $M_2$ would be uncovered.  Hence
$T_2$ is not T3-like and therefore is Vd0.

Reflection gives the same argument for $T_4$.

### Lemma 2

The role $T_5$ is Vd0.

### Proof

First note that the original open role $U_0$ cannot cover $M_5$. If it did,
its intersection with $r_5$ would contain a relative neighborhood of $M_5$
and hence have positive length.  This contradicts the fact that the unique
adjacent support of the T3-like role $T_0$ is on $r_1$.

Suppose now that $T_5$ were T3-like.  Then $T_0,T_5$ would be the two allowed
T3-like roles.  The T3-like midpoint exclusion gives $M_5\notin T_5$, and
$M_5\notin T_C$ by normalization.  The other local roles are $T_4$ and
$U_0$. Lemma 1 makes $T_4$ Vd0, so $U_4$ cannot cover
the adjacent midpoint; the preceding paragraph excludes $U_0$. Thus $M_5$
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
its realizing set. The exact nonsupercritical relaxation in `4073`
therefore remains valid without a separate constrained map.
