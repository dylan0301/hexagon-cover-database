# Full T3-Like Tangent-Envelope Conjecture: Failure Report

Status: Failed

## 1. Failed claim

The proposed no-midpoint T3-like envelope used the branch

$$
A(s)=\frac{s(s^2-s+1)}{1-s^2},
$$

$$
B(s)=\frac{s^2-s+1}{1+s},
$$

$$
F(s)=\frac{(s^2-s+1)^2}{1-s^2},
\qquad
0\le s\le\frac12,
$$

together with its reflection obtained by swapping $A(s)$ and $B(s)$.

The conjecture asserted that every closed unit equilateral $V_0$-triangle of
T3-like type

$$
(o,n)=(2,1)
$$

with required boundary data $(a,b)$ was coordinatewise dominated by one of
these two branches, with its normalized inside area also bounded by the branch
value.

That coordinatewise domination statement is false.

## 2. Local coordinate system

Use

$$
X=V_0+x(V_1-V_0)+y(V_5-V_0).
$$

Then

$$
V_0=(0,0),
$$

the adjacent boundary edges are the positive coordinate axes, and physical
squared distance is

$$
\lVert (x,y)\rVert^2=x^2+y^2-xy.
$$

Physical rotation by $60^\circ$ is

$$
R(x,y)=(x-y,x).
$$

## 3. Exact counterexample

Set

$$
d=
\left(
\frac1{\sqrt7},
-\frac2{\sqrt7}
\right).
$$

Then

$$
\lVert d\rVert^2
=
\frac17+\frac47+\frac27
=1.
$$

Let

$$
Q_-=-\frac15d
=
\left(
-\frac1{5\sqrt7},
\frac2{5\sqrt7}
\right),
$$

$$
Q_+=\frac45d
=
\left(
\frac4{5\sqrt7},
-\frac8{5\sqrt7}
\right),
$$

and

$$
S=Q_-+Rd
=
\left(
\frac{2\sqrt7}{5},
\frac{\sqrt7}{5}
\right).
$$

The triangle

$$
T=\mathrm{conv}\left\{Q_-,Q_+,S\right\}
$$

is a unit equilateral triangle.  Indeed, its three side vectors are

$$
d,
\qquad
Rd,
\qquad
Rd-d,
$$

all of physical length $1$.

Also,

$$
Q_-+\frac15(Q_+-Q_-)=0,
$$

so $V_0=(0,0)\in T$.

### 3.1 T3-like type

The vertex $Q_-$ has negative $x$ coordinate, and $Q_+$ has negative $y$
coordinate, so both lie outside $H$.

The vertex $S$ satisfies

$$
0<S_y<S_x<2
$$

and

$$
S_x-S_y=\frac{\sqrt7}{5}<1.
$$

Hence $S\in H$.  Therefore exactly two vertices of $T$ lie outside $H$:

$$
o=2.
$$

The part of $T$ in the local wedge is the quadrilateral with vertices

$$
(0,0),\qquad
\left(\frac{4\sqrt7}{15},0\right),\qquad
S,\qquad
\left(0,\frac{\sqrt7}{15}\right).
$$

Since

$$
S_x=\frac{2\sqrt7}{5}>1
$$

and the other positive-axis $x$ coordinate is below $1$, the triangle has
positive-length intersection with the adjacent ray $x=1$.

All three triangle vertices have $y<1$, so the triangle does not meet the other
adjacent ray $y=1$.  Thus

$$
n=1.
$$

Consequently,

$$
\boxed{(o,n)=(2,1),}
$$

so $T$ is T3-like.

### 3.2 Boundary data and area

The exact adjacent boundary reaches are

$$
a=\frac{\sqrt7}{15},
\qquad
b=\frac{4\sqrt7}{15}.
$$

The normalized inside area is twice the affine-coordinate area of the
quadrilateral above:

$$
\begin{aligned}
F_T
&=
bS_y+aS_x
\\
&=
\frac{4\sqrt7}{15}\frac{\sqrt7}{5}
+
\frac{\sqrt7}{15}\frac{2\sqrt7}{5}
\\
&=
\frac{14}{25}.
\end{aligned}
$$

Thus the exact counterexample data is

$$
\boxed{
\left(
a,b,F_T
\right)
=
\left(
\frac{\sqrt7}{15},
\frac{4\sqrt7}{15},
\frac{14}{25}
\right).
}
$$

## 4. Failure of coordinatewise domination

On $0\le s\le1/2$,

$$
A'(s)=
\frac{1-2s+4s^2-s^4}{(1-s^2)^2}>0,
$$

so $A$ is strictly increasing, while

$$
B'(s)=
\frac{s^2+2s-2}{(1+s)^2}<0,
$$

so $B$ is strictly decreasing.

At

$$
s=\frac15,
$$

the branch values are

$$
A\left(\frac15\right)=\frac7{40},
\qquad
B\left(\frac15\right)=\frac7{10}.
$$

The counterexample satisfies

$$
\frac{\sqrt7}{15}>\frac7{40}
$$

and

$$
\frac{4\sqrt7}{15}>\frac7{10}.
$$

Both inequalities are equivalent to

$$
8\sqrt7>21,
$$

which follows after squaring from $448>441$.

If $s\le1/5$, then

$$
A(s)\le A(1/5)<a.
$$

If $s\ge1/5$, then

$$
B(s)\le B(1/5)<b.
$$

Therefore no point of the unreflected branch satisfies

$$
A(s)\ge a,
\qquad
B(s)\ge b.
$$

For the reflected branch, domination would require $A(s)\ge b$.  But

$$
A(s)\le A(1/2)=\frac12
<
\frac{4\sqrt7}{15}=b.
$$

Hence no reflected branch point dominates the counterexample either.

This disproves the proposed coordinatewise tangent-envelope conjecture.

## 5. What remains valid

The one-dimensional branch formulas themselves are correct.  In particular,
the branch loss inequalities proved algebraically in
[`3173_T3_like_loss_from_envelope.md`](3173_T3_like_loss_from_envelope.md)
remain valid statements about that boundary family.

What fails is the claim that every T3-like triangle is coordinatewise dominated
by the family.

The weaker area statement needed by the CE0 global proof is nevertheless true.
A direct orientation and area argument proves

$$
a,b\ge m
\quad\Longrightarrow\quad
G_{\mathrm{T3}}(a,b)\ge2m-4m^2
$$

without coordinatewise domination.  See
[`3175_direct_T3_like_area_loss.md`](3175_direct_T3_like_area_loss.md).

Thus this failed envelope is not used in the completed `317X` proof.
