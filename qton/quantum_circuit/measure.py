'''
path: qton/quantum_circuit/measure.py
content:

    function:
        measure
        
'''

from numpy import zeros, arange
from numpy.random import choice


def measure(self, shots=1024):
    '''
    Take a measurement on the circuit. 

    -In:
        shots --- measurement times.
            type: int

    -Return:
        counts --- counts of measurement outputs.
            type: dict
    '''
    prob = zeros(2**self.num_qubits)
    for i in range(2**self.num_qubits):
        prob[i] = abs(self.statevector[i])**2

    counts = {}
    for i in range(shots):
        id = choice(arange(2**self.num_qubits), p = prob)
        basis = format(id, '0%db'%self.num_qubits)
        if basis in counts:
            counts[basis] += 1
        else:
            counts[basis] = 1
    return counts