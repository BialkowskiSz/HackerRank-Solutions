#!/bin/python3

import sys

def extraLongFactorials(n):
    result = 1
    if n == 0 or n == 1:
        print(result)
        return
    
    for i in range(2, n+1):
        result *= i
    print(result)

if __name__ == "__main__":
    n = int(input().strip())
    extraLongFactorials(n)

