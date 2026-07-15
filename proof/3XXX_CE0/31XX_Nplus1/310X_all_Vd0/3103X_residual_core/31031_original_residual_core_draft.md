# Seven Open Unit Equilateral Triangles versus a Closed Unit Regular Hexagon

## A rigorous research blueprint for the proposed proof strategy

> **Project status.** This document organizes a proposed strategy for the following research target:
>
> > A closed regular hexagon of side length \(1\) cannot be covered by seven open equilateral triangles of side length \(1\).
>
> The project treats this as an open problem. This document does **not** claim to prove the result, and it does not independently verify the problem's current literature status. Its purpose is to separate the rigorous reductions already available from computational observations, conjectural geometry, and unresolved logical steps.

---

## 1. Status labels used in this document

The following labels should be read literally.

- **[Established]**: follows directly from the definitions or from a short proof supplied here.
- **[Conditional]**: correct if an explicitly stated hypothesis or missing lemma is supplied.
- **[Visual observation]**: observed in a visualization or exploratory implementation, but not yet proved and possibly valid only in part of the parameter domain.
- **[Conjecture]**: a precise statement suggested by the strategy and still requiring proof or refutation.
- **[Definition]**: notation introduced for the research program.
- **[Gap]**: a logical point that must not be silently assumed.

The distinctions matter. In particular, the two-parameter comparison and the exact geometry of the admissible regions are not yet established in the form required for a complete proof.

---

## 2. The geometric problem

Let

\[
V_i=\left(\cos\frac{i\pi}{3},\sin\frac{i\pi}{3}\right),
\qquad i\in\mathbb Z/6\mathbb Z,
\]

and let

\[
H:=\operatorname{conv}\{V_0,V_1,\ldots,V_5\}.
\]

Thus \(H\) is the **closed** regular hexagon of side length \(1\), centered at

\[
O=(0,0),
\]

with

\[
V_0=(1,0),\qquad V_1=\left(\frac12,\frac{\sqrt3}{2}\right),
\]

and counterclockwise vertex indexing. Write

\[
E_i=[V_i,V_{i+1}]
\]

for the \(i\)-th edge, with all indices understood modulo \(6\).

An **open unit triangle** means the interior of an equilateral triangle of side length \(1\). Arbitrary translations and orientations are permitted.

Under a hypothetical cover, label the triangle containing \(O\) by \(T_O\) and the triangle containing \(V_i\) by \(T_i\). These are necessarily all seven distinct triangles: two points in one open unit triangle have distance strictly less than \(1\), whereas \(|O-V_i|=|V_i-V_{i+1}|=1\), and nonadjacent hexagon vertices are farther apart. The target is therefore to rule out

\[
H\subseteq T_O\cup\bigcup_{i=0}^5T_i,
\qquad
O\in T_O,\quad V_i\in T_i.
\]

---

## 3. Intended three-case structure

Define the union of the six vertex triangles by

\[
U_V:=\bigcup_{i=0}^5T_i.
\]

There are two natural boundary sets:

\[
S:=\partial H\cap U_V
\]

and

\[
G:=\partial H\setminus U_V.
\]

Because \(U_V\) is open, \(S\) is relatively open in the boundary circle \(\partial H\), while \(G\) is relatively closed. Because the full seven-triangle family covers \(H\), every point of \(G\) must lie in \(T_O\):

\[
G\subseteq T_O.
\]

The conversation's terminology “zero-segment,” “one-segment,” and “two-segment” is most coherently formalized by counting the connected components of the **uncovered-by-vertex-triangles set** \(G\), not the components of \(S\).

### Case 0: boundary-complete, or zero-gap, case

\[
G=\varnothing,
\qquad\text{equivalently}\qquad
\partial H\subseteq U_V.
\]

The six vertex triangles cover the entire boundary of the hexagon. This is the case developed in detail below.

### Case 1: one-gap case

The set \(G\) is nonempty and connected, hence is intended to be a closed boundary arc, possibly allowing a degenerate one-point arc. Equivalently, \(S\) is one relatively open arc of \(\partial H\) if its endpoints are interpreted appropriately.

### Case 2: two-gap case

The set \(G\) has two connected components, intended to be two closed boundary arcs. Equivalently, \(S\) has two complementary relatively open arcs.

**Topological check.** To make the split exhaustive, show that \(G\) has at most two components by tracking \(H\setminus T_O\) along \(\partial H\); this short argument remains to be written out.

---

## 4. Boundary-complete case: transition points

Assume for the remainder of the main strategy that

\[
\partial H\subseteq\bigcup_{i=0}^5T_i.
\]

### 4.1 Only two vertex triangles can meet a given hexagon edge

**[Established] Edge-locality lemma.** A point of \(E_i\) can belong, among the six vertex triangles, only to \(T_i\) or \(T_{i+1}\).

The reason is the diameter separation lemma. Every point of the interior of \(E_i\) has distance strictly greater than \(1\) from each \(V_j\) other than \(V_i,V_{i+1}\). At the endpoints, the same conclusion follows from the unit distances between adjacent vertices. Therefore

