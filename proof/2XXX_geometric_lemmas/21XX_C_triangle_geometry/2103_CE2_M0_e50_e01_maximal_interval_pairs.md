# CE2, Exact Midpoint $M_0$, Edges $e_{5,0}$ and $e_{0,1}$: Maximal Interval Pairs

Status: Proven

This note proves the normalized CE2 subcase in which

$$
T_C\cap\{M_0,\dots,M_5\}=\{M_0\}
$$

and the only positive-length overlaps with the hexagon boundary are on

$$
e_{5,0} \qquad\text{and}\qquad e_{0,1}.
$$

Write

$$
T_C\cap e_{5,0}=[s_{50},t_{50}], \qquad T_C\cap e_{0,1}=[s_{01},t_{01}].
$$

Maximality is product interval inclusion:

$$
([s_{50},t_{50}],[s_{01},t_{01}]) \preceq ([s'_{50},t'_{50}],[s'_{01},t'_{01}])
$$

if and only if

$$
s'_{50}\le s_{50},\quad t'_{50}\ge t_{50}, \qquad s'_{01}\le s_{01},\quad t'_{01}\ge t_{01}.
$$

## Theorem

Set

$$
x=s_{50},\qquad u=t_{50},\qquad y=s_{01},\qquad v=t_{01},
$$

and

$$
S=x+y,\qquad D=\sqrt{x^2+xy+y^2}.
$$

The maximal feasible interval pairs are exactly all pairs

$$
([s_{50},t_{50}],[s_{01},t_{01}])=([x,u],[y,v])
$$

satisfying

$$
0<x<u<1,\qquad 0<y<v<1,
$$

$$
(u+v)(x+y)-xy=\sqrt{x^2+xy+y^2},
$$

$$
u(x+y)\ge x,\qquad v(x+y)\ge y,
$$

and

$$
u(x+y)<x+\frac y2,\qquad v(x+y)<y+\frac x2.
$$

Equivalently, the square root can be removed by replacing the equation by

$$
\left((u+v)(x+y)-xy\right)^2=x^2+xy+y^2, \qquad (u+v)(x+y)-xy>0.
$$

Every feasible pair in this set is already maximal under product inclusion.

## Coordinates and half-plane model

Use the standard physical coordinates

$$
O=(0,0), \qquad V_i=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right), \qquad M_i=\frac12V_i.
$$

Thus

$$
V_0=(1,0),\quad V_1=\left(\frac12,\frac{\sqrt3}{2}\right),\quad V_5=\left(\frac12,-\frac{\sqrt3}{2}\right),
$$

and

$$
M_0=\left(\frac12,0\right),\quad M_1=\left(\frac14,\frac{\sqrt3}{4}\right),\quad M_5=\left(\frac14,-\frac{\sqrt3}{4}\right).
$$

The target edges are parameterized by

$$
e_{0,1}(b)=V_0+b(V_1-V_0)=\left(1-\frac b2,\frac{\sqrt3}{2}b\right), \qquad 0\le b\le1,
$$

and

$$
e_{5,0}(a)=V_0+a(V_5-V_0)=\left(1-\frac a2,-\frac{\sqrt3}{2}a\right), \qquad 0\le a\le1.
$$

Write a closed unit equilateral triangle as

$$
T=\{X:\ell_i(X)\ge0,\ i=0,1,2\}, \qquad \ell_i(X)=\alpha_i-n_i\cdot X,
$$

where the outward unit normals $n_i$ are separated by $120^\circ$. The unit side-length condition is

$$
\alpha_0+\alpha_1+\alpha_2=\frac{\sqrt3}{2}.
$$

## Endpoint parameterization

First, $V_0\notin T_C$. If $V_0\in T_C$, then $O,V_0\in T_C$ and $|O-V_0|=1$. In a unit equilateral triangle, distance $1$ is attained only by pairs of vertices. Hence $O$ and $V_0$ would be two vertices of $T_C$, and the third vertex would be $V_1$ or $V_5$. Then the triangle would have positive-length boundary overlap with only one of $e_{0,1}$ and $e_{5,0}$, not both.

