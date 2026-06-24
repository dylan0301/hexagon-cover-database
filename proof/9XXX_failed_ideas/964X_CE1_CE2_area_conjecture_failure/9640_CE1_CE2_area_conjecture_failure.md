# CE1/CE2 Area-Conjecture Route Failure

Status: Failed

This note records the failure of the attempted CE1/reduced-CE2 extension of the
CE0 area-conjecture route.

The failed route tried to use the seven-point perimeter model archived in
[`9641_CE1_CE2_seven_point_area_model.md`](9641_CE1_CE2_seven_point_area_model.md)
to prove, for CE1 or reduced CE2 configurations,

$$
\left\lvert \left\lbrace i : a_i+b_i>1 \right\rbrace \right\rvert\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<5.
$$

That CE1/reduced-CE2 area inequality is not a recorded proof route.  The CE0
conditional certificate in
[`../../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md`](../../3XXX_CE0/32XX_Nplus_ge2/3208_CE0_conditional_area_certificate.md)
uses the CE0 six-point relation

$$
(a_i,b_i)=(1-x_{i-1},x_i),
$$

and does not extend to the CE1/reduced-CE2 seven-point model.

## Reasons not to use this route

- The CE1/reduced-CE2 seven-point inequality above is not certified.
- The CE2 use of the seven-point model depends on the unproved CE2
  one-interval reduction.
- The threshold-relaxation and global-replacement formulations in
  [`9642_threshold_relaxation_failure.md`](9642_threshold_relaxation_failure.md)
  remain unchecked for CE1/reduced-CE2 data.

## Current replacement routes

For CE1/CE2 with $N_+\ge2$, use the skeleton-length route:

- [`../../4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md`](../../4XXX_CE1CE2/42XX_Nplus_ge2/4200_CE1_CE2_skeleton_length_route.md)

## Non-claims

This file does not record a certified counterexample to the CE1/reduced-CE2
area inequality.  It also does not close any CE1 or CE2 branch.  It records only
that the CE1/reduced-CE2 area-conjecture extension should not be used as a live
proof route unless a new certified argument is supplied.
