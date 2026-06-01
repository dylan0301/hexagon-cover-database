# Dominance Weighting Postmortem

Status: Failed

The goal was to find a weighting on the skeleton such that each unit triangle has weight at most $1$, while the target has total weight greater than $7$.

Densities:

$$
e,c,v:[0,1/2]\to\mathbb R.
$$

Cumulative functions:

$$
E(t)=\int_0^t e(s)\,ds, \quad C(t)=\int_0^t c(s)\,ds, \quad V(t)=\int_0^t v(s)\,ds.
$$

A hyperparameter $\lambda$ was intended to make one side dominate another, e.g. $E_\lambda(a)\gg E_\lambda(b)$ for $a>b$.

Failure: the necessary inequality chains among $E,C,V$ contradict each other. A version using only $C,V$ appears to reduce back to the full $E,C,V$ dominance problem.
