#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 29/04/2018

"""
Use string slicing to split number

Complexity: O(q-p) time and O(1) space
"""

import sys

def kaprekarNumbers(p, q):
    results = []
    for i in range(p, q+1):
        if i > 3:
            sq    = str(i*i)
            sqLen = len(sq)
            d     = len(str(i))
            if (int(sq[:sqLen-d:]) + int(sq[sqLen-d:sqLen:]))== i:
                results.append(str(i))
        elif i == 1:
            results.append("1")
    if results:
        return(" ".join(results))
    return "INVALID RANGE"
    
        
    
if __name__ == "__main__":
    p = int(raw_input().strip())
    q = int(raw_input().strip())
    print(kaprekarNumbers(p, q))


