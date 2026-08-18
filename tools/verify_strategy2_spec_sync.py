#!/usr/bin/env python3
"""Verify the complete Strategy 2 scalar statement interface.

This is a structural-semantic check, not a theorem prover. It locks the full
mathematical payload of the TeX scalar specifications and the complete Lean
statement file, then checks transparent cross-language contracts for domains,
objectives, strictness, and finite branch data. The in-memory mutation tests
guard against regressing to a name/marker-presence check.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "arrange/paper_draft"
LEAN_PATH = (
    ROOT
    / "formalization/strategy2_optimization/Strategy2Optimization/Problems.lean"
)

TEX_SPEC_FILES = (
    "04_strategy2_optimization_map.tex",
    "04_strategy2_optimization_domain.tex",
    "04_strategy2_optimization_labels.tex",
    "04_strategy2_optimization_registered.tex",
    "04_strategy2_optimization_t3.tex",
    "04_strategy2_optimization_rescuer.tex",
    "04_strategy2_optimization_vd.tex",
)
SOURCE_THEOREM_FILE = "04f_strategy2_pure_theorems.tex"

# These fingerprints cover every TeX math span, every uncommented source token
# (including the prose that binds displayed clauses into domains), and every
# noncomment token in Problems.lean. Update them only after reviewing the
# transparent contracts below and the displayed digest diff.
EXPECTED_TEX_MATH_SHA256 = {
    "04_strategy2_optimization_map.tex": "889ccfe169fa0f8f1cc248c2968260510153dbd5a1c2051ea276892e40f2c121",
    "04_strategy2_optimization_domain.tex": "414cdc5f5601930e9006ae6aa8d9a5ebab1eb349f1a8c8478cf25aca5cfc79ef",
    "04_strategy2_optimization_labels.tex": "3a17f52659e1650007499d18a09e87d946659cebdb384ee70021adbac3f01b9e",
    "04_strategy2_optimization_registered.tex": "48bc3e0897e6375d66accfecac7853c7a1f0cb459583ca29238689d4b64674cb",
    "04_strategy2_optimization_t3.tex": "63d753b8838de7de9d4a388f8388066311357451857868c68306d10c584da8b8",
    "04_strategy2_optimization_rescuer.tex": "83735e87b8c53fba737b4a9febe136a6c8e8368c93626d149b2a95eb93faa015",
    "04_strategy2_optimization_vd.tex": "a57a02cb05ed8c51bb517b95ccac641590421e8090874bde401c75c155a5e64e",
}
EXPECTED_TEX_SOURCE_SHA256 = {
    "04_strategy2_optimization_map.tex": "05939af0e8e38a4e094f9f00c99e6c717c9c617ddb84fd9acebc7b4e258f0b1f",
    "04_strategy2_optimization_domain.tex": "1f7bbe52f9bbc1c7d3f70001663b004da9ef37cf3a09b7a9d0811ac443ee83ca",
    "04_strategy2_optimization_labels.tex": "b12c19fb286c66cc429bfefa86d96edea442e4a8c145e4fe26299f2ccef1cad9",
    "04_strategy2_optimization_registered.tex": "60213129bb353cc70cf89747cfbc0dd99014e6492a4c426dc2ea681fecbd5a01",
    "04_strategy2_optimization_t3.tex": "3514e8eddfe1059c81fac909df6392a1a2371eeac6fc757a1c48ffa47b430364",
    "04_strategy2_optimization_rescuer.tex": "a555f3ecd29eca56b13bd236aaf08617d768e2f543a5bd672c5a8d7eeed2714b",
    "04_strategy2_optimization_vd.tex": "96ca4f06316a97f6f4c8573ad65538f8abcc8495a1cee51489108b4fda862fa6",
}
EXPECTED_SOURCE_THEOREM_SHA256 = {
    "thm:s2-univ-e1": "9d01ad48243a010bccdc097bb5fd111a5a52f9769331288d166dc8ee6bfc656d",
    "thm:s2-univ-e2": "ba4563a2588e3b4f9adafb60046470fdec844cf2377cebcc99626688c958f1f8",
    "thm:s2-univ-r1": "b87c327a59279d28a3ac082d25c1474362d6faa87dbc0453582de476b3d04b1a",
    "thm:s2-univ-r2": "c587fb64947b762782773ecd965ec9470c619ac536b766eb20feb4f64fdc8cf2",
    "thm:s2-source-t3": "702fc9617a8f0ca2cb41cc7e252890acf8c396f14c8249601783979e7d0278c3",
    "thm:s2-univ-sc": "5f6573c5b306600698455ba4e8f820f782d4c3d96b03108f056b4a6535aa0144",
    "thm:s2-univ-vd-adjacent": "65a073fa3f5c7604683cae2b366c36f36f2f99fb892b9a1f6eda9970f7c9d6f4",
    "thm:s2-univ-vd-nonadjacent": "37f86fdfe3a817361de7ae38874916a94e44cae84e293c27ce3c9a4a6988549c",
}
EXPECTED_LEAN_SHA256 = "d633412e01a850d81c05e05a57d87ca2b4910052bf3bea9be51f23b2ce5f2635"


@dataclass(frozen=True)
class ProblemContract:
    key: str
    problem_labels: tuple[str, ...]
    source_owner: str
    lean_theorems: tuple[str, ...]
    tex_require: tuple[str, ...]
    lean_require: tuple[str, ...]


@dataclass(frozen=True)
class DefinitionContract:
    """Exact TeX/Lean clauses for a family of scalar definitions."""

    key: str
    tex_file: str
    lean_defs: tuple[str, ...]
    tex_require: tuple[str, ...]
    lean_require: tuple[str, ...]


CONTRACTS = (
    ProblemContract(
        "S2-E1",
        ("prob:s2-one-gap-endpoint",),
        "thm:s2-univ-e1",
        ("problemS2E1",),
        (
            r"(r,a,d)\in\mathcal D_1\cup\mathcal D_2",
            r"F(c_-,x_-)+F(c_+,x_+)-1",
            r"\Psi_{\rm E1}(r,a,d)<0",
        ),
        (
            "oneGapCE1Domain s ∨ centerCE2Domain s",
            "forwardCap (1 - s.alpha / w s) (centerK s / s.r)",
            "forwardCap (1 - s.delta / s.r) (s.r - s.delta) - 1",
            "endpointSlackE1 s < 0",
        ),
    ),
    ProblemContract(
        "S2-E2",
        ("prob:s2-two-gap-endpoint",),
        "thm:s2-univ-e2",
        ("problemS2E2",),
        (
            r"(r,a,d)\in\mathcal D_2",
            r"F(c_-,x_-)+F(c_+,x_+)-1",
            r"\Psi_{\rm E2}(r,a,d)<0",
        ),
        (
            "centerCE2Domain s",
            "forwardCap ((w s - s.alpha) / w s) (w s - s.alpha)",
            "forwardCap ((s.r - s.delta) / s.r) (s.r - s.delta) - 1",
            "endpointSlackE2 s < 0",
        ),
    ),
    ProblemContract(
        "S2-R1",
        ("prob:s2-ce1-five-chain",),
        "thm:s2-univ-r1",
        ("problemS2R1",),
        (
            r"(r,a,d)\in\mathcal D_1",
            r"Y_1=T(1-a,Y_0)",
            r"Y_2=T(1-m,Y_1)",
            r"Y_3=T(1-d,Y_2)",
            r"\Psi_{\rm R1}(r,a,d)=w+d-Y_3",
            r"\Psi_{\rm R1}(r,a,d)<0",
        ),
        (
            "oneGapCE1Domain s",
            "propagate (1 - s.alpha) (seedReach s)",
            "propagate (1 - middleRadialRequirement s) (afterFirstPropagation s)",
            "propagate (1 - s.delta) (afterMiddlePropagation s)",
            "returnSlack s < 0",
        ),
    ),
    ProblemContract(
        "S2-R2",
        ("prob:s2-ce2-five-chain",),
        "thm:s2-univ-r2",
        ("problemS2R2",),
        (
            r"(r,a,d)\in\mathcal D_2",
            r"\Psi_{\rm R2}(r,a,d)=w+d-Y_3",
            r"\Psi_{\rm R2}(r,a,d)<0",
            r"e(a)<Y_0\quad\text{or}\quad e(d)<Y_0",
        ),
        ("centerCE2Domain s", "returnSlack s < 0"),
    ),
    ProblemContract(
        "S2-T3",
        ("prob:s2-t3-compact-projection",),
        "thm:s2-source-t3",
        ("problemS2T3",),
        (
            r"\widehat a_1",
            r"q,&b_+<s_R",
            r"r-d,&s_R\le b_+<t_R",
            r"q,&t_R\le b_+",
            r"1-t_L,&(r,a,d)\in\mathcal D_{\rm C2},\ s_L\le\beta<t_L",
            r"c_\star,&1-u_\star\le\gamma_1\le1-c_\star",
            r"1-\gamma_1,&\text{otherwise}",
            r"0<b_+<1",
            r"0<q<\frac12",
            r"0<c_\star<u_\star<1",
            r"\frac12<\widehat c_1<1",
            r"\frac12<\widehat c_5<1",
            r"F(\widehat c_5,\widehat a_5)+F(\widehat c_1,\widehat a_1)-1<0",
        ),
        (
            "centerCE1Domain x.center ∨ centerCE2Domain x.center",
            "0 < t3ForwardEnd x ∧ t3ForwardEnd x < 1",
            "0 < t3Q x ∧ t3Q x < 1 / 2",
            "1 / 2 < t3RadialReq1 x ∧ t3RadialReq1 x < 1",
            "1 / 2 < t3RadialReq5 x ∧ t3RadialReq5 x < 1",
            "forwardCap (t3RadialReq5 x) (t3BackwardReq5 x)",
            "forwardCap (t3RadialReq1 x) (t3BackwardReq1 x) - 1",
            "t3EndpointSlack x < 0",
        ),
    ),
    ProblemContract(
        "S2-SC",
        ("prob:s2-rescuer",),
        "thm:s2-univ-sc",
        ("problemS2SCT", "problemS2SCV"),
        (
            r"0\le\theta\le2-\sqrt3",
            r"x_L(\theta)\le x\le\frac12-\theta",
            r"t\ge1",
            r"\Psi_{\rm SC}(a,c,u)\le0",
            r"\Omega_{\rm SC}^{T}",
            r"\Omega_{\rm SC}^{V}",
        ),
        (
            "0 ≤ v.theta ∧ v.theta ≤ 2 - Real.sqrt 3",
            "t3SupportLowerBound v ≤ v.x ∧ v.x ≤ 1 / 2 - v.theta",
            "1 ≤ v.t",
            "adjacentSupportSlack (t3SupportBackward v) (t3SupportRadial v) (t3SupportEndpoint v) ≤ 0",
            "adjacentSupportSlack v.a (vd1SupportRadial v) (vd1SupportEndpoint v) ≤ 0",
        ),
    ),
    ProblemContract(
        "S2-VD-adjacent",
        ("prob:s2-vd-adjacent",),
        "thm:s2-univ-vd-adjacent",
        ("problemS2VDAdjacentSupport", "problemS2VDAdjacentNoSupport"),
        (
            r"0\le\lambda_+<u_+\le1",
            r"u_+\le\lambda_+",
            r"\Psi_{\rm VD}^{\rm adj,+}<0",
            r"\Psi_{\rm VD}^{\rm adj,0}<0",
        ),
        (
            "0 ≤ vdAdjSupportStart v ∧ vdAdjSupportStart v < vdAdjSupportEnd v ∧ vdAdjSupportEnd v ≤ 1",
            "vdAdjSupportEnd v ≤ vdAdjSupportStart v",
            "vdAdjSupportSlack v < 0",
            "vdAdjNoSupportSlack v < 0",
        ),
    ),
    ProblemContract(
        "S2-VD-nonadjacent",
        ("prob:s2-vd-nonadjacent",),
        "thm:s2-univ-vd-nonadjacent",
        ("problemS2VDNonadjacent",),
        (
            r"j\in\{2,4\},\qquad \mu\in\{0,1\}",
            r"\Omega_{\rm VD}^{3,\mu,\nu}",
            r"(\mu,\nu\in\{0,1\})",
            r"\max\{\sigma-A_R,\ \sigma-A_L,\ d_j-m,\ C_v-1+m\}",
            r"\Psi_{\rm VD}^{\rm non}<0",
        ),
        (
            "inductive VdPosition | pos2 | pos3 | pos4",
            "| .pos2 => v.center.delta",
            "| .pos3 => min (v.center.alpha / v.center.r) (v.center.delta / w v.center)",
            "| .pos4 => v.center.alpha",
            "let m := min (vdNonRightRequirement v) (vdNonLeftRequirement v)",
            "vdNonadjacentSlack v < 0",
        ),
    ),
)


# Each contract records complete defining formulas, not merely names.  The
# coverage check below requires every `def` in Problems.lean to occur in
# exactly this reviewed interface inventory.
DEFINITION_CONTRACTS = (
    DefinitionContract(
        "signed center primitives and domains",
        "04_strategy2_optimization_domain.tex",
        (
            "w",
            "centerRadical",
            "centerEta",
            "centerP",
            "centerK",
            "rightSurplus",
            "leftSurplus",
            "signedCenterDomain",
            "centerCE1Domain",
            "centerCE2Domain",
            "oneGapCE1Domain",
        ),
        (
            r"""
            w=1-r,\qquad
            e=\sqrt{1-rw},\qquad
            \eta=1-e,\qquad
            p=e(1-e),\qquad
            k=\eta+a+d,
            """,
            r"""
            \Delta_R=p-a-wd,
            \qquad
            \Delta_L=p-ra-d.
            """,
            r"""
            \mathcal D_{\rm sgn}
            =
            \left\{
            (r,a,d):
            0<r<1,\ a>0,\ d>0,\ \Delta_R>0
            \right\}.
            """,
            r"""
            \mathcal D_{\rm C1}
            =
            \left\{(r,a,d)\in\mathcal D_{\rm sgn}:\Delta_L\le0\right\},
            """,
            r"""
            \mathcal D_{\rm C2}
            =
            \left\{(r,a,d)\in\mathcal D_{\rm sgn}:\Delta_L>0\right\}.
            """,
            r"""
            \mathcal D_1
            =
            \left\{
            (r,a,d)\in\mathcal D_{\rm C1}:
            a<\frac w2,\quad d<\frac r2,\quad rd-wa>0
            \right\},
            """,
            r"\mathcal D_2:=\mathcal D_{\rm C2}.",
        ),
        (
            """
            def w (s : SignedCenterInput) : ℝ := 1 - s.r
            def centerRadical (s : SignedCenterInput) : ℝ := Real.sqrt (1 - s.r * w s)
            def centerEta (s : SignedCenterInput) : ℝ := 1 - centerRadical s
            def centerP (s : SignedCenterInput) : ℝ := centerRadical s * (1 - centerRadical s)
            def centerK (s : SignedCenterInput) : ℝ := centerEta s + s.alpha + s.delta
            def rightSurplus (s : SignedCenterInput) : ℝ := centerP s - s.alpha - w s * s.delta
            def leftSurplus (s : SignedCenterInput) : ℝ := centerP s - s.r * s.alpha - s.delta

            def signedCenterDomain (s : SignedCenterInput) : Prop :=
              0 < s.r ∧ s.r < 1 ∧ 0 < s.alpha ∧ 0 < s.delta ∧ 0 < rightSurplus s

            def centerCE1Domain (s : SignedCenterInput) : Prop :=
              signedCenterDomain s ∧ leftSurplus s ≤ 0

            def centerCE2Domain (s : SignedCenterInput) : Prop :=
              signedCenterDomain s ∧ 0 < leftSurplus s

            def oneGapCE1Domain (s : SignedCenterInput) : Prop :=
              centerCE1Domain s ∧
                s.alpha < w s / 2 ∧
                s.delta < s.r / 2 ∧
                w s * s.alpha < s.r * s.delta
            """,
        ),
    ),
    DefinitionContract(
        "high-radial map primitives and executable branches",
        "04_strategy2_optimization_map.tex",
        (
            "lowerBreakpoint",
            "upperBreakpoint",
            "qPlusTransition",
            "qMinus",
            "discrPlus",
            "qPlus",
            "forwardCapBranch",
            "forwardCapBranchValue",
            "forwardCap",
            "propagate",
        ),
        (
            r"h(c)=\frac{2c}{1+\sqrt{16c^2-3}}",
            r"Q_-(x,c)=\frac{\sqrt{x^2-cx+c^2}}{c}-x",
            r"\ell(c)=\frac c2\left(1-\sqrt{4c^2-3}\right)",
            r"r(c)=c-\ell(c)",
            r"D_+(c,x)=(2xc^2+c)^2-4(1-c^2)(1-x^2)c^2",
            r"""
            Q_+(x,c)=
            \frac{2(1-x^2)c^2}
            {2xc^2+c+\sqrt{D_+(c,x)}}
            """,
            r"""
            F(c,x)=
            \begin{cases}
            1-x,&0\le x\le1-c,\\
            Q_+(x,c),&1-c<x<h(c),\\
            h(c),&x=h(c),\\
            Q_-(x,c),&h(c)<x<c,\\
            1-x,&c\le x\le1.
            \end{cases}
            """,
            r"""
            F(c,x)=
            \begin{cases}
            1-x,&0\le x\le1-c,\\
            Q_+(x,c),&1-c<x\le \ell(c),\\
            \ell(c),&\ell(c)<x<r(c),\\
            Q_-(x,c),&r(c)\le x<c,\\
            1-x,&c\le x\le1.
            \end{cases}
            """,
            r"T(c,x):=1-F(c,x)",
        ),
        (
            """
            def lowerBreakpoint (c : ℝ) : ℝ :=
              c / 2 * (1 - Real.sqrt (4 * c^2 - 3))

            def upperBreakpoint (c : ℝ) : ℝ := c - lowerBreakpoint c

            def qPlusTransition (c : ℝ) : ℝ :=
              2 * c / (1 + Real.sqrt (16 * c^2 - 3))

            def qMinus (c x : ℝ) : ℝ :=
              Real.sqrt (x^2 - c * x + c^2) / c - x

            def discrPlus (c x : ℝ) : ℝ :=
              (2 * x * c^2 + c)^2 - 4 * (1 - c^2) * (1 - x^2) * c^2

            def qPlus (c x : ℝ) : ℝ :=
              2 * (1 - x^2) * c^2 /
                (2 * x * c^2 + c + Real.sqrt (discrPlus c x))
            """,
            """
            def forwardCapBranch (c x : ℝ) : ForwardCapBranch :=
              if c ≤ Real.sqrt 3 / 2 then
                if x ≤ 1 - c then .lin
                else if x < qPlusTransition c then .qPlus
                else if x = qPlusTransition c then .const
                else if x < c then .qMinus
                else .lin
              else
                if x ≤ 1 - c then .lin
                else if x ≤ lowerBreakpoint c then .qPlus
                else if x < upperBreakpoint c then .const
                else if x < c then .qMinus
                else .lin

            def forwardCapBranchValue (c x : ℝ) : ForwardCapBranch → ℝ
              | .lin => 1 - x
              | .const =>
                  if c ≤ Real.sqrt 3 / 2 then qPlusTransition c else lowerBreakpoint c
              | .qMinus => qMinus c x
              | .qPlus => qPlus c x

            def forwardCap (c x : ℝ) : ℝ :=
              forwardCapBranchValue c x (forwardCapBranch c x)

            def propagate (c x : ℝ) : ℝ := 1 - forwardCap c x
            """,
        ),
    ),
    DefinitionContract(
        "endpoint and return objectives",
        "04_strategy2_optimization_registered.tex",
        (
            "endpointSlackE1",
            "endpointSlackE2",
            "middleRadialRequirement",
            "seedReach",
            "afterFirstPropagation",
            "afterMiddlePropagation",
            "afterLastPropagation",
            "returnSlack",
        ),
        (
            r"""
            x_-=\frac{k}{r},
            \qquad x_+=r-d,
            \qquad c_-=1-\frac a w,
            \qquad c_+=1-\frac d r
            """,
            r"\Psi_{\rm E1}(r,a,d)=F(c_-,x_-)+F(c_+,x_+)-1",
            r"""
            x_-=w-a,
            \qquad x_+=r-d,
            \qquad c_-=\frac{x_-}{w},
            \qquad c_+=\frac{x_+}{r}
            """,
            r"\Psi_{\rm E2}(r,a,d)=F(c_-,x_-)+F(c_+,x_+)-1",
            r"X=r-d,\qquad Y_0=\frac{k}{2r},\qquad m=\min\left\{\frac ar,\frac dw\right\}",
            r"""
            Y_1=T(1-a,Y_0),\qquad
            Y_2=T(1-m,Y_1),\qquad
            Y_3=T(1-d,Y_2)
            """,
            r"\Psi_{\rm R1}(r,a,d)=w+d-Y_3",
            r"\Psi_{\rm R2}(r,a,d)=w+d-Y_3",
        ),
        (
            """
            def endpointSlackE1 (s : SignedCenterInput) : ℝ :=
              forwardCap (1 - s.alpha / w s) (centerK s / s.r) +
                forwardCap (1 - s.delta / s.r) (s.r - s.delta) - 1
            """,
            """
            def endpointSlackE2 (s : SignedCenterInput) : ℝ :=
              forwardCap ((w s - s.alpha) / w s) (w s - s.alpha) +
                forwardCap ((s.r - s.delta) / s.r) (s.r - s.delta) - 1
            """,
            """
            def middleRadialRequirement (s : SignedCenterInput) : ℝ :=
              min (s.alpha / s.r) (s.delta / w s)

            def seedReach (s : SignedCenterInput) : ℝ := centerK s / (2 * s.r)
            def afterFirstPropagation (s : SignedCenterInput) : ℝ := propagate (1 - s.alpha) (seedReach s)
            def afterMiddlePropagation (s : SignedCenterInput) : ℝ := propagate (1 - middleRadialRequirement s) (afterFirstPropagation s)
            def afterLastPropagation (s : SignedCenterInput) : ℝ := propagate (1 - s.delta) (afterMiddlePropagation s)
            def returnSlack (s : SignedCenterInput) : ℝ := w s + s.delta - afterLastPropagation s
            """,
        ),
    ),
    DefinitionContract(
        "compact T3 primitives, cells, domain, and objective",
        "04_strategy2_optimization_t3.tex",
        (
            "t3Radical",
            "t3Q",
            "t3RadialNear",
            "t3RadialFar",
            "t3ForwardEnd",
            "t3BackwardReq1",
            "t3BackwardReq5",
            "t3RadialReq1",
            "t3RadialReq5",
            "t3Domain",
            "t3EndpointSlack",
        ),
        (
            r"z=\sqrt{1-\tau+\tau^2}",
            r"b_+=z-\beta",
            r"q=1-z+\beta",
            r"c_\star=\frac q\tau",
            r"u_\star=1+\beta-\tau",
            r"s_R=\frac{k}{r}",
            r"t_R=w+d",
            r"s_L=\frac{k}{w}",
            r"t_L=r+a",
            r"""
            \widehat a_1=
            \begin{cases}
            q,&b_+<s_R,\\
            r-d,&s_R\le b_+<t_R,\\
            q,&t_R\le b_+,
            \end{cases}
            """,
            r"""
            \widehat a_5=
            \begin{cases}
            1-\beta,&(r,a,d)\in\mathcal D_{\rm C1},\\
            1-\beta,&(r,a,d)\in\mathcal D_{\rm C2},\ \beta<s_L,\\
            1-t_L,&(r,a,d)\in\mathcal D_{\rm C2},\ s_L\le\beta<t_L,\\
            1-\beta,&(r,a,d)\in\mathcal D_{\rm C2},\ t_L\le\beta.
            \end{cases}
            """,
            r"""
            \widehat c_1=
            \begin{cases}
            c_\star,&1-u_\star\le\gamma_1\le1-c_\star,\\
            1-\gamma_1,&\text{otherwise},
            \end{cases}
            \qquad
            \widehat c_5=1-\gamma_5
            """,
            r"(r,a,d)\in\mathcal D_{\rm C1}\cup\mathcal D_{\rm C2}",
            r"0<\tau<1",
            r"0<\beta<\frac{\tau z}{1+z}",
            r"0<b_+<1",
            r"0<q<\frac12",
            r"0<c_\star<u_\star<1",
            r"\frac12<\widehat c_1<1",
            r"\frac12<\widehat c_5<1",
            r"F(\widehat c_5,\widehat a_5)+F(\widehat c_1,\widehat a_1)-1<0",
        ),
        (
            """
            def t3Radical (x : T3Input) : ℝ :=
              Real.sqrt (1 - x.tau + x.tau^2)

            def t3Q (x : T3Input) : ℝ := 1 - t3Radical x + x.beta
            def t3RadialNear (x : T3Input) : ℝ := t3Q x / x.tau
            def t3RadialFar (x : T3Input) : ℝ := 1 + x.beta - x.tau
            def t3ForwardEnd (x : T3Input) : ℝ := t3Radical x - x.beta

            def t3BackwardReq1 (x : T3Input) : ℝ :=
              let sR := centerK x.center / x.center.r
              let tR := w x.center + x.center.delta
              if t3ForwardEnd x < sR then t3Q x
              else if t3ForwardEnd x < tR then x.center.r - x.center.delta
              else t3Q x

            def t3BackwardReq5 (x : T3Input) : ℝ := by
              classical
              exact
                if centerCE2Domain x.center then
                  let sL := centerK x.center / w x.center
                  let tL := x.center.r + x.center.alpha
                  if x.beta < sL then 1 - x.beta
                  else if x.beta < tL then 1 - tL
                  else 1 - x.beta
                else
                  1 - x.beta

            def t3RadialReq1 (x : T3Input) : ℝ :=
              let gamma1 := x.center.delta / x.center.r
              if 1 - t3RadialFar x ≤ gamma1 ∧ gamma1 ≤ 1 - t3RadialNear x then
                t3RadialNear x
              else
                1 - gamma1

            def t3RadialReq5 (x : T3Input) : ℝ :=
              1 - x.center.alpha / w x.center

            def t3Domain (x : T3Input) : Prop :=
              (centerCE1Domain x.center ∨ centerCE2Domain x.center) ∧
                0 < x.tau ∧ x.tau < 1 ∧
                0 < x.beta ∧
                x.beta < x.tau * t3Radical x / (1 + t3Radical x) ∧
                0 < t3ForwardEnd x ∧ t3ForwardEnd x < 1 ∧
                0 < t3Q x ∧ t3Q x < 1 / 2 ∧
                0 < t3RadialNear x ∧ t3RadialNear x < t3RadialFar x ∧ t3RadialFar x < 1 ∧
                1 / 2 < t3RadialReq1 x ∧ t3RadialReq1 x < 1 ∧
                1 / 2 < t3RadialReq5 x ∧ t3RadialReq5 x < 1

            def t3EndpointSlack (x : T3Input) : ℝ :=
              forwardCap (t3RadialReq5 x) (t3BackwardReq5 x) +
                forwardCap (t3RadialReq1 x) (t3BackwardReq1 x) - 1
            """,
        ),
    ),
    DefinitionContract(
        "adjacent-support primitives, domains, and objective",
        "04_strategy2_optimization_rescuer.tex",
        (
            "strictSupercriticalForwardSupremum",
            "adjacentSupportSlack",
            "t3SupportRatio",
            "t3SupportLowerBound",
            "t3SupportBackward",
            "t3SupportRadial",
            "t3SupportEndpoint",
            "t3AdjacentSupportDomain",
            "cornerRadical",
            "vd1SupportRadial",
            "vd1SupportEndpoint",
            "vd1AdjacentSupportDomain",
        ),
        (
            r"E_{\rm sc}(c)=\frac{c+\sqrt{c^2-8c+4}}2",
            r"\vartheta(a,u)=\frac{a}{a+1-u}",
            r"\Psi_{\rm SC}(a,c,u)=\max\{a,\vartheta(a,u)\}+E_{\rm sc}(c)-1",
            r"x_L(\theta)=\frac{1-4\theta+\theta^2}{2(1-2\theta)}",
            r"\rho(\theta)=\frac{1-2\theta}{1-\theta^2}",
            r"a=x\rho(\theta),\qquad c=x+\theta,\qquad u=1-\rho(\theta)+a",
            r"0\le\theta\le2-\sqrt3",
            r"x_L(\theta)\le x\le\frac12-\theta",
            r"0<a<1",
            r"0\le c\le\frac12",
            r"\frac12\le u<1",
            r"\Delta(t)=\sqrt{t^2+t+1}",
            r"t\ge1",
            r"0<a<1,\qquad 0<b<1,\qquad 0\le c\le\frac12",
            r"c=\frac{t(1-b)}{t+1}",
            r"u=\frac{\Delta(t)-a-tb-1}{t}",
            r"0\le c<u<1",
            r"a+tb\le\Delta(t)-1-\frac t2",
            r"\Delta(t)-a-tb-t\le\frac{1-a}{t+1}",
            r"\(\Omega_{\rm SC}^{T}\) be the set of",
            r"\(\Omega_{\rm SC}^{V}\) be the set of",
            r"\Psi_{\rm SC}(a,c,u)\le0",
        ),
        (
            """
            def strictSupercriticalForwardSupremum (c : ℝ) : ℝ :=
              (c + Real.sqrt (c^2 - 8 * c + 4)) / 2

            def adjacentSupportSlack (a c u : ℝ) : ℝ :=
              max a (a / (a + 1 - u)) + strictSupercriticalForwardSupremum c - 1
            """,
            """
            def t3SupportRatio (v : T3AdjacentSupportInput) : ℝ :=
              (1 - 2 * v.theta) / (1 - v.theta^2)

            def t3SupportLowerBound (v : T3AdjacentSupportInput) : ℝ :=
              (1 - 4 * v.theta + v.theta^2) / (2 * (1 - 2 * v.theta))

            def t3SupportBackward (v : T3AdjacentSupportInput) : ℝ := v.x * t3SupportRatio v
            def t3SupportRadial (v : T3AdjacentSupportInput) : ℝ := v.x + v.theta
            def t3SupportEndpoint (v : T3AdjacentSupportInput) : ℝ :=
              1 - t3SupportRatio v + t3SupportBackward v

            def t3AdjacentSupportDomain (v : T3AdjacentSupportInput) : Prop :=
              0 ≤ v.theta ∧ v.theta ≤ 2 - Real.sqrt 3 ∧
                t3SupportLowerBound v ≤ v.x ∧ v.x ≤ 1 / 2 - v.theta ∧
                0 < t3SupportBackward v ∧
                0 ≤ t3SupportRadial v ∧ t3SupportRadial v ≤ 1 / 2 ∧
                1 / 2 ≤ t3SupportEndpoint v ∧ t3SupportEndpoint v < 1
            """,
            """
            def cornerRadical (t : ℝ) : ℝ := Real.sqrt (t^2 + t + 1)
            def vd1SupportRadial (v : Vd1AdjacentSupportInput) : ℝ :=
              v.t * (1 - v.b) / (v.t + 1)
            def vd1SupportEndpoint (v : Vd1AdjacentSupportInput) : ℝ :=
              (cornerRadical v.t - v.a - v.t * v.b - 1) / v.t

            def vd1AdjacentSupportDomain (v : Vd1AdjacentSupportInput) : Prop :=
              1 ≤ v.t ∧
                0 < v.a ∧ v.a < 1 ∧
                0 < v.b ∧ v.b < 1 ∧
                0 ≤ vd1SupportRadial v ∧ vd1SupportRadial v ≤ 1 / 2 ∧
                vd1SupportRadial v < vd1SupportEndpoint v ∧ vd1SupportEndpoint v < 1 ∧
                v.a + v.t * v.b ≤ cornerRadical v.t - 1 - v.t / 2 ∧
                cornerRadical v.t - v.a - v.t * v.b - v.t ≤ (1 - v.a) / (v.t + 1)
            """,
        ),
    ),
    DefinitionContract(
        "VD residuals, corner graphs, domains, and objectives",
        "04_strategy2_optimization_vd.tex",
        (
            "traceComponentEnd",
            "residualLowerBound",
            "vdAdjRightRequirement",
            "vdAdjLeftRequirement",
            "vdAdjSupportStart",
            "vdAdjSupportEnd",
            "vdAdjBaseDomain",
            "vdAdjSupportDomain",
            "vdAdjNoSupportDomain",
            "vdAdjSupportSlack",
            "vdAdjNoSupportSlack",
            "vdNonRightRequirement",
            "vdNonLeftRequirement",
            "vdNonLeftTraceEnd",
            "vdNonRightTraceEnd",
            "vdNonCornerRadialReach",
            "vdNonCenterExit",
            "vdNonDomain",
            "vdNonadjacentSlack",
        ),
        (
            r"""
            \mathsf E(L,U;x)=
            \begin{cases}
            x,&x<L,\\
            U,&L\le x\le U,\\
            x,&U<x,
            \end{cases}
            """,
            r"\mathcal R_{[L,U]}(x)=1-\mathsf E(L,U;x)",
            r"\Delta_t=\sqrt{t^2+t+1}",
            r"t>0",
            r"A_R=\mathcal R_{[k/r,w+d]}(q_0)",
            r"A_L=\mathcal R_{[k/w,r+a]}(p_0)",
            r"\lambda_+=\frac{t(1-q_1)}{t+1}",
            r"u_+=\frac{\Delta_t-p_1-tq_1-1}{t}",
            r"(r,a,d)\in\mathcal D_2",
            r"0<p_0,q_0<1",
            r"p_0+q_0>1",
            r"p_0^2+p_0q_0+q_0^2\le1",
            r"A_L>0,\qquad A_R\ge0,\qquad A_R+A_L<\frac12",
            r"a+d<\frac1{24}",
            r"a+d<\frac{\min\{r,w\}}6",
            r"0<p_1,q_1<1",
            r"p_1\ge A_R,\qquad q_1\ge A_L",
            r"p_1+q_1<\frac12",
            r"0\le\lambda_+<u_+\le1",
            r"u_+\le\lambda_+",
            r"Let \(\Omega_{\rm VD}^{\rm adj,0}\) satisfy all the conditions above through \(p_1+q_1<1/2\)",
            r"replace the final positive-interval condition by",
            r"\Psi_{\rm VD}^{\rm adj,+}=\max\left\{d-\frac{A_L}{4},\ u_+-1+d\right\}",
            r"\Psi_{\rm VD}^{\rm adj,0}=d-\frac{A_L}{4}",
            r"x=\frac{k}{w},\qquad y=\frac{k}{r}",
            r"A_R=\mathcal R_{[y,w+d]}(q_0)",
            r"A_L=\mathcal R_{[x,r+a]}(p_0)",
            r"C_v=\frac{\Delta_t-p_v-tq_v}{t+1}",
            r"\sigma=a+d",
            r"d_2=d,\qquad d_4=a",
            r"\mathcal O_{3,0}:\quad \frac ar\le\frac dw,\quad d_3=\frac ar",
            r"\mathcal O_{3,1}:\quad \frac dw<\frac ar,\quad d_3=\frac dw",
            r"\mathcal M_0:\quad A_R\le A_L,\quad m=A_R",
            r"\mathcal M_1:\quad A_L<A_R,\quad m=A_L",
            r"A_R>0,\qquad A_L>0,\qquad A_R+A_L<\frac12",
            r"\sigma<\frac x2,\qquad \sigma<\frac y2",
            r"x^2+x(w+d)+(w+d)^2\le1",
            r"y^2+y(r+a)+(r+a)^2\le1",
            r"0<p_v,q_v<1",
            r"p_v\ge A_R,\qquad q_v\ge A_L",
            r"0\le C_v\le1",
            r"\Psi_{\rm VD}^{\rm non}=\max\{\sigma-A_R,\ \sigma-A_L,\ d_j-m,\ C_v-1+m\}",
        ),
        (
            """
            def traceComponentEnd (L U x : ℝ) : ℝ :=
              if x < L then x else if x ≤ U then U else x

            def residualLowerBound (L U x : ℝ) : ℝ := 1 - traceComponentEnd L U x
            """,
            """
            def vdAdjRightRequirement (v : VdAdjacentInput) : ℝ :=
              residualLowerBound (centerK v.center / v.center.r) (w v.center + v.center.delta) v.q0

            def vdAdjLeftRequirement (v : VdAdjacentInput) : ℝ :=
              residualLowerBound (centerK v.center / w v.center) (v.center.r + v.center.alpha) v.p0

            def vdAdjSupportStart (v : VdAdjacentInput) : ℝ :=
              v.t * (1 - v.q1) / (v.t + 1)

            def vdAdjSupportEnd (v : VdAdjacentInput) : ℝ :=
              (cornerRadical v.t - v.p1 - v.t * v.q1 - 1) / v.t

            def vdAdjBaseDomain (v : VdAdjacentInput) : Prop :=
              centerCE2Domain v.center ∧
                0 < v.p0 ∧ v.p0 < 1 ∧
                0 < v.q0 ∧ v.q0 < 1 ∧
                1 < v.p0 + v.q0 ∧
                v.p0^2 + v.p0 * v.q0 + v.q0^2 ≤ 1 ∧
                0 < vdAdjLeftRequirement v ∧ 0 ≤ vdAdjRightRequirement v ∧ vdAdjRightRequirement v + vdAdjLeftRequirement v < 1 / 2 ∧
                v.center.alpha + v.center.delta < 1 / 24 ∧
                v.center.alpha + v.center.delta < min v.center.r (w v.center) / 6 ∧
                0 < v.t ∧
                0 < v.p1 ∧ v.p1 < 1 ∧
                0 < v.q1 ∧ v.q1 < 1 ∧
                vdAdjRightRequirement v ≤ v.p1 ∧ vdAdjLeftRequirement v ≤ v.q1 ∧
                v.p1 + v.q1 < 1 / 2

            def vdAdjSupportDomain (v : VdAdjacentInput) : Prop :=
              vdAdjBaseDomain v ∧
                0 ≤ vdAdjSupportStart v ∧ vdAdjSupportStart v < vdAdjSupportEnd v ∧ vdAdjSupportEnd v ≤ 1

            def vdAdjNoSupportDomain (v : VdAdjacentInput) : Prop :=
              vdAdjBaseDomain v ∧ vdAdjSupportEnd v ≤ vdAdjSupportStart v

            def vdAdjSupportSlack (v : VdAdjacentInput) : ℝ :=
              max (v.center.delta - vdAdjLeftRequirement v / 4) (vdAdjSupportEnd v - 1 + v.center.delta)

            def vdAdjNoSupportSlack (v : VdAdjacentInput) : ℝ :=
              v.center.delta - vdAdjLeftRequirement v / 4
            """,
            """
            def vdNonRightRequirement (v : VdNonadjacentInput) : ℝ :=
              residualLowerBound (centerK v.center / v.center.r) (w v.center + v.center.delta) v.q0

            def vdNonLeftRequirement (v : VdNonadjacentInput) : ℝ :=
              residualLowerBound (centerK v.center / w v.center) (v.center.r + v.center.alpha) v.p0

            def vdNonLeftTraceEnd (v : VdNonadjacentInput) : ℝ := centerK v.center / w v.center
            def vdNonRightTraceEnd (v : VdNonadjacentInput) : ℝ := centerK v.center / v.center.r

            def vdNonCornerRadialReach (v : VdNonadjacentInput) : ℝ :=
              (cornerRadical v.t - v.pv - v.t * v.qv) / (v.t + 1)

            def vdNonCenterExit (v : VdNonadjacentInput) : ℝ :=
              match v.position with
              | .pos2 => v.center.delta
              | .pos3 => min (v.center.alpha / v.center.r) (v.center.delta / w v.center)
              | .pos4 => v.center.alpha

            def vdNonDomain (v : VdNonadjacentInput) : Prop :=
              centerCE2Domain v.center ∧
                0 < v.p0 ∧ v.p0 < 1 ∧
                0 < v.q0 ∧ v.q0 < 1 ∧
                1 < v.p0 + v.q0 ∧
                v.p0^2 + v.p0 * v.q0 + v.q0^2 ≤ 1 ∧
                0 < vdNonRightRequirement v ∧ 0 < vdNonLeftRequirement v ∧ vdNonRightRequirement v + vdNonLeftRequirement v < 1 / 2 ∧
                v.center.alpha + v.center.delta < vdNonLeftTraceEnd v / 2 ∧
                v.center.alpha + v.center.delta < vdNonRightTraceEnd v / 2 ∧
                vdNonLeftTraceEnd v ^ 2 + vdNonLeftTraceEnd v * (w v.center + v.center.delta) +
                    (w v.center + v.center.delta) ^ 2 ≤ 1 ∧
                vdNonRightTraceEnd v ^ 2 + vdNonRightTraceEnd v * (v.center.r + v.center.alpha) +
                    (v.center.r + v.center.alpha) ^ 2 ≤ 1 ∧
                0 < v.t ∧
                0 < v.pv ∧ v.pv < 1 ∧
                0 < v.qv ∧ v.qv < 1 ∧
                vdNonRightRequirement v ≤ v.pv ∧ vdNonLeftRequirement v ≤ v.qv ∧
                0 ≤ vdNonCornerRadialReach v ∧ vdNonCornerRadialReach v ≤ 1

            def vdNonadjacentSlack (v : VdNonadjacentInput) : ℝ :=
              let sigma := v.center.alpha + v.center.delta
              let m := min (vdNonRightRequirement v) (vdNonLeftRequirement v)
              max (max (sigma - vdNonRightRequirement v) (sigma - vdNonLeftRequirement v))
                (max (vdNonCenterExit v - m) (vdNonCornerRadialReach v - 1 + m))
            """,
        ),
    ),
)


REQUIRED_LEAN_TYPES = (
    "structure SignedCenterInput where r : ℝ alpha : ℝ delta : ℝ",
    "inductive ForwardCapBranch | lin | const | qMinus | qPlus",
    "structure T3Input where center : SignedCenterInput tau : ℝ beta : ℝ",
    "structure T3AdjacentSupportInput where theta : ℝ x : ℝ",
    "structure Vd1AdjacentSupportInput where t : ℝ a : ℝ b : ℝ",
    "structure VdAdjacentInput where center : SignedCenterInput p0 : ℝ q0 : ℝ t : ℝ p1 : ℝ q1 : ℝ",
    "inductive VdPosition | pos2 | pos3 | pos4",
    "structure VdNonadjacentInput where center : SignedCenterInput p0 : ℝ q0 : ℝ t : ℝ pv : ℝ qv : ℝ position : VdPosition",
)


LEAN_THEOREM_SIGNATURES = {
    "problemS2E1": (
        "(s : SignedCenterInput)",
        "(hs : oneGapCE1Domain s ∨ centerCE2Domain s)",
        "endpointSlackE1 s < 0 := by sorry",
    ),
    "problemS2E2": (
        "(s : SignedCenterInput)",
        "(hs : centerCE2Domain s)",
        "endpointSlackE2 s < 0 := by sorry",
    ),
    "problemS2R1": (
        "(s : SignedCenterInput)",
        "(hs : oneGapCE1Domain s)",
        "returnSlack s < 0 := by sorry",
    ),
    "problemS2R2": (
        "(s : SignedCenterInput)",
        "(hs : centerCE2Domain s)",
        "returnSlack s < 0 := by sorry",
    ),
    "problemS2T3": (
        "(x : T3Input)",
        "(hx : t3Domain x)",
        "t3EndpointSlack x < 0 := by sorry",
    ),
    "problemS2SCT": (
        "(v : T3AdjacentSupportInput)",
        "(hv : t3AdjacentSupportDomain v)",
        "adjacentSupportSlack (t3SupportBackward v) (t3SupportRadial v) (t3SupportEndpoint v) ≤ 0 := by sorry",
    ),
    "problemS2SCV": (
        "(v : Vd1AdjacentSupportInput)",
        "(hv : vd1AdjacentSupportDomain v)",
        "adjacentSupportSlack v.a (vd1SupportRadial v) (vd1SupportEndpoint v) ≤ 0 := by sorry",
    ),
    "problemS2VDAdjacentSupport": (
        "(v : VdAdjacentInput)",
        "(hv : vdAdjSupportDomain v)",
        "vdAdjSupportSlack v < 0 := by sorry",
    ),
    "problemS2VDAdjacentNoSupport": (
        "(v : VdAdjacentInput)",
        "(hv : vdAdjNoSupportDomain v)",
        "vdAdjNoSupportSlack v < 0 := by sorry",
    ),
    "problemS2VDNonadjacent": (
        "(v : VdNonadjacentInput)",
        "(hv : vdNonDomain v)",
        "vdNonadjacentSlack v < 0 := by sorry",
    ),
}


def compact(text: str) -> str:
    """Remove insignificant whitespace while retaining every math token."""

    return re.sub(r"\s+", "", text)


def strip_tex_comments(text: str) -> str:
    return re.sub(r"(?m)(?<!\\)%.*$", "", text)


def active_tex(text: str) -> str:
    r"""Remove comments and nested inactive ``\iffalse ... \fi`` regions."""

    text = strip_tex_comments(text)
    inactive = re.compile(r"\\iffalse\b(?:(?!\\iffalse\b|\\fi\b).)*\\fi\b", re.S)
    previous = None
    while text != previous:
        previous = text
        text = inactive.sub("", text)
    return text


def tex_math_payload(text: str) -> str:
    """Return all TeX inline/display math in source order."""

    text = active_tex(text)
    pattern = re.compile(
        r"\\\[(.*?)\\\]|\\\((.*?)\\\)|(?<!\\)\$(.*?)(?<!\\)\$",
        re.DOTALL,
    )
    spans: list[str] = []
    for match in pattern.finditer(text):
        span = next(group for group in match.groups() if group is not None)
        spans.append(compact(span))
    return "\n".join(spans)


def tex_source_payload(text: str) -> str:
    """Normalize the complete uncommented TeX source, including binding prose."""

    return re.sub(r"\s+", " ", active_tex(text)).strip()


def strip_lean_comments(text: str) -> str:
    """Strip nested Lean block comments and line comments."""

    out: list[str] = []
    i = 0
    depth = 0
    while i < len(text):
        if text.startswith("/-", i):
            depth += 1
            i += 2
        elif depth and text.startswith("-/", i):
            depth -= 1
            i += 2
        elif depth:
            i += 1
        elif text.startswith("--", i):
            newline = text.find("\n", i)
            i = len(text) if newline < 0 else newline
        else:
            out.append(text[i])
            i += 1
    return "".join(out)


LEAN_STRING_RE = re.compile(r'"(?:\\.|[^"\\])*"', re.S)


def lean_code(text: str) -> str:
    """Return uncommented Lean code with string-literal contents removed."""

    return LEAN_STRING_RE.sub('""', strip_lean_comments(text))


def lean_payload(text: str) -> str:
    """Strip comments while preserving whitespace as a token separator."""

    return re.sub(r"\s+", " ", lean_code(text)).strip()


def extract_lean_theorem(text: str, name: str) -> str:
    """Return one uncommented top-level theorem declaration and its body."""

    active = lean_code(text)
    match = re.search(
        rf"(?ms)^theorem\s+{re.escape(name)}\b.*?"
        rf"(?=^(?:theorem|def|structure|inductive|namespace|end)\b|\Z)",
        active,
    )
    return match.group(0) if match else ""


def contains_lean(text: str, fragment: str) -> bool:
    return re.sub(r"\s+", " ", fragment).strip() in lean_payload(text)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_labeled_environment(text: str, label: str) -> str:
    marker = rf"\label{{{label}}}"
    at = text.find(marker)
    if at < 0:
        return ""
    begin = text.rfind(r"\begin{theorem}", 0, at)
    end = text.find(r"\end{theorem}", at)
    if begin < 0 or end < 0:
        return ""
    return text[begin : end + len(r"\end{theorem}")]


def source_theorem_digest(text: str, label: str) -> str:
    block = extract_labeled_environment(active_tex(text), label)
    return sha256(compact(block)) if block else "MISSING"


def contains(text: str, fragment: str) -> bool:
    return compact(fragment) in compact(active_tex(text))


def validate(
    tex_sources: dict[str, str], lean: str, *, check_fingerprints: bool = True
) -> list[str]:
    errors: list[str] = []
    joined_tex = "\n".join(tex_sources.values())
    source_theorems = tex_sources[SOURCE_THEOREM_FILE]

    if check_fingerprints:
        for path, expected in EXPECTED_TEX_MATH_SHA256.items():
            actual = sha256(tex_math_payload(tex_sources[path]))
            if actual != expected:
                errors.append(
                    f"TeX mathematical payload changed: {path} "
                    f"(expected {expected}, found {actual})"
                )

        for path, expected in EXPECTED_TEX_SOURCE_SHA256.items():
            actual = sha256(tex_source_payload(tex_sources[path]))
            if actual != expected:
                errors.append(
                    f"TeX full semantic source changed: {path} "
                    f"(expected {expected}, found {actual})"
                )

        actual_lean = sha256(lean_payload(lean))
        if actual_lean != EXPECTED_LEAN_SHA256:
            errors.append(
                "Lean statement payload changed: Problems.lean "
                f"(expected {EXPECTED_LEAN_SHA256}, found {actual_lean})"
            )

    for contract in CONTRACTS:
        for label in contract.problem_labels:
            if not contains(joined_tex, rf"\label{{{label}}}"):
                errors.append(f"{contract.key}: missing TeX problem label {label}")
        if not contains(source_theorems, rf"\label{{{contract.source_owner}}}"):
            errors.append(
                f"{contract.key}: missing source-only owner {contract.source_owner}"
            )
        for theorem in contract.lean_theorems:
            theorem_block = extract_lean_theorem(lean, theorem)
            if not theorem_block:
                errors.append(f"{contract.key}: missing Lean shell {theorem}")
                continue
            for fragment in LEAN_THEOREM_SIGNATURES[theorem]:
                if not contains_lean(theorem_block, fragment):
                    errors.append(
                        f"{contract.key}: {theorem} missing signature clause: {fragment}"
                    )
        for fragment in contract.tex_require:
            if not contains(joined_tex, fragment):
                errors.append(f"{contract.key}: missing TeX semantic clause: {fragment}")
        for fragment in contract.lean_require:
            if not contains_lean(lean, fragment):
                errors.append(f"{contract.key}: missing Lean semantic clause: {fragment}")

    for contract in DEFINITION_CONTRACTS:
        tex_source = tex_sources[contract.tex_file]
        for fragment in contract.tex_require:
            if not contains(tex_source, fragment):
                errors.append(
                    f"{contract.key}: missing TeX defining clause in "
                    f"{contract.tex_file}: {fragment}"
                )
        for fragment in contract.lean_require:
            if not contains_lean(lean, fragment):
                errors.append(
                    f"{contract.key}: missing Lean defining clause: {fragment}"
                )

    for fragment in REQUIRED_LEAN_TYPES:
        if not contains_lean(lean, fragment):
            errors.append(f"missing Lean input-type declaration: {fragment}")

    mapped_defs = [
        name for contract in DEFINITION_CONTRACTS for name in contract.lean_defs
    ]
    duplicate_mappings = sorted(
        {name for name in mapped_defs if mapped_defs.count(name) != 1}
    )
    if duplicate_mappings:
        errors.append(
            "Lean definitions mapped more than once: " + ", ".join(duplicate_mappings)
        )
    actual_defs = set(
        re.findall(r"(?m)^def\s+([A-Za-z][A-Za-z0-9_']*)\b", lean_code(lean))
    )
    mapped_def_set = set(mapped_defs)
    if actual_defs - mapped_def_set:
        errors.append(
            "unmapped Lean definitions: " + ", ".join(sorted(actual_defs - mapped_def_set))
        )
    if mapped_def_set - actual_defs:
        errors.append(
            "stale mapped Lean definitions: "
            + ", ".join(sorted(mapped_def_set - actual_defs))
        )

    actual_theorems = set(
        re.findall(
            r"(?m)^theorem\s+([A-Za-z][A-Za-z0-9_']*)\b",
            lean_code(lean),
        )
    )
    expected_theorems = set(LEAN_THEOREM_SIGNATURES)
    if actual_theorems != expected_theorems:
        missing = sorted(expected_theorems - actual_theorems)
        extra = sorted(actual_theorems - expected_theorems)
        errors.append(
            "Lean theorem inventory changed: "
            f"missing={missing or 'none'}, extra={extra or 'none'}"
        )

    if check_fingerprints:
        for label, expected in EXPECTED_SOURCE_THEOREM_SHA256.items():
            actual = source_theorem_digest(source_theorems, label)
            if actual != expected:
                errors.append(
                    f"source-only theorem statement changed: {label} "
                    f"(expected {expected}, found {actual})"
                )

    branch_clauses = (
        "def forwardCapBranch (c x : ℝ) : ForwardCapBranch",
        "if x ≤ 1 - c then .lin",
        "else if x < qPlusTransition c then .qPlus",
        "else if x = qPlusTransition c then .const",
        "else if x ≤ lowerBreakpoint c then .qPlus",
        "else if x < upperBreakpoint c then .const",
        "else if x < c then .qMinus",
        "def forwardCapBranchValue",
        "forwardCapBranchValue c x (forwardCapBranch c x)",
    )
    for clause in branch_clauses:
        if not contains_lean(lean, clause):
            errors.append(f"forward-cap enumeration is not executable: {clause}")

    # This is intentionally a paper-only inventory check.  The Lean T3 shell
    # is synchronized to prob:s2-t3-compact-projection above, not asserted to
    # be equivalent to this nine-variable enumeration.
    for clause in (
        r"\label{prob:s2-t3-endpoint}",
        r"\varepsilon\in\{1,2\}",
        r"i,h\in\{0,1,2\}",
        r"j\in J_\varepsilon",
        r"For \(\varepsilon=1\), put \(J_\varepsilon=\{0\}\); for \(\varepsilon=2\), put \(J_\varepsilon=\{0,1,2\}\).",
        r"Equality at either endpoint of the hit interval belongs to \(\mathcal K_0\).",
        r"(\ell_5,\ell_1)\in\mathfrak B^2",
        r"a_1+a_5>1",
        r"a_1+a_5\le1",
        r"\Psi_{\rm T3}(\xi)<0",
    ):
        if not contains(joined_tex, clause):
            errors.append(f"paper-only T3 finite inventory changed: {clause}")

    for old_label in (
        "thm:s2-pure-e1",
        "thm:s2-pure-e2",
        "thm:s2-pure-r1",
        "thm:s2-pure-r2",
        "thm:s2-pure-t3",
        "thm:s2-pure-sc",
        "thm:s2-pure-vd-adjacent",
        "thm:s2-pure-vd-nonadjacent",
    ):
        if contains(source_theorems, rf"\label{{{old_label}}}"):
            errors.append(f"duplicate active/source-only theorem label remains: {old_label}")

    sorry_count = len(re.findall(r":= by\s+sorry\b", lean_code(lean)))
    if sorry_count != 10:
        errors.append(
            f"expected 10 intentional sorry placeholders, found {sorry_count}"
        )
    return errors


def mutation_self_tests(
    tex_sources: dict[str, str], lean: str
) -> tuple[list[str], int]:
    """Ensure substantive mutations are rejected by the same validator."""

    failures: list[str] = []
    cases: list[tuple[str, dict[str, str], str]] = []

    mutated_lean = lean.replace("endpointSlackE1 s < 0", "endpointSlackE1 s ≤ 0", 1)
    cases.append(("Lean strictness", tex_sources, mutated_lean))

    mutated_lean = lean.replace("0 < t3ForwardEnd x ∧ ", "", 1)
    cases.append(("Lean omitted domain conjunct", tex_sources, mutated_lean))

    mutated_lean = lean.replace(
        "forwardCap (1 - s.delta / s.r) (s.r - s.delta)",
        "forwardCap (s.r - s.delta) (1 - s.delta / s.r)",
        1,
    )
    cases.append(("Lean formula argument order", tex_sources, mutated_lean))

    mutated_lean = lean.replace(
        "x < qPlusTransition c then .qPlus",
        "x ≤ qPlusTransition c then .qPlus",
        1,
    )
    cases.append(("Lean branch boundary", tex_sources, mutated_lean))

    mutated_lean = lean.replace("| pos4", "| pos5", 1)
    cases.append(("Lean finite Vd position", tex_sources, mutated_lean))

    theorem_block = extract_lean_theorem(lean, "problemS2E1")
    mutated_lean = lean.replace(theorem_block, f"/-\n{theorem_block}\n-/", 1)
    cases.append(("Lean commented-out theorem shell", tex_sources, mutated_lean))

    mutated_lean = lean.replace(
        theorem_block,
        '''theorem problemS2E1 : True := by
  let auditDecoy := "(s : SignedCenterInput) (hs : oneGapCE1Domain s ∨ centerCE2Domain s) endpointSlackE1 s < 0 := by sorry"
  trivial
''',
        1,
    )
    cases.append(("Lean theorem string-literal decoy", tex_sources, mutated_lean))

    # Primitive-formula mutations that used to escape the marker-only checker.
    mutated_lean = lean.replace(
        "def t3Q (x : T3Input) : ℝ := 1 - t3Radical x + x.beta",
        "def t3Q (x : T3Input) : ℝ := 2 - t3Radical x + x.beta",
        1,
    )
    cases.append(("Lean T3 primitive formula", tex_sources, mutated_lean))

    mutated_lean = lean.replace(
        "Real.sqrt (1 - s.r * w s)",
        "Real.sqrt (2 - s.r * w s)",
        1,
    )
    cases.append(("Lean signed-center radical", tex_sources, mutated_lean))

    mutated_lean = lean.replace(
        "2 * (1 - x^2) * c^2 /",
        "3 * (1 - x^2) * c^2 /",
        1,
    )
    cases.append(("Lean Q-plus numerator", tex_sources, mutated_lean))

    mutated_lean = lean.replace(
        "def residualLowerBound (L U x : ℝ) : ℝ := 1 - traceComponentEnd L U x",
        "def residualLowerBound (L U x : ℝ) : ℝ := 2 - traceComponentEnd L U x",
        1,
    )
    cases.append(("Lean VD residual formula", tex_sources, mutated_lean))

    mutated_lean = lean.replace(
        "max (v.center.delta - vdAdjLeftRequirement v / 4) "
        "(vdAdjSupportEnd v - 1 + v.center.delta)",
        "max (v.center.delta - vdAdjRightRequirement v / 4) "
        "(vdAdjSupportEnd v - 1 + v.center.delta)",
        1,
    )
    cases.append(("Lean VD adjacent objective", tex_sources, mutated_lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_t3.tex"] = mutated_tex[
        "04_strategy2_optimization_t3.tex"
    ].replace(r"i,h\in\{0,1,2\}", r"i,h\in\{0,1\}", 1)
    cases.append(("TeX T3 branch range", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_vd.tex"] = mutated_tex[
        "04_strategy2_optimization_vd.tex"
    ].replace(r"\Psi_{\rm VD}^{\rm non}<0", r"\Psi_{\rm VD}^{\rm non}\le0", 1)
    cases.append(("TeX objective strictness", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_t3.tex"] = mutated_tex[
        "04_strategy2_optimization_t3.tex"
    ].replace(r"q=1-z+\beta", r"q=2-z+\beta", 1)
    cases.append(("TeX T3 primitive formula", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_map.tex"] = mutated_tex[
        "04_strategy2_optimization_map.tex"
    ].replace(r"2(1-x^2)c^2", r"3(1-x^2)c^2", 1)
    cases.append(("TeX Q-plus numerator", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_rescuer.tex"] = mutated_tex[
        "04_strategy2_optimization_rescuer.tex"
    ].replace(
        r"=\max\{a,\vartheta(a,u)\}+E_{\rm sc}(c)-1",
        r"=\max\{a,\vartheta(a,u)\}+E_{\rm sc}(c)-2",
        1,
    )
    cases.append(("TeX SC objective formula", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_vd.tex"] = mutated_tex[
        "04_strategy2_optimization_vd.tex"
    ].replace(
        r"\mathcal R_{[L,U]}(x)=1-\mathsf E(L,U;x)",
        r"\mathcal R_{[L,U]}(x)=2-\mathsf E(L,U;x)",
        1,
    )
    cases.append(("TeX VD residual formula", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_vd.tex"] = mutated_tex[
        "04_strategy2_optimization_vd.tex"
    ].replace(r"d-\frac{A_L}{4}", r"d-\frac{A_R}{4}", 1)
    cases.append(("TeX VD adjacent objective", mutated_tex, lean))

    # Binding prose and uncommented ownership are semantic interface data too.
    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_vd.tex"] = mutated_tex[
        "04_strategy2_optimization_vd.tex"
    ].replace(
        r"replace the final positive-interval condition by",
        r"retain the final positive-interval condition and add",
        1,
    )
    cases.append(("TeX VD no-support binding prose", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_rescuer.tex"] = mutated_tex[
        "04_strategy2_optimization_rescuer.tex"
    ].replace(r"be the set of", r"not be the set of", 1)
    cases.append(("TeX SC set-binding prose", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_t3.tex"] = mutated_tex[
        "04_strategy2_optimization_t3.tex"
    ].replace(r"J_\varepsilon=\{0,1,2\}", r"J_\varepsilon=\{0,1\}", 1)
    cases.append(("TeX T3 finite-index binding prose", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_t3.tex"] = mutated_tex[
        "04_strategy2_optimization_t3.tex"
    ].replace(
        r"belongs to \(\mathcal K_0\)",
        r"belongs to \(\mathcal K_1\)",
        1,
    )
    cases.append(("TeX T3 equality-cell binding prose", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    mutated_tex["04_strategy2_optimization_vd.tex"] = mutated_tex[
        "04_strategy2_optimization_vd.tex"
    ].replace(
        r"\label{prob:s2-vd-adjacent}",
        r"% \label{prob:s2-vd-adjacent}",
        1,
    )
    cases.append(("TeX commented-out problem owner", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    target = r"\(\Omega_{\rm SC}^{V}\) be the set of"
    mutated_tex["04_strategy2_optimization_rescuer.tex"] = mutated_tex[
        "04_strategy2_optimization_rescuer.tex"
    ].replace(target, rf"\iffalse {target} \fi", 1)
    cases.append(("TeX inactive SC binding prose", mutated_tex, lean))

    mutated_tex = dict(tex_sources)
    target = r"\label{thm:s2-univ-vd-adjacent}"
    mutated_tex[SOURCE_THEOREM_FILE] = mutated_tex[SOURCE_THEOREM_FILE].replace(
        target, rf"\iffalse {target} \fi", 1
    )
    cases.append(("TeX inactive source theorem owner", mutated_tex, lean))

    for name, mutated_sources, mutated_lean in cases:
        if not validate(
            mutated_sources, mutated_lean, check_fingerprints=False
        ):
            failures.append(f"mutation escaped detection: {name}")
    return failures, len(cases)


def load_sources() -> tuple[dict[str, str], str]:
    paths = (*TEX_SPEC_FILES, SOURCE_THEOREM_FILE)
    tex_sources = {
        path: (PAPER / path).read_text(encoding="utf-8") for path in paths
    }
    return tex_sources, LEAN_PATH.read_text(encoding="utf-8")


def print_digests(tex_sources: dict[str, str], lean: str) -> None:
    print("EXPECTED_TEX_MATH_SHA256 = {")
    for path in TEX_SPEC_FILES:
        print(f'    "{path}": "{sha256(tex_math_payload(tex_sources[path]))}",')
    print("}")
    print("EXPECTED_TEX_SOURCE_SHA256 = {")
    for path in TEX_SPEC_FILES:
        print(f'    "{path}": "{sha256(tex_source_payload(tex_sources[path]))}",')
    print("}")
    print("EXPECTED_SOURCE_THEOREM_SHA256 = {")
    theorem_source = tex_sources[SOURCE_THEOREM_FILE]
    for contract in CONTRACTS:
        label = contract.source_owner
        print(f'    "{label}": "{source_theorem_digest(theorem_source, label)}",')
    print("}")
    print(f'EXPECTED_LEAN_SHA256 = "{sha256(lean_payload(lean))}"')


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--print-digests",
        action="store_true",
        help="print reviewed structural-semantic fingerprints",
    )
    args = parser.parse_args()
    tex_sources, lean = load_sources()
    if args.print_digests:
        print_digests(tex_sources, lean)
        return

    errors = validate(tex_sources, lean)
    mutation_failures, mutation_count = mutation_self_tests(tex_sources, lean)
    errors.extend(mutation_failures)
    if errors:
        print("verify_strategy2_spec_sync: FAILED")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    definition_count = len(
        {name for contract in DEFINITION_CONTRACTS for name in contract.lean_defs}
    )
    print(
        "verify_strategy2_spec_sync: PASS "
        f"(7 universal + 1 compact-T3 theorem contracts; "
        f"{len(DEFINITION_CONTRACTS)} definition families covering "
        f"{definition_count} Lean defs and {len(REQUIRED_LEAN_TYPES)} input types; "
        f"10 admitted Lean shells; {mutation_count} fingerprint-independent "
        "mutation tests; full T3 cells paper-only)"
    )


if __name__ == "__main__":
    main()
