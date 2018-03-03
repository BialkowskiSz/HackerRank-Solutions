#!/bin/python3

import sys

#   Approach:   Reverse sort array.
#               Lowest value always at the tail
#               Truncate tail index if (value - min value) <= 0

def cutTheSticks(array):
    array.sort(reverse=True)
    length = len(array)
    minValue = array[length-1]
    
    while length > 0:
        for i in range(length):
            array[i] -= minValue
            if array[i] <= 0:
                length -= 1
        minValue = array[length-1]
        print(i+1)
        

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    cutTheSticks(arr)



