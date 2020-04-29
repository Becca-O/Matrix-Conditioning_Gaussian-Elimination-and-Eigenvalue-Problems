#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 13:29:49 2018

@author: beccers
"""

# Rebecca Olson
# Homework 7, Problem 1?

import numpy as np

def checkConditioning(tvec):
    t1 = tvec[0]
    t2 = tvec[1]
    t3 = tvec[2]
    matrix = np.array([[1, t1, 0.5*(t1**2)], [1, t2, 0.5*(t2**2)], [1, t3, 0.5*(t3**2)]])
    
    #MATRIX OF MINORS/COFACTORS
    det1 = np.linalg.det(np.array([[t2, 0.5*(t2**2)], [t3, 0.5*(t3**2)]]))
    det2 = np.linalg.det(np.array([[1, 0.5*(t2**2)], [1, 0.5*(t3**2)]]))
    det3 = np.linalg.det(np.array([[1, t2], [1, t3]]))
    det4 = np.linalg.det(np.array([[t1, 0.5*(t1**2)], [t3, 0.5*(t3**2)]]))
    det5 = np.linalg.det(np.array([[1, 0.5*(t1**2)], [1, 0.5*(t3**2)]]))
    det6 = np.linalg.det(np.array([[1, t1], [1, t3]]))
    det7 = np.linalg.det(np.array([[t1, 0.5*(t1**2)], [t2, 0.5*(t2**2)]]))
    det8 = np.linalg.det(np.array([[1, 0.5*(t1**2)], [1, 0.5*(t2**2)]]))
    det9 = np.linalg.det(np.array([[1, t1], [1, t2]]))
    # matrixOfMinors = np.array([[det1, det2, det3], [det4, det5, det6], [det7, det8, det9]])
    # matrixOfCofactors = np.array([[det1, -1*det2, det3], [-1*det4, det5, -1*det6], [det7, -1*det8, det9]])
    
    # TRANSPOSE
    transpose = np.array([[det1, -1*det4, det7], [-1*det2, det5, -1*det8], [det3, -1*det6, det9]])

    # INVERSE
    inverse = (1/(np.linalg.det(matrix))) * transpose
    print(inverse)
    
    # Ax = b
    # (A^-1)Ax = (A^-1)b
    # x = (A^-1)b
    
    x = ???? YOU NEED xi to compute the unknowns
    

tvecTest = np.array([16., 36., 96.])
x = checkConditioning(tvecTest)