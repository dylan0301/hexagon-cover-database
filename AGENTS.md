# AGENTS.md

Guidelines for Codex or any AI agents working in this repository.

The `proof/` corpus is a mathematical research database for the hexagon
covering problem, not application code. Use [README.md](README.md) for reader
orientation, [proof/0XXX_main/0001_proof_tree_index.md](proof/0XXX_main/0001_proof_tree_index.md)
for branch organization, [proof/09XX_appendices/0910_notation_dictionary.md](proof/09XX_appendices/0910_notation_dictionary.md)
for notation, and
[proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md](proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md)
for status labels.

## 1. Understand The Repository First

Before editing, read the relevant navigation files:

- [README.md](README.md)
- [proof/0XXX_main/0000_main_theorem.md](proof/0XXX_main/0000_main_theorem.md)
- [proof/0XXX_main/0001_proof_tree_index.md](proof/0XXX_main/0001_proof_tree_index.md)
- [proof/0XXX_main/0002_status_and_dependencies.md](proof/0XXX_main/0002_status_and_dependencies.md)
- [proof/09XX_appendices/0910_notation_dictionary.md](proof/09XX_appendices/0910_notation_dictionary.md)
- [proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md](proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md)
- The local index file for the folder being edited, when one exists.

The proof-tree index is navigation only. Do not treat a branch as proven unless
a proof file in `proof/` supports that status.

Assume the notes are delicate. If the request is ambiguous, ask before editing,
especially when a change could affect proof status, theorem statements,
definitions, notation, case classifications, or claims marked empirical,
failed, target, strategy, or incomplete.

## 2. Preserve Proof Status

Follow the status definitions in
[1006_proof_status_conventions.md](proof/1XXX_foundations/10XX_global_conventions/1006_proof_status_conventions.md).
Do not upgrade or imply a stronger result than the source file supports. Only
describe a result as proven if its file says `Status: Proven`.

Numerical or computational evidence stays `Empirical` unless a certificate is
explicitly added. A global minimum, maximum, or infeasibility claim must remain
`Empirical` unless it has an exact symbolic proof, interval certificate,
quantifier-elimination certificate, or another independently checkable rigorous
certificate.

## 3. Respect The Root `proof/` Layout

Use the corpus map in [README.md](README.md) and the branch scaffold in
[0001_proof_tree_index.md](proof/0XXX_main/0001_proof_tree_index.md). The root
`proof/` folder is self-contained. Do not add new links to the old
documentation tree, or to old root-level computation or experiment trees.

Computation and experiment helpers should be colocated with the proof package
they support.

## 4. Make Surgical Markdown Changes

Touch only what the user asked for.

Do not:

- refactor unrelated prose,
- rename concepts casually,
- reorganize folders unless asked,
- delete failed ideas,
- remove open questions,
- normalize notation across files unless the task explicitly asks for that.

If you notice unrelated problems, mention them instead of fixing them. Every
changed line should trace directly to the user's request.

## 5. Follow Repository Style

Use Markdown for research-note files unless explicitly asked otherwise. Do not
add image assets to proof notes unless explicitly requested.

Use LaTeX consistently:

- inline math: `$...$`; display math: `$$...$$`; do not use `\(...\)` or
  `\[...\]`.
- cardinalities:
  `\left\lvert \left\lbrace ... \right\rbrace \right\rvert`; do not use
  hash-based notation.
- thin spacing: do not use the LaTeX thin-space command, written as a
  backslash followed by a comma; use ordinary source spaces where token
  separation is needed.
- named operators: `\mathrm{...}`; do not use the operatorname macro.
- operator conditions for `\sup`, `\inf`, `\min`, and `\max`: put conditions
  in subscripts, using `\substack{...}` when needed. Do not put alignment
  markers inside operator arguments.
- scalable delimiters: `\left` and `\right` must be followed by real
  delimiters. For set braces, use `\left\{ ... \right\}`.

Prefer concise research-note prose. Add links as relative Markdown links to
existing files. Index and navigation files must use Markdown tables with a
status column when listing files or linked packages.

## 6. Protect Mathematical Meaning

When editing mathematical statements, preserve quantifiers, hypotheses,
variable names, open/closed triangle distinctions, distinctions between `H`,
`H_L`, `S`, and `S_{1/2}`, the CE and $N_+$ splits, and case labels such as
CE0, CE1, CE2, Vd0, Vd1, Vd2, and T3-like.

Preserve the Korean term **걸거치는** where it names the recurring geometric
phenomenon of a triangle crossing or straddling adjacent structure in a
non-axis-aligned way.

If a requested edit seems to change theorem, lemma, or proof content, stop and
ask.

## 7. Keep Things Simple

Use the minimum change that solves the task. Do not add new abstractions,
templates, automation, or metadata unless requested. For documentation tasks,
prefer direct edits over scripts unless the task is a broad mechanical rewrite.

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
- Check missing delimiters after scalable delimiter commands:
  `rg -n -F "$(printf '\\134left{')" README.md AGENTS.md proof prompts`
  `rg -n -F "$(printf '\\134right}')" README.md AGENTS.md proof prompts`
- Check obsolete root paths:
  `rg 'documentatio[n]/|computation[s]/|experiment[s]/' README.md proof prompts`
- Check a term replacement:
  `rg 'old term'`
- Review changed files:
  `git diff --stat`
  `git diff -- <file>`

For generated or updated navigation files, check that linked paths exist.

## 9. Be Explicit About Assumptions

Before substantial work, briefly state what you think the user wants, what
files or sections you plan to touch, and how you will verify the result. For
trivial edits, use judgment and proceed.

## 10. Do Not Overstate Completion

At the end, report only what was actually done and verified. Mention anything
not checked. Do not claim that the mathematical proof is complete unless the
repository itself supports that claim.
