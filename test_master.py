# Test of Vm processing in neuronal processing module
from neuron import process_cell
import pandas as pd

from matplotlib import pyplot
# %matplotlib qt

# Load Vm csv file
path = '/Volumes/Data/Dropbox/Code/swc/phd/EN/swc_invivo_analysis/data/studentCourse_Vm.csv'
vm = pd.read_csv(path)

# if clipped, simulate other data
#pyplot.plot(data['Vm_1'])

# RUN extraction fct
result = process_cell(vm=vm)

print(result)
# THE END



import numpy as np
from pylab import *
#Leaky Integrate-and-Fire
## setup parameters and state variables
T =50 # total time to simulate (msec)
dt = 0.125 # simulation time step (msec)
time = arange(0, T+dt, dt) # time array
t_rest =0
## LIF properties
Vm = np.zeros(len(time))
Rm =1
Cm = 10
tau_m = Rm*Cm
tau_ref =4
Vth =1
V_spike = 0.5
## Input stimulus
I       = 1.5
## iterate over each time step
for i, t in enumerate(time):
# initial refractory time
# potential (V) trace over time
# resistance (kOhm)
# capacitance (uF)
# time constant (msec)
# refractory period (msec)
# spike threshold (V)
# spike delta (V)
# input current (A)
  if t > t_rest:
    Vm[i] = Vm[i-1] + (-Vm[i-1] + I*Rm) / tau_m * dt
    if Vm[i] >= Vth:
      Vm[i] += V_spike
      t_rest = t + tau_ref
## plot membrane potential trace
plot(time, Vm)
title('Leaky Integrate-and-Fire Example')
ylabel('Membrane Potential (V)')
xlabel('Time (msec)')
ylim([0,2])
show()



pyplot.plot(diff_abs)
pyplot.axhline(thresh, 0, diff_abs.shape[0])