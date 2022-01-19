'''
path: qton/quantum_gate/x.py
content:

  class,
      X_gate

'''

from numpy import array
from ._basic_gate_ import _Basic_gate_


class X_gate(_Basic_gate_):
    base = 'Pauli-X'
    matrix = array([[0, 1], [1, 0]])