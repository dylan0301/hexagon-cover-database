# CE2, $N_+=1$, Vd1--Supercritical Adjacent Pair Axis Replacement

Status: Proven

This file proves the remaining adjacent-rescue local replacement used in the
[`4148`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md) assembly.

It treats the branch where the unique supercritical row is not $T_0$, the
unique Vd1/Vd2 row is adjacent to it, and the rescuer is Vd1.  The Vd2
neighbor-midpoint rescue branches are eliminated separately in
[`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md).

The local normal form and adjacent-ray estimates are proved in
[`4145_Vd1_Vd2_corner_side_normal_form.md`](4145_Vd1_Vd2_corner_side_normal_form.md).
The maximal $B_c(a)$ map is the one recorded in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2007_max_b_map.md),
using the admissible-set branch inequalities from
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md).

Dependency statement: the local bounds and the boundary-preserving axis
replacements are proved below. The full center-induced radial bridge is proved
in `414b`. The resulting adjacent-rescue branch is an input to the now-proved
`4013` package, so the branch is closed.

## Statement

Assume a reduced 414X cover candidate contains an adjacent pair

$$
T_{i-1}\text{ is Vd1 and covers }M_i,
\qquad
T_i\text{ is the unique supercritical row}.
$$

Assume every other vertex row is Vd0 and nonsupercritical. Then the coverage
supplied by the pair $(T_{i-1},T_i)$ can be replaced by two open-role
nonsupercritical Vd0 rows without decreasing the required boundary or radial
coverage. The replacement produces the CE2 all-Vd0 nonsupercritical
boundary/radial datum used by
[`../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md).

The reflected case in which $T_{i+1}$ is Vd1 and covers $M_i$ is identical.

## Normalized Vd1 rescuer

Normalize the pair so that the Vd1 row is a $V_0$-row touching the outgoing
adjacent ray $r_1$ and covering $M_1$. Let $a,b$ be its actual adjacent
boundary reaches. In the Case-3 use in `4148`, the center triangle has no
trace on the shared edge and no other vertex role can contribute positive
length there. Hence, if $a=b=0$, the supercritical row at $V_1$ must cover
the entire shared edge, so $a_i\ge1$. The diameter bound then forces
$a_i=1$, $b_i=0$, contradicting $a_i+b_i>1$. Thus $a+b>0$, and the exact
dichotomy in `4145` puts the rescuer in the corner-side normal form. Write

$$
d=\sqrt{t^2+t+1}.
$$

By the corner-side normal form,

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
coverage on the shared edge $e_{0,1}$ from the Vd1 side.  The Vd1 row's
own-radial reach is

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

In this Vd1 branch $t\ge1$; endpoint-only degeneracy is obtained by closure and
only weakens the inequalities below.

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

The upper bound follows from $b\ge(t-1)/(2t)$:

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

For the original open roles the inequalities used above have positive margin.
Thus the corresponding consequences are strict where needed below:

$$
a<\lambda,
\qquad
a+c<1.
$$

## Forced lower bounds on the supercritical row

The row $T_i$ must cover the part of the shared edge not covered by the Vd1 row.
Thus its incoming boundary coordinate satisfies

$$
a_i\ge1-b.
$$

The segment $V_iM_i$ is covered only by the Vd1 row and $T_i$.  Since the Vd1
row starts on this ray at $\lambda$, $T_i$ must cover at least the initial
segment up to $\lambda$ on its own ray.  Thus

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

## Max-$B$ lemma with both ordered halves

We prove

$$
\boxed{a\ge\frac12,\quad 0\le c\le\frac12
\quad\Longrightarrow\quad B_c(a)\le1-c.}
$$

Suppose, for contradiction, that an admissible triple $(a,b,c)$ satisfies

$$
a\ge\frac12,\qquad 0\le c\le\frac12,\qquad b>1-c.
$$

Then $b\ge1/2$ and $a+b>1$.  Therefore the $s>1$ admissible branch applies in
one of the two ordered halves.  In the ordered half $a\le b$, the recorded
necessary inequality is

$$
F(a,b,c):=(a^2-1)c^2+(2ab^2+b)c+(b^4-b^2)\le0.
$$

In the reflected half $b<a$, the necessary inequality is $F(b,a,c)\le0$.
We show that both inequalities are impossible.

### Ordered half $a\le b$

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
\frac{\partial}{\partial b}F\left(\frac12,b,c\right)=4b^3-2b+2bc+c.
$$

For $b\ge1-c$, this derivative is at least its value at $b=1-c$, namely

$$
-4c^3+10c^2-7c+2.
$$

This polynomial is positive on $0\le c\le1/2$: it is decreasing on this
interval and has value $1/2$ at $c=1/2$.  Hence $F(1/2,b,c)$ is increasing for
$b\ge1-c$, and

$$
F\left(\frac12,b,c\right)>F\left(\frac12,1-c,c\right).
$$

A direct calculation gives

$$
F\left(\frac12,1-c,c\right)=\frac{c^2(2c-5)(2c-1)}4\ge0
$$

for $0\le c\le1/2$.  Hence $F(a,b,c)>0$, contradicting $F(a,b,c)\le0$.

### Reflected half $b<a$

Here the necessary inequality is $F(b,a,c)\le0$.  Put $r=1-c$.  Since
$b>1-c$, both variables in $F(b,a,c)$ are at least $r$.

