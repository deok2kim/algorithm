#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diverseDeputation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER w
#
from itertools import combinations


def diverseDeputation(m, w):
    # Write your code here
    return m * (w * (w - 1) // 2) + w * (m * (m - 1) // 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = int(input().strip())

    w = int(input().strip())

    result = diverseDeputation(m, w)

    fptr.write(str(result) + '\n')

    fptr.close()
