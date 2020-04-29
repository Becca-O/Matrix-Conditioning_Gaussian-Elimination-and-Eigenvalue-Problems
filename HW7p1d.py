#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:42:08 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 1d

import numpy as np

# a new function very similar to checkConditioning that returns the matrix A given time values
def matrixCreator(tvec): # tvec is a numpy array (t1,t2,t3), the time values at which I plan to take my measurements
    t1 = tvec[0]
    t2 = tvec[1]
    t3 = tvec[2]
    A = np.array([[1, t1, 0.5*(t1**2)], [1, t2, 0.5*(t2**2)], [1, t3, 0.5*(t3**2)]])
    return A

# comparing two measurement strategies and their resulting x measurements
print('STRATEGY 1: (t1,t2,t3) = (0s, 1s, 10s) & (x1,x2,x3) = (0.30m, 0.665m, 14.30m)')
tvec1 = np.array([0., 1., 10.])
xvec1 = np.array([0.30, 0.665, 14.30])
yuH = matrixCreator(tvec1)
parameters1 = np.linalg.solve(yuH,xvec1) # solving the system to determine the best-fit parameters (x0, v0, a)
print('Unknowns: x0, v0, a')
print(parameters1)

print('')

print('STRATEGY 2: (t1,t2,t3) = (0s, 5s, 10s) ; (x1,x2,x3) = (0.30m, 4.425m, 14.30m)')
tvec2 = np.array([0., 5., 10.])
xvec2 = np.array([0.30, 4.425, 14.30])
yuHH = matrixCreator(tvec2)
parameters2 = np.linalg.solve(yuHH,xvec2) # solving the system to determine the best-fit parameters (x0, v0, a)
print('Unknowns: x0, v0, a')
print(parameters2)
# the outputted best-fit parameters for each scenario are the same