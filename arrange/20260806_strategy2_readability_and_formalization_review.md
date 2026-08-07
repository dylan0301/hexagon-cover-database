# Strategy 2 Readability and Formalization Review

This review is split into two audit documents.

1. [`20260806_strategy2_readability_diagnosis.md`](20260806_strategy2_readability_diagnosis.md) gives the reviewer recommendation, identifies the readability defects, and specifies the four-layer manuscript architecture.
2. [`20260806_strategy2_formalization_plan.md`](20260806_strategy2_formalization_plan.md) records the pure optimization specifications, notation policy, file-level revision, formalization order, successful changes, and remaining interface obligations.

## Decision

The paper should undergo a **major expository revision without changing the theorem status**. The active terminal sources remain proved. The revision therefore changes ownership and presentation of definitions and calculations, not branch validity.

## Implemented boundary

- The Strategy 2 body now explains only the geometric mechanism, the parameter records, four terminal contradiction shapes, and the branch-to-certificate register.
- Appendix `04_strategy2_optimization_problems.tex` defines the scalar transfer function, strict branch certificate convention, signed domains, and four formalization-ready optimization problems.
- The T3-like, adjacent-rescuer, and Vd terminal objectives are isolated, but their complete geometry-free feasible domains remain explicit follow-up obligations.
- The Vd1 replacement remains a geometric reduction and should not be forced into an artificial optimization formulation.

See the two linked reports for the detailed audit.

## 2026-08-07 extraction completion

The previously listed T3, adjacent-rescuer, and Vd interface obligations are
now resolved in the manuscript source.  The T3 problem is a finite explicit
cell union, both rescuer source domains are algebraic-radical, and all Vd
component/radial suprema have been replaced by piecewise or graph functions.
The verification appendix is physically split.  A Lean file records only the
problem statements and contains `sorry`; no proof-assistant proof is claimed.
