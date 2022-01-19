'''
path: qton/quantum_gate/u.py
content:

  function,
      _u_
  class,
      U_gate

'''

from numpy import array, sin, cos, exp
from ._basic_gate_ import _Parameter_gate_


def _u_(theta, phi, lamda, gamma):
    t = theta * 0.5
    return array(
        [[cos(t), -exp(1j * lamda) * sin(t)],
         [exp(1j * phi) * sin(t),
          exp(1j * lamda + 1j * phi) * cos(t)]]) * exp(1j * gamma)


class U_gate(_Parameter_gate_):
    base = 'Universal'

    def _matrix_(self, parameters):
        self.matrix = _u_(*parameters[0:4])
