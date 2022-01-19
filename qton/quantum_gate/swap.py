'''
path: qton/quantum_gate/swap.py
content:

  class,
      Swap_gate

'''

from numpy import array
from ._basic_gate_ import _Basic_gate_


class Swap_gate(_Basic_gate_):
    base = 'Swap'
    matrix = array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ])