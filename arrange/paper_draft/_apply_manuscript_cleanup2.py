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


# 1. Replace the old all-Vd0 appendix application by the same gap-rank kernel
# used in the proof packages and reader section.
exact = ROOT / "arrange/paper_draft/04_strategy2_exact_demand.tex"
all_vd0 = r"""\begin{proposition}[All-Vd0 boundary loss]
\label{prop:nplus-zero-all-vd0}
Assume that $T_C$ is CE1 or CE2, every vertex role is Vd0, and
\[
 A_i+B_i\le1\qquad(0\le i\le5).
\]
Then the seven roles do not cover $H$.
\end{proposition}

\begin{proof}
Let $g$ be the number of positive center traces containing an active V-gap.
Then $g\in\{0,1,2\}$, with $g\le1$ in CE1.

If $g=0$, the six original open vertex traces cover the connected circle
$\partial H$.  Each has length at most one, and two nonempty members of a
finite relatively open cover must overlap in positive length.  Hence
\[
 6=\Haus(\partial H)
 <\sum_{i=0}^5\Haus(U_i\cap\partial H)
 \le\sum_{i=0}^5(A_i+B_i)\le6,
\]
a contradiction.

Suppose $g=1$ and reflect so that the active trace is
\[
 I_R=\left[\frac{k}{R},W+\delta\right].
\]
Put
\[
 s=\frac{k}{R},\qquad q=R-\delta,
 \qquad \omega=W+\delta-\frac{k}{R}.
\]
Then $s+q+\omega=1$.  Gap containment gives $B_0\ge s$ and $A_1\ge q$.
The companion edge has no active gap, so $A_0+B_5\ge1$.  Since row $T_0$ is
nonsupercritical, $A_0+B_0\le1$, and therefore $B_5\ge B_0\ge s$.  The exact
radial demands at the endpoint rows are
\[
 c_1=1-\frac{\delta}{R},
 \qquad
 c_5=1-\frac{\alpha}{W}.
\]
Lemma~\ref{lem:one-side-capped-loss} gives
\[
 F_{c_5}(s)+F_{c_1}(q)<1.
\]
Thus the two actual endpoint outputs satisfy $B_1+B_5<1$.
Lemma~\ref{lem:reader-boundary-path}, applied to $T_2,T_3,T_4$, forces their
total boundary contribution above three, contrary to their three unit caps.

Finally, $g=2$ is CE2-only and is exactly
Proposition~\ref{prop:reader-common-two-gap}.  These three ranks are exhaustive.
\end{proof}"""
replace_between(
    exact,
    r"\begin{proposition}[All-Vd0 boundary loss]",
    r"We next treat the additional T3-like rows in the $N_+=0$ branch.",
    all_vd0,
)

