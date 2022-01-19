'''
path: qton/quantum_gate/i.py
content:

  class,
      I_gate

'''

from numpy import array
from ._basic_gate_ import _Basic_gate_


class I_gate(_Basic_gate_):
    base = 'Identity'
    matrix = array([[1, 0], [0, 1]])