# Full repository repair after the 2026-08-08 audit

## Scope

This repair addresses every concrete defect identified in the post-merge audit
of the main branch.  It does not attempt the later project of replacing the ten
Lean `sorry` placeholders with formal optimization proofs.

## 1. Universal Strategy 2 proof ownership

### Problem

The first optimization split proved that a geometric configuration maps into an
explicit real domain, but several registry entries cited geometric theorems as
though those theorems quantified over every syntactically feasible real point.
This left a possible image-versus-domain gap for S2-T3, S2-SC, and S2-VD and
made the proof owner of S2-E1, S2-E2, S2-R1, and S2-R2 implicit.

### Repair

`04f_strategy2_pure_theorems.tex` now contains named universal theorem owners:

- S2-E1 and S2-E2 endpoint inequalities;
- S2-R1 and S2-R2 returned-demand inequalities;
- the complete finite-cell S2-T3 theorem;
- both S2-SC source cells;
- adjacent and nonadjacent S2-VD inequalities.

The T3 proof explicitly maps an arbitrary point of `Omega_T3` to the exact
407X radical variables and checks that every residual, radial, and contact
predicate is the corresponding algebraic branch condition.  It no longer
assumes prior geometric realization.  The Vd proofs use only explicit
piecewise residual functions, corner graph formulas, and real inequalities.
The nonadjacent Vd domain was strengthened by adding the two center
endpoint-distance inequalities that its pure separation proof uses.

The bridge appendix now has only two responsibilities: prove domain membership
for a geometric record and identify the geometric terminal quantity with the
registered objective.  The application registry cites the universal real
 theorem first and the bridge second.

The numbered proof package now includes:

- `2111_strategy2_pure_optimization_registry.md`;
- `407e_pure_finite_cell_theorem.md`.

Both have status `Proven` and are included in the active dependency graph.

## 2. PDF defects

### Problem

The former symbol table was a forced nonsplittable table and extended below the
last page.  Long proof filenames and full Git hashes also overlapped on the
407X and Strategy 4 provenance pages.

### Repair

- The symbol table is now a multipage `longtable`.
- Duplicate symbol entries were consolidated.
- Printed provenance tables use compact proof identifiers and twelve-character
  hash prefixes; full hashes remain in machine-readable JSON manifests.
- CI rejects unresolved references and all overfull horizontal or vertical
  boxes.
- Every PDF page is rendered and scanned for text or pixels touching the media
  box.

## 3. CI metadata and reproducibility

### Problem

The permanent workflow compared the current rebuilt PDF with an obsolete dated
hash file describing an older 129-page build.  This made the main workflow red
even when source checks and certificate replays passed.

### Repair

- The dated summary was deleted.
- `CURRENT_VERIFICATION_SUMMARY.txt` is generated from the same canonical build
  as the tracked PDF.
- Investigation showed that XeTeX/xdvipdfmx changes document identifiers
  and compressed-object bytes even between consecutive clean builds.  Raw byte
  equality is therefore not a valid reproducibility condition.
- The replacement semantic checker is stricter on stable content: page
  geometry, outlines, labels, extracted words and coordinates, links,
  annotations, widgets, embedded files, and exact 144-DPI RGB pixels must all
  agree.
- TeX builds run in pinned TeX Live 2025.
- Python dependencies, GitHub Actions, Lean 4, and Mathlib are pinned.
- The workflow has separate proof, Lean, paper, and release jobs.

## 4. Lean statement project

### Problem

The single Lean file had no toolchain, Lake project, Mathlib pin, lockfile, or
CI elaboration.

### Repair

The Strategy 2 statement shell is now a conventional Lake project pinned to:

- Lean `v4.32.2`;
- Mathlib commit `905b95818eb32af7874a58b427f50c1711a5e96c`.

CI runs `lake build`.  The exact TeX and Lean problem registries are also
checked by `verify_strategy2_spec_sync.py`.  The ten `sorry` placeholders are
intentional and counted exactly; no full formalization is claimed.

## 5. Archival release and documentation

### Repair

The repository now includes:

- explicit dual licensing;
- reproduction instructions;
- contribution and review requirements;
- CODEOWNERS and a proof-oriented pull-request template;
- a deterministic archival bundle containing the paper, dependency and
  provenance manifests, exact certificate sources/data, and Lean project.

The roadmap and source ledger now distinguish the wrapper, problem registry,
universal theorem owner, bridge, and calculation modules.  Obsolete failure
logs, one-shot export workflows, and historical source-rewrite scripts were
removed.

## Validation requirements

The repair is accepted only if all of the following pass on the exact committed
Git tree:

1. generated active dependency graph and two-way proof manifest;
2. permanent proof linter;
3. 27 exact Strategy 2 algebra identities;
4. TeX--Lean problem synchronization;
5. both exact Strategy 4 certificate replays;
6. Lean statement-project build;
7. two pinned TeX Live 2025 rebuilds with strict semantic equivalence;
8. no unresolved references or overfull boxes;
9. full-page render and media-box border scan;
10. deterministic archival bundle construction.

The final PDF digest, page count, pinned versions, and successful checks are
recorded in `CURRENT_VERIFICATION_SUMMARY.txt` after the canonical CI build.