Since $V_0\notin T_C$, at least one side inequality is violated at $V_0$. If a violated side has outward normal $n=(p,q)$, then positive-length intersection along both adjacent edges forces

$$
n\cdot(V_1-V_0)<0, \qquad n\cdot(V_5-V_0)<0.
$$

Equivalently,

$$
p>\sqrt3|q|.
$$

Among three outward normals separated by $120^\circ$, at most one lies in this open $60^\circ$ cone. Hence exactly one side is violated at $V_0$. Relabel it as side $2$. This side cuts the initial endpoints $x=s_{50}$ and $y=s_{01}$.

The side through $e_{5,0}(x)$ and $e_{0,1}(y)$ has outward unit normal

$$
n_2=\frac1{2D}\left(\sqrt3(x+y), y-x\right).
$$

Set

$$
n_0=R_{2\pi/3}n_2,\qquad n_1=R_{-2\pi/3}n_2.
$$

The endpoint conditions force

$$
\alpha_2=n_2\cdot e_{5,0}(x)=n_2\cdot e_{0,1}(y) = \frac{\sqrt3(x+y-xy)}{2D},
$$

$$
\alpha_0=n_0\cdot e_{0,1}(v) = \frac{\sqrt3(v(x+y)-y)}{2D},
$$

and

$$
\alpha_1=n_1\cdot e_{5,0}(u) = \frac{\sqrt3(u(x+y)-x)}{2D}.
$$

Conversely, these formulas define three side lines with outward unit normals separated by $120^\circ$.

## Coupling equation

The unit side-length condition gives

$$
\alpha_0+\alpha_1+\alpha_2=\frac{\sqrt3}{2}.
$$

Substituting the three constants gives

$$
\frac{\sqrt3}{2D} \left(vS-y+uS-x+S-xy\right) = \frac{\sqrt3}{2}.
$$

Since $S=x+y$, this is equivalent to

$$
(u+v)S-xy=D.
$$

Thus

$$
(u+v)(x+y)-xy=\sqrt{x^2+xy+y^2}.
$$

This is the coupling relation between the two edge intervals.

## Exact midpoint and boundary constraints

The target overlaps have positive length exactly when

$$
0<x<u<1,\qquad 0<y<v<1.
$$

The condition $O\in T_C$ is $\alpha_i\ge0$. Since $\alpha_2>0$, this is equivalent to

$$
uS\ge x,\qquad vS\ge y.
$$

The midpoint slacks below are multiplied by the positive factor $4D/\sqrt3$.

| point | $\ell_0$ | $\ell_1$ | $\ell_2$ |
|---|---:|---:|---:|
| $M_0$ | $2vS-y$ | $2uS-x$ | $S-2xy$ |
| $M_1$ | $2vS-x-2y$ | $2uS-x+y$ | $2x+y-2xy$ |
| $M_2$ | $2vS-x-3y$ | $2uS-2x+y$ | $3x+2y-2xy$ |
| $M_3$ | $2vS-3y$ | $2uS-3x$ | $3x+3y-2xy$ |
| $M_4$ | $2vS+x-2y$ | $2uS-3x-y$ | $2x+3y-2xy$ |
| $M_5$ | $2vS+x-y$ | $2uS-2x-y$ | $x+2y-2xy$ |

The inequalities $uS\ge x$ and $vS\ge y$ imply $M_0\in T_C$, because

$$
2uS-x\ge x>0,\qquad 2vS-y\ge y>0,
$$

and

$$
S-2xy=x(1-y)+y(1-x)>0.
$$

For $M_1$, the second and third slacks are positive, so $M_1\notin T_C$ is equivalent to

$$
2vS-x-2y<0,
$$

or

$$
vS<y+\frac x2.
$$

For $M_5$, the first and third slacks are positive, so $M_5\notin T_C$ is equivalent to

