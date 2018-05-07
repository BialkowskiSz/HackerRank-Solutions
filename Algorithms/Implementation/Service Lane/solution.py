#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 07/05/2018

"""
For each case iterate through a slice of start to end widths
Check for min

Complexity: O(cw) time and O(1) space where c is cases and w is widths
(Although we iterate through the minimum slice of widths)
"""
import sys

def serviceLane(n, cases, widths):
    results = []
    
    for case in cases:
        start = case[0]
        end   = case[1] + 1         #Inclusive
        smallest = widths[start]
        for width in widths[start+1:end:]:
            if width < smallest:
                smallest = width
        results.append(smallest)
        
    return results
    
            

if __name__ == "__main__":
    n, t = input().strip().split(' ')
    n, t = [int(n), int(t)]
    widths = list(map(int, input().strip().split(' ')))
    cases = []
    for cases_i in range(t):
       cases_t = [int(cases_temp) for cases_temp in input().strip().split(' ')]
       cases.append(cases_t)
    result = serviceLane(n, cases, widths)
    print ("\n".join(map(str, result)))