\[
E_i\subseteq T_i\cup T_{i+1}.
\]

Since \(T_i\cap E_i\) and \(T_{i+1}\cap E_i\) are relatively open intervals that together cover the compact unit segment \(E_i\), they overlap. Hence

\[
E_i\cap T_i\cap T_{i+1}\ne\varnothing.
\]

In fact, this overlap is a nonempty relatively open subinterval of \(E_i\).

### 4.2 The transition points \(A_i,B_i\)

**[Definition]** For every \(i\), choose a transition point in the overlap and give it two names:

\[
B_i=A_{i+1}\in E_i\cap T_i\cap T_{i+1}.
\]

At vertex \(V_i\):

- \(A_i\in E_{i-1}=[V_{i-1},V_i]\) is the transition point on the clockwise incident edge;
- \(B_i\in E_i=[V_i,V_{i+1}]\) is the transition point on the counterclockwise incident edge.

Define the corresponding scalar distances

\[
a_i:=|V_iA_i|,
\qquad
b_i:=|V_iB_i|.
\]

Because \(A_i=B_{i-1}\) lies on the unit edge \(E_{i-1}\),

\[
\boxed{a_i+b_{i-1}=1.}
\]

Equivalently,

\[
\boxed{a_i=1-b_{i-1}}
\]

and

\[
\boxed{a_i+b_i=1+(b_i-b_{i-1}).}
\]

Summing cyclically gives

\[
\boxed{\sum_{i=0}^5(a_i+b_i)=6.}
\]

Thus the mean of the six quantities \(a_i+b_i\) is exactly \(1\).

The transition points lie in the relative interiors of their hexagon edges, so

\[
0<a_i,b_i<1.
\]

### 4.3 Generic choice of transition points

**[Established]** The transition point on each edge can be moved within a nonempty open overlap interval while remaining in both adjacent vertex triangles. The six choices therefore range over a nonempty open subset of \(\mathbb R^6\). The unwanted equalities

\[
a_i+b_i=1
\quad\Longleftrightarrow\quad
b_i=b_{i-1}
\]

form finitely many hyperplanes. Hence the transition points may be chosen so that

\[
a_i+b_i\ne1
\qquad\text{for every }i.
\]

This is the precise generic perturbation statement required later. It perturbs only the auxiliary transition points, not the seven covering triangles.

---

## 5. Supercritical, critical, and subcritical vertex triangles

**[Definition]** Relative to the chosen transition points, call \(T_i\), or equivalently the configuration at \(V_i\),

\[
\begin{aligned}
\text{supercritical} &\iff a_i+b_i>1,\\
\text{critical} &\iff a_i+b_i=1,\\
\text{subcritical} &\iff a_i+b_i<1.
\end{aligned}
\]

Using \(a_i=1-b_{i-1}\), this is equivalent to

\[
\begin{aligned}
\text{supercritical} &\iff b_i>b_{i-1},\\
\text{critical} &\iff b_i=b_{i-1},\\
\text{subcritical} &\iff b_i<b_{i-1}.
\end{aligned}
\]

**[Established]** Unless all six configurations are critical, there is at least one supercritical configuration and at least one subcritical configuration. Under the generic choice above, both types necessarily occur. This follows either from the average identity or from

\[
\sum_{i=0}^5(b_i-b_{i-1})=0.
\]

After a cyclic relabeling, one may take \(V_0\) to be supercritical.

The terminology “\(T_i\) is supercritical” is retained because it is convenient, but its dependence on the selected \(A_i,B_i\) should always be remembered.

---

## 6. Radial penetration depth

For each actual vertex triangle \(T_i\), examine the radial segment \([V_i,O]\). Since \(T_i\) is convex and contains \(V_i\), its intersection with this segment is an interval adjacent to \(V_i\).

**[Definition]** Define the radial penetration depth

\[
c_i:=\sup\left\{r\in[0,1]:
V_i+\lambda(O-V_i)\in T_i
\text{ for all }0\le\lambda<r
\right\}.
\]

Because \(|V_iO|=1\), this normalization makes \(c_i\) equal to the Euclidean length of the part of \([V_i,O]\) covered from \(V_i\) inward.

**[Conjecture] Supercritical radial-depth lemma.** If

\[
a_i+b_i>1,
\]

then

\[
\boxed{c_i<\frac12.}
\]

This lemma was proposed but not proved. Its exact role in the residual-core strategy is not yet fixed. It may supply a useful point on the radial segment that is guaranteed to remain uncovered by a supercritical vertex triangle, or it may be needed in one of the non-boundary-complete cases.

An AI working on this lemma should first test whether it is true over the entire feasible parameter domain and determine whether strict inequality follows from openness or from a stronger closed-triangle inequality \(c_i\le 1/2\).

---

## 7. Admissible regions \(\mathcal R_i(s,t)\)

For \(0\le s,t\le1\), put

