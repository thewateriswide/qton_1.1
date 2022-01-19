'''
path: qton/quantum_circuit/double_qubit_method.py
content:

  function,
      swap
      ch
      cx
      cy
      cz
      cs
      ct
      cp
      cu
      crx
      cry
      crz
      cu1
      cu2
      cu3

'''

from qton.quantum_gate import (Swap_gate, H_gate, X_gate, Y_gate, Z_gate,
                               S_gate, T_gate, P_gate, U_gate, Rx_gate,
                               Ry_gate, Rz_gate, U1_gate, U2_gate, U3_gate)


def swap(self, qubit1, qubit2):
    '''
    Swap operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 & 0 & 0 \cr
        0 & 0 & 1 & 0 \cr
        0 & 1 & 0 & 0 \cr
        0 & 0 & 0 & 1 
        \end{bmatrix}
        
    -In:
        qubit1 --- first qubit.
            type: int
        qubit2 --- second qubit.
            type: int
            
    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(Swap_gate.matrix, qubit1, qubit2)


def ch(self, ctrl, targ):
    '''
    Controlled Hadamard operation.
    
    -In:
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(H_gate(num_ctrl=1).matrix, ctrl, targ)


def cx(self, ctrl, targ):
    '''
    Controlled Pauli-X operation, or CNOT.
    
    -In:
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(X_gate(num_ctrl=1).matrix, ctrl, targ)


def cy(self, ctrl, targ):
    '''
    Controlled Pauli-Y operation.
    
    -In:
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(Y_gate(num_ctrl=1).matrix, ctrl, targ)


def cz(self, ctrl, targ):
    '''
    Controlled Pauli-Z operation.
    
    -In:
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(Z_gate(num_ctrl=1).matrix, ctrl, targ)


def cs(self, ctrl, targ):
    '''
    Controlled S operation.
    
    -In:
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(S_gate(num_ctrl=1).matrix, ctrl, targ)


def ct(self, ctrl, targ):
    '''
    Controlled T operation.
    
    -In:
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(T_gate(num_ctrl=1).matrix, ctrl, targ)


def cp(self, phi, ctrl, targ):
    '''
    Controlled phase operation.
    
    -In:
        phi --- phase angle.
            type: float
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(
        P_gate(parameters=[phi], num_ctrl=1).matrix, ctrl, targ)


def cu(self, theta, phi, lamda, gamma, ctrl, targ):
    '''
    Controlled U operation.
    
    -In:
        theta --- amplitude angle.
            type: float
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        gamma --- global phase.
            type: float
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(
        U_gate(parameters=[theta, phi, lamda, gamma], num_ctrl=1).matrix, ctrl, targ)


def crx(self, theta, ctrl, targ):
    '''
    Controlled rotatin along X axis.
    
    -In:
        theta --- rotation angle
            type: float
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(
        Rx_gate(parameters=[theta], num_ctrl=1).matrix, ctrl, targ)


def cry(self, theta, ctrl, targ):
    '''
    Controlled rotatin along Y axis.
    
    -In:
        theta --- rotation angle
            type: float
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(
        Ry_gate(parameters=[theta], num_ctrl=1).matrix, ctrl, targ)


def crz(self, theta, ctrl, targ):
    '''
    Controlled rotatin along Z axis.
    
    -In:
        theta --- rotation angle
            type: float
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(
        Rz_gate(parameters=[theta], num_ctrl=1).matrix, ctrl, targ)


def cu1(self, lamda, ctrl, targ):
    '''
    Controlled U1 operation.
    
    -In:
        lamda --- rotation angle
            type: float
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(
        U1_gate(parameters=[lamda], num_ctrl=1).matrix, ctrl, targ)


def cu2(self, phi, lamda, ctrl, targ):
    '''
    Controlled U2 operation.
    
    -In:
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(
        U2_gate(parameters=[phi, lamda], num_ctrl=1).matrix, ctrl, targ)


def cu3(self, theta, phi, lamda, ctrl, targ):
    '''
    Controlled U3 operation.
    
    -In:
        theta --- amplitude angle.
            type: float
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        ctrl --- control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._double_qubit_manipulation_(
        U3_gate(parameters=[theta, phi, lamda], num_ctrl=1).matrix, ctrl, targ)
