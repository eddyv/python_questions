#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

# if i is a multiple of both 3 and 5, print FizzBuzz
# if i is a multiple of 3 (but not 5), print Fizz
# if i is a multiple of 5 (but not 3), print Buzz
# if i is not a multiple of 3 or 5 print the value of i
# the function must print the appropriate response for each value i in the set
# {1, 2, ... n} in ascending order each on a separate line.
# 0 < n < 2 * 10^5
def fizzBuzz(n):
    for x in range(1, n + 1):
        output = ''
        if x % 3 == 0:
            output = output + 'Fizz'
        if x % 5 == 0:
            output = output + 'Buzz'
        if not output:
            output = x
        print(output)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
