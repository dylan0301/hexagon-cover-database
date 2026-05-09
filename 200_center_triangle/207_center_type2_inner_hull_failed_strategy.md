# Center Type 2 Inner Hull Failed Strategy

Status: Failed strategy

This file records the Type 2 inner-hull analysis as part of the failed attempt to separate center-triangle inner gamma tuples from vertex-triangle outer gamma tuples.

Define

\[
IH(V)=\{x\in\mathbb R_{\ge0}^6:\exists s\in V\text{ such that }x\le s\}.
\]

The attempted separation used the normalization function

\[
F(d)=\frac1{S_{\mathrm{even}}^2}-\frac1{S_{\mathrm{even}}S_{\mathrm{odd}}}+\frac1{S_{\mathrm{odd}}^2}-1.
\]

The heuristic sign fact was:

\[
x\in\operatorname{Int}(IH(V))\implies F(x)>0.
\]

This was not enough to prove the required separation. It is cross-referenced with the inner/outer gamma separation postmortem.
