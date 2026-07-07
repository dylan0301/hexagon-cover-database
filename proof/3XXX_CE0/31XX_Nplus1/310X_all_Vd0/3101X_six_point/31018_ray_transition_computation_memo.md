# Algebraic Slice Computation Memo

Status: Experiment

This memo records numerical tests for the algebraic slice targets in
[`31017_ray_transition_curve_minimum_conjecture.md`](31017_ray_transition_curve_minimum_conjecture.md)
and [`31019_constant_difference_slice_minimum_target.md`](31019_constant_difference_slice_minimum_target.md).
The file name is historical; this is no longer only a ray-slice memo.

The computations are empirical.  No interval boxes, outward-rounded arithmetic,
or machine-checkable verifier are recorded here.  The numerical statements in
this file must not be cited as proof.

All computations use the relaxed six-point construction from
[`31011_six_point_construction.md`](31011_six_point_construction.md).  The
points denoted $P_3$ and $P_5$ below are
$P_3^{\mathrm{rel}}$ and $P_5^{\mathrm{rel}}$, obtained from the relaxed centers
$X_2^{\mathrm{rel}}(b)$ and $X_5^{\mathrm{rel}}(a)$.  They are not the older
five-point actual-center points.

## 1. Tested functions

The fixed-angle function is

$$
G_E(a,b,\theta)=
\frac2{\sqrt3}\sum_{j=0}^2
\max_{P\in E}n_j(\theta)\cdot P.
$$

The optimized six-point value is

$$
F_6(a,b)=
\inf_\theta G_{K_6^{\mathrm{rel}}}(a,b,\theta),
$$

where

$$
K_6^{\mathrm{rel}}=
\{P_3^{\mathrm{rel}},P_4,P_5^{\mathrm{rel}},D_0,D_1,D_2\}
$$

with $P_4$ redundant on $\rho=1$ by the boundary collinearity recorded in
`31011`.

The experiments also used selected subsets

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

## 2. Optimization protocol

The optimized value $F_6$ was evaluated by enumerating support-tie angles.  For
fixed $(p,q)$ and finite point set $E$, candidate angles satisfy

$$
(P-Q)\cdot n_j(\theta)=0
$$

for two points $P,Q\in E$ and one of the three normals.  This follows from the
support-cell observation in `31016`.

For each slice family, the experiment inserted the explicit $T=0$ point into
the sampled slice, evaluated $F_6$ there, and compared it against sampled or
refined minima on the same slice.  Some rows were refined by scalar
one-dimensional minimization along the slice.

## 3. Constant-difference slices

The primary slice is

$$
d=q-p.
$$

The transition point is

$$
S_T(d)=
\sqrt{\frac{3+\sqrt{9+16d^2}}8},
\qquad
p_T=\frac{S_T-d}{2},
\qquad
q_T=\frac{S_T+d}{2}.
$$

### Empirical result

No optimized $F_6$ counterexample was found.

Test batches included:

- deterministic scans through representative $d$ values from $0$ to near $1$;
- random-refined scans with many $d$ values concentrated near $d=1$;
- support-branch gap scans around $S_T(d)$.

A representative random-refined batch had $120$ tested $d$ values and no
failure.  Near-limit rows with $d$ very close to $1$ had values numerically
approaching $1$ from above and still minimized at the transition point within
precision.

The transition support regimes observed along the $T=0$ curve were:

| Approximate $d$ range | Support pattern |
|---:|---|
| $d=0$ | $(D_1),(P_3,D_2),(P_5)$ |
| $0<d\lesssim0.0648$ | $(D_1),(P_3),(P_5,D_0)$ |
| $0.0648\lesssim d\lesssim0.1005$ | $(D_2),(P_3),(P_5,D_0)$ |
| $0.1005\lesssim d\lesssim0.545$ | $(D_1),(P_3,D_2),(P_5)$ |
| $0.545\lesssim d\lesssim1$ | $(D_0),(D_2),(P_4,P_5)$ |
| $d\to1$ | diagonal-point degeneracies together with $(D_2),(P_4,P_5)$ |

The important near-limit contact set is

$$
D_0,D_2,P_4,P_5.
$$

## 4. Ray slices

The ray slice is

$$
q=\kappa p.
$$

The transition point is

$$
p_T(\kappa)=
\frac{\sqrt{1+\kappa+\kappa^2}}{(1+\kappa)^2},
\qquad
q_T(\kappa)=\kappa p_T(\kappa).
$$

### Empirical result

For optimized $F_6$, ray slices behaved similarly to constant-difference
slices in the tested rows.  No optimized $F_6$ counterexample was found in the
main ray batches.

For fixed-angle $G_E$, the unrestricted all-angle ray statement is false.  A
refined fixed-angle failure was found for

$$
E=S_A,
\qquad
\kappa=7.98126139754881,
\qquad
\theta=7.5^\circ.
$$

The actual ray minimum was

$$
p_{\min}=0.1026558454521663,
$$

with

$$
G_{S_A}(p_{\min},\kappa p_{\min},\theta)
=1.0901376449036617.
$$

The transition point was

$$
p_T=0.1056910344698915,
$$

with

$$
G_{S_A}(p_T,\kappa p_T,\theta)=1.096341223913082.
$$

Thus $T=0$ is not the fixed-angle ray minimum in that row, although both values
are safely above $1$.

No failure was found in the restricted dangerous windows:

$$
S_A,\quad 18^\circ\le\theta\le26^\circ,
$$

