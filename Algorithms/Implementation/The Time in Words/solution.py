#!/bin/python3

# Authors: Szymon Bialkowski
#      github.com/BialkowskiSz
# Date: 07/05/2018

"""
Number to word dict
Keywords as variables
Check for abnormalities else calculate

Complexity: O(1) time and O(1) space
"""

import sys

numberWord = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",21:"twenty one",22:"twenty two",23:"twenty three",24:"twenty four",25:"twenty five",26:"twenty six",27:"twenty seven",28:"twenty eight",29:"twenty nine", 30:"thirty"}

to      = "to"
past    = "past"
half    = "half"
space   = " "
oclock  = "o' clock"
quarter = "quarter"
minute  = "minute"
minutes = "minutes"

def timeInWords(h, m):
    result = ""
    if m == 0:
        result = numberWord[h] + space + oclock
    elif m == 30:
        result = half + space + past + space + numberWord[h]
    elif m == 15:
        result = quarter + space + past + space + numberWord[h]
    elif m == 45:
        result = quarter + space + to + space + numberWord[h+1]
    else:
        if m < 30:
            if m == 1:
                result = numberWord[m] + space + minute + space + past + space + numberWord[h]
            else:
                result = numberWord[m] + space + minutes + space + past + space + numberWord[h]
        else:
            if m == 59:
                result = numberWord[60-m] + space + minute + space + to + space + numberWord[h+1]
            else:
                result = numberWord[60-m] + space + minutes + space + to + space + numberWord[h+1]
            
    return result

if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
