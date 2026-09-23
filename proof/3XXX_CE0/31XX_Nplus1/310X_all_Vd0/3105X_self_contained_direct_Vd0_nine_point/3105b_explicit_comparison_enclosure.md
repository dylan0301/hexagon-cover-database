# Fixed-start disk-plus-three-point enclosure by explicit comparisons

Status: Proven (exact computer-assisted algebra; geometric inputs stated below)

This is the active Case F enclosure calculation. The original nine forced
points are unchanged. The older junction-start calculation in `31054`--`31056`
and its authenticated transcript remain independently checked historical
alternatives; their polynomial data do not certify the new points below.

## Geometric input and fixed objects

Use the strict handoffs and radial forcing of
[31051](31051_direct_radial_forcing.md), the fixed-line signs in
[31052](31052_fixed_line_circle_signs.md), and the original asymmetric forcing in
[31053](31053_direct_asymmetric_witness_forcing.md). Thus

\[
0<a,b<1,\qquad a+b>1,\qquad \rho=a^2+ab+b^2<1,\qquad
h=\sqrt3/2,\quad D=\sqrt{4\rho-3}.
\]

The fixed frontier witnesses are \(Q_-,Q_0,Q_+\). The actual forced disk is
\(\mathcal D_\eta\), where
\(\eta=h(1-c_*)\) and \(c_*=c_{\max}(1-b,1-a)\).
Let \(K_{\rm wit}=\mathcal D_\eta\cup\{Q_-,Q_0,Q_+\}\).
All seven open triangles, not merely the skeleton, are assumed to cover the
hexagon when these original witnesses are forced into the C triangle.

In the corner chart
\(\Psi_4(u,v)=V_4+u(V_5-V_4)+v(V_3-V_4)\), use normalized coefficients

\[
\alpha=\frac{b+2a-bD}{2\rho},\quad
\beta=\frac{b-a+(a+b)D}{2\rho},\quad
\delta=\frac{2b+a-aD}{2\rho},\quad
\gamma=\frac{-b+a+(a+b)D}{2\rho}.
\]

They satisfy \(\alpha^2+\alpha\beta+\beta^2=1\) and
\((a+b)\alpha+b\beta=1\), and the reflected identities. Set \(U=a+b-1\).
The frontier lines, now parameterized by \(k=h\lambda\), are

\[
P_-(k)=(b-\beta k,\alpha k),\qquad
P_+(k)=(\delta k,a-\gamma k).
\]

Their junction parameter is
\(k_*=(D^2+3)/(2(D+3))\in(3/8,1/2)\).
The first circle roots satisfy \(1/2<k_-,k_+<1\) by `31052`.
One Newton step at the **fixed parameter** \(1/2\) gives

\[
\widehat k_b=\frac{1+3(b-1/2)^2}{2-3U\alpha},\qquad
\widehat k_a=\frac{1+3(a-1/2)^2}{2-3U\delta}.
\]

Define \(A=\Psi_4(P_-(\widehat k_b))\), \(B=Q_0\),
\(C=\Psi_4(P_+(\widehat k_a))\).
Strict convexity of each circle-restriction quadratic puts its tangent zero
between \(1/2\) and the first root. Therefore

\[
A\in(Q_0,Q_-),\qquad C\in(Q_0,Q_+),\qquad
\widehat K:=\operatorname{conv}(\mathcal D_\eta\cup\{A,B,C\})
\subseteq\operatorname{conv}(K_{\rm wit}).
\]

These inner points belong to the C triangle by convexity. They are **not**
claimed to be missed individually by every V triangle.

The exposed-chain proof and supporting-line estimates in the paper's
`prop:technical-four-contact-geometry` apply because the points stay on the
same two open frontier segments. In particular, the lines through \(AB,BC\)
are unchanged. Their distances satisfy
\(d_{AB},d_{BC}\ge h-2\eta\).
The generic four-contact/Gram/radius-transfer identities are recorded in
[2611](../../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2611_four_contact_disk_enclosure.md).
They are geometric inputs, not results of a floating-point plot.

## One rational radius recipe

Reflect so \(a\ge b\), put \(m=1-a\), \(\omega=m(1-m)\), and let
\(C_L(m)\in[h,1]\) be the root of
\(F_m(c)=c^4-c^2+mc-m^2\). Set

\[
r=\frac{\omega(4-\omega)(3\omega^2-4\omega+4)}
 {8(4+2m-10\omega+6\omega^2-\omega^3)},\quad
\kappa=\frac{m-r}{r},\quad e_0=\max\{r,m-\kappa U\}.
\]

The denominator is positive. The following proof supplies the needed radius
bound without selecting a new component of an algebraic equation.
Let \(c_0=1-\omega/2\). On \([h,1]\), \(F_m\) is increasing and strictly
convex, and

\[
F_m(c_0)=\frac{m^2(1-m)}{16}
(12-28m+17m^2-11m^3+3m^4-m^5)>0.
\]

