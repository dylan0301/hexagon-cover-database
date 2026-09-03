# Editorial Reorganization Report: Exact-Definition Body and Solved Optimization Appendices

Status: Editorial plan — not a proof authority

Date: 2026-09-02
Manuscript snapshot audited: `766dce5a90abadc3086839f4e1a6cd922932f1d8`

This report implements the editorial request recorded in
`20260902_appendix_reorganization.txt`. It does not establish or change any
mathematical claim. Numbered sources under `proof/` and the exact certificate
incorporated by the paper remain the mathematical authorities.

This task creates the editorial report only. It deliberately leaves the TeX,
generated paper, proof sources, certificate data, and raw request unchanged;
the manuscript rewrite described below is the subsequent implementation task.

## 1. Editorial decision

The paper should be reorganized around the following firm boundary.

The main paper will contain:

- concise, exact mathematical definitions using sets, intersections,
  complements, convex hulls, distance, measure, containment, and explicit
  `\(\min/\max/\inf/\sup\)` feasible sets;
- exact symbolic definitions of every classification, selector, witness, and
  quantity used later, or the typed lemma-linked declaration allowed by the
  fallback rule below;
- exact hypotheses and conclusions for the exhaustive case routing;
- finite witness sets defined by intersection, extremum, union, and convex-hull
  equations;
- compact formal statements of the final trace, area, and enclosure bounds;
- one short, plain-language explanation after a definition or result when it
  helps the reader.

The main paper must not replace a mathematical definition with a descriptive
sentence. When an object admits an exact geometric or set-theoretic
definition, display that definition, including every feasible set and
extremum. Use the lemma-linked fallback below only when such a definition
would itself import the deferred coordinate calculation. A formula is not
moved merely because it is displayed or spans several lines.

Apply this writing rule throughout the rewrite:

1. Introduce each technical object with its exact mathematical definition.
2. If an explanation is useful, follow with one short sentence that only names
   its role, such as “`\(C_i\)` is the radial reach of `\(T_i\)`.”
3. Do not encode hypotheses, feasible-set restrictions, endpoint conditions,
   or optimization rules in descriptive prose. Put those conditions in the
   definition itself.
4. Omit the explanatory sentence when the displayed definition is already
   clear.
5. Prefer incidence, intersection, union, set difference, closure, interior,
   image, preimage, convex hull, metric ball, distance, measure, containment,
   or an extremum over an explicitly displayed feasible set.
6. If no such definition is available without importing the deferred
   calculation, retain the function symbol already used by the canonical paper
   or its numbered source and cite the unique supplying appendix lemma
   immediately with `\zcref`. The body states the domain, codomain, hypotheses,
   and compact value or inequality it uses. The cited appendix lemma gives the
   exact definition, all branches and endpoint conventions, and the proof.
   Only an output that has no established symbol may receive a new semantic
   subscript matching the supplying lemma. Do not rename an established symbol
   merely to encode a lemma name, and do not use an unexplained generic
   function symbol.
7. Do not redesign the notation during reorganization. Reuse the symbols in
   `02_global_notation.tex` and the applicable numbered source. If no canonical
   abbreviation exists, write the exact formula in place unless the fallback
   rule genuinely requires a new function symbol.

Thus the body uses exact geometric set and extremum definitions. It does not
use a verbal surrogate for a formula. A lemma-linked function is an exceptional
typed interface, not permission to hide a geometric or set-theoretic
definition. The appendices evaluate the body definitions in coordinates and
define and evaluate the exceptional functions when the proof needs a closed
form or a calculation.

The appendices will contain only proof-used, fully solved optimization or
feasibility problems. Each module will state its feasible family and objective,
give the exact optimum or required bound, and include the complete derivation
or exact certificate. The paper must remain self-contained: an appendix may
cite a numbered `proof/` source for provenance, but it may not omit an argument
on the ground that the repository contains it elsewhere.

In particular, the main paper will not contain:

- the signed CE1/CE2 parameters or exact trace/radial-exit formulas;
- affine half-plane charts, derived point-coordinate tuples,
  parameter-dependent radical evaluations, selected roots, or piecewise reach
  formulas;
- the evaluated exact disk-plus-point enclosure formula;
- point-by-point distance, support, derivative, squaring, or polynomial-sign
  calculations;
- case splits used to evaluate an optimization, or connected-component
  selector algebra used to obtain a closed form;
- numerical atlases or unused compatibility calculations.

The boundary is therefore **definition versus evaluation**, not **formula
versus prose**:

- keep the exact formula answering “what is this object?”;
- when the fallback applies, keep its typed function declaration and immediate
  appendix-lemma reference;
- keep the compact formula answering “what result is used?”; and
- move the coordinate evaluation, closed form, and proof calculation.

For example, the body should define the actual reaches exactly on the closed
V triangle:

\[
\begin{aligned}
A_i&:=\max\{t\in[0,1]:V_i+t(V_{i-1}-V_i)\in T_i\},\\
B_i&:=\max\{t\in[0,1]:V_i+t(V_{i+1}-V_i)\in T_i\},\\
C_i&:=\max\{t\in[0,1]:V_i+t(O-V_i)\in T_i\}.
\end{aligned}
\]

It should also record that the same values are the corresponding suprema for
the open `\(U_i\)`, and should define

\[
N_+:=\bigl|\{i:A_i+B_i>1\}\bigr|.
\]

Likewise, the body should display

\[
\Lambda(K):=
\inf\{\operatorname{side}(Q):
Q\text{ is a closed equilateral triangle and }K\subseteq Q\}.
\]

The support-function expression evaluating `\(\Lambda\)`, the piecewise
closed forms evaluating `\(c_{\max}\)` or `\(C_\pm\)`, and the calculations
proving them belong in the appendices. A named point may stay in the body as
an exact singleton intersection or selected extremum. For example, retain the
established definition `\(\{Q_0\}=\ell_-\cap\ell_+\)`. Its coordinate tuple
and root calculation move to the appendix.

Short final interfaces such as a trace cap, an area-loss lower bound, or
`\(\Lambda(K)\ge 1\)` also remain displayed in the body.

## 2. Current-paper diagnosis

The canonical PDF has 91 pages. The technical material is concentrated in the
body rather than the appendices:

- common geometry occupies approximately pages 5–20;
- trace calculations occupy approximately pages 21–29;
- area calculations occupy approximately pages 30–35;
- finite-enclosure calculations occupy approximately pages 36–80;
- the two current appendices occupy only the final pages.

The active TeX closure contains roughly seven hundred displayed formulas. The
number of displays is not itself the problem: exact definitions and compact
interfaces should remain displayed. The problem is that the body also contains
their coordinate evaluations and derivations. The finite-enclosure section
alone imports the local admissible-set calculation,
neighboring-ray capacity, CE1 reverse certificate, detailed terminal
certificates, output formulas, pointwise witness catalogue, endpoint audit,
and the full zero-gap computation. This is the opposite of the requested
reader hierarchy.

The repository already contains historical reader-facing sources
(`02_reader_framework.tex`, `03_strategy1_reader.tex`, and
`05_strategy3_reader.tex`) and an old appendix roadmap. They demonstrate that
a compact-body/technical-appendix layout is feasible, but they are stale and
must be adapted rather than re-enabled verbatim.

## 3. Proposed canonical organization

### Main paper

1. **Introduction and routing.** State the theorem, canonical C triangle/V
   triangle labeling, classifications, actual maximal reaches, boundary gaps,
   and the exhaustive routing table.
2. **Common geometric reductions.** Display the exact open/closed, reach,
   classification, gap, and strict-handoff definitions; then state the
   exact-trace normalization and midpoint results.
3. **Trace-length mechanism.** Define trace length, show the perimeter and
   skeleton targets, state the final cap register, and list the routed cases it
   excludes.
4. **Area-loss mechanism.** Display the feasible family and variational
   definition of unavoidable loss, state the local and cyclic loss results,
   and explain the two excluded zero-gap rows.
5. **Finite-enclosure mechanism.** Display exact set-builder definitions for
   the least enclosing side and each capacity, and exact intersection or
   convex-hull definitions for every witness; state the nonzero-gap and
   zero-gap terminal results.
6. **Completion.** Retain the full zero-gap-first and nonzero-gap routing
   argument.

