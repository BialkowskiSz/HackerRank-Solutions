#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 07/05/2018

"""
Calculate initial chocolate purchase
While has enough wrappers add them to total
"""

import sys

def chocolateFeast(n, c, m):
    totalChocolates = wrappers = n // c
    while wrappers >= m:
        chocalates = wrappers // m
        wrappers %= m
        totalChocolates += chocalates
        wrappers += chocalates
        
    return totalChocolates

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = input().strip().split(' ')
        n, c, m = [int(n), int(c), int(m)]
        result = chocolateFeast(n, c, m)
        print(result)
