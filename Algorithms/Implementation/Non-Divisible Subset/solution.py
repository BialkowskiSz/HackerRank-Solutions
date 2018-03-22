#!/bin/python3

# Copyright (c) 2018 Szymon Bialkowski
# Authors: Szymon Bialkowski
# Date: 18/03/2018

"""
calculate number & k and place into frequency hashmap
if k = 3 we can't have 1 + 2 together, so pick higher frequency
we can always have one 0 (1 + 0 == 1) but not two 0s (0 + 0 == 0)

Complexity: O(n+k) time and O(k) space
"""

import sys

def nonDivisibleSubset(k, arr):
    length = len(arr)
    if length == 0 or length == 1:
        return length

    greatestSubset  = 0
    modFreq    = {}

    for number in arr:
        leftOver = number%k
        if leftOver in modFreq:
            modFreq[leftOver] += 1
        else:
            modFreq[leftOver] = 1

    # Can never have 2 halfs of a number but can always have 1
    if k % 2 == 0:
        var = k / 2
        if var in modFreq:
            var = modFreq[var] - 1
            greatestSubset -= var


    for freq in modFreq:
        if freq != 0 and modFreq[freq] != 0:
            diff = k - freq
            if diff in modFreq:
                if modFreq[diff] != 0:
                    freqValue = modFreq[freq]
                    diffValue = modFreq[diff]
                    if freqValue >= diffValue:
                        modFreq[diff] = 0
                        greatestSubset += freqValue
                    else:
                        modFreq[freq] = 0
                        greatestSubset += diffValue
            else:
                greatestSubset += modFreq[freq]

    # Can never have 2 zeros but can always have 1
    if 0 in modFreq:
        greatestSubset += 1


    return greatestSubset


if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, raw_input().strip().split(' ')))
    result = nonDivisibleSubset(k, arr)
    print(result)
