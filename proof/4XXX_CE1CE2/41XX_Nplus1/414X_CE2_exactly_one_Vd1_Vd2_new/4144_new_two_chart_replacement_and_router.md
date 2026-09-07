# CE1/CE2 Vd1--Supercritical Pair: Local Replacement Input

Status: Proven

This is the active replacement proof for the placement in which the unique
Vd1 role and the unique supercritical Vd0 role are adjacent, neither is based
at the center's unique midpoint, and every other V role is nonsupercritical
Vd0.  The replacement uses separate vertex charts.  It preserves the full
skeleton, produces six nonsupercritical Vd0 roles, and then invokes the type-independent N0 theorem. The input and
output gap ranks need not coincide.

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

## 3. One application of the two-vertex replacement

The local Vd1 inequalities give $a<1/2$, $a+c<1$, $a+B_1<1$ and

$$c_1^{\rm req}<\max\{1-a,1-B_1\}.$$

These are precisely the scalar inputs $(a,c,B,r)=(a,c,B_1,c_1^{\rm req})$
of [2614](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2614_two_vertex_replacement.md).
That lemma owns the separate $V_0,V_1$ charts, both minus/plus templates,
all strict margins, and preservation of the five affected skeleton pieces.
The four untouched roles are nonsupercritical, so its output has actual
$N_+'=0$, contrary to N0 in
[2612](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2612_fixed_witness_unification.md).

The input uses only the center-free shared edge and the C radial exit; no
CE2-only inequality occurred. Thus the reduced replacement is valid for CE1
as well as CE2. The original C triangle is unchanged, and no equality of
input and output gap ranks or preservation of the full hexagon is asserted.
$\square$
