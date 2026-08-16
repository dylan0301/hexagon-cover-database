import Mathlib

/-!
# Strategy 2 optimization problem statements

This file intentionally contains only the real-variable problem specifications
for Strategy 2. Every theorem is closed with `sorry`: the current milestone is
reproducible parsing and elaboration of the exact statements, not formal proofs.
No geometric bridge is formalized here.
-/

noncomputable section

namespace HexagonCover.Strategy2Optimization


open Real

structure SignedCenterInput where
  r : ℝ
  alpha : ℝ
  delta : ℝ

def w (s : SignedCenterInput) : ℝ := 1 - s.r
def centerRadical (s : SignedCenterInput) : ℝ := Real.sqrt (1 - s.r * w s)
def centerEta (s : SignedCenterInput) : ℝ := 1 - centerRadical s
def centerP (s : SignedCenterInput) : ℝ := centerRadical s * (1 - centerRadical s)
def centerK (s : SignedCenterInput) : ℝ := centerEta s + s.alpha + s.delta
def rightSurplus (s : SignedCenterInput) : ℝ := centerP s - s.alpha - w s * s.delta
def leftSurplus (s : SignedCenterInput) : ℝ := centerP s - s.r * s.alpha - s.delta

def signedCenterDomain (s : SignedCenterInput) : Prop :=
  0 < s.r ∧ s.r < 1 ∧ 0 < s.alpha ∧ 0 < s.delta ∧ 0 < rightSurplus s

def centerCE1Domain (s : SignedCenterInput) : Prop :=
  signedCenterDomain s ∧ leftSurplus s ≤ 0

def centerCE2Domain (s : SignedCenterInput) : Prop :=
  signedCenterDomain s ∧ 0 < leftSurplus s

def oneGapCE1Domain (s : SignedCenterInput) : Prop :=
  centerCE1Domain s ∧
    s.alpha < w s / 2 ∧
    s.delta < s.r / 2 ∧
    w s * s.alpha < s.r * s.delta

def lowerBreakpoint (c : ℝ) : ℝ :=
  c / 2 * (1 - Real.sqrt (4 * c^2 - 3))

def upperBreakpoint (c : ℝ) : ℝ := c - lowerBreakpoint c

def qPlusTransition (c : ℝ) : ℝ :=
  2 * c / (1 + Real.sqrt (16 * c^2 - 3))

def qMinus (c x : ℝ) : ℝ :=
  Real.sqrt (x^2 - c * x + c^2) / c - x

def discrPlus (c x : ℝ) : ℝ :=
  (2 * x * c^2 + c)^2 - 4 * (1 - c^2) * (1 - x^2) * c^2

def qPlus (c x : ℝ) : ℝ :=
  2 * (1 - x^2) * c^2 /
    (2 * x * c^2 + c + Real.sqrt (discrPlus c x))

inductive ForwardCapBranch
  | lin
  | const
  | qMinus
  | qPlus
  deriving DecidableEq, Repr

def forwardCap (c x : ℝ) : ℝ :=
  if c ≤ Real.sqrt 3 / 2 then
    if x ≤ 1 - c then 1 - x
    else if x < qPlusTransition c then qPlus c x
    else if x = qPlusTransition c then qPlusTransition c
    else if x < c then qMinus c x
    else 1 - x
  else
    if x ≤ 1 - c then 1 - x
    else if x ≤ lowerBreakpoint c then qPlus c x
    else if x < upperBreakpoint c then lowerBreakpoint c
    else if x < c then qMinus c x
    else 1 - x

def propagate (c x : ℝ) : ℝ := 1 - forwardCap c x

/-! ## S2-E1 and S2-E2 -/

def endpointSlackE1 (s : SignedCenterInput) : ℝ :=
  forwardCap (1 - s.alpha / w s) (centerK s / s.r) +
    forwardCap (1 - s.delta / s.r) (s.r - s.delta) - 1

theorem problemS2E1
    (s : SignedCenterInput)
    (hs : oneGapCE1Domain s ∨ centerCE2Domain s) :
    endpointSlackE1 s < 0 := by
  sorry

def endpointSlackE2 (s : SignedCenterInput) : ℝ :=
  forwardCap ((w s - s.alpha) / w s) (w s - s.alpha) +
    forwardCap ((s.r - s.delta) / s.r) (s.r - s.delta) - 1

theorem problemS2E2
    (s : SignedCenterInput)
    (hs : centerCE2Domain s) :
    endpointSlackE2 s < 0 := by
  sorry

/-! ## S2-R1 and S2-R2 -/

def middleRadialRequirement (s : SignedCenterInput) : ℝ :=
  min (s.alpha / s.r) (s.delta / w s)

