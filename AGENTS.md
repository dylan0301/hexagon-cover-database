# AGENTS.md

Guidelines for Codex agents working in this repository.

The proof corpus in `proof/` is a Markdown research database for the hexagon
covering problem. Treat those notes as mathematical research notes, not as
application code.

The current organizing structure is the root-level proof tree:

```text
hypothetical seven-triangle cover
  classify T_C as CE0, CE1, or CE2
  define perimeter rows (a_i,b_i)
  compute N_+ = \left\lvert \left\lbrace\, i : a_i+b_i > 1 \,\right\rbrace \right\rvert
  split first by CE0, CE1, or CE2
  split inside each CE branch by N_+ = 0, N_+ = 1, or N_+ >= 2
  split inside each N_+ branch by the number of VD0, VD1/VD2, T3 like triangles
```

The CE0/CE1/CE2 split is the primary repository organization.

Folder prefixes use four-character range labels with literal `X` digits, such
as `3XXX_CE0`, `31XX_Nplus1`, and `310X_all_Vd0_five_point`. File prefixes
remain concrete four-digit labels.

## 1. Understand The Repository First

Before editing, read the relevant navigation files:

- `README.md`
- `proof/0XXX_main/0000_main_theorem.md`
- `proof/0XXX_main/0001_proof_tree_index.md`
- `proof/0XXX_main/0003_readme_for_future_work.md`
- `proof/0XXX_main/0002_status_and_dependencies.md`
- `proof/1XXX_foundations/1006_proof_status_conventions.md`
- `proof/09XX_appendices/0940_CE_case_tree.md`
- The local index file for the folder being edited, when one exists.

The user prompt `prompts/20260610prooftreeSketch.txt` records the current
proof-tree sketch. Use it for branch organization, but do not treat sketch
claims as proven unless a proof file in `proof/` supports that status.

Assume the notes are delicate. Small wording changes can change mathematical
meaning.

If the request is ambiguous, ask before editing. In particular, ask when a
change could affect:

- proof status,
- theorem statements,
- definitions,
- notation,
- case classifications,
- claims marked empirical, failed, target, strategy, or incomplete.

## 2. Preserve Proof Status

Do not upgrade or imply a stronger result than the source file supports.

Only describe a result as proven if its file says one of:

- `Status: Proven`
- `Status: Proven local lemma`
- `Status: Proven analytic inequality`

Keep these distinctions intact:

- `Definition`: exact convention or mathematical definition.
- `Lemma target`: useful but not fully proved here.
- `Strategy`: active proof direction.
- `Empirical`: supported by computation or plotting only.
- `Failed`: known insufficient or abandoned approach.
- `Reference`: dictionary, inventory, or index.

Numerical or computational evidence stays `Empirical` unless a certificate is
explicitly added.

## 3. Respect The Root `proof/` Layout

The root `proof/` folder is now self-contained. Do not add new links to the
old documentation tree, or to old root-level computation or experiment trees.

Use these proof-tree folders for new notes:

- `proof/1XXX_foundations/`: definitions and conventions.
- `proof/2XXX_geometric_lemmas/`: reusable geometric lemmas and targets.
- `proof/3XXX_CE0/`: the CE0 branch.
- `proof/4XXX_CE1/`: the CE1 branch.
- `proof/5XXX_CE2/`: the CE2 branch.
- `proof/9XXX_failed_ideas/`: failed routes and empirical warnings.

Computation and experiment helpers are colocated with the proof package they
support, for example:

- `proof/4XXX_CE1/40XX_Nplus0/400X_all_Vd0_boundary_loss/409X_experiments/`
- `proof/9XXX_failed_ideas/962X_may21_four_point_failure/962X_computations/`
- `proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/908X_computation/`

## 4. Make Surgical Markdown Changes

Touch only what the user asked for.

Do not:

- refactor unrelated prose,
- rename concepts casually,
- reorganize folders unless asked,
- delete failed ideas,
- remove open questions,
- normalize notation across files unless the task explicitly asks for that.

If you notice unrelated problems, mention them instead of fixing them.

Every changed line should trace directly to the user's request.

## 5. Follow Repository Style

Use Markdown for research-note files unless explicitly asked otherwise.

Use LaTeX delimiters consistently:

- inline math: `$...$`
- display math: `$$...$$`
- cardinalities: write
  `\left\lvert \left\lbrace\, ... \,\right\rbrace \right\rvert` in math;
  do not use hash-based notation for cardinality.
- named operators: write `\mathrm{...}` in math; do not use the operatorname
  macro.
- operator conditions: put conditions for `\sup`, `\inf`, `\min`, and `\max`
  in subscripts, using `\substack{...}` when multiple lines are needed. Do not
  put alignment markers inside operator arguments.

Do not use `\(...\)` or `\[...\]`.

Prefer concise research-note prose. Avoid decorative formatting, long
explanations, or speculative commentary.

When adding links, use relative Markdown links to existing files.

## 6. Protect Mathematical Meaning

When editing mathematical statements:

- preserve quantifiers,
- preserve hypotheses,
- preserve variable names unless asked,
- preserve distinctions between open and closed triangles,
- preserve distinctions between `H`, `H_L`, `S`, and `S_{1/2}`,
- preserve the primary CE branch split and the internal $N_+$ split,
- preserve case labels such as CE0, CE1, CE2, Vd0, Vd1, Vd2, and T3-like.

If a requested edit seems to change the theorem, lemma, or proof content, stop
and ask.

## 7. Keep Things Simple

Use the minimum change that solves the task.

Do not add new abstractions, templates, automation, or metadata unless
requested.

For documentation tasks, prefer direct edits over scripts unless the task is a
broad mechanical rewrite.

## 8. Verify Changes

For broad Markdown edits, verify with targeted searches.

Examples:

- Check old LaTeX delimiters:
  `rg '\\\\\\(|\\\\\\)|\\\\\\[|\\\\\\]' proof README.md`
- Check obsolete hash-cardinality notation:
  `rg -n -F "$(printf '\\134#')" README.md AGENTS.md proof prompts`
  `rg -n -F "$(printf '#%s' '{')" README.md AGENTS.md proof prompts`
- Check unsupported named-operator macro:
  `rg -n -F "$(printf '\\134operator%s' name)" README.md AGENTS.md proof prompts`
- Check operator arguments with embedded alignment markers:
  `rg -n -F "$(printf ':%s' '&')" README.md AGENTS.md proof prompts`
- Check obsolete root paths:
  `rg 'documentatio[n]/|computation[s]/|experiment[s]/' README.md proof prompts`
- Check a term replacement:
  `rg 'old term'`
- Review changed files:
  `git diff --stat`
  `git diff -- <file>`

For generated or updated navigation files, check that linked paths exist.

## 9. Be Explicit About Assumptions

Before substantial work, briefly state:

1. what you think the user wants,
2. what files or sections you plan to touch,
3. how you will verify the result.

For trivial edits, use judgment and proceed.

## 10. Do Not Overstate Completion

At the end, report only what was actually done and verified.

Mention anything not checked.

Do not claim that the mathematical proof is complete unless the repository
itself supports that claim.