$$
2uS-2x-y<0,
$$

or

$$
uS<x+\frac y2.
$$

These two strict inequalities exclude all remaining midpoints. Indeed,

$$
2vS-x-3y=(2vS-x-2y)-y<0,
$$

so $M_2\notin T_C$, and

$$
2uS-3x-y=(2uS-2x-y)-x<0,
$$

so $M_4\notin T_C$. For $M_3$, if $y\ge x$, then

$$
2vS-3y<2y+x-3y=x-y\le0,
$$

with strict negativity from $vS<y+x/2$. If $x\ge y$, then

$$
2uS-3x<2x+y-3x=y-x\le0,
$$

with strict negativity from $uS<x+y/2$. Thus $M_3\notin T_C$.

Therefore the exact midpoint subset $\{M_0\}$ is equivalent to

$$
uS\ge x,\qquad vS\ge y,
$$

and

$$
uS<x+\frac y2,\qquad vS<y+\frac x2.
$$

## Boundary-edge verification

On $e_{0,1}(b)$, the side slacks multiplied by $2D/\sqrt3$ are

$$
(v-b)S,\qquad by+uS,\qquad x(b-y).
$$

Thus

$$
e_{0,1}(b)\in T_C \quad\Longleftrightarrow\quad y\le b\le v,
$$

and

$$
T_C\cap e_{0,1}=[y,v].
$$

On $e_{5,0}(a)$, the corresponding scaled slacks are

$$
ax+vS,\qquad (u-a)S,\qquad y(a-x).
$$

Thus

$$
e_{5,0}(a)\in T_C \quad\Longleftrightarrow\quad x\le a\le u,
$$

and

$$
T_C\cap e_{5,0}=[x,u].
$$

No other boundary edge has positive-length overlap. On $e_{1,2}$, with edge parameter $c\in[0,1]$, the scaled $\ell_0$ slack is

$$
vS-S-cy.
$$

Since $vS<y+x/2<S$, this is always negative. On $e_{4,5}$, the scaled $\ell_1$ slack is

$$
cx+uS-2x-y.
$$

Its maximum is $uS-x-y<0$, because $uS<x+y/2$.

On $e_{2,3}$, if a point were in $T_C$, two relevant scaled slacks would be

$$
N_0=cx+vS-x-2y, \qquad N_1=-cS+uS-x+y.
$$

Their sum is

$$
N_0+N_1=-cy+D+xy-2x-y,
$$

using $uS+vS=D+xy$. But

$$
D+xy<2x+y,
$$

because

$$
(2x+y-xy)^2-D^2 = x\left(x(1-y)(3-y)+y(3-2y)\right)>0.
$$

Hence $N_0+N_1<0$, contradiction.

On $e_{3,4}$, the corresponding sum of two necessary scaled slacks is

$$
cx+D+xy-2x-2y.
$$

This is at most $D+xy-x-2y$, and

$$
D+xy<x+2y,
$$

because

$$
(x+2y-xy)^2-D^2 = y\left(x(3-2x)+y(1-x)(3-x)\right)>0.
$$

Hence $e_{3,4}$ also has no intersection with $T_C$. Therefore the only positive-length boundary overlaps are exactly $e_{5,0}$ and $e_{0,1}$.

## Maximality

Define

$$
F(x,y)=\frac{\sqrt{x^2+xy+y^2}+xy}{x+y}=\frac{D+xy}{S}.
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

Since $S-xy>0$, squaring gives the equivalent start-domain condition

$$
2x+2y-xy\ge1.
$$

Let

$$
G=\{(x,y):0<x<1,\ 0<y<1,\ 2x+2y-xy\ge1\}.
$$

The set $G$ is upward closed in each coordinate, because the derivatives of $2x+2y-xy$ are $2-y>0$ and $2-x>0$. On $G$,

$$
\frac{\partial F}{\partial x} = \frac{y(x-y+2yD)}{2D(x+y)^2},
$$

and

