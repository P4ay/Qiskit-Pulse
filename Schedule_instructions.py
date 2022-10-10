from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
# Import qiskit packages
from qiskit import IBMQ
from qiskit import schedule, transpile
from qiskit.tools.monitor import job_monitor
import numpy as np 
from numpy import *

qc = QuantumCircuit(1,1) #difining circuit 
qc.h(0)
#qc.cx(0,1)
qc.draw('mpl')
#qc.measure(0,0)


from qiskit import pulse
IBMQ.save_account('5aa05e965118a4d4c39c15a864c922b90f9beacaa68818452d6d5bdc0a9642e3ebcec552361e81811e90133399c375cdceb726c0eebd8b318a5158259740b2f7')
IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
backend=provider.get_backend('ibmq_belem')
qct = transpile(qc, backend)
print(schedule(qct, backend).instructions)