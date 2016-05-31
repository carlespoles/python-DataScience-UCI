'''
Created on Apr 18, 2016

@author: Carles Poles-Mielgo

Homework Week 2 - To test results
'''

import Carles_Poles_Mielgo_week2 as week2Functions

result = week2Functions.stringEvenOrOdd('dog')
print result
# odd

result = week2Functions.stringEvenOrOdd('food')
print result
# even

result = week2Functions.lowerList(['HaPPy', 'DaY', 'TOday'])
print result
# ['happy', 'day', 'today']

result = week2Functions.wordCount('I love to go to the park and walk my dog. \
My dog will play with other dogs in the park.')
print result
# {'and': 1, 'dog.': 1, 'play': 1, 'love': 1, 'I': 1, 'my': 1, 'park': 1,'dog': 1,'walk': 1, 'will': 1, 'to': 2, 'with': 1, 'other': 1, 'in': 1, 'go': 1, 'the': 2, 'My': 1, 'dogs': 1, 'park.': 1}

result = week2Functions.tupleCounts2Percents([('CA', 1001), ('NY', 145), ('AZ', 123)])
print result
# [('CA', 0.7888100866824271), ('NY', 0.11426319936958235), ('AZ', 0.09692671394799054)]

result = week2Functions.tupleTagCounts([('love', 'family'), ('lunch', 'family', 'nomnom'), ('wedding', 'romance', 'love', 'lunch', 'nomnom')])
print result
# [('love', 2), ('family', 2), ('nomnom', 2), ('lunch', 2)]

result = week2Functions.list2Unique([1, 2, 'Pizza', 'Pizza', 2, 'drinks'])
print result
# [1, 2, 'Pizza', 'drinks']

result = week2Functions.cumulativeSum([1.2, 5, 29])
print result
# 35.2

result = week2Functions.returnWordsBetween('<tag>','</tag>','not important <tag> really important </tag> and more')
print result
# ['really', 'important']