# Strategy 2 Readability Diagnosis: Principal Defects I

## 3. Principal readability defects

### 3.1 The body contains an appendix-sized Strategy 2 chapter

Before this revision, `04_strategy2_summary.tex` was about 32.8 KB.  It
contained, among other things:

- the signed CE1 and CE2 semialgebraic domains;
- a formal set of center-free paths;
- the active-gap definition;
- one-gap and paired-gap endpoint formulas;
- the low root, order transition, affine coefficient sets, and threshold map;
- a five-step exact recurrence;
- a separate CE1 affine subdomain;
- a large T3-like geometric state space;
- a translated-majorant family and several suprema;
- rescuer and Vd state spaces;
- two replacement charts;
- a six-slot exact-chain register.

This is not a summary.  It duplicates the work of the technical appendices and
forces the reader to learn notation before learning the proof mechanism.

### 3.2 Geometry and calculation are interleaved

A typical current paragraph starts with a placement statement, introduces
signed center variables, defines several endpoint residuals, applies a
piecewise transfer map, switches to a contact label, proves a radical
inequality, and returns to an uncovered radial segment.

That order is natural while discovering a proof but not while presenting one.
The paper should instead use the following implication:

$$
\text{geometric state}
\longrightarrow
\text{real parameter record}
\longrightarrow
\text{optimization problem}
\longrightarrow
\text{negative optimum}
\longrightarrow
\text{geometric contradiction}.
$$

No proof step should move backward across this diagram.

### 3.3 The reader sees both canonical notation and technical aliases

The canonical notation is already complicated:

$$
g_c,\qquad
\widehat g_c,\qquad
g_c^\vee,\qquad
\widehat g_c^\vee,\qquad
g_{c,J}^\vee,\qquad
\widehat g_{c,J}^\vee,\qquad
g_c^{\rm sc}.
$$

The technical appendix then also uses

$$
B_c,\qquad F_c,\qquad G_c.
$$

These aliases are reasonable inside a branchwise calculation, but they should
not be visible in the same reader-facing argument.  The revised architecture
uses the canonical family in the geometric interface and a single explicit
bivariate function $F(c,x)$ in the pure optimization appendix.  The two
alphabets never appear in the same proof paragraph.

### 3.4 Too many variables are introduced before their role is clear

The signed center package uses

$$
R,W,E,\eta,P,k,\Delta_R,\Delta_L,\alpha,\delta.
$$

The five-chain proof then adds

$$
X,H,m_3,c_1,\ldots,c_5,z_0,\ldots,z_5,L_1,L_2.
$$

The T3 and Vd branches introduce further state spaces and endpoint variables.
Most of these variables are used only to prove one scalar sign.  A reader
should first be told the scalar sign and why it closes the branch.  Exact
coordinates should appear only in the optimization specification.