For $X,Y\ge r$ and $0\le c\le1/2$, the function $F(X,Y,c)$ is increasing in
$X$ and $Y$.  The $X$ derivative is

$$
2Xc^2+2Y^2c\ge0.
$$

The $Y$ derivative is

$$
4XYc+c+4Y^3-2Y.
$$

For $X,Y\ge r=1-c$, this is at least

$$
4r^2c+c+4r^3-2r=2-5c+4c^2>0
$$

on $0\le c\le1/2$.  Therefore

$$
F(b,a,c)>F(r,r,c).
$$

A direct calculation gives

$$
F(1-c,1-c,c)=c(1-2c)\ge0.
$$

Hence $F(b,a,c)>0$, contradicting $F(b,a,c)\le0$.

Thus no admissible triple has $b>1-c$, and $B_c(a)\le1-c$.

Apply this to $T_i$.  Its actual radial coordinate satisfies $c_i\le1/2$ in the
supercritical $s>1$ branch, and $c_i\ge\lambda$.  Since $a_i>1/2$, the max-$B$
lemma gives

$$
b_i\le1-c_i\le1-\lambda.
$$

Therefore

$$
\boxed{\lambda+b_i\le1.}
$$

Using $a\le\lambda$, we also get

$$
\boxed{a+b_i\le1.}
$$

For the original open-role data, $a<\lambda$ makes the last inequality strict:

$$
\boxed{a+b_i<1.}
$$

## Explicit axis-aligned replacement

We do not invoke a historical branch name from the maximal map. Instead, for
every $0\le p\le1$ construct an explicit unit Vd0 triangle in local
coordinates. If $p\le1/2$, put

$$
\Delta_p^-=
\mathrm{conv}\left\{
(0,1-p),
(1,1-p),
(0,-p)
\right\}.
$$

If $p\ge1/2$, put

$$
\Delta_p^+=
\mathrm{conv}\left\{
(p,0),
(p,1),
(p-1,0)
\right\}.
$$

In the local metric $\lVert(x,y)\rVert^2=x^2+y^2-xy$, each of the three side
vectors in either construction has length $1$. Direct intersection with the
two boundary axes gives exact reaches

$$
p,
\qquad
1-p.
$$

The own-radial reach is respectively $1-p$ and $p$, hence always

$$
\max\left\{p,1-p\right\}.
$$

The neighboring rays have no positive-length intersection with these
triangles, so they are Vd0. Consequently either construction realizes every
demand triple

$$
\left(p,1-p,c\right)
\qquad
\text{with}
\qquad
0\le c\le\max\left\{p,1-p\right\}.
$$

The endpoint constructions put the distinguished vertex on a side. We now
use the strict open-role margins to perturb them into valid vertex roles.

The proved inequalities give

$$
a<\lambda\le\frac12,
\qquad
a+c<1,
\qquad
a+b_i<1.
$$

The radial bridge theorem
[`414b_CE2_Vd1_axis_replacement_radial_bridge_target.md`](414b_CE2_Vd1_axis_replacement_radial_bridge_target.md)
gives

$$
c_i^{\mathrm{req}}
<
\max\{1-a,1-b_i\}.
$$

Choose

$$
a<p_1<p_2<1-b_i
$$

so that

$$
p_1<\frac12,
\qquad
1-p_1>c,
$$

and

$$
\max\{p_2,1-p_2\}>c_i^{\mathrm{req}}.
$$

If the bridge maximum is supplied by $1-a$, take both parameters close to
$a$. If it is supplied by $1-b_i$, first take $p_1$ close to $a$ and then take
$p_2$ close to $1-b_i$. This proves that the displayed choices are
simultaneously possible.

For $p\le1/2$, translate $\Delta_p^-$ by $(-\varepsilon,0)$. Its actual local
reaches become

$$
(p-\varepsilon,1-p,1-p).
$$

The distinguished vertex is interior, the row has zero adjacent support, and
its boundary row sum is $1-\varepsilon<1$.

For $p\ge1/2$, translate $\Delta_p^+$ by $(0,-\varepsilon)$. Its reaches
become

$$
(p,1-p-\varepsilon,p),
$$

with the same interior, zero-support, and strict row-sum conclusions. If
$p_2<1/2$, use the first translated construction for the second row as well.

Apply the first replacement with $p_1$ and the second with $p_2$. Choose
$\varepsilon>0$ smaller than all strict outer-boundary, outgoing-boundary,
shared-edge, and radial margins. The first row still reaches at least $a$ and
$c$. The second still reaches at least $b_i$ and
$c_i^{\mathrm{req}}$. The shared boundary edge is covered because

$$
(1-p_1)+(p_2-\varepsilon)>1.
$$

Thus the original Vd1--supercritical adjacent pair is replaced by two genuine
open nonsupercritical Vd0 roles while preserving the complete required
boundary and radial cover.

All other vertex rows in this branch are already nonsupercritical Vd0 rows.
Therefore the proved replacement produces a CE2 all-Vd0 boundary/radial
datum with every vertex row satisfying $a_j+b_j\le1$. The replacement is not
asserted to preserve the interior cover of $H$; the `4013` boundary-loss
contradiction consumes only the preserved perimeter coverage and the exact
complementary radial demands.

This reduces the branch to the CE1/CE2
all-Vd0 boundary-loss obstruction recorded in
[`../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md).

Thus the adjacent Vd1--supercritical rescue branch is impossible by the
proved `4013` boundary-loss obstruction.
