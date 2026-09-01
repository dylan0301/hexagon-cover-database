# CE1/CE2, $N_+=1$, All Vd0: Simplified Finite-Witness Proof

Status: Proven

This is the active all-Vd0 nonzero-gap proof.  It replaces the former
ten-point one-gap witness by the transverse seven-point theorem
[`4103`](4103_transverse_seven_point_enclosure.md), and uses the shorter CE2
short-ray proof in
[`2609`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md)
for the two-gap branch.

## Theorem

Let the center role be CE1 or CE2. Assume every V role is Vd0, exactly one
actual V role is supercritical, the seven original open roles cover the
hexagon skeleton, and at least one boundary edge contains a V-gap. Then no
such configuration exists.

## 1. Structural normalization

Put

$$
T_C=\overline{U_C},
\qquad
T_i=\overline{U_i}.
$$

By the exactly-one-midpoint theorem, normalize

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

Midpoint locality makes $T_0$ the unique supercritical V role, while
$T_1,\ldots,T_5$ are nonsupercritical Vd0 roles.

Every actual V-gap is a closed interval

$$
J_i=X_i([B_i,1-A_{i+1}]),
$$

including the singleton case, because the two incident V roles are open.

## 2. One gap

Normalize the unique gap to

$$
J=[X(\ell),X(r)]\subset e_{0,1},
\qquad
\ell=B_0,\quad r=1-A_1.
$$

For each $i$, let $C_i$ be the actual own-radial reach of $T_i$ and put

$$
P_i=(1-C_i)V_i.
$$

Every $P_i$ is missed by all six open V roles: it is the closed own-trace
endpoint, the adjacent roles are Vd0, and the nonlocal roles are excluded by
diameter one. Hence $P_i\in U_C$.

The active witness is only

$$
K_{\rm tr}
=
\{O,M_0,X(\ell),X(r),P_2,P_3,P_4\}.
$$

It is contained in $U_C$, whereas Theorem 2.1 of `4103` gives

$$
\Lambda(K_{\rm tr})\ge1.
$$

A compact subset of an open unit equilateral triangle has enclosure number
strictly below one. This contradiction closes the one-gap branch.

The former set

$$
K_{410}
=
\{O,M_0,X(\ell),X(r),P_0,\ldots,P_5\}
$$

may be retained as a harmless superset, but its points $P_0,P_1,P_5$ are not
needed.

## 3. Two gaps

This branch is CE2-only. Put

$$
p=W-\alpha,
\qquad
q=R-\delta.
$$

The four center-free handoffs between the two gap edges show that
$T_1,\ldots,T_5$ all dominate the common lower pair $(p,q)$. Type-aware
radial forcing from
[`2608`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
therefore puts

$$
D_2=(1-c_{\max}(p,q))V_2,
\qquad
D_4=(1-c_{\max}(p,q))V_4
$$

in $U_C$.

Theorem 2.1 of `2609` proves

$$
c_{\max}(p,q)<1-\min\{\alpha,\delta\}.
$$

If $\delta\le\alpha$, then $D_2$ lies beyond the C exit $\delta$ on $r_2$.
If $\alpha\le\delta$, then $D_4$ lies beyond the C exit $\alpha$ on $r_4$.
Either alternative contradicts containment in $U_C$.

The one- and two-gap cases are exhaustive. $\square$
