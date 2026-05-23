# AGENTS.md

Guidelines for Codex agents working in this repository.

The documentation corpus in `documentation/` is a Markdown research database for the hexagon covering problem. Treat those notes as mathematical research notes, not as application code.

## 1. Understand The Repository First

Before editing, read the relevant navigation files:

- `README.md`
- `documentation/000_INDEX.md`
- `documentation/001_README_FOR_FUTURE_WORK.md`
- `documentation/100_foundations/106_proof_status_conventions.md`
- The local index file for the folder being edited, when one exists.

Assume the notes are delicate. Small wording changes can change mathematical meaning.

If the request is ambiguous, ask before editing. In particular, ask when a change could affect:

- proof status,
- theorem statements,
- definitions,
- notation,
- case classifications,
- claims marked empirical, failed, or incomplete.

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

Numerical or computational evidence stays `Empirical` unless a certificate is explicitly added.

## 3. Make Surgical Markdown Changes

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

## 4. Follow Repository Style

Use Markdown for research-note files unless explicitly asked otherwise.

Use LaTeX delimiters consistently:

- inline math: `$...$`
- display math: `$$...$$`

Do not use `\(...\)` or `\[...\]`.

Prefer concise research-note prose. Avoid decorative formatting, long explanations, or speculative commentary.

When adding links, use relative Markdown links to existing files.

## 5. Protect Mathematical Meaning

When editing mathematical statements:

- preserve quantifiers,
- preserve hypotheses,
- preserve variable names unless asked,
- preserve distinctions between open and closed triangles,
- preserve distinctions between `H`, `H_L`, `S`, and `S_{1/2}`,
- preserve case labels such as CE0, CE1, CE2, Vd1, Vd2, and T3-like.

If a requested edit seems to change the theorem, lemma, or proof content, stop and ask.

## 6. Keep Things Simple

Use the minimum change that solves the task.

Do not add new abstractions, templates, automation, or metadata unless requested.

For documentation tasks, prefer direct edits over scripts unless the task is a broad mechanical rewrite.

## 7. Verify Changes

For broad Markdown edits, verify with targeted searches.

Examples:

- Check old LaTeX delimiters:
  `rg '\\\\\\(|\\\\\\)|\\\\\\[|\\\\\\]'`
- Check a term replacement:
  `rg 'old term'`
- Review changed files:
  `git diff --stat`
  `git diff -- <file>`

For generated or updated navigation files, check that linked paths exist.

## 8. Be Explicit About Assumptions

Before substantial work, briefly state:

1. what you think the user wants,
2. what files or sections you plan to touch,
3. how you will verify the result.

For trivial edits, use judgment and proceed.

## 9. Do Not Overstate Completion

At the end, report only what was actually done and verified.

Mention anything not checked.

Do not claim that the mathematical proof is complete unless the repository itself supports that claim.
