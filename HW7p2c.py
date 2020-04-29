#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 18:33:44 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 2c

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

# ORIGINAL MATRIX
A2 = np.array([[0., 2., 0., 1.], [2., 2., 3., 2.], [4., -3., 0., 1.], [6., 1., -6., -5.]]) # example matrix, A2
b2 = np.array([[0.], [-2.], [-7.], [6.]]) # example matrix, b2 (must be a column vector to use the dot product correctly)
x2 = np.array([[-0.5], [-1.], [1/3], [-2.]]) # provided solution, x2 (also must be a column vector to use the dot product correctly)
# variable type must be float (integer type would cause too much round-off error)
test2 = GaussElimin(A2, b2) # outputs a new upper triangular matrix via gaussian elimination (modified A2) and its corresponding b martix (modified b2)
A3, b3 = test2 # re-naming the modified A2 as A3, and the modified b2 as b3
print('ORIGINAL MATRIX')
print('Modified A2: Upper triangular matrix, A3')
print(A3)
print('')
print('Modified b2: Column Matrix, b3')
print(b3)
print('')
print('Matrix b via dot(A3, Given x2)')
b2 = np.dot(A3, x2) # comparing the modified b2 obtained via GaussElimin with the b obtained by dotting A3 (the modified matrix) with the given solution x2
print(b2)
##### yields an error because the diagonal is not zero #####

print('')
print('')
print('')

# MODIFIED MATRIX - Switched Row 1 with row 2, as well as 3 with 4 (the same changes were made to the b matrix)
print('MODIFIED MATRIX')
A2 = np.array([[2., 2., 3., 2.], [0., 2., 0., 1.], [6., 1., -6., -5.], [4., -3., 0., 1.]]) 
origA2 = A2.copy()
b2 = np.array([[-2.], [0.], [6.], [-7.]])
origb2 = b2.copy()
x2 = np.array([[-0.5], [1], [1/3], [-2]]) # x matrix stays the same (the answer does not change by preforming gaussian eliminations)
origx2 = x2.copy()
# variable type must be float (integer type would cause too much round-off error)
test2 = GaussElimin(A2, b2) # outputs a new upper triangular matrix via gaussian elimination (modified A2) and its corresponding b martix (modified b2)
A3, b3 = test2 # re-naming the modified A2 as A3, and the modified b2 as b3
print('Modified A2: Upper triangular matrix, A3')
print(A3)
print('')
print('Modified b2: Column Matrix, b3')
print(b3)
print('')
print('Matrix b via dot(A3, Given x2)')
b2 = np.dot(A3, x2) # comparing the modified b2 obtained via GaussElimin with the b obtained by dotting A3 (the modified matrix) with the given solution x2
print(b2)
# both b martices are the same = good

print('')

print('FURTHER VALIDATION:')
print('x: dot(Inverse of A2, Original b2)')
invA2 = np.linalg.inv(origA2)
x = np.dot(invA2, origb2)  # the dot product of the original A2 matrix and the original b matrix
print(x)
print('')
print('x: dot(Inverse of A3, b3)')
invA3 = np.linalg.inv(A3)
x = np.dot(invA3, b3) # the dot product of the modified matrix, A3, and the modified b matrix, b3
print(x)
# the solutions, x, are the same = good