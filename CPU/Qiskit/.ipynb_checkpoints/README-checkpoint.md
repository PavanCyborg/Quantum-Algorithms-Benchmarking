This Directory consists of framework for various Algorithms being benchmarked on **Qiskit Simulators** on CPU Platform.

## About Platform:

Here we are using Qiskit Aer Providers for benchmarking the Quantum Algorithms. All the details about versions of Qiskit and Other Programs are listed in below table under "Tested Platforms" Section.


## Installation :

Please follow the below procedure for installing required essentials to run the benchmarking Programs. Make sure that you have already installed anaconda in your device.

**Step-1 :** Creating virtual environment.

```bash
conda create -n qiskit python=3.10

conda activate qiskit
```
The above step creates new anaconda environment with name **qiskit** and activates it. Now you can go for next steps!!!

**Step-2 :** Installing **Qiskit**

```bash
pip install numpy matplotlib notebook
pip install qiskit==0.46.1 
pip install qiskit-ibm-runtime==0.20.0 
pip install qiskit-aer==0.13.3
```

These commands install compatible versions of required modules. Make sure to use these versions, becuase other versions might not be compatible with these programs.

All the installation procedure is completed !!!

## Execution :

For executing in **Jupyter Notebook** run the following command in the terminal of current directory & move to the required **.ipynb** in their corresponding Directory.
```bash
jupyter-notebook
```

For executing in **Terminal** using python follow the bellow command. (For Example : To execute Deustch-Jozsa)
```bash
cd Deustch-Jozsa 
jupyter nbconvert DJ.ipynb --to python
python DJ.py
```
This command converts the **.ipynb** file to **.py** file which will be stored in the same directory. You can use this file to run in terminal.

## NOTE :

Qiskit-Aer provides **4** types of simulators. They are:

1. qasm_simulator
2. aer_simulator
3. statevector_simulator
4. unitary_simulator

- Here we have created a Noise Model for Benchmarking. There are other noise Parameters that can be also implemented into Noise model. Follow this [link](https://qiskit.github.io/qiskit-aer/apidocs/aer_noise.html) for more information on Noise Models. *The usage of these custom noise models are completely Optional.*

With the installation of above qiskit versions, you will also get Fake-Providers(version1) and Fake-Providers(version2). ***The fake provider module in Qiskit contains fake (simulated) backend classes useful for testing the transpiler and other backend-facing functionality.***

- This [Link](https://docs.quantum.ibm.com/api/qiskit-ibm-runtime/fake_provider) is IBM's Documentation on Fake Providers. You can go through them for more information and what are the fake backends available for simulation.

- Alternatively, If you have Know the name and want to view the configuration of FakeBackend or to view the Preset values of Fake Providers run the following code in Notebook. This will print the configuration of Backend of Fake Provider.

```python
import json
# Replace 'backend.conf_filename' with the actual path to your configuration file
filename =backend.dirname+'/'+backend.conf_filename
with open(filename, 'r') as file:
    config = json.load(file)    
print(config)
```

1. Adjust the parameters as per your requirements in **custom Parameters** section of Program. It is place where you can modilfy your benchmarking Parameters like (minimum number of Qubits, or Type of Simulator for executing).

2. Saving of resulting Plots is also Optional which can be modified in **custom parameters** section. It will save the plots only if **saveplots = True**.

3. **Type_of_Simulator** value can be assigned with 3 values. **"built_in"**,**"FAKE"** and **"FAKEV2"**. If you Opted for **"built_in"**, you need to opt for one of the four simulators provided by Qiskit-Aer as mentioned above in **Declaring Backend** section of Benchmarking Program.

4. If you opted for **FAKE** or **FAKEV2**, you need to import the corresponding Backend and corresponding method should be assigned to variable backend. For example:
```python
from qiskit.providers.fake_provider import FakeAlmaden
backend = FakeAlmaden()
```

5. By default Fake Providers execute with simulator's maximum provided Qubits. And for "Built-in" simulators they will execute the custom parameters assigned to them.

6. Noise for "built-in" simulators should be explicitly passed as **NoiseModel()** where as Fake Providers have their own Noise models.

7. Basis Selection should be explicitly assigned as defined in "basis_gate_selector" dictionary and need to select one of them. But if you are executing with Fake simulator assign the value of **basis_selector = 0** in **Imports** section of Program.

## Tested Platforms :

|System Information| Version|
|------------------|--------|
|Qiskit | 0.46.1|
|qiskit_ibm_runtime	| 0.20.0|
|qiskit-aer| 0.13.3|
|qiskit_ibm_provider| 0.7.2|
|Python Version | 3.10.4|
|Python Compiler| GCC 7.5.0|
|Jupyter Lab | 4.0.9 |
|python build   | main, Mar 31 2022 08:41:55|
|OS	| Linux Ubuntu 22.04.4 LTS 64-bit|
|Processor | 12th Gen Intel(R) Core(TM) i9-12900|
|CPU Specifications | 16-Cores 24-Threads |
|CPU Clocks | Upto 5.1GHz |
|Memory (Gb)	|62.465816497802734|
