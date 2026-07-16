# Center-Independent All-Boundary Residual-Core Obstruction

Status: Proven

This note extracts the center-class-independent theorem proved by the
`3103X` residual-core route. It applies whenever six Vd0 vertex roles cover
the whole boundary and have exactly one supercritical actual row. The seventh
role need not be CE0, CE1, or CE2 at this stage; it is used only as an open
unit equilateral triangle that completes the cover of $H$.

## 1. The theorem

**Theorem.** There is no cover of the side-one regular hexagon $H$ by open
unit equilateral triangles

$$
T_C,T_0,\dots,T_5
$$

with all of the following properties:

1. every $T_i$, $0\le i\le5$, is a Vd0 vertex role at $V_i$;
2. the six vertex roles cover $\partial H$; and
3. exactly one actual maximal boundary row of the six vertex roles is
   supercritical.

Here the actual maximal incoming and outgoing reaches of $T_i$ are denoted by
$A_i$ and $B_i$. Thus the third hypothesis says that exactly one index
satisfies

$$
A_i+B_i>1.
$$

The distinction between these actual reaches and the smaller handoff demands
used below is the convention of
[`1202_local_coordinates_abc.md`](../../../../1XXX_foundations/12XX_V_triangle/1202_local_coordinates_abc.md).

## 2. Strict handoffs and the two-parameter domain

The strict boundary-handoff argument is recorded in
[`1214_strict_boundary_handoff_selection.md`](../../../../1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md)
and, for this exact-one setting, in
[`4104_all_boundary_transfer_to_310X.md`](../../../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4104_all_boundary_transfer_to_310X.md).
For completeness, the part needed here is as follows.

On the relative interior of $e_{i,i+1}$, Vd0 locality leaves only the two
endpoint roles with positive-length local support. Openness and full boundary
coverage therefore give the strict overlap

$$
1-A_{i+1}<B_i.
$$

Choose

$$
x_i\in(1-A_{i+1},B_i)
$$

and put

$$
X_i=V_i+x_i(V_{i+1}-V_i),
\qquad
(a_i,b_i)=(1-x_{i-1},x_i).
$$

Then $V_i,X_{i-1},X_i\in T_i$. If the actual row $i$ is
nonsupercritical, then

$$
x_i<B_i\le1-A_i<x_{i-1},
$$

so its selected row is strictly nonsupercritical:

$$
a_i+b_i<1.
$$

The selected row sums telescope to

$$
\sum_{i=0}^5(a_i+b_i)
=
\sum_{i=0}^5(1-x_{i-1}+x_i)
=6.
$$

Thus the remaining selected row is strictly supercritical. It has the same
index as the unique supercritical actual row. Rotate indices so that this is
row $4$. The five strict inequalities then give

$$
x_3<x_2<x_1<x_0<x_5<x_4.
\tag{1}
$$

Set

$$
a=a_4=1-x_3,
\qquad
b=b_4=x_4.
$$

Because every $X_i$ lies in the relative interior of its unit edge,
$0<a,b<1$. Equation (1) gives $a+b>1$. The two points $X_3,X_4$ lie in the
same open unit equilateral triangle $T_4$, whose diameter is $1$ but is not
attained by two of its points. In the local $120$-degree corner coordinates,
therefore,

$$
\lVert X_3-X_4\rVert^2
=a^2+ab+b^2<1.
\tag{2}
$$

Hence $(a,b)$ lies in the full strict domain required by `31032`--`31034`:

$$
0<a,b<1,
\qquad
a+b>1,
\qquad
a^2+ab+b^2<1.
\tag{3}
$$

## 3. Actual residual and model cores

