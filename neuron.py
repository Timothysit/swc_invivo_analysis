# Process Vm trace: detect spikes, clip and output Vm-clipped + spike times
# INPUT:  Vm trace matrix: timepoint X trial
# OUTPUT: Vm-clipped[LIST], spike times[LIST], optional Vm-raw
import numpy as np
import pandas as pd
from scipy.signal import savgol_filter

from matplotlib import pyplot as plt


def process_cell(vm, param=[]):
    """
    FOR each trial, detect spikes and clip

    :param vm:
    :param param:
    :return:
    """
    vm = to_np_array(vm)

    all_trials_vm_clipped = np.full(vm.shape, np.nan)
    all_spikes = []

    for trial_idx in range(vm.shape[1]):
        curr_data = vm[:, trial_idx]

        current_trial_spikes = detect_spikes(curr_data)

        all_spikes.append(current_trial_spikes)
        all_trials_vm_clipped[:, trial_idx] = clip_spikes(curr_data, current_trial_spikes)

    return all_trials_vm_clipped, all_spikes


def to_np_array(vm):
    if isinstance(vm, pd.DataFrame):
        vm = vm.values
    if not isinstance(vm, np.ndarray):
        raise ValueError('Cannot work with data of type: {}, expected numpy array'.format(type(vm)))
    return vm


def detect_spikes(vec):
    vec_diff_abs = filter_for_thresholding(vec)

    thresh = .4  # .5  # TODO: check rise-time in relation to sampling rate
    if __debug__:
        plt.plot(vec_diff_abs)
        plt.plot(np.full((vec_diff_abs.size), thresh))

    spike_peak_points = threshold_trace(thresh, vec_diff_abs)

    if __debug__:
        for spike_peak_point in spike_peak_points:
            plt.axvline(spike_peak_point, color='r')
        plt.show()

    spikes = extract_spikes(spike_peak_points, vec)

    if __debug__:
        for spike in spikes:
            plt.plot(spike)
        plt.show()
    return spikes


def extract_spikes(spike_peak_points, vec):
    spike_n_pnts = 100
    spikes = [vec[peak_pnt - spike_n_pnts // 2:peak_pnt + spike_n_pnts // 2] for peak_pnt in spike_peak_points]
    return spikes


def filter_for_thresholding(vec, n_points_rise_t=10, filter_window_length=int(.05 * 10000 + 1)):
    vec_filt = savgol_filter(vec, filter_window_length, 2)
    vec_diff = vec_filt[n_points_rise_t:] - vec_filt[:-n_points_rise_t]
    vec_diff_abs = np.abs(vec_diff)
    return vec_diff_abs


def threshold_trace(thresh, vec_diff_abs):
    vec_diff_abs_idx = np.where(vec_diff_abs > thresh)[0]
    idx_diff = np.diff(vec_diff_abs_idx)
    idx_diff_onsets = np.where(idx_diff > 1)[-1]
    spike_peak_points = [vec_diff_abs_idx[start] for start in idx_diff_onsets]
    return spike_peak_points


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
