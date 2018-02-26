#!/bin/python3

import sys
from math import sqrt, ceil

"""
Get square root of lowest number, round up,
check if between a and b using range
and increment root
"""
def squares(a, b):
    count   = 0
    myRange = range(a, b+1)
    root    = ceil(sqrt(a))
    while (root*root) in myRange:
        count   += 1
        root    += 1
    return count

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        a, b = input().strip().split(' ')
        a, b = [int(a), int(b)]
        result = squares(a, b)
        print(result)

