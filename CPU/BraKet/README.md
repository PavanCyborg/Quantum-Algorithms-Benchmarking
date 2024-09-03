This Directory consists of framework for various Algorithms being benchmarked on **Braket Simulators** on CPU Platform.

## About Platform:

Here we are using **Braket's Local Simulators** for benchmarking the Quantum Algorithms. All the details about versions of Braket and Other Programs are listed in below table under **"Tested Platform"** Section.

This Benchmarking is based on the implementation of [QC-App-Oriented-Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks/tree/master) repository by **SRI-International**.

The QED-C committee that developed these benchmarks released a paper (Oct 2021) describing the theory and methodology supporting this work at [Application-Oriented Performance Benchmarks for Quantum Computing](https://arxiv.org/abs/2110.03137).

For further information please go through the **README** file of the source repository mentioned above.

## Installation :

Please follow the below procedure for installing required essentials to run the benchmarking Programs. Make sure that you have already installed anaconda in your device.

**Step-1 :** Creating virtual environment.

```bash
conda create -n braket python==3.10

conda activate braket
```
The above step creates new anaconda environment with name **braket** and activates it. Now you can go for next steps!!!

**Step-2 :** Installing **braket**

```bash
pip install numpy matplotlib notebook openpyxl pandas
pip install boto3 amazon-braket-sdk 
```

These commands install compatible versions of required modules. 

All the installation procedure is completed !!!

## Running Benchmarks :

You are now ready to run the benchmark programs. By default, all benchmark programs are configured to run on a simulator that is provided within the target environment. Follow the instructions below to run the benchmarks using the built-in Local Quantum Simulator.

There are individual directiories allocated for each benchmarking algorithm. Inside of each directory there is a **.ipynb** file with the name of algorithm along with its dependencies *(if available)* and **Data_plotter.py** for plotting the benchmarks.

### Example:
```bash
cd Bernstein-Vazirani
jupyter nbconvert BV.ipynb --to python
python BV.py
```
This command converts the **.ipynb** file to **.py** file which will be stored in the same directory. You can use this file to run in terminal.

## NOTE :

AWS-Braket has support for **3** Local simulators. They are:

1. 'braket_dm' $\large\rightarrow$ Density Matrix Simulator
2. 'braket_sv' $\large\rightarrow$ State-vector Simulator
3. 'braket_ahs' $\large\rightarrow$ Analog Hamiltonian Simulator

There are also an option to pass **'default'** to select default-simulator which is also an **statevector simulator**.

- Here we have created a noise model for benchmarking which is only applicable if the simulator is **braket_dm**. This means noise parameters can only be passed to density matrix simulator. They are not applicable for other simulators.

- Local simulators of Braket doesn't support any feature called **Transpilation**. So for better readability of results, we are considering **Algorithmic depth** as **transpiled depth**.

- Result object of the simulator doesn't provide any data regarding the time of execution. So we are considering **Elapsed time** as the **Quantum Time**.

## Execution :

Our main code of Benchmarks are mainly categorized into 11 parts. Each part is highlighted with corresponding heading cell in the **.ipynb** file. They are:

### 1. **Custom Parameters :** 

If we want to change the input values like **min_qubits** or **max_ckts** or **Simulator** etc can be changed in this cell. All the changes made in this cell will effect the file globally.
   - We have parameter **saveplots** *(default ="false")*, which when made **true** it will save the plots obtained after successful execution into the same directory of algorithm.
   - **backend_id** is avariable which holds the string of backend name. Braket only supports ['braket_ahs', 'braket_dm', 'braket_sv', 'default'] out of which **'braket_ahs'** is yet to be implemented.
   - **Noise_Inclusion** *(default=True)* only applicable for **'braket_dm'** simulator. Other simulators are not affected by this change.
   - **Memory_utilization_plot** *(if True)* adds the plot of Memory utilized during every iteration to the results plot. All the values of plots are in the units of **(MB)**.
   - **gate_counts_plots** *(if True)* adds the plots of **average value of counts of Algorithmic and transpiled 1-Qubit and 2-Qubit gates** present in the circuit of every iteration.
   - **Store_Data** *(if True)* creates a file **__data.json** in the same directory of **.ipynb** file and stores the values of results in it.
   - **save_to_excel** *(if True and Store_Data=True)* it creates an **.xlsx** file in the name of Algorithm and stores the data into a table. Seperate excel sheets wil be created if executed with various types of simulators. Multiple entries of tables will get appended along with **last_updated** time into excel without replacing previous entries.

### 2. **Imports :**

In this cell all the required modules are imported, and name of Benchmark is declared. Variables for saved circuits which are to be displayed are declared here gloablly. If any dependent files are present in the same directory of **.ipynb** file w.r.t algorithm they will be imported in this section.

### 3. **Declaring Backend :**

In this cell the **backend** gets initialized accoring to the **backend_id** parameters which is declared in **Custom Parameters** section. As braket doesn't provide any information regarding Quantum Volume, we are considering that factor as **None**. But for volumetric positioning plot we are considering **QV_=2048**.
   - Device name is considered as platform which is used at the time of plotting and storing the data.

### 4. **Algorithm :**

The cells under this section contains all the functions that define the algorithm. The code under this section will remian unchanged when compared with source repository of [QC-App-Oriented-Benchmarks](https://github.com/SRI-International/QC-App-Oriented-Benchmarks/tree/master) . ***Kindly check for the latest commits of the source repository***

### 5. **Noise Parameters :**

This section consists of noise parameters that are added for performing benchmarks in their presence. These noise parameters are only applicable when executing the benchmarks with **'braket_dm'** simulator.

   - To Know more information about Noise parameters in Braket, please go through [this repository](https://github.com/amazon-braket/amazon-braket-examples/blob/main/examples/braket_features/Simulating_Noise_On_Amazon_Braket.ipynb)

### 6. **Fidelity Calculations :**

This section consists of **4** essential functions for calculating fidelities for Benchmarks. They are **polarization_fidelity**, **hellinger_fidelity_with_expected**, **rescale_fidelity** and **uniform_dist**. These functions remain unchanged. ***Kindly verify _common/metrics.py  of the source reposiory***.

### 7. **Functions of Volumetric Plots :**

The code under this section consists of all essential functions that are required to create **volumetric positioning plots** of Benchmarks. These functions are taken from **"_common/metrics.py"** of the source repository. They remain unchanged.

### 8. **Benchmarking Essentials and Fidelity Plots :**

This section consists of essential functions required for calculating essential results for benchmarks. 
   - **calculate_circuit_depth** calculates depth of Quantum circuit passed to it.
   - **plot_fidelity_data**  function calculates the average and standard_deviation values of **fidelity** and **Hellinger_Fidelity**.
   - **get_memory** function calculates maximum amount of memory consumed during every iteration.
   - **count_gates** and **get_gate_counts** are used to calculate 1Qubit and 2Qubit gates present in both Algorithmic and Transpiled Quantum circuits.
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
|amazon-braket-sdk | 1.83.0|
|amazon-braket-default-simulator| 1.26.0|
|amazon-braket-schemas| 1.22.0|
|boto3|1.34.145|
|Python Version | 3.10.4|
|Python Compiler| GCC 7.5.0|
|Jupyter Lab | 4.2.4 |
|python build   | main, Mar 31 2022 08:41:55|
|OS	| Linux Ubuntu 22.04.4 LTS 64-bit|
|Processor | 12th Gen Intel(R) Core(TM) i9-12900|
|CPU Specifications | 16-Cores 24-Threads |
|CPU Clocks | Upto 5.1GHz |
|Memory (Gb)	|62.465816497802734|