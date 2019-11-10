from sympy import *

init_printing()
q1, q2, q3, q4, q5, q6 = symbols('theta1:7')


def Rz(theta):
  return Matrix([
    [cos(theta), -sin(theta), 0, 0],
    [sin(theta), cos(theta), 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
  ])

def Tz(d):
  return Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, d],
    [0, 0, 0, 1],
  ])

def Tx(a):
  return Matrix([
    [1, 0, 0, a],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
  ])

def Rx(alpha):
  return Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, cos(alpha), -sin(alpha)],
    [0, 0, sin(alpha), cos(alpha)]
  ])

FW1 = Rz(q1) * Tz(505) * Rx(pi/2)
FW2 = Rz(q2)
FW3 = Rz(q3) * Tx(960) * Rx(pi/2)
FW4 = Rz(q4) * Tz(-795) * Rx(pi/2)
FW5 = Rz(q5) * Rx(-(pi/2))
FW6 = Rz(q6) * Tz(-100) * Rx(pi)

FK = FW1 * FW2 * FW3 * FW4 * FW5 * FW6
