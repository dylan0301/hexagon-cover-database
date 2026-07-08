# CE2, $N_+=1$, Vd1--Supercritical Adjacent Pair Axis Replacement

Status: Proven

This file proves the remaining adjacent-rescue local replacement used in the
[`4140`](4140_CE2_Nplus1_exactly_one_Vd1_Vd2_TODO.md) assembly.

It treats the branch where the unique supercritical row is not $T_0$, the
unique Vd1/Vd2 row is adjacent to it, and the rescuer is Vd1.  The Vd2
neighbor-midpoint rescue branches are eliminated separately in
[`4142_CE2_Nplus1_Vd2_midpoint_local_caps.md`](4142_CE2_Nplus1_Vd2_midpoint_local_caps.md).

The local normal form used below is proved in
[`4145_Vd1_Vd2_corner_side_normal_form.md`](4145_Vd1_Vd2_corner_side_normal_form.md).
The maximal $B_c(a)$ map is the one recorded in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md),
using the admissible-set branch inequalities from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).

## Statement

Assume a reduced 414X cover candidate contains an adjacent pair

$$
T_{i-1}\text{ is Vd1 and covers }M_i,
\qquad
T_i\text{ is the unique supercritical row}.
$$

Assume every other vertex row is Vd0 and nonsupercritical.  Then the boundary
coverage supplied by the pair $(T_{i-1},T_i)$ can be replaced by two
axis-aligned nonsupercritical Vd0 rows, without decreasing the boundary
coverage on the three boundary edges affected by the pair.

