#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

# lst = sorted(lst)
#     n = len(lst)
#     return min([abs(lst[i+k-1]-lst[i]) for i in range(n-k+1)])


def commonChild(s1, s2):
    # Write your code here
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for i in range(n + 1)]

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    return lcs[n - 1][m - 1]






if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)
    print(result)
