# Strict Boundary Handoff Selection

Status: Proven

This note distinguishes the actual maximal boundary reaches of the six
vertex-role triangles from smaller boundary demands selected at strict
handoffs.  It proves that the selected rows preserve an actual exact-one
supercritical pattern and that an actual at-least-two pattern admits a
selection with at least two supercritical selected rows.

All indices below are taken modulo $6$.

## 1. Actual reaches and strict overlap intervals

Let

$$
e_i=[V_i,V_{i+1}],
$$

and suppose that six open unit equilateral vertex-role triangles
$T_0,\dots,T_5$ cover $\partial H$.  For $T_i$, let

$$
A_i
=
\sup\left\{
t\in[0,1]:V_i+t(V_{i-1}-V_i)\in T_i
\right\}
$$

be its actual maximal reach from $V_i$ along the incoming edge
$e_{i-1}$, and let

$$
B_i
=
\sup\left\{
t\in[0,1]:V_i+t(V_{i+1}-V_i)\in T_i
\right\}
$$

be its actual maximal reach from $V_i$ along the outgoing edge $e_i$.
Thus $A_i,B_i$ are actual reaches in the sense of
[`1202_local_coordinates_abc.md`](1202_local_coordinates_abc.md), not
prescribed lower-bound demands.

Use the coordinate $x\in[0,1]$ on $e_i$ measured from $V_i$:

$$
X_i(x)=V_i+x(V_{i+1}-V_i).
$$

Because $V_i$ is an interior point of $T_i$, openness gives positive reach in
both edge directions.  The closure of $T_i$ is a compact equilateral triangle
of diameter $1$.  Its distance from the interior point $V_i$ to every point
of the closure is strictly less than $1$, since a diametral pair consists of
two vertices of the closed triangle.  Therefore

$$
0<A_i<1,
\qquad
0<B_i<1.
$$

In this coordinate, $T_i$ contains the initial interval $0\le x<B_i$,
while $T_{i+1}$ contains the terminal interval
$1-A_{i+1}<x\le1$.  Here convexity makes each intersection with the edge an
interval, and openness excludes its nonvertex endpoint.

No vertex role other than $T_i$ or $T_{i+1}$ can cover a relative-interior
point of $e_i$.  Indeed, every two points of an open unit equilateral
triangle are at distance strictly less than $1$, whereas a relative-interior
point of $e_i$ is at distance greater than $1$ from every nonendpoint
hexagon vertex.  Since the six roles cover $e_i$, the two open edge intervals
must overlap.  Therefore

$$
\boxed{1-A_{i+1}<B_i.}
$$

Set

$$
\ell_i=1-A_{i+1},
\qquad
u_i=B_i,
\qquad
I_i=(\ell_i,u_i).
$$

Every $I_i$ is a nonempty open interval contained in $(0,1)$.

## 2. Selected handoffs and selected demands

Choose

$$
x_i\in I_i
$$

and put

$$
X_i=X_i(x_i),
\qquad
a_i=1-x_{i-1},
\qquad
b_i=x_i.
$$

Then $X_i\in T_i\cap T_{i+1}$, and the selected demands satisfy

$$
0<a_i<A_i,
\qquad
0<b_i<B_i.
$$

In particular, the actual triangle $T_i$ contains the three selected points

$$
V_i,
\qquad
X_{i-1},
\qquad
X_i.
$$

The two selected edge anchors are therefore at mutual distance strictly less
than $1$.  In the local $120$-degree coordinates this gives

$$
\boxed{a_i^2+a_ib_i+b_i^2<1.}
$$

The actual and selected supercritical conditions are, respectively,

$$
A_i+B_i>1
\quad\Longleftrightarrow\quad
u_i>\ell_{i-1},
$$

and

$$
a_i+b_i>1
\quad\Longleftrightarrow\quad
x_i>x_{i-1}.
$$

If actual row $i$ is nonsupercritical, then

$$
u_i=B_i\le1-A_i=\ell_{i-1}.
$$

Every strict handoff selection consequently satisfies

$$
x_i<u_i\le\ell_{i-1}<x_{i-1},
$$

so

$$
\boxed{A_i+B_i\le1\quad\Longrightarrow\quad a_i+b_i<1.}
$$

Notice that the conclusion is strict even when the actual row is critical.

## 3. Exact-one preservation theorem

Suppose exactly one actual row is supercritical.  Let $p$ be its index:

$$
A_p+B_p>1,
$$

and

$$
A_i+B_i\le1
\qquad(i\ne p).
$$

