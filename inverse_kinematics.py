from sympy import *
from gp25 import *

def inverse(dh, FK46, R, P):
    # Find q4, q5 and q6 by the orientation of the wrist

    q4 = [atan2(R[2], R[5]), atan2(-R[2], -R[5])]
    q5 = [atan2(sqrt(R[2]**2 + R[5]**2), R[8]), atan2(-sqrt(R[2]**2 + R[5]**2), R[8])]
    q6 = [atan2(R[7], -R[6]), atan2(-R[7], R[6])]

    # Applie the forward kinematics to find the position of the third joint

    PW = FK46.inv() * P

    # Find q1, q2 and q3 by the position of the wrist

    a2 = dh[1][2]
    a3 = dh[2][2]

    c3 = (PW[0]**2 + PW[1]**2 + PW[2]**2 - a2**2 - a3**2) / (2 * a2 * a3)
    s3 = sqrt(1-c3)
    q3 = [atan2(s3,c3), -atan2(s3,c3)]

    # +s3
    s21 = (a2 + a3*c3)*PW[2] - a3*s3*sqrt(PW[0]**2 + PW[1]**2)
    s22 = (a2 + a3*c3)*PW[2] + a3*s3*sqrt(PW[0]**2 + PW[1]**2)
    c21 = (a2+a3*c3)*sqrt(PW[0]**2 + PW[1]**2) + a3*s3*PW[2]
    c22 = -(a2+a3*c3)*sqrt(PW[0]**2 + PW[1]**2) + a3*s3*PW[2]
    q2 = [atan2(s21,c21), atan2(s22,c22)]

    # -s3
    s3 = -s3
    s21 = (a2 + a3*c3)*PW[2] - a3*s3*sqrt(PW[0]**2 + PW[1]**2)
    s22 = (a2 + a3*c3)*PW[2] + a3*s3*sqrt(PW[0]**2 + PW[1]**2)
    c21 = (a2+a3*c3)*sqrt(PW[0]**2 + PW[1]**2) + a3*s3*PW[2]
    c22 = -(a2+a3*c3)*sqrt(PW[0]**2 + PW[1]**2) + a3*s3*PW[2]
    q2.append(atan2(s21,c21))
    q2.append(atan2(s22,c22))

    q1 = [atan2(PW[1], PW[0]), atan2(-PW[1], -PW[0])]

    return q1, q2, q3, q4, q5, q6