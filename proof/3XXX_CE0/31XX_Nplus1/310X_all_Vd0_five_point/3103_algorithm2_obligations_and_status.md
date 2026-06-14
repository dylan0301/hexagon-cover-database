# Algorithm-2 Obligations And Status

Status: Reference

The intended final implication for this folder is:

$$
T_C\text{ is CE0},\quad N_+=1,\quad\text{all }T_i\text{ are Vd0}\quad\Longrightarrow\quad\text{finite-point obstruction}.
$$

The assembly must combine:

- the fixed points from the $V_4$ strict $AB$-union frontier;
- the three algorithm-2 diagonal points;
- the limit-shape convexity proof outside the central parameter region;
- the interior finite certificate inside the central parameter region.

This file is not a proof. It records the dependency structure and current
obligations for the intended proof.

## Status Table

| Component | Recorded status | Obligation |
|---|---|---|
| Algorithm-2 setup and point construction | Empirical strategy | Define the relaxed obstruction region exactly and prove point containment for all allowed parameters. |
| Limit-shape convexity target | Lemma target | Prove convexity outside the central parameter region after fixing exact parameter ranges and active support regimes. |
| Interior box certificate target | Empirical | Replace numerical success inside the central parameter box by a finite certified cover. |
| Algorithm-2 assembly target | Lemma target | Combine point construction, limit-shape convexity, and interior certificate into the branch obstruction. |

## Limit-Shape Convexity Target

The sketch suggests that when either $a_4$ or $b_4$ lies outside the interval

$$
[0.1,0.9],
$$

the algorithm-2 enclosing-side function behaves like a limit-shape problem and
is convex in the remaining free variable. The intended reason is that the
orientation of the minimum enclosing triangle appears not to change in this
region.

A proof of this target must:

- state the exact parameter ranges replacing the empirical decimal bounds if
  sharper rational or algebraic bounds are needed;
- identify the active support pattern of the minimum enclosing triangle;
- prove the orientation does not change on the whole region;
- prove the resulting one-variable convexity inequality.

Until such a proof is recorded, this remains a lemma target.

## Interior Box Certificate Target

For the region where

$$
a_4,b_4\in[0.1,0.9],
$$

the sketch reports numerical success for algorithm 2 after splitting into
parameter subcases.

To become proof-level, this route needs a finite certificate covering the full
interior parameter region. The certificate should include:

- exact parameter boxes;
- branch-realization conditions for the selected fixed points;
- containment of the algorithm-2 diagonal points in the relaxed region;
- certified lower bound for the minimum enclosing equilateral triangle side
  length;
- endpoint and boundary-case treatment.

Until the certificate is recorded, this is empirical support only.
