'''
path: qton/quantum_gate/_basic_gate_.py

content:

  function,
      _add_control_
      _inverse_
  class,
      _Basic_gate_
      _Parameter_gate_

'''


from numpy import array, log, eye


def _add_control_(matrix, num_ctrl=1):
    '''
    Add control(s) to a gate matrix.
    -In:
        matrix --- gate matrix.
            type: numpy.ndarray
        num_ctrl --- number of controls to add.
            type: int
    -Out:
        altered --- altered gate matrix with controls.
            type: numpy.ndarray    
    '''
    mat = array(matrix)
    num_row, num_col = mat.shape
    if num_row != num_col:
        raise Exception('Not a square matrix.')
    num_qubits = log(num_row) / log(2)
    if num_qubits % 1 != 0.0:
        raise Exception('Not a valid gate matrix.')
    num_qubits = int(num_qubits)

    altered = eye(N=2**(num_qubits + num_ctrl), dtype=complex)
    offset = 2**(num_qubits + num_ctrl) - num_row
    for i_row in range(num_row):
        for i_col in range(num_col):
            altered[i_row + offset, i_col + offset] = mat[i_row, i_col]

    return altered


def _inverse_(matrix):
    '''
    Invert a gate matrix, apply a dagger(transpose and conjugate) operation.
    -In:
        matrix --- gate matrix.
            type: numpy.ndarray
    -Out:
        inverse --- inverse matrix.
            type: numpy.ndarray    
    '''
    mat = array(matrix)
    inverse = mat.transpose().conj()

    return inverse


class _Basic_gate_(object):
    '''
    Template class. Contains basic information of a gate.
    '''
    base = 'Empty'
    matrix = None
    num_ctrl = 0
    inverse = False

    def __init__(self, num_ctrl=0, inverse=False):
        '''
        -In:
            num_ctrl --- number of gate controls.
                type: int
            inverse --- the basic gate or its inverse.
                type: bool
        '''
        if num_ctrl != 0:
            self.num_ctrl = num_ctrl
            self.matrix = _add_control_(self.matrix, num_ctrl=num_ctrl)
        if inverse == True:
            self.inverse = True
            self.matrix = _inverse_(self.matrix)


class _Parameter_gate_(_Basic_gate_):
    '''
    Template class for parameterised gates.
    '''
    def __init__(self, parameters, num_ctrl=0, inverse=False):
        '''
        -In:
            parameters --- parameters for parameterised gates.
                type: float, sequence
            num_ctrl --- number of gate controls.
                type: int
            inverse --- the basic gate or its inverse.
                type: bool
        '''
        # "_matrix_" method will be realized in successors.
        self._matrix_(parameters)
        if num_ctrl != 0:
            self.num_ctrl = num_ctrl
            self.matrix = _add_control_(self.matrix, num_ctrl=num_ctrl)
        if inverse == True:
            self.inverse = True
            self.matrix = _inverse_(self.matrix)