# Current Status of the Area Conjecture Package

Status: Reference

## Recorded in this package

| Item | Status |
|---|---|
| Local function $f(a,b)$ | Definition / strategy |
| Symmetry $f(a,b)=f(b,a)$ | Definition / direct symmetry |
| Monotonicity of $f(a,b)$ under coordinate increase | Lemma target |
| Structural description of $T(a,b)$ | Conjectural strategy |
| Local square-loss bounds for $f(a,b)$ | Lemma target |
| CE0 six-point perimeter model | Main strategy |
| Conditional CE0 final inequality under local square-loss bounds | Proven analytic inequality |
| CE0 proof-tree structure | Reference |

## Conditional CE0 result now recorded

The file
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
proves the following conditional analytic inequality.

Assume the local square-loss bounds

$$
a+b\le1 \quad\Longrightarrow\quad f(a,b)\le1-\min(a,b)^2,
$$

and

$$
a+b>1 \quad\Longrightarrow\quad f(a,b)\le1-\max(a,b)^2.
$$

Then, in the CE0 six-point model,

$$
\left\lvert \left\lbrace\, i : a_i+b_i>1 \,\right\rbrace \right\rvert\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}<5.
$$

Thus the final CE0 area inequality is no longer an independent open obligation
once these local square-loss bounds are supplied.

## Open obligations

The package does not yet supply:

- a proof of the structural conjecture for $T(a,b)$;
- a sharp formula or certified upper bound for $f(a,b)$;
- a proof of the local square-loss bounds stated in
  [`3202_area_function_and_monotonicity.md`](3202_area_function_and_monotonicity.md).

## Relation to existing packages

The archived May 25 package in
[`../../9XXX_failed_ideas/963X_may25_five_point_failure/9631_CE0_may25_supremum_endpoint_archive.md`](../../9XXX_failed_ideas/963X_may25_five_point_failure/9631_CE0_may25_supremum_endpoint_archive.md)
studies a finite-point obstruction.  This folder instead studies an area upper bound for
the six vertex triangles under CE0 six-point perimeter data.  The center
triangle is then bounded only by the trivial fact that a unit equilateral
triangle contributes at most one normalized area unit.

## Status warning

The CE0 theorem in
[`3208_CE0_conditional_area_certificate.md`](3208_CE0_conditional_area_certificate.md)
should be cited as conditional on the local square-loss bounds.  It should not
be cited as an unconditional proof of the CE0 area case until those local
bounds are proved or certified.

Numerical evidence for the area conjecture or for the local structural
maximizers should be recorded as empirical unless a certificate is supplied.
