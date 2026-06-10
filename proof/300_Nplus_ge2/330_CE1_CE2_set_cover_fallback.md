# CE1/CE2 Set-Cover Fallback

Status: Strategy

The existing set-cover strategy for

$$
T_C\text{ is CE1 or CE2},\qquad N_+\ge2
$$

is recorded in
[`600_case_strategies/616_CE1_CE2_two_supercritical_set_cover_strategy.md`](../600_case_strategies/616_CE1_CE2_two_supercritical_set_cover_strategy.md).

This fallback remains useful if the skeleton-length route does not close every
CE1/CE2 subbranch.

Any proof-level set-cover certificate must include exact or interval-certified
coverage masks, a dominance certificate for the continuous triangle families,
the infeasibility certificate, and separate boundary-degeneracy treatment.
