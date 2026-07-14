# CE Classification

Status: Proven

Let

$$
N_E(T_C)=\left\lvert \left\lbrace i : T_C\cap e_{i,i+1}\text{ contains a positive-length interval} \right\rbrace \right\rvert.
$$

Then

$$
\mathrm{CE0}\iff N_E(T_C)=0,
$$

$$
\mathrm{CE1}\iff N_E(T_C)=1,
$$

$$
\mathrm{CE2}\iff N_E(T_C)=2.
$$

Historical aliases $\mathrm{Ce0}$, $\mathrm{Ce1}$, and $\mathrm{Ce2}$ refer to the same cases, but new notes use $\mathrm{CE0}$, $\mathrm{CE1}$, and $\mathrm{CE2}$.

Point-only contacts, tangencies, and vertex-only contacts are degenerate and do not count as CE edge overlaps.

## Exhaustiveness

Every unit equilateral $C$-triangle satisfies

$$
\boxed{N_E(T_C)\le2.}
$$

Consequently CE0, CE1, and CE2 are exhaustive: a $C$-triangle belongs to
exactly one of these three classes.

### Proof

Use the standard coordinates

$$
V_k=\left(\cos\frac{k\pi}{3},\sin\frac{k\pi}{3}\right).
$$

Among any three distinct edges of the six-edge cycle $\partial H$, two have no
common endpoint. A positive-length subinterval of an edge contains a point in
the relative interior of that edge. It is therefore enough to prove that
relative-interior points on two nonadjacent hexagon edges are more than unit
distance apart.

Up to a symmetry of $H$ and an interchange of the two edges, there are two
cases. First take $e_{0,1}$ and $e_{2,3}$. Write

$$
x=(1-t)V_0+tV_1,
\qquad
y=(1-s)V_2+sV_3,
\qquad
0<t,s<1.
$$

In Cartesian coordinates,

$$
x=\left(1-\frac t2,\frac{\sqrt3 t}{2}\right),
\qquad
y=\left(-\frac{1+s}{2},\frac{\sqrt3(1-s)}{2}\right),
$$

and hence

$$
\lVert x-y\rVert^2-1
=(1-t)(2-t)+s(s+t)>0.
$$

For the opposite pair $e_{0,1}$ and $e_{3,4}$, write

$$
x=(1-t)V_0+tV_1,
\qquad
y=(1-s)V_3+sV_4,
\qquad
0<t,s<1.
$$

Here

$$
x=\left(1-\frac t2,\frac{\sqrt3 t}{2}\right),
\qquad
y=\left(-1+\frac s2,-\frac{\sqrt3 s}{2}\right).
$$

Thus, with $u=t+s$,

$$
\lVert x-y\rVert^2-1
=u^2-2u+3
=(u-1)^2+2>0.
$$

Now suppose that $N_E(T_C)\ge3$. Choose two nonadjacent positively overlapped
edges and relative-interior points $x,y$ in the corresponding overlaps. The
calculation above gives $\lVert x-y\rVert>1$. But a unit equilateral triangle,
and hence also its open or closed realization, has diameter at most $1$.
Indeed, if its vertices are $A_0,A_1,A_2$ and
$p=\sum_i\lambda_iA_i$, $q=\sum_j\mu_jA_j$ are two points in their convex
hull, then

$$
\lVert p-q\rVert
\le
\sum_{i,j}\lambda_i\mu_j\lVert A_i-A_j\rVert
\le
\sum_{i,j}\lambda_i\mu_j
=1.
$$

This is a contradiction. Thus $N_E(T_C)\le2$, as claimed.

$$
\Box
$$
