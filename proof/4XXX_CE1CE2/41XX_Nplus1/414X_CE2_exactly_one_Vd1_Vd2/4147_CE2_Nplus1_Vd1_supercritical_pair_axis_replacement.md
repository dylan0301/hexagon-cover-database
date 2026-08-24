# CE2 Vd1--Supercritical Adjacent-Pair Two-Chart Replacement

Status: Proven

This note proves the replacement used in Case 3 of
[`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md).
The Vd2 alternative is eliminated by
[`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md).
In the gap-first exhaustive assembly this theorem is invoked only after the
original zero-gap state has been removed, so the input has
$N_{\rm gap}\in\{1,2\}$.  The replacement construction itself does not use
that fact and does not claim to preserve the gap rank.

## Theorem

Let $U_C,U_0,\ldots,U_5$ be the original open roles and put
$T_C=\overline{U_C}$ and $T_i=\overline{U_i}$. Assume the complementary
`414X` branch in which:

- the closed C triangle $T_C$ is CE2;
- the full skeleton $S$ is covered;
- a closed Vd1 role and the unique supercritical closed Vd0 role are adjacent;
- the Vd1 role contains the own midpoint missed by the supercritical role;
- neither special role is the vertex role at the center's unique midpoint;
- every other vertex role is nonsupercritical Vd0;
- no other vertex role has positive trace on either radial segment based at
  the two pair vertices;
- the center has no boundary trace on the shared edge of the pair.

After a fresh cyclic renumbering, write the original open roles as $U_0$ at
$V_0$ and $U_1$ at $V_1$, with $T_0$ Vd1 and $T_1$ supercritical, and write
the rescued midpoint as $M_1$.
This local renumbering does not assert that the center midpoint is $M_0$.
In these indices the preceding no-other-support hypothesis says

$$
\mathcal H^1(T_j\cap r_0)=\mathcal H^1(T_j\cap r_1)=0
\qquad(j\notin\{0,1\}).
$$

Then $U_0,U_1$ can be replaced by two open roles $U_0',U_1'$ whose closures
are nonsupercritical Vd0 and such that the modified seven roles still cover
the full skeleton.
Let $N'_{\rm gap}$ be the gap rank recomputed from the modified boundary
traces.  If $N'_{\rm gap}=0$, the common boundary-complete Method 1
consequence `2500` gives a contradiction.  If
$N'_{\rm gap}\in\{1,2\}$, the nonzero-gap Method 2 part of the all-Vd0
skeleton theorem `4013` gives a contradiction.

## 1. Vd1 margins

Let $a,b$ be the exact incident boundary reaches of the Vd1 role $T_0=
\overline{U_0}$. By the Vd corner normal form, there are $t>0$ and

$$
d=\sqrt{t^2+t+1}
$$

such that, in the $V_0$ chart,

$$
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb.
\end{aligned}
$$

Its reach on $r_0$ and the endpoints of $T_0\cap r_1$ are

$$
c=\frac{d-a-tb}{t+1},
\qquad
\lambda=\frac{t(1-b)}{t+1},
\qquad
u_{\rm adj}=\frac{d-a-tb-1}{t},
$$

where the $r_1$ coordinate is measured from $V_1$ toward $O$.

Since the original open role $U_0$ contains $M_1$, its Vd1 closure satisfies with
strict margin

$$
b>\frac{t-1}{2t},
\qquad
a+tb<d-1-\frac t2.
$$

The role has no positive-length trace on $r_5$. If $t<1$,
then

$$
d-a-tb-t>1-\frac t2>\frac1{t+1}>\frac{1-a}{t+1},
$$

which would create such a trace. Therefore

$$
\boxed{t\ge1.}
$$

Exactly as in the Vd corner calculation, one obtains the four strict margins

$$
\boxed{
a+c<1,
\qquad
a<\lambda\le\frac12,
\qquad
b<\frac12,
\qquad
u_{\rm adj}<1-a.}
\tag{1}
$$

For completeness, on the closed midpoint face
$a=d-1-t/2-tb$ one has

