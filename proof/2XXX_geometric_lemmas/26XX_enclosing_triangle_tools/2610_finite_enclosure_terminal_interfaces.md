# Finite-Enclosure Terminal Interfaces

Status: Proven

This is the active terminal-first interface for Strategy 3.  The detailed
case packages contain their placement calculations; this file states the
common forcing engine, six terminal families, and the adapter-to-terminal map.
No active proof composes boundary-transfer maps.

## 1. Common forcing engine

Suppose the closed V role \(T_i=\overline{U_i}\) realizes selected lower
bounds

\[
a_i\le A_i,\qquad b_i\le B_i.
\]

Let \(c_{\max}(a_i,b_i)\) be the exact own-ray capacity from
[`2004`](../20XX_V_triangle_geometry/2004_admissible_set.md).  For an
adjacent role actually permitted by its V type to support \(r_i\), use the
neighboring capacities \(C_+\) and \(C_-\) from
[`2008`](../20XX_V_triangle_geometry/2008_neighbor_ray_max_c_formula.md).
Put

\[
\Gamma_i
=
\max\{
c_{\max}(a_i,b_i),
C_+(a_{i-1},b_{i-1}),
C_-(a_{i+1},b_{i+1})
\},
\tag{1}
\]

omitting forbidden or undefined neighboring terms, and define

\[
D_i=(1-\Gamma_i)V_i.
\tag{2}
\]

The type-aware forcing theorem in
[`2608`](2608_residual_hull_finite_enclosure_principle.md) gives

\[
D_i\notin U_0\cup\cdots\cup U_5,
\qquad
D_i\in U_C
\tag{3}
\]

under a hypothetical cover.

For a common pair \(p,q\ge0\), \(p+q\le1\), put
\(c_*=c_{\max}(p,q)\) and \(m=\min\{p,q\}\).  Common-pair domination gives

\[
C_+(p,q),C_-(p,q)\le1-m\le c_*.
\tag{4}
\]

Thus one radial capacity controls the own traces and every permitted
neighboring trace, whether supplied by a Vd1, Vd2, or T3-like role.
Corollary 5.1 of `2608` reselects the common pair in every role and
forces the unchanged symmetric points $(1-c_*)V_i$ when $0<c_*<1$.

If a compact set \(K\) lies in the open unit C triangle, moving its three
side lines inward gives

\[
K\subset U_C
\quad\Longrightarrow\quad
\Lambda(K)<1.
\tag{5}
\]

Every global enclosure terminal below contradicts (5).

## 2. Terminal A: common disk plus the actual gap

### Theorem 2.1

A one-gap state with \(N_+=0\), no Vd1/Vd2 role, and only Vd0 roles or at
most two T3-like roles is impossible.

### Proof

Normalize the actual gap to

\[
J=[X(\ell),X(r)]\subset e_{0,1},
\qquad
\ell=B_0,\qquad r=1-A_1.
\tag{6}
\]

The five center-free handoffs give the common pair

\[
p=1-r,\qquad q=\ell.
\tag{7}
\]

The all-Vd0 chain is proved in
[`4013_new`](../../4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss_new/4013_new_all_Vd0_finite_enclosure.md),
while
[`4070_new`](../../4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2_new/4070_new_T3_like_finite_enclosure.md)
checks the permitted T3-like neighboring terms.  By (3)--(4), all six points
\((1-c_*)V_i\) lie in \(U_C\), so convexity gives

\[
\mathcal D_{h(1-c_*)}\subset U_C,
\qquad
h=\frac{\sqrt3}{2}.
\]

The actual gap, including a singleton, also lies in \(U_C\).  The
complementary-gap theorem in `2608` gives

\[
\Lambda(\mathcal D_{h(1-c_*)}\cup J)\ge1,
\]

contradicting (5). \(\square\)

The distinction between all-Vd0 and T3-like states belongs entirely to the
adapter; their terminal is identical.

## 3. Terminal B: common CE2 two-gap short ray

### Theorem 3.1

In the strict signed CE2 domain of
[`2109`](../21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md),
put

\[
p=W-\alpha,\qquad q=R-\delta,\qquad
e=\min\{\alpha,\delta\}.
\tag{8}
\]

If the intervening V roles dominate \((p,q)\) and every permitted
neighboring support is controlled by (4), then the configuration is
impossible.

### Proof

