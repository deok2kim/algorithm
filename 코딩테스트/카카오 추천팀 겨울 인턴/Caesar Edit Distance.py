#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'editDistance' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING source
#  2. STRING target
#

def editDistance(source, target):
    # Write your code here
    N = len(source) + 1
    def LCS(a, b):
        for i in range(1, N):
            for j in range(1, N):
                if b[i-1] == a[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

    # 문자 회전하기
    max_same_cnt = 0
    for i in range(ord('z') - ord('a') + 1):
        rotationSource = ''
        for s in source:
            move_idx = ord(s) + i
            if move_idx > ord('z'):
                move_idx -= ord('z') - ord('a') + 1
            rotationSource += chr(move_idx)
        dp = [[0] * N for _ in range(N)]
        cnt = LCS(rotationSource, target)
        max_same_cnt = max(max_same_cnt, cnt)
    return ( N - max_same_cnt - 1 ) * 2
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    source = input()

    target = input()

    result = editDistance(source, target)

    fptr.write(str(result) + '\n')

    fptr.close()
