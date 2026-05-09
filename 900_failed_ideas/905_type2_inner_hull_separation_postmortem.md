# Type 2 Inner-Hull Separation Postmortem

Status: Failed

The Type 2 inner-hull analysis was part of the failed separating-hypersurface program.

Definitions:

$$
IH(V)=\{x\in\mathbb R_{\ge0}^6:\exists s\in V,\ x\le s\}.
$$

The normalization function was

$$
F(d)=\frac1{S_{\mathrm{even}}^2}-\frac1{S_{\mathrm{even}}S_{\mathrm{odd}}}+\frac1{S_{\mathrm{odd}}^2}-1.
$$

Although sign behavior inside the inner hull looked structured, it did not provide a complete separation between center and outer gamma sets.
