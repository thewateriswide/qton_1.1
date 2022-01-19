'''
path: qton/quantum_gate/p.py
content:

  function,
      _p_
  class,
      P_gate

'''

from numpy import array, exp
from ._basic_gate_ import _Parameter_gate_


def _p_(phi):
    return array([[1, 0], [0, exp(1j * phi)]])


class P_gate(_Parameter_gate_):
    base = 'Phase'

    def _matrix_(self, parameters):
        self.matrix = _p_(parameters[0])
