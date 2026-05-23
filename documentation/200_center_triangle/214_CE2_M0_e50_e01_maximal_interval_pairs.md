# CE2, Exact Midpoint $M_0$, Edges $e_{5,0}$ and $e_{0,1}$: Maximal Interval Pairs

Status: Proven certificate with numerical check

This note proves the normalized CE2 subcase in which

$$
T_C\cap \{M_0,\dots,M_5\}=\{M_0\}
$$

and the only positive-length overlaps with the hexagon boundary are on

$$
e_{5,0}
\qquad\text{and}\qquad
e_{0,1}.
$$

Write

$$
T_C\cap e_{5,0}=[s_{50},t_{50}],
\qquad
T_C\cap e_{0,1}=[s_{01},t_{01}].
$$

Maximality is product interval inclusion:

$$
([s_{50},t_{50}],[s_{01},t_{01}])
\preceq
([s'_{50},t'_{50}],[s'_{01},t'_{01}])
$$

if and only if

$$
s'_{50}\le s_{50},\quad t'_{50}\ge t_{50},
\qquad
s'_{01}\le s_{01},\quad t'_{01}\ge t_{01}.
$$

## Theorem

Set

$$
x=s_{50},\qquad u=t_{50},\qquad y=s_{01},\qquad v=t_{01},
$$

and define

$$
S=x+y,\qquad D=\sqrt{x^2+xy+y^2}.
$$

The maximal feasible interval pairs are exactly the pairs

$$
\boxed{
([s_{50},t_{50}],[s_{01},t_{01}])=([x,u],[y,v])
}
$$

satisfying

$$
\boxed{
0<x<u<1,\qquad 0<y<v<1,
}
$$

$$
\boxed{
(u+v)(x+y)-xy=\sqrt{x^2+xy+y^2},
}
$$

$$
\boxed{
u(x+y)\ge x,\qquad v(x+y)\ge y,
}
$$

and

$$
\boxed{
u(x+y)<x+\frac y2,\qquad v(x+y)<y+\frac x2.
}
$$

Equivalently, the square root can be removed by replacing the middle equation with

$$
\left((u+v)(x+y)-xy\right)^2=x^2+xy+y^2,
\qquad
(u+v)(x+y)-xy>0.
$$

Every feasible pair satisfying these conditions is already product-maximal. Thus the two edge intervals are not independently optimizable; they are coupled by the equation above.

## Coordinates

Use the standard physical coordinates

$$
O=(0,0),
\qquad
V_i=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right),
\qquad
M_i=\frac12V_i.
$$

Thus

$$
V_0=(1,0),\quad
V_1=\left(\frac12,\frac{\sqrt3}{2}\right),\quad
V_5=\left(\frac12,-\frac{\sqrt3}{2}\right),
$$

and

$$
M_0=\left(\frac12,0\right),\quad
M_1=\left(\frac14,\frac{\sqrt3}{4}\right),\quad
M_5=\left(\frac14,-\frac{\sqrt3}{4}\right).
$$

The two target edges are parameterized by

$$
e_{0,1}(b)=V_0+b(V_1-V_0)
=
\left(1-\frac b2,\frac{\sqrt3}{2}b\right),
\qquad 0\le b\le1,
$$

and

$$
e_{5,0}(a)=V_0+a(V_5-V_0)
=
\left(1-\frac a2,-\frac{\sqrt3}{2}a\right),
\qquad 0\le a\le1.
$$

A closed unit equilateral triangle may be written as

$$
T=\{X:\ell_i(X)\ge0,\ i=0,1,2\},
$$

where

$$
\ell_i(X)=\alpha_i-n_i\cdot X,
$$

the outward unit normals $n_i$ are separated by $120^\circ$, and

$$
\alpha_0+\alpha_1+\alpha_2=\frac{\sqrt3}{2}.
$$

The last identity is the unit side-length condition.

## The side visible from $V_0$

First, $V_0\notin T_C$. If $V_0\in T_C$, then $O,V_0\in T_C$ and $|O-V_0|=1$. In a unit equilateral triangle, distance $1$ is attained only by pairs of vertices. Hence $O$ and $V_0$ would be two vertices of $T_C$. The third vertex would be $V_1$ or $V_5$, so the triangle would have positive-length boundary overlap with only one of $e_{0,1}$ and $e_{5,0}$, not both.

