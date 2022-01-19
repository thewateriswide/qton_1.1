'''
path: qton/quantum_gate/z.py
content:

  class,
      Z_gate

'''

from numpy import array
from ._basic_gate_ import _Basic_gate_


class Z_gate(_Basic_gate_):
    base = 'Pauli-Z'
    matrix = array([[1, 0], [0, -1]])
