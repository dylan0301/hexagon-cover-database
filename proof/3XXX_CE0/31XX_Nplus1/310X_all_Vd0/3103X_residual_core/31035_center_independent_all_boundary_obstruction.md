# Center-Independent All-Boundary Obstruction

Status: Proven

This theorem is the center-independent conclusion of the `3103X`
residual-core argument.

## Theorem

The side-one regular hexagon $H$ has no cover by open unit equilateral
triangles

$$
T_C,T_0,\dots,T_5
$$

such that

1. $T_i$ is a Vd0 role at $V_i$ for every $i$;
2. $T_0,\dots,T_5$ cover $\partial H$; and
3. exactly one actual maximal boundary row is supercritical.

No center class is assumed for $T_C$.

## Proof

### 1. The strict two-parameter domain

Apply the exact-one case of the strict-handoff theorem
[`1214_strict_boundary_handoff_selection.md`](../../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md).
It supplies points

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad 0<x_i<1,
$$

covered by both endpoint roles, and selected row demands

$$
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Exactly one selected row is supercritical, at the same index as the unique
supercritical actual row. Rotate the indices so that this is row $4$.
Every other selected row is strictly nonsupercritical, so

$$
a_i+b_i<1
\quad\Longleftrightarrow\quad
x_i<x_{i-1}
\qquad(i\ne4).
$$

Reading these five inequalities cyclically gives

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{1}
$$

Set

$$
a=1-x_3,
\qquad b=x_4.
$$

Then $0<a,b<1$, and (1) gives $a+b>1$. The points $X_3,X_4$ lie in the
open unit triangle $T_4$ and are at distances $a,b$ from $V_4$ along rays
meeting at $120^\circ$. Its closure has diameter $1$, with equality only
between two vertices; those vertices are not in the open triangle. Hence

$$
\lVert X_3-X_4\rVert^2=a^2+ab+b^2<1.
$$

Thus

$$
0<a,b<1,
\qquad a+b>1,
\qquad a^2+ab+b^2<1.
\tag{2}
$$

### 2. From the actual cover to the model cores

Let $R_i(u,v)$ be the corner-cone-clipped closed $AB$-union at $V_i$.
Its definition and exact certificate are in
[`20090_ab_set_index.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20090_ab_set_index.md)
and
[`20095_exact_caliper_certificate.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20095_exact_caliper_certificate.md).
It is antitone in both demands:

$$
u'\ge u, v'\ge v
\quad\Longrightarrow\quad
R_i(u',v')\subseteq R_i(u,v).
\tag{3}
$$

Define the residual left by the six selected rows:

$$
\mathcal U_6^\circ
=\mathrm{int}(H)
\setminus\bigcup_{i=0}^5\mathrm{int}R_i(a_i,b_i).
\tag{4}
$$

Because $T_i$ contains $V_i,X_{i-1},X_i$, its closure is one of the
triangles represented in $R_i(a_i,b_i)$. If
$P\in\mathrm{int}(H)\cap T_i$, then $P$ is interior both to the corner
cone and to $T_i$; a small plane ball around $P$ therefore lies in
$R_i(a_i,b_i)$. Thus $P\in\mathrm{int}R_i(a_i,b_i)$. No point of
$\mathcal U_6^\circ$ is covered by a vertex role, and the full cover implies

$$
\mathcal U_6^\circ\subseteq T_C.
\tag{5}
$$

Put $p=1-b$ and $q=1-a$. By (1), every $x_j$ lies in $[x_3,x_4]$.
Consequently, for $i\ne4$,

$$
a_i=1-x_{i-1}\ge p,
\qquad b_i=x_i\ge q.
\tag{6}
$$

Now define

