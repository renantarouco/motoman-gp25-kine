from sympy import *

from forward_kinematics import *

init_printing()
q1, q2, q3, q4, q5, q6 = symbols('theta1:7')

fk = DHForwardKine([
  (q1, 0, 0, pi/2),
  (q2, 0, 760, 0),
  (q3, 0, 200, pi/2),
  (q4, -945, 0, -pi/2),
  (q5, 0, 0, pi/2),
  (q6, -100, 0, 0)
])
t = fk.t_matrix

print('---p---')
print(latex(fk.p()))
print('---n---')
print(latex(fk.n()))
print('---s---')
print(latex(fk.s()))
print('---a---')
print(latex(fk.a()))