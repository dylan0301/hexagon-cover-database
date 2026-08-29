# CE1/CE2, $N_+=0$, T3-Like: Type-Aware Gap-Enclosure Proof

Status: Proven

This file replaces the nonzero-gap four-label endpoint package.  The proof
uses the exact neighboring-ray capacity only to exclude radial witnesses from
T3-like adjacent support; the terminal contradiction is the same explicit
gap-enclosure or CE2 short-ray obstruction as in the all-Vd0 case.  No
boundary-transfer composition is used.

## Theorem

Assume:

1. $T_C$ is CE1 or CE2;
2. $N_+=0$;
3. no V role is Vd1 or Vd2;
4. one or two V roles are T3-like and every other V role is Vd0;
5. the seven open roles cover the full skeleton;
6. at least one boundary edge contains a V-gap.

Then no such configuration exists.

## 1. One gap

Normalize the gap to

$$
J=[X(\ell),X(r)]\subset e_{0,1}.
$$

As in the all-Vd0 proof, strict handoffs on the other five edges and
nonsupercriticality give

$$
\ell\le x_5\le x_4\le x_3\le x_2\le x_1\le r.
\tag{1}
$$

Put

$$
p=1-r,
\qquad
q=\ell,
\qquad
c_*=c_{\max}(p,q),
\qquad
d_*=1-c_*.
\tag{2}
$$

Every V role has selected boundary reaches at least $(p,q)$ in its local
orientation.

Fix a ray $r_i$.  The own-role capacity on $r_i$ is at most $c_*$ by
coordinatewise antitonicity of $c_{\max}$.  A neighboring Vd0 role contributes
no positive interval on $r_i$.  If a neighboring role is T3-like and its
unique supported adjacent ray is $r_i$, its capacity is at most

$$
C_+(p,q)
\quad\text{or}\quad
C_-(p,q).
$$

The common-pair domination theorem in
[`2608`, Section 4](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
gives

$$
C_+(p,q),C_-(p,q)\le c_*.
$$

Therefore the type-aware radial witness theorem applies with

$$
D_i=d_*V_i.
$$

All six points $D_i$ lie in $U_C$, and convexity forces

$$
\mathcal D_{hd_*}\subset U_C.
$$

The gap segment $J$ is also contained in $U_C$.  The complementary-gap
theorem in `2608` gives

$$
\Lambda(\mathcal D_{hd_*}\cup J)\ge1,
$$

contradicting containment in an open unit equilateral triangle.

This proof does not distinguish the one-T3-like and two-T3-like placements.
The support-isolation theorem from the original package is consistent with
the type-aware capacity argument but is not needed by the terminal proof.

## 2. Two gaps

This state is CE2-only.  Put

$$
p=W-\alpha,
\qquad
q=R-\delta.
$$

The four center-free handoffs again give the common pair $(p,q)$ on
$T_1,\ldots,T_5$.  For the rays $r_2$ and $r_4$, every own or T3-like
neighboring capacity is at most

$$
c_*=c_{\max}(p,q)
$$

by common-pair domination.  Hence

$$
D_2=(1-c_*)V_2,
\qquad
D_4=(1-c_*)V_4
$$

belong to $U_C$.

The CE2 short-ray theorem in `2608` proves

$$
c_*<1-\min\{\alpha,\delta\}.
$$

Thus $D_2$ lies beyond the center on $r_2$, or $D_4$ lies beyond the center
on $r_4$.  This contradiction closes the two-gap state.

The one- and two-gap states are exhaustive, proving the theorem.

$$
\Box
$$
