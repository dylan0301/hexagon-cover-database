# Slice-Family Success And Failure Catalog

Status: Experiment

This catalog summarizes the algebraic slice families tested for reducing the
optimized six-point function to the transition curve $T=0$.  It is an
experiment record, not a proof.  The detailed definitions and formulas are in
[`31017_ray_transition_curve_minimum_conjecture.md`](31017_ray_transition_curve_minimum_conjecture.md),
the numerical memo is
[`31018_ray_transition_computation_memo.md`](31018_ray_transition_computation_memo.md),
and the primary constant-difference target is
[`31019_constant_difference_slice_minimum_target.md`](31019_constant_difference_slice_minimum_target.md).

All points are the relaxed six-point points from
[`31011_six_point_construction.md`](31011_six_point_construction.md).

## 1. Status table

The table uses the following conventions.

- `Supported`: no optimized $F_6$ counterexample found in the recorded tests.
- `Restricted`: useful only after a case split or in a restricted angle/support
  window.
- `Failed`: an optimized or fixed-angle counterexample was found.
- `Fixed-angle failure`: the optimized $F_6$ version may still work, but the
  stronger fixed-$\theta$ statement is false.

| Slice family | Transition point | Optimized $F_6$ status | Fixed-angle $G$ status | Recommendation |
|---|---|---|---|---|
| $d=q-p$ | $S_T=\sqrt{(3+\sqrt{9+16d^2})/8}$ | Supported | False globally | Primary global target |
| ray $q=\kappa p$ | $p_T=\sqrt{1+\kappa+\kappa^2}/(1+\kappa)^2$ | Supported | False globally; restricted windows supported | Secondary / fixed-angle restricted use |
| $L=p^2-pq+q^2$ | $S_T=\sqrt{(1+\sqrt{1+3L})/3}$ | Failed near $L=3/16$ | False globally | Use only after small symmetric split |
| $p^2+\lambda pq+q^2$ with $\lambda<0$ | quadratic formula in $S^2$ | Supported in coarse tests | not certified | Promising family; $\lambda=-1$ most geometric but not global |
| $pq=P$ | $S_T=\sqrt{(1+\sqrt{1-4P})/2}$ | Failed near symmetry | not recommended | Do not use globally |
| $S=p+q$ | $d_T=S\sqrt{4S^2-3}$ | Failed strongly | failed | Do not use |
| $p^2+q^2=M$ | $S_T=\sqrt{(1+\sqrt{1+8M})/4}$ | Failed | not recommended | Do not use globally |
| $p^2+pq+q^2=K$ | $S_T=K^{1/4}$ | Failed repeatedly | not recommended | Do not use |

## 2. Primary success candidate: $d=q-p$

For fixed $d$, the transition point is unique and explicit.  No optimized
$F_6$ failure was found in deterministic, random, or refined support-branch
experiments.

The observed transition support patterns were:

| Approximate $d$ range | Support pattern | Contact set |
|---:|---|---|
| $d=0$ | $(D_1),(P_3,D_2),(P_5)$ | $D_1,D_2,P_3,P_5$ |
| $0<d\lesssim0.0648$ | $(D_1),(P_3),(P_5,D_0)$ | $D_0,D_1,P_3,P_5$ |
| $0.0648\lesssim d\lesssim0.1005$ | $(D_2),(P_3),(P_5,D_0)$ | $D_0,D_2,P_3,P_5$ |
| $0.1005\lesssim d\lesssim0.545$ | $(D_1),(P_3,D_2),(P_5)$ | $D_1,D_2,P_3,P_5$ |
| $0.545\lesssim d<1$ | $(D_0),(D_2),(P_4,P_5)$ | $D_0,D_2,P_4,P_5$ |

The last branch is the near-limit branch already suggested by the limit
figures.

## 3. Ray slice status

Ray slices have the explicit transition formula

$$
p_T(\kappa)=
\frac{\sqrt{1+\kappa+\kappa^2}}{(1+\kappa)^2},
\qquad
q_T(\kappa)=\kappa p_T(\kappa).
$$

They are useful for fixed-angle dangerous windows, but the unrestricted
fixed-angle statement is false.  A recorded failure uses

$$
E=S_A,
\qquad
\kappa=7.98126139754881,
\qquad
\theta=7.5^\circ.
$$

The ray minimum occurs away from $T=0$, although both values are above $1$.

## 4. Local-metric slice status

The local-metric slice

$$
L=p^2-pq+q^2
$$

has attractive algebra and matches the local metric

$$
Q(u,v)=u^2+v^2-uv.
$$

However, the global optimized statement is false near the symmetric endpoint.
A recorded counterexample is

$$
L=0.187501.
$$

At $T=0$,

$$
F_6=1.0061352609784366,
$$

while another point on the same $L$-slice has

$$
F_6=1.0061151665458956.
$$

The contact pattern is the same at both points:

$$
(D_1),(P_3),(P_5,D_0).
$$

Thus the failure is a same-support-branch failure, not a support-change effect.
The slice may still be useful after splitting off a tiny interval near
$L=3/16$.

## 5. Negative and nonnegative quadratic slices

For

$$
Q_\lambda=p^2+\lambda pq+q^2,
$$

coarse tests found no failures for

$$
\lambda=-3,-2,-1.5,-1,-0.5,-0.25,-0.1,
$$

but failures for

$$
\lambda=0,0.1,0.25,0.5,1,1.5.
$$

The transition point is algebraically simple for all fixed $\lambda<2$, but
no member of this family is currently proven.

## 6. Failed algebraic slices

### Constant product

The product slice $pq=P$ failed near the symmetric regime.  The failure involved
a different lower contact branch away from $T=0$.

### Constant sum

The sum slice $S=p+q$ failed strongly.  In one test at $S=0.93$, the transition
value was about $1.031581$, while another point on the slice had value about
$1.017420$.

### Euclidean quadratic

The slice $p^2+q^2=M$ had small but genuine failures.

### Plus quadratic

The slice $p^2+pq+q^2=K$ failed repeatedly.  This is important because the plus
form appears in the admissible-set condition, but it is not aligned with the
relaxed line-circle geometry of the selected $P$ points.

## 7. Contact-change conclusion

The experiments do not support the literal statement that contacts always
change at $T=0$.  In many successful constant-difference slices, the same
contact pattern persists through a neighborhood of $T=0$.

The working interpretation is:

$$
T=0
$$

is a diagonal-radius balance point inside a low support branch.  The branch
change of $c_*$ can create a derivative cusp even when the contact set is
unchanged.

## 8. Recommended proof direction

The recommended proof direction is:

1. use constant-difference slices $d=q-p$;
2. reduce $F_d(S)$ to finite support-tie branches;
3. certify the four observed support regimes;
4. handle $d=0$ and $d\to1$ as endpoint degeneracies;
5. use the local-metric slice only as a backup after excluding the small
   symmetric failure interval.
