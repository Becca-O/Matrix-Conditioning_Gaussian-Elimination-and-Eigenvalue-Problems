#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 19:14:53 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 5e

import numpy as np
import matplotlib.pyplot as plt

# Part 1b
def CreateSystem(kvec,mvec):
    n = mvec.shape[0]
    A = np.zeros((n, n))
    A[0][0] = (-kvec[0]-kvec[1])/mvec[0]
    A[0][1] = kvec[1]/mvec[0]
    A[n-1][n-1] = (-kvec[n-1]-kvec[n])/mvec[n-1]
    A[n-1][n-2] = kvec[n-1]/mvec[n-1]
    for i in range(1, n-1, 1):
        A[i][i-1] = kvec[i]/mvec[i]
        A[i][i] = (-kvec[i]-kvec[i+1])/mvec[i]
        A[i][i+1] = kvec[i+1]/mvec[i]
    return A

#Part 1e
def marray(n):
    mvec = np.zeros(n)
    for i in range(n):
        if i % 2 == 1:
            mvec[i] = 1.0
        if i % 2 == 0:
            mvec[i] = 1.5
    return mvec

def karray(n):
    mvec = np.zeros(n)
    for i in range(n):
            mvec[i] = 1.0
    return mvec

yuH = CreateSystem(karray(1001), marray(1000))
eigen = np.linalg.eig(CreateSystem(karray(1001), marray(1000)))
eigenvalues, eigenvectors = eigen
#print('Eigenvalues')
#print(eigenvalues)
#print('')
#print('Eigenvectors')
#print(eigenvectors)

plt.hist(x=eigenvalues, bins=500) # bins must be narrow enough to observe relevant features
plt.title('Histogram Plot of the Eigenvalues with m2 1.5 times m1')
plt.xlabel('Eigenvalues')
plt.ylabel('Number of Occurances')
plt.ylim([0,30])
plt.show()




def marray(n):
    mvec = np.zeros(n)
    for i in range(n):
        if i % 2 == 1:
            mvec[i] = 1.0
        if i % 2 == 0:
            mvec[i] = 1.2
    return mvec

def karray(n):
    mvec = np.zeros(n)
    for i in range(n):
            mvec[i] = 1.0
    return mvec

yuH = CreateSystem(karray(1001), marray(1000))
eigen = np.linalg.eig(CreateSystem(karray(1001), marray(1000)))
eigenvalues, eigenvectors = eigen
#print('Eigenvalues')
#print(eigenvalues)
#print('')
#print('Eigenvectors')
#print(eigenvectors)

plt.hist(x=eigenvalues, bins=500)
plt.title('Histogram Plot of the Eigenvalues with m2 1.2 times m1')
plt.xlabel('Eigenvalues')
plt.ylabel('Number of Occurances')
plt.ylim([0,30])
plt.show()