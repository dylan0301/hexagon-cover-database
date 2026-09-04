# Editorial Reorganization Report: Readable Geometric Body and Solved Optimization Appendices

Status: Implementation record — not a proof authority

Date: 2026-09-02
Manuscript snapshot audited: `766dce5a90abadc3086839f4e1a6cd922932f1d8`

This report implements the editorial request recorded in
`20260902_appendix_reorganization.txt`. It does not establish or change any
mathematical claim. Numbered sources under `proof/` and the exact certificate
incorporated by the paper remain the mathematical authorities.

This report records both the editorial boundary and its implementation
requirements.  It does not replace any numbered proof source or exact
certificate.

## 0. Implementation result in the current working tree

The reorganization is implemented.  Sections 1--10 below preserve the
editorial decision, the diagnosis of the audited 91-page input, the migration
register, and the acceptance plan.  They are retained as audit history; this
section records the resulting manuscript rather than another proposal.

The canonical paper now has exactly six body sources: introduction and
routing, common geometry, trace bounds, area loss, finite enclosure, and
exhaustive assembly.  Its appendices are, in order:

- A, structural, shared-local, and signed-center optimization;
- B, trace-length optimization;
- C, area-loss optimization;
- D, nonzero-gap finite-enclosure optimization;
- E, zero-gap nine-point optimization; and
- F, the exact polynomial positivity certificate (retaining the stable source
  filename `A_zero_gap_exact_certificate.tex`).

The body now keeps the exact geometric or set-theoretic definitions, compact
interfaces, routing predicates, and useful short explanations.  Coordinate
charts, CE1/CE2 radial and interval evaluations, disk--point evaluation,
pointwise audits, selectors, roots, and polynomial calculations are supplied
by the appropriate appendix.  The established notation is unchanged:
`\(N_+\)` is defined only by actual `\(A_i+B_i>1\)`, no alias replaces
`\(N_+\)`, uppercase reaches are actual, and every selected lowercase
reach is explicitly bounded by its uppercase reach.  Decision-table
rows use exact predicates in their identifying columns, with one mathematical
statement on each visual line; concise geometric names and mechanisms remain
in separate prose fields where they help navigation.

The nonzero-gap closure now has explicit one-gap and two-gap common-pair
adapters in the body (`lem:new-one-gap-common-pair-adapter` and
`lem:new-two-gap-common-pair-adapter`), supplied by separately labeled
calculations in Appendix D.  For the CE2 two-gap normalization the implemented
endpoints are

\[
p:=\min\{x\in[0,1]:X_5(x)\in T_C\}.
\]
\[
q:=1-\max\{x\in[0,1]:X_0(x)\in T_C\}.
\]

The common-pair closure eliminates row A and the row-B cases
`\(N_+=0\)` or `\((N_+,t)=(1,0)\)`.  The former row-B subcase
`\((N_+,t)=(1,1)\)` is instead covered, for either nonzero gap rank, by the
gap-rank-independent T3-like supported-tail terminal proved from `2018` and
`4132`.  The Vd1 replacement recomputes
`\(N'_{\mathrm{gap}}\)` from the output open traces.  Rank zero returns to the
trace-length closure; ranks one and two first rederive the corresponding
common-pair adapter from the primed actual reaches and then invoke the row-A
or row-B closure.  No equality between input and output gap ranks is assumed.

The exact top-level TeX keep set in Section 3 is realized.  Superseded
top-level paper sources, the two trace-atlas wrapper sources, and the
identified unused historical publication figures have been deleted.  The
fifteen trace-exact PNG panels are restored under the manuscript figure tree
and generated from the same deterministic registry as the standalone
interactive explorer.  The separately retained
`strategy4_core_case_example.png` is an exact-byte static asset protected by
SHA-256.  These sixteen images are explanatory and have no proof-authority
status.

Verification state recorded on 2026-09-04:

- dependency installation from `arrange/_support/requirements.txt` completed;
- a clean-snapshot `python proof/check.py` passed for all 35 canonical TeX
  sources;
- the dependency-graph and trace-asset generators both passed in `--check`
  mode, and `python interactive/check.py` passed;
- `python arrange/build.py --all` completed successfully, producing the
  reorganized 91-page canonical PDF, and the proof-free build completed at 51
  pages;
- canonical and proof-free render validation passed, and the installed
  `main.pdf` agrees semantically with the rebuilt canonical PDF at 144 dpi;
- both exact zero-gap certificate programs passed with exact arithmetic and
  the expected core-polynomial SHA-256
  `dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485`;
  and
- the inspected reorganized 91-page canonical output is enforced by the
  narrowed CI interval `89--93`.

Thus the implementation and the complete acceptance suite recorded in
Section 9 are finished in the current working tree.

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
- established geometric names, brief explanations, roadmap sentences, and
  informative captions wherever they help the reader understand why a
  definition or result is present.

The main paper must not replace a mathematical definition with a descriptive
sentence, but it also must not become an uninterrupted sequence of displays.
When an object admits an exact geometric or set-theoretic definition, display
that definition, including every feasible set and extremum, and introduce or
interpret it in plain language when that improves the exposition. Use the
lemma-linked fallback below only when such a definition would itself import
the deferred coordinate calculation. A formula is not moved merely because it
is displayed or spans several lines, and useful prose is not deleted merely
because the formula is now stated exactly.

Apply this writing rule throughout the rewrite:

1. Introduce each technical object with its exact mathematical definition.
2. Retain an established or especially clear geometric name when it gives the
   reader a useful handle, and place it beside the exact definition rather than
   using it as a substitute. Terms such as “boundary gap,” “supported tail,”
   “transverse witness,” and “two-chart replacement” should remain when they
   accurately describe the displayed object or case.
3. State hypotheses, feasible-set restrictions, endpoint conditions, and
   optimization rules symbolically. Prose may summarize their geometric
   meaning, but it must not be their only specification.
4. Keep concise prose that explains what an object is, why a case matters, how
   a normalization is chosen, or what the next lemma accomplishes. Delete or
   rewrite prose only when it is stale, incorrect, genuinely repetitive, or
   inseparable from a deferred coordinate calculation.
5. Prefer incidence, intersection, union, set difference, closure, interior,
   image, preimage, convex hull, metric ball, distance, measure, containment,
   or an extremum over an explicitly displayed feasible set.
6. If no such definition is available without importing the deferred
   calculation, retain the function symbol already used by
   `02_global_notation.tex` or the current canonical paper and cite the unique
   supplying appendix lemma
   immediately with `\zcref`. The body states the domain, codomain, hypotheses,
   and compact value or inequality it uses. The cited appendix lemma gives the
   exact definition, all branches and endpoint conventions, and the proof.
   Only an output that has no established symbol may receive a new semantic
   subscript matching the supplying lemma. Do not rename an established symbol
   merely to encode a lemma name, and do not use an unexplained generic
   function symbol.
