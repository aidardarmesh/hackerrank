#!/bin/python3

import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    ar_sum = 0

    for n in ar:
        ar_sum += n

    return ar_sum

if __name__ == '__main__':
    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    print(result)