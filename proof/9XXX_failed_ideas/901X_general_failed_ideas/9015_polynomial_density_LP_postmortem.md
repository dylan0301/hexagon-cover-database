# Polynomial Density LP Postmortem

Status: Failed

A historical approach represented edge and diagonal weights as polynomial densities. Triangle constraints were integrals of these densities over covered intervals.

Problems:

- sampled nonnegativity was not a rigorous continuous condition;
- discrete interval approximation was wrong for continuous constraints;
- visualization showed validation concerns;
- the method was superseded by the P-value CDF formulation.

Do not use this as the current proof model.