7. Do not redesign the notation during reorganization. Consult a numbered
   source for notation only when the canonical paper has no symbol, and do not
   import a legacy compatibility alias that conflicts with the canonical
   notation dictionary. If no canonical abbreviation exists, write the exact
   formula in place unless the fallback rule genuinely requires a new function
   symbol.
8. Keep the paper as short as clarity, completeness, and self-containment
   permit. Relocating a calculation is not a reason to add replacement prose.
   Add a name or explanation only when it materially helps, state shared setup
   once, and do not repeat the same definition in body text, a table, and its
   caption.

Thus the body pairs exact geometric set and extremum definitions with readable
mathematical prose. Words may name and explain a case; equations must define
it. A lemma-linked function is an exceptional typed interface, not permission
to hide a geometric or set-theoretic definition. The appendices evaluate the
body definitions in coordinates and define and evaluate the exceptional
functions when the proof needs a closed form or a calculation.

The appendices will contain the proof-used, fully solved optimization or
feasibility problems, together with brief introductions, geometric
orientation, transitions, and statements of how each result is used. Each
module will state its feasible family and objective, give the exact optimum or
required bound, and include the complete derivation or exact certificate.
Exclude unrelated calculations, not useful exposition. The paper must remain
self-contained: an appendix may cite a numbered `proof/` source for
provenance, but it may not omit an argument on the ground that the repository
contains it elsewhere.

These ingredients are a content checklist, not a requirement to create a long
sequence of titled subsections. When a module is short, combine its purpose,
interface, and result in one compact theorem-and-proof unit. Put shared notation
and setup once before the modules that use it.

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

Moving any of these evaluations does not require deleting its case name,
schematic picture, geometric interpretation, or a short sentence stating what
the calculation proves. Preserve those reader aids in the body when they are
accurate and useful; place calculation-specific exposition with the
calculation in the appendix.

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
A_i&:=\max\{x\in[0,1]:V_i+x(V_{i-1}-V_i)\in T_i\},\\
B_i&:=\max\{x\in[0,1]:V_i+x(V_{i+1}-V_i)\in T_i\},\\
C_i&:=\max\{x\in[0,1]:V_i+x(O-V_i)\in T_i\}.
\end{aligned}
\]

It should also record that the same values are the corresponding suprema for
the open `\(U_i\)`, and should define

\[
N_+:=\bigl|\{i\in\mathbb Z/6\mathbb Z:A_i+B_i>1\}\bigr|.
\]

Likewise, the body should display

\[
\varnothing\ne K\subseteq\mathbb R^2,\qquad K\text{ compact},
\]
\[
\Lambda(K):=
\inf\{s>0:\exists T\,
[T\text{ is a closed equilateral triangle of side }s
\land K\subseteq T]\}.
\]

The support-function expression evaluating `\(\Lambda\)`, the piecewise
closed forms evaluating `\(c_{\max}\)` or `\(C_\pm\)`, and the calculations
proving them belong in the appendices. A named point may stay in the body as
an exact singleton intersection or selected extremum. For example, retain the
established definition `\(\{Q_0\}=\ell_-\cap\ell_+\)`. Its coordinate tuple
and root calculation move to the appendix.

Short final interfaces such as a trace cap, an area-loss lower bound, or
`\(\Lambda(K)\ge 1\)` also remain displayed in the body.

## 2. Historical diagnosis of the audited input

The audited canonical PDF had 91 pages. The technical material was
concentrated in the
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

The repository initially contained historical reader-facing sources
(`02_reader_framework.tex`, `03_strategy1_reader.tex`, and
`05_strategy3_reader.tex`) and an old appendix roadmap. They demonstrate that
a compact-body/technical-appendix layout is feasible.  Their useful text is to
be adapted into the new closure; the superseded files are then deleted rather
than kept beside the canonical paper.

## 3. Canonical organization proposed in the audit

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

This outline is not an instruction to rewrite the body as a bare theorem
ledger. Start from the existing exposition and preserve any paragraph that
gives correct motivation, geometric intuition, case navigation, or a useful
transition. When a paragraph contains both explanation and calculation, keep a
short conceptual version in the body and move the detailed calculation with
its supporting explanation to the appropriate appendix.

There is no target minimum length. A shorter paper is preferable when it
remains readable and self-contained. Do not add examples, restatements,
headings, figures, or prose merely to increase the page count; shorten by
consolidating repeated setup, repeated case descriptions, and duplicate
proofs. Let the exact proof requirements determine the appendix length.

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

Delete the two trace-exact paper-atlas TeX wrapper files.  Retain the fifteen
PNG panels, colocated under `figures/trace_exact_ab/`, and generate them from
the same deterministic preset registry as the standalone interactive
explorer.  Place selected panels directly beside the corresponding geometric
cases instead of restoring an atlas appendix.  Also retain the exact-byte
static `strategy4_core_case_example.png` and verify its SHA-256.  The generated
and static images are illustrative rather than proof-used; a geometric
explanation may use them, but no claim depends on raster inspection.

### Canonical source cleanup

After content migration, the top-level TeX keep set under
`arrange/paper_draft/` is exactly:

- `main.tex` and the six body sources `01_introduction.tex`,
  `02_structure_and_common_geometry.tex`, `03_trace_bounds.tex`,
  `05_area_loss_full.tex`, `06_finite_enclosure_full.tex`, and
  `07_exhaustive_assembly.tex`;
- `A_structural_shared_local_signed_center_optimization.tex`,
  `B_trace_length_optimization.tex`, `C_area_loss_optimization.tex`,
  `D_nonzero_gap_finite_enclosure_optimization.tex`, and
  `E_zero_gap_nine_point_optimization.tex`; and
- `A_zero_gap_exact_certificate.tex`, whose stable filename is retained while
  its input position makes it Appendix F.

Delete every other current top-level paper TeX source after its proof-used
content and labels have been transferred.  Under `figures/`, retain the role
examples, `geometry_roles.tex`, `strategy1_trace_targets.tex`, the two
area-loss images, `tikz_setup.tex`, and `finite_enclosure/fe00` through `fe18`.
Also retain `center_interval_residual.tex`,
`transfer_V_triangle_coordinates.tex`, and
`strategy2_ce1_ce2_n0_all_vd0.png`, which archived proof-paper sources still
reference.  Retain the fifteen generated `trace_exact_ab/*.png` panels and the
SHA-256-pinned static `strategy4_core_case_example.png`.  Delete every other
historical publication figure, including the twenty-one
`strategy2_*_skeleton.tex` files, four `signed_*.tex` diagrams, and three
unused `new_*` diagrams.

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

