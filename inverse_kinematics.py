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
PW3 = FK46.inv() * PW

# Find the forward kinematics to transform from base to joint 3

T01 = Rz(q1) * Rx(pi/2)
T12 = Rz(q2) * Tx(760)
T23 = Rz(q3) * Tx(200)

FK03 = T01 * T12 * T23

P = Matrix([
    [FK03[3]],
    [FK03[7]],
    [FK03[11]],
    [FK03[15]]
])
