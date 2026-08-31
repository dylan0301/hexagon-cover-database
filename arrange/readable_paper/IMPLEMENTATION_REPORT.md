# Reader-oriented paper and dependency-graph implementation report

## 1. Scope and preservation rule

This update is an **additive reader-facing publication layer** for branch
`No-more-strategy-2`, based on source head
`048320ccade291fc828c1b51fff167ebb7cb29cc`.  No pre-existing repository file
was edited, renamed, or deleted.  The authoritative proof corpus and the
current consolidated paper under `arrange/paper_draft/` remain untouched.

The new publication entry point is:

```text
arrange/readable_paper/main.tex
```

It reuses the common structural, trace-length, and area-loss sources from
`arrange/paper_draft/`, but supplies a new Introduction, Method 3 body,
zero-gap chapter, appendices, completion, navigation files, and build script.

Two independent checks enforce the preservation rule:

1. every one of the 483 files present in the source artifact before this
   additive update was rehashed after the work; all 483 hashes agree;
2. `ORIGINAL_SOURCE_MANIFEST.json` records the SHA-256 hashes of the 44
   original TeX and figure inputs actually reused by the readable PDF, and
   `tools/verify_readable_additive.py` checks them in CI.

## 2. New public proof architecture

The original mathematical content is retained, but Method 3 is no longer
presented as a single flat finite-enclosure chapter.  The readable paper now
uses the following architecture.

### 2.1 Common material

1. Introduction, canonical roles, classifications, and stable routing IDs
   `R0`-`R13`.
2. Structural reduction and signed CE1/CE2 geometry.
3. Method 1: trace and skeleton length.
4. Method 2: local and cyclic area loss.

### 2.2 Method 3, Chapter 5: local toolkit and nonzero-gap obstructions

The chapter begins with an explicit contract:

```text
normalize the case
    -> bound local capacity
    -> force a point or compact set into U_C
    -> invoke one named terminal
    -> close one stable case ID.
```

The recurring public interfaces are introduced before the cases:

- enclosure number `Lambda(K)`;
- exact own-ray capacity `c_max(a,b)`;
- neighboring capacities `C_+(a,b), C_-(a,b)`;
- type-aware radial witness `D_i`;
- complementary gap `J(p,q)`;
- anisotropic one-gap witness `K_410`.

The order is now:

1. openness, compactness, and continuity;
2. trace-exact AB-envelope interface;
3. exact own-ray and neighboring-ray capacities;
4. high-radial output interfaces;
5. type-aware radial forcing and common-pair domination;
6. one-gap and two-gap common-pair lemmas;
7. universal terminal G: complementary gap;
8. universal terminal S: CE2 short ray;
9. all-Vd0, T3-like, and Vd exceptional cases;
10. stable nonzero-gap dispatch table.

### 2.3 Method 3, Chapter 6: separate zero-gap nine-point obstruction

The zero-gap theorem is no longer nested inside the actual-gap toolkit.  It
has its own chapter and dependency spine:

```text
exact-one handoffs
    -> strict supercritical AB-union
    -> six radial witnesses
    -> three asymmetric witnesses
    -> Newton inner reduction
    -> exact/analytic cap overlaps
    -> cyclic support-arc covering
    -> zero-gap obstruction.
```

The two difficult unequal-radius overlaps remain in the exact certificate
appendix.

### 2.4 Appendices

- **Appendix A:** detailed finite-enclosure calculations, including high-radial
  piecewise outputs, selector algebra, the full CE1 reverse-path calculation,
  and detailed Vd inequalities.
- **Appendix B:** actual-gap trace-exact AB-envelope atlas.  The zero-gap
  screenshot is deliberately omitted.
- **Appendix C:** exact unequal-radius mixed-overlap certificate.

### 2.5 Completion

The final proof cites the Method 1 assembly, Method 2 assembly, nonzero-gap
Method 3 assembly, and zero-gap Method 3 assembly.  The stale phrase
“finite residual-hull theorem” has been replaced by the active forward
finite-enclosure terminology.

## 3. Statement-level restructuring

The following editorial changes are implemented as mathematical interfaces,
not merely as new headings.

### 3.1 Trace-exact actual-gap interface

A named proposition now states exactly what is used later:

- the gap endpoints are the actual maximal reaches;
- the conditioned envelopes have the correct edge sections;
- the actual incident roles lie in those envelopes;
- the envelopes are contained in the ordinary AB-unions;
- therefore `c_max` and `C_+-/C_-` remain valid while the whole actual gap is
  center-forced.

### 3.2 The `N_+=0` row is split by gap rank

The former combined proposition is now:

- a one-gap common-disk proposition using the complementary-gap theorem;
- a two-gap CE2 common-pair proposition using the short-ray theorem;
- a short assembly corollary.

### 3.3 The anisotropic all-Vd0 row is split by center type

The new interfaces are:

1. the set `K_410` is center-forced;
2. one common terminal upper bound holds at the unique supercritical role;
3. the CE1 reverse path contradicts the upper bound;
4. the CE2 `T_4/T_2` threshold dichotomy contradicts the same upper bound;
5. a final enclosure proposition combines CE1 and CE2.

The long CE1 scalar proof is in Appendix A.  The body retains its exact
hypotheses and terminal conclusion.

### 3.4 The T3-like row is split by gap rank

The O-side endpoint is first isolated in a lemma.  The one-gap case then uses
the strict-supercritical outgoing envelope and a four-role path budget.  The
two-gap case invokes the universal CE2 short-ray terminal.  A short corollary
assembles them.

### 3.5 The one-Vd assembly is split into named placements

The former four-case proof is replaced by:

- adjacent one-Vd radial separation;
- nonadjacent one-Vd radial separation;
- Vd1 neighboring-midpoint rescuer;
- two-chart replacement and output-gap rerouting;
- one assembly corollary, including the Vd2 Method 1 exit.

This makes clear which branches produce a literal uncovered point, which use
a boundary-path budget, and which are reductions.

## 4. Stable case IDs

The global routing table uses `R0`-`R13`.  Method 3 has the following reader
cards:

| ID | Branch | Terminal |
|---|---|---|
| NG0 | one gap, `N_+=0`, Vd0/T3-like | complementary gap |
| NG1 | two gaps, CE2, `N_+ in {0,1}` | short ray |
| NG2 | one gap, `N_+=1`, all Vd0 | CE1 reverse path or CE2 threshold |
| NG3 | one gap, exactly one T3-like | O-side endpoint and path budget |
| NG4 | two gaps, exactly one T3-like | short ray |
| NG5 | one Vd adjacent to supercritical `T_0` | literal radial point |
| NG6 | one Vd nonadjacent to supercritical `T_0` | `D_tau` separation |
| NG7 | Vd based at `T_0` or pair away from `T_0` | rescuer or replacement rerouting |
| ZG0 | zero gap, unique supercritical, all Vd0 | nine-point enclosure |

Every case card identifies its hypotheses, forced object, terminal, and global
routing row.

## 5. Zero-gap figure correction

The former dependency HTML used the generated trace-envelope snapshot
`zero_gap_n1_vd0.png`.  In that image the displayed `Q_-`, `Q_0`, and `Q_+`
appeared at misleading fixed locations.

The repository history contains the earlier author-facing nine-point TikZ
figure:

```text
commit: de21fd938af8379ab4fce999a956ead63ac5c46a
path:   arrange/paper_draft/figures/strategy4_nine_point_witness.tex
```

That historical source has been restored **only in the additive readable
paper tree** as:

```text
arrange/readable_paper/figures/strategy4_nine_point_witness.tex
```

It is used in Chapter 6 and rendered for the interactive graph as:

```text
interactive/assets/readable_dependency/zero_gap_nine_point_witness.png
```

The caption explicitly states that the asymmetric witness coordinates depend
on the exact handoff pair and that the schematic coordinates are not proof
data.  The actual-gap atlas now omits the zero-gap trace-envelope screenshot.

## 6. Interactive dependency graph

The new graph is stored at:

```text
interactive/readable_proof_dependency_graph.html
```

Its machine-readable companion is:

```text
interactive/readable_proof_dependency_data.json
```

The graph is generated from the recursive active `\input` closure of
`arrange/readable_paper/main.tex`.  It contains:

- 93 formal theorem/lemma/proposition/corollary nodes;
- 194 audited logical dependencies;
- 39 active TeX sources;
- 22 embedded PNG figures;
- the global routing table `R0`-`R13`;
- Method 3 case cards `NG0`-`NG7` and `ZG0`;
- the exact TeX statement, case scope, prerequisites, dependents, manuscript
  source, proof-package authority, and related figures for every node.

The graph is not the repository’s historical untyped Markdown-reference
network.  Each arrow `prerequisite -> result` is either an explicit theorem
citation in a proof or a separately declared logical/routing interface.  The
graph is audited to be acyclic.

The zero-gap `ZG0` card and all zero-gap theorem nodes use only the restored
historical nine-point figure.

## 7. Reproducible generation and CI

New tools:

```text
tools/generate_readable_dependency_graph.py
tools/verify_readable_additive.py
tools/verify_readable_html.py
```

The graph generator supports:

```bash
python tools/generate_readable_dependency_graph.py
python tools/generate_readable_dependency_graph.py --check
```

The readable PDF supports:

```bash
cd arrange/readable_paper
./build.sh
```

The new additive workflow is:

```text
.github/workflows/readable-paper-rebuild.yml
```

It checks the original-source manifest, regenerates and validates the HTML,
runs the existing proof linter, replays the zero-gap exact certificate, builds
the readable PDF in pinned TeX Live 2025, verifies the page range and rendering,
and uploads the PDF, graph, data, report, and corrected zero-gap asset.

## 8. Validation results

The local audit produced the following results.

| Check | Result |
|---|---|
| strict XeLaTeX build | PASS |
| PDF length | 95 pages |
| undefined references | none |
| multiply defined labels | none |
| overfull boxes | none |
| PDF render scan | PASS, all 95 pages |
| deterministic two-build PDF comparison | PASS |
| two PDF SHA-256 hashes | identical |
| semantic/raster comparison | PASS |
| original pre-existing files | 483/483 unchanged |
| reused original input manifest | 44/44 unchanged |
| proof linter | PASS: 53 proof sources, 36 compiled TeX sources, 208 labels |
| readable graph generation `--check` | PASS |
| readable HTML static audit | PASS: 93 nodes, 194 edges, 22 PNG figures |
| logical graph DAG test | PASS |
| exact global Bernstein positivity verifier | PASS |

The derivation-side exact certificate verifier was started locally but did not
finish within the session’s five-minute execution ceiling.  Its source and all
authenticated certificate data are unchanged, the prior branch verification at
the source head completed successfully, and the new GitHub workflow reruns the
full derivation verifier on a standard Actions runner before accepting the
artifact.

## 9. Repository-write status

The complete change set is add-only and ready as one commit.  The execution
environment used for this update exposed GitHub repository reads but no write,
commit, workflow-dispatch, or pull-request creation operation, and direct Git
network access could not resolve `github.com`.  Therefore no remote commit was
fabricated or claimed.  A Git binary patch and repository-path ZIP are provided
with the delivered artifacts so the exact prepared change can be applied as a
single commit when a write-capable GitHub session is available.
