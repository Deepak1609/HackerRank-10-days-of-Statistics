#!/bin/python3

import math
import os
import random
import re
import sys
import statistics as stat

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    s=[]
    for i in range(n):
        s += [values[i]] * freqs[i]
    N = sum(freqs)
    s.sort()
    if ((n%2 )!= 0):
        q1 = stat.median(s[:N//2])
        q3 = stat.median(s[N//2+1:])
    else:
        q1 = stat.median(s[:N//2])
        q3 = stat.median(s[N//2:])

    irdf = round(float(q3-q1), 1)
    print(irdf)
    


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
