#!/bin/python

import sys

def jumpingOnClouds(array):
    length = len(array)

    if length == 0 or length == 1:
        return length
    elif length == 2:
        return 1
    elif length == 3:
        return 2

    counter = steps = 0
    while counter < length - 1:
        if counter >= length - 2:
            return steps + 1
        if array[counter + 2] == 1:
            counter += 1
        else:
            counter += 2
        steps += 1

    return steps


if __name__ == "__main__":
    n = int(input().split())
    c = map(int, input().strip().split(' '))
    result = jumpingOnClouds(c)
    print(result)
