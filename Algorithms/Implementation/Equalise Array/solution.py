#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 25/03/2018

"""
Count up frequencys in HashMap
Determine most frequent element
Length - most frequent = Number of deletions

Complexity: O(nk) time and O(k) where k is distinct numbers
"""

def equaliseArray(a):
    
    length = len(a)
    if length == 0 or length == 1:
        return 0

    frequencys = {}

    for i in a:
        if i in frequencys:
            frequencys[i] += 1
        else:
            frequencys[i] = 1
    
    maxFreq = 0
    for i in frequencys.values():
        if i > maxFreq:
            maxFreq = i
    return length - maxFreq


if __name__ == "__main__":
    n   = int(raw_input().strip())
    arr = [ int(i) for i in raw_input().strip().split(' ') ]
    result = equaliseArray(arr)
    print(result)


