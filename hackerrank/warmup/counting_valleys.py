#!/bin/python3

import math
import os
import random
import re
import sys

'''
return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):

    n: the number of steps Gary takes
    s: a string describing his path

    A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
    A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.

'''
def countingValleys(n, s):
  numValleys=0
  currLevel = 0

  for i in range(0,n):
    if s[i] == 'U':
      currLevel+=1
      if currLevel == 0:
        numValleys+=1
    elif s[i] == 'D':
      currLevel-=1

  return numValleys
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
