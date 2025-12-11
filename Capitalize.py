#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = s.split(' ') # sẽ thường mất đi một dấu khoảng trắng
    print(words)
    for i in range(len(words)):
        words[i] = words[i].replace(words[i], words[i].capitalize())
    return ' '.join(words) # khôi phục dấu trắng còn thiếu

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()