# 2. Use the signed variables directly in the center skeleton cap.
length_file = ROOT / "arrange/paper_draft/03_strategy1_length.tex"
center_cap = r"""\begin{lemma}[Center skeleton cap]
\label{lem:center-skeleton-cap}
If $T_C$ is a CE1 or CE2 center role and contains exactly one radial
midpoint, then
\[
 L_S(T_C)<\frac32.
\]
\end{lemma}

\begin{proof}
Normalize the unique midpoint as $M_0$ and the positive boundary trace to
$e_{0,1}$.  Use the signed variables of
Proposition~\ref{prop:signed-center-normal-form}; in particular
\[
 W=1-R,\qquad E=\sqrt{1-RW},\qquad
 \eta=1-E,\qquad P=E(1-E).
\]
The positive trace condition is
\begin{equation}
 \alpha+W\delta<P.
 \label{eq:center-skeleton-domain}
\end{equation}
The two possible boundary contributions are
\[
 \ell_{01}=W+\delta-\frac{\eta+\alpha+\delta}{R},
 \qquad
 \ell_{50}=\frac{[P-(R\alpha+\delta)]_+}{W}.
\]
The six radial contributions are bounded by
\[
\begin{array}{c|cccccc}
 i&0&1&2&3&4&5\\ \hline
 \mathcal H^1(T_C\cap r_i)&
 E-\alpha-\delta&\delta/R&\delta&
 \min\{\alpha/R,\delta/W\}&\alpha&\alpha/W.
\end{array}
\]
Adding gives
\[
 L_S(T_C)\le K_R+\mathcal E(\alpha,\delta),
\]
where
\[
 K_R=W+E-\frac\eta R
\]
and
\[
 \mathcal E(\alpha,\delta)
 =-\frac\alpha R+\frac\alpha W+\delta
 +\min\left\{\frac\alpha R,\frac\delta W\right\}
 +\frac{[P-(R\alpha+\delta)]_+}{W}.
\]
Splitting only according to the minimum and the positive part gives
\begin{equation}
 \mathcal E(\alpha,\delta)\le\frac PW.
 \label{eq:center-skeleton-E-bound}
\end{equation}
For example, if $\alpha/R\le\delta/W$, the expression without the positive
part is $\alpha/W+\delta$; when the positive part is active, its excess over
$P/W$ is $\alpha-R\delta/W\le0$.  The reflected order gives excess
$\delta-W\alpha/R\le0$.  If the positive part vanishes,
\eqref{eq:center-skeleton-domain} gives the same bound strictly.

Put $A=1+R-R^2$.  Then
\[
 \frac32-K_R-\frac PW
 =\frac{1+A-2EA}{2RW}.
\]
Both sides of $1+A>2EA$ are positive, and
\[
 (1+A)^2-4A^2E^2
 =R^2W^2(5+4R-4R^2)>0.
\]
Thus $K_R+P/W<3/2$.
\end{proof}"""
replace_between(
    length_file,
    r"\begin{lemma}[Center skeleton cap]",
    r"\begin{lemma}[Positive-support skeleton cap]",
    center_cap,
)

# 3. Strategy 4 uses the universal gauge and a distinct rotation symbol.
strategy4 = ROOT / "arrange/paper_draft/06_strategy4_reader.tex"
replace_between(
    strategy4,
    "For a compact set $K$, let",
    "For a disk $\\mathbb D(X,r)$ define its level-$h$ cap",
    r"""Use the enclosure gauge $\Lambda$ from
Proposition~\ref{prop:universal-enclosure-gauge}, and let $\mathsf R$ denote
rotation through $2\pi/3$.""",
)
for old, new in [
    (r"S=K+RK+R^2K.", r"S=K+\mathsf R K+\mathsf R^2K."),
    (r"W=C+RA.", r"W=C+\mathsf R A."),
    (r"A,\ B,\ C,\ W,\ RA", r"A,\ B,\ C,\ W,\ \mathsf R A"),
    (r"I(W,\eta)&\leftrightarrow I(RA,2\eta)", r"I(W,\eta)&\leftrightarrow I(\mathsf R A,2\eta)"),
    ("Their $R$-orbits cover the", "Their $\\mathsf R$-orbits cover the"),
    (r"h_S(n)=\sum_{j=0}^2h_K(R^jn).", r"h_S(n)=\sum_{j=0}^2h_K(\mathsf R^jn)."),
    (r"Equation~\eqref{eq:reader-lambda-support} now gives", r"Proposition~\ref{prop:universal-enclosure-gauge} now gives"),
    (r"while $C+RA$ and one disk copy give", r"while $C+\mathsf R A$ and one disk copy give"),
    (r"the rays $A,B,C,W,RA$ occur", r"the rays $A,B,C,W,\mathsf R A$ occur"),
]:
    replace_exact(strategy4, old, new)

