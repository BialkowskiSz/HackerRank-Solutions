#!/bin/python

import sys

def queensAttack(n, k, rQ, cQ, obstacles):
    if n == 0 or n == 1:
        return 0

    top, bottom, left, right = [ n, 0, 0, n ]
    # Whichever one is closer to the edge will collied
    topRight = n - cQ if cQ >= rQ else n - rQ
    topLeft  = cQ - 1 if cQ <= rQ else rQ - 1
    bottomLeft, bottomRight  = [ 0, 0 ]

    for obstacle in obstacles:
        if cQ == obstacle[1]:
            if rQ < obstacle[0]:
                if top > obstacles[0]:
                    top = obstacles[0]
            else:
                if bottom < obstacle[0]:
                    bottom = obstacles[0]
        elif rQ == obstacle[0]:
            if cQ < obstacles[1]:
                if right > obstacles[1]:
                    right = obstacles[1]
            else:
                if left < obstacles[1]:
                    left = obstacles[1]

        queensDiagonal = obstacle[0] - rQ

        elif queensDiagonal == obstacle[1] - cQ:
            if queensDiagonal > 0:
                if topRight > queensDiagonal:
                    topRight = queensDiagonal
            else:
                if bottomLeft < obstacle[0] - rQ:
                    bottomLeft = queensDiagonal


if __name__ == "__main__":
    n, k      = [ int(i) for i in input().strip().split(' ') ]
    r_q, c_q  = [ int(i) for i in input().strip().split(' ') ]
    obstacles = [ ]
    for obstacle in range(k):
        obstacles_temp = map(int, input().split().strip(' '))
        obstacles.append(obstacles_temp)
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)

