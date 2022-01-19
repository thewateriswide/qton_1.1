# Qton

**Qton** is slight, written in Python. By **Qton** you can test quantum algorithms, learn how quantum simulators work. 

You are encouraged to reuse code or idea of **Qton** to build your own project.



## Version

current version = `1.1.0`

Compare to `Qton 1.0.0` :

- quantum gates are realized with **Class**
- new qubit operations added
- different definition of **measure** method
- kernel gate methods have been rewritten
- others



## Install

Place the `qton` folder in your working directory, then import it as 

```python
from qton import *
```

which is same as

```python
from qton import Quantum_circuit
```



## Requirement

**Qton** is based on _NumPy_.



## Example

Let's see how to make a bell state $\frac{|001\rangle + |111\rangle}{\sqrt 2}$.

```python
from qton import Quantum_circuit

# initialize a circuit with 3 qubits.
# always starts from |000> state.
qc = Quantum_circuit(3)

# show the number of qubits in this circuit
print(qc.num_qubits)
```

```
3
```

Apply gates on qubits.

```python
# apply Hadamard gate on qubit 0
qc.h(0)

# apply CX gate, quibt 0 controls qubit 1
qc.cx(0, 1)

# apply X gate on qubit 2
qc.x(2)

# this circuit is in the bell state now
# show the statevector
print(qc.statevector)
```

```
[0.        +0.j 0.70710678+0.j 0.        +0.j 0.        +0.j
 0.        +0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
```

For most cases, getting this vector is enough for your research.

The vector basis for each component are
$$
|000\rangle, |001\rangle, |010\rangle, |011\rangle, |100\rangle, |101\rangle, |110\rangle, |111\rangle
$$
The qubit index in a basis starts to count from rightmost to leftmost, as
$$
|q_0q_1q_2\rangle
$$


---

This circuit object can be measured.

```python
# Take 1024 measurements on the circuit
counts = qc.measure(1024)

# show the counts for each basis
print(counts)
```

```
{'111': 512, '001': 512}
```

This measure function doesn't affect the circuit state.

```python
# check the state
print(qc.statevector)
```

```
[0.        +0.j 0.70710678+0.j 0.        +0.j 0.        +0.j
 0.        +0.j 0.        +0.j 0.        +0.j 0.70710678+0.j]
```



## Gate

For convenience, all gate methods in this version of **Qton** are listed below, with instances.

 ```python
l = [0, 1, 2]
np.random.shuffle(l)
q0, q1, q2 = l
angle1, angle2, angle3, angle4 = np.random.random(4) * np.pi * 2
angle4 = 0

qc.i(q0)
qc.h(q0)
qc.x(q0)
qc.y(q0)
qc.z(q0)
qc.s(q0)
qc.t(q0)
qc.sdg(q0)
qc.tdg(q0)

qc.rx(angle1, q0)
qc.ry(angle1, q0)
qc.rz(angle1, q0)
qc.p(angle1, q0)
qc.u1(angle1, q0)
qc.u2(angle1, angle2, q0)
qc.u3(angle3, angle2, angle3, q0)
qc.u(angle1, angle2, angle3, angle4, q0)

qc.swap(q0, q1)
qc.ch(q0, q1)
qc.cx(q0, q1)
qc.cy(q0, q1)
qc.cz(q0, q1)
qc.cs(q0, q1)
qc.ct(q0, q1)

qc.crx(angle1, q0, q1)
qc.cry(angle1, q0, q1)
qc.crz(angle1, q0, q1)
qc.cp(angle1, q0, q1)
qc.cu1(angle1, q0, q1)
qc.cu2(angle1, angle2, q0, q1)
qc.cu3(angle3, angle2, angle3, q0, q1)
qc.cu(angle1, angle2, angle3, angle4, q0, q1)

qc.cswap(q0, q1, q2)
qc.cch(q0, q1, q2)
qc.ccx(q0, q1, q2)
qc.ccy(q0, q1, q2)
qc.ccz(q0, q1, q2)
qc.ccs(q0, q1, q2)
qc.cct(q0, q1, q2)

qc.ccrx(angle1, q0, q1, q2)
qc.ccry(angle1, q0, q1, q2)
qc.ccrz(angle1, q0, q1, q2)
qc.ccp(angle1, q0, q1, q2)
qc.ccu(angle1, angle2, angle3, angle4, q0, q1, q2)
 ```

