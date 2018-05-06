#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 06/05/2018

"""
HashMap keeps track of duplicates and their indexes
Calculate distance and check if less than minDistance
No protection against values which appear more than twice.

Complexity: O(n) time and O(n) space where n is the size of the array
"""
import sys

def minimumDistances(array):
    hashMap = {}
    minDistance = len(array)
    
    for index, value in enumerate(array):
        if value in hashMap:
            distance = abs(hashMap[value] - index)
            if distance < minDistance:
                minDistance = distance
        else:
            hashMap[value] = index
            
    if minDistance == len(array):
        return -1
    return minDistance
                
    
if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = minimumDistances(a)
    print(result)
