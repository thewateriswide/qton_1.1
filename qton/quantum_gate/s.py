'''
path: qton/quantum_gate/s.py
content:

  class,
      S_gate

'''

from numpy import array
from ._basic_gate_ import _Basic_gate_


class S_gate(_Basic_gate_):
    base = 'S-gate or Z-root'
    matrix = array([[1, 0], [0, 1j]])
