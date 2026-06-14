# May 24 Skeleton Cover Counterexample

Status: experimental / reproducibility aid.

This folder records the retained counterexample from
`dylan0301/hexagon-cover-visual` showing seven closed equilateral triangles,
each with side strictly less than $1$, covering the unit hexagon skeleton $S$.

Source files:

- `9087_counterexample_snapshot.json`: copied from `dylan0301/hexagon-cover-visual`.
- `9086_counterexample_cover.json`: copied from `dylan0301/hexagon-cover-visual`.
- `9088_verify_skeleton_cover.py`: independent local verifier for the explicit
  triangle coordinates in `9086_counterexample_cover.json`.

The imported source states that `counterexample_cover.py` constructs and checks
the seven triangles.  The verifier here does not regenerate the triangles from
the snapshot; it independently checks the explicit vertex data against the
local definition of

$$
S=\partial H\cup [V_0,V_3]\cup [V_1,V_4]\cup [V_2,V_5].
$$

Run:

```bash
python proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/908X_computation/9088_verify_skeleton_cover.py
```

Negative self-check:

```bash
python proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/908X_computation/9088_verify_skeleton_cover.py --expect-failure --drop-triangle C
```
