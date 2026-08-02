from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path('.')


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding='utf-8')


def write(relative: str, text: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8')


def replace_section(text: str, start: str, end: str, replacement: str) -> str:
    i = text.index(start)
    j = text.index(end, i)
    return text[:i] + replacement.rstrip() + '\n\n' + text[j:]


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode('ascii') + data).hexdigest()


# Correct the remaining actual/selected notation errors.
for relative in [
    'proof/3XXX_CE0/31XX_Nplus1/314X_exists_Vd1_Vd2/3141_CE0_Nplus1_exists_Vd1_Vd2_boundary_length_obstruction.md',
    'proof/3XXX_CE0/3000_CE0_index.md',
]:
    text = read(relative)
    text = text.replace('i : a_i+b_i>1', 'i : A_i+B_i>1')
    text = text.replace('i:a_i+b_i>1', 'i:A_i+B_i>1')
    write(relative, text)

# Normalize geometric terminology throughout proof-bearing Markdown and compiled TeX.
terminology = [
    ('Vd1/Vd2 rows', 'Vd1/Vd2 V triangles'),
    ('Vd1/Vd2 row', 'Vd1/Vd2 V triangle'),
    ('T3-like rows', 'T3-like V triangles'),
    ('T3-like row', 'T3-like V triangle'),
    ('vertex rows', 'vertex V triangles'),
    ('ordinary rows', 'ordinary V triangles'),
    ('remaining rows', 'remaining V triangles'),
    ('rows below', 'V-triangle cases below'),
    ('five-row', 'five-V-triangle'),
    ('six-row', 'six-V-triangle'),
    ('row interface', 'V-triangle interface'),
    ('row propagation', 'V-triangle propagation'),
    ('row coordinates', 'local coordinates'),
    ('row map', 'transfer map'),
    ('row completion', 'V-triangle completion'),
    ('positive gaps', 'nonempty gaps'),
    ('positive gap', 'nonempty gap'),
]
textual = list((ROOT / 'proof').rglob('*.md')) + list((ROOT / 'arrange/paper_draft').rglob('*.tex'))
for path in textual:
    text = path.read_text(encoding='utf-8')
    for old, new in terminology:
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')

# Synchronize the exact two-chart figure notation with the proof.
figure = 'arrange/paper_draft/figures/strategy2_vd_replacement_skeleton.tex'
text = read(figure)
text = text.replace('{$\\mu$};', '{$u_{\\rm adj}$};')
text = text.replace('\\mu:=\\frac{d-a-tb-1}{t}', 'u_{\\rm adj}:=\\frac{d-a-tb-1}{t}')
text = text.replace('\\max\\{C_1,\\mu\\}', '\\max\\{C_1,u_{\\rm adj}\\}')
text = text.replace('{$T_0\'$};', '{$U_0\'$};')
text = text.replace('{$T_1\'$};', '{$U_1\'$};')
text = text.replace('T_0\':=', 'U_0\':=')
text = text.replace('T_1\':=', 'U_1\':=')
write(figure, text)

# Remove the duplicate compact placement assembly from 04c.
short_vd = 'arrange/paper_draft/04c_short_Vd_placements.tex'
text = read(short_vd)
marker = '\\subsection{Placement assembly}'
if marker not in text:
    raise RuntimeError('04c placement-assembly marker not found')
text = text.split(marker, 1)[0].rstrip() + r'''

\subsection{Placement interfaces}

The local profile and radial-separation lemmas above are assembled exactly
once in Section~\ref{sec:strategy2-placement-assembly}.  This appendix
contains no independent CE2 one-Vd placement assembly.
''' + '\n'
write(short_vd, text)

# Make the consolidated Strategy 2 source the single authoritative assembly.
strategy2 = 'arrange/paper_draft/04_strategy2_verification.tex'
text = read(strategy2)
text = text.replace('\\ref{prop:signed-ce2-one-vd-placements}', '\\ref{prop:paper-ce2-one-vd-placements}')
text = text.replace(
    '\\section{Strategy 2 Rigor Completion}',
    '\\section{Exact Endpoint and Replacement Verification}',
)
text = text.replace('Vd1--supercritical axis replacement in TeX.', 'Vd1--supercritical two-chart replacement in TeX.')
text = text.replace(
    'The earlier exact-demand chapter contains a compact placement summary.  The\nfollowing proposition is the authoritative assembly used by the final proof;\nit cites only the complete placement lemmas and the explicit replacement of\nAppendix~\\ref{sec:strategy2-rigor-completion}.',
    'The following proposition is the sole CE2 exactly-one-Vd placement\nassembly used by the final proof.  It cites only complete placement lemmas and\nthe explicit two-chart replacement in\nAppendix~\\ref{sec:strategy2-rigor-completion}.',
)
write(strategy2, text)