\[
A_i(s)=(1-s)V_i+sV_{i-1},
\qquad
B_i(t)=(1-t)V_i+tV_{i+1},
\]

so that their distances from \(V_i\) are \(s\) and \(t\). Define the **admissible region**, or \(AB\)-region, directly by

\[
\boxed{
\mathcal R_i(s,t)
:=
\bigcup_{\substack{
T\text{ open unit equilateral}\\
V_i,A_i(s),B_i(t)\in T
}}T.
}
\]

It is open and satisfies the rotational identity

\[
\mathcal R_i(s,t)
=
\operatorname{Rot}_{i\pi/3}\bigl(\mathcal R_0(s,t)\bigr).
\]

For the actual transition data, \(T_i\) is one of the triangles in this union, so

\[
\boxed{T_i\subseteq\mathcal R_i(a_i,b_i).}
\]

Thus a point outside \(\mathcal R_i(a_i,b_i)\) is outside every possible vertex triangle satisfying the three-point constraints.

### 7.1 Feasible parameter domain

For the distinguished supercritical data one has at least

\[
0<s,t<1,
\qquad s+t>1,
\qquad \mathcal R_0(s,t)\ne\varnothing.
\]

A necessary condition comes from the distance between the two boundary points. Their incident edge rays meet at angle \(120^\circ\), so

\[
|A_0(s)-B_0(t)|^2=s^2+st+t^2.
\]

Any two points inside an open unit triangle have distance less than \(1\); hence actual feasibility implies

\[
s^2+st+t^2<1.
\]

This may not be a complete characterization of feasibility. Statements below should therefore be quantified either over actual feasible pairs or over a rigorously characterized domain, not merely over every pair satisfying \(0<s\le t<1\) and \(s+t>1\). In particular, every actual pair \((a_i,b_i)\) is feasible because \(T_i\subseteq\mathcal R_i(a_i,b_i)\), and hence

\[
\boxed{a_i^2+a_ib_i+b_i^2<1\qquad(i=0,\ldots,5).}
\]

### 7.2 Correct monotonicity direction

**[Established] Antitone monotonicity.** If

\[
s'\ge s,
\qquad
t'\ge t,
\]

then

\[
\boxed{
\mathcal R_i(s',t')\subseteq\mathcal R_i(s,t).
}
\]