def seedReach (s : SignedCenterInput) : ℝ := centerK s / (2 * s.r)
def afterFirstPropagation (s : SignedCenterInput) : ℝ := propagate (1 - s.alpha) (seedReach s)
def afterMiddlePropagation (s : SignedCenterInput) : ℝ := propagate (1 - middleRadialRequirement s) (afterFirstPropagation s)
def afterLastPropagation (s : SignedCenterInput) : ℝ := propagate (1 - s.delta) (afterMiddlePropagation s)
def returnSlack (s : SignedCenterInput) : ℝ := w s + s.delta - afterLastPropagation s

theorem problemS2R1
    (s : SignedCenterInput)
    (hs : oneGapCE1Domain s) :
    returnSlack s < 0 := by
  sorry

theorem problemS2R2
    (s : SignedCenterInput)
    (hs : centerCE2Domain s) :
    returnSlack s < 0 := by
  sorry

/-! ## S2-T3 -/

structure T3Input where
  center : SignedCenterInput
  tau : ℝ
  beta : ℝ

def t3Radical (x : T3Input) : ℝ :=
  Real.sqrt (1 - x.tau + x.tau^2)

def t3Q (x : T3Input) : ℝ := 1 - t3Radical x + x.beta
def t3RadialNear (x : T3Input) : ℝ := t3Q x / x.tau
def t3RadialFar (x : T3Input) : ℝ := 1 + x.beta - x.tau
def t3ForwardEnd (x : T3Input) : ℝ := t3Radical x - x.beta

def t3BackwardReq1 (x : T3Input) : ℝ :=
  let sR := centerK x.center / x.center.r
  let tR := w x.center + x.center.delta
  if t3ForwardEnd x < sR then t3Q x
  else if t3ForwardEnd x < tR then x.center.r - x.center.delta
  else t3Q x

def t3BackwardReq5 (x : T3Input) : ℝ := by
  classical
  exact
    if centerCE2Domain x.center then
      let sL := centerK x.center / w x.center
      let tL := x.center.r + x.center.alpha
      if x.beta < sL then 1 - x.beta
      else if x.beta < tL then 1 - tL
      else 1 - x.beta
    else
      1 - x.beta

def t3RadialReq1 (x : T3Input) : ℝ :=
  let gamma1 := x.center.delta / x.center.r
  if 1 - t3RadialFar x ≤ gamma1 ∧ gamma1 ≤ 1 - t3RadialNear x then
    t3RadialNear x
  else
    1 - gamma1

def t3RadialReq5 (x : T3Input) : ℝ :=
  1 - x.center.alpha / w x.center

def t3Domain (x : T3Input) : Prop :=
  (centerCE1Domain x.center ∨ centerCE2Domain x.center) ∧
    0 < x.tau ∧ x.tau < 1 ∧
    0 < x.beta ∧
    x.beta < x.tau * t3Radical x / (1 + t3Radical x) ∧
    0 < t3Q x ∧ t3Q x < 1 / 2 ∧
    0 < t3RadialNear x ∧ t3RadialNear x < t3RadialFar x ∧ t3RadialFar x < 1 ∧
    1 / 2 < t3RadialReq1 x ∧ t3RadialReq1 x < 1 ∧
    1 / 2 < t3RadialReq5 x ∧ t3RadialReq5 x < 1

def t3EndpointSlack (x : T3Input) : ℝ :=
  forwardCap (t3RadialReq5 x) (t3BackwardReq5 x) +
    forwardCap (t3RadialReq1 x) (t3BackwardReq1 x) - 1

theorem problemS2T3
    (x : T3Input)
    (hx : t3Domain x) :
    t3EndpointSlack x < 0 := by
  sorry

/-! ## S2-SC -/

def strictSupercriticalForwardSupremum (c : ℝ) : ℝ :=
  (c + Real.sqrt (c^2 - 8 * c + 4)) / 2

def adjacentSupportSlack (a c u : ℝ) : ℝ :=
  max a (a / (a + 1 - u)) + strictSupercriticalForwardSupremum c - 1

structure T3AdjacentSupportInput where
  theta : ℝ
  x : ℝ

def t3SupportRatio (v : T3AdjacentSupportInput) : ℝ :=
  (1 - 2 * v.theta) / (1 - v.theta^2)

def t3SupportLowerBound (v : T3AdjacentSupportInput) : ℝ :=
  (1 - 4 * v.theta + v.theta^2) / (2 * (1 - 2 * v.theta))

def t3SupportBackward (v : T3AdjacentSupportInput) : ℝ := v.x * t3SupportRatio v
def t3SupportRadial (v : T3AdjacentSupportInput) : ℝ := v.x + v.theta
def t3SupportEndpoint (v : T3AdjacentSupportInput) : ℝ :=
  1 - t3SupportRatio v + t3SupportBackward v