A short appendix guide should close the organization discussion in the body.
It should not become a separate non-optimization appendix.

### Appendices

- **A. Structural, shared-local, and signed-center optimization**
- **B. Trace-length optimization**
- **C. Area-loss optimization**
- **D. Nonzero-gap finite-enclosure optimization**
- **E. Zero-gap nine-point optimization**
- **F. Exact polynomial positivity certificate**

Appendix A is not a miscellaneous calculation dump. Its material must be
partitioned into named solved modules:

1. **Open/closed shrinking feasibility:** feasible scales and the strict
   compactness margin.
2. **Center and V-triangle incidence feasibility:** the allowed edge/radial
   incidence patterns and the exact classification consequence.
3. **Exact-trace normalization:** the feasible same-orientation translations,
   trace-preservation constraints, and the selected normalized output.
4. **Signed-center optimization:** the CE1/CE2 feasible cells and the boundary,
   radial, diameter, and trace extrema used later.
5. **Strict-handoff feasibility:** the product of open selector intervals and
   the existence of selections with the required supercritical indices.
6. **Shared enclosure optimization:** `\(\Lambda\)`, the local admissible set,
   and `\(c_{\max}\)`.
7. **Midpoint caliper optimization:** the feasible four-point configurations
   and the exact midpoint conclusion.

Each module must state its feasible set or feasibility question, objective,
exact result, proof, and body consequence. None of the raw calculations listed
later may enter the appendix as a free-standing lemma outside this contract.

The current trace-exact numerical atlas should remain in the repository and
interactive material but leave the canonical paper. It is illustrative rather
than proof-used and therefore does not satisfy the agreed “used solved modules
only” rule.

## 4. Detailed body/appendix audit

Line numbers below refer to the audited snapshot and are navigation aids, not
permanent identifiers. Labels are the stable references.

### 4.1 Introduction and global definitions

From `01_introduction.tex`, keep the theorem and the canonical open triangles
`\(U_C,U_0,\ldots,U_5\)`, with `\(O\in U_C\)` and `\(V_i\in U_i\)`. Define
`\(T_C=\overline{U_C}\)` and `\(T_i=\overline{U_i}\)`. Put the closed
classifications and actual maximal reaches `\((A_i,B_i,C_i)\)` on these
`\(T\)` objects, while retaining the `\(U\)` objects whenever openness or
endpoint coverage matters. Also keep the role figures, `\(N_+\)`, the
singleton-gap convention, the case counts, and Table `tab:routing`.

In every routing, classification, or terminal-subcase table, the leftmost
subcase-identifying block must contain formulas only. Split that block into as
many columns as needed for `\(N_{\mathrm{gap}}\)`, `\(N_+\)`,
`\(N_E(T_C)\)`, the already defined counts `\(d,t\)`, normalized indices,
and incidence predicates. Reuse the paper's established notation: in
particular, use
`\(N_+\)` directly rather than introducing a new index set for the same
condition. Do not add a table-only alias when an existing symbol or an exact
formula already expresses the condition.

A subcase cell may contain `\((d,t)=(0,0)\)`, `\(d=0\)`, `\(t\le2\)`, or
`\(\tau\in\{1,5\}\)`, but not a verbal replacement such as “all Vd0,” “at
most two T3-like roles,” or “an adjacent Vd role.” When the identity of an
index matters, use the established convention that `\(\sigma\)` is the
unique supercritical index and `\(\tau\)` is the unique Vd1/Vd2 index. Display
the conditions exactly, for example

\[
A_\sigma+B_\sigma>1,
\qquad
A_i+B_i\le1\quad(i\ne\sigma).
\]

Put logically distinct disjuncts in separate rows. Define any genuinely
necessary abbreviation immediately before the table. Reserve prose for the
caption and for columns outside the subcase-identifying block. This rule
applies to case tables, not to notation or bounds tables.

Edit as follows:

- Keep the exact global definition in the body:

  \[
  \lVert V_0-O\rVert=1,\qquad
  V_i:=\operatorname{Rot}_{O,i\pi/3}(V_0),
  \]
  \[
  H:=\conv\{V_0,\ldots,V_5\},\qquad
  e_{i,i+1}:=[V_i,V_{i+1}],\qquad r_i:=[O,V_i],
  \qquad M_i:=\frac{O+V_i}{2},
  \]
  \[
  S:=\partial H\cup\bigcup_{i=0}^5r_i.
  \]

  Here `\(\operatorname{Rot}_{O,\theta}\)` is ordinary rotation through
  `\(\theta\)` about `\(O\)`, not a new paper symbol. Move the cosine–sine
  coordinate realization to Appendix A, where one global chart can serve all
  evaluations. Reserve the established `\(\mathsf R\)` for counterclockwise
  rotation through `\(2\pi/3\)` in the enclosure gauge.
- Keep `\(N_+\)` defined only from actual `\(A_i+B_i>1\)`.
- Keep the exact boundary-gap set definition together with the elementary
  picture; one short sentence should say that a singleton remains uncovered
  by the two incident open V triangles.
- Rewrite the organization paragraph at lines 261–271 so Sections 2–5
  “give the exact definitions and compact interfaces,” while Appendices A–F
  solve the associated optimizations.
- Rewrite the abstract so it no longer claims that exact local calculations
  are retained in the body.

### 4.2 Structural reductions

`02_structure_and_common_geometry.tex` should become a compact body wrapper.
Split and adapt the two mixed sources it currently imports: place the retained
exact definitions, statements, and short proofs in one body-interface source, and
place only their proof-used calculations in Appendix A modules. Do not import
all of either `02_structural_reductions.tex` or
`04a_signed_center_calculus.tex` wholesale in the body or appendix; doing so
would either lose the body interfaces or duplicate their labels.

Keep compact exact body statements and short proofs for:

- `prop:open-closed-scaled`;
- `lem:distinct-roles`;
- `prop:ce-classification`;
- `lem:local-wedge`;
- `prop:vd0-exact-trace-normalization`;
- `prop:vertex-classification`;
- `prop:t3-translation`, including the warning that it is a closed-trace
  majorant rather than a replacement open triangle;
- `lem:gap-exhaustion`;
- `lem:t3-nonsupercritical`;
- `prop:strict-handoffs`;
- `lem:self-midpoint` and `prop:unique-center-midpoint`;
- `prop:exhaustive-structural-reduction`.

Keep exact reach definitions in the body. After setting
`\(R_i(t)=V_i+t(O-V_i)\)` and retaining the edge parametrization `\(X_i\)`,
write the three `\(\max\)` definitions on the closed `\(T_i\)` exactly as in
Section 1 of this report, together with their equal open-`\(U_i\)` suprema.
The initial-segment property is a compact lemma, not a prose substitute for
the definitions. Whenever selected demands appear, display
`\(a_i\le A_i\)`, `\(b_i\le B_i\)`, and `\(c_i\le C_i\)`.

Also retain the concise edge and gap definitions from
`02_structural_reductions.tex:531–548`:

\[
X_i(t):=V_i+t(V_{i+1}-V_i),
\]
\[
G_i:=e_{i,i+1}\setminus
\bigl((U_i\cap e_{i,i+1})\cup(U_{i+1}\cap e_{i,i+1})\bigr).
\]

The proposition may then identify
`\(G_i=X_i([B_i,1-A_{i+1}])\)` when
`\(B_i+A_{i+1}\le1\)`, including equality as a singleton, and
`\(G_i=\varnothing\)` otherwise. This definition must use the open `\(U\)`
traces. Define

\[
N_{\mathrm{gap}}:=\bigl|\{i:G_i\ne\varnothing\}\bigr|.
\]

Move to Appendix A:

- the compactness margin functions and quantitative shrinking calculation at
  lines 50–72;
- both center-classification squared-distance calculations at lines 126–145;
- the wedge chart and norm identities at lines 172–211;
- both orientation families and all affine side formulas at lines 213–252;
- the complete raw `(3,0)` normalization calculation at lines 277–380;
- the T3-like Type-I/Type-II calculation at lines 441–490;
- the proof of the open trace interval identities after their short exact
  definitions in the body;
- the ascent equivalence, telescoping calculation, and adjacent-selector proof
  at lines 628–689;
- the four-point midpoint caliper calculation at lines 693–752.

