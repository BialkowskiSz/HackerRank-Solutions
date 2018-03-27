#!/bin/python

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 27/03/2018

def TaumBday(b, w, x, y, z):

    if b | w == 0:
        return 0

    minBlackCost = x if (y+z) >= x else (y+z)
    minWhiteCost = y if (x+z) >= y else (x+z)

    return (b * minBlackCost) + (w * minWhiteCost)

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in range(t):
        b, w    = [ int(number) for number in raw_input().strip().split(' ') ]
        x, y, z = [ int(number) for number in raw_input().strip().split(' ') ] 
        result = TaumBday(b, w, x, y, z)
        print(result)