In every routing, classification, or terminal-subcase table, case membership
must be specified by an exact symbolic block at the left of the row. Use the
full available table width and split independent data into columns for
`\(N_{\mathrm{gap}}\)`, `\(N_+\)`, `\(N_E(T_C)\)`, the already defined
counts `\(d,t\)`, normalized indices, and incidence predicates when that
remains readable. If more conditions are needed than fit across the page,
stack them on separate lines within a cell or continue the case on additional
table lines. This is a local rule for the decision-gate columns, not a rule
that the entire table or surrounding paper be formula-only. Reuse the paper's
established notation: in particular, use `\(N_+\)` directly rather than
introducing a new index set for the same condition. Do not add a table-only
alias when an existing symbol or an exact formula already expresses the
condition.

Each visual line in a mathematical table cell must contain at most one
equation, inequality, membership statement, cardinality condition, or
quantified predicate. Do not join independent predicates on one line with a
comma, semicolon, or `\(\qquad\)`, and keep each individual statement intact
on one visual line. Give a long statement a wider column or a full-width
continuation line; if an exact definition is too long for a useful table, state
it immediately beside the table and cite it from the row. Prefer a full-width
table or multiline cells to reduced type or crowded math. This is a layout
rule only: it must not cause new mathematical content, duplicate definitions,
or extra explanatory paragraphs.

A predicate cell may contain `\((d,t)=(0,0)\)`, `\(d=0\)`, `\(t\le2\)`, or
`\(\tau\in\{1,5\}\)`. It must not rely on a verbal surrogate such as “all
Vd0,” “at most two T3-like roles,” or “an adjacent Vd role.” Those phrases may
appear, when useful, in a later **geometric name** or **mechanism** column once
the exact predicate has been stated. One concise name or mechanism phrase is
normally enough. The symbols `\(\sigma\)` and
`\(\tau\)` are local to the one-Vd placement register; define them there by

\[
\{\sigma\}:=\{i\in\mathbb Z/6\mathbb Z:A_i+B_i>1\},
\]
\[
\{\tau\}:=
\{i\in\mathbb Z/6\mathbb Z:
(o(T_i),n(T_i))\in\{(1,1),(1,2)\}\}.
\]

Display the relations used by each row exactly, for example

\[
A_\sigma+B_\sigma>1.
\]
\[
A_i+B_i\le1\quad(i\ne\sigma).
\]

Put logically distinct disjuncts that route to different arguments in separate
rows. Define any genuinely necessary abbreviation immediately before the
table. Retain concise prose in captions, introductions, geometric-name and
mechanism columns, and explanations after the table. This rule applies to case
tables, not to notation or bounds tables.

#### Recommended locations for words and symbolic case data

A useful case-table order, combining the two prose columns when space is
tight, is:

`exact gap data | exact reach/type data | exact placement data | name/mechanism | exact conclusion`.

The first three columns determine membership in the row and therefore contain
equations, inequalities, membership statements, cardinalities, or logical
combinations. The later columns tell the reader what the geometry is and why
the row is useful. In particular:

- In `tab:routing`, keep `\(N_{\mathrm{gap}}\)`, `\(N_+\)`, `\((d,t)\)`,
  and `\(N_E(T_C)\)` in exact gate columns, while retaining “trace length,”
  “area loss,” and “finite enclosure” as route names.
- In the C-type and V-type classification tables, retain the established names
  CE0, CE1, CE2, Vd0, Vd1, Vd2, and T3-like beside their exact definitions.
  These are a dictionary, not a decision table in which prose is replacing a
  predicate.
- In the finite-enclosure table, state the A--F predicates first and then keep
  the memorable names “complementary gap,” “CE2 short ray,” “transverse
  seven-point witness,” “T3-like supported tail,” “Vd1 supported tail,”
  “adjacent radial separation,” “nonadjacent radial separation,” and
  “zero-gap nine-point obstruction.”
- In the one-Vd placement register, let the exact `\(\sigma,\tau\)`, type,
  midpoint, and adjacency predicates choose the row. A later column or the
  following sentence may call the construction the “Vd1 two-chart
  replacement” and explain whether it routes to separation, a supported tail,
  or a replacement.
- In `07_exhaustive_assembly.tex`, preserve the zero-gap-first/nonzero-gap
  narrative, transition sentences, and names of the closing methods. They are
  proof navigation and should not be converted into a wall of implications.
- In figures and their captions, keep geometric labels and short explanations
  of what the reader should see. Remove coordinate or computational
  annotations only when those details move to an appendix.
- In `thm:boundary-trace-table` and every other bounds table, put each bound or
  hypothesis on its own visual line. A descriptive bound name may remain in a
  separate cell.

For example, the first three cells of a finite-enclosure row may be
`\(N_{\mathrm{gap}}=1\) | \(N_+=1\) | \((d,t)=(0,0)\)`. Each cell contains
one equation on one line. The row may then use “transverse seven-point
witness” as its geometric name, followed
by the exact definition of `\(K_{\mathrm{tr}}\)` and the conclusion
`\(\Lambda(K_{\mathrm{tr}})\ge1\)`. Similarly,
`\(\sigma=0\)` and `\(\tau\in\{1,5\}\)` occupy separate columns or separate
lines before the name “adjacent radial separation.” The name helps the reader
remember the case; the formulas determine the case.

The condensed displays later in this report are mathematical inventories, not
literal table-cell layouts. When implementing them in the manuscript, unbundle
every comma- or `\(\qquad\)`-separated condition into its own table line or
cell. Factor shared assumptions above the table and cite adjacent definitions
instead of repeating them in every row; this keeps the table legible without
making the paper longer.

Edit as follows:

- Keep the exact global definition in the body:

  \[
  O:=(0,0),\qquad
  V_i:=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right),
  \]
  \[
  H:=\conv\{V_0,\ldots,V_5\},\qquad
  e_{i,i+1}:=[V_i,V_{i+1}],\qquad r_i:=[O,V_i],
  \qquad M_i:=\frac12V_i,
  \]
  \[
  S:=\partial H\cup\bigcup_{i=0}^5r_i.
  \]

  These are the manuscript's established foundational definitions, not a
  deferred local calculation. Reserve the established `\(\mathsf R\)` for
  counterclockwise rotation through `\(2\pi/3\)` in the enclosure gauge.
