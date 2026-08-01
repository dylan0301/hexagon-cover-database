# Interval Components, Generalized Handoffs, and Boundary-Path Budgets

Status: Proven

This note isolates two elementary mechanisms that recur in the CE1/CE2
packages.  The first replaces branch-specific interval case distinctions by a
single residual-demand operator.  The second gives a boundary-path budget only
after every contribution external to the path has been explicitly accounted
for.  The latter qualification is essential: a center interval on an internal
edge cannot be silently discarded.

The generalized transfer notation follows
[`201d`](201d_raw_and_relaxed_g_chains.md): the historical map $g_c$ is in
boundary-defect coordinates, a hat imposes nonsupercriticality, and a
superscript $\vee$ denotes the complementary incoming-reach transfer.

## 1. Residual demand after a center interval

Parametrize a unit boundary edge by $[0,1]$ from its left endpoint.  Let
$J\subseteq[0,1]$ be either empty or a closed interval, and let $0\le p\le1$.
Define

$$
e_J(p)
=
\sup\left\{
x\in[0,1]:[0,x]\subseteq[0,p]\cup J
\right\},
$$

and

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

Thus enlarging any already-covered component can only decrease the remaining
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

The component of $[0,p]\cup J$ containing $0$ is $[0,e_J(p)]$.  If
$1-q>e_J(p)$, every point in the nonempty interval

$$
(e_J(p),1-q)
$$

is missed by all three traces.  Hence coverage forces
$1-q\le e_J(p)$, which is equivalent to the conclusion.  Equality is retained
for closed role triangles; strictness for original open traces is supplied
separately by the strict-handoff theorem. $\square$

## 3. Generalized actual-V triangle transfer

Let $g_c$ and $\widehat g_c$ be the raw and capped defect maps of
[`201d`](201d_raw_and_relaxed_g_chains.md).  Suppose an actual V triangle has incoming
reach at least $a$, radial reach at least $c$, and actual outgoing reach $B$.
Then

$$
B\le g_c(1-a).
$$

Define the raw center-assisted reach transfer

$$
\boxed{
g_{c,J}^\vee(a)
=
\mathcal R_J\!\left(g_c(1-a)\right).
}
$$

The edge-handoff lemma and the monotonicity of $\mathcal R_J$ give

$$
A_{\rm next}
\ge
\mathcal R_J(B)
\ge
g_{c,J}^\vee(a).
$$

If the actual V triangle is nonsupercritical, then

$$
B\le\widehat g_c(1-a).
$$

Define

$$
\boxed{
\widehat g_{c,J}^\vee(a)
=
\mathcal R_J\!\left(\widehat g_c(1-a)\right).
}
$$

Then

$$
\boxed{
A_{\rm next}
\ge
\widehat g_{c,J}^\vee(a).
}
$$

For $J=\varnothing$,

$$
g_{c,\varnothing}^\vee(a)=1-g_c(1-a)=g_c^\vee(a),
$$

and

$$
\widehat g_{c,\varnothing}^\vee(a)
=1-\widehat g_c(1-a)=\widehat g_c^\vee(a).
$$

Thus ordinary and center-assisted propagation belong to the same subscripted
$g$-family.  This formulation includes singleton center contacts and requires
no separate overlap-order split.

The exact appendix aliases are

$$
B_c(a)=g_c(1-a),
\qquad
F_c(a)=\widehat g_c(1-a),
\qquad
G_c(a)=\widehat g_c^\vee(a).
$$

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
reach to be at least $\rho(K)$.  This is the radial analogue of the boundary
handoff lemma and subsumes the usual hit-or-miss definition of the required
radial input.

## 5. Boundary-path budget with external traces accounted for

Let $E_0,E_1,\ldots,E_k$ be $k+1$ consecutive unit boundary edges, and let
$T_1,\ldots,T_k$ be the roles at the $k$ intermediate vertices.  Orient the
chain so that $T_j$ has incoming reach $A_j$ on $E_{j-1}$ and outgoing reach
$B_j$ on $E_j$.

Assume all of the following.

1. On the first edge $E_0$, the connected component covered from the endpoint
   opposite $T_1$ by **all roles other than $T_1$** has extent at most $u$.
2. On the last edge $E_k$, the analogous component covered from the endpoint
   opposite $T_k$ by **all roles other than $T_k$** has extent at most $v$.
3. On each middle edge $E_j$, $1\le j<k$, no role other than the two incident
   path roles $T_j,T_{j+1}$ has positive-length trace.  Equivalently, every
   center or external contribution on an internal edge has already been
   excluded; a point contact is harmless for the length inequality.
4. The indicated edges are covered.

Then

$$
\boxed{
\sum_{j=1}^k(A_j+B_j)
\ge
k+1-u-v.
}
$$

### Proof

The first component hypothesis and coverage give

$$
A_1\ge1-u.
$$

On a middle edge only the two incident path traces can cover a
positive-length interval, so

$$
B_j+A_{j+1}\ge1
\qquad(1\le j<k).
$$

The last component hypothesis gives

$$
B_k\ge1-v.
$$

Adding,

$$
\begin{aligned}
\sum_{j=1}^k(A_j+B_j)
&=A_1+\sum_{j=1}^{k-1}(B_j+A_{j+1})+B_k\\
&\ge(1-u)+(k-1)+(1-v)\\
&=k+1-u-v.
\end{aligned}
$$

This proves the claim. $\square$

## 6. Capacity corollary

Under the four hypotheses of Section 5, if the internal roles satisfy

$$
A_j+B_j\le\kappa_j,
$$

then the chain cannot be covered whenever

$$
\boxed{
\sum_{j=1}^k\kappa_j<k+1-u-v.
}
$$

In particular, if every internal V triangle is nonsupercritical, then
$\kappa_j=1$, and the contradiction condition is

$$
\boxed{u+v<1.}
$$

For four nonsupercritical internal V triangles, if the accounted external component
at the left has extent $b$ and the far-side requirement at the right is $h$,
then the right external component has extent $1-h$, and the path bound becomes

$$
\sum_{j=1}^4(A_j+B_j)
\ge
4+h-b.
$$

Thus $h>b$ gives an immediate contradiction to the four unit V triangle caps.

Every use of this corollary in the active proof tree verifies the internal-edge
hypothesis explicitly: the center traces are confined to the normalized one or
two adjacent boundary edges, and any endpoint center contribution is absorbed
into the residual quantities $u$ or $v$.