$$
\frac{\partial F}{\partial y} = \frac{x(y-x+2xD)}{2D(x+y)^2}.
$$

Both derivatives are strictly positive. For $\partial F/\partial x$, if $x\ge y$, then $x-y+2yD>0$. If $x<y$ and $y\ge1/2$, then $D\ge y$, so

$$
x-y+2yD\ge x-y+2y^2=x+y(2y-1)>0.
$$

If $x<y<1/2$, then $2x+2y-xy\ge1$ gives

$$
x\ge\frac{1-2y}{2-y}.
$$

Since

$$
\frac{1-2y}{2-y}>y(1-2y),
$$

and $D\ge y$, we get

$$
x-y+2yD\ge x-y+2y^2>0.
$$

Thus $\partial F/\partial x>0$. The argument for $\partial F/\partial y>0$ is symmetric.

Now suppose a feasible pair $([x,u],[y,v])$ is product-dominated by another feasible pair $([x',u'],[y',v'])$. Then

$$
x'\le x,\qquad y'\le y,\qquad u'\ge u,\qquad v'\ge v.
$$

Since both start pairs lie in $G$ and $G$ is upward closed, monotonicity gives

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

So no feasible CE2 pair is properly product-dominated. Every feasible pair in the theorem is maximal.

## Boundary cases and degeneracies

The equalities

$$
uS=x \qquad\text{or}\qquad vS=y
$$

are allowed; they place $O$ on side $1$ or side $0$.

The equality

$$
uS=x+\frac y2
$$

is not allowed, because then $M_5\in\partial T_C$. The equality

$$
vS=y+\frac x2
$$

is not allowed, because then $M_1\in\partial T_C$. Since triangles are closed, either equality violates the exact midpoint subset $\{M_0\}$.

The equalities

$$
u=x \qquad\text{or}\qquad v=y
$$

are not allowed, because one target edge overlap has zero length.

The equalities

$$
u=1 \qquad\text{or}\qquad v=1
$$

are not allowed. If $v=1$, then $V_1\in T_C$, and convexity with $O\in T_C$ gives $M_1\in T_C$. If $u=1$, then $V_5\in T_C$, and convexity with $O\in T_C$ gives $M_5\in T_C$.

The cases $x=0$ or $y=0$ are limiting boundary cases in which the visible side passes through $V_0$ or one initial cut collapses to $V_0$; they are not exact positive-length CE2 configurations of this type.

The closed relaxation is obtained by replacing the strict positive-length and midpoint-exclusion inequalities by non-strict inequalities. The boundary faces then correspond exactly to the degeneracies listed above, except that $uS=x$ and $vS=y$ remain valid when the other strict inequalities hold.

## Numerical verification

The numerical check used triangle half-plane predicates and one-dimensional segment clipping rather than the symbolic endpoint inequalities.

For each sampled unit equilateral triangle, the test:

1. checked $O\in T_C$ and $M_0\in T_C$;
2. rejected the triangle if any of $M_1,\dots,M_5$ was contained;
3. clipped the triangle against all six hexagon edges;
4. retained only triangles with positive-length overlap on exactly $e_{5,0}$ and $e_{0,1}$;
5. recorded $x=s_{50}$, $u=t_{50}$, $y=s_{01}$, and $v=t_{01}$;
6. checked the coupling equation, all target inequalities, and product maximality.

The sampler was concentrated near the product-front-critical regions. A CE2 candidate has one side with outward normal in the $V_0$ cone, so the targeted sampler used

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
\max|\text{residual}|=1.554\cdot10^{-15},
$$

and

$$
\mathrm{mean}|\text{residual}|=2.727\cdot10^{-16}.
$$

No retained raw triangle violated any symbolic inequality at tolerance $5\cdot10^{-12}$ for the coupling equation and $10^{-10}$ for one-sided inequalities.

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

The derivative minima in the monotonicity check were

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

This numerical test supports the symbolic characterization and the product-maximality statement. The computation is used only as a check; the maximality claim itself is certified by the proof above.
