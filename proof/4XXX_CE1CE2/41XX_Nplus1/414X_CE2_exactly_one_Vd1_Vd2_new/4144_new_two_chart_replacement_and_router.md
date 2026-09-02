# CE2 Vd1--Supercritical Pair: Two-Chart Replacement and Finite-Enclosure Router

Status: Proven

This is the active replacement proof for the placement in which the unique
Vd1 role and the unique supercritical Vd0 role are adjacent, neither is based
at the center's unique midpoint, and every other V role is nonsupercritical
Vd0.  The replacement uses separate vertex charts.  It preserves the full
skeleton, produces six nonsupercritical Vd0 roles, and then routes according
to the **recomputed** output gap rank.

## 1. Normalized pair and Vd1 margins

Let the original open roles be \(U_C,U_0,\ldots,U_5\), with
\(T_C=\overline{U_C}\) and \(T_i=\overline{U_i}\).  After a fresh cyclic
renumbering, let \(T_0\) be Vd1, let \(T_1\) be supercritical, and suppose
\(M_1\in T_0\).  The shared edge is center-free, and no role other than
\(T_0,T_1\) has positive trace on \(r_0\) or \(r_1\).

Let \(a,b\) be the actual incident boundary reaches of \(T_0\).  By the
corner normal form in
[`2014`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md),
there are \(t\ge1\) and \(d=\sqrt{t^2+t+1}\) such that the exact own-radial
reach and the supported interval on \(r_1\) satisfy

\[
c=\frac{d-a-tb}{t+1},
\qquad
\lambda=\frac{t(1-b)}{t+1},
\qquad
u_{\rm adj}=\frac{d-a-tb-1}{t}.
\]

The strict midpoint and one-sided-support conditions give

\[
\boxed{
a+c<1,\qquad
a<\lambda\le\frac12,\qquad
b<\frac12,\qquad
u_{\rm adj}<1-a.
}
\tag{1}
\]

For completeness, the first inequality follows by evaluating \(a+c-1\) on
the closed midpoint face and using

\[
(2t^2+4t+1)^2-4(t+1)^2(t^2+t+1)
=
4t^3+4t^2-4t-3>0
\]

for \(t\ge1\).  The other three follow directly from the endpoint formulas
and the strict midpoint inequalities.

Let \((A_1,B_1,C_1)\) be the actual reaches of the supercritical role.  The
center-free shared edge gives

\[
A_1\ge1-b>\frac12,
\qquad
C_1\ge\lambda.
\tag{2}
\]

## 2. A half-square admissibility lemma

We use the exact local admissible set
[`2004`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).

### Lemma 2.1

If an admissible demand triple \((x,y,z)\) satisfies

\[
x\ge\frac12,
\qquad
0\le z\le\frac12,
\]

then

\[
y\le1-z.
\tag{3}
\]

### Proof

Suppose \(y>1-z\).  Then \(x+y>1\), so the selected supercritical cell
applies.  In the ordered half \(x\le y\), its necessary polynomial is

\[
F(x,y,z)
=
(x^2-1)z^2+(2xy^2+y)z+y^4-y^2
\le0.
\]

It is nondecreasing in \(x\).  Its derivative in \(y\), evaluated from
\(x=1/2\), is positive for \(y\ge1-z\), and

\[
F\!\left(\frac12,1-z,z\right)
=
\frac{z^2(2z-5)(2z-1)}4
\ge0.
\]

This is a contradiction.  In the reflected half \(y<x\), apply the same
argument to \(F(y,x,z)\); both arguments exceed \(1-z\), and the relevant
partial derivatives are positive there.  At the corner,

\[
F(1-z,1-z,z)=z(1-2z)\ge0,
\]

again contradicting the selected-cell inequality. \(\square\)

A supercritical role satisfies \(C_1\le1/2\) by the selected component
condition.  Applying the lemma to (2) gives

\[
B_1\le1-C_1\le1-\lambda.
\]

Since \(a<\lambda\),

\[
\boxed{a+B_1<1.}
\tag{4}
\]

Let \(d_1^C\) be the C-triangle reach on \(r_1\), measured from \(O\), and put

\[
c_1^{\rm req}=1-d_1^C.
\]

Only the center, \(U_1\), and the adjacent trace of \(U_0\) can contribute a
positive interval on \(r_1\).  Open skeleton coverage gives

\[
c_1^{\rm req}<\max\{C_1,u_{\rm adj}\}.
\]

Using (1) and Lemma 2.1,

\[
\boxed{
c_1^{\rm req}
<
\max\{1-B_1,1-a\}.
}
\tag{5}
\]

## 3. Replacement parameters

