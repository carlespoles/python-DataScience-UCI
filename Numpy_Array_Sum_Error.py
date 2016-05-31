'''
Created on May 20, 2016

@author: Carles
'''
import numpy as np

bigList = range(0, 1000000)
A = np.array(bigList)

S = 0
for i in bigList:
    S += i

NS = A.sum()
NSA = np.int64(A.sum()).item()
NSB = np.uint32(A.sum()).item()
NSC = np.float64(A.sum()).item()
NSD = A.sum(dtype=np.int64)

# Note that S is the correct result, and the others render incorrect ones, because
# .sum() is numpy.int32 type, which is a limitation.
# The only way to fix it is by using .sum(dtype=np.int64).

print S, NS, NSA, NSB, NSC, NSD, type(S), type(NS), type(NSA), type(NSB), type(NSC), type(NSD)