The last polynomial decreases on \([0,1/2]\), with derivative at most
\(-19/2\), and its endpoint value is \(33/32\).
The tangent zero \(c_1=c_0-F_m(c_0)/F'_m(c_0)\) lies above the selected root,
and \(r=1-c_1\). Hence
\(b_0:=\omega/2<r\le1-C_L(m)<m\).

For the other capacity branch write \(s=1-U\) and
\(g_m(s)=2(s-m)/(1+\sqrt{4s^2-3})\).
The exact capacity selector gives \(s>C_L(m)\) on this branch.
Direct differentiation gives \(g'_m\le0\) and \(g''_m>0\) on the relevant
interval. For the second sign, with \(E=\sqrt{4s^2-3}\), use
\(m/s\le1/\sqrt3<2/3\) and

\[
1+3E-2E^2-\frac43E^3\ge\frac23\qquad(0\le E\le1).
\]

The root equation gives \(g_m(C_L(m))\le C_L(m)\).
Thus \(c_*\le C_L(m)\) on both branches. On \(0<U<r\), convexity of
\(g_m(1-U)\), together with endpoint bounds \(1-m\) and \(1-r\), gives the
chord upper bound \(c_*\le1-m+(m-r)U/r\).
For \(U\ge r\), use \(1-c_*\ge r\). Consequently

\[
0<b_0\le r\le e_0\le e_*:=1-c_*,\qquad r\le1-h<1/6.
\]

Also \(1+m/2+2m^2\le\kappa\le3\); the lower bound follows by the positive
polynomial factor printed in the shared paper certificate. The affine bound
\(\ell=(1+5m)/2\le\kappa\) follows from
\(1+m/2+2m^2-\ell=2(m-1/2)^2\).

## Tangent reduction and explicit polynomial proof

Let \(R\) rotate through \(120^\circ\), \(X=A\), \(Y=R^{-1}C\),
\(\nu=\langle X,Y\rangle\), and
\(\Delta_0=\operatorname{cross}(Y,X)/h>0\).
Define

\[
Q_X(e)=\Delta_0^2-\|(1-2e)X-eY\|^2,
\quad Q_Y(e)=\Delta_0^2-\|(1-2e)Y-eX\|^2.
\]

The exact norm-ordering proof gives \(\|X\|^2\ge\|Y\|^2\) after reflection.
Thus
\(Q_Y-Q_X=(1-e)(1-3e)(\|X\|^2-\|Y\|^2)\ge0\) for \(e\le1/3\).
The point-numerator formulas and exact polynomial division in the
[mathematical supplement](3105X_computation/mathematical_supplement.md) define
\(\mathcal A,\mathcal B,\Pi\), not a separately supplied coefficient table:

\[
Q_X(e)=\frac{\rho^2}{2E_a^2E_b^2}(\mathcal A+D\mathcal B),\quad
\Pi=(1+3K)\mathcal A+K(3+K)\mathcal B,\quad K=D^2.
\]

All denominators are positive. The active exact checker proves the explicit
bounds, with their low-degree comparisons and error budgets:

* \(\mathcal B(m,U,b_0)>4\), \(\mathcal B(m,U,m)>210\), and
  \(\mathcal B_{ee}<-5600\). Concavity therefore gives
  \(\mathcal B(m,U,e_0)>4\).
* Four mixed-derivative bounds and \(\Pi_e\ge1152\) give coordinatewise
  monotonicity where \(U,e\ge b_0\). The constant-radius branch satisfies
  \(\Pi_U(m,U,r)>0\).
* The affine-path curvature at \(\ell=(1+5m)/2\), \(e=1/3\), is less than
  \(-21500\). Its mixed-derivative comparison extends this to the actual
  \(e=m-\kappa U\). The physical/path sign \(\Pi_{ee}<0\) is supplied by the
  positive-weight identity with weights \((1\pm D)^3\); it is not asserted
  indiscriminately for \(D>1\).
* The shared endpoint has \(\Pi(m,r,r)>1063/1700\). The affine left endpoints
  are positive. Concavity on the affine branch and monotonicity on the
  constant branch give \(\Pi(m,U,e_0)>0\) whenever \(e_0\le1/3\).

These are fully specified **exact computer-assisted** polynomial proofs.
The supplement prints the comparison models, the common completed-square
identities, the radius and domain arguments, and the remaining Taylor bounds.
The standalone program reconstructs all polynomials from the points and
checks each identity and coefficient bound over \(\mathbb Q\).
It has no external SOS witness file, no Bernstein-transcript input, no
optimizer, and no sampling sign test. The exact coefficient calculations
and the degree-27 shared-boundary comparison remain part of the proof.

Since
\(D(1+3D^2)-D^2(3+D^2)=D(1-D)^3\ge0\), positivity of \(\mathcal B\) gives

\[
\mathcal A+D\mathcal B\ge\frac{\Pi}{1+3K}>0.
\]

Hence \(Q_X(e_0),Q_Y(e_0)>0\).

## Enclosure conclusion and scope

If \(e_*\ge1/3\), the actual disk alone needs enclosing side at least one.
Otherwise \(e_0\le e_*<1/3\). Simultaneous radius transfer gives the paired
residuals at \(e_*\), and the Gram identities give both actual-radius tangent
contact bounds. The two straight-line contacts retain their analytic bounds
\(d_{AB}+2\eta,d_{BC}+2\eta\ge h\). All four exposed contacts therefore have
support sum at least \(h\), so

\[
\Lambda(K_{\rm wit})\ge\Lambda(\widehat K)\ge1.
\]

The disk used in this exposed-hull and line-contact argument always has radius
\(he_*\). Only the residual is tested initially at \(e_0\); the proof never
substitutes the coarse disk of radius \(hb_0\) into the geometric obstruction.

## Reproduction

```bash
python 3105X_computation/verify_explicit_stage.py --output /tmp/F-explicit.json
```

Run from this directory with Python and SymPy 1.14.0, without `-O`.
The output record is diagnostic proof bookkeeping, not an input witness.
The two older certificate programs continue to run separately to protect the
historical arrays. The new active result does not relabel those arrays as
certificates for its different point formulas.
