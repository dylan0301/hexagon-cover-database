# Strict Supercritical $AB$-Union Theorem

Status: Proven

Let $e_A,e_B$ be unit vectors making an angle of $120^\circ$, and put

$$
O=0,\qquad A=ae_A,\qquad B=be_B,
$$

$$
C=\left\{ue_A+ve_B:u\ge0,\ v\ge0\right\}.
$$

The local union is

$$
\mathcal U_{AB}(a,b)
=C\cap\bigcup\left\{T:T\text{ is a closed unit equilateral triangle and }
O,A,B\in T\right\}.
$$

This note proves the closed form used by the strict supercritical branches.
The proof is independent of the empirical named-curve catalog in
[`20092_ab_set_case_catalog.md`](20092_ab_set_case_catalog.md).  It is the
strict specialization of the exhaustive caliper theorem in
[`20095_exact_caliper_certificate.md`](20095_exact_caliper_certificate.md).

## 1. Statement

Assume

$$
\sigma=a+b>1,\qquad
\rho=a^2+ab+b^2<1.
\tag{1}
$$

Then $0<a,b<1$.  Moreover,

$$
4\rho-3\sigma^2=(a-b)^2,
$$

so $3/4<\rho<1$, and

$$
D=\sqrt{4\rho-3}
$$

satisfies $0<D<1$.  In cone coordinates

$$
x=ue_A+ve_B,
$$

the metric is

$$
\lVert ue_A+ve_B\rVert^2=u^2+v^2-uv.
$$

Put $h=\sqrt3/2$ and define

$$
\alpha=\frac{h(a+2b-aD)}{2\rho},\qquad
\beta=\frac{h(a-b+\sigma D)}{2\rho},
$$

$$
\gamma=\frac{h(-a+b+\sigma D)}{2\rho},\qquad
\delta=\frac{h(2a+b-bD)}{2\rho}.
\tag{2}
$$

All four coefficients are positive.  For the middle two this follows from

$$
\sigma^2D^2-(a-b)^2=4\rho(\sigma^2-1)>0.
\tag{3}
$$

Let

$$
\mathcal D_A=
\left\{(u,v):(u-a)^2+v^2-(u-a)v\le1\right\},
$$

$$
\mathcal D_B=
\left\{(u,v):u^2+(v-b)^2-u(v-b)\le1\right\},
$$

$$
\mathcal H_A=
\left\{(u,v):\alpha(u-a)+\beta v\le0\right\},
$$

$$
\mathcal H_B=
\left\{(u,v):\gamma u+\delta(v-b)\le0\right\}.
$$

**Theorem 1.1.** Under (1),

$$
\boxed{
\mathcal U_{AB}(a,b)
=
\left(C\cap\mathcal D_A\cap\mathcal H_A\right)
\mathbin\cup
\left(C\cap\mathcal D_B\cap\mathcal H_B\right).
}
\tag{4}
$$

## 2. Caliper reduction

For a compact set $S$ and a unit vector $n$, write

$$
G_S(n)=\sum_{k=0}^2h_S(R^kn),\qquad
h_S(n)=\max_{z\in S}\langle z,n\rangle,
$$

where $R$ is rotation through $120^\circ$.  The supporting triangle with
these three normals has side $2G_S(n)/\sqrt3$.  The finite caliper theorem
therefore says that $S$ fits in a closed unit equilateral triangle exactly
when one of its hull-edge normals has $G_S\le h$.

The triangle $\triangle OAB$ fits in an equilateral triangle of side
$\sqrt\rho<1$.  It is also contained in the first component on the
right-hand side of (4).  Indeed, that component is convex and contains
$A$; it contains $O$ because $a<1$ and $-\alpha a<0$, and it contains $B$
because $\lVert A-B\rVert^2=\rho<1$ and

$$
-\alpha a+\beta b=-\frac h2(1-D)<0.
\tag{5}
$$

Thus it remains to consider $x=(u,v)\in C\setminus\triangle OAB$.  First
assume $u,v>0$.  All four points are hull vertices, in cyclic order

$$
O,B,x,A.
$$

The two cone-axis hull edges cannot certify a unit triangle.  At the outward
normal to $AO$ one obtains

$$
\frac{G}{h}=\max\left\{a,u\right\}+\max\left\{b,v-u\right\}\ge\sigma>1,
$$

and at the outward normal to $OB$ one obtains

