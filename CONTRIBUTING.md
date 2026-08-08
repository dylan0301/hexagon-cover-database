# Contributing

Changes to this repository may alter a computer-assisted mathematical proof.
The following review discipline applies to every proof-bearing change.

## Required pull-request contents

A pull request must state:

1. the theorem, definition, certificate, or presentation layer changed;
2. whether any feasible domain or quantifier changed;
3. the exact proof owner after the change;
4. the commands or GitHub Actions checks used for validation;
5. any remaining `sorry`, experiment, reduction, or unverified dependency.

## Required checks

Before merge, the permanent workflow must pass all of these jobs:

- active proof dependency and manifest checks;
- notation, provenance, and source linting;
- exact Strategy 4 certificate replay;
- Strategy 2 pure-algebra and TeX--Lean synchronization checks;
- pinned PDF rebuild with strict semantic equivalence, overflow check, and page-border scan;
- Lean statement-project elaboration;
- deterministic release-bundle construction.

Proof-bearing pull requests require review by a code owner. Direct pushes to
`main` should be restricted to repository recovery or an explicitly requested,
fully validated publication operation.

## Generated files

Do not edit these by hand:

- `proof/ACTIVE_DEPENDENCY_GRAPH.json`;
- `proof/ACTIVE_DEPENDENCIES.txt`;
- `proof/MANIFEST.txt`;
- `arrange/CURRENT_VERIFICATION_SUMMARY.txt`;
- `arrange/paper_draft/main.pdf`;
- `formalization/strategy2_optimization/lake-manifest.json`.

Regenerate them using the commands in `REPRODUCE.md` and commit them together
with the source change that caused the update.
