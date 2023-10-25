#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
        # Write your code here
        a=0
        c=0
        for i in range(len(path)):
                h=path[i]
                if h=='U':
                        k=a
                        a+=1
                elif h=='D':
                        k=a
                        a-=1
                if a==0 and k<0:
                        c+=1
        return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
