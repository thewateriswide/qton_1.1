'''
path: qton/quantum_gate/rz.py
content:

  function,
      _rz_
  class,
      Rz_gate

'''

from numpy import array, exp
from ._basic_gate_ import _Parameter_gate_


def _rz_(theta):
    t = theta * 0.5
    return array([
        [exp(-1j * t), 0],
        [0, exp(1j * t)],
    ])


class Rz_gate(_Parameter_gate_):
    base = 'Rotation-Z'

    def _matrix_(self, parameters):
        self.matrix = _rz_(parameters[0])