$$
S_C,\quad 30^\circ\le\theta\le36^\circ,
$$

and

$$
S_D,\quad 36^\circ\le\theta\le40^\circ.
$$

## 5. Constant local-metric slices

The local-metric slice is

$$
L=p^2-pq+q^2.
$$

The transition point is

$$
S_T(L)=
\sqrt{\frac{1+\sqrt{1+3L}}3},
$$

$$
d_T(L)=\sqrt{\frac{4L-S_T(L)^2}{3}},
$$

and

$$
p_T=\frac{S_T-d_T}{2},
\qquad
q_T=\frac{S_T+d_T}{2}.
$$

### Empirical result

Initial stress tests showed no failure, but refined near-symmetric tests found
that the global $L$-slice minimum statement is false.

A counterexample occurs at

$$
L=0.187501=\frac{3}{16}+10^{-6}.
$$

At $T=0$,

$$
(p_T,q_T)=
(0.43246509479010353,\ 0.4335605399343012),
$$

and

$$
F_6(p_T,q_T)=1.0061352609784366.
$$

On the same $L$-slice, a lower value was found at

$$
(p,q)=
(0.4307608616603753,\ 0.43523222192184163),
$$

with

$$
F_6(p,q)=1.0061151665458956.
$$

The gap is

$$
-2.009443254102905\cdot10^{-5}.
$$

Both points had the same contact pattern

$$
(D_1),(P_3),(P_5,D_0),
$$

so this is a same-support-branch failure, not a contact-change failure.

Further refined rows suggested that the failure is confined to a tiny interval
near $L=3/16$, approximately ending around

$$
L\approx0.187516\text{--}0.187518.
$$

## 6. General quadratic slices

For

$$
Q_\lambda(p,q)=p^2+\lambda pq+q^2,
$$

negative $\lambda$ values behaved better than nonnegative values.

The coarse scan recorded:

| $\lambda$ | Valid rows | Failures | Worst observed gap $F_{\min}-F_T$ |
|---:|---:|---:|---:|
| $-3$ | $7$ | $0$ | $0$ |
| $-2$ | $7$ | $0$ | $0$ |
| $-1.5$ | $7$ | $0$ | $0$ |
| $-1$ | $7$ | $0$ | $0$ |
| $-0.5$ | $7$ | $0$ | $0$ |
| $0$ | $7$ | $1$ | $-6.9\cdot10^{-5}$ |
| $0.5$ | $7$ | $3$ | $-2.006\cdot10^{-3}$ |
| $1$ | $7$ | $4$ | $-4.552\cdot10^{-3}$ |
| $1.5$ | $7$ | $4$ | $-7.673\cdot10^{-3}$ |

A near-zero scan found no failures at $\lambda=-0.25$ and $\lambda=-0.1$, but
failures at $\lambda=0,0.1,0.25$.

These computations suggest that negative-$\lambda$ slices may be viable, but
the special local-metric value $\lambda=-1$ still has the near-symmetric
failure above.

## 7. Product, sum, Euclidean, and plus-metric slices

The following algebraically simple slices are not recommended as global
transition-minimum routes.

### Constant product

For

$$
pq=P,
$$

one has

$$
S_T(P)=\sqrt{\frac{1+\sqrt{1-4P}}2}.
$$

Product slices failed near the symmetric regime.  One refined failure used
approximately

$$
P=0.185508,
$$

where $F_6$ at the slice minimum was below the transition value.

### Constant sum

For

$$
S=p+q,
$$

one has

$$
d_T(S)=S\sqrt{4S^2-3}.
$$

Constant-sum slices failed strongly.  At $S=0.93$, the transition value was
about $1.031581$, while a lower same-slice value about $1.017420$ was found.

### Euclidean quadratic

For

$$
p^2+q^2=M,
$$

one has

$$
S_T(M)=\sqrt{\frac{1+\sqrt{1+8M}}4}.
$$

Euclidean slices had small but genuine failures.

### Plus quadratic

For

$$
p^2+pq+q^2=K,
$$

one has

$$
S_T(K)=K^{1/4}.
$$

This slice failed repeatedly, even though it is related to the admissible-set
quadratic form.  The failure indicates that the plus form is not aligned with
the relaxed line-circle geometry of $P_3^{\mathrm{rel}}$ and
$P_5^{\mathrm{rel}}$.

## 8. Interpretation

The experiments do not support the statement that contact points always change
at $T=0$.  On many successful constant-difference slices, the contact pattern
is stable through a neighborhood of $T=0$.

The better interpretation is:

$$
T=0
$$

is a diagonal-radius balance point inside the correct low support branch.  In
some branches this balance creates a derivative cusp through the change of the
$c_*$ branch, even when the support contacts do not change.

## 9. Certificate requirements

To convert these experiments into proof-level results, one still needs:

1. an interval implementation of the relaxed point construction;
2. outward-rounded interval evaluation for $P_3^{\mathrm{rel}}$ and
   $P_5^{\mathrm{rel}}$ selected-root branches;
3. support-tie branch boxes for the observed transition regimes;
4. a certified comparison

   $$
   B_\alpha(S,d)\ge F_6(p_T(d),q_T(d))
   $$

   for every support branch $B_\alpha$ on the constant-difference slice;
5. special treatment of the endpoint $d\to1$ where diagonal ties degenerate.

Until these data are recorded, the constant-difference slice theorem remains a
lemma target, not a proven result.
