'''
Created on Apr 19, 2016

@author: Carles Poles-Mielgo

Homework Week 3
'''
import pandas as pd
import numpy as np
# For plotting:
import matplotlib as mp
mp.use("TkAgg")
import matplotlib.pyplot as plt

# 1


def loadAndPrepData(filePath):
    # Load the file with first row as column headers, set the sep option to '\t'
    # because the data fields are separated by tab
    dataFrame = pd.read_csv(filePath, header=0, sep='\t')
    # Grab the first 638 rows, because the ending rows are just notes and not data
    df = dataFrame.iloc[:638, :]
    return df
# 2


def onlyOneState(filePath, state):
    df = loadAndPrepData(filePath)
    stateDF = df[df['State'] == state]
    return stateDF
# 3


def cancerSums(filePath):
    df = loadAndPrepData(filePath)
    cancerDict = {}
    # We select the columns of data we need.
    requiredData = df[['State', 'Count']]
    # We iterate the required dataframe.
    for index, row in requiredData.iterrows():
        if not(row['State'] in cancerDict):
            cancerDict[row['State']] = row['Count']
        else:
            cancerDict[row['State']] += row['Count']
    return cancerDict

# Similar function to previous one, but using File IO.


def cancerSumsBis(filePath):
    cancerDict = {}
    lineCount = 0
    with open(filePath, "r") as f:
        for line in f:
            # After line 639, there's no data, but junk that we need to avoid reading.
            if lineCount < 639:
                lineCount = lineCount + 1
                # We also want to skip the 1st line, which contains the headers.
                if lineCount != 1:
                    # We replace the " from the file.
                    line = line.replace('"', '').rstrip()
                    # Since this is a tab delimited file, we read values per line and store them in  a variable.
                    # Note that we use split('\t').
                    notes, cancer_sites, cancer_sites_code, state, state_code, year, year_code, count = line.split('\t')
                    # All variables are string type, so we need to convert to integer the count.
                    countNumber = int(count)
                    if not(state in cancerDict):
                        cancerDict[state] = countNumber
                    else:
                        cancerDict[state] += countNumber
        return cancerDict

# 4


def stateCountAsList(filePath, state):
    dfStateSubset = onlyOneState(filePath, state)
    # The years range is from 1999 to 2011:
    yearList = range(1999, 2012)
    countsList = []
    # Removing the .0 from the Year, Count columns on the dataframe.
    dfCount = dfStateSubset['Count'].astype(int)
    dfYear = dfStateSubset['Year'].astype(int)
    # To convert the dataframe to a list, we need first to convert to series.
    dfCount = pd.Series(dfCount).tolist()
    dfYear = pd.Series(dfYear).tolist()
    totalItems = len(dfCount)
    partialCount = 0
    for year in yearList:
        if not (year in dfYear):
            countsList.append(np.nan)
        else:
            if partialCount < totalItems:
                countsList.append(dfCount[partialCount])
                partialCount = partialCount + 1
    return countsList

# 5


def getStateCountsDF(filePath):
    df = loadAndPrepData(filePath)
    # Make sure the list of states is unique.
    dfState = df['State'].unique()
    # To convert to the dataframe to a list,we need first to convert to series.
    dfState = pd.Series(dfState).tolist()
    stateCounts = []

    for x in range(len(dfState)):
        dfStateCount = stateCountAsList(filePath, dfState[x])
        stateCounts.append(dfStateCount)

    newDataFrame = pd.DataFrame(stateCounts, index=[dfState])
    return newDataFrame

# 6


def plotCounts(filePath):
    df = getStateCountsDF(filePath)
    # We need to transpose the dataframe.
    dfT = df.transpose()
    dfT.plot(legend=False)
    return plt.show()
