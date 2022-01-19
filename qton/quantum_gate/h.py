'''
path: qton/quantum_gate/h.py
content:

  class,
      H_gate

'''

from numpy import array, sqrt
from ._basic_gate_ import _Basic_gate_


class H_gate(_Basic_gate_):
    base = 'Hadamard'
    matrix = sqrt(0.5) * array([[1, 1], [1, -1]])