- Keep `\(N_+\)` defined only from actual `\(A_i+B_i>1\)`.
- Keep the established classification variables and case counts exactly:

  \[
  o(T_i):=
  \bigl|\{P\in\mathbb R^2:P\text{ is a vertex of }T_i,\ P\notin H\}\bigr|,
  \qquad
  n(T_i):=
  \bigl|\{j\in\{i-1,i+1\}:\Haus(T_i\cap r_j)>0\}\bigr|,
  \]
  \[
  d:=\bigl|\{i\in\mathbb Z/6\mathbb Z:
  (o(T_i),n(T_i))\in\{(1,1),(1,2)\}\}\bigr|,
  \qquad
  t:=\bigl|\{i\in\mathbb Z/6\mathbb Z:
  (o(T_i),n(T_i))=(2,1)\}\bigr|,
  \qquad N_{\mathrm{sp}}:=d+t.
  \]

  The four displayed type rows remain
  `\(\{(1,0),(2,0)\},\{(1,1)\},\{(1,2)\},\{(2,1)\}\)` in the
  established Vd0, Vd1, Vd2, T3-like order.
- Keep the exact boundary-gap set definition together with the elementary
  picture; retain a short explanation that a singleton remains uncovered by
  the two incident open V triangles.
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

While splitting these sources, preserve useful section openings, transition
sentences, geometric proof ideas, and warnings about how a construction is
used. Relocate the coordinate calculation, not the reader's map of the
argument. If a paragraph mixes both, rewrite it into a short body explanation
and a fuller appendix introduction instead of deleting it wholesale.

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

Keep exact reach definitions in the body. Retain the edge parametrization
`\(X_i\)` and write the three `\(\max\)` definitions on the closed `\(T_i\)` exactly as in
Section 1 of this report, together with their equal open-`\(U_i\)` suprema.
The initial-segment property is a compact lemma, not a prose substitute for
the definitions. Whenever selected demands appear, display
`\(a_i\le A_i\)`, `\(b_i\le B_i\)`, and `\(c_i\le C_i\)`.

Also retain the concise edge and gap definitions from
`02_structural_reductions.tex:531–548`:

\[
X_i(x):=V_i+x(V_{i+1}-V_i),
\]
\[
J_i:=e_{i,i+1}\setminus
\bigl((U_i\cap e_{i,i+1})\cup(U_{i+1}\cap e_{i,i+1})\bigr).
\]

Follow this display with the useful name: `\(J_i\)` is the boundary gap on
`\(e_{i,i+1}\)`. The sentence helps the reader; the set difference remains
the definition.

The proposition may then identify
`\(J_i=X_i([B_i,1-A_{i+1}])\)` when
`\(B_i+A_{i+1}\le1\)`, including equality as a singleton, and
`\(J_i=\varnothing\)` otherwise. This definition must use the open `\(U\)`
traces. Define the canonical gap count by

\[
N_{\mathrm{gap}}:=
\left|\left\{i\in\mathbb Z/6\mathbb Z:
J_i\ne\varnothing,\ J_i\subseteq U_C\cap e_{i,i+1}
\right\}\right|.
\]

Under the hypothetical-cover assumption, `lem:gap-exhaustion` gives

\[
N_{\mathrm{gap}}=
\bigl|\{i\in\mathbb Z/6\mathbb Z:J_i\ne\varnothing\}\bigr|.
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

Give the strict handoff its exact selector in the body:

\[
\xi_i\in(1-A_{i+1},B_i),\qquad
a_i:=1-\xi_{i-1},\qquad b_i:=\xi_i,
\]
\[
0<a_i<A_i,\qquad0<b_i<B_i,\qquad
a_i^2+a_ib_i+b_i^2<1.
\]

Then explain briefly that `\(\xi_i\)` is selected in the overlap of the two
adjacent open edge traces, so the resulting demands are strict. Appendix A
proves that the intervals are nonempty and proves the clauses preserving one
or at least two selected supercritical roles.

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
exact formula diagrams at lines 349–381 leave the canonical paper.  After the
proof-used calculation has been incorporated into Appendix A, delete these
unreferenced publication diagrams rather than retaining a second source form.

Do not rely on a qualitative paragraph alone. Keep the readable CE1/CE2
explanation and pair it with the exact classification definition in the body:

\[
N_E(T_C):=
\bigl|\{i\in\mathbb Z/6\mathbb Z:
  \Haus(T_C\cap e_{i,i+1})>0\}\bigr|.
\]
\[
T_C\text{ is }\CEzero\iff N_E(T_C)=0,\qquad
T_C\text{ is }\CEone\iff N_E(T_C)=1,\qquad
T_C\text{ is }\CEtwo\iff N_E(T_C)=2.
\]

For CE1 and CE2, retain the compact exact consequence

\[
\bigl|T_C\cap\{M_0,\ldots,M_5\}\bigr|=1.
\]

Retain the concise geometric explanation that a point contact has zero trace
length and hence does not create a second positive trace. A simplified
CE1/CE2 schematic may remain if it makes this distinction immediate. The
signed parameters, exact trace endpoints, and radial exits remain in Appendix
A.

The final CE1 and CE2 boundary trace caps may appear in the body trace table.

### 4.4 Trace length

Replace the body imports in `03_trace_bounds.tex` with an updated compact trace
source based on, but not copied from, `03_strategy1_reader.tex`.

Keep in the body:

- `\(L_E(T)=\Haus(T\cap E)\)` and the subadditivity principle;
- the perimeter/skeleton target figure;
- the final trace-cap table from `thm:boundary-trace-table`;
- the positive-support rescuer as its exact labeled implication, with symbolic
  hypotheses and conclusion together with its readable mechanism name;
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

Use `05_strategy3_reader.tex` only as structural scaffolding. Retain the
readable progression “local area loss,” “T3-like loss,” and “cyclic
accumulation” around the exact statements below. These mechanism names explain
the proof architecture without replacing any hypothesis. Keep in the body:

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
  \[
  a,b\in[0,1],\qquad\mathcal T(a,b)\ne\varnothing.
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
  (o(T_i),n(T_i))=(2,1),\qquad
  0\le a_i\le A_i,\quad0\le b_i\le B_i,\quad
  0\le\mu\le\frac12,\quad a_i,b_i\ge\mu
  \Longrightarrow \mathcal L(T_i)\ge2\mu-4\mu^2;
  \]
- the cyclic certificate with the strict-handoff data

  \[
  \xi_i\in(1-A_{i+1},B_i),\qquad
  a_i:=1-\xi_{i-1},\qquad b_i:=\xi_i,
  \]
  \[
  0<a_i<A_i,\qquad0<b_i<B_i,\qquad
  a_i^2+a_ib_i+b_i^2<1,
  \]

  and its two exact hypotheses and conclusions

  \[
  \bigl|\{i\in\mathbb Z/6\mathbb Z:a_i+b_i>1\}\bigr|\ge2
  \Longrightarrow
  \sum_{i=0}^5\mathcal L(T_i)>1,
  \]
  \[
  \begin{gathered}
  \bigl|\{i\in\mathbb Z/6\mathbb Z:a_i+b_i>1\}\bigr|=1,\\
  \forall i\in\mathbb Z/6\mathbb Z,\quad
  (o(T_i),n(T_i))\in\{(1,0),(2,0),(2,1)\},\\
  \exists j\in\mathbb Z/6\mathbb Z,\quad
  (o(T_j),n(T_j))=(2,1)
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

Keep the following compact exact definitions and conclusions, and surround
them with the short geometric names and explanations indicated below. The
prose accompanies these interfaces; it does not replace them with an informal
optimization paraphrase.

For every nonempty compact `\(K\)`, display

\[
\varnothing\ne K\subseteq\mathbb R^2,\qquad K\text{ compact},
\]

\[
\mathbb B(X,r):=\{Y\in\mathbb R^2:\lVert Y-X\rVert\le r\}
\qquad(X\in\mathbb R^2,\ r\ge0).
\]

\[
\Lambda(K):=
\inf\{s>0:\exists T\,
[T\text{ is a closed equilateral triangle of side }s
\land K\subseteq T]\}.
\]

Follow the definition with a short interpretation: `\(\Lambda(K)\)` is the
least equilateral enclosure side for `\(K\)`.

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

Normalize at `\(V_0\)` and retain the canonical anchor-hull notation

\[
K(a,b,c):=\conv
\{V_0,X_5(1-a),X_0(b),(1-c)V_0\},
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
\[
M_c(a):=\max\{b\in[0,1]:(a,b,c)\in\mathcal A\}
\qquad(0\le a,c\le1).
\]

Use “four-anchor hull” for `\(K(a,b,c)\)` when a short name is useful, and
describe `\(c_{\max}\)` and `\(M_c\)` as its two extremal reach functions.
The displayed feasible sets remain their definitions.

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
\exists T\ [T\text{ is a closed unit equilateral triangle},\\
\{V_0,X_5(1-a),X_0(b),(1-c)V_1\}\subseteq T]
\end{array}
\right\},
\]
\[
C_-(a,b):=C_+(b,a),
\qquad 0\le a,b\le1,\quad a+b\le1.
\]

The short phrase “neighboring-arm capacities” should stay beside
`\(C_+,C_-\)`; Appendix D supplies their coordinate evaluation.

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
\Haus(T_{i-1}\cap r_i)>0&\Longrightarrow
a_{i-1}+b_{i-1}\le1,\\
\Haus(T_{i+1}\cap r_i)>0&\Longrightarrow
a_{i+1}+b_{i+1}\le1.
\end{aligned}
\]