Consequently, any full cover in this branch would imply a CE2 all-Vd0
nonsupercritical boundary cover, contradicting the proved all-Vd0 CE1/CE2
boundary-loss package
[`../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md).

The reflected case in which $T_{i+1}$ is Vd1 and covers $M_i$ is identical.

## Normalized Vd1 rescuer

Normalize the pair so that the Vd1 row is a $V_0$-row touching the outgoing
adjacent ray $r_1$ and covering $M_1$.  Write

$$
d=\sqrt{t^2+t+1}.
$$

By the corner-side normal form, after reflection if necessary,

$$
x-(t+1)y\le a,
$$

$$
ty-(t+1)x\le tb,
$$

and

$$
tx+y\le d-a-tb.
$$

Here $a$ is the boundary coverage on the outer edge $e_{5,0}$, and $b$ is the
coverage on the shared edge $e_{0,1}$ from the Vd1 side.

The Vd1 row's own-radial reach is

$$
c=\frac{d-a-tb}{t+1}.
$$

Its first point on the neighboring ray $r_1$, measured from $V_1$ toward $O$, is

$$
\lambda=\frac{t(1-b)}{t+1}.
$$

The condition $M_1\in T_0$ gives

$$
b\ge \frac{t-1}{2t}
$$

and

$$
a+tb\le d-1-\frac t2.
$$

In this Vd1 branch the non-touched adjacent ray condition gives $t\ge1$.

## First pair inequality

We prove

$$
\boxed{a+c\le1.}
$$

Since

$$
a+c=a+\frac{d-a-tb}{t+1},
$$

this expression is increasing in $a$.  Therefore its maximum under

$$
a+tb\le d-1-\frac t2
$$

occurs when

$$
a=d-1-\frac t2-tb.
$$

At this value,

$$
a+c-1
=
-\frac{2bt^2+2bt-2dt-2d+t^2+4t+2}{2(t+1)}.
$$

Using

$$
b\ge\frac{t-1}{2t},
$$

the numerator is at least

$$
2t^2+4t+1-2(t+1)d.
$$

Thus it is enough to prove

$$
2t^2+4t+1\ge2(t+1)d.
$$

Both sides are positive.  Squaring gives

$$
(2t^2+4t+1)^2-4(t+1)^2(t^2+t+1)=4t^3+4t^2-4t-3.
$$

For $t\ge1$, this is positive: at $t=1$ it equals $1$, and its derivative is
$12t^2+8t-4>0$.  Hence $a+c\le1$.

## The neighboring-ray entry satisfies $a\le\lambda\le1/2$

The upper bound follows from

$$
b\ge\frac{t-1}{2t}:
$$

$$
\lambda=\frac{t(1-b)}{t+1}\le\frac12.
$$

For the lower bound, use

$$
a\le d-1-\frac t2-tb.
$$

It is enough to prove

$$
d-1-\frac t2-tb\le\frac{t(1-b)}{t+1}.
$$

The left side minus the right side is decreasing in $b$, so it is maximized at
$b=(t-1)/(2t)$.  At that value the difference is

$$
d-(t+1)<0.
$$

Therefore

$$
\boxed{a\le\lambda\le\frac12.}
$$

## Forced lower bounds on the supercritical row

The row $T_i$ must cover the part of the shared edge not covered by the Vd1
row.  Thus its incoming boundary coordinate satisfies

$$
a_i\ge1-b.
$$

The segment $V_iM_i$ is covered only by the Vd1 row and $T_i$.  Since the Vd1
row starts on this ray at $\lambda$, $T_i$ must cover at least the initial
segment up to $\lambda$ on its own ray.  Thus its own-radial coordinate satisfies

$$
c_i\ge\lambda.
$$

Also $b<1/2$.  Indeed, $a\ge0$ and

$$
a+tb\le d-1-\frac t2
$$

imply

$$
b\le\frac{d-1-t/2}{t}<\frac12,
$$

because $d<t+1$.  Hence

$$
a_i\ge1-b>\frac12.
$$

## Max-$B$ lemma

We prove the following local consequence of the admissible-set branch
inequalities:

$$
\boxed{a\ge\frac12,\quad 0\le c\le\frac12
\quad\Longrightarrow\quad B_c(a)\le1-c.}
$$

Suppose, for contradiction, that an admissible triple $(a,b,c)$ satisfies

$$
a\ge\frac12,\qquad 0\le c\le\frac12,\qquad b>1-c.
$$

Then $a+b>1$, so the triple lies in the $s>1$ branch of the admissible set.  In
that branch, the recorded necessary inequality is

$$
F(a,b,c):=(a^2-1)c^2+(2ab^2+b)c+(b^4-b^2)\le0.
$$

For $a\ge1/2$, $b\ge0$, and $c\ge0$,

$$
\frac{\partial F}{\partial a}=2ac^2+2b^2c\ge0.
$$

Thus

$$
F(a,b,c)\ge F\left(\frac12,b,c\right).
$$

Now

$$
\frac{\partial}{\partial b}F\left(\frac12,b,c\right)
=4b^3-2b+2bc+c.
$$

For $b\ge1-c$, this derivative is at least its value at $b=1-c$, namely

$$
-4c^3+10c^2-7c+2.
$$

This polynomial is positive on $0\le c\le1/2$: it is decreasing on this
interval and has value $1/2$ at $c=1/2$.  Hence
$F(1/2,b,c)$ is increasing for $b\ge1-c$, and so

$$
F\left(\frac12,b,c\right)>F\left(\frac12,1-c,c\right).
$$

A direct calculation gives

$$
F\left(\frac12,1-c,c\right)=\frac{c^2(2c-5)(2c-1)}4\ge0
$$

for $0\le c\le1/2$.  Therefore $F(a,b,c)>0$, contradicting the necessary
branch inequality $F(a,b,c)\le0$.

Thus no admissible triple has $b>1-c$, and $B_c(a)\le1-c$.

Apply this to $T_i$.  Its actual radial coordinate satisfies $c_i\le1/2$ in the
$s>1$ branch, and $c_i\ge\lambda$.  Since $a_i>1/2$, the max-$B$ lemma gives

$$
b_i\le1-c_i\le1-\lambda.
$$

Hence

$$
\boxed{\lambda+b_i\le1.}
$$

Using $a\le\lambda$, we also get

$$
\boxed{a+b_i\le1.}
$$

## Axis-aligned replacement

The boundary candidate in the maximal map is

$$
b_F(a)=1-a,
$$

with domain

$$
0\le a\le1,\qquad 0\le c\le\max(a,1-a).
$$

Because $a+c\le1$, we have $c\le1-a\le\max(a,1-a)$.  Therefore there is an
axis-aligned admissible Vd0 row at $V_{i-1}$ with local triple

$$
(a,\ 1-a,\ c).
$$

It preserves the outer boundary coverage $a$, preserves at least the own-radial
coverage $c$, and satisfies

$$
a+(1-a)=1.
$$

Likewise, since $\lambda+b_i\le1$, there is an axis-aligned admissible Vd0 row
at $V_i$ with local triple

$$
(1-b_i,\ b_i,\ \lambda).
$$

It preserves the outgoing boundary coverage $b_i$, covers the required initial
radial part up to $\lambda$, and satisfies

$$
(1-b_i)+b_i=1.
$$

The shared edge between the two replacement rows is covered because the two
replacement contributions have lengths $1-a$ and $1-b_i$, and

$$
(1-a)+(1-b_i)\ge1
$$

is equivalent to $a+b_i\le1$.

Thus the original Vd1--supercritical adjacent pair can be replaced, for
boundary coverage purposes, by two nonsupercritical Vd0 rows.

All other vertex rows in this branch are already nonsupercritical Vd0 rows.
Therefore any boundary cover in this branch would produce a CE2 all-Vd0 cover
with every vertex row satisfying $a_j+b_j\le1$.

This contradicts the CE1/CE2 all-Vd0 boundary-loss obstruction recorded in
[`../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md).

Hence the adjacent Vd1--supercritical rescue branch is impossible.