$$
\frac{G}{h}=\max\left\{b,v\right\}+\max\left\{a,u-v\right\}\ge\sigma>1.
\tag{6}
$$

Only the $Ax$ and $Bx$ calipers remain.

## 3. Exact $Ax$ support value

Put

$$
p=u-a,\qquad r^2=p^2+v^2-pv=\lVert x-A\rVert^2.
$$

Assume $r>0$, since $x=A$ was already handled.  Let $n_0$ be the outward
unit normal to $Ax$, and let $n_1=Rn_0$, $n_2=R^2n_0$.  Translate $A$ to
the origin.  Direct scalar products give the following supports after the
common factor $h/r$ is removed:

- on $n_1$, the values relevant to the maximum are $r^2$ from $x$ and
  $-ap+\sigma v$ from $B$; the value $a(v-p)$ from $O$ is smaller than
  the $B$ value by $bv$;
- on $n_2$, the relevant values are $0$ from $A$, $ap$ from $O$, and
  $\sigma p-bv$ from $B$; the value from $x$ is $-r^2$.

Consequently the exact caliper value is

$$
\frac{G_A}{h}
=
\frac{
\max\left\{r^2,-ap+\sigma v\right\}
+N_A}{r},
\tag{7}
$$

where

$$
N_A=
\begin{cases}
0,&p\le0,\\
ap,&0\le p\le v,\\
\sigma p-bv,&p\ge v.
\end{cases}
\tag{8}
$$

These three sectors are exhaustive; no support label has been discarded.

### 3.1. The low sector is exactly the $A$-component

Suppose $p\le0$.  Then (7) gives $G_A\le h$ exactly when

$$
r\le1,
\qquad
-ap+\sigma v\le r.
\tag{9}
$$

Set

$$
c=a+2b-aD,\qquad d=a-b+\sigma D,
$$

$$
c'=a+2b+aD,\qquad d'=a-b-\sigma D.
$$

Expansion gives the exact factorization

$$
r^2-(-ap+\sigma v)^2
=\frac{(cp+dv)(c'p+d'v)}{4\rho}.
\tag{10}
$$

By (3), $c,c',d>0$ and $d'<0$.  Thus for $p\le0$, $v\ge0$, the second
factor in (10) is nonpositive.  Since $-ap+\sigma v\ge0$, the second
inequality in (9) is therefore equivalent to

$$
cp+dv\le0.
$$

By (2), this is precisely the defining inequality of $\mathcal H_A$.
Hence

$$
p\le0:\qquad
G_A\le h
\quad\Longleftrightarrow\quad
x\in\mathcal D_A\cap\mathcal H_A.
\tag{11}
$$

Conversely, positivity of $\alpha,\beta$ shows that
$\mathcal H_A\cap C$ forces $p=u-a\le0$.

### 3.2. The middle sector is impossible

If $0<p\le v$, then $r\le v$, while (7)--(8) give

$$
\max\left\{r^2,-ap+\sigma v\right\}+ap
\ge\sigma v>r.
$$

Thus $G_A>h$ throughout this sector.

### 3.3. The high sector belongs to the opposite component

Suppose $p\ge v$ and $G_A\le h$.  Equations (7)--(8) imply both

$$
r^2+\sigma p-bv\le r,
\qquad
bp+av\le r.
\tag{12}
$$

Choose Cartesian angles so that $e_A$ has angle $0^\circ$ and $e_B$ has
angle $120^\circ$.  Write

$$
x-A=r y(\theta),\qquad 0\le\theta\le60^\circ,
$$

where the unit vector $y(\theta)$ has cone coordinates

$$
y(\theta)=t e_A+w e_B,
$$

$$
t=\frac2{\sqrt3}\cos(\theta-30^\circ),
\qquad
w=\frac2{\sqrt3}\sin\theta.
$$

Dividing (12) by $r$ gives

$$
r\le f(\theta):=1-\sigma t+bw,
\qquad
S(\theta):=bt+aw\le1.
\tag{13}
$$

Let $n_B$ be the unit vector satisfying

$$
\langle n_B,e_A\rangle=\gamma,
\qquad
\langle n_B,e_B\rangle=\delta.
$$

The identity

$$
\gamma^2+\gamma\delta+\delta^2=h^2
$$

is the dual-coordinate unit condition, so such a unit vector exists.

Its Cartesian angle $\varphi_B$ lies in $(30^\circ,90^\circ)$.  Put
$\theta_B=\varphi_B-30^\circ$.  Substitution in (2) gives