For each $i$, let $R_i(u,v)$ be the $V_i$-placed,
corner-cone-clipped closed $AB$-union determined by incoming demand $u$ and
outgoing demand $v$. Its definition and exact all-parameter certificate are
recorded in
[`20090_ab_set_index.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20090_ab_set_index.md)
and
[`20095_exact_caliper_certificate.md`](../../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/20095_exact_caliper_certificate.md).
These unions are antitone in the demands:

$$
u'\ge u,
\quad
v'\ge v
\quad\Longrightarrow\quad
R_i(u',v')\subseteq R_i(u,v).
\tag{4}
$$

Define the plane-interior residual of the six selected row unions by

$$
\mathcal U_6^\circ
=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5\mathrm{int}\left(R_i(a_i,b_i)\right).
\tag{5}
$$

The closure of the actual $T_i$ is one of the unit triangles used in the
definition of $R_i(a_i,b_i)$. Consequently, if
$P\in\mathrm{int}(H)\cap T_i$, a sufficiently small plane ball about $P$ is
contained in the interior of the corner cone and in $T_i$, and hence

$$
P\in\mathrm{int}\left(R_i(a_i,b_i)\right).
$$

Thus no point of $\mathcal U_6^\circ$ belongs to a vertex role. Since the
seven triangles cover all of $H$,

$$
\boxed{\mathcal U_6^\circ\subseteq T_C.}
\tag{6}
$$

The use of $\mathrm{int}(H)$ in (5) is essential: no assertion about a
plane-interior row union at a boundary point is needed.

Equation (1) implies, for every $i\ne4$,

$$
a_i\ge1-b,
\qquad
b_i\ge1-a.
\tag{7}
$$

Indeed, (1) places both $x_{i-1}$ and $x_i$ in the closed interval
$[x_3,x_4]$. Combining (4) and (7) gives

$$
R_i(a_i,b_i)\subseteq R_i(1-b,1-a),
\qquad i\ne4.
\tag{8}
$$

Define

$$
\mathcal C_{\mathrm{asym}}(a,b)
=
\mathrm{int}(H)
\setminus
\left(
\mathrm{int}\left(R_4(a,b)\right)
\mathbin\cup
\bigcup_{i\ne4}
\mathrm{int}\left(R_i(1-b,1-a)\right)
\right),
\tag{9}
$$

and

$$
\mathcal C_{\mathrm{sym}}(a,b)
=
\mathrm{int}(H)
\setminus
\bigcup_{i=0}^5
\mathrm{int}\left(R_i(1-b,1-a)\right).
\tag{10}
$$

For $i\ne4$, equation (8) says that the forbidden comparison-row interior
contains the forbidden selected-row interior. The distinguished row is the
same $R_4(a,b)$ in (5) and (9). Taking complements in $\mathrm{int}(H)$
therefore gives

$$
\mathcal C_{\mathrm{asym}}(a,b)
\subseteq\mathcal U_6^\circ.
$$

Moreover, $a>1-b$ and $b>1-a$, so (4) gives

$$
R_4(a,b)\subseteq R_4(1-b,1-a).
$$

The forbidden union in (10) consequently contains the forbidden union in
(9). Taking complements once more gives

$$
\mathcal C_{\mathrm{sym}}(a,b)
\subseteq\mathcal C_{\mathrm{asym}}(a,b).
$$

Together with (6), these inclusions prove

$$
\boxed{
\mathcal C_{\mathrm{sym}}(a,b)
\subseteq
\mathcal C_{\mathrm{asym}}(a,b)
\subseteq
\mathcal U_6^\circ
\subseteq T_C.
}
\tag{11}
$$

## 4. The forced compact witness

Put

$$
p=1-b,
\qquad
q=1-a,
\qquad
c_*=c_{\max}(p,q).
$$

The proven symmetric-witness theorem
[`31032_symmetric_witness_construction.md`](31032_symmetric_witness_construction.md)
gives $0<c_*<1$ and

$$
P_k=(1-c_*)V_k
\in\mathcal C_{\mathrm{sym}}(a,b),
\qquad k=0,\dots,5.
\tag{12}
$$

By (11), all six points lie in $T_C$. Their convex hull is a regular hexagon,
so convexity of $T_C$ forces the closed centered disk

$$
\mathcal D(a,b)
=
\left\{
x:\lVert x\rVert\le
\frac{\sqrt3}{2}(1-c_*)
\right\}
\tag{13}
$$

into $T_C$.

The proven asymmetric-witness theorem
[`31033_asymmetric_witness_construction.md`](31033_asymmetric_witness_construction.md)
defines exact points $Q_-(a,b),Q_0(a,b),Q_+(a,b)$ and proves

$$
Q_-,Q_0,Q_+
\in\mathcal C_{\mathrm{asym}}(a,b).
\tag{14}
$$

Hence (11), (13), and (14) give the compact containment

$$
K_{\mathrm{wit}}(a,b)
:=
\mathcal D(a,b)
\mathbin\cup
\left\{Q_-(a,b),Q_0(a,b),Q_+(a,b)\right\}
\subseteq T_C.
\tag{15}
$$

For a bounded set $K$, let $\Lambda(K)$ be the minimum side length of a
closed equilateral triangle containing $K$. The proven terminal theorem
[`31034_witness_enclosure_inequality.md`](31034_witness_enclosure_inequality.md)
states on the whole domain (3) that

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)\ge1.
\tag{16}
$$

On the other hand, a compact subset of an open unit equilateral triangle has
positive minimum clearance from its three sides. Moving all three supporting
lines inward by less than that clearance gives a closed equilateral triangle
of side strictly below $1$ containing the compact set. Thus (15) gives

$$
\Lambda\left(K_{\mathrm{wit}}(a,b)\right)<1,
$$

contradicting (16). This proves the theorem.

## 5. Relation to the older six-point route

The optional transfer in `4104` associates the same all-boundary hypotheses
with a different finite set $K_6^{\mathrm{rel}}(a,b)$ and reduces that route
to the conjectural inequality

$$
F_6(a,b)=\Lambda\left(K_6^{\mathrm{rel}}(a,b)\right)\ge1.
$$

The theorem above does **not** prove this $F_6$ inequality. It bypasses it by
using the proved disk-plus-three-point configuration $K_{\mathrm{wit}}$.
Therefore $F_6$ may remain an open optional route without being a dependency
of the all-boundary obstruction.
