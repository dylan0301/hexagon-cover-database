# Symmetric Residual-Core Witness Construction

Status: Proven

This note proves the symmetric-witness obligation used by the
center-independent all-boundary theorem
[`31035_center_independent_all_boundary_obstruction.md`](31035_center_independent_all_boundary_obstruction.md)
and its CE0 corollary
[`31030_CE0_all_Vd0_residual_core_strategy.md`](31030_CE0_all_Vd0_residual_core_strategy.md).
It uses the exact radial envelope from
[`2004_admissible_set.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md)
and the exact neighboring-ray capacity from
[`2008_neighbor_ray_max_c_formula.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md).

## 1. Candidate and transformed domain

Assume

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
$$

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
c_*=c_{\max}(p,q),
$$

and define

$$
P_k=(1-c_*)V_k,
\qquad k=0,\dots,5.
$$

The comparison demands in the symmetric core are incoming demand $p$ and
outgoing demand $q$ at every row. We prove

$$
\boxed{
P_k\in\mathcal C_{\mathrm{sym}}(a,b)
\qquad(k=0,\dots,5).
}
$$

Set

$$
s=p+q,
\qquad
m=\min\{p,q\},
\qquad
M=\max\{p,q\},
\qquad
t=1-s.
$$

Then

$$
0<p,q<1,
\qquad
0<s<1,
\qquad
0<m\le M,
\qquad
m<\frac12.
$$

Moreover,

$$
p^2+pq+q^2=s^2-pq<s^2<1,
$$

so only the two subcritical radial cells of `2004` occur. Expanding the
strict condition on $(a,b)$ gives

$$
\begin{aligned}
1
&>(1-q)^2+(1-q)(1-p)+(1-p)^2\\
&=3-3s+p^2+pq+q^2.
\end{aligned}
$$

Hence

$$
pq>(1-s)(2-s)=t(1+t).
\tag{1}
$$

In particular,

$$
\boxed{m>t.}
\tag{2}
$$

Indeed, if $m\le t$, then $M<1$ would give

$$
mM\le tM<t<t(1+t),
$$

contrary to (1). Consequently,

$$
\boxed{s>1-m.}
\tag{3}
$$

## 2. The exact radial value

Define the selector

$$
\chi=s^4-s^2+pq.
$$

The formula proved in `2004` is

$$
c_*=
\begin{cases}
C_L(m),&\chi\le0,\\
\displaystyle
\frac{2M}{1+\sqrt{4s^2-3}},&\chi>0,
\end{cases}
\tag{4}
$$

where $C_L(m)$ is the unique root in $[\sqrt3/2,1]$ of

$$
F_L(z)=z^4-z^2+mz-m^2=0.
$$

At $\chi=0$, both formulas give $c_*=s$.

We first record

$$
0<c_*<1.
\tag{5}
$$

On the $L$ branch, $c_*\ge\sqrt3/2>0$, while

$$
F_L(1)=m(1-m)>0,
$$

so the selected root is below $1$. On the other branch, $\chi>0$ implies
$s>\sqrt3/2$, because

$$
\chi
\le s^4-s^2+\frac{s^2}{4}
=s^2\left(s^2-\frac34\right).
$$

Put

$$
E=\sqrt{4s^2-3}>0.
$$

The identity

$$
s^2E^2-(M-m)^2
=4\left(s^4-s^2+mM\right)
=4\chi>0
$$

gives $sE>M-m$. Therefore

$$
s(1+E)>s+M-m=2M,
$$

and (4) gives $0<c_*<s<1$.

We next prove the strict lower bound

$$
\boxed{c_*>1-m.}
\tag{6}
$$

Suppose first that $\chi\le0$. If $s<\sqrt3/2$, then (3) gives

$$
c_*\ge\frac{\sqrt3}{2}>s>1-m.
$$

If $s\ge\sqrt3/2$, then

