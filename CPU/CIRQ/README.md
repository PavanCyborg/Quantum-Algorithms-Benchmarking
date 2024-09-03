This Directory consists of framework for various Algorithms being benchmarked on **CIRQ Simulators** on CPU Platform.

## About Platform:

Here we are using **Cirq's Simulators** for benchmarking the Quantum Algorithms. All the details about versions of Cirq and Other Programs are listed in below table under **"Tested Platform"** Section.

This Benchmarking is based on the implementation of [QC-App-Oriented-Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks/tree/master) repository by **SRI-International**.

The QED-C committee that developed these benchmarks released a paper (Oct 2021) describing the theory and methodology supporting this work at [Application-Oriented Performance Benchmarks for Quantum Computing](https://arxiv.org/abs/2110.03137).

For further information please go through the **README** file of the source repository mentioned above.

## Installation :

Please follow the below procedure for installing required essentials to run the benchmarking Programs. Make sure that you have already installed anaconda in your device.

**Step-1 :** Creating virtual environment.

```bash
conda create -n cirq python==3.10

conda activate cirq
```
The above step creates new anaconda environment with name **cirq** and activates it. Now you can go for next steps!!!

**Step-2 :** Installing **cirq**

```bash
pip install numpy matplotlib notebook openpyxl pandas
pip install scipy cirq 
```

These commands install compatible versions of required modules. 

Note; In some Windows environments, it is necessary to install one additional package (if running a Jupyter notebook results in a Windows "kernel error"):

```bash
conda install pywin32
```

All the installation procedure is completed !!!

## Running Benchmarks :

You are now ready to run the benchmark programs. By default, all benchmark programs are configured to run on a simulator that is provided within the target environment. Follow the instructions below to run the benchmarks using the built-in Simulators.

There are individual directiories allocated for each benchmarking algorithm. Inside of each directory there is a **.ipynb** file with the name of algorithm along with its dependencies *(if available)* and **Data_plotter.py** for plotting the benchmarks.

### Example:
```bash
cd Bernstein-Vazirani
jupyter nbconvert BV.ipynb --to python
python BV.py
```
This command converts the **.ipynb** file to **.py** file which will be stored in the same directory. You can use this file to run in terminal.

## NOTE :

**Cirq** has support for **3** Local simulators. They are:

1. 'Simulator' $\large\rightarrow$ cirq.Simulator()
2. 'DensityMatrixSimulator' $\large\rightarrow$ cirq.DensityMatrixSimulator()
3. 'CliffordSimulator' $\large\rightarrow$ cirq.CliffordSimulator()

- Here we have created a noise model for benchmarking. Noise parameters are to applied to Quantum Circuit before passing it into simulator for execution.

- By default, CIRQ supports only two target gatesets **"CZTarget"** and **"SqrtIswapTarget"** and transpilation can be performed only w.r.t these gatesets.

- For calculating the depth, we do not have any direct functions which retrieve the value of circuit depth so we used ***len(cirq.Circuit(qc.all_operations()))***.

- Result object of the simulator doesn't provide any data regarding the time of execution. So we are considering **Elapsed time** as the **Quantum Time**.

## Execution :

Our main code of Benchmarks are mainly categorized into 11 parts. Each part is highlighted with corresponding heading cell in the **.ipynb** file. They are:

### 1. **Custom Parameters :** 

If we want to change the input values like **min_qubits** or **max_ckts** or **Simulator** etc can be changed in this cell. All the changes made in this cell will effect the file globally.
   - We have parameter **saveplots** *(default ="false")*, which when made **true** it will save the plots obtained after successful execution into the same directory of algorithm.
   - **Type_of_Simulator** is avariable which holds the string of backend name. CIRQ only supports **"Simulator"** or **"DensityMatrixSimulator"** or **"CliffordSimulator"**.
   - **Noise_Inclusion** *(default=False)* adds noise to the Quantum circuit.
   - **Memory_utilization_plot** *(if True)* adds the plot of Memory utilized during every iteration to the results plot. All the values of plots are in the units of **(MB)**.
   - **gate_counts_plots** *(if True)* adds the plots of **average value of counts of Algorithmic and transpiled 1-Qubit and 2-Qubit gates** present in the circuit of every iteration.
   - **Store_Data** *(if True)* creates a file **__data.json** in the same directory of **.ipynb** file and stores the values of results in it.
   - **save_to_excel** *(if True and Store_Data=True)* it creates an **.xlsx** file in the name of Algorithm and stores the data into a table. Seperate excel sheets wil be created if executed with various types of simulators. Multiple entries of tables will get appended along with **last_updated** time into excel without replacing previous entries.

### 2. **Imports :**

In this cell all the required modules are imported, and name of Benchmark is declared. Variables for saved circuits which are to be displayed are declared here gloablly. If any dependent files are present in the same directory of **.ipynb** file w.r.t algorithm they will be imported in this section.
   - **basis_selector** is assigned with one of the two basis gatesets mentioned above.

### 3. **Declaring Backend :**

In this cell the **backend** gets initialized accoring to the **backend_id** parameters which is declared in **Custom Parameters** section. As cirq doesn't provide any information regarding **Quantum Volume**, we are considering that factor as **None**. But for volumetric positioning plot we are considering **QV_=2048**.
   - Device name is considered as platform which is used at the time of plotting and storing the data.

### 4. **Algorithm :**

The cells under this section contains all the functions that define the algorithm. The code under this section will remian unchanged when compared with source repository of [QC-App-Oriented-Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks/tree/master) . ***Kindly check for the latest commits of the source repository***.
   - The dependant file **cirq_utils.py** is also present in the same directory as the **.ipynb** file. Some functionalities in algorithms were imported from that file.

### 5. **Noise Parameters :**

This section consists of noise parameters that are added for performing benchmarks in their presence. 

   - To Know more information about Noise parameters in cirq, please go through [this link](https://quantumai.google/cirq/noise) as well as the [repository](https://github.com/quantumlib/Cirq/blob/main/docs/noise/representing_noise.ipynb)

### 6. **Fidelity Calculations :**

This section consists of **4** essential functions for calculating fidelities for Benchmarks. They are **polarization_fidelity**, **hellinger_fidelity_with_expected**, **rescale_fidelity** and **uniform_dist**. These functions remain unchanged. ***Kindly verify _common/metrics.py  of the source reposiory***.

### 7. **Functions of Volumetric Plots :**

The code under this section consists of all essential functions that are required to create **volumetric positioning plots** of Benchmarks. These functions are taken from **"_common/metrics.py"** of the source repository. They remain unchanged.

### 8. **Benchmarking Essentials and Fidelity Plots :**

This section consists of essential functions required for calculating essential results for benchmarks. 
   - **calculate_circuit_depth** calculates depth of Quantum circuit passed to it.
   - **calculate_transpiled_depth** calculated depth of transpiled circuit.
   - **plot_fidelity_data**  function calculates the average and standard_deviation values of **fidelity** and **Hellinger_Fidelity**.
   - **get_memory** function calculates maximum amount of memory consumed during every iteration.
   - **get_counts** function returns the dictionary of counts of executed circuit.
   - **count_gates**, **update_counts**, **count_operations**, **circuit_traverser** and **get_gate_counts** are used to calculate 1Qubit and 2Qubit gates present in both Algorithmic and Transpiled Quantum circuits.
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
|cirq| 1.4.1|
|scipy|1.13.0|
|Python Version | 3.10.14|
|Python Compiler| GCC 11.2.0|
|Jupyter Lab | 4.2.3 |
|python build   | main, May  6 2024 19:42:50|
|OS	| Linux Ubuntu 22.04.4 LTS 64-bit|
|Processor | 12th Gen Intel(R) Core(TM) i9-12900|
|CPU Specifications | 16-Cores 24-Threads |
|CPU Clocks | Upto 5.1GHz |
|Memory (Gb)	|62.465816497802734|