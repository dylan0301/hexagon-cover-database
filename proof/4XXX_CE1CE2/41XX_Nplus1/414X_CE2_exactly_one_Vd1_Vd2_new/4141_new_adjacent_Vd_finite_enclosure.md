# CE2, \(N_+=1\): Adjacent Vd Finite-Enclosure Obstruction

Status: Proven

This is the active finite-enclosure proof for the placement in which the
unique supercritical V triangle is \(T_0\) and the unique Vd1/Vd2 V triangle
is adjacent to it.  After reflection the exceptional role is \(T_1\).
The proof retains the exact residual estimate from the former package and
uses the one-third radial envelope in
[`2609`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md).

## 1. Standing placement

Assume

\[
T_C\text{ is CE2},
\qquad
T_0\text{ is the unique supercritical V triangle},
\]

\[
T_1\text{ is the unique Vd1/Vd2 V triangle},
\]

and \(T_2,T_3,T_4,T_5\) are nonsupercritical Vd0 roles.  Use the signed
center variables of
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

\[
0<R<1,\qquad W=1-R,\qquad
E=\sqrt{1-RW},\qquad \eta=1-E,
\]

\[
P=E\eta,\qquad k=\eta+\alpha+\delta.
\]

The two center intervals are

\[
I_L=\left[\frac{k}{W},R+\alpha\right]\subset e_{5,0},
\qquad
I_R=\left[\frac{k}{R},W+\delta\right]\subset e_{0,1},
\]

and the C-triangle exit on \(r_2\), measured from \(O\), is

\[
d_2^C=\delta.
\tag{1}
\]

Let \((A_0,B_0)\) be the actual boundary reaches of the supercritical role.
Thus

\[
A_0+B_0>1,
\qquad
A_0^2+A_0B_0+B_0^2\le1.
\tag{2}
\]

Use the exact residual operator of
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md)
and put

\[
\rho_R=\mathcal R_{I_R}(B_0),
\qquad
\rho_L=\mathcal R_{I_L}(A_0).
\tag{3}
\]

Here \(\rho_R\) is the incoming boundary demand forced on \(T_1\), and
\(\rho_L\) is the far boundary demand forced on \(T_5\).  In a reduced
candidate \(\rho_L>0\).  Propagation through the four center-free ordinary
roles gives

\[
A_1\ge\rho_R,
\qquad
B_1\ge\rho_L,
\qquad
B_2\ge\rho_L.
\tag{4}
\]

The Vd1/Vd2 half-unit cap from
[`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
therefore gives

\[
\boxed{\rho_R+\rho_L<\frac12.}
\tag{5}
\]

## 2. The residual dominates the C exit

We prove the stronger estimate

\[
\boxed{4\delta<\rho_L.}
\tag{6}
\]

The common CE2 budget in
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
gives

\[
\alpha+\delta<\frac1{24},
\qquad
\alpha+\delta<\frac{\min\{R,W\}}6.
\tag{7}
\]

The exact residual formula leaves two positive possibilities for \(\rho_L\).

### Case 2.1: \(\rho_L=W-\alpha\)

By (7),

\[
4\delta+\alpha
\le4(\alpha+\delta)
<\frac{2W}{3}<W.
\]

Hence

\[
4\delta<W-\alpha=\rho_L.
\]

### Case 2.2: \(\rho_L=1-A_0\)

The other residual cannot be \(1-B_0\).  Otherwise (5) would imply

\[
2-A_0-B_0<\frac12,
\]

hence \(A_0+B_0>3/2\), contradicting the diameter consequence
\(A_0+B_0\le2/\sqrt3<3/2\).  The residual formula therefore gives

\[
\rho_R=1-(W+\delta)=R-\delta,
\qquad
B_0\ge\frac{k}{R}.
\tag{8}
\]

The decreasing zero-radial diameter envelope

\[
M_0(z)=\frac{-z+\sqrt{4-3z^2}}2
\]

satisfies \(M_0(z)<1-z/2\) for \(z>0\).  From (2) and (8),

\[
A_0\le M_0(B_0)
<1-\frac{B_0}{2}
\le1-\frac{k}{2R}.
\]

Consequently

\[
\rho_L=1-A_0>\frac{k}{2R}>\frac{\eta}{2R}.
\tag{9}
\]

Combining (5), (8), and (9) gives

\[
\delta
>R-\frac12+\frac{\eta}{2R}
=:J(R).
\tag{10}
\]

The function \(J\) is strictly increasing.  Direct differentiation,
using \(E^2=1-RW\), gives

\[
4E(1+E)^2J'(R)
=
2E(1+E)(1+2E)-W(2R-1)>0.
\]

For \(R\le1/2\) the subtracted term is nonpositive.  For
\(R\ge1/2\), one has \(W(2R-1)\le1/8\), whereas the first term is
already greater than \(1/8\).  Moreover,

\[
J\!\left(\frac38\right)=\frac1{24}.
\]

Since \(\delta<1/24\) by (7), (10) forces \(R<3/8\).  Now

\[
(2-3R)^2-E^2=(3-8R)(1-R)>0,
\]

so \(E<2-3R\).  Using
\(\eta/R=W/(1+E)\), we obtain

\[
\frac{\eta}{R}>\frac13.
\]

Equation (9) gives \(\rho_L>1/6\), while (7) gives
\(4\delta<1/6\).  Thus (6) also holds in this case.

## 3. Both local V traces stop before the C interval

If \(T_1\) has positive support on \(r_2\), the supported-arm margin in
[`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md),
together with \(B_1\ge\rho_L\), gives

\[
u_{1\to2}<1-\rho_L<1-\delta.
\tag{11}
\]

If \(T_1\) has no positive support on \(r_2\), (11) is unnecessary.

Coverage of the center-free edge \(e_{1,2}\), the Vd cap, and (4) give

\[
A_2>1-B_1>\frac12+\rho_R,
\qquad
B_2\ge\rho_L.
\tag{12}
\]

Put

\[
M=\frac12+\rho_R,
\qquad
m=\rho_L.
\]

Equation (5) gives

\[
M\ge\frac12,\qquad 0<m<M,\qquad M+m<1.
\]

The one-third radial envelope in `2609`, together with coordinatewise
antitonicity of \(c_{\max}\), yields

\[
C_2
\le c_{\max}(M,m)
<1-\frac{m}{3}
=1-\frac{\rho_L}{3}.
\tag{13}
\]

By (6),

\[
1-\frac{\rho_L}{3}<1-\delta.
\tag{14}
\]

The C trace on \(r_2\) begins, in the coordinate measured from \(V_2\)
toward \(O\), at \(1-\delta\).  Equations (11), (13), and (14) show that
neither \(T_1\) nor \(T_2\) reaches that interval.  The adjacent Vd0 role on
the other side has no positive support there, and all nonlocal roles are
excluded by diameter locality.  Hence a nonempty interval of \(r_2\) is
uncovered.

Reflection proves the placement with \(T_5\) exceptional.  Therefore every
adjacent placement is impossible. \(\square\)
