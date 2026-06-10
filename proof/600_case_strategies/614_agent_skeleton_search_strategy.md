# Agent Skeleton Search Strategy

Status: Strategy

Goal: automate finite case checking and produce human-readable certificates.

After the May 24, 2026 skeleton-cover counterexample in `../800_computation/811_skeleton_cover_counterexample.md`, this search should target strengthened finite sets or additional hypotheses. It should not search for a contradiction to covering $S$ alone.

Certificate format:

```text
Case ID:
CE type:
C midpoint set:
V type tuple:
midpoint assignment:
local inequalities:
composition inequality:
contradiction:
missing assumptions:
```

The agent should enumerate cases, attach local constraints, build the chain, and output only checkable inequalities.
