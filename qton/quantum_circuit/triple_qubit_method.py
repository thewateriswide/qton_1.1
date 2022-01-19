'''
path: qton/quantum_circuit/triple_qubit_method.py
content:

  function,
      cswap
      cch
      ccx
      ccy
      ccz
      ccs
      cct
      ccp
      ccu
      ccrx
      ccry
      ccrz
      
'''

from qton.quantum_gate import (Swap_gate, H_gate, X_gate, Y_gate, Z_gate,
                               S_gate, T_gate, P_gate, U_gate, Rx_gate,
                               Ry_gate, Rz_gate)


def cswap(self, ctrl, qubit1, qubit2):
    '''
    Controlled swap operation.
    
    -In:
        ctrl --- control qubit.
            type: int
        qubit1 --- first target qubit.
            type: int
        qubit2 --- first target qubit.
            type: int
            
    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        Swap_gate(num_ctrl=1).matrix, ctrl, qubit1, qubit2)


def cch(self, ctrl1, ctrl2, targ):
    '''
    Double controlled Hadamard operation.
    
    -In:
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        H_gate(num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def ccx(self, ctrl1, ctrl2, targ):
    '''
    Double controlled Pauli-X operation.
    
    -In:
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        X_gate(num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def ccy(self, ctrl1, ctrl2, targ):
    '''
    Double controlled Pauli-Y operation.
    
    -In:
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        Y_gate(num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def ccz(self, ctrl1, ctrl2, targ):
    '''
    Double controlled Pauli-Z operation.
    
    -In:
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        Z_gate(num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def ccs(self, ctrl1, ctrl2, targ):
    '''
    Double controlled S operation.
    
    -In:
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        S_gate(num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def cct(self, ctrl1, ctrl2, targ):
    '''
    Double controlled T operation.
    
    -In:
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit.
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        T_gate(num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def ccp(self, phi, ctrl1, ctrl2, targ):
    '''
    Double controlled phase operation.
    
    -In: 
        phi --- phase angle.
            type: float
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        P_gate(parameters=[phi], num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def ccu(self, theta, phi, lamda, gamma, ctrl1, ctrl2, targ):
    '''
    Double controlled U operation.
    
    -In: 
        theta --- amplitude angle.
            type: float
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        gamma --- global phase.
            type: float
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        U_gate(parameters=[theta, phi, lamda, gamma], num_ctrl=2).matrix, ctrl1,
        ctrl2, targ)


def ccrx(self, theta, ctrl1, ctrl2, targ):
    '''
    Double controlled rotatin along X axis.
    
    -In:
        theta --- rotation angle
            type: float
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        Rx_gate(parameters=[theta], num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def ccry(self, theta, ctrl1, ctrl2, targ):
    '''
    Double controlled rotatin along Y axis.
    
    -In:
        theta --- rotation angle
            type: float
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        Ry_gate(parameters=[theta], num_ctrl=2).matrix, ctrl1, ctrl2, targ)


def ccrz(self, theta, ctrl1, ctrl2, targ):
    '''
    Double controlled rotatin along Z axis.
    
    -In:
        theta --- rotation angle
            type: float
        ctrl1 --- first control qubit.
            type: int
        ctrl2 --- second control qubit.
            type: int
        targ --- target qubit
            type: int

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._triple_qubit_manipulation_(
        Rz_gate(parameters=[theta], num_ctrl=2).matrix, ctrl1, ctrl2, targ)