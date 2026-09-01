
# Repository instructions

## Mathematical authority

A mathematical claim is established by a numbered source under `proof/` whose
status supports the claim, or by an exact certificate explicitly incorporated
by the paper. Navigation files, interactive pages, prompts, experiments, and
failed approaches are not proof authorities.

## Non-negotiable conventions

- Use **C triangle** and **V triangle**.
- Let the original open triangles be \(U_C,U_0,\ldots,U_5\), with
  \(O\in U_C\) and \(V_i\in U_i\). Put \(T_C=\overline{U_C}\) and
  \(T_i=\overline{U_i}\). Use closed classifications on the \(T\)'s and retain
  the \(U\)'s whenever openness matters.
- Uppercase \((A_i,B_i,C_i)\) denotes actual maximal reaches.
- Lowercase \((a_i,b_i,c_i)\) denotes selected lower bounds and must be
  introduced by an explicit inequality such as \(a_i\le A_i\).
- Define \(N_+\) only from \(A_i+B_i>1\).
- Preserve singleton boundary gaps.
- Preserve the CE1/CE2 distinction, all endpoint strictness, actual V-type
  restrictions on neighboring support, connected-component selectors, and
  both charts in the Vd1 replacement.
- Do not replace the exact zero-gap certificate by numerical evidence.

## Repository layout

- `proof/`: proof sources and certificate code.
- `arrange/`: canonical and reader-oriented papers.
- `interactive/`: generated and hand-authored visual explanations.
- `prompts/`: research prompt archive.

Do not recreate a top-level `tools`, `release`, `.vscode`, or formalization
directory. Put support code next to the content it validates.

## Required checks

```bash
python -m pip install -r arrange/_support/requirements.txt
python proof/check.py
python interactive/generate.py --dependency-graph --check
python interactive/check.py
python arrange/build.py --all
```

Run the two exact zero-gap certificate programs whenever their source,
provenance, or dependent theorem changes.