Then every strict handoff selection has exactly one supercritical selected
row, at the same index $p$.

### Proof

Section 2 gives

$$
a_i+b_i<1
\qquad(i\ne p).
$$

The selected row sums telescope:

$$
\begin{aligned}
\sum_{i=0}^5(a_i+b_i)
&=
\sum_{i=0}^5(1-x_{i-1}+x_i)
\\
&=6.
\end{aligned}
$$

The five sums with $i\ne p$ have total strictly less than $5$.  Hence

$$
a_p+b_p
=
6-\sum_{i\ne p}(a_i+b_i)
>1.
$$

Thus $p$ is the unique selected supercritical index.  This proves the
theorem.

## 4. At-least-two selection theorem

Suppose at least two actual rows are supercritical.  Then there is a strict
handoff selection for which at least two selected rows are supercritical.

### 4.1 Two nonconsecutive actual supercritical rows

First suppose there are nonconsecutive actual supercritical indices $p$ and
$q$.  The variable pairs

$$
\left\{x_{p-1},x_p\right\},
\qquad
\left\{x_{q-1},x_q\right\}
$$

are disjoint.

Because row $p$ is actually supercritical,

$$
\ell_{p-1}<u_p.
$$

Choose $z_p\in(\ell_{p-1},u_p)$.  Both intervals

$$
(\ell_{p-1},\min(u_{p-1},z_p))
$$

and

$$
(\max(\ell_p,z_p),u_p)
$$

are nonempty.  Choose $x_{p-1}$ in the first and $x_p$ in the second.  Then

$$
x_{p-1}<z_p<x_p,
$$

so selected row $p$ is supercritical.  Make the identical construction for
$q$.  The two constructions do not share a variable, and all remaining
$x_i$ may be chosen arbitrarily in $I_i$.  Thus selected rows $p$ and $q$
are both supercritical.

This case always applies if there are at least three actual supercritical
rows: among three indices on a six-cycle, two are nonconsecutive.  It also
applies when there are exactly two and they are nonconsecutive.

### 4.2 Exactly two adjacent actual supercritical rows

It remains to suppose that the actual supercritical set is

$$
\left\{p,p+1\right\}.
$$

For each of the four complementary indices $i$, actual
nonsupercriticality and strict boundary overlap give

$$
\ell_i<u_i\le\ell_{i-1},
$$

and therefore

$$
\ell_i<\ell_{i-1}.
$$

Applying this to $i=p+2,p+3,p+4,p+5$ yields, in particular,

$$
\ell_{p-1}<\ell_{p+1}.
$$

Now

$$
\ell_p<u_p
$$

by strict boundary overlap, and

$$
\ell_{p-1}<u_p
$$

because actual row $p$ is supercritical.  Likewise,

$$
\ell_p<u_{p+1}
$$

because actual row $p+1$ is supercritical, while

$$
\ell_{p-1}<\ell_{p+1}<u_{p+1}.
$$

Consequently,

$$
\boxed{
\max(\ell_{p-1},\ell_p)
<
\min(u_p,u_{p+1}).
}
$$

Choose

$$
x_p
\in
\left(
\max(\ell_{p-1},\ell_p),
\min(u_p,u_{p+1})
\right).
$$

Because $x_p>\ell_{p-1}$ and $I_{p-1}$ is nonempty, one can choose

$$
x_{p-1}\in I_{p-1}
$$

with $x_{p-1}<x_p$.  Because $x_p<u_{p+1}$ and $I_{p+1}$ is nonempty, one
can choose

$$
x_{p+1}\in I_{p+1}
$$

with $x_p<x_{p+1}$.  Choose the other three handoffs arbitrarily in their
strict intervals.  Then

$$
x_{p-1}<x_p<x_{p+1},
$$

so both selected rows $p$ and $p+1$ are supercritical.  This completes the
proof.

## 5. Consequence for lower-bound arguments

The actual triangle $T_i$ realizes every selected demand pair $(a_i,b_i)$.
Its closure is a closed unit equilateral triangle containing the selected
anchors, and passing to the closure does not change its area.  Therefore any
universal local area estimate for the selected anchors applies directly to
the actual role.  In particular:

- the exact-one theorem permits a proof to use a selected strict ascent at
  the same index as the unique actual supercritical row;
- the at-least-two theorem permits a proof to use two selected strict ascents
  when the actual supercritical count is at least two.

The theorem does not assert that an arbitrary strict handoff selection
preserves an actual at-least-two count.  Its at-least-two conclusion is an
existence statement, and Section 4 gives the required simultaneous choice.
