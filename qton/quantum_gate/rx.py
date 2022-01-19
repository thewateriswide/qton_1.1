'''
path: qton/quantum_gate/rx.py
content:

  function,
      _rx_
  class,
      Rx_gate

'''

from numpy import array, sin, cos
from ._basic_gate_ import _Parameter_gate_


def _rx_(theta):
    t = theta * 0.5
    return array([
        [cos(t), -1j * sin(t)],
        [-1j * sin(t), cos(t)],
    ])


class Rx_gate(_Parameter_gate_):
    base = 'Rotation-X'

    def _matrix_(self, parameters):
        self.matrix = _rx_(parameters[0])