$$
a+c-1
=-\frac{2bt^2+2bt-2dt-2d+t^2+4t+2}{2(t+1)}.
$$

Using $b\ge(t-1)/(2t)$, the numerator is at least

$$
2t^2+4t+1-2(t+1)d>0,
$$

because

$$
(2t^2+4t+1)^2-4(t+1)^2d^2
=4t^3+4t^2-4t-3>0
$$

for $t\ge1$. Strict midpoint containment gives $a+c<1$. The lower bound for
$b$ gives $\lambda\le1/2$; the closed upper bound for $a$, subtracted from
$\lambda$, is minimized at $b=(t-1)/(2t)$ and equals $(t+1)-d>0$; and

$$
t(u_{\rm adj}+a-1)
=d-(t+1)-tb+(t-1)a
\le t(d-t-1)<0.
$$

This proves (1).

## 2. The supercritical role and the bridge margin

Let

$$
(A_1,B_1,C_1)
$$

be the actual reaches of the supercritical role $T_1=\overline{U_1}$, with
$A_1$ measured on the shared edge from $V_1$ toward $V_0$ and $B_1$ measured
from $V_1$ toward $V_2$. Since the shared edge is center-free,

$$
A_1\ge1-b>\frac12.
$$

Coverage of $r_1$ up to the Vd1 interval gives

$$
C_1\ge\lambda.
$$

### Half-square admissibility lemma

If $(x,y,z)$ belongs to the exact local admissible set and

$$
x\ge\frac12,
\qquad
0\le z\le\frac12,
$$

then

$$
\boxed{y\le1-z.}
$$

Indeed, suppose $y>1-z$. Then $x+y>1$, so the selected supercritical cell
applies. In the ordered half $x\le y$, its necessary inequality is

$$
F(x,y,z)=(x^2-1)z^2+(2xy^2+y)z+y^4-y^2\le0.
$$

The function is nondecreasing in $x$. At $x=1/2$, its derivative in $y$ is

$$
4y^3-2y+2yz+z,
$$

which is increasing and positive for $y\ge1-z$. Hence

$$
F(x,y,z)>F\left(\frac12,1-z,z\right)
=\frac{z^2(2z-5)(2z-1)}4\ge0,
$$

a contradiction. In the reflected half $y<x$, use $F(y,x,z)$. Both
arguments exceed $r=1-z$. The first partial derivative is nonnegative, and
the second is minimized at $(r,r)$, where it equals

$$
4r^2z+z+4r^3-2r=2-5z+4z^2>0.
$$

Thus

$$
F(y,x,z)>F(r,r,z)=z(1-2z)\ge0,
$$

again a contradiction.

A supercritical admissible V triangle has $C_1\le1/2$ by the selected
supercritical-cell component condition. Applying the lemma gives

$$
B_1\le1-C_1\le1-\lambda.
$$

Since $a<\lambda$,

$$
\boxed{a+B_1<1.}
\tag{2}
$$

Let $d_1^C$ be the center reach on $r_1$, measured from $O$ toward $V_1$, and
put

$$
c_1^{\rm req}=1-d_1^C.
$$

Only the center, $U_1$, and the adjacent trace of $U_0$ have
positive-length intervals on $r_1$. Open skeleton coverage at the center
handoff forces

$$
c_1^{\rm req}<\max\{C_1,u_{\rm adj}\}.
$$

The half-square lemma and (1) give

$$
\max\{C_1,u_{\rm adj}\}
\le\max\{1-B_1,1-a\}.
$$

Therefore

$$
\boxed{
c_1^{\rm req}<\max\{1-B_1,1-a\}.}
\tag{3}
$$

## 3. Existence of the replacement parameters

Put

$$
L=1-B_1.
$$

By (2), $a<L$. Consider

$$
f(p)=\max\{p,1-p\}.
$$

On the open interval $(a,L)$,

$$
\sup_{a<p<L}f(p)=\max\{L,1-a\}.
$$

By (3), this supremum is strictly larger than $c_1^{\rm req}$. Hence there
exists

