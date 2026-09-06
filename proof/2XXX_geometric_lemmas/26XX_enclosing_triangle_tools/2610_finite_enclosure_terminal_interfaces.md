# Fixed Finite-Enclosure Terminal Interfaces

Status: Proven

This is the active interface for the finite-enclosure method. The shared
forcing and candidate arguments are proved in
[`2612`](2612_fixed_witness_unification.md). A fixed finite set belongs to
the original open C triangle under coverage, and every open unit candidate
is excluded from containing that same set. This is stronger than a point
lying outside the original C triangle.

Use original open roles $U_C,U_i$ and closures $T_C,T_i$. Uppercase
$A_i,B_i,C_i$ are actual maximal reaches, and $N_+$ is defined by
$A_i+B_i>1$. Actual gaps include singleton gaps. Put
$X_i(t)=(1-t)V_i+tV_{i+1}$, $M_i=V_i/2$, $h=\sqrt3/2$.

## 1. Common fixed witnesses

The actual gap on $e_{i,i+1}$ is
$J_i=X_i([B_i,1-A_{i+1}])$. Its endpoints are missed by every open V role.
For each ray set

$$
\gamma_i=\max\{C_i,u_{i-1\to i},u_{i+1\to i}\},
\qquad \widehat P_i=(1-\gamma_i)V_i,
$$

where $u_{j\to i}$ is the actual O-side endpoint of a positive neighboring
trace, measured from $V_i$ toward $O$, with zero for an absent trace.
`2612`, Lemma 2.2, proves that every $\widehat P_i$ is noncentral and missed
by the open V roles. This is not the own-ray endpoint $(1-C_i)V_i$ unless
neighboring traces are absent or dominated.

The common capacity inequality is

$$
C_+(p,q),C_-(p,q)\le1-\min\{p,q\}\le c_{\max}(p,q),
\quad p,q\ge0,\quad p+q\le1.
$$

It is proved in [`2608`](2608_residual_hull_finite_enclosure_principle.md).
A candidate containing a fixed total endpoint yields a strict lower demand
on the maximum. If both neighboring terms are below it, the own role must
supply that demand. This is the type-independent demand-recovery interface
of `2612`, Lemma 2.3.

## 2. A: complementary gap, at most seven points

For one gap and $N_+=0$, normalize the gap to $J_0$, set
$p=A_1$, $q=B_0$, $c_A=c_{\max}(p,q)$, and select its farther endpoint

$$
G_A=\begin{cases}X_0(q),&q\le p,\\X_0(1-p),&p<q.\end{cases}
$$

Then

$$
K_A=\{(1-c_A)V_i:0\le i\le5\}\cup\{G_A\},
\qquad \mathcal D_A=\{x:\|x\|\le h(1-c_A)\}.
$$

Theorem 3.1 of `2612` proves $K_A\subset U_C$ under skeleton coverage and
$\Lambda(K_A)\ge1$, for arbitrary V types. The disk is contained in the
hull of the six radial points; it is not an independent set of pointwise
V-excluded witnesses. The all-Vd0 and T3-like one-gap cases share this proof.

## 3. B: two-gap path, at most four points

Suppose the only gaps are on $e_{5,0},e_{0,1}$ and
$A_i+B_i\le1$ for $1\le i\le5$. Use

$$
K_B=\{X_5(B_5),X_0(1-A_1),\widehat P_2,\widehat P_4\}.
$$

Theorem 4.1 of `2612` proves $\Lambda(K_B)\ge1$. Under skeleton coverage,
$K_B\subset U_C$. The origin is implicit in the convex hull, and no disk
is used. This includes $N_+=0$ and $N_+=1$ with supercritical $T_0$,
without a V-type split on the five-role path.

## 4. C: one-gap path, at most six points

Suppose the only gap is $J_0$ and $A_i+B_i\le1$ for $1\le i\le5$. Use

$$
K_C=\{M_0,X_0(B_0),X_0(1-A_1),
\widehat P_2,\widehat P_3,\widehat P_4\}.
$$

Theorem 5.1 of `2612` proves $\Lambda(K_C)\ge1$. Under skeleton coverage
with distinguished C midpoint $M_0$, this set lies in $U_C$. No disk or
separate own-ray endpoints are used. The theorem does not require $T_0$ to
be supercritical. Its proof keeps the CE1 selected-branch conditions from
[`4102`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4102_new_CE1_direct_radial_certificate.md)
and recovers the three own demands before invoking the full return.

