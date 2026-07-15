# T3-Like Side Tradeoff and Crossed-Pair Obstruction

Status: Proven

This note isolates the T3-like calculation used in midpoint-matching
arguments.  All triangles in the statement are closed traces.  For an
original open T3-like role, first apply the trace-dominating translation in
[`1201`](../../1XXX_foundations/12XX_V_triangle/1201_V_triangle_types.md).
That translation preserves the selected adjacent-support direction and every
old point of the trace in the hexagon.

## Boundary-ray normal form

Let $T$ be a translated T3-like $V_0$-triangle whose selected adjacent
support is on $r_1$.  In the local coordinates

$$
X=V_0+x(V_5-V_0)+y(V_1-V_0),
$$

there are parameters

$$
D>1,
\qquad
0<R<1,
\qquad
R^2-DR+D^2=1,
$$

and $\alpha,p\ge0$ such that

$$
T\cap e_{5,0}=[0,\alpha],
\qquad
T\cap e_{0,1}=[0,p],
\qquad
\alpha+p=\frac{1}{D}.
$$

Put

$$
q=1-p=\alpha+\frac{D-1}{D}.
$$

On $r_1$, measured from $V_1$ toward $O$, the trace is

$$
T\cap r_1=[c,u],
$$

where

$$
c=\frac{Dq}{R},
\qquad
u=q+\frac{1-R}{D}.
$$

These endpoints satisfy $0<c<u<1$.

Positive-length support gives

$$
\boxed{q<\frac{R}{1+R}<\frac12},
\qquad
\boxed{\alpha<q<\frac12}.
$$

### Proof

Use the Type-II parameter $0<t<1$ from `1201` and put

$$
z=\sqrt{1-t+t^2}.
$$

In the present ordering of the cone basis, the unit direction of the side
through $V_0$ is

$$
w=(r,s)=\left(-\frac{t}{z},\frac{1-t}{z}\right).
$$

Set

$$
R=-r=\frac{t}{z},
\qquad
D=s-r=\frac1z.
$$

Because $0<t<1$, one has $t<z<1$, and hence $0<R<1<D$.  The unit-length
identity for $w$ becomes

$$
R^2-DR+D^2=1.
$$

Let $\beta$ be the Type-II offset in `1201`.  With the present reparameterized
$t$, the selected-support inequality there is

$$
\beta<\frac{tz}{1+z}.
$$

The position of $V_0$ in the side through it is $\tau=\beta/z$.  Hence

$$
0<\tau<\frac{t}{1+z}<R.
$$

The three
side inequalities of the translated triangle can be written as

$$
sx-ry\ge0,
$$

$$
\tau+sy-Dx\ge0,
$$

and

$$
\tau+rx+Dy\le1.
$$

Set $\alpha=\tau/D$.  Substitution on $y=0$ and $x=0$ gives

$$
T\cap e_{5,0}=[0,\alpha],
\qquad
T\cap e_{0,1}=\left[0,\frac{1-\tau}{D}\right].
$$

Thus $p=(1-\tau)/D$ and $\alpha+p=1/D$.  On

$$
r_1=\left\{(x,1):0\le x\le1\right\},
$$

the last two side inequalities give

$$
x\ge\frac{\tau+D-1}{R}=\frac{Dq}{R},
\qquad
x\le\frac{\tau+D-R}{D}=q+\frac{1-R}{D}.
$$

These are $c$ and $u$.  Finally, $c<u$ for positive-length support.
Moreover $c>0$, and $\tau<R$ gives

$$
u=1+\frac{\tau-R}{D}<1.
$$

Multiplication by $DR>0$ and use of $D^2-DR=1-R^2$ give

$$
q(1-R^2)<R(1-R).
$$

Division by $1-R>0$ gives $q<R/(1+R)<1/2$.  Since
$q=\alpha+(D-1)/D$ and $D>1$, also $\alpha<q$.

## One-sided tradeoff

Let $T$ be a translated T3-like $V_0$-triangle for which $V_0$ lies in the
relative interior of a side.  Suppose its selected adjacent support is on
$r_1$, and suppose $M_1\in T$.

