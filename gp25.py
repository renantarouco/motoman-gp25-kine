from sympy import *

from forward_kinematics import *

from inverse_kinematics import * 

from dynamics import *


init_printing()
t = Symbol('t')
q1, q2, q3, q4, q5, q6 = (Function('theta'+str(i))(t) for i in range(1, 7))

dh = [
  (q1, 0, 0, pi/2),
  (q2, 0, 760, 0),
  (q3, 0, 200, pi/2),
  (q4, -945, 0, -pi/2),
  (q5, 0, 0, pi/2),
  (q6, -100, 0, 0)
]

print('INIT FOWARD KINEMATICS')

fk = DHForwardKine(dh)
transform = fk.t_matrix

# print('---p---')
# print(latex(fk.p()))
# print('---n---')
# print(latex(fk.n()))
# print('---s---')
# print(latex(fk.s()))
# print('---a---')
# print(latex(fk.a()))

print('Done.')

print('INIT INVERSE KINEMATICS')
# Inverse kinematics

# Rotation Matrix
r1, r2, r3, r4, r5, r6, r7, r8, r9 = symbols("r1:10")
R = Matrix([
  [r1, r2, r3],
  [r4, r5, r6],
  [r7, r8, r9]
])

# Position
x, y, z = symbols("x, y, z")
P = Matrix([
  [x],
  [y],
  [z],
  [1]
])

# Matrix of transformation from joint 4 to joint 6
t46 = fk.link_transformation(4) * fk.link_transformation(5) * fk.link_transformation(6)

angles = inverse(dh, t46, R, P)

for i, joint  in enumerate(reversed(angles)):
  for j, solution in enumerate(joint):
    print("q" + str(len(angles)-i) + str(j+1) + " =")
    pprint(solution)

print('Done.')
#pprint(angles)

'''
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

Q = Matrix([[q1],
                   [q2],
                   [q3],
                   [q4],
                   [q5],
                   [q6]])

T = dynamics(partials, MASS, INERTIAL, Q, t)

pprint(T)

print('Done.')
'''