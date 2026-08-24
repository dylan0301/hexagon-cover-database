# CE2, $N_+=1$, Exactly One Vd1/Vd2 Assembly

Status: Proven

The complete post-repair placement audit is
[`414b_complete_placement_reaudit.md`](414b_complete_placement_reaudit.md).
This file records the terminal assembly.

## Statement

By the exactly-one-midpoint theorem
[`2100`](../../../2XXX_geometric_lemmas/21XX_C_triangle_geometry/2100_CE1_CE2_exactly_one_midpoint_lemma.md),
applied to $T_C=\overline{U_C}$ with $O\in U_C\subset\mathrm{int}(T_C)$,
we may normalize the CE2 role as follows. Assume

$$
T_C\text{ is CE2},
\qquad
T_C\cap\{M_0,\dots,M_5\}=\{M_0\},
\qquad
N_+=1,
\qquad
N_{\rm gap}\in\{1,2\},
$$

and exactly one vertex role is Vd1 or Vd2. Then the seven open roles cannot
cover $H$.

The omitted zero-gap state is already closed by the common
boundary-complete Method 1 consequence
[`2500`](../../../2XXX_geometric_lemmas/25XX_length_bounds/2500_boundary_length_bounds.md#boundary-complete-zero-gap-consequences).

## Proof

If an additional $T_i$ satisfies
$\mathcal H^1(T_i\cap r_j)>0$ for some $j\in\{i-1,i+1\}$, `414a` gives
the direct $N_++N_{\rm sp}\ge3$ skeleton contradiction. Hence assume the complementary
no-additional-support branch. Every other nonspecial vertex role is then
nonsupercritical Vd0.

Let $T_\sigma$ be the unique supercritical role and $T_\tau$ the unique
Vd1/Vd2 role.

1. If $\sigma=0$, adjacent placements are eliminated by `4144` and
   nonadjacent placements by `4146`.
2. If $\tau=0$, midpoint forcing makes $T_\sigma$ adjacent. The Vd2 case is
   `4149`; the Vd1 case is `4143`, after reflection.
3. If $\sigma\ne0$ and $\tau\ne0$, midpoint forcing makes the two special
   roles adjacent and forces $M_\sigma\in T_\tau$. The Vd2 case is `4149`.
   In the Vd1 case, corrected `4147` uses separate $V_\tau$- and
   $V_\sigma$-charts to replace the pair by two open nonsupercritical Vd0
   roles while preserving full skeleton coverage. Recompute the output gap
   rank $N'_{\rm gap}$. If it is zero, `2500` gives the Method 1
   contradiction; if it is nonzero, the nonzero-gap part of `4013` gives
   the Method 2 contradiction. The replacement does not assert that
   $N'_{\rm gap}=N_{\rm gap}$.

These cases and the positive-support complement are disjoint and exhaustive
within the standing nonzero-gap branch; see `414b` for the
hypothesis-by-hypothesis re-audit.

$$
\Box
$$
