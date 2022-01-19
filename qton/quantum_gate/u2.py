'''
path: qton/quantum_gate/u2.py
content:

  function,
      _u2_
  class,
      U2_gate

'''

from numpy import array, sqrt, exp
from ._basic_gate_ import _Parameter_gate_


def _u2_(phi, lamda):
    return array([[1, -exp(1j * lamda)],
                  [exp(1j * phi), exp(1j * lamda + 1j * phi)]]) * sqrt(0.5)


class U2_gate(_Parameter_gate_):
    base = 'U2-gate'

    def _matrix_(self, parameters):
        self.matrix = _u2_(*parameters[0:2])
