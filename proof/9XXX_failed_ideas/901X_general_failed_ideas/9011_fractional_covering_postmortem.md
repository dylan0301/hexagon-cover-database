# Fractional Covering Postmortem

Status: Failed

Attempted goal:

$$
\text{Find a weighting on a skeleton of size }1+\epsilon \text{ such that every unit triangle contains weight at most }1.
$$

The broader LP direction evolved through discrete point weights and prefix sums. Current implementation uses P-value cumulative functions instead of ordinary discrete point weights.

This older fractional-covering intuition is kept for history but is not the current proof model.