def t3AdjacentSupportDomain (v : T3AdjacentSupportInput) : Prop :=
  0 ≤ v.theta ∧ v.theta ≤ 2 - Real.sqrt 3 ∧
    t3SupportLowerBound v ≤ v.x ∧ v.x ≤ 1 / 2 - v.theta ∧
    0 < t3SupportBackward v ∧
    0 ≤ t3SupportRadial v ∧ t3SupportRadial v ≤ 1 / 2 ∧
    1 / 2 ≤ t3SupportEndpoint v ∧ t3SupportEndpoint v < 1

theorem problemS2SCT
    (v : T3AdjacentSupportInput)
    (hv : t3AdjacentSupportDomain v) :
    adjacentSupportSlack (t3SupportBackward v) (t3SupportRadial v) (t3SupportEndpoint v) ≤ 0 := by
  sorry

structure Vd1AdjacentSupportInput where
  t : ℝ
  a : ℝ
  b : ℝ

def cornerRadical (t : ℝ) : ℝ := Real.sqrt (t^2 + t + 1)
def vd1SupportRadial (v : Vd1AdjacentSupportInput) : ℝ :=
  v.t * (1 - v.b) / (v.t + 1)
def vd1SupportEndpoint (v : Vd1AdjacentSupportInput) : ℝ :=
  (cornerRadical v.t - v.a - v.t * v.b - 1) / v.t

def vd1AdjacentSupportDomain (v : Vd1AdjacentSupportInput) : Prop :=
  1 ≤ v.t ∧
    0 < v.a ∧ v.a < 1 ∧
    0 < v.b ∧ v.b < 1 ∧
    0 ≤ vd1SupportRadial v ∧ vd1SupportRadial v ≤ 1 / 2 ∧
    vd1SupportRadial v < vd1SupportEndpoint v ∧ vd1SupportEndpoint v < 1 ∧
    v.a + v.t * v.b ≤ cornerRadical v.t - 1 - v.t / 2 ∧
    cornerRadical v.t - v.a - v.t * v.b - v.t ≤ (1 - v.a) / (v.t + 1)

theorem problemS2SCV
    (v : Vd1AdjacentSupportInput)
    (hv : vd1AdjacentSupportDomain v) :
    adjacentSupportSlack v.a (vd1SupportRadial v) (vd1SupportEndpoint v) ≤ 0 := by
  sorry

/-! ## S2-VD -/

def traceComponentEnd (L U x : ℝ) : ℝ :=
  if x < L then x else if x ≤ U then U else x

def residualLowerBound (L U x : ℝ) : ℝ := 1 - traceComponentEnd L U x

structure VdAdjacentInput where
  center : SignedCenterInput
  p0 : ℝ
  q0 : ℝ
  t : ℝ
  p1 : ℝ
  q1 : ℝ

def vdAdjRightRequirement (v : VdAdjacentInput) : ℝ :=
  residualLowerBound (centerK v.center / v.center.r) (w v.center + v.center.delta) v.q0

def vdAdjLeftRequirement (v : VdAdjacentInput) : ℝ :=
  residualLowerBound (centerK v.center / w v.center) (v.center.r + v.center.alpha) v.p0

def vdAdjSupportStart (v : VdAdjacentInput) : ℝ :=
  v.t * (1 - v.q1) / (v.t + 1)

def vdAdjSupportEnd (v : VdAdjacentInput) : ℝ :=
  (cornerRadical v.t - v.p1 - v.t * v.q1 - 1) / v.t

def vdAdjBaseDomain (v : VdAdjacentInput) : Prop :=
  centerCE2Domain v.center ∧
    0 < v.p0 ∧ v.p0 < 1 ∧
    0 < v.q0 ∧ v.q0 < 1 ∧
    1 < v.p0 + v.q0 ∧
    v.p0^2 + v.p0 * v.q0 + v.q0^2 ≤ 1 ∧
    0 < vdAdjLeftRequirement v ∧ 0 ≤ vdAdjRightRequirement v ∧ vdAdjRightRequirement v + vdAdjLeftRequirement v < 1 / 2 ∧
    v.center.alpha + v.center.delta < 1 / 24 ∧
    v.center.alpha + v.center.delta < min v.center.r (w v.center) / 6 ∧
    0 < v.t ∧
    0 < v.p1 ∧ v.p1 < 1 ∧
    0 < v.q1 ∧ v.q1 < 1 ∧
    vdAdjRightRequirement v ≤ v.p1 ∧ vdAdjLeftRequirement v ≤ v.q1 ∧
    v.p1 + v.q1 < 1 / 2