Also put the shared equilateral enclosure gauge and exact local admissible-set
optimization from the opening of `06_direct_local_calculus.tex` in Appendix A.
This module is used by the trace, nonzero-gap, and zero-gap appendices, so it
must be solved once before all three rather than duplicated in Appendix D.

Do not define a strict handoff in words. Keep its exact selector in the body:

\[
\xi_i\in(1-A_{i+1},B_i),\qquad
a_i:=1-\xi_{i-1}<A_i,\qquad b_i:=\xi_i<B_i.
\]

The only explanatory sentence needed is “Thus every selected handoff is
strict.” Appendix A proves that the intervals are nonempty and proves the
clauses preserving one or at least two selected supercritical roles.

### 4.3 Signed CE1/CE2 geometry

Move all proof-used material from `04a_signed_center_calculus.tex` to
Appendix A. This is the material explicitly identified for removal from the
body:

- the affine point chart;
- `\(R,W,E,\eta,P,\alpha,\delta,k\)`;
- the three side-slack functions;
- the right and left trace intervals;
- `\(\Delta_R,\Delta_L\)` and their sign test;
- all six exact radial exits;
- total-slack, boundary-contribution, and diameter-transfer calculations;

The compatibility-only chart-conversion remark at lines 213–250 and the four
exact formula diagrams at lines 349–381 remain available as repository source
material but leave the canonical paper. Their labels have no references beyond
their definitions, and they are not solved optimization steps needed by the
final argument.

Do not replace these calculations by a qualitative paragraph. Keep the exact
classification definition in the body:

\[
N_E(T_C):=
\bigl|\{i\in\mathbb Z/6\mathbb Z:
  \mathcal H^1(T_C\cap e_{i,i+1})>0\}\bigr|,
\qquad
T_C\text{ is CE}k\iff N_E(T_C)=k,
\qquad k\in\{0,1,2\}.
\]

For CE1 and CE2, retain the compact exact consequence

\[
\bigl|T_C\cap\{M_0,\ldots,M_5\}\bigr|=1.
\]

One short sentence suffices: a point contact has zero trace length and hence
does not create a second positive trace. The signed parameters, exact trace
endpoints, and radial exits remain in Appendix A.

The final CE1 and CE2 boundary trace caps may appear in the body trace table.

### 4.4 Trace length

Replace the body imports in `03_trace_bounds.tex` with an updated compact trace
source based on, but not copied from, `03_strategy1_reader.tex`.

Keep in the body:

- `\(L_E(T)=\mathcal H^1(T\cap E)\)` and the subadditivity principle;
- the perimeter/skeleton target figure;
- the final trace-cap table from `thm:boundary-trace-table`;
- the positive-support rescuer as its exact labeled implication, with symbolic
  hypotheses and conclusion rather than a verbal paraphrase;
- `thm:common-skeleton-count`;
- `prop:ce2-vd2-midpoint-length`;
- the exact six-item list in `prop:length-branches`.

Move `03_strategy1_length.tex` and
`04b_common_CE1_CE2_budgets.tex` calculations to Appendix B, including:

- the signed center skeleton sum;
- local point-distance formulas;
- the selected supercritical polynomial cell and its smaller-root component;
- the quartic `\(Q(s,\delta)\)`, derivative factorization, and endpoint signs;
- the Vd half-plane normal form and all raw radial intervals;
- the Vd2 midpoint functions, derivative checks, and `\(t=4/3\)` split;
- the master perimeter-deficit arithmetic, small-slack bounds, and all final
  numerical substitutions.

Correct the existing Vd statements that call exact reaches `\(a,b\)`. Exact
or maximal reaches must be uppercase; lowercase notation is reserved for
explicitly introduced lower bounds.

The historical `03_strategy1_reader.tex` is not a drop-in replacement: its
first two branch descriptions say CE0, whereas the current result is the
center-independent condition `\(N_{\mathrm{gap}}=0\)`.

### 4.5 Area loss

Use `05_strategy3_reader.tex` only as structural scaffolding. Keep in the body:

- a simple local/cyclic area figure paired with exact definitions;
- the canonical feasible family and loss functions, normalized at `\(V_0\)`,

  \[
  \mathcal T(a,b):=
  \{T:T\text{ is a closed unit equilateral triangle and }
  \{V_0,V_0+a(V_5-V_0),V_0+b(V_1-V_0)\}\subseteq T\},
  \]
  \[
  \mathcal L(T):=
  \frac{\operatorname{area}(T\setminus H)}{A_\triangle},
  \qquad
  \mathcal L(a,b):=
  \inf_{T\in\mathcal T(a,b)}\mathcal L(T),
  \qquad A_\triangle=\frac{\sqrt3}{4};
  \]

  The corresponding family at `\(V_i\)` is obtained by the already defined
  hexagon symmetry while retaining the same notation. For selected reaches,
  display
  `\(0\le a_i\le A_i\)` and `\(0\le b_i\le B_i\)`; the rotated copy of
  `\(T_i\)` then belongs to `\(\mathcal T(a_i,b_i)\)`;
- the compact exact inequalities

  \[
  \mathcal L(a,b)\ge\min\{a,b\}^2,
  \qquad
  a+b>1\Longrightarrow
  \mathcal L(a,b)\ge\max\{a,b\}^2;
  \]
- the T3-like actual-triangle result

  \[
  T_i\text{ is T3-like},\qquad
  0\le a_i\le A_i,\quad0\le b_i\le B_i,\quad
  0\le\mu\le\frac12,\quad a_i,b_i\ge\mu
  \Longrightarrow \mathcal L(T_i)\ge2\mu-4\mu^2,
  \]

  unless a T3-restricted feasible family is explicitly defined; and
- the cyclic certificate with the strict-handoff data

  \[
  \xi_i\in(1-A_{i+1},B_i),\qquad
  a_i:=1-\xi_{i-1}<A_i,\qquad b_i:=\xi_i<B_i,
  \]

  and its two exact hypotheses and conclusions

  \[
  \#\{i:a_i+b_i>1\}\ge2
  \Longrightarrow
  \sum_{i=0}^5\mathcal L(T_i)>1,
  \]
  \[
  \begin{gathered}
  \#\{i:a_i+b_i>1\}=1,\qquad
  \forall i\;[T_i\text{ is Vd0 or T3-like}],\\
  \exists j\;[T_j\text{ is T3-like}]
  \end{gathered}
  \Longrightarrow
  \sum_{i=0}^5\mathcal L(T_i)>1,
  \]

  followed by `prop:area-branches`.

Move to Appendix C:

- the wedge coordinates, metric, determinant, and exact hexagon inequalities;
- both exhaustive orientation forms;
- every affine containment inequality and polygon vertex list;
- the Type-I and Type-II loss functions and all factorizations;
- the T3-like limiting family, exact endpoint `Q`, rational functions, and
  polynomial positivity checks;
- the `\(m,M\)` extrema, reflection, and both cyclic sum calculations.
  Appendix C must cite the exact handoff selector retained in the body; it must
  not redefine or duplicate it.

Correct two defects before using the old reader scaffold:

- its T3-like statement applies a bound to the unrestricted optimized
  `\(\mathcal L(a,b)\)`, while the proved result concerns the actual
  T3-like triangle `\(\mathcal L(T_i)\)` unless a T3-restricted feasible family
  is defined;
- its excluded branches are stated for CE0, but the current authoritative
  interface applies whenever `\(N_{\mathrm{gap}}=0\)`, independently of the
  center class.

Change the stale “Method 3” figure caption to “area-loss method” or
“Strategy 2.”

### 4.6 Finite-enclosure body interface

Create a new compact finite-enclosure body source rather than activating the
old zero-gap-only `06_strategy4_reader.tex`.

Keep the following compact exact definitions and conclusions. Do not replace
any of them by an English optimization paraphrase.

For every nonempty compact `\(K\)`, display

\[
\mathbb B(X,r):=\{Y:\lVert Y-X\rVert\le r\}\qquad(r\ge0).
\]

\[
\Lambda(K):=
\inf\{\operatorname{side}(Q):
Q\text{ is a closed equilateral triangle and }K\subseteq Q\}.
\]

Also retain the common contradiction lemma