$$
F_L(s)=s^4-s^2+ms-m^2
=s^4-s^2+mM
=\chi\le0.
$$

Since $F_L(1)>0$, uniqueness of the selected root gives

$$
c_*\ge s>1-m.
$$

Now suppose $\chi>0$. Retain $E$ and $t=1-s$, and define

$$
A=\frac{2M}{1-m}-1.
$$

Since $s>\sqrt3/2$ and $m<1/2$, one has $A>0$. Direct expansion gives

$$
A^2-E^2
=
\frac{
4t\left((1-m)(1-2m)+m(2-m)t\right)
}{(1-m)^2}>0.
$$

Thus $A>E$, and consequently

$$
\frac{c_*}{1-m}
=
\frac{2M}{(1-m)(1+E)}
=
\frac{1+A}{1+E}>1.
$$

This proves (6).

## 3. Comparison with both neighboring-ray capacities

For incoming demand $x$ and outgoing demand $y$, let $C_+(x,y)$ be the
upper-neighbor capacity proved in `2008`. The lower-neighbor capacity is

$$
C_-(x,y)=C_+(y,x).
$$

We use the following consequence of its exact piecewise formula.

**Lemma 3.1.** If

$$
0<m\le M,
\qquad
m+M\le1,
$$

then

$$
C_+(M,m)=1-m,
\qquad
C_+(m,M)\le1-m.
$$

*Proof.* In the notation of `2008`, put

$$
f_x(z)=z^3-(x+2)z^2+2(x+1)z-1,
$$

and, for $0\le x\le1/2$, let $\pi(x)$ be its unique root in $[x,1]$.

If $M>1/2$, the formula in `2008` gives $C_+(M,m)=1-m$. Suppose
$M\le1/2$. Since $1-m\in[M,1]$,

$$
\begin{aligned}
f_M(1-m)
&=M(1-m^2)-m+m^2-m^3\\
&\ge m(1-m^2)-m+m^2-m^3\\
&=m^2(1-2m)\ge0.
\end{aligned}
$$

The strict monotonicity proved in `2008` gives $\pi(M)\le1-m$. Hence
$m\le1-\pi(M)$, so $(M,m)$ lies in the $1-y$ branch and
$C_+(M,m)=1-m$.

For the other order,

$$
f_m(1-m)=m^2(1-2m)\ge0,
$$

and hence $\pi(m)\le1-m$. The first and plateau branches of the formula
therefore give $C_+(m,M)\le1-m$. It remains only to check the final branch

$$
C_+(m,M)
=m+\frac12-\sqrt{(m+M)^2-\frac34}.
\tag{7}
$$

If $m\le1/4$, (7) is at most $m+1/2\le1-m$. Assume $m>1/4$. Write

$$
\pi=\pi(m),
\qquad
d=\pi-m.
$$

Then $0\le d\le1-2m$. The root equation $f_m(\pi)=0$ is equivalent to

$$
d\pi(2-\pi)=2\pi-1.
\tag{8}
$$

The final branch begins after the threshold

$$
\tau(m)=1-m-d(1-\pi).
$$

Using (8),

$$
\left(m+\tau(m)\right)^2=1-d+d^2.
$$

Therefore

$$
\begin{aligned}
\left(m+\tau(m)\right)^2-\left(4m^2-2m+1\right)
&=(d-2m)(d+2m-1)\ge0,
\end{aligned}
$$

because $m>1/4$ gives

$$
d\le1-2m<2m,
$$

so both factors are nonpositive. On the final branch $M>\tau(m)$, so

$$
(m+M)^2>4m^2-2m+1.
$$

It follows that

$$
\sqrt{(m+M)^2-\frac34}>2m-\frac12,
$$

which makes (7) strictly less than $1-m$. This proves the lemma. $\square$

Combining Lemma 3.1 with (6) gives

$$
\boxed{
c_*>
\max\left\{C_+(p,q),C_+(q,p)\right\}.
}
\tag{9}
$$

