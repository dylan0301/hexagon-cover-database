# CE1/CE2, $N_+=0$, All Vd0: Gap-Enclosure Proof

Status: Proven

This file replaces the nonzero-gap portions of the former endpoint-propagation
package.  The proof uses only explicit radial witnesses, convexity, the exact
local radial envelope, and equilateral support functions.  It does not invoke
`2107`, `2108`, `2110`, or a composition of boundary-transfer maps.

## Theorem

Let

$$
U_C,U_0,\ldots,U_5
$$

be open unit equilateral roles with $O\in U_C$ and $V_i\in U_i$.  Put
$T_C=\overline{U_C}$ and $T_i=\overline{U_i}$.  Assume:

1. $T_C$ is CE1 or CE2;
2. every $T_i$ is Vd0;
3. every $T_i$ is nonsupercritical;
4. the roles cover the full hexagon skeleton;
5. at least one boundary edge contains a V-gap.

Then no such configuration exists.

## 1. One gap

After reflection, normalize the unique gap to

$$
J=[X(\ell),X(r)]\subset e_{0,1},
$$

where

$$
X(t)=V_0+t(V_1-V_0),
\qquad
0\le\ell\le r\le1.
$$

Because $J$ is the **actual** V-gap, its endpoints are the actual maximal
incident reaches:

$$
\boxed{\ell=B_0,\qquad r=1-A_1.}
\tag{0}
$$

Hence

$$
U_0\cap e_{0,1}=X([0,\ell)),
\qquad
U_1\cap e_{0,1}=X((r,1]),
$$

and every point of $J=X([\ell,r])$ is missed by the six open V roles.  For
any selected opposite-edge lower bounds, the two incident closed roles are
contained in the trace-exact AB envelopes

$$
\mathcal E_0^{\rightarrow}(a_0\mid\ell),
\qquad
\mathcal E_1^{\leftarrow}(1-r\mid b_1),
$$

from [`2009e`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/2009e_trace_exact_ab_envelopes.md).  Their closed sections on the common
edge stop exactly at $X(\ell)$ and start exactly at $X(r)$.  These envelopes
are used for the figures and for the exact gap bookkeeping; the radial bounds
below remain the established ordinary AB capacities because the trace-exact
envelopes are subunions of the ordinary AB-set.

On the other five edges choose strict handoffs

$$
x_i\in(1-A_{i+1},B_i),
\qquad i=1,\ldots,5.
$$

Nonsupercriticality gives

$$
\ell\le x_5\le x_4\le x_3\le x_2\le x_1\le r.
\tag{1}
$$

Indeed, $T_1$ gives $x_1\le r$, every middle role gives
$x_i\le x_{i-1}$, and $T_0$ gives $x_5\ge\ell$.

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

Equation (1) shows that every $T_i$ has selected adjacent boundary reaches at
least $(p,q)$, after reflecting its local chart when necessary.

For each $i$, put

$$
D_i=d_*V_i.
$$

We claim that every $D_i$ lies in $U_C$.  If $D_i\in U_i$, openness gives a
radial demand strictly larger than $c_*$ together with the selected boundary
demands $(p,q)$, contradicting the definition of $c_{\max}$.  The adjacent
roles are Vd0 and cannot contain a noncentral point of $r_i$ without positive
adjacent support.  The three nonlocal roles are excluded by the diameter-one
inequalities

$$
\lVert d_*V_i-V_{i\pm2}\rVert^2=1+d_*+d_*^2>1,
$$

and

$$
\lVert d_*V_i-V_{i+3}\rVert=1+d_*>1.
$$

Thus the six V roles miss $D_i$, so skeleton coverage forces $D_i\in U_C$.
Convexity gives

$$
\mathcal D_{hd_*}\subset U_C.
\tag{3}
$$

The entire gap segment $J$ also lies in $U_C$.  The complementary-gap theorem
[`2608`, complementary-gap theorem](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
gives

$$
\Lambda(\mathcal D_{hd_*}\cup J)\ge1.
$$

A compact subset of an open unit equilateral triangle has enclosure number
strictly below one.  This contradicts (3) and $J\subset U_C$.

The proof includes singleton gaps: no positive lower bound for $r-\ell$ was
used.

## 2. Two gaps

This state is CE2-only.  Use the signed center variables of
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md)
and put

$$
p=W-\alpha,
\qquad
q=R-\delta.
\tag{4}
$$

The two gap edges are $e_{5,0}$ and $e_{0,1}$.  The four center-free edges
between them admit handoffs $x_1,x_2,x_3,x_4$.  Gap containment and
nonsupercriticality of $T_1,\ldots,T_5$ give

$$
p<x_4<x_3<x_2<x_1<1-q.
\tag{5}
$$

Consequently each of $T_1,\ldots,T_5$ realizes the common lower boundary pair
$(p,q)$ in the appropriate local orientation.

Let

$$
c_*=c_{\max}(p,q),
\qquad
D_2=(1-c_*)V_2,
\qquad
D_4=(1-c_*)V_4.
$$

Exactly as in the one-gap argument, $D_2$ and $D_4$ are missed by every V
role and hence belong to $U_C$.

The CE2 short-ray theorem
[`2608`, Theorem 6.1](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
proves

$$
c_*<1-\min\{\alpha,\delta\}.
$$

If $\delta\le\alpha$, then $D_2$ lies at distance greater than $\delta$ from
$O$, while the CE2 center reaches exactly $\delta$ on $r_2$.  If
$\alpha\le\delta$, then $D_4$ lies beyond the center exit $\alpha$ on $r_4$.
Both alternatives contradict $D_2,D_4\in U_C$.

The one- and two-gap states are exhaustive.  This proves the theorem.

$$
\Box
$$
