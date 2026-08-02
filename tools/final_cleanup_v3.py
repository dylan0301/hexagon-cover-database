from __future__ import annotations

import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def path(rel: str) -> Path:
    return ROOT / rel


def read(rel: str) -> str:
    return path(rel).read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    target = path(rel)
    target.parent.mkdir(parents=True, exist_ok=True)
    if text and not text.endswith("\n"):
        text += "\n"
    target.write_text(text, encoding="utf-8")


def replace_required(rel: str, old: str, new: str, *, count: int | None = None) -> None:
    text = read(rel)
    actual = text.count(old)
    if actual == 0:
        raise RuntimeError(f"{rel}: required text not found: {old!r}")
    if count is not None and actual != count:
        raise RuntimeError(f"{rel}: expected {count} copies, found {actual}: {old!r}")
    write(rel, text.replace(old, new))


def replace_if_present(rel: str, old: str, new: str) -> int:
    text = read(rel)
    actual = text.count(old)
    if actual:
        write(rel, text.replace(old, new))
    return actual


# Run the authoritative architecture/redundancy cleanup first.
runpy.run_path(str(path("tools/final_cleanup_20260802.py")), run_name="__main__")

# Complete the u/nu and actual/selected normalization found in the second audit.
replace_required(
    "proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md",
    r"\nu=1-",
    r"u=1-",
    count=1,
)
replace_required(
    "proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md",
    r"\nu=\frac{d-a-tb-1}{t}",
    r"u=\frac{d-a-tb-1}{t}",
    count=1,
)
replace_required(
    "proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md",
    r"\nu_2<1-H",
    r"u_{1\to2}<1-H",
    count=1,
)
replace_required(
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31054_four_cap_enclosure_reduction.md",
    r"\nu_A<u_B<\frac12",
    r"u_A<u_B<\frac12",
    count=1,
)
replace_required(
    "proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md",
    r"a_i+b_i\le1,\qquad i=2,3,4,5.",
    r"A_i+B_i\le1,\qquad i=2,3,4,5.",
    count=1,
)

for rel in [
    "proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md",
    "proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2109_signed_CE1_CE2_center_normal_form.md",
]:
    replace_if_present(rel, r"\nuS", r"\nu S")

replace_if_present(
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4075_Tminus_low_lower_branch_obligations.md",
    r"\nu=\frac{\delta}{1-\lambda}",
    r"u=\frac{\delta}{1-\lambda}",
)

# Apply the same exact transcription repairs to compiled TeX sources.
tex_replacements = [
    (r"\nu_{\rm adj}", r"u_{\rm adj}"),
    (r"\nu=1-", r"u=1-"),
    (r"\nu=\frac{d-a-tb-1}{t}", r"u=\frac{d-a-tb-1}{t}"),
    (r"\nu_2<1-H", r"u_{1\to2}<1-H"),
    (r"\nu_A<u_B<\frac12", r"u_A<u_B<\frac12"),
    (r"\nuS", r"\nu S"),
    (r"a_i+b_i\le1,\qquad i=2,3,4,5.", r"A_i+B_i\le1,\qquad i=2,3,4,5."),
]
for tex in (ROOT / "arrange/paper_draft").rglob("*.tex"):
    text = tex.read_text(encoding="utf-8")
    original = text
    for old, new in tex_replacements:
        text = text.replace(old, new)
    if text != original:
        tex.write_text(text, encoding="utf-8")