Put \(L=1-B_1\).  Equation (4) gives \(a<L\).  Since the supremum of
\(p\mapsto\max\{p,1-p\}\) on \((a,L)\) is
\(\max\{L,1-a\}\), equation (5) permits choices

\[
a<p_1<p_2<1-B_1
\tag{6}
\]

such that

\[
p_1<\frac12,
\qquad
1-p_1>c,
\qquad
\max\{p_2,1-p_2\}>c_1^{\rm req}.
\tag{7}
\]

Choose

\[
0<\varepsilon<
\min\left\{
p_1-a,\,
p_2-p_1,\,
1-B_1-p_2,\,
1-p_1-c,\,
\max\{p_2,1-p_2\}-c_1^{\rm req}
\right\}.
\tag{8}
\]

Every term is positive.

## 4. Two separate vertex charts

Use the \(V_0\)-chart

\[
X_0(x,y)
=
V_0+x(V_5-V_0)+y(V_1-V_0)
\]

and the \(V_1\)-chart

\[
X_1(x,y)
=
V_1+x(V_0-V_1)+y(V_2-V_1).
\]

Both carry the metric \(x^2+y^2-xy\).  For \(0\le p\le1/2\), set

\[
\Delta_p^-
=
\operatorname{conv}\{(0,1-p),(1,1-p),(0,-p)\},
\]

and, for \(1/2<p\le1\), set

\[
\Delta_p^+
=
\operatorname{conv}\{(p,0),(p,1),(p-1,0)\}.
\]

For \(0<\varepsilon<p\), the shifted open triangle

\[
D_{p,\varepsilon}^-
=
\operatorname{int}(\Delta_p^-)+(-\varepsilon,0)
\]

contains the origin and has closed reaches

\[
(p-\varepsilon,\,1-p,\,1-p)
\tag{9}
\]

on the two positive axes and the diagonal.  It has no positive trace on
either neighboring support line.  For \(0<\varepsilon<1-p\),

\[
D_{p,\varepsilon}^+
=
\operatorname{int}(\Delta_p^+)+(0,-\varepsilon)
\]

contains the origin and has reaches

\[
(p,\,1-p-\varepsilon,\,p).
\tag{10}
\]

It likewise has no positive neighboring support.  These formulas follow by
substitution in the three defining half-planes.

Define

\[
U_0'=X_0(D_{p_1,\varepsilon}^-)
\]

and

\[
U_1'
=
\begin{cases}
X_1(D_{p_2,\varepsilon}^-),&p_2\le1/2,\\
X_1(D_{p_2,\varepsilon}^+),&p_2>1/2.
\end{cases}
\tag{11}
\]

Their closures contain \(V_0,V_1\) in their interiors.  By (9)--(10), each
boundary sum equals \(1-\varepsilon<1\), and neither has positive adjacent
support.  Hence both are nonsupercritical Vd0 roles.

## 5. Preservation of the full skeleton

Only

\[
e_{5,0},\quad e_{0,1},\quad e_{1,2},\quad r_0,\quad r_1
\]

can be affected.

- By (6)--(8), the \(V_0\) replacement reaches
  \(p_1-\varepsilon>a\) on \(e_{5,0}\), so it contains the former Vd1
  boundary trace.
- Its own-radial reach is \(1-p_1>c\), so it contains the former trace on
  \(r_0\).
- On the shared edge, the two new reaches satisfy
  \[
  (1-p_1)+(p_2-\varepsilon)
  =
  1+(p_2-p_1-\varepsilon)>1,
  \]
  so their open traces overlap and cover \(e_{0,1}\).
- The \(V_1\) replacement reaches more than \(B_1\) on \(e_{1,2}\) by
  (6)--(8).
- Its own-radial reach is \(\max\{p_2,1-p_2\}>c_1^{\rm req}\), so it
  overlaps the center trace and preserves all of \(r_1\).

All other skeleton components are unchanged.  Thus the modified seven open
roles still cover the full skeleton, the C triangle remains CE2, and all six
V roles are now nonsupercritical Vd0.

## 6. Recompute the output gap rank

Let \(N'_{\rm gap}\) be computed from the modified **open** boundary traces.
No equality with the input gap rank is asserted.

- If \(N'_{\rm gap}=0\), the boundary-complete length row Z0 in
  [`2531`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2531_length_budget_corollaries.md)
  gives a contradiction.
- If \(N'_{\rm gap}=1\), the all-Vd0 common-disk-plus-gap proof
  [`4013_new`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md)
  applies.
- If \(N'_{\rm gap}=2\), the CE2 two-gap short-ray theorem in
  [`2609`](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2609_simplified_finite_enclosure_lemmas.md)
  applies.

These alternatives are exhaustive.  Undoing the local renumbering and
reflection proves every replacement placement. \(\square\)
