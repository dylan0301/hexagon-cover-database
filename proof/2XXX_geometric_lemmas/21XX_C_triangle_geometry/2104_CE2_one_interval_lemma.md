# CE2 Two-Gap Systems Are Not Skeleton-Maximal

Status: Proven

This note proves a replacement theorem for an all-Vd0 skeleton cover. It
formalizes the useful part of the proposed monotonicity argument without
claiming that the original supercritical triangle already binds a center
interval endpoint.

## Normalization and gaps

Use the exact-$M_0$ CE2 normalization from
[`2103_CE2_M0_e50_e01_maximal_interval_pairs.md`](2103_CE2_M0_e50_e01_maximal_interval_pairs.md):

$$
T_C\cap e_{5,0}=[x,u],
\qquad
T_C\cap e_{0,1}=[y,v],
$$

where both edges are parameterized from $V_0$ and

$$
0<x<u<1,
\qquad
0<y<v<1.
$$

Let the actual adjacent boundary reaches of $T_0$ be

$$
a_0\text{ on }e_{5,0},
\qquad
b_0\text{ on }e_{0,1}.
$$

There is a V-gap in each CE2 interval exactly when

$$
J_L=(a_0,1-b_5)\subset[x,u]
$$

and

$$
J_R=(b_0,1-a_1)\subset[y,v]
$$

are nonempty. In particular,

$$
x\le a_0<1-b_5\le u,
$$

$$
y\le b_0<1-a_1\le v.
$$

The exact complementary radial demand at $V_0$ is, by
[`2106_CE2_exact_formulas.md`](2106_CE2_exact_formulas.md),

$$
c_0=\frac{xy}{x+y}.
$$

## Replacement-maximality convention

With $T_C$ and the other five vertex roles fixed, call the local skeleton
data at $V_0$ replacement-maximal if no unit equilateral replacement for
$T_0$ can do all of the following:

1. preserve the full skeleton cover;
2. preserve both boundary reaches already assigned to $T_0$;
3. preserve the complementary radial coverage required from $V_0$; and
4. strictly extend one boundary reach through a nonempty V-gap.

This is the $T_C$-relative maximality used in this note. Support that is lost
only where it is already covered by $T_C$ is not an uncovered loss.

## Theorem

An all-Vd0 CE2 system with V-gaps in both center intervals is not
replacement-maximal. More precisely, there are two replacements:

- a left replacement preserving $b_0$ and extending $a_0$ to $u$;
- a right replacement preserving $a_0$ and extending $b_0$ to $v$.

There is also a simultaneous replacement extending both reaches to $u$ and
$v$. It makes both CE2 center intervals redundant for boundary coverage and,
after exact unit enlargement, is a supercritical Vd0 row.

Either replacement preserves the skeleton cover and makes one entire CE2
center interval redundant for boundary coverage.

The supercritical hypothesis is not needed for this theorem. In the `410X`
branch, it is used separately to identify $T_0$ as the unique supercritical
row.

## Complementary corner triangle

Use local affine coordinates

$$
X(p,q)=V_0+p(V_5-V_0)+q(V_1-V_0).
$$

The local metric is

$$
\lVert X(p,q)-V_0\rVert^2=p^2+q^2-pq.
$$

For $a,b>0$, define

$$
A=X(a,0),
\qquad
B=X(0,b),
\qquad
Q=X(-b,-a),
$$

and

$$
\Delta(a,b)=\mathrm{conv}\left\{A,B,Q\right\}.
$$

The three squared side lengths are all

$$
a^2+ab+b^2.
$$

Thus $\Delta(a,b)$ is equilateral with side length

$$
L(a,b)=\sqrt{a^2+ab+b^2}.
$$

The point $V_0=X(0,0)$ lies in $\Delta(a,b)$. Indeed, positive barycentric
coefficients are obtained from

$$
\lambda_A=\frac ba\lambda_Q,
\qquad
\lambda_B=\frac ab\lambda_Q,
$$

with

$$
\lambda_A+\lambda_B+\lambda_Q=1.
$$

The side $AB$ has equation

$$
\frac pa+\frac qb=1.
$$

Consequently the radial ray $X(c,c)$ exits $\Delta(a,b)$ at

$$
c=\frac{ab}{a+b}.
$$

By convexity, $\Delta(a,b)$ contains the two boundary segments of lengths
$a,b$ from $V_0$ and the radial segment of length $ab/(a+b)$.

## Simultaneous two-gap replacement

Use

$$
a=u,
\qquad
b=v.
$$

Both endpoint points

$$
e_{5,0}(u),
\qquad
e_{0,1}(v)
$$

belong to the same unit center triangle $T_C$. Its diameter is one, so

$$
L:=\sqrt{u^2+uv+v^2}\le1.
$$

The complementary corner triangle

$$
\Delta(u,v)
$$

contains the full boundary segments of lengths $u$ and $v$. Since
$u\ge x$ and $v\ge y$, monotonicity of $pq/(p+q)$ gives

$$
\frac{uv}{u+v}
\ge
\frac{xy}{x+y}
=c_0.
$$

Thus this single triangle preserves the radial handoff at $V_0$ and covers
both center-boundary intervals.

If $L<1$, enlarge $\Delta(u,v)$ about $V_0$ by the factor $1/L$. In the local
coordinates $X(p,q)$, the resulting unit triangle has vertices

