# Process Vm trace: detect spikes, clip and output Vm-clipped + spike times
# INPUT:  Vm trace matrix: timepoint X trial
# OUTPUT: Vm-clipped[LIST], spike times[LIST], optional Vm-raw
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter


def process_cell(vm, param):
    """
    FOR each trial, detect spikes and clip

    :param vm:
    :param param:
    :return:
    """
    vm = to_np_array(vm)

    vm_clipped = np.full(vm.shape, np.nan)
    vm_spikes = []

    for nr_trial in range(vm.shape[1]):
        curr_data = vm[:, nr_trial]

        spikes = []
        spikes = detect_spikes(curr_data)

        vm_spikes[nr_trial] = spikes
        vm_clipped[:, nr_trial] = clip_spikes(curr_data, spikes)

    return vm_clipped, vm_spikes


def to_np_array(vm):
    if isinstance(vm, pd.DataFrame):
        vm = vm.values
    if not isinstance(vm, np.ndarray):
        raise ValueError('Cannot work with data of type: {}, expected numpy array'.format(type(vm)))
    return vm


def detect_spikes(vec):
    filt = savgol_filter(vec, int(.05 * 10000 + 1), 2)

    # diff -> mean, std
    diff = np.diff(filt)
    diff_abs = np.abs(diff)

    # diff_mean = np.mean(diff_abs)
    # diff_std = np.std(diff_abs)
    # thresh = diff_mean + diff_std * 3

    thresh = .5  # TODO: check rise-time in relation to sampling rate

    intervals = np.where(diff_abs > thresh)

    chunks = np.diff(intervals)

    # todo: extract

    return spikes


def clip_spikes(vec, times, param=[]):
    """
    Clip the spikes in vec using the spike times in times

    :param np.array vec: XX
    :param np.array times:
    :param param:
    :return:
    """
    clipped = []

    for t in times:
        pass  # clip spike around it

    return clipped
