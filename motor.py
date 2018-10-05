"""
Analysis of motor movement
Input is csv file (motorFile) output is also csv file
"""

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

# making a mini dataframe with fake data
# fake_motor_data = {'command':[0,10,15,-5,-10,-15,0], 'time':[0,1,2,3,4,5,6]}
# motor_df = pd.DataFrame(fake_motor_data, columns = ['command','time' ])
# print(motor_df)


def motor_direction(commandfile):
    """
    Determines the direction (clockwise/counterclockwise)
    of visual stimuli delivered using a command signal

    :param pd.DataFrame commandfile:
    :return:
    """
    # save the array containing commandvalues as a new column
    command_column = commandfile['command']
    print(command_column)
    cmd = command_column.values
    print(cmd)

    # calculate the direction by determining the change from current command to the next command

    direction = np.zeros((cmd.size - 1))  # -1 because diff
    direction[cmd[:-1] < cmd[1:]] = 1
    direction[cmd[:-1] > cmd[1:]] = -1
    print(direction)

    # add a time array
    length_direction_array = np.size(direction)
    print("length of direction array is:", length_direction_array)
    time = np.arange(length_direction_array)
    print(time)

    # make a dataframe of all the data
    real_motor_df = pd.DataFrame({"command": cmd[:-1],
                                  "direction": direction,
                                  "time": time})

    plt.plot(real_motor_df['command'])
    plt.plot(real_motor_df['direction'])
    plt.show()

    print(real_motor_df)

    real_motor_df.to_csv("direction_motor.csv", sep=",")
    return real_motor_df


# fake test data
test_cmd_df = pd.DataFrame({'command': np.array([0, 1, 2, 3, 7, -7, 8, 9, -2, -20, -25])})


# actual data
if __name__ == '__main__':
    command_df = pd.read_csv('studentCourse_command.csv')
    motor_direction(command_df)
