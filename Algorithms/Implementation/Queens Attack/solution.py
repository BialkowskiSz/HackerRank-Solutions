#!/bin/python3

# Copyright (c) 2018 Szymon Bialkowski
# Authors: Szymon Bialkowski
# Date: 23/03/2018

"""
Calculate max attacks in each direction in constant time
For each obstacle find if on attack lines
If blocks left after obstacle then put into max attack variables
Add all variables

Complexity: O(k) time and O(1) space
"""

import sys

def queensAttack(n, k, rQ, cQ, obstacles):
    if n == 0 or n == 1:
        return 0

    top, bottom, left, right = [ n-rQ, rQ-1, cQ-1, n-cQ ]
    topRight    = top    if top <= right    else right
    topLeft     = top    if top <= left     else left
    bottomLeft  = bottom if bottom <= left  else left
    bottomRight = bottom if bottom <= right else right

    for obstacle in obstacles:

        queensDiagonal = obstacle[0] - rQ

        #   Top and bottom
        if cQ == obstacle[1]:
            if rQ < obstacle[0]:
                blocksLeft = (obstacles[0]-(rQ-1))
                if top > blocksLeft:
                    top = blocksLeft
            else:
                blocksLeft = (rQ-obstacles[0]-1)
                if bottom > blocksLeft:
                    bottom = blocksLeft

        #   Left and right
        elif rQ == obstacle[0]:
            if cQ < obstacles[1]:
                blocksLeft = (obstacles[1]-cQ-1)
                if right > blocksLeft:
                    right = blocksLeft
            else:
                blocksLeft = (cQ-obstacles[1]-1)
                if left > blocksLeft:
                    left = blocksLeft

        #   TopRight and BottomRight diagonals
        elif queensDiagonal == (obstacle[1] - cQ):
            if queensDiagonal > 0:
                blocksLeft = queensDiagonal-1
                if topRight > blocksLeft:
                    topRight = blocksLeft
            else:
                blocksLeft = abs(queensDiagonal)-1
                if bottomLeft > blocksLeft:
                    bottomLeft = blocksLeft

        #   TopLeft and BottomRight diagonals
        elif (obstacle[0] + obstacle[1]) == (rQ + cQ):
            if rQ < obstacle[0]:
                blocksLeft = (obstacle[0]-rQ-1)
                if topLeft > blocksLeft:
                    topLeft = blocksLeft
            else:
                blocksLeft = (rQ-obstacle[0]-1)
                if bottomRight > blocksLeft:
                    bottomRight = blocksLeft

    return top + bottom + left + right + \
           topLeft + topRight + bottomRight + bottomLeft


if __name__ == "__main__":
    n, k      = [ int(i) for i in raw_input().strip().split(' ') ]
    r_q, c_q  = [ int(i) for i in raw_input().strip().split(' ') ]
    obstacles = [ ]
    for obstacle in range(k):
        obstacles_temp = [ int(i) for i in raw_input().strip().split(' ') ]
        obstacles.append(obstacles_temp)
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
