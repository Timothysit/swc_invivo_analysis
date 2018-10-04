# process neuron voltage and spike rate based on anticlockwise / clockwise data
import numpy as np
import pandas as pd

def direction_voltage(direction, mem_voltage, save_csv = False, save_name = 'direction_voltage.csv'):
    # compute mean membrane voltage for each clockwise/anticlockwise trial
    """
    INPUT
    directionVec  | clockwise / anticlockwise transition frames
    mem_voltage    | mean membrane voltage for each frame
    OUTPUT
    dirVoltageDF  | pandas data frame, col1: direction, col2: memVoltage
    """

    transition_points = np.where(np.diff(direction))[0] + 1 # +1 to make it at the first instance of change
    transition_points = np.insert(transition_points, 0, 0) # add 0 in position 0
    transition_points = np.append(transition_points, direction.shape)
    print('Transition points:')
    print(transition_points)

    # define vectors to combine in the dataframe
    trial = np.arange(0, np.size(transition_points) - 1) + 1 # to become 1 indexing
    # meanMemVoltage = np.empty(np.size(transitionPoints))
    mean_mem_voltage = list()
    clockwise = np.repeat([1, 0], repeats = np.size(transition_points)/2) # but this also transitionPoints are even

    # iterate through each pair in transitionPoints (0, 1), (1, 2) ...
    for transition_start, transition_end in pairwise(transition_points):
        # compute mean voltage
        trial_voltage = np.mean(mem_voltage[transition_start:transition_end])
        mean_mem_voltage.append(trial_voltage)

    # make pandas dataframe
    direction_voltage_df = pd.DataFrame({'Trial': trial, 'Mean voltage': mean_mem_voltage, 'Clockwise': clockwise})

    if save_csv is True:
        direction_voltage_df.to_csv(save_name, sep = ',')

    return direction_voltage_df

def direction_spike_rate():
    # compute the spike rate for
    return 1

from itertools import tee # , izip
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


# test run
if __name__ == '__main__':
    fakeDirectionData = np.array([0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1])
    fakeMemVoltageData = np.array([0.4, 0.7, 0.5, 1.7, 2.5, 3.5, 0.4, 0.7, 1.2, 1.3, 1.5])
    direction_voltage_df = direction_voltage(fakeDirectionData, fakeMemVoltageData, save_csv = True)
    print(direction_voltage_df)



