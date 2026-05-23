# C-Triangle Repository Gap

Status: Implementation note

Current source computes center ray-intersection distance data but does not compute:

- positive-length perimeter-edge overlaps of $T_C$;
- CE0/CE1/CE2 labels;
- center vertex-cone Type 1 / Type 2;
- covered midpoint set $\{i:M_i\in T_C\}$;
- CE-specific UI or graph logic.

The CE classification applies to the C-triangle mode and should not be reused unchanged for C-circle mode.
