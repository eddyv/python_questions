#!/bin/python3

import math
import os
import random
import re
import sys

''' 
return the resulting array of integers.

rotLeft has the following parameter(s):

    An array of integers 'a'
    An integer 'd', the number of rotations.
'''
def rotLeft(a, d):
  #pops the first element from the list and adds it to the end.
  for i in range(0,d):
    a.append(a.pop(0))
  return a

def rotLeftIndexSliced(a,d):
  # return the items from the 'd'th element to the end + the items from the beginning to the 'd'th element
  return a[d:] + a[:d]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeftIndexSliced(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
