'''
path: qton/quantum_gate/ry.py
content:

  function,
      _ry_
  class,
      Ry_gate

'''

from numpy import array, sin, cos
from ._basic_gate_ import _Parameter_gate_


def _ry_(theta):
    t = theta * 0.5
    return array([
        [cos(t), -sin(t)],
        [sin(t), cos(t)],
    ])


class Ry_gate(_Parameter_gate_):
    base = 'Rotation-Y'

    def _matrix_(self, parameters):
        self.matrix = _ry_(parameters[0])