$$
p_2\in(a,L)
$$

such that

$$
f(p_2)>c_1^{\rm req}.
$$

The inequalities $a<1/2$ and $a+c<1$ allow a choice

$$
a<p_1<p_2
$$

with

$$
p_1<\frac12,
\qquad
1-p_1>c.
$$

Thus

$$
\boxed{
a<p_1<p_2<1-B_1,}
$$

$$
\boxed{
p_1<\frac12,
\qquad
1-p_1>c,
\qquad
\max\{p_2,1-p_2\}>c_1^{\rm req}.}
\tag{4}
$$

Choose

$$
0<\varepsilon<
\min\left\{
p_1-a,
\ p_2-p_1,
\ 1-B_1-p_2,
\ 1-p_1-c,
\ \max\{p_2,1-p_2\}-c_1^{\rm req}
\right\}.
\tag{5}
$$

Every quantity in the minimum is positive.

## 4. Two separate vertex charts

Define the $V_0$-based chart

$$
X_0(x,y)
=V_0+x(V_5-V_0)+y(V_1-V_0)
$$

and the $V_1$-based chart

$$
X_1(x,y)
=V_1+x(V_0-V_1)+y(V_2-V_1).
$$

Both charts carry the local metric

$$
\|(x,y)\|^2=x^2+y^2-xy.
$$

In the first chart,

$$
V_0=(0,0),\quad V_5=(1,0),\quad V_1=(0,1),\quad O=(1,1),
$$

while in the second chart,

$$
V_1=(0,0),\quad V_0=(1,0),\quad V_2=(0,1),\quad O=(1,1).
$$

For $0\le p\le1/2$, put

$$
\Delta_p^-
=\operatorname{conv}\{(0,1-p),(1,1-p),(0,-p)\},
$$

and for $1/2<p\le1$, put

$$
\Delta_p^+
=\operatorname{conv}\{(p,0),(p,1),(p-1,0)\}.
$$

Their side vectors have local lengths one, so both are unit equilateral
triangles.

### Lemma 4.1: shifted minus template

If $0<\varepsilon<p$, then

$$
D_{p,\varepsilon}^-
=\operatorname{int}(\Delta_p^-)+(-\varepsilon,0)
$$

contains the origin in its interior. Its closure has reaches

$$
\boxed{(p-\varepsilon,1-p,1-p)}
$$

on the positive $x$-axis, positive $y$-axis, and diagonal $x=y$,
respectively. It has no positive-length trace on either support line
$x=1$ or $y=1$.

### Proof

The shifted triangle is given by

$$
x>-\varepsilon,
\qquad
y<1-p,
\qquad
y>x+\varepsilon-p.
$$

The origin satisfies all three inequalities exactly when
$\varepsilon<p$. Substitution of $(s,0)$, $(0,s)$, and $(s,s)$ gives the
three reaches. Moreover $x\le1-\varepsilon<1$ and $y\le1-p<1$ on the
closure. $\square$

### Lemma 4.2: shifted plus template

If $0<\varepsilon<1-p$, then

$$
D_{p,\varepsilon}^+
=\operatorname{int}(\Delta_p^+)+(0,-\varepsilon)
$$

contains the origin in its interior. Its closure has reaches

$$
\boxed{(p,1-p-\varepsilon,p)}
$$

on the positive $x$-axis, positive $y$-axis, and diagonal, respectively. It
has no positive-length trace on $x=1$ or $y=1$.

### Proof

The shifted triangle is given by

$$
y>-\varepsilon,
\qquad
x<p,
\qquad
y<x+1-p-\varepsilon.
$$

The origin is interior exactly when $\varepsilon<1-p$. The three reaches
follow by substitution, and $x\le p<1$, $y\le1-\varepsilon<1$. $\square$

The bounds in (5) imply the interior conditions in both lemmas:
$\varepsilon<p_1$, $\varepsilon<p_2$, and, in the plus case,
$\varepsilon<1-p_2$.

## 5. Definition and exact reaches of the replacements