$$
b\gamma+\sigma\delta=h,
\qquad
\sigma\gamma+a\delta=\frac h2(1+D),
\qquad
b\delta-a\gamma=\frac h2(1-D).
\tag{14}
$$

The cone coordinates of $y(\theta_B)$ are
$((\gamma+\delta)/h,\delta/h)$.  Hence (14) gives

$$
S(\theta_B)=1,
\qquad
f(\theta_B)=\frac{1-D}{2}.
\tag{15}
$$

Now $S(0)=b<1$ and $S(60^\circ)=\sigma>1$.  Its derivative has at most one
zero in this interval, and such a zero is a maximum.  Therefore
$S(\theta)\le1$ implies $\theta\le\theta_B$.

On the part where (13) is feasible, $f\ge0$ and $f'\ge0$.  If $a\le b$ this
is immediate from

$$
f(\theta)=1-\sigma\cos\theta-\frac{a-b}{\sqrt3}\sin\theta.
$$

If $a>b$, the function first decreases from $f(0)=1-\sigma<0$ and then
increases, so it can be nonnegative only after its unique minimum.  Since
$30^\circ\le\varphi_B-\theta<90^\circ$, the function

$$
J(\theta)=f(\theta)\cos(\varphi_B-\theta)
$$

satisfies

$$
J'(\theta)
=f'(\theta)\cos(\varphi_B-\theta)
+f(\theta)\sin(\varphi_B-\theta)\ge0.
$$

Equations (13)--(15) now yield

$$
r\cos(\varphi_B-\theta)
\le J(\theta)
\le J(\theta_B)
=\frac h2(1-D).
$$

Together with the last identity in (14), this is

$$
\langle n_B,x-B\rangle
=a\gamma-b\delta+r\cos(\varphi_B-\theta)\le0.
$$

Thus $x\in\mathcal H_B$.  Moreover, $G_A\le h$ already constructs a unit
triangle containing $x$ and $B$, so the diameter bound gives
$\lVert x-B\rVert\le1$.  Therefore every high-sector $Ax$ fit belongs to
$\mathcal D_B\cap\mathcal H_B$.  This includes the formerly omitted
support regimes in which $B$ supports two of the three caliper sides.

## 4. Completion of the set identity

Reflecting the preceding calculation exchanges

$$
a\leftrightarrow b,\qquad u\leftrightarrow v,
$$

and proves the identical three-sector result for the $Bx$ caliper.  The
caliper reduction and the exhaustive sectors therefore show that every
covered point outside $\triangle OAB$ lies in one of the two components in
(4).

Conversely, if $x\in C\cap\mathcal D_A\cap\mathcal H_A$, then
$u-a\le0$ and (11) gives $G_A\le h$, so $x$ is covered.  The mirror argument
covers every point of the $B$-component.  This proves (4) for $u,v>0$.

The cone axes require no new hull case.  Choose a fixed point $y$ in the
interior of $\triangle OAB$.  Both components in (4) contain that triangle.
If an axis point $x$ is covered, choose a fitting triangle $T$ for it.  Since
$T$ also contains $O,A,B$, it contains $y$, so every point
$(1-s)x+sy$, $0<s<1$, is covered and has positive cone coordinates.  The
already proved interior result places these points in the right-hand side of
(4), whose two components are closed; hence $x$ lies there as $s\to0$.
Conversely, if $x$ lies in one of those components, the same convex
combinations stay in that component and are covered by the interior result.
The fitting set is closed because
$x\mapsto\min_{\lVert n\rVert=1}G_{S_x}(n)$ is continuous.  Therefore their
limit $x$ is covered.  This proves (4) on the axes as well. $\square$

## 5. The four-piece frontier

Put

$$
\Omega=\alpha\delta-\gamma\beta
=\frac{3(1-D)(D+3)}{16\rho}>0.
$$

The five junction points are

$$
P_0=\left(0,\frac{-a+\sqrt{4-3a^2}}2\right),
$$

$$
P_1=\left(a-\frac\beta h,\frac\alpha h\right),
$$

$$
P_2=
\left(
\frac{\delta(a\alpha-b\beta)}\Omega,
\frac{\alpha(b\delta-a\gamma)}\Omega
\right),
$$

$$
P_3=\left(\frac\delta h,b-\frac\gamma h\right),
$$

