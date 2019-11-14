from functools import reduce

from sympy import *

IDENTITY = Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
  ])

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

def forward(link):
  theta, d, a, alpha = link
  return Rz(theta) * Tz(d)  * Tx(a) * Rx(alpha)

def dh_t(dh):
  dh_matrixes = [forward(link) for link in dh]
  return reduce(lambda x, y:  x * y, dh_matrixes)
