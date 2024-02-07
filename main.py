# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *

# qiskit-ibmq-provider has been deprecated.
# Please see the Migration Guides in https://ibm.biz/provider_migration_guide for more detail.
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

# Loading your IBM Quantum account(s)
service = QiskitRuntimeService(channel="ibm_quantum")

qubits = int(input("Number of bits>"))
qc = QuantumCircuit(qubits, qubits)
for i in range(qubits-1):
    qc.h(i)
for i in range(qubits-1):
    qc.cx(i, i+1)
for i in range(qubits):
    qc.measure(i, i)
 
service = QiskitRuntimeService()

# Run on the least-busy backend you have access to
sim = input("Wait in queue and run on real life quantum computer(y/n)>")
if sim == "y":
    backend = service.least_busy(simulator=False, operational=True)
else:
    backend = service.backend("simulator_statevector")
# Create an Estimator object

transpiled_qc = transpile(qc, backend)
 
# Submit the circuit
job = backend.run(transpiled_qc, shots=1)
 
# Once the job is complete, get the result
result = job.result()
bin = list(result.get_counts().keys())[0]
def bin_to_int(n):
    if n[0] == "0":
        return int(n[1:], base=2)
    else:
        return -1 * int(n[1:], base=2)
print(bin_to_int(bin))
