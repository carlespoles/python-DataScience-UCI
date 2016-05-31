'''
Created on Apr 19, 2016

@author: Carles Poles-Mielgo

Homework Week 3 - To test results
'''

import Carles_Poles_Mielgo_week3 as week3Functions
import pandas as pd
import numpy as np

pd.set_option('display.width', 200)

print week3Functions.loadAndPrepData('D:\\LiClipse Workspace\\UCIIntroPythonDataScience\\United+States+Cancer+Statistics%2C+1999-2011+Incidence.txt')

print week3Functions.onlyOneState('D:\\LiClipse Workspace\\UCIIntroPythonDataScience\\United+States+Cancer+Statistics%2C+1999-2011+Incidence.txt', 'Alabama')

print week3Functions.cancerSums('D:\\LiClipse Workspace\\UCIIntroPythonDataScience\\United+States+Cancer+Statistics%2C+1999-2011+Incidence.txt')

print week3Functions.cancerSumsBis('D:\\LiClipse Workspace\\UCIIntroPythonDataScience\\United+States+Cancer+Statistics%2C+1999-2011+Incidence.txt')

print week3Functions.stateCountAsList('D:\\LiClipse Workspace\\UCIIntroPythonDataScience\\United+States+Cancer+Statistics%2C+1999-2011+Incidence.txt', 'Alabama')

print week3Functions.getStateCountsDF('D:\\LiClipse Workspace\\UCIIntroPythonDataScience\\United+States+Cancer+Statistics%2C+1999-2011+Incidence.txt')

print week3Functions.plotCounts('D:\\LiClipse Workspace\\UCIIntroPythonDataScience\\United+States+Cancer+Statistics%2C+1999-2011+Incidence.txt')