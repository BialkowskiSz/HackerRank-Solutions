#!/bin/python

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 19/04/2018

"""
Use string slicing to skip to next column

Complexity: O(c) time and O(n) space where c = columns and n = length of array
"""

import sys
import math

def encryption(s):
    s = s.strip(" ")
    L = len(s)
    returnArray = []
    if L < 1:
        return "Impossible"
    
    rootL   = math.sqrt(L) 
    rows    = int(math.floor(rootL))
    columns = int(math.ceil(rootL))

    for i in range(columns):
        returnArray.append(s[i::columns])

    return ' '.join(returnArray)
        

if __name__ == "__main__":
    s = raw_input().strip()
    result = encryption(s)
    print result