## 4. Exclusion from all six row interiors

It is enough to treat

$$
P_0=(1-c_*)V_0.
$$

Write $c=c_*$. In local coordinates at $V_j$, with the first coordinate
along $V_{j+1}-V_j$ and the second along $V_{j-1}-V_j$, direct substitution
gives

| $j$ | local coordinates of $P_0$ | $\lVert P_0-V_j\rVert^2$ |
|---:|---:|---:|
| $0$ | $(c,c)$ | $c^2$ |
| $1$ | $(c,1)$ | $c^2-c+1$ |
| $2$ | $(1,2-c)$ | $c^2-3c+3$ |
| $3$ | $(2-c,2-c)$ | $(2-c)^2$ |
| $4$ | $(2-c,1)$ | $c^2-3c+3$ |
| $5$ | $(1,c)$ | $c^2-c+1$ |

The local metric is

$$
\lVert x(V_{j+1}-V_j)+y(V_{j-1}-V_j)\rVert^2
=x^2+y^2-xy.
$$

By the definition of $c_{\max}$ and the exact theorem in `2004`, the point
$P_0$ belongs to the closed row union $R_0(p,q)$. It is not an interior
point of that union. Otherwise a sufficiently small movement farther down
the same radial segment would put

$$
\left(1-(c+\varepsilon)\right)V_0
$$

in $R_0(p,q)$ for some $\varepsilon>0$, contradicting the maximality of
$c=c_{\max}(p,q)$. Thus

$$
P_0\notin\mathrm{int}\left(R_0(p,q)\right).
\tag{10}
$$

Every point of $R_j(p,q)$ lies with $V_j$ in a closed unit equilateral
triangle, whose diameter is $1$. For $j=2,4$, the table gives

$$
\lVert P_0-V_j\rVert^2-1
=(1-c)(2-c)>0,
$$

and for $j=3$ it gives $\lVert P_0-V_3\rVert=2-c>1$. Hence

$$
P_0\notin R_2(p,q)\cup R_3(p,q)\cup R_4(p,q).
\tag{11}
$$

At $V_5$, the point $P_0$ has upper-neighbor coordinate $c$. Membership in
$R_5(p,q)$ would imply $c\le C_+(p,q)$. At $V_1$, it has lower-neighbor
coordinate $c$, so membership in $R_1(p,q)$ would imply
$c\le C_-(p,q)=C_+(q,p)$. Both conclusions contradict (9). Therefore

$$
P_0\notin R_1(p,q)\cup R_5(p,q).
\tag{12}
$$

Equations (10)--(12) show that $P_0$ avoids the interiors of all six
comparison row unions. By (5), $1-c\in(0,1)$, so $P_0$ lies on the open
segment $(O,V_0)$ and hence in $\mathrm{int}(H)$. Thus

$$
P_0\in\mathcal C_{\mathrm{sym}}(a,b).
$$

## 5. Rotation and the forced disk

Rotation by $\pi/3$ sends

$$
R_i(p,q)\longmapsto R_{i+1}(p,q)
$$

because it preserves the incoming and outgoing parameter order. It also
preserves $\mathrm{int}(H)$ and plane interiors. Therefore
$\mathcal C_{\mathrm{sym}}(a,b)$ is invariant under this rotation. Since
$P_k$ is the $k$-th rotation of $P_0$,

$$
P_k\in\mathcal C_{\mathrm{sym}}(a,b)
\qquad(k=0,\dots,5).
$$

The points are nonzero by (5). Their convex hull is the regular hexagon of
circumradius $1-c_*$. Its centered incircle has radius

$$
\boxed{
r(a,b)=\frac{\sqrt3}{2}(1-c_*).
}
$$

This proves the symmetric-witness and forced-disk obligation used in `31035`.
It does not prove the asymmetric witness memberships or the terminal
enclosure inequality. $\square$