\[
\left.
\begin{gathered}
K\text{ is compact},\qquad K\subset U,\\
U\text{ is an open unit equilateral triangle}
\end{gathered}
\right\}
\Longrightarrow \Lambda(K)<1.
\]

Its inward-side compactness proof is short enough to remain in the body.

Use the infimum definition without a blanket attainment claim for every
compact set; a singleton would require an explicit degenerate-triangle
convention at side zero. Prove attainment only for the witness families where
it is needed. The support-function formula that evaluates `\(\Lambda\)`
belongs in Appendix A.

Normalize at `\(V_0\)` and use the established radial map
`\(R_i(c):=V_i+c(O-V_i)\)`. Retain the canonical anchor-hull notation

\[
K(a,b,c):=\conv
\{V_0,X_5(1-a),X_0(b),R_0(c)\},
\]
\[
\mathcal A:=
\{(a,b,c)\in[0,1]^3:\Lambda(K(a,b,c))\le1\}.
\]
\[
c_{\max}(a,b):=
\max\{c\in[0,1]:(a,b,c)\in\mathcal A\},
\qquad
0\le a,b\le1,\quad a^2+ab+b^2\le1.
\]

Appendix A proves the exact projection identity

\[
\{(a,b)\in[0,1]^2:\exists c\in[0,1]\ (a,b,c)\in\mathcal A\}
=\{(a,b)\in[0,1]^2:a^2+ab+b^2\le1\},
\]

as well as attainment and the evaluation of `\(c_{\max}\)`. Rotated and
reflected copies use the same `\(K,\mathcal A,c_{\max}\)`; do not introduce
indexed copies or a name for the displayed domain.

For neighboring radial support, define

\[
C_+(a,b):=
\max\left\{c\in[0,1]:
\begin{array}{l}
\exists\Delta\ [\Delta\text{ is a closed unit equilateral triangle},\\
\{V_0,X_5(1-a),X_0(b),R_1(c)\}\subseteq\Delta]
\end{array}
\right\},
\]
\[
C_-(a,b):=C_+(b,a),
\qquad 0\le a,b\le1,\quad a+b\le1.
\]

Appendix D proves attainment and evaluates `\(C_\pm\)`. Actual V-type
restrictions enter when a neighboring term is selected, not in the definition
of `\(C_\pm\)` itself.

Make that selection exact without a neighbor-index alias. Retain

\[
0\le a_j\le A_j,\qquad 0\le b_j\le B_j
\quad(0\le j\le5),
\]
\[
a_j^2+a_jb_j+b_j^2\le1\quad(0\le j\le5),
\]
\[
\begin{aligned}
\mathcal H^1(T_{i-1}\cap r_i)>0&\Longrightarrow
a_{i-1}+b_{i-1}\le1,\\
\mathcal H^1(T_{i+1}\cap r_i)>0&\Longrightarrow
a_{i+1}+b_{i+1}\le1.
\end{aligned}
\]

\[
\Gamma_i:=\max\Bigl(
\{c_{\max}(a_i,b_i)\}
\cup\{C_+(a_{i-1},b_{i-1}):\mathcal H^1(T_{i-1}\cap r_i)>0\}
\cup\{C_-(a_{i+1},b_{i+1}):\mathcal H^1(T_{i+1}\cap r_i)>0\}
\Bigr),
\qquad D_i:=(1-\Gamma_i)V_i.
\]

Retain the exact forcing interface

\[
D_i\in r_i\subseteq S,\qquad
D_i\notin\bigcup_{j=0}^5U_j,
\]
\[
S\subseteq
U_C\cup\bigcup_{j=0}^5U_j
\Longrightarrow D_i\in U_C.
\]

Also retain, for `\(p,q\ge0\)` and `\(p+q\le1\)`,

\[
C_+(p,q),C_-(p,q)
\le1-\min\{p,q\}\le c_{\max}(p,q).
\]

The appendices prove these inequalities and endpoint strictness.

The exact gap `\(G_i\)` is the set difference defined in Section 4.2; do not
replace it by “the closed complement.” Likewise, every finite witness must be
displayed as a set. For example, with `\(P_j:=R_j(C_j)\)`, retain

\[
K_{\mathrm{tr}}:=
\{O,M_0,X_0(B_0),X_0(1-A_1),P_2,P_3,P_4\}.
\]

Every other named point must be defined by an exact singleton intersection or
selected extremum, and every witness hull by `\(\conv\)` of its
displayed generators. If an optimizer is not unique, use set-valued
`\(\operatorname{Argmin}\)`/`\(\operatorname{Argmax}\)` or give an exact
tie-breaking selector. Coordinates, radicals, and pointwise verification move
to the appendix.

Rewrite the finite-enclosure case table from the following exact register.
For A–E and the replacement router, assume

\[
S\subseteq U_C\cup\bigcup_{i=0}^5U_i.
\]

Row F retains the stronger hypothetical cover of all of `\(H\)`.

The short names A–F are only cross-references; the displayed formulas are the
body definitions and interfaces. Write every reflected local orientation as
the corresponding disjunction; do not give that disjunction a new name. The
symmetry already established for `\(c_{\max}\)` gives

\[
0\le p,q\le1,\quad p^2+pq+q^2\le1
\Longrightarrow c_{\max}(p,q)=c_{\max}(q,p).
\]

**A. One actual gap and `\(N_+=0\)`.** After rotation, set

\[
N_{\mathrm{gap}}=1,\qquad N_+=0,\qquad
N_E(T_C)\in\{1,2\},\qquad d=0,\qquad t\in\{0,1,2\},
\]
\[
J:=G_0=X_0([\ell,r]),\qquad
\ell:=B_0,\qquad r:=1-A_1,
\]
\[
p:=1-r,\qquad q:=\ell,
\]
\[
0\le p,q\le1,\qquad p+q\le1,\qquad
c_*:=c_{\max}(p,q).
\]
\[
\mathcal D_{(\sqrt3/2)(1-c_*)}:=
\mathbb B\!\left(O,\frac{\sqrt3}{2}(1-c_*)\right)
=\left\{x:\lVert x-O\rVert\le\frac{\sqrt3}{2}(1-c_*)\right\}.
\]

For

\[
\forall i\in\mathbb Z/6\mathbb Z\quad
[(p\le A_i\land q\le B_i)\lor(q\le A_i\land p\le B_i)],
\]

retain

\[
\mathcal D_{(\sqrt3/2)(1-c_*)}\cup J\subset U_C,
\qquad
\Lambda\bigl(\mathcal D_{(\sqrt3/2)(1-c_*)}\cup J\bigr)\ge1.
\]

The definition of `\(J\)` includes `\(\ell=r\)`, so this row includes a
singleton gap. Appendix D proves the two displayed conclusions.

**B. Two actual gaps in CE2.** Normalize the two positive C-triangle traces to
`\(e_{5,0}\)` and `\(e_{0,1}\)`, and define

\[
p:=\min\{t\in[0,1]:X_5(t)\in T_C\},\qquad
q:=1-\max\{t\in[0,1]:X_0(t)\in T_C\},
\]
\[
0\le p,q\le1,\qquad p+q\le1,\qquad
c_*:=c_{\max}(p,q),
\qquad D_2:=(1-c_*)V_2,\quad D_4:=(1-c_*)V_4.
\]

\[
N_E(T_C)=2,\qquad N_{\mathrm{gap}}=2,\qquad
N_+\in\{0,1\},\qquad d=0,
\]
\[
\forall i\in\{1,2,3,4,5\}\quad
[(p\le A_i\land q\le B_i)\lor(q\le A_i\land p\le B_i)],
\]
\[
c_{\max}(q,p)=c_{\max}(p,q)=c_*,\qquad
D_2,D_4\in U_C,\qquad \{D_2,D_4\}\nsubseteq T_C.
\]

Appendix D evaluates the signed CE2 problem and proves the final
noncontainment; the signed parameters do not appear in this body row.

**C. One gap, one supercritical role, and all Vd0.** Rotate the unique
supercritical role to `\(T_0\)`, use `\(J=X_0([\ell,r])\)` from row A, and set

\[
N_{\mathrm{gap}}=1,\qquad N_+=1,\qquad
N_E(T_C)\in\{1,2\},\qquad(d,t)=(0,0),\qquad
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
\]
\[
\{\sigma\}=\{i:A_i+B_i>1\},\qquad \sigma=0,
\]
\[
P_i:=R_i(C_i),\qquad
K_{\mathrm{tr}}:=\{O,M_0,X_0(\ell),X_0(r),P_2,P_3,P_4\}.
\]

