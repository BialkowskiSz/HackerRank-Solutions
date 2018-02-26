#!/bin/python3

import sys

def appendAndDelete(string, desiredString, operations):
    lengthString        = len(string)
    lengthDesiredString = len(desiredString)
    operationsRequired  = 0
    shortestString      = lengthString if lengthString < lengthDesiredString else lengthDesiredString
    sameIndex           = shortestString
    
    
    #   Determine first character which isn't the same
    for i in range(shortestString):
        if string[i] != desiredString[i]:
            sameIndex = i
            break
            
    
    #   Length of substring which differs
    lengthString        -= sameIndex
    lengthDesiredString -= sameIndex
    
    operationsRequired = lengthString + lengthDesiredString
    
    if lengthString > operations:
        return "No"
    
    if operationsRequired == operations:
        return "Yes"
    else:
        if sameIndex == 0:
            return "Yes"
        #   Technically 10 and 12 operations are the same since you just take away another and add it back
        if operationsRequired != 0:
            if ((operations % operationsRequired) % 2 == 0):
                return "Yes"
        print(sameIndex)
        return "No"
    
    
            
    
    

if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    result = appendAndDelete(s, t, k)
    print(result)

