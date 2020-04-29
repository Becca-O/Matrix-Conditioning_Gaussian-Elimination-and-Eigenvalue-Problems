#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 15:41:00 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 1c

import numpy as np
import matplotlib.pyplot as plt

# Part 1b
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

# Part 1c
t1 = 0.
t2 = np.arange(0.1, 10., 0.01) # t2 over the entire possible range of t2
t3 = 10. # since the cart runs out of track after 10 seconds
yeaa = []

for element in t2:
    yeaa = np.append(yeaa, checkConditioning(np.array([t1, element, t3])))
      
plt.plot(t2, yeaa) # used to find out at what time t2 (the second measurement) should be taken
plt.title('Ratio, R, vs t2')
plt.xlabel('t2 (seconds)')
plt.ylabel('Ratio, R')
plt.grid(True)
plt.show()
# explores what happens with different ways of measuring the cart under acceleration

# same idea but uses a smaller range in order to zero in on what the function's exact maximum is
t1 = 0.
t2 = np.arange(4.7, 4.8, 0.01)
t3 = 10.
yeaa = []

for element in t2:
    yeaa = np.append(yeaa, checkConditioning(np.array([t1, element, t3])))

plt.plot(t2, yeaa, 'o')
plt.title('Zommed in: Ratio, R, vs t2')
plt.xlabel('t2 (seconds)')
plt.ylabel('Ratio, R')
plt.grid(True)
plt.show()
# t2 = 4.74 seconds suggests the best conditioning to within 0.01 seconds of accuracy