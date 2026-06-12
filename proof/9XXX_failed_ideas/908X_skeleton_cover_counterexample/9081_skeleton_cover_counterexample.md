# Skeleton Cover Counterexample

Status: Empirical

This file records the May 24, 2026 numerical counterexample showing that the
full skeleton $S$ is covered by seven closed equilateral triangles, each with
side strictly less than $1$.

The imported data is stored in
`20260524_skeleton_cover/counterexample_cover.json`.
The independent local verifier is
`20260524_skeleton_cover/verify_skeleton_cover.py`.

Source repository:

- [`dylan0301/hexagon-cover-visual`](https://github.com/dylan0301/hexagon-cover-visual)

Source files:

- [`COUNTEREXAMPLE.md`](https://github.com/dylan0301/hexagon-cover-visual/blob/main/COUNTEREXAMPLE.md)
- [`counterexample_snapshot.json`](https://github.com/dylan0301/hexagon-cover-visual/blob/main/counterexample_snapshot.json)
- [`counterexample_cover.py`](https://github.com/dylan0301/hexagon-cover-visual/blob/main/counterexample_cover.py)
- [`counterexample_cover.json`](https://github.com/dylan0301/hexagon-cover-visual/blob/main/counterexample_cover.json)

The source note states that the retained snapshot produces seven closed
equilateral triangles with side lengths:

$$
0.997938057288,\quad 0.999413329246,\quad 0.999200000000,\quad 0.999200000000,\quad 0.999494082847,\quad 0.999200000000,\quad 0.999469224232.
$$

The local verifier checks the explicit vertex coordinates directly. It verifies:

- every imported triangle is numerically equilateral;
- every computed side length is strictly less than $1$;
- the six boundary edges of $H$ are covered;
- the six radial segments $[O,V_i]$ are covered.

Thus the full skeleton

$$
S=\partial H\cup [V_0,V_3]\cup [V_1,V_4]\cup [V_2,V_5]
$$

is numerically covered by these seven triangles.

## Verification command

Run:

```bash
python proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/908X_computation/9092_verify_skeleton_cover.py
```

The current local output reports:

```text
triangles checked: 7
max side length: 0.999494082847
verification passed
```

This remains a floating-point verification, not an exact symbolic or interval
certificate.

A negative self-check is also available:

```bash
python proof/9XXX_failed_ideas/908X_skeleton_cover_counterexample/908X_computation/9092_verify_skeleton_cover.py --expect-failure --drop-triangle C
```

Dropping the center triangle leaves gaps on all six radial segments.

## Consequence

The strategy

$$
\text{prove the main theorem by proving seven unit triangles cannot cover }S
$$

is false as a standalone target.

This does not prove a cover of the full hexagon $H$. It only shows that
the full skeleton $S$ is too small a target for the global obstruction.

This also does not change conditional half-skeleton results unless the
counterexample is separately shown to satisfy their hypotheses. In particular,
the CE0 + Vd1/Vd2 half-skeleton theorem remains a conditional theorem about
$S_{1/2}$ under its stated assumptions.