Retain

\[
K_{\mathrm{tr}}\subset U_C,\qquad
\Lambda(K_{\mathrm{tr}})\ge1.
\]

Do not add `\(P_0,P_1,P_5\)` to this witness. Appendix D contains the CE1 and
CE2 calculations establishing the same enclosure interface.

**D. T3-like or Vd1 supported tail.** Give the two normalized adapters
separate formula-only rows. The T3-like row is

\[
N_{\mathrm{gap}}=1,\quad N_+=1,\quad(d,t)=(0,1),\quad
N_E(T_C)\in\{1,2\},\quad
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
\]
\[
(o(T_0),n(T_0))=(2,1),\quad M_1\in T_0,\quad A_1+B_1>1,
\]
\[
(o(T_i),n(T_i))\in\{(1,0),(2,0)\}
\qquad(1\le i\le5).
\]

The Vd1 row is

\[
N_{\mathrm{gap}}\in\{1,2\},\quad N_+=1,\quad(d,t)=(1,0),\quad
N_E(T_C)=2,\quad
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
\]
\[
(o(T_0),n(T_0))=(1,1),\quad M_1\in T_0,\quad A_1+B_1>1,
\]
\[
(o(T_i),n(T_i))\in\{(1,0),(2,0)\}
\qquad(1\le i\le5).
\]

Both adapters use the established interval coordinates

\[
T_0\cap r_1=R_1([c,u]),\qquad
0\le c\le\frac12\le u<1,qquad
\varepsilon:=1-u,qquad C_1\ge c.
\]

Retain the canonical strict-supercritical envelope

\[
M_c^{\mathrm{sup}}:=
\sup\{b\in[0,1]:\exists a\in[0,1]\;
((a,b,c)\in\mathcal A\land a+b>1)\}
\qquad\left(0\le c<\frac12\right),
\]
\[
M_{1/2}^{\mathrm{sup}}:=\frac12,
\qquad M:=M_c^{\mathrm{sup}}.
\]

The value at `\(c=1/2\)` is the continuous extension, not the supremum of
an empty strict feasible set. The adapters prove

\[
R_1(u)=\varepsilon V_1\in U_C,qquad
A_0+\varepsilon\le1,qquad A_0\le1-M,qquad
\frac{A_0}{A_0+\varepsilon}\le1-M,
\]
\[
B_1<M,qquad A_i+B_i\le1\quad(2\le i\le5).
\]

The shared body conclusion is

\[
\sum_{i=2}^5(A_i+B_i)\ge4+M-B_1>4.
\]

Appendix D evaluates `\(M_c^{\mathrm{sup}}\)` and verifies the displayed
premises separately for the T3-like and Vd1 adapters.

**E. Adjacent or nonadjacent Vd radial separation.** Retain the routing
hypotheses

\[
N_E(T_C)=2,\qquad N_{\mathrm{gap}}\in\{1,2\},\qquad
N_+=1,\qquad(d,t)=(1,0),
\]
\[
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
\]
\[
\{\sigma\}=\{i:A_i+B_i>1\},\qquad
\{\tau\}=\{i:(o(T_i),n(T_i))\in\{(1,1),(1,2)\}\},
\]
\[
\sigma=0,\qquad\tau\in\{1,2,3,4,5\},\qquad
(o(T_j),n(T_j))\in\{(1,0),(2,0)\}
\quad(j\ne\tau).
\]

For the routed radial arm `\(r_i\)`, use the established separation
interface with exact extremal definitions

\[
d_C:=\max\{x\in[0,1]:xV_i\in T_C\},
\]
\[
c_{\mathrm{loc}}:=
\sup\{t\in[0,1]:R_i(t)\in U_{i-1}\cup U_i\cup U_{i+1}\}.
\]
\[
T_C\cap r_i=\{xV_i:0\le x\le d_C\},
\qquad
(U_{i-1}\cup U_i\cup U_{i+1})\cap r_i
\subseteq\{xV_i:1-c_{\mathrm{loc}}\le x\le1\}.
\]
\[
c_{\mathrm{loc}}<1-d_C
\Longrightarrow
\varnothing\ne\{xV_i:d_C<x<1-c_{\mathrm{loc}}\}
\subseteq
S\setminus\left(U_C\cup\bigcup_{j=0}^5U_j\right).
\]

For the adjacent adapter, the formula-only subcase is

\[
\sigma=0,\qquad\tau\in\{1,5\}.
\]

After reflection take `\((\sigma,\tau)=(0,1)\)` and apply the displayed
interface with `\(i=2\)`. Appendix D proves
`\(c_{\mathrm{loc}}<1-d_C\)` from the exact adjacent residual bounds.

For the nonadjacent adapter, retain

\[
\sigma=0,\qquad\tau\in\{2,3,4\}.
\]

For a closed interval `\(I\subseteq[0,1]\)` and `\(0\le p\le1\)`, use the
established residual operator

\[
\mathcal R_I(p):=
1-\sup\{x\in[0,1]:[0,x]\subseteq[0,p]\cup I\}.
\]

With the normalized C-triangle trace intervals

\[
I_R:=\{x\in[0,1]:X_0(x)\in T_C\},\qquad
I_L:=\{x\in[0,1]:X_5(1-x)\in T_C\},
\]

retain the established residuals and radial point

\[
\rho_R:=\mathcal R_{I_R}(B_0),\qquad
\rho_L:=\mathcal R_{I_L}(A_0),\qquad
\rho:=\min\{\rho_R,\rho_L\},\qquad D_\tau:=\rho V_\tau.
\]
\[
d_\tau^C:=\max\{x\in[0,1]:xV_\tau\in T_C\},\qquad
d_\tau^C<\rho<1-C_\tau,
\]
\[
D_\tau\in
S\setminus\left(U_C\cup\bigcup_{j=0}^5U_j\right).
\]

Appendix D proves the two strict radial estimates and all nonlocal diameter
exclusions.

**F. No gap, one supercritical role, and all Vd0.** Use the exact definitions
in Section 4.8 below. Its body row is

\[
N_{\mathrm{gap}}=0,\qquad N_+=1,\qquad
(d,t)=(0,0),
\]
\[
H\subseteq U_C\cup\bigcup_{i=0}^5U_i,
\]
\[
K_{\mathrm{wit}}(a,b)\subset U_C,\qquad
\Lambda(K_{\mathrm{wit}}(a,b))\ge1.
\]

The two-chart Vd1 replacement is a router, not a seventh terminal. If its
normalized input is

\[
S\subseteq U_C\cup\bigcup_{i=0}^5U_i,\qquad
N_E(T_C)=2,\qquad N_{\mathrm{gap}}\in\{1,2\},\qquad N_+=1,
\]
\[
(o(T_0),n(T_0))=(1,1),\qquad M_1\in T_0,\qquad A_1+B_1>1,
\]
\[
A_i+B_i\le1\quad(i\ne1),\qquad
(o(T_i),n(T_i))\in\{(1,0),(2,0)\}\quad(1\le i\le5),
\]
\[
U_C\cap e_{0,1}=\varnothing,\qquad
\mathcal H^1(T_j\cap r_k)=0
\quad(2\le j\le5,\ k\in\{0,1\}),
\]

then the body theorem should state

\[
\exists\varepsilon>0\ \exists U'_0,U'_1\quad
\bigl[U'_k\text{ is an open unit equilateral triangle and }V_k\in U'_k
\quad(k=0,1)\bigr],
\]

such that, after setting

\[
U'_i:=U_i\quad(2\le i\le5),\qquad
T'_i:=\overline{U'_i}\quad(0\le i\le5),
\]

define

\[
G'_i:=e_{i,i+1}\setminus
\bigl((U'_i\cap e_{i,i+1})\cup(U'_{i+1}\cap e_{i,i+1})\bigr),
\qquad
N'_{\mathrm{gap}}:=\bigl|\{i:G'_i\ne\varnothing\}\bigr|.
\]
\[
N'_{\mathrm{gap}}\in\{0,1,2\}.
\]
\[
\begin{aligned}
A'_i&:=\max\{t\in[0,1]:V_i+t(V_{i-1}-V_i)\in T'_i\},\\
B'_i&:=\max\{t\in[0,1]:V_i+t(V_{i+1}-V_i)\in T'_i\},\\
C'_i&:=\max\{t\in[0,1]:R_i(t)\in T'_i\}.
\end{aligned}
\]

