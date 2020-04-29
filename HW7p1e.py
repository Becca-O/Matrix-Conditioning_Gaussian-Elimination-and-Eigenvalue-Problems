#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 10:12:19 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 1e

import numpy as np

# Part 1d
def matrixCreator(tvec): # tvec is a numpy array (t1,t2,t3), the time values at which I plan to take my measurements
    t1 = tvec[0]
    t2 = tvec[1]
    t3 = tvec[2]
    A = np.array([[1, t1, 0.5*(t1**2)], [1, t2, 0.5*(t2**2)], [1, t3, 0.5*(t3**2)]])
    return A
    
# Part 1d
    
print('STRATEGY 1: (t1,t2,t3) = (0s, 1s, 10s) & (x1,x2,x3) = (0.30m, 0.665m, 14.30m)')
tvec1 = np.array([0., 1., 10.])
xvec1 = np.array([0.30, 0.665, 14.30])
yuH = matrixCreator(tvec1)
parameters1 = np.linalg.solve(yuH,xvec1)
print('Unknowns: x0, v0, a')
print(parameters1)

# Part 1e
# error estimtaion: upper-lower bound method
x1 = xvec1[0]
x2 = xvec1[1]
x3 = xvec1[2]
delta = 0.005 # known measurement accuracy in position, delta_x = 0.005 m
error1 = np.array([x1, x2 - delta, x3 - delta]) # worst-case scenario as the parameters obtained for a lower bound: (x1, x2 - delta_x, x3 - delta_x)
print('Lower Bound of x')
print(error1)
print('LB Resulting best fit values: v0, a')
bestf1 = np.linalg.solve(yuH, error1) # computing the resulting best-fit values of (v0, a)
print(bestf1)
error2 = np.array([x1, x2 + delta, x3 + delta]) # worst-case scenario as the parameters obtained for a upper bound: (x1, x2 + delta_x, x3 + delta_x)
print('Upper Bound of x')
print(error2)
print('UB Resulting best fit values: v0, a')
bestff1 = np.linalg.solve(yuH, error2)
print(bestff1)

print('')
    
# Part 1d
print('STRATEGY 2: (t1,t2,t3) = (0s, 5s, 10s) ; (x1,x2,x3) = (0.30m, 4.425m, 14.30m)')
tvec2 = np.array([0., 5., 10.])
xvec2 = np.array([0.30, 4.425, 14.30])
yuHH = matrixCreator(tvec2)
parameters2 = np.linalg.solve(yuHH,xvec2) # computing the resulting best-fit values of (v0, a)
print('Unknowns: x0, v0, a')
print(parameters2)

# Part 1e
# error estimtaion: upper-lower bound method
x1 = xvec2[0]
x2 = xvec2[1]
x3 = xvec2[2]
delta = 0.005 # measurement accuracy in position, delta_x = 0.005 m
error1 = np.array([x1, x2 - delta, x3 - delta]) # worst-case scenario as the parameters obtained for a lower bound: (x1, x2 - delta_x, x3 - delta_x)
print('Lower Bound of x')
print(error2)
print('LB Resulting best fit values: v0, a')
bestff1 = np.linalg.solve(yuHH, error1)
print(bestff1)
error2 = np.array([x1, x2 + delta, x3 + delta]) # worst-case scenario as the parameters obtained for a upper bound: (x1, x2 + delta_x, x3 + delta_x)
print('Upper Bound of x')
print(error2)
print('UB Resulting best fit values: v0, a')
bestff2 = np.linalg.solve(yuHH, error2)
print(bestff2)