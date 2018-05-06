#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 06/05/2018

"""
Store numbers in HashSet
Iterate through elements and if element + d and element + d + d in hashSet then valid triplet

Complexity: O(n) time and O(n) space
"""

import sys

def beautifulTriplets(d, arr):
    hashSet = set()
    triplets = 0
    
    for element in arr:
        if element not in hashSet:
            hashSet.add(element)
            
    for element in arr:
        second = element + d
        third  = second  + d
        if second in hashSet and third in hashSet:
            triplets += 1
            
    return triplets
                        

if __name__ == "__main__":
    n, d = [ int(i) for i in input().strip().split(' ') ]
    arr =  [ int(i) for i in input().strip().split(' ') ]
    result = beautifulTriplets(d, arr)
    print(result)
