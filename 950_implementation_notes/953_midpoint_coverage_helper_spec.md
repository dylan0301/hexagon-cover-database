# Midpoint Coverage Helper Spec

Status: Implementation note

Function:

```ts
getCoveredMidpoints(T_C): number[]
```

Checks

\[
M_i\in T_C.
\]

For open-triangle reasoning, strict containment is relevant. For closed computational models, boundary containment may be accepted but must be flagged as degenerate.