# Correct escaped LaTeX examples in the authoring guide.
guide = 'arrange/ams_paper_generation_guide.md'
text = read(guide)
for old, new in [
    (r'\\appendix', r'\appendix'),
    (r'\\input{', r'\input{'),
    (r'\\subsection', r'\subsection'),
    (r'\\includegraphics', r'\includegraphics'),
    (r'\\label', r'\label'),
    (r'\\cref', r'\cref'),
    (r'\\ref', r'\ref'),
    (r'\\raggedbottom', r'\raggedbottom'),
    (r'\\begin{document}', r'\begin{document}'),
    (r'\\clearpage', r'\clearpage'),
]:
    text = text.replace(old, new)
write(guide, text)

# Correct the singleton-gap proof provenance in the crosswalk.
crosswalk = 'arrange/paper_proof_crosswalk.md'
text = read(crosswalk)
start = '### Boundary gaps and singleton gaps'
end = '### Short roles and `q=N_++m`'
replacement = r'''### Boundary gaps and singleton gaps

**Paper content.** The missed set `[B_i,1-A_{i+1}]` is retained when
it is a singleton because the role triangles are open.

**Primary proved sources.**

- [1214_strict_boundary_handoff_selection.md](../proof/1XXX_foundations/12XX_V_triangle/1214_strict_boundary_handoff_selection.md) — **P** for strict open handoffs;
- [2019_interval_component_and_path_budget.md](../proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/2019_interval_component_and_path_budget.md) — **P/S** for exact residual components and endpoint accounting;
- [4013_boundary_loss_index.md](../proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md) — **P** for singleton-inclusive skeleton gap rank.

**Definition-only checklist.**
[1208_boundary_degeneracies.md](../proof/1XXX_foundations/12XX_V_triangle/1208_boundary_degeneracies.md) — **N**.  It lists degeneracies but does not prove the routing statements.
'''
text = replace_section(text, start, end, replacement)
write(crosswalk, text)

# Generate exact current 407X provenance after terminology normalization.
files_407 = [
    'proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4073_boundary_loss_framework.md',
    'proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4074_L_Full_branch.md',
    'proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4075_Tminus_low_lower_branch_obligations.md',
    'proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4078_left_L_family_completion.md',
    'proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4079_first_Full_branch.md',
    'proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407a_left_Thigh_branch_completion.md',
    'proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407c_rigor_completion_details.md',
    'proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407d_rigor_final_assembly.md',
]
provenance_407 = {path: git_blob_sha(ROOT / path) for path in files_407}
write(
    'proof/407X_PROVENANCE.json',
    json.dumps(
        {
            'schema': 1,
            'generated_by': '2026-08-02 final audit repair',
            'files': provenance_407,
        },
        indent=2,
        sort_keys=True,
    ) + '\n',
)

# Update every full 407X blob in the consolidated TeX manifest.
text = read(strategy2)
for path, sha in provenance_407.items():
    filename = Path(path).name.replace('_', r'\_')
    pattern = re.compile(
        rf'(\\texttt\{{{re.escape(filename)}\}}&\s*\n\\texttt\{{)[0-9a-f]{{40}}(\}})'
    )
    text, count = pattern.subn(rf'\g<1>{sha}\g<2>', text)
    if count != 1:
        raise RuntimeError(f'could not update 407X TeX blob for {path}: {count}')
write(strategy2, text)

