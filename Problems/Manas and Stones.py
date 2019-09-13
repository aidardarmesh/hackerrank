#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    sums = set()

    for i in range(n):
        sums.add(a*((n-1)-i) + b*i)

    return sorted(sums)

if __name__ == '__main__':
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        print(' '.join(map(str, result)))