Let $b$ be the endpoint of $T\cap e_{0,1}$ measured from $V_0$, let $c$ be
the endpoint of $T\cap r_0$ measured from $V_0$, and let $\ell$ be the first
point of $T\cap r_1$ measured from $V_1$.  Then

$$
\boxed{b+c<1},
\qquad
\boxed{b+\ell>1}.
$$

The reflected statement holds when the selected support is on $r_5$.

### Proof

Use the local coordinates from `1201`,

$$
X=V_0+x(V_1-V_0)+y(V_5-V_0).
$$

Thus

$$
e_{0,1}=\left\{(x,0):0\le x\le1\right\},
$$

$$
r_0=\left\{(w,w):0\le w\le1\right\},
\qquad
r_1=\left\{(1,y):0\le y\le1\right\},
$$

and $M_1=(1,1/2)$.  The exhaustive translated Type-II form proved in
`1201` is

$$
T=\left\{(x,y):
\begin{array}{l}
(1-t)x+ty\ge0,\\
\beta+tx-y\ge0,\\
\beta+x-(1-t)y\le z
\end{array}
\right\},
$$

where

$$
0<t<1,
\qquad
z=\sqrt{1-t+t^2}<1,
\qquad
0<\beta<z.
$$

All denominators below are therefore positive.  The selected
positive-length support on $r_1$ is equivalent, by the same normal-form
proof, to

$$
\beta<\frac{z-(1-t+t^2)}{t}
=\frac{(1-t)z}{1+z}
<(1-t)z.
$$

Substitution on $e_{0,1}$ gives

$$
b=z-\beta.
$$

On $r_0$, the two possible exit parameters are

$$
\frac{\beta}{1-t},
\qquad
\frac{z-\beta}{t}.
$$

The support inequality $\beta<(1-t)z$ shows that the first is smaller, so

$$
c=\frac{\beta}{1-t}.
$$

On $r_1$, the interval begins at

$$
\ell=\frac{\beta+1-z}{1-t}.
$$

The condition $M_1\in T$ gives $\ell\le1/2$, equivalently

$$
\beta\le z-\frac{1+t}{2}.
$$

Consequently

$$
\begin{aligned}
b+c
&=z+\frac{t\beta}{1-t}\\
&\le z+\frac{t}{1-t}
\left(z-\frac{1+t}{2}\right).
\end{aligned}
$$

The gap from $1$ to the last expression is exactly

$$
\frac{(1-z)^2}{2(1-t)}>0.
$$

Thus $b+c<1$.  For the other inequality, direct substitution gives

$$
b+\ell-1
=\frac{t(1-z+\beta)}{1-t}>0.
$$

This proves the tradeoff.  Reflection interchanges the adjacent sides.

## Crossed adjacent pairs

Let $T_i,T_{i+1}$ be translated T3-like traces such that

$$
M_{i+1}\in T_i,
\qquad
M_i\in T_{i+1}.
$$

Suppose their selected supports point toward one another and no other role
has positive-length support on the outer half-arms

$$
[V_i,M_i],
\qquad
[V_{i+1},M_{i+1}].
$$

Then the two half-arms cannot both be covered.

### Proof

Let $b_i,c_i,\ell_i$ be the boundary reach, own-arm exit, and adjacent-arm
entry for $T_i$.  For $T_{i+1}$ write the corresponding quantities, measured
from its own vertex, as $a_{i+1},c_{i+1},\ell_{i+1}$.  The tradeoff and its
reflection give

$$
b_i+c_i<1,
\qquad
b_i+\ell_i>1,
$$

and

$$
a_{i+1}+c_{i+1}<1,
\qquad
a_{i+1}+\ell_{i+1}>1.
$$

Coverage of the two outer half-arms, with no other positive-length
supporter, forces

$$
c_i\ge\ell_{i+1},
\qquad
c_{i+1}\ge\ell_i.
$$

The first inequality gives $a_{i+1}+c_i>1$, and comparison with
$b_i+c_i<1$ yields $a_{i+1}>b_i$.  The second gives
$b_i+c_{i+1}>1$, and comparison with $a_{i+1}+c_{i+1}<1$ yields
$b_i>a_{i+1}$.  This is impossible.
