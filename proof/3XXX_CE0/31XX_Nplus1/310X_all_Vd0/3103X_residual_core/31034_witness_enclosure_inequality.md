# Witness Enclosure Inequality

Status: Proven

The witness-membership obligations of the residual-core route are proved in
[`31032_symmetric_witness_construction.md`](31032_symmetric_witness_construction.md)
and
[`31033_asymmetric_witness_construction.md`](31033_asymmetric_witness_construction.md).
This note proves the remaining terminal enclosure inequality. The proof uses
an analytic adjacent-line estimate and an outward-rounded certificate for two
mixed cap overlaps. It also retains the exact finite support-event reduction
and falsification audit that led to the proof.

## 1. Exact target and the automatic disk region

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

The forced disk proved in `31032` is

$$
\mathcal D_\eta=\left\{x:\lVert x\rVert\le\eta\right\}.
$$

Let $Q_-,Q_0,Q_+$ be the exact points defined in `31033`, and set

$$
K_{\mathrm{wit}}
=
\mathcal D_\eta\mathbin\cup\{Q_-,Q_0,Q_+\}.
$$

For a unit vector $n$,

$$
h_{K_{\mathrm{wit}}}(n)
=
\max\left\{
\eta,
\langle Q_-,n\rangle,
\langle Q_0,n\rangle,
\langle Q_+,n\rangle
\right\}.
\tag{1}
$$

Writing $R$ for counterclockwise rotation through $2\pi/3$, the terminal
target is

$$
\boxed{
\Lambda(K_{\mathrm{wit}})
=
\frac1h
\min_{\lVert n\rVert=1}
\sum_{j=0}^2 h_{K_{\mathrm{wit}}}(R^j n)
\ge1.
}
\tag{2}
$$

It is quantified over the full strict domain

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
\rho:=a^2+ab+b^2<1.
\tag{3}
$$

Equation (1) gives

$$
\Lambda(K_{\mathrm{wit}})
\ge\frac{3\eta}{h}
=3(1-c_*).
$$

Therefore (2) is automatic when

$$
\boxed{c_*\le\frac23.}
\tag{4}
$$

Only $c_*>2/3$ remains below. In this region

$$
\eta<\frac h3.
\tag{5}
$$

## 2. Exact finite support-event audit

This section records an exact active-support partition independently of the
later cap proof. Put

$$
q_1=Q_-,
\qquad
q_2=Q_0,
\qquad
q_3=Q_+,
$$

and let $J_{90}$ denote counterclockwise rotation through $\pi/2$.
The strict root inequalities in `31033` put $Q_-$ and $Q_+$ strictly away
from $Q_0$ on two distinct line pieces, so the three points are pairwise
distinct.

**Proposition 2.1.** For fixed $(a,b)$ in (3), the minimum in (2) is attained
at one of at most twelve support-tie orientations, except that one arbitrary
orientation must also be tested for the constant all-disk case. The
point--point tie normals are

$$
n=\mathbin\pm
\frac{J_{90}(q_\ell-q_k)}{\lVert q_\ell-q_k\rVert},
\qquad
1\le k<\ell\le3,
\tag{6}
$$

and the disk--point tie normals are

$$
n=
\frac{
\eta q_k
\mathbin\pm
\sqrt{\lVert q_k\rVert^2-\eta^2}J_{90}q_k
}{\lVert q_k\rVert^2},
\qquad
\lVert q_k\rVert\ge\eta.
\tag{7}
$$

*Proof.* Partition the orientation circle into cells on which the active
support label in each of the three directions is fixed. On the relative
interior of such a cell, the support sum has the form

$$
H(\theta)
=
k\eta+
\sum_{j\text{ with point support}}
\langle q_{\ell_j},n_j(\theta)\rangle.
$$

Every active point projection is strictly larger than $\eta>0$. Unless all
three labels are the disk,

$$
H''(\theta)
=-
\sum_{j\text{ with point support}}
\langle q_{\ell_j},n_j(\theta)\rangle
<0.
$$

Thus a nonconstant cell has no interior minimum. A global minimum lies on a
cell boundary, where one direction has a point--point or disk--point tie.
Cyclic relabeling lets that direction be $n_0$. Equations (6) and (7) are the
complete unit-normal solutions of the two tie equations. An all-disk cell
either has a boundary already in (7), or is constant on the whole circle.
This proves the proposition. $\square$

