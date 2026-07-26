from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def replace_exact(path: Path, old: str, new: str, *, count: int = 1) -> None:
    text = path.read_text(encoding="utf-8")
    actual = text.count(old)
    if actual != count:
        raise RuntimeError(f"{path}: expected {count} copies, found {actual}: {old!r}")
    path.write_text(text.replace(old, new), encoding="utf-8")


# Strategy 4: use one rotation symbol throughout the reader cap chain.
strategy4 = ROOT / "arrange/paper_draft/06_strategy4_reader.tex"
replace_exact(strategy4, "the full $R$-orbits of", "the full $\\mathsf R$-orbits of")
replace_exact(strategy4, "sector from the ray of $A$ to the ray of $RA$.",
              "sector from the ray of $A$ to the ray of $\\mathsf R A$.")

# The all-Vd0 trace width must not reuse the universal radical symbol omega.
for relative in [
    "arrange/paper_draft/04_strategy2_exact_demand.tex",
    "proof/4XXX_CE1CE2/40XX_Nplus0/401X_all_Vd0_boundary_loss/4013_boundary_loss_index.md",
]:
    path = ROOT / relative
    replace_exact(path, r"\qquad \omega=W+\delta-\frac{k}{R}.",
                  r"\qquad w_0=W+\delta-\frac{k}{R}.")
    replace_exact(path, r"s+q+\omega=1", r"s+q+w_0=1")

# Restore two one-line justifications omitted when the Vd appendix was
# condensed, and make the nonadjacent standing inequalities explicit.
short_vd = ROOT / "arrange/paper_draft/04c_short_Vd_placements.tex"
replace_exact(
    short_vd,
    "One-sided support forces $t\\ge1$: otherwise the raw $r_5$ interval has positive\nlength.",
    "One-sided support forces $t\\ge1$.  Indeed, if $t<1$, then\n"
    "\\[\n"
    " d-a-tb-t\\ge1-\\frac t2>\\frac1{t+1}>\\frac{1-a}{t+1},\n"
    "\\]\n"
    "so the raw $r_5$ interval has positive length, contrary to the Vd1 type.",
)
replace_exact(
    short_vd,
    "\\[\n"
    " 4E(1+E)^2J'(R)\n"
    " =2E(1+E)(1+2E)-W(2R-1)>0.\n"
    "\\]\n"
    "Since $J(3/8)=1/24$, the bound $\\delta<1/24$ forces $R<3/8$.",
    "\\[\n"
    " 4E(1+E)^2J'(R)\n"
    " =2E(1+E)(1+2E)-W(2R-1).\n"
    "\\]\n"
    "If $R\\le1/2$, the second term is nonnegative after subtraction.  If\n"
    "$R\\ge1/2$, then $W(2R-1)\\le1/8$, while the first term is larger\n"
    "than $1/8$.  Thus $J'(R)>0$.  Since $J(3/8)=1/24$, the bound\n"
    "$\\delta<1/24$ forces $R<3/8$.",
)
replace_exact(
    short_vd,
    "Lemma~\\ref{lem:signed-endpoints-dominate-slack} gives\n"
    "\\[\n"
    " T<\\frac12\\min\\{x,y\\}.\n"
    "\\]\n"
    "Let\n",
    "Lemma~\\ref{lem:signed-endpoints-dominate-slack} gives\n"
    "\\[\n"
    " T<\\frac12\\min\\{x,y\\}.\n"
    "\\]\n"
    "Let $(a_0,b_0)$ be the reaches of the unique supercritical row.  Then\n"
    "\\[\n"
    " a_0+b_0>1,\\qquad a_0^2+a_0b_0+b_0^2\\le1.\n"
    "\\]\n"
    "Let\n",
)