# Expand the status manifest to the transitive active sources most relevant to
# the repaired branches and the exact Strategy 4 package.
active_rel = "proof/ACTIVE_DEPENDENCIES.txt"
active_text = read(active_rel).rstrip() + "\n"
extra_active = [
    "proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31050_self_contained_direct_Vd0_nine_point_index.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31051_direct_radial_forcing.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31052_fixed_line_circle_signs.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31053_direct_asymmetric_witness_forcing.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31054_four_cap_enclosure_reduction.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31055_rational_radial_envelopes_and_mixed_reduction.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31056_global_analytic_mixed_positivity.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31057_terminal_nine_point_enclosure.md|Proven",
    "proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31059_CE0_Nplus1_all_Vd0_completion.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4070_CE1CE2_Nplus0_T3_like_no_Vd1Vd2_index.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4071_CE1CE2_Nplus0_T3_like_forces_V0_T3_like.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4072_support_isolation_after_T0_T3_like.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4073_boundary_loss_framework.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4074_L_Full_branch.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4075_Tminus_low_lower_branch_obligations.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4078_left_L_family_completion.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/4079_first_Full_branch.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407a_left_Thigh_branch_completion.md|Proven",
    "proof/4XXX_CE1CE2/40XX_Nplus0/407X_T3_like_no_Vd1Vd2/407c_rigor_completion_details.md|Proven",
    "proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4102_CE2_two_gap_completion.md|Proven",
    "proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4105_CE1_CE2_one_gap_five_V_triangle_interface.md|Proven",
    "proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4106_CE1_one_gap_five_map_completion.md|Proven",
    "proof/4XXX_CE1CE2/41XX_Nplus1/410X_all_Vd0/4107_CE2_one_gap_five_map_completion.md|Proven",
    "proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md|Proven",
    "proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md|Proven",
]
for entry in extra_active:
    if entry.split("|", 1)[0] + "|" not in active_text:
        active_text += entry + "\n"
write(active_rel, active_text)

# Add exact recurrence checks to the persistent linter after the architectural
# cleanup has rewritten it.
lint_rel = "tools/proof_lint.py"
lint = read(lint_rel)
marker = "\nif ERRORS:\n"
if marker not in lint:
    raise RuntimeError("proof_lint.py: terminal error block not found")
additional_lint = r'''
additional_bad = {
    r"\nu=\frac{d-a-tb-1}{t}": "local radial endpoint must use Latin u",
    r"\nu=1-\frac{R_{\rm loc}}D+a": "T3-like local radial endpoint must use Latin u",
    r"\nu_2<1-H": "4144 local endpoint must be u_{1\\to2}",
    r"\nu_A<u_B": "31054 local coordinate must be u_A",
    r"\nuS": "signed CE2 endpoint product is missing a separator",
    r"\nu=\frac{\delta}{1-\lambda}": "4075 local endpoint must use Latin u",
    r"a_i+b_i\le1,\qquad i=2,3,4,5.": "4131 nonsupercritical conclusion must use actual reaches",
}
for token, description in additional_bad.items():
    if token in all_active_text:
        fail(description)

required_4131 = ROOT / "proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md"
text_4131 = required_4131.read_text(encoding="utf-8")
if r"A_i+B_i\le1,\qquad i=2,3,4,5." not in text_4131:
    fail("4131 is missing the actual-reach nonsupercritical conclusion")
'''
lint = lint.replace(marker, "\n" + additional_lint + marker, 1)
write(lint_rel, lint)

# Final exact assertions make the cleanup fail before any status is retained
# if a requested repair did not land.
assert r"\nu_{\rm adj}" not in read("proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4147_CE2_Nplus1_Vd1_supercritical_pair_axis_replacement.md")
assert r"\nu=1-" not in read("proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4132_CE1_CE2_exactly_one_T3_like_boundary_obstruction.md")
assert r"\nu=\frac{d-a-tb-1}{t}" not in read("proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4143_CE2_Nplus1_T0_Vd1_M1_T1_supercritical_obstruction.md")
assert r"\nu_2<1-H" not in read("proof/4XXX_CE1CE2/41XX_Nplus1/414X_CE2_exactly_one_Vd1_Vd2/4144_CE2_Nplus1_T0_supercritical_T1_Vd1_Vd2_adjacent_obstruction.md")
assert r"\nu_A<u_B" not in read("proof/3XXX_CE0/31XX_Nplus1/310X_all_Vd0/3105X_self_contained_direct_Vd0_nine_point/31054_four_cap_enclosure_reduction.md")
assert r"\nuS" not in read("proof/2XXX_geometric_lemmas/21XX_C_triangle_geometry/2106_CE2_exact_formulas.md")
assert r"a_i+b_i\le1,\qquad i=2,3,4,5." not in read("proof/4XXX_CE1CE2/41XX_Nplus1/413X_exactly_one_T3_like/4131_midpoint_forcing_reduction.md")

print("final notation and dependency cleanup applied")
