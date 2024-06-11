This program performs Benchmarks of **Grover's Search** Algorithm on various simulators provided by **Aer** provider and also includes benchmarks performed with **FakeProviders**.


|Platform|Parameters|Noise Parameters|Benchmarks|Volumetric Positioning|Remarks|
|--------|----------|----------------|----------|----------------------|-------|
|qasm_simulator (0.13.3)|min_qubits=3, max_qubits=31, skip_qubits=2(default), max_circuits=2, num_shots=1000, basis: 1-['rx', 'ry', 'rz', 'cx']|***ideal***|[Test-1](1.jpg)|[Test-1-QV](1-QV.jpg)|Qasm simulator only supports upto **31** qubits.|
|qasm_simulator (0.13.3)|min_qubits=3, max_qubits=31, skip_qubits=1, max_circuits=2, num_shots=1000,basis: 1-['rx', 'ry', 'rz', 'cx']|depol_one_qb_error = 0.05, depol_two_qb_error = 0.005, reset_to_zero_error = 0.005, reset_to_one_error = 0.005|[Test-2](2.jpg)|[Test-2-QV](2-QV.jpg)|Qasm simulator only supports upto **31** qubits.|
|ibmq_athens (1.3.13) **FAKE**|min_qubits=3, max_qubits=5(default), skip_qubits=1, max_circuits=2, num_shots=1000, basis: (default-Provider)|***Provider Preset***|[Test-3](3.jpg)|[Test-3-QV](3-QV.jpg)|This is Fake Backend with maximum supported qubits **5**.|
|fake_cambridge (1.2.0) **FAKEV2**|min_qubits=3, max_qubits=28(default), skip_qubits=1, max_circuits=2, num_shots=1000 ,basis: (default-Provider)|***Provider Preset***|[Test-4](4.jpg)|[Test-4-QV](4-QV.jpg)|This is Fake Backend *(version-2)* with maximum supported qubits **28**|