The later proof does not need to decide which of these events is active. It
replaces their case analysis by a support-dominating Minkowski construction.

## 3. Junction-tangent inner witnesses

The selected first circle roots in `31033` contain an additional square
radical. For the terminal estimate it is useful to move each outer witness
toward $Q_0$ by one exact tangent, or Newton, step.

Retain the coefficients $\alpha,\beta,\gamma,\delta$ and discriminant

$$
D=\sqrt{4\rho-3}
$$

from `31033`, and write

$$
\bar\alpha=\frac{\alpha}{h},
\qquad
\bar\beta=\frac{\beta}{h},
\qquad
\bar\gamma=\frac{\gamma}{h},
\qquad
\bar\delta=\frac{\delta}{h}.
$$

Use the dimensionless parameters

$$
\xi=\frac{\lambda}{h},
\qquad
\zeta=\frac{\mu}{h},
\qquad
\xi_*=\zeta_*=\frac{8\rho}{3(D+3)}.
$$

The two line--circle restrictions are

$$
g_-(\xi)
=
\frac9{16}\xi^2
-\frac94(\bar\alpha+b\bar\beta)\xi
+3b^2-3b+2,
\tag{8}
$$

and

$$
g_+(\zeta)
=
\frac9{16}\zeta^2
-\frac94(\bar\delta+a\bar\gamma)\zeta
+3a^2-3a+2.
\tag{9}
$$

Define

