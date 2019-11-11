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

signal = True

# Find q4, q5 and q6

if signal:
    q4 = atan2(R[2], R[5])
    q5 = atan2(sqrt(R[2]**2 + R[5]**2), R[8])
    q6 = atan2(R[7], -R[6])
else:
    q4 = atan2(-R[2], -R[5])
    q5 = atan2(-sqrt(R[2]**2 + R[5]**2), R[8])
    q6 = atan2(-R[7], R[6])