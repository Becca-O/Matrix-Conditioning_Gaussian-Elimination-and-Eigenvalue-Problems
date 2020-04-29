#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:29:09 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 5b

import numpy as np

# Part 1b
# inputs an (n+1)×1 vector of spring constants k, and an n × 1
# vector of masses, m
def CreateSystem(kvec,mvec):
    n = mvec.shape[0]
    A = np.zeros((n, n))
    A[0][0] = (-kvec[0]-kvec[1])/mvec[0] # first and last row must be hard coded as they do not follow the pattern
    A[0][1] = kvec[1]/mvec[0]
    A[n-1][n-1] = (-kvec[n-1]-kvec[n])/mvec[n-1]
    A[n-1][n-2] = -kvec[n-1]/mvec[n-1]
    for i in range(1, n-1, 1):
        A[i][i-1] = kvec[i]/mvec[i]
        A[i][i] = (-kvec[i]-kvec[i+1])/mvec[i]
        A[i][i+1] = kvec[i+1]/mvec[i]
    return A # outputs the n × n system matrix that I solved for in part a