The short-ray theorem in
[`2609`](2609_simplified_finite_enclosure_lemmas.md) gives

\[
c_{\max}(p,q)<1-e.
\tag{9}
\]

Type-aware forcing puts

\[
D_2=(1-c_{\max}(p,q))V_2,
\qquad
D_4=(1-c_{\max}(p,q))V_4
\]

in \(U_C\).  If \(e=\delta\), \(D_2\) lies beyond the C exit on \(r_2\);
if \(e=\alpha\), \(D_4\) lies beyond the C exit on \(r_4\).  Both alternatives
are impossible. \(\square\)

This terminal is independent of the criticality of \(T_0\).  It closes all
applicable two-gap Vd0/T3-like rows with \(N_+\in\{0,1\}\), including the
rank-two output of the corrected Vd1 replacement.

## 4. Terminal C: one-gap transverse return

### Theorem 4.1

Assume exactly one actual gap, all V roles are Vd0, and exactly one actual V
role is supercritical.  Normalize that role to \(T_0\), write the gap as in
(6), and put

\[
P_i=(1-C_i)V_i
\]

for the actual own-radial reaches.  Then

\[
K_{\rm tr}
=
\{O,M_0,X(\ell),X(r),P_2,P_3,P_4\}
\tag{10}
\]

satisfies \(\Lambda(K_{\rm tr})\ge1\).

### Proof

The points in (10) are center-forced by open endpoint ownership, Vd0
locality, and diameter locality.  The direct theorem
[`4103`](../../4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0_new/4103_transverse_seven_point_enclosure.md)
proves the enclosure bound.  Its two endings use the same setup:

1. the gap endpoints give \(A_0<1-Q\);
2. the five gap-free edges give
   \(A_1<A_2<A_3<A_4<A_5<A_0\);
3. CE2 ends with the thresholds supplied by \(P_2,P_4\);
4. CE1 ends with the reverse return supplied by \(P_4,P_3,P_2\), which
   gives \(A_0>1-Q\).

Thus (5) is contradicted. \(\square\)

The former points \(P_0,P_1,P_5\) are not active terminal data.

## 5. Terminal D: supported rescuer tail

For \(0\le c\le1/2\), let

\[
M_c^{\rm sup}
=
\frac{c+\sqrt{c^2-8c+4}}2
\]

be the nonattained outgoing supremum for a strict-supercritical role with
own-radial reach at least \(c\).

### Theorem 5.1

Suppose a special role at \(V_0\) has supported interval
\([c,u]\subset r_1\), measured from \(V_1\) toward \(O\), and boundary
endpoint \(a\) on \(e_{5,0}\).  Put \(\varepsilon=1-u\) and
\(M=M_c^{\rm sup}\).  Assume

\[
\varepsilon V_1\in U_C,\qquad
a+\varepsilon\le1,
\tag{11}
\]

\[
a\le1-M,\qquad
\frac{a}{a+\varepsilon}\le1-M.
\tag{12}
\]

If \(T_1\) is uniquely supercritical and \(T_2,T_3,T_4,T_5\) are
nonsupercritical on the center-free four-edge path, then the skeleton is not
covered.

### Proof

The rescuer-tail theorem in `2609` shows that (11)--(12) force the far demand
on \(T_5\) to be at least \(M\), while strict supercriticality gives
\(B_1<M\).  Adding the four center-free handoffs yields

\[
\sum_{i=2}^5(A_i+B_i)
\ge4+M-B_1
>4,
\]

contrary to nonsupercriticality. \(\square\)

The two active type-specific adapters are:

- the T3-like proof
  [`4130_new`](../../4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like_new/4130_new_T3_like_finite_enclosure.md);
- the Vd1 proof
  [`4143_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4143_new_Vd1_rescuer_finite_enclosure.md).

They verify the same hypotheses (11)--(12).  No type-specific center-hiding
argument remains after that verification.

## 6. Terminal E: residual radial separation

### Lemma 6.1

Parametrize \(r_i\) by \(xV_i\), \(0\le x\le1\).  Suppose the closed C role
has radial trace contained in \(0\le x\le d_C\), and suppose there is
\(c_{\rm loc}\) such that

\[
(U_{i-1}\cup U_i\cup U_{i+1})\cap r_i
\subseteq
\{xV_i:x\ge1-c_{\rm loc}\}.
\tag{13}
\]

If

\[
c_{\rm loc}<1-d_C,
\tag{14}
\]

then the skeleton is not covered.

### Proof

Choose \(x\) with \(d_C<x<1-c_{\rm loc}\).  The point \(xV_i\) is missed
by the C role and the three local V roles.  The remaining V roles are
excluded by diameter locality.  Hence \(xV_i\) is uncovered. \(\square\)

The active placement proofs are now both contained in the new one-Vd package:

- [`4141_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4141_new_adjacent_Vd_finite_enclosure.md)
  verifies (13)--(14) on \(r_2\) by the exact residual estimate and the
  one-third radial envelope;
