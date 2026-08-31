# CE1/CE2, $N_+=1$, All Vd0: Direct Finite-Witness Proof

Status: Proven

This package replaces the one-gap five-map proof and the two-gap paired-endpoint
proof.  The one-gap argument uses the actual radial endpoints of the six Vd0
roles as a finite set forced into the center.  CE2 is closed by a direct
one-site threshold dichotomy.  CE1 is closed by the direct reverse boundary
path proved in [`4102_new`](4102_new_CE1_direct_radial_certificate.md).  No
formal iterate or composition of transfer maps occurs.

## Theorem

Let the center role be CE1 or CE2.  Assume every V role is Vd0, exactly one
actual V role is supercritical, the seven open roles cover $H$, and at least
one boundary edge contains a V-gap.  Then no such configuration exists.

## 1. Normalization and the finite witness set

By the unique-center-midpoint theorem, normalize

$$
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\}.
$$

The midpoint argument makes $T_0$ the unique supercritical role and
$T_1,\ldots,T_5$ nonsupercritical.

For each $i$, let $C_i$ be the actual maximal own-radial reach of $T_i$ and
put

$$
P_i=(1-C_i)V_i.
\tag{1}
$$

Because $U_i$ is open, $P_i\notin U_i$.  The adjacent roles are Vd0, and the
three nonlocal roles are excluded by diameter one.  Thus every $P_i$ is missed
by all six open V roles and therefore

$$
\boxed{P_i\in U_C.}
\tag{2}
$$

Let the normalized V-gap on $e_{0,1}$ be

$$
J=[X(\ell),X(r)].
$$

By definition of an actual V-gap,

$$
\boxed{\ell=B_0,\qquad r=1-A_1.}
\tag{2a}
$$

Thus

$$
U_0\cap e_{0,1}=X([0,\ell)),
\qquad
U_1\cap e_{0,1}=X((r,1]),
\tag{2b}
$$

and the whole closed interval $J$ is center-forced.  If $a_0\le A_0$ and
$b_1\le B_1$ are the selected opposite-side lower bounds, then the local
closed footprints of the incident roles lie in

$$
\mathcal E_0^{\rightarrow}(a_0\mid\ell),
\qquad
\mathcal E_1^{\leftarrow}(1-r\mid b_1),
\tag{2c}
$$

respectively, by the trace-exact AB-envelope theorem
[`2009e`](../../../2XXX_geometric_lemmas/20XX_V_triangle_geometry/2009X_ab_set/2009e_trace_exact_ab_envelopes.md).  This is the proof-level model used in
the accompanying figures.  It is a source-conditioned subunion of the
ordinary AB-set, not an affine clipping of that set.

When there is one gap, define

$$
K_{410}=\{O,M_0,X(\ell),X(r),P_0,\ldots,P_5\}.
\tag{3}
$$

Equation (2), gap containment, and convexity give

$$
K_{410}\subset U_C.
$$

We prove directly that no open unit equilateral triangle contains $K_{410}$.
Suppose otherwise that an open unit triangle $U_C'$ contains it.  The six
fixed V roles together with $U_C'$ cover the full skeleton:

- the V roles cover every boundary edge except the displayed gap, and
  $U_C'$ contains the whole gap segment;
- on $r_i$, the V role covers from $V_i$ to its radial endpoint $P_i$, while
  $U_C'$ contains the segment from $O$ through $P_i$.

Thus the exact center and local-reach conclusions may be applied to $U_C'$.
Write its signed variables as

$$
R,W,E,\eta,P,\alpha,\delta,
\qquad W=1-R,
$$

and put

$$
k=\eta+\alpha+\delta.
$$

Containment of $P_i$ says precisely that the actual V reach satisfies

