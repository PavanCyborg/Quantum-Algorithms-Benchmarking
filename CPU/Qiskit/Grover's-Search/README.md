This program performs Benchmarks of **Grover's Search** Algorithm on various simulators provided by **Aer** provider and also includes benchmarks performed with **FakeProviders**.


|Platform|Parameters|Noise Parameters|Benchmarks|Volumetric Positioning|Remarks|
|--------|----------|----------------|----------|----------------------|-------|
|qasm_simulator (0.13.3)|min_qubits=3, max_qubits=13, skip_qubits=2(*default if given <2*), max_circuits=2, num_shots=1000, basis: 1-['rx', 'ry', 'rz', 'cx']|***ideal***|![Test-1](Test-1.jpg)|![Test-1-QV](Test-1-QV.jpg)|Qasm simulator supports upto **31** qubits. But at 15 qubits, overall System's Memory consumption is over **67 GB** so, the process is getting killed.|