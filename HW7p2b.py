#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 00:10:37 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 2b

import numpy as np

# this function inputs an nxn matrix "Ainput" and an nx1 column matrix "binput"
# it performs Gaussian elimination and outputs the eliminated new matrices A and b
# where "A" is nxn upper triangular, and "b" is an nx1 column matrix
def GaussElimin(Ainput,binput):
    n=len(binput)
    A = Ainput.copy() # make copies so as not to write over originals
    b = binput.copy()
    # loop over pivot rows from row 1 to row n-1 (i to n-2)
    for i in range(0,n-1):
        # loop over row to be zero'ed from row j+1 to n (j+1 to n-1)
        for j in range(i+1,n):
            c = A[j,i]/A[i,i] # multiplicative factor to zero point
            A[j,i] = 0.0 # we know this element goes to zero
            A[j,i+1:n]=A[j,i+1:n]-c*A[i,i+1:n] # do subtraction of two rows
            b[j] = b[j]-c*b[i] # do substraction of b's as well
    return (A,b)  # return modified A and b

A1 = np.array([[4., -2., 1.], [-3., -1., 4.], [1., -1., 3.]]) # given example matrix, A1
origA1 = A1.copy() # making copies so as not to write over originals (used later to confirm solution)
b1 = np.array([[15.], [8.], [13.]]) # given example matrix, b1 (must be a column vector to use the dot product correctly)
origb1 = b1.copy()
x1 = np.array([[2.], [-2.], [3.]]) # provided solution, x1 (also must be a column vector to use the dot product correctly)
origx1 = x1.copy()
# variable type must be float (integer type would cause too much round-off error)
test1 = GaussElimin(A1, b1) # outputs a new upper triangular matrix via gaussian elimination (modified A1) and its corresponding b martix (modified b1)
A2, b2 = test1 # re-naming the modified A1 as A2, and the modified b1 as b2
print('Modified A1: Upper triangular matrix, A2')
print(A2) 
print('')
print('Modified b1: Column Matrix, b2')
print(b2) 
print('')
print('Matrix b via dot(A2, Given x1)')
b1 = np.dot(A2, x1) # comparing the b2 obtained via GaussElimin with the b obtained by dotting A2 (the modified matrix) with the given solution x1
print(b1)
# both b martices are the same = good

print('')

print('FURTHER VALIDATION:')
print('x: dot(Inverse of A1, Original b1)')
invA1 = np.linalg.inv(origA1)
x = np.dot(invA1, origb1) # the dot product of the original A1 matrix and the original b matrix
print(x)
print('')
print('x: dot(Inverse of A2, b2)')
invA2 = np.linalg.inv(A2)
x = np.dot(invA2, b2) # the dot product of the modified matrix, A2, and the modified b matrix, b2
print(x)
# the solutions, x, are the same = good