$$
C_i\ge1-d_i^{C'},
\tag{4}
$$

where $d_i^{C'}$ is the corresponding center exit.

## 2. Terminal upper bound at the supercritical role

Assume the gap lies in the right center trace

$$
\left[\frac{k}{R},W+\delta\right].
$$

Put

$$
X=R-\delta,
\qquad
Q=\frac{k}{2R}.
\tag{5}
$$

Gap containment gives

$$
B_0\ge\frac{k}{R},
\qquad
A_1\ge X.
\tag{6}
$$

Containment of $P_0$ and (4) give $C_0\ge k$.  The adjacent-edge diameter
bound therefore gives

$$
A_0
\le M_0\left(\frac{k}{R}\right)
<1-\frac{k}{2R}
=1-Q.
\tag{7}
$$

This is the only upper bound needed at the supercritical role.

## 3. Direct CE2 one-gap proof

Assume first that $U_C'$ is CE2.  The strict signed domain is

$$
\alpha+W\delta<P,
\qquad
R\alpha+\delta<P.
\tag{8}
$$

For

$$
0<d<1-rac{\sqrt3}{2},
$$

define the selected low root

$$
e(d)=rac{1-d}{2}
\left(1-\sqrt{4(1-d)^2-3}
ight).
	ag{8a}
$$

The following direct local threshold follows from the exact admissible set
`2004`: if a nonsupercritical V triangle has incoming boundary reach greater
than $e(d)$ and own-radial reach at least $1-d$, then its outgoing reach is at
most $e(d)$.  Indeed, the radial demand exceeds $1/2$, so the supercritical
cell is absent.  On the selected $L$ component the smaller coordinate is at
most $e(d)$; on the selected $T$ component the two roots of the exact quadratic
separate the feasible fiber, and the component selector discards the formal
large root.  The linear cap is unavailable once the incoming reach exceeds
$e(d)$.

From the first inequality in (8),

$$
WX=RW-W\delta=\eta+P-W\delta>\eta+\alpha.
$$

The concavity calculation

$$
\pi(q)=(\eta+q)(1-2q)-2qW
$$

has

$$
\pi(0)=\eta>0,
\qquad
\pi(P)=\eta(\eta+2ER^2)>0.
$$

Hence

$$
\boxed{X>e(\alpha).}
\tag{9}
$$

Put $T=\alpha+\delta$.  Multiplying the two inequalities in (8) by $W$ and
$R$ and adding gives

$$
E^2T<P=E\eta,
\qquad
T<\frac\eta E.
$$

The low-root bound and the concavity of

$$
\chi(t)=(\eta+t)(1-t)-2Rt
$$

on $[0,\eta/E]$ give

$$
\boxed{\min\{e(\alpha),e(\delta)\}<Q.}
\tag{10}
$$

The five nonsupercritical roles lie on center-free or V-gap-free boundary
edges.  Consequently their incoming reaches are nondecreasing along the path:

$$
A_1\le A_2\le A_3\le A_4\le A_5\le A_0.
\tag{11}
$$

Indeed, $A_i+B_i\le1$ and boundary coverage gives
$B_i+A_{i+1}\ge1$.

If $e(\alpha)<Q$, then (6), (9), and (11) give

$$
A_4>e(\alpha).
$$

The center-forced radial demand at $T_4$ is $1-\alpha$, so the direct
threshold gives

$$
B_4\le e(\alpha).
$$

Hence

$$
A_5\ge1-B_4\ge1-e(\alpha)>1-Q,
$$

and (11) yields $A_0>1-Q$, contradicting (7).

If $e(\alpha)\ge Q$, then (10) gives $e(\delta)<Q$.  Equations (6), (9), and
(11) give

$$
A_2\ge X>e(\alpha)\ge Q>e(\delta).
$$

The radial demand at $T_2$ is $1-\delta$, so

$$
B_2\le e(\delta),
\qquad
A_3\ge1-e(\delta)>1-Q.
$$

Again (11) contradicts (7).  Thus no CE2 unit triangle contains $K_{410}$.
Reflection handles a gap in the companion trace.

## 4. Direct CE1 one-gap proof

If $U_C'$ is CE1, then

$$
\Delta_L=P-R\alpha-\delta\le0.
$$

The direct reverse-path certificate
[`4102_new`](4102_new_CE1_direct_radial_certificate.md) applies to the actual
reaches supplied by (4) and the boundary coverage of the fixed V roles.  It
proves

$$
A_0>1-Q,
$$

contradicting (7).  That proof is written entirely in terms of the actual
reaches $A_i,B_i,C_i$: it starts from the assumed upper bound at $T_0$, moves
backward through $T_5,T_4,T_3,T_2$, uses two selected local chord inequalities
and one direct radial threshold, and reaches

$$
A_1+B_1>1.
$$

No formal transfer iterate is used.

Thus no CE1 unit triangle contains $K_{410}$.

## 5. Two gaps

The two-gap state is CE2-only.  The roles $T_1,\ldots,T_5$ are
nonsupercritical, while no condition on the criticality of $T_0$ is needed.
Put

$$
p=W-\alpha,
\qquad
q=R-\delta.
$$

The four center-free handoffs give the common lower pair $(p,q)$ on
$T_1,\ldots,T_5$.  The points

$$
D_2=(1-c_{\max}(p,q))V_2,
\qquad
D_4=(1-c_{\max}(p,q))V_4
$$

are missed by all V roles and forced into the center.  The CE2 short-ray
theorem
[`2608`, Theorem 6.1](../../../2XXX_geometric_lemmas/26XX_enclosing_triangle_tools/2608_residual_hull_finite_enclosure_principle.md)
places one of them strictly beyond the center exit on $r_2$ or $r_4$, a
contradiction.

The one- and two-gap states are exhaustive.  This proves the theorem.

$$
\Box
$$
