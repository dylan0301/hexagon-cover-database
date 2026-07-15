# CE2 Vd1--Supercritical Adjacent-Pair Axis Replacement

Status: Proven

This note proves the Vd1 replacement used in the Case-3 branch of
[`4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md`](4148_CE2_Nplus1_exactly_one_Vd1_Vd2_assembly.md).
The Vd2 alternative is eliminated by
[`4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md`](4149_CE2_Nplus1_Vd2_neighbor_midpoint_obstruction.md).

## Statement

Assume the original open roles cover the perimeter and radial skeleton in the
complementary 414X branch. Let $T_i$ be the unique supercritical row, with
$i\ne0$, and let an adjacent Vd1 row distinct from $T_0$ contain $M_i$.
Assume every other vertex row is Vd0 and nonsupercritical.

Then the Vd1--supercritical pair can be replaced by two open-role,
nonsupercritical Vd0 rows while preserving every boundary and radial demand
used by the CE2 all-Vd0 boundary-loss package. Hence this branch reduces to
the proved
[`4013`](../../40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md)
obstruction.

The case with the Vd1 row on the other side of $T_i$ follows by reflection.

## Normalization and local consequences

Normalize the Vd1 row at $V_0$, the supercritical row at $V_1$, and the
rescued midpoint as $M_1$. The center triangle has no boundary trace on the
shared edge $e_{0,1}$ in this Case-3 placement.

Let $a,b$ be the Vd1 row's exact incident-edge reaches. By the normal form in
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2014_Vd1_Vd2_corner_normal_form.md),
there are $t>0$ and

$$
d=\sqrt{t^2+t+1}
$$

such that the row is

$$
\begin{aligned}
x-(t+1)y&\le a,\\
ty-(t+1)x&\le tb,\\
tx+y&\le d-a-tb.
\end{aligned}
$$

Its own-radial reach and its neighboring-ray endpoints are

$$
c=\frac{d-a-tb}{t+1},
$$

and

$$
\lambda=\frac{t(1-b)}{t+1},
\qquad
\mu=\frac{d-a-tb-1}{t},
$$

where the neighboring-ray coordinate runs from $V_1$ toward $O$.

Because the original open Vd1 role contains $M_1$, its closure satisfies,
with strict margin,

$$
b>\frac{t-1}{2t},
\qquad
a+tb<d-1-\frac t2.
$$

The row has no positive-length intersection with the other adjacent arm
$r_5$. Since $a<1$, the lower raw endpoint there is positive. The preceding
midpoint inequality gives

$$
d-a-tb-t>1-\frac t2.
$$

If $t<1$, then

$$
1-\frac t2>\frac1{t+1}>\frac{1-a}{t+1},
$$

which would force a positive $r_5$ interval. Therefore

$$
\boxed{t\ge1.}
$$

We next record four consequences needed by the replacement:

$$
\boxed{
a+c<1,
\qquad
a<\lambda\le\frac12,
\qquad
b<\frac12,
\qquad
\mu<1-a.
}
$$

For $a+c<1$, maximize

$$
a+c=a+\frac{d-a-tb}{t+1}
$$

under the midpoint inequality. At the closed upper face

$$
a=d-1-\frac t2-tb,
$$

one has

$$
a+c-1
=-
\frac{2bt^2+2bt-2dt-2d+t^2+4t+2}{2(t+1)}.
$$

Using $b\ge(t-1)/(2t)$, the numerator is at least

$$
2t^2+4t+1-2(t+1)d.
$$

This is positive for $t\ge1$, because

$$
(2t^2+4t+1)^2-4(t+1)^2d^2
=4t^3+4t^2-4t-3>0.
$$

The last cubic is positive at $t=1$ and has positive derivative for
$t\ge1$.

The original midpoint inequalities are strict, so $a+c<1$.

The bound $\lambda\le1/2$ follows directly from
$b\ge(t-1)/(2t)$. For the other direction, the upper bound for $a$ gives

$$
a<d-1-\frac t2-tb.
$$

The right side minus $t(1-b)/(t+1)$ decreases with $b$ and, at
$b=(t-1)/(2t)$, equals $d-(t+1)<0$. Thus $a<\lambda$.

Also,

$$
b<\frac{d-1-t/2}{t}<\frac12,
$$

because $d<t+1$.

Finally,

$$
t(\mu+a-1)
=d-(t+1)-tb+(t-1)a.
$$

Using the closed midpoint bounds for $a$ and $b$ gives

$$
t(\mu+a-1)
\le t\left(d-2-\frac{t-1}{2}-tb\right)
\le t(d-t-1)<0.
$$

Hence $\mu<1-a$.

## The supercritical row

Let $a_i,b_i,c_i$ be the actual incoming, outgoing, and own-radial reaches of
the supercritical row at $V_1$. Since no center or other vertex row has
positive boundary trace on the shared edge,

$$
a_i\ge1-b>\frac12.
$$

On the rescued arm, the Vd1 interval starts at $\lambda$. The center excludes
$M_1$, and every other vertex row has zero adjacent support. Thus coverage
from $V_1$ up to the Vd1 interval forces

$$
c_i\ge\lambda.
$$

We use the following direct consequence of the exact admissible set.

### Half-square admissibility lemma

If $(x,y,z)$ is an admissible demand triple and

