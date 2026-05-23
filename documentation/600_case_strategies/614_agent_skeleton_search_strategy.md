# Agent Skeleton Search Strategy

Status: Strategy

Goal: automate finite case checking and produce human-readable certificates.

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
