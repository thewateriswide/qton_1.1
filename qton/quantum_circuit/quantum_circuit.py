'''
path: qton/quantum_circuit/quantum_circuit.py
content:

    class,
        Quantum_circuit
        
'''

__all__ = ['Quantum_circuit']

from numpy import zeros, sqrt, matmul


class Quantum_circuit(object):
    '''
    Basic behaviour of interactive quantum circuits.

    We take Big-Endian on the basis convention, which is opposite to Qiskit.

    Example for usage:

        Create an instance:
            qc = Quantum_circuit(num_qubits)
            
        Invoke the number of qubits:
            qc.num_qubits
            
        Apply CX gate, qubit 0 controls qubit 1:
            qc.cx(0, 1)
        Qubits are indexed by integers start from 0.
        
        Invoke the instance's state:
            qc.statevector
            
        Take a measurement on the instance, on qubit 2 and 3:
            observe = qc.measure([2, 3])
        Which retruns a count of basis.
    '''
    num_qubits = 0
    statevector = None

    from .initialize import initialize
    from .measure import measure
    from .single_qubit_method import (i, h, x, y, z, s, sdg, t, tdg, p, u, rx,
                                      ry, rz, u1, u2, u3)
    from .double_qubit_method import (swap, ch, cx, cy, cz, cs, ct, cp, cu,
                                      crx, cry, crz, cu1, cu2, cu3)
    from .triple_qubit_method import (cswap, cch, ccx, ccy, ccz, ccs, cct, ccp,
                                      ccu, ccrx, ccry, ccrz)

    def __init__(self, num_qubits=0):
        '''
        
        Circuit starts from |0...0> state by default.

        -In:
            num_qubits --- number of qubits.
                type: int
        
        -Influenced:
            self.num_qubits --- number of qubits.
                type: int
            self.statevector --- qubit state vector.
                type: numpy.ndarray, complex
        '''
        self.num_qubits = num_qubits
        self.statevector = zeros(2**num_qubits, complex)
        self.statevector[0] = 1.0

    def _inner_swap_(self, qubit1, qubit2):
        '''
        Swap two qubits.
        Swap two correlated bases in state vector actually.

        This method is only for internal use, don't mix up with normal "swap" method.
        If two input qubits are same, does nothing.

        The principle behind is to switch coefficients of two bases like

            |...b[q1]...b[q2]...> 
        
        and 
        
            |...b[q2]...b[q1]...>

        -In:
            qubit1 --- first qubit index.
                type: int
            qubit2 --- second qubit index.
                type: int

        -Influenced:
            self.statevector --- qubit state vector.
                type: numpy.ndarray, complex
        '''
        if qubit1 == qubit2:
            return None

        # "q1" should be on left side of "q2"
        # the left qubit has smaller index
        if qubit2 < qubit1:
            q1 = qubit2
            q2 = qubit1
        else:
            q1 = qubit1
            q2 = qubit2

        # set location of qubit digits
        # counts digit from right to left
        x1 = self.num_qubits - q1 - 1  # location of "q1"
        x2 = self.num_qubits - q2 - 1  # location of "q2"

        # weight of location
        w1 = 2**x1
        w2 = 2**x2

        old_statevector = self.statevector.copy()
        for i in range(2**self.num_qubits):
            # digits for "q1" and "q2"
            a = i & w1
            b = i & w2
            if a >> x1 != b >> x2:
                # if two digits are not same
                # switch them
                tmp1 = 2**64 - 1 - w1 - w2  # 64 means we support switch between at most 63 qubits
                delta = x1 - x2
                tmp2 = (b << delta) + (a >> delta)
                j = i & tmp1 | tmp2
                self.statevector[i] = old_statevector[j]

    def _single_qubit_manipulatoin_(self, gate, targ):
        '''
        Apply a single-qubit gate on given qubits. 
        
        This is an internal method based on another internal method "_inner_swap_".

        First swap the target qubit with the rightmost qubit.
        Apply the gate on the rightmost qubit, then swap back.
        Target could be a sequence of qubits.  

        -In:
            gate --- single-qubit gate matrix.
                type: numpy.ndarray
            targ --- target qubit(s).
                type: int, or int sequence

        -Influenced:
            self.statevector --- qubit state vector.
                type: numpy.ndarray, complex
        '''
        if type(targ) is int:
            targ = [targ]
        else:
            targ = list(set(targ))

        num_basis = 2**self.num_qubits
        for i in targ:
            self._inner_swap_(i, self.num_qubits - 1)
            for j in range(0, num_basis, 2):
                self.statevector[j:j + 2] = matmul(gate,
                                                   self.statevector[j:j + 2])
            self._inner_swap_(i, self.num_qubits - 1)

    def _double_qubit_manipulation_(self, gate, qubit1, qubit2):
        '''
        Apply a double-qubit gate on two given qubits. 
        
        This is an internal method. "qubit1" and "qubit2" can only be scalars.
        
        Find out which 4 elements in state vector vary simultaneously.
        Multiply the gate matrix on them.

        -In:
            gate --- double-qubit gate matrix.
                type: numpy.ndarray
            qubit1 --- usually the control qubit.
                type: int
            qubit2 --- usually the target qubit.
                type: int

        -Influenced:
            self.statevector --- qubit state vector.
                type: numpy.ndarray, complex
        '''
        if qubit1 == qubit2:
            raise Exception('Cannot be same qubits.')

        reg = [qubit2, qubit1]
        q = list(set(range(self.num_qubits)) - set(reg))
        q.sort(reverse=True)

        wgt = [2**(self.num_qubits - i - 1) for i in reg + q]
        x = 0
        l = list(range(2**self.num_qubits))
        for i in range(1, 2**self.num_qubits - 1):
            for j in range(self.num_qubits):
                if i % (2**j) == 0: x ^= wgt[j]
            l[i] = x
        for i in range(0, 2**self.num_qubits, 4):
            vec = matmul(gate, [
                self.statevector[l[i]],
                self.statevector[l[i + 1]],
                self.statevector[l[i + 2]],
                self.statevector[l[i + 3]],
            ])
            for j in range(4):
                self.statevector[l[i + j]] = vec[j]

    def _triple_qubit_manipulation_(self, gate, qubit1, qubit2, qubit3):
        '''
        Apply a triple-qubit gate on three given qubits. 
        
        This is an internal method. "qubit1", "qubit2" and "qubit3" can only be scalars. 

        Find out which 8 elements in state vector vary simultaneously.
        Multiply the gate matrix on them.

        -In:
            gate --- triple-qubit gate matrix.
                type: numpy.ndarray
            qubit1 --- usually the first control qubit.
                type: int
            qubit2 --- usually the second control qubit.
                type: int
            qubit3 --- usually the target qubit.
                type: int

        -Influenced:
            self.statevector --- qubit state vector.
                type: numpy.ndarray, complex
        '''
        if len({qubit1, qubit2, qubit3}) < 3:
            raise Exception('Should be 3 different qubits.')

        reg = [qubit3, qubit2, qubit1]
        q = list(set(range(self.num_qubits)) - set(reg))
        q.sort(reverse=True)

        wgt = [2**(self.num_qubits - i - 1) for i in reg + q]
        x = 0
        l = list(range(2**self.num_qubits))
        for i in range(1, 2**self.num_qubits - 1):
            for j in range(self.num_qubits):
                if i % (2**j) == 0: x ^= wgt[j]
            l[i] = x
        for i in range(0, 2**self.num_qubits, 8):
            vec = matmul(gate, [
                self.statevector[l[i]], self.statevector[l[i + 1]],
                self.statevector[l[i + 2]], self.statevector[l[i + 3]],
                self.statevector[l[i + 4]], self.statevector[l[i + 5]],
                self.statevector[l[i + 6]], self.statevector[l[i + 7]]
            ])
            for j in range(8):
                self.statevector[l[i + j]] = vec[j]