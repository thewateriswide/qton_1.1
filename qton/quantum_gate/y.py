'''
path: qton/quantum_gate/y.py
content:

  class,
      Y_gate

'''

from numpy import array
from ._basic_gate_ import _Basic_gate_


class Y_gate(_Basic_gate_):
    base = 'Pauli-Y'
    matrix = array([[0, -1j], [1j, 0]])
