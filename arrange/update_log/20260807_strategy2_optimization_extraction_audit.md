# Strategy 2 optimization extraction, verification split, and Lean problem shell

Date: 2026-08-07

## Scope

This revision completes the requested Strategy 2 interface work without
attempting a proof-assistant proof.

1. The support-isolated T3 endpoint calculation is expressed as a finite union
   of explicit real-variable cells.
2. The non-symmetry trace-dominating translation is replaced by exact
   radical parameters.  The preceding \(D_6\)-symmetry normalizations are
   retained.
3. The adjacent-rescuer source domains are explicit.
4. Every Vd residual component and radial endpoint is an explicit piecewise or
   graph function; no placement-defined supremum remains.
5. The former consolidated verification appendix is split into a registry and
   one file per technical section.
6. A Lean file records only the optimization problem statements, with every
   theorem closed by `sorry`.

## T3 feasible-domain extraction

The pure T3 variables are

\[
(r,a,d,\tau,\beta,A_1,A_5,C_1,C_5).
\]

The signed center belongs to the full CE1 or CE2 cell.  The exact
post-translation Type-II source is

\[
0<\tau<1,\qquad
z^2=1-\tau+\tau^2,\qquad
z>0,\qquad
0<\beta<\frac{\tau z}{1+z}.
\]

The boundary and radial graph values are

\[
b_-=\beta,\qquad b_+=z-\beta,\qquad
q=1-z+\beta,
\]

\[
c_\star=\frac q\tau,\qquad
u_\star=1+\beta-\tau.
\]

The endpoint record is divided into:

- three right residual orders;
- one CE1 or three CE2 left residual orders;
- three radial hit/miss orders;
- an easy endpoint-sum cell;
- sixteen exact hard contact-label pairs.

Equality at every transition is assigned to one named cell.  Consequently the
four-label formulas are never applied outside their own domains.

## Translation decision

Two operations had previously been described near each other.

- Sending the unique center midpoint to \(M_0\) and reflecting the chosen
  support to \(r_1\) are \(D_6\)-symmetry normalizations.  They remain
  geometric WLOG steps.
- Replacing a T3-like trace by a translated dominating trace is not a
  \(D_6\)-symmetry.  Its output is now represented by the explicit
  \((\tau,\beta)\) source equations above.

The same distinction is used in the adjacent-rescuer problem.

## Vd radial extraction

The interval component endpoint is now the explicit three-cell function

\[
\mathsf E(L,U;x)=
\begin{cases}
x,&x<L,\\
U,&L\le x\le U,\\
x,&U<x,
\end{cases}
\qquad
\mathsf R(L,U;x)=1-\mathsf E(L,U;x).
\]

For a corner parameter \(t>0\), the adjacent supported endpoint and the
nonadjacent own-radial endpoint are

\[
u_+=\frac{\sqrt{t^2+t+1}-p_1-tq_1-1}{t},
\]

\[
C_v=\frac{\sqrt{t^2+t+1}-p_v-tq_v}{t+1}.
\]

Positive support and absence of positive support are separated by the exact
order of the raw interval endpoints.  The three possible nonadjacent center
exits and both possible minima are also split into finite order cells.

## Verification appendix split

`04_strategy2_verification.tex` is now an input-only wrapper.

- The first module is a concise registry connecting each problem identifier to
  its existing exact proof.
- Every later `\section` of the previous consolidated file is preserved
  verbatim in its own numbered module.

This removes the historical reader exposition from the calculation files
without deleting proof details.

## Lean scope

The new folder is

```text
formalization/strategy2_optimization/
```

The Lean source defines the real-variable functions, domains, recurrences, and
theorem statements for S2-E1, S2-E2, S2-R1, S2-R2, S2-T3, S2-SC, and S2-VD.
Every theorem uses `sorry`.  No geometric bridge or optimization proof is
claimed to be formalized.

## Proof status

No existing mathematical terminal status is changed.  The T3, rescuer, and Vd
inequalities continue to be proved by the existing TeX and numbered proof
sources.  This revision changes their interface and file ownership.

## Validation

The branch workflow records source checks, LaTeX compilation, reference
checks, page rendering, and the generated PDF below.

## Branch build result

- Source commit that triggered the build: `f97b41e6d54293e0d0cd49c19b480d7542b59bea`
- GitHub Actions run: `31158983609`
- Repository source checks: **PASS**
- Exact Strategy 4 certificate replay: **PASS**
- XeLaTeX/latexmk compilation: **PASS**
- Undefined or multiply-defined references: **none detected**
- Rendered PDF pages: **133**
- PDF SHA-256: `dc0ddffd4296dd6823615230eaa9b95ebde046b32ac284a9a8c40b91aadc7882`
- Lean scope: problem statements only; `sorry` retained intentionally.
