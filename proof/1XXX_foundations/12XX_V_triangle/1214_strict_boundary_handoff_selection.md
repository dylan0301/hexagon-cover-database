# Strict Boundary Handoff Selection

Status: Proven

All indices are modulo $6$. This note transfers the actual maximal boundary
reaches of the six original vertex roles to strict selected handoff demands.
It preserves the exact-one supercritical pattern and, when at least two actual
rows are supercritical, permits one simultaneous selection with at least two
selected supercritical rows.

## 1. Actual reaches and handoff intervals

Let $T_i$ be the original open unit equilateral triangle containing $V_i$ and
assume that $T_0,\ldots,T_5$ cover $\partial H$. Define

$$
\begin{aligned}
A_i&=\sup\{t\in[0,1]:V_i+t(V_{i-1}-V_i)\in T_i\},\\
B_i&=\sup\{t\in[0,1]:V_i+t(V_{i+1}-V_i)\in T_i\}.
\end{aligned}
$$

Because $V_i$ is interior to a diameter-one triangle,

$$
0<A_i<1,
\qquad
0<B_i<1.
$$

On $e_i=[V_i,V_{i+1}]$, parametrized from $V_i$, the incident open traces are

$$
[0,B_i)
\qquad\text{and}\qquad
(1-A_{i+1},1].
$$

No nonincident vertex role contains a relative-interior point of $e_i$, by the
distance-one obstruction. Hence the two incident traces cover the edge and
must overlap strictly. Put

$$
\ell_i=1-A_{i+1},
\qquad
U_i=B_i,
\qquad
I_i=(\ell_i,U_i).
$$

Every $I_i$ is therefore a nonempty subinterval of $(0,1)$. Choose
$x_i\in I_i$ and set

$$
a_i=1-x_{i-1},
\qquad
b_i=x_i.
$$

Then

$$
0<a_i<A_i,
\qquad
0<b_i<B_i,
$$

and the two selected anchors lie in the same open unit triangle, so

$$
a_i^2+a_ib_i+b_i^2<1. \tag{1}
$$

The actual and selected supercritical tests are

$$
A_i+B_i>1
\iff
\ell_{i-1}<U_i,
\qquad
a_i+b_i>1
\iff
x_{i-1}<x_i. \tag{2}
$$

If actual row $i$ is nonsupercritical, then

$$
x_i<U_i\le\ell_{i-1}<x_{i-1},
$$

so every strict selection satisfies

$$
A_i+B_i\le1
\Longrightarrow
a_i+b_i<1. \tag{3}
$$

This includes the actual critical case $A_i+B_i=1$.

## 2. Exactly one actual supercritical row

Suppose $p$ is the unique actual supercritical index. By (3), every selected
row $i\ne p$ is strictly subcritical. Also

$$
\sum_{i=0}^5(a_i+b_i)
=
\sum_{i=0}^5(1-x_{i-1}+x_i)
=6. \tag{4}
$$

The five terms with $i\ne p$ have sum below $5$, so (4) forces
$a_p+b_p>1$. Thus every strict handoff selection has exactly one selected
supercritical row, at the same index $p$.

## 3. At least two actual supercritical rows

We construct one strict selection with at least two selected ascents.

First suppose two supercritical indices $p,q$ are nonadjacent. For a
supercritical index $r$, (2) gives

$$
\ell_{r-1}<U_r.
$$

Choose $z_r$ in this interval, then choose

$$
\begin{aligned}
x_{r-1}&\in
(\ell_{r-1},\min\{U_{r-1},z_r\}),\\
x_r&\in
(\max\{\ell_r,z_r\},U_r).
\end{aligned} \tag{5}
$$

Both intervals are nonempty because $I_{r-1},I_r$ are nonempty and
$\ell_{r-1}<z_r<U_r$. Thus $x_{r-1}<x_r$. For nonadjacent $p,q$, the two
pairs of variables in (5) are disjoint, so both choices can be made
simultaneously. Any set of at least three indices on a six-cycle contains two
nonadjacent indices, so this also covers every pattern with at least three
supercritical rows.

It remains to treat exactly two adjacent supercritical rows $p,p+1$. For the
other four nonsupercritical rows,

$$
\ell_i<U_i\le\ell_{i-1}.
$$

Applying these inequalities successively gives

$$
\ell_{p-1}<\ell_{p+1}. \tag{6}
$$

Supercriticality at $p,p+1$, strict overlap, and (6) imply

$$
\max\{\ell_{p-1},\ell_p\}
<
\min\{U_p,U_{p+1}\}. \tag{7}
$$

Choose $x_p$ in (7). Since $x_p>\ell_{p-1}$ and $x_p<U_{p+1}$, choose

$$
x_{p-1}\in I_{p-1},
\qquad
x_{p+1}\in I_{p+1}
$$

so that

$$
x_{p-1}<x_p<x_{p+1}.
$$

Then rows $p$ and $p+1$ are both selected supercritical by (2). The remaining
handoffs may be chosen arbitrarily in their nonempty intervals.

## 4. Consequence

The closure of each actual role realizes the selected pair $(a_i,b_i)$ and has
the same area as the open role. Hence every universal local inequality for the
selected anchors applies to the actual role. The exact-one conclusion holds for
every strict selection; the at-least-two conclusion is an existence statement
supplied by the construction above.
