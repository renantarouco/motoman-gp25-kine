from sympy import *
from dynamics import *

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
    [0, cos(alpha), -sin(alpha), 0],
    [0, sin(alpha), cos(alpha), 0 ],
    [0, 0, 0, 1]
  ])

FW1 = Rz(q1) * Tz(505) * Rx(pi/2)
FW2 = Rz(q2) * Tx(150)
FW3 = Rz(q3) * Rx(pi/2)
FW4 = Rz(q4) * Tz(760) * Rx(-(pi/2))
FW5 = Rz(q5) * Rx(pi/2)
FW6 = Rz(q6) * Tz(795)

FK = FW1 * FW2 * FW3 * FW4 * FW5 * FW6

transforms = [FW1, FW2, FW3, FW4, FW5, FW6]

M = Matrix([[1.2],
            [2],
            [1],
            [0.5],
            [1],
            [0.7]])

P = calculateLinksCenterMass(transforms)
J = calculateJacobian(transforms)
U = calculatePotentialEnergy(P, M)
pprint(U)

