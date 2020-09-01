#!/bin/python3

import math
import os
import random
import re
import sys

'''
return an integer, the maximum hourglass sum in the array.

hourglassSum has the following parameter(s):

    arr: an array of integers

'''
def hourglassSum(arr):
  sum = []
  for i in range (1,len(arr)-1):
    for j in range (1, len(arr)-1):
      sum.append(arr[i][j] + arr[i-1][j-1] + arr[i-1][j] + arr[i-1][j+1] + arr[i+1][j-1] + arr[i+1][j] + arr[i+1][j+1])
  return max(sum)
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
