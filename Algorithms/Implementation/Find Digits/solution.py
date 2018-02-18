
#!/bin/python3

import sys

def findDigits(number):
    numberString    = str(number)
    
    if len(numberString) == 0:
        return 0
    
    numbersSplit    = [ int(i) for i in numberString ]
    count           = 0
    
    for i in numbersSplit:
        if i != 0:
            if (number % i) == 0:
                count += 1
    return count
            
    

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        result = findDigits(n)
        print(result)
