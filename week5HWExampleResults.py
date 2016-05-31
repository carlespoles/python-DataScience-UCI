'''
Created on May 3, 2016

@author: Carles Poles-Mielgo

Homework Week 5 - To test results
'''
import Carles_Poles_Mielgo_week5 as week5Functions
import numpy as np

A = np.array([[0.31903967, 0.49385635], [0.13983727, -0.40484725]])

print week5Functions.findSDArray(A)

print week5Functions.normalizeArray(A)

print week5Functions.negativesToZero(A)

# Below is an example.

'''
A = np.random.rand(3, 1) - 0.5

B = np.random.rand(3, 1) - 0.5

C = np.random.rand(3, 1)

print '\n', A

print '\n', B

print '\n', C

I = np.all([A > 0, B > 0], axis=0)

print '\n', I

I = np.reshape(I, (3,))

print '\n', I

print '\n', C[I, :]

'''