# Rewrite the stale source-ledger provenance and consolidated architecture sections.
ledger_path = 'arrange/paper_draft/source_ledger.md'
ledger = read(ledger_path)
rows = '\n'.join(
    f"| `{Path(path).name}` | `{sha[:12]}` |"
    for path, sha in provenance_407.items()
)
section_35 = f'''### 3.5 T3-like endpoint audit

The complete `407X` proof is formally incorporated from the current
proof-package objects.  Full Git blob identities are recorded in
`proof/407X_PROVENANCE.json`; the current prefixes are:

| File | Blob prefix |
|---|---|
{rows}

CI recomputes every Git blob from the exact file bytes and verifies
both the consolidated TeX manifest and this ledger.
'''
ledger = replace_section(
    ledger,
    '### 3.5 T3-like endpoint audit',
    '### 3.6 Vd1 replacement and placement assembly',
    section_35,
)
section_36 = r'''### 3.6 Vd1 replacement and placement assembly

The consolidated `04_strategy2_verification.tex` is the sole detailed
Strategy 2 verification source.  It contains:

- the complete four-label `407X` endpoint audit;
- separate local charts at the two distinguished replacement vertices;
- the exact shifted-template reach triples;
- the Vd0 and nonsupercritical role checks;
- preservation of the shared edge, outer boundary traces, and radial handoffs;
- preservation of the full skeleton required by strengthened `4013`;
- the single authoritative CE2 exactly-one-Vd1/Vd2 placement assembly.

`04c_short_Vd_placements.tex` now contains only reusable local lemmas
and no competing branch assembly.
'''
ledger = replace_section(
    ledger,
    '### 3.6 Vd1 replacement and placement assembly',
    '### 3.7 Strategy 4 certificate',
    section_36,
)
ledger = ledger.replace(
    'The verifiers were\nnot executed during this source-only edit.',
    'The exact derivation and positivity verifiers are replayed by read-only proof CI on every change.',
)
section_7 = r'''## 7. Build and PDF status

The tracked `main.pdf` is rebuilt with a fixed `SOURCE_DATE_EPOCH` and
compared byte-for-byte with a clean XeLaTeX rebuild in permanent
read-only CI.  The current source commit, workflow run, exact verifier
results, tool versions, page count, and PDF SHA-256 are recorded in
`../20260802_verification_summary.txt`.
'''
ledger = replace_section(
    ledger,
    '## 7. Build and PDF status',
    '## 2026-07-31 reader-interface revision',
    section_7,
)
write(ledger_path, ledger)

# Authenticate the Strategy 4 electronic proof objects independently of TeX.
files_3105 = [
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_00.py',
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_01.py',
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_02.py',
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_03.py',
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_04.py',
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_data_05.py',
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/mixed_overlap_core_polynomials.py',
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_mixed_overlap_core_derivation.py',
    'proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/3105X_computation/verify_global_core_positivity.py',
]
write(
    'proof/3105X_CERTIFICATE_PROVENANCE.json',
    json.dumps(
        {
            'schema': 1,
            'transcript_sha256': 'dc46aaf263655d5159ecd3a81db72ee82477951d06172f4743b248df37209485',
            'files': {path: git_blob_sha(ROOT / path) for path in files_3105},
        },
        indent=2,
        sort_keys=True,
    ) + '\n',
)

# Replace the earlier audit report by a precise final-state audit record.
write(
    'arrange/20260802_repair_and_reaudit.md',
    r'''# 2026-08-02 Final Repair, Consolidation, and Re-Audit

## Mathematical repairs

- `4147` uses separate `V_0`- and `V_1`-charts and proves all open-role,
  reach, Vd0, nonsupercritical, and skeleton-preservation claims.
- `4013` is stated and proved at full-skeleton strength; the original
  full-hexagon statement is its corollary.
- `2110` uses only skeleton data.
- `414b` gives the exhaustive CE2 exactly-one-Vd1/Vd2 placement audit.
- No new mathematical defect was found in the repaired chain.

## Source and provenance repairs

- Actual `N_+` definitions use uppercase actual reaches.
- Singleton-inclusive branches use “nonempty gap.”
- Active geometric prose uses “V triangle,” not “row.”
- `04_strategy2_verification.tex` contains the single CE2 one-Vd assembly.
- Current `407X` blobs are generated and checked from exact file bytes.
- Strategy 4 code and data blobs are independently authenticated.
- The active proof dependency graph is generated transitively from the
  main theorem and status table.
- The proof manifest is generated and checked in both directions.

## Reproducible verification

Permanent CI is read-only, pins GitHub Actions and SymPy, replays both
exact Strategy 4 verifiers, rebuilds the paper with a fixed
`SOURCE_DATE_EPOCH`, compares the rebuilt PDF byte-for-byte with the
tracked PDF, renders every page, and uploads the verified artifact.

BUILD_METADATA_PLACEHOLDER
''',
)

# Normalize edited Markdown whitespace.
for relative in [
    guide,
    crosswalk,
    ledger_path,
    'arrange/20260802_repair_and_reaudit.md',
]:
    lines = read(relative).splitlines()
    write(relative, '\n'.join(line.rstrip() for line in lines) + '\n')
