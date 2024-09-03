This Directory consists of framework for various Algorithms being benchmarked on **dm_simulator** of Qiskit's BasicAer on CPU Platform.

## About Platform:

Here we are using **Qiskit BasicAer Providers** for benchmarking the Quantum Algorithms. All the details about versions of Qiskit and Other Programs are listed in below table under "Tested Platforms" Section.

This Benchmarking is based on the implementation of [QC-App-Oriented-Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks/tree/master) repository by **SRI-International**.

The QED-C committee that developed these benchmarks released a paper (Oct 2021) describing the theory and methodology supporting this work at [Application-Oriented Performance Benchmarks for Quantum Computing](https://arxiv.org/abs/2110.03137).

For further information please go through the **README** file of the source repository mentioned above.

For the repository of this dm_simulator please go through [Qiskit-Aakash](https://github.com/indian-institute-of-science-qc/qiskit-aakash/tree/terra_upgrade)

## Installation :

Please follow the below procedure for installing required essentials to run the benchmarking Programs. Make sure that you have already installed anaconda in your device.

**Step-1 :** Creating virtual environment.

```bash
conda create -n QiskitAakash python=3.8.19

conda activate QiskitAakash
```
The above step creates new anaconda environment with name **QiskitAakash** and activates it. Now you can go for next steps!!!

**Step-2 :** Clone the repository 
```bash
git clone -b terra_upgrade https://github.com/indian-institute-of-science-qc/qiskit-aakash.git
```
This will download a folder with the name of **qiskit-aakash**.

**Step-3 :** Go to the specified hash-id:
```bash
cd qiskit-aakash
git checkout -b dmsim bea98fbff86c234c0b1990add17493a1e86917cb
git log -n1
```
**Step-4 :** Installation of requirements :
Install ipython-genutils :
```bash
python -m pip install ipython-genutils
```
or
```bash
conda install -c conda-forge ipython_genutils
```
Install rustup :
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
python -m pip install setuptools-rust
```

Install requirements : If you want to run tests or linting checks, install the developer requirements.
```bash
pip install -r requirements-dev.txt
```

**Step-5 :** Installing **Qiskit** from the repository of **Qiskit-Aakash**

```bash
pip install numpy matplotlib notebook openpyxl pandas
pip install .
```

These commands install compatible versions of required modules. Make sure to use these versions, because other versions might not be compatible with these programs.

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

Here we are only using **dm_simulator** of **BasicAer**.

- Here we are passing noise parameters as a dictionary into **execute()** function for execution with noise. For more information of noise usage please go through this [link](https://github.com/indian-institute-of-science-qc/qiskit-aakash/blob/terra_upgrade/dm_simulator_user_guide/features/noise.ipynb)


As you were installing a specific version of Qiskit-Aakash repository for dm_simulator please note that it has the following issues.

**1. Reverse Order of Probabilities :**

Density Matrix simulator (on the basis of Basic-Aer) represents the **Measurements** in the reverse order when compared with that of QASM-Simulator.

- To resolve this we are using a built-in functionality called **reverse_bits()**.

- This function places measurement gates in reverse order of which QASM Simulator uses.

- Use this fucnction while creating the Quantum Circuit.

For example:
```python
qc = BersteinVazirani(num_qubits, s_int, method).reverse_bits()
```

**2. Partial and Ensemble probabilities :**

In this repository we mostly measure our resulting probabilities in two methods. 

a. Measurement with Ensemble Probability

b. Measurement with Partial Probability

- While creating Quantum Circuit, if we use basis as "Ensemble" then we get our measurements as **ensemble_probability** in our result object. But if we haven't mentioned any basis specifically, dm_simulator by default gives **partial_probability** in our result object.


**3. Issues with Ensemble Probability Measurement :**

Ensemble probability measures every qubit in the quantum circuit and returns measurements accordingly. But in our benchmarking suite most of the algorithms use **n-1** measurements for **n** number of qubits. This is because the remaining one qubit is considered as **auxillary** which isn't meant for measurement. (Check the algorithms for better clarification).

- Due to this reason we are not using Ensemble-measurement for our Benchmarking. *Benchmarking with Ensemble measurement is implemented in Deutsch-Jozsa Algorithm (optional)*.

**4. Limitations of Partial probability measurement :**

Atleast **2** measurements are needed to be performed (i.e., the Quantum circuit should have atleast 2 Measurement gates at the output) to calculate **partial_probability** values. Anything less-than **2** doesn't work, it simply throws an error. ***This version of DM_Simulator doesn't have the implementation to get the partial_probability for single-qubit measurement***.


1. Adjust the parameters as per your requirements in **custom Parameters** section of Program. It is place where you can modilfy your benchmarking Parameters like (minimum number of Qubits, or Type of Simulator for executing).

2. Saving of resulting Plots is also Optional which can be modified in **custom parameters** section. It will save the plots only if **saveplots = True**.

3. Basis Selection should be explicitly assigned as defined in "basis_gate_selector" dictionary and need to select one of them.


## Execution :

Our main code of Benchmarks are mainly categorized into 11 parts. Each part is highlighted with corresponding heading cell in the **.ipynb** file. They are:

### 1. **Custom Parameters :** 

If we want to change the input values like **min_qubits** or **max_ckts** etc can be changed in this cell. All the changes made in this cell will effect the file globally.
   - We have parameter **saveplots** *(default ="false")*, which when made **true** it will save the plots obtained after successful execution into the same directory of algorithm.
   - **backend** is a variable which holds the string of Backend's name which is **'dm_simulator'**. 
   - **Noise_Inclusion** *(default=False)* adds noise to the Quantum circuit. If executed on fake backend, noise is added from the backend itself regardless of the value this variable holds. 
   - **Memory_utilization_plot** *(if True)* adds the plot of Memory utilized during every iteration to the results plot. All the values of plots are in the units of **(MB)**.
   - **gate_counts_plots** *(if True)* adds the plots of **average value of counts of Algorithmic and transpiled 1-Qubit and 2-Qubit gates** present in the circuit of every iteration.
   - **Store_Data** *(if True)* creates a file **__data.json** in the same directory of **.ipynb** file and stores the values of results in it.
   - **save_to_excel** *(if True and Store_Data=True)* it creates an **.xlsx** file in the name of Algorithm and stores the data into a table. Seperate excel sheets wil be created if executed with various types of simulators. Multiple entries of tables will get appended along with **last_updated** time into excel without replacing previous entries.

### 2. **Imports :**

In this cell all the required modules are imported, and name of Benchmark is declared. Variables for saved circuits which are to be displayed are declared here gloablly. If any dependent files are present in the same directory of **.ipynb** file w.r.t algorithm they will be imported in this section.
   - **basis_selector** is assigned with one of the two basis gatesets mentioned above.

### 3. **Declaring Backend :**

In this cell the **backend** gets initialized to BasicAer's **'dm_simulator'** . 

   - For built_in simulators, by default **QV_** is made **2048**.

### 4. **Algorithm :**

The cells under this section contains all the functions that define the algorithm. The code under this section will remian unchanged when compared with source repository of [QC-App-Oriented-Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks/tree/master) . ***Kindly check for the latest commits of the source repository***.
  

### 5. **Noise Parameters :**

This section consists of noise parameters that are added for performing benchmarks in their presence. 

   - To Know more information about Noise parameters please go through this [link](https://github.com/indian-institute-of-science-qc/qiskit-aakash/blob/terra_upgrade/dm_simulator_user_guide/features/noise.ipynb)

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
   - Instead of **backend.run()** we use **execute()** function.

### 11. **Triggering RUN function :**

As the name suggests, the code under this section acts as the triggering point for execution of **RUN** function which performs execution of Algorithm. All the data is retrieved in this section and post processing on that data is performed here.

   - All the parameters are calculated for their averages and standard_deviation values w.r.t **num_ckts** and results are stored into **__data.json** and **.xlsx** files respectively if mentioned.
   - The same data is used for plotting the **Parameter Benchmarks** and **Volumetric Positioning** plots.

**Data_plotter.py** file can be used to plot the data that is present in **__data.json** without need for re-execution.

## Tested Platforms :

|System Information| Version|
|------------------|--------|
|qiskit-sphinx-theme | 1.16.1|
|scipy| 1.10.1|
|Python Version | 3.8.19|
|Python Compiler| GCC 11.2.0|
|Jupyter Lab | 4.1.5 |
|python build   |default Mar 20 2024 19:58:24|
|OS	| Linux Ubuntu 22.04.4 LTS 64-bit|
|Processor | 12th Gen Intel(R) Core(TM) i9-12900|
|CPU Specifications | 16-Cores 24-Threads |
|CPU Clocks | Upto 5.1GHz |
|Memory (Gb)	|62.465816497802734|