Define

$$
U_0'=X_0(D_{p_1,\varepsilon}^-)
$$

and

$$
U_1'=
\begin{cases}
X_1(D_{p_2,\varepsilon}^-),&p_2\le1/2,\\
X_1(D_{p_2,\varepsilon}^+),&p_2>1/2.
\end{cases}
$$

Let

$$
T_0'=\overline{U_0'},
\qquad
T_1'=\overline{U_1'}.
$$

The first replacement is a role at $V_0$, and

$$
(A(T_0'),B(T_0'),C(T_0'))
=(p_1-\varepsilon,1-p_1,1-p_1).
\tag{6}
$$

The second replacement is a role at $V_1$. If $p_2\le1/2$, then

$$
(A(T_1'),B(T_1'),C(T_1'))
=(p_2-\varepsilon,1-p_2,1-p_2),
\tag{7-}
$$

while if $p_2>1/2$, then

$$
(A(T_1'),B(T_1'),C(T_1'))
=(p_2,1-p_2-\varepsilon,p_2).
\tag{7+}
$$

In particular, $V_0\in U_0'$ and $V_1\in U_1'$.

Each boundary sum is exactly

$$
1-\varepsilon<1.
$$

For $i=0,1$, the two templates satisfy

$$
\mathcal H^1(\overline{U_i'}\cap r_{i-1})
=\mathcal H^1(\overline{U_i'}\cap r_{i+1})=0.
$$

By the exhaustive vertex classification, both are nonsupercritical Vd0 roles.

## 6. Preservation of the full skeleton

The special pair can have positive open trace only on

$$
e_{5,0},\ e_{0,1},\ e_{1,2},\ r_0,\ r_1.
$$

All other skeleton components are unchanged.

### Outer boundary edge at $V_0$

By (5) and (6),

$$
A(T_0')=p_1-\varepsilon>a.
$$

Hence the new $V_0$ role contains the entire former Vd1 open trace on
$e_{5,0}$.

### Own radial arm at $V_0$

By (4),

$$
C(T_0')=1-p_1>c.
$$

Thus the former own-radial trace on $r_0$ is preserved.

### Shared edge

The $V_0$ replacement reaches $1-p_1$ from $V_0$. The $V_1$ replacement
reaches at least $p_2-\varepsilon$ from $V_1$. Since

$$
(1-p_1)+(p_2-\varepsilon)
=1+(p_2-p_1-\varepsilon)>1,
$$

the two open traces overlap and cover all of $e_{0,1}$.

### Outer boundary edge at $V_1$

If $p_2\le1/2$, then

$$
B(T_1')=1-p_2>B_1.
$$

If $p_2>1/2$, then

$$
B(T_1')=1-p_2-\varepsilon>B_1
$$

by (5). Hence the former supercritical open trace on $e_{1,2}$ is preserved.

### Own radial arm at $V_1$

In both cases,

$$
C(T_1')=\max\{p_2,1-p_2\}>c_1^{\rm req}.
$$

The new vertex-side radial trace therefore overlaps the center trace, whose
vertex-side beginning is $c_1^{\rm req}$. Thus all of $r_1$ remains covered.

Consequently the modified seven open roles cover the full skeleton $S$.
Their closed C triangle remains CE2, and all six closed V triangles are now
nonsupercritical Vd0.  Now recompute the modified gap rank
$N'_{\rm gap}\in\{0,1,2\}$; no equality with the original gap rank has been
asserted or used.

If $N'_{\rm gap}=0$, the six modified open V roles cover $\partial H$, so the
common boundary-complete Method 1 consequence
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md#boundary-complete-zero-gap-consequences)
gives a contradiction.  If $N'_{\rm gap}\in\{1,2\}$, apply Sections 4 and 5
of the skeleton-level all-Vd0 theorem
[`4013`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md),
which are the nonzero-gap Method 2 branches.  These two alternatives are
exhaustive.

Reflection and undoing the fresh cyclic renumbering prove every placement
covered by the theorem.

$$
\Box
$$
