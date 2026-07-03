# Far-From-Tight Algorithm-2 Status

Status: Reference

This file records the current far-from-tight status for the CE0, $N_+=1$, all-Vd0 five-point route.

## Variables

Use the algorithm-2 variables

$$
p=1-b_4,\qquad q=1-a_4.
$$

In the lower symmetric half, take

$$
p\le q.
$$

The strict $V_4$ branch is

$$
(1-p)^2+(1-p)(1-q)+(1-q)^2<1,
$$

and the supercritical condition is

$$
p+q<1.
$$

The away-from-limit cutoff currently used in this package is

$$
p\ge0.1,\qquad q\ge0.1.
$$

## Proved Inputs

The strict branch-realization file proves that, in the strict $\rho<1$ branch, the two selected fixed points lie on the line pieces

$$
P_3\in\Gamma_A^{\mathrm{lin}},\qquad P_5\in\Gamma_B^{\mathrm{lin}}.
$$

The two-variable model file proves that, under the equality assumptions

$$
a_3+b_3=1,\qquad a_5+b_5=1,
$$

algorithm 2 depends only on $(p,q)$ and uses one common diagonal coordinate

$$
c_*=c_{\max}(p,q).
$$

For $p\le q$, the branch transition is

$$
T(p,q)=(p+q)^4-(p+q)^2+pq.
$$

The mixed and quartic branches are

$$
T\ge0:\quad c_*=\frac{2q}{1+\sqrt{4(p+q)^2-3}},
$$

and

$$
T\le0:\quad c_*^4-c_*^2+pc_*-p^2=0,\qquad c_*\ge p+q.
$$

The same file proves that

$$
r=1-c_*
$$

is nondecreasing in both $p$ and $q$.

The convex-order file proves that line realization implies the cyclic convex order

$$
D_0,D_1,D_2,P_3,P_5.
$$

Thus, under algorithm 2 and strict line realization, only the five hull-edge support pairs remain.

## Transition Strip Certificate Outline

The file [`3119_algorithm2_transition_strip_certificate.md`](3119_algorithm2_transition_strip_certificate.md) records a certificate outline on

$$
0.1\le p\le0.15.
$$

It includes:

| Part | Recorded status | Notes |
|---|---|---|
| Dangerous edge $P_3P_5$ | Empirical / certificate outline | Envelope with base value $1.0031590223\ldots$. |
| Edges $D_0D_1$ and $D_1D_2$ | Empirical / certificate outline | Lower-bound formulas recorded. |
| Edges $D_2P_3$ and $P_5D_0$ | Empirical / certificate outline | Denominator-free $G_{23}$ and $G_{40}^{(2)}$ interpolation constants recorded. |

This is not yet a proof-level certificate because the terminal interval boxes, verifier code, and selected-root branch checks are not recorded in the repository.

## Remaining Far-From-Tight Obligations

| Obligation | Status |
|---|---|
| Upgrade the transition-strip outline to a reproducible certificate. | Open. |
| Prove the farther region $p\ge0.15$ and its reflection. | Open. |
| Treat the strict-curve limiting boundary $\rho=1$. | Open. |
| Assemble the far-from-tight proof with the close-to-tight proof. | Open. |
