#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:41:40 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 5d

import numpy as np

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

#Part 1c
kvec1 = np.array([[1.], [1.], [1.], [1.]])
mvec = np.array([[1.], [1.], [1.]])
eigen = np.linalg.eig(CreateSystem(kvec1, mvec)) # computing the eigenvalues and eigenvectors for an n = 3 system where all of the k’s and m’s equal 1 again
eigenvalues, eigenvectors = eigen
print('Eigenvalues')
print(eigenvalues)
print('')
print('Eigenvectors')
print(eigenvectors)