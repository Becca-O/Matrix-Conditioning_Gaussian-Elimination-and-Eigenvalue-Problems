#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 22:43:04 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 3a

import numpy as np

#Part 3a

# this function inputs an nxn matrix "Ainput" and
# performs LU decomposition, outputing an upper triangular matrix, U, 
# and a lower triangular matrix of the multiplicative factors, L
def LUdecomp(Ainput):
    n=len(Ainput)
    U = Ainput.copy() # make copies so as not to write over originals
    L = Ainput.copy() # make copies so as not to write over originals
    for i in range(0, n):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1, n):
            c = U[j,i]/U[i,i] # multiplicative factor to zero point
            L[j,i] = c
            U[j,i] = 0.0 # we know this element goes to zero
            U[j,i+1:n]=U[j,i+1:n]-c*U[i,i+1:n] # do subtraction of two rows
            L[i,j] = 0.0
        L[i,i] = 1.0
    return (L,U)  # return modified form of A
# only requires a forward- and back-substitution for each b, once the matrix A has been decomposed

# Part 3b
# shows that the outputs from LUdecomp satisfy A = LU when inputting the arrays A1 and the modified A2 from Problem 2 
print('LU DECOMPOSITION OF MATRIX A1')
A1 = np.array([[4., -2., 1.], [-3., -1., 4.], [1., -1., 3.]])
test1 = LUdecomp(A1)
L, U = test1
print('Matrix L')
print(L)
print('Matrix U')
print(U)
print('Dot Product of L and U')
A = np.dot(L, U)
print(A)
print('Original Matrix, A1')
print(A1)

print('')
print('')

print('LU DECOMPOSITION OF MOFIFIED MATRIX A2')
A2 = np.array([[2., 2., 3., 2.], [0., 2., 0., 1.], [6., 1., -6., -5.], [4., -3., 0., 1.]])
test2 = LUdecomp(A2)
L, U = test2
print('Matrix L')
print(L)
print('Matrix U')
print(U)
print('Dot Product of L and U')
A = np.dot(L, U)
print(A)
print('Original Matrix, A2')
print(A2)