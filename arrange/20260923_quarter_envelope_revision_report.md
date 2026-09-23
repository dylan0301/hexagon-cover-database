# Quarter-range envelope and factored rescuer ratios: implementation report

## Revision and scope

Repository: `dylan0301/hexagon-cover-database`
Baseline: `c7373742f8975d24a18456f458c8e1208a9b454b`
Delivery branch: `chatgpt/quarter-envelope-simplification-20260923045806`
Date: 23 September 2026

This revision implements the approved next-target drafts. It changes the
calculation inside the existing BC, D, and F interfaces, synchronizes both
manuscript editions and the numbered proof sources, and updates the dependency
graph and regression tests. It does not change the main theorem, the witness
counts 5/4/9, or the exact BC/D/F witness definitions. No merge to `main` is part
of this delivery. The final publication identifiers and CI outcomes belong in
the exported delivery record, which extends this source-level report.

## 1. Measured manuscript changes

| Measure | Baseline | Revised clean local build |
|---|---:|---:|
| Canonical pages | 70 | 67 |
| Inline-proof pages | 68 | 65 |
| Canonical extracted text characters | 144,847 | 141,999 |
| Inline extracted text characters | 135,132 | 132,289 |
| Canonical formal statements | 88 | 89 |
| Inline formal statements / immediate proofs | 78 | 79 |
| Complete canonical proof bodies matched to inline | 76 | 77 |

These are measurements, not estimates. The one additional statement is the
strict own-ray lemma reused in F; there is no claim of reducing the number of
formal results. The same ten remaining canonical-to-inline merges are retained.
Fonts, margins, page size, both main preambles, and figure scale are unchanged.
The canonical CI guard is shifted from 68--72 to 65--69 after measuring 67 pages;
its width and the other publication checks are unchanged. Publication builds
repeat the checks in pinned TeX Live 2025; the exported record reports their
actual outcome and final counts.

## 2. Shared quadratic deficit bound

The exact own-ray deficit remains `f(a,b)=1-c_max(a,b)`. For
`m=min(a,b)`, the local capacity comparison still gives `f(a,b)>=ell(m)`, where
`c=1-ell(m)` is the selected root in `[sqrt(3)/2,1]` of
`F(c,m)=c^4-c^2+mc-m^2=0`.

The previous expanded substitution certificate for `q(m)=m(1-m)/2` is replaced by

$$
\ell c^2(1+c)=m(c-m),
$$
$$
2(c-m)-(1-m)c^2(1+c)
=(1-c)((1-m)c(c+2)-2m)\ge0.
$$

The bracket is at least `1/32` on `0<=m<=1/2`. Division proves
`q(m)<=ell(m)<=f(a,b)`. The full half-range of the shared bound is preserved.

## 3. Quarter-range BC comparison envelope

The exact two nonuniform witness radii are unchanged:

$$r=f(1-y,z),\qquad t=f(1-z,x/2),\qquad \widehat t=\min(t,A_3).$$

Set `u=x/2` and

$$P(y,r,t)=2(r+t)-(1-y+r)(4u-y+r).$$

On the original domain, `P_r>=0` and `P_t=2`. Thus smaller certified radii can
be substituted in this scalar inequality. No nesting of the two point sets is
asserted, and no rational radius replaces an actual witness in the viewer.

### Smaller difficult region

The inherited quadratic-bound arguments handle `y>=1/2` and `z>=2u`.
For `y<=1/2` and `1/4<=z<=2u`, the same bound gives

$$
P\ge q(z)(1-q(z))-u+3u^2
\ge\frac3{32}\frac{29}{32}-\frac1{12}=\frac5{3072}>0.
$$

Only `z<=1/4` requires the stronger envelope. Define

$$\beta(m)=\frac{2m}{4+3m},\qquad \kappa(m)=1+\frac32m.$$

For `m<=1/4`, the proof establishes

$$
f(a,b)\ge\max\{\beta(m),m-\kappa(m)(1-a-b)\}.
$$

The baseline follows from a quartic substitution with the increasing polynomial
`B(m)=81m^4+405m^3+656m^2+272m-128`, whose endpoint value is `-3163/256`.
For the affine bound, test `Cbar=1-m+kappa(m)delta` in the selected triangular
capacity quadratic. Its residual is `delta N_m(delta)/4`, where

$$
N_m(\delta)=(3m+2)^2\delta^3-10m(3m+2)\delta^2
 +(28m^2-22m-20)\delta+14m(1-m).
$$

On `0<delta<=beta(m)`, its derivative is at most `-18325/1024` and
`N_m(beta(m))=-2mB(m)/(4+3m)^3>0`. The argument explicitly retains the
selected smaller-root component; a polynomial sign is not treated as an
unconditional geometric feasibility criterion. The ordered coordinate bound
`1-2m-beta(m)>=15/38` is included.

### Explicit transitions

The remaining comparison radii switch at the rational curves
`y=g(z)` and `z=g(u)`, with `g(v)=v+beta(v)`. They no longer use `v+ell(v)`.
On `y=2u`, the nonbaseline radius is quadratic and
`(R(1-R))''<=-5`. On `y=g(z)`, the two derivatives in `u` are bounded above
by `-2` and equal to `6u+z>0`, respectively. Piecewise minima therefore occur
at the listed endpoints and three switch configurations. Their positive bounds
are printed in full in source 2615 and the manuscript:

$$\frac{z^2(9z^2+36z+44)}{4(3z+4)^2},$$
$$\frac{u^2(1+19u-4u^2-12u^3)}{3u+4},$$
$$\frac{3u^2(81u^4+441u^3+768u^2+460u+48)}
 {(3u+2)(3u+4)^2(3u+8)}.$$

