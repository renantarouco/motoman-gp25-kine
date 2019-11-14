from functools import reduce

from sympy import *

class DHForwardKine:
  def __init__(self, dh_table):
    self.dh_table = dh_table
    self.link_matrixes = [self.forward_link(link) for link in self.dh_table]
    #self.t_matrix = trigsimp(simplify(reduce(lambda x, y:  x * y, self.link_matrixes)))

  def rz(self, theta):
    return Matrix([
      [cos(theta), -sin(theta), 0, 0],
      [sin(theta), cos(theta), 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1]
    ])

  def tz(self, d):
    return Matrix([
      [1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, d],
      [0, 0, 0, 1],
    ])

  def tx(self, a):
    return Matrix([
      [1, 0, 0, a],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 0, 0, 1],
    ])

  def rx(self, alpha):
    return Matrix([
      [1, 0, 0, 0],
      [0, cos(alpha), -sin(alpha), 0],
      [0, sin(alpha), cos(alpha), 0 ],
      [0, 0, 0, 1]
    ])

  def forward_link(self, link):
    theta, d, a, alpha = link
    return simplify(self.rz(theta) * self.tz(d)  * self.tx(a) * self.rx(alpha))

  def link_transformation(self, link_id):
    if link_id == 0 or link_id > len(self.link_matrixes):
      return None
    return self.link_matrixes[link_id - 1]
  
  def p(self):
    return self.t_matrix.col(-1).row_del(-1)

  def n(self):
    return self.t_matrix.col(0).row_del(-1)

  def s(self):
    return self.t_matrix.col(1).row_del(-1)
  
  def a(self):
    return self.t_matrix.col(2).row_del(-1)