# 4. Give area loss notation disjoint from the propagation maps G_c.
area = ROOT / "arrange/paper_draft/05_strategy3_area.tex"
text = area.read_text(encoding="utf-8")
for old, new in [
    (r"G_{\mathrm{II}}", r"\mathcal L_{\mathrm{II}}"),
    (r"G_{\mathrm I}", r"\mathcal L_{\mathrm I}"),
    (r"G_0", r"\mathcal L_0"),
    (r"G(\widehat T)", r"\mathcal L(\widehat T)"),
    (r"G(z,A)", r"\mathcal L(z,A)"),
    (r"G(z,L)", r"\mathcal L(z,L)"),
    (r"G(a,b)", r"\mathcal L(a,b)"),
    (r"G(T)", r"\mathcal L(T)"),
]:
    text = text.replace(old, new)
for forbidden in ["G(T)", "G(a,b)", "G_{\\mathrm I}", "G_{\\mathrm{II}}", "G_0"]:
    if forbidden in text:
        raise RuntimeError(f"area notation replacement incomplete: {forbidden}")
area.write_text(text, encoding="utf-8")

# 5. Introduction: identify the three certificate classes and record the
# all-Vd0 gap-rank kernel without removing the explanatory figures.
intro = ROOT / "arrange/paper_draft/01_introduction.tex"
replace_exact(
    intro,
    "exhaustive routing table, and previews the four mechanisms that close its\nrows.",
    "exhaustive routing table, and previews the three certificate types, retained\nas four named strategies, that close its rows.",
)
replace_exact(
    intro,
    r"\subsection{The four strategies}",
    r"\subsection{Three certificate types and four named strategies}",
)
insert_after = "\\label{tab:routing}\n\\end{table}\n"
addition = r"""

Within the two all-$\Vdzero$ CE1/CE2 rows, let $g$ be the number of center
traces containing active V-gaps.  The proof uses one $2\times3$ kernel:
\[
\begin{array}{c|ccc}
 &g=0&g=1&g=2\\ \hline
N_+=0&\text{open-trace budget}&\text{one-side loss}&\text{paired loss}\\
N_+=1&\text{nine-point support}&\text{five-row transfer}&\text{paired loss}.
\end{array}
\]
The last column is CE2-only.  Thus the same paired endpoint theorem closes
both two-gap cells.

The four named strategies belong to three mathematical certificate classes.
Strategies~1 and~3 are additive measure deficits, Strategy~2 is an isotone
transfer certificate, and Strategy~4 is a convex support certificate.  The
names are retained because they give the clearest geometric route through the
routing table."""
replace_exact(intro, insert_after, insert_after + addition)
replace_exact(
    intro,
    "Section~\\ref{sec:strategy2-reader} gives the common actual-row\n"
    "propagation mechanism; Appendices~\\ref{sec:exact-local-demand-calculus}--%\n"
    "\\ref{sec:t3-vd-demand-branches} retain the exact piecewise map and the\n"
    "branch-specific scalar certificates.",
    "Section~\\ref{sec:universal-calculus} gives the interval residuals and\n"
    "actual-row transfer; Section~\\ref{sec:strategy2-reader} applies them to the\n"
    "gap-rank kernel.  Appendix~\\ref{sec:exact-local-demand-calculus} retains the\n"
    "exact piecewise map and branch-specific scalar certificates.",
)
replace_exact(
    intro,
    "Their convex hull cannot fit in an open unit equilateral triangle: an exact\n"
    "caliper argument gives enclosing side at least one, whereas compact\n"
    "containment in $U_C$ would give side strictly below one.",
    "Their convex hull cannot fit in an open unit equilateral triangle: the same\n"
    "enclosure gauge $\\Lambda$ used for local demand geometry gives side at\n"
    "least one, whereas compact containment in $U_C$ would give side strictly\n"
    "below one.",
)

# 6. The historical half-edge paper source is no longer input by any active
# manuscript file.  Its theorem remains available in the proof corpus.
half_edge = ROOT / "arrange/paper_draft/04a_strategy2_half_edge_envelope.tex"
if not half_edge.exists():
    raise RuntimeError(f"missing expected historical paper source: {half_edge}")
half_edge.unlink()

print("second manuscript cleanup applied successfully")
