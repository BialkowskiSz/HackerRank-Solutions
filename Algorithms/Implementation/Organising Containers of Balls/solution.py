#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 23/03/2018

def organizingContainers(container):
    lengths = {}
    hashMap = {}
    for pitIndex, pit in enumerate(container):
        pitBallCount = 0
        for ballIndex, ballCount in enumerate(pit):
            pitBallCount += ballCount
            if ballIndex in hashMap:
                hashMap[ballIndex] += ballCount
            else:
                hashMap[ballIndex] = ballCount
        if pitBallCount in lengths:
            lengths[pitBallCount] += 1
        else:
            lengths[pitBallCount] = 1

    for number in hashMap.values():
        if number not in lengths:
            return "Impossible"
        elif lengths[number] == 0:
            return "Impossible"
        lengths[number] -= 1
    return "Possible"


if __name__ == "__main__":
    q = int(raw_input().strip())
    for _ in range(q):
        n = int(raw_input().strip())
        container = []
        for container_i in range(n):
            number = [ int(i) for i in raw_input().strip().split(' ') ]
            container.append(number)
        result = organizingContainers(container)
        print(result)
