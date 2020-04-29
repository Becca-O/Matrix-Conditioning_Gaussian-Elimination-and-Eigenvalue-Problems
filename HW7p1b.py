#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 14:51:22 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 1b

import numpy as np

def checkConditioning(tvec): # tvec is a numpy array (t1,t2,t3), the time values at which I plan to take my measurements
    t1 = tvec[0]
    t2 = tvec[1]
    t3 = tvec[2]
    A = np.array([[1, t1, 0.5*(t1**2)], [1, t2, 0.5*(t2**2)], [1, t3, 0.5*(t3**2)]])
    det = np.linalg.det(A)
    
    # calculating the euclidian norm
    n = A.shape[0]
    s = 0.0
    for i in range(0, n, 1): # iterate through the rows
        for j in range(0, n, 1): # iterate through the columns
            s = s + (A[i][j])**2
    norm = np.sqrt(s)
    R = np.abs(det)/norm # a measure of “better” conditioning (larger values should produce more accurate and stable results) 
    return R # returns the ratio |det(A)|/norm(A)
    # if |det(A)| is much smaller than the norm of A, the sytem is ill-conditioned