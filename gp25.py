from sympy import *

from forward_kinematics import *

from inverse_kinematics import * 

from dynamics import *


init_printing()
t = Symbol('t')
q1, q2, q3, q4, q5, q6 = (Function('theta'+str(i))(t) for i in range(1, 7))
#q1, q2, q3, q4, q5, q6 = functions('theta1:7')(t)
#pprint(q1)
#pprint(q2)

dh = [
  (q1, 0, 0, pi/2),
  (q2, 0, 760, 0),
  (q3, 0, 200, pi/2),
  (q4, -945, 0, -pi/2),
  (q5, 0, 0, pi/2),
  (q6, -100, 0, 0)
]

fk = DHForwardKine(dh)
#t = fk.t_matrix

# print('---p---')
# print(latex(fk.p()))
# print('---n---')
# print(latex(fk.n()))
# print('---s---')
# print(latex(fk.s()))
# print('---a---')
# print(latex(fk.a()))

# # Inverse kinematics

# # Rotation Matrix
# r1, r2, r3, r4, r5, r6, r7, r8, r9 = symbols("r1:10")
# R = Matrix([
#   [r1, r2, r3],
#   [r4, r5, r6],
#   [r7, r8, r9]
# ])

# # Position
# x, y, z = symbols("x, y, z")
# P = Matrix([
#   [x],
#   [y],
#   [z],
#   [1]
# ])

# # Matrix of transformation from joint 4 to joint 6
# fk46 = DHForwardKine(dh[3:])
# t46 = fk46.t_matrix

# q1, q2, q3, q4, q5, q6 = inverse(dh, t46, R, P)


# Dynamics
print('INIT DYNAMICS')
partials = []
for i in range(1, 7):
  partials.append(fk.link_transformation(i))
MASS = Matrix([[1.2],
            [2],
            [1],
            [0.5],
            [1],
            [0.7]])

INERTIAL = Matrix([[1.2],
            [2],
            [1],
            [0.5],
            [1],
            [0.7]])


P = calculateLinksPosition(partials)

U = calculatePotentialEnergy(P, MASS)

J = calculateJacobian(partials)

V, W = calculateLinksVelocity(P, J, (q1,q2,q3,q4,q5,q6), t)

K = calculateKineticEnergy(V, W, MASS, INERTIAL)
pprint(K)
#V = diff(P, q1)
#pprint(J)