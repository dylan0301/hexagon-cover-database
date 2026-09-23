# Fixed-start proof of the moving adjacent-triangle signs

Status: Proven

The exact frontier geometry is the strict supercritical AB-union theorem in
[20091](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20091_ab_union_curve_a_plus_b_gt_1.md).
This note replaces the expanded moving-junction polynomial calculations;
it does not change the frontier witnesses or their selected first roots.

## Definitions

Assume \(0<a,b<1\), \(a+b>1\), \(\rho=a^2+ab+b^2<1\), and put
\(h=\sqrt3/2\), \(U=a+b-1\), \(z=a-b\), \(D=\sqrt{4\rho-3}\).
Use cone coordinates with metric \(\mathsf q(u,v)=u^2+v^2-uv\), and normalized
frontier coefficients

\[
x=\frac{b+2a-bD}{2\rho},\quad y=\frac{b-a+(a+b)D}{2\rho},\quad
w=\frac{2b+a-aD}{2\rho},\quad v=\frac{-b+a+(a+b)D}{2\rho}.
\]

The two lines are \(P_-(k)=(b-yk,xk)\), \(P_+(k)=(wk,a-vk)\), with
common junction \(J\) at
\(k_*=(D^2+3)/(2(D+3))\in(3/8,1/2)\).
The circle centers are \(E_-=(1-b,2-b)\), \(E_+=(2-a,1-a)\).
Let \(k_-,k_+\) denote their first intersections with the corresponding lines.
The original parameters satisfy \(k=h\lambda\) or \(k=h\mu\).

## Two-coefficient bound

If \(x,y>0\), \(x^2+xy+y^2=1\), \(R>1\), \(0<c<1\), and
\(Rx+cy=1\), then

\[
cx<1/\sqrt3,\qquad x-y<2(1-c).
\]

Indeed \(cy<1-x\), so
\(c<(x+y)/(1+x)\) and
\(cx<x(x+y)/(1+x)\le(x+y)/2\le1/\sqrt3\).
Also \(1-c>(1-y)/(1+x)\); if \(x\ge y\), then
\(x-y\le1-y<(1+x)(1-c)<2(1-c)\), while the other case is immediate.

Here
\(x^2+xy+y^2=w^2+wv+v^2=1\) and
\((a+b)x+by=(a+b)w+av=1\). Consequently

\[
bx,aw<1/\sqrt3,\quad x-y<2(1-b),\quad w-v<2(1-a).
\]

## First roots and junction signs

The first circle restriction is

\[
f_b(k)=\mathsf q(P_-(k)-E_-)-1
=k^2-3(1-Ux)k+3b^2-3b+2.
\]

At the fixed parameter \(1/2\),

\[
f_b(1/2)=3(b-1/2)^2+3Ux/2>0,\qquad f'_b(1/2)<-3/2.
\]

Moreover \(f_b(1)=3(Ux-b(1-b))<0\), since
\(\rho=1+U(1+a)-b(1-b)<1\) and \(x<1\).
Thus \(k_*<1/2<k_-<1\). Reflection gives \(k_*<1/2<k_+<1\).
Both quadratics decrease before \(1/2\), so they are positive at the junction.

The identities

\[
D^2-(3U-z)^2=6U(1+z-U)>0,\quad
D^2-(3U+z)^2=6U(1-z-U)>0
\]

give \(J_u,J_v<1/2\). Coordinate positivity along the relevant segments can
also be checked without the old expanded polynomials: exact substitution gives
\(\rho-1=(y-b)(x+y-b)/x^2\).
Since \(x+y>1>b\), we get \(y<b\), and by reflection \(v<a\).
Thus both outer endpoints \(P_-(1),P_+(1)\) lie in \((0,1)^2\), as do the
junction and the two first-root points.

## Moving centers

Put \(Z_5(t)=(1+t,t)\), \(1-a\le t\le b\), and
\(F(P,t)=\mathsf q(P-Z_5(t))-1\). Since
\(F_t(P,t)=1+2t-P_u-P_v\), the positive junction value increases with \(t\).
On the opposite line,

\[
\frac{d}{dk}F(P_-(k),t)
=2k+(1-b)(2y+x)+t(y-x)
\ge2k-bx>3/4-1/\sqrt3>0.
\]

Hence \(F(P_-(k_-),t)>F(J,t)>0\).
On the correct line,
\(P_+(k_+)_u+P_+(k_+)_v=a+k_+(w-v)<2-a\).
Therefore \(F_t(P_+(k_+),t)>1-a>0\), and its value is zero at \(t=1-a\).
We conclude

\[
F(P_+(k_+),t)\ge0,\qquad F(J,t)>0,\qquad F(P_-(k_-),t)>0.
\]

Reflect \((u,v,a,b)\leftrightarrow(v,u,b,a)\) for the other adjacent center.
These are the same signs used by [31053](31053_direct_asymmetric_witness_forcing.md),
with the stronger coordinate-sum bound \(<2-a<3-2a\).
No candidate triangle changes these fixed witness definitions.
