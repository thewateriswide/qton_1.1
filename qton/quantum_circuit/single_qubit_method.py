'''
path: qton/quantum_circuit/single_qubit_method.py
content:

  function,
      i
      h
      x
      y
      z
      s
      sdg
      t
      tdg
      p
      u
      rx
      ry
      rz
      u1
      u2
      u3

'''

from qton.quantum_gate import (I_gate, H_gate, X_gate, Y_gate, Z_gate, S_gate,
                            T_gate, P_gate, U_gate, Rx_gate, Ry_gate, Rz_gate,
                            U1_gate, U2_gate, U3_gate)


def i(self, targ):
    '''
    Identity operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 \cr
        0 & 1
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(I_gate.matrix, targ)


def h(self, targ):
    '''
    Hadamard operation.

    LaTeX matrix form:
    
        \frac{1}{\sqrt 2}\begin{bmatrix}
        1 & 1 \cr
        1 & -1
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(H_gate.matrix, targ)


def x(self, targ):
    '''
    Pauli-X operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        0 & 1 \cr
        1 & 0
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(X_gate.matrix, targ)


def y(self, targ):
    '''
    Pauli-Y operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        0 & -i \cr
        i & 0
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(Y_gate.matrix, targ)


def z(self, targ):
    '''
    Pauli-Z operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 \cr
        0 & -1
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(Z_gate.matrix, targ)


def s(self, targ):
    '''
    S operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 \cr
        0 & i
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(S_gate.matrix, targ)


def sdg(self, targ):
    '''
    S dagger operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 \cr
        0 & -i
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(S_gate(inverse=True).matrix, targ)


def t(self, targ):
    '''
    T operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 \cr
        0 & \frac{1+i}{\sqrt 2}
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(T_gate.matrix, targ)


def tdg(self, targ):
    '''
    Identity operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 \cr
        0 & \frac{1-i}{\sqrt 2}
        \end{bmatrix}

    -In:
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(T_gate(inverse=True).matrix, targ)


def p(self, phi, targ):
    '''
    Phase operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 \cr
        0 & e^{i\phi}
        \end{bmatrix}

    -In:
        phi --- phase angle.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(P_gate(parameters=[phi]).matrix, targ)


def u(self, theta, phi, lamda, gamma, targ):
    '''
    U operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        \cos\frac{\theta}{2} & -e^{i\lambda}\sin\frac{\theta}{2} \cr
        e^{i\phi}\sin\frac{\theta}{2} & e^{i\lambda+i\phi}\cos\frac{\theta}{2}
        \end{bmatrix}

    -In:
        theta --- amplitude angle.
            type: float
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        gamma --- global phase.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(
        U_gate(parameters=[theta, phi, lamda, gamma]).matrix, targ)


def rx(self, theta, targ):
    '''
    Rotation along X axis.
    
    LaTeX matrix form:
    
        \exp(-i \frac{\theta}{2} X) =
        \begin{bmatrix}
        \cos\frac{\theta}{2} & -i\sin\frac{\theta}{2} \cr
        -i\sin\frac{\theta}{2} & \cos\frac{\theta}{2}
        \end{bmatrix}

    -In:
        theta --- rotation angle.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(Rx_gate(parameters=[theta]).matrix, targ)


def ry(self, theta, targ):
    '''
    Rotation along Y axis.
    
    LaTeX matrix form:
    
        \exp(-i \frac{\theta}{2} Y) =
        \begin{bmatrix}
        \cos\frac{\theta}{2} & -\sin\frac{\theta}{2} \cr
        \sin\frac{\theta}{2} & \cos\frac{\theta}{2}
        \end{bmatrix}

    -In:
        theta --- rotation angle.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(Ry_gate(parameters=[theta]).matrix, targ)


def rz(self, theta, targ):
    '''
    Rotation along Z axis.
    
    LaTeX matrix form:
    
        \exp(-i \frac{\theta}{2} Z) =
        \begin{bmatrix}
        e^{-i\theta/2} & 0 \cr
        0 & e^{i\theta/2}
        \end{bmatrix}

    -In:
        theta --- rotation angle.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(Rz_gate(parameters=[theta]).matrix, targ)


def u1(self, lamda, targ):
    '''
    U1 operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        1 & 0 \cr
        0 & e^{i\lambda}
        \end{bmatrix}

    -In:
        lamda --- phase angle.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(U1_gate(parameters=[lamda]).matrix, targ)


def u2(self, phi, lamda, targ):
    '''
    U2 operation.
    
    LaTeX matrix form:
    
        \frac{1}{\sqrt 2}\begin{bmatrix}
        1 & -e^{i\lambda} \cr
        e^{i\phi} & e^{i\lambda+i\phi}
        \end{bmatrix}

    -In:
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(
        U2_gate(parameters=[phi, lamda]).matrix, targ)


def u3(self, theta, phi, lamda, targ):
    '''
    U3 operation.
    
    LaTeX matrix form:
    
        \begin{bmatrix}
        \cos\frac{\theta}{2} & -e^{i\lambda}\sin\frac{\theta}{2} \cr
        e^{i\phi}\sin\frac{\theta}{2} & e^{i\lambda+i\phi}\cos\frac{\theta}{2}
        \end{bmatrix}

    -In:
        theta --- amplitude angle.
            type: float
        phi --- phase angle 1.
            type: float
        lamda --- phase angle 2.
            type: float
        targ --- target qubit(s).
            type: int, or int sequence

    -Influenced:
        self.statevector --- qubit state vector.
            type: numpy.ndarray, complex
    '''
    self._single_qubit_manipulatoin_(
        U3_gate(parameters=[theta, phi, lamda]).matrix, targ)
