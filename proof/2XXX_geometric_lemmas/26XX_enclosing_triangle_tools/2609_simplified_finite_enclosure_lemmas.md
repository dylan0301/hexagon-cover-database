# Simplified Finite-Enclosure Lemmas

Status: Proven

This note records four reusable simplifications for the finite-enclosure
strategy:

1. a finite caliper theorem for a centered disk and finitely many points;
2. a shorter proof of the CE2 two-gap short-ray inequality;
3. a one-third radial envelope on the half-edge domain used by the adjacent
   Vd placement;
4. a common rescuer-tail budget covering both the T3-like and Vd1
   neighboring-midpoint arguments.

The local admissible set is the exact set proved in
[`2004`](../20XX_V_triangle_geometry/2004_admissible_set.md), and the signed
center variables are those of
[`2109`](../21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md).

Throughout,

$$
h=\frac{\sqrt3}{2},
$$

and $\mathsf R,\mathsf J$ denote counterclockwise rotations through
$2\pi/3$ and $\pi/2$, respectively.

## 1. Disk--finite-set calipers

Let

$$
\mathcal D_\eta=\{x:\|x\|\le\eta\},
\qquad
P=\{p_1,\ldots,p_m\},
$$

and put

$$
\Psi_P(n)
=
\sum_{j=0}^2
\max\left\{
\eta,\max_{1\le i\le m}\langle p_i,\mathsf R^j n\rangle
\right\}
\qquad(\|n\|=1).
$$

The enclosing gauge is

$$
\Lambda(\mathcal D_\eta\cup P)
=
\frac1h\min_{\|n\|=1}\Psi_P(n).
\tag{1}
$$

For $p_i\ne p_k$, define the point--point candidate normals

$$
\mathcal N_{\rm pp}
=
\left\{
\pm\frac{\mathsf J(p_k-p_i)}{\|p_k-p_i\|}
:1\le i<k\le m
\right\}.
$$

For $\|p_i\|\ge\eta$, define the two point--disk tangent normals

$$
n_i^\pm
=
\frac{
\eta p_i\pm\sqrt{\|p_i\|^2-\eta^2}\,\mathsf Jp_i
}{
\|p_i\|^2
},
$$

and let $\mathcal N_{\rm pd}$ be the set of all such normals.

### Theorem 1.1

If there is a unit normal $n$ such that

$$
\langle p_i,\mathsf R^j n\rangle\le\eta
\qquad
(1\le i\le m,\ 0\le j\le2),
$$

then

$$
\boxed{
\Lambda(\mathcal D_\eta\cup P)=\frac{3\eta}{h}.
}
$$

Otherwise,

$$
\boxed{
\Lambda(\mathcal D_\eta\cup P)
=
\frac1h
\min_{n\in\mathcal N_{\rm pp}\cup\mathcal N_{\rm pd}}
\Psi_P(n).
}
\tag{2}
$$

Thus a least enclosing equilateral triangle may be chosen so that one side
either contains two points of $P$, or is tangent to the disk and contains one
point of $P$.

### Proof

Parameterize $n=n(\theta)$. The finitely many point--point and point--disk
ties partition the normal circle into open cells on which the support source
in each of the three directions is fixed. Suppose that $q$ of the three
sources are the disk. On such a cell,

$$
\Psi_P(n(\theta))
=
q\eta+\langle v,n(\theta)\rangle
$$

for one fixed vector $v$, obtained by rotating the active point supports back
to the first normal direction.

If at least one point is active, every active point projection is strictly
larger than $\eta\ge0$. Hence

$$
\langle v,n(\theta)\rangle>0
$$

throughout the cell, and

$$
\frac{d^2}{d\theta^2}\Psi_P(n(\theta))
=
-\langle v,n(\theta)\rangle<0.
$$

The support sum is strictly concave and has no interior minimum. A minimum
therefore occurs at a cell boundary. Such a boundary is either a point--point
tie

$$
\langle p_i,\mathsf R^j n\rangle
=
\langle p_k,\mathsf R^j n\rangle
$$

or a point--disk tie

$$
\langle p_i,\mathsf R^j n\rangle=\eta.
$$

Rotational invariance of the three-term support sum moves the tied direction
to $j=0$, producing precisely the candidates above. If no point is active on
a cell, then $\Psi_P=3\eta$, which is the global minimum because every one of
the three supports is at least $\eta$. This proves (2). $\square$

