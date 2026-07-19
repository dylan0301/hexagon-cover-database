# Four-Cap Enclosure Reduction and Adjacent Overlaps

Status: Proven

This note proves the geometric part of the terminal nine-point enclosure
argument.  It handles the automatic disk region, replaces the two outer
frontier witnesses by exact Newton inner witnesses, reduces the remaining
problem to four consecutive cap overlaps, proves the ray and radius
hypotheses, and proves both adjacent overlaps analytically.  The two exact
mixed targets left by the reduction are treated in
[`31055_rational_radial_envelopes_and_mixed_reduction.md`](31055_rational_radial_envelopes_and_mixed_reduction.md)
and
[`31056_global_analytic_mixed_positivity.md`](31056_global_analytic_mixed_positivity.md).

## 1. Domain and support formula

Assume

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
\rho:=a^2+ab+b^2<1.
\tag{1}
$$

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
c_*=c_{\max}(p,q),
\qquad
h=\frac{\sqrt3}{2},
$$

and

$$
\eta=h(1-c_*).
$$

The exact radial envelope $c_{\max}$ is the one proved in
[`2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).
Let $Q_-,Q_0,Q_+$ be the three exact witnesses defined in
[`31053_direct_asymmetric_witness_forcing.md`](31053_direct_asymmetric_witness_forcing.md),
and set

$$
\mathcal D_\eta
=
\left\{X:\left\lVert X\right\rVert\le\eta\right\},
$$

$$
K_{\mathrm{wit}}(a,b)
=
\mathcal D_\eta
\mathbin\cup
\left\{Q_-,Q_0,Q_+\right\}.
\tag{2}
$$

For a compact plane set $K$, write

$$
h_K(n)=\max_{X\in K}\langle X,n\rangle
$$

and let $\Lambda(K)$ be the least side length of a closed equilateral
triangle containing $K$.  If $R$ denotes counterclockwise rotation through
$2\pi/3$, then

$$
\boxed{
\Lambda(K)
=
\frac1h
\min_{\left\lVert n\right\rVert=1}
\sum_{j=0}^2 h_K(R^j n).
}
\tag{3}
$$

Indeed, for a fixed unit normal $n$, the three supporting lines with outward
normals $n,Rn,R^2n$ form an equilateral triangle.  Translating the three
lines changes the location but not the sum of their signed support numbers,
and their side length is that sum divided by the altitude $h$.  The least
triangle at this orientation uses the three support numbers of $K$.
Minimizing over $n$ proves (3).

The disk in (2) alone gives

$$
\Lambda(K_{\mathrm{wit}})
\ge
\frac{3\eta}{h}
=3(1-c_*).
$$

Consequently

$$
\boxed{c_*\le\frac23
\quad\Longrightarrow\quad
\Lambda(K_{\mathrm{wit}})\ge1.}
\tag{4}
$$

It remains to consider $c_*>2/3$, for which

$$
0<\eta<\frac h3<\frac h2.
\tag{5}
$$

## 2. Newton inner witnesses

Put

$$
D=\sqrt{4\rho-3}.
$$

The strict inequalities in (1) imply $0<D<1$.  Retain the exact frontier
coefficients

$$
\alpha=\frac{h(b+2a-bD)}{2\rho},
\qquad
\beta=\frac{h(b-a+(a+b)D)}{2\rho},
$$

$$
\gamma=\frac{h(-b+a+(a+b)D)}{2\rho},
\qquad
\delta=\frac{h(2b+a-aD)}{2\rho}
$$

from `31053`, and normalize them by

$$
\bar\alpha=\frac\alpha h,
\quad
\bar\beta=\frac\beta h,
\quad
\bar\gamma=\frac\gamma h,
\quad
\bar\delta=\frac\delta h.
$$

In the local corner coordinates at $V_4$, the two frontier lines are

$$
L_3(\lambda)=(b-\beta\lambda,\alpha\lambda),
\qquad
L_5(\mu)=(\delta\mu,a-\gamma\mu).
$$

Their junction parameters are

$$
\lambda_*=\mu_*=\frac{8h\rho}{3(D+3)}.
$$

Use dimensionless parameters

$$
\xi=\frac\lambda h,
\qquad
\zeta=\frac\mu h,
\qquad
\xi_*=\zeta_*=\frac{8\rho}{3(D+3)}.
$$

The two line-circle restrictions are

$$
g_-(\xi)
=
\frac9{16}\xi^2
-\frac94(\bar\alpha+b\bar\beta)\xi
+3b^2-3b+2,
\tag{6}
$$

$$
g_+(\zeta)
=
\frac9{16}\zeta^2
-\frac94(\bar\delta+a\bar\gamma)\zeta
+3a^2-3a+2.
\tag{7}
$$

The complete fixed-line sign proof in
[`31052_fixed_line_circle_signs.md`](31052_fixed_line_circle_signs.md)
gives

$$
g_-(\xi_*)>0,
\qquad
g_-'(\xi_*)<0,
\qquad
g_+(\zeta_*)>0,
\qquad
g_+'(\zeta_*)<0,
\tag{8}
$$

and places the junction strictly before the first root of each quadratic.
Define one Newton step at the junction by

$$
\widehat\xi_-
=
\xi_*-
\frac{g_-(\xi_*)}{g_-'(\xi_*)},
\qquad
\widehat\zeta_+
=
\zeta_*-
\frac{g_+(\zeta_*)}{g_+'(\zeta_*)}.
\tag{9}
$$

For a strictly convex quadratic $g$, suppose $x$ precedes its first root
$r$ and $g(x)>0>g'(x)$.  Then

$$
x<x-\frac{g(x)}{g'(x)}<r.
$$

The first inequality is immediate.  Strict convexity puts the tangent line
at $x$ strictly below $g$ at $r$, so the tangent zero occurs before $r$.
Applying this observation to (6)--(9), define

$$
A^{\mathrm{loc}}
=
\left(
b-\frac34\bar\beta\widehat\xi_-,
\frac34\bar\alpha\widehat\xi_-
\right),
\tag{10}
$$

$$
B^{\mathrm{loc}}
=Q_0^{\mathrm{loc}}
=
\left(
\frac{2b+a-aD}{D+3},
\frac{b+2a-bD}{D+3}
\right),
\tag{11}
$$

$$
C^{\mathrm{loc}}
=
\left(
\frac34\bar\delta\widehat\zeta_+,
a-\frac34\bar\gamma\widehat\zeta_+
\right).
\tag{12}
$$

Convert a local point $(u,v)$ to the global vector

$$
V_4+u(V_5-V_4)+v(V_3-V_4).
\tag{13}
$$

Then

$$
A\in(Q_0,Q_-),
\qquad
C\in(Q_0,Q_+),
\tag{14}
$$

where the parentheses denote open line segments.  Thus, for

$$
\widehat K
=
\mathrm{conv}
\left(
\mathcal D_\eta\mathbin\cup\{A,B,C\}
\right),
$$

convexity and (14) give

$$
\widehat K\subseteq\mathrm{conv}(K_{\mathrm{wit}}).
\tag{15}
$$

Support functions are monotone under inclusion, so

$$
\Lambda(K_{\mathrm{wit}})\ge\Lambda(\widehat K).
\tag{16}
$$

All coordinates in (10)--(12) are rational functions of $a,b,D$.

## 3. Four-cap Minkowski reduction

For a point $X$ and $r\ge0$, put

$$
\mathbb D(X,r)
=
\left\{Y:\left\lVert Y-X\right\rVert\le r\right\}.
$$

Set

$$
S=\widehat K+R\widehat K+R^2\widehat K.
$$

Then $S$ is convex and $R$-invariant, and

$$
h_S(n)=\sum_{j=0}^2h_{\widehat K}(R^j n).
\tag{17}
$$

The three summands can contribute a witness point or the centered disk
independently.  Hence $S$ contains the full $R$-orbits of

$$
\mathbb D(A,2\eta),
\quad
\mathbb D(B,2\eta),
\quad
\mathbb D(C,2\eta),
\quad
\mathbb D(W,\eta),
\qquad
W=C+RA.
\tag{18}
$$

For example, $A+R\mathcal D_\eta+R^2\mathcal D_\eta$ is
$\mathbb D(A,2\eta)$, while $C+RA+R^2\mathcal D_\eta$ is
$\mathbb D(W,\eta)$.

For a disk $\mathbb D(X,r)$, define its level-$h$ cap of normal directions
by

$$
I(X,r)
=
\left\{
n:\left\lVert n\right\rVert=1,
\ \langle X,n\rangle+r\ge h
\right\}.
\tag{19}
$$

If the caps belonging to the disks in (18) cover the unit circle, then
$h_S(n)\ge h$ for every unit $n$.  Equations (3) and (17) then give
$\Lambda(\widehat K)\ge1$.

Put

$$
\tau=h-2\eta=h(2c_*-1)>0.
\tag{20}
$$

The required chain in the sector from $A$ to $RA$ is

$$
I(A,2\eta)
\longleftrightarrow
I(B,2\eta)
\longleftrightarrow
I(C,2\eta)
\longleftrightarrow
I(W,\eta)
\longleftrightarrow
I(RA,2\eta).
\tag{21}
$$

The first two overlaps follow from

$$
\frac{\mathrm{cross}(A,B)}{\left\lVert B-A\right\rVert}
\ge\tau,
\qquad
\frac{\mathrm{cross}(B,C)}{\left\lVert C-B\right\rVert}
\ge\tau,
\tag{22}
$$

provided both crosses are positive.  At the common outer normal of the first
two center points, for example, both equal-radius disks have support

$$
2\eta+
\frac{\mathrm{cross}(A,B)}{\left\lVert B-A\right\rVert},
$$

so (22) puts that normal in both caps.

For the two mixed overlaps, define

$$
\Delta=\mathrm{cross}(C,RA),
\qquad
u=\langle C,RA\rangle,
$$

and, for $X=A,C$,

$$
Z_X=\tau\left\lVert X\right\rVert^2-\eta u,
\tag{23}
$$

$$
P_X(\eta)
=
\left(\left\lVert X\right\rVert^2-\eta^2\right)\Delta^2
-Z_X^2.
\tag{24}
$$

If

$$
\left\lVert A\right\rVert,
\left\lVert C\right\rVert>\eta,
\qquad
\Delta>0,
\qquad
P_A(\eta),P_C(\eta)\ge0,
\tag{25}
$$

then

$$
\sqrt{\left\lVert X\right\rVert^2-\eta^2}\Delta
\ge
\left\lvert Z_X\right\rvert
\ge Z_X.
\tag{26}
$$

For $X=A$, equation (26) is equivalent to

$$
2\eta+
\frac{
\eta u+
\sqrt{\left\lVert A\right\rVert^2-\eta^2}\Delta
}{\left\lVert A\right\rVert^2}
\ge h.
\tag{27}
$$

The left side is the common support of $\mathbb D(C,2\eta)$ and
$\mathbb D(W,\eta)$ at their outer tangent normal.  The instance $X=C$ is
the corresponding common-support inequality for $\mathbb D(W,\eta)$ and
$\mathbb D(RA,2\eta)$.  Thus

$$
\boxed{P_A(\eta)\ge0,
\qquad
P_C(\eta)\ge0}
\tag{28}
$$

are the exact two mixed targets.

Every nonempty cap in (21) is a single arc of half-width less than $\pi/2$:
for the equal-radius caps this follows from $h-2\eta=\tau>0$, and for the
mixed-radius cap it follows from $h-\eta=hc_*>0$.  Once the five center rays
are in cyclic order and all consecutive crosses are positive, every overlap
in (21) occurs across the intervening short sector.  Hence the five caps
cover the sector from $A$ to $RA$, and their $R$-orbits cover the unit circle.

## 4. Ray order and radius hypotheses

Write the local coordinates of $A,B,C$ as $(u_X,v_X)$.  The coordinate
bounds in `31052`, together with the strict Newton placement (14), give

$$
0<u_A,v_A,u_B,v_B,u_C,v_C<1,
$$

$$
u_A<u_B<\frac12,
\qquad
v_C<v_B<\frac12.
\tag{29}
$$

The identities

$$
\alpha^2+\alpha\beta+\beta^2=h^2,
\qquad
\gamma^2+\gamma\delta+\delta^2=h^2
$$

and the two line directions give

$$
\frac{\mathrm{cross}(A,B)}{\left\lVert B-A\right\rVert}
=\alpha(1-b)+\beta>0,
\tag{30}
$$

$$
\frac{\mathrm{cross}(B,C)}{\left\lVert C-B\right\rVert}
=\gamma+\delta(1-a)>0.
\tag{31}
$$

All three points have negative global second coordinate by (29), so
(30)--(31) put their rays in the order $A,B,C$ in the lower half-plane.

For the remaining order, put

$$
X=1-u_A,
\qquad
Y=1-v_A,
\qquad
P=1-u_C,
\qquad
Q=1-v_C.
$$

Then $0<X,Y,P,Q<1$, while $X>1/2$ and $Q>1/2$.  In the basis

$$
E_0=V_5-V_4,
\qquad
E_1=V_3-V_4,
$$

the centered coefficient vectors are

$$
A=(-X,-Y),
\qquad
C=(-P,-Q),
\qquad
RA=(Y,Y-X).
$$

Therefore

$$
\frac{\Delta}{h}=PX+(Q-P)Y.
\tag{32}
$$

If $Q\ge P$, the right side is positive.  If $Q<P$ and $X\ge Y$, it is
again positive.  In the only remaining case, $Q<P$ and $X<Y$,

$$
PX-(P-Q)Y
>
\frac P2-(P-Q)
=Q-\frac P2
>0.
$$

Thus $\Delta>0$.  Since $W=C+RA$ is a positive sum of two nonopposite
vectors, its ray lies strictly between the rays of $C$ and $RA$.  Hence the
rays

$$
A, B, C, W, RA
\tag{33}
$$

occur in this cyclic order from $A$ to $RA$.

The same coordinates give

$$
\left\lVert A\right\rVert^2
=X^2+Y^2-XY
=\left(Y-\frac X2\right)^2+\frac34X^2
>\frac3{16}
=\left(\frac h2\right)^2.
$$

The reflected calculation using $Q>1/2$ gives
$\left\lVert C\right\rVert>h/2$.  By (5),

$$
\left\lVert A\right\rVert,
\left\lVert C\right\rVert
>\frac h2>\eta.
\tag{34}
$$

This proves every order, determinant, and radius condition in (25).

## 5. Analytic proof of both adjacent overlaps

By reflection, assume $a\le b$ and put

$$
m=1-b,
\qquad
M=1-a,
\qquad
U=a+b-1,
$$

$$
s=m+M=1-U,
\qquad
w=M-m.
$$

Then

$$
0<m\le M,
\qquad
0<U<\frac2{\sqrt3}-1<\frac16,
$$

$$
D=\sqrt{w^2+6U+3U^2}\in(0,1).
$$

Put

$$
\mathcal A=1-m+m^2,
\qquad
\rho=\mathcal A+U(1+m+U).
$$

The smaller of the two normalized line distances in (30)--(31) is

$$
d
=
\frac{
\mathcal A+U(2m-1)+D(\mathcal A+U)
}{2\rho}.
\tag{35}
$$

The other distance exceeds it by

$$
\frac{(b-a)U(1-D)}{2\rho}\ge0.
\tag{36}
$$

Thus it suffices to prove

$$
d\ge2c_*-1.
\tag{37}
$$

### 5.1 The quartic radial cell

Let

$$
\chi=s^4-s^2+mM.
$$

On $\chi\le0$, the exact radial formula says that $c_*$ is the unique
selected root in $[h,1]$ of

$$
F_m(z)=z^4-z^2+mz-m^2.
$$

Set

$$
r=1-\frac m2+\frac{m^2}{2}.
$$

Since $0<m<1/2$, one has $r\ge7/8>h$.  Direct substitution gives

$$
F_m(r)
=
\frac{m^2(m-1)}{16}
\left(
m^5-3m^4+11m^3-17m^2+28m-12
\right).
\tag{38}
$$

The polynomial in parentheses is strictly increasing on $(0,1/2)$ because
its derivative is

$$
28-34m+m^2(5m^2-12m+33)>0.
$$

Its value at $m=1/2$ is $-33/32$, so (38) is positive.  Also

$$
F_m(h)=-\left(m-\frac h2\right)^2\le0.
$$

Uniqueness of the selected root gives

$$
c_*\le r,
\qquad
2c_*-1\le1-m+m^2=\mathcal A.
\tag{39}
$$

Put

$$
X_0=\mathcal A+U,
$$

$$
Y_0
=
2\rho\mathcal A-\mathcal A-U(2m-1).
$$

Then

$$
d-\mathcal A
=
\frac{DX_0-Y_0}{2\rho}.
\tag{40}
$$

Exact expansion gives

$$
\begin{aligned}
Y_0={}&
2(m^2-m+1)U^2
+(2m^3-2m+3)U\\
&+(m^2-m+1)(2m^2-2m+1)>0.
\end{aligned}
$$

A second exact expansion gives

$$
D^2X_0^2-Y_0^2=4m\rho\Phi(U,m),
\tag{41}
$$

where

$$
\begin{aligned}
\Phi(U,m)={}&
(1-m)(m^2-m+2)U^2\\
&+(2-m^2)(m^2-m+1)U\\
&-m(1-m)^2(m^2-m+1).
\end{aligned}
$$

In these variables

$$
\chi
=
U^4-4U^3+5U^2-(m+2)U+m(1-m).
$$

Since $U^2(U^2-4U+5)>0$, the inequality $\chi\le0$ implies

$$
U>\frac{m(1-m)}{m+2}.
\tag{42}
$$

The polynomial $\Phi$ is strictly increasing in $U$.  At the right side of
(42),

$$
\Phi
=
\frac{
m^2(1-m)
\left(m^4-2m^3+6m^2-6m+4\right)
}{(m+2)^2}
>0.
$$

The last quartic equals

$$
(m^2-m)^2+5m^2-6m+4>0,
$$

because the remaining quadratic has negative discriminant.  Thus (41) is
positive.  Since $D,X_0,Y_0>0$, equation (40) gives

$$
d>\mathcal A\ge2c_*-1.
\tag{43}
$$

### 5.2 The radical radial cell

On $\chi>0$, put

$$
E=\sqrt{4s^2-3}.
$$

The identity

$$
4\chi=s^2E^2-w^2
$$

gives

$$
s>h,
\qquad
0\le w<sE,
\qquad
c_*=\frac{s+w}{1+E}.
\tag{44}
$$

For fixed $U$, formula (35) becomes

$$
d=\frac{1+D}{2}-U B(D,w),
\tag{45}
$$

where

$$
B(D,w)
=
\frac{(1+U)(3+D)+w(1-D)}{D^2+3}.
$$

Differentiate with respect to $w$ at fixed $U$.  Then

$$
0\le D'=\frac wD\le1,
\qquad
B_w=\frac{1-D}{D^2+3}\ge0.
$$

Writing the numerator of $B$ as $N$, direct differentiation gives

$$
B_D
=
\frac{
(1+U-w)(D^2+3)-2DN
}{(D^2+3)^2}
>-\frac{34}{27}.
\tag{46}
$$

Indeed, the first term in the numerator is positive, while

$$
1+U-w=2a>0,
\qquad
N<\frac76\mathbin\cdot4+1=\frac{17}{3},
$$

$$
D<1,
\qquad
D^2+3\ge3.
$$

If $B_D<0$, then $B_DD'\ge B_D$; if $B_D\ge0$, then $B_DD'\ge0$.
Consequently $B'=B_w+B_DD'>-34/27$.  Since $U<1/6$, equation (45) gives

$$
d'
<
\frac12+\frac16\frac{34}{27}
=\frac{115}{162}<1.
\tag{47}
$$

On the other hand,

$$
(2c_*-1)'=\frac2{1+E}\ge1.
\tag{48}
$$

Thus $d-(2c_*-1)$ decreases with $w$.  At $w=sE$, one has $\chi=0$ and
$c_*=s$.  This boundary point is admissible.  Indeed $h<s<1$ and

$$
D^2=4s^4-12s+9<1,
$$

because

$$
s^4-3s+2
=(s-1)(s^3+s^2+s-2)<0.
$$

The second factor is increasing and at $s=h$ equals

$$
h^3+h^2+h-2=\frac{7h-5}{4}>0.
$$

The two radial formulas agree at the boundary, and Section 5.1 gives
$d\ge2s-1$ there.  Monotonicity therefore proves (37) throughout the radical
cell.

Reflection and (36) now prove

$$
\frac{\alpha(1-b)+\beta}{h}\ge2c_*-1,
\qquad
\frac{\gamma+\delta(1-a)}{h}\ge2c_*-1.
\tag{49}
$$

By (20), (30), and (31), these are exactly the two adjacent overlaps in
(22).

## 6. Reduction theorem

For every $(a,b)$ in (1), the enclosure inequality is automatic when
$c_*\le2/3$.  When $c_*>2/3$, equations (15)--(16) give an inner set
$\widehat K$; equations (33)--(34) give the required ray order and radii; and
(49) gives both adjacent cap overlaps.  It remains only to prove the two exact
mixed residual signs (28), or the corresponding signs for concentric smaller
disks.  Once those signs hold, the cap chain (21) and its rotations cover the
unit circle, so

$$
\Lambda(K_{\mathrm{wit}})
\ge
\Lambda(\widehat K)
\ge1.
$$

This proves the stated four-cap reduction and every non-mixed geometric
inequality used by it. $\square$
