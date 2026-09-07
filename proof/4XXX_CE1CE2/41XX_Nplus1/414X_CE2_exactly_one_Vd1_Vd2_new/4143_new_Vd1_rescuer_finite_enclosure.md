# CE1/CE2, \(N_+=1\): Vd1 Supported-Endpoint Rescuer Obstruction

Status: Proven

This is the active finite-enclosure proof for the placement in which the
unique Vd1 role is \(T_0\), it contains the neighboring midpoint \(M_1\), and
\(T_1\) is the unique supercritical role.  The Vd1 calculation below verifies
the hypotheses of the common fixed four-point interface in
[`2612`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md).

## 1. Reduced placement and the forced endpoint

Assume

\[
T_C\text{ is CE1 or CE2},
\qquad
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
\]

\[
T_0\text{ is Vd1},\qquad M_1\in T_0,
\qquad
T_1\text{ is uniquely supercritical},
\]

and \(T_2,T_3,T_4,T_5\) are nonsupercritical Vd0 roles.

Let \(a,b\) be the actual boundary reaches of \(T_0\).  In the Vd corner
normal form of
[`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
there is \(t>0\), with

\[
d=\sqrt{t^2+t+1},
\]

such that

\[
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb.
\end{aligned}
\tag{1}
\]

Write the supported interval on \(r_1\), measured from \(V_1\) toward \(O\),
as

\[
T_0\cap r_1=[c,u].
\]

Its exact endpoints are

\[
c=\frac{t(1-b)}{t+1},
\qquad
u=\frac{d-a-tb-1}{t}.
\tag{2}
\]

The midpoint condition gives

\[
c\le\frac12\le u.
\tag{3}
\]

The radial-frontier corollary in `2612` gives

\[
\boxed{P_{\rm Vd1}=(1-u)V_1\in U_C.}
\tag{5}
\]

Indeed the supercritical own role stops before $M_1$, the supported interval
reaches $M_1$, and all other possible neighboring contributions are absent.
This forcing and the chart calculation below use no CE2-only inequality.

Put

\[
\varepsilon=1-u.
\tag{6}
\]

Here \(\varepsilon>0\).  Otherwise the closed Vd1 role would contain
\(O\), which is at distance one from the interior point \(V_0\); this is
impossible for a diameter-one triangle.

## 2. The exact Vd1 inequalities

The Vd1 hypothesis forces

\[
\boxed{t\ge1.}
\tag{7}
\]

Indeed, the midpoint condition gives
\(a+tb\le d-1-t/2\).  If \(t<1\), the raw \(r_5\)-trace endpoints
from `2014` satisfy

\[
d-a-tb-t
\ge1-\frac t2
>
\frac1{t+1}
>
\frac{1-a}{t+1},
\]

so the reflected neighboring arm has a positive interval.  This contradicts
the Vd1 type.

For \(0\le c\le1/2\), define the nonattained strict-supercritical outgoing
supremum

\[
M=M_c^{\rm sup}
=
\frac{c+\sqrt{c^2-8c+4}}2.
\tag{8}
\]

We prove

\[
\boxed{
a\le1-M,
\qquad
\frac{a}{a+\varepsilon}\le1-M.
}
\tag{9}
\]

From (2)--(3),

\[
tb=t-c(t+1),
\]

and the midpoint inequality gives

\[
a\le
d-1-\frac{3t}{2}+c(t+1)
=:F(t,c).
\tag{10}
\]

For fixed \(c\le1/2\), \(F(t,c)\) decreases for \(t\ge1\).  Therefore

\[
a\le F(t,c)\le F(1,c)
=
\sqrt3-\frac52+2c
=:L(c).
\tag{11}
\]

A direct squaring calculation gives

\[
2L(c)\le1-M.
\tag{12}
\]

Indeed, (12) is equivalent to

\[
20c^2+(18\sqrt3-52)c+47-24\sqrt3\ge0,
\]

and the quadratic is decreasing on \([0,1/2]\) with positive value
\(26-15\sqrt3\) at \(1/2\).  Since \(a\ge0\), (11)--(12) imply the first
inequality in (9).

For the ratio, direct substitution in (2) gives

\[
\varepsilon
=
\varepsilon_0+\frac at,
\qquad
\varepsilon_0
=
\frac{2t+1-c(t+1)-d}{t}>0.
\tag{13}
\]

The map

\[
z\longmapsto
\frac{z}{z+\varepsilon_0+z/t}
\]

is increasing for \(z\ge0\), while

\[
\varepsilon_0+\frac{F(t,c)}{t}=\frac12.
\]

Using (10)--(12),

\[
\frac{a}{a+\varepsilon}
\le
\frac{F(t,c)}{F(t,c)+1/2}
\le
\frac{L(c)}{L(c)+1/2}
\le
2L(c)
\le1-M.
\]

This proves (9).

Finally, the Vd half-unit cap gives \(a<1/2\), and (3) gives
\(\varepsilon\le1/2\).  Thus

\[
a+\varepsilon<1.
\tag{14}
\]

## 3. Apply the common fixed-witness interface

The local chart has verified $A_0+\varepsilon\le1$ and
$A_0/(A_0+\varepsilon)\le1-M$. The supported endpoint is the total radial
frontier from [2612](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md),
Corollary 2.2a. Skeleton coverage from $V_1$ to the start $c$ of the
rescuer's interval gives $C_1\ge c$: the center misses $M_1$ and the
other V roles have no positive trace on this ray. Corollary 6.2 of `2612`
therefore supplies the same four actual points and contradiction for either
gap rank. No repeated boundary-tail proof and no disk are needed. $\square$
