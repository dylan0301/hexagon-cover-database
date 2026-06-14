# Proof Tree for the CE0 Area Certificate

Status: Reference

This file records the proof-tree structure for the CE0 conditional area
certificate.

## CE0 proof tree

```text
Input assumptions:
  T_C is CE0
  N_+ >= 2

Six-point perimeter data:
  one ordinary cut point on each edge: x_0,...,x_5

Induced rows:
  (a_i,b_i) = (1-x_{i-1},x_i), i=0,...,5

Local area bounds:
  prove or certify the local square-loss inputs
    a+b <= 1  =>  f(a,b) <= 1 - min(a,b)^2
    a+b >  1  =>  f(a,b) <= 1 - max(a,b)^2
  supercritical input is supplied by 3204 if the structural hypothesis holds

Analytic certificate:
  apply 3208_CE0_conditional_area_certificate.md

Conclusion under these local bounds:
  if at least two rows satisfy a_i+b_i>1, then
    sum_i f(a_i,b_i) < 99/20 < 5

Area contradiction:
  the six vertex triangles contribute less than five unit-triangle areas
  the center triangle contributes at most one unit-triangle area
  the seven unit triangles then contribute less than area(H)
  so they cannot cover H
```

## Required local input

The remaining local input is the square-loss hypothesis for the local area
function $f(a,b)$:

$$
a+b\le1 \quad\Longrightarrow\quad f(a,b)\le1-\min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad f(a,b)\le1-\max(a,b)^2.
$$

The supercritical implication is proved in
[`3204_supercritical_vertex_loss_lemma.md`](3204_supercritical_vertex_loss_lemma.md)
(Status: Proven analytic inequality), conditional on the supercritical
structural hypothesis for $T(a,b)$.  The subcritical implication and that
structural hypothesis remain open unless separately proved or certified.

The conditional analytic step itself is recorded in
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
(Status: Proven analytic inequality).
