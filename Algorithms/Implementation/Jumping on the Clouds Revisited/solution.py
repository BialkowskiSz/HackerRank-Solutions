#!/bin/python3

import sys

def jumpingOnClouds(array, jumpStep):
    energy          = 100
    normalCloud     = 0
    currentCloud    = 0
    sizeOfArray     = len(array)
    
    if sizeOfArray == 0:
        return energy
    
    while True:
        currentCloud = (currentCloud + jumpStep) % sizeOfArray
        if array[currentCloud] == normalCloud:
            energy -= 1
        else:
            energy -= 3
        if currentCloud == 0:
            return energy
        

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    c = list(map(int, input().strip().split(' ')))
    result = jumpingOnClouds(c, k)
    print(result)

