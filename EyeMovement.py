# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 13:24:35 2018
Spike: Reading in the Eyetracking Data and processing it (delete outliers)
@author: svenja
"""
import pandas as pd

### read in csv files 
LeftEyeRaw = pd.read_csv("data\studentCourse_eyes.csv")
RightEyeRaw = pd.read_csv("data\studentCourse_eyes2.csv")

### drop the last 4 columns (x to arena, y to arena, measure, in tracking roi)
LeftEyeReduced = LeftEyeRaw.drop(['x to arena','y to arena','measure', 'in trakcing roi'], axis = 1)
RightEyeReduced = RightEyeRaw.drop(['x to arena','y to arena','measure', 'in trakcing roi'], axis = 1)

### Remove outliers with median filtering
#define window over which to calculate median and std
window = 10 

#Calculate Median and Std and make an extra column for it
LeftEyeReduced['median']= LeftEyeReduced['x'].rolling(window).median()
LeftEyeReduced['std'] = LeftEyeReduced['x'].rolling(window).std()

#replace every value outside of Median+3*Std with an average value
#the average value is computed from neighbouring values
i = 1
while i < len(LeftEyeReduced.x):
    if (LeftEyeReduced.x[i] <= LeftEyeReduced['median']+3*LeftEyeReduced['std']) & (LeftEyeReduced.x[i] >= LeftEyeReduced['median']-3*LeftEyeReduced['std']):
        LeftEyeReduced.x[i] = (LeftEyeReduced.x[i-1]+LeftEyeReduced.x[i+1])/2
        print(i)
    
    

