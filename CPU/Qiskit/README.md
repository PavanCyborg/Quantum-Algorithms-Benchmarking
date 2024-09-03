This Directory consists of framework for various Algorithms being benchmarked on **Qiskit Simulators** on CPU Platform.

## About Platform:

Here we are using **Qiskit Aer Providers** for benchmarking the Quantum Algorithms. All the details about versions of Qiskit and Other Programs are listed in below table under "Tested Platforms" Section.

This Benchmarking is based on the implementation of [QC-App-Oriented-Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks/tree/master) repository by **SRI-International**.

The QED-C committee that developed these benchmarks released a paper (Oct 2021) describing the theory and methodology supporting this work at [Application-Oriented Performance Benchmarks for Quantum Computing](https://arxiv.org/abs/2110.03137).

For further information please go through the **README** file of the source repository mentioned above.

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
pip install numpy matplotlib notebook openpyxl pandas
pip install qiskit==0.46.1 
pip install qiskit-ibm-runtime==0.20.0 
pip install qiskit-aer==0.13.3
```

These commands install compatible versions of required modules. Make sure to use these versions, becuase other versions might not be compatible with these programs.

All the installation procedure is completed !!!

## Running Benchmarks :

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


## Execution :

Our main code of Benchmarks are mainly categorized into 11 parts. Each part is highlighted with corresponding heading cell in the **.ipynb** file. They are:

### 1. **Custom Parameters :** 

If we want to change the input values like **min_qubits** or **max_ckts** or **Type_of_Simulator** etc can be changed in this cell. All the changes made in this cell will effect the file globally.
   - We have parameter **saveplots** *(default ="false")*, which when made **true** it will save the plots obtained after successful execution into the same directory of algorithm.
   - **Type_of_Simulator** is a variable which holds the string of backend type. This value can be **"built_in"** or **"FAKE"** or **"FAKEV2"**.
   - **backend_name** is a variable which holds the string of Backend's name. By Default : **built_in -> qasm_simulator and FAKE -> FakeSantiago and FAKEV2 -> FakeSantiagoV2**
   - **Noise_Inclusion** *(default=False)* adds noise to the Quantum circuit. If executed on fake backend, noise is added from the backend itself regardless of the value this variable holds. 
   - **Memory_utilization_plot** *(if True)* adds the plot of Memory utilized during every iteration to the results plot. All the values of plots are in the units of **(MB)**.
   - **gate_counts_plots** *(if True)* adds the plots of **average value of counts of Algorithmic and transpiled 1-Qubit and 2-Qubit gates** present in the circuit of every iteration.
   - **Store_Data** *(if True)* creates a file **__data.json** in the same directory of **.ipynb** file and stores the values of results in it.
   - **save_to_excel** *(if True and Store_Data=True)* it creates an **.xlsx** file in the name of Algorithm and stores the data into a table. Seperate excel sheets wil be created if executed with various types of simulators. Multiple entries of tables will get appended along with **last_updated** time into excel without replacing previous entries.

### 2. **Imports :**

In this cell all the required modules are imported, and name of Benchmark is declared. Variables for saved circuits which are to be displayed are declared here gloablly. If any dependent files are present in the same directory of **.ipynb** file w.r.t algorithm they will be imported in this section.
   - **basis_selector** is assigned with one of the two basis gatesets mentioned above.

### 3. **Declaring Backend :**

In this cell the **backend** gets initialized accoring to the **backend_id** parameters which is declared in **Custom Parameters** section. Qiskit provides value of Quantum volume for Fake backends. **get_QV** function is used to retrieve that value for fake_backends. 

   - For built_in simulators, by default **QV_** is made **2048**.

### 4. **Algorithm :**

The cells under this section contains all the functions that define the algorithm. The code under this section will remian unchanged when compared with source repository of [QC-App-Oriented-Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks/tree/master) . ***Kindly check for the latest commits of the source repository***.
  

### 5. **Noise Parameters :**

This section consists of noise parameters that are added for performing benchmarks in their presence. 

   - To Know more information about Noise parameters in **qiskit_aer**, please go through [this link](https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.noise.NoiseModel.html) .

### 6. **Fidelity Calculations :**

This section consists of **4** essential functions for calculating fidelities for Benchmarks. They are **polarization_fidelity**, **hellinger_fidelity_with_expected**, **rescale_fidelity** and **uniform_dist**. These functions remain unchanged. ***Kindly verify _common/metrics.py  of the source reposiory***.

### 7. **Functions of Volumetric Plots :**

The code under this section consists of all essential functions that are required to create **volumetric positioning plots** of Benchmarks. These functions are taken from **"_common/metrics.py"** of the source repository. They remain unchanged.

### 8. **Benchmarking Essentials and Fidelity Plots :**

This section consists of essential functions required for calculating essential results for benchmarks. 
   - **calculate_circuit_depth** calculates depth of Quantum circuit passed to it.
   - **calculate_transpiled_depth** performs transpilation w.r.t required gateset and then finds depth of that transpiled circuit.
   - **plot_fidelity_data**  function calculates the average and standard_deviation values of **fidelity** and **Hellinger_Fidelity**.
   - **get_memory** function calculates maximum amount of memory consumed during every iteration.
   - **list_of_standardgates**, **update_counts**, **count_operations**, **circuit_traverser** and **get_gate_counts** are used to calculate 1Qubit and 2Qubit gates present in both Algorithmic and Transpiled Quantum circuits.
   - **get_cpu_info** function retrieves the information about the **CPU** on which the code is being executed.
   - **update_excel_with_data** function creates an **.xlsx** file or appends the result data to the existing file.

### 9. **Analyzer Function :**

The code of this section is essential in calculating **correct distribution** or **ideal distribution** which is used for calculating the values of **fidelity** and **hf_fidelity**. These functions are unique to every algorithm and run function dependant. ***Kindly verify analyzer_and_print_result functions present in respective algorithm of source repository***.

### 10. **Run Function :**

The code under this section is a single function which calls other dependant functions, creates Quantum circuits and performs their execution and stores their result.It stores data into their respective data structures at every iteration. This function returns all the stored data when called.

### 11. **Triggering RUN function :**

As the name suggests, the code under this section acts as the triggering point for execution of **RUN** function which performs execution of Algorithm. All the data is retrieved in this section and post processing on that data is performed here.

   - All the parameters are calculated for their averages and standard_deviation values w.r.t **num_ckts** and results are stored into **__data.json** and **.xlsx** files respectively if mentioned.
   - The same data is used for plotting the **Parameter Benchmarks** and **Volumetric Positioning** plots.

**Data_plotter.py** file can be used to plot the data that is present in **__data.json** without need for re-execution.

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
