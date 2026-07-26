from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_exact(path: Path, old: str, new: str, *, count: int = 1) -> None:
    text = path.read_text(encoding="utf-8")
    actual = text.count(old)
    if actual != count:
        raise RuntimeError(f"{path}: expected {count} copies, found {actual}: {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


def replace_between(path: Path, start: str, end: str, replacement: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(start) != 1 or text.count(end) != 1:
        raise RuntimeError(f"{path}: non-unique block markers {start!r}, {end!r}")
    i = text.index(start)
    j = text.index(end, i)
    path.write_text(text[:i] + replacement + "\n\n" + text[j:], encoding="utf-8")


# Correct the high-sheet variable at the source and retire the explanatory
# alias file.
for relative in [
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407a_left_Thigh_branch_completion.md",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407c_rigor_completion_details.md",
]:
    replace_exact(ROOT / relative, r"u=\gamma_5,", r"\nu=\gamma_5,")

index_407 = ROOT / "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md"
replace_exact(
    index_407,
    "The branch proofs retain $\\beta,m_\\beta$ where that notation is shorter; the\n"
    "independent center radical $\\sqrt{r^2-r+1}$ remains necessary. The high-sheet\n"
    "center variable is $\\nu=\\gamma_5$ throughout `407a` and Section 2 of `407c`;\n"
    "[`407e`](407e_high_sheet_symbol_convention.md) records the exact symbol\n"
    "convention and separates it from the unrelated local variable $u$ in `407c`.",
    "The branch proofs retain $\\beta,m_\\beta$ where that notation is shorter; the\n"
    "independent center radical $\\sqrt{r^2-r+1}$ remains necessary.  The high-sheet\n"
    "center variable is written explicitly as $\\nu=\\gamma_5$ throughout `407a`\n"
    "and Section 2 of `407c`, while the unrelated local variable $u$ remains confined\n"
    "to the center-transfer lemma.",
)
replace_exact(
    index_407,
    "| [`407e_high_sheet_symbol_convention.md`](407e_high_sheet_symbol_convention.md) | Definition | Fixes $\\nu=\\gamma_5$ as the common high-sheet center variable and distinguishes it from the unrelated local $u$ in `407c`. |\n",
    "",
)
replace_exact(
    index_407,
    "| $T_+^{hi}$ | `407a`, with details in `407c`, common curvature in `2016`, and symbol convention in `407e` |",
    "| $T_+^{hi}$ | `407a`, with details in `407c` and common curvature in `2016` |",
)

symbol_file = ROOT / "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407e_high_sheet_symbol_convention.md"
if not symbol_file.exists():
    raise RuntimeError(f"missing expected symbol file: {symbol_file}")
symbol_file.unlink()

# Replace the long T3-like local polynomial proof by the rational profile and
# common rescuer theorem proved in 04c.
exact = ROOT / "arrange/paper_draft/04_strategy2_exact_demand.tex"
t3_replacement = r"""\subsection{The exactly-one-$T3$ branch}

\begin{proposition}[Exactly one T3-like row]
\label{prop:nplus-one-one-t3}
Assume the center role is CE1 or CE2, $N_+=1$, exactly one vertex role is
T3-like, and no role is Vd1 or Vd2.  Then the roles do not cover $H$.
\end{proposition}

\begin{proof}
Normalize the center midpoint to $M_0$.  A T3-like row misses its own
midpoint, a supercritical row misses its local midpoint, and a Vd0 row cannot
rescue a neighboring midpoint.  Consequently, after reflection,
\[
 T_0\text{ is T3-like},\qquad M_1\in T_0,
 \qquad T_1\text{ is uniquely supercritical},
\]
and $T_2,\ldots,T_5$ are nonsupercritical Vd0 rows.  The rational local
calculation is Lemma~\ref{lem:short-t3-rescuer-profile}.  It verifies the two
local inequalities in \eqref{eq:signed-rescuer-local}, while midpoint and
support isolation force the center to cover the $O$-side radial gap.  The
common adjacent-rescuer obstruction, Corollary~\ref{cor:signed-adjacent-rescuers},
therefore gives the contradiction.
\end{proof}"""
replace_between(
    exact,
    r"\subsection{The exactly-one-$T3$ branch}",
    r"\subsection{The nonsupercritical CE1/CE2 boundary packages}",
    t3_replacement,
)

# Replace the repeated Vd1 hiding proof by the local profile corollary.
vd_replacement = r"""\begin{lemma}[Vd1 adjacent rescue]
\label{lem:vd1-adjacent-rescue}
Assume an original open-role skeleton cover in the CE2 exact-$M_0$ branch,
with $T_0$ the unique Vd1 row, $M_1\in T_0$, $T_1$ uniquely supercritical,
$T_2,\ldots,T_5$ nonsupercritical Vd0, and no other positive-adjacent-support
role.  Then the perimeter together with $r_1$ is not covered.
\end{lemma}

\begin{proof}
Lemma~\ref{lem:short-vd1-rescuer-profile} proves the two local inequalities
in \eqref{eq:signed-rescuer-local}.  Midpoint and support isolation force the
center to cover the $O$-side radial gap before the Vd1 interval.  The result is
therefore Corollary~\ref{cor:signed-adjacent-rescuers}.
\end{proof}"""
replace_between(
    exact,
    r"\begin{lemma}[Vd1 adjacent rescue]",
    r"\begin{lemma}[Vd1--supercritical replacement]",
    vd_replacement,
)

replace_exact(exact, "\\input{04a_strategy2_half_edge_envelope}\n\n", "")

replace_exact(
    exact,
    "For CE2, the exactly-one-gap state is\n"
    "Proposition~\\ref{prop:signed-ce2-one-gap}; if both center intervals contain gaps, the\n"
    "endpoint bounds and exact exits are those of\n"
    "Lemma~\\ref{lem:two-endpoint-capped-loss}, so the two far outgoing reaches sum\n"
    "to less than one.  Rows $2,3,4$ would then have to cover more than three\n"
    "boundary units, contradicting their three nonsupercritical caps.",
    "For CE2, the exactly-one-gap state is\n"
    "Proposition~\\ref{prop:signed-ce2-one-gap}; the two-gap state is the common\n"
    "application in Proposition~\\ref{prop:reader-common-two-gap}.",
)

# Use explicit center intervals in the nonadjacent placement proof.
short_vd = ROOT / "arrange/paper_draft/04c_short_Vd_placements.tex"
replace_exact(
    short_vd,
    "B=e_{I_R}(b_0),\n \\qquad U=e_{I_L}(a_0),",
    "B=e_{[y,W+\\delta]}(b_0),\n \\qquad U=e_{[x,R+\\alpha]}(a_0),",
)

print("unification edits applied successfully")
