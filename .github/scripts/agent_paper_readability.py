from __future__ import annotations

from pathlib import Path
import re

ROOT = Path.cwd()
PAPER = ROOT / "arrange" / "paper_draft"


def load(rel: str) -> str:
    path = ROOT / rel
    if not path.exists():
        raise FileNotFoundError(rel)
    return path.read_text(encoding="utf-8")


def save(rel: str, text: str) -> None:
    path = ROOT / rel
    path.write_text(text, encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one literal occurrence, found {count}")
    return text.replace(old, new, 1)


def replace_between(text: str, start: str, end: str, new: str, label: str) -> str:
    i = text.find(start)
    if i < 0:
        raise RuntimeError(f"{label}: start marker not found")
    j = text.find(end, i + len(start))
    if j < 0:
        raise RuntimeError(f"{label}: end marker not found")
    return text[:i] + new + text[j:]


def replace_table_by_label(text: str, label: str, new: str) -> str:
    marker = f"\\label{{{label}}}"
    pos = text.find(marker)
    if pos < 0:
        raise RuntimeError(f"table label not found: {label}")
    start = text.rfind("\\begin{table}[H]", 0, pos)
    end = text.find("\\end{table}", pos)
    if start < 0 or end < 0:
        raise RuntimeError(f"table bounds not found: {label}")
    end += len("\\end{table}")
    return text[:start] + new + text[end:]


# ---------------------------------------------------------------------------
# 1. Body: Proposition 2.5 becomes a qualitative interface; exact formulas
#    and the two formula-heavy figures remain in Appendix B.
# ---------------------------------------------------------------------------
rel = "arrange/paper_draft/02_reader_framework.tex"
text = load(rel)
start = "\\begin{proposition}[Explicit admissible-set description]"
end = "\\subsection{The transfer alphabet and its inequality interface}"
new_admissible = r"""\begin{proposition}[Geometric structure of the admissible set]
\label{prop:body-admissible-description}
The local admissible set $\mathcal A$ has the following properties.
\begin{enumerate}
\item It is compact, coordinatewise downward closed, and invariant under
interchanging the two boundary coordinates $a$ and $b$.
\item Its enclosure-gauge description is
\[
 (a,b,c)\in\mathcal A
 \quad\Longleftrightarrow\quad
 \Lambda\bigl(K(a,b,c)\bigr)\le1.
\]
\item Every one-coordinate fiber of $\mathcal A$ is a nonempty compact initial
interval.  In particular, each maximum used to define a transfer map below is
attained.
\item The boundary of $\mathcal A$ is obtained from a finite caliper
comparison.  Equivalently, the least enclosing-equilateral side is the minimum
of finitely many continuous support expressions on finitely many geometric
cells.
\end{enumerate}
The exact support expressions, their cell conditions, and the resulting
piecewise equations for $\mathcal A$ are stated and proved in
Appendix~\ref{sec:admissible-set-derivation}.
\end{proposition}

\begin{proof}
Compactness and downward closure follow directly from the containment
definition and compactness of the oriented unit-triangle family modulo
translation.  Reflection in the radial axis exchanges $a$ and $b$.  The gauge
equivalence is Proposition~\ref{prop:universal-enclosure-gauge}.  Convexity of
containment along each coordinate gives the initial-interval fibers.  The
finite-caliper assertion and all exact cell formulas are proved in
Appendix~\ref{sec:admissible-set-derivation}.
\end{proof}

\begin{figure}[H]
\centering
\resizebox{.98\linewidth}{!}{%
\input{figures/strategy2_enclosure_gauge_skeleton}}
\caption{The support-function definition of the equilateral enclosure gauge,
placed in the full skeleton containing the local demand hull.  This figure is
a geometric sketch; the exact caliper equations are in Appendix~\ref{sec:admissible-set-derivation}.}
\label{fig:strategy2-enclosure-gauge-skeleton}
\end{figure}

\subsection{The transfer alphabet and its inequality interface}"""
text = replace_between(text, start, end, new_admissible, "Proposition 2.5 block")

# Definition 2.12: retain geometric definitions and properties only.
start = "\\begin{definition}[Signed CE1/CE2 center normal form]"
end = "\\begin{proposition}[Signed center interface]"
new_center_definition = r"""\begin{definition}[Geometric signed CE1/CE2 center data]
\label{def:body-signed-center-data}
Normalize one positive-length center trace to $e_{0,1}$.  The signed affine
normal form of Appendix~\ref{sec:signed-ce12-reductions} assigns to the
normalized center triangle a parameter triple $(R,\alpha,\delta)$ in its exact
signed domain $\mathcal D_{\rm sgn}$; write the resulting closed center
triangle as $T_C(R,\alpha,\delta)$.

Let $\mathcal I_{\mathrm R}=T_C\cap e_{0,1}$ be the normalized active trace,
and let $\mathcal I_{\mathrm L}=T_C\cap e_{5,0}$ be the possible companion
trace.  Denote their lengths by $\ell_R$ and $\ell_L$.  The signed companion
coordinate $\sigma_L$ is the affine quantity defined in Appendix
\ref{sec:signed-ce12-reductions}; its sign records whether the companion trace
has positive length.

For each $i\in\mathbb Z/6\mathbb Z$, let $d_i^C$ denote the farthest parameter
reached by $T_C$ on the radial arm $r_i$, measured from $O$ toward $V_i$, and
put $c_i^C=1-d_i^C$.  Thus $d_i^C$ is the center-side radial exit and $c_i^C$
is the complementary radial demand imposed on the V triangle $T_i$.
\end{definition}

"""
text = replace_between(text, start, end, new_center_definition, "Definition 2.12 block")

start = "\\begin{proposition}[Signed center interface]"
end = "\\input{02c_strategy2_skeleton_atlas}"
new_center_prop = r"""\begin{proposition}[Signed center interface]
\label{prop:body-signed-center-interface}
For the normalization of Definition~\ref{def:body-signed-center-data}, the
active trace $\mathcal I_{\mathrm R}$ has positive length.  The center type is
read from the companion trace:
\[
 T_C\text{ is CE1}
 \quad\Longleftrightarrow\quad
 \ell_L=0,
 \qquad
 T_C\text{ is CE2}
 \quad\Longleftrightarrow\quad
 \ell_L>0.
\]
Equivalently, CE2 is characterized by $\sigma_L>0$, while CE1 has
$\sigma_L\le0$; the equality case is a single companion contact point.
Moreover,
\[
 L_{\partial H}(T_C)=\ell_R+\ell_L,
\]
and the six exits $d_i^C$ and complementary demands $c_i^C$ are continuous
piecewise-algebraic functions of the signed parameters.  The bounds needed in
the reader-facing proof are
\[
 L_{\partial H}(T_C)\le \frac{\sqrt3}{2}-\frac34
 \quad\text{in CE1},
 \qquad
 L_{\partial H}(T_C)<\frac12
 \quad\text{in CE2}.
\]
All exact affine side equations, trace endpoints, exit formulas, and sign-cell
conditions are collected in Appendix~\ref{sec:signed-ce12-reductions}.
\end{proposition}

\begin{proof}
This is Proposition~\ref{prop:signed-center-normal-form} and
Corollary~\ref{cor:signed-center-boundary}.  Their exact calculation is kept in
Appendix~\ref{sec:signed-ce12-reductions}; only the geometric classification
and the two boundary bounds are used in the body.
\end{proof}

\input{02c_strategy2_skeleton_atlas}"""
text = replace_between(text, start, end, new_center_prop, "signed center proposition block")
save(rel, text)

# Move exact admissible-set diagrams to Appendix B.
rel = "arrange/paper_draft/02b_admissible_set_derivation.tex"
text = load(rel)
if "fig:strategy2-admissible-scalars-skeleton" not in text:
    text = text.rstrip() + r"""

\subsection{Exact admissible-set diagrams}

\begin{figure}[H]
\centering
\resizebox{.98\linewidth}{!}{%
\input{figures/strategy2_admissible_scalars_skeleton}}
\caption{The scalar and caliper-denominator data entering the exact
admissible-set formula.}
\label{fig:strategy2-admissible-scalars-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.98\linewidth}{!}{%
\input{figures/strategy2_admissible_minimum_skeleton}}
\caption{The complete piecewise least-enclosure function and its exact
relation to $\mathcal A$.}
\label{fig:strategy2-admissible-minimum-skeleton}
\end{figure}
""" + "\n"
save(rel, text)

# Keep only geometric signed-center sketches in the body atlas.
rel = "arrange/paper_draft/02c_strategy2_skeleton_atlas.tex"
text = r"""\subsection{Hexagon-skeleton atlas for the two interfaces}
\label{sec:interface-notation-atlas}

The figures below place the reader-facing transfer and signed-center objects on
the regular hexagon skeleton.  Dashed extremal segments are not actual traces,
and panels marked schematic record incidence and order rather than metric
placement.  Exact admissible-set and signed-center equations are intentionally
kept in Appendices~\ref{sec:admissible-set-derivation} and
\ref{sec:signed-ce12-reductions}.

\begin{figure}[H]
\centering
\resizebox{.92\linewidth}{!}{\input{figures/transfer_row_coordinates}}
\caption{Selected demands, actual V-triangle reaches, incoming defect, raw
extremal output, and the center-free complementary handoff.}
\label{fig:transfer-row-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.90\linewidth}{!}{\input{figures/transfer_raw_hat_dual}}
\caption{The zero-radial geometry and the complement dual.  The identity is
$\widehat g_0$, not raw $g_0$.}
\label{fig:transfer-zero-dual-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.99\linewidth}{!}{\input{figures/center_interval_residual}}
\caption{The three geometric cases in the residual operator
$\mathcal R_{[L,U]}(p)$, drawn on a handoff edge.}
\label{fig:transfer-residual-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.90\linewidth}{!}{\input{figures/supercritical_envelope}}
\caption{A representative strict-supercritical envelope configuration.  Its
outgoing bound is unconditional; only a center-free edge permits the
complementary next-V-triangle bound.}
\label{fig:transfer-supercritical-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.96\linewidth}{!}{%
\input{figures/strategy2_transfer_domains_skeleton}}
\caption{The interval family $\mathfrak J$, strict-supercritical input set, and
its supremal output, shown on the skeleton.}
\label{fig:strategy2-transfer-domains-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.86\linewidth}{!}{\input{figures/relaxed_composition}}
\caption{Exact and lower-relaxed iterates placed on successive V triangles.}
\label{fig:relaxed-composition-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.99\linewidth}{!}{\input{figures/signed_center_traces}}
\caption{Representative CE1 and CE2 center triangles on the full skeleton.
The blue segments are the geometric boundary traces; exact parameter equations
are in Appendix~\ref{sec:signed-ce12-reductions}.}
\label{fig:signed-center-samples-skeleton}
\end{figure}
"""
save(rel, text)

# Move the exact signed-center atlas panels to Appendix D.
rel = "arrange/paper_draft/04a_signed_center_calculus.tex"
text = load(rel)
if "fig:signed-parameter-skeleton" not in text:
    text = text.rstrip() + r"""

\subsection{Exact signed-center diagrams}

\begin{figure}[H]
\centering
\resizebox{.88\linewidth}{!}{\input{figures/signed_parameter_map}}
\caption{The affine center chart and the exact dependency structure of the
signed parameters.}
\label{fig:signed-parameter-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.84\linewidth}{!}{\input{figures/signed_companion_sign}}
\caption{The exact sign test for the candidate companion trace, including the
CE1 point-contact case.}
\label{fig:signed-companion-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.82\linewidth}{!}{\input{figures/signed_center_exits}}
\caption{The six exact center exits $d_i^C$ and complementary radial demands
$c_i^C=1-d_i^C$.}
\label{fig:signed-center-exits-skeleton}
\end{figure}

\begin{figure}[H]
\centering
\resizebox{.82\linewidth}{!}{\input{figures/signed_center_boundary_budgets}}
\caption{The exact CE1 and CE2 center-boundary contributions and their general
bounds.}
\label{fig:signed-center-budget-skeleton}
\end{figure}
""" + "\n"
save(rel, text)

# ---------------------------------------------------------------------------
# 2. Proposition 3.1: use one trace notation for every V triangle.
# ---------------------------------------------------------------------------
rel = "arrange/paper_draft/03_strategy1_reader.tex"
text = load(rel)
old = r"""\begin{proposition}[Trace-cap register]
\label{prop:body-trace-register}
Under the hypotheses indicated in each row,
\begin{center}"""
new = r"""\begin{proposition}[Trace-cap register]
\label{prop:body-trace-register}
For every classified V triangle $T_i$, the boundary trace is supported on its
two incident boundary edges, and therefore
\[
 L_{\partial H}(T_i)=A_i+B_i.
\]
Under the hypotheses indicated in each table entry, the following unified
trace bounds hold.
\begin{center}"""
text = replace_once(text, old, new, "Proposition 3.1 preamble")
text = text.replace("role and target&upper bound", "triangle role and target&upper bound")
text = text.replace("supercritical Vd0 role on $\\partial H$&$A_i+B_i\\le2/\\sqrt3$", "supercritical Vd0 V triangle on $\\partial H$&$L_{\\partial H}(T_i)\\le2/\\sqrt3$")
text = text.replace("Vd1 or Vd2 role on $\\partial H$&$A_i+B_i<1/2$", "Vd1 or Vd2 V triangle on $\\partial H$&$L_{\\partial H}(T_i)<1/2$")
text = text.replace("nonsupercritical Vd0 role on $\\partial H$&$A_i+B_i\\le1$", "nonsupercritical Vd0 V triangle on $\\partial H$&$L_{\\partial H}(T_i)\\le1$")
text = text.replace("T3-like role on $\\partial H$&$A_i+B_i<1$", "T3-like V triangle on $\\partial H$&$L_{\\partial H}(T_i)<1$")
text = text.replace("supercritical Vd0 rows", "supercritical Vd0 V triangles")
text = text.replace("distinguished nonsupercritical rows", "distinguished nonsupercritical V triangles")
text = text.replace("every remaining row", "every remaining V triangle")
text = text.replace("remaining rows substitute", "remaining branches substitute")
text = text.replace("unlisted rows bounded", "unlisted V triangles bounded")
save(rel, text)

# ---------------------------------------------------------------------------
# 3. Strategy 2: imported exact signed auxiliaries and a true six-slot table.
# ---------------------------------------------------------------------------
rel = "arrange/paper_draft/04_strategy2_summary.tex"
text = load(rel)
intro_marker = "\\begin{definition}[Geometric-order composition and identity slots]"
import_note = r"""\paragraph{Signed-center auxiliaries used by the certificates.}
Definition~\ref{def:body-signed-center-data} gives the geometric meaning of the
signed center data.  Appendix~\ref{sec:signed-ce12-reductions} defines the
associated auxiliary functions $W,E,\eta,P,k,\Delta_R,\Delta_L$ and the exact
semialgebraic domain $\mathcal D_{\rm sgn}$.  The reader-facing argument uses
those named functions and domains, but does not repeat their affine equations.

"""
if import_note not in text:
    text = replace_once(text, intro_marker, import_note + intro_marker, "Strategy 2 signed auxiliary import")
text = text.replace("With $W,E,P,\\Delta_R,\\Delta_L$ as in\nDefinition~\\ref{def:body-signed-center-data}, define", "With the exact signed auxiliary functions and domain from\nAppendix~\\ref{sec:signed-ce12-reductions}, define")
text = text.replace("with $W,\\eta,k$ as in\nDefinition~\\ref{def:body-signed-center-data},", "with $W,\\eta,k$ as defined in\nAppendix~\\ref{sec:signed-ce12-reductions},")

six_slot_definition_and_table = r"""\begin{definition}[Full six-slot V-triangle chain]
\label{def:body-six-slot-chain}
For each $i\in\mathbb Z/6\mathbb Z$, let
\[
 J_i^C:=\xi_i^{-1}(T_C\cap e_{i,i+1})\in\mathfrak J
\]
be the scalar center interval on the outgoing edge of $T_i$.  Define the exact
raw and nonsupercritical V-triangle transfers
\[
 \Phi_i^{\rm raw}:=g_{c_i,J_i^C}^{\vee},
 \qquad
 \Phi_i^{\rm ns}:=\widehat g_{c_i,J_i^C}^{\vee}.
\]
The full cyclic chain is always written with six explicit slots in geometric
V-triangle order:
\[
 [\Phi_0\mid\Phi_1\mid\Phi_2\mid\Phi_3\mid\Phi_4\mid\Phi_5].
\]
If $T_i$ is nonsupercritical and the outgoing edge is an ordinary
center-free handoff, then $J_i^C=\varnothing$ and
\[
 A_{i+1}\ge\widehat g_{c_i}^{\vee}(A_i)\ge A_i.
\]
Only under this condition, together with exclusion of nonincident boundary
traces on that edge, may the $i$th slot be lowered to $\mathrm I$.
\end{definition}

\begin{table}[H]
\centering
\scriptsize
\renewcommand{\arraystretch}{1.18}
\begin{tabular}{@{}p{.20\textwidth}p{.69\textwidth}@{}}
\toprule
branch&six explicitly displayed functions and the certified relaxation\\
\midrule
$N_+=0$, all Vd0, $\mathrm{gr}=0$
&$[\widehat g_{c_0}^{\vee}\mid\widehat g_{c_1}^{\vee}\mid
\widehat g_{c_2}^{\vee}\mid\widehat g_{c_3}^{\vee}\mid
\widehat g_{c_4}^{\vee}\mid\widehat g_{c_5}^{\vee}]
\ \succeq\ [\mathrm I\mid\mathrm I\mid\mathrm I\mid
\mathrm I\mid\mathrm I\mid\mathrm I]$; strict cyclic ascent.\\
\addlinespace
$N_+=0$, all Vd0, $\mathrm{gr}=1$
&After cyclic normalization $J_0^C\ne\varnothing$:
$[\widehat g_{c_0,J_0^C}^{\vee}\mid\widehat g_{c_1}^{\vee}\mid
\widehat g_{c_2}^{\vee}\mid\widehat g_{c_3}^{\vee}\mid
\widehat g_{c_4}^{\vee}\mid\widehat g_{c_5}^{\vee}]
\ \succeq\ [\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1}^{\vee}\mid\mathrm I\mid\mathrm I\mid\mathrm I\mid
\widehat g_{c_5}^{\vee}]$; one-gap endpoint sum $<1$.\\
\addlinespace
CE2, $\mathrm{gr}=2$
&With the two center-trace intervals normalized as $J_0^C,J_5^C$:
$[\widehat g_{c_0,J_0^C}^{\vee}\mid\widehat g_{c_1}^{\vee}\mid
\widehat g_{c_2}^{\vee}\mid\widehat g_{c_3}^{\vee}\mid
\widehat g_{c_4}^{\vee}\mid\widehat g_{c_5,J_5^C}^{\vee}]
\ \succeq\ [\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1}^{\vee}\mid\mathrm I\mid\mathrm I\mid\mathrm I\mid
\widehat g_{c_5,J_5^C}^{\vee}]$; paired endpoint sum $<1$.\\
\addlinespace
$N_+=0$, one T3-like V triangle
&For the support-isolated T3-like V triangle $T_0$:
$[\widehat g_{c_0,J_0^C}^{\vee}\mid\widehat g_{c_1}^{\vee}\mid
\widehat g_{c_2}^{\vee}\mid\widehat g_{c_3}^{\vee}\mid
\widehat g_{c_4}^{\vee}\mid\widehat g_{c_5,J_5^C}^{\vee}]
\ \succeq\ [\widehat g_{c_0,J_0^C}^{\vee}\mid
\widehat g_{c_1}^{\vee}\mid\mathrm I\mid\mathrm I\mid\mathrm I\mid
\widehat g_{c_5,J_5^C}^{\vee}]$; audited four-label endpoint sum $<1$.\\
\addlinespace
$N_+=1$, all Vd0, one gap
&With $T_0$ the unique strictly supercritical V triangle:
$[g_{c_0,J_0^C}^{\vee}\mid\widehat g_{c_1}^{\vee}\mid
\widehat g_{c_2}^{\vee}\mid\widehat g_{c_3}^{\vee}\mid
\widehat g_{c_4}^{\vee}\mid\widehat g_{c_5}^{\vee}]$.
The proof retains the exact five-slot hatted subchain on
$T_1,\ldots,T_5$ and closes the $T_0$ slot by
$A_0<1-h_{\mathrm{term}}<Z$.\\
\bottomrule
\end{tabular}
\caption{The reader-facing Strategy~2 $g$-composition register.  Each displayed
$\mathrm I$ is justified by the explicit handoff inequality in
Definition~\ref{def:body-six-slot-chain}; it is not an informal placeholder.}
\label{tab:body-strategy2-chains}
\end{table}

\begin{center}
\small
\begin{tabular}{p{.36\textwidth}p{.52\textwidth}}
\toprule
non-composition terminal&certificate\\
\midrule
one T3-like or adjacent Vd1 rescuer&strict-supercritical envelope versus an
ordinary center-free boundary path\\
adjacent Vd1/Vd2&two center residuals and the quarter-radial envelope\\
nonadjacent Vd1/Vd2&two center residuals and the Vd corner margin\\
Vd1--supercritical pair&two explicit axis replacements followed by the
all-Vd0 contradiction\\
\bottomrule
\end{tabular}
\end{center}"""
text = replace_table_by_label(text, "tab:body-strategy2-chains", six_slot_definition_and_table)
save(rel, text)

# ---------------------------------------------------------------------------
# 4. Reader-facing terminology: no standalone “row” for a V triangle.
#    Protect labels, references, and input paths so cross-references are stable.
# ---------------------------------------------------------------------------
protected_command = re.compile(r"\\(?:label|ref|eqref|pageref|autoref|input|includegraphics)\{[^{}]*\}")


def clean_latex_rows(s: str) -> str:
    held: list[str] = []
    def hold(m: re.Match[str]) -> str:
        held.append(m.group(0))
        return f"@@PROTECTEDCOMMAND{len(held)-1}@@"
    s = protected_command.sub(hold, s)
    fixes = {
        "routing rows": "routing entries",
        "routing row": "routing entry",
        "table rows": "table entries",
        "table row": "table entry",
        "row of Table": "entry of Table",
        "rows of Table": "entries of Table",
        "first applicable row": "first applicable entry",
        "last row": "last entry",
        "matrix rows": "matrix lines",
        "matrix row": "matrix line",
        "array rows": "array lines",
        "array row": "array line",
    }
    for a, b in fixes.items():
        s = s.replace(a, b)
    s = re.sub(r"\brows\b", "V triangles", s)
    s = re.sub(r"\brow\b", "V triangle", s)
    s = re.sub(r"\bRows\b", "V triangles", s)
    s = re.sub(r"\bRow\b", "V triangle", s)
    compounds = {
        "V triangle order": "V-triangle order",
        "V triangle count": "V-triangle count",
        "V triangle data": "V-triangle reach data",
        "V triangle coordinates": "V-triangle reach coordinates",
        "five-V triangle": "five-V-triangle",
        "four-V triangle": "four-V-triangle",
        "three-V triangle": "three-V-triangle",
        "next-V triangle": "next-V-triangle",
    }
    for a, b in compounds.items():
        s = s.replace(a, b)
    for idx, original in enumerate(held):
        s = s.replace(f"@@PROTECTEDCOMMAND{idx}@@", original)
    return s

for path in PAPER.glob("*.tex"):
    path.write_text(clean_latex_rows(path.read_text(encoding="utf-8")), encoding="utf-8")
for path in (PAPER / "figures").glob("*.tex"):
    path.write_text(clean_latex_rows(path.read_text(encoding="utf-8")), encoding="utf-8")

# ---------------------------------------------------------------------------
# 5. Canonical proof package: establish the full six-slot chain formally and
#    normalize terminology in proved/active reader-facing notes.  Historical
#    filenames remain unchanged so links and the manifest stay stable.
# ---------------------------------------------------------------------------
rel = "proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md"
text = load(rel)
if "## 10. Full six-V-triangle branch chain" not in text:
    text = text.rstrip() + r"""

## 10. Full six-V-triangle branch chain

For each $i\in\mathbb Z/6\mathbb Z$, parametrize the outgoing edge by

$$
\xi_i(t)=V_i+t(V_{i+1}-V_i),
\qquad 0\le t\le1,
$$

and let

$$
J_i^C=\xi_i^{-1}(T_C\cap e_{i,i+1})
$$

be the empty or closed scalar center interval.  For a selected radial demand
$c_i$, define

$$
\Phi_i^{\rm raw}=g_{c_i,J_i^C}^{\vee},
\qquad
\Phi_i^{\rm ns}=\widehat g_{c_i,J_i^C}^{\vee}.
$$

Use $\Phi_i^{\rm ns}$ when $T_i$ is nonsupercritical and
$\Phi_i^{\rm raw}$ otherwise.  The generalized handoff lemma gives

$$
A_{i+1}\ge \Phi_i(A_i)
\qquad(i\in\mathbb Z/6\mathbb Z).
$$

Consequently the exact cyclic certificate is the six-slot composition

$$
\boxed{
A_0\ge
[\Phi_0\mid\Phi_1\mid\Phi_2\mid\Phi_3\mid\Phi_4\mid\Phi_5](A_0).
}
$$

The six functions must be displayed even when a terminal proof later cuts the
cycle at a center trace or replaces internal slots by lower relaxations.  An
identity replacement in slot $i$ is valid only when

$$
J_i^C=\varnothing,
$$

all nonincident boundary traces have been excluded on $e_{i,i+1}$, and $T_i$
is nonsupercritical.  Under precisely these hypotheses,

$$
A_{i+1}
\ge \widehat g_{c_i}^{\vee}(A_i)
\ge A_i,
$$

so

$$
\mathrm I\le\widehat g_{c_i}^{\vee}.
$$

For the $N_+=1$ all-Vd0 one-gap branch, $T_0$ uses the raw center-assisted
slot $g_{c_0,J_0^C}^{\vee}$ and $T_1,\ldots,T_5$ use the five hatted slots.
The one-gap proof retains that exact five-V-triangle subchain and closes the
remaining $T_0$ slot with its independent terminal diameter cap.  Thus the
reader-facing six-slot register is a faithful expansion of the proven
certificate, not a new or stronger assertion.
""" + "\n"
save(rel, text)

md_link_dest = re.compile(r"(?<=\]\()([^)]*)(?=\))")
inline_code = re.compile(r"`[^`\n]*`")


def clean_markdown_rows(s: str) -> str:
    held: list[str] = []
    def hold(m: re.Match[str]) -> str:
        held.append(m.group(0))
        return f"@@MDPROTECTED{len(held)-1}@@"
    s = md_link_dest.sub(hold, s)
    s = inline_code.sub(hold, s)
    for a, b in {
        "routing rows": "routing entries",
        "routing row": "routing entry",
        "table rows": "table entries",
        "table row": "table entry",
        "row of the table": "entry of the table",
        "row of Table": "entry of Table",
        "matrix rows": "matrix lines",
        "matrix row": "matrix line",
    }.items():
        s = s.replace(a, b)
    s = re.sub(r"\brows\b", "V triangles", s)
    s = re.sub(r"\brow\b", "V triangle", s)
    s = re.sub(r"\bRows\b", "V triangles", s)
    s = re.sub(r"\bRow\b", "V triangle", s)
    for a, b in {
        "V triangle order": "V-triangle order",
        "V triangle count": "V-triangle count",
        "V triangle data": "V-triangle reach data",
        "five-V triangle": "five-V-triangle",
        "four-V triangle": "four-V-triangle",
        "next-V triangle": "next-V-triangle",
    }.items():
        s = s.replace(a, b)
    for idx, original in enumerate(held):
        s = s.replace(f"@@MDPROTECTED{idx}@@", original)
    return s

canonical = {
    ROOT / "README.md",
    ROOT / "proof/09XX_appendices/0910_notation_dictionary.md",
    ROOT / "proof/0XXX_main/0000_main_theorem.md",
    ROOT / "proof/0XXX_main/0001_proof_tree_index.md",
    ROOT / "proof/0XXX_main/0002_status_and_dependencies.md",
    ROOT / "proof/1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md",
    ROOT / "arrange/ams_paper_generation_guide.md",
    ROOT / "arrange/paper_proof_crosswalk.md",
    ROOT / "arrange/paper_draft/source_ledger.md",
}
for path in (ROOT / "proof").rglob("*.md"):
    source = path.read_text(encoding="utf-8")
    if "Status: Proven" in source:
        canonical.add(path)
for path in sorted(canonical):
    if path.exists():
        path.write_text(clean_markdown_rows(path.read_text(encoding="utf-8")), encoding="utf-8")

rel = "proof/1XXX_foundations/12XX_V_triangle/1212_vertex_rows_and_Nplus.md"
text = load(rel)
text = re.sub(r"^# .*?$", "# Vertex V-Triangle Reaches and the Count $N_+$", text, count=1, flags=re.M)
save(rel, text)

rel = "arrange/paper_draft/source_ledger.md"
text = load(rel)
ledger_note = r"""

## 2026-07-31 reader-interface revision

- Proposition 2.5 now states only the definition-level and qualitative
  properties of the admissible set; its finite-caliper equations and formula
  diagrams are in Appendix B.
- Definition 2.12 now defines the signed center geometry without reproducing
  its affine equations; the exact chart, traces, exits, sign cells, and diagrams
  are in Appendix D.
- Proposition 3.1 uses $L_{\partial H}(T_i)$ uniformly for all four V-triangle
  boundary roles.
- Table 2 displays six functions in every $g$-composition chain and states the
  exact hypotheses under which an identity slot is a valid lower relaxation.
- Canonical proved notes use “V triangle” for the geometric object; historical
  filenames and link targets containing `row` were retained for repository
  stability.
"""
if "## 2026-07-31 reader-interface revision" not in text:
    text = text.rstrip() + ledger_note + "\n"
save(rel, text)

# ---------------------------------------------------------------------------
# 6. Static consistency assertions before compilation.
# ---------------------------------------------------------------------------
body2 = load("arrange/paper_draft/02_reader_framework.tex")
app_b = load("arrange/paper_draft/02b_admissible_set_derivation.tex")
app_d = load("arrange/paper_draft/04a_signed_center_calculus.tex")
strat1 = load("arrange/paper_draft/03_strategy1_reader.tex")
strat2 = load("arrange/paper_draft/04_strategy2_summary.tex")
canon = load("proof/2XXX_geometric_lemmas/20XX_V_triangle_geometry/201d_raw_and_relaxed_g_chains.md")

for forbidden in ["L_{OA}=", "L_{AC}=", "L_{\\min}(a,b,c)=", "F_0(a,b)&=", "d_i^C&E-"]:
    if forbidden in body2:
        raise RuntimeError(f"exact formula remained in body: {forbidden}")
for required in ["L_{OA}", "L_{AC}", "L_{\\min}"]:
    if required not in app_b:
        raise RuntimeError(f"admissible exact formula missing from Appendix B: {required}")
for required in ["F_0", "\\Delta_R", "d_i^C"]:
    if required not in app_d:
        raise RuntimeError(f"signed-center exact formula missing from Appendix D: {required}")
for required in [
    "L_{\\partial H}(T_i)\\le2/\\sqrt3",
    "L_{\\partial H}(T_i)<1/2",
    "L_{\\partial H}(T_i)\\le1",
    "L_{\\partial H}(T_i)<1",
]:
    if required not in strat1:
        raise RuntimeError(f"unified trace entry missing: {required}")
for required in [
    "g_{c_0,J_0^C}^{\\vee}",
    "\\widehat g_{c_5,J_5^C}^{\\vee}",
    "[\\mathrm I\\mid\\mathrm I\\mid\\mathrm I\\mid",
    "def:body-six-slot-chain",
]:
    if required not in strat2:
        raise RuntimeError(f"six-slot table datum missing: {required}")
if "## 10. Full six-V-triangle branch chain" not in canon:
    raise RuntimeError("canonical six-slot proof-package statement missing")

print("SOURCE_PATCH_OK")
