'''
path: qton/quantum_gate/t.py
content:

  class,
      T_gate

'''

from numpy import array, sqrt
from ._basic_gate_ import _Basic_gate_


class T_gate(_Basic_gate_):
    base = 'T-gate or S-root'
    matrix = array([[1, 0], [0, (1 + 1j) * sqrt(0.5)]])
