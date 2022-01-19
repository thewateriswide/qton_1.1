'''
path: qton/quantum_circuit/initialize.py
content:

    function,
        initialize
        
'''

from numpy import zeros, sqrt, matmul


def initialize(self, statevector):
    '''
    Initialize the circuit state with a vector. 
    This vector will be normalized before continue, thus zero vector is forbidden.

    -In:
        statevector --- qubit state vector.
            type: numpy.ndarray, complex

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex.
    '''
    ket = zeros(2**self.num_qubits, complex)
    for i in range(min(len(statevector), len(ket))):
        ket[i] = statevector[i]
    norm = sqrt(matmul(ket.conj(), ket))
    if norm == 0.0:
        raise Exception('Zero norm detected.')
    else:
        ket = ket / norm
    self.statevector = ket.copy()