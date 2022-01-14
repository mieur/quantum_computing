from qiskit import *

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from numpy import pi

from qiskit.visualization import plot_bloch_multivector
from qiskit.visualization import plot_state_city
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(4)

qc.x(0)
qc.x(1)
qc.cx(1, 0)
qc.ccx(0, 1, 3)
qc.z(3)
qc.ccx(0, 1, 3)
qc.cx(1, 0)
qc.x(1)
qc.x(0)

backend = BasicAer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
psi = result.get_statevector(qc)
psi_prob = result.get_counts(qc)

qc.draw('mpl')

#plot_bloch_multivector(psi)
#plot_state_city(psi)
#plot_histogram(psi_prob)

plt.show()
