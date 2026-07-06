# Ray-Slice Transition Computation Memo

Status: Experiment

This memo records numerical tests for the ray-slice transition target from
[`31017_ray_transition_curve_minimum_conjecture.md`](31017_ray_transition_curve_minimum_conjecture.md).
The computations are empirical and are not a certificate.  In particular, no
interval boxes, outward-rounded arithmetic, or machine-checkable verifier are
recorded here.

The computations in this memo use the relaxed six-point construction from
[`31011_six_point_construction.md`](31011_six_point_construction.md).  The
points denoted $P_3$ and $P_5$ below are
$P_3^{\mathrm{rel}}$ and $P_5^{\mathrm{rel}}$, obtained from the relaxed centers
$X_2^{\mathrm{rel}}(b)$ and $X_5^{\mathrm{rel}}(a)$.  They are not the older
five-point actual-center points.

## 1. Tested functions

The fixed-angle function was

$$
G_E(a,b,\theta)=
\frac2{\sqrt3}\sum_{j=0}^2
\max_{P\in E} n_j(\theta)\cdot P.
$$

The tested subsets were

$$
S_A=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_0,D_2\},
$$

$$
S_C=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_1,D_2\},
$$

and

$$
S_D=\{P_3^{\mathrm{rel}},P_5^{\mathrm{rel}},D_1\}.
$$

The full six-point set

$$
K_6^{\mathrm{rel}}=
\{P_3^{\mathrm{rel}},P_4,P_5^{\mathrm{rel}},D_0,D_1,D_2\}
$$

was also tested.

The ray coordinate was

$$
q=\kappa p,
\qquad
1\le\kappa\le8.518281505052565\ldots .
$$

The transition point was inserted explicitly in every sampled ray:

$$
p_T(\kappa)=
\frac{\sqrt{1+\kappa+\kappa^2}}{(1+\kappa)^2}.
$$

## 2. Numerical protocol

For each sampled pair $(\kappa,\theta)$, the computation sampled the admissible
ray interval in $p$, inserted $p_T(\kappa)$ exactly, and compared

$$
G_E(p_T(\kappa),\kappa p_T(\kappa),\theta)
$$

against the smallest sampled value along the ray.

The deterministic test used:

- $15$ equally spaced $\kappa$ values in $[1,8.518281505052565\ldots]$;
- the special values $\kappa=1$, $\kappa=2.06369311056$, and
  $\kappa=8.518281505052565\ldots$;
- angle grids in the relevant ranges, including the previously observed
  critical angles $22.4415575848^\circ$, $31.9567137616^\circ$, and
  $36^\circ$;
- $161$ $p$-samples per ray, with $p_T$ inserted separately.

Selected rows were then refined by one-dimensional scalar minimization with
absolute tolerance about $10^{-14}$.

## 3. Deterministic grid summary

The table records whether the ray minimum was found at the transition point, up
to a tolerance of $5\cdot10^{-5}$ in side length.

| Function/window | Rows | Failures | Rows with value $<1.02$ | Near-critical failures | Smallest transition value |
|---|---:|---:|---:|---:|---:|
| $G_{K_6^{\mathrm{rel}}}$, $0^\circ\le\theta\le60^\circ$ | $448$ | $16$ | $15$ | $0$ | $1.006152417887511$ |
| $G_{S_A}$, $0^\circ\le\theta\le30^\circ$ | $416$ | $29$ | $24$ | $0$ | $1.0051622245921823$ |
| $G_{S_A}$, $18^\circ\le\theta\le26^\circ$ | $416$ | $0$ | $68$ | $0$ | $1.0051622245921823$ |
| $G_{S_C}$, $30^\circ\le\theta\le36^\circ$ | $416$ | $0$ | $21$ | $0$ | $1.006152417887511$ |
| $G_{S_D}$, $36^\circ\le\theta\le60^\circ$ | $400$ | $0$ | $5$ | $0$ | $1.0110161712095387$ |
| $G_{S_D}$, $36^\circ\le\theta\le40^\circ$ | $400$ | $0$ | $18$ | $0$ | $1.0110161712095387$ |

The strong all-angle assertion that every ray minimum occurs at $T=0$ is
therefore numerically false.  The failures occurred away from the dangerous
near-$1$ region.  No failure was found in the restricted dangerous windows used
by the proposed proof strategy.

## 4. Refined transition minima

The refined transition-curve minima were:

| Function | Window | Value | $\kappa$ | $p_T$ | $q_T$ | $\theta$ | Supports |
|---|---:|---:|---:|---:|---:|---:|---|
| $G_{S_A}$ | $18^\circ\le\theta\le26^\circ$ | $1.0051622245921823$ | $8.518281505052565$ | $0.1000000000$ | $0.8518281505$ | $22.4415575848^\circ$ | $(D_0),(D_2),(P_3,P_5)$ |
| $G_{S_C}$ | $30^\circ\le\theta\le36^\circ$ | $1.006152417887511$ | $1$ | $0.4330127019$ | $0.4330127019$ | $31.9567137616^\circ$ | $(D_1),(D_2),(P_5)$ |
| $G_{S_D}$ | $36^\circ\le\theta\le40^\circ$ | $1.0110161712095387$ | $2.06369311056$ | $0.2882968077$ | $0.5949561358$ | $36^\circ$ | $(D_1),(P_3),(P_5)$ |

All three transition minima remain above $1$ with margin at least

$$
0.0051622245921823\ldots .
$$

## 5. Refined counterexample to the strong all-angle form

The following row refutes the unrestricted claim that the transition point is
always the ray minimum for fixed-angle $G_E$.

For

$$
E=S_A,
\qquad
\kappa=7.98126139754881,
\qquad
\theta=7.5^\circ,
$$

one-dimensional refinement gives

$$
p_{\min}=0.1026558454521663,
$$

where

$$
G_{S_A}(p_{\min},\kappa p_{\min},\theta)
=1.0901376449036617.
$$

The transition point is

$$
p_T=0.1056910344698915,
$$

and

$$
G_{S_A}(p_T,\kappa p_T,
\theta)=1.096341223913082.
$$

Thus

$$
G_{S_A}(p_T,\kappa p_T,\theta)-
G_{S_A}(p_{\min},\kappa p_{\min},\theta)
=0.006203579009420368\ldots >0.
$$

The same row also gives the same failure for the full six-point function,
because the active supports are

$$
(P_5),(D_2),(P_3),
$$

and the extra points do not change the support values at that angle.

This failure is harmless for the current proof strategy because the lower bound
is already far above $1$.

## 6. Interpretation

The computations support the following conclusions.

1. The unrestricted all-angle ray-minimum principle is false.
2. The restricted dangerous-window ray-minimum principle remains consistent
   with all tests recorded here.
3. The transition curve $T=0$ still appears to capture the true worst part of
   the far-from-limit fixed-angle proof.
4. The proof should therefore use ray monotonicity only in the dangerous windows
   from `31017`, and use simpler coarse lower bounds in the remaining angle
   ranges.

## 7. Certificate requirements

To convert this memo into a proof-level result, one still needs:

1. a recorded implementation of the relaxed point construction;
2. interval boxes for $(\kappa,p,\theta)$ in each support regime;
3. outward-rounded interval evaluation of the relevant support inequalities;
4. separate selected-root checks for $P_3^{\mathrm{rel}}$ and
   $P_5^{\mathrm{rel}}$;
5. a transition-curve certificate proving the three lower bounds in Section 4;
6. coarse certificates for the non-dangerous angle windows.

Until those items are recorded, the present note remains an experiment memo.
