# CE2, \(N_+=1\): Nonadjacent Vd Finite-Enclosure Obstruction

Status: Proven

This is the active finite-enclosure proof for the placement in which \(T_0\)
is the unique supercritical V triangle and the unique Vd1/Vd2 role
\(T_\tau\) is nonadjacent:

\[
\tau\in\{2,3,4\}.
\]

The proof converts the two residual boundary tails into one radial point that
lies beyond both the Vd trace and the C-triangle trace.

## 1. Signed center and residual data

Assume every V role other than \(T_0,T_\tau\) is nonsupercritical Vd0.
Use the signed center variables from
[`2109`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md):

\[
0<R<1,\qquad W=1-R,\qquad
E=\sqrt{1-RW},\qquad \eta=1-E,
\]

\[
T=\alpha+\delta,\qquad k=\eta+T.
\]

The initial endpoints of the two CE2 center intervals are

\[
x=\frac{k}{W},
\qquad
y=\frac{k}{R}.
\tag{1}
\]

The common endpoint-slack lemma in
[`2530`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2530_common_CE1_CE2_budget_lemmas.md)
gives

\[
\boxed{T<\frac12\min\{x,y\}.}
\tag{2}
\]

Let \((A_0,B_0)\) be the actual reaches of the supercritical role.  Thus

\[
A_0+B_0>1,
\qquad
A_0^2+A_0B_0+B_0^2\le1.
\tag{3}
\]

Using the interval-component calculus of
[`2019`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md),
let \(B\) and \(U\) be the farthest already covered extents on the two active
boundary edges, and put

\[
\rho_R=1-B,
\qquad
\rho_L=1-U.
\tag{4}
\]

Boundary handoffs through the intervening nonsupercritical roles force

\[
A_\tau\ge\rho_R,
\qquad
B_\tau\ge\rho_L.
\tag{5}
\]

The Vd1/Vd2 boundary cap in
[`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md)
therefore implies

\[
\rho_R+\rho_L<\frac12.
\tag{6}
\]

## 2. Diameter transfer gives large residual tails

Define

\[
M_0(q)=\frac{-q+\sqrt{4-3q^2}}2.
\]

We claim

\[
\boxed{B\le M_0(x),\qquad U\le M_0(y).}
\tag{7}
\]

We prove the first inequality; the second follows by reflection.  The exact
interval-component formula says that \(B\) is either \(B_0\) or the far
endpoint of the relevant center interval.

If \(B\) is the center endpoint, the C triangle contains points with
parameters \(x,B\) on adjacent boundary edges.  Its diameter is one, so

\[
x^2+xB+B^2\le1
\]

and \(B\le M_0(x)\).

Suppose instead that \(B=B_0\).  If \(A_0<x\), then the component on the
other active edge ends at \(A_0\), so \(U=A_0\).  Equation (6) would give

\[
A_0+B_0>\frac32,
\]

contradicting (3), which implies \(A_0+B_0\le2/\sqrt3<3/2\).  Hence
\(A_0\ge x\), and the endpoint-distance inequality gives

\[
B_0\le M_0(A_0)\le M_0(x),
\]

because \(M_0\) is decreasing.  This proves (7).

For every \(q>0\),

\[
1-M_0(q)>\frac q2.
\tag{8}
\]

Combining (2), (4), (7), and (8) gives

\[
\boxed{
\rho_R>\frac x2>T,
\qquad
\rho_L>\frac y2>T.
}
\tag{9}
\]

Put

\[
\rho=\min\{\rho_R,\rho_L\}.
\tag{10}
\]

Then \(T<\rho\).

## 3. Radial separation

The relevant C-triangle exits, measured from \(O\), are

\[
d_2^C=\delta,
\qquad
d_4^C=\alpha,
\qquad
d_3^C=
\min\left\{\frac{\alpha}{R},\frac{\delta}{W}\right\}.
\tag{11}
\]

The first two are strictly below \(T\).  For the third,

\[
d_3^C
\le
R\frac{\alpha}{R}
+
W\frac{\delta}{W}
=T.
\]

Thus, for every \(\tau\in\{2,3,4\}\),

\[
d_\tau^C<\rho.
\tag{12}
\]

The Vd own-radial margin in
[`201c`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md),
applied to (5), gives

\[
C_\tau<1-\rho.
\tag{13}
\]

Consider the point

\[
D_\tau=\rho V_\tau.
\tag{14}
\]

Equation (12) puts \(D_\tau\) beyond the C trace, while (13) puts it beyond
the own-radial trace of \(T_\tau\).  The two adjacent ordinary roles are Vd0
and have no positive trace on \(r_\tau\); all nonlocal roles are excluded by
diameter locality.  Hence \(D_\tau\) is uncovered.

All three nonadjacent placements are impossible. \(\square\)
