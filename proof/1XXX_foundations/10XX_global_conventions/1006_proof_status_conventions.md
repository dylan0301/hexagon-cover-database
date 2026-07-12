# Proof Status Conventions

Status: Definition

Labels used in these notes:

- `Definition`: exact convention or mathematical definition.
- `Proven`: complete proof in the file or in explicitly referenced local files,
  including local lemmas and analytic inequalities.
- `Reduction`: complete proof that the remaining obstruction is carried into
  explicitly named local targets or dependencies. This certifies the routing
  itself, not any terminal target. The branch closes only when every named
  terminal dependency is `Proven`.
- `Practically proven`: proof is known and the statement may be used as a
  working dependency, but the complete written proof is not recorded here.
- `Lemma target`: useful statement whose proof is not complete here.
- `Strategy`: active proof direction.
- `Empirical`: supported by computation or plotting only.
- `Failed`: known insufficient or abandoned approach.
- `Experiment`: experiment plan, helper script, or reproducibility aid.
- `Reference`: dictionary, inventory, index, navigation file, or status table.

Numerical optimization claims stay `Empirical` until certified.
