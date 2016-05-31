'''
Created on Apr 18, 2016

@author: Carles Poles-Mielgo

Homework Week 2
'''
from __future__ import division
# 1


def stringEvenOrOdd(inputString):
    if len(inputString) % 2 == 0:
        result = 'even'
    else:
        result = 'odd'
    return result

# 2


def lowerList(inputList):
    for i in range(len(inputList)):
        inputList[i] = inputList[i].lower()
    return inputList

# 3


def wordCount(inputString):
    # Line below in case we need to lower case the input.
    # Comment if not required.
    inputString = inputString.lower()
    dictString = {}
    for word in inputString.split():
        if word in dictString:
            dictString[word] += 1
        else:
            dictString[word] = 1
    return dictString

# 4


def tupleCounts2Percents(inputList):
    totalSum = 0
    newList = []
    for i in range(len(inputList)):
        totalSum = totalSum + inputList[i][1]
    for i in range(len(inputList)):
        newList.append((inputList[i][0], inputList[i][1]/totalSum))
    return newList

# 5


def tupleTagCounts(inputList):
    newList = []
    dictString = {}
    for i in range(len(inputList)):
        for j in range(len(inputList[i])):
            if inputList[i][j] in dictString:
                dictString[inputList[i][j]] += 1
            else:
                dictString[inputList[i][j]] = 1
    for key, value in dictString.iteritems():
        if value > 1:
            newList.append((key, value))
    return newList

# 6


def list2Unique(inputList):
    distinctList = []
    for x in inputList:
        if x not in distinctList:
            distinctList.append(x)
    return distinctList

# 7


def cumulativeSum(inputList):
    totalSum = 0
    for x in range(len(inputList)):
        totalSum = totalSum + inputList[x]
    return totalSum

# 8


def returnWordsBetween(firstWord, secondWord, inputString):
    start = inputString.split().index(firstWord)
    end = inputString.split().index(secondWord)
    finalString = inputString.split()[start + 1:end]
    return finalString