Retain

\[
S\subseteq U_C\cup\bigcup_{i=0}^5U'_i,\qquad
N_E(T_C)=2,\qquad
(o(T'_i),n(T'_i))\in\{(1,0),(2,0)\}\quad(0\le i\le5),
\]
\[
A'_i+B'_i\le1\quad(0\le i\le5),
\]
\[
A'_0+B'_0=A'_1+B'_1=1-\varepsilon<1,
\]
\[
(A'_i,B'_i,C'_i)=(A_i,B_i,C_i)\quad(2\le i\le5),\qquad
\bigl|\{i:A'_i+B'_i>1\}\bigr|=0.
\]

Route only from the recomputed value:

\[
\begin{aligned}
N'_{\mathrm{gap}}=0&\Longrightarrow
S\nsubseteq U_C\cup\bigcup_{i=0}^5U'_i,\\
N'_{\mathrm{gap}}=1&\Longrightarrow
S\nsubseteq U_C\cup\bigcup_{i=0}^5U'_i,\\
N'_{\mathrm{gap}}=2&\Longrightarrow
S\nsubseteq U_C\cup\bigcup_{i=0}^5U'_i.
\end{aligned}
\]

The three implications cite, respectively, `prop:length-branches` row Z0,
`thm:new-complementary-gap`, and `thm:new-ce2-short-ray`.

Do not assert `\(N'_{\mathrm{gap}}=N_{\mathrm{gap}}\)`. Both replacement charts
and all strict epsilon inequalities belong in Appendix D.

The final body table may compress this register only by splitting its leftmost
subcase-identifying block into as many symbolic hypothesis columns as needed.
Every entry in those columns must be an equation, inequality, membership
statement, quantified predicate, cardinality, or logical combination of them;
no subcase entry may be a verbal name. Every row must cite the adjacent exact
definitions and state an exact symbolic conclusion. A family name is not a
mathematical interface.

Keep schematic versions of the roadmap, complementary-gap, CE2 short-ray,
transverse-witness, zero-gap witness, and support-arc figures, paired with the
exact adjacent definitions. Remove only coordinate and computational
annotations. Move figures whose purpose is to display exact signed parameters,
evaluated neighbor-capacity branches, disk formulas, or CE1 algebra to the
appendices.

### 4.7 Nonzero-gap optimization

Move to Appendix D:

- the derivation of the gap endpoint identities and the common-pair proof from
  `06_finite_enclosure_full.tex:73–115`; retain `\(G_i\)` and every named
  source-conditioned union by exact set-builder definition if it is used in
  the body;
- the evaluated piecewise formulas for `\(C_+,C_-\)` and their common-pair
  corollary; retain their variational definitions and the exact
  `\(\Gamma_i,D_i\)` construction in the body. Appendix D cites the general
  `\(c_{\max}\)` solution in Appendix A and does not derive it again;
- the evaluated disk-plus-point formula and complementary-gap calculation;
  retain `\(K=\mathbb B(X,r)\cup\{P\}\)` and `\(\Lambda(K)\)` as exact body
  definitions whenever that object is used;
- all `\(p,q,e\)` inequalities, roots, concavity, and endpoint checks in the
  CE2 short-ray theorem;
- the transverse set coordinates, endpoint squeeze, CE1 reverse return, and
  CE2 threshold calculation;
- the finite-enclosure-specific thresholds, selected-chord estimates, and
  other downstream calculations from `06_direct_local_calculus.tex`; its
  shared enclosure gauge and exact admissible-set module belong to Appendix A,
  while exact feasible-set definitions, variational definitions, and compact
  terminal inequalities remain in the body;
- the piecewise neighboring-ray formula and selectors from
  `06a_neighbor_ray_calculus.tex`;
- the proof-used caliper, one-third envelope, and rescuer-tail calculations;
- the CE1 reverse-path certificate;
- T3-like, adjacent Vd, nonadjacent Vd, and Vd1 coordinate and pointwise
  verification formulas, after each named body point has received an exact
  intersection or extremum definition.

Consolidate repeated proofs from `06d_detailed_direct_certificates.tex` and
`06f_casewise_witness_details.tex` so every optimization is solved exactly
once. Omit the unused quarter-radial lemma from the canonical paper.

Resolve the remaining mixed finite-enclosure sources explicitly:

- move all of `06b_ce1_direct_certificate.tex`, including its signed
  parameter statement, to Appendix D; retain the body proposition
  `prop:readable-k410-ce1` in the exact form that no CE1 open unit triangle
  contains `\(K_{\mathrm{tr}}\)`, with its short proof citing the appendix
  calculation;
- rewrite the compact terminal statements from
  `06c_exceptional_direct_terminals.tex` into the body, preserving
  `prop:new-one-t3-terminal` and the assembly-used
  `prop:new-one-vd-assembly`, and move their proof-used formulas and proofs to
  Appendix D;
- move every proof-used calculation from
  `06e_direct_local_proof_details.tex` to Appendix D, while omitting its unused
  quarter-radial module and leaving no piecewise/root catalogue in the body;
  and
- rewrite the conclusions of
  `06i_simplified_finite_enclosure_interfaces.tex` as compact exact body
  interfaces, while moving evaluated closed forms and every supporting
  calculation to Appendix D.

The current endpoint audit must not be moved blindly:

- `06g_endpoint_selector_audit.tex:138–171` derives the upper squeeze using
  `\(P_0\)`, but the current transverse witness deliberately uses only
  `\(P_2,P_3,P_4\)` and states that no radial point on `\(r_0\)` is used.
  Replace this subsection with the current gap-endpoint squeeze.
- Lines 186–197 incorrectly say that all six actual radial endpoints are
  retained and cite nonexistent equation numbers. Remove or rewrite them for
  the three-transverse witness.

Appendix D must incorporate the complete Proven two-chart replacement from
`proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2_new/4144_new_two_chart_replacement_and_router.md`.
The current paper contains only a prose summary. The self-contained appendix
must preserve:

- distinct `\(V_0\)` and `\(V_1\)` charts;
- the shifted minus template for the first replacement;
- the minus/plus split for the second replacement at `\(p_2=1/2\)`;
- all strict epsilon margins;
- preservation of the five affected skeleton pieces;
- six nonsupercritical Vd0 output roles;
- recomputation of `\(N'_{\mathrm{gap}}\in\{0,1,2\}\)` from the output open
  traces;
- no assertion that the input and output gap ranks agree.

Preserve the source’s mathematics and strictness, but not its legacy symbol
roles: translate every unindexed lowercase quantity used there as an actual
reach into indexed uppercase actual-reach notation. Use lowercase quantities
only when they are explicitly recast as selected lower bounds with inequalities
against those uppercase reaches.

### 4.8 Zero-gap optimization and exact certificate

Use the public notation of `06_strategy4_reader.tex`; do not introduce a
second zero-gap notation layer. Under a hypothetical cover, the formula-only
body row is

\[
N_{\mathrm{gap}}=0,\qquad N_+=1,\qquad(d,t)=(0,0).
\]

Rotate the unique supercritical role to index `\(4\)`. Retain

\[
\xi_3<\xi_2<\xi_1<\xi_0<\xi_5<\xi_4,
\]
\[
a:=1-\xi_3,\qquad b:=\xi_4,\qquad
p:=1-b,\qquad q:=1-a,
\]
\[
0<a,b<1,\qquad a=a_4<A_4,\qquad b=b_4<B_4,
\qquad a+b>1,\qquad a^2+ab+b^2<1,
\]
\[
a_i\ge p,\qquad b_i\ge q\qquad(0\le i\le5).
\]

These relations are supplied by `\zcref{lem:ab-extreme-jump}`. Preserve the
public equation labels `eq:reader-extreme-chain`,
`eq:reader-ab-parameters`, and `eq:reader-ab-domain`.

Define the two boundary anchors and feasible union geometrically:

\[
P_A:=V_4+a(V_3-V_4),\qquad
P_B:=V_4+b(V_5-V_4),
\]
\[
\mathcal R_{AB}(a,b):=
\bigcup\left\{
T\cap H:
\begin{array}{l}
T\text{ is a closed unit equilateral triangle},\\
V_4,P_A,P_B\in T
\end{array}
\right\}.
\]

Use the already defined `\(c_{\max}\)` and retain

\[
c_\ast:=c_{\max}(p,q),\qquad
h:=\frac{\sqrt3}{2},\qquad r_\ast:=h(1-c_\ast),
\]
\[
P_i^{\mathrm{rad}}:=(1-c_\ast)V_i\qquad(0\le i\le5),
\]
\[
\mathbb B(0,r_\ast):=\{X:\lVert X\rVert\le r_\ast\}.
\]

The exact radial-forcing consequence is

\[
\mathbb B(0,r_\ast)
\subseteq\conv\{P_0^{\mathrm{rad}},\ldots,
P_5^{\mathrm{rad}}\}\subset U_C.
\]

Cite `\zcref{lem:symmetric-core-witness}` and retain
`eq:reader-forced-disk`.

For the asymmetric points, retain the established symbols
`\(\ell_-,\ell_+,\mathcal C_-,\mathcal C_+\)`. Define

\[
\mathcal C_-:=\partial\mathbb B(X_2(b),1),\qquad
\mathcal C_+:=\partial\mathbb B(X_5(1-a),1).
\]

Define the line pieces as the corresponding maximal nondegenerate line
segments of the interior frontier:

\[
\{\ell_-\}:=
\left\{
[X,Y]:
\begin{array}{l}
X,Y\in\mathbb R^2,\quad X\ne Y,\quad [X,Y]\subseteq
\partial\mathcal R_{AB}(a,b)\cap\interior(H),\\
[X,Y]\cap\mathcal C_-\ne\varnothing,\\
\nexists X',Y'\in\mathbb R^2\;[X,Y]\subsetneq[X',Y']
\subseteq\partial\mathcal R_{AB}(a,b)\cap\interior(H)
\end{array}
\right\},
\]
\[
\{\ell_+\}:=
\left\{
[X,Y]:
\begin{array}{l}
X,Y\in\mathbb R^2,\quad X\ne Y,\quad [X,Y]\subseteq
\partial\mathcal R_{AB}(a,b)\cap\interior(H),\\
[X,Y]\cap\mathcal C_+\ne\varnothing,\\
\nexists X',Y'\in\mathbb R^2\;[X,Y]\subsetneq[X',Y']
\subseteq\partial\mathcal R_{AB}(a,b)\cap\interior(H)
\end{array}
\right\}.
\]

Then define only the established three points:

\[
\{Q_0\}:=\ell_-\cap\ell_+,
\qquad
\{Q_-\}:=\ell_-\cap\mathcal C_-,
\qquad
\{Q_+\}:=\ell_+\cap\mathcal C_+.
\]

Appendix E proves existence and uniqueness from
`\zcref{thm:strict-ab-union,lem:fixed-line-signs}` and evaluates the points.
The body retains

\[
Q_-,Q_0,Q_+\in
\interior(H)\setminus\bigcup_{i=0}^5U_i,
\]

by `\zcref{lem:asymmetric-core-witness}`. Under the hypothetical cover this
gives

\[
Q_-,Q_0,Q_+\in U_C.
\]

Retain `eq:reader-forced-asymmetric` and define the public witness exactly by

\[
K_{\rm wit}(a,b):=
\mathbb B(0,r_\ast)\cup\{Q_-,Q_0,Q_+\}.
\]

The body retains

\[
K_{\rm wit}(a,b)\subset U_C,
\qquad
\Lambda(K_{\rm wit}(a,b))\ge1.
\]

Preserve `eq:reader-witness-set`, `thm:reader-witness-enclosure`,
`thm:reader-zero-gap-obstruction`, and `prop:reader-ab-core-branches`.

Move the coordinate evaluation of `\(\mathcal R_{AB}(a,b)\)`, the line and
circle equations, the roots defining `\((Q_-,Q_+)\)`, all pointwise
exclusions, the Newton inner points, and the support-arc calculation to
Appendix E. Retain there the existing labels `lem:ab-extreme-jump`,
`thm:strict-ab-union`, `lem:symmetric-core-witness`,
`lem:fixed-line-signs`, `lem:asymmetric-core-witness`,
`lem:technical-newton-reduction`, `eq:reader-newton-reduction`,
`prop:technical-four-overlaps`, and `lem:reader-cap-chain`.

Move the complete `06_zero_gap_ab_core.tex` calculation and the proof-used
parts of `06_zero_gap_completion.tex` to Appendix E. This appendix must precede
the exact certificate because the certificate depends on its AB variables,
frontier points, Newton inner points, and support-overlap proposition. Define
every retained public label exactly once.

Appendix F retains `A_zero_gap_exact_certificate.tex` substantively intact:
the manifest digest, rational upper envelopes, both L/T branch families, all
three compact cells/charts `\(T,L_0,L_1\)`, Gram reductions, eight exact
polynomial signs, all twenty exact Bernstein expansions (four on `\(T\)` and
sixteen on `\(L_0,L_1\)`), and both verifier references remain exact. Correct
only stale navigation prose:

- “Method 4” must become the current finite-enclosure method;
- the deleted “source ledger” reference must point to the actual provenance
  manifest or be removed.

The exact certificate may be presented as the solved problem of proving that
the minimum of each listed polynomial on its compact parameter cell is
nonnegative. It must never be replaced by numerical evidence.

### 4.9 Completion of the proof

Keep all of `07_exhaustive_assembly.tex` in the body. Its symbols identify
cases rather than perform local calculation. Preserve:

- the zero-gap-first split;
- actual `\(N_+\)`;
- the CE1/CE2 distinction;
- the hybrid CE2 one-Vd row;
- recomputation of the replacement output gap rank;
- the open/closed scaling corollary.

## 5. Optimization-module format

Every appendix module should use the same reader contract:

1. **Exact interface.** Copy or cite the body's geometric or set-theoretic
   definition. For a lemma-linked fallback function, cite its typed body
   declaration and give its exact definition in this unique appendix lemma.
   Never replace either form by a verbal paraphrase.
2. **Variables and feasible set.** Introduce the evaluation coordinates,
   inequalities, open versus closed endpoint conventions, type restrictions,
   and selected
   connected component.
3. **Objective.** State the maximum reach, maximum trace, minimum area loss,
   minimum enclosure side, or strict feasibility margin being determined.
4. **Exact result.** State the optimum or sufficient exact bound, with all
   endpoint strictness.
5. **Solution.** Give the full support, algebraic, or certificate proof.
6. **Body consequence.** Name the compact body proposition supplied by the
   solved problem.

This format keeps the appendices “pure optimization problems” while leaving
the complete proof inside the published paper.

No relocated calculation may be pasted between modules as background algebra.
It must belong to exactly one named module with an explicit feasible set,
objective or feasibility question, exact result, and cited body consequence.

Use one theorem-linkage pattern throughout: the body owns each compact public
labeled theorem; a separately labeled appendix lemma supplies its full
optimization calculation; and the body proof cites that appendix lemma before
giving the short exact implication and, if useful, one explanatory sentence.
Never repeat the public theorem label
in the appendix.

For every fallback function, retain the symbol used by the canonical paper or
its numbered source and cite the supplying appendix lemma immediately with
`\zcref`. Only when no established symbol exists may a new semantic subscript
be introduced; its stem must match the supplying appendix lemma's title and
label. Do not place a raw label key, a rendered lemma number, or `\zcref`
itself inside the function symbol.

## 6. Labels, numbering, and generated material

- Keep the established public labels on compact body statements used by
  `07_exhaustive_assembly.tex`.
- The current preamble loads only `hyperref`. Load `zref-clever` after it in
  the rewritten manuscript and use `\zcref` for the appendix-lemma links
  described above. Retain the existing ordinary semantic `\label` commands;
  conversion to `\zlabel` is not required.
- Give appendix-only lemmas semantic labels. Do not compile duplicate theorem
  statements carrying the same label.
- Remove every hard-coded `\tag{6.xx}` from relocated material. Use semantic
  `\label`/`\eqref` pairs only for equations cited later; leave uncited
  calculations unnumbered.
- This also fixes existing duplicate printed tags, including both sets of
  `6.24a–e`, the repeated `6.15` and `6.66`, and the colliding
  `6.73`/`6.73a`/`6.73b` series.
- Update the dependency-graph generator’s source grouping and declared body
  interfaces after labels move into reader-facing files.
- Replace the hard-coded “Appendix A contains” description at
  `interactive/_support/generate_dependency_graph.py:915` with a semantic
  exact-certificate-appendix reference, since the certificate becomes
  Appendix F.
- Update `proof/check.py` so its required canonical closure names the new
  active appendix modules rather than forcing stale or unused duplicated
  files into the paper.
- Regenerate the dependency graph and canonical PDF after the source closure
  changes.

## 7. Mathematical safeguards

The reorganization must preserve all of the following without abbreviation:

- C triangle and V triangle terminology;
- `\(O\in U_C\)`, `\(V_i\in U_i\)`, `\(T_C=\overline{U_C}\)`, and
  `\(T_i=\overline{U_i}\)`;
- classifications and maximal reaches on the closed `\(T\)` objects, with
  the open `\(U\)` objects retained wherever openness or endpoints matter;
- uppercase actual reaches and explicitly bounded lowercase selected reaches;
- `\(N_+\)` defined only from actual `\(A_i+B_i>1\)`;
- singleton boundary gaps;
- CE1 versus CE2, including the point-contact boundary;
- endpoint strictness at every open trace and handoff;
- actual V-type restrictions on neighboring support;
- connected-component and smaller-root selectors;
- the closed-majorant status of the T3-like translation;
- both charts and both branches of the Vd1 replacement;
- the exact zero-gap certificate and its authenticated data.

Any editorially discovered claim discrepancy must be reconciled against its
numbered Proven source before the TeX is changed. At minimum, the implementation
inventory must anchor the rewritten modules as follows:

- definitions and open/closed setup: `1001` (Definition) and `1003` (Proven);
- C triangle/V triangle classifications and strict handoffs: `1101`, `1201`,
  and `1214` (Proven);
- local admissibility, midpoint, and signed-center geometry: `2004`, `2005`,
  `2100`, and `2109` (Proven);
- trace interfaces: `2500`, `2510`, `2530`, and `2531` (Proven);
- area interfaces: `2400`, `3175`, and `3205` (Proven);
- finite-enclosure interfaces: `2608`, `2609`, and `2610` (Proven);
- current nonzero-gap terminals: `4013_new`, `4101_new`, `4102_new`, `4103`,
  `4130_new`, and `4140_new` (Proven);
- two-chart replacement and routing: `4144_new` (Proven);
- zero-gap package: `31050` is a Reference index, while `31051` through
  `31059` are the Proven authorities; and
- mixed-overlap positivity: the exact data, provenance manifest, appendix
  identities, and both verifier programs must agree exactly.

This is the minimum governing map, not permission to ignore a more specific
numbered source cited by a moved lemma. Step 1 below freezes the complete
claim-to-source inventory before any manuscript text moves.

## 8. Implementation sequence

1. Freeze the current theorem/label inventory and map every body conclusion to
   its numbered proof authority.
2. Build the compact Sections 2–5 under the geometric/set-theoretic-definition
   policy, retaining established function symbols for every `\zcref`-linked
   fallback, adapting the historical reader sources, and creating a new
   finite-enclosure reader source.
3. Extract the exact calculations into Appendices A–F using the common solved
   optimization format.
4. Consolidate duplicates, repair the stale transverse-witness passages, and
   incorporate the full two-chart replacement.
5. Convert hard-coded equation tags, install the `zref-clever` reference
   convention, rebuild case-table subcase blocks as formula-only columns,
   resolve all forward references, and update abstract, organization prose,
   captions, appendix guide, dependency metadata, and closure checks.
6. Build the paper and inspect both the normal and proof-free renderings. The
   proof-free rendering should preserve a coherent chain of exact definitions,
   hypotheses, and implications rather than disconnected theorem labels or
   prose substitutes for definitions.
7. Run every required repository check and the exact certificate programs,
   then regenerate publication artifacts only after all checks pass.
8. Validate the rebuilt canonical PDF, replace the tracked publication PDF
   with those exact validated bytes, and rerun the semantic/render checks.
   Measure the final page count; review and change CI’s current `84–104` bound
   only if the intentional measured output requires it.

## 9. Verification commands

Run the repository-required checks:

```bash
python -m pip install -r arrange/_support/requirements.txt
python proof/check.py
python interactive/generate.py --dependency-graph --check
python interactive/check.py
python arrange/build.py --all
```

Because the dependent zero-gap theorem and its placement in the manuscript
will change, also run:

```bash
python proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_mixed_overlap_core_derivation.py
python proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_global_core_positivity.py
```

Build the proof-free paper:

```bash
arrange/_support/build_proof_free_paper.sh
```

Then inspect its table of contents, theorem numbering, figure placement,
appendix dependency order, and the absence of undefined or duplicated
references.

For the publication artifact, validate the clean build before installing it,
then confirm that the tracked and rebuilt PDFs agree semantically:

```bash
python arrange/_support/verify_pdf_render.py arrange/_build/canonical.pdf
cp arrange/_build/canonical.pdf arrange/paper_draft/main.pdf
python arrange/_support/compare_pdfs_semantically.py arrange/paper_draft/main.pdf arrange/_build/canonical.pdf --dpi 144
```

Record the measured page count. Removing the numerical atlas changes that
count and may cross the hard-coded `84–104` range at
`.github/workflows/ci.yml:108`; update the bound only after inspecting the
intended final PDF, and keep it as narrow as the publication policy allows.

## 10. Acceptance criteria

The reorganization is complete only when:

- every set, scalar, function, selector, and witness used in the body either
  has an exact geometric or set-theoretic definition at first use or is an
  exceptional typed function with an explicit domain, codomain, hypotheses,
  its established canonical symbol, and an immediate `\zcref` to its unique
  defining appendix lemma; only a genuinely unnamed output receives a new
  semantic lemma-matching subscript, and no essential object is defined only
  by descriptive prose;
- every `\(\min\)`, `\(\max\)`, `\(\inf\)`, `\(\sup\)`,
  `\(\operatorname{Argmin}\)`, or `\(\operatorname{Argmax}\)` has an explicit
  feasible set and, where relevant, all actual V-type restrictions;
  single-valued extrema are used only when attainment and, where needed,
  uniqueness are established;
- body displays retain the foundational geometry, exact set/measure/
  containment/extremal definitions, actual-versus-selected inequalities,
  classification and routing conditions, witness-set equations, and compact
  theorem conclusions;
- the main paper contains no signed CE1/CE2 endpoint or radial-exit formulas;
- the main paper contains no derived point coordinates, piecewise reach
  evaluation, parameter-dependent radical root
  catalogue, polynomial expansion, exact disk-plus-point evaluation, affine
  point chart, or pointwise distance audit;
- every named body point is defined by an exact singleton intersection or
  selected extremum whenever possible; any exception uses the typed
  lemma-linked fallback, and every witness is defined by an exact set, union,
  or convex-hull formula;
- every lowercase reach is introduced by an explicit inequality against an
  uppercase actual reach;
- in every routing, classification, or terminal-subcase table, the leftmost
  subcase-identifying block contains only exact symbolic predicates, split
  across multiple columns where needed; no subcase is identified there by
  prose, and no new alias replaces an established quantity such as `\(N_+\)`;
- the final trace, area, and enclosure interfaces are visible in the body and
  the exhaustive proof can be followed from the exact definitions and compact
  implications without consulting the coordinate evaluations;
- every deferred result has one complete, proof-used solved optimization
  module in Appendices A–F;
- the Vd1 two-chart replacement is fully incorporated and the stale `P_0`
  argument is gone;
- the exact zero-gap certificate remains mathematically unchanged and both
  verifiers pass;
- the canonical closure contains no duplicate or stale optimization proof;
- `arrange/paper_draft/main.pdf` is the validated canonical output and passes
  the repository’s semantic and render checks;
- the CI page-count interval contains the measured intentional output and was
  not broadened speculatively;
- all required checks pass and the rebuilt paper has no unresolved references,
  duplicate labels, or false hard-coded section equation numbers.
