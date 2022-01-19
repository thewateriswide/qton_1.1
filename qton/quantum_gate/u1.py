'''
path: qton/quantum_gate/u1.py
content:

  function,
      _u1_
  class,
      U1_gate

'''

from numpy import array, exp
from ._basic_gate_ import _Parameter_gate_


def _u1_(lamda):
    return array([[1, 0], [0, exp(1j * lamda)]])


class U1_gate(_Parameter_gate_):
    base = 'U1-gate'

    def _matrix_(self, parameters):
        self.matrix = _u1_(parameters[0])
