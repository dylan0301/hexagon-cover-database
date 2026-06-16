# Algorithm-2 Obligations And Status

Status: Reference

The intended final implication for this folder is:

$$
T_C\text{ is CE0},\quad N_+=1,\quad\text{all }T_i\text{ are Vd0}\quad\Longrightarrow\quad\text{finite-point obstruction}.
$$

This file is not a proof. It records the dependency structure and current obligations for the intended proof.

## Current Dependency Table

| Component | Recorded status | Source | Obligation |
|---|---|---|---|
| Algorithm-2 setup and point construction | Strategy | [`3102_algorithm2_setup_and_point_construction.md`](3102_algorithm2_setup_and_point_construction.md) | Define the relaxed obstruction region exactly and prove point containment for all allowed parameters. |
| Strict $P_3,P_5$ line realization | Proven | [`3105_strict_branch_line_realization.md`](3105_strict_branch_line_realization.md) | Treat the limiting boundary $\rho=1$ separately. |
| Algorithm-2 two-variable model | Proven | [`3106_algorithm2_two_variable_transition.md`](3106_algorithm2_two_variable_transition.md) | Depends on the still-open equalities $a_3+b_3=1$ and $a_5+b_5=1$. |
| Algorithm-1 tangent gap | Proven | [`3107_algorithm1_limit_tangent_gap.md`](3107_algorithm1_limit_tangent_gap.md) | Add a finite-$x$ remainder bound for the near-limit region. |
| Convex cyclic order | Proven | [`3108_convex_order_from_line_branches.md`](3108_convex_order_from_line_branches.md) | Uses strict line realization and the algorithm-2 diagonal model. |
| Transition-strip certificate | Empirical | [`3109_algorithm2_transition_strip_certificate.md`](3109_algorithm2_transition_strip_certificate.md) | Add verifier code or exact certificate data for the interval enclosures. |
| Current status ledger | Reference | [`3110_current_status_and_remaining_obligations.md`](3110_current_status_and_remaining_obligations.md) | Tracks remaining open tasks. |

## Assembly Target

The intended proof must combine:

| Input | Current status |
|---|---|
| Fixed $V_4$ points from the strict $AB$-union frontier | Strict line-piece branch proved for $\rho<1$; boundary $\rho=1$ open. |
| Three algorithm-2 diagonal points | Two-variable construction proved under equality assumptions; containment in the relaxed obstruction region open. |
| Near-limit treatment | Algorithm-1 tangent gap proved; finite-$x$ bound open. |
| Away-region treatment | Transition strip has a certificate outline; region $p\ge0.15$ remains open. |
| Full branch reduction | Slack/equality reduction to $a_3+b_3=a_5+b_5=1$ remains open. |

## Transition-Strip Target

The transition strip is organized in the variables

$$
p=1-b_4,\qquad q=1-a_4,
$$

with

$$
0.1\le p\le0.15,\qquad p\le q.
$$

The branch transition is

$$
T(p,q)=(p+q)^4-(p+q)^2+pq.
$$

The certificate outline in [`3109_algorithm2_transition_strip_certificate.md`](3109_algorithm2_transition_strip_certificate.md) records the current numerical constants for:

| Edge or branch | Recorded status |
|---|---|
| Dangerous edge $P_3P_5$ | Empirical interval-certificate outline with lower value $1.0031590223\ldots$. |
| Non-dangerous edge $D_0D_1$ | Conditional interval certificate outline. |
| Non-dangerous edge $D_1D_2$ | Conditional interval certificate outline. |
| Non-dangerous edge $D_2P_3$ | Conditional interpolation certificate outline. |
| Non-dangerous edge $P_5D_0$ | Conditional interpolation certificate outline. |

Until verifier data is added, these remain empirical or certificate-outline claims, not proven lemmas.

## Remaining Required Work

| Task | Status |
|---|---|
| Prove or replace the reduction to $a_3+b_3=1$ and $a_5+b_5=1$. | Open. |
| Prove the limiting degeneration at $\rho=1$. | Open. |
| Prove algorithm-2 point containment in the relaxed obstruction region. | Open. |
| Package the transition-strip interval certificate. | Open. |
| Finish $p\ge0.15$ and reflected away regions. | Open. |
| Prove the finite-$x$ algorithm-1 near-limit bound. | Open. |
| Assemble all local components into the CE0, $N_+=1$, all-Vd0 contradiction. | Open. |
