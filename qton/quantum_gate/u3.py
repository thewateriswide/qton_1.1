'''
path: qton/quantum_gate/u3.py
content:

  function,
      _u3_
  class,
      U3_gate

'''

from numpy import array, cos, sin, exp
from ._basic_gate_ import _Parameter_gate_


def _u3_(theta, phi, lamda):
    t = theta * 0.5
    return array(
        [[cos(t), -exp(1j * lamda) * sin(t)],
         [exp(1j * phi) * sin(t),
          exp(1j * lamda + 1j * phi) * cos(t)]])


class U3_gate(_Parameter_gate_):
    base = 'U3-gate'

    def _matrix_(self, parameters):
        self.matrix = _u3_(*parameters[0:3])