def vdAdjSupportDomain (v : VdAdjacentInput) : Prop :=
  vdAdjBaseDomain v ∧
    0 ≤ vdAdjSupportStart v ∧ vdAdjSupportStart v < vdAdjSupportEnd v ∧ vdAdjSupportEnd v ≤ 1

def vdAdjNoSupportDomain (v : VdAdjacentInput) : Prop :=
  vdAdjBaseDomain v ∧ vdAdjSupportEnd v ≤ vdAdjSupportStart v

def vdAdjSupportSlack (v : VdAdjacentInput) : ℝ :=
  max (v.center.delta - vdAdjLeftRequirement v / 4) (vdAdjSupportEnd v - 1 + v.center.delta)

def vdAdjNoSupportSlack (v : VdAdjacentInput) : ℝ :=
  v.center.delta - vdAdjLeftRequirement v / 4

theorem problemS2VDAdjacentSupport
    (v : VdAdjacentInput)
    (hv : vdAdjSupportDomain v) :
    vdAdjSupportSlack v < 0 := by
  sorry

theorem problemS2VDAdjacentNoSupport
    (v : VdAdjacentInput)
    (hv : vdAdjNoSupportDomain v) :
    vdAdjNoSupportSlack v < 0 := by
  sorry

inductive VdPosition
  | pos2
  | pos3
  | pos4
  deriving DecidableEq, Repr

structure VdNonadjacentInput where
  center : SignedCenterInput
  p0 : ℝ
  q0 : ℝ
  t : ℝ
  pv : ℝ
  qv : ℝ
  position : VdPosition

def vdNonRightRequirement (v : VdNonadjacentInput) : ℝ :=
  residualLowerBound (centerK v.center / v.center.r) (w v.center + v.center.delta) v.q0

def vdNonLeftRequirement (v : VdNonadjacentInput) : ℝ :=
  residualLowerBound (centerK v.center / w v.center) (v.center.r + v.center.alpha) v.p0

def vdNonLeftTraceEnd (v : VdNonadjacentInput) : ℝ := centerK v.center / w v.center
def vdNonRightTraceEnd (v : VdNonadjacentInput) : ℝ := centerK v.center / v.center.r

def vdNonCornerRadialReach (v : VdNonadjacentInput) : ℝ :=
  (cornerRadical v.t - v.pv - v.t * v.qv) / (v.t + 1)

def vdNonCenterExit (v : VdNonadjacentInput) : ℝ :=
  match v.position with
  | .pos2 => v.center.delta
  | .pos3 => min (v.center.alpha / v.center.r) (v.center.delta / w v.center)
  | .pos4 => v.center.alpha

def vdNonDomain (v : VdNonadjacentInput) : Prop :=
  centerCE2Domain v.center ∧
    0 < v.p0 ∧ v.p0 < 1 ∧
    0 < v.q0 ∧ v.q0 < 1 ∧
    1 < v.p0 + v.q0 ∧
    v.p0^2 + v.p0 * v.q0 + v.q0^2 ≤ 1 ∧
    0 < vdNonRightRequirement v ∧ 0 < vdNonLeftRequirement v ∧ vdNonRightRequirement v + vdNonLeftRequirement v < 1 / 2 ∧
    v.center.alpha + v.center.delta < vdNonLeftTraceEnd v / 2 ∧
    v.center.alpha + v.center.delta < vdNonRightTraceEnd v / 2 ∧
    vdNonLeftTraceEnd v ^ 2 + vdNonLeftTraceEnd v * (w v.center + v.center.delta) +
        (w v.center + v.center.delta) ^ 2 ≤ 1 ∧
    vdNonRightTraceEnd v ^ 2 + vdNonRightTraceEnd v * (v.center.r + v.center.alpha) +
        (v.center.r + v.center.alpha) ^ 2 ≤ 1 ∧
    0 < v.t ∧
    0 < v.pv ∧ v.pv < 1 ∧
    0 < v.qv ∧ v.qv < 1 ∧
    vdNonRightRequirement v ≤ v.pv ∧ vdNonLeftRequirement v ≤ v.qv ∧
    0 ≤ vdNonCornerRadialReach v ∧ vdNonCornerRadialReach v ≤ 1

def vdNonadjacentSlack (v : VdNonadjacentInput) : ℝ :=
  let sigma := v.center.alpha + v.center.delta
  let m := min (vdNonRightRequirement v) (vdNonLeftRequirement v)
  max (max (sigma - vdNonRightRequirement v) (sigma - vdNonLeftRequirement v))
    (max (vdNonCenterExit v - m) (vdNonCornerRadialReach v - 1 + m))

theorem problemS2VDNonadjacent
    (v : VdNonadjacentInput)
    (hv : vdNonDomain v) :
    vdNonadjacentSlack v < 0 := by
  sorry

end HexagonCover.Strategy2Optimization