\[
\Gamma_i:=\max\Bigl(
\{c_{\max}(a_i,b_i)\}
\cup\{C_+(a_{i-1},b_{i-1}):\Haus(T_{i-1}\cap r_i)>0\}
\cup\{C_-(a_{i+1},b_{i+1}):\Haus(T_{i+1}\cap r_i)>0\}
\Bigr),
\qquad D_i:=(1-\Gamma_i)V_i.
\]

Afterward, say that `\(\Gamma_i\)` is the largest applicable capacity and
`\(D_i\)` is the resulting point on `\(r_i\)`. This is useful interpretation,
not a replacement for the type-aware maximum above.

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

The exact gap `\(J_i\)` is the set difference defined in Section 4.2; do not
replace it by “the closed complement.” Likewise, every finite witness must be
displayed as a set. For example, with
`\(P_j:=(1-C_j)V_j\)`, retain

\[
K_{\mathrm{tr}}:=
\{O,M_0,X_0(B_0),X_0(1-A_1),P_2,P_3,P_4\}.
\]

Every other named point must be defined by an exact singleton intersection or
selected extremum, and every witness hull by `\(\conv\)` of its displayed
generators. If an optimizer on `\(F\)` is not unique, retain the exact optimizer
set, for example
`\(\{x\in F:f(x)=\inf_{y\in F}f(y)\}\)`, or give an exact tie-breaking
selector. Coordinates, radicals, and pointwise verification move to the
appendix.

Rewrite the finite-enclosure case table from the following exact register.
The register is compact for auditing; in the typeset A--F table, unbundle its
packed hypotheses so each equation or predicate occupies its own cell line.
State common assumptions once above the table rather than repeating them.
For A–E and the replacement router, assume

\[
S\subseteq U_C\cup\bigcup_{i=0}^5U_i.
\]

Row F retains the stronger hypothetical cover of all of `\(H\)`.

