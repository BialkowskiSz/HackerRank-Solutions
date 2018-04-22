#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 22/04/2018

"""
Iterate through each combination of strings
Iterate through number of topics
Count and push to max heap
while pop == pop count++


Complexity: O(n^2m) time and O(x) space where x is number of possible teams
"""
import sys, heapq

def acmTeam(topic):
    if not topic:
        return (0,0)
    
    heap = []
    length = len(topic)
    stringLength = len(topic[0])
    
    for i in range(length-1):
        for j in range(i+1, length):
            counter = 0
            for z in range(stringLength):
                if topic[i][z] == '1' or topic[j][z] == '1':
                    counter += 1
            heapq.heappush(heap, -1*counter)
    
    counter = 1
    biggest = heapq.heappop(heap)
    while biggest == heapq.heappop(heap):
        counter += 1
    
    return (abs(biggest), counter)

if __name__ == "__main__":
    n, m = raw_input().strip().split(' ')
    n, m = [int(n), int(m)]
    topic = []
    topic_i = 0
    for topic_i in xrange(n):
        topic_t = str(raw_input().strip())
        topic.append(topic_t)
    result = acmTeam(topic)
    print "\n".join(map(str, result))