Since $V_0\notin T_C$, at least one side inequality is violated at $V_0$. If a side with outward normal $n=(p,q)$ is violated at $V_0$, then the positive-length intersections on both adjacent edges force the slack to increase from $V_0$ in both directions $V_1-V_0$ and $V_5-V_0$. Therefore

$$
n\cdot(V_1-V_0)<0,
\qquad
n\cdot(V_5-V_0)<0.
$$

Equivalently,

$$
p>\sqrt3|q|.
$$

This is an open $60^\circ$ cone. Among three outward normals separated by $120^\circ$, at most one lies in this cone. Hence exactly one side is violated at $V_0$. Relabel the sides so that this side is side $2$. It cuts the initial endpoints $x=s_{50}$ and $y=s_{01}$.

Let

$$
S=x+y,\qquad D=\sqrt{x^2+xy+y^2}.
$$

The side $2$ line passes through $e_{5,0}(x)$ and $e_{0,1}(y)$. Its outward unit normal pointing toward $V_0$ is

$$
n_2=\frac1{2D}\left(\sqrt3(x+y),\,y-x\right).
$$

Define

$$
n_0=R_{2\pi/3}n_2,\qquad n_1=R_{-2\pi/3}n_2.
$$

The side constants are then forced by the endpoint conditions:

$$
\alpha_2=n_2\cdot e_{5,0}(x)=n_2\cdot e_{0,1}(y)
=
\frac{\sqrt3(x+y-xy)}{2D},
$$

$$
\alpha_0=n_0\cdot e_{0,1}(v)
=
\frac{\sqrt3(v(x+y)-y)}{2D},
$$

and

$$
\alpha_1=n_1\cdot e_{5,0}(u)
=
\frac{\sqrt3(u(x+y)-x)}{2D}.
$$

Conversely, for any endpoint data satisfying the theorem, these formulas define three halfplanes with outward unit normals separated by $120^\circ$.

## The unit-equilateral coupling equation

Using the unit side-length condition,

$$
\alpha_0+\alpha_1+\alpha_2=\frac{\sqrt3}{2}.
$$

Substituting the three constants gives

$$
\frac{\sqrt3}{2D}
\left(vS-y+uS-x+S-xy\right)
=
\frac{\sqrt3}{2}.
$$

Since $S=x+y$, this is equivalent to

$$
\boxed{
(u+v)S-xy=D.
}
$$

Thus

$$
\boxed{
(u+v)(x+y)-xy=\sqrt{x^2+xy+y^2}.
}
$$

This is the coupling relation between the two edge intervals.

## Exact target inequalities

The positive-length target edge overlaps require

$$
0<x<u<1,\qquad 0<y<v<1.
$$

Because $O=(0,0)$, the condition $O\in T_C$ is

$$
\alpha_i\ge0,\qquad i=0,1,2.
$$

Here $\alpha_2>0$ automatically, and the other two inequalities are

$$
\boxed{
uS\ge x,\qquad vS\ge y.
}
$$

Now compute midpoint slacks. The table below is scaled by the positive factor $4D/\sqrt3$.

| point | $\ell_0$ | $\ell_1$ | $\ell_2$ |
|---|---:|---:|---:|
| $M_0$ | $2vS-y$ | $2uS-x$ | $S-2xy$ |
| $M_1$ | $2vS-x-2y$ | $2uS-x+y$ | $2x+y-2xy$ |
| $M_5$ | $2vS+x-y$ | $2uS-2x-y$ | $x+2y-2xy$ |

The two $O$-containment inequalities imply $M_0\in T_C$, because

$$
2vS-y\ge y>0,
\qquad
2uS-x\ge x>0,
$$

and

$$
S-2xy=x(1-y)+y(1-x)>0.
$$

For $M_1$, the second and third slacks are automatically positive, so $M_1\notin T_C$ is equivalent to

$$
2vS-x-2y<0.
$$

Thus

$$
\boxed{
vS<y+\frac x2.
}
$$

For $M_5$, the first and third slacks are automatically positive, so $M_5\notin T_C$ is equivalent to

$$
2uS-2x-y<0.
$$

Thus

$$
\boxed{
uS<x+\frac y2.
}
$$

These two strict exclusions force all other midpoint exclusions.

For $M_2$,

$$
\frac{4D}{\sqrt3}\ell_0(M_2)
=
2vS-x-3y
=
(2vS-x-2y)-y<0.
$$

For $M_4$,

