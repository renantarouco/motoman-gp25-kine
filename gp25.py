from sympy import *

from forward_kinematics import *

init_printing()
q1, q2, q3, q4, q5, q6 = symbols('theta1:7')

fk = DHForwardKine([
  (q1, 505, 0, pi/2),
  (q2, 0, 150, 0),
  (q3, 0, 0, pi/2),
  (q4, 760, 0, -pi/2),
  (q5, 0, 0, pi/2),
  (q6, 795, 0, 0)
])

t = fk.tranformation_matrix()

f1 = fk.link_transformation(1)
f2 = fk.link_transformation(2)
