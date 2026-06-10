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
  compute N_+ = #{i : a_i+b_i > 1}
  split first by N_+ = 0, N_+ = 1, or N_+ >= 2
```

The CE0/CE1/CE2 split is now a subbranch inside the $N_+$ tree, not the primary
repository organization.

## 1. Understand The Repository First

Before editing, read the relevant navigation files:

- `README.md`
- `proof/000_main_theorem.md`
- `proof/001_proof_tree_index.md`
- `proof/001_readme_for_future_work.md`
- `proof/002_status_and_dependencies.md`
- `proof/100_foundations/106_proof_status_conventions.md`
- `proof/appendices/E_case_tree.md`
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

- `proof/010_setup/`: setup bridge files and proof-tree definitions.
- `proof/100_Nplus0/`: the $N_+=0$ branch.
- `proof/200_Nplus1/`: the $N_+=1$ branch.
- `proof/300_Nplus_ge2/`: the $N_+\ge2$ branch.
- `proof/400_local_lemmas/`: local lemma targets and reusable local facts.
- `proof/500_finite_point_algorithms/`: finite-point algorithm routes.
- `proof/900_failed_and_empirical/`: failed and empirical route index.

Legacy source packages such as `proof/100_foundations/`,
`proof/300_vertex_triangle/`, `proof/600_case_strategies/`, and
`proof/appendices/` remain part of the self-contained corpus and should be
linked locally.

Computation and experiment helpers are colocated with the proof package they
support, for example:

- `proof/550_CE_Vd0_boundary_loss/experiments/`
- `proof/620_may21_patternA/computations/`
- `proof/800_computation/20260524_skeleton_cover/`

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
- preserve the primary $N_+$ branch split,
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