Retain the A--F labels and the descriptive headings below as reader-facing
navigation. They are useful names, while the displayed predicates remain the
authoritative case definitions. Write every reflected local orientation as the
corresponding disjunction; explain the symmetry in prose without giving the
disjunction a new symbolic alias. The symmetry already established for
`\(c_{\max}\)` gives

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
J:=J_0=X_0([\ell,r]),\qquad
\ell:=B_0,\qquad r:=1-A_1,\qquad0<\ell\le r<1,
\]
\[
p:=1-r,\qquad q:=\ell,
\]
\[
0<p,q<1,\qquad p+q\le1,\qquad
c_*:=c_{\max}(p,q).
\]
\[
\mathcal D_{(\sqrt3/2)(1-c_*)}:=
\left\{x\in\mathbb R^2:
\lVert x-O\rVert\le\frac{\sqrt3}{2}(1-c_*)\right\}.
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
singleton gap.  The body closure derives the containment from the one-gap
adapter, type-aware radial forcing, and common-pair domination, and then uses
the enclosure calculation supplied by Appendix D.

**B. Two actual gaps in CE2.** Normalize the two positive C-triangle traces to
`\(e_{5,0}\)` and `\(e_{0,1}\)`, and define

\[
p:=\min\{x\in[0,1]:X_5(x)\in T_C\},\qquad
q:=1-\max\{x\in[0,1]:X_0(x)\in T_C\},
\]
\[
0<p,q<1,\qquad p+q<1,\qquad
c_*:=c_{\max}(p,q),
\qquad D_2:=(1-c_*)V_2,\quad D_4:=(1-c_*)V_4.
\]

\[
N_E(T_C)=2,\qquad N_{\mathrm{gap}}=2,\qquad
N_+\in\{0,1\},\qquad d=0,\qquad N_++t\le2,
\]
\[
N_+t=0,
\]
\[
\forall i\in\{1,2,3,4,5\}\quad
[(p\le A_i\land q\le B_i)\lor(q\le A_i\land p\le B_i)],
\]
\[
c_{\max}(q,p)=c_{\max}(p,q)=c_*,\qquad
D_2,D_4\in U_C,\qquad \{D_2,D_4\}\nsubseteq T_C.
\]

Appendix D supplies the two-gap common-pair adapter, evaluates the signed CE2
problem, and proves the final noncontainment; the signed parameters do not
appear in this body row.

**C. One gap, one supercritical role, and all Vd0.** Rotate the unique
supercritical role to `\(T_0\)`. Keep this descriptive heading, followed by
the exact placement conditions

\[
N_{\mathrm{gap}}=1,\qquad N_+=1,\qquad
N_E(T_C)\in\{1,2\},\qquad(d,t)=(0,0),\qquad
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
\]
\[
A_0+B_0>1,\qquad A_i+B_i\le1\quad(1\le i\le5),
\]
\[
\bigl[J=J_0=X_0([B_0,1-A_1])\bigr]
\lor
\bigl[J=J_5=X_5([B_5,1-A_0])\bigr].
\]

After reflection select the first branch and put

\[
J:=J_0=X_0([\ell,r]),\qquad
\ell:=B_0,\qquad r:=1-A_1,\qquad0<\ell\le r<1,
\]
\[
P_i:=(1-C_i)V_i,\qquad
K_{\mathrm{tr}}:=\{O,M_0,X_0(\ell),X_0(r),P_2,P_3,P_4\}.
\]

Retain

\[
K_{\mathrm{tr}}\subset U_C,\qquad
\Lambda(K_{\mathrm{tr}})\ge1.
\]

Do not add `\(P_0,P_1,P_5\)` to this witness. Appendix D contains the CE1 and
CE2 calculations establishing the same enclosure interface.

**D. T3-like or Vd1 supported tail.** Keep “supported tail” as the shared
geometric name and give the two normalized adapters separate exact hypothesis
rows. The T3-like row is

\[
N_{\mathrm{gap}}=1,\quad N_+=1,\quad(d,t)=(0,1),\quad
N_E(T_C)\in\{1,2\},\quad
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
\]
\[
(o(T_0),n(T_0))=(2,1),
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
(o(T_0),n(T_0))=(1,1),\qquad A_0+B_0<\frac12.
\]
\[
(o(T_i),n(T_i))\in\{(1,0),(2,0)\}
\qquad(1\le i\le5).
\]

The shared exact orientation condition is

\[
\bigl[M_1\in T_0\land A_1+B_1>1\bigr]
\lor
\bigl[M_5\in T_0\land A_5+B_5>1\bigr].
\]

After reflection select the first branch. Then

\[
U_C\cap\bigcup_{k=1}^4e_{k,k+1}=\varnothing.
\]

Both adapters use the established interval coordinates

\[
T_0\cap r_1=\{V_1+x(O-V_1):c\le x\le u\},\qquad
0<c\le\frac12\le u<1,\qquad
\varepsilon:=1-u,\qquad C_1\ge c.
\]

Retain the canonical strict-supercritical envelope

\[
M_c^{\mathrm{sup}}:=
\sup\{M_c(a):0\le a\le1,\ M_c(a)>1-a\}
\qquad\left(0\le c<\frac12\right),
\]
\[
M_{1/2}^{\mathrm{sup}}:=\frac12,
\qquad M:=M_c^{\mathrm{sup}}.
\]

The value at `\(c=1/2\)` is the continuous extension, not the supremum of
an empty strict feasible set. The adapters prove

\[
\varepsilon V_1\in U_C,\qquad
A_0\le1-M,\qquad
\frac{A_0}{A_0+\varepsilon}\le1-M,
\]
\[
\begin{aligned}
(o(T_0),n(T_0))=(2,1)&\Longrightarrow A_0+\varepsilon\le1,\\
(o(T_0),n(T_0))=(1,1)&\Longrightarrow A_0+\varepsilon<1,
\end{aligned}
\]
\[
B_1<M,\qquad A_i+B_i\le1\quad(2\le i\le5).
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
\{\sigma\}=\{i\in\mathbb Z/6\mathbb Z:A_i+B_i>1\},\qquad
\{\tau\}=\{i\in\mathbb Z/6\mathbb Z:
(o(T_i),n(T_i))\in\{(1,1),(1,2)\}\},
\]
\[
\sigma=0,\qquad\tau\in\{1,2,3,4,5\},\qquad
(A_\tau+B_\tau)<\frac12,\qquad
(o(T_j),n(T_j))\in\{(1,0),(2,0)\}
\quad\bigl(j\in(\mathbb Z/6\mathbb Z)\setminus\{\tau\}\bigr).
\]

For the routed radial arm `\(r_i\)`, use the established separation
interface with exact extremal definitions

\[
d_C:=\max\{x\in[0,1]:xV_i\in T_C\},
\]
\[
c_{\mathrm{loc}}:=
\sup\{s\in[0,1]:V_i+s(O-V_i)\in
U_{i-1}\cup U_i\cup U_{i+1}\}.
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

For the adjacent adapter, retain the name “adjacent radial separation” beside
the exact subcase condition

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

For `\(I\subseteq[0,1]\)` either empty or a closed interval, and
`\(0\le p\le1\)`, use the established residual operator

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

The two-chart Vd1 replacement is a router, not a seventh terminal. Keep that
sentence because it prevents a structural misunderstanding. Its exact
placement block before the fresh local renumbering is

\[
N_E(T_C)=2,\qquad N_{\mathrm{gap}}\in\{1,2\},\qquad
N_+=1,\qquad(d,t)=(1,0),
\]
\[
T_C\cap\{M_0,\ldots,M_5\}=\{M_0\},
\]
\[
\{\sigma\}=\{i\in\mathbb Z/6\mathbb Z:A_i+B_i>1\},\qquad
\{\tau\}=\{i\in\mathbb Z/6\mathbb Z:
(o(T_i),n(T_i))\in\{(1,1),(1,2)\}\},
\]
\[
\sigma,\tau\in\{1,2,3,4,5\},\qquad
\sigma\ne\tau,\qquad \sigma-\tau\equiv\pm1\pmod 6,
\]
\[
(o(T_\tau),n(T_\tau))=(1,1),\qquad M_\sigma\in T_\tau.
\]

Fresh cyclic renumbering and, if necessary, reflection make
\((\tau,\sigma)=(0,1)\). Thus \(T_0\) is the Vd1 role and \(T_1\) is the
supercritical Vd0 role. The resulting exact input is

\[
S\subseteq U_C\cup\bigcup_{i=0}^5U_i,\qquad
N_E(T_C)=2,\qquad N_{\mathrm{gap}}\in\{1,2\},\qquad
N_+=1,\qquad(d,t)=(1,0),
\]
\[
(o(T_0),n(T_0))=(1,1),\qquad A_0+B_0<\frac12,\qquad
M_1\in T_0,\qquad A_1+B_1>1,
\]
\[
A_i+B_i\le1\quad(i\ne1),\qquad
(o(T_i),n(T_i))\in\{(1,0),(2,0)\}\quad(1\le i\le5),
\]
\[
U_C\cap e_{0,1}=\varnothing,\qquad
\Haus(T_j\cap r_k)=0
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

define the recomputed output gap rank directly:

\[
N'_{\mathrm{gap}}:=
\left|\left\{i\in\mathbb Z/6\mathbb Z:
e_{i,i+1}\setminus
\bigl((U'_i\cap e_{i,i+1})\cup(U'_{i+1}\cap e_{i,i+1})\bigr)
\ne\varnothing
\right\}\right|.
\]
\[
N'_{\mathrm{gap}}\in\{0,1,2\}.
\]

Use the established actual-reach functions, without introducing primed reach
aliases:

\[
\begin{aligned}
A(T'_i)&:=\max\{x\in[0,1]:V_i+x(V_{i-1}-V_i)\in T'_i\},\\
B(T'_i)&:=\max\{x\in[0,1]:V_i+x(V_{i+1}-V_i)\in T'_i\},\\
C(T'_i)&:=\max\{x\in[0,1]:V_i+x(O-V_i)\in T'_i\}.
\end{aligned}
\]

Retain

\[
S\subseteq U_C\cup\bigcup_{i=0}^5U'_i,\qquad
N_E(T_C)=2,\qquad
(o(T'_i),n(T'_i))\in\{(1,0),(2,0)\}\quad(0\le i\le5),
\]
\[
A(T'_i)+B(T'_i)\le1\quad(0\le i\le5),
\]
\[
A(T'_0)+B(T'_0)=A(T'_1)+B(T'_1)=1-\varepsilon<1,
\]
\[
\bigl(A(T'_i),B(T'_i),C(T'_i)\bigr)=(A_i,B_i,C_i)
\quad(2\le i\le5),\qquad
\bigl|\{i\in\mathbb Z/6\mathbb Z:
A(T'_i)+B(T'_i)>1\}\bigr|=0.
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

For `\(N'_{\mathrm{gap}}=0\)`, invoke `prop:length-branches` row Z0.  For
`\(N'_{\mathrm{gap}}=1\)`, reapply the one-gap common-pair adapter to the
primed actual reaches and then invoke the row-A branch of
`prop:new-nplus-zero-gap-closures`.  For
`\(N'_{\mathrm{gap}}=2\)`, reapply the two-gap common-pair adapter and then
invoke the row-B branch of that proposition.  Thus the hypotheses used after
replacement are rederived from the output configuration rather than carried
over from the input.

Do not assert `\(N'_{\mathrm{gap}}=N_{\mathrm{gap}}\)`. Both replacement charts
and all strict epsilon inequalities belong in Appendix D.

The final body table must split this register into as many symbolic hypothesis
columns or stacked table lines as needed. Each visual line contains at most one
equation, inequality, membership statement, quantified predicate, cardinality
condition, or logical formula; distinct predicates are never packed together
with commas or `\(\qquad\)`, and each statement stays intact on its own line.
Use the full text width, or a landscape/full-width table when the publication
format supports it, before reducing type size. If the row is still too wide,
use multiline cells for separate statements or give a long statement a
full-width continuation line. A verbal name must not replace a predicate in
the identifying block. After that block, retain one short geometric-name or
mechanism field and an exact conclusion field. Cite the adjacent definitions
instead of copying them into every row.
A family name is a useful reader handle, but it is not by itself a
mathematical interface. These layout choices must organize the existing
content, not lengthen it.

Keep schematic versions of the roadmap, complementary-gap, CE2 short-ray,
transverse-witness, zero-gap witness, and support-arc figures, paired with the
exact adjacent definitions. Preserve descriptive arrows, geometric labels, and
captions that tell the reader what to notice. Remove only coordinate and
computational annotations from the body. Move figures whose purpose is to
display exact signed parameters, evaluated neighbor-capacity branches, disk
formulas, or CE1 algebra to the appendices.

### 4.7 Nonzero-gap optimization

Move to Appendix D:

- the derivation of the gap endpoint identities and the common-pair proof from
  `06_finite_enclosure_full.tex:73–115`; retain `\(J_i\)` and every named
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
once. Remove the unused quarter-radial derivation from the canonical proof, but
retain a brief geometric remark or schematic if it genuinely motivates the
chosen witness.

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
  `06e_direct_local_proof_details.tex` to Appendix D, while removing its unused
  quarter-radial calculation and leaving no piecewise/root catalogue in the
  body; retain any concise geometric motivation that remains relevant;
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
The current paper contains only a prose summary. Keep that summary, revised as
needed, as the reader's roadmap to the two charts; add the self-contained exact
appendix calculation rather than replacing the roadmap. The appendix must
preserve:

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
second zero-gap notation layer. Retain the name “zero-gap nine-point
obstruction.” Under a hypothetical cover, its exact symbolic body row is

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
sixteen on `\(L_0,L_1\)`), and both verifier references remain exact. Retain
the labels `lem:paper-branchwise-cbar`, `lem:paper-residual-to-overlap`, and
`thm:paper-exact-mixed-certificate`. Correct only stale navigation prose:

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

1. **Geometric purpose.** In one or two sentences, name the configuration and
   explain what the optimization supplies to the body.
2. **Exact interface.** Copy or cite the body's geometric or set-theoretic
   definition. For a lemma-linked fallback function, cite its typed body
   declaration and give its exact definition in this unique appendix lemma.
   Do not replace either form by a verbal paraphrase; use prose alongside it.
3. **Variables and feasible set.** Introduce the evaluation coordinates,
   inequalities, open versus closed endpoint conventions, type restrictions,
   and selected
   connected component.
4. **Objective.** State the maximum reach, maximum trace, minimum area loss,
   minimum enclosure side, or strict feasibility margin being determined.
5. **Exact result.** State the optimum or sufficient exact bound, with all
   endpoint strictness.
6. **Solution.** Give the full support, algebraic, or certificate proof, using
   short transitions that explain the geometric meaning of major steps.
7. **Body consequence.** Name the compact body proposition supplied by the
   solved problem.

This format keeps the appendices focused solved optimization modules, with
enough orientation prose to remain readable, while leaving the complete proof
inside the published paper.

The seven items are a checklist, not seven mandatory titled subsections. A
short module should combine them into a compact introduction, statement, and
proof. Shared coordinates, notation, and feasible-set setup appear once at the
start of the relevant appendix and are cited thereafter; do not repeat them to
make every module artificially stand-alone.

No relocated calculation may be pasted between modules as background algebra.
It must belong to exactly one named module with an explicit feasible set,
objective or feasibility question, exact result, and cited body consequence.

Use one theorem-linkage pattern throughout: the body owns each compact public
labeled theorem; a separately labeled appendix lemma supplies its full
optimization calculation; and the body proof cites that appendix lemma before
giving the short exact implication and, if useful, one explanatory sentence.
Never repeat the public theorem label
in the appendix.

For every fallback function, retain the symbol used by the canonical paper
and cite the supplying appendix lemma immediately with `\zcref`. If the
canonical paper has no symbol, use the current numbered source only when its
symbol does not conflict with the canonical notation dictionary. Only when no
established symbol exists may a new semantic subscript be introduced; its stem
must match the supplying appendix lemma's title and label. Do not place a raw
label key, a rendered lemma number, or `\zcref` itself inside the function
symbol.

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
- current nonzero-gap terminals: `2018`, `4013_new`, `4101_new`, `4102_new`,
  `4103`, `4132`, and `4140_new` (Proven);
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
   convention, rebuild case-table subcase blocks as exact symbolic columns
   with at most one predicate per visual line, using full table width or
   stacked cells as needed. Pair them with one concise case-name/mechanism
   field, without repeated formulas or redundant prose. Resolve all forward
   references, and update abstract, organization prose, captions, appendix
   guide, dependency metadata, and closure checks.
6. Once every needed statement, proof, label, and figure reference is present
   in the new closure, delete every superseded top-level paper TeX source, the
   two paper-atlas TeX wrappers, and the unreferenced historical publication
   figures.  Do not delete anything under `proof/`; retain the three figure
   assets still referenced by archived proof-paper sources, the fifteen
   trace-exact panels, and the pinned static core-case image.
7. Refactor the trace-asset generator so one registry produces the standalone
   explorer, preset JSON, and fifteen colocated PNG panels.  Remove references
   to the deleted atlas wrappers from interactive checks and the dependency
   graph, while mechanically checking case identifiers, actual-reach
   supercritical counts, singleton-inclusive gaps, and role counts.
8. Build the paper and inspect both the normal and proof-free renderings. The
   proof-free rendering should preserve a coherent chain of exact definitions,
   hypotheses, and implications rather than disconnected theorem labels or
   prose substitutes for definitions.
9. Run every required repository check and the exact certificate programs,
   then regenerate publication artifacts only after all checks pass.
10. Validate the rebuilt canonical PDF, replace the tracked publication PDF
   with those exact validated bytes, and rerun the semantic/render checks.
   Measure the final page count; review and change the audited CI's then-current
   `84–104` bound only if the intentional measured output requires it.  The
   resulting reorganized 91-page publication uses the tight expected interval
   `89--93`.

## 9. Verification commands

Run the repository-required checks:

```bash
python -m pip install -r arrange/_support/requirements.txt
python proof/check.py
python interactive/generate.py --trace-assets --check
python interactive/generate.py --dependency-graph --check
python interactive/check.py
python arrange/build.py --all
```

If the working checkout contains environment-owned top-level directories such
as `.agents`, `.codex`, or an audit virtual environment, run the structural
check in a clean temporary snapshot of the tracked tree.  Do not delete those
environment directories and do not weaken the repository allowlist for them.

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
references. Inspect every routing and case table at the final page size:
confirm one mathematical statement per visual cell line, no crowded or
clipped formulas, readable type, and no repeated setup added solely to fill
the widened layout.

For the publication artifact, validate the clean build before installing it,
then confirm that the tracked and rebuilt PDFs agree semantically:

```bash
python arrange/_support/verify_pdf_render.py arrange/_build/canonical.pdf
cp arrange/_build/canonical.pdf arrange/paper_draft/main.pdf
python arrange/_support/compare_pdfs_semantically.py arrange/paper_draft/main.pdf arrange/_build/canonical.pdf --dpi 144
```

Record the measured page count. Removing the atlas wrappers while placing
selected explanatory panels beside their cases changes that count and could
cross the audited workflow's former hard-coded `84–104` range; update the
bound only after inspecting the intended final PDF, and keep it as narrow as
the publication policy allows.  The final reorganized canonical paper is 91
pages, the proof-free paper is 51 pages, and the corresponding expected CI
interval is `89--93`.
If the correct concise paper falls below the current lower bound, change the
bound; never add filler, duplicate exposition, or unnecessary figures merely
to satisfy a page-count floor.

## 10. Acceptance criteria

The reorganization is complete only when:

- every set, scalar, function, selector, and witness used in the body either
  has an exact geometric or set-theoretic definition at first use or is an
  exceptional typed function with an explicit domain, codomain, hypotheses,
  its established canonical symbol, and an immediate `\zcref` to its unique
  defining appendix lemma; only a genuinely unnamed output receives a new
  semantic lemma-matching subscript, and no essential object is defined only
  by descriptive prose;
- every `\(\min\)`, `\(\max\)`, `\(\inf\)`, or `\(\sup\)`, and every exact
  optimizer set, has an explicit feasible set and, where relevant, all actual
  V-type restrictions;
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
  across multiple columns or stacked table lines where needed; each visual
  cell line contains at most one equation, inequality, membership statement,
  cardinality condition, or quantified predicate, each such statement remains
  intact on that line, and distinct predicates are not joined there by a
  comma, semicolon, or `\(\qquad\)`; the table uses its available width,
  separate multiline-cell lines, or full-width continuation rows rather than
  crowded or reduced-size math;
  no verbal surrogate replaces a predicate, no new alias replaces an
  established quantity such as `\(N_+\)`, and readable case names and
  mechanism descriptions remain in separate columns, headings, captions, or
  adjacent prose;
- useful section introductions, normalization explanations, theorem names,
  figure captions, proof-roadmap transitions, and short geometric
  interpretations have been retained or rewritten rather than deleted merely
  because an exact display is present;
- the rewrite is no longer than clarity, self-containment, and the complete
  proof require: shared setup is stated once, adjacent definitions are cited
  rather than copied into every table row, repeated proofs and explanations
  are consolidated, and no text, example, heading, figure, or page is added
  merely to make the paper longer;
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
- the only top-level TeX sources under `arrange/paper_draft` are `main.tex`,
  the six body sources, the five solved optimization appendices, and the exact
  certificate source rendered as Appendix F;
- the two paper-atlas wrappers are absent; the standalone explorer, preset
  JSON, and exactly fifteen colocated `figures/trace_exact_ab/*.png` panels are
  reproducible from one registry; the pinned static core-case image has the
  required SHA-256; and none of these explanatory images is treated as a proof
  authority;
- every remaining publication figure is used either by the new paper closure
  or by an archived proof-paper source;
- `arrange/paper_draft/main.pdf` is the validated canonical output and passes
  the repository’s semantic and render checks;
- the CI page-count interval contains the measured intentional output and was
  not broadened speculatively; a concise paper is not padded to meet the old
  lower bound;
- all required checks pass and the rebuilt paper has no unresolved references,
  duplicate labels, or false hard-coded section equation numbers.
