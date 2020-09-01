#!/bin/python3

import math
import os
import random
import re
import sys

'''
return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

    c: an array of binary integers

cumulus = 0
thundercloud = 1
'''


def jumpingOnClouds(c):
  cLength = len(c)
  if len(c) == 1 : return 0
  if len(c) == 2 :
    if c[1]== 0:
      return 1
    else:
      return 0
  # truncate the array by removing the first two elements
  # If you cant take two steps, take 1 step
  if c[2] == 0:
    return 1 + jumpingOnClouds(c[2:])
  elif c[1] == 0:
    return 1 + jumpingOnClouds(c[1:])
  return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