Both the adjacent and nonadjacent one-Vd placements with supercritical
$T_0$ now use C with one gap and B with two gaps. The old residual-separation
estimates are retained as alternatives, not active E families.

## 5. D: supported rescuer, at most four points

Let $Y(t)=(1-t)V_0+tV_5$. In the reduced rescuer placement, $T_0$ rescues
$M_1$, $T_1$ is uniquely supercritical, and the four remaining roles are
nonsupercritical on the center-free path. Write the actual neighboring trace
on $r_1$ as $[c,u]$, put $\varepsilon=1-u$, and set

$$
M=M_c^{\rm sup}=\frac{c+\sqrt{c^2-8c+4}}2.
$$

The local adapter must prove

$$
\varepsilon V_1\in U_C,\quad C_1\ge c,\quad
A_0+\varepsilon\le1,\quad
\frac{A_0}{A_0+\varepsilon}\le1-M.
$$

Corollary 6.2 of `2612` then gives the fixed set

$$
K_D=\{O,\varepsilon V_1,Y(A_0),Y(1-B_5)\}\subset U_C,
\qquad \Lambda(K_D)\ge1.
$$

No disk is used. The same geometric four-point lemma applies to the
T3-like local calculation in
[`4130_new`](../../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md)
and the Vd1 calculation in
[`4143_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md),
for both nonzero gap ranks. The former sum greater than four is not the
active terminal. A Vd2 rescuer still uses its length exit; these local ratio
inequalities are not assumed for it.

## 6. F: unchanged zero-gap nine-point enclosure

For zero gaps and $N_+=1$, the type-independent theorem
[`31058`](../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md)
forces

$$
K_F=\{(1-c_*)V_i:0\le i\le5\}\cup\{Q_-,Q_0,Q_+\}
$$

and proves $\Lambda(K_F)\ge1$, where
$c_*=c_{\max}(1-b,1-a)$ for the selected strict-supercritical demands
$a<A_4$, $b<B_4$. The comparison disk is

$$
\mathcal D_F=\{x:\|x\|\le h(1-c_{\max}(1-b,1-a))\}.
$$

If $c_*\le2/3$, its six radial points already suffice. Otherwise the same
three asymmetric points and exact certificate are used. Neither the source
of the asymmetric witnesses nor the exact certificate is modified by this
refactor. Full-hexagon coverage, not merely skeleton coverage, is required.
The four-contact caliper theorem `2611` is distinct from D's four-point lemma.

## 7. N0 and the replacement exit

Theorem 7.1 of `2612` states that a skeleton cover has $N_+\ge1$.
Its proof treats zero gaps by strict boundary overlap, one gap by A, and
two gaps by B. It does not restrict the nonsupercritical V types.

The two-chart Vd1 replacement
[`4144_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md)
keeps the original C triangle fixed, preserves the skeleton, and produces
six nonsupercritical V roles. It therefore ends directly by N0. Input and
output gap ranks are not identified; the gap split is internal to N0.
Replacement is not an additional enclosure theorem for the original set.

## 8. Exhaustive assembly and source ownership

The structural placement audit still supplies the finite reduced placements.
Length and area exits remain explicitly distinct:

| Reduced input | Active route |
|---|---|
| zero gaps, $N_+=0$ | strict boundary-overlap contradiction |
| zero gaps, $N_+=1$ | F |
| zero gaps, $N_+\ge2$ | retained area route |
| nonzero gaps, $N_+=0$ | N0 (A or B) |
| one gap, $N_+=1$, supercritical at $M_0$ | C, arbitrary path V types |
| two gaps, $N_+=1$, supercritical at $M_0$ | B, arbitrary path V types |
| center-based T3-like or Vd1 rescuer | D, either gap rank |
| away Vd1--supercritical pair | replacement then N0 |
| Vd2 rescuer or excess positive support | retained length filters |
| nonzero gaps, $N_+\ge2$ | retained skeleton-length route |

The complete one-Vd placement audit remains
[`4145_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4145_new_complete_placement_audit.md).
It no longer dispatches adjacent and nonadjacent Vd placements to separate
active enclosure recipes. The sources `4141_new` and `4142_new` preserve
those former quantitative arguments as alternatives. The independent
conditional CE1 algebra, the two rescuer charts, and the exact zero-gap
certificate remain local proof responsibilities rather than duplicated
terminal endings.
