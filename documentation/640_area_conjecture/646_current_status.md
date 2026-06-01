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
| CE1 seven-point perimeter model | Strategy |
| CE2 seven-point model after one-interval reduction | Strategy, conditional |
| Pointwise threshold bound $f(a_i,b_i)\le f(a_i,1+\varepsilon-a_i)$ | Strategy |
| Global replacement formulation $a_i+b_i=1+\varepsilon$ | Strategy / unchecked |
| Proof-tree structure | Reference |

## Conditional CE0 result now recorded

The file `647_CE0_conditional_area_certificate.md` proves the following
conditional analytic inequality.

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
\#\{i:a_i+b_i>1\}\ge2 \quad\Longrightarrow\quad \sum_{i=0}^5 f(a_i,b_i)<\frac{99}{20}<5.
$$

Thus the final CE0 area inequality is no longer an independent open obligation
once these local square-loss bounds are supplied.

## Open obligations

The package does not yet supply:

- a proof of the structural conjecture for $T(a,b)$;
- a sharp formula or certified upper bound for $f(a,b)$;
- a proof of the local square-loss bounds needed by
  `647_CE0_conditional_area_certificate.md`;
- a proof of the CE2 one-interval lemma;
- a complete pointwise threshold-bound reduction, including the boundary
  regime $1<a_i+b_i<1+\varepsilon$, for routes that still use threshold
  relaxation;
- a decision about whether the older global replacement formulation can be
  made into a valid CE0 six-point or CE1/reduced-CE2 seven-point cut-point map;
- a certified proof of

  $$
  \sum_{i=0}^5 f(a_i,b_i)<5
  $$

  in the CE1/reduced-CE2 seven-point extension whenever at least two rows
  satisfy $a_i+b_i>1$.

## Relation to existing packages

The CE1/CE2 boundary-loss package in `../550_CE_Vd0_boundary_loss/` proves a
different perimeter-length reduction under all-Vd0 assumptions.  This folder
records a separate area-based route.

The May 25 package in `../630_may25_five_point_conjecture/` studies a
finite-point obstruction.  This folder instead studies an area upper bound for
the six vertex triangles, first under CE0 six-point perimeter data and
separately under CE1 or reduced CE2 seven-point perimeter data.  The center
triangle is then bounded only by the trivial fact that a unit equilateral
triangle contributes at most one normalized area unit.

## Status warning

The CE0 theorem in `647_CE0_conditional_area_certificate.md` should be cited as
conditional on the local square-loss bounds.  It should not be cited as an
unconditional proof of the CE0 area case until those local bounds are proved or
certified.

Numerical evidence for the area conjecture or for the local structural
maximizers should be recorded as empirical unless a certificate is supplied.
