# Strict Boundary Handoff Selection

Status: Proven

This note connects the actual maximal boundary reaches of the six vertex
roles to smaller demands chosen at boundary handoffs.  It proves two facts
used by the $N_+$ branches:

- one actual supercritical row remains the unique selected supercritical row
  for every strict handoff selection;
- two or more actual supercritical rows permit one selection with at least
  two selected supercritical rows.

All indices are modulo $6$.

## 1. Actual reaches and strict handoffs

Let $T_i$ be the open unit equilateral vertex-role triangle containing
$V_i$.  Assume that these six triangles cover $\partial H$, and let

$$
\begin{aligned}
A_i&=\sup\left\{
t\in[0,1]:V_i+t(V_{i-1}-V_i)\in T_i
\right\},\\
B_i&=\sup\left\{
t\in[0,1]:V_i+t(V_{i+1}-V_i)\in T_i
\right\}
\end{aligned}
$$

be its actual maximal reaches from $V_i$ along the incoming and outgoing
hexagon edges.  These are actual reaches, not prescribed demands; compare
[`1202_local_coordinates_abc.md`](1202_local_coordinates_abc.md).

Because $V_i$ is interior to $T_i$, both reaches are positive.  They are
also smaller than $1$: the distance from an interior point of a closed unit
equilateral triangle to every point of that triangle is strictly less than
its diameter $1$.  Hence

$$
0<A_i<1,\qquad 0<B_i<1.
$$

Parametrize $e_i=[V_i,V_{i+1}]$ by

$$
X_i(x)=V_i+x(V_{i+1}-V_i),\qquad 0\le x\le1.
$$

Convexity and openness give the edge traces

$$
T_i\cap e_i=[0,B_i),qquad
T_{i+1}\cap e_i=(1-A_{i+1},1]
$$

in this coordinate.  No other vertex role can contain an interior point of
$e_i$: that point is more than distance $1$ from every nonendpoint hexagon
vertex, whereas two points of an open unit equilateral triangle are less
than distance $1$ apart.  Since the six roles cover $e_i$, the displayed
traces must overlap strictly.  Thus, with

$$
\ell_i=1-A_{i+1},qquad u_i=B_i,qquad I_i=(\ell_i,u_i),
$$

every $I_i$ is a nonempty subinterval of $(0,1)$.

Choose a strict handoff $x_i\in I_i$ on every edge and define the selected
demands at $V_i$ by

$$
a_i=1-x_{i-1},qquad b_i=x_i.
$$

Then $X_{i-1}(x_{i-1})$ and $X_i(x_i)$ lie in $T_i$, and

$$
0<a_i<A_i,qquad 0<b_i<B_i.
$$

Their mutual distance is strictly less than $1$, so the local $120$-degree
coordinates satisfy

$$
a_i^2+a_ib_i+b_i^2<1.                                      \tag{1}
$$

The actual and selected row tests now become

$$
\begin{aligned}
A_i+B_i>1 &\iff \ell_{i-1}<u_i,\\
a_i+b_i>1 &\iff x_{i-1}<x_i.
\end{aligned}                                               \tag{2}
$$

In particular, if actual row $i$ is nonsupercritical, then

$$
x_i<u_i\le\ell_{i-1}<x_{i-1},
$$

and therefore

$$
A_i+B_i\le1\quad\Longrightarrow\quad a_i+b_i<1.             \tag{3}
$$

The strict conclusion in (3) also covers an actual critical row.

## 2. Supercritical-row transfer theorem

For the strict handoffs constructed above:

1. if exactly one actual row is supercritical, every selection has exactly
   one selected supercritical row, at the same index;
2. if at least two actual rows are supercritical, some selection has at
   least two selected supercritical rows.

We prove the two assertions separately.

### Exact-one case

Suppose $p$ is the only actual supercritical index.  Equation (3) gives

$$
a_i+b_i<1\qquad(i\ne p)
$$

for every strict handoff selection.  On the other hand,

$$
\sum_{i=0}^5(a_i+b_i)
=\sum_{i=0}^5(1-x_{i-1}+x_i)=6.                            \tag{4}
$$

The five terms with $i\ne p$ have sum less than $5$, so (4) forces
$a_p+b_p>1$.  Thus every strict selection has exactly one selected
supercritical row, at the same index $p$.

### At-least-two case

Suppose at least two actual rows are supercritical.  We construct a strict
selection with at least two selected ascents $x_{i-1}<x_i$, which are the
desired rows by (2).

First assume that two supercritical indices $p,q$ are nonadjacent.  For a
supercritical index $r$, relation (2) gives

$$
\ell_{r-1}<u_r.
$$

Choose $z_r$ strictly between these endpoints, then choose

$$
\begin{aligned}
x_{r-1}&\in
(\ell_{r-1},\min(u_{r-1},z_r)),\\
x_r&\in
(\max(\ell_r,z_r),u_r).
\end{aligned}                                               \tag{5}
$$

Both intervals in (5) are nonempty because $I_{r-1}$ and $I_r$ are
nonempty and $\ell_{r-1}<z_r<u_r$.  The choice gives
$x_{r-1}<z_r<x_r$.  Apply it for $r=p$ and $r=q$.  The two pairs of
variables are disjoint because $p,q$ are nonadjacent; choose every remaining
$x_i$ arbitrarily in $I_i$.  Rows $p$ and $q$ are then selected
supercritical.  This covers every pattern containing three or more
supercritical indices, since three vertices of a $6$-cycle cannot be
pairwise adjacent, and also covers two nonadjacent indices.

It remains to treat exactly two adjacent supercritical indices, say
$p,p+1$.  For each other index $i$, strict overlap and actual
nonsupercriticality give

$$
\ell_i<u_i\le\ell_{i-1}.
$$

Applying this successively at $i=p+2,p+3,p+4,p+5$ yields

$$
\ell_{p-1}<\ell_{p+1}.                                     \tag{6}
$$

Strict overlap and supercriticality of rows $p,p+1$ give

$$
\ell_p<u_p,\qquad \ell_{p-1}<u_p,\qquad
\ell_p<u_{p+1},\qquad \ell_{p+1}<u_{p+1}.                 \tag{7}
$$

By (6), the last inequality in (7) also gives
$\ell_{p-1}<u_{p+1}$.  Hence every number in the lower pair is smaller than
every number in the upper pair, so

$$
\max(\ell_{p-1},\ell_p)<\min(u_p,u_{p+1}).                 \tag{8}
$$

Choose $x_p$ in the interval in (8).  Since
$x_p>\ell_{p-1}$ and $x_p<u_{p+1}$, choose

$$
x_{p-1}\in I_{p-1},\qquad x_{p+1}\in I_{p+1}
$$

so that $x_{p-1}<x_p<x_{p+1}$; the nonemptiness of the two intervals makes
both choices possible.  Choose the other handoffs arbitrarily.  Then rows
$p$ and $p+1$ are both selected supercritical, completing the proof.

## 3. Consequence for lower-bound arguments

The actual triangle $T_i$ contains the vertex and both selected anchors, so
its closure is a closed unit equilateral triangle realizing the demand pair
$(a_i,b_i)$.  Passing to the closure does not change its area.  Therefore
any universal local area lower bound for those selected anchors applies to
the actual role.

The exact-one conclusion holds for every strict selection.  The
at-least-two conclusion is only an existence statement, and the construction
above supplies the required simultaneous choice.
