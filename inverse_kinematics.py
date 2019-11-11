from sympy import *
from forward_kinematics import *

# Given the orientation of the wrist

r1, r2, r3, r4, r5, r6, r7, r8, r9 = symbols('r1:10')

R = Matrix([
    [r1, r2, r3],
    [r4, r5, r6],
    [r7, r8, r9]
])

# Given the signal of the angle theta5
# True = + and False = -

sigq5 = True

# Given the end-effector position

px, py, pz = symbols('px, py, pz')

PW = Matrix([
    [px],
    [py],
    [pz],
    [1]  # 0 or 1 ?
])

# Find q4, q5 and q6

if sigq5:
    q4 = atan2(R[2], R[5])
    q5 = atan2(sqrt(R[2]**2 + R[5]**2), R[8])
    q6 = atan2(R[7], -R[6])
else:
    q4 = atan2(-R[2], -R[5])
    q5 = atan2(-sqrt(R[2]**2 + R[5]**2), R[8])
    q6 = atan2(-R[7], R[6])

# Applie the forward kinematics to find the position of the third joint

FK46 = FW4 * FW5 * FW6
PA = FK46.inv() * PW

# Find q1, q2 and q3

