# CQRS

This folder contains models, scripts, data, and results of the [CQRS](https://learn.microsoft.com/en-us/azure/architecture/patterns/cqrs) design pattern.


## Print figures in the paper
Please, follow these steps to print the same figures presented in the paper for this design pattern:
1. Start a Jupyter notebook using <tt>jupyter notebook</tt>.
2. Open <tt>analysis.ipynb</tt>.
3. Execute all cells in that file.


## Reproduce results in the paper
To reproduce results presented in the paper, users can run new simulation. In this case, they should note that slightly different values may be observed due to the stochastic simulation. Please, follow these steps:
1. Run <tt>python3 runSim.py</tt> from the folder <tt>separated\_HW/</tt>.
2. Run <tt>python3 runSim.py</tt> from the folder <tt>separated\_SW/</tt>.
3. Start a Jupyter notebook using <tt>jupyter notebook</tt> from the <tt>CQRS/</tt>.
4. Open <tt>analysis.ipynb</tt>.
5. Execute all cells in that file.


## Run provided models with different input parameters
Users can also tune input parameters of provided models to study different applications designed with the same patter.
Please, follow these steps to study your own applications with our model:
1. Open <tt>separated\_HW/runSim.py</tt>
2. Edit lines 54--64 with your input parameters (see the [HW Parameter Table](#hw-parameter-table) for detailed explanation of available parameters) and save the file.
3. Open <tt>separated\_SW/runSim.py</tt>
4. Edit lines 54--63 with your input parameters (see the [SW Parameter Table](#sw-parameter-table) for detailed explanation of available parameters) and save the file.
5. Run <tt>python3 runSim.py</tt> from the folder <tt>separated\_HW/</tt>.
6. Run <tt>python3 runSim.py</tt> from the folder <tt>separated\_SW/</tt>.
7. Start a Jupyter notebook using <tt>jupyter notebook</tt> from the <tt>CQRS/</tt>.
8. Open <tt>analysis.ipynb</tt>.
9. Execute all cells in that file.

Note that all input parameters (except <tt>OUTFILE</tt> and <tt>NUM\_SIM\_THREADS</tt>) are defined as lists to facilitate the execution of multiple simulation. If lists are not used, the tool will stop working. Use a list with *length = 1* to consider a single value for a parameter; otherwise, use a list with *length = N* to study your system with *N* different values for the considered parameter. 

The tool *combines* all provided input parameters and executes as many simulations as the total number of combinations of input parameters.


### HW Parameter Table

| Parameter | Description |
| --- | --- |
| OUTFILE | Name of the file where simulation results will be stored |
| NUM\_SIM\_THREADS | How many simulations should be run in parallel |
| N\_TOT | Total number of requests in the system |
| N\_r | Number of Read requests in the system |
| Z\_r | Think time of Read requests |
| Z\_w | Think time of Write requests |
| C\_DB\_r | Number of CPUs allocated to the storage service that handles Read requests |
| S\_r | Service time of Read requests |
| C\_DB\_w | Number of CPUs allocated to the storage service that handles Write requests |
| S\_w | Service time of Write requests |


### SW Parameter Table

| Parameter | Description |
| --- | --- |
| OUTFILE | Name of the file where simulation results will be stored |
| NUM\_SIM\_THREADS | How many simulations should be run in parallel |
| N\_TOT | Total number of requests in the system |
| N\_r | Number of Read requests in the system |
| Z\_r | Think time of Read requests |
| Z\_w | Think time of Write requests |
| C\_DB | Number of CPUs allocated to the storage service |
| S\_r | Service time of Read requests |
| S\_w | Service time of Write requests |
