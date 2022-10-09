from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('TOKEN') # replace this with your IMBQ API Key
provider = IBMQ.get_provider(hub='ibm-q')

def random(bits=16):
	q = QuantumRegister(bits, 'q')
	c = ClassicalRegister(bits, 'c')
	circuit = QuantumCircuit(q, c)
	circuit.h(q)
	circuit.measure(q, c)
	
	backend = provider.get_backend('ibmq_qasm_simulator')
	job = execute(circuit, backend, shots=1)
	
	job_monitor(job)
	counts = job.result().get_counts()
	
	return counts