For a minimizing normal $n_*$, the actual triangle is

$$
\bigcap_{j=0}^2
\left\{
x:
\langle x,\mathsf R^j n_*\rangle\le c_j
\right\},
\qquad
c_j=
\max\left\{
\eta,\max_i\langle p_i,\mathsf R^j n_*\rangle
\right\}.
$$

Its side length is $(c_0+c_1+c_2)/h$.

## 2. Short CE2 two-gap proof

Use the strict CE2 domain

$$
0<R<1,\qquad W=1-R,
$$

$$
E=\sqrt{1-RW},
\qquad
\eta=1-E,
\qquad
P=E\eta,
$$

$$
\alpha+W\delta<P,
\qquad
R\alpha+\delta<P.
\tag{3}
$$

Put

$$
p=W-\alpha,
\qquad
q=R-\delta,
\qquad
e=\min\{\alpha,\delta\}.
$$

### Theorem 2.1

One has

$$
\boxed{c_{\max}(p,q)<1-e.}
\tag{4}
$$

Consequently, if the common pair $(p,q)$ is realized on the intervening V
roles, then the type-aware radial witness on $r_2$ or $r_4$ lies strictly
beyond the corresponding C-triangle exit.

### Proof

Let

$$
M=\max\{R,W\}.
$$

If $M=R$, the second inequality in (3) gives

$$
P>R\alpha+\delta\ge(1+R)e=(1+M)e.
$$

If $M=W$, use the first inequality. Thus

$$
P>(1+M)e.
\tag{5}
$$

Since $E^2=1-M+M^2$,

$$
(1+M)^2-(3M-1)^2E^2
=
3M(1-M)(3M^2-2M+3)>0.
$$

Therefore

$$
\eta=\frac PE>(3M-1)e.
\tag{6}
$$

The first inequality in (3) and $RW=\eta+P$ give

$$
Wq=RW-W\delta>\eta+\alpha\ge\eta+e>3Me.
$$

Because $W\le M$, this yields $q>3e$. The reflected calculation gives
$p>3e$. Since

$$
p+q=1-\alpha-\delta\le1-2e,
$$

we also obtain

$$
\boxed{3e<p,q<1-5e.}
\tag{7}
$$

Moreover,

$$
e<\frac{P}{1+M}
\le
\frac{h(1-h)}{3/2}
=
\frac{2\sqrt3-3}{6}
<
\frac1{12}.
\tag{8}
$$

Set $c=1-e$ and

$$
f_c(t)=c^4-c^2+ct-t^2.
$$

This is concave in $t$. Direct substitution gives

$$
f_c(3e)
=
e(1-7e-4e^2+e^3)>0,
$$

$$
f_c(1-5e)
=
e(2-15e-4e^2+e^3)>0
$$

on the interval (8). Hence (7) and concavity imply

$$
f_c(p)>0,
\qquad
f_c(q)>0.
\tag{9}
$$

Also $p+c>1$, $q+c>1$, and $c>p+q$. In the exact local minimum-side formula
of `2004`, the four relevant side lengths at radial demand $c$ are therefore

$$
p+c,\qquad q+c,
$$

$$
\frac{c^2}{\sqrt{p^2-pc+c^2}},
\qquad
\frac{c^2}{\sqrt{q^2-qc+c^2}}.
$$

The first two exceed one. The last two exceed one exactly by (9). Thus
$(p,q,c)$ is not admissible, proving (4).

If $e=\delta$, then $(1-c_{\max}(p,q))V_2$ lies beyond the C exit $\delta$
on $r_2$. If $e=\alpha$, the reflected conclusion holds on $r_4$.
$\square$

## 3. Half-edge one-third radial envelope

### Theorem 3.1

Suppose

$$
M\ge\frac12,
\qquad
0<m\le M,
\qquad
M+m<1.
$$

Then

$$
\boxed{
c_{\max}(M,m)<1-\frac m3.
}
\tag{10}
$$

### Proof

Put

$$
s=M+m,
\qquad
c_0=1-\frac m3.
$$

Only the selected $L$ and $T$ cells of `2004` can occur.

First assume $0<m\le3/8$. On the $L$ cell the selected radial root is the
unique root in $[h,1]$ of

$$
F_L(c)=c^4-c^2+mc-m^2.
$$

At $c_0$,

$$
F_L(c_0)
=
\frac m{81}(m^3-12m^2-63m+27).
$$