$$
x\ge\frac12,
\qquad
0\le z\le\frac12,
$$

then

$$
\boxed{y\le1-z.}
$$

Suppose instead that an admissible triple $(x,y,z)$ has $y>1-z$.
Then $x+y>1$, so the supercritical algebraic cell of
[`../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2004_admissible_set.md)
applies.

In the ordered half $x\le y$, its necessary inequality is

$$
F(x,y,z):=(x^2-1)z^2+(2xy^2+y)z+(y^4-y^2)\le0.
$$

The function $F$ is increasing in $x$. At $x=1/2$, its derivative in $y$ is

$$
4y^3-2y+2yz+z.
$$

This derivative is increasing for $y\ge1-z$ and is positive at $y=1-z$.
Indeed, its value there is

$$
-4z^3+10z^2-7z+2>0
$$

on $0\le z\le1/2$: its derivative is nonpositive there, and its value at
$z=1/2$ is $1/2$. The derivative with respect to $y$ is increasing because
its own derivative is at least

$$
12(1-z)^2-2+2z>0.
$$

Therefore

$$
F(x,y,z)>F\left(\frac12,1-z,z\right)
=\frac{z^2(2z-5)(2z-1)}4\ge0,
$$

a contradiction.

In the reflected half $y<x$, the necessary inequality is $F(y,x,z)\le0$.
Put $r=1-z$. Both arguments of $F$ are greater than or equal to $r$. On this
quadrant $F$ is increasing in both arguments: the first derivative is
nonnegative, and the second is bounded below by

$$
4r^2z+z+4r^3-2r=2-5z+4z^2>0.
$$

Here $4v^3-2v$ is increasing for $v\ge r\ge1/2$, which justifies the stated
lower bound.

Thus

$$
F(y,x,z)>F(r,r,z)=z(1-2z)\ge0,
$$

again a contradiction. This proves the lemma.

For a supercritical row, the selected cell gives $c_i\le1/2$. Applying the
lemma to $(x,y,z)=(a_i,b_i,c_i)$ yields

$$
b_i\le1-c_i\le1-\lambda.
$$

Since $a<\lambda$,

$$
\boxed{a+b_i<1.}
$$

## Center handoff

Let $d_i$ be the center triangle's covered length on the rescued arm, measured
from $O$ toward $V_i$, and let

$$
c_i^{\mathrm{req}}=1-d_i
$$

be the exact vertex-side demand left by the CE2 center triangle on the rescued
arm. The only original open roles with positive intervals on this arm are the
supercritical row, the Vd1 row, and the center row. Therefore open coverage at
the center handoff forces

$$
c_i^{\mathrm{req}}<\max\{c_i,\mu\}.
$$

Equality would leave the common open exit or entry point uncovered. Combining
the preceding bounds gives

$$
\boxed{
c_i^{\mathrm{req}}<\max\{1-b_i,1-a\}.
}
$$

This proves the required radial bridge.

## Explicit Vd0 replacements

For $0\le p\le1$, define a closed unit triangle by

$$
\Delta_p^-=
\mathrm{conv}\left\{
(0,1-p),(1,1-p),(0,-p)
\right\}
\qquad(p\le1/2),
$$

and

$$
\Delta_p^+=
\mathrm{conv}\left\{
(p,0),(p,1),(p-1,0)
\right\}
\qquad(p\ge1/2).
$$

In the local metric, all three side vectors have length $1$. The two
incident-edge reaches are $p$ and $1-p$, the own-radial reach is respectively
$1-p$ or $p$, and there is no positive adjacent-ray support.

The strict inequalities proved above allow parameters

$$
a<p_1<p_2<1-b_i
$$

such that

$$
p_1<\frac12,
\qquad
1-p_1>c,
$$

and

$$
\max\{p_2,1-p_2\}>c_i^{\mathrm{req}}.
$$

Choose $p_1$ close to $a$. For $p_2$, choose a point close to $a$ if the
radial bridge is supplied by $1-a$, and close to $1-b_i$ if it is supplied by
$1-b_i$.

Translate $\Delta_{p_1}^-$ by $(-\varepsilon,0)$. Its actual reaches become

$$
(p_1-\varepsilon,1-p_1,1-p_1).
$$

The distinguished vertex is interior, the row has zero adjacent support, and
its boundary sum is $1-\varepsilon$.

For the second row, translate $\Delta_{p_2}^-$ by $(-\varepsilon,0)$ when
$p_2<1/2$, and translate $\Delta_{p_2}^+$ by $(0,-\varepsilon)$ when
$p_2\ge1/2$. The relevant reaches are respectively

$$
(p_2-\varepsilon,1-p_2,1-p_2)
$$

or

$$
(p_2,1-p_2-\varepsilon,p_2).
$$

Choose $\varepsilon>0$ below every strict boundary and radial margin. The
first row still supplies at least $a$ and $c$, and the second still supplies
at least $b_i$ and $c_i^{\mathrm{req}}$. The shared boundary edge is covered
because

$$
(1-p_1)+(p_2-\varepsilon)>1.
$$

Thus both replacements are genuine open Vd0 roles with boundary sum less
than $1$, and all required boundary and radial intervals are preserved. Every
other vertex row was already nonsupercritical Vd0. The resulting datum is
therefore excluded by the proved `4013` all-Vd0 boundary-loss package.

$$
\Box
$$
