from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, IBMQ
from qiskit.tools.monitor import job_monitor

IBMQ.enable_account('TOKEN') # replace this with your IMBQ API Key
provider = IBMQ.get_provider(hub='ibm-q')

def format(counts:dict) -> int:
	"""Format the result of the quantum job."""
	for _ in counts: # only one element allowed in counts
		return int(_, 2) 

def random(bits:int =16) -> int:
	"""Generate a random number in the given number of bits

	Keyword arguments:
	bits -- the amount of qubits to compute with (default 16)
	"""
	q = QuantumRegister(bits, 'q')
	c = ClassicalRegister(bits, 'c')
	circuit = QuantumCircuit(q, c)
	circuit.h(q)
	circuit.measure(q, c)
	
	backend = provider.get_backend('ibmq_qasm_simulator')
	job = execute(circuit, backend, shots=1)
	
	job_monitor(job)
	counts = job.result().get_counts()
	
	return format(counts)

def random_in(a:int, b:int) -> int:
	"""Generate a random number in [a, b]

	Positional Arguments:
	a -- left closed interval
	b -- right closed interval
	"""
	binary = '{0:08b}'.format(b-a)
	max_bits = len(binary)

	q = QuantumRegister(max_bits, 'q')
	c = ClassicalRegister(max_bits, 'c')
	ciruit = QuantumCircuit(q, c)
	circuit.h(q)
	circuit.measure(q, c) 

	backend = provider.get_backend('ibmq_qasm_simulator')
	job = execute(circuit, backend, shots=1)

	job_monitor(job)
	counts = job.result().get_counts()

	result = format(counts)

	return result + a