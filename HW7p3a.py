#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:57:07 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 3a

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