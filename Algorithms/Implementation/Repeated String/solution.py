#!/bin/python3

import sys

def repeatedString(s, n):
    
    length          = len(s)
    frequency       = 0
    searchLetter    = 'a'
    
    if n <= length:
        for i in range(n):
            if s[i] == searchLetter:
                frequency += 1
        return frequency
    
    #   (character in string * string repeats) + left over characters
    roundDown       = n // length
    modulus         = n % length
    leftOver        = 0
    
    for i, value in enumerate(s):
        if value == searchLetter:
            frequency += 1
            if i < modulus:
                leftOver += 1

    return (frequency * roundDown) + leftOver
            
    

if __name__ == "__main__":
    s = input().strip()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)

