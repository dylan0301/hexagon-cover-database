# Interval Components, Generalized Handoffs, and Boundary-Path Budgets

Status: Proven

This note isolates two elementary mechanisms that recur in the CE1/CE2
packages.  The first replaces branch-specific interval case distinctions by a
single residual-demand operator.  The second replaces repeated terminal sums
along consecutive boundary edges by one path-budget lemma.

## 1. Residual demand after a center interval

Parametrize a unit boundary edge by $[0,1]$ from its left endpoint.  Let
$J\subseteq[0,1]$ be either empty or a closed interval, and let $0\le p\le1$.
Define

$$
e_J(p)
=
sup\left\{
x\in[0,1]:[0,x]\subseteq[0,p]\cup J
\right\},
$$

and define the residual demand

$$
\boxed{\mathcal R_J(p)=1-e_J(p).}
$$

If $J=[L,U]$, then

$$
\boxed{
\mathcal R_{[L,U]}(p)
=
\begin{cases}
1-p,&p<L,\\[2mm]
1-\max\{p,U\},&p\ge L.
\end{cases}}
$$

For the empty interval,

$$
\boxed{\mathcal R_{\varnothing}(p)=1-p.}
$$

Indeed, when $p<L$, the connected component of $[0,p]\cup J$ containing
$0$ is $[0,p]$.  When $p\ge L$, the two intervals meet and that component is
$[0,\max\{p,U\}]$.

The operator has the monotonicities

$$
p_1\le p_2
\quad\Longrightarrow\quad
\mathcal R_J(p_1)\ge\mathcal R_J(p_2),
$$

and

$$
J_1\subseteq J_2
\quad\Longrightarrow\quad
\mathcal R_{J_1}(p)\ge\mathcal R_{J_2}(p).
$$

Thus enlarging any already-covered part can only decrease the remaining
far-side demand.

## 2. Edge-handoff lemma

Suppose a boundary edge is covered by three traces:

- a left trace contained in $[0,p]$;
- a center trace $J$;
- a right trace contained in $[1-q,1]$.

Then

$$
\boxed{q\ge\mathcal R_J(p).}
$$

### Proof

The component of $[0,p]\cup J$ containing $0$ is

$$
[0,e_J(p)].
$$

If $1-q>e_J(p)$, then every point in the nonempty interval

$$
(e_J(p),1-q)
$$

is missed by all three traces.  Hence coverage forces

$$
1-q\le e_J(p),
$$

which is equivalent to the displayed conclusion.  The equality case is
retained at the level of closed role triangles; strictness for the original
open traces is supplied separately by the strict-handoff theorem.

## 3. Generalized actual-row transfer

Let $F_c(a)$ be the exact capped outgoing map from
[`2011`](2011_capped_demand_map.md).  Suppose an actual nonsupercritical role
has incoming reach at least $a$, radial reach at least $c$, and actual outgoing
reach $B$.  Then

$$
B\le F_c(a).
$$

If the next boundary edge also contains a center interval $J$, the edge-handoff
lemma and the monotonicity of $\mathcal R_J$ give

$$
A_{\mathrm{next}}
\ge
\mathcal R_J(B)
\ge
\mathcal R_J(F_c(a)).
$$

Define

$$
\boxed{
\mathcal G_{c,J}(a)
=
\mathcal R_J(F_c(a)).
}
$$

Then

$$
\boxed{A_{\mathrm{next}}\ge\mathcal G_{c,J}(a).}
$$

For $J=\varnothing$,

$$
\mathcal G_{c,\varnothing}(a)
=
1-F_c(a)
=
G_c(a).
$$

Hence the usual capped demand map $G_c$ is the empty-center-interval member of
one generalized family.  This formulation includes singleton center contacts
and requires no separate overlap-order case split.

## 4. Radial component form

Parametrize a radial arm from its outer vertex by $[0,1]$, with $1=O$.  Let
$K$ be the union of all closed center-side and adjacent-role radial intervals.
Define

$$
\rho(K)
=
\inf\left\{
x\in[0,1]:[x,1]\text{ is contained in the component of }K
\text{ containing }1
\right\}.
$$

If the own vertex role is the only remaining role capable of covering a
positive interval from the vertex side, then coverage forces its own-radial
reach to be at least $\rho(K)$.  This is the radial analogue of the preceding
edge-handoff lemma and subsumes the usual hit-or-miss definition of the
required radial input.

## 5. Boundary-path budget

Let $T_1,\ldots,T_k$ be roles assigned to a chain of $k+1$ consecutive unit
boundary edges.  Suppose an external role contributes at most $u$ on the first
edge and an external role contributes at most $v$ on the last edge.  Then
coverage forces

$$
\boxed{
\sum_{j=1}^k(A_j+B_j)
\ge
k+1-u-v.
}
$$

### Proof

The first edge gives

$$
A_1\ge1-u.
$$

Each middle edge gives

$$
B_j+A_{j+1}\ge1
\qquad(1\le j<k),
$$

and the last edge gives

$$
B_k\ge1-v.
$$

Adding,

$$
\begin{aligned}
\sum_{j=1}^k(A_j+B_j)
&=
A_1+
\sum_{j=1}^{k-1}(B_j+A_{j+1})+B_k\\
&\ge
(1-u)+(k-1)+(1-v)\\
&=
k+1-u-v.
\end{aligned}
$$

## 6. Capacity corollary

If the internal roles satisfy

$$
A_j+B_j\le\kappa_j,
$$

then the chain cannot be covered whenever

$$
\boxed{
\sum_{j=1}^k\kappa_j<k+1-u-v.
}
$$

In particular, if every internal row is nonsupercritical, then
$\kappa_j=1$, and the contradiction condition is simply

$$
\boxed{u+v<1.}
$$

For four nonsupercritical internal rows, if the external left contribution is
$b$ and the far-side requirement is $h$, then the right external contribution
is $1-h$, and the path bound becomes

$$
\sum_{j=1}^4(A_j+B_j)
\ge
4+h-b.
$$

Thus $h>b$ gives an immediate contradiction to the four unit row caps.