The cubic in parentheses decreases on $[0,3/8]$ and has value $891/512$ at
$3/8$. Thus $F_L(c_0)>0$, while
$F_L(h)=-(m-h/2)^2\le0$ and $F_L$ is increasing on $[h,1]$. The selected
$L$ root is strictly below $c_0$.

At an $L/T$ transition the two selected formulas agree and equal $s$. On the
$T$ cell,

$$
c_T(s)=
\frac{2(s-m)}{1+\sqrt{4s^2-3}}.
$$

Writing $r=\sqrt{4s^2-3}$, direct differentiation gives

$$
c_T'(s)
=
\frac{2(r+4ms-3)}{r(1+r)^2}<0.
$$

Indeed, $m\le s/2$, and for $h\le s<1$ one has
$r+2s^2-3<0$. Hence $c_T$ decreases after the transition and remains below
$c_0$.

Now assume $3/8\le m<1/2$. Since $M\ge1/2$,

$$
s\ge\frac78,
\qquad
mM\ge\frac3{16},
$$

and the selector satisfies

$$
s^4-s^2+mM
\ge
\left(\frac78\right)^4-\left(\frac78\right)^2+\frac3{16}
=
\frac{33}{4096}>0.
$$

Only the $T$ cell occurs. The derivative calculation above shows that, for
fixed $m$, $c_T$ decreases with $M$. Its maximum is at $M=1/2$. There
$s\ge7/8$, so $\sqrt{4s^2-3}\ge1/4$ and

$$
c_T\le\frac1{1+1/4}=\frac45
<
\frac56
<
1-\frac m3.
$$

This proves (10). $\square$

## 4. Common rescuer-tail budget

For $0\le c\le1/2$, let

$$
M_c^{\rm sup}
=
\frac{c+\sqrt{c^2-8c+4}}2
$$

be the nonattained strict-supercritical outgoing supremum.

### Theorem 4.1

Suppose a special V role based at $V_0$ has a positive interval
$[c,u]\subset r_1$, measured from $V_1$ toward $O$, and a boundary endpoint
$a$ on $e_{5,0}$. Put

$$
\varepsilon=1-u,
\qquad
M=M_c^{\rm sup}.
$$

Assume:

1. $\varepsilon V_1$ is missed by all six open V roles and hence belongs to
   $U_C$;
2. $a+\varepsilon\le1$;
3.
   $$
   a\le1-M,
   \qquad
   \frac{a}{a+\varepsilon}\le1-M;
   \tag{11}
   $$
4. $T_1$ is the unique supercritical V role, has own-radial reach at least
   $c$, and $T_2,T_3,T_4,T_5$ are nonsupercritical;
5. the four-edge path from $e_{1,2}$ through $e_{4,5}$ is center-free.

Then the skeleton is not covered.

### Proof

Let $h_T$ be the far boundary reach required from $T_5$ toward $V_0$.

If the companion C trace on $e_{5,0}$ is absent or does not hide the endpoint
$a$, then

$$
h_T\ge1-a\ge M.
\tag{12}
$$

In the only hiding configuration, the companion C trace is

$$
\left[\frac{k}{W},R+\alpha\right],
$$

with $k/W\le a$. Since the C triangle contains $\varepsilon V_1$, its exit on
$r_1$ satisfies $\delta/R\ge\varepsilon$. Therefore

$$
Wa\ge k=\eta+\alpha+\delta>\alpha+R\varepsilon,
$$

and hence

$$
a-R(a+\varepsilon)>\alpha.
$$

Also $Wa>\delta\ge R\varepsilon$, so
$R<a/(a+\varepsilon)$. Because $a+\varepsilon\le1$,

$$
R+\alpha
<
a+R(1-a-\varepsilon)
<
\frac{a}{a+\varepsilon}
\le1-M.
$$

The boundary tail beyond the C trace again has length at least $M$, proving
(12).

The strict-supercritical envelope gives

$$
B_1<M.
$$

The four ordinary roles satisfy

$$
A_2\ge1-B_1,
$$

$$
B_2+A_3\ge1,\qquad
B_3+A_4\ge1,\qquad
B_4+A_5\ge1,
$$

and $B_5\ge h_T$. Adding gives

$$
\sum_{i=2}^5(A_i+B_i)
\ge4+h_T-B_1>4,
$$

contrary to nonsupercriticality of $T_2,\ldots,T_5$. $\square$