$$
P_4=\left(\frac{-b+\sqrt{4-3b^2}}2,0\right).
\tag{16}
$$

To prove their order, set

$$
c=a(1-D)+2b,\qquad e=2a+b(1-D).
$$

Direct simplification gives

$$
P_1=\left(\frac{(1-D)c}{4\rho},\frac c{2\rho}\right),
\qquad
P_3=\left(\frac e{2\rho},\frac{(1-D)e}{4\rho}\right),
\tag{17}
$$

and

$$
a\alpha-b\beta=b\delta-a\gamma=\frac h2(1-D).
\tag{18}
$$

Thus $P_2$ is a positive multiple of $(\delta,\alpha)$, and the successive
cone-ray slopes are

$$
+\infty,
\quad \frac2{1-D},
\quad \frac ce,
\quad \frac{1-D}{2},
\quad 0.
\tag{19}
$$

The strict middle inequalities in (19) are exactly

$$
2e-(1-D)c=a\left(4-(1-D)^2\right)>0,
$$

$$
2c-(1-D)e=b\left(4-(1-D)^2\right)>0.
\tag{20}
$$

Also $P_0,P_4$ are positive because $a,b<1$.  The $v$-coordinate of
$P_0$ exceeds $b$, and the $u$-coordinate of $P_4$ exceeds $a$, exactly
because $\rho<1$.  Hence

$$
P_0\longrightarrow P_1\longrightarrow P_2
\longrightarrow P_3\longrightarrow P_4
$$

is the strict cone-boundary order from the $e_B$ ray to the $e_A$ ray.

The identities

$$
\alpha^2+\alpha\beta+\beta^2=h^2,
\qquad
\gamma^2+\gamma\delta+\delta^2=h^2
\tag{21}
$$

show that $P_1$ and $P_3$ are exactly the in-cone line--circle
intersections.  Furthermore

$$
P_2=A+\lambda(P_1-A),
\qquad
\lambda=\frac{2\rho}{D+3}\in(0,1),
$$

and the mirror identity places $P_2$ between $B$ and $P_3$.  Thus the two
line pieces remain inside their associated disks.  The two lines meet only
at $P_2$ because their determinant is $\Omega>0$.  Their radial order changes
there by (18).  Finally, the proved set identity implies that both components
lie in both unit disks, by the diameter bound; hence the other component
cannot protrude beyond either displayed circle arc.

It follows that the non-axis frontier consists, in order, of

$$
\Gamma_A^{\mathrm{circ}}:
(u-a)^2+v^2-(u-a)v=1,
$$

from $P_0$ to $P_1$,

$$
\Gamma_A^{\mathrm{lin}}:
\alpha(u-a)+\beta v=0,
$$

from $P_1$ to $P_2$,

$$
\Gamma_B^{\mathrm{lin}}:
\gamma u+\delta(v-b)=0,
$$

from $P_2$ to $P_3$, and

$$
\Gamma_B^{\mathrm{circ}}:
u^2+(v-b)^2-u(v-b)=1,
$$

from $P_3$ to $P_4$.  Equivalently, the circle branches are

$$
v=\frac{u-a+\sqrt{4-3(u-a)^2}}2,
\qquad
0\le u\le a-\frac\beta h,
$$

and

$$
v=b+\frac{u-\sqrt{4-3u^2}}2,
\qquad
\frac{-b+\sqrt{4-3b^2}}2\le u\le\frac\delta h.
$$

The two line formulas are

$$
v=\frac\alpha\beta(a-u),
\qquad
v=b-\frac\gamma\delta u.
$$

Thus all four pieces and all five junctions in the strict branch are proved.

## 6. The $\rho=1$ degeneration

For completeness, suppose $a,b>0$, $a+b>1$, and $\rho=1$.  Then $D=1$ and
the two half-planes in (4) coincide:

$$
bu+av\le ab.
$$

Because $\lVert A-B\rVert=1$, any unit equilateral triangle containing
$A,B$ has them as vertices.  Exactly one of the two choices contains $O$,
and its intersection with $C$ is

$$
C\cap\left\{bu+av\le ab\right\}=\triangle OAB.
$$

Both disks contain this triangle.  Hence the limiting identity is
$\mathcal U_{AB}(a,b)=\triangle OAB$.  In (16), $P_0=P_1=B$ and
$P_3=P_4=A$; the two line pieces merge into $AB$, while $\Omega=0$ and the
isolated line--line junction is replaced by the whole merged segment.
