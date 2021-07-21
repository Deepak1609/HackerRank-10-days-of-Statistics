#!/bin/python3
import os
import math
import random
import re
import sys
# from statistics import mean
#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = (sum(arr)/n)
    s1=[]
    for i in range(n):
        s1+= [(arr[i] - mean) **2]
    print(round(math.sqrt(sum(s1)/n),1))    

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
