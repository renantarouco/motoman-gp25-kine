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
fk46 = DHForwardKine(dh[3:])
t46 = fk46.t_matrix

angles = inverse(dh, t46, R, P)
print('Done.')
#pprint(angles)


# Dynamics
print('INIT DYNAMICS')
partials = []
for i in range(1, 7):
  partials.append(fk.link_transformation(i))

MASS = Matrix([[5.0],
               [3.6],
               [2.4],
               [2.8],
               [3],
               [0.7]])

Ixx1 = 0.00455; Ixy1 =  0.00000; Ixz1 = 0.00000; Iyy1 = 0.00454; Iyz1 = 0.00001; Izz1 = 0.00029
Ixx2 = 0.00032; Ixy2 =  0.00000; Ixz2 = 0.00000; Iyy2 = 0.00010; Iyz2 = 0.00000; Izz2 = 0.00042
Ixx3 = 0.00223; Ixy3 = -0.00005; Ixz3 = 0.00007; Iyy3 = 0.00219; Iyz3 = 0.00007; Izz3 = 0.00073

I1 = Matrix([[Ixx1, -Ixy1, -Ixz1],
             [-Ixy1, Iyy1, -Iyz1],
             [-Ixz1, -Iyz1, Izz1],])
I2 = Matrix([[Ixx2, -Ixy2, -Ixz2],
             [-Ixy2, Iyy2, -Iyz2],
             [-Ixz2, -Iyz2, Izz2],])
I3 = Matrix([[Ixx3, -Ixy3, -Ixz3],
             [-Ixy3, Iyy3, -Iyz3],
             [-Ixz3, -Iyz3, Izz3],])

Q = Matrix([[q1],
                   [q2],
                   [q3],
                   [q4],
                   [q5],
                   [q6]])

T = dynamics(partials, MASS, (I1, I2, I3), Q, t)

pprint(T)

print('Done.')