# The same stronger margin should be explicit in the paper-generation guide.
guide = ROOT / "arrange/ams_paper_generation_guide.md"
replace_exact(
    guide,
    "|-- 04a_signed_center_calculus.tex\n"
    "|-- 03_strategy1_length.tex",
    "|-- 04a_signed_center_calculus.tex\n"
    "|-- 02a_universal_calculus.tex\n"
    "|-- 03_strategy1_length.tex",
)
replace_exact(guide, "|-- 04a_strategy2_half_edge_envelope.tex\n", "")
replace_exact(
    guide,
    "- `04a_signed_center_calculus.tex` proves the common signed CE1/CE2 model and\n"
    "  defines the local propagation interface in the body.\n"
    "- `03_strategy1_length.tex` contains the complete length arguments.",
    "- `04a_signed_center_calculus.tex` proves the common signed CE1/CE2 model and\n"
    "  defines the local propagation interface in the body.\n"
    "- `02a_universal_calculus.tex` proves the enclosure gauge, universal radical,\n"
    "  interval residuals, boundary-path budget, selected-$T_+$ curve, and\n"
    "  threshold routing once for all later strategies.\n"
    "- `03_strategy1_length.tex` contains the complete length arguments.",
)
replace_exact(
    guide,
    "- `04_strategy2_reader.tex` contains the universal selected-$T_+$ curve,\n"
    "  threshold routing, shortened CE1 one-gap proof, CE2 routing, and\n"
    "  reader-facing branch assembly.",
    "- `04_strategy2_reader.tex` contains the all-Vd0 gap-rank kernel, one common\n"
    "  CE2 two-gap application, the two sign-dependent one-gap clauses, and\n"
    "  reader-facing branch assembly.",
)
replace_exact(
    guide,
    "After `\\appendix`, input:\n\n"
    "- `04_strategy2_exact_demand.tex`: the proof-complete exact admissible-set",
    "After `\\appendix`, input:\n\n"
    "- `04c_short_Vd_placements.tex`: the quarter radial envelope, rational\n"
    "  T3-like and Vd1 profiles, common adjacent rescuer, and shortened Vd\n"
    "  placements;\n"
    "- `04_strategy2_exact_demand.tex`: the proof-complete exact admissible-set",
)
replace_exact(
    guide,
    "\\input{04a_signed_center_calculus}\n"
    "\\input{03_strategy1_length}",
    "\\input{04a_signed_center_calculus}\n"
    "\\input{02a_universal_calculus}\n"
    "\\input{03_strategy1_length}",
)
replace_exact(
    guide,
    "Do not input `04a_strategy2_half_edge_envelope.tex`,\n"
    "`appendix_certificates.tex`, or\n"
    "`appendix_exact_mixed_overlap.tex` directly from `main.tex`; their owning\n"
    "sources control their placement.",
    "Do not input `appendix_certificates.tex` or\n"
    "`appendix_exact_mixed_overlap.tex` directly from `main.tex`; their owning\n"
    "sources control their placement.  The historical half-edge $1/3$ envelope\n"
    "has no standalone manuscript source and is not an active dependency.",
)
replace_exact(
    guide,
    "### 5.2. Universal selected-$T_+$ curve",
    "### 5.2. Interval residuals and boundary paths\n\n"
    "Use $\\mathcal R_J(p)$ for the far-side demand after an initial trace and\n"
    "a center interval.  The generalized transfer is\n"
    "$\\mathcal G_{c,J}=\\mathcal R_J\\mathbin{\\circ}F_c$, and\n"
    "$\\mathcal G_{c,\\varnothing}=G_c$.  Use the boundary-path lemma instead of\n"
    "repeating three-row or four-row terminal sums.\n\n"
    "The all-Vd0 CE1/CE2 proof is organized by $N_+\\in\\{0,1\\}$ and the\n"
    "active-gap rank $g\\in\\{0,1,2\\}$; the paired endpoint theorem has one\n"
    "common geometric application in the two $g=2$ cells.\n\n"
    "### 5.3. Universal selected-$T_+$ curve",
)
replace_exact(guide, "### 5.3. Threshold routing", "### 5.4. Threshold routing")
replace_exact(guide, "### 5.4. CE1 one-gap proof", "### 5.5. CE1 one-gap proof")
replace_exact(guide, "### 5.5. The $407X$ package", "### 5.6. The $407X$ package")
replace_exact(guide, "### 5.6. The `4144` branch", "### 5.7. The `4144` branch")
replace_exact(
    guide,
    "The active shortened `4144` proof uses the common signed small-slack bounds\n"
    "and the exact adjacent-placement lemma.  The half-edge envelope remains\n"
    "available only on its stated domain and is not a substitute outside that\n"
    "domain.",
    "The active `4144` proof uses interval residuals, the common small-slack\n"
    "bounds, the stronger margin $\\delta<H/4$, and the global quarter envelope\n"
    "$c_{\\max}(p,h)\\le1-h/4$.  The historical half-edge $1/3$ envelope is not\n"
    "an active manuscript dependency.",
)
replace_exact(
    guide,
    "The body defines the support functional\n\n"
    "$$\n"
    "\\Lambda(K)=\n"
    "\\frac{1}{\\sqrt3/2}\n"
    "\\min_{\\lVert n\\rVert=1}\n"
    "\\sum_{j=0}^2h_K(R^jn)\n"
    "$$\n\n"
    "and the disk caps",
    "The universal calculus section defines the enclosure gauge $\\Lambda$ once.\n"
    "Strategy 4 reuses it and defines only the disk caps",
)
replace_exact(
    guide,
    "- `2016` and `2017` are active Strategy 2 dependencies;\n"
    "- `4106` uses the shortened $X>1/2$ proof;\n"
    "- `407a` and `407c` use the universal selected-$T_+$ curve;\n"
    "- `4144` is unchanged;",
    "- `2019`, `201a`, `201b`, and `201c` are active universal-calculus\n"
    "  dependencies;\n"
    "- `2016` and `2017` remain the authoritative selected-$T_+$ and threshold\n"
    "  sources;\n"
    "- `4106` uses the shortened $X>1/2$ proof;\n"
    "- `407a` and `407c` write $\\nu=\\gamma_5$ directly and use the universal\n"
    "  selected-$T_+$ curve;\n"
    "- `4144` uses the quarter envelope;",
)

# Add the Vd radial-margin dependency to the two global proof indexes.
proof_tree = ROOT / "proof/0XXX_main/0001_proof_tree_index.md"
replace_exact(
    proof_tree,
    "    - `201b`: proved the global quarter radial envelope\n"
    "      $c_{\\max}(p,h)\\le1-h/4$\n",
    "    - `201b`: proved the global quarter radial envelope\n"
    "      $c_{\\max}(p,h)\\le1-h/4$\n"
    "    - `201c`: proved the own-radial and supported-arm margins extracted\n"
    "      from the Vd1/Vd2 corner normal form\n",
)
status = ROOT / "proof/0XXX_main/0002_status_and_dependencies.md"
replace_exact(
    status,
    "| Global quarter radial envelope | [`../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md) | Proven |\n",
    "| Global quarter radial envelope | [`../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201b_quarter_radial_envelope.md) | Proven |\n"
    "| Vd1/Vd2 corner radial margins | [`../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md`](../2XXX_geometric_lemmas/20XX_V_triangle_geometry/201c_Vd_corner_radial_margins.md) | Proven |\n",
)

print("final source edits applied successfully")
