#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    length = len(arr)
    qty_pos = 0
    qty_neg = 0
    qty_zero = 0

    for elem in arr:
        if elem > 0:
            qty_pos += 1
        elif elem < 0:
            qty_neg += 1
        else:
            qty_zero += 1
    print(f"{(qty_pos / length):.6f}")
    print(f"{(qty_neg / length):.6f}")
    print(f"{(qty_zero / length):.6f}")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
