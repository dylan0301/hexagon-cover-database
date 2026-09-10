#!/usr/bin/env python3
"""Targeted order/type contracts and exact algebra; not full formalization."""
from pathlib import Path
import re
import sympy as s
ROOT=Path(__file__).resolve().parents[3];PAPER=ROOT/'arrange/paper_draft'
def expand(path):
 text=re.sub(r'(?m)(?<!\\)%.*$','',path.read_text())
 def inc(m):
  q=Path(m.group(1));q=q if q.suffix else q.with_suffix('.tex')
  return expand(next(x for x in (path.parent/q,PAPER/q) if x.is_file()))
 return re.sub(r'\\input\{([^}]+)\}',inc,text)
full=expand(PAPER/'main.tex');checks=[]
def check(name,yes):
 assert yes,name
 checks.append(name)
for a,b in [
 ('eq:enclosure-definition','lem:compact-cover-margin'),
 ('eq:diameter-envelope-definition','lem:shared-gap-anchor-transfer'),
 ('eq:supercritical-envelope-definition','thm:fixed-four-point-rescuer'),
 ('lem:new-common-pair-domination','lem:fixed-total-radial-forcing'),
 ('thm:fixed-four-point-rescuer','tab:finite-enclosure-subcases'),
 ('eq:reader-witness-set','tab:finite-enclosure-subcases'),
 ('lem:shared-corner-chart','lem:app-vd0-trace-normalization-calculation'),
 ('eq:orientation-type-II','lem:app-t3-translation-calculation'),
 ('lem:support-cell-rotation','prop:new-disk-finite-caliper'),
 ('prop:vd-corner-normal-form','lem:app-supercritical-skeleton-calculation'),
 ('lem:vd1-forward-orientation','prop:appendix-vd1-two-chart-replacement'),
 ('prop:new-four-direct-outputs','lem:new-selected-chords'),
 ('eq:selected-low-root','lem:ce1-first-return-step'),
 ('lem:new-selected-chords','lem:ce1-first-return-step'),
 ('lem:ce1-first-return-step','eq:fixed-ce1-third-demand'),
 ('eq:ce1-second-chord','fig:ce1-reverse-path'),
 ('eq:four-contact-residuals','fig:zero-gap-four-contacts')]:
 check(a+' before '+b,full.index('\\label{'+a+'}')<full.index('\\label{'+b+'}'))
main=(PAPER/'main.tex').read_text()
for typ in ('lemma','proposition','corollary','definition','remark'):
 check('reference type '+typ,'\\newaliascnt{'+typ+'}{theorem}' in main and '\\aliascntresetthe{'+typ+'}' in main)
E=(PAPER/'E_zero_gap_nine_point_optimization.tex').read_text()
check('origins separate','O_{\\rm loc}' in E)
check('Newton global','B&=\\Psi_4(J)' in E)
check('Newton rescaling first',E.index('\\widetilde g_-(x)=g_-(hx)')<E.index('\\widehat\\xi_-='))
check('actual handoff function','$X_5=Z_5' not in E and 'X_5(\\xi_5)' in E)
B=(PAPER/'fixed_witness/06_fixed_witness_body.tex').read_text()
check('table after construction','\\begin{longtable}' not in B)
check('rescuer endpoint first',B.index('P_T=\\varepsilon V_1')<B.index('fe08_t3_rescuer'))
F=(PAPER/'A_zero_gap_exact_certificate.tex').read_text()
check('Bernstein first',F.index('Bernstein basis polynomial')<F.index('global tensor Bernstein expansions'))
check('electronic appendix named','electronic appendix at an immutable revision' in F)
print(f'editorial reading-order/reference contracts: {len(checks)} PASS')
identities=[]
def zero(name,v):
 assert s.simplify(v)==0,name
 identities.append(name)
def positive(name,v):
 v=s.simplify(v);assert v.is_positive is True,(name,v)
 identities.append(name)
m,M,c,x,t,th,a,al=s.symbols('m M c x t th a al',real=True)
z=s.sqrt(1-t+t*t);Fs=(m*m-1)*c*c+(2*m*M*M+M)*c+M**4-M*M
zero('envelope factor',Fs.subs(m,1-M)-M*(c-M)*(1-2*c+c*M-M*M))
zero('envelope derivative',s.diff(Fs,m)-2*c*(M*M+c*m))
zero('actual endpoint',(1+al+a-z)/(1-t)-(a/(1-t)+t/(1+z)+al/(1-t)))
zero('actual size',a+(1-a-t)-(1-t))
zero('own midpoint',t*(1-t)-2*(z-z*z)-(1-z)**2)
tth=th*(2-th)/(1-th*th);low=(1-4*th+th*th)/(2*(1-2*th))
zero('midpoint lower endpoint',(s.Rational(1,2)-tth)/(1-tth)-low)
Q=2*x*x+(th-1)*x+th
zero('quadratic lower endpoint',Q.subs(x,low)-th*(1-5*th+11*th**2-th**3)/(2*(1-2*th)**2))
zero('quadratic vertex',low-(1-th)/4-(1-5*th)/(4*(1-2*th)))
zero('quadratic minimum',Q.subs(x,(1-th)/4)-(10*th-1-th*th)/8)
zero('actual ratio',(x*x+(c-2)*x+c).subs(c,x+th+al/(1-t))-Q-al*(x+1)/(1-t))
zero('Vd1 opposite support',1-t/2-1/(t+1)-t*(1-t)/(2*(t+1)))
vc=20*c*c+(18*s.sqrt(3)-52)*c+47-24*s.sqrt(3)
zero('Vd1 squaring',(12-4*s.sqrt(3)-9*c)**2-(c*c-8*c+4)-4*vc)
positive('Vd1 endpoint',vc.subs(c,s.Rational(1,2)))
positive('Vd1 decreasing',-s.diff(vc,c).subs(c,s.Rational(1,2)))
positive('Vd1 unsquared sign',s.Rational(15,2)-4*s.sqrt(3))
e=s.symbols('e',real=True);q=e+(1-e)*x;p=q-1+s.sqrt(1-x+x*x)
zero('chord equation',x*(1-x)-(q-p)*(2-q+p))
zero('chord convex parameter',s.diff(p,x,2)-3/(4*(1-x+x*x)**s.Rational(3,2)))
zero('chord lower range',(1-5*e)*(7-16*e)-2-(80*e*e-51*e+5))
positive('chord endpoint',-(80*e*e-51*e+5).subs(e,s.Rational(1,8)))
positive('chord upper bound',49*6-17**2)
v={t:s.Rational(7,10),a:s.Rational(1,200),al:s.Rational(1,1000)}
ce=((1+al+a-z)/(1-t)).subs(v);ue=(a+t).subs(v)
positive('example near positive',ce)
positive('example near before midpoint',s.Rational(1,2)-ce)
positive('example far beyond midpoint',ue-s.Rational(1,2))
positive('example far below one',1-ue)
zero('example translation error',ce-(a/(1-t)+t/(1+z)).subs(v)-s.Rational(1,300))
positive('example larger theta',(t/(1+z)).subs(v)-(2-s.sqrt(3)))
print(f'editorial local algebra/sign regressions: {len(identities)} PASS')