$$
\frac{4D}{\sqrt3}\ell_1(M_4)
=
2uS-3x-y
=
(2uS-2x-y)-x<0.
$$

For $M_3$,

$$
\frac{4D}{\sqrt3}\ell_0(M_3)=2vS-3y,
\qquad
\frac{4D}{\sqrt3}\ell_1(M_3)=2uS-3x.
$$

If $y\ge x$, then

$$
2vS-3y<2y+x-3y=x-y\le0,
$$

with strict negativity because $vS<y+x/2$. If $x\ge y$, then

$$
2uS-3x<2x+y-3x=y-x\le0,
$$

with strict negativity because $uS<x+y/2$. Hence $M_3\notin T_C$.

Therefore the exact midpoint target is equivalent to

$$
uS\ge x,\qquad vS\ge y,
$$

and

$$
uS<x+\frac y2,\qquad vS<y+\frac x2.
$$

## Boundary-edge verification

On $e_{0,1}(b)$, the side slacks scaled by $2D/\sqrt3$ are

$$
\ell_0=(v-b)S,
$$

$$
\ell_1=by+uS,
$$

and

$$
\ell_2=x(b-y).
$$

Thus

$$
e_{0,1}(b)\in T_C
\quad\Longleftrightarrow\quad
y\le b\le v,
$$

and therefore

$$
T_C\cap e_{0,1}=[y,v].
$$

On $e_{5,0}(a)$, the side slacks scaled by $2D/\sqrt3$ are

$$
\ell_0=ax+vS,
$$

$$
\ell_1=(u-a)S,
$$

and

$$
\ell_2=y(a-x).
$$

Thus

$$
e_{5,0}(a)\in T_C
\quad\Longleftrightarrow\quad
x\le a\le u,
$$

and therefore

$$
T_C\cap e_{5,0}=[x,u].
$$

It remains to show that no other boundary edge has positive-length overlap.

On $e_{1,2}$, write the edge parameter as $c\in[0,1]$. The scaled $\ell_0$ slack is

$$
vS-S-cy.
$$

Since $vS<y+x/2<S$, this is negative for every $c\in[0,1]$. Hence $T_C\cap e_{1,2}=\varnothing$.

On $e_{4,5}$, the scaled $\ell_1$ slack is

$$
cx+uS-2x-y.
$$

Its maximum over $0\le c\le1$ is $uS-x-y$, and

$$
uS<x+\frac y2<x+y.
$$

Hence $T_C\cap e_{4,5}=\varnothing$.

On $e_{2,3}$, if a point were in $T_C$, then both relevant scaled slacks

$$
N_0=cx+vS-x-2y
$$

and

$$
N_1=-cS+uS-x+y
$$

would be nonnegative. But using the coupling relation,

$$
N_0+N_1=-cy+D+xy-2x-y.
$$

For $0<x,y<1$,

$$
D+xy<2x+y,
$$

because

$$
(2x+y-xy)^2-D^2
=
x\left(x(1-y)(3-y)+y(3-2y)\right)>0.
$$

Thus $N_0+N_1<0$, contradiction. Hence $T_C\cap e_{2,3}=\varnothing$.

On $e_{3,4}$, if a point were in $T_C$, then the corresponding two scaled slacks would have sum

$$
cx+D+xy-2x-2y.
$$

This is at most

$$
D+xy-x-2y.
$$

For $0<x,y<1$,

$$
D+xy<x+2y,
$$

because

$$
(x+2y-xy)^2-D^2
=
y\left(x(3-2x)+y(1-x)(3-x)\right)>0.
$$

Thus no point of $e_{3,4}$ lies in $T_C$.

Therefore the only positive-length boundary overlaps are exactly on $e_{5,0}$ and $e_{0,1}$.

## Maximality

Define

$$
F(x,y)=\frac{\sqrt{x^2+xy+y^2}+xy}{x+y}
=
\frac{D+xy}{S}.
$$

Every feasible pair satisfies

$$
u+v=F(x,y).
$$

The $O$-containment inequalities give

$$
uS+vS\ge x+y=S.
$$

Using the coupling relation, this becomes

$$
D+xy\ge S.
$$

Since $S-xy>0$, after squaring this is equivalent to

$$
\boxed{
2x+2y-xy\ge1.
}
$$

Let

$$
G=\{(x,y):0<x<1,\ 0<y<1,\ 2x+2y-xy\ge1\}.
$$

The set $G$ is upward closed in both coordinates, because

