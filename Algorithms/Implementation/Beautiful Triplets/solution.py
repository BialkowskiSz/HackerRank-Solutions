#!/bin/python3

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
