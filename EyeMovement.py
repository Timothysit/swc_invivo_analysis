# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:24:35 2018
Spike: Reading in the Eyetracking Data and processing it (delete outliers)
@author: svenja
"""

import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


def main():
    ### read in csv files
    left_eye_raw = pd.read_csv("data\studentCourse_eyes.csv")
    right_eye_raw = pd.read_csv("data\studentCourse_eyes2.csv")

    left_eye_reduced = drop_redundant_columns(left_eye_raw)
    right_eye_reduced = drop_redundant_columns(right_eye_raw)

    left_eye_reduced = filter_eye(left_eye_reduced)
    right_eye_reduced = filter_eye(right_eye_reduced)

    column_mean_l = left_eye_reduced['median_x'].mean()
    column_sd_l = left_eye_reduced['median_x'].std()
    left_eye_reduced['median_x'][left_eye_reduced['median_x'] < (column_mean_l - 4 * column_sd_l)] = np.nan

    column_mean_r = right_eye_reduced['median_x'].mean()
    column_sd_r = right_eye_reduced['median_x'].std()
    right_eye_reduced['median_x'][right_eye_reduced['median_x'] < (column_mean_r - 4 * column_sd_r)] = np.nan

    clean_data_columns = {'Index': left_eye_reduced['frame'],
                          'Time': left_eye_reduced['time'],
                          'X (Left Eye)': left_eye_reduced['median_x'],
                          'Y (Left Eye)': left_eye_reduced['median_y'],
                          'X (Right Eye)': right_eye_reduced['median_x'],
                          'Y (Right Eye)': right_eye_reduced['median_y']}
    clean_data_df = pd.DataFrame(data=clean_data_columns)
    clean_data_df.to_csv('data\clean_data_eyes.csv')

    # plt.plot(left_eye_reduced['x'], left_eye_reduced['y'])
    # plt.plot(left_eye_reduced['median_x'], left_eye_reduced['median_y'])
    # plt.show()

    # # replace every value outside of Median+3*Std with an average value
    # # the average value is computed from neighbouring values
    # for i in range(15, len(left_eye_reduced.x)):
    #     if (left_eye_reduced.x[i] <= left_eye_reduced['median'] + 3 * left_eye_reduced['std']) &\
    #             (left_eye_reduced.x[i] >= left_eye_reduced['median'] - 3 * left_eye_reduced['std']):
    #         left_eye_reduced.x[i] = (left_eye_reduced.x[i - 1] + left_eye_reduced.x[i + 1]) / 2
    #         print(i)


def filter_eye(input_df, median_window_width=10):
    """
    Adds a median filtered cversion of x and y as separate columns and an sd column for both

    .. Warning::

        modifies input in place

    :param pd.DataFrame input_df:
    :param int median_window_width:
    :return:
    """

    # Calculate Median and Std and make an extra column for it
    input_df['median_x'] = input_df['x'].rolling(median_window_width).median()
    input_df['std_x'] = input_df['x'].rolling(median_window_width).std()
    input_df['median_y'] = input_df['y'].rolling(median_window_width).median()
    input_df['std_y'] = input_df['y'].rolling(median_window_width).std()
    return input_df


def drop_redundant_columns(raw_eye_df):
    """
    drop the last 4 columns (x to arena, y to arena, measure, in tracking roi)

    :param raw_eye_df:
    :return:
    """
    redundant_columns = ['x to arena', 'y to arena', 'measure', 'in trakcing roi']
    reduced_eye_df = raw_eye_df.drop(redundant_columns, axis = 1)
    return reduced_eye_df


if __name__ == '__main__':
    main()
