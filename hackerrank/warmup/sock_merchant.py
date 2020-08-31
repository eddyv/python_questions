#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.

'''
It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

    n: the number of socks in the pile
    ar: the colors of each sock

For example, there are socks with colors . There is one pair of color and one of color . There are three odd socks left, one of each color. The number of pairs is . 

'''
def sockMerchant(n, ar):
  numPairs = 0
  sockSet = set()
  for x in range(0,n):
    if ar[x] in sockSet:
      numPairs +=1
      sockSet.remove(ar[x])
    else:
      sockSet.add(ar[x])
  return numPairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
