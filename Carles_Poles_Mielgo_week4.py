'''
Created on May 3, 2016

@author: Carles Poles-Mielgo

Homework Week 4
'''
# For plotting:
import matplotlib as mp
mp.use("TkAgg")
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def makeMap(latList, lonList, cityList):
    minLon = -130
    minLat = 25
    maxLon = -60
    maxLat = 50

    # Below is used to offset a bit the labels of the cities, for projection='merc'.
    labelYOffset = -0.9
    labelXOffset = 0.8

    # Below is used to offset a bit the labels of the cities, for projection='cyl'.
    #labelYOffset = -0.4
    #labelXOffset = 0.8

    plt.figure(1, figsize=(15, 15))
    myMap = Basemap(minLon, minLat, maxLon, maxLat, projection='merc', resolution='h')
    myMap.drawcoastlines()
    # Below if we want to show counties.
    #myMap.drawcounties(linewidth=1, linestyle='solid', color='red')
    # Below if we want to show states.
    #myMap.drawstates(linewidth=2, linestyle='solid', color='green')
    myMap.drawcountries(linewidth=3, linestyle='solid', color='black')
    myMap.drawrivers(linewidth=1, linestyle='solid', color='blue')

    # Another nice option is shaderelief().
    #myMap.shadedrelief()
    myMap.etopo()

    myMap.scatter(latList, lonList, latlon=True, c='red', s=100)
    X, Y = myMap(latList, lonList)
    # The for loop is to add the text labels of the cities.
    for x, y, label in zip(X, Y, cityList):
        plt.text(x + labelXOffset, y + labelYOffset, label)

    return plt.show()


# Below is to test the above function.
# We could also pass minLon, minLat, maxLon and maxLat, but it would look
# a bit messy. So the function assumes this is for a map of the USA.

# Lists of latitudes and longitudes from http://www.worldatlas.com/aatlas/findlatlong.htm.
latitudes = [-87.37, -74.0, -118.14]
longitudes = [41.52, 40.42, 34.3]
# List of the names of the cities to plot.
labels = ['Chicago', 'New York', 'Los Angeles']

# Calling the function:
print makeMap(latitudes, longitudes, labels)
