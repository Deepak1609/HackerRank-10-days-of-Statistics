#!/bin/python3

import math
import os
import random
import re
import sys
# import numpy as np
# from scipy import stats
from statistics import median

# import numpy as np
# from scipy import stats
#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    arr.sort()
    t=int(len(arr)/2)
    if(len(arr)%2)==0:
        L=arr[:t]
        U=arr[t:]
    else:
        L=arr[:t]
        U=arr[t+1:]
    
    q1=int(median(L))
    q2=int(median(arr))
    q3=int(median(U))
    ar=[]
    ar.append(q1)
    ar.append(q2)
    ar.append(q3)
    return ar
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