$$
\widehat\xi_-
=
\xi_*-\frac{g_-(\xi_*)}{g_-'(\xi_*)},
\qquad
\widehat\zeta_+
=
\zeta_*-\frac{g_+(\zeta_*)}{g_+'(\zeta_*)}.
\tag{10}
$$

The fixed-line certificate used in `31033` proves that the junction precedes
the first root of each quadratic. Hence

$$
g_-(\xi_*)>0,
\qquad
g_-'(\xi_*)<0,
\qquad
g_+(\zeta_*)>0,
\qquad
g_+'(\zeta_*)<0.
$$

For a strictly convex quadratic $g$, a point $x$ before its first root $r$
has

$$
x<x-\frac{g(x)}{g'(x)}<r.
$$

Indeed, the first inequality follows from $g(x)>0>g'(x)$. The tangent line at
$x$ has value strictly below $g(r)=0$ at $r$, so its zero lies before $r$.
Consequently the points

$$
A^{\mathrm{loc}}
=
\left(
b-\frac34\bar\beta\widehat\xi_-,
\frac34\bar\alpha\widehat\xi_-
\right),
\tag{11}
$$

$$
B^{\mathrm{loc}}=Q_0^{\mathrm{loc}}=J,
\tag{12}
$$

and

$$
C^{\mathrm{loc}}
=
\left(
\frac34\bar\delta\widehat\zeta_+,
a-\frac34\bar\gamma\widehat\zeta_+
\right)
\tag{13}
$$

satisfy

$$
A\in(Q_0,Q_-),
\qquad
C\in(Q_0,Q_+).
\tag{14}
$$

Here the intervals are the open line segments and local points are converted
to global points by the convention in `31033`. All coordinates in
(11)--(13) are rational functions of $a,b,D$.

Put

$$
\widehat K
=
\mathrm{conv}\left(
\mathcal D_\eta\mathbin\cup\{A,B,C\}
\right).
$$

Equation (14) gives

$$
\widehat K
\subseteq
\mathrm{conv}(K_{\mathrm{wit}}).
\tag{15}
$$

Support functions are monotone under inclusion, so

$$
\Lambda(K_{\mathrm{wit}})\ge\Lambda(\widehat K).
\tag{16}
$$

It is therefore enough to prove $\Lambda(\widehat K)\ge1$.

## 4. Four-cap Minkowski reduction

For a point $X$ and $r\ge0$, write

$$
\mathbb{D}(X,r)
=
\left\{Y:\lVert Y-X\rVert\le r\right\}.
$$

Write $\mathrm{cross}(X,Y)$ for the oriented Cartesian determinant of the
two vectors.

Set

$$
S=\widehat K+R\widehat K+R^2\widehat K.
$$

Then $S$ is convex and invariant under $R$, and

$$
h_S(n)
=
\sum_{j=0}^2h_{\widehat K}(R^j n).
\tag{17}
$$

The three summands can independently contribute one witness point or the
centered disk. Hence $S$ contains the full $R$-orbits of

$$
\mathbb{D}(A,2\eta),
\quad
\mathbb{D}(B,2\eta),
\quad
\mathbb{D}(C,2\eta),
\quad
\mathbb{D}(W,\eta),
\qquad
W=C+RA.
\tag{18}
$$

For a disk $\mathbb{D}(X,r)$, define its level-$h$ cap of normal directions by

$$
I(X,r)
=
\left\{
n:\lVert n\rVert=1,\ \langle X,n\rangle+r\ge h
\right\}.
\tag{19}
$$

If the caps in (18) cover the unit circle, then $h_S(n)\ge h$ for every unit
$n$, and (17) gives $\Lambda(\widehat K)\ge1$.

Put

$$
\tau=h-2\eta=h(2c_*-1).
$$

Suppose the rays of

$$
A,\ B,\ C,\ W,\ RA
\tag{20}
$$

occur in that cyclic order in the sector from $A$ to $RA$. The equal-radius
cap overlaps are ensured by

$$
\mathrm{cross}(A,B)^2
\ge
\tau^2\lVert B-A\rVert^2,
\tag{21}
$$

and

$$
\mathrm{cross}(B,C)^2
\ge
\tau^2\lVert C-B\rVert^2,
\tag{22}
$$

provided the displayed crosses are positive.

For example, the common outer-normal support of the first pair is

$$
2\eta+
\frac{\mathrm{cross}(A,B)}{\lVert B-A\rVert}.
$$

Since $\tau>0$, requiring this value to be at least $h$ is exactly (21), and
the corresponding tie normal then belongs to both caps. The second pair is
identical. Only this sufficient implication is used below.

For the two mixed overlaps, put

$$
\Delta=\mathrm{cross}(C,RA),
\qquad
u=\langle C,RA\rangle,
$$

and, for $X=A,C$,

$$
Z_X=\tau\lVert X\rVert^2-\eta u,
\tag{23}
$$

$$
P_X
=
\left(\lVert X\rVert^2-\eta^2\right)\Delta^2-Z_X^2.
\tag{24}
$$

If

$$
\lVert A\rVert,\lVert C\rVert>\eta,
\qquad
\Delta>0,
\qquad
P_A,P_C\ge0,
\tag{25}
$$

then

$$
\sqrt{\lVert X\rVert^2-\eta^2}\Delta
\ge
\lvert Z_X\rvert
\ge Z_X.
\tag{26}
$$

For $X=A$, (26) is precisely

$$
2\eta+
\frac{
\eta u+\sqrt{\lVert A\rVert^2-\eta^2}\Delta
}{\lVert A\rVert^2}
\ge h.
\tag{27}
$$

This is the common support of $\mathbb{D}(C,2\eta)$ and
$\mathbb{D}(W,\eta)$ at their outer tangent normal. The $X=C$ instance is the
corresponding common-support inequality for $\mathbb{D}(W,\eta)$ and
$\mathbb{D}(RA,2\eta)$.

Thus (21), (22), and (25) give four consecutive cap overlaps along the sector
in (20):

$$
I(A,2\eta)
\leftrightarrow
I(B,2\eta)
\leftrightarrow
I(C,2\eta)
\leftrightarrow
I(W,\eta)
\leftrightarrow
I(RA,2\eta).
$$

Here $\tau>0$ and $h-\eta=hc_*>0$, so every nonempty cap in the chain is a
single arc with half-width less than $\pi/2$. The four overlap inequalities
make all five caps nonempty. Since each consecutive center-ray gap is less
than $\pi$, their overlap occurs across that intervening short sector.
Therefore these overlaps cover the whole sector from $A$ to $RA$. Rotation
by $R$ covers the other two sectors. This proves the following reduction.

**Proposition 4.1.** Under the ray order (20), inequalities
(21), (22), and (25) imply

$$
\Lambda(\widehat K)\ge1.
\tag{28}
$$

## 5. Exact order and radius hypotheses

Write the global image of a $V_4$-local point $(u,v)$ as

$$
V_4+u(V_5-V_4)+v(V_3-V_4).
$$

The coordinate proof in `31033`, together with (14), gives

$$
0<u_A,v_A,u_B,v_B,u_C,v_C<1,
\qquad
u_A<u_B<\frac12,
\qquad
v_C<v_B<\frac12.
\tag{29}
$$

The two line directions and the identities

$$
\alpha^2+\alpha\beta+\beta^2=h^2,
\qquad
\gamma^2+\gamma\delta+\delta^2=h^2
$$

give

$$
\frac{\mathrm{cross}(A,B)}{\lVert B-A\rVert}
=
\alpha(1-b)+\beta>0,
\tag{30}
$$

and

$$
\frac{\mathrm{cross}(B,C)}{\lVert C-B\rVert}
=
\gamma+\delta(1-a)>0.
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

Then $0<X,Y,P,Q<1$, while $X>1/2$ and $Q>1/2$. In the basis

$$
E_0=V_5-V_4,
\qquad
E_1=V_3-V_4,
$$

the centered coefficient vectors of $A,C,RA$ are

$$
A=(-X,-Y),
\qquad
C=(-P,-Q),
\qquad
RA=(Y,Y-X).
$$

Consequently

$$
\frac{\Delta}{h}
=
PX+(Q-P)Y.
\tag{32}
$$

If $Q\ge P$, the right side is positive. If $Q<P$ and $X\ge Y$, it is again
positive. In the only remaining case, $Q<P$ and $X<Y$,

$$
PX-(P-Q)Y
>
\frac P2-(P-Q)
=Q-\frac P2
>0.
$$

Thus $\Delta>0$. Since $W=C+RA$ is a positive sum of two vectors whose angle
is less than $\pi$, its ray lies strictly between the rays of $C$ and $RA$.
This proves (20).

The same centered coordinates give

$$
\lVert A\rVert^2
=
X^2+Y^2-XY
=
\left(Y-\frac X2\right)^2+\frac34X^2
>
\frac3{16}
=
\left(\frac h2\right)^2.
$$

The analogous calculation using $Q>1/2$ gives $\lVert C\rVert>h/2$. By (5),

$$
\lVert A\rVert,\lVert C\rVert>\frac h2>\eta.
\tag{33}
$$

Therefore all geometric and sign hypotheses of Proposition 4.1 have now been
proved except the four overlap inequalities.

## 6. Analytic proof of the adjacent overlaps

By reflection, assume in this section that $a\le b$, and put

$$
m=1-b,
\qquad
M=1-a,
\qquad
U=a+b-1,
\qquad
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

and

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
\frac{\alpha(1-b)+\beta}{h}
=
\frac{
\mathcal A+U(2m-1)+D(\mathcal A+U)
}{2\rho}.
\tag{34}
$$

Indeed, the other distance exceeds it by

$$
\frac{(b-a)U(1-D)}{2\rho}\ge0.
\tag{35}
$$

It is enough to prove

$$
d\ge2c_*-1.
\tag{36}
$$

### 6.1 The $C_L(m)$ radial cell

Let

$$
\chi=s^4-s^2+mM.
$$

On $\chi\le0$, the selected radial value $c_*=C_L(m)$ is the unique root in
$[h,1]$ of

$$
F_L(z)=z^4-z^2+mz-m^2.
$$

Set

$$
r=1-\frac m2+\frac{m^2}{2}.
$$

Since $0<m<1/2$, one has $r\ge7/8>h$. Direct substitution gives

$$
F_L(r)
=
\frac{m^2(m-1)}{16}
\left(
m^5-3m^4+11m^3-17m^2+28m-12
\right).
\tag{37}
$$

The polynomial in parentheses is strictly increasing on $(0,1/2)$ because
its derivative is

$$
28-34m+m^2(5m^2-12m+33)>0.
$$

Its value at $m=1/2$ is $-33/32$, so (37) is positive. Also

$$
F_L(h)=-\left(m-\frac h2\right)^2\le0.
$$

Uniqueness of the selected root gives

$$
c_*\le r,
\qquad
2c_*-1\le1-m+m^2=\mathcal A.
\tag{38}
$$

It remains to prove $d\ge\mathcal A$. Put

$$
X_0=\mathcal A+U,
$$

and

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
\tag{39}
$$

The exact expansion

$$
\begin{aligned}
Y_0={}&
2(m^2-m+1)U^2
+(2m^3-2m+3)U\\
&+(m^2-m+1)(2m^2-2m+1)
\end{aligned}
$$

shows $Y_0>0$. A second exact expansion gives

$$
D^2X_0^2-Y_0^2
=
4m\rho\Phi(U,m),
\tag{40}
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

Since $U^2(U^2-4U+5)>0$, the assumption $\chi\le0$ implies

$$
U>\frac{m(1-m)}{m+2}.
\tag{41}
$$

Both coefficients of the positive powers of $U$ in $\Phi$ are positive, so
$\Phi$ is strictly increasing in $U$. At the right side of (41),

$$
\Phi
=
\frac{
m^2(1-m)
\left(m^4-2m^3+6m^2-6m+4\right)
}{(m+2)^2}
>0.
$$

The last quartic is

$$
(m^2-m)^2+5m^2-6m+4>0;
$$

the remaining quadratic has negative discriminant. Thus (40) is positive.
Since $D,X_0,Y_0>0$, equation (39) gives

$$
d>\mathcal A\ge2c_*-1.
\tag{42}
$$

### 6.2 The other radial cell

On $\chi>0$, put

$$
E=\sqrt{4s^2-3}.
$$

Since

$$
4\chi=s^2E^2-w^2,
$$

one has

$$
s>h,
\qquad
0\le w<sE,
\qquad
c_*=\frac{s+w}{1+E}.
\tag{43}
$$

For fixed $U$, formula (34) can be rewritten as

$$
d
=
\frac{1+D}{2}-UB(D,w),
\tag{44}
$$

where

$$
B(D,w)
=
\frac{
(1+U)(3+D)+w(1-D)
}{D^2+3}.
$$

Differentiate with respect to $w$ at fixed $U$. Then

$$
D'=\frac wD\le1.
$$

At fixed $D$,

$$
B_w=\frac{1-D}{D^2+3}\ge0.
$$

Writing the numerator of $B$ as $N$, one has

$$
B_D
=
\frac{
(1+U-w)(D^2+3)-2DN
}{(D^2+3)^2}
>-\frac{34}{27}.
$$

Indeed,

$$
N
<
\frac76\mathbin\cdot4+1
=
\frac{17}{3},
\qquad
D<1,
\qquad
D^2+3\ge3,
$$

and the first term in the numerator of $B_D$ is positive. Now
$B'=B_w+B_DD'$. If $B_D\ge0$ the desired lower bound is immediate; if
$B_D<0$, then $0\le D'\le1$ gives $B_DD'\ge B_D$. Hence in both cases
$B'>-34/27$. Equations (44) and
$U<1/6$ give

$$
d'
<
\frac12+\frac16\frac{34}{27}
=
\frac{115}{162}
<1.
\tag{45}
$$

On the other hand,

$$
(2c_*-1)'=\frac2{1+E}\ge1.
\tag{46}
$$

Thus $d-(2c_*-1)$ is strictly decreasing in $w$. At $w=sE$, the selector
satisfies $\chi=0$. This is an admissible boundary point: $h<s<1$ and
$0<E<1$ give $0<m\le M<1$, while

$$
D^2=4s^4-12s+9<1.
$$

Indeed,

$$
s^4-3s+2
=(s-1)(s^3+s^2+s-2)<0
$$

for $h<s<1$: the first factor is negative, while the second is increasing
from

$$
h^3+h^2+h-2=\frac{7h-5}{4}>0.
$$

The two radial formulas agree at this boundary and $c_*=s$. The result of
Section 6.1 gives $d\ge2s-1$ there. Therefore (36) holds for every $w<sE$
as well.

Reflection and (35) now prove both inequalities

$$
\frac{\alpha(1-b)+\beta}{h}\ge2c_*-1,
\qquad
\frac{\gamma+\delta(1-a)}{h}\ge2c_*-1
\tag{47}
$$

throughout (3). By (30)--(31), these are exactly (21)--(22).

## 7. Outward-rounded certificate for the mixed overlaps

It remains to prove $P_A,P_C\ge0$ from (24). This is the only
computer-assisted part of the proof. The self-contained verifier is

[`3103X_computation/verify_tangent_witness_mixed_overlap.py`](3103X_computation/verify_tangent_witness_mixed_overlap.py).

### 7.1 Radical-free certificate quantities

Reflection lets the verifier assume

$$
z=a-b\ge0.
$$

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
s=p+q=1-U,
\qquad
m=q,
\qquad
z=p-q.
$$

Represent a global vector as $(x,hy)$ and put

$$
C'=R^{-1}C.
$$

If $A=(x_A,hy_A)$ and $C'=(x',hy')$, define

$$
\Delta_0=x_Ay'-y_Ax',
\qquad
u=\langle A,C'\rangle.
$$

Then

$$
\Delta=-h\Delta_0,
\qquad
u=\langle C,RA\rangle.
$$

For $X=A,C$, put

$$
r_X^0
=
\lVert X\rVert^2-\frac34(1-c_*)^2,
$$

$$
\ell_X^0
=
(1-c_*)u-(2c_*-1)\lVert X\rVert^2,
$$

and

$$
P_X^0
=
r_X^0\Delta_0^2-(\ell_X^0)^2.
\tag{48}
$$

Since $\eta=h(1-c_*)$, equations (23)--(24) give

$$
r_X^0=\lVert X\rVert^2-\eta^2,
\qquad
P_X=h^2P_X^0.
$$

The verifier simultaneously proves

$$
r_A^0,r_C^0\ge0,
\qquad
\Delta_0\le0,
\qquad
P_A^0,P_C^0\ge0.
\tag{49}
$$

Both $P$ inequalities are checked on the same half-domain. This is essential:
reflection by itself would exchange them at the swapped parameter and would
not prove both at a fixed asymmetric parameter.

### 7.2 Complete parameter charts

On the $C_L(m)$ radial sheet, set

$$
x=2c_*-\sqrt{4c_*^2-3}=1+t.
$$

The identities

$$
c_*=\frac{x^2+3}{4x},
\qquad
m=
\frac{(x^2+3)(x-1)(x+3)}{16x^2}
\tag{50}
$$

parameterize the selected root. The root and selector signs give
$s\le c_*$. More explicitly, $p\ge q=m$ gives $s\ge2m$, and
$F_L(c_*)=0$ is quadratic in $m$. Thus $m\le c_*/2$ selects

$$
m=\frac{c_*}{2}\left(1-\sqrt{4c_*^2-3}\right),
$$

which is exactly the second identity in (50). Put

$$
v=c_*-s.
$$

The domain bound

$$
U<\frac2{\sqrt3}-1<\frac4{25}
$$

gives the enclosing rectangle

$$
0\le t\le\frac34,
\qquad
0\le v\le\frac4{25}.
\tag{51}
$$

Indeed, $x\le\sqrt3<7/4$ and $v\le U$.
The second rational comparison follows after squaring from
$2500<2523$.

On the other radial sheet, set

$$
x=2s-\sqrt{4s^2-3}=1+t,
\qquad
E=\frac{3-x^2}{2x}.
$$

Then

$$
s=\frac{x^2+3}{4x},
\qquad
c_*=s-v,
\qquad
z=sE-v(1+E).
\tag{52}
$$

The selector gives $v\ge0$, while $c_*>2/3$ and $s\le1$ give $v<1/3$.
Thus the second enclosing rectangle is

$$
0\le t\le\frac34,
\qquad
0\le v\le\frac13.
\tag{53}
$$

Equations (51) and (53) are closed superrectangles. They include the selector,
radial, and endpoint faces, so no limiting parameter family is omitted.

### 7.3 Interval method and safe pruning

Every basic binary64 endpoint operation is widened by one
next-representable number toward the appropriate infinity. Rational constants
are enclosed on both sides. Square-root endpoints are adjusted until exact
integer-ratio comparisons verify

$$
(\text{lower endpoint})^2
\le\text{input}
\le
(\text{upper endpoint})^2.
$$

Thus the square-root enclosure does not rely on an unchecked library rounding
assumption.

The verifier discards a box only if outward intervals prove that it cannot
satisfy one of the necessary domain conditions

$$
x^2\le3,
\quad
z\ge0,
\quad
m\ge0,
\quad
U\ge0,
\quad
0\le D^2\le1,
$$

or, on the second sheet, $c_*>2/3$. Proving (49) on any retained points
outside the original domain is harmless. A box meeting a domain boundary is
not discarded. Before certification, the box must lie strictly in $D^2>0$
and both Newton denominators must have negative interval upper endpoints.
Therefore every certified expression is continuously differentiable on its
whole box.

Each expression is evaluated together with interval enclosures of its two
partial derivatives. For a box centered at $(t_0,v_0)$, the mean-value
enclosure is

$$
\begin{aligned}
f(\text{box})\subseteq{}&
f(t_0,v_0)
+\partial_t f(\text{box})(t-t_0)\\
&+\partial_v f(\text{box})(v-v_0).
\end{aligned}
\tag{54}
$$

This centered form controls the cancellation in the tangent formulas. Boxes
that do not yet prove all five signs in (49) are bisected along the larger
relative chart width, through maximum adaptive depth $16$.

### 7.4 Reproduction and output

Run from the repository root:

    python3 proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3103X_residual_core/3103X_computation/verify_tangent_witness_mixed_overlap.py

The deterministic output is:

    {"centered_form":"first_order_interval_automatic_differentiation","certificate":"3103X_junction_tangent_mixed_overlaps","charts":[{"branch":"L","certified_boxes":9907,"minimum_certified_mixed_P_lower_bound":2.522678787629918e-07,"processed_boxes":21040,"pruned_boxes":1258,"unresolved_boxes":0},{"branch":"T","certified_boxes":9208,"minimum_certified_mixed_P_lower_bound":9.92316118814129e-07,"processed_boxes":18574,"pruned_boxes":222,"unresolved_boxes":0}],"maximum_adaptive_depth":16,"reflection_half_domain":"z=a-b>=0","result":"PASS","rounding":"binary64_nextafter_outward_with_exact_sqrt_endpoint_checks","total_unresolved_boxes":0}

There are no unresolved boxes. Reflection supplies $z\le0$, so (49), hence
(25), holds throughout the remaining parameter domain.

## 8. Completion of the enclosure proof

When $c_*\le2/3$, equation (4) proves (2). When $c_*>2/3$:

- Section 5 proves the cyclic ray order, positive crosses, and radius
  hypotheses of Proposition 4.1;
- Section 6 proves the two equal-radius cap overlaps; and
- Section 7 proves both mixed cap overlaps.

Proposition 4.1 therefore gives

$$
\Lambda(\widehat K)\ge1.
$$

Finally, (16) gives

$$
\boxed{
\Lambda(K_{\mathrm{wit}}(a,b))\ge1
}
$$

for every $(a,b)$ in (3). This proves the terminal target.

## 9. Falsification audit, limiting families, and a failed shortcut

The empirical scan
[`3103X_computation/scan_witness_enclosure.py`](3103X_computation/scan_witness_enclosure.py)
evaluates exactly the event list in Proposition 2.1 for the original
first-root witnesses. Its default $38{,}560$ parameter samples found no value
below $1$ within the stated tolerance. Up to reflection, only two minimizing
event families occurred in the remaining region:

- an adjacent point--point tie with two disk supports; and
- a disk--outer-point tie with the opposite outer point active after one
  $120$-degree rotation.

This observation motivated Sections 6--7, but it is not used as proof.

The limiting family is sharp. As $(a,b)\to(0,1)$,

$$
c_*\to1,
\qquad
\eta\to0,
$$

and, in $V_4$-local coordinates,

$$
(Q_-,Q_0,Q_+)
\longrightarrow
\left(
(0,0),
\left(\frac12,0\right),
(1,0)
\right).
$$

The limiting witness hull is

$$
\mathrm{conv}\left\{
O,V_4,\frac{V_4+V_5}{2},V_5
\right\}
=
\mathrm{conv}\{O,V_4,V_5\},
$$

which is itself a unit equilateral triangle. Hence the limiting value is
exactly $1$; no uniform positive gap is possible on the closure. Reflection
gives the limit $(a,b)\to(1,0)$.

Finally, the tempting disk-plus-two-point shortcut is rigorously false. At

$$
(a,b)=\left(\frac1{10},\frac{187}{200}\right),
$$

the outward-rounded verifier
[`3103X_computation/verify_two_point_subset_counterexamples.py`](3103X_computation/verify_two_point_subset_counterexamples.py)
isolates the selected $C_L$ root and evaluates explicit rational unit
normals. It certifies

$$
\Lambda\left(\mathcal D_\eta\mathbin\cup\{Q_-,Q_0\}\right)
\le0.995781778030217886,
$$

$$
\Lambda\left(\mathcal D_\eta\mathbin\cup\{Q_0,Q_+\}\right)
\le0.993522844066214568,
$$

and

$$
\Lambda\left(\mathcal D_\eta\mathbin\cup\{Q_-,Q_+\}\right)
\le0.996310453071134844.
$$

Thus all three asymmetric witnesses are genuinely necessary for this
fixed-subset route, even though an individual witness can be inactive at the
minimizing orientation of the full set.