$$
\frac{\partial}{\partial x}(2x+2y-xy)=2-y>0
$$

and

$$
\frac{\partial}{\partial y}(2x+2y-xy)=2-x>0.
$$

On $G$,

$$
\frac{\partial F}{\partial x}
=
\frac{y(x-y+2yD)}{2D(x+y)^2},
$$

and

$$
\frac{\partial F}{\partial y}
=
\frac{x(y-x+2xD)}{2D(x+y)^2}.
$$

Both derivatives are strictly positive. For $\partial F/\partial x$, if $x\ge y$, then $x-y+2yD>0$. If $x<y$ and $y\ge1/2$, then $D\ge y$, so

$$
x-y+2yD\ge x-y+2y^2=x+y(2y-1)>0.
$$

If $x<y<1/2$, the inequality $2x+2y-xy\ge1$ gives

$$
x\ge\frac{1-2y}{2-y}.
$$

Since

$$
\frac{1-2y}{2-y}>y(1-2y),
$$

we again get

$$
x-y+2yD\ge x-y+2y^2>0.
$$

Thus $\partial F/\partial x>0$. The proof that $\partial F/\partial y>0$ is symmetric.

Now suppose a feasible pair $([x,u],[y,v])$ is product-dominated by another feasible pair $([x',u'],[y',v'])$. Then

$$
x'\le x,\qquad y'\le y,\qquad u'\ge u,\qquad v'\ge v.
$$

Since both start pairs lie in $G$ and $G$ is upward closed, the strict monotonicity of $F$ gives

$$
F(x',y')\le F(x,y),
$$

with equality only if $x'=x$ and $y'=y$. But domination gives

$$
u'+v'\ge u+v.
$$

Using $u'+v'=F(x',y')$ and $u+v=F(x,y)$, equality must hold. Therefore

$$
x'=x,\qquad y'=y,
$$

and then

$$
u'+v'=u+v.
$$

Since $u'\ge u$ and $v'\ge v$, this forces

$$
u'=u,\qquad v'=v.
$$

Thus no feasible pair is properly product-dominated. Every feasible CE2 interval pair in the theorem is maximal.

## Boundary cases and degeneracies

The exact CE2 target is not a closed subset of endpoint space because positive-length overlap and midpoint exclusion are strict conditions.

The equalities

$$
uS=x
$$

and

$$
vS=y
$$

are allowed. They mean $O$ lies on side $1$ or side $0$ of the triangle.

The equality

$$
uS=x+\frac y2
$$

is not allowed, because then $M_5\in\partial T_C$. Since triangles are closed, this violates the exact midpoint subset $\{M_0\}$.

The equality

$$
vS=y+\frac x2
$$

is not allowed, because then $M_1\in\partial T_C$.

The equalities

$$
u=x
\qquad\text{or}\qquad
v=y
$$

are not allowed, because one of the target edge overlaps has zero length.

The equalities

$$
u=1
\qquad\text{or}\qquad
v=1
$$

are not allowed. If $v=1$, then $V_1\in T_C$, and convexity with $O\in T_C$ gives $M_1\in T_C$. If $u=1$, then $V_5\in T_C$, and convexity with $O\in T_C$ gives $M_5\in T_C$.

The cases

$$
x=0
\qquad\text{or}\qquad
y=0
$$

are limiting boundary cases. They place the visible side through $V_0$ or collapse one initial cut to $V_0$, and they are not exact positive-length CE2 configurations of this type.

The closed relaxation is obtained from the theorem by replacing the strict inequalities

$$
0<x<u<1,\qquad 0<y<v<1,
$$

and

$$
uS<x+\frac y2,\qquad vS<y+\frac x2
$$

by non-strict inequalities. The resulting boundary faces are precisely the degeneracies listed above, except that the lower equalities $uS=x$ and $vS=y$ remain valid exact configurations when the other strict inequalities hold.

## Numerical verification

The numerical check used half-plane and determinant containment predicates rather than the symbolic endpoint inequalities above.

For each sampled unit equilateral triangle, the test:

1. checked $O\in T_C$ and $M_0\in T_C$;
2. rejected the triangle if any of $M_1,\dots,M_5$ was contained;
3. intersected the triangle with each hexagon edge by substituting the edge parameter into the three affine half-plane inequalities;
4. retained only those triangles with positive-length overlap on $e_{5,0}$ and $e_{0,1}$ and zero positive-length overlap on every other boundary edge;
5. recorded $x=s_{50}$, $u=t_{50}$, $y=s_{01}$, and $v=t_{01}$;
6. checked the coupling equation, all target inequalities, and product maximality.

