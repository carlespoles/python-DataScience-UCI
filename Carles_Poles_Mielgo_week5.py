'''
Created on May 3, 2016

@author: Carles Poles-Mielgo

Homework Week 5
'''
import numpy as np

# 1


def findSDArray(A):
    B = np.nanstd(A, axis=0)
    return B


# 2


def normalizeArray(A):
    B = findSDArray(A)
    return A/B


# 3


def negativesToZero(A):
    A[A < 0] = 0
    return A
