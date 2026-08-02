# Complete Re-Audit of the CE2 Exactly-One-Vd1/Vd2 Placements

Status: Proven

This file re-audits the placement partition after the two-chart repair of
`4147` and the skeleton-level strengthening of `4013`.

## Standing branch

Assume:

- the center role is CE2 and has unique center midpoint $M_0$;
- $N_+=1$;
- exactly one vertex role is Vd1 or Vd2;
- the branch with an additional positive-support vertex role has already been
  removed by `414a`.

Let $T_\sigma$ be the unique supercritical role and $T_\tau$ the unique
Vd1/Vd2 role. They are distinct because Vd1/Vd2 roles have boundary sum
strictly below $1/2$.

Every other vertex role is nonsupercritical Vd0. The partition below is
therefore exhaustive.

## Case 1: $\sigma=0$

The unique supercritical role is based at the center-covered midpoint.

- If $\tau\in\{1,5\}$, the Vd role is adjacent. After reflection this is
  exactly `4144`.
- If $\tau\in\{2,3,4\}$, the Vd role is nonadjacent. This is exactly `4146`.

No other index is possible.

## Case 2: $\tau=0$

The unique Vd role is based at the center-covered midpoint, while
$\sigma\ne0$. The midpoint $M_\sigma$ is missed by the supercritical role and
by the center. A nonsupercritical Vd0 role cannot rescue an adjacent midpoint.
Therefore $T_0$ must rescue $M_\sigma$, and diameter locality forces

$$
\sigma\in\{1,5\}.
$$

- If $T_0$ is Vd2, `4149` gives the neighboring-midpoint perimeter
  contradiction.
- If $T_0$ is Vd1, reflection reduces to `4143`.

## Case 3: $\sigma\ne0$ and $\tau\ne0$

Again $M_\sigma$ is missed by the center and by $T_\sigma$. Every other role
except $T_\tau$ is Vd0 and cannot rescue an adjacent midpoint. Hence
$T_\tau$ contains $M_\sigma$, and diameter locality makes $\tau$ adjacent to
$\sigma$.

- If $T_\tau$ is Vd2, `4149` applies.
- If $T_\tau$ is Vd1, the pair is away from the center-midpoint role. Its
  shared edge is center-free. The no-additional-support complement gives all
  remaining hypotheses of the corrected two-chart replacement `4147`.
  That theorem preserves full skeleton coverage and produces six
  nonsupercritical Vd0 roles. The skeleton-level theorem `4013` gives the
  contradiction.

## Positive-support complement

If any role in addition to the unique Vd role has positive adjacent-arm
support, then the unique supercritical role, the Vd role, and that additional
role are three distinct short roles. The skeleton trace theorem `414a` gives
the contradiction.

## Audit conclusion

The positive-support complement and Cases 1--3 are pairwise disjoint and
exhaust all relative positions of $T_0,T_\sigma,T_\tau$. Each terminal is
proved under exactly the hypotheses supplied by its placement:

| placement | terminal | audited interface |
|---|---|---|
| $\sigma=0$, adjacent Vd | `4144` | exact residuals and two radial-bridge exclusions |
| $\sigma=0$, nonadjacent Vd | `4146` | Vd-specific radial separation |
| $\tau=0$, Vd2 rescue | `4149` | neighboring-midpoint perimeter cap |
| $\tau=0$, Vd1 rescue | `4143` | local Vd1 profile and center-free path budget |
| neither special role at $0$, Vd2 | `4149` | neighboring-midpoint perimeter cap |
| neither special role at $0$, Vd1 | `4147` + `4013` | two correct vertex charts, full skeleton preservation, skeleton obstruction |
| additional positive-support role | `414a` | three-short-role skeleton budget |

Thus the CE2, $N_+=1$, exactly-one-Vd1/Vd2 branch is closed.

$$
\Box
$$