The original coupled theorem and its capacity-free five-point threshold remain
unchanged. The singleton-gap case and the `A_3<t` diameter exit are not modified.
Implicit-root differentiation is removed from the active coupling proof.

### Preserve the older theorem's domain honestly

The wider `m<=3/8` envelope is not silently changed to a quarter-range theorem.
Its full original analytic proof is retained in the separate numbered source
`2615a_wide_range_slack_envelope.md`, which is explicitly not required by the
active BC route. The historical algebra auditors remain enabled. The new beta
is stronger than the old baseline on their common quarter-range, but is not
claimed with the same formula beyond that range.

## 4. Two factored D ratio arguments

Both adapters keep their statements, actual endpoint identities, supported-ray
frontier arguments, the size condition, and `C_1>=c`. Only the scalar ratio
calculation changes. Put `Q_c(x)=x^2+(c-2)x+c` and
`x=a/(a+epsilon)`; the existing scalar test converts `Q_c(x)>=0` to the D ratio.

For the T3-like chart, the original midpoint constraints give
`c>x+theta`, `theta>t/2`, and `x+(1-x)t>1/2`. Therefore

$$
Q_c(x)>\frac{(1-2x)(4x^2-3x+1)}{4(1-x)}>0.
$$

This removes the inverse formula in theta, the split at `theta=1/5`, and two
minimizations. The positive original slack is retained, not set to zero.

For Vd1, first retain the actual epsilon calculation giving
`x<=2L(c)`, with `L(c)=sqrt(3)-5/2+2c`. Since `sqrt(3)<7/4`,
`c>(3+2x)/8` and `x<1/2`. Consequently

$$Q_c(x)>\frac{(1-2x)(3-5x)}8>0.$$

The radical squaring, derivative test, and special sqrt(3)-coefficient
quadratic disappear. The numbered Vd1 source's additional bound on `a` follows
from `a<=x`, using the unchanged size condition. The pure four-point rescuer
geometry, original witnesses, and both replacement charts remain byte-identical.

## 5. Strict own-ray bound and F

The new reusable lemma states

$$a,b>0,\ a+b<1\quad\Longrightarrow\quad c_{\max}(a,b)>1-\min(a,b).$$

Start with the known nonstrict common-pair bound and exclude equality. With
`m=min(a,b)` and `delta=1-a-b>0`, the two selected branch equations give

$$F(1-m,m)=-m((1-m)^3+m^2)<0,$$
$$H(1-m)=-\delta((1-m)(1-2m)+m(2-m)\delta)<0.$$

For F's positive complementary pair, this and the shared q-bound immediately
give `0<1-c_*<m`. Uniform forcing supplies the same six radial points and disk.
Only the preliminary radial inequalities are shortened: `c_*`, the frontier
points `Q_-,Q_0,Q_+`, all exposed-contact analysis, exact coefficients, selectors,
and exact certificate data/provenance remain unchanged.

## 6. Source and interface synchronization

The principal edited proof owners are 2615, 2008b, 31051, 4130_new, and 4143_new.
The corresponding canonical and inline proofs are synchronized. The pure BC/D
caliper source 2616 and the active witness-definition file are unchanged.
The final obsolete paragraph in 2613 is corrected: CE1/CE2 remain structural
inputs, but the terminal BC calculation uses the threshold and capacity
instance, not a CE1 return or separate terminal sign-domain arguments.

The dependency graph includes the strict own-ray input to F and describes the
quarter-range envelope. Its source links point to the delivery branch. The
standalone caliper viewer's numerical code is unchanged. Historical proof-tree
snapshots and animation provenance are not relabeled as new proofs.

The new `verify_quarter_envelope_revision.py` runs 58 exact identity/sign checks,
22,680 exact rational-grid diagnostics, and 76 transition/near-endpoint tests.
The diagnostics are not universal proofs: the complete analytic domain
reduction is supplied in the numbered source and both editions.

The two intentionally changed supplier hashes have a before/after ledger in
`arrange/_support/quarter_envelope_preservation.json`. That same record protects
19 unchanged files, including the BC/D witness and caliper sources, replacement,
both preambles, and every original exact certificate data/replay file. The old
readability inventory is archived as `pre_quarter_envelope_baseline.json`;
the new inventory is recorded as a reviewed mathematical revision, not an
exemption from the source checks. All previous audits remain enabled.

## 7. Validation and publication protocol

Local full proof checks, immediate-proof correspondence, reviewed inventory,
dependency graph, interactive pages, proof-tree source/offline viewer, animation
assets, both exact zero-gap replay programs, clean builds, and full-page PDF
render scans passed. The local PDF logs had no undefined or multiply defined
references and no overfull boxes.

The local container cannot install the pinned registry packages. Its NumPy and
Matplotlib differ from the publication versions, so the unchanged trace-image
regeneration did not byte-match. Those incidental image changes were restored;
they are not part of this revision. This is recorded as a failed local check,
not disguised as success. Publication repeats source, certificate, image-byte,
and PDF checks with pinned dependencies and TeX Live 2025.

A temporary read-only Actions snapshot supplied the exact baseline because
shell GitHub networking was unavailable. Its reconstructed Git tree matched
`ca9c2359d5a3d072eeabdb5f8e646e0eb4ee01f8`. The delivery uses the requested
new branch only, with an allowlisted, hash-checked source payload, read-only
validation, and separate minimally privileged publication. Temporary transport
files/workflows are removed after delivery; the final tree and exact changed
bytes are checked against the validated publication manifest. The exported
report records the actual final commit, PR, CI results, artifact hashes, and
cleanup state. Neither a green transport run nor a local commit alone is
reported as publication.

These checks are mathematical/source and exact-certificate audits, not a
proof-assistant formalization of the entire theorem.