$$
\left(\frac uL,0\right),
\qquad
\left(0,\frac vL\right),
\qquad
\left(-\frac vL,-\frac uL\right).
$$

Its actual adjacent boundary reaches are

$$
a_0'=\frac uL,
\qquad
b_0'=\frac vL.
$$

Because

$$
L^2-u^2=uv+v^2>0,
\qquad
L^2-v^2=u^2+uv>0,
$$

both positive vertices lie before the neighboring hexagon vertices. The
third vertex has both local coordinates negative. Moreover every point of
the triangle has both local coordinates strictly less than one, so it has no
positive intersection with either adjacent radial arm. It is therefore Vd0.

Finally,

$$
(u+v)^2-L^2=uv>0,
$$

and hence

$$
a_0'+b_0'=\frac{u+v}{L}>1.
$$

The simultaneous replacement is exactly supercritical and turns the two-gap
system into an all-boundary-covered CE2 skeleton system. This is an exact
branch classification of the replacement; it is not a claim that the
original $T_0$ binds either endpoint.

## Left replacement

Use

$$
a=u,
\qquad
b=b_0.
$$

The two points

$$
e_{5,0}(u),
\qquad
e_{0,1}(b_0)
$$

belong to $T_C$, because $b_0\in[y,v]$. A unit equilateral triangle has
diameter one, so

$$
u^2+ub_0+b_0^2
=
\left\lVert e_{5,0}(u)-e_{0,1}(b_0)\right\rVert^2
\le1.
$$

Hence

$$
L(u,b_0)\le1.
$$

The function

$$
f(p,q)=\frac{pq}{p+q}
$$

is increasing in both variables on the positive quadrant. Since

$$
u\ge x,
\qquad
b_0\ge y,
$$

we have

$$
\frac{ub_0}{u+b_0}
\ge
\frac{xy}{x+y}
=c_0.
$$

Therefore

$$
T_0^L=\Delta(u,b_0)
$$

has side length at most one, preserves the old outgoing reach $b_0$, covers
the required radial segment, and extends the incoming reach through $u$.
In particular,

$$
T_C\cap e_{5,0}=[x,u]\subset T_0^L.
$$

If a triangle of side exactly one is required, enlarge $T_0^L$
concentrically to side one.

## Right replacement

The reflected construction uses

$$
a=a_0,
\qquad
b=v.
$$

Now $a_0\in[x,u]$, so both

$$
e_{5,0}(a_0),
\qquad
e_{0,1}(v)
$$

belong to $T_C$. Therefore

$$
a_0^2+a_0v+v^2\le1,
$$

and

$$
\frac{a_0v}{a_0+v}
\ge
\frac{xy}{x+y}
=c_0.
$$

Thus

$$
T_0^R=\Delta(a_0,v)
$$

preserves $a_0$, covers the required radial segment, and extends the outgoing
reach through $v$. Hence

$$
T_C\cap e_{0,1}=[y,v]\subset T_0^R.
$$

## Preservation of the skeleton cover

For the left replacement, the new triangle weakly enlarges the old
$T_0$-coverage on $e_{5,0}$ and preserves it on $e_{0,1}$. It covers the
radial arm from $V_0$ through the complementary handoff point $c_0$, while
$T_C$ covers the remaining radial segment to $O$. The right replacement is
symmetric.

An all-Vd0 $T_0$ has no positive-length support on another radial arm.
Point-only contacts cannot be essential in a finite closed cover: a punctured
sequence near such a point is covered by the other finitely many closed
triangles, so one of them contains a convergent subsequence and hence the
limit point. Thus either replacement preserves the full skeleton cover.

Because $J_L$ or $J_R$ has positive length and is newly covered by either
one-sided replacement, the original two-gap system was not
replacement-maximal. The simultaneous replacement covers both positive gaps
and gives the stronger exact exit stated above.

## Why bare monotonicity is insufficient

Supercriticality alone does not force the original $T_0$ to bind $u$ or $v$.
For example, set

$$
x=y=\frac3{10},
\qquad
u=v=\frac{10\sqrt3+3}{40},
\qquad
c_0=\frac3{20}.
$$

These values satisfy the CE2 coupling and strict midpoint inequalities. In
physical coordinates with $V_0=(0,0)$ and the inward radial direction
horizontal, take the unit triangle with vertices

$$
\left(-\frac{101}{200},0\right),
$$

$$
\left(\frac{\sqrt3}{2}-\frac{101}{200},\frac12\right),
$$

and

$$
\left(\frac{\sqrt3}{2}-\frac{101}{200},-\frac12\right).
$$

It has

$$
a_0=b_0=\frac{101}{200},
$$

and radial reach

$$
\frac{\sqrt3}{2}-\frac{101}{200}>\frac3{20}.
$$

Thus

$$
a_0+b_0>1,
\qquad
a_0<u,
\qquad
b_0<v.
$$

The proved conclusion is therefore an explicit replacement normalization,
not a claim about endpoint binding by the original supercritical triangle.

## Proof-tree scope

Concentric enlargement can change the V-type or the value of $N_+$. The
replacement proves the two-gap skeleton normalization, but a branch proof
must route every changed type or row-sum class to the corresponding proof-tree
branch. It may not silently assume that the replacement stays inside `410X`.