- [`4142_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4142_new_nonadjacent_Vd_finite_enclosure.md)
  forces \(D_\tau\) beyond both the Vd and C traces.

## 7. Terminal F: zero-gap asymmetric support

### Theorem 7.1

If the six original open V roles cover \(\partial H\) and exactly one
actual role is supercritical, a seven-role cover of \(H\) is impossible,
independently of the C-triangle class and the normalized V-type pattern.

### Proof

The center-independent theorem
[`31058`](../../3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31058_center_independent_direct_nine_point_obstruction.md)
constructs

\[
K_{\rm wit}
=
\mathcal D_{h(1-c_*)}\cup\{Q_-,Q_0,Q_+\}
\subset U_C
\]

and proves \(\Lambda(K_{\rm wit})\ge1\).  The six radial points use the same
common-pair forcing engine as Terminal A: reselecting \((p,q)\) makes
every permitted maximum equal to \(c_*\). The asymmetric-point exclusions
use actual handoffs and distances, not Vd0 locality. Since no actual gap is available,
the three asymmetric frontier witnesses replace the missing gap segment.
The two mixed support-cap overlaps are verified by the exact colocated
certificate.  Equation (5) gives the contradiction. \(\square\)

The polynomial certificate remains specific to this terminal.

## 8. Corrected replacement is a router

The active two-chart construction is

[`4144_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md).

It preserves the covered skeleton and produces six nonsupercritical Vd0
roles.  It is not a seventh terminal.  Its output gap rank must be recomputed.

| Output gap rank | Destination |
|---:|---|
| \(0\) | boundary-complete length row Z0 in [`2531`](../25XX_length_bounds/2531_length_budget_corollaries.md) |
| \(1\) | Terminal A |
| \(2\) | Terminal B |

No preservation of the input gap rank is asserted.

## 9. Strategy 3 assembly

### Theorem 9.1

Every routing row assigned wholly or partly to Strategy 3 is impossible.

### Proof

| Normalized row | Terminal |
|---|---|
| \(N_{\rm gap}=0,\ N_+=1\), arbitrary V types | F |
| one gap, \(N_+=0\), all Vd0 or at most two T3-like roles | A |
| two gaps, \(N_+\in\{0,1\}\), all Vd0/T3-like | B |
| one gap, \(N_+=1\), all Vd0 | C |
| one gap, \(N_+=1\), exactly one T3-like role | D |
| CE2, \(N_+=1\), exactly one Vd1/Vd2 role | D, E, Strategy 1, or the replacement router |

The first five rows are Theorems 2.1--7.1.  The final row is the complete
package
[`4140_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4140_new_one_Vd_finite_enclosure_assembly.md),
whose placement audit is
[`4145_new`](../../4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4145_new_complete_placement_audit.md).
\(\square\)

## 10. Detailed source ownership

| Source | Adapter or calculation | Terminal |
|---|---|---|
| `4013_new` | all-Vd0 common-pair chains | A or B |
| `4070_new` | T3-like neighboring-capacity check | A or B |
| `4102_new`, `4103` | CE1 reverse return and CE2 thresholds | C |
| `4130_new` | T3-like endpoint inequalities | D or B |
| `4141_new` | adjacent Vd residual estimate and one-third envelope | E |
| `4142_new` | nonadjacent diameter transfer and radial separation | E |
| `4143_new` | Vd1 endpoint inequalities | D |
| `4144_new` | two-chart replacement | router |
| `4145_new` | placement exhaustiveness | final one-Vd assembly |
| `3105X` | asymmetric witnesses and exact support-cap certificate | F |

The old 4143, 4144, 4146, 4147, 4148, and 414b paths are
Reference-status compatibility pointers and contain no second proof body.