The sampling was intentionally concentrated near the product-front-critical regions. A CE2 candidate has one side with outward normal in the $V_0$ cone, so the targeted sampler used that side angle

$$
-\frac\pi6<\delta<\frac\pi6
$$

with extra density near $\delta=\pm\pi/6$, near $O$-on-side faces, near the $M_1$ and $M_5$ exclusion walls, near $x=0$ and $y=0$, and near interval-collapse faces $u=x$ and $v=y$.

The run used seed `20260506`.

| source | tested | retained feasible | retention rate |
|---|---:|---:|---:|
| uniform $C$-triangle half-plane samples | 250,000 | 1,573 | 0.006292 |
| targeted triangle-native samples | 1,200,000 | 318,463 | 0.265386 |
| combined | 1,450,000 | 320,036 | 0.220714 |

Across all retained feasible samples, the coupling residual

$$
(u+v)(x+y)-xy-\sqrt{x^2+xy+y^2}
$$

satisfied

$$
\max |\text{residual}|=1.554\cdot10^{-15},
$$

and

$$
\operatorname{mean}|\text{residual}|=2.727\cdot10^{-16}.
$$

No retained raw triangle violated any of the symbolic inequalities at tolerance $5\cdot10^{-12}$ for the coupling equation and $10^{-10}$ for one-sided inequalities.

Boundary stress coverage was:

| quantity | samples below $10^{-6}$ |
|---|---:|
| minimum $O$-containment lower slack | 75,531 |
| minimum $M_1/M_5$ exclusion slack | 852 |
| start-domain slack $2x+2y-xy-1$ | 5,183 |
| length $u-x$ | 304 |
| length $v-y$ | 290 |
| $\min(x,y)$ | 373 |
| $\min(1-u,1-v)$ | 220 |

Product maximality was tested in two finite pairwise dominance searches.

| test set | size | dominated samples found |
|---|---:|---:|
| boundary and extreme stress subset | 7,741 | 0 |
| larger mixed subset | 32,142 | 0 |

In addition, $13$ nonlinear max-min domination searches were run against boundary, extreme, symmetric, and random targets. The largest returned domination slack was

$$
-1.695\cdot10^{-11}.
$$

A positive value would indicate a strict feasible product dominator. None was found.

The monotonicity mechanism in the proof was also checked on all retained raw feasible samples. The derivative minima were

$$
\min\frac{\partial F}{\partial x}=1.468\cdot10^{-7},
$$

and

$$
\min\frac{\partial F}{\partial y}=1.268\cdot10^{-7}.
$$

A compact version of the independent check is:

```python
def accept_triangle(normals, alpha):
    if not contains_halfplane_triangle(normals, alpha, O):
        return None
    if not contains_halfplane_triangle(normals, alpha, M[0]):
        return None
    if any(contains_halfplane_triangle(normals, alpha, M[i]) for i in range(1, 6)):
        return None

    intervals = [triangle_edge_interval(normals, alpha, edge) for edge in range(6)]
    positive = []
    for edge, interval in enumerate(intervals):
        if interval is not None:
            s, t = interval
            if t - s > 1e-8:
                positive.append(edge)

    if set(positive) != {0, 5}:
        return None

    y, v = intervals[0]
    x, u = intervals[5]
    return x, u, y, v

max_residual = 0.0
dominance_candidates = []

for normals, alpha in targeted_and_uniform_samples(seed=20260506):
    q = accept_triangle(normals, alpha)
    if q is None:
        continue

    x, u, y, v = q
    residual = (u + v) * (x + y) - x * y - (x * x + x * y + y * y)**0.5
    max_residual = max(max_residual, abs(residual))

    assert 0 < x < u < 1
    assert 0 < y < v < 1
    assert u * (x + y) >= x - 1e-10
    assert v * (x + y) >= y - 1e-10
    assert u * (x + y) < x + 0.5 * y + 1e-10
    assert v * (x + y) < y + 0.5 * x + 1e-10

assert max_residual <= 5e-12
assert no_sample_product_dominates_another(retained_samples, tolerance=1e-10)
```

This numerical test supports the symbolic characterization and the product-maximality statement. As required by the numerical evidence policy, the computation is used only as a check; the maximality claim itself is certified by the proof above.