Proof: a convex triangle containing \(V_i\) and the farther point \(A_i(s')\) also contains the nearer point \(A_i(s)\) on the segment between them; the same applies to \(B_i(t)\). Thus increasing either parameter makes the admissible region smaller.

---

## 8. Distinguished parameters and the two-parameter reduction

Choose a supercritical vertex and cyclically relabel it as \(V_0\). Set

\[
\boxed{s:=a_0,\qquad t:=b_0.}
\]

Then

\[
s+t>1.
\]

Reflecting the entire configuration in the radial line \(OV_0\) interchanges the two incident sides. Hence, after reflection if necessary, one may assume

\[
\boxed{s\le t.}
\]

It was additionally proposed to choose \(V_0\) so that \(a_0+b_0\) is maximal among all \(a_i+b_i\). In terms of the cyclic \(b\)-sequence,

\[
a_0+b_0=1+(b_0-b_5),
\]

so this selects a largest adjacent increase \(b_0-b_5\).

Define the complementary parameter pair

\[
\boxed{q(s,t):=(1-t,1-s).}
\]

Because \(s+t>1\),

\[
s>1-t,
\qquad
t>1-s.
\]

Therefore antitone monotonicity gives

\[
\boxed{
\mathcal R_0(s,t)
\subseteq
\mathcal R_0(1-t,1-s).
}
\]

In set-theoretic language, the supercritical admissible region is the **smaller** region, while the complementary-parameter comparison region is the **larger** region.

### 8.1 The intended comparison for the other five vertices

The desired inclusions are

\[
\boxed{
\mathcal R_i(a_i,b_i)
\subseteq
\mathcal R_i(1-t,1-s),
\qquad i=1,\ldots,5.
}
\]

By antitone monotonicity, a sufficient coordinatewise condition is

\[
a_i\ge1-t,
\qquad
b_i\ge1-s.
\]

Since

\[
s=a_0=1-b_5,
\qquad
t=b_0,
\]

these inequalities are equivalent to

\[
b_{i-1}\le b_0,
\qquad
b_i\ge b_5.
\]

They hold for every \(i\) if

\[
\boxed{
b_5=\min_jb_j,
\qquad
b_0=\max_jb_j.
}
\]

That is: the selected global minimum must be immediately followed by the selected global maximum in the cyclic sequence.

### 8.2 The main comparison gap

**[Gap]** Choosing \(a_0+b_0\) maximal only says that \(b_0-b_5\) is a largest **adjacent increase**. It does not imply that \(b_5\) is the global minimum or that \(b_0\) is the global maximum.

Therefore the five comparison inclusions do not follow merely from maximality of \(a_0+b_0\). A complete proof needs one of the following:

1. a transition-point selection lemma forcing a global minimum immediately before a global maximum;
2. a new argument proving the coordinatewise bounds without that adjacency;
3. a finite case split according to the cyclic order of the \(b_i\);
4. a comparison region depending on more appropriate extrema;
5. or a different reduction that does not require all five nondistinguished regions to be identical.

This issue should be investigated before investing heavily in the final two-parameter optimization, because a counterexample to the comparison lemma would require redesigning the model residual core.

### 8.3 Conditional comparison lemma

The exact statement currently available is the following.

**[Conditional] Two-parameter comparison lemma.** If \(V_0\) is supercritical, \(s=a_0\), \(t=b_0\), and

\[
b_5=\min_jb_j,
\qquad
b_0=\max_jb_j,
\]

then for every \(i\ne0\),

\[
\mathcal R_i(a_i,b_i)
\subseteq
\mathcal R_i(1-t,1-s).
\]

Under these explicit extrema hypotheses, the proof is immediate from the identities above and antitone monotonicity.

---

## 9. Actual, asymmetric, and symmetric residual cores

### 9.1 Actual residual set

**[Definition]** The part of the hexagon not covered by the six actual vertex triangles is

\[
K_{\mathrm{actual}}
:=
H\setminus\bigcup_{i=0}^5T_i.
\]

Since the hypothetical seven triangles cover \(H\),

\[
K_{\mathrm{actual}}\subseteq T_O.
\]

### 9.2 Asymmetric residual core

Assuming the five comparison inclusions, define

\[
\boxed{
\mathcal C_{\mathrm{asym}}(s,t)
:=
H\setminus
\left(
\mathcal R_0(s,t)
\cup
\bigcup_{i=1}^5\mathcal R_i(1-t,1-s)
\right).
}
\]

There is one smaller supercritical region at \(V_0\) and five equal, rotated copies of the larger comparison region at the other vertices.

Because

\[
T_0\subseteq\mathcal R_0(s,t)
\]

and, conditionally,

\[
T_i\subseteq\mathcal R_i(a_i,b_i)
\subseteq\mathcal R_i(1-t,1-s)
\quad(i\ne0),
\]

one obtains

\[
\boxed{
\mathcal C_{\mathrm{asym}}(s,t)
\subseteq
K_{\mathrm{actual}}
\subseteq
T_O.
}
\]

Thus every point of the model asymmetric core is guaranteed to be left for the center triangle.

Each \(\mathcal R_i\) is open, so \(\mathcal C_{\mathrm{asym}}\) is closed in the compact hexagon \(H\), hence compact.

### 9.3 Symmetric residual core

Replace the one smaller region \(\mathcal R_0(s,t)\) by the same larger region used at the other five vertices:

\[
\boxed{
\mathcal C_{\mathrm{sym}}(s,t)
:=
H\setminus
\bigcup_{i=0}^5\mathcal R_i(1-t,1-s).
}
\]

Because

\[
\mathcal R_0(s,t)
\subseteq
\mathcal R_0(1-t,1-s),
\]

the symmetric construction removes a larger set at \(V_0\). Therefore

\[
\boxed{
\mathcal C_{\mathrm{sym}}(s,t)
\subseteq
\mathcal C_{\mathrm{asym}}(s,t).
}
\]

The symmetric core is invariant under rotation by \(60^\circ\).

**[Visual observation]** In the explored configurations, \(\mathcal C_{\mathrm{sym}}(s,t)\) appears as a small sixfold-symmetric, hexagon-like or star-like region around \(O\). Its exact topology, nonemptiness, and boundary description still require proof over the full feasible parameter domain.

---

## 10. Observed geometry of the supercritical admissible region

Only

\[
\mathcal R_0(s,t)\cap H
\]

matters for the residual-core argument.

**[Visual observation] Boundary structure.** For feasible supercritical parameters with
\[
s+t>1,
\qquad s\le t,
\]

the portion of the boundary lying in the interior of \(H\) appears, in counterclockwise order from the \(V_5\)-side toward the \(V_1\)-side, to consist of four pieces:

\[
\boxed{
\Gamma_-\ \longrightarrow\ L_-\ \longrightarrow\ L_+\ \longrightarrow\ \Gamma_+,
}
\]

where

- \(\Gamma_-\) is a circular arc closer to the incident edge \(E_5=[V_5,V_0]\);
- \(L_-\) is a straight segment on the \(V_5\)-side;
- \(L_+\) is a straight segment on the \(V_1\)-side;
- \(\Gamma_+\) is a circular arc closer to \(E_0=[V_0,V_1]\).

The two straight pieces meet at an interior corner

\[
\boxed{X=X(s,t):=L_-\cap L_+.}
\]

The full relative boundary in \(H\) also uses portions of \(E_5\) and \(E_0\).

This should not be described as “four line segments”: the observed decomposition has **two circular arcs and two straight segments**.

**Task for subsequent AIs.** Verify this boundary pattern numerically across the feasible parameter domain, including near its boundary, and then prove it analytically—or identify and prove the correct parameter-dependent alternatives if the pattern changes.

### 10.1 Required boundary-structure theorem

**[Conjecture]** On the relevant feasible domain, the observed four-piece structure is exact. A rigorous version should provide:

1. a complete characterization of \(\mathcal R_0(s,t)\cap H\);
2. formulas for the endpoints and supporting lines of \(L_-,L_+\);
3. a formula for \(X(s,t)\);
4. the centers, radii, endpoints, and angular ranges of \(\Gamma_-,\Gamma_+\);
5. a proof that no additional boundary pieces occur;
6. a list of parameter values at which pieces collapse or the combinatorial boundary type changes.

It is possible that \(s+t>1\) and \(s\le t\) are not enough to guarantee one uniform boundary type. The domain should be partitioned if phase transitions occur.

### 10.2 The points \(C,X,D\)

The visualization identified three intended asymmetric witness points:

\[
C=C(s,t)\in L_-,
\qquad
X=X(s,t),
\qquad
D=D(s,t)\in L_+.
\]

Their order along the interior boundary is

\[
\Gamma_-\longrightarrow C\longrightarrow X\longrightarrow D\longrightarrow\Gamma_+.
\]

The point \(C\) was described informally as lying on the side of \(X\) closer to \(V_5\), near—but outside—the comparison region attached to \(V_5\). The point \(D\) is the corresponding selected point on the \(V_1\)-side segment, although symmetry between \(C\) and \(D\) should not be assumed unless proved.

**[Gap]** \(C\) and \(D\) do not yet have intrinsic definitions. “A point near \(V_5\)” is not mathematically sufficient. Their definitions should come from an exact equality or intersection, for example:

- an intersection of \(L_-\) or \(L_+\) with the boundary of another admissible region;
- a support-line contact in a specified direction;
- an intersection with an explicitly defined radial or affine line;
- or the optimizer of a one-dimensional support functional along the segment.

The necessary membership statement is

\[
\boxed{
C,X,D\in\mathcal C_{\mathrm{asym}}(s,t).
}
\]

Being on \(\partial\mathcal R_0(s,t)\) only proves that a point is not in the **open** set \(\mathcal R_0(s,t)\). One must additionally prove that it lies outside all five comparison regions

\[
\mathcal R_i(1-t,1-s),
\qquad i=1,\ldots,5.
\]

This is likely why \(C\) and \(D\) must be chosen at precise contacts rather than arbitrarily on \(L_-\) and \(L_+\).

---

## 11. Symmetric radial witnesses, the witness hexagon, and the forced disk

Assume \(\mathcal C_{\mathrm{sym}}(s,t)\) is nonempty. Since it is compact, choose

\[
P=P(s,t)\in\mathcal C_{\mathrm{sym}}(s,t)
\]

with maximal radial distance from the origin:

\[
\boxed{
\rho(s,t):=|P|
=
\max_{x\in\mathcal C_{\mathrm{sym}}(s,t)}|x|.
}
\]

Rotate \(P\) through the six hexagonal symmetry angles:

\[
P_k:=\operatorname{Rot}_{k\pi/3}(P),
\qquad k=0,\ldots,5.
\]

By rotational invariance,

\[
P_k\in\mathcal C_{\mathrm{sym}}(s,t)
\subseteq\mathcal C_{\mathrm{asym}}(s,t).
\]

Define the **symmetric witness hexagon**

\[
\boxed{
\mathcal W(s,t)
:=
\operatorname{conv}\{P_0,\ldots,P_5\}.
}
\]

It is a regular hexagon centered at \(O\) with circumradius \(\rho(s,t)\). Its inscribed disk is

\[
\boxed{
\mathcal D(s,t)
:=
\{x\in\mathbb R^2:|x|\le r(s,t)\},
\qquad
r(s,t):=\frac{\sqrt3}{2}\rho(s,t).
}
\]

Call \(\mathcal D(s,t)\) the **forced central disk**.

### 11.1 Important convexity correction

It has not been proved that either

\[
\mathcal W(s,t)\subseteq\mathcal C_{\mathrm{sym}}(s,t)
\]

or

\[
\mathcal D(s,t)\subseteq\mathcal C_{\mathrm{sym}}(s,t).
\]

The symmetric residual core may be nonconvex. Fortunately, these containments are unnecessary.

Every triangle containing \(\mathcal C_{\mathrm{asym}}\) contains the six points \(P_k\). Since a triangle is convex, it must then contain their convex hull \(\mathcal W\), and hence its inscribed disk \(\mathcal D\). Therefore

\[
\boxed{
\text{every convex set containing }\mathcal C_{\mathrm{asym}}
\text{ also contains }\mathcal D(s,t).
}
\]

The disk is “forced” by convexity even if it is not a subset of the residual core itself.

### 11.2 Quantitative task for the symmetric core

**[Visual observation]** In the apparent limiting regime

\[
(s,t)\to(0,1),
\]

the symmetric core and \(\rho(s,t)\) appear to shrink toward \(O\). The radius seems to remain of a controlled order, perhaps linear in \(s\), but no constant has been proved.

The required result is an explicit lower bound such as

\[
\rho(s,t)\ge f(s,t)
\]

or

\[
r(s,t)\ge g(s,t),
\]

strong enough for the final enclosure inequality. A statement of the form

\[
r(s,t)\ge c\,s
\]

is only a heuristic placeholder until both \(c\) and its domain are proved.

It may be easier to choose an explicitly described point in the symmetric core rather than the abstract radial maximizer. Any certified point and its six rotations give a valid, possibly smaller, forced disk.

---

## 12. Equilateral enclosure width

### 12.1 Definition

For a nonempty compact set \(K\subset\mathbb R^2\), define its **equilateral enclosure width**—also called its triangular diameter in the original discussion—by

\[
\boxed{
\tau(K)
:=
\inf\left\{
\ell>0:
K\text{ is contained in a closed equilateral triangle of side }\ell
\right\}.
}
\]

Monotonicity is immediate:

\[
K\subseteq L
\quad\Longrightarrow\quad
\tau(K)\le\tau(L).
\]

More generally, if every equilateral triangle containing \(L\) is forced by convexity to contain a set \(K\), then

\[
\tau(L)\ge\tau(K).
\]

### 12.2 Support-function formula

For a compact set \(K\), define its support function by

\[
h_K(u):=\max_{x\in K}\langle x,u\rangle,
\qquad |u|=1.
\]

Let

\[
u_\theta=(\cos\theta,\sin\theta).
\]

Then

\[
\boxed{
\tau(K)
=
\frac{2}{\sqrt3}
\min_{\theta\in\mathbb R}
\left[
h_K(u_\theta)
+h_K(u_{\theta+2\pi/3})
+h_K(u_{\theta+4\pi/3})
\right].
}
\]

The three unit vectors are outward normals to the three sides of an enclosing equilateral triangle. For a fixed orientation, the tightest three supporting half-planes have offsets \(h_K\) in those directions. Since the normals sum to zero, the sum of the three offsets is translation-invariant, and multiplying it by \(2/\sqrt3\) gives the side length. Minimizing over the orientation gives the formula.

The factor \(2/\sqrt3\) is essential.

### 12.3 Why the bound \(\tau\ge1\) is enough

**[Established] Open-containment lemma.** If a compact set \(K\) is contained in an open equilateral triangle of side length \(1\), then

\[
\tau(K)<1.
\]

Proof: compactness gives positive clearance from all three sides. Moving the three sides inward by a sufficiently small equal amount produces a smaller closed equilateral triangle that still contains \(K\).

Therefore, if

\[
\tau\bigl(\mathcal C_{\mathrm{asym}}(s,t)\bigr)\ge1,
\]

then the compact asymmetric residual core cannot lie inside the seventh open unit triangle \(T_O\). This is the precise point at which openness of the covering triangles becomes decisive.

---

## 13. The finite forced-witness reduction

Assume that the following have been rigorously certified:

1. \(P_0,\ldots,P_5\in\mathcal C_{\mathrm{sym}}\subseteq\mathcal C_{\mathrm{asym}}\);
2. \(C,X,D\in\mathcal C_{\mathrm{asym}}\).

Define the **forced witness configuration**

\[
\boxed{
\mathcal Q(s,t)
:=
\mathcal D(s,t)\cup\{C(s,t),X(s,t),D(s,t)\}.
}
\]

The disk need not be a subset of the residual core. Nevertheless, every equilateral triangle containing \(\mathcal C_{\mathrm{asym}}\) contains the six rotated points, hence their convex hull, hence \(\mathcal D\); it also contains \(C,X,D\). Consequently,

\[
\boxed{
\tau\bigl(\mathcal C_{\mathrm{asym}}(s,t)\bigr)
\ge
\tau\bigl(\mathcal Q(s,t)\bigr).
}
\]

For a disk of radius \(r\) centered at \(O\),

\[
h_{\mathcal D}(u)=r.
\]

Thus

\[
h_{\mathcal Q}(u)
=
\max\left\{
r,
\langle C,u\rangle,
\langle X,u\rangle,
\langle D,u\rangle
\right\}.
\]

The final analytic inequality becomes

\[
\boxed{
\frac{2}{\sqrt3}
\min_\theta
\sum_{k=0}^2
\max\left\{
r(s,t),
\langle C,u_{\theta+2k\pi/3}\rangle,
\langle X,u_{\theta+2k\pi/3}\rangle,
\langle D,u_{\theta+2k\pi/3}\rangle
\right\}
\ge1.
}
\]

This formula makes the intended geometry precise:

- the forced disk prevents an enclosing triangle from translating too far away from the origin;
- \(C,X,D\) force outward reach in the distinguished \(V_0\)-direction;
- the goal is to prove that these simultaneous requirements force side length at least \(1\).

### Witness-set enclosure theorem

**[Conjecture]** For every feasible pair in the intended two-parameter reduction,

\[
\boxed{
\tau\bigl(\mathcal Q(s,t)\bigr)\ge1.
}
\]

The stronger expectation is

\[
\tau\bigl(\mathcal Q(s,t)\bigr)>1
\]

for all nondegenerate feasible pairs, with infimum \(1\) approached only as

\[
(s,t)\to(0,1).
\]

That limiting statement is also conjectural. Notice that \(s\to0\), together with \(s+t>1\) and \(t\le1\), forces \(t\to1\). The quantity expected to tend to \(1\) is the enclosure width \(\tau\); the forced-disk radius is expected to tend to \(0\).

---

## 14. Reconstructed proof architecture for the boundary-complete case

The intended proof can now be displayed as a chain, with the missing implications marked.

> **Instruction for subsequent agents.** Fill in every step labeled **[Missing]** below to make the proof work.

1. Assume seven open unit triangles cover \(H\).

2. By unit-distance separation, label six distinct vertex triangles \(T_0,\ldots,T_5\) and the distinct center triangle \(T_O\).

3. Enter the boundary-complete case:
   \[
   \partial H\subseteq\bigcup_{i=0}^5T_i.
   \]

4. Choose generic transition points \(A_i,B_i\), obtaining
   \[
   a_i+b_{i-1}=1
   \]
   and at least one supercritical index.

5. Choose a distinguished supercritical \(V_0\), set
   \[
   s=a_0,\qquad t=b_0,
   \]
   and reflect so that \(s\le t\).

6. **[Missing reduction]** Prove hypotheses strong enough to obtain
   \[
   \mathcal R_i(a_i,b_i)
   \subseteq
   \mathcal R_i(1-t,1-s)
   \quad(i\ne0).
   \]

7. Define the asymmetric residual core and conclude
   \[
   \mathcal C_{\mathrm{asym}}(s,t)
   \subseteq
   K_{\mathrm{actual}}
   \subseteq
   T_O.
   \]

8. Replace the small distinguished region by the larger comparison region and obtain
   \[
   \mathcal C_{\mathrm{sym}}
   \subseteq
   \mathcal C_{\mathrm{asym}}.
   \]

9. **[Missing symmetric geometry]** Produce a certified point \(P\in\mathcal C_{\mathrm{sym}}\), rotate it six times, and derive an explicit forced-disk radius \(r(s,t)\).

10. **[Missing asymmetric geometry]** Derive exact boundary formulas for \(\mathcal R_0(s,t)\), define \(C,X,D\), and prove
    \[
    C,X,D\in\mathcal C_{\mathrm{asym}}.
    \]

11. **[Missing optimization]** Prove
    \[
    \tau\left(\mathcal D(s,t)\cup\{C,X,D\}\right)\ge1.
    \]

12. It follows that
    \[
    \tau(\mathcal C_{\mathrm{asym}})\ge1.
    \]

13. But a compact set contained in the open unit triangle \(T_O\) has enclosure width strictly less than \(1\), a contradiction.

14. Therefore the boundary-complete case is impossible.

Even after this chain is completed, the one-gap and two-gap cases—and the exhaustiveness of the three cases—remain to be proved.

---

## 15. What is established, what is conditional, and what is conjectural

### 15.1 Established within this framework

1. Seven hypothetical triangles split into six distinct vertex triangles and one distinct center triangle.
2. In the boundary-complete case, only \(T_i,T_{i+1}\) can cover \(E_i\), and transition overlaps exist.
3. The identities
   \[
   a_i+b_{i-1}=1,
   \qquad
   \sum_i(a_i+b_i)=6
   \]
   hold.
4. Transition points can be chosen generically so that no \(a_i+b_i\) equals \(1\).
5. A generic cyclic configuration has both supercritical and subcritical indices.
6. The monotonicity direction is
   \[
   (s',t')\ge(s,t)
   \Longrightarrow
   \mathcal R_i(s',t')\subseteq\mathcal R_i(s,t).
   \]
7. For \(s+t>1\),
   \[
   \mathcal R_0(s,t)
   \subseteq
   \mathcal R_0(1-t,1-s).
   \]
8. Under the explicit adjacent-extrema hypothesis, the five desired comparison inclusions follow.
9. Under those inclusions,
   \[
   \mathcal C_{\mathrm{sym}}
   \subseteq
   \mathcal C_{\mathrm{asym}}
   \subseteq
   K_{\mathrm{actual}}
   \subseteq
   T_O.
   \]
10. Six rotated symmetric-core points force their convex hull and its inscribed disk into every convex enclosing triangle.
11. The stated support-function formula for \(\tau\) and the compact-open containment argument reduce the contradiction to \(\tau\ge1\).

### 15.2 Conditional statements

1. The two-parameter model correctly dominates all six actual vertex triangles only if the five nondistinguished comparison inclusions are proved.
2. The residual-core and witness argument works only if the symmetric core is nonempty and suitable witness points can be certified.
3. The finite witness reduction works only if \(C,X,D\) are proved to belong to the asymmetric core.

### 15.3 Visual observations requiring proof

1. The supercritical admissible-region boundary has the order
   \[
   \Gamma_-,L_-,L_+,\Gamma_+.
   \]
2. The symmetric residual core is a small sixfold star-like or hexagon-like region.
3. A useful radial witness exists at a controlled distance from \(O\).
4. Suitable points \(C,X,D\) appear on the two straight boundary pieces of \(\mathcal R_0(s,t)\).
5. The enclosure width appears to exceed \(1\) away from the limiting regime and approach \(1\) as \((s,t)\to(0,1)\).

### 15.4 Main conjectural lemmas and theorems

1. Exhaustiveness of the zero-gap, one-gap, and two-gap cases.
2. Supercritical radial-depth lemma: \(a_i+b_i>1\Rightarrow c_i<1/2\).
3. An unconditional two-parameter comparison lemma, or a valid replacement.
4. Exact four-piece boundary-structure theorem for \(\mathcal R_0(s,t)\cap H\).
5. Explicit symmetric-core radial lower bound.
6. Exact definitions and asymmetric-core membership of \(C,X,D\).
7. Witness-set enclosure theorem: \(\tau(\mathcal Q(s,t))\ge1\).
8. Complete arguments for the one-gap and two-gap cases.

---

## 16. Computational work that would be useful—but not itself a proof

1. **Parameter-domain exploration.** Sample feasible \((s,t)\) and detect changes in the boundary combinatorics of \(\mathcal R_0(s,t)\).
2. **Comparison stress tests.** Generate cyclic \(b_i\)-sequences and test the proposed coordinatewise bounds; retain exact rational counterexamples when possible.
3. **Envelope reconstruction.** Numerically union many admissible triangles to guess exact equations for arcs and lines.
4. **Witness extraction.** Numerically locate \(X\) and contacts with neighboring comparison regions to infer definitions of \(C,D\).
5. **Support minimization.** Plot the orientation-dependent support sum for \(\mathcal Q(s,t)\) and identify active-set patterns.
6. **Certified verification.** Once formulas are conjectured, replace floating-point plots by symbolic inequalities, rational bounds, or interval arithmetic.

Every numerical claim should record:

- the exact parameter domain sampled;
- whether open sets were approximated by closed inequalities;
- numerical tolerances;
- candidate phase boundaries;
- and any configurations close to violating the desired inequality.

---

## 17. Compact notation table

| Symbol | Meaning |
|---|---|
| \(H\) | Closed regular hexagon of side \(1\) |
| \(O\) | Center of \(H\) |
| \(V_i\) | Hexagon vertices, counterclockwise, indices mod \(6\) |
| \(E_i\) | Edge \([V_i,V_{i+1}]\) |
| \(T_i\) | Actual open unit triangle containing \(V_i\) |
| \(T_O\) | Actual open unit triangle containing \(O\) |
| \(U_V\) | Union of the six vertex triangles |
| \(S\) | Boundary portion covered by vertex triangles, \(\partial H\cap U_V\) |
| \(G\) | Boundary gaps, \(\partial H\setminus U_V\) |
| \(A_i,B_i\) | Transition points adjacent to \(V_i\), with \(B_i=A_{i+1}\) |
| \(a_i,b_i\) | Distances \(|V_iA_i|,|V_iB_i|\) |
| \(c_i\) | Radial penetration depth of \(T_i\) toward \(O\) |
| \(\mathcal R_i(s,t)\) | Union of all open unit triangles containing \(V_i,A_i(s),B_i(t)\) |
| \(s,t\) | Distinguished values \(a_0,b_0\) |
| \(q(s,t)\) | Complementary pair \((1-t,1-s)\) |
| \(K_{\mathrm{actual}}\) | Hexagon left uncovered by the six actual vertex triangles |
| \(\mathcal C_{\mathrm{asym}}\) | Model core from one smaller and five larger admissible regions |
| \(\mathcal C_{\mathrm{sym}}\) | Model core from six equal larger admissible regions |
| \(\Gamma_\pm\) | Conjectural circular boundary arcs of \(\mathcal R_0\cap H\) |
| \(L_\pm\) | Conjectural straight boundary pieces of \(\mathcal R_0\cap H\) |
| \(X\) | Conjectural meeting point \(L_-\cap L_+\) |
| \(C,D\) | Asymmetric witness points still requiring exact definitions |
| \(P_k\) | Six rotations of a symmetric-core radial witness |
| \(\mathcal W\) | Convex hull of the six \(P_k\), a regular witness hexagon |
| \(\rho\) | Circumradius of \(\mathcal W\) |
| \(\mathcal D\) | Forced central disk, the incircle of \(\mathcal W\) |
| \(r\) | Radius \((\sqrt3/2)\rho\) of \(\mathcal D\) |
| \(\mathcal Q\) | Forced configuration \(\mathcal D\cup\{C,X,D\}\) |
| \(h_K\) | Support function of a compact set \(K\) |
| \(\tau(K)\) | Minimum side length of a closed equilateral triangle containing \(K\) |
