#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
''' 
return an integer representing the number of occurrences of the character 'a' in the prefix of length n

in the infinitely repeating string.

repeatedString has the following parameter(s):

    s: a string to repeat
    n: the number of characters to consider

'''


def repeatedString(s, n):
    stringLength = len(s)
    # the number of times to repeat the string
    stringMultiplier = n // stringLength

    # the number of times the string would need to be repeated multiplied by the number of 'a's in the original string
    numAs = s.count('a') * stringMultiplier
    # the number of 'a's in the remainder of the string after being multiplied
    numAs += s[:n % stringLength].count('a')

    return numAs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