$$
\begin{aligned}
\mathcal C_{\mathrm{asym}}(a,b)
&=\mathrm{int}(H)\setminus
\left(\mathrm{int}R_4(a,b)
\cup\bigcup_{i\ne4}\mathrm{int}R_i(p,q)\right),\\
\mathcal C_{\mathrm{sym}}(a,b)
&=\mathrm{int}(H)\setminus
\bigcup_{i=0}^5\mathrm{int}R_i(p,q).
\end{aligned}
\tag{7}
$$

Equations (3) and (6) give
$R_i(a_i,b_i)\subseteq R_i(p,q)$ for $i\ne4$. Taking complements in
$\mathrm{int}(H)$ gives

$$
\mathcal C_{\mathrm{asym}}(a,b)\subseteq\mathcal U_6^\circ.
$$

Also $a>p$ and $b>q$, so (3) gives
$R_4(a,b)\subseteq R_4(p,q)$. A second complement reverses this inclusion.
Together with (5),

$$
\boxed{
\mathcal C_{\mathrm{sym}}(a,b)
\subseteq\mathcal C_{\mathrm{asym}}(a,b)
\subseteq\mathcal U_6^\circ
\subseteq T_C.}
\tag{8}
$$

These are the only comparisons between the actual cover and the two model
cores.

### 3. The forced compact set

Let $c_*=c_{\max}(p,q)$. The symmetric-witness theorem
[`31032_symmetric_witness_construction.md`](31032_symmetric_witness_construction.md)
proves that $0<c_*<1$ and that

$$
P_k=(1-c_*)V_k\in\mathcal C_{\mathrm{sym}}(a,b)
\qquad(k=0,\dots,5).
$$

By (8), all six $P_k$ lie in the convex triangle $T_C$. Their convex hull
contains the closed disk

$$
\mathcal D(a,b)
=\left\{x:\lVert x\rVert\le
\frac{\sqrt3}{2}(1-c_*)\right\},
$$

so $\mathcal D(a,b)\subseteq T_C$. The asymmetric-witness theorem
[`31033_asymmetric_witness_construction.md`](31033_asymmetric_witness_construction.md)
also gives exact points

$$
Q_-(a,b),Q_0(a,b),Q_+(a,b)
\in\mathcal C_{\mathrm{asym}}(a,b).
$$

Therefore (8) forces the compact set

$$
K_{\mathrm{wit}}(a,b)
=\mathcal D(a,b)\cup\{Q_-(a,b),Q_0(a,b),Q_+(a,b)\}
\subseteq T_C.
\tag{9}
$$

Let $\Lambda(K)$ be the least side length of a closed equilateral triangle
containing $K$. The terminal cap reduction and analytic adjacent-overlap proof
are in
[`31034_witness_enclosure_inequality.md`](31034_witness_enclosure_inequality.md),
and the two remaining mixed overlaps are proved without interval arithmetic in
[`31037_rational_cmax_upper_envelope.md`](31037_rational_cmax_upper_envelope.md).
Together they prove throughout (2) that

$$
\Lambda(K_{\mathrm{wit}}(a,b))\ge1.
\tag{10}
$$

But a compact subset of an open unit equilateral triangle has positive
clearance from all three sides. Moving the three sides inward by less than
that clearance produces a closed equilateral triangle of side less than $1$
that still contains the compact set. Equation (9) therefore gives
$\Lambda(K_{\mathrm{wit}}(a,b))<1$, contradicting (10). This proves the theorem.

The proof used no CE0, CE1, or CE2 property of $T_C$. It also does not use
the optional $F_6$ conjecture in `4104`.

The exact-one hypothesis supplies the adjacent global-minimum-to-global-maximum
handoff used in (6). It cannot in general be replaced by $N_+\ge2$ and a
different strict-handoff selection. The exact comparison criterion, an
$AB$-set noninclusion, and an actual all-Vd0 full-boundary counterexample are
proved in
[`31036_Nplus_ge2_complementary_AB_comparison_counterexample.md`](31036_Nplus_ge2_complementary_AB_comparison_counterexample.md).
